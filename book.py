class Book:
    """Class for book representation"""
    def __init__(self, name, author, pages):
        """Initialing attributes"""
        self.name = name
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.mark = None

    def __str__(self):
        """Method for representations"""
        if self.mark is None:
            if self.pages > 1:
                return "Book<{} by {}: {} pages," \
                       " currently on page {}>".format(
                        self.name, self.author, self.pages, self.current_page)
            else:
                return "Book<{} by {}: {} page," \
                       " currently on page {}>".format(
                        self.name, self.author, self.pages, self.current_page)
        else:
            return "Book<{} by {}: {} pages, currently on page {}," \
                   " page {} bookmarked>".format(
                    self.name, self.author, self.pages,
                    self.current_page, self.mark)

    def turnPage(self, number):
        """Turns a page"""
        self.current_page += number
        if self.current_page > self.pages or self.current_page <= 0:
            self.current_page = self.pages

    def getCurrentPage(self):
        """Returns current page"""
        return self.current_page

    def getBookmarkedPage(self):
        """Returns mark position"""
        return self.mark

    def placeBookmark(self):
        """Places a book mark on current page"""
        self.mark = self.current_page

    def turnToBookmark(self):
        """Goes back to book mark"""
        if self.mark is not None:
            self.current_page = self.mark

    def removeBookmark(self):
        """Removes a bookmark"""
        self.mark = None

    def __eq__(self, other):
        """Checking equality"""
        if [self.name, self.author, self.pages,
            self.current_page, self.mark] == \
                [other.name, other.author, other.pages,
                 other.current_page, other.mark]:
            return True
        return False
