"""Command line interface for semantic-cache-sqlite."""
from .cache import SemanticCacheSQLite

def main():
    cache = SemanticCacheSQLite()
    cache.set("hello", [1.0, 0.0], "Greeting response")
    hit = cache.get([0.98, 0.05])
    print("Semantic Cache Hit:", hit)

if __name__ == "__main__":
    main()
