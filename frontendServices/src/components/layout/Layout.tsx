import { Routes, Route } from 'react-router-dom';
import { Box } from '@mui/material';

import Header from '@/components/ui/Header';
import Home from '@/pages/Home';
import Read from '@/pages/Read';
import Paddle from '@/pages/Paddle';
import Explore from '@/pages/Explore';
import About from '@/pages/About';
import Footer from '../ui/Footer';

const Layout = () => {
  return (
    <Box minHeight="100vh" display="flex" flexDirection="column">
      <Header />

      {/* Main page content */}
      <Box component="main" flex={1}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/read" element={<Read />} />
          <Route path="/paddle" element={<Paddle />} />
          <Route path="/explore" element={<Explore />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Box>
      <Footer/>
    </Box>
  );
};

export default Layout;
