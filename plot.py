#!/usr/bin/python

import sys
from numpy import array
import re
from pylab import plot, show, legend


datare = re.compile(r"[\w\.\+-]+")

if __name__ == '__main__':
    totlist = []
    for i in sys.stdin:
        templist = []
        for j in datare.findall(i):
            templist.append(float(j))
        totlist.append(templist)
    dataarr = array(totlist)
    if len(sys.argv)-1 == len(dataarr[1, :]):
        for i in range(1, len(dataarr[1, :])):
            plot(dataarr[:, 0], dataarr[:, i], sys.argv[-1], label=sys.argv[i])
        legend()
        show()
    elif len(sys.argv) == len(dataarr[1, :]):
        for i in range(1, len(dataarr[1, :])):
            plot(dataarr[:, 0], dataarr[:, i], label=sys.argv[i])
        legend()
        show()
    elif len(sys.argv) == 2:
        for i in range(1, len(dataarr[1, :])):
            plot(dataarr[:, 0], dataarr[:, i], sys.argv[-1])
        show()
    else:
        for i in range(1, len(dataarr[1, :])):
            plot(dataarr[:, 0], dataarr[:, i], "o--")
        show()
