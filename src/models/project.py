from asok.orm import Model, Field
from asok.admin import ModelAdmin


class Projet(Model):
    __tablename__ = "projects"
    name = Field.String(max_length=255, nullable=False, unique=True)
    description = Field.Text(nullable=False)
    description_en = Field.Text(nullable=True)
    icon = Field.String(max_length=255, nullable=True)
    image1 = Field.File(upload_to="projects", nullable=True)
    image2 = Field.File(upload_to="projects", nullable=True)
    image3 = Field.File(upload_to="projects", nullable=True)
    url = Field.URL(nullable=True)
    type = Field.String(max_length=50, default="web", nullable=False)
    status = Field.String(max_length=50, default="active", nullable=True)
    technologies = Field.JSON(default=[], nullable=True)
    gradient_from = Field.Color(default="#8b5cf6", nullable=True)
    gradient_to = Field.Color(default="#9333ea", nullable=True)
    order = Field.Integer(default=0, nullable=False)
    is_featured = Field.Boolean(default=False, nullable=False)
    is_private = Field.Boolean(default=False, nullable=False)
    created_at = Field.CreatedAt()

    @classmethod
    def _valid_column(cls, col):
        return col in ("`order`", "[order]", "order") or super()._valid_column(col)

    class Admin(ModelAdmin):
        list_display = ["name", "type", "status", "order", "is_featured"]
        list_filter = ["type", "status", "is_featured", "is_private"]
        search_fields = ["name", "description"]

    def __str__(self):
        return self.name