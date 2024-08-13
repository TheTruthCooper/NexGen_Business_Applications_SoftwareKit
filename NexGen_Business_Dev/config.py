import os
from dotenv import load_dotenv

load_dotenv()

#   WILL NEED TO ADD CONFIGURATION FOR GoDaddy

class Config:
    PROVIDER_NAME = os.getenv('PROVIDER_NAME')
    API_KEY = os.getenv('API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SSL_CERT = os.getenv('SSL_CERT', 'ssl/cert.pem')
    SSL_KEY = os.getenv('SSL_KEY', 'ssl/key.pem')
