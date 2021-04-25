from freqtag import foo, Bar


def test_foo():
    assert foo() == 'foo'


def test_bar_init():
    arg = 'arg'
    bar = Bar(arg)
    assert bar.arg == arg
