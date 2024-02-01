from jose import jwt


class JwtHandler:
    @staticmethod
    def generate_token(claims):
        token = jwt.encode(claims, "secretkey", algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        return jwt.decode(token, "secretkey")
