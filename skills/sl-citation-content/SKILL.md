---
name: sl-citation-content
description: >-
  Write or rewrite content so AI assistants quote it verbatim. Use when the user asks how to write
  content that ChatGPT or Perplexity will cite, wants pages rewritten for AI search, asks why their
  content ranks but never gets quoted, needs citation-worthy paragraphs, asks what makes an LLM lift
  a passage, or wants to structure an article for AI Overviews. Applies the five-element citation
  pattern and the Aggarwal evidence on which tactics measurably help.
version: 1.0.0
when_to_use: >-
  When the gap is content rather than identity or authority. Run sl-geo-audit first if you do not
  know which. If the machine cannot identify the brand at all, use sl-entity-infrastructure instead,
  because no amount of rewriting fixes an entity the model cannot resolve.
triggers:
  en:
    - write content AI will cite
    - citation-worthy content
    - rewrite for AI search
    - why is my content not quoted
    - content for AI Overviews
    - make LLMs quote my page
    - GEO copywriting
  ar:
    - كتابة محتوى يستشهد به الذكاء الاصطناعي
    - تحسين المحتوى لمحركات الإجابة
compatibility:
  - Claude Code
  - any runtime that reads SKILL.md frontmatter
metadata:
  author: Omar Fouad
  category: search
  tags: [geo, content, copywriting, citation, aggarwal, eeat]
license: MIT
last_validated: 2026-05-21
freshness: drift-watch
references_used: [Aggarwal-2023, Google-EEAT-Helpful, Google-SchemaFAQ-HowTo]
---

# Citation-worthy content

## TL;DR

A paragraph an LLM lifts has all five of these. Miss one and it degrades; miss three and it is
invisible.

| # | Element | Test |
|---|---|---|
| 1 | **Entity named explicitly** | No pronouns, no "the product". Could this sentence survive alone? |
| 2 | **One definitive claim** | Not "may help". Stated |
| 3 | **A number, date or proof** | Something quotable |
| 4 | **Attributed source, inline** | Not a reference list at the bottom |
| 5 | **Standalone readability** | No "as mentioned above" |

**Length:** 3 to 5 sentences, 40 to 80 words. Long enough to carry evidence, short enough to lift whole.

## Before starting

1. **Load [`CONTEXT.md`](../../CONTEXT.md).**
2. **Confirm the gap is content.** If the entity is unresolvable, rewriting is wasted effort. Route
   to `sl-entity-infrastructure`.
3. **Establish YMYL status.** Health, finance and legal content is held to a higher evidentiary bar,
   and **accuracy always outranks citation-worthiness**. Never sharpen a hedge into a definitive
   claim the source does not support just because definitive statements get cited more.
4. **Get the source material.** This skill cannot invent evidence. If there is no study, no number
   and no credible third party to cite, the honest output is "this page has nothing citable yet",
   plus what would need to exist.

## Core framework: what the evidence says works

From a controlled study of nine optimization tactics across 10,000 queries `[Aggarwal-2023]`,
ranked by measured visibility lift:

| Rank | Tactic | Lift |
|---:|---|---:|
| 1 | Quotation addition, insert verbatim quotes from credible sources | **+41%** |
| 2 | Statistics addition, replace qualitative claims with quantified ones | **+33%** |
| 3 | Fluency optimization, improve readability and flow | **+29%** |
| 4 | Cite sources, add inline citations | **+28%** |
| 5 | Technical terms, domain vocabulary where appropriate | +18% |
| 6 | Easy-to-understand, simplify without losing meaning | +14% |
| 7 | Authoritative tone, rewrite to sound more authoritative | +12% |
| 8 | Unique words, add rare terminology | +6% |
| 9 | **Keyword stuffing** | **−9%** |

**Three conclusions that should drive every rewrite:**

1. **Substance beats style.** The top four are all about adding evidence. The bottom four are about
   how the text sounds. Sounding authoritative is worth +12%; actually citing a source is +28%.
2. **Keyword stuffing is worse than doing nothing.** This inverts a traditional SEO instinct and is
   the single largest divergence between the surfaces.
3. **Lower-ranked pages gain most.** The same study reports the largest single effect for pages
   around rank five, where adding citations produced roughly a +115% visibility lift
   `[Aggarwal-2023]`. **Inference:** mid-rank pages are the highest-leverage rewrite targets, so
   start there rather than on already-dominant pages.

## Workflow

### [Phase 1/5: Select] Pick the pages worth rewriting

Priority order:

1. Pages ranking roughly 5 to 20 on a query where an AI Overview triggers. Biggest measured upside
2. Pages where a competitor is cited and this site is not, despite comparable rank
3. Pages with real evidence available but written vaguely
4. Everything else

**Do not start with the homepage.** It is rarely the citable asset.

### [Phase 2/5: Diagnose] Score the existing paragraphs

Run the five-element test on each substantive paragraph. Most failures cluster in two places:
**pronouns instead of the entity name**, and **hedged claims with no number**.

### [Phase 3/5: Rewrite] Apply the pattern

```
[Entity] is [precise definition or classification]. [Credible source] reported in [year] that
[quantified definitive claim]. Unlike [alternative], [Entity] [differentiator with mechanism].
```

