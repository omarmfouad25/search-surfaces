---
title: "SEO vs AEO vs GEO: the matrix"
file: seo-vs-aeo-vs-geo
surface: cross
tags: [foundations, comparison, matrix, terminology, strategy]
last_validated: 2026-05-21
freshness: drift-watch
references_used: [Aggarwal-2023, HigherVisibility-SearchPref-2025, Conductor-AEO-GEO-2026, Ahrefs-AIO-CTR-Feb2026, Profound-Citations-2026, Google-EEAT-Helpful]
---

# SEO vs AEO vs GEO

Three surfaces, one asset. This file is the reference matrix. The argument for why three terms and
not one, or seven, is in [`../../research/the-alphabet-problem.md`](../../research/the-alphabet-problem.md).

## The matrix

| | **SEO** | **AEO** | **GEO** |
|---|---|---|---|
| **Goal** | Rank the page | Be the answer above the links | Be the citation inside the reply |
| **Surface** | Classic results | Snippets, People Also Ask, voice | AI Overviews, ChatGPT, Perplexity, Claude, Gemini |
| **Primary lever** | Authority and relevance | Q&A structure and schema | Evidence, freshness, entity clarity |
| **Key metric** | Rank, clicks, CTR | Snippet presence | Citation rate, mention share |
| **Index** | Google | Google | Google **and Bing** and live retrieval |
| **Unit of success** | A ranking URL | An extracted paragraph | A quoted sentence |
| **Who sees it** | Someone who clicks | Someone who reads and often does not click | Someone who may never visit a search engine |
| **Feedback speed** | Weeks | Weeks | 30 to 90 days |
| **Measurement tooling** | Search Console | Manual SERP inspection | Cross-assistant tracking, mostly paid or manual |

## The single most useful distinction

**SEO wins a position. AEO wins a box. GEO wins a sentence.**

The unit matters, because it changes what you optimise. Ranking optimises a page. Citation optimises
a **paragraph**, and specifically a paragraph that survives being pulled out of its page and dropped
into someone else's answer. That is a different craft, applied to the same asset.

## Where the volume actually is

Do not let the growth surface eclipse the volume surface.

| Fact | Source |
|---|---|
| ~79.8% of surveyed US consumers still prefer traditional engines for informational queries | `[HigherVisibility-SearchPref-2025]` |
| AI Overviews trigger on roughly 25% to 50% of queries depending on method, ~48.75% in healthcare | `[Conductor-AEO-GEO-2026]` |
| AI Overviews measured reducing clicks by 58%, up from 34.5% a year earlier | `[Ahrefs-AIO-CTR-Feb2026]` |

Read together: **classic search is still where most of the volume is, and it is where the losses are
happening.** The clicks are leaking from the surface that still carries the traffic. That is the
actual argument for GEO, and it is a stronger one than "AI is the future".

## Where they overlap, which is most of the way

A senior practitioner doing topical depth, clean structure, accurate schema and real answers to real
questions is already executing the majority of all three. The shared core:

- Crawlable, indexable, fast
- Topically deep rather than thin
- Clear heading hierarchy
- Genuine answers to genuine questions
- Accurate structured data
- Named, credentialed authors `[Google-EEAT-Helpful]`

**Roughly 70 to 80% of the work is shared.** Any framing that hides this is selling something.

## Where they genuinely diverge

Three places, and only three that matter:

**1. Keyword handling inverts.** Keyword stuffing helped in classic SEO in moderation. In generative
engines it measured **−9%, worse than doing nothing** `[Aggarwal-2023]`. Not a difference of degree.

**2. The index widens.** SEO and AEO are Google. GEO adds Bing, which gates ChatGPT search entirely,
plus live retrieval. **A site invisible to Bing is invisible to an entire assistant regardless of
Google rank**, and almost nobody checks.

**3. The rank window moves.** SEO optimises toward position one. Citation draws heavily from
mid-rank: 48% of AI Overview citations come from outside the top 10, and the controlled study found
its largest effect around rank five at roughly +115% `[Aggarwal-2023]`. **A programme organised
purely around reaching first place systematically under-invests in the pages with the most citation
upside.**

## Priority order

```
SEO first.  GEO next.  AEO last.
```

Roughly half of AI citations still originate from top-10 pages, so ranking is the substrate rather
than a parallel track. GEO precedes AEO because the answer box is a subset of a shrinking classic
result page while citation share is growing.

**This is a judgement, not a measurement**, and the counter-case is real: someone weighting the
zero-click numbers more heavily would put AEO second. The weight profiles in
[`../../research/scoring-rubric.md`](../../research/scoring-rubric.md) exist so this can be overridden
per engagement rather than argued about.

**The one hard rule:** a site failing foundations gets no GEO advice. It cannot be cited if it
cannot be crawled.

## The platforms are not one surface either

Even inside GEO the differences are severe. Cited-domain overlap between ChatGPT, AI Overviews and
Perplexity is roughly **11%** `[Profound-Citations-2026]`. Wikipedia supplies 47.9% of ChatGPT's
top-10 sources and does not feature in Perplexity's at all.

**Never report a single blended AI visibility score.** It averages away the only actionable
information, which is which specific platform is not citing you and why.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Collapsing all three into "search optimization" | Hides that the measurement differs, which is the entire justification for the vocabulary |
| Treating GEO as a replacement for SEO | Classic search still carries most volume |
| Selling three separate retainers | 70 to 80% of the work is shared. That is value-padding |
| Reporting one blended AI score | ~11% platform overlap makes it meaningless |
| Optimising only for rank 1 | Misses the mid-rank citation window entirely |
| Ignoring Bing | Gates ChatGPT search completely |

## References

| Key | Resolution |
|---|---|
| `[Aggarwal-2023]` | Aggarwal et al. GEO: Generative Engine Optimization. https://arxiv.org/abs/2311.09735 |
| `[HigherVisibility-SearchPref-2025]` | Higher Visibility. How People Search Today, 1,500 US consumers. ⚠ Vendor |
| `[Conductor-AEO-GEO-2026]` | Conductor. 2026 AEO/GEO Benchmarks, 21.9M searches. ⚠ Vendor |
| `[Ahrefs-AIO-CTR-Feb2026]` | Ahrefs. AI Overviews reduce clicks by 58%. ⚠ Vendor |
| `[Profound-Citations-2026]` | Profound. Cross-platform citation shares. ⚠ Vendor |
| `[Google-EEAT-Helpful]` | Google Search Central. Helpful content and E-E-A-T guidance |

Full registry: [`../../references.md`](../../references.md).

## Related files

- [`../../research/the-alphabet-problem.md`](../../research/the-alphabet-problem.md), why three terms and not seven
- [`../01-platforms/ai-overviews.md`](../01-platforms/ai-overviews.md)
- [`../01-platforms/chatgpt-search.md`](../01-platforms/chatgpt-search.md)
- [`../01-platforms/perplexity.md`](../01-platforms/perplexity.md)
- [`../../skills/sl-search-surfaces/SKILL.md`](../../skills/sl-search-surfaces/SKILL.md), this matrix as an invokable skill
