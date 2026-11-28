# __The Charged-Current Piece: Two Terms, One CKM Matrix, One Purely Left Vertex__

## Introduction

**The claim.** The charged current is one block with two terms and not one term,

$$
\mathcal{L}_{\mathrm{CC}}=-\frac{g}{\sqrt2}\Bigl(\bar u_{L}\gamma^\mu V_{\mathrm{CKM}}d_{L}\,W^+_\mu+\bar\nu_{L}\gamma^\mu e_{L}\,W^+_\mu\Bigr)+\mathrm{h.c.}
$$

The two share a coupling and a purely left-handed vertex, and they differ in everything else: the first carries colour and the mixing matrix, the second carries neither. The census counts them as two rows, because a row is a term with its own coefficient, and the coefficient of the quark term carries $V_{\mathrm{CKM}}$.

**The answer.**

$$
\boxed{\;\text{two rows},\qquad \text{one coupling }\frac{g}{\sqrt2},\qquad \text{one mixing matrix in the quark row alone}\;}
$$

**Why two and not one.** A single piece would need one coefficient for both currents and one mixing matrix for both, and neither is available. The quark current is a colour triplet and the lepton current is a colour singlet; they couple to the same vector but they are different operators, and the sum of two operators with one coefficient is two rows.

**The standing.** Both pieces are standard, the corpus's own form is $\rho W^+_{\tilde\mu}d\tilde q$ and its conjugate in The Weak Interaction in Biquaternionic Form, and the mixing matrix is [The CKM Matrix and CP Violation](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). What this article explains is why the matrix appears in one row and not in the other.

## The Two Pieces

**Written out.**

$$
-\frac{g}{\sqrt2}\bar u_{L}\gamma^\mu V_{\mathrm{CKM}}d_{L}W^+_\mu+\mathrm{h.c.},
\qquad
-\frac{g}{\sqrt2}\bar\nu_{L}\gamma^\mu e_{L}W^+_\mu+\mathrm{h.c.}
$$

**The coupling, and where each factor comes from.** The $W$ field is the combination $W^\pm=(W_1\mp iW_2)/\sqrt2$, which supplies $1/\sqrt2$, and the isospin ladder supplies $\tfrac12$. In the projector form the coefficient per chirality is therefore $g/(2\sqrt2)$, and since $\bar u_L\gamma^\mu d_L=\tfrac12\bar u\gamma^\mu(1-\gamma_5)d$, the left-handed form carries $g/\sqrt2$.

**The $V-A$ structure.** Both rows annihilate left-handed fields and create right-handed ones, which is the statement that the current is $\bar\psi_L\gamma^\mu\psi_L$ and that its conjugate is $\bar\psi_R\gamma^\mu\psi_R$. A vector current would be the sum of the two; the weak current is one of them.

**The conjugate is inside the piece.** The $+\mathrm{h.c.}$ doubles the field content and not the piece count. Writing the two terms separately would give four rows, and the census of [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) counts a term with its conjugate as one.

## Why the Mixing Matrix Appears in One Piece Only

**The quark sector has two rotations that do not cancel.** The mass-basis fields are obtained by rotating the up-type and down-type fields separately, and the $W$ couples an up-type field to a down-type one. The product of the two rotations is not the identity, and what survives is $V_{\mathrm{CKM}}$.

**The lepton sector has one rotation that is unphysical.** The neutrino is massless in this content, so its mass-basis field is defined only up to a rotation, and that rotation can be used to undo the charged lepton's. The leptonic mixing matrix is therefore absent, and the lepton piece is diagonal in the mass basis.

**What the difference costs.** The quark piece carries four parameters — three angles and one phase — and the lepton piece carries none. A reader who expects a symmetric treatment will look for a PMNS matrix in the second piece and will not find one; its absence is a consequence of the masslessness of the neutrinos and not an omission.

**Where the matrix would go.** If the three neutrinos had Dirac masses, a leptonic matrix would appear in the second piece exactly as the quark matrix appears in the first, with four parameters for three generations. [The Nine Dirac Masses](the-nine-dirac-masses-and-the-tenth-the-minimal-model-omits.html) prices that extension.

## The Interaction Count

**This piece is one of the five.** The fermion kinetic ancestor produces five interaction rows, and this article's two are two of them. The other three are the gluon, the photon and the $Z$ ones, and the split of the charged current into two is the reason the number is five and not four.

**Why the split is by colour and not by generation.** The colour is a property of the operator; the generation is an index on it. The quark piece carries both colour and generation indices, summed over both, and the second sum is contracted with $V_{\mathrm{CKM}}$, which is why one row carries nine numbers.

## Checks

1. The count. Two rows, the twenty-seventh and twenty-eighth of the forty-seven.
2. The coupling. $g/(2\sqrt2)$ per chirality in the projector form, which is $g/\sqrt2$ on the left-handed fields because $\bar u_L\gamma^\mu d_L=\tfrac12\bar u\gamma^\mu(1-\gamma_5)d$.
3. The dimension. $\bar\psi\gamma^\mu\psi W_\mu$ has dimension four.
4. The chirality. Left-handed fields only, and the conjugate couples right-handed ones.
5. The mixing. $V_{\mathrm{CKM}}$ in the quark piece and the identity in the lepton piece.
6. The parameters. Four in the quark piece, none in the lepton piece.
7. The colour. A triplet current in the first piece and a singlet in the second.
8. The conjugate. One row with its $\mathrm{h.c.}$, not two.
9. The interaction count. Two of the five fermion interaction rows.
10. The consistency with the content. Three left-handed neutrinos and no right-handed one, which is why the lepton piece is diagonal.

## Summary

The charged current is one block with two rows, one for quarks and one for leptons, both with the coupling $g/\sqrt2$ and the $V-A$ structure. The factor comes from the normalisation of the $W$ field and from the chiral projector, and it is the same in both rows.

The quark piece carries the CKM matrix and the lepton piece does not. The difference is that the up-type and down-type rotations do not cancel in the quark sector and the neutrino's rotation is unphysical in the lepton sector, because the neutrinos are massless in this content.

The two rows are two of the five interaction rows the fermion kinetic term produces. The split is by colour, and it is why the charged current contributes two rows where the neutral current contributes one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_{\mathrm{CKM}}$ | The quark mixing matrix, four parameters |
| $u_L$, $d_L$ | Up-type and down-type left-handed quark fields, colour triplets |
| $\nu_L$, $e_L$ | Neutrino and charged lepton left-handed fields, colour singlets |
| $g/\sqrt2$ | The coupling of the $(1-\gamma_5)$ structure |

## Further Reading

- The Weak Interaction in Biquaternionic Form. The corpus's form of the charged current.
- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The matrix and its four parameters.
- The Gauge Bosons and the Charged Current. The $W$ as the carrier.
- [The Neutral-Current Piece](the-neutral-current-piece-two-coefficient-tables-and-the-two-zeros-that-are-not-the-same.html). The companion piece, and the reason it is one row.
- [The $h\bar ff$ Pieces](the-hff-pieces-nine-couplings-fixed-by-nine-masses.html). The other place the mass-basis rotations leave a residue.
