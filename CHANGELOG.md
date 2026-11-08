# Changelog

Releases of the azman0101 fork. Earlier versions are
[RAR/ha-aqara-fp400](https://github.com/RAR/ha-aqara-fp400) releases.

## 1.3.5

- The zone card now draws corner-mounted sensors in their corner. It looked for
  `select.<name>_radar_side_install`, but Home Assistant names that entity
  `select.<name>_radar_side_install_position` (from "Side install position"), so the
  sensor was always drawn as wall-mounted unless `mount:` was set in the card. The old
  name is still tried as a fallback. README entity names corrected.
- After updating, reload the dashboard: the new version number makes browsers fetch
  the new card.

## 1.3.4

- The integration has its own icon, shipped in `custom_components/aqara_fp400/brand/`
  (`icon.png` 256×256 and `icon@2x.png` 512×512). Home Assistant 2026.10 and later
  serve brand images from a custom integration's `brand` folder, so the icon shows
  on the integration and device pages without a change to the `home-assistant/brands`
  repository. Logos and dark variants fall back to the same icon.

## 1.3.3

The integration was nearly silent when something was wrong. It now says why:

- **Repairs:** a warning appears under Settings → System → Repairs when the FP400 is
  controlled through a Matter fabric with vendor ID 0x134B (the Home Assistant
  Matter Server add-on's default). The FP400 refuses its zones, regions, settings
  and position stream from that fabric. The warning explains that every device must
  be commissioned again after changing the vendor ID; restarting the server is not
  enough.
- **Diagnostics:** the integration can now download diagnostics: Matter nodes with
  their vendor and product IDs, whether each is recognised as an FP400, the fabric
  vendor ID, the sensor's state and its vendor-cluster attributes. No serial numbers
  or zone names.
- **Warnings without debug logging:** when no FP400 is found on the Matter server
  (listing the nodes it does see), and the first time reading the zones from the
  device fails (naming the fabric vendor ID). A later success is logged once.
- README: new Troubleshooting section.

## 1.3.2

Fixes found while reviewing the integration for this fork. Not sent upstream yet:
they will be proposed once validated on a live installation.

- A `MotionDetected` code the integration does not know (for example one added by
  a firmware update) no longer breaks the last motion sensors. They show
  `unrecognized` instead, and the raw code is logged once as a warning. Before,
  the value fell outside the sensors' enum options, so Home Assistant refused to
  write the state and the entities notified after it in the same update were
  skipped too.
- The `"rows,cols"` cell format of `set_zones` and `set_region` now rejects
  reversed ranges (`"10-5,0-15"`), out-of-grid ranges and malformed specs
  (missing comma, `"1-"`) with a clear error. Before, a reversed range silently
  gave no cells, and for the monitoring region no cells means the whole grid.

## 1.3.1

Same code as upstream 1.3.0. Fork maintenance only:

- `manifest.json` points `codeowners`, `documentation` and `issue_tracker` to the
  azman0101 fork.
- `NOTICE.md` credits Andrew Rankin (@RAR) as the original author and states the
  fork's maintenance. A copy of `LICENSE` and `NOTICE.md` is in
  `custom_components/aqara_fp400`, so the folder HACS downloads carries them.
- The README installs from the fork and links to the new `docs/INSTALL.md`, which
  explains how to switch between RAR's repository and this fork in HACS without
  losing entities, zone names or history.

After updating, restart Home Assistant. Publish a `v1.3.1` GitHub release so HACS
offers the update.
