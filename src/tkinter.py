import sys
from tkinter import *
readNextUserIdFrom = "../data/u.info"
addUserTo = "../data/database.users"
from main import *
from addUser import *
from addRating import *


def start():
    filler.pack()
    new_user.pack()
    or_label.pack()
    log_in.pack()

def promptUserLogin():
    removeSuperflousWidgets()
    login_l.pack()
    user_e = Entry(textvariable = current_user).pack()
    login_b.pack()


def loadUserProfile():
    registeredLabel.pack_forget()
    login_b.pack_forget()
    login_l.pack_forget()
    hello_label.pack()
    recommend_b.pack()

def recommend():
    user = current_user.get()
    recommend_b.pack_forget()
    hello_label.pack_forget()
    ranked_list = findMovies(user)
    if ranked_list:
        filler.pack()
        recommendations_l.pack()
        listbox.pack()
        for item in ranked_list:
            listbox.insert(END, item)
        close_b = Button(text = 'Close', command = lambda: mgui.destroy()).pack()
    else:
        select_l.pack()
        filler.pack()
        global possiblyRatableMovies
        possiblyRatableMovies = topGenre(user)

        movieToRate1 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[0]), variable = v1)
        movieToRate2 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[1]), variable = v2)
        movieToRate3 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[2]), variable = v3)
        movieToRate4 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[3]), variable = v4)
        movieToRate5 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[4]), variable = v5)
        movieToRate6 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[5]), variable = v6)
        movieToRate7 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[6]), variable = v7)
        movieToRate8 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[7]), variable = v8)
        movieToRate9 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[8]), variable = v9)
        movieToRate10 = Checkbutton(state = ACTIVE, text = str(possiblyRatableMovies[9]), variable = v10)

        movieToRate1.pack()
        movieToRate2.pack()
        movieToRate3.pack()
        movieToRate4.pack()
        movieToRate5.pack()
        movieToRate6.pack()
        movieToRate7.pack()
        movieToRate8.pack()
        movieToRate9.pack()
        movieToRate10.pack()
        #cont_b = Button(text='Continue', command = lambda: saveRatings(possiblyRatableMovies)).pack()
        cont_b.pack()
        
def saveRatings():
    movies = possiblyRatableMovies
    print(possiblyRatableMovies, "WAAAAAAAAAAAAAAAAAAAAAAWAAAAAAAAAAAAAAAAAAAAAAWAAAAAAAAAAAAAAAA")
    cont_b.pack_forget()
    v_list = [v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get()]
    print(len(v_list))
    print(v_list)
    for i in range(0,len(v_list)):
        print('This one is = ' + str(v_list[i]))
        print('movie is = ' + movies[i])
        if v_list[i] == 1:
            addRating(movies[i], str(current_user.get()), "4.8")              #addRating(movie_id, user_id, rating)
        else:
            pass
    file = open('../data/database.ratings', "r")
    lines = file.readlines()
    file.close()
    print(lines.pop())
    recommend_b = Button(text='Recommend', command = lambda: recommend()).pack()

def registerUser():
    removeSuperflousWidgets()
    form_label.pack()

    name_l.pack()
    name_e.pack()										#Name will not be registered with user
    age_l.pack()
    age_e.pack()
    gender_l.pack()
    gender_e.pack()
    occ_l.pack()
    occ_e.pack()
    zip_l.pack()
    zip_e.pack()

    continueButton.pack()

def setPrefs():
    continueButton.pack_forget()
    form_label.pack_forget()

    name_l.pack_forget()
    name_e.pack_forget()										#Name will not be registered with user
    age_l.pack_forget()
    age_e.pack_forget()
    gender_l.pack_forget()
    gender_e.pack_forget()
    occ_l.pack_forget()
    occ_e.pack_forget()
    zip_l.pack_forget()
    zip_e.pack_forget()   

    pref_label.pack()


    action_c.pack()
    adventure_c.pack()
    animation_c.pack()
    childrens_c.pack()
    comedy_c.pack()
    crime_c.pack()
    documentary_c.pack()
    drama_c.pack()
    fantasy_c.pack()
    filmnoir_c.pack()
    horror_c.pack()
    musical_c.pack()
    mystery_c.pack()
    romance_c.pack()
    scifi_c.pack()
    thriller_c.pack()
    war_c.pack()
    western_c.pack()
    

    saveButton.pack()

def save():
    saveButton.pack_forget()
    pref_label.pack_forget()
    action_c.pack_forget()
    adventure_c.pack_forget()
    animation_c.pack_forget()
    childrens_c.pack_forget()
    comedy_c.pack_forget()
    crime_c.pack_forget()
    documentary_c.pack_forget()
    drama_c.pack_forget()
    fantasy_c.pack_forget()
    filmnoir_c.pack_forget()
    horror_c.pack_forget()
    musical_c.pack_forget()
    mystery_c.pack_forget()
    romance_c.pack_forget()
    scifi_c.pack_forget()
    thriller_c.pack_forget()
    war_c.pack_forget()
    western_c.pack_forget()
    saveButton.pack_forget()

    user = getNewUserId()
    var_list.extend((var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get(),var13.get(),var14.get(),var15.get(),var16.get(),var17.get(),var18.get()))
    prefs = "0"
    for i in range(0,len(var_list)):
        if var_list[i] == 1:
            prefs+= "1"
        else:
            prefs+= "0"
    preferences = prefs
    line_to_add = user + "|" + age.get() + "|" + gender.get() + "|" + occupation.get() + "|" + zip_code.get() + "|" + preferences
    addToUsers(line_to_add)
    registeredLabel.pack()
    user_info_l = Label(text = user).pack()
    ok_button.pack()
    

