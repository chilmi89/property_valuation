import json

notebook_path = '/home/syelha/Documents/pns_2026/kelompok/SalesHouse/Valuasi_Properti_SVR.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Remove redundant df = pd.read_csv in cells other than the setup cell (index 2)
for i, cell in enumerate(nb['cells']):
    if i == 2: continue # Keep setup cell
    if cell['cell_type'] == 'code':
        cell['source'] = [line for line in cell['source'] if 'pd.read_csv' not in line]

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
