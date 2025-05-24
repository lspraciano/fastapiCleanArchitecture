from fastapi import APIRouter, HTTPException

from src.adapters.http.dto.user_dtos import UserResponse, UserRequest
from src.application.use_cases.user_change_last_name_use_case import UserChangeLastNameUseCase
from src.domain.entities.user_entity import UserEntity

user_router: APIRouter = APIRouter()


@user_router.post(
    path="/register",
    response_model=UserResponse
)
def user_change_last_name_use_case_(
        user: UserRequest
):
    use_case: UserChangeLastNameUseCase = UserChangeLastNameUseCase()

    try:
        updated_user: UserEntity = use_case.change(
            first_name=user.first_name,
            last_name=user.last_name
        )

        return UserResponse(
            first_name=updated_user.first_name,
            last_name=updated_user.last_name
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
