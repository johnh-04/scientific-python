# Scientific Python — Complete Setup & Workflow Guide

This project introduces a complete environment and workflow for scientific computing in Python.
It is designed for data analysis, numerical computation, and reproducible research, organized through a sequence of structured Jupyter Notebooks.

---

## 📌 What is Scientific Python?

Scientific Python refers to the ecosystem of Python libraries used for:

* Data analysis and manipulation
* Numerical computation and matrix calculus
* Scientific modeling and signal processing
* Data visualization
* Machine learning foundations

It is widely used in physics, engineering, data science, and research.

---

## ⚙️ Environment Setup

### 1. Create project folder

**macOS / Linux**
mkdir scientific-python
cd scientific-python

**Windows**
mkdir scientific-python
cd scientific-python

---

### 2. Create virtual environment

python3 -m venv venv

---

### 3. Activate environment

**macOS / Linux**
source venv/bin/activate

**Windows**
venv\Scripts\activate

---

### 4. Upgrade pip (recommended)

pip install --upgrade pip

---

## 📦 Scientific Stack Installation

Install the core libraries and Jupyter core dependencies in your virtual environment:

pip install numpy pandas matplotlib scipy scikit-learn jupyter

### Alternative (using requirements file)

pip install -r requirements.txt

---

## 📦 Generate dependencies

After installing packages, freeze the environment to ensure reproducibility:

pip freeze > requirements.txt

Install later with:

pip install -r requirements.txt

---

## 🧪 Project Workflow & Notebooks Structure

The repository is structured as a progressive learning path. Each notebook covers a milestone of the scientific stack:

### 1. Introduction
* `01-introduction.ipynb` — Setting up the environment, Jupyter workflow, and Python core baselines.

### 2. Numerical Computing
* `02-numpy.ipynb` — Multi-dimensional arrays (`ndarrays`), vectorization, linear algebra, and mathematical operations.

### 3. Data Manipulation
* `03-pandas.ipynb` — Structured data handling via Series and DataFrames, alignment, data cleaning, and CSV/time-series management.

### 4. Visualization
* `04-matplotlib.ipynb` — Plotting architectures, functional vs object-oriented APIs, multi-panel figures, and data visualization.

### 5. Machine Learning & Advanced Computing
* `05-ml-foundations.ipynb` — Scientific algorithms with **SciPy** (optimization, signal processing, integration) and predictive modeling pipelines with **Scikit-Learn**.

---

## ▶️ Running the Notebooks

Launch the local Jupyter server to explore and execute the files:

jupyter notebook

Alternatively, you can open the workspace directly in **Visual Studio Code** using the Jupyter Extension.

---

## ⚠️ Best Practices

* Always use a virtual environment
* Never commit the `venv/` folder (add it to `.gitignore`)
* Use vectorization (NumPy/Pandas) instead of explicit python loops (`for`) for heavy computations
* Save checkpoints and raw data separately in the `data/` folder
* Ensure all notebook cells are executable sequentially from top to bottom

---

## 🚀 Next Steps & Application Fields

Once comfortable with this core stack, these foundations can be scaled toward:

* Advanced Machine Learning & Deep Learning pipelines
* Real-time Data Science and Automation systems
* Physics simulations and astrophysics computations
* Embedded systems and Aerospace/Satellite data processing

---

## 🧠 Summary

Scientific Python is a complete ecosystem that transforms Python into a powerful tool for research, engineering, and data-driven discovery.