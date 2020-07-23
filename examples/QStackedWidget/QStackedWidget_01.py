# ---------------------------
# StackedWidgetを表示する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit, QStackedWidget

app = QApplication(sys.argv)

qw_text_edit_1 = QTextEdit()
qw_text_edit_1.append('1')

qw_text_edit_2 = QTextEdit()
qw_text_edit_2.append('2')

qw_stack = QStackedWidget()
 # QStackedWidgetにTextEditを2つ追加する
qw_stack.addWidget(qw_text_edit_1)
qw_stack.addWidget(qw_text_edit_2)
print(qw_stack.currentIndex())

qw_stack.show() # 最初に追加したTextEditが表示される

sys.exit(app.exec_())