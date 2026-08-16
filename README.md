# Search Surfaces

**Agent skills for getting cited by AI search, grounded in primary research rather than vendor blog posts.**

![Skills](https://img.shields.io/badge/skills-4-black)
![Format](https://img.shields.io/badge/format-SKILL.md-blue)
![Citations](https://img.shields.io/badge/every%20number-primary%20sourced-green)
![License](https://img.shields.io/badge/license-MIT-black)

Four Claude Code skills that treat SEO, AEO and GEO as **three surfaces of one asset** instead of
three disciplines: rank the page, be the answer, be the citation.

---

## Why this exists

I went looking for a straight answer on generative engine optimization and mostly found content
marketing. The same handful of statistics circulate without provenance, most "GEO guides" are
written by companies selling GEO tools, and a large share of the advice is traditional SEO wearing
a new acronym.

So I read the primary sources instead: the Aggarwal et al. paper that coined the term, the platform
documentation, and the industry studies that publish their sample sizes. This repository is the
result, packaged so an agent can execute it.

**The three positions this research landed on**, each of which is contestable and each of which the
skills state openly:

1. **Most of the acronyms are aliases.** SEO, AEO and GEO are real and measurably different. AIO,
   LLMO, GAIO and SXO are marketing. See [`research/the-alphabet-problem.md`](research/the-alphabet-problem.md),
   which argues the skeptic's case (*"it's all just SEO"*) before disagreeing with it.
2. **The skeptic is mostly right about substance and mostly wrong about operations.** The underlying
   craft barely changed. The **measurement** changed completely, and that is why the vocabulary
   earns its keep.
3. **Keyword stuffing actively backfires in generative engines.** Not "works less well". Worse than
   doing nothing, at −9% visibility against baseline `[Aggarwal-2023]`. This is the single biggest
   divergence from traditional SEO practice.

## The skills

| Skill | What it does | Start here when |
|---|---|---|
| **`sl-search-surfaces`** | The hub. Loads the three-surface model, the vocabulary lock and the priority order. Every other skill checks it first. | You want the model, or you are about to run any of the others |
| **`sl-geo-audit`** | Scores a site across Foundations, Answer Engine and Generative Citation, then maps gaps to actions | "Why does the AI never mention us?" |
| **`sl-citation-content`** | Writes and rewrites paragraphs so an LLM will lift them verbatim | You have content that ranks but never gets quoted |
| **`sl-entity-infrastructure`** | Entity graph, schema depth, AI crawler access, `llms.txt` | The machine cannot tell who you are |

They compose. The audit tells you which of the other two you need.

## Install

Claude Code, per project:

```bash
git clone https://github.com/omarmfouad25/search-surfaces.git
mkdir -p .claude/skills
cp -R search-surfaces/skills/* .claude/skills/
```

Or globally, for every project:

```bash
cp -R search-surfaces/skills/* ~/.claude/skills/
```

Then invoke by name (`/sl-geo-audit`) or just describe the task and let the model match on the
skill's triggers. Skills are plain `SKILL.md` files with YAML frontmatter, so they also work in any
agent runtime that reads that format. Nothing here depends on a plugin manifest.

The `sl-` prefix exists to prevent collisions with the several other marketing-skill collections you
may already have loaded.

## The priority order, which is the most contested thing here

```
SEO first.  GEO next.  AEO last.
```

Because roughly half of AI citations still originate from pages already ranking in the top ten, a
site that cannot rank cannot be cited. GEO outranks AEO because the answer box is a subset of a
shrinking classic SERP while citation share is the surface actually growing.

**This is a judgement call, not a finding.** A reader who weights the zero-click numbers more
heavily than I do would reasonably put AEO second. The skills state the reasoning so you can
override it, and `sl-geo-audit` ships a weight profile for exactly that.

## Freshness, which is this field's real problem

**Every quantitative claim carries a citation key** resolving to
[`references.md`](references.md). If a number has no key, it is flagged inline as inference.

**Figures were last validated 2026-05-21.** In this subject that is old. AI Overview trigger rates,
click-loss percentages and platform citation shares all move quarterly, and several of the headline
numbers in circulation have already doubled once. Each skill declares a `freshness` field:

| Value | Meaning | Re-validate |
|---|---|---|
| `stable` | Conceptual, unlikely to move | Annually |
| `drift-watch` | Sound today, mechanism may shift | Quarterly |
| `volatile` | Platform-specific numbers that move fast | Before you quote them |

**Do not present a `volatile` figure to a client or an audience without re-checking it first.** A
document arguing that the ground is moving has no business shipping stale numbers, which is a
mistake I would rather name than repeat.

### The rules are enforced, not just stated

```bash
python3 validate.py
```

Standard library only, no dependencies. It fails the build if a citation key does not resolve to
`references.md`, an internal link is broken, a skill is missing a required section or frontmatter
field, `freshness` holds an undefined value, or an em dash appears anywhere. It runs in CI on every
push and pull request.

An unenforced convention is a promise. This one is a test.

## What this deliberately is not

- **Not a ranking guarantee.** Nobody can sell you citation. The mechanisms are undocumented and
  change without notice.
- **Not a tool pitch.** `sl-geo-audit` names DataForSEO, Profound and Otterly because measurement
  requires some instrument, and it also gives the manual method for people with no budget.
- **Not vendor research.** Sources are the arXiv paper, platform documentation, and studies that
  publish their sample sizes. Where a source is a vendor with an interest, it is labelled.
- **Not an SEO course.** It assumes you already know what a canonical tag is.

## Repository layout

```
CONTEXT.md                        the hub file: load before running any skill
references.md                     citation registry, every key resolved
skills/
  sl-search-surfaces/SKILL.md     the model, the vocabulary, the priority order
  sl-geo-audit/SKILL.md           scored audit across three dimensions
  sl-citation-content/SKILL.md    the 5-element citation pattern
  sl-entity-infrastructure/SKILL.md  entity graph, schema, crawler access
research/
  the-alphabet-problem.md         which acronyms are real, and the skeptic's case
  aggarwal-2023-findings.md       what the foundational study actually measured
  scoring-rubric.md               the weights, and why they are set that way
```

## License

MIT. Use it, fork it, ship it in your own collection. Attribution appreciated, not required.

Research and skills by [Omar Fouad](https://github.com/omarmfouad25).
