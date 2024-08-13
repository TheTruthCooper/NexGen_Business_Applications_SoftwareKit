import random
import string
import hashlib
import hmac
import base64
import os
from dotenv import load_dotenv

class PromoCodeGenerator:
    def __init__(self, code_length=8, prefix='', suffix='', fixed_chars=''):
        self._code_length = code_length  # Private variable
        self._prefix = prefix  # Private variable
        self._suffix = suffix  # Private variable
        self._fixed_chars = fixed_chars  # Private variable
        self._char_set = string.ascii_uppercase + string.digits  # Character set (A-Z, 0-9)

    def _generate_random_part(self, length):
        """Private method to generate the random part of the code."""
        return ''.join(random.choice(self._char_set) for _ in range(length))

    def generate_code(self):
        """Public method to generate a single promotional code."""
        random_part_length = self._code_length - len(self._prefix) - len(self._suffix)
        random_part = self._generate_random_part(random_part_length)

        if self._fixed_chars:
            # Fill in the random part according to fixed_chars structure
            code = list(self._fixed_chars)
            random_index = 0
            for i in range(len(code)):
                if code[i] == '_':
                    code[i] = random_part[random_index]
                    random_index += 1
            code = ''.join(code)
        else:
            # Combine prefix, random part, and suffix
            code = f'{self._prefix}{random_part}{self._suffix}'
        
        return code

    def generate_codes(self, num_codes=10):
        """Public method to generate multiple unique promotional codes."""
        promo_codes = set()  # Use a set to ensure uniqueness
        while len(promo_codes) < num_codes:
            code = self.generate_code()
            promo_codes.add(code)
        return list(promo_codes)


class DatabaseConnector:
    def __init__(self, provider_name, api_key, secret_key):
        self.provider_name = provider_name
        self.api_key = api_key
        self.secret_key = secret_key
        # Here, you would initialize the connection to the payment provider's API/database

    def _hash_and_sign(self, data):
        """Private method to hash and sign data with SHA-512."""
        # Create a HMAC object with the secret key and hash the data with SHA-512
        hmac_obj = hmac.new(self.secret_key.encode(), data.encode(), hashlib.sha512)
        # Return the base64-encoded HMAC digest
        return base64.b64encode(hmac_obj.digest()).decode()

    def connect(self):
        """Simulate connecting to a payment provider's database."""
        print(f"Connecting to {self.provider_name} with API key: {self.api_key}")
        # Real implementation would involve authentication and setup steps

    def save_codes(self, codes):
        """Simulate saving promotional codes to the payment provider's database."""
        # Hash and sign the API key before use
        signed_api_key = self._hash_and_sign(self.api_key)
        print(f"Using signed API key: {signed_api_key}")

        print("Saving codes to the database...")
        for code in codes:
            # In a real-world scenario, you would send an API request here
            print(f"Code {code} saved to {self.provider_name} database.")
        print("All codes have been saved successfully.")


# Load environment variables from the .env file
load_dotenv()

# Example usage of both classes
if __name__ == "__main__":
    # Step 1: Generate promotional codes
    generator = PromoCodeGenerator(code_length=8, prefix='PROMO', fixed_chars='P__X__')
    promo_codes = generator.generate_codes(num_codes=10)

    # Step 2: Link to payment provider's database and save codes
    provider_name = os.getenv('PROVIDER_NAME')
    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')

    payment_provider = DatabaseConnector(provider_name=provider_name, api_key=api_key, secret_key=secret_key)
    payment_provider.connect()
    payment_provider.save_codes(promo_codes)