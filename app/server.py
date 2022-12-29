from fastapi import FastAPI
server = FastAPI(title='my_server',description="My own API powered by FastAPI.")
@api.get('/',tags =['Home'])
def get_index():
    return {'data': 'TeKa_exam_Docker_CICD'}

if __name__ == '__main__':
    uvicorn.run("server:server", reload=True)
