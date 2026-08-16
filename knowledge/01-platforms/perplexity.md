---
title: "Perplexity"
file: perplexity
surface: geo
tags: [perplexity, platform, freshness, reddit, citation, rag]
last_validated: 2026-05-21
freshness: volatile
references_used: [Profound-Citations-2026, Aggarwal-2023]
---

# Perplexity

A real-time answer engine. Where ChatGPT blends training knowledge with retrieval, **Perplexity runs
a fresh web search for every query** and synthesizes from what it finds, with inline citations.

## TL;DR

| | |
|---|---|
| **Index** | Live retrieval per query, multi-source |
| **Citations per answer** | **~22**, roughly 4x an AI Overview `[Profound-Citations-2026]` |
| **Citation philosophy** | Community-weighted |
| **Defining property** | Reddit at 46.7% of top-10 cited sources `[Profound-Citations-2026]` |
| **Freshness** | The dominant signal. Reported ~82% of cited content under 30 days old |
| **Overlap with ChatGPT** | ~11% of cited domains |

## The architectural fact that determines everything else

**Every query triggers a fresh retrieval.** There is no reliance on what the model memorised. Three
consequences follow:

1. **Freshness dominates.** Recent content is cited disproportionately, and stale content on an
   authoritative domain loses to fresher community content.
2. **Citation count is high**, around 22 per answer, so the bar for being *one of* the cited sources
   is lower here than anywhere else.
3. **Source diversity skews to community.** Forums, Reddit and video transcripts punch far above
   their weight.

**Inference:** point two is the strategically useful one and it is under-appreciated. With ~5 slots
in an AI Overview, citation is close to zero-sum. With ~22, a competent mid-authority page has a
genuinely reachable target. Perplexity is the easiest of the three surfaces to get cited on, and it
is the one most teams ignore.

## What gets cited

Domain shares `[Profound-Citations-2026]`:

| Domain | Share of Perplexity citations | Share of top-10 sources |
|---|---:|---:|
| **Reddit** | **6.6%** | **46.7%** |
| YouTube | 2.0% | 13.9% |
| Gartner | 1.0% | |
| Yelp | 0.8% | |
| LinkedIn | 0.8% | |

**Reddit dominance is the defining feature, and the inverse is just as striking: Wikipedia, which
supplies 47.9% of ChatGPT's top-10 sources, does not appear in Perplexity's top sources at all.**

Those two facts side by side are the clearest possible demonstration that "AI search optimization"
as a single activity does not exist. The two platforms have close to opposite source preferences.

## Ranking factors

**1. Freshness, the dominant signal.** Reported analyses put roughly **82% of cited content within
the last 30 days**, and visible year markers in titles and headings are associated with materially
higher citation rates. Accurate `dateModified` matters, and so does actually changing the content
rather than touching the field.

**2. Real-time architecture.** Because retrieval is live, **indexing speed matters**. A slow-to-index
site loses the window entirely on fast-moving topics, which is a failure mode that does not exist on
the other surfaces.

**3. Consensus across independent sources.** Perplexity appears to weight agreement. A brand
mentioned once looks like an outlier; the same brand described consistently across Reddit, video,
two trade publications and an analyst report reads as established. **Inference:** this is reasoning
from how retrieval-and-synthesis behaves under conflicting sources, not a published finding.

**4. Retrievability of the chunk.** Semantic clarity, lists, tables and question-answer structure
score better in a retriever than dense unstructured prose. This is the same craft that pays on every
surface `[Aggarwal-2023]`.

**5. Genuine user voice.** Real reviews, transcripts and case studies with attribution outperform
corporate copy.

## The five levers

| Lever | Notes |
|---|---|
| **Freshness discipline** | Real quarterly refresh on cornerstone pages, monthly on fast-moving topics. Visible review dates |
| **Indexing speed** | Fast publish-to-index is a competitive advantage here specifically |
| **Reddit presence** | **Do not astroturf.** Both the platform and the community detect it, and the downside is severe. Disclosed participation only |
| **Video with transcripts** | YouTube at 13.9% of top-10 sources. Transcripts are retrievable text |
| **Consistent cross-source positioning** | Describe yourself the same way everywhere so consensus can form |

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Astroturfing Reddit | Detected, and the reputational downside dwarfs the citation upside |
| Touching `dateModified` without changing content | Transparent, and it trains readers to distrust your dates |
| Porting a ChatGPT strategy unchanged | Near-opposite source preferences. Wikipedia does not carry here |
| Ignoring it because it is smaller than Google | ~22 citation slots make it the most winnable surface of the three |
| Publishing slowly on fast-moving topics | Live retrieval means a missed window is a missed citation |
| One blended AI visibility score | ~11% domain overlap with ChatGPT makes the average meaningless |

## What is not known

- Whether the ~82% freshness figure holds across verticals or is skewed by news-heavy queries
- How consensus is actually weighted, as opposed to observed
- Whether Pro and free tiers differ in retrieval breadth
- Non-English behaviour, which is largely unmeasured in public

## References

| Key | Resolution |
|---|---|
| `[Profound-Citations-2026]` | Profound. Domain-level citation shares across platforms. ⚠ Vendor |
| `[Aggarwal-2023]` | Aggarwal et al. GEO: Generative Engine Optimization. https://arxiv.org/abs/2311.09735 |

Full registry: [`../../references.md`](../../references.md).

## Related files

- [`chatgpt-search.md`](chatgpt-search.md), the opposite citation philosophy
- [`ai-overviews.md`](ai-overviews.md), the balanced middle
- [`../03-measurement/mention-tracking.md`](../03-measurement/mention-tracking.md), measuring per platform
- [`../../skills/sl-citation-content/SKILL.md`](../../skills/sl-citation-content/SKILL.md), the writing craft
