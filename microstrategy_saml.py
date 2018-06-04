def microstrategy_saml_func(folder, IDP):
    from file_movements import idp_changes
    from find_directories import directory_search
    from tomcat_actions import stop_tomcat
    from tomcat_actions import start_tomcat
    from file_movements import file_transfer
    from file_movements import web_xml_write

    #################################

    # directory_search handles getting the names of all the directories needed to move the files and start/stop tomcat
    # the directory_search function requires the stage folder as an input
    [folder, SAML, tomcat, bin_folder, WEBINF] = directory_search(folder)
    print('got the idp information, saml, stage amd webinf folfer info\n')
    #################################

    import os
    current = os.getcwd

    # the stop_tomcat function required the tomcat bin folder as an input. Will navigate the the bin folder and run the shutdown.sh script

    stop_tomcat(bin_folder)
    print('stopped tomcat\n')

    #################################

    # this function requires the target SAML  and the stage directories as inputs. The files in the staging will then be moved to the SAML directory

    file_transfer(folder, SAML)
    print('moved all the files in the stage folder to the saml folder\n')

    #################################

    # idp_changes handle the renaming and movements of the IDPMetadata
    # this function requires the target SAML directory as an input the function will prompt the user for the location of the file that will be renamed as IDPMetadata.xml the file will then be moved to the correct directory

    idp_changes(SAML, IDP)
    print('moved the idp file to the saml folder and made it named IDPMetadata.xml\n')

    #################################

    # web_xml_write handles writing to file the updated web.xml file
    # this function requires the the string array of the web.xml and the WEB-INF directory as an input
    web_xml_write(WEBINF, SAML)
    print('renamed the original web.xml to web_original.xml\n')

    #################################

    # start_tomcat will start tomcat after all the file changes have been made
    # this function requires the locations of the tomcat bin folder as an input.
    start_tomcat(bin_folder)
    print('started tomcat\n')
