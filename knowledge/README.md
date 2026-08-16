---
title: "Knowledge base: the map"
file: README
surface: cross
tags: [index, map, navigation, contributing]
last_validated: 2026-05-21
freshness: stable
references_used: []
---

# Knowledge base

**This layer is open to the community.** The research layer is one person's argument; the knowledge
base is meant to outgrow that. If you know something here is wrong, incomplete, or has moved, the
repository wants your correction more than it wants your agreement.

The bar for a contribution is not credentials. **It is a source.**

## The map

```
00-foundations/     the model everything else assumes
01-platforms/       how each surface actually behaves
02-signals/         individual tactics, and whether they hold up
03-measurement/     how to know if any of it worked
```

| File | What it covers | Freshness |
|---|---|---|
| [`00-foundations/seo-vs-aeo-vs-geo.md`](00-foundations/seo-vs-aeo-vs-geo.md) | The matrix, where the surfaces overlap and where they genuinely diverge | `drift-watch` |
| [`01-platforms/ai-overviews.md`](01-platforms/ai-overviews.md) | Google. The mid-rank citation window, structural anatomy, click impact | `volatile` |
| [`01-platforms/chatgpt-search.md`](01-platforms/chatgpt-search.md) | Bing-indexed, Wikipedia-concentrated | `volatile` |
| [`01-platforms/perplexity.md`](01-platforms/perplexity.md) | Live retrieval, freshness-dominant, community-weighted | `volatile` |
| [`02-signals/llms-txt.md`](02-signals/llms-txt.md) | A worked example of evaluating a tactic before adopting it | `volatile` |
| [`03-measurement/mention-tracking.md`](03-measurement/mention-tracking.md) | Citation share, the free method and the tooled one | `drift-watch` |

## Reading order

**New to this:** the matrix, then whichever platform matters to you, then measurement.

**Here to act:** measurement first. Get a baseline before you change anything, because this work
moves slowly and without a starting point you cannot tell whether it worked.

**Here to argue:** [`../research/the-alphabet-problem.md`](../research/the-alphabet-problem.md),
which puts the case against this whole field before making the case for it.

## How the three layers relate

| Layer | Question | Changes |
|---|---|---|
| `knowledge/` | What is true about how these systems behave | Constantly. Community-maintained |
| `research/` | What follows from it, and what is arguable | Rarely. One author's position, open to challenge |
| `skills/` | What to do about it, as an executable procedure | When the knowledge changes |

**Knowledge flows upward.** A finding lands here first. If it changes what you should *do*, the skill
gets updated too, and the PR should say so.

## Contributing a file

1. Copy [`_TEMPLATE.md`](_TEMPLATE.md).
2. Fill the frontmatter honestly, especially `freshness`.
3. **Every number needs a citation key** resolving to [`../references.md`](../references.md). No key,
   no number. Reasoning without a source is fine but must be labelled `Inference:`.
4. End with a `## References` tail and a `## Related files` tail.
5. Run `python3 validate.py` from the repository root. It will tell you what is missing.

Keep files roughly 100 to 300 lines. If a file is growing past that, it is probably two files.

## The most valuable contribution

**A number here that is now wrong.**

Everything marked `volatile` decays fast, figures were last validated 2026-05-21, and the person who
notices a stale statistic is doing more for this repository than the person who writes a new page.
Open an issue with the current figure and its source. You do not need to write the fix.

## What is missing, if you want somewhere to start

Gaps that are real and currently unfilled:

- **Claude and Gemini citation behaviour.** Both are named throughout and neither has a platform
  file, because published measurement is thin. Even a careful manual study would be new.
- **Non-English and RTL search.** Nearly all published measurement is English. This is a genuine
  hole in the entire field, not just here.
- **AEO depth.** Featured snippets, People Also Ask and voice are referenced but not documented.
- **Regulated verticals.** How YMYL topics are handled differently, with evidence rather than
  assumption.
- **Anything with a negative result.** A tactic that did not work, measured, is worth more than
  another list of tactics that might.
