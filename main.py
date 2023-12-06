from fastapi import FastAPI, Request
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def hello(request: Request):
    return {"message": "world"}

#  pip install fastapi uvicorn mangum   
# pip install -t dependencies -r requirements.txt   
# {cd dependencies; zip ../aws_lambda_artifact.zip -r .}
#  zip aws_lambda_artifact.zip -u main.py