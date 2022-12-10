from filesystem import FileSystem, _SimpleFileSystem
from directory import Directory
from countingobserver import CountingObserver

if __name__ == '__main__':
    print(FileSystem.get_instance())
    print(FileSystem.get_instance())

    # 継承
    print(isinstance(FileSystem.get_instance(), FileSystem))
    print(isinstance(FileSystem.get_instance(), _SimpleFileSystem))

    fs: FileSystem = FileSystem.get_instance()

    # ディレクトリの作成
    dir: Directory = fs.create_directory("dir1")
    dir.add_observer(CountingObserver())
    # ファイルを作成しdir1へ追加
    dir.add(fs.create_file("file1"))
