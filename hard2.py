from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu2 = None
ans = 0

def hard(window, ans1, qu1):
    global qu2, ans
    ans += ans1
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Ενεργοποίηση αναδίπλωσης κειμένου
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''2. Ποια είναι η πρωτεύουσα του Μαρόκου;''')
    elif instance == 2:
        question.setText('''2. Ποια χώρα έχει τον μεγαλύτερο πληθυσμό στην Αφρική;''')
    elif instance == 3:
        question.setText('''2. Ποια είναι η δεύτερη χώρα σε πληθυσμό στην Αφρική μετά τη Νιγηρία;''')

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
        import hard3
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu2)
        hard3.hard(window, ans, qu2, qu1)

    def answer_france():
        global qu2, ans
        if instance == 1:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_spain():
        global qu2, ans
        if instance == 1:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu2 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu2 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_ukraine():
        global qu2, ans
        if instance == 1:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_poland():
        global qu2, ans
        if instance == 1:
            qu2 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu2 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Λούξορ")
            kroatia.setText("Β) Κάιρο")
            norway.setText("Γ) Αμπού Ντάμπι")
            poland.setText("Δ) Ραμπάτ")
        if instance == 2:
            dania.setText("Α) Αίγυπτος")
            kroatia.setText("Β) Νιγηρία")
            norway.setText("Γ) Αιθιοπία")
            poland.setText("Δ) Κονγκό")
        if instance == 3:
            dania.setText("Α) Αίγυπτος")
            kroatia.setText("Β) Αιθιοπία")
            norway.setText("Γ) Κονγκό")
            poland.setText("Δ) Νότια Αφρική")

    dania = QPushButton("Α) Γαλλία", window)
    dania.resize(500, 120)
    dania.move(250, 140)
    dania.setFont(font)
    dania.show()
    dania.clicked.connect(answer_france)

    kroatia = QPushButton("Β) Ισπανία", window)
    kroatia.setFont(font)
    kroatia.resize(500, 120)
    kroatia.move(250, 270)
    kroatia.show()
    kroatia.clicked.connect(answer_spain)

    norway = QPushButton("Γ) Ουκρανία", window)
    norway.resize(500, 120)
    norway.move(250, 400)
    norway.setFont(font)
    norway.show()
    norway.clicked.connect(answer_ukraine)

    poland = QPushButton("Δ) Πολωνία", window)
    poland.resize(500, 120)
    poland.move(250, 530)
    poland.setFont(font)
    poland.show()
    poland.clicked.connect(answer_poland)
    setcorrecttext()