from phone_book import Query, process_queries


def test_process_queries():
    data = [
        ('add', 911, 'police'),
        ('add', 76213, 'Mom'),
        ('add', 17239, 'Bob'),
        ('find', 76213),
        ('find', 910),
        ('find', 911),
        ('del', 910),
        ('del', 911),
        ('find', 911),
        ('find', 76213),
        ('add', 76213, 'Dad'),
        ('find', 76213)
    ]
    queries = [Query(q) for q in data]

    results = process_queries(queries)
    assert results == ['Mom', 'not found', 'police', 'not found', 'Mom', 'Dad']
