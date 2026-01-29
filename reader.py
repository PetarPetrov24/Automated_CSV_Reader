import pandas as pd

def read_csv(file):
    if file is None:
        return None
    try:
        data_frame = pd.read_csv(file)
        return pd.read_csv(file)
    except FileNotFoundError:
        print(f"File {file} not found!")
        return None


