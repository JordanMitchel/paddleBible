import {
  AppBar,
  Toolbar,
  Box,
  Typography,
  Button,
  IconButton,
  Menu,
  MenuItem,
} from "@mui/material";
import { GiHamburgerMenu } from "react-icons/gi";
import { BsFillPersonFill } from "react-icons/bs";
import { GiPaddles } from "react-icons/gi";
import { useState } from "react";
import { useThemeMode } from "@/context/theme-context";
import { NAVIGATION_TABS } from "@/utils/constants";
import { NavLink } from 'react-router-dom';



interface HeaderProps {
  user?: boolean; // or a more complex user object
}

export function Header({
  user,
}:HeaderProps) {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const menuOpen = Boolean(anchorEl);
  const { toggleMode } = useThemeMode(); // <--- get the real toggle function

  const openMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const closeMenu = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar position="sticky" elevation={2} sx={{bgcolor:'background.paper'}} >
      <Toolbar sx={{ justifyContent: "space-between", px: 3 }}>
        {/* Logo */}
        <Box display="flex" alignItems="center" gap={1}>
          <IconButton
            onClick={toggleMode}
            aria-label="Toggle theme mode"
            sx={{color:"text.primary"}}
          >
            <GiPaddles size={26} />
          </IconButton>
          <Typography
            variant="h5"
            fontWeight="bold"
            color="text.primary"
          >
            Paddle - Bible
          </Typography>
        </Box>

        {/* Desktop menu */}
        <Box
          sx={{
            display: { xs: "none", md: "flex" },
            alignItems: "center",
            gap: 2,
          }}
        >
          {user && <BsFillPersonFill  color="primary" />}

          {NAVIGATION_TABS.map((item: any) => (
          <Button
            component={NavLink}
            to={item.path}
            sx={{color: "text.primary"}}
          >
            {item.label}
          </Button>
          ))}

          <Button
            sx={{ color:"text.primary", fontWeight: 600}}
            onClick={() => console.log("login")}
          >
            Login
          </Button>


        </Box>

        {/* Mobile controls */}
        <Box sx={{ display: { xs: "flex", md: "none" }, gap: 1 }}>
          {user && <BsFillPersonFill  color="primary" />}

          <IconButton
            aria-label="Open menu"
            onClick={openMenu}
            color="inherit"
          >
            <GiHamburgerMenu />
          </IconButton>

          <Menu
            anchorEl={anchorEl}
            open={menuOpen}
            onClose={closeMenu}
            anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
            transformOrigin={{ vertical: "top", horizontal: "right" }}
          >
            {NAVIGATION_TABS.map((item:any) => (
            <Button
              component={NavLink}
              to={item.path}
            >
              <item.icon />
              {item.label}
            </Button>
            ))}

            <MenuItem
              onClick={() => {
                console.log("login");
                closeMenu();
              }}
            >
              Login
            </MenuItem>

            <MenuItem
              onClick={() => {
                toggleMode();
                closeMenu();
              }}
            >
              Toggle theme
            </MenuItem>
          </Menu>
        </Box>
      </Toolbar>
    </AppBar>
  );
}


export default Header;