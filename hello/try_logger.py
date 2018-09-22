# coding:utf-8

import logging
from logging import getLogger,StreamHandler,Formatter,FileHandler

# use other file
import try_child_logger

#logger
logger = getLogger("LogTest")
logger.setLevel(logging.DEBUG)

#handler foramt
handler_format = Formatter('%(asctime)s - %(name)s- %(levelname)s - %(message)s')

#Handler StreamHandler!
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(handler_format)

#FileHandler
file_handler = FileHandler('sample03.log','a')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(handler_format)

# set handler to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# noset -> debug -> info -> warn -> error -> critical
logger.debug("I am debug")
logger.info("I am info")
logger.warn("I am warn")
logger.error("I am error")
logger.critical("I am critical")

try_child_logger.i_am_here()

# 2018-09-21 19:07:22,688 - LogTest- DEBUG - I am debug
# 2018-09-21 19:07:22,688 - LogTest- INFO - I am info
# 2018-09-21 19:07:22,688 - LogTest- WARNING - I am warn
# 2018-09-21 19:07:22,688 - LogTest- ERROR - I am error
# 2018-09-21 19:07:22,688 - LogTest- CRITICAL - I am critical
# 2018-09-21 19:07:22,688 - LogTest- DEBUG - Hi,I am a child!
