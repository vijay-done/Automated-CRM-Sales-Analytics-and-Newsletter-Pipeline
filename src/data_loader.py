from pathlib import Path
import pandas as pd


def load_data():
    """
    Load the CRM Excel dataset and return it as a DataFrame.
    """

    project_path = Path(__file__).resolve().parent.parent

    excel_path = project_path / "data" / "CRM_Sales_Operations_2026.xlsx"

    df = pd.read_excel(excel_path)

    return df
