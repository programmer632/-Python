from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu9 = None
ans = 0

def easy(window, ans8, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu9, ans
    ans += ans8
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''9. Ποια είναι η πρωτεύουσα της Ουγγαρίας;''')
    elif instance == 2:
        question.setText('''9. Ποια από τις παρακάτω χώρες-πρωτεύουσες
είναι σωστός ο συνδυασμός;''')
    elif instance == 3:
        question.setText('''9. Ποιος είναι ο μεγαλύτερος ποταμός της Ευρώπης;''')

    window_width = window.frameGeometry().width()
    question_width = 600
    question_height = 100
    question_x = (window_width - question_width) // 2
    question_y = 20
    question.setGeometry(question_x, question_y, question_width, question_height)
    question.setStyleSheet("font-size: 20px; font-weight: bold;")
    question.show()

    def next_question():
        import easy10
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu9)
        easy10.easy(window, ans, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1)

    def answer_dania():
        global qu9, ans
        if instance == 1:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def answer_kroatia():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = True
            ans += 2
            next_question()

    def answer_norway():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = False
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def answer_lichtenstain():
        global qu9, ans
        if instance == 1:
            qu9 = False
            next_question()
        elif instance == 2:
            qu9 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu9 = False
            next_question()

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Βουδαπέστη")
            kroatia.setText("Β) Βελιγράδι")
            norway.setText("Γ) Βιέννη")
            poland.setText("Δ) Πράγα")
        if instance == 2:
            dania.setText("Α) Γεωργία-Γερεβάν")
            kroatia.setText("Β) Αρμενία-Τιφλίδα (Τμπιλίσι)")
            norway.setText("Γ) Αρμενία-Μπακού")
            poland.setText("Δ) Γεωργία-Τιφλίδα (Τμπιλίσι)")
        if instance == 3:
            dania.setText("Α) Δούναβης")
            kroatia.setText("Β) Βόλγας")
            norway.setText("Γ) Ρήνος")
            poland.setText("Δ) Σηκουάνας")

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