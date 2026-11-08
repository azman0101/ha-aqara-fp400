"""Diagnostics: what the integration sees on the Matter server, to debug a silent setup."""

from __future__ import annotations

from typing import Any

from homeassistant.components.matter.helpers import get_matter
from homeassistant.core import HomeAssistant

from . import FP400ConfigEntry, is_fp400
from .const import CONF_ZONE_NAMES, PRODUCT_ID_FP400, VENDOR_CLUSTERS, VENDOR_ID


def _hex(value: Any) -> str | None:
    return f"0x{value:04X}" if isinstance(value, int) and not isinstance(value, bool) else None


async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: FP400ConfigEntry) -> dict[str, Any]:
    """Matter nodes, FP400 state and vendor-cluster attributes. No serial numbers or zone names."""
    try:
        client = get_matter(hass).matter_client
    except Exception as err:  # the Matter integration is not loaded
        return {"error": f"Matter integration unavailable: {err or type(err).__name__}"}

    info = client.server_info
    nodes = []
    for node in client.get_nodes():
        attrs = node.node_data.attributes
        nodes.append(
            {
                "node_id": node.node_id,
                "available": node.available,
                "vendor_id": _hex(attrs.get("0/40/2")),
                "product_id": _hex(attrs.get("0/40/4")),
                "product_name": attrs.get("0/40/3"),
                "is_fp400": is_fp400(node),
            }
        )

    sensors = []
    for fp in entry.runtime_data.nodes.values():
        attrs = fp.node.node_data.attributes
        vendor_attributes = {path: value for path, value in attrs.items() if int(path.split("/")[1]) in VENDOR_CLUSTERS}
        sensors.append(
            {
                "node_id": fp.node_id,
                "available": fp.node.available,
                "fabric_vendor_id": _hex(fp.fabric_vendor_id),
                "zones": len(fp.zones),
                "zones_pending": fp.zones_pending,
                "zones_error": fp.zones_error,
                "zones_read_failing": fp.zones_read_failing,
                "regions": {key: len(cells) for key, cells in fp.regions.items()},
                "regions_error": dict(fp.regions_error),
                "live_tracking": fp.live_tracking,
                "location_stream_failing": fp._renew_failing,
                "targets": len(fp.targets),
                "human_count": fp.human_count,
                "activity_state": fp.activity_state,
                "last_motion": fp.last_motion,
                "vendor_cluster_attributes": vendor_attributes,
            }
        )

    return {
        "expected_device": {"vendor_id": _hex(VENDOR_ID), "product_id": _hex(PRODUCT_ID_FP400)},
        "matter_server": {
            "sdk_version": getattr(info, "sdk_version", None),
            "schema_version": getattr(info, "schema_version", None),
        },
        "matter_nodes": nodes,
        "fp400": sensors,
        "zone_names_stored_for": len(entry.data.get(CONF_ZONE_NAMES, {})),
    }
