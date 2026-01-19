import ButtonGroup from '@mui/material/ButtonGroup';
import Button from '@mui/material/Button';
type buttonPropsType = {
    buttonName?: string;
    onClick?: () => void;
};
export default function DisableElevation(buttonProps:buttonPropsType[]) {
  return (
    <ButtonGroup
      disableElevation
      variant="contained"
      aria-label="Disabled button group"
    >
        {buttonProps.map((btnProp, index) => (
            <Button key={index} onClick={btnProp.onClick}>{btnProp.buttonName}</Button>
        ))}
      <Button>One</Button>
      <Button>Two</Button>
    </ButtonGroup>
  );
}