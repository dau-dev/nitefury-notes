from math import log2
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

        size = int(log2(clk_freq // 8))
        counter = Signal(size, init=0)

        m.submodules.counter = Instance(
            "counter",
            i_clk=ClockSignal(),
            o_out=counter,
            p_OUT_SIZE=size,
        )
        m.submodules.shifter = Instance(
            "shifter",
            i_clk=ClockSignal(),
            i_counter=counter,
            o_out=Cat(led.o for led in leds),
            p_IN_SIZE=size,
            p_OUT_SIZE=4,
        )

        platform.add_file("counter.sv", Path("counter.sv").read_text())
        platform.add_file("shifter.sv", Path("shifter.sv").read_text())
        return m


NitefuryIIPlatform().build(Chaser(), do_program=True)
