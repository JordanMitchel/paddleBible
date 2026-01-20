import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";


export default function CardChapter({bookName, chapterNumber}: {bookName: string; chapterNumber: number}) {
  return (
    <Card>
      <CardHeader
        title= {bookName} 
        subheader= {`Chapter ${chapterNumber}`}
      />
    </Card>
  );
}
