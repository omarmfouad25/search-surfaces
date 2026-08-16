# Changelog

## 1.1.0 · 2026-08-17

Renamed from `search-surfaces` to **`geo-lab`**, and opened the knowledge layer to the community.

**Added: `knowledge/`, the third layer**
- `00-foundations/seo-vs-aeo-vs-geo.md`, the matrix
- `01-platforms/ai-overviews.md`, `chatgpt-search.md`, `perplexity.md`
- `02-signals/llms-txt.md`, a worked example of evaluating a tactic before adopting it
- `03-measurement/mention-tracking.md`, citation share, free method and tooled
- `_TEMPLATE.md`, the contribution scaffold

**Added: community infrastructure**
- Issue templates for stale figures, platform changes and new pages
- Pull request template with the citation checklist
- Code of conduct. Fabricating a citation is the one immediate-removal offence

**Changed**
- `references.md` grew from 8 keys to 13, and now flags vendor-published sources explicitly and
  documents where two good sources disagree by a factor of two rather than averaging them
- `validate.py` extended to the knowledge layer, and **fixed a real bug**: it was parsing markdown
  links inside fenced code blocks as if they were real links, which would have failed every
  contributor whose page included a code example

## 1.0.0 · 2026-08-17

First release. Four skills, three research files, one citation registry.

**Skills**
- `sl-search-surfaces`, the hub: three-surface model, vocabulary lock, priority order
- `sl-geo-audit`, scored audit across Foundations, Answer Engine and Generative Citation
- `sl-citation-content`, the five-element citation pattern and the Aggarwal tactic evidence
- `sl-entity-infrastructure`, five layers from crawler access to entity graph

**Research**
- `the-alphabet-problem.md`, which acronyms are real, with the skeptic's case argued first
- `aggarwal-2023-findings.md`, what the foundational study measured, including the caveats the
  secondary coverage drops
- `scoring-rubric.md`, audit weights and the counter-argument against them

**Notes on this release**
- All figures were last validated 2026-05-21. Anything marked `volatile` should be re-checked before
  being quoted. See the freshness policy in `README.md`.
- `sl-entity-infrastructure` is marked `volatile` in full: crawler user-agent names and `llms.txt`
  adoption change without notice.
