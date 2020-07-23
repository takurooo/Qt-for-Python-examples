# ---------------------------
# Treeにitemに子itemを追加する
# ---------------------------
import sys
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

app = QApplication(sys.argv)

qw_tree = QTreeWidget()
qw_tree.setHeaderLabels(["name", "tel", "mail"])
qw_tree_parent_item = QTreeWidgetItem(['family'])
qw_tree_parent_item.addChild(QTreeWidgetItem(['A', '111-111-111', 'aaa@gmail.com']))  # Itemに子Itemを追加
qw_tree.addTopLevelItem(qw_tree_parent_item)
qw_tree.expandAll()  # TreeのItemを全て開く
qw_tree.show()

sys.exit(app.exec_())