import yaml
import pandas as pd
import spacy


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

