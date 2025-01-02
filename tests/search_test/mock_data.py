from src.models.response import ResponseModel

mock_bible_books = ResponseModel(
        success=True,
        data=[
            {'book': 1, 'book_name': 'Genesis'},
            {'book': 2, 'book_name': 'Exodus'},
            {'book': 3, 'book_name': 'Leviticus'},
        ]
    )
