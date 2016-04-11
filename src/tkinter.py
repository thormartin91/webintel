import sys
from tkinter import *
readNextUserIdFrom = "../data/u.info"
addUserTo = "../data/u.user"
from main import findMovies
from addUser import *


def promptUserLogin():
    user = StringVar()
    login_l = Label(text = 'Log in using your user ID:').pack()
    user_e = Entry(textvariable = user).pack()
    login_b = Button(text = 'Log in', command = lambda: loadUserProfile(user.get())).pack()
    

def loadUserProfile(user):
    welcome_label = Label(text = 'Welcome, user #'+user+'!', font = ('helvetica', 20)).pack()
    recommend_b = Button(text = 'Recommend a movie for me', command = lambda: recommend(user)).pack()

def recommend(user):
    ranked_list = findMovies(user)[0:10]
    if ranked_list:
        filler_l = Label(text = '').pack()
        recommendations_l = Label(text = 'Based on your user profile, we recommend these movies for you:').pack()
        listbox = Listbox(mgui, width=50, height=15)
        listbox.pack()
        for item in ranked_list:
            listbox.insert(END, item)
    else:
        filler_2 = Label(text = 'Please select movies you have seen and liked:').pack()
        possiblyRatableMovies = topGenre(user)
        v1 = IntVar()
        v2 = IntVar()
        v3 = IntVar()
        v4 = IntVar()
        v5 = IntVar()
        v6 = IntVar()
        v7 = IntVar()
        v8 = IntVar()
        v9 = IntVar()
        v10 = IntVar()

        movieToRate1 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[0]), variable = v1).pack()
        movieToRate2 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[1]), variable = v2).pack()
        movieToRate3 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[2]), variable = v3).pack()
        movieToRate4 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[3]), variable = v4).pack()
        movieToRate5 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[4]), variable = v5).pack()
        movieToRate6 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[5]), variable = v6).pack()
        movieToRate7 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[6]), variable = v7).pack()
        movieToRate8 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[7]), variable = v8).pack()
        movieToRate9 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[8]), variable = v9).pack()
        movieToRate10 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[9]), variable = v10).pack()

def registerUser():
    form_label = Label(text= 'Personal information:').pack()

    name_l = Label(text='Name:').pack()
    name_e=Entry(textvariable = name).pack()										#Name will not be registered with user
    age_l = Label(text='Age:').pack()
    age_e = Entry(textvariable = age).pack()
    gender_l = Label(text='Gender (M/F/O):').pack()
    gender_e = Entry(textvariable = gender).pack()
    occ_l = Label(text='Occupation:').pack()
    occ_e = Entry(textvariable = occupation).pack()
    zip_l = Label(text='Zip code:').pack()
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
    var_list.extend((var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),var16.get(),var17.get(),var18.get()))
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
    ok_button = Button(text = 'Ok', command =  close).pack()

def close():
    mgui.destroy()


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


mgui.geometry('700x850+500+10')
mgui.title('AppName')

header_label = Label(text='My Recommender System', fg='red', bg='blue', font=("Helvetica",25, 'bold')).pack()         #.place(x=700, y=200)
new_user = Button(text = 'New User', font = ('Helvetica', 15), command = registerUser).pack()
or_label = Label(text = "or").pack()
log_in = Button(text = "I have an account", command=promptUserLogin).pack()



#mgui.mainloop() Trenger dette til windows. Keeps the wondow running








################################
