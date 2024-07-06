import configparser
from pathlib import Path

cfgFILE = 'petqa.ini'
cfgFILEDIR = 'config'
config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent

CONFIGFILE = BASE_DIR.joinpath(cfgFILEDIR).joinpath(cfgFILE)
config.read(CONFIGFILE)

# cfgfileflaskapp= 'qa.ini'
# configflaskapp=configparser.ConfigParser()
config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent

CONFIGFILE = BASE_DIR.joinpath(cfgFILEDIR).joinpath(cfgFILE)

# CONFIGFILE_flaskapp = BASE_DIR.joinpath(cfgFILEDIR).joinpath(cfgfileflaskapp)
config.read(CONFIGFILE)


# config.read(CONFIGFILE_flaskapp)


# def getFlaskAppBaseURL():
#     baseURL = 'http://' + configflaskapp['flaskapp']['url'] + ":" + configflaskapp['flaskapp']['port'] + '/api/'
#     return baseURL


def getPetApiURL():
    return config['pet']['baseURI']


print(getPetApiURL())
# print(getFlaskAppBaseURL())
