"""
Screenshot Grabber

Requirements:
On a priveldged terminal window, input "pip install pywin32"
"""
import base64
from operator import le
from turtle import width
import win32api # Provides various libraries and objects utilized to deal with the Windows system's API
import win32con
import win32gui
import win32ui

def get_dimensions():
    # Used to determine the required dimensions for a screenshot
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width, height, left, top)

def screenshot(name='screenshot'):
    hdesktop = win32gui.GetDesktopWindow()
    # Acquire a handle to the entire desktop, which includes th entire viewable area across multiple monitors
    width, height, left, top = get_dimensions()

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    # Use the GetWindowDC function call and pass in a handle to the desktop
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()
    # Create a memory-based device context where we will store our screenshot until we write the bitmap bytes to a file

    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
    # Create a bitmap object that is set to the device context of the desktop. 
    # The SelectObject call then sets the memory-based device context to point at the bitmap obejct that we are capturing.
    screenshot.SaveBitmapFile(mem_dc, f'{name}.bmp')
    # Dump this screenshot to the disk.
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

def run():
    # Calls the screenshot function to create an image, then reads and returns the file data
    screenshot()
    with open('screenshot.bmp') as f:
        img = f.read()
    return img

if __name__ == '__main__':
    screenshot()
