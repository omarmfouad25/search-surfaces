---
title: "llms.txt: the honest assessment"
file: llms-txt
surface: geo
tags: [llms-txt, signals, skepticism, evidence, hype]
last_validated: 2026-05-21
freshness: volatile
references_used: [LLMSTxt-Spec, Rankability-llmstxt-2026]
---

# llms.txt

A proposed convention: a markdown file at `/llms.txt` giving AI crawlers a curated map of a site,
by analogy with `robots.txt` `[LLMSTxt-Spec]`.

**The honest position: it has not earned its hype.** This file exists partly as a worked example of
how to evaluate a tactic before adopting it, because the pattern here will repeat with the next
proposed standard.

## TL;DR

| | |
|---|---|
| **Status** | Community proposal. Not ratified by any major model operator |
| **Adoption** | ~10.13% of ~300,000 domains studied `[Rankability-llmstxt-2026]` |
| **Measured effect on citation** | **None.** No statistical correlation found `[Rankability-llmstxt-2026]` |
| **Cost to ship** | About fifteen minutes |
| **Verdict** | Ship it if you have real docs. **Do not sell it. Do not claim it drives citation** |

## What it looks like

```markdown
# Brand Name

> One-line description of what this site covers.

## Docs
- [About](/about): what the organisation does
- [Products](/products): the catalogue
- [Blog](/blog): editorial

## Optional
- [Press](/press): media coverage
```

The intent is reasonable: give a retrieval agent a curated index optimised for machines instead of
making it infer structure from navigation built for humans.

## What the evidence says

From a study across roughly 300,000 domains `[Rankability-llmstxt-2026]`:

| Finding | Result |
|---|---|
| Adoption rate | 10.13% |
| Correlation between presence and citation frequency | **None found** |
| Machine-learning analysis of citation likelihood | **No measurable effect** |
| Crawler behaviour | Major crawlers do not fetch it as part of routine indexing |
| Adoption by sector | Concentrated in SaaS, publishing and developer tooling. Under 10% in finance, healthcare and legal |
| Adoption by traffic tier | Higher among medium and low traffic sites than among authoritative ones |

That last row is quietly the most telling. **The sites that most need citation adopt it most, and
the sites that already get cited do not bother.** That is the signature of a tactic being sold to
the anxious rather than one that works.

## Why the hype outran the evidence

Three forces, all of which will recur with the next proposal:

1. **A satisfying analogy.** "AI search needs its own robots.txt" is intuitive, memorable and easy
   to repeat, which is not the same as being true.
2. **It is trivially easy to sell.** Generators shipped fast because the deliverable is cheap to
   produce and impossible to disprove in the short term.
3. **Genuine confusion with structured data.** Many practitioners conflated it with schema markup,
   which does have an evidenced role in eligibility. The confusion transferred schema's credibility
   onto an unrelated file.

## When it is still worth doing

Not zero. Two cases:

- **You have real, structured documentation.** A curated map is genuinely useful to humans and to
  agents reading your docs, independent of any citation claim. Developer-tool and API sites get real
  value here.
- **It costs fifteen minutes and cannot hurt.** As hygiene, fine. As strategy, no.

**What is not acceptable:** billing for it, listing it as a GEO deliverable, or implying it drives
citation. There is no evidence for that, and one vendor publishing the negative result
`[Rankability-llmstxt-2026]` deserves credit for it.

## The transferable lesson

This is the template for evaluating the next proposed standard:

1. **Has any major operator committed to reading it?** Not "can it be read", but is it fetched as
   routine behaviour.
2. **Is there a study with a real sample and a published method?**
3. **Who is promoting it, and do they sell the remedy?**
4. **Who is adopting it?** If adoption concentrates among sites that need visibility rather than
   sites that have it, that is a signal about marketing, not efficacy.
5. **What is the cost of being wrong?** Fifteen minutes, ship it. A retainer line item, do not.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Selling `llms.txt` as a citation driver | No measured correlation |
| Listing it as a GEO deliverable | Value-padding |
| Confusing it with schema markup | Different mechanism, different evidence base |
| Skipping schema because you shipped `llms.txt` | You swapped the evidenced thing for the unevidenced one |
| Assuming the study settles it forever | Marked `volatile`. If an operator commits to fetching it, this file needs rewriting |

## What would change this verdict

State the falsifier up front, so this file can be corrected rather than defended:

- A major model operator documenting that it fetches `/llms.txt` during routine indexing
- A study with a published method finding a real correlation with citation, controlling for the
  obvious confound that sites bothering with it also tend to do other things well

**If you can point to either, open an issue.** That is a contribution this repository wants.

## References

| Key | Resolution |
|---|---|
| `[LLMSTxt-Spec]` | llms.txt community proposal. https://llmstxt.org/ . Proposal status |
| `[Rankability-llmstxt-2026]` | Rankability with SE Ranking. Adoption and impact across ~300,000 domains. ⚠ Vendor, publishing a negative result about a tactic vendors sell |

Full registry: [`../../references.md`](../../references.md).

## Related files

- [`../01-platforms/chatgpt-search.md`](../01-platforms/chatgpt-search.md), where the real levers are
- [`../../skills/sl-entity-infrastructure/SKILL.md`](../../skills/sl-entity-infrastructure/SKILL.md), llms.txt as layer 5 of 5, deliberately last
