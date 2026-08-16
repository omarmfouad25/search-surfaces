---
title: "Mention tracking: measuring citation share"
file: mention-tracking
surface: geo
tags: [measurement, tracking, citation-share, tooling, methodology]
last_validated: 2026-05-21
freshness: drift-watch
references_used: [Profound-Citations-2026, Conductor-AEO-GEO-2026]
---

# Mention tracking

Measuring whether AI assistants name you, how often, and instead of whom.

**This is the layer that justifies the vocabulary.** SEO has Search Console. AEO has the visible
result page. GEO has neither, and building the measurement yourself is most of the work.

## TL;DR

| | |
|---|---|
| **Core metric** | Share of citation: of N queries across M assistants, how often are you named |
| **Minimum viable** | 10 queries, 4 assistants, manual, about one hour |
| **Cadence** | Monthly. Weekly mostly measures sampling noise |
| **Non-negotiable** | Report **per assistant**. Never one blended score |
| **Hardest part** | Outputs are not reproducible. Undated evidence is not evidence |

## What makes this genuinely hard

Four properties that no other search measurement has:

1. **Non-determinism.** The same prompt returns different answers run to run. A single query is an
   anecdote, not a measurement.
2. **No official reporting.** No assistant offers the equivalent of Search Console. Everything is
   external observation.
3. **No history.** You cannot backfill. Whatever you did not capture is gone, which makes starting a
   baseline urgent rather than optional.
4. **Personalisation.** Results may vary by account, location and memory, so your reading is not
   necessarily anyone else's.

**Consequence: sample, date and screenshot everything.** A citation-share figure with no date and no
sample size is decoration.

## The free method, which is where to start

One hour, no budget, and it answers most first questions.

1. **Write 10 to 30 queries** in the words a real buyer would use. Informational and
   commercial-investigation intent, because those are where overviews trigger hardest.
2. **Name 3 to 10 competitors** you expect to appear.
3. **Run every query through four assistants:** ChatGPT with web access, Perplexity, Claude, and
   Google. Use a clean session.
4. **Record per query, per assistant:** were you named, at what position, which competitors were
   named, and which URL was cited.
5. **Screenshot everything**, with the date visible.
6. **Repeat monthly**, same queries, same method.

That produces a real baseline. Most teams have never done it even once.

## The tooled method

| Purpose | Tool |
|---|---|
| Programmatic prompt submission and citation capture | DataForSEO `ai_opt_*` family |
| Continuous brand citation tracking across assistants | Profound, Otterly |
| AI search analytics | Various, and the category is churning |

Tooling buys frequency and consistency, not insight. **Do the manual round first**, because it
teaches you what the queries should be, and choosing the wrong query set is the expensive mistake
here, not choosing the wrong tool.

## The metric

```
Citation share = (queries where you were named) / (total queries x assistants)
```

Report it **sliced by assistant**, always:

```
                ChatGPT   AI Overviews   Perplexity   Claude
Cited              4/20          7/20         11/20     3/20
Competitor A      12/20         14/20          9/20    11/20
Competitor B       8/20          6/20         13/20     7/20
```

**A blended average would hide the entire story in that table.** Cited-domain overlap between
platforms runs around 11% `[Profound-Citations-2026]`, so the platforms genuinely disagree about who
is worth citing. Perplexity is often the strongest column and ChatGPT the weakest, and those two
gaps have completely different remedies: Perplexity rewards freshness and community presence, while
ChatGPT rewards entity infrastructure and earned media.

## What to track beyond presence

| Signal | Why |
|---|---|
| **Position** | Named first reads differently from named last |
| **Cited URL** | Yours, or someone writing about you. Very different problems |
| **Competitor set** | Who the assistant considers comparable to you, which is market intelligence in itself |
| **Factual accuracy** | **Highest priority.** A confidently wrong answer is worse than absence |
| **Overview trigger** | Whether an AI Overview appeared at all. Trigger rates vary hugely by query type and vertical `[Conductor-AEO-GEO-2026]` |
| **Classic rank alongside** | Rank present but citation absent is the cheapest gap to close |

## Reading the results

| Pattern | Diagnosis | Remedy |
|---|---|---|
| Never named on any assistant | Identity. The model cannot resolve you | Entity infrastructure |
| Named on Perplexity, absent on ChatGPT | Bing index or entity gap | Check Bing first, then Wikidata |
| Named on ChatGPT, absent on Perplexity | Freshness or community absence | Refresh cadence, real community presence |
| Named but a third party is cited | Others describe you better than you do | Citation-worthy content on your own pages |
| Ranking top 10, never cited | Content gap, not authority | The cheapest fix available. Rewrite the paragraph |
| Named, but wrong | Source contamination | Urgent. Correct at the contaminating source |

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| One blended AI visibility score | Averages away the only actionable signal |
| Measuring weekly | Mostly measures non-determinism |
| One prompt as a measurement | Outputs vary run to run. Sample |
| No screenshots | Assistant outputs are not reproducible. No evidence, no proof of movement |
| No baseline before changes | This work moves slowly. Without a starting point you cannot show it worked |
| Reporting share with no date or sample size | Meaningless within a quarter |
| Buying tooling before defining the query set | The query set is the hard part, and the tool cannot choose it |
| Promising a citation-share target | Nobody controls these mechanisms |

## References

| Key | Resolution |
|---|---|
| `[Profound-Citations-2026]` | Profound. Cross-platform citation shares, ~11% domain overlap. ⚠ Vendor |
| `[Conductor-AEO-GEO-2026]` | Conductor. 2026 AEO/GEO Benchmarks, 21.9M searches. ⚠ Vendor |

Full registry: [`../../references.md`](../../references.md).

## Related files

- [`../01-platforms/ai-overviews.md`](../01-platforms/ai-overviews.md)
- [`../01-platforms/chatgpt-search.md`](../01-platforms/chatgpt-search.md)
- [`../01-platforms/perplexity.md`](../01-platforms/perplexity.md)
- [`../../skills/sl-geo-audit/SKILL.md`](../../skills/sl-geo-audit/SKILL.md), this as a scored procedure
- [`../../research/scoring-rubric.md`](../../research/scoring-rubric.md), where citation share sits in the score
