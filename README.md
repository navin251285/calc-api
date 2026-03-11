# calc-api

Simple FastAPI calculator API.

## Project Structure

```text
calc-api
|
|-- app
|   `-- main.py
|
|-- requirements.txt
|-- Dockerfile
`-- README.md
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
uvicorn app.main:app --reload --port 8000
```

## Test

Open:

`http://localhost:8000/sum?a=3&b=4`

Expected response:

```json
{"result": 7}
```