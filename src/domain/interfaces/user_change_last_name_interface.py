from abc import ABC, abstractmethod

from src.domain.entities.user_entity import UserEntity


class UserChangeLastNameInterface(ABC):
    @abstractmethod
    def change(
            self,
            first_name: str,
            last_name: str,
    ) -> UserEntity:
        ...
