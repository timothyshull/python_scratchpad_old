import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element


if __name__ == '__main__':
    avg(1, 2)
    avg(1, 2, 3, 4)
    make_element('item', 'Albatross', size='large', quantity=6)
    make_element('p', '<span>')
