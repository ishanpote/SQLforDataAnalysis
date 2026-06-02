# Advanced Relational SQL Data Analytics & Performance Pipeline

## 📌 Project Overview
This repository contains a production-grade relational database layout and advanced analytics execution matrix designed to model and query retail transactional metrics. By separating standard flat table files into a normalized Star Schema architecture (incorporating an operational Fact table alongside isolated Dimension maps), this pipeline enables optimized analytical queries using complex joins, nested subqueries, aggregations, database views, and automated performance indexes.

The data engine uses **SQLite** as the transactional relational storage system, managed via DB Browser for SQLite.

---

## 🏗️ Relational Database Schema Architecture
The raw transactional rows were programmatically normalized into three dedicated relation arrays to enforce database design integrity:
* **`orders` (Fact Table):** Tracks numerical transaction metrics including `sales`, `quantity`, `discount`, `profit`, and structural key pointers (`customer_id`, `product_id`).
* **`customers` (Dimension Table):** Contains independent profiles mapping unique `customer_id` identities to alphanumeric attributes like names, market segments, and geographical regions.
* **`products` (Dimension Table):** Evaluates standalone product characteristics, binding inventory keys (`product_id`) to categories, sub-categories, and official names.

---

## 💻 Production-Grade SQL Analytical Script

The following optimized queries are compiled to generate enterprise performance reviews:

### Query 1: Revenue and Profitability Analysis by Product Sub-Category
* **Objective:** Identify top revenue streams and isolate categories leaking margins.

```sql
SELECT p.sub_category, 
       ROUND(SUM(o.sales), 2) AS total_sales, 
       ROUND(SUM(o.profit), 2) AS total_profit,
       ROUND((SUM(o.profit) / SUM(o.sales)) * 100, 2) AS profit_margin_percentage
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.sub_category
ORDER BY total_sales DESC;
```

### Query 2: Identifying High-Value Customers via Nested Subqueries
* **Objective:** Extract consumer profiles whose lifetime spending exceeds the global average customer baseline.

```sql
SELECT c.customer_name, 
       c.segment, 
       ROUND(SUM(o.sales), 2) AS total_customer_spend
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
HAVING total_customer_spend > (
    -- Subquery: Calculates the baseline average total sales per customer entity
    SELECT AVG(customer_total_sales)
    FROM (
        SELECT SUM(sales) AS customer_total_sales
        FROM orders
        GROUP BY customer_id
    )
)
ORDER BY total_customer_spend DESC;
```

### Query 3: Creating an Operational Regional Performance View
* **Objective:** Establish a persistent reporting abstraction layer for macro business reviews.

```sql
DROP VIEW IF EXISTS view_regional_performance;

CREATE VIEW view_regional_performance AS
SELECT c.region,
       COUNT(DISTINCT o.order_id) AS total_orders_processed,
       ROUND(SUM(o.sales), 2) AS total_sales_volume,
       ROUND(SUM(o.profit), 2) AS total_net_profit
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region;

-- Querying the virtual view layer directly
SELECT * FROM view_regional_performance 
ORDER BY total_net_profit DESC;
```

### Query 4: Database Optimization via Indexing
* **Objective:** Build background lookup maps on foreign keys to optimize query execution time.

```sql
CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_product ON orders(product_id);
```

---

## 📊 Verification Outputs & Screenshots
<img width="799" height="898" alt="Screenshot 2026-06-02 133604" src="https://github.com/user-attachments/assets/895a9d99-46b2-4d48-9aaa-f205d551e094" />
<img width="798" height="933" alt="Screenshot 2026-06-02 133719" src="https://github.com/user-attachments/assets/2345aed4-28f8-4dda-bee4-92fd2c08e898" />
<img width="678" height="694" alt="Screenshot 2026-06-02 133825" src="https://github.com/user-attachments/assets/0598c907-2194-4324-89f1-4959b531b1b9" />
<img width="751" height="686" alt="Screenshot 2026-06-02 133948" src="https://github.com/user-attachments/assets/48c0fff9-32cc-4bf6-a4be-3bc7bf7d7c1c" />

* **Sub-Category Results:** Returns 17 rows tracking revenue performance. (Isolates Tables and Bookcases as net-negative loss leaders).

* **High-Value Client Results:** Filters down to 294 high-tier consumers exceeding global store spend averages.

* **Regional View Output:** Aggregates database records into 4 foundational geographic rows, identifying the West region as the primary profit engine.

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ishanpote/SQLforDataAnalysis.git
   cd SQLforDataAnalysis
   ```

2. **Open the database:**
   - Download and install [DB Browser for SQLite](https://sqlitebrowser.org/)
   - Open your SQLite database file with DB Browser

3. **Execute the queries:**
   - Copy and paste each query from the SQL Analytical Script section
   - Review the results and optimization performance

---

## 🛠️ Technologies Used
- **Database:** SQLite
- **Query Language:** SQL
- **Database Management:** DB Browser for SQLite
- **Language:** Python (data pipeline)

---

## 📝 License
This project is open source and available for educational and analytical purposes.

---

## 👤 Author
[ishanpote](https://github.com/ishanpote)
