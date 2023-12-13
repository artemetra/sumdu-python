import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)
fixed_df = pd.read_csv(
    "data.csv",
    sep=",",
    encoding="utf-8",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
fixed_df = fixed_df.drop(fixed_df.columns[[0]], axis=1)
print(fixed_df[:3])
fixed_df.plot(figsize=(15, 10))
plt.show()
agg_df = fixed_df.T.agg("sum").T
sum_over_months = agg_df.groupby(agg_df.index.month).sum()
sum_over_months.plot(figsize=(15, 10))
plt.show()