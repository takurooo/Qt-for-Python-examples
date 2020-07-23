# ---------------------------
# TextEditの文字の大きさを変える
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit

app = QApplication(sys.argv)

qw_text_edit = QTextEdit()
qw_text_edit.setFontPointSize(30)  # 文字の大きさを変える
qw_text_edit.append('This is a text edit widget.')
qw_text_edit.show()

sys.exit(app.exec_())