# NYCU Data Mining (Spring 2026) - Assignment 1

This repository contains the completed notebooks and model code for all tasks in Assignment 1.

## Environment Setup (`uv`)

1. Install dependencies from `pyproject.toml`:

```bash
uv sync
```

2. Run Jupyter Notebook:

```bash
uv run jupyter notebook
```

3. (Optional) Execute all notebooks in batch mode:

```bash
uv run jupyter nbconvert --to notebook --execute --inplace Linear_Regression.ipynb
uv run jupyter nbconvert --to notebook --execute --inplace Logistic_Regression.ipynb
uv run jupyter nbconvert --to notebook --execute --inplace Real_World_Classification.ipynb
```

## Output Artifacts

Generated plots and metric tables are saved to:

```text
report_assets/
├── linear_regression/
├── logistic_regression/
└── real_world_classification/
```

## File Structure

```text
.
├── Linear_Regression.ipynb
├── Logistic_Regression.ipynb
├── Real_World_Classification.ipynb
├── DM_asg1_314554024.md
├── pyproject.toml
├── uv.lock
├── data/
├── model/
│   ├── activations.py
│   ├── gradients.py
│   ├── linear_model.py
│   ├── metrics.py
│   └── utils.py
└── report_assets/
```
