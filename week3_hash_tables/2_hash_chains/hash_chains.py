# python3
from typing import List


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class Node:
    def __init__(self, value: str, next_node=None):
        self._value = value
        self._next_node = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v: str):
        self._value = v

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, n: 'Node'):
        self._next_node = n


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems: List[Node] = [None for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'check':
            if self.elems[query.ind]:
                chain = self._collect_str(query.ind)
                self.write_chain(chain)
            else:
                print('')
        else:
            h_v = self._hash_func(query.s)
            cur_node = self.elems[h_v]
            is_exist = False

            if query.type == 'find':
                while cur_node:
                    if cur_node.value == query.s:
                        self.write_search_result(True)
                        return
                    cur_node = cur_node.next_node
                self.write_search_result(False)

            elif query.type == 'add':
                while cur_node:
                    if cur_node.value == query.s:
                        is_exist = True
                        break
                    cur_node = cur_node.next_node
                if not is_exist:
                    new_node = Node(query.s, next_node=self.elems[h_v])
                    self.elems[h_v] = new_node

            elif query.type == 'del':
                if not cur_node:
                    return
                elif cur_node.value == query.s:
                    self.elems[h_v] = cur_node.next_node
                else:
                    pre_node = cur_node
                    cur_node = cur_node.next_node
                    while cur_node:
                        if cur_node.value == query.s:
                            is_exist = True
                            break
                        pre_node = cur_node
                        cur_node = cur_node.next_node
                    if is_exist:
                        pre_node.next_node = cur_node.next_node

    def _collect_str(self, i: int) -> List[str]:
        """
        Internal helper function to collect the values the linked list.
        """
        cur = self.elems[i]
        res = []
        while cur:
            res.append(cur.value)
            cur = cur.next_node

        return res

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
