"""SQLite-based vector semantic cache."""
import sqlite3
import json
import math
from typing import List, Optional, Tuple, Any

class SemanticCacheSQLite:
    def __init__(self, db_path: str = ":memory:", threshold: float = 0.90):
        self.threshold = threshold
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    query TEXT,
                    embedding TEXT,
                    response TEXT
                )
            """)

    @staticmethod
    def _cosine(v1: List[float], v2: List[float]) -> float:
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        return dot / (norm1 * norm2) if norm1 and norm2 else 0.0

    def get(self, embedding: List[float]) -> Optional[str]:
        cur = self.conn.cursor()
        cur.execute("SELECT embedding, response FROM cache")
        best_score = -1.0
        best_resp = None

        for emb_json, resp in cur.fetchall():
            cand_emb = json.loads(emb_json)
            sim = self._cosine(embedding, cand_emb)
            if sim > best_score:
                best_score = sim
                best_resp = resp

        if best_score >= self.threshold:
            return best_resp
        return None

    def set(self, query: str, embedding: List[float], response: str) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO cache (query, embedding, response) VALUES (?, ?, ?)",
                (query, json.dumps(embedding), response)
            )
