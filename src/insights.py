from src.jobs import read


def get_unique_job_types(path: str):
    jobs = read(path)
    job_types = [job["job_type"] for job in jobs]

    return list(set(job_types))


def filter_by_job_type(jobs, job_type):
    jobs_type = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_type.append(job)
    return jobs_type


def get_unique_industries(path: str):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    filtered = []
    for job in jobs:
        if job['industry'] == industry:
            filtered.append(job)
    return filtered


def get_max_salary(path: str):
    jobs = read(path)
    salaries = [
        int(job["max_salary"])
        for job in jobs
        if job["max_salary"].isdigit()
        ]

    return max(salaries)


def get_min_salary(path: str):
    jobs = read(path)
    salaries = [
        int(job["min_salary"])
        for job in jobs
        if job["min_salary"].isdigit()
        ]

    return min(salaries)


def matches_salary_range(job, salary):
    max_salary = job.get("max_salary", None)
    min_salary = job.get("min_salary", None)

    if type(max_salary) != int or type(min_salary) != int:
        raise ValueError()
    elif max_salary < min_salary:
        raise ValueError()
    elif type(salary) != int:
        raise ValueError()

    is_range = max_salary >= salary >= min_salary

    return is_range


def filter_by_salary_range(jobs, salary):
    filtered_jobs = [
        job
        for job in jobs
        if type(job["max_salary"]) == int
        and type(job["min_salary"]) == int
        and type(salary) == int
        and job["max_salary"] >= salary >= job["min_salary"]
    ]

    return filtered_jobs
