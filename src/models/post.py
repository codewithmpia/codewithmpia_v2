from asok.orm import Model, Field, Relation
from asok.admin import ModelAdmin


class Category(Model):
    __tablename__ = "categories"
    name = Field.String(max_length=255, nullable=False, unique=True)
    name_en = Field.String(max_length=255, unique=True)
    slug = Field.Slug(populate_from="name", nullable=True, unique=True)
    description = Field.Text(nullable=True)
    description_en = Field.Text(nullable=True)
    posts = Relation.HasMany("Post")
    created_at = Field.CreatedAt()

    class Admin(ModelAdmin):
        list_display = ["name", "slug", "created_at"]
        form_exclude = ["slug", "created_at"]
        group = "Blog"

    def __str__(self):
        return self.name


class Tag(Model):
    __tablename__ = "tags" 
    name = Field.String(max_length=100, nullable=False, unique=True)
    slug = Field.Slug(populate_from="name", nullable=True, unique=True)
    posts = Relation.BelongsToMany("Post")
    created_at = Field.CreatedAt()

    class Admin(ModelAdmin):
        list_display = ["name", "slug"]
        form_exclude = ["slug", "created_at"]
        group = "Blog"

    def __str__(self):
        return self.name 


class Post(Model):
    __tablename__ = "posts"
    title = Field.SearchableText(max_length=255, nullable=False)
    title_en = Field.SearchableText(max_length=255, nullable=False)
    slug = Field.Slug(populate_from="title", nullable=True, unique=True)
    excerpt = Field.SearchableText(nullable=False)
    excerpt_en = Field.SearchableText(nullable=True)
    body = Field.SearchableText(nullable=False)
    body_en = Field.SearchableText(nullable=True)
    author = Field.String(max_length=50, default="Admin", nullable=True)
    image_sm = Field.File(upload_to="blog", nullable=True)
    image_lg = Field.File(upload_to="blog", nullable=True)
    is_published = Field.Boolean(default=False)
    is_active = Field.Boolean(default=False)
    view_count = Field.Integer(default=0)
    reading_time = Field.Integer(default=2)
    category_id = Field.ForeignKey("Category.id", default=True)
    category = Relation.BelongsTo("Category")
    tags = Relation.BelongsToMany("Tag")
    comments = Relation.MorphMany("Comment", relation_name="commentable")
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["title", "autor", "is_published", "view_count", "created_at"]
        list_filter = ["is_published", "is_active", "category_id"]
        search_fields = ["title", "excerpt", "body"]
        form_exclude = ["slug", "created_at", "updated_at"]
        group = "Blog"

    def __str__(self):
        return self.title



