import tkinter as tk, os
def shutdown():
    os.system('shutdown -s -t 0')
def restart():
    os.system('shutdown -r -t 0')
def hibernate():
    os.system('shutdown /h')
    
def help():
    root = tk.Tk()
    root.geometry('400x200')
    root.title('About')
    Help_label1 = tk.Label(root, text='Power Menu By Madana').place(relx=0.5, rely=0.2, anchor='center')
    Help_label2 = tk.Label(root, text='This Power menu is same, but there is one thing different\nThis Power menu can stop the PC from running\n (the common shutdown does not stop the PC)\n\nSleep does not included, its normal ("/)').place(relx=0.5, rely=0.5, anchor='center')
    got_it = tk.Button(root, text='Got it', command=button)
    root.mainloop()

def button():
    root = tk.Tk()
    root.title('Power')
    Shutdown = tk.Button(root, text='Shutdown', command=shutdown).place(relx=0.5, rely=0.2, anchor='center')
    Restart = tk.Button(root, text='Restart', command=restart).place(relx=0.5, rely=0.45, anchor='center')
    Hibernate = tk.Button(root, text='Hibernate', command=hibernate).place(relx=0.5, rely=0.7, anchor='center')
    Power_menu_label = tk.Label(root, text='Power menu').place(relx=0.5, rely=0.87, anchor='center')
    Help = tk.Button(root, text=' ? ', command=help).place(relx=0, rely=0, anchor='nw')

    root.mainloop()

button()