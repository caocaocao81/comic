DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123'
HOST = '8.142.98.163'
PORT = '3306'
DATABASE = 'py_flask'
# 'mysql+pymysql://root:123@8.142.98.163:3306/py_flask'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
    DIALECT,
    DRIVER,
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)

TEMPLATES_AUTO_RELOAD = True
SEND_FILE_MAX_AGE_DEFAULT = 0
SQLALCHEMY_TRACK_MODIFICATIONS = True
