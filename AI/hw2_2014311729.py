#2014311729_이대희
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
            #학교에 갈 짐을 쌉니다. 교재와 펜을 챙겨야 합니다.
            'pack',
            parameters=(
                ('things', 'th'),
            ),
            preconditions=(
                ('at', 'home'),
            ),
            effects=(
                ('packed', 'th'),
            ),
        ),
        
        Action(
            #교재와 펜을 챙기면 밖으로 나올 수 있습니다. 피시방을 가거나 학교에 갑니다.
            'walk',
            parameters=(
                ('locations', 'loc'),
            ),
            preconditions=(
                ('packed', 'textbook'),
                ('packed', 'pen'),
            ),
            effects=(
                ('at', 'loc'),
            ),
        ),
        
        Action(
            #맞는 교실을 갑니다. 지금은 인공지능 수업을 가야할 때 입니다.
            'goclass',
            parameters=(
                ('buildings', 'bui'),
            ),
            preconditions=(
                ('at', 'waytoschool'),
            ),
            effects=(
                ('at', 'bui'),
                neg(('at','waytoschool')),
            ),
        ),
        
        Action(
            #가지고 온 것들을 엽니다. 인공지능 수업에 있고 교재가 필요합니다.
            'seetextbook',
            parameters=(
                ('things', 'th'),
            ),
            preconditions=(
                ('at', 'aiclass'),
                ('packed','textbook')
            ),
            effects=(
                neg(('packed', 'textbook')),
                ('open','th')
            ),
        ),
        
        Action(
            #수업을 듣습니다. 교재를 핀 상태여야 합니다.
            'takeclass',
            parameters=(
                ('things', 'th'),
            ),
            preconditions=(
                ('open', 'textbook'),
            ),
            effects=(
                ('study', 'th'),
            ),
        ),
        
        Action(
            #수업이 끝나면 물건들을 닫고 마무리합니다.
            'endclass',
            parameters=(
                ('things', 'th'),
            ),
            preconditions=(
                ('study', 'textbook'),
            ),
            effects=(
                ('closed', 'th'),
            ),
        ),
        
    ))
    problem = Problem(
        domain,
        {
            'things': ('textbook', 'comicbook','pen'),
            'locations': ('PCroom', 'waytoschool'),
            'buildings': ('aiclass', 'algorithmclass'),
            
        },
        init=(
            ('at', 'home'),
        ),
        goal=(
            ('closed', 'textbook'),
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
