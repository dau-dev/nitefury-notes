# Notes
- [Main Sample Repo](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury)
- [Synth / Flash](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury/tree/master/Sample-Projects/Project-0/FPGA)
- [Flashing guide](https://github.com/Gbps/nitefury-openocd-flashing-guide)

## basic project
The example project has the following functionality:
- DMA from host into onboard DDR (DMA/Bridge Subsystem, MIG Generator, AXI interconnect)
- Read/Write some registers (GPIO hardcoded "NITE" and "2", XADC Sensors for onboard voltage and temp)
- blinky one of the onboard LEDs

## blocks
- DMA/Bridge Subsystem for PCIe: Connection between host and on-card registers (xadc and gpio) and on-card memory (MIG to onboard DDR3)
- AXI Interconnect 1 - DMA to MIG
- AXI Interconnect 2 - Registers (XADC and GPIO)
- MIG - AXI bridge to the onboard DDR3

## addressing

See [readme.md](https://github.com/RHSResearchLLC/NiteFury-and-LiteFury/blob/master/Sample-Projects/Project-0/FPGA/readme.md) which shows the register map:
- `0`: 4 byte hardcoded text of "NITE", from GPIO register block
- `4`: 4 byte hardcoded value 2, from GPIO register block

- 0x0000: mapped to gpio 0
- 0x1000: mapped to gpio 1
- 0x2000: mapped to gpio 2
- 0x3000: mapped to XADC sensors
- 0x10000: mapped to axi quad spi

1100
  
## other stuff
- LED A1: mapped to codeblinker.v
- LED A2: mapped to bit 0 of gpio
- LED A3: mapped to [user_lnk_up](https://docs.xilinx.com/r/en-US/pg195-pcie-dma/XDMA-Global-Ports) from xdma: "Output Active-High Identifies that the PCI Express core is linked up with a host device."
- LED A4: mapped to [init_calib_complete](https://docs.xilinx.com/r/en-US/pg353-versal-acap-soft-ddr4-mem-ip/init_calib_complete) from MIG: "PHY asserts init_calib_complete when calibration is finished. The application has no need to wait for init_calib_complete before sending commands to the Memory Controller."
- LED M2: mapped to bit 0 of gpio

## setup
### Digilent FT232H cable drivers
```
cd /opt/Xilinx/Vivado/2022.2/data/xicom/cable_drivers/lin64/install_script/install_drivers
sudo install_digilent.sh
```

### mount XDMA
```bash
sudo modprobe xdma
```

### run tests
```bash
./test_general -i NITE -v 2
./test-ddr.py
```

- `test_general` reads/writes the GPIO registers containing the hard coded "NITE" and the version, and the XADC register with system information like temp and voltage.
- `test-ddr` writes data through the DMA to the onboard memory, then reads data back through the DMA from the onboard memory. 
