from pathlib import Path

from amaranth_boards.nitefury import NitefuryIIPlatform
from amaranth import (
    Elaboratable,
    Module,
    Instance,
    ClockSignal,
    ResetSignal,
    Signal,
    Cat,
)
from amaranth.lib import io


class Chaser(Elaboratable):
    def elaborate(self, platform):
        m = Module()

        clk_freq = platform.default_clk_frequency

        leds = [io.Buffer("o", platform.request("led", i, dir="-")) for i in range(4)]
        m.submodules += leds

        size = range(int(clk_freq // 8))
        counter = Signal(size, init=0)
        flops = Signal(4, init=7)
        
        m.submodules.counter = Instance(
            "counter",
            i_clk=ClockSignal(),
            o_out=counter,
            p_DATA_SIZE=int(clk_freq//8),
        )
        m.submodules.shifter = Instance(
            "shifter",
            i_clk=ClockSignal(),
            o_out=flops,
            p_DATA_SIZE=4,
        )
        m.submodules.setter = Instance(
            "setter",
            i_clk=ClockSignal(),
            i_data=flops,
            o_leds=Cat(led.o for led in leds),
            p_DATA_SIZE=4,
        )

        platform.add_file("counter.sv", Path("counter.sv").read_text())
        platform.add_file("shifter.sv", Path("shifter.sv").read_text())
        platform.add_file("setter.sv", Path("setter.sv").read_text())
        return m


NitefuryIIPlatform().build(Chaser(), do_program=True)
