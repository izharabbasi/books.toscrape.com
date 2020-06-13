from bs4 import BeautifulSoup

from locators.book_page_locators import PageLocators
from parsers.books import FindBooks


class QuotesPage:

    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books(self):
        locators = PageLocators.BOOKS
        books_item = self.soup.select_one(locators)
        return [FindBooks(e) for e in books_item]
