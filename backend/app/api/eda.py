from fastapi import APIRouter
from app.schemas.eda import EDARequest
import pandas as pd

router = APIRouter()

@router.post("/")
def eda(req: EDARequest):
    df = pd.read_csv(req.path)
    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "nulls": df.isnull().sum().to_dict(),
        "head": df.head().to_dict()
    }
    return summary
