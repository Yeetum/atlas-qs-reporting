import pandas as pd

def parse_df(filepath, date_format):
  df = pd.read_csv(filepath, header=None)
  df[2] = df[1].pct_change()
  df.columns = ['index', 'price', 'pct_change']
  if date_format == 'date':
    df['index'] = df['index'].apply(lambda x : pd.to_datetime(x)) #edit T to add the time datetime format
  elif date_format == 'timestamp':
    df['index'] = df['index'].apply(lambda x : pd.Timestamp(x+'T00')) #edit T to add the time, ex. T01 is 01:00:00, Timestamp format
  df.index = df.pop('index')
  df.pop('price')
  df = df.dropna()
  return df