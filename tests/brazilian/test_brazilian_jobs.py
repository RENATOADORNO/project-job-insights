from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    list_job = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in list_job:
        assert job.get("title") is not None
        assert job.get("salary") is not None
        assert job.get("type") is not None
