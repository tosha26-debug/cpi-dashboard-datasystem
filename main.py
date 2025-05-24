import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Load your CSV files once when server starts
cpi_facts_df = pd.read_csv('part-00000-36444227-c777-41f8-b1bc-3cecd5aabf63-c000.csv')
cpi_dim_df = pd.read_csv('dim_date.csv')

# Create a Pydantic model for facts (you can create another for dim if needed)
class CPIFact(BaseModel):
    date: str
    cpi_value: float
    year: int
    month: int

class CPIDim(BaseModel):
    date: str
    year: int
    month: int
    month_name: str
    quarter: int

@app.get("/v0/cpi/facts", response_model=List[CPIFact])
def get_cpi_facts():
    return cpi_facts_df.to_dict(orient="records")

@app.get("/v0/cpi/dim", response_model=List[CPIDim])
def get_cpi_dim():
    return cpi_dim_df.to_dict(orient="records")
