# __The QED Piece: One Charge Matrix and the Charge Table It Fixes__

## Introduction

**The claim.** The electromagnetic interaction contributes one row to the forty-seven. The row contains every charged field in the content, and it contains them through one matrix $Q$ whose entries are fixed by the hypercharges. The matrix is not a parameter: it is a table, and the table is the charge assignment of the twelve species.

**The answer.**

$$
\boxed{\;\mathcal{L}_{\mathrm{QED}}=-e\sum_{\psi}\bar\psi\gamma^\mu Q_\psi\psi\,A_\mu\;,\qquad Q=\mathrm{diag}\Bigl(\tfrac23,\tfrac23,\tfrac23,-\tfrac13,-\tfrac13,-\tfrac13,-1,-1,-1,0,0,0\Bigr)\;}
$$

**Why one row and not twelve.** The piece is one monomial with one coupling and one matrix. The twelve species enter as the entries of the matrix, and a reader who writes twelve separate terms has written the same row expanded. The first convention of [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html) folds the sum.

**The standing.** The piece is standard and the charge assignment is the content's. What this article adds is the statement that the matrix fixes the table, that the table has no free entry once the hypercharges are fixed, and that the row therefore costs one constant and not twelve.

## The Piece

**Written out.**

$$
\mathcal{L}_{\mathrm{QED}}=-e\sum_{\psi}\bar\psi\,\gamma^\mu Q_\psi\,\psi\,A_\mu ,
$$

with $\psi$ running over the twelve species and $Q_\psi$ the entry of the charge matrix for that species.

**The charge table.**

| Species | $T_3$ | $Y$ | $Q=T_3+Y$ |
|---|---|---|---|
| $u,c,t$ | $+\tfrac12$ | $+\tfrac16$ | $+\tfrac23$ |
| $d,s,b$ | $-\tfrac12$ | $+\tfrac16$ | $-\tfrac13$ |
| $e,\mu,\tau$ | $-\tfrac12$ | $-\tfrac12$ | $-1$ |
| $\nu_e,\nu_\mu,\nu_\tau$ | $+\tfrac12$ | $-\tfrac12$ | $0$ |

**The rule behind the table.** $Q=T_3+Y$, with $T_3$ the weak isospin of the left-handed component and $Y$ the hypercharge. The table is what the assignment produces, and every entry is a rational number fixed by the two columns on its left.

**Why the matrix is diagonal.** The photon couples to the charge and the charge is a property of the species; no charged current flows through the photon at tree level, because the photon is neutral. A flavour-changing photon coupling would need an off-diagonal entry in $Q$, and $Q$ is diagonal in the mass basis by construction.

## What the Table Fixes

**The charges of the composite states.** A proton is $uud$, so its charge is $\tfrac23+\tfrac23-\tfrac13=+1$; a neutron is $udd$, so $\tfrac23-\tfrac13-\tfrac13=0$. The neutrality of the hydrogen atom is then the statement that the electron's $-1$ cancels the proton's $+1$, and it follows from the same table.

**The anomaly conditions.** The sum of the charges over a generation, weighted by colour and by chirality, vanishes. The table is not arbitrary: a different assignment would produce a triangle anomaly and the theory would not be renormalisable. The condition is a constraint on the content and not a piece of the list.

**The relation to the weak couplings.** $e=g\sin\theta_W$. The QED coupling is not independent of the two unbroken ones; it is the combination that survives the rotation, which is why the row costs one constant and not a new pair. [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) places $e$ among the eighteen.

**The charge of the $W$.** The $W$ carries $\pm1$, and its coupling to the photon is not in this row: it is a triple gauge vertex inside the field strength, counted among the six vertices of [The Gauge Self-Interactions](the-gauge-self-interactions-two-triple-vertices-and-four-quartic-vertices.html). The distinction is the same one the census makes everywhere: a fermion–fermion–photon structure is a row, and a three-gauge structure is a vertex.

## What the Row Does Not Fix

**It does not fix the masses.** The charge matrix is flavour-blind within a charge class: $u$, $c$ and $t$ have the same entry, and the row cannot tell them apart. The masses are nine separate rows from the Yukawa term.

**It does not fix the mixing.** The photon coupling is diagonal in the mass basis, so there is no electromagnetic analogue of $V_{\mathrm{CKM}}$. A reader who expects a mixing matrix in QED is expecting the charged current's structure in a place where the gauge field is neutral.

**It does not fix $e$'s value.** The row carries the symbol and not the number; the value is a measurement and belongs to [The Data Boundary](the-data-boundary.html).

## Checks

1. The row count. One row for twelve species.
2. The matrix. Diagonal, with four distinct entries.
3. The entries. $\tfrac23$, $-\tfrac13$, $-1$, $0$, from $Q=T_3+Y$.
4. The proton. $\tfrac23+\tfrac23-\tfrac13=+1$.
5. The neutron. $\tfrac23-\tfrac13-\tfrac13=0$.
6. The neutrino. $Q=0$, so no photon coupling.
7. The coupling. $e=g\sin\theta_W$, one constant and not a new pair.
8. The $W$. Its photon coupling is a triple vertex and not a row.
9. The flavour blindness. The entry depends on the charge class and not on the mass.
10. The anomalies. The charge sums cancel per generation, which is a constraint on the content.

## Summary

QED is one row of the forty-seven: one monomial with one coupling $e$ and one diagonal matrix $Q$. The matrix's entries are the charge table, and the table is fixed by $Q=T_3+Y$ once the hypercharges are assigned.

The row fixes the charges of the composite states — the proton's $+1$ and the neutron's $0$ are sums of three entries — and it satisfies the anomaly conditions, which are constraints on the content rather than pieces of the list. The coupling is not independent: $e=g\sin\theta_W$, which is why the row costs one constant.

The row is flavour-blind and diagonal, so it fixes no mass and no mixing. The photon's coupling to the $W$ is a triple gauge vertex and belongs with the other five structures of that kind.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q$ | The charge matrix, diagonal in the mass basis |
| $T_3$ | Weak isospin of the left-handed component |
| $Y$ | Hypercharge |
| $e$ | The electromagnetic coupling, $g\sin\theta_W$ |
| twelve species | six quarks, three charged leptons, three neutrinos |

## Further Reading

- [The Charge Theorem](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html). Where the charge assignment comes from.
- [The Neutral-Current Piece](the-neutral-current-piece-two-coefficient-tables-and-the-two-zeros-that-are-not-the-same.html). The same table read through the $Z$.
- [The Replacement of the Derivative](the-replacement-of-the-derivative-five-blocks-and-nothing-else.html). Where the row comes from.
- [The Gauge Self-Interactions](the-gauge-self-interactions-two-triple-vertices-and-four-quartic-vertices.html). The $\gamma W^+W^-$ vertex, which is not this row.
- [The Data Boundary](the-data-boundary.html). The value of $e$.
