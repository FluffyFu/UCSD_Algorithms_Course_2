# python3

from collections import namedtuple
from typing import List
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    """
    Naive implementation. For each task, loop through all the workers to find
    the next available work.

    Time Complexity O(n * m)
    """
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers: int, jobs: List[int]) -> List[AssignedJob]:
    """
    Given n_workers and a list of jobs (the time to finish), returns the worker id
    and job start time.

    Use a priority queue to store the worker. The key is a tuple (finish time, id).
    For each task, we pop the min from the PQ and update its finish time, then push it
    back to the PQ.

    Time Complexity O(m * log(n)), where m is the number of jobs and n is the number of workers.

    Returns:
        a list of tuples contains the worker's id and its start time.
    """
    results = []
    pq = [(0, i) for i in range(n_workers)]

    for job in jobs:
        start_time, worker_id = heapq.heappop(pq)
        results.append(AssignedJob(worker=worker_id, started_at=start_time))
        start_time += job
        heapq.heappush(pq, (start_time, worker_id))

    return results


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