**Weak:**

> Our platform can help many teams work faster. It uses modern automation and is well regarded in
> the industry.

Nothing here is liftable: no entity name, no number, no source, and two hedges.

**Citation-worthy:**

> **Acme Deploy** is a continuous-deployment service for containerised applications. In its 2025
> customer benchmark, published in full with methodology, median time from merge to production fell
> from 42 minutes to 6 across 180 participating teams. Unlike agent-based tools, Acme Deploy runs
> entirely from the existing CI pipeline, so no runtime is installed on production hosts.

Entity named twice, one definitive claim, three numbers, an attributed and methodologically
transparent source, a mechanism-level differentiator, and it survives being pulled out of context.

> **Illustrative example. The company and figures are invented.** Never publish a number you cannot
> resolve to a real source, and never reverse-engineer a statistic to fit the pattern.

### [Phase 4/5: Structure] Make the page extractable

- **H2s as real questions**, in the words a buyer would actually say aloud
- **A 40 to 60 word direct answer immediately under each H2**, before any preamble
- **One cited statistic and one named-source quote per page**, minimum
- **Tables and lists for comparisons**, which extract far more cleanly than prose
- **Visible author byline with credentials**, plus `Person` schema. On YMYL, non-negotiable
  `[Google-EEAT-Helpful]`
- **Visible `dateModified`**, human-readable, not markup only
- **Inline citations, not a bibliography.** Models lift sentences, not reference lists

### [Phase 5/5: Verify] Check before shipping

- Read each target paragraph aloud in isolation. Does it stand up?
- Does every number resolve to a real, nameable source?
- Has any hedge become a claim the source does not support? Revert it if so
- Is the entity named, not pronouned, in the first sentence?
- Has keyword density gone **down**?

## Best practices

- **Write the quotable paragraph first**, then build the page around it.
- **Quote other people.** The highest-lift tactic is adding verbatim quotes from credible sources,
  which most brand content avoids out of misplaced territoriality.
- **Publish your own numbers with methodology.** Original data is the most citable asset available,
  and almost nobody does it.
- **Specifics over adjectives**, always. "Reduces onboarding from 42 minutes to 6" beats
  "dramatically faster".
- **Say what you are not.** Explicit differentiation against a named alternative is exactly the
  comparison shape assistants reach for.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Keyword stuffing | −9% measured. Actively harms eligibility `[Aggarwal-2023]` |
| Authoritative tone with no evidence | +12%, one of the weakest. Models weigh evidence, not confidence |
| Vague quantifiers: "many", "often", "studies show" | Nothing to quote |
| Rare-word padding | +6%, and it costs readability |
| Dense academic prose | Readability outperforms it, +29% against +14% |
| Bottom-of-page reference lists | Models lift sentences with inline citations |
| FAQ schema on everything | Overuse is penalised. Mark up real Q&A only `[Google-SchemaFAQ-HowTo]` |
| Schema with no content quality behind it | No markup guarantees citation |
| Sharpening a hedge the source does not support | Fabrication. Disqualifying on YMYL, and wrong everywhere else |
| Rewriting a page for an entity the model cannot resolve | Wrong skill. Fix identity first |

## Output format

Per page:

```
PAGE: <url>
Current: <n>/5 elements present    Target: 5/5
Diagnosis: <which elements are missing and where>

REWRITE
  <the paragraph, ready to paste>

EVIDENCE USED
  <claim> -> <source, with link>      (one row per number; no unresolved rows)

STRUCTURE CHANGES
  <H2 rewrites, answer paragraphs, tables, schema, byline, date>

NOT DONE, AND WHY
  <claims that could not be sourced, and what evidence would be needed to make them>
```

That last block is the important one. Ending with an honest list of what could not be substantiated
is what separates this from generating plausible sentences.

## Questions to ask when the brief is thin

1. What is the most specific true thing you can say, that a competitor cannot?
2. Do you have original data, a study, a benchmark, or customer numbers you could publish?
3. Who is the credentialed human behind this page?
4. What do you want the assistant to say when someone asks about this topic? Say it in one sentence
5. Which named alternative are you better than, and by what mechanism?
6. Is any claim here regulated?

## References

| Key | Resolution |
|---|---|
| `[Aggarwal-2023]` | Aggarwal et al., Princeton and IIT Delhi. *GEO: Generative Engine Optimization*, 10,000-query study. https://arxiv.org/abs/2311.09735 |
| `[Google-EEAT-Helpful]` | Google Search Central. *Creating helpful, reliable, people-first content*. https://developers.google.com/search/docs/fundamentals/creating-helpful-content |
| `[Google-SchemaFAQ-HowTo]` | Google Search Central. FAQPage and HowTo structured data. https://developers.google.com/search/docs/appearance/structured-data/faqpage |

Full registry: [`references.md`](../../references.md). Study detail:
[`research/aggarwal-2023-findings.md`](../../research/aggarwal-2023-findings.md).

## Related skills

- `sl-search-surfaces`, the model
- `sl-geo-audit`, tells you which pages to rewrite and in what order
- `sl-entity-infrastructure`, run first if the entity is unresolvable
