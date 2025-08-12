import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# 1️⃣ Cargar datos
df = pd.read_csv("customer_segmentation.csv")

# Variables para clustering
features = ["purchase_frequency", "average_purchase", "loyalty_points", "months_active"]

X = df[features].values

# 2️⃣ Estandarizar variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3️⃣ Entrenar K-means
k = 3  # Cambia si quieres probar otro valor
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(X_scaled)

# 4️⃣ Calcular métricas
inertia = kmeans.inertia_
sil_score = silhouette_score(X_scaled, labels)

# 5️⃣ Obtener tamaños y centroides
sizes = np.bincount(labels)
centroids = kmeans.cluster_centers_

# 6️⃣ Crear salida en formato requerido (usando solo 2 primeras dimensiones como en tu ejemplo)
rows = []
for i in range(k):
    rows.append([f"cluster{i}_center_x", round(centroids[i, 0], 2)])  # primera variable estandarizada
    rows.append([f"cluster{i}_center_y", round(centroids[i, 1], 2)])  # segunda variable estandarizada

rows.append(["inertia", round(inertia, 2)])
rows.append(["silhouette_score", round(sil_score, 2)])
for i in range(k):
    rows.append([f"cluster{i}_size", float(sizes[i])])

# 7️⃣ Exportar CSV
df_out = pd.DataFrame(rows, columns=["ID", "value"])
df_out.to_csv("submission.csv", index=False)
print("✅ Archivo 'submission.csv' generado con éxito.")
