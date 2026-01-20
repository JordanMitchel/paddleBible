

export interface Bible {
  books: BibleBook[];
  book_count: number;
  book_names: string[];
}
export interface BibleBook {
  [x: string]: any;
  book_ids: number;
  book_name: string;
  chapter_count: number;
  chapters: chapter[];
}
export interface chapter {
  chapter_id: number;
  verse_count: number;
  verses: verse[];
  
}
export interface verse {
  verse_id: number;
  verse_text: string;
}

