import pandas as pd
import numpy as np
from pandasgui import show


df = pd.read_csv("./data.csv", encoding="latin1",low_memory=False)

df = df.where(pd.notna(df), None)

for col in df.columns:
    print(f"'{col}',")

relevant_columns = {
    "Please rate each of the following statements using the appropiare scale:  How would you rate your overall mental health?\n Where 1= very poor mental health, 10= excellent mental health": "mental_health",
    "Please rate each of the following statements using the appropiare scale:  In general, how happy or unhappy do you usually feel?\n extremely unhappy:Where 1=Extremely unhappy, 10=Extremely happy": "happiness",
    "Please rate each of the following statements using the appropiare scale:  Overall, how satisfied are you with life as a whole these days??\n Where 1 = Not satisfied at all, 10 = Completely Satisfied": "life_satisfaction",
    "Please rate each of the following statements using the appropiare scale:  IOverall, to what extent do you feel the things you do in your life are worthwhile? \n Where 1 is = Not at All Worthwhile, and 10 = Completely Worthwhile": "purpose_worth",
    "Please rate each of the following statements using the appropiare scale:  I understand my purpose in life \n Where 1 = strongly disagree, 10 = Strongly agree": "life_purpose",
    "Please rate each of the following statements using the appropiare scale:  I always act to promote good in all circumstances, even in difficult and challenging  situations \n Where 1= Not true about me, 10 = Completely true about me": "act_for_good",
    "Please rate each of the following statements using the appropiare scale:  I am always able to give up some happiness now for greater happiness later.\n Where 1= not true of me, 10 = totally true of me": "delay_gratification",
    "Please rate each of the following statements using the appropiare scale:  I am content with my friendships and relationships.\n Where 1 = strongly disagree, 10= Totally agree": "relationship_content",
    "Please rate each of the following statements using the appropiare scale:  My relationships are as satisfying as I would want them to be \n Where 1= strongly disagree, 10= Totally agree": "relationship_satisfaction",
    "Please rate each of the following statements using the appropiare scale:  How often do you worry about being able to meet normal monthly living expenses?\n Where 1= worry all of the time, 10= Do not ever worry": "financial_stress",
    "Please rate each of the following statements using the appropiare scale:  How often do you worry about safety, food, or housing?\n Where 1= worry all the time, 10= Do not ever worry": "survival_stress",

    "living country": "living_country",
    "In which state do you live?": "living_state",
    "nationality": "nationality",

    "Since graduating from Tecnológico de Monterrey, have you founded a company, either as part of the group of partners or as owner? By partner we mean those who contributed money and/or work to start the company": "founded_company",
    "How many organizations have you founded?": "num_founded",
    "How many are still in operation (actives)?": "num_active",
    "Por favor, nos puede proporcionar la siguiente información de las principales organizaciones soci...  Area  organization 1": "org1_area",
    "Por favor, nos puede proporcionar la siguiente información de las principales organizaciones soci...  Foundation year  organization 1": "org1_year",
    "Por favor, nos puede proporcionar la siguiente información de las principales organizaciones soci...  # of years in operation  organization 1": "org1_years_op",
    "Por favor, nos puede proporcionar la siguiente información de las principales organizaciones soci...  Number of employees in the last year  organization 1": "org1_employees",
    "Por favor, nos puede proporcionar la siguiente información de las principales organizaciones soci...  Country  organization 1": "org1_country",

    "AGE": "age",
    "How many hours do you usually work per week?": "hours_worked",
    "Gender": "gender",
    "nivel_descripción": "education_level",
    "Have you completed postgraduate studies?": "postgrad"
}

df_relevant = df[relevant_columns.keys()].rename(columns=relevant_columns)
wellbeing_cols = [
    'mental_health', 'happiness', 'life_satisfaction', 'purpose_worth',
    'life_purpose', 'act_for_good', 'delay_gratification',
    'relationship_content', 'relationship_satisfaction',
    'financial_stress', 'survival_stress'
]

for col in wellbeing_cols:
    df_relevant[col] = pd.to_numeric(df_relevant[col], errors='coerce')
df_relevant["founded_company"] = df_relevant["founded_company"].str.strip().str.lower()
df_relevant["founded_company"] = df_relevant["founded_company"].map({
    "yes": 1, "no": 0
})

df_founders = df_relevant[df_relevant['founded_company'] == 1]

show(df_founders)