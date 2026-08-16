---
title: "Google AI Overviews"
file: ai-overviews
surface: geo
tags: [ai-overviews, google, platform, citation, zero-click]
last_validated: 2026-05-21
freshness: volatile
references_used: [SurferSEO-AIO-2025, Profound-Citations-2026, Conductor-AEO-GEO-2026, BrightEdge-AIO-Feb2026, Ahrefs-AIO-CTR-2025, Ahrefs-AIO-CTR-Feb2026, Aggarwal-2023, Google-AIO-Launch-2024]
---

# Google AI Overviews

AI-generated answer blocks at the top of Google results, synthesizing multiple cited sources. They
replaced the "Search Generative Experience" labelling when Google made them a default feature
`[Google-AIO-Launch-2024]`.

**Why this file matters most:** of the three major generative surfaces, this is the one attached to
the search engine that still carries the majority of query volume. It is the highest-consequence
surface for existing organic traffic.

## TL;DR

| | |
|---|---|
| **Index** | Google |
| **Typical length** | ~157 words, 99% under 328 words `[SurferSEO-AIO-2025]` |
| **Sources per answer** | ~5, with 90% citing 8 or fewer `[SurferSEO-AIO-2025]` |
| **Citation philosophy** | The most balanced of the three: authoritative plus community |
| **Defining property** | **48% of citations come from outside the top 10** `[SurferSEO-AIO-2025]` |
| **Trigger rate** | 25% to 50% depending on whose method you accept, see below |

## How often they trigger, and why nobody can tell you precisely

| Source | Rate | Method |
|---|---:|---|
| `[BrightEdge-AIO-Feb2026]` | ~48% | Tracked queries, nine industries, +58% year on year |
| `[Conductor-AEO-GEO-2026]` | 25.11% | 21.9M searches |

**These disagree by roughly a factor of two, and both are defensible.** They sample different query
populations. The honest statement is a **range: 25% to 50% of US English queries, trending up**, and
higher in some verticals: healthcare measured at 48.75% `[Conductor-AEO-GEO-2026]`.

Treat any single precise figure for this as a red flag about the person quoting it.

## Trigger rate by query type, which is the actually useful cut

Aggregate rates hide the pattern that should drive strategy. Trigger probability varies enormously
by **query shape**, drawn from published trigger analyses:

| Query type | Trigger rate |
|---|---:|
| Comparison, "X vs Y" | ~95% |
| Review queries | ~86% |
| Question-format | ~86% |
| "Near me" informational | ~77% |
| Informational, broad | ~36% |
| Commercial investigation | ~8% |
| Transactional | ~5% |

**The asymmetry is the whole strategy.** Transactional queries still resolve to maps, ads and
classic listings, so ordinary SEO and local discipline carry them. But comparison and question
content is near-certain to trigger an overview, which means on those queries you are either a cited
source or you are absent. **Comparison content is where the investment compounds.**

## Structural anatomy

From the largest published structural sample, 405,576 overviews `[SurferSEO-AIO-2025]`:

| Property | Finding |
|---|---|
| Average length | 157 words, roughly 984 characters |
| Length ceiling | 99% under 328 words |
| Sources cited | ~5 average, 90% cite 8 or fewer |
| Source repetition | Under 1%. The same URL rarely appears twice |
| List usage | 78% include a list. 22% are paragraph only |
| Exact-query match | Only 5.4%. Overviews paraphrase rather than restate |
| E-commerce sources | 0.3% of citations |
| User-generated sources | 0.3% |

**Read on length:** a 40 to 60 word answer block is roughly the right scale for one citable chunk.
Past about 80 words the model paraphrases or skips, which loses you the verbatim lift.

## What gets cited

Domain-level shares `[Profound-Citations-2026]`:

| Domain | Share of AIO citations | Share of top-10 AIO sources |
|---|---:|---:|
| Reddit | 2.2% | 21.0% |
| YouTube | 1.9% | 18.8% |
| Quora | 1.5% | 14.3% |
| LinkedIn | 1.3% | |
| Gartner | 0.7% | |

**Balanced, and that is the distinguishing feature.** Overviews blend authoritative sources with
community discussion. This is the most heterogeneous citation mix of the three major surfaces: wider
than ChatGPT, which concentrates on Wikipedia, and less community-tilted than Perplexity.

## The mid-rank window

This is the most actionable finding in the whole file `[SurferSEO-AIO-2025]`:

- **52%** of cited sources also rank in the top 10 for that query
- **48% of citations come from pages outside the top 10**
- Among overlapping sources, the average position is **5**
- 71% of the time, top-10 domains rank for more keywords than the AIO-cited domains
- 69% of the time, top-10 domains get more traffic than the AIO-cited domains

