# Distributed Big Data Analytics & ML Pipeline (Hadoop + MapReduce + ML)

## Overview

This repository demonstrates an **end-to-end Big Data analytics pipeline** designed to reflect how modern, large-scale data platforms operate in real production environments.

The focus of this project is on **data engineering, distributed systems, and scalable analytics**, showing how raw data is ingested, processed, and transformed into meaningful insights before it ever reaches advanced AI models.

Rather than emphasizing model accuracy alone, the project highlights:
- Scalable system design
- Distributed storage and batch processing
- Fault-tolerant architectures
- Integration between Big Data platforms and machine learning workflows

---

## Architecture Overview

```
Raw Data
   ↓
HDFS (Distributed Storage)
   ↓
MapReduce (Batch Processing)
   ↓
Feature Engineering
   ↓
Machine Learning (Clustering + Classification)
   ↓
Insights & Visualizations
```

### Core Technologies
- **Hadoop HDFS** – Distributed, fault-tolerant storage
- **MapReduce (Hadoop Streaming)** – Parallel batch processing
- **Docker** – Reproducible infrastructure
- **Python (scikit-learn)** – Machine learning & analytics
- **Matplotlib** – Visualization

---

## Pipeline Explanation

### 1. Distributed Infrastructure Setup

A Docker-based Hadoop cluster is deployed in pseudo-distributed mode, consisting of:
- **NameNode** for filesystem metadata
- **DataNode** for block storage
- **Secondary NameNode** for metadata checkpointing
- **Python ML container** for analytics and visualization

This setup mirrors how Big Data systems separate metadata management, storage, and computation.

---

### 2. Data Ingestion into HDFS

Retail transaction data is uploaded into HDFS where:
- Files are split into fixed-size blocks (128MB)
- Blocks are distributed across DataNodes
- Metadata is managed using FSImage and EditLog

This enables parallel processing and data locality.

---

### 3. Distributed Batch Processing (MapReduce)

A MapReduce job is executed using Hadoop Streaming to perform **geographic transaction analysis**.

- **Mapper:** Extracts country field and emits `<country, 1>`
- **Reducer:** Aggregates transaction counts per country
- **YARN:** Manages resource allocation and job execution

This stage demonstrates large-scale batch analytics using distributed computation.

---

### 4. Feature Preparation

Processed data is exported and sampled for analytics:
- Data cleaning and validation
- Encoding of categorical features
- Feature engineering
- Scaling for ML readiness

This reflects real-world pipelines where Big Data systems prepare data for downstream ML.

---

### 5. Machine Learning Layer

A hybrid ML approach is used:

#### Unsupervised Learning
- **K-Means clustering** to identify behavioral customer segments

#### Supervised Learning
- **Random Forest classification** to predict customer segments
- Evaluated using accuracy, precision, recall, and F1-score

This combination balances data-driven discovery with business interpretability.

---

### 6. Visualization & Insights

Outputs include:
- Customer cluster visualizations
- Payment method distributions
- Processed datasets with engineered features

These artifacts translate large-scale computation into decision-ready insights.

---

## How to Run the Project

### 1. Start the Hadoop Cluster
```bash
docker-compose up -d
```

### 2. Verify Containers
```bash
docker ps
```

### 3. Upload Data to HDFS
```bash
docker exec -it namenode bash
hdfs dfs -mkdir -p /retail
hdfs dfs -put /data/retail_data.csv /retail/
```

### 4. Verify Block Distribution
```bash
hdfs fsck /retail/retail_data.csv -files -blocks -locations
```

---

### 5. Run MapReduce Job
```bash
bash scripts/country_analysis.sh
```

---

### 6. Run Machine Learning Pipeline
```bash
docker exec -it python-ml bash
pip install pandas numpy matplotlib scikit-learn
python scripts/ml_analysis.sh
```

---

## Outputs

- `output/mapreduce_results.txt`
- `output/processed_retail_data.csv`
- `output/customer_clusters.png`
- `output/payment_method_distribution.png`

---

## Key Takeaways

- How distributed storage enables scalable analytics
- Why Big Data systems are foundational to modern AI pipelines
- How batch processing frameworks work at scale
- Where machine learning fits within data engineering workflows
- Designing systems that scale horizontally by architecture

---

## Future Enhancements

- Multi-node cluster benchmarking
- Spark-based processing comparison
- Streaming ingestion pipelines
- Advanced feature engineering
- Model orchestration and scheduling

---

## Disclaimer

This project focuses on **architecture, system design, and workflow integration**.  
The goal is to demonstrate scalable data pipelines rather than production benchmarking.
