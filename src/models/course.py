import enum
from asok.orm import Model, Field, Relation
from asok.admin import ModelAdmin


class Level(enum.Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class Course(Model):
    __tablename__ = "courses"
    title = Field.SearchableText(max_length=255, nullable=False)
    title_en = Field.SearchableText(max_length=255, nullable=True)
    slug = Field.Slug(populate_from="title", nullable=True, unique=True)
    description = Field.SearchableText(wysiwyg=True, nullable=True)
    description_en = Field.SearchableText(wysiwyg=True, nullable=True)
    level = Field.Enum(Level, default=Level.BEGINNER, nullable=False)
    price = Field.Float(default=0.0, nullable=False) 
    cover_image = Field.File(upload_to="courses", nullable=True)
    is_published = Field.Boolean(default=False, nullable=False)
    is_featured = Field.Boolean(default=False, nullable=False)
    chapters = Relation.HasMany("Chapter")
    enrollments = Relation.HasMany("Enrollment")
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["title", "level", "price", "is_published", "is_featured"]
        list_filter = ["level", "is_published", "is_featured"]
        form_exclude = ["slug"]
        group = "Formation"

    def __str__(self):
        return self.title


class Chapter(Model):
    __tablename__ = "chapters"
    course_id = Field.ForeignKey("Course.id", nullable=False)
    title = Field.SearchableText(max_length=255, nullable=False)
    title_en = Field.SearchableText(max_length=255, nullable=True)
    description = Field.SearchableText(wysiwyg=True, nullable=True)
    description_en = Field.SearchableText(wysiwyg=True, nullable=True)
    order = Field.Integer(default=0, nullable=False)
    lessons = Relation.HasMany("Lesson")
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["title", "course_id", "order"]
        list_filter = ["course_id"]
        group = "Formation"

    def __str__(self):
        return f"Chapitre {self.order} : {self.title}"


class Lesson(Model):
    __tablename__ = "lessons"
    chapter_id = Field.ForeignKey("Chapter.id", nullable=False)
    title = Field.SearchableText(max_length=255, nullable=False)
    title_en = Field.SearchableText(max_length=255, nullable=True)
    slug = Field.Slug(populate_from="title", nullable=True, unique=True)
    body = Field.SearchableText(wysiwyg=True, nullable=False)
    body_en = Field.SearchableText(wysiwyg=True, nullable=True)
    order = Field.Integer(default=0, nullable=False)
    duration = Field.Integer(default=10, nullable=False) # durée en minutes
    is_free = Field.Boolean(default=False, nullable=False)
    is_published = Field.Boolean(default=False, nullable=False)
    comments = Relation.MorphMany("Comment", relation_name="commentable")
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["title", "chapter_id", "order", "is_published"]
        list_filter = ["is_published", "is_free"]
        form_exclude = ["slug"]
        group = "Formation"

    def __str__(self):
        return self.title