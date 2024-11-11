class Book:
    material = "paper"
    text_is_presented = True

    def __init__(self, name, author, volume, isbn, reserved):
        self.name = name
        self.author = author
        self.volume = volume
        self.isbn = isbn
        self.reserved = reserved

    def display_reservation_status(self):
        if self.reserved:
            return "зарезервирована"
        else:
            return ""

    def display_book_details(self):
        print(f"Название книги: {self.name}, "
              f"Автор: {self.author}, "
              f"Количество страниц: {self.volume}, "
              f"Материал: {self.material},"
              f"{self.display_reservation_status()}")


Ulysses = Book("Ulysses", "James", 345, None, True)
Mockingbird = Book("Mockingbird", "Harper", 455, None, False)
Lolita = Book("Lolita", "Nabokov", 565, None, False)
Watchbird = Book("Watchbird", "Sheckley", 134, None, False)
Beloved = Book("Beloved", "Morrison", 456, None, False)

Ulysses.display_book_details()
Mockingbird.display_book_details()
Lolita.display_book_details()
Watchbird.display_book_details()
Beloved.display_book_details()


class School(Book):
    def __init__(self, name, author, volume, isbn, reserved, subject, klass, exercises):
        super().__init__(name, author, volume, isbn, reserved)
        self.subject = subject
        self.klass = klass
        self.exercises = exercises

    def display_book_details(self):
        super().display_book_details()
        print(f"предмет: {self.subject}, класс: {self.klass}")


Math = School("Algebra", "Ivanov", 450, None, True, "Algebra", "9 класс", None)
English_language = School("English", "James", 600, None, False, "English", "10 класс", None)
Chemistry = School("Biology", "Smirnov", 456, None, False, "Biology", "11 класс", None)
Math.display_book_details()
English_language.display_book_details()
Chemistry.display_book_details()
