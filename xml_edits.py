def read_xml(WEBINF):
    import os

    os.chdir(WEBINF)

    lines = [line.rstrip('\n') for line in open('web.xml')]
    return lines


def remove_org_saml_support(lines):
    len_lines = len(lines)

    position_in_file_s = []
    position_in_file_end_s = []

    for i in range(0, len_lines):
        if "<!-- SAML Config GUI -->" in lines[i]:
            position_in_file_s.append(i + 1)
        if " <!-- End SAML Config GUI -->" in lines[i]:
            position_in_file_end_s.append(i)

    lines[position_in_file_s[0]:position_in_file_end_s[0]] = []

    return lines, position_in_file_end_s, position_in_file_s


def remove_security_constraints(lines):
    position_in_file = []
    position_in_file_end = []

    len_lines = len(lines)
    for i in range(0, len_lines):

        if "<security-constraint>" in lines[i]:
            position_in_file.append(i)
        if "</security-constraint>" in lines[i]:
            position_in_file_end.append(i + 1)

    len_file = len(position_in_file) - 1

    for ii in range(len_file, 0, -1):
        lines[position_in_file[ii]:position_in_file_end[ii]] = []

    lines[position_in_file[0]:position_in_file_end[0]] = []

    return lines


# noinspection PyUnusedLocal,PyUnusedLocal
def add_web_changes(SAML, lines, folder, position_in_file_end_s, position_in_file_s):
    import os
    os.chdir(SAML)
    thisFile = "WebXmlChanges.txt"
    web_xml_rows = []
    for line in lines:
        web_xml_rows.append(line.strip().split('\t'))

    web_changes_rows = []

    with open(thisFile) as g:
        g_contents = map(str.rstrip, g)

    for line in g_contents:
        web_changes_rows.append(line.strip().split('\t'))

    g.close()

    start_pos = position_in_file_s[0]

    for x in range(0, len(web_changes_rows)):
        web_xml_rows.insert((start_pos + x), web_changes_rows[x])

    result = ''
    for element in web_xml_rows:
        result += str(element)

    newstr = result.replace("'", "")
    newstr = newstr.replace("[", "")
    lines = newstr.replace("]", "")

    return lines


def web_xml_write(webinf):
    import os
    os.chdir(webinf)
    os.rename('web.xml', 'web_original.xml')
