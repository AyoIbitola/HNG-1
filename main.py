from fastapi import FastAPI, Query,status
import math
from utils import *
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

def get_fun_fact(n : int):
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available"

@app.get("/api/classify-number",status_code=status.HTTP_200_OK)
async def get_properties(number : str= Query(..., title="Number", description="Please enter a number")):

    try:
        n = int(number)  
    except ValueError:
        return {
            "number": number,
            "error": True
        }
       

    return{
    "number": get_number(n),
    "is_prime": is_prime(n),
    "is_perfect": is_perfect(n),
    "properties": properties(n),
    "digit_sum": digit_sum(n), 
    "fun_fact": get_fun_fact(n)
    }
