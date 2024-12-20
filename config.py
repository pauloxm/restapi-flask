class DevConfig:
    SQLALCHEMY_DATABASE_URI = 'mariadb://root:admin@192.168.56.70/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class MockConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True  # Importante para os testes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
