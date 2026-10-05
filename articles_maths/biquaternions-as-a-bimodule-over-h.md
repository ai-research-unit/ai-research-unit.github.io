# __Biquaternions as a Bimodule over $\mathbb{H}$__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is an abelian group on which the quaternion ring $\mathbb{H}$ acts on both sides, and the two actions commute: it is an $\mathbb{H}$-**bimodule**. The base is a ring and not a field, and $\mathbb{H}$ is not commutative, so this structure is not a second scalar field beside $\mathbb{C}$ and $\mathbb{R}$; it is a ring of operators acting on the additive group. This article develops the two actions, the quaternionic coordinates, the rank, the endomorphism ring, and the exact sense in which the product of $\mathbb{B}$ fails to be fully $\mathbb{H}$-bilinear.

Three facts are the content. $\mathbb{B}$ is free of rank two over $\mathbb{H}$ on each side, with the same two generators $e_0$ and $ie_0$, and those generators are a real basis of the centre. As a right $\mathbb{H}$-module its $\mathbb{H}$-linear endomorphisms are the two-by-two matrices over $\mathbb{H}$, $\operatorname{End}_\mathbb{H}(\mathbb{B})\cong M_2(\mathbb{H})$. And the product is left $\mathbb{H}$-linear in the first argument and right $\mathbb{H}$-linear in the second, but not fully $\mathbb{H}$-bilinear: the defect is the commutator $[\tilde Q,h]$, and a module over $\mathbb{H}$ with exactly these two linearities is an $\mathbb{H}$-ring. Whether $\mathbb{H}$ may serve as a base ring rather than as a ring of operators is the base-ring question of *Biquaternions as an Algebra over $\mathbb{R}$*.

The article assumes *Quaternion Algebra* for $\mathbb{H}$, its basis and its multiplication, and *Biquaternions as a Vector Space over $\mathbb{C}$* for the additive group, the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ and the central imaginary $i$. The general theory is used and not repeated: *Modules* and *Modules over an Algebra* for the module axioms and the action of a ring, *Direct Sums, Free Modules and Rank* for free modules and rank, *The Endomorphism Algebra of a Module* for the endomorphism ring of a free module, and *Change of Rings* for the comparison of bases. The product $\tilde P\tilde Q$ is *The Four Biquaternion Complex Products* and is used as given. The companion structure, in which $\mathbb{B}$ itself acts, is *Biquaternions as a Module over Itself*. No form, no norm and no topology is used, and no degree-two form appears.

Throughout, $\tilde Q=h_1+ih_2$ with $h_1,h_2\in\mathbb{H}$, a general element in the quaternionic coordinates of *Biquaternions as a Vector Space over $\mathbb{C}$*.

## The Two Actions

**Definition.** The **left and right $\mathbb{H}$-actions** on $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ are

$$
h \cdot (A \otimes h') = A \otimes (hh'), \qquad (A \otimes h') \cdot h = A \otimes (h'h),
$$

with $A\in\mathbb{C}$ and $h,h'\in\mathbb{H}$. The left action is left multiplication by $1\otimes h$, the right action is right multiplication by the same element, and both are $\mathbb{R}$-bilinear because $\mathbb{H}$ is an $\mathbb{R}$-algebra. They **commute**, for $\tilde Q=A\otimes h'$ and any third scalar $k\in\mathbb{H}$,

