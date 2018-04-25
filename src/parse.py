# -*- coding: utf-8 -*-

from constants import DATA_FILE, OUTPUT_DATA_FILE, ORIGINAL, MODIFIED, METRICS

import pandas as pd
import json
import tqdm

import nlgeval


def get_data(file=DATA_FILE):
    '''Reads the raw data from the file

    :param file:
    :return:
    '''
    # xls_file = pd.ExcelFile(file)
    # print(xls_file.sheet_names)
    # df = pd.DataFrame()
    # for sheet_name in xls_file.sheet_names:
    #    df.append(xls_file.parse(sheet_name))

    # return df
    # return pd.read_excel(file, sheet_name='sheet1')
    df = pd.read_excel(file, sheet_name='sheet1')
    df = df.append(pd.read_excel(file, sheet_name='sheet2'), ignore_index=True)
    return df


def save_json(data_dic, file=OUTPUT_DATA_FILE):
    '''Saves dict as json file

    :param data_dic:
    :param file:
    :return:
    '''

    with open(file, 'w') as f:
        json.dump(data_dic, f, indent=2)


def compute_metrics(hypothesis, references):
    '''

    :param hypothesis:
    :param references:
    :return:
    '''

    return nlgeval.compute_individual_metrics(hypothesis, references, True, True, False)


def gen_data():
    '''Generates data

    :return:
    '''
    combined_dict = {}
    data = get_data()
    data = data[data[MODIFIED] != 'skip']
    data = data[data[MODIFIED].notnull()]
    for _, row in tqdm(data.iterrows(), desc='Computing Metrics...', total=data.shape[0]):
        entry_dict = {}
        entry_dict[ORIGINAL] = row[ORIGINAL]
        entry_dict[MODIFIED] = row[MODIFIED]
        entry_dict[METRICS] = compute_metrics(str(row[ORIGINAL]), str(row[MODIFIED]))
        combined_dict[_] = entry_dict
        print(entry_dict)

    return combined_dict


if __name__ == "__main__":
    dt = gen_data()
    print(dt)
    save_json(dt)
