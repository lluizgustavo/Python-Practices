# another_test.py
def test_list_item_multiply(my_list):
    assert [item * 3 for item in my_list] == [3, 6, 9]


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: marks tests as slow"
    )