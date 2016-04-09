import sys
from tkinter import *
readNextUserIdFrom = "../data/u.info"
addUserTo = "../data/u.user"


def loadUserProfile():
    return
    

def registerUser2():
    #user_id = getNewUserId()
    c = Checkbutton(state = ACTIVE, text="Expand").pack()
    form_label = Label(text= 'Personal information:').pack()
    
    name_e=Entry(textvariable = name).pack()#"Name:"										#Name will not be registered with user
    age_e = Entry(textvariable = age).pack()
    gender_e = Entry(textvariable = gender).pack()
    occ_e = Entry(textvariable = occupation).pack()
    zip_e = Entry(textvariable = zip_code).pack()

    continueButton = Button(text = 'Continue', command = cont).pack()

def cont():
    pref_label = Label(text= 'Check the boxes of your preferred genres:').pack()


    action_c = Checkbutton(state = ACTIVE, text = 'Action', variable = var1).pack()
    adventure_c = Checkbutton(state = ACTIVE, text = 'Adventure', variable = var2).pack()
    animation_c = Checkbutton(state = ACTIVE, text = 'Animation', variable = var3).pack()
    childrens_c = Checkbutton(state = ACTIVE, text = "Children's", variable = var4).pack()
    comedy_c = Checkbutton(state = ACTIVE, text = 'Comedy', variable = var5).pack()
    crime_c = Checkbutton(state = ACTIVE, text = 'Crime', variable = var6).pack()
    documentary_c = Checkbutton(state = ACTIVE, text = 'Documentary', variable = var7).pack()
    drama_c = Checkbutton(state = ACTIVE, text = 'Drama', variable = var8).pack()
    fantasy_c = Checkbutton(state = ACTIVE, text = 'Fantasy', variable = var9).pack()
    filmnoir_c = Checkbutton(state = ACTIVE, text = 'Film-Noir', variable = var10).pack()
    horror_c = Checkbutton(state = ACTIVE, text = 'Horror', variable = var11).pack()
    musical_c = Checkbutton(state = ACTIVE, text = 'Musical', variable = var12).pack()
    mystery_c = Checkbutton(state = ACTIVE, text = 'Mystery', variable = var13).pack()
    romance_c = Checkbutton(state = ACTIVE, text = 'Romance', variable = var14).pack()
    scifi_c = Checkbutton(state = ACTIVE, text = 'Sci-Fi', variable = var15).pack()
    thriller_c = Checkbutton(state = ACTIVE, text = 'Thriller', variable = var16).pack()
    war_c = Checkbutton(state = ACTIVE, text = 'War', variable = var17).pack()
    western_c = Checkbutton(state = ACTIVE, text = 'Western', variable = var18).pack()
    

    saveButton = Button(text = 'Save', command = save).pack()

def save():
    user_id = getNewUserId()
    
    print(var_list)
    var_list.extend((var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),var16.get(),var17.get(),var18.get()))
    print(var_list)
    print(var_list[0])
    print(len(var_list))
    prefs = "0"
    for i in range(0,len(var_list)):
        if var_list[i] == 1:
            prefs+= "1"
        else:
            prefs+= "0"
    preferences = prefs

    line_to_add = user_id + "|" + age.get() + "|" + gender.get() + "|" + occupation.get() + "|" + zip_code.get() + "|" + preferences
    addToUsers(line_to_add)
    registeredLabel = Label(text = 'You are now registered! Log in with user ID:     ' + user_id).pack()

def getNewUserId():
	file = open(readNextUserIdFrom, "r")
	next_id = str(int(file.readline().split()[0])+1)            #get first word of first line of u.info, which contains amount of users. Increment and return as string
	incrementTotalUsers(next_id)
	file.close()
	return next_id

def incrementTotalUsers(new_total):
	file = open(readNextUserIdFrom, "r")
	lines = file.readlines()
	file.close()
	print(lines)
	lines[0] = str(new_total) + " users\n"
	print(lines)
	file = open(readNextUserIdFrom, "w")
	for line in lines:
		file.write(line)
	file.close()

def addToUsers(line):
	users = open(addUserTo, "a")
	users.write("\n" + line)
	users.close()

mgui = Tk()

user_id = StringVar()
name = StringVar()
age = StringVar()
gender = StringVar()						#raw_input
occupation = StringVar()
zip_code = StringVar()
preferences = StringVar()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var_list = []

#genres from 0 - 18
genres = ['unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']


mgui.geometry('2000x1000+5000+200')
mgui.title('AppName')

header = Label(text='My label', fg='red', bg='blue', font=("Helvetica",20)).pack()         #.place(x=700, y=200)
new_user = Button(text = 'New User', command = registerUser2).pack()
log_in = Button(text = "Log in", command=loadUserProfile).pack()



#mgui.mainloop() Trenger dette til windows. Keeps the wondow running








################################
