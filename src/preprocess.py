import pandas as pd
import numpy as np
COL_TO_DROP=["CustomValueEstimate","CapitalOutstanding",
             "WrittenOff","Rebuilt","Converted","CrossBorder","NumberOfVehiclesInFleet"]

def preprocess_insurance_data(df)-> pd.DataFrame:
    """Preprocess the insurance dataset.
    ARgs:
        df (pd.DataFrame): Raw Insurance DataFrame 
    Returns:
        pd.DataFrame: Preprocessed Insurance DataFrame
    preprocesses the insurance dataset for EDA and modeling.
          - Drop sparse/uninformative columns 
          - Fill modarate missing Values
          - Add Loss Ratio column
          - Convert object columns to catagorical dtype

        """
    df=df.copy()
    # drop columns with a lot of missing values
    for col in COL_TO_DROP:
        if col in df.columns:
            df = df.drop(columns=col)
    # create Loss Ration Column
    df['LossRatio'] =df['TotalClaims']/df['TotalPremium']
    df['LossRatio'] = df['LossRatio'].replace([np.inf, -np.inf], np.nan)
    # Fill missing Catagorical value with mode
    cat_cols=df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
        df[col]= df[col].astype('category') # convert to catagorical dtype
    # Fill missing Numeric values with median
    num_cols=df.select_dtypes(include=['int64','float64']).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
    # Fill missing Boolean value with mode
    bool_cols=df.select_dtypes(include=['bool']).columns
    for col in bool_cols:
        df[col]= df[col].fillna(df[col].mode()[0])
    return df
 
    