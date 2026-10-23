from asok.orm import Model, Field
from asok.admin import ModelAdmin


class CheatSheet(Model):
    __tablename__ = "cheat_sheets"
    title = Field.SearchableText(max_length=255, nullable=False)
    title_en = Field.SearchableText(max_length=255, nullable=True)
    slug = Field.Slug(populate_from="title", nullable=True, unique=True)
    description = Field.SearchableText(wysiwyg=True, nullable=True)
    description_en = Field.SearchableText(wysiwyg=True, nullable=True)
    cover_image = Field.File(upload_to="cheatsheets/covers", nullable=True)
    filename = Field.File(upload_to="cheatsheets/pdfs", nullable=False)
    is_published = Field.Boolean(default=False, nullable=False)
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["title", "is_published", "created_at"]
        list_filter = ["is_published", "created_at"]
        search_fields = ["title", "description"]
        form_exclude = ["slug"]
        group = "Ressources"

    def __str__(self):
        status = "En ligne" if self.is_published else "Brouillon"
        return f"{self.title} ({status})"