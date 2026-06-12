#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import sqlite3
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = Path(
    os.environ.get(
        "VALUE_INVESTING_KB_PATH",
        SKILL_ROOT / "data" / "value_investing_kb.sqlite",
    )
)
SOURCE_PRIORITY_SQL = "CASE WHEN book = '价值分析框架' THEN 1 ELSE 0 END"


def build_match_query(query: str) -> str:
    parts = [part for part in query.split() if part]
    if not parts:
        return '""'
    if len(parts) == 1:
        return '"' + parts[0].replace('"', '""') + '"'
    return " AND ".join('"' + part.replace('"', '""') + '"' for part in parts)


def like_sql_for_terms(query: str) -> tuple[str, list[str]]:
    parts = [part for part in query.split() if part] or [query]
    conditions = " AND ".join("content LIKE ?" for _ in parts)
    return conditions, [f"%{part}%" for part in parts]


def search(query: str, limit: int, book: str | None) -> list[sqlite3.Row]:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"知识库不存在：{DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    sql = (
        "SELECT book, section, locator, "
        "snippet(chunks_fts, 3, '[', ']', ' ... ', 18) AS snippet, "
        "bm25(chunks_fts) AS score "
        "FROM chunks_fts WHERE chunks_fts MATCH ?"
    )
    params: list[object] = [build_match_query(query)]
    if book:
        sql += " AND book = ?"
        params.append(book)
    sql += f" ORDER BY {SOURCE_PRIORITY_SQL}, score LIMIT ?"
    params.append(limit)

    try:
        rows = conn.execute(sql, params).fetchall()
    except sqlite3.OperationalError:
        rows = []

    if not rows:
        like_conditions, like_values = like_sql_for_terms(query)
        like_sql = (
            "SELECT book, section, locator, substr(content, 1, 320) AS snippet, 0.0 AS score "
            f"FROM chunks_fts WHERE {like_conditions}"
        )
        like_params: list[object] = list(like_values)
        if book:
            like_sql += " AND book = ?"
            like_params.append(book)
        like_sql += f" ORDER BY {SOURCE_PRIORITY_SQL}, length(content) DESC LIMIT ?"
        like_params.append(limit)
        rows = conn.execute(like_sql, like_params).fetchall()

    conn.close()

    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the local value investing knowledge base.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Maximum results to show")
    parser.add_argument("--book", help="Optional exact book name filter")
    args = parser.parse_args()

    try:
        rows = search(args.query, args.limit, args.book)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not rows:
        print("未找到结果。")
        return 0

    for index, row in enumerate(rows, start=1):
        print(f"[{index}] {row['book']} | {row['section']} | {row['locator']}")
        print(row["snippet"])
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
