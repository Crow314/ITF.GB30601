from indentobserver import IndentObserver
from countingobserver import CountingObserver
from filesystem import FileSystem

fs = FileSystem.get_instance()
root = fs.create_directory("root")
root.add_observer(CountingObserver())
root.add_observer(IndentObserver())
subdir1 = fs.create_directory("bin")
subdir2 = fs.create_directory("usr")
subdir1.add(fs.create_file("command1"))
subdir1.add(fs.create_file("command2"))
subdir2.add(fs.create_file("data.txt"))
root.add(subdir1)
root.add(subdir2)
