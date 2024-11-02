import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles
from starlette_wtf import CSRFProtectMiddleware

from docs.config import BASE_DIR, settings
from docs.routes import router
from docs.templates import hotreload, setup_filters

# delete all existing default loggers
logger.remove()
logger.add(sys.stderr, colorize=True, backtrace=True, diagnose=True)


@asynccontextmanager
async def on_startup(app: FastAPI):
    logger.info(f"Welcome to {settings.APP_NAME}")
    # silence bcrypt noise
    logging.getLogger("passlib").setLevel(logging.ERROR)

    await hotreload.startup()

    setup_filters()
    yield
    await hotreload.shutdown()


app = FastAPI(docs_url=None, redoc_url=None, lifespan=on_startup)


# Add middleware for sessions and CSRF protection
app.add_middleware(SessionMiddleware, secret_key=settings.JWT_SECRET)
app.add_middleware(CSRFProtectMiddleware, csrf_secret=settings.CSRF_SECRET)

# static files
app.mount(
    "/static",
    StaticFiles(directory=f"{BASE_DIR}/docs/static"),
    name="static",
)


# include routes for docs
app.include_router(router)
