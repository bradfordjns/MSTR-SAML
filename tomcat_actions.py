def start_tomcat(bin_folder):
    # import win32serviceutil
    import os
    
    import time
    from subprocess import Popen
    import tkMessageBox


    import platform
    import subprocess
    op_sys=platform.system()
    os.chdir(bin_folder)
    if op_sys=="Linux":
      subprocess.call(['./startup.sh'])
    else:
      Popen("startup.bat")
    time.sleep(3)
    # noinspection PyUnusedLocal
    msg = tkMessageBox.showinfo("MicroStrategy SAML Config", "Tomcat has been successfully started\nplease wait till Tomcat is fully started")

    return


# noinspection PyUnusedLocal
def stop_tomcat(bin_folder):
    # import win32serviceutil
    import os
    import time
    import tkMessageBox

    from subprocess import Popen
    import platform
    import subprocess
    op_sys=platform.system()
    os.chdir(bin_folder)
    if op_sys=="Linux":
      subprocess.call(['./shutdown.sh'])
    else:
      Popen("shutdown.bat")

    time.sleep(3)
    msg = tkMessageBox.showinfo("MicroStrategy SAML Config", "Tomcat has been successfully stopped\n changes to the Virtual Directory will now be made")
    return
