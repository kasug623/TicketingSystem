import configparser
import ticketing
import notificate

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

notificate.notificate(config_ini)