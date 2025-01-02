import xml.etree.ElementTree as eT
from src.db.config import get_database


async def insert_xml_bible_to_mongo(bible_version:str):
    tree = eT.parse(f'../../Data/xml/{bible_version}.xml')
    
    bible_xml = tree.findall('BIBLEBOOK')
    
    version_of_bible = tree.getroot().attrib.get('biblename')[-3:]
    collection = f"Bible_{version_of_bible}"
    db =  await get_database()
    coll = db[collection]
    
    for book in bible_xml:
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
    
                bible_dict = {
                    "book_name": book_name,
                    "book": book_number,
                    "chapter": chapter_num,
                    "verse": verse_num,
                    "text": verse_text,
                }
                coll.insert_one(bible_dict)
    
    print (coll.count())

insert_xml_bible_to_mongo("Bible_English_MSG")