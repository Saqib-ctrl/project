
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import candidate_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(candidate_router.router)

from .routers import application_router
app.include_router(application_router.router)

from .routers import job_router
app.include_router(job_router.router)

from .routers import admin_router
app.include_router(admin_router.router)

from .routers import message_router
app.include_router(message_router.router)

from .routers import contract_router
app.include_router(contract_router.router)

from .routers import email_router
app.include_router(email_router.router)

from .routers import blog_router
app.include_router(blog_router.router)

from .routers import analytics_router
app.include_router(analytics_router.router)

from .routers import audit_router
app.include_router(audit_router.router)
