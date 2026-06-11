# -*- coding: utf-8 -*-
"""
Demonstratie-hulpprogramma (telt NIET mee voor de beoordeling).

Dit bestand staat los van het eindprogramma op het MysteryDevice. Hier mogen wel
extra libraries gebruikt worden, omdat het alleen dient om tijdens de presentatie
een echte afbeelding in te laden / te tonen en om te zetten naar een numpy-bestand
(.npy) dat mysterydevice.ipynb met alleen numpy kan inlezen.

Gebruik:
    python prepare_image.py mijn_cijfer.png
-> schrijft 'mijn_cijfer.npy' (28x28) weg, die je in mysterydevice.ipynb kunt laden.
"""
import sys
import numpy as np
from PIL import Image


def png_naar_npy(png_pad, npy_pad=None):
    """Laadt een afbeelding, zet om naar 28x28 grijswaarden en slaat op als .npy."""
    if npy_pad is None:
        npy_pad = png_pad.rsplit(".", 1)[0] + ".npy"

    img = Image.open(png_pad).convert("L")      # naar grijswaarde
    img = img.resize((28, 28))                   # naar 28x28
    arr = np.array(img, dtype=np.uint8)          # 28x28 array, waarden 0-255

    np.save(npy_pad, arr)
    print(f"Opgeslagen: {npy_pad}  (shape {arr.shape}, dtype {arr.dtype})")
    return npy_pad


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gebruik: python prepare_image.py <afbeelding.png>")
        sys.exit(1)
    png_naar_npy(sys.argv[1])
