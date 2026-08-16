---
name: sl-geo-audit
description: >-
  Audit and score a site for AI citation readiness across three dimensions: Foundations, Answer
  Engine and Generative Citation. Use when the user asks why AI assistants never mention their
  brand, wants an AI visibility audit, asks how to measure GEO, wants to know why competitors get
  cited instead, needs a share-of-citation baseline, or asks what to fix first to appear in AI
  Overviews, ChatGPT, Perplexity or Claude answers.
version: 1.0.0
when_to_use: >-
  When the task is to measure and prioritise rather than to write or to build. Run sl-search-surfaces
  first. Produces a scored, weighted audit with a ranked action list, and hands off to
  sl-citation-content or sl-entity-infrastructure depending on where the gaps land.
triggers:
  en:
    - AI visibility audit
    - why does AI not mention us
    - GEO audit
    - share of citation
    - measure AI search performance
    - competitor gets cited and we do not
    - AI Overview audit
  ar:
    - تدقيق الظهور في الذكاء الاصطناعي
    - قياس الاستشهاد في نتائج الذكاء الاصطناعي
compatibility:
  - Claude Code
  - any runtime that reads SKILL.md frontmatter
metadata:
  author: Omar Fouad
  category: search
  tags: [geo, audit, scoring, measurement, entity, citation-share]
license: MIT
last_validated: 2026-05-21
freshness: drift-watch
references_used: [Aggarwal-2023, Conductor-AEO-GEO-2026, Ahrefs-AIO-CTR-Feb2026, Profound-Citations-2026]
---

# GEO citation audit

## TL;DR

| | |
|---|---|
| **Produces** | Three sub-scores (0 to 100) plus a weighted composite, and a ranked action list |
| **Default weights** | Foundations 0.30 · Answer Engine 0.20 · Generative Citation 0.50 |
| **Hard gate** | Foundations below 50 stops the audit. Fix that first |
| **Minimum viable run** | 10 queries, 4 assistants, 20 pages sampled. Roughly two hours, no paid tooling |
| **Hands off to** | `sl-citation-content` for content gaps, `sl-entity-infrastructure` for identity gaps |

## Before starting

1. **Load [`CONTEXT.md`](../../CONTEXT.md)** and run `sl-search-surfaces` if it has not run.
2. **Collect the inputs below.** Do not start without the query list; it determines everything.

| Input | Required | Notes |
|---|---|---|
| Canonical entity name and aliases | Yes | Exactly how the brand should be named |
| Target query list | Yes | 10 to 30, informational and commercial-investigation intent |
| Competitor list | Yes | 3 to 10 named |
| Key page URLs | Yes | 20 for the content sample |
| YMYL status | Yes | Health, finance or legal raises the authorship bar |
| Measurement tooling | No | Manual fallback given at every step |

3. **Confirm the weight profile** before scoring. Changing it afterwards to flatter the result is
   the fastest way to make an audit worthless.

## Core framework: three dimensions

### A. Foundations (0 to 100) · default weight 0.30

Can the site be crawled, indexed and understood?

| Sub | Item | Points |
|---|---|---|
| A1 | Crawl and indexability, **in Google and in Bing** | 20 |
| A2 | Core Web Vitals on mobile | 15 |
| A3 | On-page hygiene: titles, headings, canonicals | 15 |
| A4 | Schema baseline: Organization, LocalBusiness, Article | 15 |
| A5 | Internal linking and architecture | 15 |
| A6 | International and RTL handling where applicable | 10 |
| A7 | Backlink health | 10 |

**A1 is where most sites quietly fail for GEO.** ChatGPT search runs on Bing. Teams check Google
Search Console and never open Bing Webmaster Tools, so a Bing indexing problem stays invisible while
a whole assistant cannot see them.

### B. Answer Engine (0 to 100) · default weight 0.20

| Sub | Item | Points |
|---|---|---|
| B1 | Snippet ownership on target queries | 30 |
| B2 | Content structured for extraction: question H2s, direct answer paragraphs, lists, tables | 25 |
| B3 | AEO schema coverage: FAQPage, HowTo, QAPage | 20 |
| B4 | People Also Ask coverage | 15 |
| B5 | Voice readiness | 10 |

