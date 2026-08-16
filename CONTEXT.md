# CONTEXT: load this before running any skill in this repository

Last validated: 2026-05-21
Status: canonical context source. Every `sl-` skill checks this file first.

This is the hub. It carries the model, the vocabulary lock, the priority order and the working
rules that all four skills assume. A skill that runs without this loaded will still function, but
it will re-derive things that are already decided here, and it may use terminology inconsistently.

---

## 1. The model: three surfaces, one asset

A single page can earn attention three ways. They are not three disciplines, they are three doors
into the same asset.

| Surface | Goal | Won by | Measured in |
|---|---|---|---|
| **SEO** | Rank the page | Authority, relevance, crawl health, UX | Rank, clicks, CTR |
| **AEO** | Be the answer above the links | Clean Q&A structure, schema, concision | Snippet capture, voice readouts |
| **GEO** | Be the citation inside the AI reply | Evidence, freshness, entity clarity | Citation rate, mention share |

The index behind them differs, which matters operationally: SEO and AEO are Google's index, GEO
draws on Google **and Bing** (ChatGPT search runs on Bing) **and real-time retrieval**. A site
invisible to Bing is invisible to a large share of generative citation regardless of Google rank.

## 2. Vocabulary lock

**Three terms are used. Everything else is an alias.**

| Use | Do not use | Why |
|---|---|---|
| SEO | SXO | Pre-AI. UX is cross-cutting, not a discipline |
| AEO | AIO | Overloaded: a Google product name and an umbrella term at once |
| GEO | LLMO, GAIO | Synonyms for GEO. Prefer the term the original paper used `[Aggarwal-2023]` |

If a user or client uses "AIO" or "LLMO", **mirror their term in conversation** and write
deliverables in the locked vocabulary with a one-line glossary note. Do not correct them in public.

The full argument, including the strongest version of the case that all of this is just SEO with new
labels, is in [`research/the-alphabet-problem.md`](research/the-alphabet-problem.md). Read it before
defending the distinction to a skeptic, because the skeptic has real points.

## 3. Priority order

```
SEO first.  GEO next.  AEO last.
```

**Reasoning:** roughly half of AI citations still originate from pages already ranking in the top
ten, so ranking is the substrate rather than a parallel track. GEO precedes AEO because the answer
box is a subset of a shrinking classic SERP, while citation share is the surface that is growing.

**This is a judgement, not a measurement.** Flag it as such when asked. A reader weighting zero-click
data more heavily would put AEO second and would not be wrong. `sl-geo-audit` ships alternative
weight profiles precisely so this can be overridden per engagement.

**Hard gate:** a site failing Foundations does not get GEO advice. Score Foundations first. Below
50, fix that and stop. Recommending entity infrastructure to a site that cannot be crawled is
malpractice.

## 4. Citation discipline

This is the rule that makes the repository worth more than a blog post.

1. **Every numerical, statistical or research claim resolves to a citation key** in
   [`references.md`](references.md). Format `[Author-Year]` or `[Org-Topic-Year]`.
2. **Cite inline in prose**: `keyword stuffing costs about 9% visibility [Aggarwal-2023]`.
3. **Every skill and research file ends with a `## References` tail** enumerating each key used and
   resolving it.
4. **Unsourced reasoning is labelled inline** as `Inference:` so a reader can tell the difference
   between something measured and something argued.
5. **A vendor source is labelled as a vendor source.** Much of this field's published research comes
   from companies selling the remedy.

If a claim cannot be sourced and is not marked as inference, it does not ship.

## 5. Freshness policy

Every file carries `last_validated` and `freshness` in frontmatter.

| `freshness` | Meaning | Re-validate |
|---|---|---|
| `stable` | Conceptual or mechanism-level | Annually |
| `drift-watch` | Sound now, mechanism may shift | Quarterly |
| `volatile` | Platform numbers that move fast | Before quoting |

**Current figures were validated 2026-05-21.** Treat every `volatile` number as needing a re-check
before it reaches a client, a deck, or an audience. State the validation date whenever you present
one.

## 6. Working rules for any skill in this repo

- **Never blur the surfaces into "search optimization."** The distinction is the point.
- **Never promise citation.** The mechanisms are undocumented and change without notice. Talk in
  terms of eligibility and probability, never guarantees.
- **Lead with what overlaps.** A competent SEO already executes most of GEO. Saying so builds trust
  and costs nothing; pretending otherwise is the thing that made this field noisy.
- **Prefer the manual method when there is no budget.** Every measurement step in these skills has a
  free fallback. Tooling is an accelerant, not a prerequisite.
- **YMYL raises the bar.** Health, finance and legal content needs named authorship, credentials,
  `Person` schema and visible review dates before any of the rest matters.
- **Regulated claims stay conservative.** Never draft a medical, financial or legal claim the source
  does not support, even when a more definitive sentence would be more citable. Citation-worthiness
  never outranks accuracy.

## 7. Tooling assumed

None is required. Where a skill names a tool it also gives the manual path.

| Purpose | Tooling | Free fallback |
|---|---|---|
| LLM mention tracking | DataForSEO `ai_opt_*`, Profound, Otterly | Manual prompt testing, logged in a sheet |
| SERP and AI Overview capture | DataForSEO SERP | Manual search, screenshot |
| Schema validation | Schema.org validator, Google Rich Results Test | Same, both free |
| Crawl and Core Web Vitals | Screaming Frog, PageSpeed Insights | PageSpeed Insights, free |
| Index coverage | Google Search Console, Bing Webmaster Tools | Both free, and Bing is the one people skip |

## 8. The three layers

| Layer | Question it answers | Who maintains it |
|---|---|---|
| `knowledge/` | What is true about how these systems behave | **Open. Community-maintained** |
| `research/` | What follows from it, and what is arguable | One author's position, open to challenge |
| `skills/` | What to do about it, executably | Maintained, PRs welcome |

**Knowledge flows upward.** A finding lands in `knowledge/` first. If it changes what someone should
*do*, the skill is updated too and the change says so. A skill must never assert something the
knowledge base does not support.

**When running as an agent:** prefer `knowledge/` for "how does X behave", `research/` for "why do
you claim Y", and `skills/` for "do Z for me".

## 9. Related files

- [`README.md`](README.md), what this repository is and how to install it
- [`references.md`](references.md), the citation registry
- [`skills/sl-search-surfaces/SKILL.md`](skills/sl-search-surfaces/SKILL.md), the model as an invokable skill
- [`research/the-alphabet-problem.md`](research/the-alphabet-problem.md), terminology, and the skeptic's case
- [`research/aggarwal-2023-findings.md`](research/aggarwal-2023-findings.md), what the foundational study measured
- [`research/scoring-rubric.md`](research/scoring-rubric.md), the audit weights and their justification
