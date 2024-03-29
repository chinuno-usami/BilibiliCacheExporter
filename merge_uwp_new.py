#!/usr/bin/env python3
# encoding: utf-8

import sys
import os
import json


def get_bgm_name(dirname):
    basepath = dirname[:dirname.rfind("/") + 1]
    infoname = basepath + "info.json"
    try:
        with open(infoname, 'r') as f:
            info = f.read()
            parsed = json.loads(info)
            return parsed["Title"]
    except Exception as e:
        print(e)
        return ""


def get_info(path, dirname):
    with open(path, 'r') as f:
        info = f.read()
        parsed = json.loads(info)
        if "IsDash" in parsed:
            dash = parsed['IsDash']
        if "CID" in parsed:
            return ("{}_{}_{}".format(get_bgm_name(dirname), parsed['Index'], parsed['EpisodeTitle']), dash)
        return ("",False)


def do_merge(dirname, title, dash):
    if dash:
        os.system(os.path.dirname(os.path.abspath(__file__)) + '/merge_uwp_new.sh "'+ dirname + '" "' + title + '"')
    else:
        os.system(os.path.dirname(os.path.abspath(__file__)) + '/merge_android.sh "'+ dirname + '" "' + title + '"')


def trav_dirs(root):
    list_dirs = os.walk(root)
    list_tasks = [(dirname, os.path.join(dirname, info_path))
                  for dirname, _, info_paths in list_dirs
                  for info_path in info_paths
                  if info_path == "info.json"]
    for dirname, info in list_tasks:
        name, dash = get_info(info, dirname)
        title = name.replace("/", "／")
        if title:
            do_merge(dirname, title, dash)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python ' + sys.argv[0] + ' path/to/cache')
        exit(0)
    trav_dirs(sys.argv[1])
