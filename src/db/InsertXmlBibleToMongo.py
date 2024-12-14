import xml.etree.ElementTree as ET
from src.db.config import get_database

tree = ET.parse('../../Data/xml/Bible_English_MSG.xml')

bibleXml = tree.findall('BIBLEBOOK')

version_of_bible = tree._root.attrib.get('biblename')[-3:]
collection = f"Bible_{version_of_bible}"
db =  get_database()
coll = db[collection]

for book in bibleXml:
    # bibleBook = book.find('BIBLEBOOK').text
    book_name = book.attrib.get("bname")
    book_number = book.attrib.get("bnumber")

    chapters = book.findall("CHAPTER")
    for chapter in chapters:
        chapter_num = chapter.attrib.get("cnumber")
        chapter_text = chapter.text
        verses = chapter.findall("VERS")
        for verse in verses:
            verse_num = verse.attrib.get("vnumber")
            verse_text = verse.text
            bible_dict = [
                dict(book_name=book_name, book=book_number, chapter=chapter_num, verse=verse_num, text=verse_text)
            ]
            x = coll.insert(bible_dict)

print (coll.count())
