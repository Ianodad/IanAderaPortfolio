#!/usr/bin/env python3
"""
WCAG contrast checker for the Receipts design tokens.
Converts OKLCH -> OKLab -> linear sRGB -> relative luminance -> contrast ratio.
No dependencies beyond the standard library.
"""

import math

# ---- OKLCH -> sRGB -----------------------------------------------------

def oklch_to_oklab(L, C, H):
    h_rad = math.radians(H)
    a = C * math.cos(h_rad)
    b = C * math.sin(h_rad)
    return L, a, b


def oklab_to_linear_srgb(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b

    l = l_ ** 3
    m = m_ ** 3
    s = s_ ** 3

    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b_ = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return r, g, b_


def linear_to_srgb_channel(c):
    c = max(0.0, min(1.0, c))
    if c <= 0.0031308:
        return 12.92 * c
    return 1.055 * (c ** (1 / 2.4)) - 0.055


def oklch_to_srgb(L, C, H):
    ol, a, b = oklch_to_oklab(L, C, H)
    r, g, bl = oklab_to_linear_srgb(ol, a, b)
    return tuple(linear_to_srgb_channel(ch) for ch in (r, g, bl))


def relative_luminance(rgb):
    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast_ratio(rgb1, rgb2):
    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


# ---- Alpha compositing over a ground color -----------------------------

def composite(fg_rgb, alpha, bg_rgb):
    return tuple(fg * alpha + bg * (1 - alpha) for fg, bg in zip(fg_rgb, bg_rgb))


# ---- Tokens (DESIGN.md) -------------------------------------------------

TOKENS = {
    "paper":        (0.965, 0.012, 78),
    "paper-2":      (0.935, 0.016, 78),
    "ink":          (0.23, 0.018, 60),
    "ink-2":        (0.45, 0.02, 60),
    "oxide":        (0.53, 0.165, 38),
    "oxide-deep":   (0.44, 0.145, 38),
    "oxide-tint":   (0.92, 0.04, 45),
    "on-oxide":     (0.975, 0.012, 78),
    "on-oxide-dim": (0.93, 0.03, 70),
}

RGB = {name: oklch_to_srgb(*vals) for name, vals in TOKENS.items()}

# rule token carries alpha; composite over paper and oxide separately
RULE_L, RULE_C, RULE_H, RULE_A = 0.23, 0.018, 60, 0.16
rule_fg = oklch_to_srgb(RULE_L, RULE_C, RULE_H)
RGB["rule-on-paper"] = composite(rule_fg, RULE_A, RGB["paper"])
RGB["rule-on-oxide-band"] = composite(rule_fg, RULE_A, RGB["oxide"])

# rule-on-oxide token (on-oxide at 0.4 alpha), composited over oxide
RULE_OX_A = 0.4
RGB["rule-on-oxide"] = composite(RGB["on-oxide"], RULE_OX_A, RGB["oxide"])

# Pairs actually used on the page: (label, fg, bg, size_class)
PAIRS = [
    ("ink on paper (body text)",              "ink", "paper", "normal"),
    ("ink on paper-2 (career body)",          "ink", "paper-2", "normal"),
    ("ink-2 on paper (secondary/intro text)", "ink-2", "paper", "normal"),
    ("ink-2 on paper-2 (career receipt/eyebrow)", "ink-2", "paper-2", "normal"),
    ("oxide on paper (index numbers, >=48px)", "oxide", "paper", "large"),
    ("oxide-deep on paper (verify links, body size)", "oxide-deep", "paper", "normal"),
    ("oxide-deep on paper-2 (ledger date labels)", "oxide-deep", "paper-2", "normal"),
    ("oxide-deep on oxide-tint (status chip)", "oxide-deep", "oxide-tint", "normal"),
    ("on-oxide on oxide (hero lead, contact heading, buttons text)", "on-oxide", "oxide", "normal"),
    ("on-oxide-dim on oxide (receipt labels, small)", "on-oxide-dim", "oxide", "normal"),
    ("oxide-deep on paper (btn text, contact ground fill = paper)", "oxide-deep", "paper", "normal"),
]

FLOORS = {"normal": 4.5, "large": 3.0}


def main():
    print(f"{'Pair':55s} {'Ratio':>8s}  {'Floor':>6s}  Result")
    print("-" * 90)
    worst = None
    for label, fg, bg, size in PAIRS:
        ratio = contrast_ratio(RGB[fg], RGB[bg])
        floor = FLOORS[size]
        ok = ratio >= floor
        status = "PASS" if ok else "FAIL"
        print(f"{label:55s} {ratio:8.2f}  {floor:6.1f}  {status}")
        if worst is None or ratio < worst[1]:
            worst = (label, ratio)

    print("-" * 90)
    print(f"Lowest ratio: {worst[0]} = {worst[1]:.2f}:1")

    # Non-text UI contrast (hairlines, decorative -- informational only, no floor enforced)
    print()
    print("Non-text reference (informational, no WCAG text floor applies):")
    r1 = contrast_ratio(RGB["rule-on-paper"], RGB["paper"])
    r2 = contrast_ratio(RGB["rule-on-oxide-band"], RGB["oxide"])
    r3 = contrast_ratio(RGB["rule-on-oxide"], RGB["oxide"])
    print(f"  rule hairline on paper:   {r1:.2f}:1")
    print(f"  rule hairline on oxide (unmixed --rule): {r2:.2f}:1 (not used; oxide sections use --rule-on-oxide instead)")
    print(f"  rule-on-oxide (dotted leader / border) on oxide: {r3:.2f}:1")


if __name__ == "__main__":
    main()
