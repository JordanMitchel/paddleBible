import { FormControlLabel, Switch } from '@mui/material';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Typography from '@mui/material/Typography';
import { QRCodeCanvas } from "qrcode.react";

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

export default function BibleModal({open, onClose, shareData}: {open: boolean; onClose: () => void; shareData?: {title: string; text: string; url: string}}) {


  return (
    <div>
      <Modal
        keepMounted
        open={open}
        onClose={onClose}
        aria-labelledby="keep-mounted-modal-title"
        aria-describedby="keep-mounted-modal-description"
      >
        <Box sx={style}>
            {shareData?.url &&(
            <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2 }}>
                <QRCodeCanvas
                    value={shareData.url}
                    size={150}
                    bgColor={"#ffffff"}
                    fgColor={"#000000"}
                    level={"H"}
                />
            </Box>
            )}
          <Typography id="keep-mounted-modal-title" variant="h6" component="h2">
            {shareData?.title}
          </Typography>
          <Typography id="keep-mounted-modal-description" sx={{ mt: 2 }}>
            {shareData?.text} - {shareData?.url}
          </Typography>
            <FormControlLabel control={<Switch defaultChecked={false} />} label="Allow Multi-control" />

        </Box>
      </Modal>
    </div>
  );
}
