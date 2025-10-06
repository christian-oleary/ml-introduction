# ml-introduction
Introduction to basic ML modelling using Python

This repository contains code examples to introduce students to the absolute basics of Python, pandas, and scikit-learn.

## Overview

This tutorial consists of three progressive lessons presented as Jupyter notebooks:

1. **Python Basics** (`01_python_basics.ipynb`) - Learn fundamental Python concepts including:
   - Variables and data types
   - Lists and dictionaries
   - Control flow (if/else statements)
   - Loops (for and while)
   - Functions
   - List comprehensions

2. **pandas Basics** (`02_pandas_basics.ipynb`) - Learn data manipulation with pandas:
   - Creating DataFrames
   - Viewing and exploring data
   - Selecting and filtering data
   - Adding and modifying columns
   - Sorting and aggregation
   - Handling missing data
   - Reading and writing CSV files

3. **scikit-learn Basics** (`03_sklearn_basics.ipynb`) - Introduction to machine learning:
   - Linear regression for predicting continuous values
   - Classification with decision trees
   - Train/test split
   - Model evaluation (accuracy, RMSE)
   - Feature importance
   - Real-world example: Student performance prediction

## Setup

1. Clone this repository:
```bash
git clone https://github.com/christian-oleary/ml-introduction.git
cd ml-introduction
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Open and run each Jupyter notebook in order:

```bash
jupyter notebook
```

Then open the notebooks in your browser:
- `01_python_basics.ipynb`
- `02_pandas_basics.ipynb`
- `03_sklearn_basics.ipynb`

Each notebook is organized into sections with explanations and code cells that you can run interactively.

## Requirements

- Python 3.7 or higher
- numpy
- pandas
- scikit-learn
- jupyter

See `requirements.txt` for specific version requirements.

## Learning Path

We recommend following the notebooks in order:
1. Start with Python basics if you're new to programming
2. Move to pandas to learn data manipulation
3. Finally, explore scikit-learn for machine learning concepts

Each notebook is self-contained and can be run independently, but they build on concepts from previous lessons.

## License

MIT License - see LICENSE file for details
