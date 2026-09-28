-- Design Watchdog hotfix template.
-- A hotfix is a runtime-only patch: it can change behavior, add timers,
-- adjust drivers - it CANNOT add controls, pins, pages, or properties
-- (those are design-time; ship a new .qplug through Designer for that).
--
-- Contract: the file must `return function(ctx) ... end`. The Watchdog
-- fetches it, verifies sha256 against the manifest, runs it immediately on
-- install, and re-runs it on every script start while ctx.version matches
-- the manifest "base". A hotfix should therefore be idempotent.
--
-- ctx fields:
--   ctx.version       running plugin version (e.g. "1.6.0")
--   ctx.hotfix        previously active hotfix version ("" if none)
--   ctx.log(msg)      write to the Watchdog activity log
--   ctx.dbg(...)      debug-gated print
--   ctx.alert(subject, body)        SMTP2GO email (if configured)
--   ctx.proxyPushLog(sev, text)     Reflect event-log entry via proxy
--   ctx.Controls / ctx.Component / ctx.Timer / ctx.json
--
-- Keep hotfixes small and single-purpose; the changelog records the install.

return function(ctx)
  ctx.log("hotfix template active (running " .. ctx.version .. ")")

  -- Example: watch one extra thing the shipped version missed.
  -- local ok, comp = pcall(ctx.Component.New, "Some Component")
  -- if ok and comp then
  --   comp["some control"].EventHandler = function(c)
  --     ctx.log("hotfix-watched control changed: " .. tostring(c.String))
  --   end
  -- end
end
