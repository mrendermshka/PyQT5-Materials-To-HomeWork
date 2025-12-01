from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout
import sys

app = QApplication(sys.argv)                     # Створюємо програму, щоб вона могла працювати

win = QWidget()                                  # Створюємо головне вікно програми
layout = QVBoxLayout(win)                        # Робимо коробку, куди складатимемо елементи зверху вниз

tabs = QTabWidget()                              # Створюємо набір вкладок (як у браузері)
tabs.setTabsClosable(False)                      # Вкладки поки що не можна закривати хрестиком

# ------------------- перша вкладка -------------------

first_tab = QWidget()                            # Створюємо першу вкладку
first_layout = QVBoxLayout(first_tab)            # Робимо коробку всередині вкладки
first_layout.addWidget(QLabel("Це перший таб"))  # Пишемо текст, щоб було видно, що це перша вкладка
tabs.addTab(first_tab, "Tab 1")                  # Додаємо вкладку з назвою "Tab 1"

# ------------------- вкладка з плюсом -------------------

plus_tab = QWidget()                             # Створюємо вкладку для кнопки "+"
tabs.addTab(plus_tab, "+")                       # Додаємо вкладку, яка виглядає як кнопка "+"

# ------------------- коли натискають на "+", створюємо нову вкладку -------------------

def on_tab_changed(index):                       # Це відбувається, коли людина натискає іншу вкладку
    if tabs.tabText(index) == "+":               # Якщо людина натиснула на ту вкладку, де написано "+"
        new_tab = QWidget()                      # Створюємо нову вкладку
        new_layout = QVBoxLayout(new_tab)        # Робимо коробку всередині нової вкладки
        new_layout.addWidget(QLabel("Новий таб"))# Показуємо текст, що це нова вкладка

        count = tabs.count()                     # Дізнаємося, скільки вкладок уже є
        tabs.insertTab(count - 1, new_tab, f"Tab {count}")  # Додаємо нову вкладку перед плюсом

        tabs.setCurrentIndex(count - 1)          # Перемикаємося на нову вкладку, щоб її було видно

tabs.currentChanged.connect(on_tab_changed)      # Якщо вкладка змінюється – запускаємо нашу функцію

layout.addWidget(tabs)                           # Додаємо вкладки у головне вікно
win.show()                                       # Показуємо вікно на екрані
sys.exit(app.exec_())                            # Запускаємо програму, щоб вона не закрилась одразу
