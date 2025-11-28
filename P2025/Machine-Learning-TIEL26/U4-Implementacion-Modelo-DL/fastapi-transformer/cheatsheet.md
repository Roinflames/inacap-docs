docker build --network=host -t fastapi-transformer .

docker run -p 8000:8000 fastapi-transformer

curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "El producto es excelente"}'

docker system prune -a
