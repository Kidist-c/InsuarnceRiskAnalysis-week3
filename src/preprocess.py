import pandas as pd
import numpy as np

# Columns to drop due to excessive missingness or irrelevance
COL_TO_DROP = [
    "CustomValueEstimate", "CapitalOutstanding",
    "WrittenOff", "Rebuilt", "Converted",
    "CrossBorder", "NumberOfVehiclesInFleet"
]

def preprocess_insurance_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the insurance dataset for EDA and modeling.
    
    Steps performed:
    - Drop sparse/uninformative columns
    - Fill moderate missing values
    - Add LossRatio column
    - Convert object columns to categorical dtype
    - Clean string columns (strip whitespace)
    - Ensure boolean columns are correctly filled
    - Ensure numeric columns have no missing values

    Args:
        df (pd.DataFrame): Raw insurance data
    
    Returns:
        pd.DataFrame: Preprocessed insurance data
    """
    df = df.copy()

    # ----------------------
    # 1️⃣ Drop sparse/uninformative columns
    # ----------------------
    for col in COL_TO_DROP:
        if col in df.columns:
            df = df.drop(columns=col)

    # ----------------------
    # 2️⃣ Create LossRatio column
    # ----------------------
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    df['LossRatio'] = df['LossRatio'].replace([np.inf, -np.inf], np.nan)

    # ----------------------
    # 3️⃣ Fill and convert categorical columns
    # ----------------------
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        # Strip whitespace
        df[col] = df[col].str.strip()
        # Fill missing with mode
        df[col] = df[col].fillna(df[col].mode()[0])
        # Convert to category
        df[col] = df[col].astype('category')

    # ----------------------
    # 4️⃣ Fill numeric columns with median
    # ----------------------
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    # ----------------------
    # 5️⃣ Fill boolean columns with mode
    # ----------------------
    bool_cols = df.select_dtypes(include=['bool']).columns
    for col in bool_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df
