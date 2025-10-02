from datetime import timedelta


class Config(object):

    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = "supersecretkey123!456@"
    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    SWAGGER_AUTHORIZATION = {
        "JsonWebToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization"
        }
    }