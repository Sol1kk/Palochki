from  tkinter import *
from random import *
from tkinter import messagebox
hard=20 # количество палочек у трудного бота
easy=20 # количество палочек у легко бота
pl,pm=0,0

def bot1():  #Легкий бот
    def s1():  #Первая кнопка
        global easy,pm
        if pm==0:
            u = 1
            easy = easy - int(u)  #Проверка количества палочек
            if easy <= 0:
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole1)
                if answer:
                    IgrovoePole1.destroy()
                    easy = 20
            else:
                sticks.config(text=easy * "| ")  #Удаление выбранных палочек
            pm+=1
    def s2():  #Вторая кнопка
        global easy,pm
        if pm==0:
            u = 2
            easy = easy - int(u)
            if easy <= 0:  #Проверка количества палочек
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole1)
                if answer:
                    IgrovoePole1.destroy()
                    easy = 20
            else:
                sticks.config(text=easy * "| ")  #Показывает количество палочек
            pm+=1
    def s3():  #Третья кнопка
        global easy,pm
        if pm==0:
            u = 3
            easy = easy - int(u)
            if easy <= 0:  #Проверка количества палочек
                sticks.config(text="Компьютер победил")  #Выводит текст, что компьютер выиграл
                sticks.place(x=475, y=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole1)
                if answer:
                    IgrovoePole1.destroy()
                    easy = 20
            else:
                sticks.config(text=easy * "| ")  #Показывает количество палочек
            pm+=1
    def pc():
        global easy,pm
        if pm==1:
            b = randint(1, 3)
            if easy == 4:  #Если осталось 4 палочки
                b = 3  #Компьютер убирает 3
            elif easy == 3:  #Если осталось 3 палочки
                b = 2  #Компьютер убирает 2
            elif easy == 2:  #Если осталось 2 палочки
                b = 1  #Компьютер убирает 1
            easy = easy - b
            if easy <= 0:
                sticks.config(text="Игрок победил")  #Выводит текст, что игрок выиграл
                sticks.place(x=140, y=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole1)
                if answer:
                    IgrovoePole1.destroy()
                    easy = 20
            else:
                sticks.config(text=easy * "| ")
            pm-=1
    IgrovoePole1 = Tk()
    IgrovoePole1.geometry("1116x631")  #Настройка окна
    IgrovoePole1.resizable(width=False, height=False)
    IgrovoePole1.configure(bg='#2E4553')
    text1 = Label(IgrovoePole1, text="Палочки",bg='#2E4553',fg='Black')  #Настройка текста палочки на поле
    text1.config(font=("Times New Roman", 35, 'bold'))
    text1.pack()
    knopka1 = Button(IgrovoePole1, text="1", command=s1,bg='Grey', fg='Black')  #Настройка кнопки "1" на игровом поле, которая отвечает, сколько палочек возьмёт игрок
    knopka1.config(font=("Times New Roman", 17, 'bold'))
    knopka1.place(x=300, y=230)
    knopka2 = Button(IgrovoePole1, text="2", command=s2,bg='Grey', fg='Black')  #Настройка кнопки "2" на игровом поле, которая отвечает, сколько палочек возьмёт игрок
    knopka2.config(font=("Times New Roman", 17, 'bold'))
    knopka2.place(x=550, y=230)
    knopka3 = Button(IgrovoePole1, text="3", command=s3,bg='Grey', fg='Black')  #Настройка кнопки "3" на игровом поле, которая отвечает, сколько палочек возьмёт игрок
    knopka3.config(font=("Times New Roman", 17, 'bold'))
    knopka3.place(x=800, y=230)
    sticks = Label(IgrovoePole1, text=easy * "| ",)
    sticks.config(font=("Times New Roman", 50, 'bold'), fg='Black',bg="#2E4553")  #Настройка палочек на поле
    sticks.place(x=255, y=370)
    PcKnopka = Button(IgrovoePole1, text="Ход компьютера", command=pc,bg='Grey', fg='Black')  #Кнопка отвечающиеся за ход компьютера
    PcKnopka.config(font=("Times New Roman", 17, 'bold'))
    PcKnopka.place(x=464, y=550)
    IgrovoePole1.title("Палочки")
    IgrovoePole1.mainloop()  #Режим с легким ботом

