---
title: "What the Aggarwal GEO study actually measured"
file: aggarwal-2023-findings
surface: geo
tags: [research, aggarwal, evidence, tactics, primary-source]
last_validated: 2026-05-21
freshness: stable
references_used: [Aggarwal-2023]
---

# What the Aggarwal study actually measured

Nearly every claim in circulation about generative engine optimization traces back to one paper:
Aggarwal et al., *GEO: Generative Engine Optimization*, Princeton and IIT Delhi, 2023
`[Aggarwal-2023]`. It coined the term.

It is worth reading the paper rather than the posts about it, because the posts consistently drop
the caveats and keep the headline.

**Source:** https://arxiv.org/abs/2311.09735

## What it did

The authors built a benchmark of roughly 10,000 queries, applied nine distinct optimization tactics
to source content, and measured the change in visibility inside generated answers. Visibility was
scored with position-adjusted word count, which weights both how much of a source is used and where
it appears in the answer.

The important design choice: **it is a controlled comparison against an unoptimized baseline**, not
an observational study of what happens to rank well. That is why it can support causal-sounding
statements about tactics, and it is why it is more useful than most of what followed it.

## The result table

Nine tactics, ranked by measured lift:

| Rank | Tactic | Visibility | Lift |
|---:|---|---:|---:|
| 1 | Quotation addition, verbatim quotes from credible sources | 27.8 | **+41%** |
| 2 | Statistics addition, quantify qualitative claims | 25.9 | **+33%** |
| 3 | Fluency optimization, readability and flow | 25.1 | **+29%** |
| 4 | Cite sources, inline citations to credible references | 24.9 | **+28%** |
| 5 | Technical terms, domain vocabulary | 23.1 | +18% |
| 6 | Easy-to-understand, simplify without losing meaning | 22.2 | +14% |
| 7 | Authoritative, more persuasive and authoritative tone | 21.8 | +12% |
| 8 | Unique words, rare terminology | 20.7 | +6% |
| 9 | **Keyword stuffing**, pack query keywords into the text | **17.8** | **−9%** |

A second run against a live generative engine produced smaller absolute lifts but **the same
ordering and the same sign on keyword stuffing**, which is the part that matters. Tactics that work
in one generative engine tend to work in others; keyword stuffing reliably backfires.

## The three conclusions worth keeping

**1. Substance beats style, and it is not close.** The four substance tactics (quotations,
statistics, citations, fluency) all cleared +28%. The tone and vocabulary tactics clustered between
+6% and +18%. **Sounding authoritative was worth +12%; actually citing a source was worth +28%.**
Most brand content invests in the first and avoids the second.

**2. Keyword stuffing is worse than doing nothing.** At −9% it is the only tactic tested that
underperformed the baseline. This is the sharpest divergence between classic SEO instinct and
generative engines, and it is the single most useful thing in the paper.

**3. Lower-ranked pages gain the most.** The largest single effect reported is around rank five,
where adding citations produced roughly a **+115% visibility lift**. Combined tactics averaged
around +31%.

**Inference, not a finding:** point three implies mid-rank pages are the highest-leverage rewrite
targets, and that an SEO programme organised entirely around reaching position one will
systematically under-invest in exactly the pages with the most citation upside. The paper reports
the effect; the strategic conclusion is mine.

## Caveats the secondary coverage drops

Read the paper for these; almost no blog post carries them.

- **It is 2023.** Generative engines have changed substantially since. The *ordering* of tactics has
  proven durable, the *magnitudes* should not be quoted as current.
- **Position-adjusted word count is a proxy for visibility**, not a business metric. It is not
  traffic, not conversion, and not brand recall.
- **Effectiveness varied by domain.** A single global ranking hides real variation between subject
  areas.
- **The benchmark is synthetic** in construction. It is a controlled experiment, with the usual
  trade-off against ecological validity.
- **The authors have an interest in the framing.** They named the field. That does not make the
  measurements wrong, but it is worth stating.

## Why it still matters

Three years on it remains the only widely cited **controlled** study in this area. Nearly everything
published since is either observational correlation or vendor research with an interest in the
conclusion. When a GEO claim conflicts with this paper, the burden of proof sits with the claim.

Treat it as the strongest available evidence, not as settled fact, and re-check magnitudes before
quoting them.

## References

| Key | Resolution |
|---|---|
| `[Aggarwal-2023]` | Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande. *GEO: Generative Engine Optimization*. Princeton University and IIT Delhi, Nov 2023. https://arxiv.org/abs/2311.09735 |

## Related files

- [`the-alphabet-problem.md`](the-alphabet-problem.md), where this evidence sits in the terminology argument
- [`../skills/sl-citation-content/SKILL.md`](../skills/sl-citation-content/SKILL.md), the tactics turned into a writing workflow
