from config.base_config import BaseConfig

class Configuration(BaseConfig):
    DEBUG = True
    # DB_URI = 'mysql+pymysql://root:1234@localhost/ctf' 
    DB_URI = 'mysql+pymysql://ctf_event:ctfevent@mysql.selfmade.ninja/ctf_event_ctf' 