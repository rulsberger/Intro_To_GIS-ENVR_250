import pandas as pd 
class HealthCondition:
    def __init__(self,HealthCode, HealthDescription, Comments) -> None:
        self.HealthCode = HealthCode
        self.HealthDescription = HealthDescription  
        self.Comments = Comments 

code = [0, 1, 2, 3]
description = ['poor', 'fair', 'good', 'excellent']
comments = ["real bad shape", "could use more prey", "goood access to prey", "this ones fat"]

conditions = []

for k,v,d in zip(code, description, comments):
    conditions.append(HealthCondition(k,v,d).__dict__)
    
conditions_df = pd.DataFrame(conditions)
conditions_df.head()
conditions_df.to_csv("conditions.csv")