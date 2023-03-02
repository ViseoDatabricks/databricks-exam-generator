import random
from itertools import compress

import pandas as pd


def display_question(form, nested_question_dic, question_num, answers_dic):
    form.markdown("## Question " + str(question_num))
    form.write(nested_question_dic["questions"])
    if nested_question_dic["expected_answers"] == 1:
        answer = form.radio("", nested_question_dic["choices"], key=str(question_num) + "_question")
        answers_dic[str(question_num)] = get_index_single_choice(nested_question_dic["choices"], answer) + 1
    else:
        i = 0
        dic_choices = {}
        for choice in nested_question_dic["choices"]:
            dic_choices[str(i) + "_" + str(question_num)] = form.checkbox(
                choice, key=str(question_num) + "_" + str(i) + "_question"
            )
            i = i + 1
        answers_dic[str(question_num)] = get_indexes_multiple_choices([1, 2, 3, 4, 5], list(dic_choices.values()))
    return answers_dic


def get_index_single_choice(list_, element):
    idx = list_.index(element)
    return idx


def get_indexes_multiple_choices(choices, bool_list):
    return list(compress(choices, bool_list))


def pick_randomized_questions(data, nb_questions):
    exam_dic = {}
    i = 0
    for topic in data:
        idx = list(data.keys()).index(topic)
        nb_questions_topic = nb_questions[idx]
        keys = random.sample(list(data[topic]), nb_questions_topic)
        values = [data[topic][k] for k in keys]
        for j in range(0, nb_questions_topic):
            exam_dic[str(i + j)] = values[j]
        i = len(exam_dic)
    return exam_dic


def generate_full_exam(questions_dict, form, answers_dic):
    i = 1
    for question in questions_dict.values():
        display_question(form, question, i, answers_dic)
        i = i + 1
    return answers_dic


def get_answers(questions_dic):
    answers_dic = {}
    for question in questions_dic:
        answers_dic[str(int(question) + 1)] = questions_dic[question]["answers"]
    return answers_dic


def get_results(dic_answers_expected, dic_answers_provided):
    result = []
    for key in dic_answers_expected:
        if key in dic_answers_provided:
            result.append(dic_answers_expected[key] == dic_answers_provided[key])
    count_true = result.count(True)
    percentage_true = (count_true / len(result)) * 100
    return count_true, round(percentage_true, 1), result


def table_results(results_list):
    data = [(i + 1, "✅" if val else "❌") for i, val in enumerate(results_list)]
    df = pd.DataFrame(data, columns=["Question", "Result"])
    df.set_index("Question", inplace=True)
    return df
