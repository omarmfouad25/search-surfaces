---
name: sl-entity-infrastructure
description: >-
  Make a brand machine-resolvable so AI assistants can identify it before deciding to cite it.
  Use when the user asks about Wikidata, knowledge panels, sameAs, entity SEO, llms.txt, allowing
  or blocking GPTBot and ClaudeBot, schema depth for AI search, why an assistant confuses their
  brand with another, or why ChatGPT cannot find them at all despite good Google rankings.
version: 1.0.0
when_to_use: >-
  When the gap is identity rather than content. Symptoms: the assistant has never heard of the
  brand, confuses it with a similarly named one, or states something false about it. Run before
  sl-citation-content, because rewriting pages for an entity the model cannot resolve does nothing.
triggers:
  en:
    - entity SEO
    - Wikidata for my brand
    - knowledge panel
    - sameAs schema
    - llms.txt
    - allow GPTBot ClaudeBot PerplexityBot
    - AI confuses our brand
    - ChatGPT does not know us
  ar:
    - تحسين الكيانات
    - الرسم البياني المعرفي
    - الذكاء الاصطناعي لا يعرف علامتنا التجارية
compatibility:
  - Claude Code
  - any runtime that reads SKILL.md frontmatter
metadata:
  author: Omar Fouad
  category: search
  tags: [geo, entity, schema, wikidata, llms-txt, crawlers, technical]
license: MIT
last_validated: 2026-05-21
freshness: volatile
references_used: [LLMSTxt-Spec, Google-EEAT-Helpful, Aggarwal-2023]
---

# Entity infrastructure

## TL;DR

| Layer | Question it answers | Effort | Impact |
|---|---|---|---|
| **Crawler access** | Is the assistant allowed in at all? | Minutes | Blocking. Nothing else matters if this fails |
| **Bing index** | Can ChatGPT search see the site? | Hours | Blocking for one whole assistant |
| **Schema depth** | Does the machine know what this is? | Days | High |
| **Entity graph** | Can it be disambiguated from similar names? | Weeks | High, and durable |
| **`llms.txt`** | Emerging convention, unproven | Minutes | Low. Do it last, claim nothing |

**Order matters.** Work top down. The first two are cheap and blocking; the fourth is slow and
compounding.

> **`freshness: volatile`.** Crawler user-agent names, `llms.txt` adoption and knowledge-panel
> behaviour all change without notice. Re-verify every user-agent string and every claim in this
> file against current platform documentation before acting on it.

## Before starting

1. **Load [`CONTEXT.md`](../../CONTEXT.md).**
2. **Confirm the symptom is identity, not content.** Ask the assistants directly: *"What is
   [brand]?"* Three distinct failures, three different remedies:

| Response | Failure | Fix |
|---|---|---|
| "I do not have information about that" | Not resolvable | This skill, layers 1 to 4 |
| Describes a **different** company with a similar name | Disambiguation | This skill, layer 4 first |
| Describes it correctly but never cites it | Not an identity problem | `sl-citation-content` |
| States something **false** | Source contamination | This skill, plus correction at the source |

3. **Establish notability honestly** before recommending anything Wikipedia-shaped.

## Core framework: five layers

### Layer 1 · Crawler access (blocking, minutes)

If `robots.txt` blocks the retrieval agent, nothing downstream matters. Check the live file and
confirm the intended posture for each named agent.

Agents to make an explicit decision about, rather than leave to a default:

| Agent | Belongs to | Typical purpose |
|---|---|---|
| `GPTBot` | OpenAI | Training and retrieval |
| `OAI-SearchBot` | OpenAI | Search retrieval |
| `ChatGPT-User` | OpenAI | User-initiated fetch |
| `ClaudeBot` | Anthropic | Crawling |
| `Claude-User` | Anthropic | User-initiated fetch |
| `PerplexityBot` | Perplexity | Search index |
| `Google-Extended` | Google | Gemini training, **separate from Googlebot** |
| `Bingbot` | Microsoft | Bing index, which ChatGPT search reads |

