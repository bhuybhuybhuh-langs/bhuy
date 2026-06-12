# Data Directory

Place your private local knowledge-base database here if you have one:

```text
data/value_investing_kb.sqlite
```

This repository does not include copyrighted books, OCR files, raw excerpts, generated chunks, or SQLite databases. Keep those files private unless you have permission to publish them.

You can also use an external database path:

```bash
VALUE_INVESTING_KB_PATH=/path/to/value_investing_kb.sqlite python3 scripts/query_kb.py "能力圈"
```
