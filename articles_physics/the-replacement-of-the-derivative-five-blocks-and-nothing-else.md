# __The Replacement $\partial\to D$: Five Blocks and Nothing Else__

## Introduction

**The claim.** Replacing the ordinary derivative by the covariant one is the operation that produces every interaction in the list. Applied to the broken content it produces five blocks and nothing else: QCD, QED, the charged current, the neutral current, and the scalar's derivative block. The five blocks contain nine rows, and the other thirty-eight rows of the forty-seven come from the field strengths, the fermion kinetic terms, the potential and the Yukawa terms.

**The answer.**

$$
\boxed{\;9=\underbrace{1}_{\text{QCD}}+\underbrace{1}_{\text{QED}}+\underbrace{2}_{\text{CC}}+\underbrace{1}_{\text{NC}}+\underbrace{4}_{|DH|^2},\qquad 47=38+9\;}
$$

**Why the five and not four.** The scalar's derivative block is the fifth, and it is the one a reader is most likely to forget: $|D_\mu H|^2$ produces the two $hVV$ rows and the two $hhVV$ rows, and those four rows are interactions in exactly the sense the other five are. A count that names only QCD, QED and the two weak currents is counting the derivative on the fermions and forgetting it on the scalar.

**The standing.** The replacement is standard. The corpus's own version is the line $\partial\to\partial+igA$ in [The Standard Model and the Lagrangian](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html). What this article adds is the enumeration of what the replacement produces, and the statement of what it does not.

## One Derivative, One Connection per Factor

**The replacement, before and after the rotation.**

$$
\partial_\mu\;\longrightarrow\;D_\mu=\partial_\mu-ig_sG^a_\mu T^a-igW^a_\mu T^a-ig_{\mathrm Y}B_\mu Y ,
$$

and in the mass basis, with $W^3=\cos\theta_WZ+\sin\theta_WA$ and $B=-\sin\theta_WZ+\cos\theta_WA$,

$$
D_\mu=\partial_\mu-ig_sG^a_\mu T^a-ieQA_\mu-i\frac{g}{\cos\theta_W}\Bigl(T_3-Q\sin^2\theta_W\Bigr)Z_\mu-i\frac{g}{\sqrt2}\bigl(T_+W^+_\mu+T_-W^-_\mu\bigr).
$$

**Each term in the derivative is one block.** Colour gives QCD, charge gives QED, the ladder gives the charged current, the diagonal combination gives the neutral current. The scalar carries the same derivative and its block is the fifth.

**The two couplings that are one.** $e=g\sin\theta_W$ and $g_{\mathrm Y}=g\cos\theta_W$ are not extra entries: they are the two unbroken couplings written in the rotated basis, and the replacement is the same replacement. [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) states the map.

## The Five Blocks

**Block by block, with the rows it produces.**

| Block | Acted on | Rows | Coefficient |
|---|---|---|---|
| QCD | quarks | $1$ | $g_s$ |
| QED | every charged field | $1$ | $e$ |
| charged current | left-handed doublets | $2$ | $g/\sqrt2$ |
| neutral current | every fermion | $1$ | $g/\cos\theta_W$ |
| scalar derivative | $H$ | $4$ | $g$, $g_{\mathrm Y}$, $v$ |

**Why the charged current is two rows and the others one.** The quark term carries the mixing matrix and the lepton term does not, so the two terms have different coefficients and are two pieces. The other three blocks each have one coefficient for all species, so each is one row with a sum inside it.

**Why the scalar block is four rows.** The square $(v+h)^2$ has three levels and two vectors: the linear level gives $hWW$ and $hZZ$, the quadratic gives $hhWW$ and $hhZZ$, and the constant level gives the two Proca masses, which are the rows outside the forty-seven.

**The nine rows and their pieces.** QCD, QED, the two charged currents, the neutral current, $hWW$, $hZZ$, $hhWW$ and $hhZZ$. Those are the nine, and they are exactly the rows whose coefficient carries a coupling rather than a mass.

## What the Replacement Does Not Produce

**The absences are as informative as the presences.** Each is a statement about a quantum number of the broken content.

| Absent | Why |
|---|---|
| a gluon–photon coupling | the gluon is electrically neutral, $Q=0$ on the adjoint of colour |
| a gluon–$Z$ coupling | the same: $T_3=0$ and $Q=0$ on a colour octet |
| a photon–neutrino coupling | the neutrino is neutral, $Q=0$ |
| a right-handed charged current | there is no $\nu_R$, and the ladder acts only on left-handed doublets |
| a flavour-changing neutral current | $T_3$ and $Q$ are diagonal in the mass basis |
| an $hAA$ or $hZ\gamma$ row | the photon is the combination that annihilates the vacuum |

