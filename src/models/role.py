from asok.orm import Field, Model
from asok.admin import ModelAdmin


class Role(Model):
    name = Field.String(unique=True, nullable=False)
    label = Field.String()
    permissions = Field.String(default="")
    created_at = Field.CreatedAt()

    class Admin(ModelAdmin):
        show_in_overview = False
        group = "Administration"

    def __str__(self):
        return self.label or self.name
