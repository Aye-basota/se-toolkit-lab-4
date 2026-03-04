"""Learning Management Service — FastAPI application."""

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth import verify_api_key
from app.routers import interactions, items, learners
from app.settings import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    description="A learning management service API.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(verify_api_key)],
)

@router.post("/", response_model=InteractionLog, status_code=201)
async def post_interaction(
    body: InteractionLogCreate, session: AsyncSession = Depends(get_session)
):
    """Create a new interaction log."""
    try:
        return await create_interaction(
            session,
            learner_id=body.learner_id,
            item_id=body.item_id,
            kind=body.kind,
        )
    except IntegrityError as exc:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc.orig),
        )