def removeSuperflousWidgets():
    registeredLabel.pack_forget()
    new_user.pack_forget()
    or_label.pack_forget()
    log_in.pack_forget()
    ok_button.pack_forget()

mgui = Tk()

user_id = StringVar()
name = StringVar()
age = StringVar()
gender = StringVar()						#raw_input
occupation = StringVar()
zip_code = StringVar()
preferences = StringVar()

current_user = StringVar()

#Genre variables
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

# Movie rating variables
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
v_list = []

#genres from 0 - 18
genres = ['unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

#GUI specs
mgui.geometry('700x850+500+10')
mgui.title('RecSys')

#Labels and buttons to be shown and hidden
header_label = Label(mgui,text='My Recommender System', fg="black", font=("Helvetica",25, 'bold')).pack()    #.place(x=700, y=200)
start_filler = Label(mgui, text = '').pack()
start_b = Button(text = 'Home', command = start).pack()
new_user = Button(mgui, text = 'New User', command = registerUser)#.pack()
or_label = Label(mgui, text = "or")#.pack()
log_in = Button(mgui, text = "I have an account", command=promptUserLogin)#.pack()
login_l = Label(mgui, text = 'Log in using your user ID:')
recommendations_l = Label(text = 'Based on your user profile, we recommend these movies for you:')
listbox = Listbox(mgui, width=50, height=15)
select_l = Label(text = 'Please select movies you have seen and liked:')
filler = Label(text = '')
login_b = Button(text = 'Log in', command = lambda: loadUserProfile())
recommend_b = Button(text = 'Recommend a movie for me', command = lambda: recommend())

possiblyRatableMovies = []
cont_b = Button(text='Continue', command = lambda: saveRatings())

form_label = Label(text= 'Personal information:')
name_l = Label(text='Name:')
name_e=Entry(textvariable = name)										#Name will not be registered with user
age_l = Label(text='Age:')
age_e = Entry(textvariable = age)
gender_l = Label(text='Gender (M/F/O):')
gender_e = Entry(textvariable = gender)
occ_l = Label(text='Occupation:')
occ_e = Entry(textvariable = occupation)
zip_l = Label(text='Zip code:')
zip_e = Entry(textvariable = zip_code)
continueButton = Button(text = 'Continue', command = setPrefs)

pref_label = Label(text= 'Check the boxes of your preferred genres:')
action_c = Checkbutton(state = ACTIVE, text = 'Action', variable = var1)
adventure_c = Checkbutton(state = ACTIVE, text = 'Adventure', variable = var2)
animation_c = Checkbutton(state = ACTIVE, text = 'Animation', variable = var3)
childrens_c = Checkbutton(state = ACTIVE, text = "Children's", variable = var4)
comedy_c = Checkbutton(state = ACTIVE, text = 'Comedy', variable = var5)
crime_c = Checkbutton(state = ACTIVE, text = 'Crime', variable = var6)
documentary_c = Checkbutton(state = ACTIVE, text = 'Documentary', variable = var7)
drama_c = Checkbutton(state = ACTIVE, text = 'Drama', variable = var8)
fantasy_c = Checkbutton(state = ACTIVE, text = 'Fantasy', variable = var9)
filmnoir_c = Checkbutton(state = ACTIVE, text = 'Film-Noir', variable = var10)
horror_c = Checkbutton(state = ACTIVE, text = 'Horror', variable = var11)
musical_c = Checkbutton(state = ACTIVE, text = 'Musical', variable = var12)
mystery_c = Checkbutton(state = ACTIVE, text = 'Mystery', variable = var13)
romance_c = Checkbutton(state = ACTIVE, text = 'Romance', variable = var14)
scifi_c = Checkbutton(state = ACTIVE, text = 'Sci-Fi', variable = var15)
thriller_c = Checkbutton(state = ACTIVE, text = 'Thriller', variable = var16)
war_c = Checkbutton(state = ACTIVE, text = 'War', variable = var17)
western_c = Checkbutton(state = ACTIVE, text = 'Western', variable = var18)
saveButton = Button(text = 'Save', command = save)

registeredLabel = Label(text = 'You are now registered! Log in with user ID: ')
ok_button = Button(text = 'OK', command = lambda: promptUserLogin())
hello_label = Label(mgui, text = 'Hello, friendly user!', font = ('helvetica', 15))



#mgui.mainloop() Trenger dette til windows. Keeps the wondow running








################################