def bot2():  #Трудный бот
    ai_map = [False for _ in range(hard)]
    def p1():   #Первая кнопка
        global hard, pl
        if pl == 0:
            u = 1
            hard = hard - int(u)
            if hard <= 0:
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole2)
                if answer:
                    IgrovoePole2.destroy()
                    hard = 20
            else:
                sticks.config(text=hard * "| ")
            pl+=1

    def p2():   #Вторая кнопка
        global hard, pl
        if pl == 0:
            u = 2
            hard = hard - int(u)
            if hard <= 0:
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, y=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole2)
                if answer:
                    IgrovoePole2.destroy()
                    hard = 20
            else:
                sticks.config(text=hard * "| ")
            pl += 1

    def p3():  #Третья кнопка
        global hard, pl
        if pl == 0:
            u = 3
            hard = hard - int(u)
            if hard <= 0:
                sticks.config(text="Компьютер победил")
                sticks.place(x=475, f=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole2)
                if answer:
                    IgrovoePole2.destroy()
                    hard = 20
            else:
                sticks.config(text=hard * "| ")
            pl += 1
    def ps():
        global hard,pl
        if pl==1:
            start_cell = 20 - hard - 1
            for cell_index in range(20):
                cell = 20 - cell_index - 1
                if 0 < cell_index % (1 + 3) <= 1:
                    ai_map[cell] = True
            for x in range(start_cell, 20):
                if ai_map[x] and 1 <= x - start_cell <= 3:
                    a = x - start_cell
                elif x - start_cell > 3:
                    a = randint(1, 3)
                else:
                    a = randint(1, 3)
            hard = hard - int(a)
            if hard <= 0:
                sticks.config(text="Игрок победил")
                sticks.place(x=140, y=70)
                answer = messagebox.showinfo('Конец игры', 'Спасибо за игру',parent=IgrovoePole2)
                if answer:
                    IgrovoePole2.destroy()
                    hard = 20
            else:
                sticks.config(text=hard * "| ")
            pl-=1
    IgrovoePole2 = Tk()
    IgrovoePole2.geometry("1116x631") #Настройка окна
    IgrovoePole2.resizable(width=False, height=False)
    IgrovoePole2.configure(bg='#0A1C34')
    text1 = Label(IgrovoePole2, text="Палочки",bg='#0A1C34',fg='#dcd9cd')  #Настройка текста палочки на поле
    text1.config(font=("Times New Roman", 35, 'bold'))
    text1.pack()
    knopka1 = Button(IgrovoePole2, text="1", command=p1,bg='black',fg='#dcd9cd')  #Настройка кнопки "1" на игровом поле, которая отвечает, сколько палочек возьмёт игрок
    knopka1.config(font=("Times New Roman", 17, 'bold'))
    knopka1.place(x=300, y=230)
    knopka2 = Button(IgrovoePole2, text="2", command=p2, bg='black',fg='#dcd9cd')  #Настройка кнопки "2" на игровом поле, которая отвечает, сколько палочек возьмёт игрок
    knopka2.config(font=("Times New Roman", 17, 'bold'))
    knopka2.place(x=550, y=230)
    knopka3 = Button(IgrovoePole2, text="3", command=p3,bg='black',fg='#dcd9cd')  #Настройка кнопки "3" на игровом поле, которая отвечает, сколько палочек возьмёт игрок
    knopka3.config(font=("Times New Roman", 17, 'bold'))
    knopka3.place(x=800, y=230)
    sticks = Label(IgrovoePole2, text=hard * "| ")
    sticks.config(font=("Times New Roman", 50, 'bold'), fg='#dcd9cd',bg='#0A1C34')  #Настройка палочек на поле
    sticks.place(x=255, y=370)
    PcKnopka = Button(IgrovoePole2, text="Ход компьютера", command=ps,bg='black',fg='#dcd9cd')  #Кнопка отвечающиеся за ход компьютера
    PcKnopka.config(font=("Times New Roman", 17, 'bold'))
    PcKnopka.place(x=464, y=550)
    IgrovoePole2.resizable(0, 0)
    IgrovoePole2.title("Палочки")
    IgrovoePole2.mainloop()  #Режим с трудным ботом
