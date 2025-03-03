from app.models.email_verification import EmailVerification


class AuthRepository:
    def __init__(self, db):
        self.db = db

    def get_email_code(self, email: str, code: str):
        return self.db.query(EmailVerification).filter(
            EmailVerification.email == email,
            EmailVerification.code == code
        )

    def create_email_code(self, email, code, expired_at):
        email_code = EmailVerification(email=email, code=code, expired_at=expired_at)
        self.db.add(email_code)
        return email_code

