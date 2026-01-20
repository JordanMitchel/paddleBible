import { Box, Container } from "@mui/material";

type pageContainerTypes = {
    children: React.ReactNode;
    bgcolor?: string;
}

const PageSection = ({ children, bgcolor }:pageContainerTypes) => (
  <Box
    component="section"
    py={{ xs: 4, md: 7, lg: 12 }}
    bgcolor={bgcolor}
  >
    <Container maxWidth="lg">
      {children}
    </Container>
  </Box>
);
export default PageSection;