**Verify each string against current platform documentation before writing it into a live
`robots.txt`.** These names change, and this file is marked volatile for exactly this reason.

**The real trap:** `Google-Extended` is not `Googlebot`. Blocking it does not affect Google Search
ranking, and allowing it does not improve ranking. Teams block it for a training-data policy reason
and then wonder about Gemini visibility. That is a legitimate trade, but it should be a decision,
not an accident.

**Business decision, not a technical one:** allowing retrieval is how citation becomes possible.
Blocking is a defensible choice for a publisher whose content is the product. State the trade
plainly; do not quietly optimise for citation on behalf of someone who chose to block.

### Layer 2 · Bing index (blocking for one assistant, hours)

ChatGPT search runs on Bing. Verify in **Bing Webmaster Tools**, not Google Search Console. This is
the single most commonly skipped check in the whole discipline, because SEO teams have spent a
decade correctly ignoring Bing for ranking purposes and the habit carried into an era where it
gates an entire assistant.

- Site verified in Bing Webmaster Tools
- Sitemap submitted **there**, separately
- Index coverage compared against Google's, with gaps explained

### Layer 3 · Schema depth (days)

Baseline most sites already have:

- `Organization` or `LocalBusiness` on the homepage
- `Article` with `author` on editorial content
- `BreadcrumbList`

What actually moves entity resolution:

- **`sameAs` on `Organization`**, pointing to every official profile **plus Wikidata plus Wikipedia
  where they exist**. This is the single highest-value property for disambiguation and it is
  routinely left empty
- **`Person` schema for named authors**, with `jobTitle`, `alumniOf`, credentials, and `sameAs` to
  their own profiles. On YMYL this is a floor, not a nicety `[Google-EEAT-Helpful]`
- **Offering-appropriate types** for products or services
- **`dateModified`**, accurate and **visible to a human**, not markup only

Validate with the Schema.org validator and Google's Rich Results Test. Both free.

### Layer 4 · Entity graph (weeks, durable)

This is the layer that compounds, and the one most teams skip because it is slow.

**Wikidata.** The most tractable step. A structured, sourced item with correct properties
(`instance of`, `industry`, `founded by`, `official website`), linked from `sameAs`. Wikidata has a
notability bar but it is far lower than Wikipedia's, and it is a legitimate place to start.

**Wikipedia.** Only where genuine notability exists: substantial coverage in independent, reliable
sources that the brand did not place. **Do not create an article for a non-notable company.** It
gets deleted, the deletion is public and permanent, and it damages exactly the credibility the
exercise was meant to build. If notability is absent, the honest answer is "not yet, and here is
what would have to be true first".

**Consistency across the open web.** Name, address and phone identical everywhere. Same canonical
brand name. Conflicting facts across sources are what produce a confidently wrong assistant answer.

**Third-party corroboration.** Independent coverage, directory listings, and being cited by others
in the category. **Inference:** co-citation appears to matter more than self-description, since a
model that only ever sees a brand describing itself has one unverified source, while a model that
sees three independent sources describing it consistently has a resolvable entity. This is reasoning
from how retrieval works, not a measured finding, and it is labelled as such.

### Layer 5 · `llms.txt` (minutes, unproven)

A proposed convention: a markdown file at `/llms.txt` giving models a curated map of the site
`[LLMSTxt-Spec]`.

**Honest status: a proposal with real adoption among documentation sites, and no confirmed major
assistant that requires it.** There is no published evidence that it improves citation.

**Recommendation:** ship it if the site has structured documentation, because it costs fifteen
minutes and is genuinely useful to humans and agents reading the docs. **Do not sell it, do not
bill for it, and do not claim it drives citation.** It is the current example of a convention being
marketed ahead of its evidence, and treating it soberly is a credibility asset.

## Workflow

