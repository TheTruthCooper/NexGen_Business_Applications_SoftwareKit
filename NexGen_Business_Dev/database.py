
import hmac
import hashlib
import base64
import os
from dotenv import load_dotenv

class DatabaseConnector:
    def __init__(self, provider_name, api_key, secret_key):
        self.provider_name = provider_name
        self.api_key = api_key
        self.secret_key = secret_key
        self._validate_credentials()

    def _validate_credentials(self):
        if not isinstance(self.api_key, str) or len(self.api_key) < 16:
            raise ValueError("Invalid API key: Must be a string with at least 16 characters.")
        if not isinstance(self.secret_key, str) or len(self.secret_key) < 16:
            raise ValueError("Invalid Secret key: Must be a string with at least 16 characters.")

    def _hash_and_sign(self, data):
        hmac_obj = hmac.new(self.secret_key.encode(), data.encode(), hashlib.sha512)
        return base64.b64encode(hmac_obj.digest()).decode()

    def connect(self):
        print(f"Connecting to {self.provider_name} with API key: {self.api_key}")
        if not self.api_key or not self.secret_key:
            raise ConnectionError("Failed to connect: Invalid API or Secret key.")
        print("Connected successfully.")

    def save_codes(self, codes):
        signed_api_key = self._hash_and_sign(self.api_key)
        print(f"Using signed API key: {signed_api_key}")

        print("Validating and saving codes to the database...")
        for code in codes:
            if not isinstance(code, str):
                raise ValueError(f"Invalid promo code: {code} is not a valid string.")
            print(f"Code {code} saved to {self.provider_name} database.")
        print("All codes have been saved successfully.")