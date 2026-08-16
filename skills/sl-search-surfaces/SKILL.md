---
name: sl-search-surfaces
description: >-
  Load the three-surface model of search before doing any SEO, AEO or GEO work. Use when the user
  asks about generative engine optimization, AI search visibility, getting cited by ChatGPT or
  Perplexity, AI Overviews, answer engine optimization, featured snippets, LLM SEO, "how do I show
  up in AI answers", or asks what GEO, AEO, AIO or LLMO actually mean and whether the distinction
  is real. This is the hub skill: run it first, then hand off to the specialist skill.
version: 1.0.0
when_to_use: >-
  First, before sl-geo-audit, sl-citation-content or sl-entity-infrastructure. Also standalone when
  the question is conceptual ("is GEO real?", "what is the difference between AEO and GEO?") rather
  than a request to audit or write something.
triggers:
  en:
    - generative engine optimization
    - GEO / AEO / AIO / LLMO
    - get cited by AI
    - AI search visibility
    - show up in ChatGPT answers
    - AI Overviews optimization
    - answer engine optimization
    - is GEO just SEO
  ar:
    - تحسين محركات الإجابة
    - الظهور في نتائج الذكاء الاصطناعي
    - الاستشهاد في إجابات الذكاء الاصطناعي
compatibility:
  - Claude Code
  - any runtime that reads SKILL.md frontmatter
metadata:
  author: Omar Fouad
  category: search
  tags: [seo, aeo, geo, ai-search, hub, terminology]
license: MIT
last_validated: 2026-05-21
freshness: stable
references_used: [Aggarwal-2023, HigherVisibility-SearchPref-2025, Conductor-AEO-GEO-2026, Ahrefs-AIO-CTR-Feb2026]
---

# Search surfaces: the model

## TL;DR

| | SEO | AEO | GEO |
|---|---|---|---|
| **Goal** | Rank the page | Be the answer above the links | Be the citation inside the reply |
| **Surface** | Classic SERP | Snippets, People Also Ask, voice | AI Overviews, ChatGPT, Perplexity, Claude |
| **Primary lever** | Authority and relevance | Q&A structure and schema | Evidence, freshness, entity clarity |
| **Key metric** | Rank, clicks, CTR | Snippet presence | Citation rate, mention share |
| **Index** | Google | Google | Google + Bing + real-time retrieval |
| **Priority** | 1st | 3rd | 2nd |

**One asset, three doors.** Do not treat them as three disciplines with three budgets.

## Before starting

1. **Load [`CONTEXT.md`](../../CONTEXT.md)** from the repository root. It carries the vocabulary
   lock, the citation discipline and the freshness policy this skill assumes.
2. **Establish which surface the user actually cares about.** Most people say "AI SEO" and mean one
   specific thing: usually GEO. Ask before proceeding if it is ambiguous.
3. **Check whether the question is conceptual or operational.** Conceptual questions end here.
   Operational ones hand off in Phase 4.

## Core principles

**1. The surfaces are real, the disciplines mostly are not.** A senior SEO doing topical depth,
clean structure, schema and accurate FAQs is already executing most of GEO. Say this out loud. It
is true, it builds trust, and pretending otherwise is what made this field noisy.

**2. What genuinely changed is measurement, not craft.** SEO measures rank. AEO measures snippet
presence. GEO measures citation share inside a synthesized answer. Different instruments, different
gaps, different reporting. That is why the vocabulary earns its keep, and it is the only reason.

**3. Keyword stuffing inverts.** The one tactic that historically worked in moderation for SEO is
actively harmful in generative engines, at roughly −9% visibility against doing nothing
`[Aggarwal-2023]`. This is the single largest divergence between the surfaces.

**4. Substance beats style.** In the same study the four substance tactics (adding quotations,
adding statistics, citing sources, improving fluency) all cleared +28%, while tone and vocabulary
tactics clustered between +6% and +18% `[Aggarwal-2023]`. Evidence outranks authoritative voice.

**5. Classic search is still the majority surface.** Around 79.8% of surveyed US consumers still
preferred traditional engines for informational queries `[HigherVisibility-SearchPref-2025]`. GEO is
the growth surface, not the current volume surface. Anyone selling GEO as a replacement for SEO is
selling something.

## Workflow

### [Phase 1/4: Frame] Name the surfaces and kill the aliases

Three terms are used: **SEO, AEO, GEO**. AIO, LLMO, GAIO and SXO are aliases or product names.

Mirror the user's own term in conversation, write deliverables in the locked vocabulary, and add a
one-line glossary note. Do not correct anyone publicly over an acronym.

