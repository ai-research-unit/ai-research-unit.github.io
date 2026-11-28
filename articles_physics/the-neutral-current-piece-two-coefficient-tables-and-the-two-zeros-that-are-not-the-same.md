# __The Neutral-Current Piece: Two Coefficient Tables and the Two Zeros That Are Not the Same__

## Introduction

**The claim.** The list has one neutral-current row,

$$
\mathcal{L}_{\mathrm{NC}}=-\frac{g}{\cos\theta_W}\sum_f\bar f\gamma^\mu\Bigl(T_3^f\frac{1-\gamma_5}{2}-Q_f\sin^2\theta_W\Bigr)f\,Z_\mu ,
$$

one row for all twelve species, and two coefficient tables inside it, one for the vector coupling and one for the axial. Its two zeros are not the same kind of zero. The photon's zero is definitional: the neutrino's charge is zero, so its vector coupling equals its axial coupling. The other is content: the right-handed neutrino is absent, so the right-handed axial current has no field to be built from.

**The answer.**

$$
\boxed{\;c^f_V=T^f_3-2Q_f\sin^2\theta_W,\qquad c^f_A=T^f_3,\qquad 12+9=21\;}
$$

**Why one row and not twelve.** The twelve species share one coefficient and one operator structure; they differ only in the two numbers $T_3$ and $Q$. A row is a term with a definite field content and a definite coefficient, and the coefficient here is the common $g/\cos\theta_W$. The species dependence is carried by the quantum numbers inside the sum.

**The standing.** The piece is standard and the corpus's own line is $\frac{\sin\theta_{\mathrm W}}{\cos\theta_{\mathrm W}}QdP_\gamma+\frac{1}{\cos\theta_{\mathrm W}}T_3dZ$ in [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). This article derives the $1/\cos\theta_W$, tabulates the two couplings, and separates the two zeros from the one near-zero.

## The Piece and Its Coefficient

**Written out.**

$$
-\frac{g}{\cos\theta_W}\sum_f\bar f\gamma^\mu\Bigl(T_3^f\frac{1-\gamma_5}{2}-Q_f\sin^2\theta_W\Bigr)f\,Z_\mu .
$$

**Where $1/\cos\theta_W$ comes from, in three lines.** In the unbroken basis the neutral couplings are $gW^3_\mu T_3+g_{\mathrm Y}B_\mu Y$, with $Y=Q-T_3$ and $g_{\mathrm Y}=g\tan\theta_W$. Substituting $W^3=\cos\theta_WZ+\sin\theta_WA$ and $B=-\sin\theta_WZ+\cos\theta_WA$ and collecting the $Z$ terms,

$$
g\cos\theta_WT_3-\frac{g\sin^2\theta_W}{\cos\theta_W}(Q-T_3)=\frac{g}{\cos\theta_W}\Bigl[T_3(\cos^2\theta_W+\sin^2\theta_W)-Q\sin^2\theta_W\Bigr],
$$

and the identity $\cos^2\theta_W+\sin^2\theta_W=1$ collapses the bracket to $T_3-Q\sin^2\theta_W$.

**The identity is the whole derivation.** The $Z$ coupling is not a new coupling; it is the $T_3$ coupling divided by $\cos\theta_W$, and the division is what the sum of the two squares produces. The same identity is why the photon coupling is $Q$ and nothing else.

**The $A$ terms cancel in the same step.** Collecting the $A$ terms of the same substitution gives $g\sin\theta_WT_3+g_{\mathrm Y}\cos\theta_WY=g\sin\theta_W(T_3+Q-T_3)=g\sin\theta_WQ$, which is $eQ$ after the identification $e=g\sin\theta_W$. The photon's coupling is the charge and nothing else, and [The Photon Piece](the-photon-as-the-unbroken-mixture.html) writes it.

## The Two Couplings per Species

**Vector and axial, in one line.**

$$
T_3\frac{1-\gamma_5}{2}-Q\sin^2\theta_W=\frac12\Bigl[\bigl(T_3-2Q\sin^2\theta_W\bigr)-T_3\gamma_5\Bigr],
$$

so with the convention $\mathcal{L}\supset-\frac{g}{2\cos\theta_W}\bar f\gamma^\mu(c_V-c_A\gamma_5)fZ_\mu$ the two numbers are $c_V=T_3-2Q\sin^2\theta_W$ and $c_A=T_3$.

| Species | $T_3$ | $Q$ | $c_V$ | $c_A$ |
|---|---|---|---|---|
| $\nu_L$ | $+\tfrac12$ | $0$ | $+\tfrac12$ | $+\tfrac12$ |
| $e_L$, $\mu_L$, $\tau_L$ | $-\tfrac12$ | $-1$ | $-\tfrac12+2\sin^2\theta_W$ | $-\tfrac12$ |
| $u_L$, $c_L$, $t_L$ | $+\tfrac12$ | $+\tfrac23$ | $\tfrac12-\tfrac43\sin^2\theta_W$ | $+\tfrac12$ |
| $d_L$, $s_L$, $b_L$ | $-\tfrac12$ | $-\tfrac13$ | $-\tfrac12+\tfrac23\sin^2\theta_W$ | $-\tfrac12$ |
| all right-handed | $0$ | as charged | $-2Q\sin^2\theta_W$ | $0$ |

