import logging

from fastapi import FastAPI

import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sentry_sdk.integrations.logging import LoggingIntegration

from src.parser.handlers import router as parser_router
from src.settings import settings


sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
    _experiments={
        "continuous_profiling_auto_start": True,
    },
)

sentry_logger = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="API Luna parser")

app.add_middleware(SentryAsgiMiddleware)

app.include_router(router=parser_router)