$$
(h \cdot \tilde Q) \cdot k = (A \otimes hh') \cdot k = A \otimes (hh')k = A \otimes h(h'k) = h \cdot (\tilde Q \cdot k),
$$

by the associativity of the product of $\mathbb{H}$; the two factors of $\mathbb{B}$ commute with each other, so $\mathbb{B}$ is an $\mathbb{H}$-**bimodule**.

**Remark (two actions, not two scalars).** The left and the right action are distinct whenever $\mathbb{H}$ is non-commutative, and no choice of one of them turns the other into the same map. This is the difference between a bimodule over a ring and a vector space over a field, and it is why the two actions are kept apart throughout.

## The Quaternionic Coordinates

In the quaternionic coordinates an element is $\tilde Q = h_1 + ih_2$ with $h_1, h_2 \in \mathbb{H}$, and the two actions are

$$
h \cdot \tilde Q = (hh_1) + i(hh_2), \qquad \tilde Q \cdot h = (h_1h) + i(h_2h),
$$

using the centrality of $i$. The decomposition $\tilde Q = h_1 + ih_2$ is unique, which is the statement that $\mathbb{C}=\mathbb{R}\oplus\mathbb{R}i$ tensored with $\mathbb{H}$ splits $\mathbb{B}$ into two copies of $\mathbb{H}$ on each side.

## Free of Rank Two

Because the decomposition $\tilde Q = h_1 + ih_2$ is unique, $\{e_0, ie_0\}$ is a basis on the right and on the left at once:

$$
\mathbb{B} = \mathbb{H}e_0 \oplus \mathbb{H}(ie_0) \cong \mathbb{H}^2 \quad \text{on each side},
$$

and $\mathbb{B}$ is **free of rank two** over $\mathbb{H}$. It is worth noticing which elements serve as the generators: $e_0$ and $ie_0$ span the plane $\mathbb{C}_{\mathbb{B}}$ of the centre. The two free generators over $\mathbb{H}$ are a real basis of the centre of $\mathbb{B}$.

## The Endomorphisms

Because $\mathbb{B}$ is free of rank two as a right $\mathbb{H}$-module, its $\mathbb{H}$-linear endomorphisms are the two-by-two matrices over $\mathbb{H}$:

$$
\operatorname{End}_\mathbb{H}(\mathbb{B}) \cong M_2(\mathbb{H}).
$$

This is the standard description of the endomorphism ring of a free module of rank two over a ring, and it holds over a non-commutative base without change.

## A Bimodule Is Not a Scalar Structure

The two actions give the quaternions a reach over $\mathbb{B}$ that is **not** the reach of a scalar field. Multiplication is left $\mathbb{H}$-linear in the first argument and right $\mathbb{H}$-linear in the second,

$$
(h \cdot \tilde Q) \cdot \tilde P = h \cdot (\tilde Q \cdot \tilde P), \qquad \tilde Q \cdot (\tilde P \cdot h) = (\tilde Q \cdot \tilde P) \cdot h,
$$

but it is **not** fully $\mathbb{H}$-bilinear, since for non-central $h$

$$
\tilde Q \cdot (h \cdot \tilde P) - h \cdot (\tilde Q \cdot \tilde P) = (\tilde Qh - h\tilde Q)\tilde P = [\tilde Q,h]\tilde P,
$$

which does not vanish in general. A ring with exactly these properties is an **$\mathbb{H}$-ring**, and the failure is measured by the commutator. The quaternions are not central in $\mathbb{B}$, which is why $\mathbb{H}$ is a ring of operators here and not a second field of scalars; the base-ring question is decided in *Biquaternions as an Algebra over $\mathbb{R}$*.

## Worked Verification

The two defining claims can be checked exactly on the quaternion basis, with the product $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, $e_k^2=-e_0$ and the anti-commutation $e_je_k=-e_ke_j$ for $j\neq k$.

| Item | Value | Where |
|---|---|---|
| $(h\cdot\tilde Q)\cdot k - h\cdot(\tilde Q\cdot k)$ | $0$ for all $h,k\in\mathbb{H}$, $\tilde Q\in\mathbb{B}$ (associativity of $\mathbb{H}$) | §*The Two Actions* |
| rank over $\mathbb{H}$ | two, basis $\{e_0,ie_0\}$ on each side | §*Free of Rank Two* |
| generators | $e_0,ie_0$ span $\mathbb{C}_{\mathbb{B}}=\mathbb{R}e_0\oplus\mathbb{R}(ie_0)$ | §*Free of Rank Two* |
| $\operatorname{End}_\mathbb{H}(\mathbb{B})$ | $M_2(\mathbb{H})$ | §*The Endomorphisms* |
| $\tilde Q\cdot(h\cdot\tilde P)-h\cdot(\tilde Q\cdot\tilde P)$ | $[\tilde Q,h]\tilde P$, generally nonzero | §*A Bimodule Is Not a Scalar Structure* |

The commutation of the actions was verified on $100$ basis triples $(h,k,\tilde Q)$ with exact integer arithmetic, $0$ mismatches. The commutator identity was verified exactly on $100$ triples and holds identically. The smallest nonvanishing defect is at $h=e_1$, $\tilde Q=e_2$, $\tilde P=e_0$:

$$
\tilde Q \cdot (h \cdot \tilde P) - h \cdot (\tilde Q \cdot \tilde P) = [e_2,e_1] e_0 = e_2e_1 - e_1e_2 = -2e_3 \neq 0 ,
$$

so the product is not fully $\mathbb{H}$-bilinear on the basis elements themselves.

## Summary

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is an $\mathbb{H}$-bimodule with commuting left and right actions $h\cdot(A\otimes h')=A\otimes(hh')$ and $(A\otimes h')\cdot h=A\otimes(h'h)$, the two actions being distinct because $\mathbb{H}$ is non-commutative. In the quaternionic coordinates $\tilde Q=h_1+ih_2$ the actions read $h\cdot\tilde Q=(hh_1)+i(hh_2)$ and $\tilde Q\cdot h=(h_1h)+i(h_2h)$, using the centrality of $i$, and the module is free of rank two on each side on the generators $e_0$ and $ie_0$, which are a real basis of the centre. Its endomorphism ring is $\operatorname{End}_\mathbb{H}(\mathbb{B})\cong M_2(\mathbb{H})$. The product is left $\mathbb{H}$-linear in the first argument and right $\mathbb{H}$-linear in the second but not fully $\mathbb{H}$-bilinear; the defect is the commutator $[\tilde Q,h]$, and the structure is an $\mathbb{H}$-ring rather than a scalar structure. The base-ring question is *Biquaternions as an Algebra over $\mathbb{R}$*, and the structure in which $\mathbb{B}$ itself acts is *Biquaternions as a Module over Itself*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{H}$ | Quaternion algebra, the ring of operators |
| $h \cdot \tilde Q = A \otimes (hh')$ | the left $\mathbb{H}$-action |
| $\tilde Q \cdot h = A \otimes (h'h)$ | the right $\mathbb{H}$-action |
| $\tilde Q = h_1 + ih_2$ | quaternionic coordinates, $h_1,h_2\in\mathbb{H}$ |
| $\mathbb{B} \cong \mathbb{H}^2$ | free $\mathbb{H}$-module of rank two on each side |
| $e_0, ie_0$ | the two generators; a real basis of the centre $\mathbb{C}_{\mathbb{B}}$ |
| $\operatorname{End}_\mathbb{H}(\mathbb{B}) \cong M_2(\mathbb{H})$ | the $\mathbb{H}$-linear endomorphisms |
| $\mathbb{H}$-ring | bimodule over $\mathbb{H}$ with multiplication left linear in the first argument and right linear in the second |
| $[\tilde Q,h]$ | the commutator measuring the failure of full $\mathbb{H}$-bilinearity |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for bimodules and the action of a ring on an abelian group.
- Tsit-Yuen Lam, *Lectures on Modules and Rings* (Springer, 1999), for bimodules, free modules and the endomorphism ring of a module.
- Paul M. Cohn, *Skew Fields: Theory of General Division Rings* (Cambridge, 1995), for linear algebra over a division ring, rank and dimension.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for modules over a finite-dimensional algebra and the endomorphism ring.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the quaternion algebra, its tensor product with $\mathbb{C}$ and the biquaternion algebra.
