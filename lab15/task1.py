import pandas as pd

heights = {
    "Ellie Clarson": [173, "F"],
    "Ben Jenkins": [170, "M"],
    "Tom Smith": [162, "M"],
    "Julie Rose": [183, "F"],
    "Kirill Sawyer": [151, "F"],
    "Jimmy Kim": [179, "M"],
    "Kylie Johnes": [165, "M"],
    "James Jennar": [191, "M"],
    "Lisa Groot": [169, "F"],
    "Alan Alison": [159, "M"],
}


def none_func(*x):
    return None


df_T = pd.DataFrame(heights).T
df_T.columns = ("height", "gender")
print(df_T)
print("\n")
print(df_T.agg({"height": ["mean"], "gender": ["mode"]}))
