import pandas as pd
from scipy.stats import ttest_rel
#Read the data set
df = pd.read_csv("Concrete.csv")
#display column names
print("Dataset columns:", df.columns.tolist())
#Extract concrete strength after 2and 7 days
Day2 = df["Day2"]
Day7 = df["Day7"]
#Calculate the mean strength
mean_day2 = day2.mean()
mean_day7 = day7.mean()

print("\nMean strenggth after 2 days:",mean_day2)
print("Mean strength after 7 days:", mean_day7)

#Set the significance level
alpha = 0.01
#Perform paired t-test
t_stat, p_value = ttest_rel(
    day2,
    day7,
    alternative="less"
)
print("\nT-statistic:", t_stat)
print("P-value:", p-value)
#Make the decision
if p_value: < alpha:
    print("\nreject the null hypothesis.")
    print("there is sufficient evidence that mean strength")
    print("at 2 days is loer than at 7 days.")
    else:
        print("\nFail to reject the null hypothesis.")
        print("There is insufficient evidence that mean strength")
        print("at 2 days is lower than at 7 days.")