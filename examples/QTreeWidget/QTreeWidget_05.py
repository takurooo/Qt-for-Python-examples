import sys
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

app = QApplication(sys.argv)

qw_tree = QTreeWidget()
qw_tree.setHeaderLabels(["name", "tel", "mail"])

qw_tree_parent_item_1 = QTreeWidgetItem(['family'])
qw_tree_parent_item_1.addChild(QTreeWidgetItem(['A', '111-111-111', 'aaa@gmail.com']))
qw_tree_parent_item_1.addChild(QTreeWidgetItem(['B', '222-222-222', 'bbb@gmail.com']))

qw_tree_parent_item_2 = QTreeWidgetItem(['school'])
qw_tree_parent_item_2.addChild(QTreeWidgetItem(['C', '333-333-333', 'ccc@gmail.com']))
qw_tree_parent_item_2.addChild(QTreeWidgetItem(['D', '444-444-444', 'ddd@gmail.com']))

qw_tree.addTopLevelItem(qw_tree_parent_item_1)
qw_tree.addTopLevelItem(qw_tree_parent_item_2)
qw_tree.expandAll()
qw_tree.show()

sys.exit(app.exec_())