from openai import OpenAI
client = OpenAI()

with client.responses.stream(
    model="gpt-4o-mini",
    input="Hello world"
) as stream:
    for event in stream:
        yield event  # forward chunks to client A
      from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.post("/chat")
async def chat_proxy(payload: dict):
    def event_generator():
        with client.responses.stream(**payload) as stream:
            for event in stream:
                yield f"data: {event.json()}\n\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")
if payload.get("provider") == "openai":
    client = OpenAI(api_key=OPENAI_KEY)
elif payload.get("provider") == "anthropic":
    client = Anthropic(api_key=ANTHROPIC_KEY)

