import timeit
from collections import OrderedDict
from random import Random

KEY_COUNT = 10000


def lru_cmp(key):
    return key.hit_count


class RecordValue(object):
    def __init__(self, value, last_access_time, hit_count):
        self.value = value
        self.last_access_time = last_access_time
        self.hit_count = hit_count

class Cache(dict):
    def __init__(*args, **kwds):
        '''Initialize an ordered dictionary.  The signature is the same as
        regular dictionaries, but keyword arguments are not recommended because
        their insertion order is arbitrary.

        '''
        if not args:
            raise TypeError("descriptor '__init__' of 'OrderedDict' object "
                            "needs an argument")
        self = args[0]
        args = args[1:]
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__root
        except AttributeError:
            self.__root = root = []                     # sentinel node
            root[:] = [root, root, None]
            self.__map = {}


class Bench(object):
    def __init__(self):
        self.keys = list()
        r = Random()
        for i in xrange(0, KEY_COUNT):
            self.keys.append(RecordValue(r.randint(0, KEY_COUNT), r.randint(0, KEY_COUNT), r.randint(0, KEY_COUNT)))
        self.data_dic = dict()
        self.data_list = range(0, KEY_COUNT)
        self.random_ints = [r.randint(0, KEY_COUNT) for _ in xrange(0, KEY_COUNT)]
        self.i = 0

        cache = Cache()
        print cache

    def put_dic(self):
        self.data_dic[self.i] = self.keys[self.i]
        self.i += 1

    def put_list(self):
        self.data_list[self.i] = self.keys[self.i]
        self.i += 1

    def sort(self):
        self.data_list.sort(key=lru_cmp)

    def sort2(self):
        self.random_ints.sort()

    def measure(self):
        print "Dict Put time: {}".format(timeit.timeit(self.encode, number=KEY_COUNT))
        # print "Decode time: {}".format(timeit.timeit(self.decode, number=100000))


if __name__ == '__main__':
    # global bench
    # bench = Bench()
    #
    # setup = "from __main__ import Bench"
    # # setup = "from __main__ import Bench;global bench;bench = Bench()"
    # number = KEY_COUNT
    # put_dict_time = timeit.timeit(bench.put_dic, setup=setup, number=number)
    # bench.i = 0
    # put_list_time = timeit.timeit(bench.put_list, setup=setup, number=number)
    # bench.i = 0
    #
    # # sort_time = timeit.timeit(bench.sort, setup=setup, number=number)
    # sort_time2 = timeit.timeit(bench.sort2, setup=setup, number=number)
    #
    # print "--------------------------------------------------------------------------------"
    # print "Put-dict op/s: {}".format(number / put_dict_time)
    # print "Put-list op/s: {}".format(number / put_list_time)
    # # print "sort_time op/s: {}".format(number / sort_time)
    # print "sort_time2 op/s: {}".format(number / sort_time2)
    # print "--------------------------------------------------------------------------------\n\n"
    d = dict()
    d["k1"] = "val1"
    d["k2"] = "val2"
    d["k3"] = "val3"
    d["k4"] = "val4"
    d["k5"] = "val5"
    d["k6"] = "val6"
    d["k7"] = "val7"

    start = 0
    end = 5
    for i in xrange(start, end):
        print d.keys()[i]
