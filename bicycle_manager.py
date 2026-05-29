import os
import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QAbstractItemView,
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

DB_FILE = "bicycles.db"


def initialize_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Bycle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            qty INTEGER NOT NULL
        );
        """
    )
    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM Bycle;")
    count = cursor.fetchone()[0]
    if count == 0:
        bikes = []
        for i in range(1, 101):
            bikes.append(
                (
                    f"Bike {i:03d}",
                    10000 + (i * 150),
                    1 + ((i - 1) % 15),
                )
            )
        cursor.executemany(
            "INSERT INTO Bycle (name, price, qty) VALUES (?, ?, ?);",
            bikes,
        )
        connection.commit()

    return connection


class BicycleManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_connection = initialize_database()
        self.db_cursor = self.db_connection.cursor()
        self.setWindowTitle("자전거 관리 앱")
        self.setMinimumSize(720, 520)
        self._build_ui()
        self.refresh_table()

    def _build_ui(self):
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)

        label_font = QFont()
        label_font.setPointSize(11)

        input_font = QFont()
        input_font.setPointSize(10)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_widget.setObjectName("main_widget")
        main_widget.setStyleSheet(
            "#main_widget {"
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
            "stop:0 #050a1f, stop:1 #13294b);"
            "}"
        )

        header_label = QLabel("🚲 Bicycle Manager")
        header_label.setFont(title_font)
        header_label.setStyleSheet(
            "color: #f9f0ff;"
            "padding: 14px 0px;"
        )
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        form_container = QWidget()
        form_container.setObjectName("form_container")
        form_container.setStyleSheet(
            "#form_container {"
            "background: rgba(255, 255, 255, 0.08);"
            "border: 1px solid rgba(255, 255, 255, 0.15);"
            "border-radius: 18px;"
            "padding: 18px;"
            "}"
        )

        form_layout = QGridLayout(form_container)
        form_layout.setSpacing(14)

        label_id = QLabel("ID:")
        label_id.setFont(label_font)
        label_id.setStyleSheet("color: #e8f7ff;")
        self.input_id = QLineEdit()
        self.input_id.setReadOnly(True)
        self.input_id.setPlaceholderText("자동 생성")
        self.input_id.setFont(input_font)

        label_name = QLabel("자전거명:")
        label_name.setFont(label_font)
        label_name.setStyleSheet("color: #e8f7ff;")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("예: Bike 001")
        self.input_name.setFont(input_font)

        label_price = QLabel("가격:")
        label_price.setFont(label_font)
        label_price.setStyleSheet("color: #e8f7ff;")
        self.input_price = QLineEdit()
        self.input_price.setPlaceholderText("숫자만 입력")
        self.input_price.setFont(input_font)

        label_qty = QLabel("수량:")
        label_qty.setFont(label_font)
        label_qty.setStyleSheet("color: #e8f7ff;")
        self.input_qty = QLineEdit()
        self.input_qty.setPlaceholderText("숫자만 입력")
        self.input_qty.setFont(input_font)

        label_search = QLabel("검색(이름 또는 ID):")
        label_search.setFont(label_font)
        label_search.setStyleSheet("color: #e8f7ff;")
        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText("Bike 또는 10")
        self.input_search.setFont(input_font)

        for edit in (self.input_id, self.input_name, self.input_price, self.input_qty, self.input_search):
            edit.setStyleSheet(
                "QLineEdit {"
                "background: rgba(255,255,255,0.12);"
                "border: 1px solid rgba(255,255,255,0.18);"
                "border-radius: 10px;"
                "color: #f8faff;"
                "padding: 8px;"
                "}"
                "QLineEdit:focus {"
                "border: 1px solid #77b0ff;"
                "background: rgba(255,255,255,0.18);"
                "}"
            )

        self.input_id.setFixedWidth(120)
        self.input_name.setMinimumWidth(220)
        self.input_price.setFixedWidth(160)
        self.input_qty.setFixedWidth(120)

        self.btn_add = QPushButton("입력")
        self.btn_update = QPushButton("수정")
        self.btn_delete = QPushButton("삭제")
        self.btn_search = QPushButton("검색")
        self.btn_refresh = QPushButton("전체 목록")
        self.btn_export = QPushButton("엑셀출력")

        for btn, color in [
            (self.btn_add, "#4fd6ac"),
            (self.btn_update, "#8fdcff"),
            (self.btn_delete, "#ff7f91"),
            (self.btn_search, "#ffd76b"),
            (self.btn_refresh, "#c18dff"),
            (self.btn_export, "#7cafff"),
        ]:
            btn.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(
                f"background-color: {color}; color: #0f172a; border: none; border-radius: 12px; padding: 12px 16px; min-width: 100px;"
            )

        self.btn_add.clicked.connect(self.add_record)
        self.btn_update.clicked.connect(self.update_record)
        self.btn_delete.clicked.connect(self.delete_record)
        self.btn_search.clicked.connect(self.search_records)
        self.btn_refresh.clicked.connect(self.refresh_table)
        self.btn_export.clicked.connect(self.export_to_excel)

        form_layout.addWidget(label_id, 0, 0)
        form_layout.addWidget(self.input_id, 0, 1)
        form_layout.addWidget(label_name, 0, 2)
        form_layout.addWidget(self.input_name, 0, 3)

        form_layout.addWidget(label_price, 1, 0)
        form_layout.addWidget(self.input_price, 1, 1)
        form_layout.addWidget(label_qty, 1, 2)
        form_layout.addWidget(self.input_qty, 1, 3)

        form_layout.addWidget(label_search, 2, 0)
        form_layout.addWidget(self.input_search, 2, 1, 1, 3)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_update)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_search)
        button_layout.addWidget(self.btn_refresh)
        button_layout.addWidget(self.btn_export)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["ID", "이름", "가격", "수량"])
        self.table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_widget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table_widget.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table_widget.cellClicked.connect(self.on_table_clicked)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setStyleSheet(
            "QTableWidget {"
            "background: rgba(255, 255, 255, 0.08);"
            "border: 1px solid rgba(255, 255, 255, 0.18);"
            "border-radius: 16px;"
            "color: #eef4ff;"
            "gridline-color: rgba(255,255,255,0.12);"
            "}"
            "QHeaderView::section {"
            "background: rgba(255,255,255,0.14);"
            "color: #f3f9ff;"
            "padding: 10px;"
            "border: none;"
            "font-weight: bold;"
            "}"
            "QTableWidget::item:selected {"
            "background: rgba(255, 255, 255, 0.25);"
            "color: #0f172a;"
            "}"
        )
        header = self.table_widget.horizontalHeader()
        header.setStretchLastSection(True)
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setHighlightSections(False)

        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(16, 18, 16, 16)
        main_layout.setSpacing(14)
        main_layout.addWidget(header_label)
        main_layout.addWidget(form_container)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table_widget)

    def _show_message(self, title, message, icon=QMessageBox.Icon.Information):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(message)
        dlg.setIcon(icon)
        dlg.exec()

    def refresh_table(self, rows=None):
        query = "SELECT id, name, price, qty FROM Bycle ORDER BY id;"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        self._populate_table(rows)

    def search_records(self):
        term = self.input_search.text().strip()
        if not term:
            self._show_message("검색 오류", "검색어를 입력하세요.")
            return

        if term.isdigit():
            self.db_cursor.execute(
                "SELECT id, name, price, qty FROM Bycle WHERE id = ? OR name LIKE ? ORDER BY id;",
                (int(term), f"%{term}%"),
            )
        else:
            self.db_cursor.execute(
                "SELECT id, name, price, qty FROM Bycle WHERE name LIKE ? ORDER BY id;",
                (f"%{term}%",),
            )

        rows = self.db_cursor.fetchall()
        if not rows:
            self._show_message("검색 결과", "조건에 맞는 자전거가 없습니다.")
        self._populate_table(rows)

    def add_record(self):
        name = self.input_name.text().strip()
        price_text = self.input_price.text().strip()
        qty_text = self.input_qty.text().strip()

        if not name or not price_text or not qty_text:
            self._show_message("입력 오류", "모든 항목을 입력해 주세요.")
            return

        try:
            price = int(price_text)
            qty = int(qty_text)
        except ValueError:
            self._show_message("입력 오류", "가격과 수량은 숫자여야 합니다.")
            return

        self.db_cursor.execute(
            "INSERT INTO Bycle (name, price, qty) VALUES (?, ?, ?);",
            (name, price, qty),
        )
        self.db_connection.commit()
        self.refresh_table()
        self._show_message("저장 완료", "자전거가 추가되었습니다.")
        self._clear_inputs()

    def update_record(self):
        item_id = self.input_id.text().strip()
        name = self.input_name.text().strip()
        price_text = self.input_price.text().strip()
        qty_text = self.input_qty.text().strip()

        if not item_id:
            self._show_message("수정 오류", "수정할 자전거를 선택하세요.")
            return

        if not name or not price_text or not qty_text:
            self._show_message("수정 오류", "모든 항목을 입력해 주세요.")
            return

        try:
            price = int(price_text)
            qty = int(qty_text)
        except ValueError:
            self._show_message("입력 오류", "가격과 수량은 숫자여야 합니다.")
            return

        self.db_cursor.execute(
            "UPDATE Bycle SET name = ?, price = ?, qty = ? WHERE id = ?;",
            (name, price, qty, int(item_id)),
        )
        self.db_connection.commit()
        self.refresh_table()
        self._show_message("수정 완료", "자전거 정보가 수정되었습니다.")
        self._clear_inputs()

    def delete_record(self):
        item_id = self.input_id.text().strip()
        if not item_id:
            self._show_message("삭제 오류", "삭제할 자전거를 선택하세요.")
            return

        answer = QMessageBox.question(
            self,
            "삭제 확인",
            "선택한 자전거를 삭제하시겠습니까?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if answer != QMessageBox.StandardButton.Yes:
            return

        self.db_cursor.execute("DELETE FROM Bycle WHERE id = ?;", (int(item_id),))
        self.db_connection.commit()
        self.refresh_table()
        self._show_message("삭제 완료", "자전거가 삭제되었습니다.")
        self._clear_inputs()

    def export_to_excel(self):
        try:
            from openpyxl import Workbook
        except ImportError:
            self._show_message(
                "설치 필요", "openpyxl 패키지가 필요합니다. pip install openpyxl 를 실행하세요.",
                QMessageBox.Icon.Warning,
            )
            return

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "엑셀로 저장",
            os.path.join(os.getcwd(), "bicycle_list.xlsx"),
            "Excel Files (*.xlsx)",
        )
        if not filename:
            return

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "자전거 목록"
        headers = ["ID", "이름", "가격", "수량"]
        sheet.append(headers)

        self.db_cursor.execute("SELECT id, name, price, qty FROM Bycle ORDER BY id;")
        rows = self.db_cursor.fetchall()
        for row in rows:
            sheet.append(row)

        workbook.save(filename)
        self._show_message("엑셀 저장 완료", f"데이터를 {filename}에 저장했습니다.")

    def on_table_clicked(self, row, column):
        item_id = self.table_widget.item(row, 0).text()
        name = self.table_widget.item(row, 1).text()
        price = self.table_widget.item(row, 2).text()
        qty = self.table_widget.item(row, 3).text()
        self.input_id.setText(item_id)
        self.input_name.setText(name)
        self.input_price.setText(price)
        self.input_qty.setText(qty)

    def _populate_table(self, rows):
        self.table_widget.setRowCount(len(rows))
        for row_index, row_data in enumerate(rows):
            for col_index, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                if col_index in (0, 2, 3):
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                self.table_widget.setItem(row_index, col_index, item)

    def _clear_inputs(self):
        self.input_id.clear()
        self.input_name.clear()
        self.input_price.clear()
        self.input_qty.clear()
        self.input_search.clear()

    def closeEvent(self, event):
        self.db_connection.close()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BicycleManager()
    window.show()
    sys.exit(app.exec())
