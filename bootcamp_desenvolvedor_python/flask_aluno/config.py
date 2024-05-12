import os

# A primeira Config
# contém a configuração básica da aplicação. Ela contém o atributo basedir.
# Este atributo indica o diretório base do projeto.
class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

# contém os atributos do ambiente de desenvolvimento
# do projeto. Existe nesta classe uma configuração especial. A configuração
# SQLALCHEMY_DATABASE_URI mostra onde será criado o database e o nome
# que ele terá (“data.db”).
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(Config.basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IP_HOST = 'localhost'
    PORT_HOST = 3000