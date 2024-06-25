# ==========
# LIBRAIRIES
# ==========

# import pickle
import os
import sys
import pandas as pd
from ydata_profiling import ProfileReport

# ==========
# CONSTANTES
# ==========

## Base de données
FILENAME_BASE_AUTO = "base_auto_projet.pkl"
DIR_DATA = "./data"

with open(file=os.path.join(DIR_DATA, FILENAME_BASE_AUTO), mode="rb") as f:
    base_auto = pd.read_pickle(f)

profile = ProfileReport(base_auto, title="Profiling Report - base_auto")
profile.to_file("./data_profiling.html")
