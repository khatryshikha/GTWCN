#!/usr/bin/env python
# vim:fileencoding=utf8
#
# Project: Implementation of the Lemke-Howson algorithm for finding MNE
# Author:  Petr Zemek <s3rvac@gmail.com>, 2009
#

"""Runs a program which computes MNE in the given 2-player game
using the Lemke-Howson algorithm.
"""


import sys
from src import matrix


def main():
    try:
        # These imports must be here because of possible
        # SyntaxError exceptions in different versions of python
        # (this program needs python 2.5)
        import src.io
        import src.lh

        # Check program arguments (there should be none)
        if len(sys.argv) > 1:
            stream = sys.stderr
            if sys.argv[1] in ['-h', '--help']:
                stream = sys.stdout
            src.io.printHelp(stream)
            return 1

        # Obtain input matrices from the standard input
        m1, m2 = src.io.parseInputMatrices(sys.stdin.read())

        # Compute the equilibirum
        eq = src.lh.lemkeHowson(m1, m2)

        # Print both matrices and the result
        src.io.printGameInfo(m1, m2, eq, sys.stdout)
        m1RowValues =row(m1,eq)
        print(m1RowValues)
        m1ColValues = col(m1,eq)
        print(m1ColValues)
        print("Game value for costumer 1")
        print(intersection(m1ColValues,m1RowValues))
        
        m2RowValues =row(m2,eq)
        print(m2RowValues)
        m2ColValues = col(m2,eq)
        print(m2ColValues)
        print("Game value for costumer 2")
        print(intersection(m2ColValues,m2RowValues))

        return 0
    except SyntaxError:
        sys.stderr.write('Need python 2.5 to run this program.\n')
    except Exception, e:
        sys.stderr.write('Error: ' + e.message + '\n')
        return 1

def row(m1,eq) :
    eqs = m1.getNumRows() * [0]
    row = []
    # Equilibrium is in the second column of the tableaux
    for j in range(1, m1.getNumRows()) :
        sum=0
        for i in xrange(1, m1.getNumRows() + 1):
           sum += m1.getItem(i, j)*eq[0][i-1]
           
        row.append(sum)

    return row

def col(m1,eq) :
    eqs = m1.getNumRows() * [0]
    col = []
    # Equilibrium is in the second column of the tableaux
    for j in range(1, m1.getNumRows()+1) :
        sum=0
        for i in xrange(1, m1.getNumRows() + 1):
           sum += m1.getItem(j, i)*eq[1][i-1]
        col.append(sum)
    return col

def intersection(ColValues, RowValues):
    for i in ColValues:
        for j in RowValues:
            if(i==j):
                return i
    return 0



if __name__ == '__main__':
    main()
