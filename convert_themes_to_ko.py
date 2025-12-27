#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
convert_themes_to_ko.py

- 모든 메시지 JSON 파일을 순회
- themes 배열에 들어 있는 영어 값을 한국어로 변환
- 이미 한국어인 값은 그대로 유지
"""

import json
import argparse
from pathlib import Path

THEME_MAP = {
    "sign": "징표",
    "beginning": "시작",
    "prayer": "기도",
    "peace": "평화",
    "conversion": "회개",
    "faith": "믿음",
    "hope": "희망",
    "suffering": "고통",
    "church": "교회",
    "fasting": "단식",
    "confession": "고백성사"
}


def convert_themes(themes):
    new_themes = []
    for t in themes:
        if t in THEME_MAP:
            new_themes.append(THEME_MAP[t])
        else:
            new_themes.append(t)  # 이미 한국어이거나 미정의 값
    return new_themes


def process_file(path: Path, dry_run=False):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if "themes" not in data or not isinstance(data["themes"], list):
        return False

    old = data["themes"]
    new = convert_themes(old)

    if old == new:
        return False

    data["themes"] = new

    if not dry_run:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-dir",
        required=True,
        help="messages 폴더 경로 (예: data/messages)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="실제 파일 수정 없이 변경 여부만 출력"
    )

    args = parser.parse_args()
    base_dir = Path(args.base_dir)

    files = list(base_dir.glob("**/*.json"))
    changed = 0

    for file in files:
        if process_file(file, dry_run=args.dry_run):
            print(f"[UPDATED] {file}")
            changed += 1

    print(f"\n완료: 변경된 파일 {changed}개 / 전체 {len(files)}개")


if __name__ == "__main__":
    main()

