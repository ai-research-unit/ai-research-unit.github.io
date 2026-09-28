
# __Comparison of the Polar Element Representation__

## Introduction

This article compares the polar representation of the eight algebras $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$. It states the polar decomposition of an element into a modulus and a unit factor, the number of factors of the parametrisation and the group each factor carries, the positive scale, the elliptic, hyperbolic and parabolic phases, the hyperbolic rotation and the rotor, the domain of the decomposition and its boundary, and the place of each algebra in the definite and the indefinite polar series, in tables with the eight algebras as columns in the fixed order of *The Eight Algebras Compared*. Every entry restates a result of the eight polar representation articles cited in the explanations. The article stops at the decomposition of an element: the norm itself and the group of units are the subject of *Comparison of Norms and Invertibility*, and the exponential of the unit factor and the Lie group structure of the group of units are the subject of *Comparison of the Exponential and Lie Group Structure*.

The organising thread is the **number and the character of the factors**. Every element of non-vanishing norm is written $a=\rho u$ with a positive modulus $\rho$ and a unit factor $u$, but the unit factor splits further: it is discrete in $\mathbb{R}$, circular in $\mathbb{C}$, a sphere in $\mathbb{H}$, a hyperbola or a shear in the split cases, and a product of a central phase, a hyperbolic rotation in the Hermitian subspace and a rotor in $\mathbb{B}$. The columns divide into the **definite polar series** $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$, whose unit factor carries a compact rotor, and the **indefinite polar series** $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$, whose unit factor carries a non-compact hyperbolic or parabolic factor.

## The Polar Parametrisation

The following table compares the polar parametrisation of the eight algebras: the modulus, the unit factor, the number of factors, the domain of the decomposition and the series to which the algebra belongs. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| modulus | $\lvert x\rvert$ | $\sqrt{N}$ | $\sqrt{\lvert N\rvert}$ | $\lvert a\rvert$ | $\sqrt{N}$ | $\sqrt{\lvert N\rvert}$ | $\sqrt{\lvert N\rvert}$ | $\rho_\pm=\lvert A\pm A'\rvert$, scale $\lambda=\sqrt{\rho_+\rho_-}$ |
| unit factor | $\{\pm1\}$ | $U(1)$ | $\{N=\pm1\}$ | $1+\mathrm{M}$ | $Sp(1)$ | $\{N=\pm1\}$ | $U(1)\cdot B_+\cdot Sp(1)$ | $e^{j\tau}\cdot(S^3\times S^3)$ |
| number of factors | $2$ | $2$ | $2$ | $2$ | $2$ | $2$ | $4$ | $2$ |
| domain | $\mathbb{R}\setminus\{0\}$ | $\mathbb{C}\setminus\{0\}$ | $N\neq0$ | $a\neq0$ | $\mathbb{H}\setminus\{0\}$ | $N\neq0$ | $N\neq0$ | all elements |
| series | definite | definite | indefinite | indefinite | definite | indefinite | definite | indefinite |

The table records the two-factor shape of the decomposition in seven columns and its sharpening in the eighth. The modulus is the square root of the norm — the absolute value of it when the form is indefinite — and it is positive real except in $\mathbb{B}$, where the norm is complex-valued, and in $\mathbb{H}_{\mathbb{D}}$, where it is the pair $\rho_\pm=\lvert A\pm A'\rvert$ of the idempotent components whose geometric mean is the positive scale $\lambda$ (*Real Polar Element Representation*; *Complex Polar Element Representation*; *Split-Complex Polar Element Representation*; *Dual-Numbers Polar Element Representation*; *Quaternion Polar Element Representation*; *Split-Quaternion Polar Element Representation*; *Biquaternion Polar Element Representation*; *Split-Biquaternion Polar Element Representation*). The unit factor is the set of elements of unit modulus; the decomposition $a=\rho u$ exists exactly on the elements of non-vanishing norm, so its domain is the complement of the origin in $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, the complement of the null cone in $\mathbb{D}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$, the complement of the maximal ideal in $\mathbb{D}'$, and the whole algebra in $\mathbb{H}_{\mathbb{D}}$, whose modulus needs no branch and whose decomposition exists for every element (*Split-Biquaternion Polar Element Representation*, §*The Theorem*). The number of factors is two in seven columns; $\mathbb{B}$ is the one column with four factors, the scale, the central phase, the hyperbolic rotation in the Hermitian subspace and the rotor, and $\mathbb{H}_{\mathbb{D}}$ has the two factors of the central modulus and the rotor, the scale and the hyperbolic phase together forming the central factor (*Biquaternion Polar Element Representation*, §*Why Four Factors*; *Split-Biquaternion Polar Element Representation*, §*Why Two Factors*). The columns divide into the definite series $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$ and the indefinite series $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$.

## The Factors and Their Groups

The following table compares the factor groups of the polar decomposition of the eight algebras: the positive scale, the elliptic, hyperbolic and parabolic phases, the hyperbolic rotation and the rotor. The eight algebras are the columns, in the fixed order, with the marker **—** where a factor does not occur.

| factor | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| scale | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ |
| elliptic phase | — | $U(1)$ | — | — | — | — | $U(1)$ | — |
| hyperbolic phase | — | — | $e^{\phi j}$ | — | — | — | — | $e^{j\tau}$ |
| parabolic phase | — | — | — | $1+\mathrm{M}$ | — | — | — | — |
| hyperbolic rotation | — | — | — | — | — | yes | yes | — |
| rotor | $\{\pm1\}$ | — | — | — | $Sp(1)$ | $S^1$ | $Sp(1)$ | $S^3\times S^3$ |

