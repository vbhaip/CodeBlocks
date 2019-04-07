import datetime



def check_time():
    return datetime.datetime.now().minute % 2 == 0

def ret_false():
    return False

def ret_true():
    return True