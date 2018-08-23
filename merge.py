#!/usr/bin/env python3
# encoding: utf-8

import sys
import os
import json


def get_name(path):
    with open(path, 'r') as f:
        info = f.read()
        parsed = json.loads(info)
        return parsed['Title']


def do_merge(dirname, title):
    os.system(os.path.dirname(os.path.abspath(__file__)) + '/merge.sh "'+ dirname + '" "' + title + '"')


def trav_dirs(root):
    list_dirs = os.walk(root)
    list_tasks = [(dirname, os.path.join(dirname, info_path))
                  for dirname, _, info_paths in list_dirs
                  for info_path in info_paths
                  if info_path.endswith('.info')]
    for dirname, info in list_tasks:
        title = get_name(info)
        do_merge(dirname, title)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python ' + sys.argv[0] + ' path/to/cache')
        exit(0)
    trav_dirs(sys.argv[1])
