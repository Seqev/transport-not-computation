#!/usr/bin/env python3
"""make_figures.py -- umbrella/review figures.
Numbers are the verified headline values from the constituent papers (each
reproduced from raw logs in its own repository); listed in NUMBERS below for
transparency. Run: python3 make_figures.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

FIG = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.titlesize": 9.5, "axes.labelsize": 9,
    "legend.fontsize": 7.5, "figure.dpi": 150})

# ---------------------------------------------------------------------------
# FIG 1 -- the program arc: four causal gates converging on one thesis.
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

def box(x, y, w, h, title, sub, fc):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.12",
                 fc=fc, ec="#33424f", lw=1.0))
    ax.text(x+w/2, y+h-0.30, title, ha="center", va="top", fontsize=8.6, fontweight="bold", color="#1b2a36")
    ax.text(x+w/2, y+h-0.74, sub, ha="center", va="top", fontsize=7.1, color="#33424f")

gates = [
    ("\u03b3  attention", "redirect a key's weight\n\u2192 TRANSPORT\n(re-delivery explains it)", "#dbe7f0"),
    ("delivery ladder", "is there a skill shortcut?\n\u2192 NO \u2014 fix is delivery\n(27-byte binding)", "#dbe7f0"),
    ("synthesis", "compose an ABSENT fact?\n\u2192 retrieval+elimination;\nCoT = self-delivery", "#dbe7f0"),
    ("latent scratchpad", "OPTIMIZE a latent state\n\u2192 answer-injection,\nnot composition", "#dbe7f0"),
]
xs = [0.15, 2.55, 4.95, 7.35]
for x, (t, s, c) in zip(xs, gates):
    box(x, 3.5, 2.25, 2.1, t, s, c)
    ax.add_patch(FancyArrowPatch((x+1.125, 3.5), (5.0, 2.05),
                 arrowstyle="-|>", mutation_scale=10, color="#7f8c8d", lw=0.9, alpha=0.8))

# thesis box
box(2.0, 0.25, 6.0, 1.6, "ONE THESIS (1B\u20133B, two families, cross-model)",
    "the network DELIVERS, and composes only through an EXTERNAL buffer;\n"
    "it does not latently COMPUTE \u2014 and a latent scratchpad cannot be optimized into existence",
    "#fbe9e7")
ax.text(5, 5.78, "Four independent causal gates, matched-controlled, pre-registered",
        ha="center", fontsize=8.4, style="italic", color="#555")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig1_arc.pdf")); fig.savefig(os.path.join(FIG, "fig1_arc.png"))
plt.close(fig)

# ---------------------------------------------------------------------------
# FIG 2 -- four gates, one signature. Each panel: the decisive contrast.
# Verified headline numbers from the constituent papers.
# ---------------------------------------------------------------------------
NUMBERS = {
 "gamma":   dict(labels=["weight-gain", "re-deliver"],            vals=[0.80, 1.00], note="re-delivery \u2265 weight-gain\n\u21d2 transport"),
 "ladder":  dict(labels=["27B binding", "bare code 9B"],          vals=[1.00, 0.58], note="the binding, not the code\nis the floor"),
 "synth":   dict(labels=["implicit", "CoT (control)"],            vals=[0.08, 0.87], note="middle hop used only\nwhen written (CoT)"),
 "latent":  dict(labels=["code REMOVED\nfloor", "composition\nwould need"], vals=[0.88, 0.0], note="carries the answer\nwithout the chain"),
}
titles = {"gamma":"\u03b3: attention", "ladder":"delivery ladder",
          "synth":"synthesis (mid-hop use)", "latent":"latent scratchpad (C1)"}
order = ["gamma","ladder","synth","latent"]
cols = ["#7f8c8d","#1b6ca8"]
fig, axes = plt.subplots(1, 4, figsize=(8.4, 2.5))
for ax, key in zip(axes, order):
    d = NUMBERS[key]
    bars = ax.bar([0,1], d["vals"], color=cols, width=0.62)
    for b, v in zip(bars, d["vals"]):
        ax.text(b.get_x()+b.get_width()/2, v+0.03, f"{v:.2f}", ha="center", va="bottom", fontsize=7.5)
    ax.set_xticks([0,1]); ax.set_xticklabels(d["labels"], fontsize=6.8)
    ax.set_ylim(0, 1.5); ax.set_title(titles[key], fontsize=8.2, pad=18)
    ax.text(0.5, 1.34, d["note"], ha="center", va="top", transform=ax.transData,
            fontsize=6.4, color="#c0392b")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    if key != "gamma": ax.set_yticklabels([])
axes[0].set_ylabel("recovery / usage / floor")
fig.suptitle("Four gates, one signature: delivery, not computation", fontsize=9.5, y=1.04)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig2_signature.pdf"), bbox_inches="tight")
fig.savefig(os.path.join(FIG, "fig2_signature.png"), bbox_inches="tight")
plt.close(fig)
print("figures written:", sorted(os.listdir(FIG)))
