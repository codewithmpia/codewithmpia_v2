from asok.orm import Field, Model
from asok.admin import ModelAdmin


class AdminTrash(Model):
    __tablename__ = "asok_trash"
    model_name = Field.String(nullable=False)
    model_slug = Field.String(nullable=False)
    object_id = Field.Integer(nullable=True)
    object_repr = Field.String()
    data = Field.Text()
    deleted_by_id = Field.Integer(nullable=True)
    deleted_at = Field.CreatedAt()

    class Admin(ModelAdmin):
        hidden = True
        show_in_overview = False
