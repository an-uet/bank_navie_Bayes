import pandas as pd
from tkinter import *

def XScoulmtranging(data, rows):
    yes = 0
    no = 0
    for i in rows:
        if data[i][-1] == "yes":
            yes += 1
        else:
            no += 1
    ansn = no / (yes + no)
    ansy = yes / (yes + no)
    return ansy, ansn, yes, no


def NaiveBayes(data, rows, columns, X):
    ansy, ansn, yes, no = XScoulmtranging(data, rows)
    mulyes = 1
    mulno = 1
    list_count_yes = []
    list_count_no = []
    y = 0
    n = 0
    for j in columns:
        countyes = 0
        countno = 0
        key = X[list(X)[j]]
        for i in rows:
            if data[i][j] == key:
                if data[i][-1] == "yes":
                    countyes += 1
                else:
                    countno += 1
        list_count_yes.append(countyes)
        list_count_no.append(countno)
    for i in range(0, len(list_count_yes)):
        if list_count_yes[i] == 0:
            y += 1
    for i in range(0, len(list_count_no)):
        if list_count_no[i] == 0:
            n += 1
    for i in range(0, len(list_count_yes)):
        if y == 0:
            mulyes *= list_count_yes[i] / yes
        else:
            mulyes *=float((1 + list_count_yes[i])/(yes + len(X)))
    for i in range(0, len(list_count_no)):
        if n == 0:
            mulno *= float(list_count_no[i] / no)
        else:
            mulno *= float((1 + list_count_no[i])/(no + len(X)))
    p_yes = mulyes * ansy
    p_no = mulno * ansn
    print(ansy,ansn)
    print("khách hàng X có khả năng đăng ký một khoản tiền gửi có kỳ hạn (biến y) hay không?")
    if p_yes > p_no and p_yes >= 0.0001:
        print("CÓ")
        return "YES"
    else:
        print("KHÔNG")
        return "NO"



#gui
root = Tk()
root.geometry("400x700")

def show():
    df = pd.read_csv('bank-full.csv')
    data = df.iloc[:, 1:].values
    
    df = pd.read_csv('bank-full.csv')
    data = df.iloc[:, 1:].values
    attribute_list = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome']
    X = {'age': text.get()
    ,'job': clicked2.get()
    ,'marital': clicked3.get()
    ,'education': clicked4.get()
    ,'default': clicked5.get()
    ,'balance':text1.get()
    ,'housing': clicked6.get()
    ,'loan':clicked7.get()
    ,'contact':clicked8.get()
    ,'day':text2.get()
    ,'month':clicked9.get()
    ,'duration':text3.get()
    ,'campaign':text4.get()
    ,'pdays':text5.get()
    ,'previous':text6.get()
    ,'poutcome':clicked10.get()
    }
    rows = [i for i in range(0, 35000)]
    columns = [i for i in range(0, 16)]
    myLabel = Label(root, text = NaiveBayes(data, rows, columns, X), font =("helvetica",16)).place(x = 175, y = 620)
    print(text.get()
    ,clicked2.get()
    ,clicked3.get()
    ,clicked4.get()
    ,clicked5.get()
    ,text1.get()
    ,clicked6.get()
    ,clicked7.get()
    ,clicked8.get()
    ,text2.get()
    ,clicked9.get()
    ,text3.get()
    ,text4.get()
    ,text5.get()
    ,text6.get()
    ,clicked10.get())
    
#age
text = Entry(root,width= 30)
label = Label(root, text ="age").place(x = 30, y = 30)
text.place(x = 100, y = 30)


#job
options2 =[
    'admin','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown'

]
clicked2 = StringVar()
clicked2.set("job")

drop2 = OptionMenu(root, clicked2, *options2).place(x = 100, y = 60)

label2 = Label(root, text ="job").place(x = 30, y =60)

#marital
options3 = ['divorced','married','single','unknown'

]
clicked3 = StringVar()
clicked3.set("marital")

drop3 = OptionMenu(root, clicked3, *options3).place(x =100, y =90)
label1 = Label(root, text ="marital").place(x = 30, y = 90)

#education
options4 =['basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown'
]
clicked4 = StringVar()
clicked4.set("education")

drop4 = OptionMenu(root, clicked4, *options4).place(x = 100, y =120)
label4 = Label(root, text ="education").place(x = 30, y=120)


#default
options5 = ['no','yes','unknown']
clicked5 = StringVar()
clicked5.set("default")

drop5 = OptionMenu(root, clicked5, *options5).place(x = 100, y = 150)
label5 = Label(root, text = "default").place(x = 30, y= 150)

#balance
text1 = Entry(root,width= 30)
label6 = Label(root, text ="balance").place(x = 30, y = 180)
text1.place(x = 100, y = 180)


#housing
options6 = ['no','yes','unknown']
clicked6 = StringVar()
clicked6.set("housing")

drop6 = OptionMenu(root, clicked6, *options6).place(x = 100, y= 210)
label7 = Label(root, text ="housing").place(x = 30, y = 210)

#loan
options7 = ['no','yes','unknown']
clicked7 = StringVar()
clicked7.set("loan")

drop7 = OptionMenu(root, clicked7, *options7).place(x = 100, y = 240)
label8 = Label(root, text ="loan").place(x = 30, y= 240)

#contact
options8 = [ 'cellular','telephone','unknown']
clicked8 = StringVar()
clicked8.set("contact")

drop8 = OptionMenu(root, clicked8, *options8).place(x = 100, y= 270)
label9 = Label(root, text ="contact").place(x = 30, y = 270)

#day
text2 = Entry(root,width= 30)
label10 = Label(root, text ="day").place(x = 30, y = 305)
text2.place(x = 100, y = 305)
#month
options9 = ['jan', 'feb', 'mar',"apr", 'may','jun','jul','aug','sep','oct','nov', 'dec']
clicked9 = StringVar()
clicked9.set("month")

drop9 = OptionMenu(root, clicked9, *options9).place(x = 100, y = 330)
label11 = Label(root, text = "month").place(x = 30, y = 330)
#duration
text3= Entry(root,width= 30)
label12 = Label(root, text ="duration").place(x = 30, y = 365)
text3.place(x = 100, y = 365)
# campaign
text4 = Entry(root,width= 30)
label13 = Label(root, text ="campaign").place(x = 30, y = 395)
text4.place(x = 100, y = 395)
# pdays
text5 = Entry(root,width= 30)
label14 = Label(root, text ="pdays").place(x = 30, y = 425)
text5.place(x = 100, y = 425)
# previous
text6 = Entry(root,width= 30)
label15= Label(root, text ="previous").place(x = 30, y = 455)
text6.place(x = 100, y = 455)
# poutcome
options10 =['success','unknown','failure','other']
clicked10 = StringVar()
clicked10.set("poutcome")

drop10 = OptionMenu(root, clicked10, *options10).place(x = 100, y = 485)
label15 = Label(root, text ="poutcome").place(x = 30, y = 485)

button = Button(root, text ="result", command = show).place(x = 170 , y = 560)

root.mainloop()






    
