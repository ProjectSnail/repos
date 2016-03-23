
import argparse

def Parser():

    ### TODO: use subparsers in future
    ### [service, action] arguments should redirect a subparser

    """

    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(help='sub-command help', dest='service')

    gh = subparsers.add_parser('github', help = "Interact  with github repos")
    bb = subparsers.add_parser('bitbucket', help = "Interact  with github repos")

    ## Setup options for parser_a

    ## Add nargs="*" for zero or more other commands
    argparser.add_argument('action', nargs=, help = 'Other commands')

    ## Do similar stuff for other sub-parsers
    return argparser

    """

    psr = argparse.ArgumentParser(description='Remote repos manager')

    psr.add_argument('service', choices=['github','bitbucket','gh','bb'] )

    psr.add_argument('action', help='The main action to do',
                        choices=['create', 'list', 'url', 'info', 'remove'] )

    psr.add_argument('--org', '-o', type=str, metavar="organization",
                        dest="org", help="define organization name" )

    psr.add_argument('args', nargs='*') # args for name of repo, user, route...

    return psr


def parse():

    return Parser().parse_args()
