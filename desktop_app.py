
import sys
import os
if sys.platform.startswith('win'):
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'.venv\Lib\site-packages\PyQt5\Qt5\plugins'
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QCompleter,
    QPushButton, QTableWidget, QTableWidgetItem, QLabel
)
from PyQt5.QtCore import Qt


class PSUApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Подбор блока питания")
        self.resize(600, 400)

        # Загружаем Excel
        self.gpu_df = pd.read_excel("Table_gpu_Pblock.xlsx", sheet_name="GPU", header=None, usecols=[0, 1])
        self.psu_df = pd.read_excel("Table_gpu_Pblock.xlsx", sheet_name="PSU", header=None, usecols=[0, 1])
        self.gpu_df.columns = ["Название", "Рекомендуемая мощность (Вт)"]
        self.psu_df.columns = ["Модель", "Мощность (Вт)"]
        # Интерфейс
        layout = QVBoxLayout()

        self.label = QLabel("Введите название видеокарты:")
        layout.addWidget(self.label)

        # Поле ввода с автодополнением
        self.gpu_input = QLineEdit()
        completer = QCompleter(self.gpu_df["Название"].tolist())
        completer.setCaseSensitivity(False)  # игнор регистра
        completer.setFilterMode(Qt.MatchContains)  # поиск по подстроке!
        self.gpu_input.setCompleter(completer)
        layout.addWidget(self.gpu_input)

        # Кнопка поиска
        self.btn = QPushButton("Подобрать блок питания")
        self.btn.clicked.connect(self.find_psu)
        layout.addWidget(self.btn)

        # Таблица для вывода результатов
        self.result_table = QTableWidget()
        layout.addWidget(self.result_table)

        self.setLayout(layout)

    def find_psu(self):
        gpu_name = self.gpu_input.text().strip()

        if gpu_name not in self.gpu_df["Название"].values:
            self.label.setText("❌ Видеокарта не найдена!")
            return

        # Находим требуемую мощность
        required_power = self.gpu_df.loc[
            self.gpu_df["Название"] == gpu_name, "Рекомендуемая мощность (Вт)"
        ].values[0]

        self.label.setText(f"Видеокарта: {gpu_name}, рекомендуемая мощность: {required_power} Вт")

        # Фильтруем подходящие БП
        psu_filtered = self.psu_df[self.psu_df["Мощность (Вт)"] >= required_power]

        # Заполняем таблицу
        self.result_table.setRowCount(len(psu_filtered))
        self.result_table.setColumnCount(len(psu_filtered.columns))
        self.result_table.setHorizontalHeaderLabels(psu_filtered.columns)

        for row in range(len(psu_filtered)):
            for col, value in enumerate(psu_filtered.iloc[row]):
                self.result_table.setItem(row, col, QTableWidgetItem(str(value)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PSUApp()
    window.show()
    sys.exit(app.exec_())
