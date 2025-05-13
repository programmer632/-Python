from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QLineEdit, QTableView
from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem, QPixmap, QImage, QColor
from PyQt5.QtCore import QTimer, Qt
import sys
import threading
import matplotlib.pyplot as plt
import os
import io
import json

# Ρυθμίσεις διαδρομών
if getattr(sys, 'frozen', False):
    # Όταν είναι .exe, η βάση είναι ο φάκελος που περιέχει το εκτελέσιμο
    base_path = os.path.dirname(sys.executable)
else:
    # Όταν τρέχει ως script, η βάση είναι ο τρέχων φάκελος
    base_path = os.path.abspath(".")

def resource_path(relative_path):
    # Χρησιμοποιείται για πόρους μόνο για ανάγνωση (π.χ. εικονίδια, ήχοι)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Διαδρομές αρχείων
imaje = resource_path("186-europis-70x100-1.ico")
send_answer = os.path.join(base_path, "skore.txt")  # Αποθηκεύεται δίπλα στο .exe
path = os.path.join(base_path, "data.json")        # Αποθηκεύεται δίπλα στο .exe

font = QFont("Calibri", 18)
correct_color = QColor(0, 128, 0)    # Πράσινο
wrong_color = QColor(255, 0, 0)      # Κόκκινο
info_color = QColor(0, 102, 204)     # Μπλε

# Global μεταβλητές
list_with_answers = None
true_list = [0]
correct_count = None
diagram_pixmap = None

def create_diagram():
    global list_with_answers, true_list
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list_with_answers:
        length = len(true_list)
        if i:
            if length == 1:
                true_list.append(1)
            elif length >= 2:
                true_list.append(true_list[length-1] + 1)
        else:
            if length == 1:
                true_list.append(-1)
            elif length >= 2:
                true_list.append(true_list[length-1] - 1)
                
    plt.plot(x, true_list, marker="o", linestyle="-", color="b", label='''Σωστό: +1\nΛάθος: -1''')
    plt.xlabel("Ερώτηση:")
    plt.ylabel("Σωστό / Λάθος")
    plt.title("Εξέλιξη απαντήσεων")
    plt.legend()
    
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png", dpi=150, bbox_inches="tight")
    img_buffer.seek(0)
    global diagram_pixmap
    image = QImage()
    image.loadFromData(img_buffer.getvalue())
    diagram_pixmap = QPixmap(image)
    img_buffer.close()
    plt.close()

def back(layout):
    widgets_to_remove = []
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget and (isinstance(widget, QLabel) and widget.pixmap() or isinstance(widget, QPushButton) and widget.text() == "Επιστροφή"):
            widgets_to_remove.append(widget)
    for widget in widgets_to_remove:
        layout.removeWidget(widget)
        widget.deleteLater()
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.show()

def show_diagrams(layout):
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.hide()
    label_statistic = QLabel()
    label_statistic.setPixmap(diagram_pixmap)
    layout.addWidget(label_statistic)
    but_return = QPushButton("Επιστροφή")
    but_return.setFont(font)
    but_return.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    but_return.clicked.connect(lambda: back(layout))
    layout.addWidget(but_return)

def false(y, layout):
    if (y-1) <= 9:
        label = QLabel(f"❌ Ερώτηση {y}: Λάθος")
        label.setFont(font)
        label.setStyleSheet(f"color: {wrong_color.name()}; padding: 5px; background-color: #ffe6e6;")
        layout.addWidget(label)
    if y == 10:
        button_statistic = QPushButton("Εξέλιξη των απαντήσεων")
        button_statistic.setFont(font)
        button_statistic.setStyleSheet("""
            QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
            QPushButton:hover { background-color: #008040; }
        """)
        thread = threading.Thread(target=create_diagram, daemon=True)
        thread.start()
        button_statistic.clicked.connect(lambda: show_diagrams(layout))
        layout.addWidget(button_statistic)

def true(y, layout):
    label = QLabel(f"✅ Ερώτηση {y}: Σωστή")
    label.setFont(font)
    label.setStyleSheet(f"color: {correct_color.name()}; padding: 5px; background-color: #e6ffe6;")
    layout.addWidget(label)
    if y == 10:
        button_statistic = QPushButton("Εξέλιξη των απαντήσεων")
        button_statistic.setFont(font)
        button_statistic.setStyleSheet("""
            QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
            QPushButton:hover { background-color: #008040; }
        """)
        thread = threading.Thread(target=create_diagram, daemon=True)
        thread.start()
        button_statistic.clicked.connect(lambda: show_diagrams(layout))
        layout.addWidget(button_statistic)

# Λειτουργίες για τον πίνακα βαθμολογιών
def show_leaderboard_window():
    leaderboard_window = QWidget()
    leaderboard_window.setWindowTitle("Πίνακας Βαθμολογιών")
    leaderboard_window.setStyleSheet("background-color: #f0f0f0;")
    if os.path.exists(imaje):
        leaderboard_window.setWindowIcon(QIcon(imaje))
    leaderboard_window.resize(450, 500)

    leaderboard_layout = QVBoxLayout()
    leaderboard_layout.setAlignment(Qt.AlignCenter)
    leaderboard_layout.setSpacing(10)
    leaderboard_window.setLayout(leaderboard_layout)

    text_field = QLineEdit()
    text_field.setFont(font)
    text_field.setPlaceholderText("Εισάγετε το όνομά σας")

    button_save = QPushButton("Αποθήκευση")
    button_save.setFont(font)
    button_save.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    button_save.clicked.connect(lambda: save_name(text_field, leaderboard_window))

    button_close = QPushButton("Κλείσιμο")
    button_close.setFont(font)
    button_close.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    button_close.clicked.connect(leaderboard_window.close)

    button_clear = QPushButton("Καθαρισμός")
    button_clear.setFont(font)
    button_clear.setStyleSheet("""
        QPushButton { background-color: #006633; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
        QPushButton:hover { background-color: #008040; }
    """)
    button_clear.clicked.connect(lambda: clear_leaderboard(leaderboard_window))

    leaderboard_layout.addWidget(text_field)
    leaderboard_layout.addWidget(button_save)
    leaderboard_layout.addWidget(button_close)
    leaderboard_layout.addWidget(button_clear)

    create_leaderboard_table(leaderboard_window, leaderboard_layout)
    leaderboard_window.show()

