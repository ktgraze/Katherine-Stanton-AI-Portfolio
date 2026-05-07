# HALO — Domain-Specific RAG Marketing Assistant for Hairstylists 💇‍♀️

**Course:** ITAI2377 — Data Science in AI  
**Group:** Icarus Squad  
**Team Members:** Oyinade Balogun · Francisco Medina Diaz · Rodrigo Sierra · **Katherine Stanton**

---

## Problem Statement

Independent hairstylists and small salon owners are skilled professionals who struggle with the marketing side of running a business. They know their craft but lack experience with social media content creation, campaign planning, interpreting analytics, client retention messaging, and communicating their competitive positioning. Generic AI tools do not understand the language, seasonal rhythms, or platform dynamics of the beauty industry.

HALO (Hair And Lifestyle Operations) is a domain-specific Retrieval-Augmented Generation system designed to give independent hairstylists access to practical, beauty-industry-specific marketing guidance in plain language — without requiring any marketing expertise.

HALO addresses five core capabilities:
1. Social media content creation (Instagram, TikTok, Facebook)
2. Seasonal and holiday campaign planning
3. Marketing metrics explained in plain English
4. Client follow-up and rebooking messages
5. Competitive positioning and personal branding

---

## Approach and Methodology

### Architecture

HALO is built on a Retrieval-Augmented Generation (RAG) pipeline — a two-stage architecture that retrieves relevant knowledge before generating a response. This ensures responses are grounded in curated, domain-specific content rather than general AI knowledge, which reduces hallucination and improves relevance for a specialized domain.

```
User Query
    ↓
Sentence Embedding (all-MiniLM-L6-v2)
    ↓
ChromaDB Vector Search (cosine similarity)
    ↓
Top-5 Chunk Retrieval with Metadata Filtering
    ↓
Prompt Assembly with Retrieved Context
    ↓
LLM Response Generation (Groq / Llama 3.3 70B)
    ↓
HALO Response
```

### Data Collection (Notebook 1)

The knowledge base was built from three source types:

- **Scraped articles (71.6% of chunks):** 42 articles collected automatically using `trafilatura` and `BeautifulSoup` from sources including Hootsuite Blog, Sprout Social, Later, and beauty industry publications such as American Salon, Modern Salon, and Salon Today
- **Synthetic content (21.7% of chunks):** 60 files generated using the Groq API (Llama 3.3 70B) covering topics not sufficiently represented in scraped sources, including TikTok-specific guides, seasonal marketing content, and client retention templates
- **Manual files (6.7% of chunks):** 13 files uploaded directly by team members from curated beauty industry sources

**Final knowledge base:** 667 chunks across 115 source files, approximately 209,000 words total

### Preprocessing Pipeline

1. **Text cleaning:** URL removal, emoji stripping, hashtag symbol removal, whitespace normalization — with a protected vocabulary list of 60+ beauty industry terms (balayage, keratin, co-wash, locs, etc.) preserved from normalization
2. **Chunking:** 400-word target chunks with 50-word overlap to preserve context across boundaries
3. **Feature engineering (5 metadata features per chunk):**
   - `platform_tag` — Instagram, TikTok, Facebook, Pinterest, Google Business, or general
   - `season_tag` — Spring, Summer, Fall, Winter, or year-round
   - `content_type_tag` — Promotional, Educational, Engagement, or Retention
   - `domain_relevance_score` — 0–1 score measuring beauty-industry specificity
   - `length_label` — Short, Medium, or Long
4. **Embedding generation:** `all-MiniLM-L6-v2` sentence transformer model (384-dimensional vectors)
5. **Vector storage:** ChromaDB with cosine similarity distance metric, persisted to Google Drive

### RAG Pipeline (Notebook 2)

- **Retrieval:** Three-tier fallback strategy — attempts both platform and content type filters together, falls back to a single filter, then falls back to unfiltered search — guaranteeing every query returns chunks
- **Prompt assembly:** Retrieved chunks are labeled with source, content type, and platform metadata before being assembled into a structured prompt
- **Generation:** Llama 3.3 70B via Groq API with a carefully engineered system prompt defining HALO's persona, behavioral rules, and domain scope
- **Logging:** Every query, retrieval event, response, and feedback rating is persisted to CSV on Google Drive

