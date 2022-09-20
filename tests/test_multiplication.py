"""This is the starting test file"""


def test_remove_meant_to_fail_must_remove():
    """This always passes"""
    assert 6 == m(2, 3)

def m(n1, n2):
    return n1*n2
