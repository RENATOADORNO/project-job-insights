from src.counter import count_ocurrences
from unittest.mock import mock_open, patch
import pytest


@pytest.fixture
def jobs():
    return [
        {"title": "Front end developer", "salary": "2000", "type": "trainee"},
        {"title": "Back end developer", "salary": "3000", "type": "full time"},
        {
            "title": "Full stack end developer",
            "salary": "4000",
            "type": "full time",
        },
    ]


def test_counter(jobs):
    with patch("builtins.open", mock_open(read_data=str(jobs))):
        normal_counter = count_ocurrences("src/jobs.csv", "developer")
        assert normal_counter == 3

        sensitive_counter = count_ocurrences("src/jobs.csv", "dEvELoPER")
        assert sensitive_counter == 3
