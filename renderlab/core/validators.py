from typing import Any
from .exceptions import ValidationFailedError

class CoreValidator:
    """Base validation utility providing fail-fast assertations."""

    @staticmethod
    def assert_not_none(value: Any, field_name: str) -> None:
        """Throws an error if the value is None"""
        if value is None:
            raise ValidationFailedError(f"'{field_name}' cannot be None.")
        
    @staticmethod
    def assert_type(value: Any, expected_type: type, field_name: str) -> None:
        """Throws an error if the value is not of the expected type."""
        if not isinstance(value, expected_type):
            raise ValidationFailedError(
                f"'{field_name}' must be of type {expected_type.__name__}, "
                f"got {type(value).__name__} instead."
            )