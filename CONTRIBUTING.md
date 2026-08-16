# Contributing

**The knowledge base is open.** The research layer is one person's argument and the skills are
maintained, but `knowledge/` is meant to outgrow its author.

**The bar is a source, not credentials.** Nobody here cares where you work. They care whether the
number resolves.

Start from [`knowledge/_TEMPLATE.md`](knowledge/_TEMPLATE.md) for a new page. Use the issue
templates for anything smaller, including the one for reporting a stale figure, which needs no PR
at all.

## The one rule that matters

**Every number needs a source.** If you add a quantitative claim, add its citation key to
[`references.md`](references.md) and cite it inline. If the claim is reasoning rather than
measurement, label it `Inference:` so a reader can tell the difference.

A pull request that adds an unsourced statistic will be asked for the source. That is the whole
point of the repository.

## Especially welcome

- **A number that is now wrong.** This field moves quarterly and staleness is the main failure mode
  here. Open an issue with the current figure and its source, even if you do not want to write a PR.
- **A primary source replacing a vendor one.** Several entries are vendor-published because nothing
  better exists. If you know of independent research on the same question, that is a real upgrade.
- **A tactic that measurably did or did not work**, with enough method that someone could repeat it.
- **Platform behaviour changes**, particularly crawler user-agent names and `llms.txt` adoption.
  `sl-entity-infrastructure` is marked `volatile` for this reason.
- **A disagreement with the priority order**, argued. It is a judgement call and it is stated as
  one.

## Less welcome

- **More acronyms.** The repository argues that most of them are aliases. Adding one needs an
  argument for why it names something the existing three do not.
- **Skill splitting.** Four coherent skills beat forty atomic ones. New capability should extend an
  existing skill unless it genuinely does not fit any of them.
- **Tool promotion.** Naming a tool is fine where it does a job. Every tooled step must keep its
  free manual fallback.
- **Guarantees.** No copy in this repository promises citation, and none should. The mechanisms are
  undocumented and change without notice.

## Conventions

- **kebab-case** filenames, everywhere.
- **`sl-` prefix** on every skill, to avoid collisions with other skill collections loaded
  alongside this one.
- **Frontmatter is required** on every skill and research file: `name` or `title`, `description`,
  `version`, `last_validated`, `freshness`, `references_used`.
- **Skill body order:** TL;DR → Before starting → Core framework → Workflow (numbered phases) →
  Best practices → Anti-patterns → Output format → Questions → References → Related skills.
- **`freshness`** is one of `stable`, `drift-watch` or `volatile`. Set it honestly; it tells the
  reader how much to trust the file's numbers.
- **Update `last_validated`** only when you have actually re-checked the sources. Bumping the date
  without re-verifying is worse than leaving it stale, because it launders an old claim as new.
- **No em dashes.** Use a colon for an explanation, a comma or brackets for an aside, a full stop to
  split clauses, or a middot in a header.

## Before you open a pull request

```bash
python3 validate.py
```

It fails on an unresolved citation key, a broken internal link, a missing skill section or
frontmatter field, an invalid `freshness` value, or an em dash. CI runs the same check, so a PR that
fails locally will fail there too.

## Testing a skill change

The validator checks structure, not judgement. For the judgement part:

1. Load the skill in Claude Code and invoke it on a real site you know well.
2. Check the output matches the declared output format.
3. Check every number in the output resolves to a source.
4. Confirm the anti-patterns section would have caught the mistake you were most tempted to make.

## Licensing

MIT. By contributing you agree your contribution ships under the same terms.
