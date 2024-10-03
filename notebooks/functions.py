import yaml
import pandas as pd
import spacy
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, root_mean_squared_error,accuracy_score,classification_report


# Global vars

nlp = spacy.load('en_core_web_sm')



#import yaml paths
def import_yaml():
    try:
        with open("../config.yaml", "r") as file:
            config = yaml.safe_load(file)
    except:
        print("The config.yaml file was not found in the main folder!")

    return config


def convert_token(text):
    
    # Lowercasing the text
    doc = nlp(str(text).lower()) 

    # Lemmatize and remove stopwords
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

def print_evaluation (y_val_split , y_pred,X_train_split, y_train_split,model):
    # Evaluate the model
    print(classification_report(y_val_split, y_pred))
    print(f'Validation Accuracy: {accuracy_score(y_val_split, y_pred): .2f}')
    print(f"MAE {mean_absolute_error(y_pred, y_val_split): .2f}") 
    print(f"RMSE, {root_mean_squared_error(y_pred, y_val_split): .2f}")
    print(f"R2 score, {model.score(X_train_split, y_train_split): .2f}")