from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GitHub AI Reviewer Bot running!"}

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    # In a real bot, process PR event here and call LLM
    return {"status": "received", "action": payload.get("action")}
