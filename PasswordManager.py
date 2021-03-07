import csv

fields = ['Email', 'Password', 'URL']

# data rows of csv file  
email,password,url = input("Please Enter your Email, Password, and Website URL with a space in between each:").split()

print("Your Email is:", email)

print("Your Password is:", password)

print("The Website is:", url)

print("Your password.csv file should be in your foulder where the program is located")   

rows = [ [email, passwor, url ],
['unga bunga', 'bunga boo']]

# name of csv file  
filename = "Passwords.csv"
    
# writing to csv file  
with open(filename) as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 
    