### C. Generative Citation (0 to 100) · default weight 0.50

| Sub | Item | Points |
|---|---|---|
| C1 | LLM mention share against competitors, across assistants | 30 |
| C2 | Entity infrastructure: Wikidata, Wikipedia, `sameAs`, knowledge panel | 25 |
| C3 | Citation-worthy content, chunks an LLM can lift | 20 |
| C4 | E-E-A-T signals: bylines, credentials, `Person` schema, external recognition | 15 |
| C5 | Freshness: `dateModified` discipline, visible review dates, refresh cadence | 10 |

### Composite

```
Overall = (A x W_A) + (B x W_B) + (C x W_C)      where W_A + W_B + W_C = 1.0
```

| Profile | W_A | W_B | W_C | Use when |
|---|---|---|---|---|
| **Future-weighted** (default) | 0.30 | 0.20 | 0.50 | Mature site, AI-Overview-heavy queries |
| **Balanced** | 0.35 | 0.30 | 0.35 | Surface priority genuinely unclear |
| **Classic** | 0.50 | 0.30 | 0.20 | Broken foundations, defer GEO |

**Automatic override:** Foundations below 50 forces the Classic profile regardless of the default,
and the audit reports that it did so. The tool does not recommend GEO spend on a broken site.

## Workflow

### [Phase 1/7: Entity] Can the machine identify the subject?

- Wikidata entry, present and correctly linked
- Wikipedia article, where notability genuinely permits. **Do not advise creating one otherwise**
- `sameAs` in schema pointing at every official profile plus Wikidata
- Knowledge panel on a brand-name search
- Name, address and phone consistency across the open web

Feeds **C2**.

### [Phase 2/7: Schema] Depth beyond the baseline

- `Organization` or `LocalBusiness` on the homepage
- `Person` for named authors, with credentials, for every editorial page
- Offering-appropriate types for products or services
- `Article` plus author on all editorial content
- `dateModified` present, accurate and **visible to a human reader**, not only in markup

Feeds **A4**, **B3**, **C4**, **C5**.

### [Phase 3/7: Content] Sample 20 pages for citation-worthiness

Score each page against the five-element test from `sl-citation-content`:

1. Entity named explicitly, no pronouns
2. One definitive claim, not hedged
3. A number, date or proof the model can quote
4. An attributed source, inline
5. Standalone readability, no "as mentioned above"

Record the count of pages carrying at least one liftable chunk. Feeds **C3**.

### [Phase 4/7: Measure] Citation share across assistants

Run the query list through each assistant. Per query record: was the entity named, at what
position, which competitors were named, and which URL was cited.

**Free method:** test manually in ChatGPT search, Perplexity, Claude and Google AI Overviews.
Screenshot everything. An hour for ten queries.
**Tooled method:** DataForSEO `ai_opt_llm_ment_*`, Profound, or Otterly for continuous tracking.

Aggregate to **share of citation** per topic. Feeds **C1**.

> Do not aggregate assistants into a single number without saying so. Cited-domain overlap between
> ChatGPT, AI Overviews and Perplexity is low, around 11% `[Profound-Citations-2026]`, so a blended
> average hides exactly the platform-specific gap worth acting on.

### [Phase 5/7: AI Overview] Zero-click exposure

For each target query: does an AI Overview trigger, is the entity cited in it, and what is the
classic rank. Trigger rates run around a quarter of searches overall and roughly half in healthcare
`[Conductor-AEO-GEO-2026]`, and AI Overviews have been measured cutting clicks by 58%
`[Ahrefs-AIO-CTR-Feb2026]`.

**The high-value cell:** an AI Overview triggers, a competitor is cited, and the site ranks in the
top ten. Ranking is present, citation is not, so the gap is content or entity, not authority. These
are the cheapest wins in the whole audit.

### [Phase 6/7: Accuracy] What does the AI get wrong?

Ask each assistant directly about the brand. Log every factual error.

**Errors outrank optimization.** An assistant confidently stating something false is more damaging
than not being mentioned, and it needs correcting at the source the model is drawing from, not on
the site's own marketing pages.

### [Phase 7/7: Map] Gaps to actions

