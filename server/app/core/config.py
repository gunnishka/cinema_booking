import os
from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent

load_dotenv()

class Settings():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("Переменная среды DATABASE_URL не установлена.")
    
class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "private_key.pem"
    public_key_path: Path = BASE_DIR / "certs" / "public_key.pem"
    algorithm: str = "RS256"
