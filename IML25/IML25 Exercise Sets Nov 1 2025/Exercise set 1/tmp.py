most_common_class = df['class4'].value_counts().idxmax()
p = len(df) - df['class4'].value_counts()['nonevent'] / len(df)

test = pd.read_csv("test.csv")
submission = pd.DataFra