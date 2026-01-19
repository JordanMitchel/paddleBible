import React, { useEffect, useState } from "react";
import { QRCodeCanvas } from "qrcode.react";
import { BibleBook, getBibleBooks } from "@/services/scripture";
import SelectCustom from "@/components/ui/Select";

const Read: React.FC = () => {
  const [books, setBooks] = useState<BibleBook[]>([]);
  const [book, setBook] = useState<string>("");
  // const [chapters, setChapters] = useState<number[]>([]);
  // const [chapter, setChapter] = useState<number>(1);
  // const [verses, setVerses] = useState<number[]>([]);
  // const [verseCounts, setVerseCounts] = useState<Record<number, number>>({});
  // const [verse, setVerse] = useState<number>(1);
  // const [chapterText, setChapterText] = useState<{ verse: number; text: string }[]>([]);
  const [showModal, setShowModal] = useState(false);
  const [code, setCode] = useState("");

  // const verseRefs = useRef<Record<number, HTMLParagraphElement | null>>({});

  // Load initial books
  useEffect(() => {
    getBibleBooks().then(setBooks).catch(console.error);
    },[]);


  const handleGoClick = () => {
    const newCode = Math.random().toString(36).substring(2, 8).toUpperCase();
    setCode(newCode);
    setShowModal(true);
  };
  const handleClose = () => setShowModal(false);

  return (
    <div className="w-full max-w-2xl mx-auto px-4 sm:px-6 py-8 sm:py-16">
      {/* Selectors */}
      <div className="flex flex-col sm:flex-row mb-6 gap-4">
        <div className="flex  gap-4 flex-grow">
          {/* Book */}
          <SelectCustom/>
          <SelectCustom/>
          <SelectCustom/>

        </div>

        <div className="flex items-end justify-end flex-grow mt-4 ">
          <button
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded-lg ml-4"
            onClick={handleGoClick}
          >
            Share
          </button>
          <button className="bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-2 rounded-lg ml-2">
            Go
          </button>
        </div>
      </div>

    </div>
  );
};

export default Read;
