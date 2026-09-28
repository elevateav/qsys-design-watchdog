-- Design Watchdog hotfix 1.6.0-hf1 (pipeline verification)
-- Benign and idempotent: proves fetch -> sha256 verify -> install -> boot
-- reload works end-to-end. Logs locally and into the Reflect event log.
return function(ctx)
  ctx.log("hotfix 1.6.0-hf1 active - remote update pipeline verified end-to-end")
  ctx.proxyPushLog("Normal", "Design Watchdog: hotfix 1.6.0-hf1 active (update pipeline verified)")
end
