from asok.orm import Field, Model
from asok.admin import ModelAdmin


class AdminLog(Model):
    __tablename__ = "admin_logs"
    user_id = Field.Integer(nullable=True)
    action = Field.String(nullable=False)
    entity = Field.String(nullable=False)
    entity_id = Field.Integer(nullable=True)
    changes = Field.String()
    created_at = Field.CreatedAt()

    class Admin(ModelAdmin):
        label = "Logs"
        slug = "logs"
        group = "System & Audit"
        list_display = ["id", "created_at", "user_id", "action", "entity", "entity_id"]
        list_filter = ["action", "entity"]
        search_fields = ["action", "entity", "changes"]
        show_in_overview = False
        per_page = 50
        can_add = False
        can_edit = False
        can_delete = False
