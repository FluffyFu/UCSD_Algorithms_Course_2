from job_queue import assign_jobs, assign_jobs_naive, AssignedJob
from hypothesis import given, assume
import hypothesis.strategies as st
import glob


@given(st.lists(st.integers(min_value=1)), st.integers(min_value=1, max_value=1000))
def test_assign_jobs_random(jobs, n_workers):
    assume(len(jobs) >= 1)
    assert assign_jobs(n_workers, jobs) == assign_jobs_naive(n_workers, jobs)


def test_assign_jobs_cases():
    all_files = glob.glob('tests/')

    q_names = sorted([f for f in all_files if 'a' not in f])
    a_names = sorted([f for f in all_files if 'a' in f])

    for q, a in zip(q_names, a_names):
        with open(q) as f:
            n_workers, n_jobs = map(int, f.readline().split())
            jobs = list(map(int, f.readline().split()))

        truth = []
        with open(a) as f:
            for line in f.readlines():
                worker, start_at = map(int, line.split())

            truth.append(AssignedJob(worker=worker, start_at=start_at))

        assert assign_jobs(n_workers, jobs) == truth
