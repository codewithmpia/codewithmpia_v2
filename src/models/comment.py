from asok.orm import Model, Field, Relation
from asok.admin import ModelAdmin


class Comment(Model):
    __tablename__ = "comments"
    author_name = Field.String(max_length=100, nullable=False)
    author_email = Field.Email(max_length=150, nullable=True)
    body = Field.Text(wysiwyg=True, nullable=False)
    is_visible = Field.Boolean(default=True, nullable=False)
    parent_id = Field.ForeignKey("Comment.id", nullable=True)
    commentable_id = Field.Integer(nullable=True)
    commentable_type = Field.String(max_length=50, nullable=True)
    commentable = Relation.MorphTo()
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()

    class Admin(ModelAdmin):
        list_display = ["author_name", "author_email", "commentable_type", "is_visible", "created_at"]
        list_filter = ["is_visible", "commentable_type", "created_at"]
        search_fields = ["author_name", "author_email", "body"]
        group = "Moderation"

    def __str__(self):
        return f"Commentaire de {self.author_name} sur {self.commentable_type} #{self.commentable_id}"