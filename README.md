# Tecnologies

- Python 3.8
- Flask (for expose REST resources)
- Pytest (for test)

# How to start application

- Install flask library: `pip install flask`
- Start application: `python3 -m src.main`

# How to test application

- To test risk calculator, use a tools like Postman or use command below:

```json
curl --location --request POST 'localhost:5000/risk/calculate' \
--header 'Content-Type: application/json' \
--data-raw '{
  "age": 35,
  "dependents": 2,
  "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "married",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2018}
}'

```

# How to run unit test

- Install pytest library: `pip install pytest`
- Run tests: `pytest`
