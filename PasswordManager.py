import csv
import tkinter

# GUI setup
# Colors: honeydew: #F0FFF0, white: #FFFFFF
ws = Tk()
ws.title("Passsword Manager")
ws.geometry('500x300')
ws.configure(bg='#FFFFFF')

#GUI login & 
login = tk.button(text="Login", width=25, height=5, fg='#F0FFF0', bg='#FFFFFF')
register = tk.button(text="Register", fg='#F0FFF0', bg='#FFFFFF')

fields = ['Email', 'Password', 'URL']

# data rows of csv file  
a,b,c = input("Please Enter your Email, Password, and Website URL with a space in between each:").split()

print("Your Email is:", a)

print("Your Password is:", b)

print("The Website is:", c)

print("Your password.csv file should be in your foulder where the program is located")   

rows = [ [a, b, c ] ]

# name of csv file  
filename = "Passwords.csv"
    
# writing to csv file  
with open(filename, 'w', newline="\n") as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 
    
winddow.mainloop()

