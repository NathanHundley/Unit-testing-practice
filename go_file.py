def do_stuff(num=1):
    try:
        if num == 0:
            return 5
        elif num:
            return int(num) + 5
        else:
            return 'Please enter a number.'
    except ValueError as err:
        return err