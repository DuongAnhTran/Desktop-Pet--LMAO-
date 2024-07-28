import pyautogui
import random
import tkinter as tk


x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'D:\Lecture notes\On-going\Semester Project\Desktop Pet (LMAO)'


#Event changes
#Transfer random no. to event
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('Staring at you right now :)')
        window.after(400, update_frame, cycle, check ,event_number, x) # 1,2, 3, 4 are idle

    elif event_number == 5:
        check = 1
        print('Getting eepy D:')
        window.after(200, update_frame, cycle, check, event_number, x) # 5 is going to sleep
    
    elif event_number in walk_left:
        check = 4
        print('Advancing to the left >:3')
        window.after(200, update_frame, cycle, check, event_number, x) # walk left 6, 7
    
    elif event_number in walk_right:
        check = 5
        print('Advancing to the right >:3')
        window.after(200, update_frame, cycle, check, event_number, x) # walk right 8, 9
    
    elif event_number in sleep_num:
        check = 2
        print('eeping :3')
        window.after(600, update_frame, cycle, check, event_number, x) #` 10,11,12,13,15 eep
    
    elif event_number == 14:
        check = 3
        print('stop eeping :D')
        window.after(100, update_frame, cycle, check, event_number, x) #14 sleep to idle

    #Explaination:
    #100/1000 in window.after is assigned to be the time in ms where 
    #the system will wait and initiate the update function
    #-> control the speed 4of the animation by changing this value



#To make the gif works:
def gif_working(cycle,frames,event_number,first_num,last_num):
    if cycle < len(frames) -1:
        cycle+=1
    else:
        cycle = 0
        event_number = random.randrange(first_num,last_num+1,1)
    return cycle,event_number
    
    #Explaination:
    #Every time when the function is called, the variable 'cycle' increase
    #However, when it is big enough to be length of frame array -1
    #It will reset back to 0 and change the event_number into a random num
    # -> Basically make it more natural


#Updating frame:
def update_frame(cycle, check, event_number, x):
    #idle:
    if check ==0:
        frame = idle[cycle]
        cycle ,event_number = gif_working(cycle,idle,event_number,1,9)
  
#idle to sleep
    elif check ==1:
        frame = idle_to_sleep[cycle]
        cycle ,event_number = gif_working(cycle,idle_to_sleep,event_number,10,10)


#sleep
    elif check == 2:
       frame = eep[cycle]
       cycle ,event_number = gif_working(cycle,eep,event_number,10,15)


#sleep to idle
    elif check ==3: 
       frame = sleep_to_idle[cycle]
       cycle ,event_number = gif_working(cycle,sleep_to_idle,event_number,1,1)


#walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle , event_number = gif_working(cycle,walk_positive,event_number,1,9)
        x -= 3


#walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle , event_number = gif_working(cycle,walk_negative,event_number,1,9)
        x -= -3
    window.geometry('72x60+'+str(x)+'+1050')
    label.configure(image=frame)
    window.after(1,event,cycle,check,event_number,x)



#call action .gif to an array
window = tk.Tk()


idle = [tk.PhotoImage(file='Animation 3\idle1.gif',format = 'gif -index %i' %(i)) for i in range(4)]#idle gif
idle_to_sleep = [tk.PhotoImage(file='Animation 3\idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(6)]#idle to sleep gif
eep = [tk.PhotoImage(file='Animation 3\sleeping.gif',format = 'gif -index %i' %(i)) for i in range(4)]#sleep gif
sleep_to_idle = [tk.PhotoImage(file='Animation 3\sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(6)]#sleep to idle gif
walk_positive = [tk.PhotoImage(file='Animation 3\walk_nega.gif',format = 'gif -index %i' %(i)) for i in range(4)]#walk to left gif
walk_negative = [tk.PhotoImage(file='Animation 3\walk_posi.gif',format = 'gif -index %i' %(i)) for i in range(4)]#walk to right gif


#Make the background transparent
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')

label = tk.Label(window, bd = 0, bg ='black')
label.pack()

#loop
window.after(1,update_frame,cycle,check,event_number,x)
window.mainloop()