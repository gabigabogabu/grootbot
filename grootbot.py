#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

#run with python3

import praw
import logging
from time import sleep

def get_logger():
    log = logging.getLogger('_name_')
    logFormat = '[%(asctime)s] [%(levelname)s] - %(message)s'

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logging.Formatter(logFormat))
    log.addHandler(streamHandler)

    fileHandler = logging.FileHandler('grootbot.log')
    fileHandler.setFormatter(logging.Formatter(logFormat))
    log.addHandler(fileHandler)

    log.setLevel(level=logging.INFO)
    return log

# def log_comment(msg, comment):
#     log.info(msg + ': ' comment.id)

def handle_comment(comment):
    #don't comment on own comments
    if comment.author == 'grootbot':
        log.info('own comment found: %s', comment.id)
        return

    if ' groot ' in comment.body.lower():
        log.info('" groot " found: %s', comment.id)
        comment.reply('I am Groot')
    elif 'groot' in comment.body.lower():
        log.info('"groot" (without spaces) found')
    elif 'this' == comment.body.lower().strip() or 'this.' == comment.body.lower().strip():
        log.info('useless comment found: "this": %s', comment.id)
    elif 'listen here you little shit' == comment.body.lower().strip():
        log.info('insert some navy seals copypasta here')
    else:
        pass
        # print(comment.id)

if __name__ == '__main__':
    log = get_logger()
    reddit = praw.Reddit('grootbot')
    attempts = 0
    while True:
        try:
            for c in reddit.subreddit('all').stream.comments():
                handle_comment(c)
                attempts = 0
        except Exception as e:
            log.critical('well shit: ' + str(e))
            sleep(attempts)
            continue
