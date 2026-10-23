Entity Network Analysis

Part A: Entity Name Standardization

Entity names are standardized by converting them to a consistent format and mapping known aliases to a canonical name. For example, `RAVI KUMAR` and `Ravi Kumar` are treated as the same entity. Duplicate mentions within a report are removed before generating edges.

Part B: Co-occurrence Graph

A graph is constructed using Python and NetworkX. Each person represents a node. An edge connects two people when they appear together in the same report. The edge weight represents the number of reports in which that pair co-occurs.

The degree of a node is used to identify the most connected person. Breadth-first search is used to find the shortest path between Arjun Singh and Imran.

Scalability and Database Choice

1. Processing 50 Million Reports

For a dataset containing 50 million reports, Elasticsearch can be used to search and filter documents efficiently. Reports should be processed in batches using the Elasticsearch scroll API or Point in Time with `search_after`, rather than loading all documents into memory at once.

Entity names should be standardized using a consistent entity-resolution process. For each report, unique entities can be extracted, and co-occurring entity pairs can be generated. Pair counts can be aggregated incrementally or using distributed processing when required. The resulting nodes and weighted edges can then be stored for graph analysis.

2. Elasticsearch vs. Graph Database

Elasticsearch is suitable for full-text search, filtering, and retrieving reports. A graph database such as Neo4j is useful when the main requirement is exploring relationships, finding multi-hop connections, and performing graph traversals.

A practical architecture can use Elasticsearch to retrieve relevant reports and Neo4j to store and query the resulting entity relationships. The choice depends on query patterns, performance requirements, and operational complexity.