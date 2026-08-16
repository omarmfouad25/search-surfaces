# References: the citation registry

Last validated: 2026-05-21

**This file is the quality bar of the whole project.** Every numerical, statistical or research
claim anywhere in this repository resolves to a key here. Files cite by key in prose, for example
`−9% visibility [Aggarwal-2023]`, and each file ends with a `## References` tail resolving the keys
it used. `validate.py` fails the build if a cited key is missing from this table.

**Key format:** `[Author-Year]` for papers and individually authored work, `[Org-Topic-Year]` for
industry research and official documentation.

| Marker | Meaning |
|---|---|
| ★ | Treated as authoritative for that topic |
| ⚠ Vendor | Published by a company selling into the area it measured. Not disqualifying, often the only data available, but the reader should see it |
| **volatile** | Expected to move within a quarter. Re-check before quoting |

**Most research in this field is vendor-published.** That is a fact about the field, not an attack
on any single source. Making it visible is the point.

---

## Registry

| Key | Author / Org | Title and method | URL | Date | Notes |
|---|---|---|---|---|---|
| `[Aggarwal-2023]` | Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande (Princeton, IIT Delhi) | GEO: Generative Engine Optimization. ~10,000-query controlled benchmark across nine tactics. Coined the term | https://arxiv.org/abs/2311.09735 | 2023-11 | ★ The only widely cited **controlled** study in the field |
| `[Ahrefs-AIO-CTR-2025]` | Ahrefs | AI Overviews reduce clicks by 34.5%, across 300K keywords | https://ahrefs.com/blog/ai-overviews-reduce-clicks/ | 2025-04 | ⚠ Vendor · superseded by the 2026 follow-up |
| `[Ahrefs-AIO-CTR-Feb2026]` | Ahrefs | Update: AI Overviews reduce clicks by 58%. Follow-up to the 34.5% finding | https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/ | 2026-02 | ★ click impact · ⚠ Vendor · **volatile** |
| `[BrightEdge-AIO-Feb2026]` | BrightEdge | AI Overview prevalence across nine industries. ~48% of tracked queries, +58% year on year | https://www.brightedge.com/ | 2026-02 | ⚠ Vendor · **volatile** · disagrees with Conductor, see below |
| `[Conductor-AEO-GEO-2026]` | Conductor | 2026 AEO/GEO Benchmarks Report. 21.9M searches; 25.11% AI Overview trigger rate, 48.75% in healthcare | https://www.conductor.com/ | 2026 | ★ prevalence, conservative method · ⚠ Vendor · **volatile** |
| `[Google-AIO-Launch-2024]` | Google | AI Overviews general launch, replacing Search Generative Experience labelling | https://blog.google/products/search/generative-ai-google-search-may-2024/ | 2024-05 | Primary |
| `[Google-EEAT-Helpful]` | Google Search Central | Creating helpful, reliable, people-first content. E-E-A-T guidance | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | continuously updated | ★ E-E-A-T · Primary |
| `[Google-SchemaFAQ-HowTo]` | Google Search Central | FAQPage and HowTo structured data | https://developers.google.com/search/docs/appearance/structured-data/faqpage | continuously updated | Primary · several rich result types deprecated 2023 to 2024 |
| `[HigherVisibility-SearchPref-2025]` | Higher Visibility | How People Search Today. 1,500 US consumers; 79.8% still prefer traditional engines for informational queries | https://www.highervisibility.com/seo/learn/how-people-search/ | 2025-02 | ★ behaviour split · ⚠ Vendor · **volatile** |
| `[LLMSTxt-Spec]` | llms.txt community | The llms.txt proposal and specification | https://llmstxt.org/ | proposal | Proposal status. No major assistant confirmed to require it |
| `[Profound-Citations-2026]` | Profound | AI platform citation patterns. Domain-level source shares across ChatGPT, AI Overviews and Perplexity; ~11% cited-domain overlap between platforms | https://www.tryprofound.com/ | 2026 | ★ cross-platform citation mix · ⚠ Vendor · **volatile** |
| `[Rankability-llmstxt-2026]` | Rankability, with SE Ranking | llms.txt adoption and impact study across ~300,000 domains. 10.13% adoption, no statistical correlation with citation frequency | https://www.rankability.com/ | 2026 | ★ llms.txt evidence · ⚠ Vendor · notable for publishing a **negative** result about a tactic vendors were selling |
| `[SurferSEO-AIO-2025]` | SurferSEO | Structural analysis of 405,576 AI Overviews. Length, source counts, list usage, rank correlation | https://surferseo.com/blog/ | 2025 | ★ AIO anatomy · ⚠ Vendor · largest published AIO structural sample |

---

## Where the sources disagree, and why that is left visible

**AI Overview trigger rate** is the clearest case, and the disagreement is not noise:

| Source | Rate | Method |
|---|---:|---|
| `[BrightEdge-AIO-Feb2026]` | ~48% | Tracked query set across nine industries |
| `[Conductor-AEO-GEO-2026]` | 25.11% | 21.9M searches |

Both are vendor-published, both are defensible, and they differ by roughly a factor of two because
they sample different query populations. **This repository does not average them into a single
comfortable number.** The honest statement is a range: 25% to 50% of US English queries depending on
vertical and query mix, trending up. Anyone quoting one precise figure here is not being careful.

## How to extend this

1. Add the key alpha-sorted into the table.
2. **Record the method or sample size** wherever the source publishes one. A study that will not say
   how big its sample was should be treated with suspicion in this field.
3. Flag `⚠ Vendor` whenever the publisher sells into the area it measured.
4. Mark `volatile` on anything expected to move within a quarter.
5. Cite the key inline, and resolve it in that file's `## References` tail.
6. Run `python3 validate.py`. It fails if a cited key does not resolve here.

## What does not get a key

Reasoning is not evidence. Anything argued rather than measured is labelled inline as `Inference:`
so a reader can tell the two apart at a glance. There are a small number across the repository, each
one marked.
