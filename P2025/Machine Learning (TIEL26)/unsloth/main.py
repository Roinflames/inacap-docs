from unsloth import FastLanguageModel

# Carga un modelo base compatible
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/mistral-7b-bnb-4bit",
    max_seq_length = 2048,
    dtype = None,  # Usa la mejor precisión disponible automáticamente
    load_in_4bit = True,  # Optimiza memoria y velocidad
)

# Ejemplo de inferencia
inputs = tokenizer("Hola, ¿cómo estás?", return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