def mainwindow():
    window = Tk()
    window.geometry("330x250")  # Настройка основного окна
    window.configure(bg='#2E4553')
    window.resizable(False, False)
    TexturaTitle = Label(window, text="Палочки", bg='#2E4553', fg='#dcd9cd')  # Название игры в главном меню
    TexturaTitle.config(font=("Times New Roman", 20, 'bold'))
    TexturaTitle.pack()
    PlayButt = Button(window, text=" Играть ", width=11, command=game, bg='Grey', fg='Black')  # Кнопка играть
    PlayButt.place(x=120, y=80)
    RulesButt = Button(window, text="Правила", width=11, command=pravila, bg='Grey',fg='black')  # Кнопка с правилами игры
    RulesButt.place(x=120, y=130)
    ExitButt = Button(window, text="Выход", width=11, command=Exit, bg='Grey', fg='black')  # Кнопка выхода с игры
    ExitButt.place(x=120, y=180)
def Exit():
    exit()
def pravila():
    pravila=Toplevel(window)
    pravila.geometry("330x250")  # Окно с правилами
    pravila.resizable(width=0, height=0)
    pravila.configure(bg='#2E4553')
    textura1 = Label(pravila, text="Правила", bg='#2E4553', fg='#dcd9cd')
    textura1.config(font=("Times New Roman", 20, 'bold'))
    textura1.pack()
    textura1 = Label(pravila, text="1. Суть очень проста: перед пользователем и компьютером лежит 20 палочек. \n 2. Ходят по очереди. Каждый в своей ход берет от 1 до 3 палочек. \n 3. Проигрывает тот, кто берет последнюю палочку.",bg='#2E4553',fg='#dcd9cd',wraplength=325,height=7 )
    textura1.pack()
    Back1Butt= Button(pravila, text="Вернуться в главное  меню",width=25,command=pravila.withdraw,bg='Grey', fg='Black')
    Back1Butt.place(x=75, y=155)
def game():
    Game=Tk()
    Game.geometry("330x250") #Настройка окна с выбором сложности
    Game.resizable(width=0, height=0)
    Game.configure(bg='#2E4553')
    textura1 = Label(Game, text="Выбор режима", bg='#2E4553', fg='#dcd9cd')
    textura1.config(font=("Times New Roman", 20, 'bold'))
    textura1.pack()
    PlayEasyButt= Button(Game, text="Играть с легким ботом ",width=25,command=bot1,bg='Grey', fg='Black')
    PlayEasyButt.place(x=75, y=80)
    PlayHardButt= Button(Game, text="Играть с трудным ботом",width=25,command=bot2,bg='Grey', fg='Black')
    PlayHardButt.place(x=75, y=130)
    Back2Butt=Button(Game, text="Вернуться в главное меню",width=25,command=Game.withdraw,bg='Grey', fg='Black')
    Back2Butt.place(x=75,y=180)
    Game.title("Палочки")
    Game.mainloop()  #Запсук окна при нажатии на кнопку "Играть"

window = Tk()
window.geometry("330x250")  #Настройка основного окна
window.configure(bg='#2E4553')
window.resizable(False, False)
TexturaTitle = Label(window, text="Палочки",bg='#2E4553', fg='#dcd9cd')  #Название игры в главном меню
TexturaTitle.config(font=("Times New Roman",20, 'bold'))
TexturaTitle.pack()
PlayButt = Button(window, text=" Играть ",width=11,command = game,bg='Grey', fg='Black')  #Кнопка играть
PlayButt.place(x=120, y=80)
RulesButt =Button(window, text="Правила",width=11,command = pravila,bg='Grey', fg='black')  #Кнопка с правилами игры
RulesButt.place(x=120, y=130)
ExitButt=Button(window, text="Выход",width=11,command = Exit, bg='Grey',fg='black')  #Кнопка выхода с игры
ExitButt.place(x=120, y=180)
window.title("Палочки")
window.mainloop()  #Запуск окна
