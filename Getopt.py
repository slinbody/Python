#reference:
# http://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm

#!/usr/bin/python3
import sys, getopt

ifile = ''
ofile = ''

myopts,args = getopt.getopt(sys.argv[1:],"a:b:")
for o,a in myopts:
    if o == '-a':
        ifile = a
    elif o == '-b':
        ofile = a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])
# Display input and output file name passed as the args

print ("Input file : %s and output file: %s" % (ifile,ofile) )
