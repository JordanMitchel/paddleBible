import React, { useState } from "react";
import { QRCodeCanvas } from "qrcode.react";
import { bibleBooks } from "@/utils/bibleBooks";


const chapters = Array.from({ length: 50 }, (_, i) => i + 1); // Example: 50 chapters
const verses = Array.from({ length: 40 }, (_, i) => i + 1);   // Example: 40 verses

const Read: React.FC = () => {
  const [showModal, setShowModal] = useState(false);
  const [code, setCode] = useState("");
  const [book, setBook] = useState(bibleBooks[0]);
  const [chapter, setChapter] = useState(chapters[0]);
  const [verse, setVerse] = useState(verses[0]);

  const handleGoClick = () => {
    // Generate a random code (you can customize this)
    const newCode = Math.random().toString(36).substring(2, 8).toUpperCase();
    setCode(newCode);
    setShowModal(true);
  };

  const handleClose = () => setShowModal(false);

  return (
    <div className="max-w-4xl mx-auto px-6 py-16">
      <div className="flex mb-6">
        <div className="flex space-x-4 flex-grow">
          <div>
            <label htmlFor="language" className="block text-sm font-medium text-gray-700 mb-1">Language</label>
            <select id="language" className="border rounded px-3 py-2 w-40">
              <option value="en">English</option>
              <option value="es">Spanish</option>
              <option value="fr">French</option>
              <option value="de">German</option>
            </select>
          </div>
          <div>
            <label htmlFor="version" className="block text-sm font-medium text-gray-700 mb-1">Bible Version</label>
            <select id="version" className="border rounded px-3 py-2 w-40">
              <option value="niv">NIV</option>
              <option value="kjv">KJV</option>
              <option value="esv">ESV</option>
              <option value="nasb">NASB</option>
           </select>
          </div>
          <div>
            <label htmlFor="book" className="block text-sm font-medium text-gray-700 mb-1">Book</label>
            <select
              id="book"
              className="border rounded px-3 py-2 w-40"
              value={book}
              onChange={e => setBook(e.target.value)}
            >
              {bibleBooks.map(bk => (
                <option key={bk} value={bk}>{bk}</option>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="chapter" className="block text-sm font-medium text-gray-700 mb-1">Chapter</label>
            <select
              id="chapter"
              className="border rounded px-3 py-2 w-28"
              value={chapter}
              onChange={e => setChapter(Number(e.target.value))}
            >
              {chapters.map(ch => (
                <option key={ch} value={ch}>{ch}</option>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="verse" className="block text-sm font-medium text-gray-700 mb-1">Verse</label>
            <select
              id="verse"
              className="border rounded px-3 py-2 w-28"
              value={verse}
              onChange={e => setVerse(Number(e.target.value))}
            >
              {verses.map(vs => (
                <option key={vs} value={vs}>{vs}</option>
              ))}
            </select>
          </div>
        </div>
        <div className="flex items-end justify-end flex-grow">
          <button
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded-lg ml-4"
            onClick={handleGoClick}
          >
            Share
          </button>
          <button
            className="bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-2 rounded-lg ml-2"
            // Add your Go button logic here if needed
          >
            Go
          </button>
        </div>
      </div>

      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-40 z-50">
          <div className="bg-white rounded-lg shadow-lg p-8 flex flex-col items-center">
            <h2 className="text-xl font-bold mb-4">Your Code</h2>
            <div className="text-2xl font-mono mb-4">{code}</div>
            <QRCodeCanvas value={code} size={128} />
            <button
              className="mt-6 bg-gray-700 text-white px-4 py-2 rounded"
              onClick={handleClose}
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Read;