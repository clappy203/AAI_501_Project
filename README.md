# Sentiment-Informed Drug Effectiveness Prediction Using NLP Techniques

## Dataset Overview

This project explores the relationship between patient sentiment and perceived drug effectiveness by analyzing 4,143 patient-written reviews sourced from DrugLib.com via the UCI Machine Learning Repository. By integrating Natural Language Processing (NLP), sentiment analysis, and machine learning techniques, the study aims to predict drug effectiveness and uncover latent patterns in patient experiences.
The dataset contains processed drug reviews from DrugLib.com, combining both training and test sets.

## Features Description

### Original Features

- `urlDrugName`: Name of the drug
- `rating`: User rating (1-10)
- `effectiveness`: Effectiveness level (categorical)
- `sideEffects`: Side effects severity (categorical)
- `condition`: Medical condition treated
- `benefitsReview`: Text review of benefits
- `sideEffectsReview`: Text review of side effects
- `commentsReview`: Additional comments

## Project Structure

The repository is organized as follows:​

- `drug_review_analysis/`: Contains the `__init__.py` file.​

- `eda/`: Includes the dataset (`train.csv` and `test.csv`) and a Jupyter notebook for exploratory data analysis.​

- `cleancode.ipynb`: Finalized notebook encompassing hypothesis formulation, EDA, data preprocessing, feature engineering, machine learning pipeline, deep learning clustering, conclusions, and recommendations.​

- `poetry.lock` & `pyproject.toml`: Files for dependency management using Poetry.​

- `initial_hypothesis.md`: Document outlining the initial hypotheses of the study.​

## Setup Instructions

- Python 3.8 or higher​
- Poetry package manager

### 🚀 Getting Started

To clone the repository and navigate into the project directory, run the following commands in your terminal:

```bash
git clone https://github.com/clappy203/AAI_501_Project.git
cd AAI_501_Project
```

### 📦 Install Poetry

If you don't have Poetry installed, follow the [official installation guide](https://python-poetry.org/docs/#installation) to install it:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Once installed, verify the installation:

```bash
poetry --version
```

### 🧪 Create & Activate Virtual Environment

Use Poetry to create and activate a virtual environment with all the necessary dependencies:

```bash
# Activate Poetry virtual environment
poetry shell

# Install all dependencies
poetry install

```

### 📓 Launch Jupyter Notebook

Start Jupyter Notebook to run the finalized clean code notebook:

```bash
 jupyter notebook

```

- Navigate to `cleancode.ipynb` in the project root.

- Run all cells sequentially to execute the full pipeline from hypothesis testing to model and evaluation.

## 🔄 Project Workflow & Methodology

The study follows a structured AI pipeline.
The following steps outline the complete pipeline used in this project:

1. 📥 **Data Collection**

   - Source: DrugLib dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/)

2. 🧹 **Data Preprocessing**

   - Merging, cleaning, and filtering the dataset
   - Text cleaning & tokenization (`clean_and_tokenize` function)
   - POS tagging
   - Lemmatization
   - Removal of stopwords and noise

3. 🧠 **Sentiment Analysis**

   - Sentiment scoring using the **VADER** model
   - Compound scores appended to dataset for modeling

4. 🏗️ **Feature Engineering**

   - Vectorization using **Bag-of-Words** and **TF-IDF**
   - Label encoding of categorical features
   - Correlation analysis between sentiment, ratings, and other features

5. 🤖 **Supervised Machine Learning**

   - Models: Logistic Regression, Random Forest, XGBoost
   - Evaluated via `train_and_evaluate()` function
   - Metrics: Accuracy, F1 Score, Log Loss

6. 🔍 **Unsupervised Learning & Clustering**

   - K-Means Clustering on sentiment, effectiveness, and side effects
   - PCA for visualization of clusters

7. 📈 **Exploratory Data Analysis (EDA)**

   - Visualization with **matplotlib** and **seaborn**
   - Bar plots, count plots, and word clouds

8. 📊 **Model Evaluation & Results Interpretation**

   - Comparison of model performance
   - Visualization of cluster insights
   - Interpretation of sentiment vs clinical effectiveness

9. ✅ **Conclusion & Recommendations**
   - Summary of findings
   - Suggestions for healthcare applications
   - Identifying emotionally dissatisfied but clinically satisfied patient groups

## 🧰 Libraries and Tools Used

| Category                      | Libraries & Tools                                                                                                                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 🧠 **NLP & Text Processing**  | ![NLTK](https://img.shields.io/badge/NLTK-Text%20Processing-green?logo=python&logoColor=white) ![VADER](https://img.shields.io/badge/VADER-Sentiment%20Analysis-blueviolet?logo=python&logoColor=white)            |
| 🤖 **Machine Learning**       | ![Scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-GradientBoosting-brightgreen?logo=xgboost&logoColor=white) |
| 📊 **Data Visualization**     | ![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-Stats%20Plots-cyan?logo=python&logoColor=white)          |
| 🛠️ **Environment Management** | ![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Management-purple?logo=python&logoColor=white)                                                                                                          |

## 🗂️ Kanban Board

Track the project's progress, task assignments, and milestones via our GitHub Projects Kanban Board:

🔗 [View Kanban Board](https://github.com/users/clappy203/projects/2)
