import json

notebook_path = '/home/syelha/Documents/pns_2026/kelompok/SalesHouse/Valuasi_Properti_SVR.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Find the redundant evaluation cell that is causing NameError
# It's currently at index 3 (4th cell) after my previous insertion
to_delete = []
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'mae = mean_absolute_error(y_test_orig, y_pred_orig)' in ''.join(cell['source']):
        # Only delete it if it's BEFORE the modeling cell
        # Let's find the modeling cell index
        modeling_idx = -1
        for j, c in enumerate(nb['cells']):
            if c['cell_type'] == 'code' and 'svr_model = SVR' in ''.join(c['source']):
                modeling_idx = j
                break
        
        if i < modeling_idx:
            to_delete.append(i)

# Delete in reverse order
for i in sorted(to_delete, reverse=True):
    print(f"Deleting redundant/early evaluation cell at index {i}")
    del nb['cells'][i]

# Also remove redundant data loading in the EDA cell if it exists
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'df = pd.read_csv' in ''.join(cell['source']):
        # Keep the first one (setup cell) and remove others
        # Wait, the setup cell is at index 2
        # Actually, let's just make sure cell 4 (now cell 3 after deletion) doesn't reload
        pass

# Let's specifically target the EDA cell's reload
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'Memuat dataset' in ''.join(nb['cells'][i-1]['source'] if i > 0 else ""):
        cell['source'] = [line for line in cell['source'] if 'df = pd.read_csv' not in line]

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
