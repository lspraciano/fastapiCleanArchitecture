from src.domain.entities.user_entity import UserEntity
from src.domain.interfaces.user_change_last_name_interface import UserChangeLastNameInterface


class UserChangeLastNameUseCase(UserChangeLastNameInterface):
    def change(
            self,
            first_name: str,
            last_name: str,
    ) -> UserEntity:
        return UserEntity(
            first_name=first_name,
            last_name="New Last Name",
        )
