def get_first_or_none(sq):
    try:
        return sq[0]
    except IndexError:
        return None