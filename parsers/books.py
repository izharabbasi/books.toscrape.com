from locators.book_locators import booksLocators


class FindBooks:

    RATING = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    def __init__(self, parent):
        self.parent = parent

    @property
    def Name(self):
        locators = booksLocators.NAME
        name = self.parent.select_one(locators).attrs["title"]
        return name

    @property
    def Link(self):
        locators = booksLocators.LINK
        link = self.parent.select_one(locators).attrs["href"]
        return link

    @property
    def Price(self):
        locators = booksLocators.PRICE
        price = self.parent.select_one(locators).string
        return price

    @property
    def Rating(self):
        locators = booksLocators.RATING
        rating = self.parent.select_one(locators)
        classes = rating.attrs["class"]
        rating_classess = [r for r in classes if r != "star-rating"]
        rating_number = FindBooks.RATING.get(rating_classess)
        return rating_number
