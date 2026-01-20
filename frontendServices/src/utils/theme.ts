import { createTheme } from "@mui/material/styles";

export const getTheme = (mode: "light" | "dark") =>
  createTheme({
    palette: {
      mode,
      background: {
        default: mode === "dark" ? "#13273f" : "#F7F9FC",

        // 👇 semi-transparent by design
        paper:
          mode === "dark"
            ? "rgba(10, 20, 30, 0.65)"
            : "rgba(255, 255, 255, 0.75)",
      },
      primary: {
        main: mode === "dark" ? "#90caf9" : "#000000",
      },
      secondary: {
        main: mode === "dark" ? "#3d97e0" : "#5a5a5a",
      },
        gradient: {
    title:
      mode === "dark"
        ? "linear-gradient(90deg, #041830, #22d3ee, #a78bfa)"
        : "linear-gradient(90deg, #8594b4, #2012da, #0c2e79)",
  },
    },

    components: {
      /** 🌍 GLOBAL BACKGROUND */
      MuiCssBaseline: {
        styleOverrides: {
          body: {
            backgroundImage:
              mode === "dark"
                ? "url('/src/assets/testPaddleNight3.jpg')"
                : "url('/src/assets/testPaddleDay2.jpg')",
            backgroundSize: "100% auto",
            backgroundRepeat: "repeat-y",
            backgroundPosition: "top center",
            minHeight: "100vh",
          },
        },
      },

      /** 🧭 HEADER */
      MuiAppBar: {
        styleOverrides: {
          root: {
            backgroundImage:
              mode === "dark"
                ? "url('/images/header-night.jpg')"
                : "url('/images/header-day.jpg')",
            backgroundSize: "cover",
            backgroundPosition: "center",
          },
        },
      },
    },
  });
