import datetime
import random
import string
from httprunner import __version__


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


def assert_back(code, content):
    if code == 0:
        assert content.__contains__('task_id') and str(content).isdigit()
        return True
    elif code == 10007:
        assert isinstance(content, list)
        return True
    else:
        return False


if __name__ == '__main__':
    print(end_date())
    print(start_date())