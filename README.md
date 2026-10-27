# Food Access Analysis Project

This project analyzes food access and insecurity in different census tracts using machine learning and data visualization techniques.

## Project Overview

The project uses census data to predict and analyze food insecurity patterns across different regions. It includes:

- Machine learning models (Logistic Regression and MLP Classifier) to predict food insecurity
- Data visualization tools to understand the relationship between poverty rates, income, and food access
- Geographic analysis using choropleth maps

## Key Files

- `train.py`: Contains the machine learning models and training pipeline
- `visualize.py`: Generates visualizations and analysis of the data
- `choropleth map final.R`: Creates geographic visualizations of food access patterns
- `bias.py`: Analyzes potential biases in the data and models

## Data

The project uses two main datasets:
- `train.csv`: Main training dataset with census tract information
- `FoodAccessData.csv`: Additional food access data for analysis

## Requirements

- Python 3.x
- Required Python packages: pandas, scikit-learn, matplotlib, seaborn
- R (for choropleth map visualization)

## Usage

1. Run `train.py` to train the models and generate predictions
2. Use `visualize.py` to create visualizations of the results
3. Run the R script for geographic analysis

## Results

The project provides insights into:
- The relationship between poverty rates and food insecurity
- Geographic patterns of food access
- Model performance in predicting food insecurity
- Potential biases in the data and predictions 
