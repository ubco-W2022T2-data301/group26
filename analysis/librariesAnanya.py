def load_and_preprocess(path_to_csv_file):
    # Method Chain 1 (Load data)
    df = pd.read_csv(path_to_csv_file)

    # Method Chain 2 (deal with not used data)
    df2 = (
        df.drop(columns=['some_column_name'], errors='ignore')
          .dropna()
          .loc[:, ['G', 'xG', 'G - xG', 'xG90']]
    )

    return df2