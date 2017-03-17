from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from xml.dom import minidom


def object_to_xml(tag, obj):
    elem = Element(tag)
    if isinstance(obj, list):
        for val in obj:
            child = object_to_xml('value', val)
            elem.append(child)
    elif isinstance(obj, dict):
        for key, val in obj.items():
            child = object_to_xml(key, val)
            elem.append(child)
    else:
        elem.text = str(obj)

    return elem


def pretty_print_xml(elem):
    return minidom.parseString(ElementTree.tostring(elem, 'utf-8')).toprettyxml(indent="    ")


def main():
    test1 = {
        'one': 1,
        'two': 2,
        'three': [
            1,
            2,
            3
        ],
        'four': 'four',
        'five': [
            'one',
            'two',
            'three'
        ],
        'six': {
            'one': 1,
            'two': [
                1,
                2
            ]
        }
    }

    test1_res = object_to_xml('test1', test1)
    print(pretty_print_element(test1_res))


if __name__ == '__main__':
    main()
