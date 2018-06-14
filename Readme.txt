------------Read Me for the MicroStrategySAML tool------------

Note: This will only work currently as of 5/25/18 for the MicroStrategy Web and Mobile applications on Tomcat. 


The zipped folder contains two files:

1. MicroStrategySAML_GUI_win.exe	-	command window will be hidden
		
2. MicroStrategySAML_GUI_linux	-	command window will be shown

	
	
	> Both executables will:
		1. 	Ask the user for the MicroStrategy Web/Mobile Stage Directory:
		3. 	Ask the user for the file to become the IDPMetadata.xml
		4. 	Start/stop tomcat
		5. 	Perform all the file movements from the MicroStrategy Web/Mobile Stage Directory to the SAML Directory
		6. 	Create a backup of the current Web.xml file and rename as Web_original.xml
		7. 	Edit the Web.xml file:
				- Remove the secuirty contraints
				- Remove the original SAML support lines
				- Append the WebXMLChanges.txt content to configure for SAML Authenication
		8. 	Move the IDPMetadata.xml File to the SAML Directory
		
		*** If the SPMetadata.xml configuration files have not been generated please use the "Go to Config Open Page" 
		*** This will prepopulate the URL to use which will be set to port 8080 and the MicroStrategy Web application
		
		
Troubleshooting:

	1. 	Take a screenshot of the command window when the error occurs
	2.	Collect the "Log_SAML_Config.txt" file that is created in the same folder where the executable is ran from
		- A successfull run will output a file that displays:
		
				pressed start button

				got the idp information

				got the stage folder information

				got the idp information, saml, stage amd webinf folfer info

				stopped tomcat

				moved all the files in the stage folder to the saml folder

				moved the idp file to the saml folder and made it named IDPMetadata.xml

				removed the old saml config from web.xml

				removed the admin, taskadmin, and taskdev security constraints from web.xml

				add the WebXmlChanges.txt content to web.xml

				renamed the original web.xml to web_original.xml

				started tomcat

				successfully ending last function
		

	

Information:

For any questions or enhancements please contact:

Bradford Jones
bjones@microstrategy.com 



------------Read Me for the MicroStrategySAML  tool------------