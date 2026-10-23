from asok.orm import Model, Field, Relation
from asok.admin import ModelAdmin


class Enrollment(Model):
    __tablename__ = "enrollments"
    user_id = Field.ForeignKey("User.id", nullable=False, index=True)
    course_id = Field.ForeignKey("Course.id", nullable=False, index=True)
    last_lesson_id = Field.Integer(nullable=True)
    completed_at = Field.DateTime(nullable=True)
    created_at = Field.CreatedAt()
    updated_at = Field.UpdatedAt()
    user = Relation.BelongsTo("User")
    course = Relation.BelongsTo("Course")

    class Admin(ModelAdmin):
        label = "Inscriptions aux formations"
        list_display = ["user_id", "course_id", "completed_at", "created_at"]
        list_filter = ["course_id"]
        group = "Formation"

    def __str__(self):
        return f"Enrollment user={self.user_id} course={self.course_id}"


class LessonProgress(Model):
    __tablename__ = "lesson_progress"
    user_id = Field.ForeignKey("User.id", nullable=False, index=True)
    lesson_id = Field.ForeignKey("Lesson.id", nullable=False, index=True)
    course_id = Field.ForeignKey("Course.id", nullable=False, index=True)
    completed_at = Field.CreatedAt()
    user = Relation.BelongsTo("User")
    lesson = Relation.BelongsTo("Lesson")

    class Admin(ModelAdmin):
        label = "Progression des leçons"
        list_display = ["user_id", "lesson_id", "course_id", "completed_at"]
        list_filter = ["course_id"]
        can_add = False
        can_edit = False
        group = "Formation"

    def __str__(self):
        return f"Progress user={self.user_id} lesson={self.lesson_id}"
