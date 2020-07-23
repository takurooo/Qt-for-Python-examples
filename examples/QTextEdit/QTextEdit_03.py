# ---------------------------
# TextEditを編集禁止にする
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit

app = QApplication(sys.argv)

qw_text_edit = QTextEdit()
qw_text_edit.setReadOnly(True)  # 編集禁止にする
qw_text_edit.append('This is a text edit widget.')
qw_text_edit.show()

sys.exit(app.exec_())