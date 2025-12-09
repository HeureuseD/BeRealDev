from fastapi import FastAPI
from backend.app.routes.keyword import router as keyword_router
#from backend.app.routes.user import router as user_router
from backend.app.database import engine, Base

app = FastAPI()


@app.on_event("startup")
def on_startup():
	# Create all tables defined on Base when the application starts
	Base.metadata.create_all(bind=engine)


app.include_router(keyword_router)
#app.include_router(user_router)
