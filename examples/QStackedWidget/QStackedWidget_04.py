# ---------------------------
# TreeをクリックしてTextEditを切り替える
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QTextEdit, QStackedWidget, QSplitter

app = QApplication(sys.argv)

qw_stack = QStackedWidget()

qw_tree = QTreeWidget()
qw_tree.setHeaderLabels(["test"])


def tree_item_clicked(item, column):
    print(item, column, item.type())
    # TreeがクリックされたときにTextEditを切り替える
    qw_stack.setCurrentIndex(item.type())


for i in range(3):
    text = 'page No.' + str(i+1)
    qw_tree_item = QTreeWidgetItem([text], type=i)
    qw_tree.addTopLevelItem(qw_tree_item)

    qw_text_edit = QTextEdit()
    qw_text_edit.append(text)

    stack_idx = qw_stack.addWidget(qw_text_edit)
    # print(stack_idx)

# Treeがクリックされたときに呼ばれる関数を登録
qw_tree.itemClicked.connect(tree_item_clicked)

qw_splitter = QSplitter()
qw_splitter.addWidget(qw_tree)
qw_splitter.addWidget(qw_stack)

qw_splitter.show()

sys.exit(app.exec_())