class DevConfig:
    SQLALCHEMY_DATABASE_URI = 'mariadb://root:admin@192.168.56.70/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig:
    SQLALCHEMY_DATABASE_URI = 'mariadb://root:admin@192.168.56.70/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
