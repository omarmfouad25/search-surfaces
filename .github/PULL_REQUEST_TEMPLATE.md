## What this changes

One or two sentences.

## Type

- [ ] Corrects a stale or wrong figure
- [ ] Documents a platform behaviour change
- [ ] New knowledge page
- [ ] Updates a skill
- [ ] Challenges a conclusion in `research/`
- [ ] Docs, typos, links

## The checks

- [ ] **`python3 validate.py` passes.** It checks citation keys, links, frontmatter, required
      sections and em dashes. CI runs the same thing
- [ ] **Every new number has a citation key** resolving to `references.md`
- [ ] **Any new source is flagged `⚠ Vendor`** if the publisher sells into the area it measured
- [ ] **Reasoning is labelled `Inference:`** rather than presented as a finding
- [ ] **`last_validated` reflects a date I actually re-checked the sources**, not a copied-forward one
- [ ] **`freshness` is set honestly**
- [ ] No em dashes

## If this changes a knowledge page

Does it change what someone should *do*? If so, which skill needs updating, and did you update it?

## Sources

List them, with dates and sample sizes where published.

---

*The bar here is a source, not credentials. A one-line PR fixing a stale number is exactly as
welcome as a new page.*
