"""
Marketing Campaign Performance Dataset - Data Cleaning Script
Criteo Data Analyst Internship Project

Ye script raw CSV ko clean karke Power BI / SQL ke liye ready banata hai.
"""

import pandas as pd
import numpy as np

# ============================================
# STEP 1: LOAD DATA
# ============================================
df = pd.read_csv('marketing_campaign_dataset.csv')
print("Original shape:", df.shape)
print("\nOriginal dtypes:\n", df.dtypes)

# ============================================
# STEP 2: CLEAN ACQUISITION_COST
# "$16,174.00" -> 16174.00
# ============================================
df['Acquisition_Cost'] = (
    df['Acquisition_Cost']
    .replace(r'[\$,]', '', regex=True)
    .astype(float)
)

# ============================================
# STEP 3: CLEAN DURATION
# "30 days" -> 30
# ============================================
df['Duration_Days'] = (
    df['Duration']
    .str.extract(r'(\d+)')
    .astype(int)
)
df.drop('Duration', axis=1, inplace=True)

# ============================================
# STEP 4: CONVERT DATE
# ============================================
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
df['Month_Num'] = df['Date'].dt.month
df['Day_of_Week'] = df['Date'].dt.day_name()
df['Quarter'] = df['Date'].dt.quarter

# ============================================
# STEP 5: DROP DUPLICATES
# ============================================
before = len(df)
df.drop_duplicates(inplace=True)
print(f"\nDuplicates removed: {before - len(df)}")

# ============================================
# STEP 6: FEATURE ENGINEERING (KPI Columns)
# ============================================

# CTR = Clicks / Impressions * 100
df['CTR_%'] = (df['Clicks'] / df['Impressions']) * 100

# Cost Per Click
df['CPC'] = df['Acquisition_Cost'] / df['Clicks']

# Estimated conversions (Conversion_Rate is a %, apply to Clicks)
df['Estimated_Conversions'] = (df['Conversion_Rate'] / 100) * df['Clicks']

# Cost per estimated conversion
df['Cost_Per_Conversion'] = df['Acquisition_Cost'] / df['Estimated_Conversions'].replace(0, np.nan)

# Engagement Rate (Engagement Score is 1-10 scale as given, keep as is, but normalize view)
df['Engagement_Level'] = pd.cut(
    df['Engagement_Score'],
    bins=[0, 3, 6, 10],
    labels=['Low', 'Medium', 'High']
)

# ROI performance bucket
df['ROI_Category'] = pd.cut(
    df['ROI'],
    bins=[-np.inf, 0, 3, 6, np.inf],
    labels=['Negative', 'Low', 'Medium', 'High']
)

# ============================================
# STEP 7: HANDLE INFINITE / NaN FROM DIVISIONS
# ============================================
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df['Cost_Per_Conversion'] = df['Cost_Per_Conversion'].fillna(0)

# ============================================
# STEP 8: FINAL CHECK
# ============================================
print("\nFinal shape:", df.shape)
print("\nFinal columns:", list(df.columns))
print("\nNull check:\n", df.isnull().sum())
print("\nSample rows:\n", df.head())

# ============================================
# STEP 9: SAVE CLEANED DATA
# ============================================
df.to_csv('marketing_campaign_cleaned.csv', index=False)
print("\n✅ Cleaned file saved as 'marketing_campaign_cleaned.csv'")
print(f"Ready for Power BI / SQL import — {df.shape[0]} rows, {df.shape[1]} columns")
