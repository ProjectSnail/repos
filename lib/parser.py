
import argparse

def parse():
    psr = argparse.ArgumentParser(description='Remote repos manager')

    psr.add_argument('action',
                        choices=['create', 'list', 'url', 'info', 'remove'],
                        help='The main action to do')

    psr.add_argument('--org', '-o', type=str, metavar="organization",
                        dest="org", help="define organization name")

    psr.add_argument('args', nargs='+')

    return psr.parse_args()
