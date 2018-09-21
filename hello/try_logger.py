import logging
from logging import getLogger,StreamHandler,Formatter

#logger
logger = getLogger("LogTest")
logger.setLevel(logging.DEBUG)

#Handler
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
#handler foramt
handler_format = Formatter('%(asctime)s - %(name)s- %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)

# set handler to logger
logger.addHandler(stream_handler)

# noset -> debug -> info -> warn -> error -> critical
logger.debug("I am debug")
logger.info("I am info")
logger.warn("I am warn")
logger.error("I am error")
logger.critical("I am critical")


# 2018-09-21 19:07:22,688 - LogTest- DEBUG - I am debug
# 2018-09-21 19:07:22,688 - LogTest- INFO - I am info
# 2018-09-21 19:07:22,688 - LogTest- WARNING - I am warn
# 2018-09-21 19:07:22,688 - LogTest- ERROR - I am error
# 2018-09-21 19:07:22,688 - LogTest- CRITICAL - I am critical
