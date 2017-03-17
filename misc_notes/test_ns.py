import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()

# iter_str ='{http://characters.example.com}./actor/name'
# iter_str = '{http://characters.example.com}'
#
# for elem in root.findall(iter_str):
#     print(elem.text)

# for actor in root.findall('{http://people.example.com}actor'):
#     name = actor.find('{http://people.example.com}name')
#     print name.text
#     for char in actor.findall('{http://characters.example.com}character'):
#         print ' |-->', char.text

for elem in root.findall('{http://people.example.com}actor'):
    for actor in elem.findall('./name'):
        print(actor.text)
