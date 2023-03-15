import random
from itertools import compress

import pandas as pd


def display_question(form, nested_question_dic, question_num, answers_dic):
    """
        Displays a single question in a form and records the student's answer.

        Args:
        - form: a Streamlit form object.
        - nested_question_dic: a dictionary containing information about the question to be displayed. Should have the following keys:
            - "questions": a string containing the question text.
            - "expected_answers": an integer indicating the expected number of correct answers. Should be either 1 or the number of choices.
            - "choices": a list of strings representing the answer choices.
        - question_num: an integer representing the number of the question in the exam.
        - answers_dic: a dictionary to which the student's answer will be added.

        Returns:
        - answers_dic: the updated dictionary of student answers.
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
        Returns the index of an element in a list.

        Args:
        - list_: a list of elements.
        - element: an element to find in the list.

        Returns:
        - idx: an integer representing the index of the element in the list.
        """
    idx = list_.index(element)
    return idx


def get_indexes_multiple_choices(choices, bool_list):
    """
        Returns a list of the indexes of True values in a boolean list.

        Args:
        - choices: a list of integers representing the possible answer choices.
        - bool_list: a list of Boolean values indicating which answer choices were selected.

        Returns:
        - A list of integers representing the indexes of the True values in bool_list.
        """
    return list(compress(choices, bool_list))


def pick_randomized_questions(data, nb_questions):
    """
        Randomly selects a specified number of questions from each topic in a dictionary.

        Args:
        - data: a dictionary where each key is a topic and each value is a dictionary of questions.
        - nb_questions: a list of integers indicating how many questions to select for each topic.

        Returns:
        - exam_dic: a dictionary containing the selected questions, with keys representing question numbers and values representing question dictionaries.
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
    """
        Displays all questions in an exam form and records the student's answers.

        Args:
        - questions_dict: a dictionary of questions to be displayed, where keys represent question numbers and values are question dictionaries.
        - form: a Google Form object.
        - answers_dic: a dictionary to which the student's answers will be added.

        Returns:
        - answers_dic: the updated dictionary of student answers.
        """
    i = 1
    for question in questions_dict.values():
        display_question(form, question, i, answers_dic)
        i = i + 1
    return answers_dic


def get_answers(questions_dic):
    """
        Returns a dictionary of the expected answers for each question in an exam.

        Args:
        - questions_dic: a dictionary of questions, where keys represent question numbers and values are question dictionaries.

        Returns:
        - answers_dic: a dictionary of expected answers, where keys represent question numbers and values are lists of answer indexes.
        """
    answers_dic = {}
    for question in questions_dic:
        answers_dic[str(int(question) + 1)] = questions_dic[question]["answers"]
    return answers_dic


def get_results(dic_answers_expected, dic_answers_provided):
    """
       Grades a student's exam and returns the number correct, percentage correct, and a list of Boolean values indicating whether each question was answered correctly.

       Args:
       - dic_answers_expected: a dictionary of expected answers, where keys represent question numbers and values are lists of answer indexes.
       - dic_answers_provided: a dictionary of student answers, where keys represent question numbers and values are lists of answer indexes.

       Returns:
       - count_true: an integer representing the number of questions answered correctly.
       - percentage_true: a float representing the percentage of questions answered correctly.
       - result: a list of the right and wrong answers.
       """
    result = []
    for key in dic_answers_expected:
        if key in dic_answers_provided:
            result.append(dic_answers_expected[key] == dic_answers_provided[key])
    count_true = result.count(True)
    percentage_true = (count_true / len(result)) * 100
    return count_true, round(percentage_true, 1), result


def table_results(results_list):
    """
        Generates a pandas DataFrame containing the results of the exam.

        Args:
            results_list (list): A list of boolean values representing the correctness of the answers provided by the student.

        Returns:
            pandas.DataFrame: A DataFrame containing the results of the exam. The index contains the question numbers and the columns indicate if the answer was correct or incorrect, represented by a check mark or a cross respectively.
        """
    data = [(i + 1, "✅" if val else "❌") for i, val in enumerate(results_list)]
    df = pd.DataFrame(data, columns=["Question", "Result"])
    df.set_index("Question", inplace=True)
    return df
