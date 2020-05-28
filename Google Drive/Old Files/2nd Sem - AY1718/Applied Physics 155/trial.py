import pandas as pd

file = "MacbethColorChecker.xslx"
x1 = pd.read_excel(file)
print(x1.columns)