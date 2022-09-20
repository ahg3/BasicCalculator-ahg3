"""This is the starting test file"""


def test_remove_meant_to_fail_must_remove():
    """This always passes"""
    assert 3 == div(6,2)

def div (n1, n2):
    return n1 / n2;

