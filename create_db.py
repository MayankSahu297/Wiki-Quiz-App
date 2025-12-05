from backend.app.database import engine, Base
from backend.app import models  # Make sure models are imported so they are registered
Base.metadata.create_all(bind=engine)
print("✅ DB tables created")
