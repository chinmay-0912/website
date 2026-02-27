from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Email:
    """
    Value Object representing a validated email address.

    Immutable by design.
    """
    value: str

    def __post_init__(self):
        # Basic email validation pattern
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, self.value):
            raise ValueError("Invalid email format")

        # Normalize email to lowercase
        object.__setattr__(self, "value", self.value.lower())

    def __str__(self):
        return self.value
