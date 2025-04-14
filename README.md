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