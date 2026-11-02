"""Unit tests for SemanticCacheSQLite."""
import unittest
from semantic_cache_sqlite.cache import SemanticCacheSQLite

class TestSemanticCache(unittest.TestCase):
    def test_cache_hit_and_miss(self):
        c = SemanticCacheSQLite(threshold=0.9)
        c.set("q1", [1.0, 0.0], "answer1")
        # Near vector
        self.assertEqual(c.get([0.99, 0.01]), "answer1")
        # Far vector
        self.assertIsNone(c.get([0.0, 1.0]))

if __name__ == "__main__":
    unittest.main()
