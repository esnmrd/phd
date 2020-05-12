#%% [markdown]
# ## Analysis of Covariance (ANCOVA)
# ### Ehsan Moradi, Ph.D. Candidate

#%% [markdown]
# ### Load required libraries
import pandas as pd
import matplotlib.pyplot as plt
import pingouin as pg
from scipy import stats

#%% [markdown]
# ### Load data from Excel to a pandas dataframe
def load_sample_from_Excel():
    directory = "../../../Google Drive/Academia/PhD Thesis/Charts, Tables, Forms, Flowcharts, Spreadsheets/"
    input_file = "Paper I - SVR and ANN Results.xlsx"
    input_path = directory + input_file
    sheets_dict = pd.read_excel(
        input_path, sheet_name=["SVR - ANCOVA", "ANN - ANCOVA"], header=0
    )
    df_svr = sheets_dict["SVR - ANCOVA"]
    df_ann = sheets_dict["ANN - ANCOVA"]
    return df_svr, df_ann


#%% [markdown]
# ### Perform the ANCOVA
df_svr, df_ann = load_sample_from_Excel()
# stats.normaltest(df_svr["AGE"])
pg.ancova(
    data=df_svr, dv="SCORE", covar="ENGINE_DISPLACEMENT", between="CAR_SEGMENT",
)