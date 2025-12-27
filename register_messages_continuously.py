#!/usr/bin/env python3
import os
import json
from datetime import date, timedelta
import argparse

BASE_TEMPLATE = {
    "language": "ko",
    "source": "Medjugorje Message Archive",
    "visionary": "평화의 모후 성모 마리아",
    "message": "",
    "themes": [],
    "liturgical_links": [],
    "media": {
        "tts_duration_sec": 30,
        "voice": "sunkyung"
    }
}

def daterange(start: date, end: date):
    cur = start
    while cur <= end:
        yield cur
        cur += timedelta(days=1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", required=True)
    parser.add_argument("--start", required=True, help="YYYY-MM-DD")
    parser.add_argument("--end", required=True, help="YYYY-MM-DD")
    args = parser.parse_args()

    start = date.fromisoformat(args.start)
    end = date.fromisoformat(args.end)

    created = 0
    skipped = 0

    for d in daterange(start, end):
        year_dir = os.path.join(args.base_dir, str(d.year))
        os.makedirs(year_dir, exist_ok=True)

        fname = f"{d.isoformat()}.ko.json"
        fpath = os.path.join(year_dir, fname)

        if os.path.exists(fpath):
            skipped += 1
            continue

        data = BASE_TEMPLATE.copy()
        data["date"] = d.isoformat()
        data["message"] = f"{d.year}년 {d.month}월 {d.day}일 메주고리예 성모님 메시지 (정리 중)."
        data["themes"] = ["기도", "평화"]

        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        created += 1
        print(f"[CREATED] {fpath}")

    print(f"\n완료: 생성 {created} / 건너뜀 {skipped}")

if __name__ == "__main__":
    main()