### [Phase 1/5: Access] Audit `robots.txt` and decide per agent
### [Phase 2/5: Index] Verify Bing coverage independently of Google
### [Phase 3/5: Identity] Ask four assistants "What is [brand]?" and log verbatim answers with dates
### [Phase 4/5: Build] Schema depth, then `sameAs`, then Wikidata, then corroboration
### [Phase 5/5: Re-test] Re-ask the same four questions after 30 and 90 days

Entity changes propagate slowly. **Do not re-measure at one week and conclude it did not work.**

## Best practices

- **Fix blocking layers before compounding ones.** A `robots.txt` line beats a Wikidata entry.
- **Log verbatim assistant answers with dates.** Outputs are not reproducible; this is your only
  evidence of movement.
- **Treat factual errors as urgent.** A confidently wrong assistant is worse than an absent one, and
  it is fixed at the contaminating source, not on the brand's own marketing pages.
- **Make crawler access an explicit business decision**, documented, with the trade stated.
- **Expect 30 to 90 days.** Set that expectation before starting, not when asked why nothing moved.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Creating a Wikipedia article for a non-notable brand | Deleted, publicly, and it costs credibility |
| Blocking `Google-Extended` and expecting Gemini visibility | That is the switch that controls it |
| Checking Google indexing only | ChatGPT search runs on Bing |
| Empty `sameAs` | The highest-value disambiguation property, routinely skipped |
| Selling `llms.txt` as a citation driver | No evidence supports it |
| `dateModified` in markup only, or touched without real change | Transparent, and it erodes trust |
| Re-measuring after a week | Entity propagation is slow. You will conclude the wrong thing |
| Copying user-agent strings from a blog post | They change. Use platform documentation |
| Building entity infrastructure for a site with no citable content | Necessary, not sufficient. Pair with `sl-citation-content` |

## Output format

```
ENTITY INFRASTRUCTURE REPORT
Entity:   <canonical name>   Date: <YYYY-MM-DD>

L1 Crawler access   [pass/fail]  <per-agent posture, and whether it was deliberate>
L2 Bing index       [pass/fail]  <coverage vs Google, gaps>
L3 Schema depth     [score/25]   <present, missing, invalid>
L4 Entity graph     [score/25]   <Wikidata, Wikipedia, sameAs, knowledge panel, NAP>
L5 llms.txt         [n/a]        <shipped or not; no claims attached>

RESOLUTION TEST  (verbatim, dated)
  ChatGPT:    "<answer>"
  Perplexity: "<answer>"
  Claude:     "<answer>"
  Gemini:     "<answer>"

FACTUAL ERRORS FOUND   <each error, the likely source, the correction route>   <- highest priority
BLOCKING              <what stops everything else>
ORDERED ACTIONS       <blocking first, then compounding, with realistic timelines>
RE-TEST DUE           <date, 30 and 90 days out>
```

## Questions to ask when the brief is thin

1. What is the exact canonical brand name, and what does it get confused with?
2. Has anyone opened Bing Webmaster Tools for this site?
3. Is there any independent coverage the brand did not place?
4. Who are the named humans, and what are their verifiable credentials?
5. Is there a deliberate policy on AI crawler access, or has nobody decided?
6. Has anyone asked the assistants what they currently say, and written it down?

## References

| Key | Resolution |
|---|---|
| `[LLMSTxt-Spec]` | llms.txt community proposal. https://llmstxt.org/ . Proposal status, adoption unconfirmed |
| `[Google-EEAT-Helpful]` | Google Search Central. *Creating helpful, reliable, people-first content*. https://developers.google.com/search/docs/fundamentals/creating-helpful-content |
| `[Aggarwal-2023]` | Aggarwal et al. *GEO: Generative Engine Optimization*. https://arxiv.org/abs/2311.09735 |

Full registry: [`references.md`](../../references.md).

## Related skills

- `sl-search-surfaces`, the model
- `sl-geo-audit`, scores this as dimension C2
- `sl-citation-content`, run after identity resolves
