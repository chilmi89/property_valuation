import json

notebook_path = '/home/syelha/Documents/pns_2026/kelompok/SalesHouse/Valuasi_Properti_SVR.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Define the new setup cell
new_setup_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "from sklearn.svm import SVR\n",
        "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, f1_score\n",
        "\n",
        "# Load Dataset\n",
        "df = pd.read_csv('data/kc_house_data.csv')\n",
        "print('Dataset berhasil dimuat. Siap untuk pemrosesan.')"
    ]
}

# Find the insertion point: after "### 1. Setup & Inisialisasi"
# We'll look for the markdown cell with that text.
insert_idx = 0
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and '### 1. Setup & Inisialisasi' in ''.join(cell['source']):
        insert_idx = i + 1
        break

# Insert the new setup cell
nb['cells'].insert(insert_idx, new_setup_cell)

# Now fix the evaluation cell
# It should be further down. Let's look for "mean_absolute_error"
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if any('mean_absolute_error' in line for line in source):
            # Remove the redundant import if it exists
            cell['source'] = [line for line in source if 'from sklearn.metrics import f1_score' not in line]

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
