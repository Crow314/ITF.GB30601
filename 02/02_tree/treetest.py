from tree import Tree

if __name__ == "__main__":
  root = Tree("A",
    Tree("B",
      Tree("C", None, None),
      Tree("D", None, None)),
    Tree("E",
      Tree("F", None, None),
      None))

  for node in root:
    print(node._label)# treetest.py
