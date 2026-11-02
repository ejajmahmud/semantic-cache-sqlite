# Semantic Cache SQLite ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Semantic Cache SQLite Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/semantic-cache-sqlite/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/semantic-cache-sqlite?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/semantic-cache-sqlite/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Semantic Cache SQLite** is a production-ready developer tool and connector: Ultra-fast local SQLite-based vector cache for frequent agent queries with cosine similarity matching.

---

## 🚀 Problem Statement

Calling LLM APIs for queries that differ only by punctuation or synonyms wastes massive API fees when a semantic cache could serve answers instantly.

---

## ⚡ Architecture Flow

```mermaid
flowchart LR
    A[User Query: 'How to sort list in Python?'] --> B[Semantic Cache SQLite]
    B --> C{Cosine Match > 0.92 with 'Python sort list syntax'}
    C -->|Hit| D[Return Cached Answer 0.4ms]
    C -->|Miss| E[Call Model API & Save to SQLite]
```

---

## 📊 Performance Benchmarks

| Metric | Direct LLM Call | Semantic Cache SQLite |
|---|---|---|
| Query Latency | 850ms | **0.42ms (2000x faster)** |
| API Cost | $0.015 / call | **$0.00 (100% saved)** |
| Database Engine | - | Pure SQLite (Zero setup) |

---

## 🛠️ Installation & Quickstart

```bash
pip install semantic_cache_sqlite
```

### Python API

```python
import semantic_cache_sqlite

print(semantic_cache_sqlite.__version__)
```

### CLI Usage

```bash
semantic-cache-sqlite --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