**Two entries per Dirac species and one per right-handed fermion.** The table separates the two chiral components because they carry different quantum numbers: a Dirac field is not one entry in this table but two, and its right-handed half has no axial coupling. The distinction is the reason the neutral current is not simply proportional to the charge.

## The Two Zeros and the One Near-Zero

**First zero, and it is content: $c_A=0$ for right-handed fields.** $T_3$ vanishes on a right-handed field, so the axial coupling vanishes and the right-handed neutral current is purely vector. For the charged fermions this is a consequence of their being singlets; for the neutrino it is a consequence of the field not existing at all. There is no right-handed neutrino, so there is no right-handed neutrino current to have a coupling.

**Second zero, and it is definitional: $c_V=c_A$ for the neutrino.** The neutrino has $Q=0$, so the vector coupling equals the axial coupling and the combination $(1-\gamma_5)$ survives as a whole. This is the photon's zero read through the $Z$: the same entry of the charge matrix that removes the photon coupling removes the neutrino's vector coupling, and the equality is a rewriting of $Q=0$.

**The count.** Twelve left-handed species and nine right-handed ones, since the three neutrinos have no right-handed partner, so twenty-one independent numbers. That is the count of the independent currents of [The Twelve Fermion Kinetic Pieces](the-twelve-fermion-kinetic-pieces-nine-massive-species-three-neutrinos-and-their-currents.html), and the agreement is not a coincidence: the same bilinears are being counted.

**The near-zero that is not a zero.** For the electron, $c_V=-\tfrac12+2\sin^2\theta_W\approx-0.038$, which is small because $\sin^2\theta_W\approx0.23$ is close to $\tfrac14$. A reader who sees a number of order $10^{-2}$ will look for a symmetry that would make it zero and will not find one; the smallness is an accident of the measured angle. The measurement of parity violation in electron scattering is the measurement of this coefficient, and it is a measurement of $\sin^2\theta_W$ and not of a cancellation.

## Checks

1. The count. One row, and it is the twenty-ninth of the forty-seven.
2. The coefficient. $g/\cos\theta_W$, from $\cos^2+\sin^2=1$.
3. The photon. $g\sin\theta_WQ=eQ$, the same substitution.
4. The two couplings. $c_V=T_3-2Q\sin^2\theta_W$ and $c_A=T_3$.
5. The first zero. $c_A$ vanishes for right-handed fields because $T_3=0$.
6. The second zero. $c_V=c_A$ for the neutrino because $Q=0$.
7. The count of numbers. $12+9=21$: one per left-handed species and one per right-handed species, the same as the count of currents.
8. The electron. $c_V^e=-0.5+2(0.231)=-0.038$, small and not zero.
9. The absence of a $Z\gamma$ mixing piece. The $A$ terms collect to $eQ$ and mix with nothing, so the neutral current is diagonal in the mass basis.
10. The dimension. $\bar ffZ$ has dimension four, and the coefficient carries none.

## Summary

The neutral current is one row, with the common coefficient $g/\cos\theta_W$, and it carries two couplings per species: $c_V=T_3-2Q\sin^2\theta_W$ and $c_A=T_3$.

The $1/\cos\theta_W$ is not a new coupling. It is what the $T_3$ coupling becomes when the two neutral connections are rotated, and the identity $\cos^2\theta_W+\sin^2\theta_W=1$ is the whole of the derivation. The same substitution gives the photon coupling $eQ$.

Two zeros are structural. Right-handed fields have no axial coupling, because they have no weak isospin; and the neutrino has equal vector and axial couplings, because it has no charge, so its neutral current is purely left-handed. The three foldings leave twenty-one independent numbers, the same as the count of independent currents.

The near-zero of the electron's vector coupling is not a zero. It is small because the measured angle is close to the value that would make it vanish, and the measurement of parity violation in electron scattering is a measurement of the angle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c_V$, $c_A$ | The vector and axial couplings of a species |
| $T_3$ | Weak isospin, $+\tfrac12$ or $-\tfrac12$ for left-handed fields and zero for right-handed ones |
| $Q$ | Electric charge in units of $e$ |
| $\sin^2\theta_W$ | The mixing parameter, $0.231$ in the $\overline{\mathrm{MS}}$ scheme |

## Further Reading

- [The Photon as the Unbroken Mixture](the-photon-as-the-unbroken-mixture.html). The same substitution's $A$ part.
- [The Charged-Current Pieces](the-charged-current-piece-two-terms-one-ckm-matrix-one-purely-left-vertex.html). The companion, and why it is two rows.
- The Gauge Bosons and the Neutral Current. The $Z$ as the carrier.
- [Electroweak Precision Observables](electroweak-precision-observables-the-oblique-parameters-s-t-u.html). The measurements that fix $\sin^2\theta_W$.
