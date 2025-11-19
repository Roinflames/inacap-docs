# pipenv install "huggingface-hub<1.0,>=0.23.2" 
# pipenv install "transformers==4.41.2"
# pipenv install "evaluate==0.4.0"
import sys
print(sys.executable)
print(sys.version)

import huggingface_hub
import transformers

print("huggingface-hub:", huggingface_hub.__version__)
print("transformers:", transformers.__version__)

# 2. Importar librerías (0.6s)
import evaluate
accuracy = evaluate.load("accuracy")
accuracy.compute(predictions=[1,0,1], references=[1,0,0])

# 3. Cargar dataset (9.3s)
# dataset = load_dataset("imdb")
# dataset["train"][0]

# 4. Cargar modelo preentrenado (9.1s)
# model_name = "distilbert-base-uncased"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# 5. Tokenización (30s)
# def tokenize_fn(example):
#     return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

# tokenized = dataset.map(tokenize_fn, batched=True)

# 6. Proceso de entrenamiento, evaluación y selección del mejor modelo 
# usando la clase Trainer de HuggingFace (20m 39s +)
# from transformers import TrainingArguments, Trainer, IntervalStrategy
# import evaluate
# import numpy as np

# import os
# os.environ["WANDB_DISABLED"] = "true"
# accuracy = evaluate.load("accuracy")

# def compute_metrics(eval_pred):
#     logits, labels = eval_pred
#     predictions = np.argmax(logits, axis=-1)
#     return accuracy.compute(predictions=predictions, references=labels)

# args = TrainingArguments(
#     output_dir="./results",
#     save_strategy="epoch",
#     #
#     eval_strategy="epoch",  # Cambiado de evaluation_strategy
#     learning_rate=2e-5,
#     per_device_train_batch_size=16,
#     per_device_eval_batch_size=16,
#     num_train_epochs=3,
#     weight_decay=0.01,
#     load_best_model_at_end=True,
#     metric_for_best_model="accuracy",
#     logging_dir='./logs',
#     logging_steps=10,
# )

# trainer = Trainer(
#     model=model,
#     args=args,
#     train_dataset=tokenized["train"].shuffle(seed=42).select(range(2000)),
#     eval_dataset=tokenized["test"].shuffle(seed=42).select(range(500)),
#     compute_metrics=compute_metrics,
# )

# trainer.train()

# 6.5 Guardar Modelo 
# model.save_pretrained("./modelo_entrenado")
# tokenizer.save_pretrained("./modelo_entrenado")

# 7. Evaluación
# trainer.evaluate()

# Si quieres probar el modelo ya guardado, por ejemplo después de reiniciar el runtime:
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("./modelo_entrenado")
tokenizer = AutoTokenizer.from_pretrained("./modelo_entrenado")

# Y luego puedes ejecutar tus bloques 8 y 9 sin cambiar nada.

# 8. Prueba con texto nuevo
text = "This movie was absolutely amazing!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
pred = outputs.logits.argmax().item()
print("Positiva" if pred == 1 else "Negativa")

# 9. Prueba con texto nuevo
text = "This movie was absolutely shitty!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
pred = outputs.logits.argmax().item()
print("Positiva" if pred == 1 else "Negativa")