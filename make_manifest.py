#!/usr/bin/env python3
"""
make_manifest.py - cut a Design Watchdog release manifest.

Usage:
  python3 make_manifest.py --latest 1.6.0 \
      [--hotfix hotfix.lua --hotfix-version 1.6.0-hf1 --base 1.6.0 \
       --hotfix-url https://raw.githubusercontent.com/elevateav/qsys-design-watchdog/v1.6.0-hf1/hotfix.lua \
       --hotfix-notes "fixes X"] \
      [--notes "release notes"] [-o manifest.json]

Writes manifest.json for the repo root. The plugin fetches it from Update URL
(raw.githubusercontent.com), compares "latest" against its own version
(notify-only), and offers "hotfix" for install when base matches exactly.

Release discipline (this is remote code execution on customer cores - treat
it that way):
  * Point hotfix-url at a TAG, never a branch head.
  * Commit hotfix.lua and the manifest in the same tagged release.
  * The sha256 here must be of the exact bytes GitHub will serve.
"""
import argparse
import hashlib
import json
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--latest", required=True, help="newest full .qplug version")
    ap.add_argument("--notes", default="")
    ap.add_argument("--hotfix", help="path to hotfix .lua file")
    ap.add_argument("--hotfix-version", help="e.g. 1.6.0-hf1")
    ap.add_argument("--base", help="exact plugin version the hotfix targets")
    ap.add_argument("--hotfix-url", help="raw URL (tagged!) the plugin will fetch")
    ap.add_argument("--hotfix-notes", default="")
    ap.add_argument("-o", "--out", default="manifest.json")
    args = ap.parse_args()

    manifest = {"plugin": "design_watchdog", "latest": args.latest}
    if args.notes:
        manifest["notes"] = args.notes

    if args.hotfix:
        if not (args.hotfix_version and args.base and args.hotfix_url):
            sys.exit("--hotfix requires --hotfix-version, --base, and --hotfix-url")
        data = open(args.hotfix, "rb").read()
        if b"\r\n" in data:
            print("WARNING: hotfix has CRLF line endings; ensure the served "
                  "bytes match (git autocrlf will silently change the hash)",
                  file=sys.stderr)
        manifest["hotfix"] = {
            "base": args.base,
            "version": args.hotfix_version,
            "url": args.hotfix_url,
            "sha256": hashlib.sha256(data).hexdigest(),
        }
        if args.hotfix_notes:
            manifest["hotfix"]["notes"] = args.hotfix_notes

    with open(args.out, "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    print(f"wrote {args.out}:")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
