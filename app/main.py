from fastapi import FastAPI
app = FastAPI(title="消费者客服会话路由服务")
@app.get("/health")
def health():
    return {"status": "ok"}