Sort every gap into one of three buckets, because the remedy differs entirely:

| Bucket | Symptom | Route to |
|---|---|---|
| **Identity** | The machine cannot tell who this is | `sl-entity-infrastructure` |
| **Content** | Identity fine, nothing liftable on the page | `sl-citation-content` |
| **Authority** | Both fine, still not cited | External citations, digital PR, co-citation. Slowest to move |

Rank by leverage, not effort. State effort separately.

## Best practices

- **Baseline before you change anything.** Without a starting citation share there is no way to show
  movement, and this work is slow enough that proof matters.
- **Re-measure monthly, not weekly.** The signal is noisy; weekly readings mostly measure sampling.
- **Keep the screenshots.** Assistant outputs are not reproducible. Undated evidence is not evidence.
- **Report per assistant as well as blended**, given how low the overlap is.
- **Say which numbers are vendor-published.** Much of the measurement research in this field comes
  from companies selling measurement.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Auditing GEO on a site failing Foundations | Cannot be cited if it cannot be crawled |
| One blended "AI visibility score" | Hides the platform-specific gap, which is the actionable part |
| Checking Google indexing only | ChatGPT search runs on Bing |
| Adjusting weights after seeing the score | Makes the audit unfalsifiable |
| Recommending a Wikipedia article for a non-notable brand | It gets deleted, and it burns credibility |
| Treating one prompt as a measurement | Assistants vary run to run. Sample, and record the date |
| Reporting citation share with no date | Meaningless within a quarter |
| Promising a citation-share target | Nobody controls these mechanisms |

## Output format

Deliver as a folder:

```
<YYYY-MM-DD>-geo-audit/
  score.md            three sub-scores, weights used, composite, profile and any auto-override
  citation-share.csv  per query, per assistant, per competitor
  entity-infra.md     Wikidata, schema, sameAs, knowledge panel current state
  findings.md         what is true today, with evidence
  priorities.md       ranked actions, each tagged identity / content / authority
  screenshots/        dated assistant outputs
```

### Handoff summary block

Every audit ends with this, so a downstream skill or human can pick it up cold:

```
AUDIT HANDOFF
Entity:        <canonical name>
Date:          <YYYY-MM-DD>
Profile:       <Future-weighted | Balanced | Classic>  (auto-override: yes/no)
Scores:        A:<0-100>  B:<0-100>  C:<0-100>  Composite:<0-100>
Citation share: <n>% across <k> queries x <m> assistants
Top gap:       <identity | content | authority>
Next skill:    <sl-citation-content | sl-entity-infrastructure>
Blocking:      <anything that stops work>
Figures dated: <validation date of any external statistic quoted>
```

## Questions to ask when the brief is thin

1. What ten questions should name you, in the words a real buyer would use?
2. Who gets named instead today, and are they genuinely comparable?
3. Where do you rank in classic search for those, right now?
4. Are you in the Bing index?
5. Who is the named, credentialed author on your key pages?
6. When did those pages last genuinely change, not just get a touched timestamp?
7. Is any of this YMYL?
8. Has anyone checked what the assistants currently say about you, correct or not?

## References

| Key | Resolution |
|---|---|
| `[Aggarwal-2023]` | Aggarwal et al. *GEO: Generative Engine Optimization*. https://arxiv.org/abs/2311.09735 |
| `[Conductor-AEO-GEO-2026]` | Conductor. *2026 AEO/GEO Benchmarks Report*, 21.9M searches. Vendor-published |
| `[Ahrefs-AIO-CTR-Feb2026]` | Ahrefs. *AI Overviews reduce clicks by 58%*, Feb 2026. Vendor-published |
| `[Profound-Citations-2026]` | Profound. AI platform citation patterns, cited-domain overlap across ChatGPT, AI Overviews and Perplexity. Vendor-published |

Full registry: [`references.md`](../../references.md). Scoring rationale:
[`research/scoring-rubric.md`](../../research/scoring-rubric.md).

## Related skills

- `sl-search-surfaces`, the model this audit assumes
- `sl-citation-content`, fixes content-bucket gaps
- `sl-entity-infrastructure`, fixes identity-bucket gaps
