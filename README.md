# Natural Language to NGSI-LD Corpus Generator

## Overview
This repository contains tools and data for creating a corpus of Natural Language sentences paired with their NGSI-LD representations. The main goal is to fine-tune Large Language Models (LLMs) to better understand and generate NGSI-LD context information from natural language queries.

## Repository Contents

### 1. Context Broker Service
- Docker compose configuration for running a FIWARE Context Broker
- Setup instructions and configuration details
- Basic usage examples

### 2. Data Processing Tools
- CSV to NGSI-LD converter utilities
- Data population scripts
- Sample datasets

### 3. Training Corpus
The core component of this repository is the training corpus containing:
- Natural language queries related to FIWARE use cases
- Corresponding NGSI-LD representations
- Mapping between natural language and structured NGSI-LD format
- Tools from converting from CSV to JSONL files that serve as training input for LLMs.




