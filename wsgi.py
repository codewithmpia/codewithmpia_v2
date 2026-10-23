from datetime import datetime, timezone
from asok import Asok
from asok.admin import Admin
from asok_lucide import AsokLucideExtension

app = Asok()
app.register_extension(AsokLucideExtension(alias="Icon"))

from src.models.announcement import Announcement

app.share(
    year=lambda: datetime.now(timezone.utc).year,
    site_name="codewithmpia",
    announcements=lambda: Announcement.query().filter_by(is_active=True).get()
)

Admin(app)
