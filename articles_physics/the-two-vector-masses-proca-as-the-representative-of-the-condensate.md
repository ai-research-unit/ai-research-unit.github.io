# __The Two Vector Masses: Proca as the Representative of the Condensate__

## Introduction

**The claim.** Two pieces of the list give the vector fields their masses,

$$
\mathcal{L}_{\mathrm{mass},V}=-M_W^2W^+_\mu W^{-\mu}-\tfrac12M_Z^2Z_\mu Z^\mu ,
$$

and these two are the only rows of the forty-nine with no counterpart in the invariant enumeration of the unbroken theory. They are not added terms. They are what the scalar kinetic piece becomes when the scalar sits at its minimum, written in the gauge in which the Goldstones are zero.

**The answer.**

$$
\boxed{\;M_W=\tfrac12gv,\qquad M_Z=\tfrac12\sqrt{g^2+g_{\mathrm Y}^2}\,v=\frac{M_W}{\cos\theta_W}\;}
$$

**Why the qualification matters.** The corpus argues, in [One Obstruction, Four Groups](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html), that a mass term for a connection is never an invariant term. That argument is correct and it is not contradicted here. What changes is the representative: the same theory written around the vacuum has a mass term in it, and the term is the residue of a piece that is invariant.

**The standing.** The Proca term, its equation and its three polarisations are standard. The corpus's own reading is [The Lagrangian and the W and Z Bosons](the-lagrangian-and-the-w-and-z-bosons.html), and the expansion that produces the two masses is [Electroweak Symmetry Breaking](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html). This article's subject is the status of the two rows, not their derivation.

## The Two Pieces

**Written out.**

$$
\mathcal{L}_{\mathrm{mass},V}=-M_W^2\,W^+_\mu W^{-\mu}-\tfrac12\,M_Z^2\,Z_\mu Z^\mu .
$$

**The factor of two is the reality of the neutral field.** $W^+_\mu W^{-\mu}$ is the modulus squared of one complex field and carries a coefficient of one; $Z_\mu Z^\mu$ is the square of one real field and carries $\tfrac12$. The same factor appears in the kinetic pieces and in the propagators, and [The Higgs–Vector Pieces](the-hvv-pieces-two-mass-term-normalisations-two-couplings-and-the-photon-that-does-not-appear.html) shows how it is absorbed when the two $hVV$ couplings are written as $2M_V^2/v$.

**Why the photon and the gluon have no such row.** Their masses are zero. A piece $M_\gamma^2A_\mu A^\mu$ would break the $U(1)_{\mathrm{em}}$ that the photon gauges, and a piece $M_g^2G^a_\mu G^{a\mu}$ would break colour. The two zeros are the statement that the vacuum is neutral under both groups.

## The Obstruction and Its Resolution

**The obstruction, restated in one line.** Under a gauge transformation the connection shifts by a derivative, $\delta A_\mu=\partial_\mu\alpha$, so $\delta(A_\mu A^\mu)=2A^\mu\partial_\mu\alpha$, which is not zero and is not a total derivative unless $\partial\cdot A=0$. A mass term therefore cannot be invariant.

**The resolution, restated in one line.** The mass term is not in the invariant Lagrangian. It is in the expansion of $-\sum_\mu(D_\mu H)^\dagger(D_\mu H)$ about $H=(0,(v+h)/\sqrt2)$, and the field that would have made it non-invariant — the Goldstone — has been removed by the gauge choice.

**The two statements are one statement.** In a general gauge the mass term is accompanied by the mixing term $M_W\partial_\mu G^+W^{-\mu}$ and by the Goldstone's own kinetic term, and the combination is invariant. In unitary gauge the mixing term and the Goldstone are gone and the mass term stands alone, which is why it looks like a Proca term added by hand.

**What a reader should not conclude.** That the two rows are exceptions to the audit of [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). The audit is of the unbroken expression, where these two rows do not appear. The broken expression has them because it is a different basis for the same function.

## The Proca Equation and the Constraint

**The variation.** Varying $W^+_\mu$ in the two pieces plus its kinetic piece gives

$$
\partial_\nu W^{+\nu\mu}+M_W^2W^{+\mu}=0 ,
$$

and taking the divergence gives $M_W^2\partial_\mu W^{+\mu}=0$, so $\partial\cdot W^+=0$. The constraint is what reduces four components to three.

