#!/usr/bin/env python3
"""celebrity-elysia — one-shot installer for AI-agent harnesses.

Detects which harnesses are installed on this machine and copies the skill
into each host's skills directory, so the skill is discovered automatically
(filesystem-discovery style). Works on Windows, macOS and Linux with only the
Python standard library.

Usage:
    python3 tools/install.py                 # auto-detect hosts, install to all found
    python3 tools/install.py --host claude-code,workbuddy   # install to specific hosts
    python3 tools/install.py --force         # overwrite existing installs
    python3 tools/install.py --dry-run       # show plan without writing

One-liner install (no clone needed):
    bash:    curl -fsSL https://raw.githubusercontent.com/chen2940/celebrity-elysia/main/install.sh | bash
    windows: irm https://raw.githubusercontent.com/chen2940/celebrity-elysia/main/install.ps1 | iex
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

SKILL_DIR_NAME = "celebrity-elysia"
SKILL_SOURCE = Path(__file__).resolve().parent.parent  # repo root (parent of tools/)

# hosts: id -> (display name, resolver returning candidate skills dirs)
HOSTS = {
    "claude-code": (
        "Claude Code",
        lambda home: [home / ".claude" / "skills"],
    ),
    "openclaw": (
        "OpenClaw",
        lambda home: [
            home / ".openclaw" / "skills",                  # observed layout
            home / ".openclaw" / "workspace" / "skills",    # docs layout
        ],
    ),
    "codex": (
        "Codex",
        lambda home: [home / ".codex" / "skills"],
    ),
    "hermes": (
        "Hermes",
        lambda home: [home / ".hermes" / "skills"],
    ),
    "dsh": (
        "DeepSeek Harness",
        lambda home: [resolve_dsh_skills_dir(home)],
    ),
    "workbuddy": (
        "WorkBuddy",
        lambda home: [home / ".workbuddy" / "skills"],
    ),
    "trae": (
        "TRAE",
        lambda home: [home / ".trae" / "skills"],
    ),
    "cursor": (
        "Cursor",
        lambda home: [home / ".cursor" / "skills"],
    ),
}

IGNORE_NAMES = shutil.ignore_patterns(
    ".git", ".workbuddy", "__pycache__", "*.pyc", ".DS_Store",
    "*.zip",
    "output",
)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def resolve_dsh_skills_dir(home: Path) -> Path:
    """DeepSeek Harness honors DSH_HOME when set."""
    dsh_home = os.environ.get("DSH_HOME")
    if dsh_home:
        return Path(dsh_home).expanduser() / "skills"
    return home / ".dsh" / "skills"


def candidates_for(host_id: str, home: Path) -> list[Path]:
    """Candidate skills directories for a host, in priority order."""
    _label, resolver = HOSTS[host_id]
    return [Path(p).expanduser() for p in resolver(home)]


def pick_skills_dir(host_id: str, home: Path) -> Path:
    """First existing candidate dir, else the first candidate (created on demand)."""
    for cand in candidates_for(host_id, home):
        if cand.exists():
            return cand
    return candidates_for(host_id, home)[0]


def detected_hosts(home: Path) -> list[str]:
    """Hosts whose skills directory already exists on this machine."""
    found: list[str] = []
    for host_id in HOSTS:
        if any(cand.exists() for cand in candidates_for(host_id, home)):
            found.append(host_id)
    return found


def install_to_host(
    host_id: str,
    skills_dir: Path,
    *,
    source: Path,
    force: bool,
    dry_run: bool,
) -> dict:
    """Install the skill into one host's skills directory."""
    label, _resolver = HOSTS[host_id]
    install_dir = skills_dir / SKILL_DIR_NAME
    skill_file = install_dir / "SKILL.md"

    # Guard: never copy a repo onto itself (e.g. running from ~/.dsh/skills/celebrity-elysia).
    try:
        if install_dir.resolve() == source.resolve():
            return {
                "host": host_id,
                "label": label,
                "status": "is-source",
                "install_dir": str(install_dir),
                "skill_file": str(skill_file),
            }
    except OSError:
        pass

    status = "skip"
    if not skills_dir.exists() and not dry_run:
        skills_dir.mkdir(parents=True, exist_ok=True)

    if install_dir.exists() and not force and not dry_run:
        status = "exists"
    elif dry_run:
        status = "would-install" if not (install_dir.exists() and not force) else "would-overwrite"
    else:
        if install_dir.exists():
            shutil.rmtree(install_dir)
        install_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, install_dir, ignore=IGNORE_NAMES)
        metadata = {
            "skill": SKILL_DIR_NAME,
            "host": host_id,
            "source": str(source),
            "installed_at": now_iso(),
            "installer": "tools/install.py",
            "version": "v7",
        }
        (install_dir / ".install-metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        status = "installed"

    return {
        "host": host_id,
        "label": label,
        "status": status,
        "install_dir": str(install_dir),
        "skill_file": str(skill_file),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Install celebrity-elysia skill into AI-agent harnesses",
    )
    parser.add_argument(
        "--host",
        default=None,
        help="Comma-separated host ids to install to "
             "(default: auto-detect installed hosts): " + ", ".join(HOSTS),
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing installs")
    parser.add_argument("--dry-run", action="store_true", help="Show plan without writing files")
    parser.add_argument("--source", default=str(SKILL_SOURCE), help="Skill repo root (default: this repo)")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not (source / "SKILL.md").exists():
        sys.exit(f"error: {source} is not a skill repo (no SKILL.md)")

    home = Path.home()

    if args.host:
        requested = [h.strip() for h in args.host.split(",") if h.strip()]
        unknown = [h for h in requested if h not in HOSTS]
        if unknown:
            sys.exit(f"error: unknown host(s): {', '.join(unknown)}")
        targets = requested
    else:
        targets = detected_hosts(home)
        if not targets:
            print("No supported harness detected on this machine.")
            print("Install manually by cloning this repo into a host skills dir, e.g.:")
            print(f"  git clone https://github.com/chen2940/celebrity-elysia.git "
                  f"\"{home / '.claude' / 'skills' / SKILL_DIR_NAME}\"")
            sys.exit(1)

    results = []
    for host_id in targets:
        skills_dir = pick_skills_dir(host_id, home)
        results.append(install_to_host(
            host_id,
            skills_dir,
            source=source,
            force=args.force,
            dry_run=args.dry_run,
        ))

    print(f"celebrity-elysia  ({'dry-run plan' if args.dry_run else 'install result'})")
    for r in results:
        print(f"  [{r['status']:>15}] {r['label']:<16} -> {r['install_dir']}")
    print("\nRestart (or reload) the harness, then invoke the skill as:")
    print("  /celebrity-elysia   (slash-command hosts: Claude Code / OpenClaw / Hermes / DSH)")
    print("  celebrity-elysia    (Codex / WorkBuddy / TRAE by skill name)")


if __name__ == "__main__":
    main()
