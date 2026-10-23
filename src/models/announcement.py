import enum
from asok.orm import Model, Field
from asok.admin import ModelAdmin


class AnnouncementType(enum.Enum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"


class Announcement(Model):
    __tablename__ = "announcements"
    message = Field.Text(nullable=False)
    message_en = Field.Text(nullable=True)
    type = Field.Enum(AnnouncementType, default=AnnouncementType.INFO, nullable=False)
    is_active = Field.Boolean(default=False)
    is_dismissible = Field.Boolean(default=True)
    start_date = Field.DateTime(nullable=True)
    end_date = Field.DateTime(nullable=True)
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["message", "type", "is_active", "created_at", "updated_at"]
        list_filter = ["type", "is_active"]
        group = "Marketing"

    def __str__(self):
        return self.message[:20]
    