from fastapi import FastAPI

from src.parser.handlers import router as parser_router


app = FastAPI(title="API Luna parser")


app.include_router(router=parser_router)
