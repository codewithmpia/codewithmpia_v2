from asok.orm import Field, Model, Relation
from asok.admin import ModelAdmin


class User(Model):
    email = Field.String(unique=True, nullable=False)
    password = Field.Password()
    name = Field.String()
    avatar = Field.File(upload_to="users", nullable=True)
    is_admin = Field.Boolean(default=False, protected=True)
    totp_secret = Field.String(nullable=True, hidden=True, protected=True)
    totp_enabled = Field.Boolean(default=False, protected=True)
    backup_codes = Field.String(nullable=True, hidden=True, protected=True)
    created_at = Field.CreatedAt()
    enrollments = Relation.HasMany("Enrollment")
    lesson_progress = Relation.HasMany("LessonProgress")

    class Admin(ModelAdmin):
        show_in_overview = False
        group = "Administration"

