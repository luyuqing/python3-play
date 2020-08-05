def test():
    a = {}
    try:
        x = a['a']
    except Exception as e:
        raise ValueError('wrong') from e


err = None
try:
    test()
except Exception as e:
    err = e


print((err, err.__cause__))  # (ValueError('wrong',), KeyError('a',))
