#!/usr/bin/env python3
"""校验 Claude Code 用户可升级的插件版本契约。"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
VERSION_PATTERN = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT_DIR, text=True, stderr=subprocess.DEVNULL
    ).strip()


def previous_release_tag(current_version: str) -> str | None:
    tags = git("tag", "--merged", "HEAD", "--sort=-version:refname").splitlines()
    current_tag = f"v{current_version}"
    return next((tag for tag in tags if tag != current_tag), None)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release",
        action="store_true",
        help="校验本次发布相对上一发布版本的升级契约",
    )
    args = parser.parse_args()

    version = (ROOT_DIR / "VERSION").read_text(encoding="utf-8").strip()
    marketplace_path = ROOT_DIR / ".claude-plugin" / "marketplace.json"
    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    errors = []

    if not VERSION_PATTERN.fullmatch(version):
        errors.append(f"VERSION 不符合 MAJOR.MINOR.PATCH：{version!r}")

    for plugin in marketplace.get("plugins", []):
        name = plugin.get("name", "<未命名>")
        plugin_version = plugin.get("version")
        if plugin_version != version:
            errors.append(f"插件 {name} 的更新版本为 {plugin_version!r}，应为 {version!r}")

    for manifest_path in ROOT_DIR.glob("**/.claude-plugin/plugin.json"):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_version = manifest.get("version")
        if manifest_version is not None and manifest_version != version:
            errors.append(
                f"{manifest_path.relative_to(ROOT_DIR)} 的 version 为 "
                f"{manifest_version!r}，会覆盖 marketplace 的插件版本"
            )

    if args.release:
        try:
            previous_tag = previous_release_tag(version)
        except subprocess.CalledProcessError:
            previous_tag = None
        if previous_tag:
            old_marketplace = json.loads(
                git("show", f"{previous_tag}:.claude-plugin/marketplace.json")
            )
            old_versions = {
                plugin["name"]: plugin.get("version")
                for plugin in old_marketplace.get("plugins", [])
            }
            for plugin in marketplace.get("plugins", []):
                name = plugin.get("name", "<未命名>")
                if old_versions.get(name) == plugin.get("version"):
                    errors.append(
                        f"插件 {name} 与上一发布 {previous_tag} 使用相同版本 "
                        f"{plugin.get('version')!r}，Claude Code 会跳过更新"
                    )

    if errors:
        print("插件升级契约校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        sys.exit(1)

    scope = "发布版本" if args.release else "当前工作区"
    print(f"插件升级契约校验通过：{scope} v{version}")


if __name__ == "__main__":
    main()
