class StripText:
    def __init__(self, chars=' \r\t\n'):
        self.chars = chars

    def __call__(self, value):
        try:
            return value.strip(self.chars)
        except:  # noqa E722
            return value

def str_to_float(x):
    x = x.replace(',', '')
    try:
        return float(x)
    except:  # noqa E722
        return x


def str_to_int(x):
    try:
        return int(str_to_float(x))
    except:  # noqa E722
        return x