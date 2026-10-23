import enum
from asok.orm import Model, Field
from asok.admin import ModelAdmin


class UserLanguage(enum.Enum):
    FR = "fr"
    EN = "en"


class Subscriber(Model):
    __tablename__ = "subscribers"
    email = Field.Email(max_length=100, nullable=False, unique=True)
    confirmed = Field.Boolean(default=False, nullable=True)
    confirm_token = Field.String(max_length=255, nullable=True, unique=True)
    locale = Field.Enum(UserLanguage, default=UserLanguage.FR, nullable=False)
    created_at = Field.CreatedAt()

    class Admin(ModelAdmin):
        list_display = ["email", "confirmed", "created_at", "locale"]

    def __str__(self):
        return self.email