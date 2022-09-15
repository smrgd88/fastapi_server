from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Hello World!'}


@app.get('/test')
async def test():
    return {'message': 'This is Test'}
