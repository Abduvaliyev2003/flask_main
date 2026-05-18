from flask_migrate import Migrate
from main import app, db

# Faqat migratsiyani app va db bilan bog'laymiz
migrate = Migrate(app, db)