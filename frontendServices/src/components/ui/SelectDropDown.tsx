import * as React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';

type SelectDropDownProps = {
  dropDownType: string;
  valuesList ?: string[] | number[];
};

export default function SelectDropDown({dropDownType,valuesList}:SelectDropDownProps) {
  const [formVal, setFormVal] = React.useState('');

  const handleChange = (event: SelectChangeEvent) => {
    setFormVal(event.target.value);
  };

  return (
    <div>
      <FormControl sx={{ m: 1, minWidth: 120 }}>
        <InputLabel id="demo-simple-select-autowidth-label">{dropDownType}</InputLabel>
        <Select
          labelId="demo-simple-select-autowidth-label"
          id="demo-simple-select-autowidth"
          value={formVal}
          onChange={handleChange}
          autoWidth
          label= {dropDownType}
        >
          {valuesList && valuesList.map((val) => (
            <MenuItem key={val} value={val}>{val}</MenuItem>
          ))}
        </Select>
      </FormControl>
    </div>
  );
}
