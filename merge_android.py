#!/usr/bin/env python3
# encoding: utf-8

import sys
import os
import json


def get_name(path):
    with open(path, 'r') as f:
        info = f.read()
        parsed = json.loads(info)
        title = parsed['title']
        if 'page_data' in parsed:
            page_data = parsed['page_data']
            return title + str(page_data['page']) + page_data['part']
        elif 'ep' in parsed:
            ep = parsed['ep']
            return title + str(ep['index']) + ep['index_title']


def do_merge(dirname, title):
    title = title.replace("/", "")
    os.system(os.path.dirname(os.path.abspath(__file__)) + '/merge_android.sh "'+ dirname + '" "' + title + '"')


def trav_dirs(root):
    list_dirs = os.walk(root)
    list_tasks = [(dirname, os.path.join(dirname, info_path))
                  for dirname, _, info_paths in list_dirs
                  for info_path in info_paths
                  if info_path.endswith('entry.json')]
    for dirname, info in list_tasks:
        title = get_name(info)
        do_merge(dirname, title)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python ' + sys.argv[0] + ' path/to/cache')
        exit(0)
    trav_dirs(sys.argv[1])
