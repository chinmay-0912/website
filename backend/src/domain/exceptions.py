from __future__ import annotations


class DomainError(Exception):
    """
    Base class for all domain-level exceptions.

    These exceptions represent business rule violations and should
    not depend on any infrastructure concerns (HTTP, DB, etc).

    Application layer may catch these and translate them into
    appropriate responses (API errors, logs, etc).
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message


# =========================
# Email Related Exceptions
# =========================

class InvalidEmailError(DomainError):
    """
    Raised when an email value object receives
    an invalid email format.
    """

    def __init__(self, email: str):
        super().__init__(f"Invalid email format: '{email}'")


# =========================
# User Related Exceptions
# =========================

class UserAlreadyExistsError(DomainError):
    """
    Raised when trying to register a user
    with an email that already exists.
    """

    def __init__(self, email: str):
        super().__init__(f"User with email '{email}' already exists.")


class UserNotFoundError(DomainError):
    """
    Raised when a user cannot be found
    by id or email.
    """

    def __init__(self, identifier: str):
        super().__init__(f"User not found with identifier '{identifier}'.")


class InvalidUserStateError(DomainError):
    """
    Raised when a user entity violates
    internal invariants.
    """

    def __init__(self, reason: str):
        super().__init__(f"Invalid user state: {reason}")


class InvalidCredentialsException(DomainError):
    """
    Raised when user provides invalid credentials during login.
    """

    def __init__(self, message: str = "Invalid email or password"):
        super().__init__(message)


class PasswordResetTokenExpiredError(DomainError):
    """
    Raised when a password reset token has expired.
    """

    def __init__(self, message: str = "Password reset token has expired"):
        super().__init__(message)

class InvalidPasswordResetTokenError(DomainError):
    """
    Raised when a password reset token is invalid (e.g. malformed, signature mismatch).
    """

    def __init__(self, message: str = "Invalid password reset token"):
        super().__init__(message)

class PasswordResetFailedError(DomainError):
    """
    Raised when password reset process fails due to invalid token or expired token.
    """

    def __init__(self, message: str = "Password reset failed due to invalid or expired token"):
        super().__init__(message)

class UserNotFoundException:
    """
    Raised when a user is not found in the repository.
    """

    def __init__(self, message: str = "User not found"):
        self.message = message
        super().__init__(message)
