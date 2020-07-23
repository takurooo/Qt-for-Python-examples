# ---------------------------
# StackedWidgetに登録されたwidgetをインデックスで指定して表示する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTextEdit, QStackedWidget

app = QApplication(sys.argv)

qw_text_edit_1 = QTextEdit()
qw_text_edit_1.append('1')

qw_text_edit_2 = QTextEdit()
qw_text_edit_2.append('2')

qw_stack = QStackedWidget()
idx_qw_text_edit_1 = qw_stack.addWidget(qw_text_edit_1)
idx_qw_text_edit_2 = qw_stack.addWidget(qw_text_edit_2)
print(idx_qw_text_edit_1, idx_qw_text_edit_2)

 # 表示するwidgetをインデックスで指定する
qw_stack.setCurrentIndex(idx_qw_text_edit_2)
print(qw_stack.currentIndex())

qw_stack.show()

sys.exit(app.exec_())