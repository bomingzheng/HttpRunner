import datetime
import random
import string
import time


def end_time():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def start_time():
    return str((datetime.datetime.now() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d %H:%M:%S"))


def search_date():
    return str(datetime.datetime.now().strftime("%Y%m%d"))


def start_date():
    return str(int(datetime.datetime.today().strftime("%Y%m%d")) - 2)


def end_date():
    return datetime.datetime.now().strftime("%Y%m%d")


def requestId():
    return ''.join(random.sample(string.ascii_letters + string.digits, 10))


def end_timestamp():
    return int(time.time()) + 184600


def timestamp():
    return int(time.time())


def start_timestamp():
    return int(time.time() - 172800)


def random_book():
    return random.randint(1, 9999999)


def dd():
    return random.randint(0, 1)


def tr():
    return ''.join(random.sample(string.ascii_letters+string.digits, 28))


if __name__ == '__main__':
    print(tr())
