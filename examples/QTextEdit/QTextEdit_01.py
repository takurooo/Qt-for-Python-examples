# ---------------------------
# TextEditを表示する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit

app = QApplication(sys.argv)

qw_text_edit = QTextEdit()
qw_text_edit.show()

sys.exit(app.exec_())