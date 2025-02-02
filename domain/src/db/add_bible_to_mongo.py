import asyncio
import json
import aiofiles
import xml.etree.ElementTree as eT
from domain.src.db.add_coordinates_to_mongo import insert_to_mongo
from shared.src.models.FileType import FileTypeEnum


async def insert_bible_store(file_path, file_type, collection_name,bible_version="custom"):
    if file_type == FileTypeEnum.JSON:

        async with aiofiles.open(file_path) as file:
            data = await file.read()
            json_data = json.loads(data)

            data = json_data["verses"]

            await insert_to_mongo(data, collection_name)
    else:
        tree = eT.parse(f'../../Data/xml/{bible_version}.xml')
        bible_xml = tree.findall('BIBLEBOOK')
        version_of_bible = tree.getroot().attrib.get('biblename')[-3:]
        bible_collection_name = f"Bible_{version_of_bible}"

        await insert_into_each_book(bible_xml, bible_collection_name)


async def process_book(book, collection_name):
    book_name = book.attrib.get("bname")
    book_number = book.attrib.get("bnumber")
    book_data = []

    chapters = book.findall("CHAPTER")
    for chapter in chapters:
        chapter_num = chapter.attrib.get("cnumber")
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
            book_data.append(bible_dict)

    if book_data:
        await insert_to_mongo(book_data, collection_name)

async def insert_into_each_book(bible_xml, collection_name):
    tasks = [process_book(book, collection_name) for book in bible_xml]
    await asyncio.gather(*tasks)