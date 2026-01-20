import "@mui/material/styles";

declare module "@mui/material/styles" {
  interface Palette {
    gradient: {
      title: string;
    };
  }

  interface PaletteOptions {
    gradient?: {
      title?: string;
    };
  }
}
