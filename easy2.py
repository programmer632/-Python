from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu2 = None
ans = 0

def easy(window, ans1, qu1):
    global qu2, ans
    ans += ans1
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''2. Σε ποια χώρα ανήκει η Κορσική;''')
    elif instance == 2:
        question.setText('''2. Ποια είναι η μεγαλύτερη χώρα σε έκταση
που βρίσκεται εξ ολοκλήρου στην Ευρώπη;''')
    elif instance == 3:
        question.setText('''2. Σε ποιο κράτος ανήκουν τα νησιά Φερόε;''')

    # Υπολογισμός θέσης
    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20

    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import easy3
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu2)
        easy3.easy(window, ans, qu2, qu1)

    def answer_dania():
        global qu2, ans
        if instance == 1:
            qu2 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_kroatia():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_norway():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu2 = False
            next_question()

    def answer_lichtenstain():
        global qu2, ans
        if instance == 1:
            qu2 = False
            next_question()
        elif instance == 2:
            qu2 = False
            next_question()
        elif instance == 3:
            qu2 = True
            ans += 2
            next_question()

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Γαλλία")
            kroatia.setText("Β) Ισπανία")
            norway.setText("Γ) Ουκρανία")
            lichtenstain.setText("Δ) Πολωνία")
        elif instance == 2:
            dania.setText("Α) Γαλλία")
            kroatia.setText("Β) Ισπανία")
            norway.setText("Γ) Ουκρανία")
            lichtenstain.setText("Δ) Πολωνία")
        elif instance == 3:
            dania.setText("Α) Γαλλία")
            kroatia.setText("Β) Ισπανία")
            norway.setText("Γ) Ουκρανία")
            lichtenstain.setText("Δ) Πολωνία")

    dania = QPushButton("Α) Δανία", window)
    dania.resize(500, 120)
    dania.move(250, 140)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_dania)

    kroatia = QPushButton("Β) Κροατία", window)
    kroatia.setFont(font)
    kroatia.resize(500, 120)
    kroatia.move(250, 270)
    kroatia.show()
    kroatia.clicked.connect(answer_kroatia)

    norway = QPushButton("Γ) Νορβηγία", window)
    norway.resize(500, 120)
    norway.move(250, 400)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_norway)

    lichtenstain = QPushButton("Δ) Λιχτενστάιν", window)
    lichtenstain.resize(500, 120)
    lichtenstain.move(250, 530)
    lichtenstain.setFont(font)
    lichtenstain.show()
    lichtenstain.clicked.connect(answer_lichtenstain)

    setcorrecttext()