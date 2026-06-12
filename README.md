# Value Investing KB Skill - AI Value Investing Research Framework for Codex

`value-investing-kb` is an AI-assisted value investing skill for Codex. It is designed for stock research, company analysis, valuation, financial statement review, industry chain analysis, moat analysis, management evaluation, capital allocation review, free cash flow modeling, margin of safety judgment, and long-term investment thesis building.

This repository provides a reusable investment research workflow that combines value investing principles, Feynman-style explanation, Graham downside protection, Fisher growth quality, Munger/Duan Yongping/Li Lu business-quality thinking, and supply-chain bottleneck analysis. It helps turn vague questions like "Is this stock worth buying?" into a structured process with facts, inferences, conclusions, valuation assumptions, risks, and falsification conditions.

The public repository contains the Codex skill instructions, analytical checklists, reusable frameworks, version notes, and a local retrieval script. It intentionally does **not** include copyrighted books, OCR exports, raw excerpts, generated chunks, or SQLite databases.

## SEO Keywords

Value investing, AI investing skill, Codex skill, stock analysis, company analysis, equity research, valuation framework, discounted cash flow, DCF, free cash flow, owner earnings, margin of safety, moat analysis, management quality, capital allocation, Graham investing, Fisher growth investing, Charlie Munger mental models, Duan Yongping investing, Li Lu value investing, supply chain analysis, industry chain analysis, bottleneck company analysis, financial statement analysis, investment checklist, long-term investing, fundamental analysis, China stocks, US stocks, Hong Kong stocks.

中文关键词：价值投资、股票分析、公司分析、企业分析、估值框架、DCF 估值、自由现金流、安全边际、护城河、管理层、资本配置、财报分析、产业链分析、供应链瓶颈、格雷厄姆、费雪、芒格、段永平、李录、长期投资、基本面分析、投资清单、Codex 技能、AI 投资研究。

## What This Skill Does

- Builds investment analysis around first principles instead of ad-hoc market opinions.
- Forces a Feynman-style explanation before reaching a buy, hold, avoid, or continue-tracking conclusion.
- Separates `facts`, `inferences`, and `conclusions` so the reasoning chain is auditable.
- Combines Graham downside protection, Fisher growth-quality checks, Munger/Duan Yongping/Li Lu style business-quality thinking, and supply-chain bottleneck analysis.
- Requires valuation to bridge future free cash flow into enterprise value, equity value, intrinsic value per share, and margin of safety.
- Adds explicit failure conditions so the investment thesis can be falsified later.
- Helps prevent common errors such as confusing market heat with business quality, confusing revenue growth with free cash flow, and treating a popular industry theme as a real moat.

## Best Use Cases

- Analyze whether a stock is worth researching, buying, holding, or avoiding.
- Review a company using value investing principles and long-term business quality.
- Build a structured investment memo.
- Compare valuation assumptions with current market capitalization.
- Analyze free cash flow quality and owner earnings.
- Judge whether a company has a durable moat.
- Evaluate management integrity, incentive alignment, and capital allocation.
- Map a company into its upstream, midstream, downstream, or infrastructure position.
- Identify whether a company is a real supply-chain bottleneck or only riding a hot theme.
- Build a falsifiable investment thesis with clear mistake signals.

## Core Analysis Modules

1. **Feynman Gate** - explain the business, moat, culture, downside risk, and margin of safety in plain language.
2. **Graham Downside Filter** - investment vs speculation, balance-sheet safety, earnings stability, Mr. Market, and margin of safety.
3. **Fisher Growth Quality** - long runway, R&D productivity, sales organization, management depth, profit-margin resilience, and scuttlebutt evidence.
4. **Business Essence** - customer value proposition, revenue engine, moat type, moat trend, and industry endgame.
5. **Supply-Chain Bottleneck Framework** - upstream/downstream position, customer mapping, bottleneck type, value capture, and market perception gap.
6. **Culture and Management** - values, incentives, honesty, long-termism, disclosure quality, and capital allocation discipline.
7. **Financial Reality** - revenue, margins, ROE/ROIC, operating cash flow, free cash flow, leverage, dilution, and accounting quality.
8. **Valuation Bridge** - future FCF to enterprise value, equity value, intrinsic value per share, and margin of safety.
9. **Inversion and Risk** - why the thesis could fail, what would prove it wrong, and what opportunity cost exists.
10. **Final Output Contract** - facts, inferences, conclusions, action view, and falsification conditions.

## Repository Layout

```text
.
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── VERSION
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── investment_principles.md
│   ├── investment_checklist.md
│   └── industry_supply_chain_bottleneck_framework.md
├── scripts/
│   └── query_kb.py
└── data/
    └── README.md
```

## Installation

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/bhuybhuybhuh-langs/bhuy.git ~/.codex/skills/value-investing-kb
```

Then restart Codex or reload your skills.

## Optional Local Knowledge Base

The script `scripts/query_kb.py` expects a local SQLite FTS database at:

```text
data/value_investing_kb.sqlite
```

You can also point it to another local database:

```bash
VALUE_INVESTING_KB_PATH=/path/to/value_investing_kb.sqlite \
python3 scripts/query_kb.py "margin of safety"
```

The database is not included in this public repo. Keep copyrighted source books, OCR output, and raw excerpts private unless you have the rights to publish them.

## Usage Examples

```bash
python3 scripts/query_kb.py "能力圈"
python3 scripts/query_kb.py "安全边际"
python3 scripts/query_kb.py "自由现金流 护城河"
python3 scripts/query_kb.py "产业链 瓶颈"
```

For an analysis request, invoke the skill and follow the fixed workflow in `SKILL.md`:

1. Read `references/investment_principles.md`.
2. Read `references/investment_checklist.md`.
3. Use `scripts/query_kb.py` for local evidence when a database is available.
4. Separate `事实 / 推断 / 结论`.
5. Include `判错条件`.

## Version Features

Current version: `v0.1.0`

- **Investment theory layer**: first-principles value investing framework with plain-language concept explanations.
- **Execution checklist**: fixed step-by-step process for company, stock, industry, and valuation research.
- **Valuation module**: DCF/free-cash-flow bridge from future cash flow to intrinsic value and margin of safety.
- **Moat and culture module**: evaluates durable competitive advantage, management incentives, capital allocation, and company values.
- **Supply-chain bottleneck module**: maps upstream/midstream/downstream position and judges whether bottleneck strength can convert into revenue, margin, free cash flow, and valuation upside.
- **Evidence retrieval script**: local SQLite FTS query helper for private knowledge-base search.
- **Public-safe repo layout**: excludes copyrighted raw books, OCR files, chunks, and generated databases.

## Suggested GitHub Repository Description

AI value investing research skill for Codex: stock analysis, DCF valuation, moat, free cash flow, management quality, capital allocation, margin of safety, and supply-chain bottleneck framework.

## Suggested GitHub Topics

```text
value-investing
ai-investing
codex-skill
stock-analysis
equity-research
valuation
dcf
free-cash-flow
margin-of-safety
moat
financial-analysis
supply-chain-analysis
capital-allocation
```

## Safety Notes

This skill is for research workflow and decision discipline. It does not provide financial advice. Always verify current facts with primary sources such as annual reports, filings, exchange disclosures, investor presentations, and official company announcements.
