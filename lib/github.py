#!/usr/bin/env python

# -*- coding: utf-8 -*-

ghURL = "https://api.github.com/"

import requests, json, colored as col, time

def list(username=None, orgname=None, auth=None):
    if orgname:
        url = "%sorgs/%s/repos" % (ghURL,orgname)
    else:
        if not username:
            if auth:
                username = auth[0]
            else:
                return False
        url = "%susers/%s/repos" % (ghURL, username)

    r = requests.get( url, auth=auth )

    if r.status_code >= 400:
        print "Error, code:", r.status_code
        return

    if r.status_code >= 300:
        print "Error, code:", r.status_code
        return

    data = json.loads(r.text)

    for o in data:
        print "  %s%4s%s" %(col.fg(2),o["name"], col.fg(0))

def create(name=None, orgname=None, auth=None):
    """
    POST /user/repos
    POST /orgs/:orgname/repos

        name            : [REQUIRED]
        description     :
        homepage        :
        private         :
        has_issues      :
        has_wiki        :
        has_downloads   :
        team_id         :
        auto_init       :
        gitignore       : (template)
        license         : (template)
    """
    if not name:
        return False
    if not auth:
        return False
    if orgname:
        url = "%sorgs/%s/repos" % (ghURL, orgname)
    else:
        url = "%suser/repos" % ghURL
    r = requests.post(url, data=json.dumps({"name":name}), auth=auth)
    print r.status_code
    print r.text
    return "--",url,"--"

def edit(name=None, orgname=None, auth=None):
    """
        PATCH /repos/:owner/:repo

        name            : [REQUIRED]
        description     :
        homepage        :
        private         :
        has_issues      :
        has_wiki        :
        has_downloads   :
        team_id         :
        auto_init       :
        default_branch  :

    """

def delete(name=None, orgname=None, auth=None):
    """
        DELETE /repos/:owner/:repo
    """

    if not name:
        return False
    if not auth:
        return False

    url = "%srepos/%s/%s" % (ghURL, orgname or auth[0], name)
    r = requests.delete(url, auth=auth)

    print r.status_code, url
    print r.text

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        list(username=sys.argv[1])
