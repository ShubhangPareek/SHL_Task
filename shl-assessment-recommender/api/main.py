from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.recommender import recommend

app = FastAPI(title="SHL Assessment Recommender API")

# Allow cross-origin requests (optional for Streamlit/JS frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommend")
def get_recommendations(query: str = Query(..., description="Job description or keywords")):
    results = recommend(query)
    return {"results": results}