**Three polarisations, and where the third came from.** A massless vector has two transverse polarisations. The constraint removes the longitudinal one when $M=0$ and permits it when $M\ne0$. The permitted one is the Goldstone mode, and the count $2\to3$ is the count of the eaten scalar.

**Why the equation has no gauge invariance left.** The Proca equation is not invariant under $W_\mu\mapsto W_\mu+\partial_\mu\alpha$; the mass term breaks it. That is not a defect of the broken description. It is the statement that the gauge symmetry is realised non-linearly, with the Goldstone absorbed.

## The Masses Are One Number and One Angle

**Two masses from three constants.**

$$
M_W=\tfrac12gv,\qquad M_Z=\tfrac12\sqrt{g^2+g_{\mathrm Y}^2}\,v,
\qquad
\frac{M_W^2}{M_Z^2}=\frac{g^2}{g^2+g_{\mathrm Y}^2}=\cos^2\theta_W .
$$

**The ratio is the content.** The two masses are not independent. One vacuum value and one angle fix both, and the ratio is $1$ in the variable $\rho=M_W^2/(M_Z^2\cos^2\theta_W)$, which is the tree-level custodial relation of [Custodial Symmetry and the Rho Parameter](custodial-symmetry-and-the-rho-parameter.html).

**What the framework does not supply.** Neither $g$ nor $v$ nor $\theta_W$. The three are imported, and the two masses are three constants in two combinations.

## Checks

1. The count. Two rows, numbered 48 and 49 in the display, and the only two outside the forty-seven.
2. The dimensions. $M_W^2W^+W^-$ has dimension four: $2+1+1$.
3. The factor of two. $W^+W^-$ is a modulus squared, $Z^2$ is a square, and the kinetic pieces carry the same $\tfrac12$ against $-\tfrac14$.
4. The constraint. The divergence of the Proca equation gives $\partial\cdot W=0$ for $M\ne0$.
5. The polarisation count. $2\to3$ per massive vector, and the third is the eaten Goldstone.
6. The ratio. $M_W^2/M_Z^2=\cos^2\theta_W$, recomputed from the two relations.
7. The invariance test. $\delta(M^2W_\mu W^\mu)=2M^2W^\mu\partial_\mu\alpha\ne0$, so the piece is not invariant on its own.
8. The audit's consistency. The two rows are absent from the unbroken list, which is why [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html) excludes $V_\mu V^\mu$ for $\gamma$ and $G^a$ and admits it for $W$ and $Z$ only through the scalar kinetic term.
9. The lineage. Both rows descend from $-\sum_\mu(D_\mu H)^\dagger(D_\mu H)$, as [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html) tabulates.

## Summary

The two vector mass pieces are $-M_W^2W^+_\mu W^{-\mu}$ and $-\tfrac12M_Z^2Z_\mu Z^\mu$. They are unitary-gauge images of the scalar kinetic term and not additions to the invariant Lagrangian, and their presence in the broken list does not contradict the statement that no gauge mass is an invariant term.

The factor of two between them is the difference between a complex field and a real one, and it propagates into the $hVV$ couplings, the propagators and the polarisation sums.

The Proca equation follows from the two pieces and the kinetic one, and its divergence gives the constraint $\partial\cdot W=0$, which is what reduces four components to three. The third polarisation is the Goldstone mode, and its appearance is the degree-of-freedom count of the breaking.

The two masses are functions of three constants: $M_W=gv/2$ and $M_Z=M_W/\cos\theta_W$. Their ratio is the tree-level custodial relation, and the framework supplies none of the three constants.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_W$, $M_Z$ | The two vector masses |
| $v$ | The vacuum value |
| $g$, $g_{\mathrm Y}$, $\theta_W$ | The couplings and the mixing angle |
| $\rho$ | $M_W^2/(M_Z^2\cos^2\theta_W)$, equal to one at tree level |
| $G^\pm$, $G^0$ | The Goldstones, set to zero in unitary gauge |

## Further Reading

- [One Obstruction, Four Groups: The Gauge Mass That Is Never Admitted](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html). The argument that the mass term is not an invariant, which this article reconciles with the Proca row.
- [The Lagrangian and the W and Z Bosons](the-lagrangian-and-the-w-and-z-bosons.html). The action and the Proca equation derived from it.
- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Vector-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html). The expansion that produces the two masses.
- [Custodial Symmetry and the Rho Parameter](custodial-symmetry-and-the-rho-parameter.html). The ratio of the two masses.
- [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html). The lineage of the two rows.
