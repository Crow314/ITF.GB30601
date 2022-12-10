from __future__ import annotations  # クラス内で自分自身の型を参照するために必要

from abc import ABC, abstractmethod
from typing import Optional
from file import File
from directory import Directory


class FileSystem(ABC):
    _instance: Optional[FileSystem] = None

    @staticmethod
    def get_instance():
        # 唯一のインスタンスを(必要なら生成して)返す．

        # (ここに何らかの処理を記述する)
        if FileSystem._instance is None:
            FileSystem._instance = _SimpleFileSystem()

        return FileSystem._instance

    @abstractmethod
    def create_directory(self, name: str) -> Directory:
        pass

    @abstractmethod
    def create_file(self, name: str) -> File:
        pass


class _SimpleFileSystem(FileSystem):
    def create_directory(self, name: str) -> Directory:
        return Directory(name)

    def create_file(self, name: str) -> File:
        return File(name)
