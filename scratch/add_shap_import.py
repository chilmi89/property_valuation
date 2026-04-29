import json

notebook_path = '/home/syelha/Documents/pns_2026/kelompok/SalesHouse/Valuasi_Properti_SVR.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Find the setup cell (it should be at index 2)
setup_cell = nb['cells'][2]
source = setup_cell['source']

# Check if 'import shap' is already there (it shouldn't be)
if not any('import shap' in line for line in source):
    # Add it after seaborn or somewhere appropriate
    new_source = []
    for line in source:
        new_source.append(line)
        if 'import seaborn as sns' in line:
            new_source.append("import shap\n")
    setup_cell['source'] = new_source

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully with shap import.")
