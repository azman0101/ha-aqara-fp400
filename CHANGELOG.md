# Changelog

Releases of the azman0101 fork. Earlier versions are
[RAR/ha-aqara-fp400](https://github.com/RAR/ha-aqara-fp400) releases.

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
