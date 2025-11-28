# === 1️⃣ Instalación y setup ===
# !pip install --upgrade sagemaker boto3

import boto3
import sagemaker
from sagemaker import get_execution_role
import os
import io
import pickle, gzip
import numpy as np
import sagemaker.amazon.common as smac
import matplotlib.pyplot as plt

# %matplotlib inline
plt.rcParams["figure.figsize"] = (2,10)

# Sesión SageMaker local
sess = sagemaker.LocalSession()
sess.config = {"local": {"local_code": True}}

# Bucket S3 (opcional, solo si quieres subir datos o resultados)
bucket = sess.default_bucket()
prefix = "sagemaker/DEMO-linear-mnist"

# Role requerido por SageMaker (no importa en local)
role = "SageMakerLocalRole"

# Bucket SageMaker con MNIST de ejemplo
region = boto3.Session().region_name
downloaded_data_bucket = f"sagemaker-example-files-prod-{region}"
downloaded_data_prefix = "datasets/image/MNIST"
