import { BookIcon, BookmarkIcon, GroupIcon, SearchIcon, Settings2Icon, StarIcon } from "lucide-react";

const features = [
  {
    icon: <BookIcon color="blue" size={32} />,
    title: "Clean Reading Mode",
    description: "Distraction-free optimised for long reading sessions.",
    backgroundColor: "#4b56b9",
  },
  {
    icon: <BookmarkIcon color="teal" size={32} />,
    title: "Explore by Theme",
    description: "Navigate by topic, keywords, or character arcs.",
    backgroundColor: "#c2dbaa",
  },
  {
    icon: <GroupIcon color="navy" size={32} />,
    title: "Community Study",
    description: "Join group reading sessions, share insights with others.",
    backgroundColor: "#914ea1",
  },
  {
    icon: <SearchIcon color="grey" size={32} />,
    title: "Powerful Search",
    description: "Instantly find passages across any text or version.",
    backgroundColor: "#6e7f8080",
  },
  {
    icon: <StarIcon color="teal" size={32} />,
    title: "Custom Highlights",
    description: "Color-coded notes and highlights for quick reference.",
    backgroundColor: "#927c34",
  },
  {
    icon: <Settings2Icon color="#7468a080" size={32} />,
    title: "Version Control",
    description: "Switch translations or editions seamlessly.",
    backgroundColor: "#e274ab80",
  },
];

export default features;