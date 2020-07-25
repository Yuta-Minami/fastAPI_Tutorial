from urls import app
import uvicorn

if __name__ == '__main__':
    # コンソールで [$ uvicorn run:app --reload]でも可，サーバーを立ち上げる
    uvicorn.run(app=app)