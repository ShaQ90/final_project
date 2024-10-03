

# Kaggle Competition: Sentiment Analysis on Movie Reviews


## Description

This project was based in a Kaggle Competition, the premisse for the competion is to construct a model that can can indetify the 
For that we have 2 Data Sets, one to train our model and another to test our model, the evaluation metri c is the word-level Jaccard score, that is often used in NLP to compare sets of words from different texts, more about in (https://en.wikipedia.org/wiki/Jaccard_index).


## Data Cleaning

The data set is cleaned, no null values or duplicated values.

## Data processing 

Spacy was used for the Tokenization process, to handle the multiple words per sentence, and the  TF-IDF to transform the string to number.



## ML models

 1. Logistic Regression
 2. Random Forest
 3. SVM
 4. KNN
 5. XGBClassifier


## Final model

For time issues and lack of computer processing power i used the model for the Logistic Regression with the parameters:
```
	C': [10], 
    'penalty': ['l2'],  
    'solver': ['liblinear'] 
```

The test data had the following results:

```
precision    recall  f1-score   support

0       0.34      0.18      0.23       280
1       0.44      0.32      0.37      1103
2       0.64      0.80      0.71      3069
3       0.48      0.41      0.44      1307
4       0.41      0.24      0.30       377

    accuracy                           0.57      6136
   macro avg       0.46      0.39      0.41      6136
weighted avg       0.54      0.57      0.54      6136

Validation Accuracy:  0.57
MAE  0.51
RMSE,  0.82
R2 score,  0.73
```


## Data Sources

[Kaggle - # Sentiment Analysis on Movie Reviews ](https://www.kaggle.com/competitions/sentiment-analysis-on-movie-reviews/overview)

[Project Presentation ](https://docs.google.com/presentation/d/1yfRydOZ8ubi3OEiwG6IsvofMsnllwp4dS7r3jcV9kPk/edit?usp=sharing)
