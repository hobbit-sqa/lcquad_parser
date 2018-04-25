# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

from constants import OUTPUT_SORTED_DATA_FILE, OUTPUT_DATA_FILE, VECS, METRICS


def get_json(from_file=OUTPUT_DATA_FILE):
    '''

    :param str from_file:
    :rtype json.JSON:
    '''

    return json.load(open(from_file))


def sort_json_dict(json_dict):
    '''

    :param json.JSON json_dict:
    :return:
    '''
    ordered_items = sorted(json_dict.items(), key=lambda item: item[1][METRICS][VECS])
    ordered_dict = OrderedDict(ordered_items)
    return ordered_dict


def save_json(data_dic, file=OUTPUT_SORTED_DATA_FILE):
    '''Saves dict as json file

    :param data_dic:
    :param file:
    :return:
    '''

    with open(file, 'w') as f:
        json.dump(data_dic, f, indent=2)


if __name__ == '__main__':
    dt = get_json()
    sorted_dt = sort_json_dict(dt)
    save_json(sorted_dt)
