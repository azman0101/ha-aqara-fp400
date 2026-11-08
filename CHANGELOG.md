# Changelog

Releases of the azman0101 fork. Earlier versions are
[RAR/ha-aqara-fp400](https://github.com/RAR/ha-aqara-fp400) releases.

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
