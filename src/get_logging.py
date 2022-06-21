import logging


def doLogging():
    logger = logging.getLogger(__name__)
    logger.warning('This is a warning')
    #logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
    #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    #logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('This is a Warning')
    name = 'John'
    logging.error('%s raised an error', name)
    logging.error(f'{name} raised an error')

    # printing the stack trace
    a = 5
    b = 0
    try:
        c = a / b
    except Exception as e:
        #logging.error("Exception occurred", exc_info=True)
        #OR
        logging.exception("Exception occurred")
