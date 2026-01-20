import React, { useEffect, useState } from "react";
import { Bible } from "@/services/scripture";
import SelectDropDown from "@/components/ui/SelectDropDown";
import { Box, Button, Grid, Stack, Typography } from "@mui/material";
import { apiGetRequest } from "@/services/api";
import CardChapter from "@/components/ui/CardChapter";
import BibleModal from "@/components/ui/BibleModal";
const Read: React.FC = () => {
  const [openModal, setOpenModal] = React.useState(false);
  const [shareData, setShareData] = useState<{title: string; text: string; url: string} | undefined>(undefined);
  const handleCloseModal = () => setOpenModal(false);
  const [bible, setBible] = useState<Bible>({books: [], book_names: [], book_count: 0});
  const [selectedBookId, setSelectedBookId] = useState<number >(1);
  const [selectedChapterId, setSelectedChapterId] = useState<number>(1);
  const [selectedVerseId, setSelectedVerseId] = useState<number>(1);
  const  chapterArray  : number[] = bible.books.length > 0 ?
    [...Array(bible.books[selectedBookId].chapter_count).keys()].map(i => i + 1) : [];
  const  verseArray  : number[] = (bible.books.length > 0 && bible.books[selectedBookId].chapters.length > 0) ?
    [...Array(bible.books[selectedBookId].chapters[selectedChapterId].verse_count).keys()].map(i => i + 1) : [];
  // Load initial books
  useEffect(() => {
    apiGetRequest("/scripture/BibleBooks").then((data) => {
      setBible(data);
    }).catch((error) => {
      console.error("Error fetching Bible books:", error);
    });
    },[]);

    const handleOnShareClick = () => {
      const data = {
        title: 'Paddle Reading',
        text: `Check out this reading from Paddle: ${bible.book_names[selectedBookId]} Chapter ${selectedChapterId} Verse ${selectedVerseId}`,
        url: window.location.href,
      };
      setShareData(data);
      console.log("Share Data:", shareData);
      setOpenModal(true);
    }

  return (
    <>
    <Stack direction='row' alignItems='center' mt={2}>

      <Stack direction="row" spacing={4} ml={2} >
        <SelectDropDown dropDownType="Book"  valuesList={chapterArray}/>
        <SelectDropDown dropDownType="Chapter" valuesList={bible.book_names}/>
        <SelectDropDown dropDownType="Verse" valuesList={verseArray}/>
      </Stack>
      <Box sx={{ ml: 'auto', display: 'flex', gap: 2  }} mr={2}>
        <Button variant="contained" color="secondary">Go</Button>
        <Button variant="contained" onClick={handleOnShareClick}>Share</Button>
      </Box>
    </Stack>
    <Grid>
      <Typography variant="h3" mt={4} textAlign='left' ml={10}>
        {bible.books.length > 0 &&
          bible.book_names[selectedBookId]
        } G
      </Typography>
      <Box mt={4} mx={10} p={4} boxShadow={3} borderRadius={2} bgcolor="background.paper">
        <Stack spacing={2}>
          {bible.books.length > 0 &&
            bible.books[selectedBookId].chapters.length > 0 &&
            bible.books[selectedBookId].chapters.map((chapter_id) => (
              <CardChapter
                key={chapter_id.chapter_id}
                bookName={bible.book_names[selectedBookId]}
                chapterNumber={chapter_id.chapter_id} />
              ))}
        </Stack>
        <Box mt={4} textAlign="center">

        </Box>
      </Box>  

    </Grid>
    <BibleModal open={openModal} onClose={handleCloseModal} shareData ={shareData} />;

    </>
  );

  
};

export default Read;
