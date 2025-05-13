from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu9 = None
ans = 0

def hard(window, ans8, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu9, ans
    ans += ans8
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Ενεργοποίηση αναδίπλωσης κειμένου
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''9. Ποια από τις παρακάτω χώρες δεν συνορεύει με το Κονγκό (Λ.Δ.);''')
    elif instance == 2:
        question.setText('''9. Ποια αφρικανική χώρα έχει τη μοναδική σημαία που δεν είναι ορθογώνια, αλλά έχει δύο τρίγωνα;''')
    elif instance == 3:
        question.setText('''9. Ποια είναι η πρωτεύουσα της Μποτσουάνας;''')

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
        import hard10
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu9)
        hard10.hard(window, ans, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    def answer_dania():
        global qu9, ans
        if instance == 1:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_kroatia():
        global qu9, ans
        if instance == 1:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_norway():
        global qu9, ans
        if instance == 1:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu9 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_lichtenstain():
        global qu9, ans
        if instance == 1:
            qu9 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu9 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu9 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Ανγκόλα")
            kroatia.setText("Β) Κεντροαφρικανική Δημοκρατία")
            norway.setText("Γ) Ζάμπια")
            poland.setText("Δ) Νιγηρία")  # Σωστό
        if instance == 2:
            dania.setText("Α) Νεπάλ")
            kroatia.setText("Β) Μποτσουάνα")
            norway.setText("Γ) Νότια Αφρική")
            poland.setText("Δ) Δεν υπάρχει τέτοια αφρικανική χώρα")  # Σωστό
        if instance == 3:
            dania.setText("Α) Φράνσισταουν")
            kroatia.setText("Β) Λίβινγκστον")
            norway.setText("Γ) Γκαμπορόνε")  # Σωστό
            poland.setText("Δ) Γουίντχουκ")

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