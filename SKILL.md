---
name: value-investing-kb
description: Use when the user asks about stocks, companies, valuation, financial statements, industry analysis, moat, management quality, capital allocation, growth-stock quality, margin of safety, or investing decisions that should be grounded in the local value-investing knowledge base built from Duan Yongping Q&A, Poor Charlie's Almanack, Li Lu's modernization/value-investing framework, Benjamin Graham's defensive value framework, Philip Fisher's growth-stock/scuttlebutt framework, and the user's value-analysis framework.
---

# Value Investing KB

Use this skill for finance/equity tasks that must be anchored to a structured value-investing workflow and, when available, a private local KB.

## Theory layer

- `references/investment_principles.md`
  Read first. This is the first-principles and Feynman-style concept layer distilled from the local book sources.
- `references/investment_checklist.md`
  Read second. This is the execution checklist and output contract.
- `references/knowledge_base.md`
  Read when you need public repo data policy and local retrieval details.
- `references/industry_supply_chain_bottleneck_framework.md`
  Read when the request involves industry stock selection, upstream/downstream mapping, AI supply chain, bottleneck companies, semiconductor, power, data center, optics, materials, equipment, or when the user asks where a stock sits in its industry chain.
- `scripts/query_kb.py`
  Use for concept evidence and source fragments.

## Required workflow

1. Read `investment_principles.md` to set the conceptual frame.
2. Pass the Feynman gate: if you cannot explain a concept in plain language, the conclusion is not ready.
3. Read `investment_checklist.md` and structure the analysis in that order.
4. When a private local KB database is available, run:
   `python3 scripts/query_kb.py "<query>"`
   to retrieve local evidence. You can also set `VALUE_INVESTING_KB_PATH=/path/to/value_investing_kb.sqlite`.
5. Treat the local KB as a private evidence layer when available. Do not publish copyrighted source books, OCR output, raw excerpts, chunks, or generated databases unless you have permission.
6. Output must separate `事实` / `推断` / `结论`, and include `判错条件`.
7. For any "is it worth buying / is it cheap" analysis, combine:
   - Graham: investment vs speculation, margin of safety, Mr. Market, balance-sheet and downside protection.
   - Fisher: 15-point growth quality, scuttlebutt evidence, management integrity, R&D/sales organization, long runway, and sell discipline.
   - Munger/Duan/Li Lu: moat, culture, incentives, ability circle, free cash flow, opportunity cost, inversion, and tacit knowledge.
8. For valuation, always include the Buffett-style cash-flow bridge:
   - forecast future FCF or owner earnings;
   - discount it into enterprise value;
   - add cash and subtract debt to get equity value / fair market cap;
   - divide by diluted shares to get intrinsic value per share;
   - compare with current market cap and price to state margin of safety;
   - reverse-engineer what growth and FCF margin the current market cap already implies.
9. For industry stock selection or company analysis, always include the supply-chain bottleneck module:
   - identify upstream/midstream/downstream/infrastructure position;
   - map direct customers and final demand driver;
   - judge whether the company is a real bottleneck, an important participant, or merely riding the theme;
   - score bottleneck strength using substitutability, capacity elasticity, qualification barriers, supply concentration, order visibility, and value capture;
   - explain whether the bottleneck can convert into revenue, margin, FCF, and valuation upside.

## Query tips

- Start with compact terms: `能力圈`, `护城河`, `现金流`, `自由现金流`, `贴现现金流`, `安全边际`, `资本配置`, `反过来想`.
- Use Graham/Fisher terms when needed: `投资 投机`, `市场波动`, `价格波动`, `防御型 投资者`, `15要点`, `闲聊`, `利润率`, `研究 销售`.
- For narrower retrieval, use `--book`:
  - `--book "大道段永平投资问答录"`
  - `--book "穷查理宝典"`
  - `--book "聪明的投资者"`
  - `--book "怎样选择成长股"`
  - `--book "费雪论成长股获利"`

## Coupling rule

If the request also involves media/user sentiment or cross-platform discussion, invoke a separate media-sentiment workflow before final output.