### [Phase 2/4: Locate] Work out where the user actually is

| Symptom | Surface at fault |
|---|---|
| "We do not rank at all" | SEO. Stop here, fix this first |
| "We rank but traffic is falling" | Zero-click erosion. AEO plus GEO |
| "We rank and the AI still never mentions us" | GEO, almost always entity infrastructure or citation-worthiness |
| "A competitor is always named and we are not" | GEO, citation share |
| "The AI says something wrong about us" | GEO, and it is urgent. Correct at source |

### [Phase 3/4: Order] Apply the priority, and say it is a judgement

```
SEO first.  GEO next.  AEO last.
```

Because roughly half of AI citations still originate from pages ranking in the top ten, ranking is
the substrate rather than a parallel track. GEO precedes AEO because the answer box is a subset of
a shrinking classic SERP while citation share is growing.

**Present this as a judgement call, not a finding.** Someone weighting zero-click data more heavily
would put AEO second and would have a case: AI Overviews have been measured reducing clicks by 58%
`[Ahrefs-AIO-CTR-Feb2026]`, and trigger on roughly a quarter of searches overall, rising to about
half in healthcare `[Conductor-AEO-GEO-2026]`.

**Hard gate:** if Foundations score below 50, GEO advice is withheld until that is fixed.

### [Phase 4/4: Hand off] Route to the specialist skill

| Need | Skill |
|---|---|
| Measure the current state, score it, rank the gaps | `sl-geo-audit` |
| Rewrite content so an LLM will lift it | `sl-citation-content` |
| Fix the entity graph, schema, crawler access | `sl-entity-infrastructure` |

## Best practices

- **Lead with the overlap.** "Most of this is SEO you already know" is the honest opening and the
  one that earns the rest of the conversation.
- **Quantify the surface split** before recommending investment, so the user is not moving budget
  from the majority surface to the growth surface on vibes.
- **Give the free method.** Manual prompt testing across four assistants costs an hour and answers
  most first questions.
- **Date every number you present.** Say "as of May 2026" out loud.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Selling GEO as a separate discipline with a separate retainer | Most of the work is shared with SEO. It is value-padding unless the deliverable includes real cross-LLM tracking and entity rebuild |
| "Optimize for AI" as an instruction | Means nothing operationally. Name the surface and the metric |
| Recommending GEO on a site with broken foundations | Cannot be cited if it cannot be crawled or ranked |
| Promising citation | Undocumented mechanisms, no guarantees exist. Talk in eligibility and probability |
| Treating AI Overviews and ChatGPT as one surface | Different indexes, different citation behaviour, low overlap in cited domains |
| Quoting a 2025 statistic in 2026 without re-checking | Several headline figures in this field have already doubled once |

## Output format

When this skill runs standalone, return:

1. **Surface diagnosis**, which of the three is actually at fault, with the symptom that shows it
2. **The overlap statement**, what the user is already doing that counts
3. **Priority order for their case**, with any deviation from the default explained
4. **Handoff**, the named next skill and why
5. **Freshness note**, the validation date of any figure quoted

## Questions to ask when the brief is thin

1. What do you type into an AI assistant where you would expect to be named?
2. Which competitors get named instead?
3. Do you rank in the top ten for those topics in classic search today?
4. Is the site in the **Bing** index? (Most people have never checked, and ChatGPT search runs on it)
5. Is there a named author with credentials on your key pages?
6. Is this a YMYL topic (health, finance, legal)? If so the bar for authorship and sourcing rises.

## References

| Key | Resolution |
|---|---|
| `[Aggarwal-2023]` | Aggarwal et al., Princeton and IIT Delhi. *GEO: Generative Engine Optimization*. https://arxiv.org/abs/2311.09735 |
| `[HigherVisibility-SearchPref-2025]` | Higher Visibility. *How People Search Today*, 1,500 US consumers, Feb 2025. Vendor-published survey |
| `[Conductor-AEO-GEO-2026]` | Conductor. *2026 AEO/GEO Benchmarks Report*, 21.9M searches. Vendor-published |
| `[Ahrefs-AIO-CTR-Feb2026]` | Ahrefs. *AI Overviews reduce clicks by 58%*, follow-up study, Feb 2026. Vendor-published |

Full registry: [`references.md`](../../references.md).

## Related skills

- `sl-geo-audit`, measure and score the current state
- `sl-citation-content`, write what LLMs lift
- `sl-entity-infrastructure`, make the machine able to identify you
- [`research/the-alphabet-problem.md`](../../research/the-alphabet-problem.md), the terminology argument in full