The table shows how the four slots of the family are occupied. The positive scale $\mathbb{R}_{>0}$ is present in every column, and the factors that carry the compact topology are the phases and the rotors. In the definite series the rotor is compact: the discrete sign group $\{\pm1\}$ in $\mathbb{R}$, the circle $U(1)$ in $\mathbb{C}$, the sphere $Sp(1)=S^3$ in $\mathbb{H}$; and $\mathbb{B}$ carries, besides its compact central phase $e^{i\alpha}$ and its compact rotor $Sp(1)$, a non-compact **hyperbolic rotation** in the Hermitian subspace $\mathbb{M}_+$ of real dimension three, so that its four factors have dimensions $1+1+3+3=8$ (*Real Polar Element Representation*, §*What the Two Factors Are*; *Complex Polar Element Representation*, §*What the Two Factors Are*; *Quaternion Polar Element Representation*, §*The Modulus and the Unit Factor*; *Biquaternion Polar Element Representation*, §*The Four Factors and Their Meanings*). The hyperbolic rotation of $\mathbb{B}$ is the one occurrence of a hyperbolic rotation in the definite series, and it is present because the complex norm of $\mathbb{B}$ is indefinite while its Hermitian scalar part is positive definite.

In the indefinite series the unit factor is genuinely non-compact. The split complex algebra has a hyperbolic unit factor $e^{\phi j}$ and no elliptic one, because it has no root of $-1$; the dual numbers have the parabolic factor $1+\mathrm{M}=\{1+s\varepsilon\}$, a shear with a globally defined angle; the split quaternions have a hyperbolic rotation in $\operatorname{span}\{1,e_2,e_3\}$ together with a one-parameter rotor $S^1$ from the elliptic direction $e_1$ and a discrete reflection component; and the split biquaternions have a rotor $S^3\times S^3$ of dimension six in place of a hyperbolic rotation and a central hyperbolic phase $e^{j\tau}$, the scale and the phase being the two components of the split complex modulus (*Split-Complex Polar Element Representation*, §*Position and Signature*; *Dual-Numbers Polar Element Representation*, §*The Factors and Their Meanings*; *Split-Quaternion Polar Element Representation*, §*The Polar Decomposition*; *Split-Biquaternion Polar Element Representation*, §*The Factors and Their Meanings*). The split biquaternion column is the only one whose polar data has no hyperbolic rotation, and it is the only column whose decomposition exists on the whole algebra, the rotor alone degenerating on the zero divisors.

## Summary

Every element of non-vanishing norm has a polar decomposition $a=\rho u$ into a modulus and a unit factor, and the modulus is the square root of the norm — its absolute value when the form is indefinite, and a pair of real absolute values in $\mathbb{H}_{\mathbb{D}}$. The decomposition has two factors in seven columns and four in $\mathbb{B}$, the scale, the central phase, the hyperbolic rotation in the Hermitian subspace and the rotor; in $\mathbb{H}_{\mathbb{D}}$ the two factors are the central modulus, whose scale and hyperbolic phase are the components of the split complex modulus, and the rotor $S^3\times S^3$. The factor groups are the positive scale $\mathbb{R}_{>0}$, present in every column, the elliptic phase $U(1)$ of $\mathbb{C}$ and $\mathbb{B}$, the hyperbolic phase $e^{\phi j}$ of $\mathbb{D}$ and $e^{j\tau}$ of $\mathbb{H}_{\mathbb{D}}$, the parabolic phase $1+\mathrm{M}$ of $\mathbb{D}'$, the hyperbolic rotation of $\mathbb{H}_{\mathrm{s}}$ and of $\mathbb{B}$, and the rotor, discrete in $\mathbb{R}$, the circle $S^1$ in $\mathbb{H}_{\mathrm{s}}$ and the sphere $Sp(1)$ or the product $S^3\times S^3$ in $\mathbb{H}$, $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$. The decompositions fall into the definite series $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$ and the indefinite series $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$, and only the last column has the whole algebra as its domain.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\rho$ | the modulus of the polar decomposition |
| $\lambda$ | the positive scale of $\mathbb{H}_{\mathbb{D}}$, $\sqrt{\rho_+\rho_-}$ |
| $u$ | the unit factor of the decomposition |
| $\rho_\pm=\lvert A\pm A'\rvert$ | the two idempotent components of the modulus of $\tilde Q=A+jA'$ |
| $U(1),Sp(1)=S^3$ | the compact phase of $\mathbb{C}$ and $\mathbb{B}$, and the compact rotor of $\mathbb{H}$ and $\mathbb{B}$ |
| $e^{\phi j},e^{j\tau}$ | the hyperbolic phase of $\mathbb{D}$ and of $\mathbb{H}_{\mathbb{D}}$ |
| $1+\mathrm{M}$ | the parabolic phase of $\mathbb{D}'$, $\mathrm{M}=(\varepsilon)$ |
| $B_+$ | the Hermitian positive subspace of $\mathbb{B}$ carrying the hyperbolic rotation |
| $S^1$ | the rotor of $\mathbb{H}_{\mathrm{s}}$ from the elliptic direction $e_1$ |
| $N$ | the norm of the algebra |
| `—` | an empty cell, stated and never filled |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the polar decomposition of a matrix and its uniqueness on the invertible elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the polar forms of the low-dimensional real algebras and their indefinite refinements.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the modulus, the unit factor and the norm-one group of a quaternion algebra.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the compact subgroups and the exponential parametrisation of an element.
