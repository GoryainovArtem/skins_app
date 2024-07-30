from fastapi import APIRouter


case_router = APIRouter(
    prefix="/cases",
    tags=["Case"]
)


@case_router.get("/")
async def get_all_cases():
    ...