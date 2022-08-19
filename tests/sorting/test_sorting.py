from src.sorting import sort_by


SALARY_CRITERIAS = ["min_salary", "max_salary"]

SALARY = [
    {"max_salary": 9000, "min_salary": 2500},
    {"max_salary": 999, "min_salary": 1000},
    {"max_salary": 15000, "min_salary": 500},
    {"max_salary": 5, "min_salary": 2},
]


def test_sort_by_criteria():
    for criteria in SALARY_CRITERIAS:
        sort_by(SALARY, criteria)
        if criteria == "min_salary":
            assert (SALARY[0][criteria] <= SALARY[1][criteria])
            assert (SALARY[1][criteria] <= SALARY[2][criteria])
            assert (SALARY[2][criteria] <= SALARY[3][criteria])

        else:
            assert (SALARY[0][criteria] >= SALARY[1][criteria])
            assert (SALARY[1][criteria] >= SALARY[2][criteria])
            assert (SALARY[2][criteria] >= SALARY[3][criteria])
