from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu7 = None
ans = 0

def hard(window, ans6, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu7, ans
    ans += ans6
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Ενεργοποίηση αναδίπλωσης κειμένου
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''7. Ποια είναι η πρωτεύουσα της Γκάνας;''')
    elif instance == 2:
        question.setText('''7. Ποια είναι η πρωτεύουσα του Σουδάν;''')
    elif instance == 3:
        question.setText('''7. Ποια είναι η πρωτεύουσα της Λιβύης;''')

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
        import hard8
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu7)
        hard8.hard(window, ans, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    def answer_dania():
        global qu7, ans
        if instance == 1:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu7 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_kroatia():
        global qu7, ans
        if instance == 1:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu7 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_norway():
        global qu7, ans
        if instance == 1:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_lichtenstain():
        global qu7, ans
        if instance == 1:
            qu7 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu7 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Ουαγκαντούγκου")
            kroatia.setText("Β) Λουάντα")
            norway.setText("Γ) Μπομπάσα")
            poland.setText("Δ) Άκκρα")
        if instance == 2:
            dania.setText("Α) Τζούμπα")
            kroatia.setText("Β) Χαρτούμ")
            norway.setText("Γ) Κιγκάλι")
            poland.setText("Δ) Νιαμέι")
        if instance == 3:
            dania.setText("Α) Τρίπολη")
            kroatia.setText("Β) Αλγέρι")
            norway.setText("Γ) Λουσάκα")
            poland.setText("Δ) Μαπούτο")

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