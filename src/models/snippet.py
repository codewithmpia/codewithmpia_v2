import enum
from asok import Model, Field, ModelAdmin


class ProgrammingLanguage(enum.Enum):
    TYPESCRIPT = "typescript"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    SVELTE = "svelte"
    HTML = "html"
    CSS = "css"
    BASH = "bash"
    SQL = "sql"
    DART = "dart"


class Snippet(Model):
    __tablename__ = "snippets"
    title = Field.SearchableText(max_length=255, nullable=False)
    title_en = Field.SearchableText(max_length=255, nullable=True)
    slug = Field.Slug(populate_from="title", nullable=False, unique=True)
    description = Field.SearchableText(nullable=True)
    description_en = Field.SearchableText(nullable=True)
    code = Field.Text(nullable=False)
    language = Field.Enum(
        ProgrammingLanguage, 
        default=ProgrammingLanguage.PYTHON, 
        nullable=False
    )
    is_premium = Field.Boolean(default=True, nullable=False)
    is_hidden = Field.Boolean(default=False, nullable=False)
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["title", "language", "is_premium", "is_hidden", "created_at"]
        list_filter = ["language", "is_premium", "is_hidden", "created_at"]
        search_fields = ["title", "description"]
        group = "Ressources"

    def __str__(self):
        lang = self.language.value if hasattr(self.language, 'value') else self.language
        return f"[{str(lang).upper()}] {self.title}"