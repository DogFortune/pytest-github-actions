from create_param import main

def test_main():
    actual = main.main(3, 4)
    assert actual == 5