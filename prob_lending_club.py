import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)
loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplot")
loansData.hist(column='Amount.Requested')
plt.savefig("Histogram")
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("QQ")
print("The Amount Requested data is very similar to the amound funded. They both have the same median and are right tailed while not being normally distributed.")