**The first three are one statement.** A gauge field couples only to the quantum number it gauges, and a field that carries none of it does not couple. The gluon gauges colour, so it couples to colour and to nothing else; the photon gauges charge, so it couples to charge and to nothing else.

**The fourth is a statement about the content.** The charged current is purely left-handed because the only right-handed fields in the content are colour triplets and charged-lepton singlets, and neither carries the weak isospin that the ladder needs. [The Charged-Current Piece](the-charged-current-piece-two-terms-one-ckm-matrix-one-purely-left-vertex.html) states the consequence for the vertex.

**The fifth is a statement about the basis.** The replacement is written in the mass basis, where the neutral generators are diagonal. In a general flavour basis there would be off-diagonal entries, and the rotation that diagonalises the masses is the same rotation that removes them; this is why the neutral current is diagonal and the charged current is not.

## Why Nothing Else

**Every other row of the forty-seven comes from a different ancestor.** The four field strengths give the four kinetic rows; the fermion kinetic term gives twelve; the potential gives the scalar mass and the two self-pieces; the Yukawa term gives nine masses and nine $h\bar ff$. None of them involves the replacement.

**The count in one line.** $47=38+9$, where the thirty-eight are $4+12+1+1+1+1+9+9$: four curvatures, twelve fermion kinetics, the $h$ kinetic, the $h$ mass, the two self-pieces, nine masses and nine $h\bar ff$.

**A reader who wants a sixth block will find it in a different derivative.** A second scalar doublet would give a charged-current block on the scalars; a right-handed neutrino would give a neutral-current block on it; a colour-octet fermion would give a different QCD representation. The five blocks are five because the content has five kinds of charge carrier.

## Checks

1. The block count. Five: QCD, QED, charged current, neutral current, scalar derivative.
2. The row count. $1+1+2+1+4=9$.
3. The complement. $47-9=38$, and the thirty-eight are accounted for by the other four ancestors.
4. The charged current. Two rows, because the quark term carries $V_{\mathrm{CKM}}$ and the lepton term does not.
5. The scalar block. Four rows, from the linear and quadratic levels of $(v+h)^2$.
6. The Proca rows. Two more from the constant level, outside the forty-seven.
7. The couplings. $e=g\sin\theta_W$ and $g_{\mathrm Y}=g\cos\theta_W$, a change of basis and not a new number.
8. The gluon. No photon coupling and no $Z$ coupling, because $Q=0$ and $T_3=0$ on a colour octet.
9. The neutrino. No photon coupling, because $Q=0$; a $Z$ coupling, because $T_3=\tfrac12$ on the left-handed field.
10. The neutral current. Diagonal in the mass basis, because the same rotation diagonalises the masses and the neutral generators.

## Summary

The replacement of the derivative by the covariant derivative produces five blocks: QCD from colour, QED from charge, the charged current from the ladder, the neutral current from the diagonal combination, and the scalar's four rows from $|D_\mu H|^2$. It produces nine rows, and the other thirty-eight rows of the forty-seven come from the field strengths, the fermion kinetic terms, the potential and the Yukawa terms.

The absences are statements about quantum numbers. The gluon carries colour and no charge, so it does not couple to the photon or the $Z$. The neutrino carries no charge, so it does not couple to the photon. The right-handed fields carry no weak isospin, so the charged current is purely left-handed. The neutral generators are diagonal in the mass basis, so there is no flavour-changing neutral current.

A sixth block would need a sixth kind of charge carrier, and the content does not have one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D_\mu$ | The covariant derivative, with one connection per gauge factor |
| $T^a$ | The colour generators, $a=1,\dots,8$ |
| $T_\pm$ | The weak ladder operators |
| five blocks | QCD, QED, charged current, neutral current, scalar derivative |
| $47=38+9$ | Pieces with and without the replacement |

## Further Reading

- [The QCD Piece](the-qcd-piece-eight-generators-three-colours-one-coupling.html). Block one in full.
- [The QED Piece](the-qed-piece-one-charge-matrix-and-the-charge-table-it-fixes.html). Block two in full.
- [The Charged-Current Piece](the-charged-current-piece-two-terms-one-ckm-matrix-one-purely-left-vertex.html). Block three, and why it is two rows.
- [The Neutral-Current Piece](the-neutral-current-piece-two-coefficient-tables-and-the-two-zeros-that-are-not-the-same.html). Block four, and its two zeros.
- [The $hVV$ Pieces](the-hvv-pieces-two-mass-term-normalisations-two-couplings-and-the-photon-that-does-not-appear.html). Block five's linear level.
- [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html). Where the forty-seven comes from.
