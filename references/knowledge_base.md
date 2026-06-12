# Knowledge Base Policy and Retrieval Notes

This public repository ships the skill workflow, checklists, frameworks, and retrieval helper script. It does not ship the private local knowledge-base database.

## Public Files Included

- `SKILL.md`
- `references/investment_principles.md`
- `references/investment_checklist.md`
- `references/industry_supply_chain_bottleneck_framework.md`
- `scripts/query_kb.py`

## Private Files Excluded

The following files should stay private unless you have explicit rights to publish them:

- Original books such as `.epub`, `.pdf`, `.mobi`, `.azw3`
- OCR output
- Raw excerpts
- `chunks.jsonl`
- Generated SQLite databases
- SQLite WAL/SHM files
- Any dataset containing long copyrighted passages

## Local Retrieval

By default, the retrieval helper looks for:

```text
data/value_investing_kb.sqlite
```

You can override the database path:

```bash
VALUE_INVESTING_KB_PATH=/path/to/value_investing_kb.sqlite python3 scripts/query_kb.py "能力圈"
```

If no database exists, the skill still works as a structured analysis workflow, but book-grounded retrieval will be unavailable.

## Evidence Discipline

For current company analysis, always verify facts with primary sources:

- Annual reports
- Quarterly reports
- Exchange filings
- Company announcements
- Investor presentations
- Earnings call transcripts
- Regulatory disclosures

The local KB should support reasoning discipline. It should not replace current facts.
