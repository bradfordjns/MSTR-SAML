def file_transfer(folder, SAML):
    import os
    from os.path import join
    from os import listdir
    from shutil import move
    os.chdir(folder)
    for filename in listdir(folder):
        move(join(folder, filename), join(SAML, filename))

    return


def idp_changes(SAML, IDP):
    import os
    idp_target = SAML + 'IDPMetadata.xml'
    os.rename(IDP, idp_target)

    return


def web_xml_write(webinf, SAML):
    import os
    from web_move import web_xml_edits

    os.chdir(webinf)
    os.rename('web.xml', 'web_original.xml')

    web_xml_edits(webinf, SAML)
