import React from 'react';
import Button from '@/components/ui/Button';
import { useApp } from '@/context/AppContext';
import HomeCard from '@/components/ui/HomeCard';
import { Grid, Stack, Typography } from '@mui/material';

import PageSection from '@/components/ui/PageSection';
import features from '@/utils/features';

const Home: React.FC = () => {
  const { setActiveTab } = useApp(); // Get setActiveTab from context

  return (
    <div>


      
        <PageSection bgcolor="transparent">
          <Stack spacing={0} textAlign={'left'} mb={4} maxWidth={400}>
              <Typography variant='h2' fontWeight={400}
                sx={{
                  background: (theme) => theme.palette.gradient.title,
                  WebkitBackgroundClip: 'text',
                    WebkitTextFillColor: "transparent",
}}
                  >
                  Paddle.
              </Typography>
              <Typography variant='h4' fontWeight={700}>
                Read. Explore.
              </Typography>
              <Typography variant='h4' color='Blue' fontWeight={700}>
                Connect.
              </Typography>
              <Typography variant='h6' color='primary' fontWeight={300} mt={2}>
                Paddle is your digital reading companion designed to enhance your reading experience.
                For thougghtful exploration, colloboration, and deep engagement with texts.
              </Typography>
              <Stack direction="row" spacing={2} mt={2}>
                <Button size="lg" >Start Reading</Button>
                <Button variant="outline"
                  size="lg"
                  onClick={() => setActiveTab('about')} // Add click handler
                >
                  Learn More
                </Button>
              </Stack>

            </Stack>
        </PageSection>
        <PageSection bgcolor="transparent">
          <Stack spacing={5}>
            <Stack spacing={1} textAlign={'center'}>

              <Typography variant='h4' fontWeight={700}>
                Built for deep reading & study
              </Typography>
              <Typography variant='h6' color='primary' fontWeight={500}>
                Everything you need for meaningful engagement with texts
              </Typography>
            </Stack>
            <Grid container spacing={0}>
              {features.map((feature) => (
                <Grid 
                key={feature.title as string}
                size={{ xs: 12, sm: 6, md: 4 }}
                >
                  <HomeCard {...feature} />
                </Grid>
              ))}
            </Grid>
          </Stack>
        </PageSection>
        <PageSection bgcolor="transparent">
          <Stack spacing={2} textAlign={'center'} alignItems={'center'}
  sx={{
    backdropFilter: "blur(10px)",
    backgroundColor: "#a88e8e33",
    borderRadius: 3,
  }}>
            <Typography variant='h6' fontWeight={500} color='primary'>
              Join thousands of readers enhancing their reading experience with Paddle.
            </Typography>
            <Button size="lg" style={{maxWidth:400}}  >Get Started</Button>
            <Typography variant='caption' color='primary' fontWeight={300}>
              Free forever for the Bible • no credit card required.
            </Typography>
          </Stack>
        </PageSection>

    </div>
  );
};

export default Home;