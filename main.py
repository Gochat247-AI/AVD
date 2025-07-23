import uvicorn
from fastapi import FastAPI


# Import your routers
from .routers.nest_and_scrape import router as nest_and_scrape_router
from .routers.extraction_service import router as extraction_service_router
from .routers.new_element_identifier_service import router as new_element_identifier_router
from .routers.embeddings_router import router as embeddings_router
# from .routers.google_apple_service import router as google_apple_router

# Create FastAPI application
# Create FastAPI application
app = FastAPI(
    title="Web Scraping & AI Services",
    description="Comprehensive service for web scraping, extraction, and embeddings",
    version="1.0.0"
)

# Include routes
app.include_router(nest_and_scrape_router)
app.include_router(extraction_service_router)
app.include_router(new_element_identifier_router)
app.include_router(embeddings_router)  # NEW - adds /embeddings/* endpoints
# app.include_router(google_apple_router)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Web Scraping & AI Services API",
        "version": "1.0.0",
        "services": [
            "nest_and_scrape",
            "extraction_service", 
            "new_element_identifier_service",
            "embeddings"  # NEW
        ]
    }

# If you want to run via "python -m app.main"
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)
