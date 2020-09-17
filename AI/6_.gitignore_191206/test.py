#!/usr/bin/env python
"""
Example of using PyDDL to solve the "Missionaries and Cannibals" Problem.
A boat must transport a group of 3 missionaries and 3 cannibals across a river,
but at no time can the cannibals outnumber the missionaries at either side of
the river.
"""
from __future__ import print_function
from pyddl import Domain, Problem, Action, neg, planner

def problem(verbose):
    domain = Domain((
        Action(
            'oppoint',
            preconditions=(
                ('at', 'home'),
            ),
            effects=(
                ('loverget', 'present'),
            ),
        ),
        
        Action(
            'dating',
            preconditions=(
                ('loverget', 'present'),
            ),
            effects=(
                ('feel', 'happy'),
            ),
        ),
        
    ))
    problem = Problem(
        domain,
        {
            'storelist': ('restaurant', 'bookstore'),
            'buylist': ('book', 'food'),
            'decidelist': ('outside', 'playground'),
            
        },
        init=(
            ('at', 'home'),
        ),
        goal=(
            #('loverget', 'present'),

            ('feel', 'happy'),
        )
    )

    plan = planner(problem, verbose=verbose)
    if plan is None:
        print('No Plan!')
    else:
        for action in plan:
            print(action)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(usage="Usage: %prog [options]")
    parser.add_option('-q', '--quiet',
                      action='store_false', dest='verbose', default=True,
                      help="don't print statistics to stdout")

    # Parse arguments
    opts, args = parser.parse_args()
    problem(opts.verbose)
