import sys
import pytest
import streamlit as st
import pandas as pd

sys.path.append("..")
from utils.exam import (
    display_question,
    get_index_single_choice,
    get_indexes_multiple_choices,
    pick_randomized_questions,
    get_answers,
    get_results,
    table_results,
)


@pytest.fixture
def form():
    return st.form("123")


@pytest.fixture
def questions_dict():
    return {
        "0": {
            "questions": "What is the capital of France?",
            "choices": ["London", "Paris", "Madrid"],
            "expected_answers": 1,
            "answers": [2],
        },
        "1": {
            "questions": "Which of these countries are in Europe?",
            "choices": ["Spain", "France", "Brazil", "Italy"],
            "expected_answers": 3,
            "answers": [1,2,4],
        },
        "2": {
            "questions": "What is the largest country in the world?",
            "choices": ["USA", "China", "Russia", "India"],
            "expected_answers": 1,
            "answers": [4],
        },
    }


@pytest.fixture
def nb_questions():
    return [1, 1, 1]


def test_display_question_single_choice(form):
    answers_dic = {}
    question = {"questions": "What is the capital of France?", "choices": ["London", "Paris", "Madrid"], "expected_answers": 1}
    result = display_question(form, question, 1, answers_dic)
    assert result == {"1": 1}


def test_display_question_multiple_choices(form):
    answers_dic = {}
    question = {
        "questions": "Which of these countries are in Europe?",
        "choices": ["Spain", "France", "Brazil", "Italy"],
        "expected_answers": 3,
    }
    result = display_question(form, question, 2, answers_dic)
    assert result == {"2": []}


def test_get_index_single_choice():
    result = get_index_single_choice(["London", "Paris", "Madrid"], "Paris")
    assert result == 1


def test_get_indexes_multiple_choices():
    result = get_indexes_multiple_choices([1, 2, 3, 4, 5], [True, False, True, False, True])
    assert result == [1, 3, 5]


def test_pick_randomized_questions(questions_dict, nb_questions):
    result = pick_randomized_questions(questions_dict, nb_questions)
    assert len(result) == 3


def test_get_answers(questions_dict):
    result = get_answers(questions_dict)
    assert result == {'1': [2], '2': [1,2, 4], '3': [4]}


def test_get_results():
    dic_answers_expected = {"1": [1], "2": [3], "3": [3]}
    dic_answers_provided = {"1": [1], "2": [1, 2, 4], "3": [3]}
    count_true, percentage_true, result = get_results(dic_answers_expected, dic_answers_provided)
    assert count_true == 2
    assert percentage_true == 66.7
    assert result == [True, False, True]


def test_table_results():
    result = table_results([True, False, True])
    expected_answer = [(1, "✅"), (2, "❌"), (3, "✅")]
    df_expected = pd.DataFrame(expected_answer, columns=["Question", "Result"])
    df_expected.set_index("Question", inplace=True)
    assert result.equals(df_expected)