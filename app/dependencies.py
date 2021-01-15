from .models import Session

def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()