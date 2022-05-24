# Filename      :       002_singleton_decorator.py
# Created By    :       Suyog Shimpi
# Created Date  :       23/05/22

def singleton(class_):
    """Singleton decorator"""
    instances = {}

    def get_instances(*args, **kwargs):
        """
        Get an instance of class. If instance not exists in the dict then
        it will create an instance and set it into the instance's dict as well.
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instances


@singleton
class Database(object):
    """Database connector"""

    def __init__(self):
        print('Initializing database connection...')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
