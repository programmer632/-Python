from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu10 = None
ans = 0

def easy(window, ans9, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    global qu10, ans
    ans += ans9
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''10. Ποιο είναι το νόμισμα της Σουηδίας;''')
    elif instance == 2:
        question.setText('''10. Σε ποια χώρα βρίσκεται το όρος Μπεν Νέβις,
η κορυφή της οροσειράς Κάμπρια Όρη
(Cambrian Mountains);''')
    elif instance == 3:
        question.setText('''10. Ποια χώρα έχει τα περισσότερα νησιά στην Ευρώπη;''')

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
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_kroatia():
        global qu10, ans
        if instance == 1:
            qu10 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_norway():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu10 = False
            next_question()

    def answer_lichtenstain():
        global qu10, ans
        if instance == 1:
            qu10 = False
            next_question()
        elif instance == 2:
            qu10 = False
            next_question()
        elif instance == 3:
            qu10 = True
            ans += 2
            next_question()

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Ευρώ")
            kroatia.setText("Β) Κορόνα")
            norway.setText("Γ) Φράγκο")
            poland.setText("Δ) Λίρα")
        if instance == 2:
            dania.setText("Α) Ιρλανδία")
            kroatia.setText("Β) Αγγλία")
            norway.setText("Γ) Σκωτία")
            poland.setText("Δ) Ουαλία")
        if instance == 3:
            dania.setText("Α) Ιταλία")
            kroatia.setText("Β) Ελλάδα")
            norway.setText("Γ) Νορβηγία")
            poland.setText("Δ) Σουηδία")

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