# GEO Lab

**Generative Engine Optimization: agent skills, a knowledge base, and independent research into how
AI search decides what to cite.**

![Skills](https://img.shields.io/badge/agent%20skills-4-black)
![Knowledge](https://img.shields.io/badge/knowledge%20base-open%20to%20contributions-blue)
![Citations](https://img.shields.io/badge/every%20number-primary%20sourced-green)
![CI](https://img.shields.io/badge/rules-enforced%20in%20CI-brightgreen)
![License](https://img.shields.io/badge/license-MIT-black)

Three surfaces, one asset: **rank the page (SEO), be the answer (AEO), be the citation (GEO).**

---

## Why this exists

I went looking for a straight answer on generative engine optimization and mostly found content
marketing. The same handful of statistics circulate without provenance, most guides are published by
companies selling the remedy, and a large share of the advice is traditional SEO wearing a new
acronym.

So I read the primary sources instead: the paper that coined the term, the platform documentation,
and the industry studies that publish their sample sizes. **This repository is that research, made
executable, and then opened up.**

**The rule that holds the whole thing together: every number resolves to a source, and CI fails the
build if it does not.** That is the difference between this and another curated list.

## Three layers

| Layer | What it is | Who owns it |
|---|---|---|
| **[`knowledge/`](knowledge/)** | How each surface and platform actually behaves | **Open. Community-maintained** |
| **[`research/`](research/)** | What follows from the evidence, and what is arguable | One author's position, open to challenge |
| **[`skills/`](skills/)** | Executable agent skills built on both | Maintained, PRs welcome |

Knowledge flows upward. A finding lands in `knowledge/`, and if it changes what you should *do*, the
skill changes too.

## The skills

| Skill | What it does | Reach for it when |
|---|---|---|
| **`sl-search-surfaces`** | The hub. The model, the vocabulary lock, the priority order. Every other skill checks it first | You want the model, or you are starting anything else |
| **`sl-geo-audit`** | Scores a site across Foundations, Answer Engine and Generative Citation, then maps gaps to actions | "Why does the AI never mention us?" |
| **`sl-citation-content`** | Writes and rewrites paragraphs so an LLM lifts them verbatim | You rank but never get quoted |
| **`sl-entity-infrastructure`** | Entity graph, schema depth, AI crawler access, `llms.txt` | The machine cannot tell who you are |

## The knowledge base

| File | Covers |
|---|---|
| [`00-foundations/seo-vs-aeo-vs-geo.md`](knowledge/00-foundations/seo-vs-aeo-vs-geo.md) | The matrix. Where the surfaces overlap and where they genuinely diverge |
| [`01-platforms/ai-overviews.md`](knowledge/01-platforms/ai-overviews.md) | Google. The mid-rank citation window, structural anatomy, click impact |
| [`01-platforms/chatgpt-search.md`](knowledge/01-platforms/chatgpt-search.md) | Bing-indexed, Wikipedia-concentrated |
| [`01-platforms/perplexity.md`](knowledge/01-platforms/perplexity.md) | Live retrieval, freshness-dominant, community-weighted |
| [`02-signals/llms-txt.md`](knowledge/02-signals/llms-txt.md) | A worked example of evaluating a tactic before adopting it |
| [`03-measurement/mention-tracking.md`](knowledge/03-measurement/mention-tracking.md) | Citation share, the free method and the tooled one |

## Three findings worth arguing with

Each is stated as contestable, because each one is.

**1. Most of the acronyms are aliases.** SEO, AEO and GEO are real and measurably different. AIO,
LLMO, GAIO and SXO are marketing. [`research/the-alphabet-problem.md`](research/the-alphabet-problem.md)
argues the skeptic's case, *"it's all just SEO"*, at full strength before disagreeing with it.

**2. The skeptic is mostly right about substance and mostly wrong about operations.** The underlying
craft barely changed. The **measurement** changed completely, and that is the only thing that earns
the vocabulary.

**3. Keyword stuffing actively backfires in generative engines.** Not "helps less". Worse than doing
nothing, at −9% against baseline `[Aggarwal-2023]`. That is the sharpest divergence from traditional
SEO instinct, and the single most useful thing in the literature.

## Install

Claude Code, per project:

```bash
git clone https://github.com/omarmfouad25/geo-lab.git
mkdir -p .claude/skills
cp -R geo-lab/skills/* .claude/skills/
```

Or globally:

```bash
cp -R geo-lab/skills/* ~/.claude/skills/
```

Invoke by name (`/sl-geo-audit`) or describe the task and let the model match on the triggers. These
are plain `SKILL.md` files with YAML frontmatter, so they work in any runtime that reads that format.
No plugin manifest required. The `sl-` prefix avoids collisions with other skill collections.

## Contributing

**The knowledge base is open, and the bar is a source, not credentials.**

The single most valuable contribution is **a number here that is now wrong**. Everything marked
`volatile` decays fast. Open an issue with the current figure and its source; you do not need to
write the fix.

Also wanted: platform behaviour changes, **negative results** (a tactic that measurably did not
work), and the gaps listed in [`knowledge/README.md`](knowledge/README.md), which currently include
Claude and Gemini citation behaviour and non-English search.

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`knowledge/_TEMPLATE.md`](knowledge/_TEMPLATE.md).

Disagreeing with a conclusion is welcome. The priority order and the terminology lock are judgements
and are labelled as such.

## Freshness, which is this field's real problem

**Figures were last validated 2026-05-21.** In this subject that is old. Every file declares:

| `freshness` | Meaning | Re-validate |
|---|---|---|
| `stable` | Conceptual, unlikely to move | Annually |
| `drift-watch` | Sound today, mechanism may shift | Quarterly |
| `volatile` | Platform numbers that move fast | Before you quote them |

**Do not present a `volatile` figure to a client or an audience without re-checking it.** A project
arguing that the ground is moving has no business shipping stale numbers.

### The rules are enforced, not just stated

```bash
python3 validate.py
```

Standard library only, no dependencies. It fails on an unresolved citation key, a broken internal
link, a missing required section or frontmatter field, an invalid `freshness` value, or an em dash.
It runs in CI on every push and pull request.

**An unenforced convention is a promise. This one is a test.**

## What this deliberately is not

- **Not a ranking guarantee.** Nobody can sell you citation. The mechanisms are undocumented and
  change without notice.
- **Not vendor research.** Where a source is a vendor with an interest, it is labelled `⚠ Vendor`.
  Most research in this field is. Making that visible is the point.
- **Not a link list.** There are several good `awesome-geo` lists. This is not one.
- **Not an SEO course.** It assumes you know what a canonical tag is.

## License

MIT. Use it, fork it, ship it in your own collection.

Founded and maintained by [Omar Fouad](https://github.com/omarmfouad25). The research layer is mine;
the knowledge base belongs to whoever improves it.
