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
 --Org, -o :orgname                 given name is for organization
 --Private, -p
"""

import requests, json, colored, time
from lib import github

auth=("user","pass")

github.list(orgname="projectsnail", auth=auth)
