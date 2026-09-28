# Q-SYS Design Watchdog (Elevate AV)

Q-SYS plugin that tracks post-handoff design changes on a core: redeploy
detection with control-level diffs, live-edit detection, acknowledge-to-
changelog workflow, schematic banners, Reflect integration via Monitoring
Proxy, and a notify-plus-approved-install remote update channel.

This repo is the update distribution point: cores fetch `manifest.json` from
`main` and hotfix modules from tagged releases only. See
`hotfix_template.lua` for the hotfix module contract and `make_manifest.py`
for cutting releases.

Plugins: `design_watchdog.qplug` (main), `change_log.qplug` (companion viewer).
