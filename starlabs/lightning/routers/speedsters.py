from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as
from typing import List
from uuid import UUID

from ..schemas.speedster import Speedster, SpeedsterCreate
from ..repositories.speedsters import SpeedstersRepository


router = APIRouter(prefix="/speedsters", tags=["speedsters"])


@router.get("/", response_model=List[Speedster])
def list_speedsters(skip: int = 0, max: int = 10, speedsters: SpeedstersRepository = Depends()):
    db_speedsters = speedsters.all(skip=skip, max=max)
    return parse_obj_as(List[Speedster], db_speedsters)


@router.post("/", response_model=Speedster, status_code=status.HTTP_201_CREATED)
def store_speedster(speedster: SpeedsterCreate, speedsters: SpeedstersRepository = Depends()):
    db_speedster = speedsters.find_by_email(email=speedster.email)

    if db_speedster:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    db_speedster = speedsters.create(speedster)
    return Speedster.from_orm(db_speedster)


@router.get("/{speedster_id}", response_model=Speedster)
def get_speedster(speedster_id: UUID, speedsters: SpeedstersRepository = Depends()):
    db_speedster = speedsters.find(speedster_id)

    if db_speedster is None:
        raise HTTPException(
            status_code=404,
            detail="Speedster not found"
        )

    return Speedster.from_orm(db_speedster)