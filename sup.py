

from tkinter import *
import math
import os
import random
from tkinter import messagebox


class osman:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700+30+10')
        self.root.title('Super Market')
        self.root.resizable(False, False)
        self.root.iconbitmap('E:\\Projects\\logo.ico')
        title1 = Label(self.root, text='ادارة البرنامج : سوبر ماركت',
                       fg='white', bg='#f4cf65', font=("tajawal", 15, 'bold'))
        title1.pack(fill=X)
        # ===========================
        self.name = StringVar()
        self.number = StringVar()
        self.recept = StringVar()
        x = random.randrange(1, 100000)
        self.recept.set(x)
        # ==========================
        self.foodsum = StringVar()
        self.itemsum = StringVar()
        self.drinksum = StringVar()
        # ========customer data======
        f1 = Frame(root, width=340, height=177, bg='#5533CC')
        f1.place(x=0, y=35)
        buyerdetail = Label(f1, text='Buyer Details:', bg='#5533CC',
                            fg='#aa33cc', font=('tajawal', 16, 'bold'))
        buyerdetail.place(x=4, y=2)
        buyername = Label(f1, text='Buyer name', bg='#5533CC',
                          fg='#f4cf65', font=('tajawal', 12, 'bold'))
        buyername.place(x=6, y=35)
        buyernumber = Label(f1, text='Buyer Number', bg='#5533CC',
                            fg='#f4cf65', font=('tajawal', 12, 'bold'))
        buyernumber.place(x=6, y=70)
        buyerre = Label(f1, text='Receipt Number', bg='#5533CC',
                        fg='#f4cf65', font=('tajawal', 12, 'bold'))
        buyerre.place(x=6, y=105)
        entname = Entry(f1, justify='center', font=(
            'tajawal', 12, 'bold'), textvariable=self.name)
        entname.place(x=140, y=36)
        entnumb = Entry(f1, justify='center', font=(
            'tajawal', 12, 'bold'), textvariable=self.number)
        entnumb.place(x=140, y=71)
        entrecpt = Entry(f1, justify='center', font=(
            'tajawal', 12, 'bold'), textvariable=self.recept)
        entrecpt.place(x=140, y=106)

        btn_search = Button(f1, text='Search', width=6, height=1,
                            bg='white',  font=('tajawal', 10))
        btn_search.place(x=270, y=140)
        # ==========bills=========
        recept = Label(f1, text='[Receipts]', fg='#f4cf65',
                       bg='#5533CC', font=('tajawal', 14, 'bold'))
        recept.place(x=138, y=148)
        f2 = Frame(root, bd=2, width=340, height=350, bg='white')
        f2.place(x=0, y=213)
        scrollbill = Scrollbar(f2, orient=VERTICAL)

        self.textarea = Text(f2, yscrollcommand=scrollbill.set, width=40
                             )
        scrollbill.pack(side=RIGHT, fill=Y)
        scrollbill.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        # Frame for price =======
        f3 = Frame(root, bd=2, width=658, height=110, bg='#5533CC')
        f3.place(x=0, y=580)
        btnsum = Button(f3, text='SUM', font="tajawal",
                        bg="#aa33cc", fg='black', width=10, height=1, command=self.total)
        btnsum.place(x=2, y=5)
        btnprint = Button(f3, text='Print', font="tajawal",
                          bg="#aa33cc", fg='black', width=10, height=1)
        btnprint.place(x=2, y=45)
        btnreset = Button(f3, text='Reset', font="tajawal",
                          bg="#aa33cc", fg='black', width=10, height=1)
        btnreset.place(x=100, y=5)
        btnexit = Button(f3, text='Exit', font="tajawal",
                         bg="#aa33cc", fg='black', width=10, height=1, command=quit)
        btnexit.place(x=100, y=45)
        lblfoods = Label(f3, text='Sum of foods', font=(
            'tajawal', 10, 'bold'), bg='#5533CC', fg='gold')
        lblfoods.place(x=220, y=5)
        lbldrinks = Label(f3, text='Sum of Drinks', font=(
            'tajawal', 10, 'bold'), bg='#5533CC', fg='gold')
        lbldrinks.place(x=220, y=40)
        lblan = Label(f3, text='Sum of another', font=(
            'tajawal', 10, 'bold'), bg='#5533CC', fg='gold')
        lblan.place(x=220, y=75)
        entfood = Entry(f3, width=24, textvariable=self.foodsum)
        entfood.place(x=320, y=5)
        entdrinks = Entry(f3, width=24, textvariable=self.drinksum)
        entdrinks.place(x=320, y=40)
        entan = Entry(f3, width=24, textvariable=self.itemsum)
        entan.place(x=320, y=75)
        # food corner ========
        f4 = Frame(root, width=340, height=660, bg='#5533CC')
        f4.place(x=1000, y=35)
        food = Label(f4, text="FOODS", fg='#f4cf65',
                     bg='#5533cc', font=('tajawal', 24, 'bold'))
        food.place(x=100, y=3)
        food1 = Label(f4, text='cheese', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food1.place(x=3, y=55)
        food2 = Label(f4, text='chicken', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food2.place(x=3, y=85)
        food3 = Label(f4, text='meat', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food3.place(x=150, y=55)
        food4 = Label(f4, text='beef', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food4.place(x=150, y=85)
        food5 = Label(f4, text='cheese', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food5.place(x=3, y=115)
        food6 = Label(f4, text='chicken', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food6.place(x=3, y=145)
        food7 = Label(f4, text='meat', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food7.place(x=150, y=115)
        food8 = Label(f4, text='beef', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food8.place(x=150, y=145)
        food9 = Label(f4, text='cheese', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food9.place(x=3, y=175)
        food10 = Label(f4, text='chicken', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food10.place(x=3, y=205)
        food11 = Label(f4, text='meat', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food11.place(x=150, y=175)
        food12 = Label(f4, text='beef', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food12.place(x=150, y=205)
        food13 = Label(f4, text='cheese', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food13.place(x=3, y=235)
        food13 = Label(f4, text='chicken', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food13.place(x=3, y=265)
        food14 = Label(f4, text='meat', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food14.place(x=150, y=235)
        food15 = Label(f4, text='beef', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food15.place(x=150, y=265)
        food16 = Label(f4, text='cheese', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food16.place(x=3, y=295)
        food17 = Label(f4, text='chicken', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food17.place(x=3, y=325)
        food18 = Label(f4, text='meat', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food18.place(x=150, y=295)
        food19 = Label(f4, text='beef', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food19.place(x=150, y=325)
        food20 = Label(f4, text='cheese', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food20.place(x=3, y=355)
        food21 = Label(f4, text='chicken', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food21.place(x=3, y=385)
        food22 = Label(f4, text='meat', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food22.place(x=150, y=355)
        food22 = Label(f4, text='meat', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        food22.place(x=150, y=385)
        # ===========================
        self.fod1 = IntVar()
        self.fod2 = IntVar()
        self.fod3 = IntVar()
        self.fod4 = IntVar()
        self.fod5 = IntVar()
        self.fod6 = IntVar()
        self.fod7 = IntVar()
        self.fod8 = IntVar()
        self.fod9 = IntVar()
        self.fod10 = IntVar()
        self.fod11 = IntVar()
        self.fod12 = IntVar()
        self.fod13 = IntVar()
        self.fod14 = IntVar()
        self.fod15 = IntVar()
        self.fod16 = IntVar()
        self.fod17 = IntVar()
        self.fod18 = IntVar()
        self.fod19 = IntVar()
        self.fod20 = IntVar()
        self.fod21 = IntVar()
        self.fod22 = IntVar()
        self.fod23 = IntVar()
        self.fod24 = IntVar()
        # ==========================

        entfd1 = Entry(f4, width=7, textvariable=self.fod1)
        entfd1.place(x=80, y=65)
        entfd2 = Entry(f4, width=7, textvariable=self.fod2)
        entfd2.place(x=80, y=95)
        entfd3 = Entry(f4, width=7, textvariable=self.fod3)
        entfd3.place(x=210, y=65)
        entfd4 = Entry(f4, width=7, textvariable=self.fod4)
        entfd4.place(x=210, y=95)
        entfd5 = Entry(f4, width=7, textvariable=self.fod5)
        entfd5.place(x=80, y=125)
        entfd6 = Entry(f4, width=7, textvariable=self.fod6)
        entfd6.place(x=80, y=155)
        entfd7 = Entry(f4, width=7, textvariable=self.fod7)
        entfd7.place(x=210, y=125)
        entfd8 = Entry(f4, width=7, textvariable=self.fod8)
        entfd8.place(x=210, y=155)
        entfd9 = Entry(f4, width=7, textvariable=self.fod9)
        entfd9.place(x=80, y=185)
        entfd10 = Entry(f4, width=7, textvariable=self.fod10)
        entfd10.place(x=80, y=215)
        entfd11 = Entry(f4, width=7, textvariable=self.fod11)
        entfd11.place(x=210, y=185)
        entfd12 = Entry(f4, width=7, textvariable=self.fod12)
        entfd12.place(x=210, y=215)
        entfd13 = Entry(f4, width=7, textvariable=self.fod13)
        entfd13.place(x=80, y=245)
        entfd14 = Entry(f4, width=7, textvariable=self.fod14)
        entfd14.place(x=80, y=275)
        entfd15 = Entry(f4, width=7, textvariable=self.fod15)
        entfd15.place(x=210, y=245)
        entfd16 = Entry(f4, width=7, textvariable=self.fod16)
        entfd16.place(x=210, y=275)
        entfd17 = Entry(f4, width=7, textvariable=self.fod17)
        entfd17.place(x=80, y=305)
        entfd18 = Entry(f4, width=7, textvariable=self.fod18)
        entfd18.place(x=80, y=335)
        entfd19 = Entry(f4, width=7, textvariable=self.fod19)
        entfd19.place(x=210, y=305)
        entfd20 = Entry(f4, width=7, textvariable=self.fod20)
        entfd20.place(x=210, y=335)
        entfd21 = Entry(f4, width=7, textvariable=self.fod21)
        entfd21.place(x=80, y=365)
        entfd22 = Entry(f4, width=7, textvariable=self.fod22)
        entfd22.place(x=80, y=395)

        entfd23 = Entry(f4, width=7, textvariable=self.fod23)
        entfd23.place(x=210, y=365)
        entfd24 = Entry(f4, width=7, textvariable=self.fod24)
        entfd24.place(x=210, y=395)

        # items=====================
        f5 = Frame(root, width=338, height=660, bg='#5533CC')
        f5.place(x=660, y=35)
        items = Label(f5, text="ITEMS", fg='#f4cf65',
                      bg='#5533cc', font=('tajawal', 24, 'bold'))
        items.place(x=100, y=3)
        item1 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item1.place(x=3, y=55)
        item2 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item2.place(x=3, y=85)
        item3 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item3.place(x=150, y=55)
        item4 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item4.place(x=150, y=85)
        item5 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item5.place(x=3, y=115)
        item6 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item6.place(x=3, y=145)
        item7 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item7.place(x=150, y=115)
        item8 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item8.place(x=150, y=145)
        item9 = Label(f5, text='item', fg='#f4cf65',
                      bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item9.place(x=3, y=175)
        item10 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item10.place(x=3, y=205)
        item11 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item11.place(x=150, y=175)
        item12 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item12.place(x=150, y=205)
        item13 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item13.place(x=3, y=235)
        item14 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item14.place(x=3, y=265)
        item15 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item15.place(x=150, y=235)
        item16 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item16.place(x=150, y=265)
        item17 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item17.place(x=3, y=295)
        item18 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item18.place(x=3, y=325)
        item19 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item19.place(x=150, y=295)
        item20 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item20.place(x=3, y=325)
        item21 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item21.place(x=3, y=355)
        item22 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item22.place(x=150, y=325)
        item23 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item23.place(x=150, y=355)
        item24 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item24.place(x=3, y=385)
        item25 = Label(f5, text='item', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        item25.place(x=150, y=385)
        # =============================
        self.it1 = IntVar()
        self.it2 = IntVar()
        self.it3 = IntVar()
        self.it4 = IntVar()
        self.it5 = IntVar()
        self.it6 = IntVar()
        self.it7 = IntVar()
        self.it8 = IntVar()
        self.it9 = IntVar()
        self.it10 = IntVar()
        self.it11 = IntVar()
        self.it12 = IntVar()
        self.it13 = IntVar()
        self.it14 = IntVar()
        self.it15 = IntVar()
        self.it16 = IntVar()
        self.it17 = IntVar()
        self.it18 = IntVar()
        self.it19 = IntVar()
        self.it20 = IntVar()
        self.it21 = IntVar()
        self.it22 = IntVar()
        self.it23 = IntVar()
        self.it24 = IntVar()

        entit1 = Entry(f5, width=7, textvariable=self.it1)
        entit1.place(x=80, y=65)
        entit2 = Entry(f5, width=7, textvariable=self.it2)
        entit2.place(x=80, y=95)
        entit3 = Entry(f5, width=7, textvariable=self.it3)
        entit3.place(x=210, y=65)
        entit4 = Entry(f5, width=7, textvariable=self.it4)
        entit4.place(x=210, y=95)
        entit5 = Entry(f5, width=7, textvariable=self.it5)
        entit5.place(x=80, y=125)
        entit6 = Entry(f5, width=7, textvariable=self.it6)
        entit6.place(x=80, y=155)
        entit7 = Entry(f5, width=7, textvariable=self.it7)
        entit7.place(x=210, y=125)
        entit8 = Entry(f5, width=7, textvariable=self.it8)
        entit8.place(x=210, y=155)
        entit9 = Entry(f5, width=7, textvariable=self.it9)
        entit9.place(x=80, y=185)
        entit10 = Entry(f5, width=7, textvariable=self.it10)
        entit10.place(x=80, y=215)
        entit11 = Entry(f5, width=7, textvariable=self.it11)
        entit11.place(x=210, y=185)
        entit12 = Entry(f5, width=7, textvariable=self.it12)
        entit12.place(x=210, y=215)
        entit13 = Entry(f5, width=7, textvariable=self.it13)
        entit13.place(x=80, y=245)
        entit14 = Entry(f5, width=7, textvariable=self.it14)
        entit14.place(x=80, y=275)
        entit15 = Entry(f5, width=7, textvariable=self.it5)
        entit15.place(x=210, y=245)
        entit16 = Entry(f5, width=7, textvariable=self.it16)
        entit16.place(x=210, y=275)
        entit17 = Entry(f5, width=7, textvariable=self.it17)
        entit17.place(x=80, y=305)
        entit18 = Entry(f5, width=7, textvariable=self.it18)
        entit18.place(x=80, y=335)
        entit19 = Entry(f5, width=7, textvariable=self.it19)
        entit19.place(x=210, y=305)
        entit20 = Entry(f5, width=7, textvariable=self.it20)
        entit20.place(x=210, y=335)
        entit21 = Entry(f5, width=7, textvariable=self.it21)
        entit21.place(x=80, y=365)
        entit22 = Entry(f5, width=7, textvariable=self.it22)
        entit22.place(x=80, y=395)

        entit23 = Entry(f5, width=7, textvariable=self.it23)
        entit23.place(x=210, y=365)
        entit24 = Entry(f5, width=7, textvariable=self.it24)
        entit24.place(x=210, y=395)

        # drinkes=====================
        f6 = Frame(root, width=318, height=543, bg='#5533CC')
        f6.place(x=340, y=35)
        drinkes = Label(f6, text="DRINKES", fg='#f4cf65',
                        bg='#5533cc', font=('tajawal', 24, 'bold'))
        drinkes.place(x=100, y=3)
        drink1 = Label(f6, text='drink', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        drink1.place(x=3, y=55)
        drink2 = Label(f6, text='drink', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        drink2.place(x=3, y=85)
        drink3 = Label(f6, text='drink', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        drink3.place(x=150, y=55)
        drink4 = Label(f6, text='drink', fg='#f4cf65',
                       bg='#5533cc', font=('Tajawal', 15, 'bold'))
        drink4.place(x=150, y=85)
        # =========================
        self.dr1 = IntVar()
        self.dr2 = IntVar()
        self.dr3 = IntVar()
        self.dr4 = IntVar()

        entdr1 = Entry(f6, width=7, textvariable=self.dr1)
        entdr1.place(x=75, y=65)
        entdr2 = Entry(f6, width=7, textvariable=self.dr2)
        entdr2.place(x=75, y=95)
        entdr3 = Entry(f6, width=7, textvariable=self.dr3)
        entdr3.place(x=210, y=65)
        entdr4 = Entry(f6, width=7, textvariable=self.dr4)
        entdr4.place(x=210, y=95)
        self.welcome()

    def total(self):
        self.valfod1 = self.fod1.get()*90
        self.valfod2 = self.fod2.get()*80
        self.valfod3 = self.fod3.get()*70
        self.valfod4 = self.fod4.get()*50
        self.valfod5 = self.fod5.get()*40
        self.valfod6 = self.fod6.get()*30
        self.valfod7 = self.fod7.get()*100
        self.valfod8 = self.fod8.get()*90
        self.valfod9 = self.fod9.get()*92
        self.valfod10 = self.fod10.get()*10
        self.valfod11 = self.fod11.get()*90
        self.valfod12 = self.fod12.get()*70
        self.valfod13 = self.fod13.get()*55
        self.valfod14 = self.fod14.get()*66
        self.valfod15 = self.fod15.get()*35
        self.valfod16 = self.fod16.get()*56
        self.valfod17 = self.fod17.get()*77
        self.valfod18 = self.fod18.get()*20
        self.valfod19 = self.fod19.get()*20
        self.valfod20 = self.fod20.get()*20
        self.valfod21 = self.fod21.get()*20
        self.valfod22 = self.fod22.get()*20
        self.valfod23 = self.fod23.get()*20
        self.valfod24 = self.fod24.get()*20
        self.totalval = float(
            self.valfod1 +
            self.valfod2 +
            self.valfod3 +
            self.valfod4 +
            self.valfod5 +
            self.valfod6 +
            self.valfod7 +
            self.valfod8 +
            self.valfod9 +
            self.valfod10 +
            self.valfod11 +
            self.valfod12 +
            self.valfod13 +
            self.valfod14 +
            self.valfod15 +
            self.valfod16 +
            self.valfod17 +
            self.valfod18 +
            self.valfod19 +
            self.valfod20 +
            self.valfod21 +
            self.valfod22 +
            self.valfod23 +
            self.valfod24
        )
        self.foodsum.set(str(self.totalval)+'L.E')

        self.valit1 = self.it1.get()*90
        self.valit2 = self.it2.get()*80
        self.valit3 = self.it3.get()*70
        self.valit4 = self.it4.get()*50
        self.valit5 = self.it5.get()*40
        self.valit6 = self.it6.get()*30
        self.valit7 = self.it7.get()*100
        self.valit8 = self.it8.get()*90
        self.valit9 = self.it9.get()*92
        self.valit10 = self.it10.get()*10
        self.valit11 = self.it11.get()*90
        self.valit12 = self.it12.get()*70
        self.valit13 = self.it13.get()*55
        self.valit14 = self.it14.get()*66
        self.valit15 = self.it15.get()*35
        self.valit16 = self.it16.get()*56
        self.valit17 = self.it17.get()*77
        self.valit18 = self.it18.get()*20
        self.valit19 = self.it19.get()*20
        self.valit20 = self.it20.get()*20
        self.valit21 = self.it21.get()*20
        self.valit22 = self.it22.get()*20
        self.valit23 = self.it23.get()*20
        self.valit24 = self.it24.get()*20
        self.valit24 = self.it24.get()*20

        self.totalvalit = float(
            self.valit1 +
            self.valit2 +
            self.valit3 +
            self.valit4 +
            self.valit5 +
            self.valit6 +
            self.valit7 +
            self.valit8 +
            self.valit9 +
            self.valit10 +
            self.valit11 +
            self.valit12 +
            self.valit13 +
            self.valit14 +
            self.valit15 +
            self.valit16 +
            self.valit17 +
            self.valit18 +
            self.valit19 +
            self.valit20 +
            self.valit21 +
            self.valit22 +
            self.valit23 +
            self.valit24
        )
        self.itemsum.set(str(self.totalvalit)+'L.E')

        self.valdr1 = self.dr1.get()*35
        self.valdr2 = self.dr2.get()*25
        self.valdr3 = self.dr3.get()*45
        self.valdr4 = self.dr4.get()*75
        self.totaldr = float(
            self.valdr1 +
            self.valdr2 +
            self.valdr3 +
            self.valdr4
        )
        self.drinksum.set(str(self.totaldr)+'L.E')
        self.all = float(
            self.totalval +
            self.totaldr +
            self.totalvalit
        )

    def welcome(self):
        self.textarea.delete('1.5', END)
        self.textarea.insert(END, '\t Welcome To Our Market')
        self.textarea.insert(
            END, '\n========================================')
        self.textarea.insert(END, '\n\t    Have A Nice Day')
        self.textarea.insert(
            END, '\n========================================')
        self.textarea.insert(END, f'\nYour Name :{self.name.get()}')
        self.textarea.insert(END, f'\nPhone :{self.number.get()}')
        self.textarea.insert(END, f'\nReceiptNum:{self.recept.get()}')
        self.textarea.insert(
            END, '\n========================================')
        self.textarea.insert(END, f'\n  Items   \t quantity  \t price ')
        self.textarea.insert(
            END, '\n========================================')


root = Tk()
openroot = osman(root)  # for open root (our window)
root.mainloop()
