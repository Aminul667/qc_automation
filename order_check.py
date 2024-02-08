import pandas as pd

data_path = r''
data_path_on_windows = data_path.replace('\\', '/')

disl_path = r''
disl_path_on_windows = disl_path.replace('\\', '/')

df = pd.read_csv(data_path_on_windows, sep=';')
disl = pd.read_excel(disl_path_on_windows, sheet_name='Sheet1')

variables_from_data = df.columns.to_list()
variables_from_disl = disl['variables'].to_list()

for i, variable in enumerate(variables_from_disl):
    if variables_from_data[i] == variable:
        print(f'{i+1} OK -> {variable} = {variables_from_data[i]}')
    else:
        print(f'{i+1} Caution: {variable} is not in order')