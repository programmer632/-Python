from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QCheckBox, QApplication, QFileDialog, QVBoxLayout,QComboBox
from PyQt5.QtGui import QFont, QIcon
import os
import sys
import threading
import random
import time
import subprocess
from PyQt5.QtCore import Qt

try:
    import vlc
except ImportError:
    print("Σφάλμα: Το vlc δεν βρέθηκε. Εγκαταστήστε το με 'pip install python-vlc'.")
    sys.exit(1)
try:
    import easy
    import normal
    import hard
except ImportError as e:
    print(f"Σφάλμα: Το module {e.name} δεν βρέθηκε.")
    sys.exit(1)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

credi = resource_path("product.txt")
setting = resource_path("settings.txt")
path1 = resource_path("musik.wav")
path2 = resource_path("Vibramusic.wav")
path3 = resource_path("Memories-of-Spring(chosic.com).wav")
path4 = resource_path("Cinspirational.wav")
path5 = resource_path("Σαρακινοί.wav")
imaje = resource_path("186-europis-70x100-1.ico")

music_quest = []

if not os.path.exists(setting):
    print(f"Το {setting} δεν βρέθηκε. Δημιουργείται με προεπιλογές.")
    with open(setting, 'w', encoding='utf-8') as settings_file:
        settings_file.write("1\n0\n0\n0\n0\n")
try:
    with open(setting, 'r', encoding='utf-8') as settings_file:
        lines = settings_file.readlines()
        print(lines)
        if len(lines) < 5:
            raise ValueError("Το settings.txt έχει λιγότερες από 5 γραμμές.")
        Standard_Music = lines[0].strip()
        Memories_of_Spring = lines[1].strip()
        Vibramusic = lines[2].strip()
        Cinspirational = lines[3].strip()
        Σαρακινοί = lines[4].strip()
        quest_setting = [Σαρακινοί, Cinspirational, Vibramusic, Memories_of_Spring, Standard_Music]
except Exception as e:
    print(f"Σφάλμα ανάγνωσης {setting}: {e}. Χρησιμοποιούνται προεπιλογές.")
    Standard_Music, Memories_of_Spring, Vibramusic, Cinspirational, Σαρακινοί = "1", "0", "0", "0", "0"
    quest_setting = [Σαρακινοί, Cinspirational, Vibramusic, Memories_of_Spring, Standard_Music]

for path, setting_val in zip([path1, path3, path2, path4, path5], quest_setting):
    if setting_val == "1" and os.path.exists(path):
        music_quest.append(path)
    elif setting_val == "1":
        print(f"Προειδοποίηση: Το {path} δεν βρέθηκε.")

if os.path.exists(credi):
    with open(credi, 'r', encoding='utf-8') as file:
        product = file.read()
else:
    product = "Δεν βρέθηκαν πληροφορίες κατασκευαστών."

font = QFont("Calibri", 15)
app = QApplication([])
window = QWidget()
window.setWindowTitle("Quiz γεωγραφίας")
player = vlc.MediaPlayer()

def sound():
    def random_choice():
        global music_quest
        if not music_quest:
            print("Δεν υπάρχουν διαθέσιμες μουσικές.")
            return
        x = random.choice(music_quest)
        media = vlc.Media(x)
        player.set_media(media)
        player.play()
        player.audio_set_volume(100)
    random_choice()
    while True:
        state = player.get_state()
        time.sleep(0.2)
        if state == vlc.State.Ended:
            random_choice()
        time.sleep(1)  # Μικρή καθυστέρηση για αποφυγή υπερφόρτωσης CPU

if "1" in quest_setting and music_quest:
    thread = threading.Thread(target=sound, daemon=True)
    thread.start()

def go_to_easy():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    easy.easy(window)

def go_to_normal():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    normal.normal(window)

def go_to_hard():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()
    hard.hard(window)

