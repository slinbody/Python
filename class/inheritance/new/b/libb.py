import sys
sys.path.append('/tmp/test_class/a/')
import liba

class big_Car(liba.car):
    def __init__(self):
        self.size='Big'
        super(big_Car, self).__init__()

    def car_size(self):
        print 'My size is '+self.size


if __name__ == '__main__':
    c = big_Car()
    c.car_size()
    c.car_wheel()
    print c.wheel
