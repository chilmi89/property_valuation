import json

notebook_path = '/home/syelha/Documents/pns_2026/kelompok/SalesHouse/Valuasi_Properti_SVR.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Find the SHAP cell
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'shap.KernelExplainer' in ''.join(cell['source']):
        # Optimization:
        # 1. Use kmeans for background (much faster)
        # 2. Reduce the number of instances to explain
        optimized_source = [
            "# Optimasi SHAP: Menggunakan kmeans untuk background dan mengurangi jumlah sampel\n",
            "# Hal ini akan mempercepat proses interpretasi secara signifikan\n",
            "print(\"Menghitung SHAP values (Optimized)... Mohon tunggu.\")\n",
            "background_summary = shap.kmeans(X_train_scaled, 10) # 10 cluster jauh lebih cepat dari 100 random samples\n",
            "explainer = shap.KernelExplainer(svr_model.predict, background_summary)\n",
            "\n",
            "# Hitung untuk 30 sampel saja (sudah cukup untuk melihat tren fitur)\n",
            "shap_values = explainer.shap_values(X_test_scaled[:30], nsamples=100) \n",
            "\n",
            "plt.figure(figsize=(10, 6))\n",
            "plt.title(\"Interpretasi SHAP: Fitur Pendukung Harga Properti (Top 30 Samples)\")\n",
            "shap.summary_plot(shap_values, X_test.iloc[:30], feature_names=features)\n"
        ]
        cell['source'] = optimized_source

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("SHAP cell optimized successfully.")
