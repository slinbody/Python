'''
Example of switch case
'''
def x1():
        for i in sys.argv[:]:
                print i

def y1():
        for i in reversed(sys.argv[:]):
                print i

if __name__ == '__main__':
        case_fun = {
                'x': x1,
                'y': y1,
                'z': z1
        }
        case_fun[sys.argv[1]]()
