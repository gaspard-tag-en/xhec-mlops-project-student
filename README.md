

# MLOPS - Industrialization of the Abalone Age Prediction Model

# Introduction
This repository is the industrialization of the Abalone Age Prediction Model (https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest. It takes the form of an API that runs locally that can be used to make prediction on new data for the age of abalone (column 'Rings') from physical measurements ("Shell weight", "Diameter", etc...).

# Table of Contents
1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [Usage](#Usage)
4. [Contribution](#Contribution)
5. [License](#License)

# Installation

### **Prerequisites**
  - This project requires Python 3.9 or higher

### **Steps**

1. **Clone the repository**:

  git clone https://github.com/gaspard-tag-en/xhec-mlops-project-student.git


2. **Navigate to the project directory**:
  cd xhec-mlops-project-student


3. **Set up a virtual environment**:
  conda create --name x-hec-solution python=3.9
  conda activate x-hec-solution


4. **Install dependencies**:
  pip install -r requirements-dev.txt



# Usage
 to run on data : python src/modelling/main.py "data/abalone.csv"

# Acknowledgements
Guillaume de Surville
Matthieu Haguenauer
Gaspard de Fommervault
Kenzo Bounhecta
Alexis Constensoux
Marine Chouraqui