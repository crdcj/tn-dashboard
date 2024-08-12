import pandas as pd
from pathlib import Path
import pyarrow.feather as feather

DATA_PATH = Path("__file__").parent / "data"

# Load di data
DI_DATA_FILE = DATA_PATH / "di_dataset_st.feather"
df_di = feather.read_feather(DI_DATA_FILE)
df_di['expiration_mY'] = df_di['expiration'].dt.strftime('%m-%y')


# Configurações e constantes
RATES_URL = (
    "https://raw.githubusercontent.com/crdcj/pyield-data/main/anbima_rates.csv.gz"
)

df_rates = pd.read_csv(RATES_URL, parse_dates=["ReferenceDate", "MaturityDate"])
