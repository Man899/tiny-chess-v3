# tiny-chess v3: 0x88 alpha-beta engine, 150k nodes/move + check extension.
# The engine is lzma-packed in engine.lzma (same code as the measured v3).
import lzma, os
exec(lzma.decompress(open(os.path.join(os.path.dirname(__file__), "engine.lzma"), "rb").read()))
