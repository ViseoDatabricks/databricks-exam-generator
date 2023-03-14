import random
from itertools import compress

import pandas as pd


def display_question(form, nested_question_dic, question_num, answers_dic):
    """
    Display a question in the form and allow the user to answer it.
    Returns the dictionary of answers.

    Parameters
    ----------
    form : object
        The form object used to display the question and collect the answer.
    nested_question_dic : dict
        A dictionary containing the question and its options.
    question_num : int
        The number of the question.
    answers_dic : dict
        A dictionary containing the user's answers.

    Returns
    -------
    dict
        A dictionary containing the user's answers.
    """
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
    """
    Get the index of an element in a list.

    Parameters
    ----------
    list_ : list
        The list to search the element in.
    element : object
        The element to search.

    Returns
    -------
    int
        The index of the element in the list.
    """
    idx = list_.index(element)
    return idx


def get_indexes_multiple_choices(choices, bool_list):
    """Returns a list of the indexes of the selected choices.

    Args:
        choices (list): List of all possible choices.
        bool_list (list): List of boolean values indicating whether each choice was selected or not.

    Returns:
        list: List of the indexes of the selected choices.
    """
    return list(compress(choices, bool_list))


def pick_randomized_questions(data, nb_questions):
    """Picks a given number of randomized questions from each topic in the data.

    Args:
        data (dict): Dictionary containing the topics and questions.
        nb_questions (list): List containing the number of questions to pick from each topic.

    Returns:
        dict: Dictionary containing the picked questions.
    """
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
    """Generates a full exam by displaying each question in the form.

    Args:
        questions_dict (dict): Dictionary containing all the questions.
        form (streamlit.form.Form): Form in which to display the questions.
        answers_dic (dict): Dictionary containing the answers given by the user.

    Returns:
        dict: Dictionary containing the answers given by the user.
    """


def get_answers(questions_dic):
    """Returns a dictionary containing the expected answers for each question.

    Args:
        questions_dic (dict): Dictionary containing all the questions.

    Returns:
        dict: Dictionary containing the expected answers for each question.
    """
    answers_dic = {}
    for question in questions_dic:
        answers_dic[str(int(question) + 1)] = questions_dic[question]["answers"]
    return answers_dic


def get_results(dic_answers_expected, dic_answers_provided):
    """Compares the expected and provided answers and returns the results.

    Args:
        dic_answers_expected (dict): Dictionary containing the expected answers for each question.
        dic_answers_provided (dict): Dictionary containing the answers provided by the user.

    Returns:
        tuple: Tuple containing the number and percentage of correct answers, as well as a list of boolean values indicating whether each question was answered correctly or not.
    """
    result = []
    for key in dic_answers_expected:
        if key in dic_answers_provided:
            result.append(dic_answers_expected[key] == dic_answers_provided[key])
    count_true = result.count(True)
    percentage_true = (count_true / len(result)) * 100
    return count_true, round(percentage_true, 1), result


def table_results(results_list):
    """Returns a Pandas dataframe containing the results of the exam.

    Args:
        results_list (list): List of boolean values indicating whether each question was answered correctly or not.

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing the results of the exam.
    """
    data = [(i + 1, "✅" if val else "❌") for i, val in enumerate(results_list)]

