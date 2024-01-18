# TODO Найдите количество книг, которое можно разместить на дискете
bytes_in_char = 4
chars_in_line = 25
lines_in_page = 50
pages_in_book = 100
diskette_size_MB = 1.44

book_size = bytes_in_char * chars_in_line * lines_in_page * pages_in_book
diskette_size_B = diskette_size_MB * (1024 ** 2)
max_books_on_diskette = int(diskette_size_B // book_size)

print("Количество книг, помещающихся на дискету:", max_books_on_diskette)
