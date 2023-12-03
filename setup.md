# Notes
- [Main Sample Repo](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury)
- [Synth / Flash](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury/tree/master/Sample-Projects/Project-0/FPGA)
- [Flashing guide](https://github.com/Gbps/nitefury-openocd-flashing-guide)

## basic project
The example project has the following functionality:
- DMA from host into onboard DDR (DMA/Bridge Subsystem, MIG Generator, AXI interconnect)
- Read/Write some registers (GPIO hardcoded "NITE" and "2", XADC Sensors for onboard voltage and temp)
- blinky one of the onboard LEDs

## addressing
See [readme.md](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury/blob/master/Sample-Projects/Project-0/FPGA/readme.md) which shows the register map:
- `0`: 4 byte hardcoded text of "NITE", from GPIO register block
- `4`: 4 byte hardcoded value 2, from GPIO register block

- 0x0000: mapped to gpio 0
- 0x1000: mapped to gpio 1
- 0x2000: mapped to gpio 2
- 0x3000: mapped to XADC sensors
- 0x10000: mapped to axi quad spi

## Digilent FT232H cable drivers
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

- `test_general` reads/writes the GPIO registers containing the hard coded "NITE" and the version, and the XADC register with system information like temp and voltage.
- `test-ddr` writes data through the DMA to the onboard memory, then reads data back through the DMA from the onboard memory. 
