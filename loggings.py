import logging
import traceback

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')


# This is a comment in python
logging.critical('critical message')


stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)



formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)


logger.error('error message')
logger.warning('warning message')



# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     logger.error(e, exc_info=True)


try:
    a = [1, 2, 3]
    val = a[4]
except:
    logger.error('The error is %s', traceback.format_exc())