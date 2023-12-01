# Notes
- [Main Sample Repo](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury)
- [Synth / Flash](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury/tree/master/Sample-Projects/Project-0/FPGA)
- [Flashing guide](https://github.com/Gbps/nitefury-openocd-flashing-guide)


## Get Vivado to recognize Digilent FT232H cable
```
cd /opt/Xilinx/Vivado/2022.2/data/xicom/cable_drivers/lin64/install_script/install_drivers
sudo install_digilent.sh
```

## mount XDMA
```bash
sudo modprobe xdma
```

## run tests
```bash
./test_general -i NITE -v 2
./test-ddr.py
```
