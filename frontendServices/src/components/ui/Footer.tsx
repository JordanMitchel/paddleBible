import { FOOTER_SECTIONS } from '@/utils/footer.config';
import { Grid, Stack, Typography, Link } from '@mui/material';


export default function Footer() {
  return (
    <Grid
      container
      justifyContent="center"
      padding={4}
      bgcolor="background.paper"
      spacing={4}
    >
      {FOOTER_SECTIONS.map((section) => {
        const iconLinks = section.links.filter((l) => l.icon);
        const textLinks = section.links.filter((l) => !l.icon);

        return (
          <Grid size={{ xs: 12, sm: 6, md: 3 }} key={section.title}>
            <Stack spacing={1.5} alignItems="flex-start">
              <Typography variant="h6" color="primary">
                {section.title}
              </Typography>

              {/* 🔹 Icon row (Login section only, implicitly) */}
              {iconLinks.length > 0 && (
                <Stack direction="row" spacing={2} alignItems="center">
                  {iconLinks.map((link) => (
                    <Link
                      key={link.label}
                      href={link.href}
                      aria-label={link.label}
                      sx={{ display: 'inline-flex' }}
                    >
                      {link.icon}
                    </Link>
                  ))}
                </Stack>
              )}

              {/* 🔹 Normal text links */}
              {textLinks.map((link) => (
                <Link
                  key={link.label}
                  href={link.href}
                  underline="hover"
                  variant="body2"
                >
                  {link.label}
                </Link>
              ))}
            </Stack>
          </Grid>
        );
      })}

      {/* Footer bottom row */}
      <Grid size={{ xs: 12 }}>
        <Stack alignItems="center" mt={4}>
          <Typography variant="body2" color="text.secondary">
            © 2026 Paddle. All rights reserved.
          </Typography>
        </Stack>
      </Grid>
    </Grid>
  );
}
