from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu3 = None
ans = 0

def easy(window, ans2, qu2, qu1):
    global qu3, ans
    ans += ans2
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText("""3. Ποια ευρωπαϊκή χώρα περιβάλλεται
εξ ολοκλήρου από την Ιταλία;""")
    elif instance == 2:
        question.setText("3. Ποια χώρα έχει ως πρωτεύουσα τη Βουδαπέστη;")
    elif instance == 3:
        question.setText("3. Ποια χώρα διασχίζεται από τον ποταμό Δούναβη;")

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
        import easy4
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu3)
        easy4.easy(window, ans, qu3, qu2, qu1)

    def answer_dania():
        global qu3, ans
        if instance == 1:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_kroatia():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = True
            ans += 2
            next_question()
        elif instance == 3:
            qu3 = True
            ans += 2
            next_question()

    def answer_norway():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def answer_lichtenstain():
        global qu3, ans
        if instance == 1:
            qu3 = False
            next_question()
        elif instance == 2:
            qu3 = False
            next_question()
        elif instance == 3:
            qu3 = False
            next_question()

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Άγιος Μαρίνος")
            kroatia.setText("Β) Ιταλία")
            norway.setText("Γ) Βατικανό")
            lichtenstain.setText("Δ) Μονακό")
        elif instance == 2:
            dania.setText("Α) Σλοβακία")
            kroatia.setText("Β) Ουγγαρία")
            norway.setText("Γ) Ρουμανία")
            lichtenstain.setText("Δ) Σερβία")
        elif instance == 3:
            dania.setText("Α) Ισπανία")
            kroatia.setText("Β) Γερμανία")
            norway.setText("Γ) Γαλλία")
            lichtenstain.setText("Δ) Πορτογαλία")

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