##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100
# pixels.
##############################################################################
import tkinter as tk
# main window
root = tk.Tk()
root.wm_geometry("200x200")

root.title("Authorization")
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news" )



frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(padx=50) 

ent_username = tk.Entry(frame_login, bd=3, show = "*") 
ent_username.pack()

lbl_password = tk.Label(frame_login, text='password:')
lbl_password.pack(padx=50) 

ent_password = tk.Entry(frame_login, bd=3, show = "*") 
ent_password.pack()

def test_button():
    print("click")
    frame_auth.tkraise()


button_login = tk.Button(frame_login, text='Login:', command = test_button)
button_login.pack()

#Authorization
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news" )









frame_login.tkraise()
root.mainloop()

