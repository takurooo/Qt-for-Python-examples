# ---------------------------
# TextEditの文字の色を変える
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit
from PySide2.QtGui import QColor

app = QApplication(sys.argv)

qw_text_edit = QTextEdit()
qw_text_edit.setTextColor(QColor(255, 0, 0, 255)) # 文字の色を赤色にする
qw_text_edit.append('This is a text edit widget.')
qw_text_edit.show()

sys.exit(app.exec_())