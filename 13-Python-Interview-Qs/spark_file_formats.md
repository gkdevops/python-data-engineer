# File Formats Supported by Apache Spark

Apache Spark can read from and write to a variety of storage formats.  
Choosing the right one affects performance, storage footprint, schema-handling, and interoperability.  
Below is a concise, well-structured reference in Markdown.

---

## 1. Parquet

**Advantages**
- **Columnar storage** – reads only the columns required ➜ less disk I/O.
- **Compression** – supports Snappy, Gzip, LZO, etc. → high compression.
- **Predicate push-down** – Spark can push filters to the storage layer.

**Disadvantages**
- Schema evolution can be tricky when changes are frequent.

**Typical use cases**
- Analytical / reporting workloads where fast scans and small footprint matter.

**Compression ratio**
- Roughly **50 % – 90 %** (data & codec dependent).

---

## 2. ORC (Optimized Row Columnar)

**Advantages**
- Very high compression ratios.
- Predicate push-down similar to Parquet.
- Better built-in support for schema evolution.

**Disadvantages**
- Slower write performance; optimized mainly for reads.

**Typical use cases**
- Data-warehousing workloads that still require decent write performance.

**Compression ratio**
- Roughly **50 % – 90 %** (comparable to Parquet).

---

## 3. Avro

**Advantages**
- Strong schema evolution support (backward & forward compatible).
- Compact binary encoding.
- Dynamic typing allows graceful evolution.

**Disadvantages**
- Not as fast as Parquet/ORC for large-scale analytics.
- Compression exists, but ratios are usually lower.

**Typical use cases**
- Streaming pipelines where schemas change frequently.

**Compression ratio**
- Roughly **30 % – 60 %**.

---

## 4. JSON

**Advantages**
- Human-readable & easy for debugging.
- Flexible schema—fields can be added/removed freely.

**Disadvantages**
- Space-inefficient; slower to parse.
- No type enforcement ⇒ potential data-quality issues.

**Typical use cases**
- Interop with services/APIs that expect JSON.
- Situations where readability trumps performance.

**Compression ratio**
- Roughly **10 % – 50 %** (highly variable).

---

## 5. CSV (Comma-Separated Values)

**Advantages**
- Extremely simple, universally supported.
- Human-readable; easy to inspect manually.

**Disadvantages**
- No built-in schema ⇒ data-quality risks.
- Inefficient storage & slower processing.

**Typical use cases**
- Legacy system integration and quick ad-hoc data exchange.

**Compression ratio**
- Roughly **10 % – 50 %** (varies with data & codec).

---

## When to Use What 🤔

| Scenario / Requirement                              | Recommended Format |
|-----------------------------------------------------|--------------------|
| Fast analytics, heavy aggregations                  | **Parquet** or **ORC** |
| Best Hadoop ecosystem compatibility                 | **Parquet** |
| Need robust schema evolution in analytics           | **ORC** |
| Streaming with frequent schema changes              | **Avro** |
| Human-readable interchange or API integration       | **JSON** or **CSV** |

Consider:
1. **Query performance** – columnar beats row for analytics.
2. **Storage efficiency** – Parquet/ORC compress the best.
3. **Schema evolution** – Avro & ORC handle changes gracefully.
4. **Interoperability** – JSON/CSV remain the lowest common denominator.

---

### TL;DR

- Use **Parquet/ORC** for most analytical Spark jobs.  
- Use **Avro** for streaming pipelines needing evolving schemas.  
- Stick to **JSON/CSV** only when human readability or legacy compatibility outweighs performance and storage concerns.

Happy Sparking! 🚀
