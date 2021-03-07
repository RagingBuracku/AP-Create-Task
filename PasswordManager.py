import csv

fields = ['Email', 'Password', 'URL']

# data rows of csv file  
a,b,c = input("Please Enter your Email, Password, and Website URL with a space in between each:").split()

print("Your Email is:", a)

print("Your Password is:", b)

print("The Website is:", c)

print("Your password.csv file should be in your foulder where the program is located")   

rows = [ [a, b, c ],
['unga bunga', 'bunga boo']]

# name of csv file  
filename = "Passwords.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 
    
