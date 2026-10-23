from asok.orm import Model, Field, Relation
from asok.admin import ModelAdmin


class ToolCategory(Model):
    __tablename__ = "tool_categories"
    name = Field.String(max_length=255, nullable=False, unique=True)
    name_en = Field.String(max_length=255, nullable=True)
    slug = Field.Slug(populate_from="name", nullable=True, unique=True)
    description = Field.Text(wysiwyg=True, nullable=False)
    description_en = Field.Text(wysiwyg=True, nullable=True)
    created_at = Field.CreatedAt()
    tools = Relation.HasMany("Tool", foreign_key="tool_category_id")

    class Admin(ModelAdmin):
        list_display = ["name", "slug", "created_at"]
        form_exclude = ["slug"]
        group = "Ressources"

    def __str__(self):
        return self.name


class Tool(Model):
    __tablename__ = "tools"
    title = Field.SearchableText(max_length=255, nullable=False)
    title_en = Field.SearchableText(max_length=255, nullable=True)
    slug = Field.Slug(populate_from="title", nullable=True, unique=True)
    url = Field.URL(nullable=False)
    description = Field.SearchableText(wysiwyg=True, nullable=False)
    description_en = Field.SearchableText(wysiwyg=True, nullable=True)
    is_internal = Field.Boolean(default=True, nullable=False)
    created_at = Field.CreatedAt()
    tool_category_id = Field.ForeignKey("ToolCategory.id")

    class Admin(ModelAdmin):
        list_display = ["title", "is_internal", "created_at"]
        form_exclude = ["slug"]
        group = "Ressources"

    def __str__(self):
        return self.title