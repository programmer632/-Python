from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os
import sys
import random

qu4 = None
ans = 0

def hard(window, ans3, qu3, qu2, qu1):
    global qu4, ans
    ans += ans3
    font = QFont("Calibri", 13)
    instance = random.randint(1, 3)

    # Δημιουργία ερώτησης με κεντραρισμένο κείμενο
    question = QLabel("", window)
    question.setFont(font)
    question.setWordWrap(True)  # Ενεργοποίηση αναδίπλωσης κειμένου
    question.setAlignment(Qt.AlignCenter)

    if instance == 1:
        question.setText('''4. Ποια από τις παρακάτω πόλεις είναι μία από τις πρωτεύουσες της Νότιας Αφρικής;''')
    elif instance == 2:
        question.setText('''4. Ποιο είναι το μεγαλύτερο νησί της Αφρικής;''')
    elif instance == 3:
        question.setText('''4. Ποια από τις παρακάτω χώρες βρίσκεται στην περιοχή του Σαχέλ;''')

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
        import hard5
        for widget in window.children():
            widget.deleteLater()
        print(ans)
        print(qu4)
        hard5.hard(window, ans, qu4, qu3, qu2, qu1)

    def answer_dania():
        global qu4, ans
        if instance == 1:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu4 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_kroatia():
        global qu4, ans
        if instance == 1:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_norway():
        global qu4, ans
        if instance == 1:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu4 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def answer_lichtenstain():
        global qu4, ans
        if instance == 1:
            qu4 = True
            ans += 2
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 2:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")
        elif instance == 3:
            qu4 = False
            try:
                next_question()
            except Exception as e:
                print(f"Σφάλμα: {e}")

    def setcorrecttext():
        if instance == 1:
            dania.setText("Α) Πρετόρια")
            kroatia.setText("Β) Κέιπ Τάουν")
            norway.setText("Γ) Μπλουμφοντέιν")
            poland.setText("Δ) Όλες οι παραπάνω")
        if instance == 2:
            dania.setText("Α) Μαδαγασκάρη")
            kroatia.setText("Β) Σεϋχέλλες")
            norway.setText("Γ) Κομόρες")
            poland.setText("Δ) Μαυρίκιος")
        if instance == 3:
            dania.setText("Α) Γκάνα")
            kroatia.setText("Β) Μποτσουάνα")
            norway.setText("Γ) Μάλι")
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