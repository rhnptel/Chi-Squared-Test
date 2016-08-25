from scipy import stats
import collections
import matplotlib.pyplot as plt
import pandas as pd
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
stats.chisquare(freq.values())