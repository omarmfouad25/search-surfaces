---
title: "The alphabet problem: which search acronyms are real, and the skeptic's case"
file: the-alphabet-problem
surface: cross
tags: [terminology, framework, comparison, skepticism]
last_validated: 2026-05-21
freshness: stable
references_used: [Aggarwal-2023, HigherVisibility-SearchPref-2025]
---

# The alphabet problem

Five acronyms entered the search vocabulary in about two years. Most are aliases. A few are real.
The work underneath is mostly the same.

This file commits to a vocabulary, but it argues the other side first, because the other side has a
case and pretending otherwise is how this field got noisy.

## The acronyms in circulation

| Acronym | Full name | Claims to cover |
|---|---|---|
| **SEO** | Search Engine Optimization | Ranking pages in classic results |
| **AEO** | Answer Engine Optimization | Featured snippets, People Also Ask, voice |
| **GEO** | Generative Engine Optimization | Citation inside AI-synthesized answers `[Aggarwal-2023]` |
| AIO | AI Optimization | Umbrella term, and also a Google product name |
| LLMO | LLM Optimization | GEO, renamed |
| GAIO | Generative AI Optimization | GEO, with extra letters |
| SXO | Search Experience Optimization | UX plus SEO, pre-AI |

Six of these point at overlapping and sometimes identical work.

## The skeptic's case, put at full strength

The position, widely held among senior practitioners, is roughly: *it is all just SEO.*

**1. The tactics overlap almost completely.** Comparison pages, factual content with citations,
schema markup, direct answers to real questions, fast accessible sites. These are SEO fundamentals
that predate every new acronym. Renaming them does not make them disciplines.

**2. The skills are the same.** Someone who has spent a decade writing topically deep content with
clean structure is already executing most of what the GEO playbooks prescribe. They do not need a
new practice; they need a new report.

**3. Acronym churn sells consulting.** "Master GEO before your competitors" is sellable in a way
that "keep doing solid SEO" is not. Follow the incentive: most GEO guides are published by companies
selling GEO tools.

**4. Foundations still carry the volume.** Around 79.8% of surveyed US consumers still preferred
traditional search engines for informational queries `[HigherVisibility-SearchPref-2025]`. Classic
search is not the past tense.

**5. Even GEO advocates concede the overlap.** A common formulation in pro-GEO content is that
whatever you call it, it comes down to doing good SEO. When the people selling the distinction admit
the substance is shared, that is worth noticing.

**This argument is largely correct.** Any treatment of GEO that does not concede it is selling
something.

## The case for keeping three words

Three counter-points survive the above.

**1. The measurement genuinely differs.** SEO measures rank and clicks. AEO measures snippet
presence. GEO measures citation share inside a synthesized answer. Different instruments, and no
existing SEO report surfaces the GEO gap. Collapsing the vocabulary hides the measurement hole.

**2. Some tactics invert, rather than merely differing in degree.** Keyword stuffing measured at
roughly −9% visibility in generative engines, worse than doing nothing `[Aggarwal-2023]`. A tactic
that historically helped in moderation now actively harms. That is a real divergence, not a
rebrand.

**3. The opportunity sits in a different place.** The same study found the largest single effect on
pages around rank five, where adding citations produced roughly a +115% visibility lift
`[Aggarwal-2023]`. An SEO playbook organised around reaching position one will systematically
under-invest in exactly the pages with the most citation upside.

There is also an operational point that is not about evidence at all: the client conversation is
different. Wikidata entries, Reddit presence and cross-assistant mention tracking do not appear on a
traditional SEO contract, and pretending they are business as usual makes them invisible.

## Where this lands

**The skeptic is largely right about substance and mostly wrong about operations.**

- **Substance:** GEO is not a revolution. It is a sharper articulation of where good SEO has been
  heading for a decade. Helpful content, semantic depth, technical hygiene and authority drive
  citation across every surface.
- **Operations:** the surfaces are real, the measurement is genuinely different, and collapsing the
  distinction costs specific leverage: the Bing index for ChatGPT, freshness weighting for
  Perplexity, comparison content for AI Overviews.

So: distinct vocabulary, not because the craft fragmented, but because the **measurement** did.

## Locked vocabulary

| Term | Definition |
|---|---|
| **SEO** | Optimizing for rank in classic results |
| **AEO** | Optimizing for the answer slot above the links |
| **GEO** | Optimizing for citation inside AI-synthesized answers |

Not used: **AIO** (overloaded, and a product name), **LLMO** and **GAIO** (synonyms for GEO; the
original paper's term wins), **SXO** (pre-AI; UX is cross-cutting).

If someone uses a term from the second list, mirror it in conversation and write deliverables in
the first. Correcting people about acronyms is not a good use of anyone's credibility.

## How to explain this without selling snake oil

**1. Lead with the overlap.** "Most of this is SEO you already know, and if your fundamentals are
good you are already most of the way there." True, and it earns the rest of the conversation.

**2. Then name what is actually different.** Different measurement surfaces. Different platforms
with different citation behaviour and low overlap between them. A handful of structural tactics that
only matter for AI surfaces.

**3. Then drop the acronyms entirely.** "We will make sure your foundations are solid. We will make
sure your content is structured so AI tools can quote it. We will measure which tools cite you and
which do not, and fix the gaps." That is the same work, stated in a way nobody needs a glossary for.

## The pricing implication, stated plainly

Some agencies charge a GEO premium for what is largely SEO plus a few additions.

- **Do not bill GEO as a separate retainer** unless the deliverable genuinely includes new tooling
  and ongoing cross-assistant mention tracking.
- **Bundle it.** Measurement adds time; the content and technical work is shared.
- **A premium is defensible only when** the work includes cross-assistant citation tracking, an
  entity infrastructure rebuild, and continuing platform-specific measurement. Otherwise it is
  value-padding.

## References

| Key | Resolution |
|---|---|
| `[Aggarwal-2023]` | Aggarwal et al., Princeton and IIT Delhi. *GEO: Generative Engine Optimization*. https://arxiv.org/abs/2311.09735 |
| `[HigherVisibility-SearchPref-2025]` | Higher Visibility. *How People Search Today*, 1,500 US consumers, Feb 2025. Vendor-published survey |

## Related files

- [`aggarwal-2023-findings.md`](aggarwal-2023-findings.md), the study behind the two hard numbers here
- [`../CONTEXT.md`](../CONTEXT.md), the vocabulary lock as an operating rule
- [`../skills/sl-search-surfaces/SKILL.md`](../skills/sl-search-surfaces/SKILL.md), the model as a skill
