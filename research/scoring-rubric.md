---
title: "Audit scoring rubric: the weights, and why they are set that way"
file: scoring-rubric
surface: cross
tags: [audit, scoring, rubric, weights, measurement]
last_validated: 2026-05-21
freshness: drift-watch
references_used: [Conductor-AEO-GEO-2026, Ahrefs-AIO-CTR-Feb2026, HigherVisibility-SearchPref-2025]
---

# Audit scoring rubric

One rubric that scores any site across the three surfaces, so results are comparable between sites
and over time. Used by `sl-geo-audit`.

The value of a rubric is not precision. These weights are judgements, and a different practitioner
would set them differently. The value is that the judgement is **written down before the audit runs**
and can be argued with, rather than being smuggled into a conclusion afterwards.

## Dimensions

| Dimension | Measures |
|---|---|
| **A. Foundations** | Can the site be discovered, crawled, indexed and understood? |
| **B. Answer Engine** | Does it capture snippets, People Also Ask, voice? |
| **C. Generative Citation** | Does the brand get cited inside AI answers? Is the entity resolvable? |

### A. Foundations (0 to 100)

| | Item | Points |
|---|---|---|
| A1 | Crawl and indexability, **Google and Bing** | 20 |
| A2 | Core Web Vitals, mobile | 15 |
| A3 | On-page hygiene | 15 |
| A4 | Schema baseline | 15 |
| A5 | Internal linking and architecture | 15 |
| A6 | International and RTL where applicable | 10 |
| A7 | Backlink health | 10 |

### B. Answer Engine (0 to 100)

| | Item | Points |
|---|---|---|
| B1 | Snippet ownership on target queries | 30 |
| B2 | Content structured for extraction | 25 |
| B3 | AEO schema coverage | 20 |
| B4 | People Also Ask coverage | 15 |
| B5 | Voice readiness | 10 |

### C. Generative Citation (0 to 100)

| | Item | Points |
|---|---|---|
| C1 | LLM mention share against competitors | 30 |
| C2 | Entity infrastructure | 25 |
| C3 | Citation-worthy content | 20 |
| C4 | E-E-A-T signals | 15 |
| C5 | Freshness discipline | 10 |

## Composite

```
Overall = (A x W_A) + (B x W_B) + (C x W_C)      where W_A + W_B + W_C = 1.0
```

## Weight profiles

| Profile | W_A | W_B | W_C | Use when |
|---|---|---|---|---|
| **Future-weighted** (default) | 0.30 | 0.20 | 0.50 | Mature site, AI-Overview-heavy queries |
| **Balanced** | 0.35 | 0.30 | 0.35 | Surface priority genuinely unclear |
| **Classic** | 0.50 | 0.30 | 0.20 | Broken foundations, defer GEO |

### Why the default leans to GEO

Three reasons, none of them decisive on its own:

1. **AI Overviews are absorbing informational queries.** Trigger rates measured around a quarter of
   searches overall, rising to roughly half in healthcare `[Conductor-AEO-GEO-2026]`, with measured
   click reduction of 58% `[Ahrefs-AIO-CTR-Feb2026]`.
2. **Assistant-native users bypass classic search entirely.** No amount of ranking reaches someone
   who never opens a search engine.
3. **AEO is the structural prerequisite for GEO**, not a parallel investment. Content structured for
   answer extraction is largely the same content that gets cited, so a chunk of AEO value is already
   counted inside C.

### The honest counter-argument

Classic search still carries the majority of volume: around 79.8% of surveyed US consumers still
preferred traditional engines for informational queries `[HigherVisibility-SearchPref-2025]`.
**A defensible reading of the same evidence puts Foundations at 0.50 and treats GEO as an option on
the future rather than the main event.** That is what the Classic profile is for.

Pick a profile deliberately, record which one and why, and do not change it after seeing the score.

## The automatic override

**Foundations below 50 forces the Classic profile**, regardless of the chosen default, and the audit
must report that the override fired.

A site that cannot be crawled cannot be cited. Recommending entity infrastructure spend to someone
whose pages are not indexed is the most common way this kind of audit does damage.

## Scoring discipline

- Report **per dimension and composite**. A single number hides where the problem is.
- Report **per assistant** for C1. Cited-domain overlap between assistants is low, so a blended
  average hides the actionable gap.
- **Track over time.** Drift is the signal. A one-off score is nearly meaningless.
- **A red dimension blocks the next tier.** Do not audit AEO on a site failing Foundations.
- **Date every external figure quoted**, and re-check anything marked volatile.

## Changelog

- 2026-05-21, v1.0, weights locked at Future-weighted 0.30 / 0.20 / 0.50

## References

| Key | Resolution |
|---|---|
| `[Conductor-AEO-GEO-2026]` | Conductor. *2026 AEO/GEO Benchmarks Report*, 21.9M searches. Vendor-published |
| `[Ahrefs-AIO-CTR-Feb2026]` | Ahrefs. *AI Overviews reduce clicks by 58%*, follow-up study, Feb 2026. Vendor-published |
| `[HigherVisibility-SearchPref-2025]` | Higher Visibility. *How People Search Today*, 1,500 US consumers, Feb 2025. Vendor-published survey |

## Related files

- [`../skills/sl-geo-audit/SKILL.md`](../skills/sl-geo-audit/SKILL.md), the audit that applies this
- [`../CONTEXT.md`](../CONTEXT.md), the priority order this rubric encodes
