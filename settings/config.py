from dotenv import load_dotenv #to use .env
import os #read from os


class Config:    
    """
        config class for environment dependencies
    """
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path=env_path)
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DB_URL = os.environ.get("DB_URL")
    DB_NAME = os.environ.get("DB_NAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")