import enum
from asok.orm import Model, Field
from asok.admin import ModelAdmin


class Subject(enum.Enum):
    # Les sujets du messages sont à compléter ou modifier
    QUESTION = "Question générale"
    COURSE = "Suggestion de formation"
    PARTNERSHIP = "Partenariat"
    BUG = "Bug sur le site"


class Contact(Model):
    __tablename__ = "contacts"
    name = Field.String(max_length=50, nullable=False)
    email = Field.Email(max_length=100, nullable=False)
    subject = Field.Enum(Subject, default=Subject.QUESTION, nullable=False)
    message = Field.Text(nullable=False)
    handled = Field.Boolean(default=False)
    created_at = Field.CreatedAt()

    class Admin(ModelAdmin):
        list_display = ["name", "email", "subject", "created_at", "handled"]
        list_filter = ["handled", "created_at", "subject"]
        group = "Marketing"

    def __str__(self):
        return f"Message de {self.name} du {self.created_at}"
