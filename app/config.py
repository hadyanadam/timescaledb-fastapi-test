import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path('.').resolve()
load_dotenv(BASE_DIR / '.env')
DATABASE_URI = os.getenv("DATABASE_URI")