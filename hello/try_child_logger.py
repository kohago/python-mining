# coding:utf-8
import logging
from logging import getLogger,StreamHandler,Formatter

logger = getLogger("LogTest").getChild("childTest")

def i_am_here():
    logger.debug("Hi ,I am a child!")
    # can set parent logger by 
    # logger.parent.setLever()
    # logger.parent.addHandler(stream_handler)