### Frontend Interface (Notebook 3)

A polished Gradio interface built with `gr.Blocks` featuring:
- Editorial beauty industry branding (Playfair Display + DM Sans typography, warm cream and gold color palette)
- Five quick-prompt buttons (one per HALO capability) for easy demo access
- Platform and content type filter dropdowns
- Thumbs up / thumbs down feedback collection saved to Google Drive

### Technical Stack

| Component | Technology |
|---|---|
| Embedding model | `all-MiniLM-L6-v2` (Sentence Transformers) |
| Vector database | ChromaDB (local, persisted to Google Drive) |
| LLM | Llama 3.3 70B via Groq API |
| Web scraping | trafilatura + BeautifulSoup |
| Frontend | Gradio (gr.Blocks) |
| Storage | Google Drive |
| Development environment | Google Colab |

---

## Results and Evaluation

### Knowledge Base Quality

| Metric | Value |
|---|---|
| Total chunks | 667 |
| Total source files | 115 |
| Average chunk size | 371 words |
| Average similarity score (sanity check) | 0.5948 |
| Domain relevance mean | 0.247 |

### 20-Question Evaluation Suite

Responses were evaluated across all five HALO capabilities using a 3-point manual scoring scale:
- `2` = Fully useful — directly addresses the request with specific, actionable content
- `1` = Partially useful — related but vague, incomplete, or needs editing
- `0` = Not useful — off-topic, generic, or failed (API error)

| Score | Count | Percentage |
|---|---|---|
| 2 — Fully useful | 13 | 65% |
| 1 — Partially useful | 5 | 25% |
| 0 — Not useful / Error | 2 | 10% |

**Overall Relevance Rate (score ≥ 1): 90%** — exceeds the 80% minimum threshold defined in the project plan

Note: Both score-0 responses were caused by API rate limiting during the evaluation run, not by model quality issues. HALO's actual content quality across all 18 successfully generated responses was consistently relevant to hairstylist marketing needs.

### Response Time

- Only 1 of 20 responses fell under the 5-second target (Q16 at 1.12 seconds)
- Most responses ranged from 7–20 seconds, primarily due to the large context window sent with each prompt
- Response time is identified as a key area for future optimization

### Strengths

- Campaign planning and competitive positioning responses were consistently strong and actionable
- Client retention message templates were warm, personal, and immediately usable
- The three-tier fallback retrieval strategy ensured HALO always returned a response, even when metadata filters returned no matching chunks

### Limitations

- Domain relevance scores were lower than expected (mean 0.247) because most scraped sources are general marketing sites rather than beauty-specific publications — despite efforts to include American Salon, Modern Salon, and Salon Today
- Response times exceeded the 5-second target for most queries due to large prompt sizes
- Some responses still referenced "excerpts" despite system prompt instructions, indicating prompt engineering requires further iteration
- The model occasionally retrieved non-beauty-specific chunks when filtered searches returned no results

---

## Learning Outcomes

**RAG Architecture Design**  
Building HALO from scratch provided hands-on experience with every component of a RAG pipeline — from document collection and chunking strategy to embedding generation, vector storage, and prompt engineering. Understanding how retrieval quality directly impacts generation quality was one of the most concrete technical lessons of the project.

**Data Engineering at Scale**  
Designing and implementing a preprocessing pipeline that handles three source types (scraped, synthetic, manual) with consistent quality metrics reinforced the importance of data quality over data quantity. The protected vocabulary approach to preserve domain-specific terminology was a novel solution to a real NLP preprocessing challenge.

**Feature Engineering for Retrieval**  
Designing the five metadata features (platform tag, season tag, content type tag, domain relevance score, length label) and implementing the three-tier fallback retrieval strategy demonstrated how structured metadata can dramatically improve the relevance of vector search results beyond raw similarity scores.

**Prompt Engineering**  
Iterating on the HALO system prompt across multiple versions — adding behavioral constraints, removing excerpt references, adjusting tone instructions — provided practical experience with how prompt design shapes model behavior in ways that code changes alone cannot.

**Collaborative Development Workflow**  
Managing a multi-notebook shared codebase across four team members using Google Colab and Google Drive highlighted the challenges of collaborative AI development — including session management, API key security, token limit coordination, and version control without traditional Git workflows.

