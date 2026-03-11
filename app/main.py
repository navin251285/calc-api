from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}
