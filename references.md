# References: the citation registry

Last validated: 2026-05-21

Every numerical, statistical or research claim in this repository resolves to a key in the table
below. Files cite by key in prose, for example `−9% visibility [Aggarwal-2023]`, and each file ends
with a `## References` tail resolving the keys it used.

**Key format:** `[Author-Year]` for papers and individually authored work, `[Org-Topic-Year]` for
industry research and official documentation.

**★** marks the source treated as authoritative for that topic.

**⚠ Vendor** marks a source published by a company selling a product in the area it researched. Not
disqualifying, and often the only data available, but it should be visible to the reader. Much of
the published research in this field carries this flag, which is itself worth knowing.

---

## Registry

| Key | Author / Org | Title | URL | Date | Notes |
|---|---|---|---|---|---|
| `[Aggarwal-2023]` | Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande (Princeton, IIT Delhi) | GEO: Generative Engine Optimization. ~10,000-query controlled benchmark; nine tactics; coined the term | https://arxiv.org/abs/2311.09735 | 2023-11 | ★ Peer-reviewed. The only widely cited controlled study in the field |
| `[Ahrefs-AIO-CTR-Feb2026]` | Ahrefs | Update: AI Overviews reduce clicks by 58% (follow-up to an earlier 34.5% finding across 300K keywords) | https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/ | 2026-02 | ★ click impact · ⚠ Vendor · **volatile** |
| `[Conductor-AEO-GEO-2026]` | Conductor | 2026 AEO/GEO Benchmarks Report. 21.9M searches; ~25% AI Overview trigger rate overall, ~48% in healthcare | https://www.conductor.com/ | 2026 | ★ prevalence · ⚠ Vendor · **volatile** |
| `[Google-EEAT-Helpful]` | Google Search Central | Creating helpful, reliable, people-first content (E-E-A-T guidance) | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | continuously updated | ★ E-E-A-T. Primary platform documentation |
| `[Google-SchemaFAQ-HowTo]` | Google Search Central | FAQPage and HowTo structured data | https://developers.google.com/search/docs/appearance/structured-data/faqpage | continuously updated | Primary. Several rich result types deprecated 2023 to 2024 |
| `[HigherVisibility-SearchPref-2025]` | Higher Visibility | How People Search Today. 1,500 US consumers; 79.8% still prefer traditional engines for informational queries | https://www.highervisibility.com/seo/learn/how-people-search/ | 2025-02 | ★ search-behaviour split · ⚠ Vendor · **volatile** |
| `[LLMSTxt-Spec]` | llms.txt community | The llms.txt proposal and specification | https://llmstxt.org/ | proposal | Proposal status. **No confirmed major assistant requires it.** No evidence it drives citation |
| `[Profound-Citations-2026]` | Profound | AI platform citation patterns. Cited-domain overlap across ChatGPT, AI Overviews and Perplexity at roughly 11% | https://www.tryprofound.com/ | 2026 | ⚠ Vendor · **volatile** |

---

## How to extend this

1. Add the key alpha-sorted into the table above.
2. Record the **sample size or methodology** in the title cell where the source publishes one. A
   study that does not publish its sample size should be treated with suspicion in this field.
3. Flag `⚠ Vendor` whenever the publisher sells into the area they measured.
4. Mark `volatile` on any figure expected to move within a quarter.
5. Cite the key inline in the file that uses it, and resolve it in that file's `## References` tail.

## What does not get a key

Reasoning is not evidence. Anything argued rather than measured is labelled inline as `Inference:`
so a reader can tell the two apart. There are a small number of these across the repository, each
one marked, and each one is mine rather than a finding from a source.
