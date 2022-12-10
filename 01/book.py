class Book:
  _author: str
  _title: str
  _pages: int

  # オブジェクト生成時に _author フィールドと _title フィールドをセットする．
  def __init__(self, author, title):
    self._author = author
    self._title = title

  # Properties

  @property
  def author(self):
    return self._author

  @property
  def title(self):
    return self._title
  
  @property
  def pages(self):
    return self.pages

  @pages.setter
  def pages(self, pages):
    self._pages = pages

  # Functions

  def print_author(self):
    print(self._author)

  def print_title(self):
    print(self._title)

  def print_pages(self):
    print(self._pages)

  def print_details(self):
    self.print_author()
    self.print_title()
    self.print_pages()


if __name__ == "__main__":
  b = Book("夏目漱石", "坊っちゃん")
  b.pages = 500
  b.print_details()
  b2 = Book("Charles Dickens", "A Tale of Two Cities")
  b2.pages = 400
  b2.print_details()
