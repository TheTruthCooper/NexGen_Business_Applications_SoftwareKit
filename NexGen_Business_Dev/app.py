
from flask import Flask, jsonify
from promo_code import PromoCodeGenerator
from database import DatabaseConnector
from config import Config

app = Flask(__name__)

@app.route('/generate-codes', methods=['GET'])
def generate_codes():
    generator = PromoCodeGenerator(code_length=8, prefix='PROMO', fixed_chars='P__X__')
    promo_codes = generator.generate_codes(num_codes=10)
    
    # Database connection
    payment_provider = DatabaseConnector(provider_name=Config.PROVIDER_NAME, 
                                         api_key=Config.API_KEY, 
                                         secret_key=Config.SECRET_KEY)
    payment_provider.connect()
    payment_provider.save_codes(promo_codes)

    return jsonify({"promo_codes": promo_codes})

if __name__ == '__main__':
    context = (Config.SSL_CERT, Config.SSL_KEY)
    app.run(host='0.0.0.0', port=443, ssl_context=context)
