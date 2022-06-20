import time


def display():

    
 print('#####################################################################################')

 for x in range(2):
    time.sleep(0.2)                                                                           
    print('#                                                                                   #')

 def line():
    for x in range(1):
        time.sleep(0.2)
        print('#  ###############################                                                  #')
        time.sleep(0.2)


 line()                                                                                     
 print('# J.A.R.V.I.S is listening.....                                                     #')
 line()
 time.sleep(1)
 print('#                                                                                   #')
 print('#  Following are the questions you can ask Jarvis:                                  # ')
 time.sleep(0.2)
 print("#  1. Tell the time                                                                 #")
 time.sleep(0.2)
 print("#  2. Introduce yourself                                                            #")
 time.sleep(0.2)
 print("#  3. Tell a joke                                                                   #")
 time.sleep(0.2)
 print("#  4. Give you information from wikipedia                                           #")
 time.sleep(0.2)
 print("#  5. Play a song                                                                   #")
 print('#####################################################################################')


display()