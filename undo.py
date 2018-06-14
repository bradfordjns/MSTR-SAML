import subprocess
import os
from os.path import join
from shutil import move
from os import listdir

saml_folder="/opt/apache-tomcat-8.5.31/webapps/MicroStrategy/WEB-INF/classes/resources/SAML/"
stage_folder="/opt/apache-tomcat-8.5.31/webapps/MicroStrategy/WEB-INF/classes/resources/SAML/stage/"
webinf_folder="/opt/apache-tomcat-8.5.31/webapps/MicroStrategy/WEB-INF/"
bin_folder="/opt/apache-tomcat-8.5.31/bin/"
os.chdir(saml_folder)
for filename in listdir(saml_folder):
    move(join(saml_folder, filename), join(stage_folder, filename))

os.chdir(webinf_folder)

web_source=webinf_folder+'web-original.xml'
web_target=webinf_folder+'web.xml'
os.rename(web_source, web_target)

os.chdir(bin_folder)

subprocess.call(['./startup.sh'])