import random
import string

class PromoCodeGenerator:
    def __init__(self, code_length=8, prefix='', suffix='', fixed_chars=''):
        self._code_length = code_length
        self._prefix = prefix
        self._suffix = suffix
        self._fixed_chars = fixed_chars
        self._char_set = string.ascii_uppercase + string.digits

    def _generate_random_part(self, length):
        return ''.join(random.choice(self._char_set) for _ in range(length))

    def generate_code(self):
        num_placeholders = self._fixed_chars.count('_')
        random_part_length = num_placeholders if self._fixed_chars else (self._code_length - len(self._prefix) - len(self._suffix))
        random_part = self._generate_random_part(random_part_length)

        if self._fixed_chars:
            code = list(self._fixed_chars)
            random_index = 0
            for i in range(len(code)):
                if code[i] == '_':
                    if random_index < len(random_part):
                        code[i] = random_part[random_index]
                        random_index += 1
                    else:
                        raise ValueError("Mismatch between placeholders and available random characters.")
            code = ''.join(code)
        else:
            code = f'{self._prefix}{random_part}{self._suffix}'
        
        return code

    def generate_codes(self, num_codes=10):
        promo_codes = set()
        while len(promo_codes) < num_codes:
            code = self.generate_code()
            promo_codes.add(code)
        return list(promo_codes)

