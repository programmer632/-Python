from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

def easy(window):  
    global font, ans, qu1
    font = QFont("Calibri", 13)
    ans = 0
    qu1 = None
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)  # Κεντράρισμα κειμένου

    if instance == 1:
        question.setText('''1. Ποια από τις παρακάτω χώρες
βρίσκεται στη Σκανδιναβική χερσόνησο;''')
    elif instance == 2:
        question.setText('''1. Ποια από τις χώρες που αναφέρονται
δεν έχει έξοδο στη θάλασσα;''')
    elif instance == 3:
        question.setText('''1. Ποια από τις παρακάτω χώρες έχει
πρωτεύουσα πόλη την Κοπεγχάγη;''')

    # Υπολογισμός για να είναι στο κέντρο του Χ αλλά πάνω στο Υ
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100  # Μικρότερο ύψος για να μην είναι πολύ μεγάλη η ετικέτα
    question_x = (window_width - question_width) // 2  # Στο κέντρο οριζόντια
    question_y = 20  # Πάνω, αφήνοντας ένα μικρό κενό

    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import easy2
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu1)
        try:
            easy2.easy(window, ans, qu1)
        except Exception as e:
            print(f"Σφάλμα: {e}")

    def answer_dania():
        global qu1, ans
        if instance == 1:
            qu1 = False
            next_question()
        elif instance == 2:
            qu1 = False
            next_question()
        elif instance == 3:
            qu1 = True
            ans += 2
            next_question()

    def answer_latvia():
        global qu1, ans
        if instance == 1:
            qu1 = False
            next_question()
        elif instance == 2:
            qu1 = False
            next_question()
        elif instance == 3:
            qu1 = False
            next_question()

    def answer_norway():
        global qu1, ans
        if instance == 1:
            qu1 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu1 = False
            next_question()
        elif instance == 3:
            qu1 = False
            next_question()

    def answer_lichtenstain():
        global qu1, ans
        if instance == 1:
            qu1 = False
            next_question()
        elif instance == 2:
            qu1 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu1 = False
            next_question()

    dania = QPushButton("Α) Δανία", window)
    dania.resize(500, 120)
    dania.move(250, 130)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_dania)

    andora = QPushButton("Β) Λιθουανία", window)
    andora.setFont(font)
    andora.resize(500, 120)
    andora.move(250, 260)
    andora.show()
    andora.clicked.connect(answer_latvia)

    norway = QPushButton("Γ) Νορβηγία", window)
    norway.resize(500, 120)
    norway.move(250, 390)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_norway)

    lichtenstain = QPushButton("Δ) Λιχτενστάιν", window)
    lichtenstain.resize(500, 120)
    lichtenstain.move(250, 520)
    lichtenstain.setFont(font)
    lichtenstain.show()
    lichtenstain.clicked.connect(answer_lichtenstain)