**API Integration and Rate Limit Management**  
Working through Groq and Gemini API rate limits in real time during evaluation runs provided practical experience with production constraints that are rarely covered in coursework but are universally encountered in applied AI development.

---

## Requirements and Dependencies

### Python Libraries

```
chromadb
sentence-transformers
nltk
spacy
en_core_web_sm (spaCy model)
langchain
langchain-community
matplotlib
seaborn
pandas
numpy
tqdm
groq
requests
beautifulsoup4
trafilatura
gradio
```

Install all dependencies by running the first cell of any notebook, or manually:

```bash
pip install chromadb sentence-transformers nltk spacy langchain langchain-community \
    matplotlib seaborn pandas numpy tqdm groq requests beautifulsoup4 trafilatura gradio

python -m spacy download en_core_web_sm
```

### API Keys Required

| Key | Purpose | How to Get |
|---|---|---|
| `GROQ_API_KEY` | Synthetic content generation (Notebook 1 only, if adding new topics) | Free at [console.groq.com](https://console.groq.com) |

Store API keys in Google Colab Secrets (🔑 key icon in left sidebar). Never paste keys directly into notebook cells.

### Runtime Requirements

- **Google Colab** with T4 GPU runtime recommended for embedding generation (Step 8 of Notebook 1)
- **Google Drive** with at least 500MB free space for ChromaDB, source files, and outputs
- Minimum 8GB RAM (Colab free tier sufficient)

---

## Data Access and Reproduction Instructions

### Google Drive Setup

All project files are organized in a shared Google Drive folder:

```
HALO_Project/
├── knowledge_base/       ← source .txt files (scraped, synthetic, manual)
├── chromadb/             ← vector database (generated by Notebook 1)
├── processed_chunks/     ← halo_chunks.csv (all chunks + metadata)
├── visualizations/       ← preprocessing and evaluation charts
├── evaluation/           ← halo_eval_results.csv (scored evaluation)
└── logs/                 ← retrieval_log.csv, response_log.csv, halo_feedback.csv
```

To mount the shared folder in Colab, add a shortcut to your personal Drive:
1. Open Google Drive → Shared with me
2. Right click **HALO_Project** → Organize → Add shortcut to Drive
3. Place shortcut in My Drive root
4. `BASE_DIR = '/content/drive/MyDrive/HALO_Project'` will resolve correctly

### Running the Project

Run notebooks in order:

**Notebook 1 — Data Collection and Preprocessing**
- Steps 2.5 and 2.6 collect and generate source content (can be skipped if knowledge_base/ is already populated)
- Steps 3–12 must be run in sequence to build ChromaDB
- Use T4 GPU runtime for Step 8 (embedding generation)

**Notebook 2 — RAG Pipeline and Evaluation**
- Requires Notebook 1 to be complete and ChromaDB saved to Drive
- Requires `GROQ_API_KEY` in Colab Secrets
- Run Steps 1–9 to generate evaluation results
- Manually score `halo_eval_results.csv` in Google Sheets, then re-run Step 10

**Notebook 3 — Gradio Frontend**
- Self-contained — can be run independently after Notebook 1
- Requires `GROQ_API_KEY` in Colab Secrets
- `demo.launch(share=True)` generates a public 72-hour link for team testing and demos

### Reproducing the Knowledge Base from Scratch

If starting fresh without the shared Drive folder:
1. Run Notebook 1 Steps 1–2 to install dependencies and mount Drive
2. Step 2.5 will scrape articles from the URL list automatically
3. Step 2.6 will generate synthetic content (requires `GROQ_API_KEY`)
4. Add any manual `.txt` files to `knowledge_base/`
5. Run Steps 3–12 to process everything into ChromaDB

Target: 500–800 chunks. The project achieved 667 chunks from 115 source files.

---

## Project Files

| File | Description |
|---|---|
| `HALO_Notebook1_Improved.ipynb` | Data collection, preprocessing, ChromaDB pipeline |
| `HALO_Notebook2_Improved.ipynb` | RAG query pipeline, evaluation framework |
| `HALO_Notebook3_Improved.ipynb` | Polished Gradio frontend interface |
| `README.md` | This file |

---

*HALO — Built by Icarus Squad · ITAI2377 · 2026*
