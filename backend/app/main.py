"""
NEPSE Data System — FastAPI skeleton
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NEPSE Data System",
    description="Solid multi-source NEPSE market data API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "NEPSE Data System",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

# Placeholder routers — expand later
@app.get("/api/v1/companies")
def list_companies():
    return {"message": "Implement from database"}

@app.get("/api/v1/prices/{symbol}")
def get_prices(symbol: str):
    return {"symbol": symbol, "message": "Implement OHLC query"}

@app.get("/api/v1/live")
def live_market():
    return {"message": "Implement live snapshot"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
