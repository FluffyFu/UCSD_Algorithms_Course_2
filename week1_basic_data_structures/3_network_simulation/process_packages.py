# python3

from collections import namedtuple
from typing import List
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    """
    Buffer with given size to store and process network package.
    """

    def __init__(self, size: int):
        self._size = size
        self._finish_time: deque = deque(maxlen=size)

    def process(self, request: Request):
        arrive_time = request.arrived_at

        # pop jobs that has already finished.
        while len(self._finish_time) > 0 and self._finish_time[0] <= arrive_time:
            self._finish_time.popleft()

        # insert current request if there's space in the buffer
        if len(self._finish_time) == 0:
            # no other jobs in the queue, start time is arrival time.
            self._finish_time.append(request.time_to_process + arrive_time)
            return Response(False, arrive_time)

        elif len(self._finish_time) < self._size:
            # some other jobs in queue, start time is the finish time of the last job in queue.
            previous_finish_time = self._finish_time[-1]
            self._finish_time.append(
                previous_finish_time + request.time_to_process)
            return Response(False, previous_finish_time)
        else:
            # no space in buffer, drop this job.
            return Response(True, -1)


def process_requests(requests: List[Request], net_buffer: Buffer) -> List[Response]:
    """
    Process a series of Requests with the buffer.

    Returns:
        The response of the Requests
    """
    responses = []
    for request in requests:
        responses.append(net_buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    net_buffer = Buffer(buffer_size)
    responses = process_requests(requests, net_buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
