import praw
import logging
from time import sleep

reactions = {
    'i am groot': 'I am Groot',
    "ich bin groot": "Yo soy Groot",
    "yo soy groot": "Je s'appelle Groot",
    "je s'appelle groot": "Jestem Groot",
    "jestem groot": "Io sono Groot",
    "io sono groot": "Eu sou Groot",
    "eu sou groot": "Adim Groot",
    "adim groot": "Ja jsem Groot",
    "ja jsem groot": "Я є Грут",
    "Я є Грут": "En vagyok Groot",
    "en vagyok groot": "私はグルート",
    "私はグルート": "Атым Грут",
    "Атым Грут": "Я есть Грут",
    "Я есть Грут": " मैं हूँ Groot",
    " मैं हूँ groot": "我是格鲁特",
    "我是格鲁特": "Ich bin Groot",
    "groot sucks": "[I am Groot >:(](http://i.imgur.com/bM3DcDu.gif)",
    "grootbot": "[I am Groot 👋](https://data.whicdn.com/images/302342903/original.gif)",
    # "taserface": "[I am Groot 😂](http://i.imgur.com/f5yiWCl.gif)",
    # "what button": "[I am Groot?](http://i.imgur.com/5rBz2lG.gif)",
}

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

def handle_comment(comment):
    # don't comment on own comments
    if comment.author == reddit.user.me():
        log.info('own comment found: %s', comment.id)
        return

    for r in reactions.keys():
        if r in comment.body.lower():
            log.info('"{}" comment found'.format(r))
            comment.reply(reactions[r])

log = get_logger()
reddit = praw.Reddit('grootbot')
log.info('logged in')
sleepUntilNextTry = 0
while True:
    try:
        for c in reddit.subreddit('all').stream.comments():
            handle_comment(c)
            sleepUntilNextTry = 0
    except Exception as e:
        log.critical('well shit: ' + str(e))
        sleepUntilNextTry += .1
        log.critical('sleeping %ss', sleepUntilNextTry)
        sleep(sleepUntilNextTry)
        continue
