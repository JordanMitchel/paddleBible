import { Box, Card, CardActionArea, CardContent, CardMedia, Icon, Typography } from '@mui/material';
import React from 'react';

type HomeCardProps= {
    icon: React.ReactNode;
    backgroundColor?: string;
    title: string;
    description: string;
}

const HomeCard= ({ icon, title, description, backgroundColor }: HomeCardProps) => {
  return (
            <Card sx={{ margin:1, width: 345,  height: 170, borderRadius: '30px' }}>

                <CardContent>
                    <Box sx={{ mt: 2, display: 'flex', alignItems: 'center' }}>
                        <Box
                        sx={{
                            borderRadius: '30%',
                            width: 50,
                            height: 50,
                            display: 'flex',
                            justifyContent: 'center',
                            alignItems: 'center',
                            mr: 1,
                            backgroundColor: backgroundColor,
                        }}
                        >
                        {icon}
                        </Box>

                        <Typography variant="h5">
                        {title}
                        </Typography>
                    </Box>
                    
                    <Typography variant="body2" sx={{ mt:2,color: 'text.secondary' }}>
                        {description}
                    </Typography>
                </CardContent>
            </Card>
  );
}
export default HomeCard;