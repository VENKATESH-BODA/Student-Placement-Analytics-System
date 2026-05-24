# STUDENT PLACEMENT ANALYTICS SYSTEM

# Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# STEP 1 — LOAD DATASET

print("Loading Dataset...\n")

# Load Excel Dataset
df = pd.read_excel("../data/placement_data.xlsx")

# Show First 5 Rows
print("FIRST 5 ROWS OF DATASET")
print(df.head())

print("\n====================================\n")

# STEP 2 — DATASET INFORMATION

print("DATASET INFORMATION")
print(df.info())

print("\n====================================\n")

# STEP 3 — CHECK NULL VALUES

print("CHECKING NULL VALUES")
print(df.isnull().sum())

print("\n====================================\n")

# STEP 4 — DATA CLEANING

print("CLEANING DATA...\n")

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove completely empty rows
df.dropna(how='all', inplace=True)

# Fill text columns
df['Student Name'].fillna("Unknown", inplace=True)
df['Skills'].fillna("Unknown", inplace=True)
df['Company'].fillna("Unknown", inplace=True)
df['Branch'].fillna("Unknown", inplace=True)

# Fill numeric columns
df['CGPA'].fillna(0, inplace=True)
df['Package (LPA)'].fillna(0, inplace=True)

# Convert columns to numeric
df['CGPA'] = pd.to_numeric(
    df['CGPA'],
    errors='coerce'
)

df['Package (LPA)'] = pd.to_numeric(
    df['Package (LPA)'],
    errors='coerce'
)

print("DATA CLEANING COMPLETED")

print("\n====================================\n")

# STEP 5 — BASIC STATISTICS

print("BASIC STATISTICS")
print(df.describe())

print("\n====================================\n")

# STEP 6 — TOTAL STUDENTS

total_students = len(df)

print(f"TOTAL STUDENTS : {total_students}")

print("\n====================================\n")

# STEP 7 — BRANCH-WISE STUDENT COUNT

print("BRANCH-WISE STUDENT COUNT\n")

branch_count = df['Branch'].value_counts()

print(branch_count)

print("\n====================================\n")

# STEP 8 — AVERAGE CGPA BY BRANCH

print("AVERAGE CGPA BY BRANCH\n")

cgpa_avg = df.groupby('Branch')['CGPA'].mean()

print(cgpa_avg)

print("\n====================================\n")

# STEP 9 — TOP SKILLS ANALYSIS

print("TOP SKILLS ANALYSIS\n")

skills_count = df['Skills'].value_counts()

print(skills_count)

print("\n====================================\n")

# STEP 10 — COMPANY ANALYSIS

print("TOP RECRUITING COMPANIES\n")

company_count = df['Company'].value_counts()

print(company_count)

print("\n====================================\n")

# STEP 11 — PACKAGE ANALYSIS

df['Package (LPA)'] = pd.to_numeric(
    df['Package (LPA)'],
    errors='coerce'
)

highest_package = df['Package (LPA)'].max()

average_package = df['Package (LPA)'].mean()

print(f"HIGHEST PACKAGE : {highest_package} LPA")

print(f"AVERAGE PACKAGE : {average_package:.2f} LPA")

print("\n====================================\n")

# STEP 12 — TOP 5 STUDENTS BY CGPA

print("TOP 5 STUDENTS BY CGPA\n")

top_students = df.sort_values(
    by='CGPA',
    ascending=False
)

print(
    top_students[
        ['Student Name', 'CGPA', 'Branch']
    ].head()
)

print("\n====================================\n")

# STEP 13 — BRANCH COUNT VISUALIZATION

plt.figure(figsize=(8, 5))

branch_count.plot(kind='bar')

plt.title("Students by Branch")

plt.xlabel("Branch")

plt.ylabel("Number of Students")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()

# STEP 14 — CGPA DISTRIBUTION

plt.figure(figsize=(8, 5))

plt.hist(df['CGPA'], bins=10)

plt.title("CGPA Distribution")

plt.xlabel("CGPA")

plt.ylabel("Number of Students")

plt.tight_layout()

plt.show()

# STEP 15 — PACKAGE DISTRIBUTION

plt.figure(figsize=(8, 5))

df['Package (LPA)'].dropna().plot(kind='hist')

plt.title("Package Distribution")

plt.xlabel("Package (LPA)")

plt.ylabel("Students")

plt.tight_layout()

plt.show()

# STEP 16 — PROJECT INSIGHTS

print("PROJECT INSIGHTS\n")

print("1. Branch with highest students :")
print(branch_count.idxmax())

print("\n2. Branch with highest average CGPA :")
print(cgpa_avg.idxmax())

print("\n3. Highest package offered :")
print(highest_package)

print("\n4. Most common skill :")
print(skills_count.idxmax())

print("\n5. Top recruiting company :")
print(company_count.idxmax())

print("\n====================================\n")

# STEP 17 — EXPORT CLEANED DATA

df.to_excel(
    "../reports/cleaned_placement_report.xlsx",
    index=False
)

print("CLEANED REPORT EXPORTED SUCCESSFULLY")

print("\n====================================\n")

# PROJECT COMPLETED

print("STUDENT PLACEMENT ANALYTICS COMPLETED SUCCESSFULLY")