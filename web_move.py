# noinspection PyUnusedLocal
def web_xml_edits(webinf, SAML):
    import itertools
    import xml.etree.ElementTree
    import os
    from os.path import join
    from shutil import move
    import tkMessageBox
    # get correct directory
    os.chdir(webinf)

    #root = ElementTree.parse("web_original.xml").getroot()
    root = xml.etree.ElementTree.parse("web_original.xml").getroot()
    # b = root.getchildren()[39]

    servlet = root.getchildren()[2]
    servlet_map = root.getchildren()[3]
    root.remove(servlet)
    root.remove(servlet_map)

    name = root.find('{http://java.sun.com/xml/ns/j2ee}servlet')
    print('removed the old saml config from web.xml\n')
    for x in range(0, len(name) - 2):
        root.remove(name[x])

    name = root.findall("{http://java.sun.com/xml/ns/j2ee}security-constraint")

    # only remove this first three from name

    for x in range(0, len(name) - 1):
        root.remove(name[x])
    print('removed the admin, taskadmin, and taskdev security constraints from web.xml\n')
    # ElementTree.dump(root)

    # get correct directory
    os.chdir(SAML)

    with open("WebXmlChanges.txt") as f:
        it = itertools.chain('<root>', f, '</root>')
        test = xml.etree.ElementTree.fromstringlist(it)

    # noinspection PyUnusedLocal,PyUnusedLocal
    msg = tkMessageBox.showinfo("MicroStrategy SAML Config",
                                "just opened the web_changes folder")
    # noinspection PyUnusedLocal
    ns = root.tag

    a = len(test.getchildren())

    for x in range(0, a):
        b = len(test.getchildren()[x].getchildren())
        new_tag = '{http://java.sun.com/xml/ns/j2ee}' + test.getchildren()[x].tag
        test.getchildren()[x].tag = new_tag
        for xx in range(0, b):
            new_tag = '{http://java.sun.com/xml/ns/j2ee}' + test.getchildren()[x].getchildren()[xx].tag
            test.getchildren()[x].getchildren()[xx].tag = new_tag

    root_start = 2
    for x in range(0, a):
        root.insert(root_start, test.getchildren()[x])
        root_start = root_start + 1

    # ElementTree.dump(root)

    tree = xml.etree.ElementTree.ElementTree(root)
    print('add the WebXmlChanges.txt content to web.xml\n')
    tree.write(open('web.xml', 'wb'))

    file_test = open('web.xml', 'r')

    # noinspection PyUnusedLocal
    msg = tkMessageBox.showinfo("MicroStrategy SAML Config",
                                "just opened the web_original folder")

    data = file_test.read().replace('\n', '')

    file_test.close()

    data = data.replace('ns0:', '')
    prefixed = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>' + data

    file_test = open('web.xml', 'wb')
    file_test.write(prefixed)
    file_test.close()

    move(join(SAML, 'web.xml'), join(webinf, 'web.xml'))
