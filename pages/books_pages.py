from bs4 import BeautifulSoup

from locators.book_page_locators import PageLocators


class QuotesPage:

    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser").content

    @property
    def books(self):
        locators = PageLocators.BOOKS
        book = self.soup.select_one(locators)
        return [BookParsers(e) for e in book]
