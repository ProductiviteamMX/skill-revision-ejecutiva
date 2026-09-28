#!/usr/bin/env python3
"""Contraste WCAG de uno o más colores contra un fondo.

Uso: contraste.py "#0C1947,#00BBCE,#ED5F18" --fondo "#FBFAF6"
Umbrales: 4.5 texto normal, 3.0 texto grande o marcas de gráficas.
"""
import sys


def lum(hexc):
    hexc = hexc.lstrip("#")
    rgb = [int(hexc[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    fondo = "#FFFFFF"
    if "--fondo" in args:
        i = args.index("--fondo")
        fondo = args[i + 1]
        args = args[:i] + args[i + 2:]
    for c in args[0].split(","):
        r = ratio(c.strip(), fondo)
        estado = "texto OK" if r >= 4.5 else ("solo marcas/texto grande" if r >= 3 else "FALLA")
        print(f"{c.strip()} sobre {fondo}: {r:.2f}:1  {estado}")
