import requests

from pages.books_pages import QuotesPage

page_content = requests.get("http://books.toscrape.com/").content
page = QuotesPage(page_content)

books = page.books
for book in books:
    print(book)
