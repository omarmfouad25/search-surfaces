---
title: "Short descriptive title"
file: kebab-case-filename-without-extension
surface: geo
tags: [three, to, six, tags]
last_validated: 2026-01-01
freshness: drift-watch
references_used: [Key-Year, Org-Topic-Year]
---

<!--
  COPY THIS FILE to start a new knowledge page. Delete these comments as you go.

  surface:    foundations | seo | aeo | geo | cross
  freshness:  stable      conceptual, unlikely to move          re-check annually
              drift-watch sound now, mechanism may shift        re-check quarterly
              volatile    platform numbers that move fast       re-check before quoting

  Set freshness honestly. It tells the reader how much to trust your numbers, and it is
  the single most useful field in the frontmatter.

  last_validated: the date YOU checked the sources. Do not copy a date forward without
  re-checking. Bumping it without verifying is worse than leaving it stale, because it
  launders an old claim as a fresh one.

  references_used: every citation key you cite in the body. validate.py cross-checks
  this against the body and warns on mismatches in either direction.

  Run `python3 validate.py` from the repo root before opening a PR.
-->

# Title

One or two sentences on what this covers and why it matters. Lead with the thing a reader would want
to know if they read nothing else.

## TL;DR

| | |
|---|---|
| **Key fact** | With a citation `[Key-Year]` |
| **Defining property** | What makes this different from the adjacent topic |
| **Verdict** | If the page is evaluating a tactic, say so here rather than at the end |

<!-- A table beats a prose intro. Readers scan. So do models. -->

## Core content

Three to eight `##` sections, each readable standalone. Someone should be able to link to one section
and have it make sense out of context, which is the same property this repository argues content
needs in order to be cited.

**Every number carries a key**, like this: adoption measured at 10.13% `[Key-Year]`.

**Reasoning is labelled.** When you are arguing rather than reporting, say so:

> **Inference:** this appears to follow from how retrieval behaves under conflicting sources, but it
> has not been measured directly.

That distinction is the whole quality bar. A reader must be able to tell in one glance whether a
sentence is a finding or an opinion.

## What is not known

List the open questions honestly. **A page that admits its gaps is more useful than one that papers
over them**, and it tells the next contributor exactly where to help.

<!-- If evaluating a tactic, state what would change your verdict. Make the page falsifiable. -->

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| The mistake a competent person would actually make | The mechanism, not just "it is bad" |

<!-- Anti-patterns are usually the most-read section. Write them last, from real mistakes. -->

## References

| Key | Resolution |
|---|---|
| `[Key-Year]` | Author or Org. Title, with sample size or method if published. URL. ⚠ Vendor if applicable |

Full registry: [`../../references.md`](../../references.md).

<!-- Adjust the relative path depth to match where your file sits. -->

## Related files

- [`sibling.md`](sibling.md), one line on why a reader would go there next
- Link **up** to the broader topic, **down** to specifics, and **sideways** to adjacent pages.
  Bi-directional linking is a convention here: if you link to a file, add a link back from it.
