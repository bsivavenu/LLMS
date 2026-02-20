# 🤖 LLMS — Large Language Models Learning Repository

A personal learning repository covering LLMs, LangChain, LlamaIndex, Generative AI, Fine-tuning, OCR, and more — aggregated from Udemy, Coursera, YouTube, and mini-courses.

---

## 📁 Repository Structure

```
LLMS/
├── Udemy_langchain_apps/           # LangChain Udemy course projects & notebooks
├── coursera_GenAI/                 # Coursera Generative AI specialization labs
├── mini_courses/                   # Short focused courses (DeepLearning.AI etc.)
│   ├── finetuning_LLMS/
│   ├── neo4j_RAG/
│   └── opensource_models_huggingface/
├── python/                         # Python scripts, NLP models, assignments
│   └── CSV Data Analysis - Project 7/
├── youtube_apps/                   # YouTube tutorial notebooks
│   ├── langchain/
│   └── llamaindex/
└── pyproject.toml
```

---

## ⚙️ Setup

### Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) — fast Python package manager

### Installation

```bash
# Clone the repo
git clone https://github.com/bsivavenu/LLMS.git
cd LLMS

# Create virtual environment
uv venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install all dependencies
uv sync
```

---

## 📚 Learning Sources

| Folder | Source | Topics Covered |
|--------|--------|----------------|
| `Udemy_langchain_apps/` | Udemy | LangChain chains, agents, embeddings, RAG, apps |
| `coursera_GenAI/` | Coursera | Summarization, fine-tuning, RLHF, detoxification |
| `mini_courses/finetuning_LLMS/` | DeepLearning.AI | Why fine-tune, training, evaluation |
| `mini_courses/neo4j_RAG/` | DeepLearning.AI | Knowledge graphs, RAG with Neo4j |
| `mini_courses/opensource_models_huggingface/` | DeepLearning.AI | NLP, translation, embeddings, ASR, TTS, object detection |
| `python/` | Self-study | NLP models, OCR, TF-IDF, bigrams, topic modeling |
| `youtube_apps/` | YouTube | LangChain, LlamaIndex, AutoGPT, MistralAI, VoiceGPT |

---

## 🗂️ Key Projects

### Udemy — LangChain Apps
| Project | Description |
|---------|-------------|
| `conversational_app/` | Simple conversational chatbot using LangChain |
| `similar_words_finder_app/` | Semantic similarity search app |
| `ChatGPT Clone - Source Code/` | ChatGPT-style app with Streamlit |
| `MCQ Creator App/` | Auto-generate MCQs from documents |
| `LangChain_Course+_Complete.ipynb` | Full LangChain course walkthrough |

### Python Scripts
| File | Description |
|------|-------------|
| `ocr_model.py` | Extract text from images using OCR |
| `lang_translation.py` | Language translation using LangChain |
| `tfidf_model.py` | TF-IDF text vectorization |
| `bigram_text_generation_model.py` | Simple bigram language model |
| `topic_model.py` | Topic modeling (LDA) |
| `API_for_car_detection.ipynb` | Car detection via computer vision API |
| `CSV Data Analysis - Project 7/` | Pandas CSV data analysis project |

### YouTube Apps
| File | Description |
|------|-------------|
| `langchain/` | 20+ LangChain notebooks — RAG, agents, SQL, embeddings |
| `llamaindex/` | LlamaIndex notebooks — RAG, Pinecone, text-to-SQL |
| `Auto_GPT.ipynb` | AutoGPT implementation |
| `voiceGPT.ipynb` | Voice-powered GPT app |
| `PandasAI_demo.ipynb` | Natural language queries on DataFrames |
| `train-llama2-chatbot/` | Fine-tune LLaMA 2 with AutoTrain |
| `remove-image-background/` | Background removal using Python |
| `watermark/` | Add watermarks to images |

### Coursera — GenAI Labs
| File | Description |
|------|-------------|
| `Lab_1_summarize_dialogue.ipynb` | Dialogue summarization with FLAN-T5 |
| `Lab_2_fine_tune_generative_ai_model.ipynb` | Full fine-tuning walkthrough |
| `Lab_3_fine_tune_model_to_detoxify_summaries.ipynb` | RLHF-based detoxification |

---

## 🚀 Topics Covered

- **LangChain** — Chains, Agents, Tools, Memory, RAG, SQL, JSON, Multimodal
- **LlamaIndex** — Document indexing, querying, Pinecone, text-to-SQL
- **OpenAI API** — GPT-3.5/4, embeddings, function calling, assistants
- **HuggingFace** — Transformers, pipelines, NLP, ASR, TTS, object detection
- **Fine-tuning** — FLAN-T5, LLaMA 2, RLHF, PEFT, AutoTrain
- **RAG** — Retrieval Augmented Generation with FAISS, Chroma, Pinecone, Neo4j
- **OCR** — Image-to-text extraction
- **Vector Stores** — FAISS, ChromaDB, Pinecone
- **Python NLP** — TF-IDF, bigrams, topic modeling, embeddings
- **Prompt Engineering** — Summarization, classification, generation

---

## 📝 Notes

- Never commit your `.env` file — only `.env_sample.txt` should be in git
- Notebook checkpoints (`.ipynb_checkpoints/`) are gitignored
- Run `uv sync` after cloning to install all dependencies from `pyproject.toml`
- For Jupyter notebooks, register the kernel: `uv run python -m ipykernel install --user --name=llms-env`

---

## 📄 License

MIT License — feel free to learn from and reference this code.
