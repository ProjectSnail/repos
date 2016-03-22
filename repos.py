#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
repos                               list all existing repos
repos list [username]               list all repos of given user, default auth
repos create    :name               create a new repo, default public
repos edit      :name               edits repo values
repos delete    :name               removes a repo
"""

"""  Options:
--org, -o :orgname                 given name is for organization
--private, -p
"""

import requests, json, colored, time
from lib import github
from lib import parser

print parser.parse()
