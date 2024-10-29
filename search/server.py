from fastapi import FastAPI
from pydantic import BaseModel

from vecrorize import Search

app = FastAPI()
search = Search()

class TextRequest(BaseModel):
    text: str

@app.post("/embed")
async def get_embedding(request: TextRequest):
    ids = search.search_relevant_id(words=request.text)
    return {"ids": ids}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)