def start():
    for widget in window.children():
        widget.deleteLater()
    window.repaint()

    def settings():
        def demo_music():
            demo_player = vlc.MediaPlayer()

            def back_to_settings():
                demo_player.stop()
                time.sleep(0.1)
                player.play()
                demo_window.deleteLater()
                settings()

            def demo_Standard_Music():
                if os.path.exists(path1):
                    y = vlc.Media(path1)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Vibramusic():
                if os.path.exists(path2):
                    y = vlc.Media(path2)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Memories_of_Spring():
                if os.path.exists(path3):
                    y = vlc.Media(path3)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Cinspirational():
                if os.path.exists(path4):
                    y = vlc.Media(path4)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            def demo_Σαρακινοί():
                if os.path.exists(path5):
                    y = vlc.Media(path5)
                    demo_player.set_media(y)
                    if demo_player.get_state() == vlc.State.Playing:
                        demo_player.stop()
                    demo_player.play()

            demo_window = QWidget()
            demo_window.setWindowTitle("Quiz γεωγραφίας")
            demo_window.resize(500, 400)
            layout = QVBoxLayout()

            with open(setting, 'r', encoding='utf-8') as settings_file:
                lines = settings_file.readlines()
                Standard_Music = lines[0].strip()
                Memories_of_Spring = lines[1].strip()
                Vibramusic = lines[2].strip()
                Cinspirational = lines[3].strip()
                Σαρακινοί = lines[4].strip()

            if Standard_Music == "1" and os.path.exists(path1):
                but_Standard_Music = QPushButton("Standard Music", demo_window)
                but_Standard_Music.setFont(font)
                layout.addWidget(but_Standard_Music)
                but_Standard_Music.clicked.connect(demo_Standard_Music)
            if Memories_of_Spring == "1" and os.path.exists(path3):
                but_Memories_of_Spring = QPushButton("Memories of Spring", demo_window)
                but_Memories_of_Spring.setFont(font)
                layout.addWidget(but_Memories_of_Spring)
                but_Memories_of_Spring.clicked.connect(demo_Memories_of_Spring)
            if Vibramusic == "1" and os.path.exists(path2):
                but_Vibramusic = QPushButton("Vibramusic", demo_window)
                but_Vibramusic.setFont(font)
                layout.addWidget(but_Vibramusic)
                but_Vibramusic.clicked.connect(demo_Vibramusic)
            if Cinspirational == "1" and os.path.exists(path4):
                but_Cinspirational = QPushButton("Cinspirational", demo_window)
                but_Cinspirational.setFont(font)
                layout.addWidget(but_Cinspirational)
                but_Cinspirational.clicked.connect(demo_Cinspirational)
            if Σαρακινοί == "1" and os.path.exists(path5):
                but_Σαρακινοί = QPushButton("Σαρακινοί", demo_window)
                but_Σαρακινοί.setFont(font)
                layout.addWidget(but_Σαρακινοί)
                but_Σαρακινοί.clicked.connect(demo_Σαρακινοί)

            back = QPushButton("Επιστροφή", demo_window)
            back.setFont(font)
            layout.addWidget(back)
            back.clicked.connect(back_to_settings)

            demo_window.setLayout(layout)
            demo_window.show()

        def go_to_back():
            global music_quest
            with open(setting, 'w', encoding='utf-8') as settings_file:
                settings_file.write("1\n" if music1.isChecked() else "0\n")
                settings_file.write("1\n" if music2.isChecked() else "0\n")
                settings_file.write("1\n" if music3.isChecked() else "0\n")
                settings_file.write("1\n" if music4.isChecked() else "0\n")
                settings_file.write("1\n" if music5.isChecked() else "0\n")
            music_quest.clear()
            quest_setting = [
                "1" if music5.isChecked() else "0",
                "1" if music4.isChecked() else "0",
                "1" if music3.isChecked() else "0",
                "1" if music2.isChecked() else "0",
                "1" if music1.isChecked() else "0"
            ]
            for path, setting_val in zip([path1, path3, path2, path4, path5], quest_setting):
                if setting_val == "1" and os.path.exists(path):
                    music_quest.append(path)
            start()

        def reopen():
            player.stop()  # Σταμάτα τον VLC player
            with open(setting, 'w', encoding='utf-8') as settings_file:
                settings_file.write("1\n" if music1.isChecked() else "0\n")
                settings_file.write("1\n" if music2.isChecked() else "0\n")
                settings_file.write("1\n" if music3.isChecked() else "0\n")
                settings_file.write("1\n" if music4.isChecked() else "0\n")
                settings_file.write("1\n" if music5.isChecked() else "0\n")
            global music_quest
            music_quest.clear()
            quest_setting = [
                "1" if music5.isChecked() else "0",
                "1" if music4.isChecked() else "0",
                "1" if music3.isChecked() else "0",
                "1" if music2.isChecked() else "0",
                "1" if music1.isChecked() else "0"
            ]
            for path, setting_val in zip([path1, path3, path2, path4, path5], quest_setting):
                if setting_val == "1" and os.path.exists(path):
                    music_quest.append(path)
            if getattr(sys, 'frozen', False):
                executable = sys.executable
                if os.path.exists(executable):
                    subprocess.Popen([executable])
                else:
                    print(f"Σφάλμα: Δεν βρέθηκε το εκτελέσιμο {executable}")
            else:
                script_path = os.path.abspath(__file__)
                if os.path.exists(script_path):
                    subprocess.Popen(["python", script_path])
                else:
                    print(f"Σφάλμα: Δεν βρέθηκε το script {script_path}")
            sys.exit(0)

        def go_to_demo_music():
            player.pause()
            with open(setting, 'w', encoding='utf-8') as settings_file:
                settings_file.write("1\n" if music1.isChecked() else "0\n")
                settings_file.write("1\n" if music2.isChecked() else "0\n")
                settings_file.write("1\n" if music3.isChecked() else "0\n")
                settings_file.write("1\n" if music4.isChecked() else "0\n")
                settings_file.write("1\n" if music5.isChecked() else "0\n")
            global music_quest
            music_quest.clear()
            quest_setting = [
                "1" if music5.isChecked() else "0",
                "1" if music4.isChecked() else "0",
                "1" if music3.isChecked() else "0",
                "1" if music2.isChecked() else "0",
                "1" if music1.isChecked() else "0"
            ]
            for path, setting_val in zip([path1, path3, path2, path4, path5], quest_setting):
                if setting_val == "1" and os.path.exists(path):
                    music_quest.append(path)
            demo_music()

        def open_the_file():
            music_file, _ = QFileDialog.getOpenFileName(window, "Open Video", "", "Music Files (*.mp3 *.wav *.m4a *.opus)")
            if music_file:
                player.stop()
                media = vlc.Media(music_file)
                player.set_media(media)
                time.sleep(0.1)
                player.play()

        for widget in window.children():
            widget.hide()
        text = '''
              Επιλέξτε τις μουσικές που θέλετε να παίζουν
              κάθε φορά που θα ανοίγετε το παιχνίδι.
'''
        label_music = QLabel(text, window)
        label_music.setFont(font)
        label_music.resize(600, 150)
        label_music.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 20px;
        """)
        label_music.move(0, 0)

        music1 = QCheckBox("Standard Music", window)
        music1.resize(400, 70)
        music1.move(150, 160)
        music1.setFont(font)

        music2 = QCheckBox("Memories of Spring", window)
        music2.setFont(font)
        music2.resize(400, 70)
        music2.move(150, 200)

        music3 = QCheckBox("Vibramusic", window)
        music3.setFont(font)
        music3.resize(400, 70)
        music3.move(150, 240)

        music4 = QCheckBox("Cinspirational", window)
        music4.setFont(font)
        music4.resize(400, 70)
        music4.move(150, 280)

        music5 = QCheckBox("Σαρακινοί", window)
        music5.setFont(font)
        music5.resize(400, 70)
        music5.move(150, 320)

        but_ret = QPushButton("Επιστροφή", window)
        but_ret.setFont(font)
        but_ret.resize(400, 100)
        but_ret.move(300, 390)

        demo = QPushButton("Δοκιμή", window)
        demo.setFont(font)
        demo.resize(400, 100)
        demo.move(568, 180)

        open_yours_file = QPushButton("Παίξε από δικό σου αρχείο.", window)
        open_yours_file.setFont(font)
        open_yours_file.resize(400, 100)
        open_yours_file.move(568, 285)

        note = QLabel('''Σημείωση: Οι αλλαγές εφαρμόζονται αμέσως
μετά την επανεκκίνηση του παιχνιδιού.''', window)
        note.setFont(font)
        note.resize(600, 150)
        note.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 20px;
        """)
        note.setAlignment(Qt.AlignCenter)
        note.move(200, 500)

        with open(setting, 'r', encoding='utf-8') as settings_file:
            lines = settings_file.readlines()
            Standard_Music = lines[0].strip()
            Memories_of_Spring = lines[1].strip()
            Vibramusic = lines[2].strip()
            Cinspirational = lines[3].strip()
            Σαρακινοί = lines[4].strip()

        music1.setChecked(Standard_Music == "1")
        music2.setChecked(Memories_of_Spring == "1")
        music3.setChecked(Vibramusic == "1")
        music4.setChecked(Cinspirational == "1")
        music5.setChecked(Σαρακινοί == "1")

        restart = QPushButton("Επανεκκίνηση παιχνιδιού.", window)
        restart.setFont(font)
        restart.resize(400, 100)
        restart.move(300, 670)

        restart.show()
        demo.show()
        open_yours_file.show()
        music3.show()
        music5.show()
        music4.show()
        music2.show()
        music1.show()
        label_music.show()
        but_ret.show()
        note.show()

        open_yours_file.clicked.connect(open_the_file)
        but_ret.clicked.connect(go_to_back)
        restart.clicked.connect(reopen)
        demo.clicked.connect(go_to_demo_music)

    def show_credit():
        def back():
            label_creators.deleteLater()
            but_return.deleteLater()
            start()
        but_level.deleteLater()
        but_settings.deleteLater()
        but_creators.deleteLater()
        window.repaint()
        label_creators = QLabel(product, window)
        label_creators.setFont(font)
        label_creators.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 22px; padding: 100px;
        """)
        label_creators.move(25, 0)
        label_creators.resize(950, 680)
        but_return = QPushButton("Επιστροφή", window)
        but_return.setFont(font)
        but_return.resize(400, 100)
        but_return.move(300, 690)
        but_return.clicked.connect(back)
        label_creators.show()
        but_return.show()

    def leve():
        but_level.deleteLater()
        but_settings.deleteLater()
        but_creators.deleteLater()
        window.repaint()
        label = QLabel("Επιλέξτε επίπεδο δυσκολίας", window)
        label.setFont(font)
        label.setStyleSheet("""
            border: 2px solid black; border-radius: 10px; font-size: 22px; font-weight: bold; padding: 100px;
        """)
        label.resize(500, 125)
        label.move(250, 0)
        label.show()

        but_easy = QPushButton("Εύκολο", window)
        but_easy.resize(500, 125)
        but_easy.setFont(font)
        but_easy.move(250, 140)

        but_normal = QPushButton("Μεσαίο", window)
        but_normal.setFont(font)
        but_normal.resize(500, 125)
        but_normal.move(250, 270)

        but_hard = QPushButton("Δύσκολο", window)
        but_hard.setFont(font)
        but_hard.resize(500, 125)
        but_hard.move(250, 400)

        but_ret = QPushButton("Επιστροφή", window)
        but_ret.setFont(font)
        but_ret.resize(400, 100)
        but_ret.move(300, 530)

        but_ret.clicked.connect(start)
        but_easy.clicked.connect(go_to_easy)
        but_normal.clicked.connect(go_to_normal)
        but_hard.clicked.connect(go_to_hard)

        but_ret.show()
        label.show()
        but_easy.show()
        but_normal.show()
        but_hard.show()

    but_level = QPushButton("Επιλογή επιπέδου δυσκολίας", window)
    but_level.setFont(font)
    but_level.resize(500, 150)
    but_level.move(250, 165)

    but_settings = QPushButton("Ρυθμίσεις", window)
    but_settings.resize(500, 150)
    but_settings.setFont(font)
    but_settings.move(250, 325)

    but_creators = QPushButton("Συντελεστές", window)
    but_creators.resize(500, 150)
    but_creators.setFont(font)
    but_creators.move(250, 485)

    but_level.clicked.connect(leve)
    but_creators.clicked.connect(show_credit)
    but_settings.clicked.connect(settings)
    but_level.show()
    but_settings.show()
    but_creators.show()
    if os.path.exists(imaje):
        window.setWindowIcon(QIcon(imaje))
    window.resize(1000, 800)
    window.show()

start()
sys.exit(app.exec_())
