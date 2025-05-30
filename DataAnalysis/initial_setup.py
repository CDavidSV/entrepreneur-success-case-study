import pandas as pd
from pandasgui import show
import unicodedata
import sys
sys.stdout.reconfigure(encoding='utf-8')

relevant_columns_cleaned = {
    "Overall_Mental": "mental_health",
    "Happiness": "happiness",
    "life_satisfaction": "life_satisfaction",
    "Worthwhile": "purpose_worth",
    "Life_Purpose": "life_purpose",
    "Good_Circumstances": "act_for_good",
    "Greater_Happiness_Later": "delay_gratification",
    "Content_Friends": "relationship_content",
    "Satisfying_Relationships": "relationship_satisfaction",
    "Normal_Monthly_Living": "financial_stress",
    "Worryness": "survival_stress",

    "living country": "living_country",
    "In which state do you live?": "living_state",
    "nationality": "nationality",

    "founded_company": "founded_company",
    "How many organizations have you founded?": "num_founded",
    "How many are still in operation (actives)?": "num_active",
    "area_org_1": "org1_area",
    "Foundation_Year_Org_1": "org1_year",
    "operation_years_org_1": "org1_years_op",
    "Num_Emp_Org_1": "org1_employees",
    "Country_Org_1": "org1_country",

    "AGE": "age",
    "How many hours do you usually work per week?": "hours_worked",
    "Gender": "gender",
    "nivel_descripcion": "education_level",
    "Have you completed postgraduate studies?": "postgrad"
}



df = pd.read_csv("./DataAnalysis/data.csv", encoding='utf-8', low_memory=False)
df = df.rename(columns=relevant_columns_cleaned)[list(relevant_columns_cleaned.values())]

founders_df = df[df["founded_company"].str.lower() == "yes"]

show(founders_df)
