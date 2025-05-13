from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu3 = None
ans = 0

def hard(window, ans2, qu2, qu1):
    global qu3, ans
    ans += ans2
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Ενεργοποίηση αναδίπλωσης κειμένου
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText("3. Ποια είναι η μεγαλύτερη λίμνη της Αφρικής;")
    elif instance == 2:
        question.setText("3. Σε ποια χώρα βρίσκονται οι καταρράκτες Βικτώρια;")
    elif instance == 3:
        question.setText("3. Ποιο από τα παρακάτω νησιά ανήκει στην Αφρική;")

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
        import hard4
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu3)
        hard4.hard(window, ans, qu3, qu2, qu1)

    def answer_dania():
        global qu3, ans
        if instance == 1:
            qu3 = True
            ans += 2
        elif instance == 2:
            qu3 = False
        elif instance == 3:
            qu3 = False
        next_question()

    def answer_kroatia():
        global qu3, ans
        if instance == 1:
            qu3 = False
        elif instance == 2:
            qu3 = True
            ans += 2
        elif instance == 3:
            qu3 = False
        next_question()

    def answer_norway():
        global qu3, ans
        if instance == 1:
            qu3 = False
        elif instance == 2:
            qu3 = False
        elif instance == 3:
            qu3 = False
        next_question()

    def answer_lichtenstain():
        global qu3, ans
        if instance == 1:
            qu3 = False
        elif instance == 2:
            qu3 = False
        elif instance == 3:
            qu3 = True
            ans += 2
        next_question()

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Λίμνη Βικτώρια")
            kroatia.setText("Β) Λίμνη Τανγκανίκα")
            norway.setText("Γ) Λίμνη Νιασά")
            poland.setText("Δ) Λίμνη Μαλάουι")
        elif instance == 2:
            dania.setText("Α) Ζιμπάμπουε")
            kroatia.setText("Β) Ζάμπια")
            norway.setText("Γ) Μοζαμβίκη")
            poland.setText("Δ) Α και Β")
        elif instance == 3:
            dania.setText("Α) Νήσος των Χριστουγέννων")
            kroatia.setText("Β) Μαλδίβες")
            norway.setText("Γ) Κύπρος")
            poland.setText("Δ) Μαδαγασκάρη")

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

    poland = QPushButton("Δ) Λιχτενστάιν", window)
    poland.resize(500, 120)
    poland.move(250, 530)
    poland.setFont(font)
    poland.show()
    poland.clicked.connect(answer_lichtenstain)

    setcorrecttext()