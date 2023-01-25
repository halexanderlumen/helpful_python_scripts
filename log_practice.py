# -*- coding: utf-8 -*-


import logging 
import sys 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(formatter)

fileHandler = logging.handlers.RotatingFileHandler(filename = r'C:\Users\AD13062\OneDrive - Lumen\Personal Projects\LoggingTutorial\test_log.log', maxBytes = 1024000)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

smtpHandler = logging.handlers.SMTPHandler(
                mailhost = 'mailhost.corp.intranet'
                , fromaddr = 'no-reply@lumen.com'
                , toaddrs = ['haddon.alexander@lumen.com']
                , subject = 'Test Log')


smtpHandler.setLevel(logging.CRITICAL)
smtpHandler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    logger.addHandler(smtpHandler)

print(len(logger.handlers))

a = "Hello World"

logger.info("Hello World Printed")

print(a)

b = 5

c = b/a