**Overviews cite mid-rank pages at rates well above those pages' traffic share.** That is the entry
door for a site that does not rank first, and it converges with the controlled finding that rank-5
pages gained roughly +115% visibility from adding citations `[Aggarwal-2023]`. Two independent
methods pointing the same way is the strongest evidence in this repository.

**Practical consequence:** prioritise rewriting pages sitting at rank 4 to 20 on queries that
trigger an overview. Not the homepage, and not the pages already ranking first.

## Click impact

| Source | Finding |
|---|---|
| `[Ahrefs-AIO-CTR-2025]` | 34.5% reduction in average CTR for top-ranking pages, 300K keywords |
| `[Ahrefs-AIO-CTR-Feb2026]` | **58%** in the follow-up study |

**The click loss nearly doubled in under a year.** That trajectory, more than either absolute
number, is the thing to plan around.

**Implication:** ranking first is no longer sufficient. A page can hold position one and still lose
a third to well over half its clicks to the block above it. Citation inside the overview becomes the
visibility win, with clicks following indirectly through brand recall rather than directly.

## What appears to drive citation

There is no published algorithm. This is synthesis from the controlled study, the structural sample
and practitioner observation, and it is ordered by how confident the evidence is.

**Reasonably supported**

1. **Structure.** Clear heading hierarchy, lists and tables. 78% of overviews contain a list
2. **Citation-worthy paragraphs.** Entity named, quantified, attributed
3. **Topical depth across the domain**, not a single isolated page
4. **Being indexed and topically relevant.** Top-10 rank is not required, as the 48% figure shows
5. **Schema markup**, which improves eligibility without guaranteeing anything

**Weak or unproven**

1. Domain authority on its own
2. Exact-match keywords. Only 5.4% phrase match; semantic relevance dominates
3. `llms.txt` presence, where the measured correlation is zero. See [`../02-signals/llms-txt.md`](../02-signals/llms-txt.md)

**Actively negative**

1. Thin content
2. Aggressive commercial framing. **Inference:** the 0.3% e-commerce citation share is consistent
   with promotional pages being filtered at synthesis, though the data shows the outcome rather than
   the mechanism
3. Content that only exists after client-side rendering

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Quoting one precise trigger rate | The two best sources disagree by 2x. Give the range |
| Optimising the homepage for citation | Rarely the citable asset. Mid-rank informational pages are |
| Writing 300-word answer blocks | Past ~80 words the model paraphrases instead of lifting |
| Chasing transactional queries with GEO tactics | ~5% trigger rate. Ordinary SEO owns those |
| Assuming rank 1 protects traffic | Measured click loss reached 58% |
| Treating this as the same surface as ChatGPT | Different index, different citation mix |

## What is not known

- How freshness is weighted against authority. Observed, not measured
- Whether non-English and RTL queries behave differently. Almost all measurement is English
- How regulated verticals are handled. Medical queries sometimes return disclaimer-heavy overviews
  with thin citation
- Whether author markup causes lift or merely correlates with sites that would rank anyway

## References

| Key | Resolution |
|---|---|
| `[SurferSEO-AIO-2025]` | SurferSEO. Structural analysis of 405,576 AI Overviews. ⚠ Vendor |
| `[Profound-Citations-2026]` | Profound. Domain-level citation shares across platforms. ⚠ Vendor |
| `[Conductor-AEO-GEO-2026]` | Conductor. 2026 AEO/GEO Benchmarks, 21.9M searches. ⚠ Vendor |
| `[BrightEdge-AIO-Feb2026]` | BrightEdge. AIO prevalence across nine industries. ⚠ Vendor |
| `[Ahrefs-AIO-CTR-2025]` | Ahrefs. 34.5% CTR reduction, 300K keywords. ⚠ Vendor |
| `[Ahrefs-AIO-CTR-Feb2026]` | Ahrefs. 58% CTR reduction, follow-up. ⚠ Vendor |
| `[Aggarwal-2023]` | Aggarwal et al. GEO: Generative Engine Optimization. https://arxiv.org/abs/2311.09735 |
| `[Google-AIO-Launch-2024]` | Google. AI Overviews launch announcement |

Full registry: [`../../references.md`](../../references.md).

## Related files

- [`chatgpt-search.md`](chatgpt-search.md), the Bing-indexed surface
- [`perplexity.md`](perplexity.md), the freshness-dominant surface
- [`../00-foundations/seo-vs-aeo-vs-geo.md`](../00-foundations/seo-vs-aeo-vs-geo.md), the matrix
- [`../03-measurement/mention-tracking.md`](../03-measurement/mention-tracking.md), how to measure citation share
- [`../../skills/sl-citation-content/SKILL.md`](../../skills/sl-citation-content/SKILL.md), turning this into pages
