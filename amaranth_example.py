from amaranth_boards.nitefury import NitefuryIIPlatform
from amaranth import Elaboratable, Module, Signal, Cat
from amaranth.lib import io


class Chaser(Elaboratable):
    def elaborate(self, platform):
        m = Module()

        clk_freq = platform.default_clk_frequency

        leds = [io.Buffer("o", platform.request("led", i, dir="-")) for i in range(4)]
        m.submodules += leds

        timer = Signal(range(int(clk_freq//8)), init=0)
        flop_1 = Signal(1, init=1)
        flop_2 = Signal(1, init=1)
        flop_3 = Signal(1, init=1)
        flop_4 = Signal(1, init=0)

        m.d.comb += Cat(led.o for led in leds).eq(Cat(flop_1, flop_2, flop_3, flop_4))

        with m.If(timer == 0):
            m.d.sync += flop_1.eq(flop_4)
            m.d.sync += flop_2.eq(flop_1)
            m.d.sync += flop_3.eq(flop_2)
            m.d.sync += flop_4.eq(flop_3)
        m.d.sync += timer.eq(timer + 1)
        return m

NitefuryIIPlatform().build(Chaser(), do_program=True)
