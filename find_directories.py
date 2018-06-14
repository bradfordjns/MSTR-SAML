def directory_search(folder):
    import os, tkMessageBox
    # root = Tkinter.Tk()
    # root.withdraw()

    # folder = tkFileDialog.askdirectory(parent=root, initialdir="/",
    #                                  title='Please select the MicroStrategy Stage directory')

    SAML_sep = 'stage'
    bin_sep = 'webapps'
    web_inf_sep = 'classes'
    SAML = folder.split(SAML_sep, 1)[0]
    tomcat = str(folder.split(bin_sep, 1)[0])
    bin_folder = tomcat + '/bin'
    WEBINF = folder.split(web_inf_sep, 1)[0]

    try:
        os.chdir(tomcat)
    except OSError:
        tkMessageBox.showwarning("MicroStrategy SAML Config",
                                 "Tomcat Folder does not exist, \n please review and update")
        exit()

    try:
        os.chdir('bin')
        bin_folder = os.getcwd()
        if os.path.basename(bin_folder) == 'bin':
            pass
        else:
            tkMessageBox.showwarning("MicroStrategy SAML Config",
                                     "tomcat bin Folder does not match the end of the path specified, \n please review and update")
            exit()
    except OSError:
        tkMessageBox.showwarning("MicroStrategy SAML Config",
                                 "tomcat bin Folder does not exist, \n please review and update")
        exit()

    os.chdir(SAML)
    saml_folder = os.getcwd()

    if os.path.isdir(SAML):
        if os.path.basename(saml_folder) == 'SAML':
            pass
        else:
            tkMessageBox.showwarning("MicroStrategy SAML Config",
                                     "SAMLFolder does not match the end of the path specified, \n please review and update")
            exit()
    else:
        tkMessageBox.showwarning("MicroStrategy SAML Config",
                                 "SAML Folder does not exist, \n please review and update")
        exit()
    if os.path.isdir(folder):
        if os.path.basename(folder) == 'stage':
            pass
        else:
            tkMessageBox.showwarning("MicroStrategy SAML Config",
                                     "stage Folder does not match the end of the path specified, \n please review and update")
            exit()
    else:
        tkMessageBox.showwarning("MicroStrategy SAML Config",
                                 "STAGE Folder does not exist, \n please review and update")
        exit()
    os.chdir(WEBINF)
    web_folder = os.getcwd()
    if os.path.isdir(WEBINF):
        if os.path.basename(web_folder) == 'WEB-INF':
            pass
        else:
            tkMessageBox.showwarning("MicroStrategy SAML Config",
                                     "WEB-INF Folder does not match the end of the path specified, \n please review and update")
            exit()
    else:
        tkMessageBox.showwarning("MicroStrategy SAML Config",
                                 "WEB-INF Folder does not exist, \n please review and update")
        exit()

    return folder, SAML, tomcat, bin_folder, WEBINF
