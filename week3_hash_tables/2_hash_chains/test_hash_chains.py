from hash_chains import Query, QueryProcessor
import pudb


def test_query_processor():
    pudb.set_trace()

    bucket_count = 5
    qp = QueryProcessor(bucket_count)

    q1 = Query(('add', 'world'))
    q2 = Query(('add', 'HellO'))

    qp.process_query(q1)
    qp.process_query(q2)
