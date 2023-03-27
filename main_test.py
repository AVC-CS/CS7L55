
import main


def test_main():

    kargs = {'Math': 90, 'English': 100, 'Computer': 90}
    main.printscores1(**kargs)
    main.printscores2(kargs)
    main.printscores3(**kargs)

    # assert v1 == -10, "Min value does not match"
    # assert v2 == 5, "Max value does not match"