def save_name(text_field, leaderboard_window):
    name = text_field.text()
    if name.strip():
        save_all(name, leaderboard_window)
    else:
        print("Παρακαλώ εισάγετε ένα έγκυρο όνομα.")

def save_all(name, leaderboard_window):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as json_file:
                dictionary = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            dictionary = {}
    else:
        dictionary = {}
    dictionary[name] = correct_count * 2
    try:
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(dictionary, json_file, indent=4)
    except PermissionError:
        print("Σφάλμα: Δεν υπάρχουν δικαιώματα εγγραφής στον φάκελο.")
    create_leaderboard_table(leaderboard_window, leaderboard_window.layout())

def clear_leaderboard(leaderboard_window):
    dictionary = {}
    try:
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(dictionary, json_file, indent=4)
    except PermissionError:
        print("Σφάλμα: Δεν υπάρχουν δικαιώματα εγγραφής στον φάκελο.")
    create_leaderboard_table(leaderboard_window, leaderboard_window.layout())

def create_leaderboard_table(leaderboard_window, layout):
    for i in reversed(range(layout.count())):
        widget = layout.itemAt(i).widget()
        if isinstance(widget, QTableView):
            layout.removeWidget(widget)
            widget.deleteLater()
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            dictionary = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        dictionary = {}

    if not dictionary:
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Κατάταξη", "Όνομα", "Βαθμολογία"])
        table_view = QTableView()
        table_view.setModel(model)
        table_view.setStyleSheet("""
            QTableView { background-color: #ffffff; padding: 5px; font: 18pt Calibri; }
            QHeaderView::section { background-color: #e6f3ff; padding: 5px; }
        """)
        layout.insertWidget(0, table_view)
        return

    sorted_data = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Κατάταξη", "Όνομα", "Βαθμολογία"])

    for i, (name, score) in enumerate(sorted_data, start=1):
        rank_item = QStandardItem(str(i))
        name_item = QStandardItem(name)
        score_item = QStandardItem(str(score))
        rank_item.setEditable(False)
        name_item.setEditable(False)
        score_item.setEditable(False)
        model.setItem(i - 1, 0, rank_item)
        model.setItem(i - 1, 1, name_item)
        model.setItem(i - 1, 2, score_item)

    table_view = QTableView()
    table_view.setModel(model)
    table_view.setStyleSheet("""
        QTableView { background-color: #ffffff; padding: 5px; font: 18pt Calibri; }
        QHeaderView::section { background-color: #e6f3ff; padding: 5px; }
    """)
    layout.insertWidget(0, table_view)

def show_leaderboard():
    global correct_count, send_answer
    x = correct_count * 2
    try:
        with open(send_answer, 'w', encoding='utf-8') as file:
            file.write(str(x))
    except PermissionError:
        print("Σφάλμα: Δεν υπάρχουν δικαιώματα εγγραφής στον φάκελο.")
    show_leaderboard_window()

def show_marks(window, ans10, qu10, qu9, qu8, qu7, qu6, qu5, qu4, qu3, qu2, qu1):
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignCenter)
    layout.setSpacing(10)
    window.setStyleSheet("background-color: #f0f0f0;")
    window.setLayout(layout)

    start_label = QLabel("⏳ Έλεγχος των απαντήσεών σου...")
    start_label.setFont(font)
    start_label.setStyleSheet(f"color: {info_color.name()}; padding: 10px;")
    start_label.setAlignment(Qt.AlignCenter)
    layout.addWidget(start_label)

    def scan_answers():
        global list_with_answers
        list_with_answers = [qu1, qu2, qu3, qu4, qu5, qu6, qu7, qu8, qu9, qu10]
        for y, answer in enumerate(list_with_answers, start=1):
            if answer:
                timer.singleShot(y * 800, lambda y=y: true(y, layout))
            else:
                timer.singleShot(y * 800, lambda y=y: false(y, layout))
        timer.singleShot(len(list_with_answers) * 800 + 1000, lambda: start_label.hide())
        timer.singleShot(len(list_with_answers) * 800 + 1500, show_summary)

    def show_summary():
        global correct_count
        correct_count = sum(1 for ans in [qu1, qu2, qu3, qu4, qu5, qu6, qu7, qu8, qu9, qu10] if ans)
        summary_label = QLabel(f"🎉 Ολοκληρώθηκε! Σκορ: {correct_count*2}/20")
        summary_label.setFont(QFont("Calibri", 20, QFont.Bold))
        summary_label.setStyleSheet("color: #006633; padding: 15px; background-color: #e6f3ff;")
        summary_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(summary_label)

        button_leaderboard = QPushButton("Πίνακας Βαθμολογιών")
        button_leaderboard.setFont(font)
        button_leaderboard.setStyleSheet("""
            QPushButton { background-color: #004080; color: white; padding: 10px; border-radius: 5px; min-width: 200px; }
            QPushButton:hover { background-color: #0059b3; }
        """)
        button_leaderboard.clicked.connect(show_leaderboard)
        layout.addWidget(button_leaderboard)

    timer = QTimer()
    scan_answers()