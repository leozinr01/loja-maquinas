import pandas as pd


def export_to_excel(filename, df: pd.DataFrame):
    with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Relatório")
