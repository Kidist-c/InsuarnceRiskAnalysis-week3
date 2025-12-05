import pandas as pd

# Columns for different types
DATE_COLS = ["TransactionMonth", "VehicleIntroDate"]

# Boolean columns that are stored as Yes/No strings
BOOL_STR_COLS = [ "WrittenOff", "Rebuilt", "Converted","CrossBorder"]

# Boolean columns already True/False
BOOL_BOOL_COLS = ["IsVATRegistered"]

# Numeric columns
NUMERIC_COLS = [
    "mmcode","Cylinders","cubiccapacity","kilowatts","NumberOfDoors",
    "CustomValueEstimate","CapitalOutstanding","NumberOfVehiclesInFleet",
    "SumInsured","CalculatedPremiumPerTerm","TotalPremium","TotalClaims"
]

def load_insurance_data(filepath: str) -> pd.DataFrame:
    """
    Loads the insurance dataset, converts datatypes, and prepares it for analysis.
    
    Parameters
    ----------
    filepath : str
        Path to the pipe-separated .txt file.
    
    Returns
    -------
    pd.DataFrame
        DataFrame ready for EDA, with safe types.
    """
    
    # Load data
    df = pd.read_csv(filepath, sep="|", header=0)
    
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    # Strip whitespace from string/object columns
    obj_cols = df.select_dtypes(include='object').columns
    for col in obj_cols:
        df[col] = df[col].str.strip()
    
    # Convert date columns
    for col in DATE_COLS:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Convert numeric columns
    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Convert boolean string columns (Yes/No -> True/False)
    for col in BOOL_STR_COLS:
        df[col] = df[col].map({'Yes': True, 'No': False})
    
    # Ensure boolean columns that are already True/False
    for col in BOOL_BOOL_COLS:
        df[col] = df[col].astype(bool)
    
    return df
