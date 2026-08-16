---
title: "ChatGPT search"
file: chatgpt-search
surface: geo
tags: [chatgpt, openai, bing, platform, wikipedia, citation]
last_validated: 2026-05-21
freshness: volatile
references_used: [Profound-Citations-2026, Aggarwal-2023, Rankability-llmstxt-2026]
---

# ChatGPT search

ChatGPT's web-retrieval mode fetches live results, synthesizes an answer, and attaches inline
citations.

## TL;DR

| | |
|---|---|
| **Index** | **Bing.** This is the single most important fact on the page |
| **Citation philosophy** | Concentrated on authoritative reference sources |
| **Defining property** | Wikipedia at 47.9% of top-10 cited sources `[Profound-Citations-2026]` |
| **Community sources** | Low. Reddit at 1.8% |
| **Overlap with Perplexity** | ~11% of cited domains `[Profound-Citations-2026]` |

## The architectural fact that determines everything else

**ChatGPT search retrieves through Microsoft Bing's index.**

Four consequences, in order of how often they are missed:

1. **Not in Bing means not citable by ChatGPT**, regardless of Google rank. A site can dominate
   Google and be invisible here.
2. **Bing Webmaster Tools matters again.** Separate verification, separate sitemap submission,
   separate coverage report. Most teams have never opened it, because a decade of correctly ignoring
   Bing for ranking carried into an era where it gates an entire assistant.
3. **Disallowing Bingbot in `robots.txt` blocks ChatGPT citation.** Check this rather than assume it.
4. **Bing's index lags on fresh content**, so newly published pages have a delay before they can be
   cited here that they would not have in Perplexity.

**This is the cheapest high-value check in the whole discipline.** It takes ten minutes and it is
binary.

## What gets cited

Domain shares `[Profound-Citations-2026]`:

| Domain | Share of ChatGPT citations |
|---|---:|
| **Wikipedia** | **7.8% overall, 47.9% of top-10 cited sources** |
| Reddit | 1.8% |
| Forbes | 1.1% |
| G2 | 1.1% |
| TechRadar | 0.9% |

**The Wikipedia concentration is the defining property.** No other major surface concentrates on one
source the way this one does. Two consequences follow directly:

1. **Entity presence in Wikidata and Wikipedia is the highest-leverage move for ChatGPT
   visibility**, more than anything you can do on your own domain.
2. **Earned coverage in established publications is second.** Low-authority domains are
   systematically downweighted here in a way they are not in Perplexity.

## How it differs from the other two

| Dimension | ChatGPT | AI Overviews | Perplexity |
|---|---|---|---|
| Citations per answer | ~3 to 5 | ~5 | **~22** |
| Source diversity | Concentrated, Wikipedia-heavy | Balanced | High, community-heavy |
| Index | Bing | Google | Live multi-source |
| Freshness weighting | Moderate | Moderate | **Very high** |
| Community sources | Low, Reddit 1.8% | Medium, Reddit 21% of top-10 | High, Reddit 46.7% of top-10 |

**Optimising for ChatGPT is not optimising for Perplexity.** Only about 11% of cited domains overlap
`[Profound-Citations-2026]`. A blended "AI visibility" number averages away the only actionable
signal, which is which specific platform is not citing you and why.

## The four levers, in dependency order

**1. Bing index health.** Foundational. Verify in Bing Webmaster Tools, submit the sitemap there,
allow Bingbot, watch coverage. Nothing below matters until this passes.

**2. Wikidata and Wikipedia presence.** Given the 47.9% concentration, this is the highest-leverage
entity work available. A structured, sourced Wikidata item first; a Wikipedia article only where
genuine independent notability exists. **Do not create one otherwise:** it gets deleted, publicly,
and the deletion is permanent.

**3. Earned media authority.** One placement in a genuinely respected publication can compound,
because roundup and "best of" articles get lifted close to verbatim.

**4. Depth on your own domain.** Topic clusters, real internal linking, citation-worthy paragraphs,
and author schema. Necessary but, on this surface specifically, not the highest-leverage layer.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Checking Google indexing only | The retrieval index is Bing |
| Assuming Bingbot is allowed | Verify. It is one line and it is binary |
| Forcing a Wikipedia article for a non-notable brand | Deleted publicly, and it costs credibility |
| Treating "About Us" as an authority source | Self-published pages are rarely cited here; third-party coverage is |
| Blended cross-platform visibility scores | ~11% domain overlap makes the average meaningless |
| Keyword stuffing | −9% across generative engines `[Aggarwal-2023]` |
| Shipping `llms.txt` and expecting citation | No measured correlation `[Rankability-llmstxt-2026]` |
| Heavy promotional copy | Downweighted at synthesis |

## What is not known

- How user-feedback signals feed source selection, if at all
- Whether model version changes shift citation patterns, and by how much
- How memory and personalisation interact with citation
- Non-English citation behaviour. Published measurement is overwhelmingly English

## References

| Key | Resolution |
|---|---|
| `[Profound-Citations-2026]` | Profound. Domain-level citation shares across platforms. ⚠ Vendor |
| `[Aggarwal-2023]` | Aggarwal et al. GEO: Generative Engine Optimization. https://arxiv.org/abs/2311.09735 |
| `[Rankability-llmstxt-2026]` | Rankability with SE Ranking. llms.txt study, ~300K domains. ⚠ Vendor |

Full registry: [`../../references.md`](../../references.md).

## Related files

- [`ai-overviews.md`](ai-overviews.md), the Google surface
- [`perplexity.md`](perplexity.md), the opposite citation philosophy
- [`../02-signals/llms-txt.md`](../02-signals/llms-txt.md), why it is not a lever
- [`../../skills/sl-entity-infrastructure/SKILL.md`](../../skills/sl-entity-infrastructure/SKILL.md), the Bing and entity work as a procedure
