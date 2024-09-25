import yaml
import pandas as pd

#import yaml paths
def import_yaml():
    try:
        with open("../config.yaml", "r") as file:
            config = yaml.safe_load(file)
    except:
        print("The config.yaml file was not found in the main folder!")

    return config


# change sentiment from word to int
def sentiment_to_int(df):
    
    df['sentiment'] = df['sentiment'].replace({'positive': 1, 'neutral': 0, 'negative': -1})
    pd.to_numeric(df['sentiment'])
    return df
