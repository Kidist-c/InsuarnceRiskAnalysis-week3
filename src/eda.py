# import libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


## create class for Eda
class InsuranceEDA:
    def __init__(self, df: pd.DataFrame):
       "" "Initialize the InsuranceEDA class with a Processed DataFrame."""
       self.df = df
       print("EDA Instance Created")
    # 1. DATA SUMMIRIZATION
    def data_summary(self):
        """ Generate a summsry of DataFrame including data types,
        shape,missing values and basic staistics"""
        print(f"Data Shape: {self.df.shape}")
        print(f"\nData Types:{self.df.dtypes}")
        print(f"\nMissing Values:{self.df.isnull().sum()}")
        print(f"\nBasic Statisrics:{self.df.describe()}")
        print(f"Catagorical description:{self.df.describe(include=["category","object"])}")
    # 2.---UNIVARIANTE ANALYSIS--
    def univariante_analysis(self):
        """ Perform univariante analysis on numerical and catagorical features."""
        num_cols=self.df.select_dtypes(include=[np.number]).columns
        cat_cols=self.df.select_dtypes(include=["category","object"]).columns
        for col in num_cols:
            plt.figure(figsize=(6,4))
            sns.histplot(self.df[col],kde=True)
            plt.title(f"Distribution of {col}")
            plt.show()
        for col in cat_cols:
            plt.figure(figsize=(6,4))
            self.df[col].value_counts().plot(kind="bar")
            plt.title(f"Count plot of {col}")
            plt.show()
    # 3.---BIVARIANTE ANALYSIS--
    def bivariante_analysis(self):
        """ 
         Perform bivariante analysis between numerical and catagorical features.
        """
        # correlation matrix
        plt.figure(figsize=(6,4))
        sns.heatmap(self.df.corr(numeric_only=True),annot=True,cmap="Blues")
        plt.title("Correlation Heatmap")
        plt.show()
        # Scatter:Premium Vs Claims by Zipcode
        if "ZipCode" in self.df.columns:
            plt.figure(figsize=(8,6))
            sns.scatterplot(data=self.df,x="TotalPremium",y="TotalClaims",hue="ZipCode")
            plt.title("Total Premium Vs Total Claims colored By ZipCode")
            plt.show()
    # 4.---OUTLIER DETECTION--
    def outlier_detection(self):
        """ Detect Outliers in numerical feateures using boxplots."""
        num_cols=self.df.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            plt.figure(figsize=(6,4))
            sns.boxplot(x=self.df[col])
            plt.title(f"Boxplot of {col}")
            plt.show()
    # 5.---CREATIVE INSIGHT PLOTS--
    def creative_insight_plots(self):
        """ Generate creative plots to gain insights."""
        #Insight 1: Loss Ratio by province
        if "Province" in self.df.columns and "LossRatio"in self.df.columns:
            plt.figure(figsize=(8,6))
            sns.boxplot(data=self.df,x="Province",y="LossRatio")
            plt.title("Loss Ratio by Province")
            plt.show()
        #Insight 2: Claims Severity by Vehicle Type
        if "VehicleType" in self.df.columns and "TotalClaims" in self.df.columns:
            plt.figure(figsize=(8,6))
            sns.violinplot(data=self.df,x="VehicleType",y="TotalClaims")
            plt.title("Claims Severity by Vehicle Type")
            plt.show()
        #INsight 3: Monthly Trends
        if "PolicyStartDate" in self.df.columns and "TotalClaims" in self.df.columns:
            self.df["Month"]=self.df["PolicyStartDate"].dt.month
            Monthly=self.df.groupby("Month")["TotalClaims"].sum()
            plt.figure(figsize=(8,6))
            Monthly.plot(kind="line",marker="o")
            plt.title("Monthly Trends Of Total Claims")
            plt.xlabel("Month")
            plt.ylabel("Total Claims")
            plt.show()
     # 6.---RuN ALL EDA--
    def run_all_eda(self):
        """ Run all EDA methods sequentially."""
        self.data_summary()
        self.univariante_analysis()
        self.bivariante_analysis()
        self.outlier_detection()
        self.creative_insight_plots()
        print("All EDA Completed")


            
        







    
