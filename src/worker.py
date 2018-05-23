# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

from constants import OUTPUT_SORTED_DATA_FILE, OUTPUT_DATA_FILE, VECS, METRICS, LIMIT, LANGUAGE_EN, DATASET_ID, \
    OUTPUT_QALD_FILE, ID, QUESTION, QUESTIONS, LANGUAGE, STRING, MODIFIED, GMS, EACS, SPARQL, \
    LCQUAD_DATA_FILE, LCQUAD_MODIFIED_FILE, ORIGINAL, MODIFIED
from tqdm import tqdm


def get_json(from_file=OUTPUT_DATA_FILE):
    '''

    :param str from_file:
    :rtype json.JSON:
    '''

    return json.load(open(from_file))


def sort_json_dict(json_dict, metric=VECS):
    '''Sorts by metric given

    :param str metric:
    :param json.JSON json_dict:
    :return:
    '''
    ordered_items = sorted(json_dict.items(), key=lambda item: item[1][METRICS][metric])
    ordered_dict = OrderedDict(ordered_items)
    return ordered_dict


def save_json(data_dic, file=OUTPUT_SORTED_DATA_FILE):
    '''Saves dict as json file

    :param data_dic:
    :param file:
    :return:
    '''

    with open(file, 'w') as f:
        json.dump(data_dic, f, indent="\t")


def export_to_qald(input_json_file=OUTPUT_DATA_FILE, metric=VECS, output_qald_file=OUTPUT_QALD_FILE, limit=LIMIT,
                   language=LANGUAGE_EN, dataset_id=DATASET_ID):
    '''

    :param input_json_file:
    :param limit:
    :param language:
    :param dataset_id:
    :return:
    '''
    json_data = json.load(open(input_json_file))
    ordered_items = sorted(json_data.items(), key=lambda item: item[1][METRICS][metric])
    counter = 0
    data_qlad = {}
    data_qlad[ID] = dataset_id
    questions_list = []

    for obj in tqdm(ordered_items, desc='Building QALD file...', total=limit):
        counter += 1
        qlad_obj = {}
        qlad_obj[ID] = str(counter)
        qlad_obj[QUESTION] = [{LANGUAGE: language, STRING: obj[1][MODIFIED]}]
        qlad_obj["query"] = {"sparql": obj[1][SPARQL]}
        questions_list.append(qlad_obj)
        if counter == limit:
            break

    data_qlad[QUESTIONS] = questions_list

    json.dump(data_qlad, open(output_qald_file, 'w'), indent='\t', sort_keys=True)


def replace_questions_in_qlad(questions_file=OUTPUT_DATA_FILE, data_file=LCQUAD_DATA_FILE, output_file=LCQUAD_MODIFIED_FILE):
    '''

    :param questions_file:
    :param data_file:
    :param output_file:
    :return:
    '''
    json_lcquad_data = json.load(open(data_file))
    json_questions = json.load(open(questions_file))
    def find_question(question_str):
        '''

        :param question_str:
        :return:
        '''
        for obj in json_questions:
            if question_str == json_questions[obj][ORIGINAL]:
                return json_questions[obj][MODIFIED]
        return None


    for question in tqdm(json_lcquad_data['questions'], desc='Parsing LCQUAD...'):
        if find_question(question['question'][0]['string']):
            question['question'][0]['string']=find_question(question['question'][0]['string'])

    save_json(json_lcquad_data, output_file)


def calc_metrics_means():
    '''

    :return:
    '''
    data = get_json()
    data_len = len(data)
    mean_vecs = 0.0
    mean_gms = 0.0
    mean_eacs = 0.0
    for key in data:
        mean_eacs += data[key][METRICS][EACS]
        mean_gms += data[key][METRICS][GMS]
        mean_vecs += data[key][METRICS][VECS]
    mean_vecs = mean_vecs / data_len
    mean_gms = mean_gms / data_len
    mean_eacs = mean_eacs / data_len

    return {'total_number_of_questions': data_len, 'mean_eacs': mean_eacs, 'mean_gms': mean_gms, 'mean_vecs': mean_vecs}


if __name__ == '__main__':
    #dt = get_json()
    #print(len(dt))
    #sorted_dt = sort_json_dict(dt)
    #save_json(sorted_dt)
    #################################
    #export_to_qald()
    #################################
    print(calc_metrics_means())
    #################################
    replace_questions_in_qlad()
