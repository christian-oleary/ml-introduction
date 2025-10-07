# Introduction to Machine Learning (ML)

Introduction to basic ML modelling using [Python](https://www.python.org/downloads/).

This repository contains code examples to introduce students to the absolute basics of [Python](https://www.python.org/downloads/), [pandas](https://pandas.pydata.org/getting_started.html), and [scikit-learn](https://scikit-learn.org/stable/getting_started.html).

You can [download this code from here](https://github.com/christian-oleary/ml-introduction/archive/refs/heads/main.zip) as a zip file.

## Overview

This guide consists of three progressive lessons presented as Jupyter notebooks:

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

## Where Can I Run This Code?

- **Option 1 (beginner-friendly)**: [JupyterLite](https://jupyterlite.rtfd.io/en/stable/try/lab) is a free and open-source means of running Python code

- **Option 2 (beginner-friendly)**: Google Colab allows you to run Python in the browser. Requires a gmail account.
  - Link: <https://colab.google/>
  - YouTube: [tutorial](https://www.youtube.com/watch?v=Xi9-W26cDBs) (2023), [another tutorial](https://www.youtube.com/watch?v=RLYoEyIHL6A) (2021)

- **Option 3**: Run Jupyter notebooks and Python scripts on your own device: see the [Setup](#setup-for-running-code-on-your-device) section below.

## Setup For Running Code on Your Device

***You can ignore this section if you are using Google Colab or JupyterLite***.

If you have programming experience in Python, install and setup your own Python environment using your preferred tools. Otherwise, this section gives high-level steps to get started using Python via Anaconda.

1. Install [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://repo.anaconda.com/miniconda/). There is a [guide](https://www.anaconda.com/blog/anaconda-python-complete-beginners-guide).

2. Download a copy of this repository to your device:
   - For beginners: you can download as a .zip file from [this link](https://github.com/christian-oleary/ml-introduction/archive/refs/heads/main.zip).

      **OR**
   - Use using Git: ```git clone https://github.com/christian-oleary/ml-introduction.git```

3. Install the required Python packages. The packages are listed in the [requirements.txt](./requirements.txt) file of this repository:
   - For beginners: the [Anaconda guide](https://www.anaconda.com/docs/tools/anaconda-navigator/getting-started) shows you how to install packages.

      **OR**
   - If using a terminal (command line interface), you can set up a conda environment and install packages using:

   ```bash
   conda create -n ml -y  # Creates a Python environment called "ml"
   conda activate ml      # Use the "ml" environment

   pip install -r requirements.txt  # Install required packages
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

## Learning Path

We recommend following the notebooks in order:

1. Start with Python basics if you're new to programming
2. Move to pandas to learn data manipulation
3. Finally, explore scikit-learn for machine learning concepts

Each notebook is self-contained and can be run independently, but they build on concepts from previous lessons.

## License

MIT License - see [LICENSE](./LICENSE) file for details
