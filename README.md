# Drug Reviews Dataset Documentation

## Dataset Overview
This dataset contains processed drug reviews from DrugLib.com, combining both training and test sets.

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

### Engineered Features
- `effectiveness_encoded`: Numerical encoding of effectiveness (1-5)
  - 1: Ineffective
  - 2: Marginally Effective
  - 3: Moderately Effective
  - 4: Considerably Effective
  - 5: Highly Effective

- `side_effects_encoded`: Numerical encoding of side effects (1-5)
  - 1: No Side Effects
  - 2: Mild Side Effects
  - 3: Moderate Side Effects
  - 4: Severe Side Effects
  - 5: Extremely Severe Side Effects

- `has_severe_side_effects`: Binary indicator (0/1)
  - 1: Severe or Extremely Severe Side Effects
  - 0: Otherwise

- `is_highly_effective`: Binary indicator (0/1)
  - 1: Highly Effective
  - 0: Otherwise

- `review_length`: Total length of all review text fields combined

## Data Preprocessing Steps
1. Combined train and test sets
2. Encoded categorical variables
3. Created new numerical features
4. Handled missing values
5. Removed duplicates

## Potential ML Tasks
1. Predicting drug ratings
2. Classifying effectiveness levels
3. Predicting side effects severity
4. Analyzing review sentiment
5. Drug recommendation system

## Notes for ML Team
- The dataset is ready for both classification and regression tasks
- Text fields (benefitsReview, sideEffectsReview, commentsReview) are available for NLP tasks
- Binary features can be used for classification tasks
- Numerical encodings maintain ordinal relationships in categorical variables 