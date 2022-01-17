from fastapi import FastAPI
from models import BMI
import uvicorn
import numpy as np

app = FastAPI()


@app.get("/")
def read_root():
    return {"project": "Python BMi-Calculator"}

@app.post("/")
def get_bmi(body: BMI):   
    """
    Height : float in cm \n
    Weight : float in kg
    """
    bmi=  int(body.weight / (body.height/100)**2) 
    
    condition = {        25 : "You are healthy",
        30 : "You are overweight",
    }
    
    condlist = [bmi <= 25, bmi <= 30]
    resultlist = ["You are healthy", "You are overweight"]
    result = str(np.select(condlist, resultlist, "You are obese"))
        
    return {"Condition" : result}
    

uvicorn.run(app,port=8000)