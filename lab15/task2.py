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
print(fixed_df[:3])
fixed_df.plot(figsize=(15, 10))
plt.show()