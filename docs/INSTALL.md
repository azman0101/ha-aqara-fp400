# Installing and switching providers

## Switching HACS providers safely

[RAR/ha-aqara-fp400](https://github.com/RAR/ha-aqara-fp400) and this fork both
provide the same `aqara_fp400` domain. Their downloads go into the same
`custom_components/aqara_fp400` directory, so installing or updating either one
replaces the other's code. Home Assistant keeps running the code it loaded at
startup: entities that still work after a HACS download do not tell you which
code the next restart will load.

Keep only one HACS repository active for this domain. Before changing:

1. Back up the Home Assistant configuration, including `custom_components/aqara_fp400`.
2. Add the repository you want as a custom repository in HACS and download it.
   If you remove the other repository's download in HACS, do it **before**
   downloading the new one: removing a download deletes the shared directory.
3. Restart Home Assistant. A reload of the integration is not enough to load new
   Python code.

Do **not** delete the **Aqara FP400 (Matter)** integration entry or its devices
while switching:

- Entity and device IDs come from the Matter node ID, so they stay the same as
  long as the entry is kept, with their history and dashboard references.
- Zone names are stored in this entry (the device has no name field). Deleting
  the entry loses them. Zones and regions themselves are stored on the device
  and are not affected.
- The live tracking switch restores its last state after the restart.

The integration registers the zone card itself, at
`/aqara_fp400/aqara-fp400-zone-card.js?v=<version>`. The version in that URL
changes when the installed version changes, which makes browsers load the new
card. If both repositories ever ship different code under the same version
number, force-reload the dashboard (or clear the browser cache) after switching.

After the restart, check the `version` in
`custom_components/aqara_fp400/manifest.json` (or the `?v=` value of the card
resource under Settings → Dashboards → Resources), then check that the zone card,
the zone names and the live tracking switch behave as expected.

A merge on GitHub does not update an installed copy: HACS offers a new version
only once a release is published.
