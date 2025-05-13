from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu10 = None
ans = 0

def hard(window, ans9, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu10, ans
    ans += ans9
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Ενεργοποίηση αναδίπλωσης κειμένου
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''10. Ποια είναι η πρωτεύουσα του Καμερούν;''')
    elif instance == 2:
        question.setText('''10. Ποια χώρα έχει σημαία με μόνο δύο χρώματα: πράσινο και λευκό;''')
    elif instance == 3:
        question.setText('''10. Ποιες χώρες συνορεύουν με το Μαρόκο;''')

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
        import easy_marks
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu10)
        easy_marks.show_marks(window, ans, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    def answer_dania():
        global qu10, ans
        if instance == 1:
            qu10 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_kroatia():
        global qu10, ans
        if instance == 1:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu10 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_norway():
        global qu10, ans
        if instance == 1:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu10 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_lichtenstain():
        global qu10, ans
        if instance == 1:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu10 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Γιαουντέ")  # Σωστό
            kroatia.setText("Β) Ντουάλα")
            norway.setText("Γ) Μπαγκί")
            poland.setText("Δ) Λιμπρεβίλ")
        if instance == 2:
            dania.setText("Α) Γκάνα")
            kroatia.setText("Β) Τυνησία")
            norway.setText("Γ) Νιγηρία")  # Σωστό
            poland.setText("Δ) Σουδάν")
        if instance == 3:
            dania.setText("Α) Αίγυπτος και Σουδάν")
            kroatia.setText("Β) Αλγερία και Δυτική Σαχάρα")  # Σωστό
            norway.setText("Γ) Νότια Αφρική")
            poland.setText("Δ) Λιβύη")

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