📋 Project Overview
This project implements a comprehensive Big Data analytics pipeline for e-commerce retail data using Hadoop ecosystem technologies. The system processes a 486MB transactional dataset through distributed storage, parallel processing, and machine learning techniques to extract actionable business insights.

🎯 Key Features
Distributed Storage: Hadoop HDFS setup with Docker containers

Parallel Processing: MapReduce implementation for transaction analysis

Machine Learning: Customer segmentation using K-Means clustering and Random Forest classification

Visualization: Business insights through data visualization

Scalable Architecture: Designed to handle large-scale retail data

🏗️ Architecture Components
Hadoop Cluster (Pseudo-distributed)

NameNode: Metadata management

DataNode: Distributed data storage

Secondary NameNode: Checkpointing service

Processing Pipeline

Data Ingestion → HDFS Storage → MapReduce Processing → ML Analysis → Visualization

Analytical Components

Geographic transaction analysis

Customer segmentation

Payment method analysis

Business intelligence extraction

🚀 Project Setup Instructions
Prerequisites
Docker and Docker Compose installed
4GB+ RAM available for containers
Python 3.10+ (for ML components)
Git (for cloning the repository)

Step 1: Clone and Prepare Project Structure