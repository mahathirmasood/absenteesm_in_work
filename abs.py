import pandas as pd
data = pd.read_csv('Absenteeism_data.csv')
data = data.copy()
data = data.drop(['ID'], axis=1)
print(sorted(data['Reason for Absence'].unique()))
