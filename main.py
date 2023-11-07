from fastapi import FastAPI
from micro_blog.routers import router

app = FastAPI()

# Since we are separating routes in different files
app.include_router(router)
