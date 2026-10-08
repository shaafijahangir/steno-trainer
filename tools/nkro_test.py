# Polls global key state; reports most keys held at once. Focus doesn't matter.
import ctypes, time, sys
u = ctypes.windll.user32
secs = float(sys.argv[1]) if len(sys.argv) > 1 else 20
names = {i: chr(i) for i in range(0x41, 0x5B)}
names.update({0xBA: ';', 0xDE: "'", 0xBC: ',', 0xBE: '.', 0xBF: '/', 0xDB: '[', 0xDD: ']',
              0x20: 'Space'})
names.update({0x30 + i: str(i) for i in range(10)})
best = set(); end = time.time() + secs
print(f"Press and HOLD as many letter keys as you can at once, both hands. {secs:.0f}s...", flush=True)
while time.time() < end:
    down = {n for vk, n in names.items() if u.GetAsyncKeyState(vk) & 0x8000}
    if len(down) > len(best):
        best = down; print(f"  {len(best)} keys at once: {' '.join(sorted(best))}", flush=True)
    time.sleep(0.005)
print(f"\nMAX = {len(best)} keys. Plover needs ~10+ (full steno chord). 6 or less = 6KRO, won't work well.")
