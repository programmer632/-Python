from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu5 = None
ans = 0

def hard(window, ans4, qu4, qu3, qu2, qu1):
    global qu5, ans
    ans += ans4
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Ενεργοποίηση αναδίπλωσης κειμένου
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''5. Ποιο είναι το ψηλότερο βουνό της Αφρικής;''')
    elif instance == 2:
        question.setText('''5. Ποια είναι η πρωτεύουσα της Κένυας;''')
    elif instance == 3:
        question.setText('''5. Ποιο από τα παρακάτω κράτη συνορεύει με την Αίγυπτο;''')

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
        import hard6
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu5)
        hard6.hard(window, ans, qu5, qu4, qu3, qu2, qu1)

    def answer_dania():
        global qu5, ans
        if instance == 1:
            qu5 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu5 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_kroatia():
        global qu5, ans
        if instance == 1:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu5 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_norway():
        global qu5, ans
        if instance == 1:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_lichtenstain():
        global qu5, ans
        if instance == 1:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu5 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Κιλιμάντζαρο")
            kroatia.setText("Β) Άλμα")
            norway.setText("Γ) Μακκαρόν")
            poland.setText("Δ) Έβερεστ")
        if instance == 2:
            dania.setText("Α) Κιμπό")
            kroatia.setText("Β) Ναϊρόμπι")
            norway.setText("Γ) Λουσάκα")
            poland.setText("Δ) Ντουμπάι")
        if instance == 3:
            dania.setText("Α) Σουδάν")
            kroatia.setText("Β) Μαρόκο")
            norway.setText("Γ) Νιγηρία")
            poland.setText("Δ) Σομαλία")

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