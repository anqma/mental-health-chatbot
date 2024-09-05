import os
import pandas as pd
import minsearch

DATA_PATH = os.getenv("DATA_PATH", "../data/Mental_Health_FAQ.csv")


def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path)
    documents = df.to_dict(orient="records")

    index = minsearch.Index(text_fields=["Questions", "Answers"], keyword_fields=[])

    index.fit(documents)

    return index
