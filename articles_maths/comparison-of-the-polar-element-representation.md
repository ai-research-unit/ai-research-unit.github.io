
# __Comparison of the Polar Element Representation__

## Introduction

This article compares the polar representation of the eight algebras $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$. It states the polar decomposition of an element into a modulus and a unit factor, the number of factors of the parametrisation and the group each factor carries, the positive scale, the elliptic, hyperbolic and parabolic phases, the hyperbolic rotation and the rotor, the domain of the decomposition and its boundary, and the place of each algebra in the definite and the indefinite polar series, in tables with the eight algebras as columns in the fixed order of *The Eight Algebras Compared*. Every entry restates a result of the eight polar representation articles cited in the explanations. The article stops at the decomposition of an element: the norm itself and the group of units are the subject of *Comparison of Norms and Invertibility*, and the exponential of the unit factor and the Lie group structure of the group of units are the subject of *Comparison of the Exponential and Lie Group Structure*.

The organising thread is the **number and the character of the factors**. Every element of non-vanishing norm is written $a=\rho u$ with a positive modulus $\rho$ and a unit factor $u$, but the unit factor splits further: it is discrete in $\mathbb{R}$, circular in $\mathbb{C}$, a sphere in $\mathbb{H}$, a hyperbola or a shear in the split cases, and a product of a central phase, a hyperbolic rotation in the Hermitian subspace and a rotor in $\mathbb{B}$. The columns divide into the **definite polar series** $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$, whose unit factor carries a compact rotor, and the **indefinite polar series** $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$, whose unit factor carries a non-compact hyperbolic or parabolic factor.

**The symbols of the comparison.** Throughout, $e_0$ is the algebra unit of whichever algebra is in view, and the element is a name of that algebra.

- **The element.** $a \in \mathbb{R}$ (second coefficient $a' \in \mathbb{R}$ for $\mathbb{D}$), $A \in \mathbb{C}$, $\mathbb{D}$ or $\mathbb{D}'$, $\tilde q \in \mathbb{H}$ or $\mathbb{H}_{\mathrm{s}}$, $\tilde Q \in \mathbb{B}$ or $\mathbb{H}_{\mathbb{D}}$.
- **The generating units.** The quaternion units $e_1,e_2,e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$; the complex unit $i$ with $i^2 = -1$; the split-complex unit $j$ with $j^2 = +1$, central; and the nilpotent unit $\varepsilon$ with $\varepsilon^2 = 0$.
- **The norm.** $N$, the norm of the algebra in view: for $\mathbb{R}$ and $\mathbb{D}'$ the real form $a^2$, for $\mathbb{C}$ and $\mathbb{H}$ the definite form, for $\mathbb{D}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ the split or biquaternion form.
- **The polar factors.** The modulus $\rho > 0$ off the origin, and the unit factor $u$, of norm one for the definite forms and of norm $\pm1$ for the indefinite ones.
- **The $\mathbb{H}_{\mathbb{D}}$ column.** The letters $A,A' \in \mathbb{H}$ denote the quaternion and split-quaternion parts of $\tilde Q = A + jA'$, whose idempotent components are $\tilde\Pi_{1,2} = \tfrac12(1\pm j)$ and whose modulus components are $\rho_\pm = |A\pm A'|$.
- **The further symbols of the exponential table.** $\mu$, a unit pure quaternion (a root of $-e_0$ in $\mathbb{H}$); $\sigma \in \operatorname{span}\{e_2,e_3\}$; $\mu_\pm$, unit pure real quaternions, and $\theta_\pm \in \mathbb{R}$, the two rotation angles of $\mathbb{H}_{\mathbb{D}}$; $s \in R$, the shear parameter of $\mathbb{D}'$; and $B_+$, the set of unit boosts $\exp(\mathbb{M}_+\cap\{\text{traceless}\}) = H^3$.

The symbols are those of the eight polar articles and are defined there; the sets they carry are the columns of the tables.

## The Exponentials of the Factors

Every factor of every column is the exponential of an element of its algebra, and the eight columns are the eight readings of one rule. The reference word of the series, the four-factor biquaternion word, reads

$$
\tilde{Q} = \exp(\ln r)\,\exp(i\alpha)\,\exp\bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\bigr)\,\exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr) ,
$$

with the rapidity $\psi \in \mathbb{R}$, $\psi\ge0$, of the boost and its unit axis $\vec u_{\mathrm b} \in \mathcal{A}$ (the axis sphere, the unit vectors of $\mathbb{R}^3$), and the rotation angle $\theta \in [0,2\pi]$ of the rotor and its unit axis $\vec u_{\mathrm r} \in \mathcal{A}$; the other seven columns write their word the same way with as many exponentials as they have factors, and the number of the exponentials is the number of factors counted in the table below. For an element $\nu$ of the algebra in view and a real $t \in \mathbb{R}$, the series $\exp(\nu t)=\sum_{n\ge0}\nu^nt^n/n!$ collapses according to the square of $\nu$:

$$
\exp(\nu t) =
\begin{cases}
\cos t\,e_0 + \nu\sin t , & \nu^2 = -e_0 , \\
e_0 + \nu t , & \nu^2 = 0 , \\
\cosh t\,e_0 + \nu\sinh t , & \nu^2 = +e_0 .
\end{cases}
$$

The powers of $\nu$ repeat with period four in the trigonometric case, truncate at the second term in the parabolic case, and repeat with period two in the hyperbolic case. Each factor of each column writes its exponent as a parameter times a **root**, and the row that the root occupies is the topology of the factor: a root of $-e_0$ gives a compact factor, a root of $+e_0$ a non-compact one, and a nilpotent a parabolic one.

The following table writes the word of each algebra as a product of exponentials, together with the root of each exponent and its character. The scale is the same in every column, the hyperbolic exponential $\exp(\ln\rho)$ of the real unit; the other factors are the content of the algorithm row of each polar article.

| algebra | the word as exponentials | the root of the exponent and its row |
|---|---|---|
| $\mathbb{R}$ | $a = \exp(\ln\lvert a\rvert)\cdot(\pm e_0)$ | the scale has the hyperbolic unit $e_0$; the sign is **not** an exponential, since $\exp(\mathbb{R})=\mathbb{R}_{>0}$ misses $-1$ |
| $\mathbb{C}$ | $A = \exp(\ln\lvert A\rvert)\,\exp(i\theta)$ | the cosine root $i$, trigonometric |
| $\mathbb{D}$ | $A = \exp(\ln\sqrt{\lvert N\rvert})\cdot\bigl(\pm\exp(j\phi)\bigr)$ | the hyperbolic root $j$, hyperbolic; the sign is the discrete component |
| $\mathbb{D}'$ | $A = \exp(\ln\lvert a\rvert)\,\exp(\varepsilon s)$ | the nilpotent root $\varepsilon$, parabolic |
| $\mathbb{H}$ | $\tilde q = \exp(\ln\sqrt{N})\,\exp\bigl(\mu\tfrac{\theta}{2}\bigr)$ | the cosine root $\mu$, a unit pure quaternion, trigonometric |
| $\mathbb{H}_{\mathrm{s}}$ | $\tilde q = \exp(\ln\sqrt{\lvert N\rvert})\,\exp(\sigma)\cdot\bigl(\exp(\tfrac{\theta}{2} e_1)\bigr)\cdot(\text{optional } e_2)$ | the hyperbolic exponent $\sigma\in\operatorname{span}\{e_2,e_3\}$ and the cosine root $e_1$; the reflection $e_2$ is discrete |
| $\mathbb{B}$ | $\tilde Q = \exp(\ln r)\,\exp(i\alpha)\,\exp\bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\bigr)\,\exp\bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | the hyperbolic roots $e_0$ and $i\vec u_{\mathrm b}$, the cosine roots $i$ and $\vec u_{\mathrm r}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\tilde Q = \exp(\ln\lambda)\,\exp(j\tau)\,\exp\bigl(\tfrac{\theta_+}{2}\mu_+\tilde\Pi_1+\tfrac{\theta_-}{2}\mu_-\tilde\Pi_2\bigr)$ | the hyperbolic roots $e_0$ and $j$, the cosine roots $\mu_+\tilde\Pi_1$ and $\mu_-\tilde\Pi_2$ |

The table is the exponential reading of the two parametrisation tables. Three features of it are worth separating.

- **The scale is present in every column.** It is the one factor common to all eight columns, and it is the degenerate hyperbolic exponential, $\exp(\ln\rho)=\rho$.
- **The split algebras carry a factor that no exponential produces.** The sign group of $\mathbb{R}$ and the finite component of $\mathbb{D}$ and of $\mathbb{H}_{\mathrm{s}}$ are the boundary of the exponential, and the polar word keeps them as factors because the representation counts components and not only connected parameters.
- **Only $\mathbb{D}'$ occupies the parabolic row.** It does so because its unit factor is a shear $1+\varepsilon s$, which is $\exp(\varepsilon s)$ exactly by the truncation of the series.

The remaining columns occupy the trigonometric row for their compact factors and the hyperbolic row for their non-compact ones, and the count of the two rows is the count of the factors recorded in the two tables below.

**Two of the eight columns have exponents that do not commute.** In $\mathbb{B}$ the boost exponent and the rotor exponent fail to, and in $\mathbb{H}_{\mathrm{s}}$ the boost exponent and the rotation exponent fail to; in those two columns the order of the factors is part of the information, and the exponents may not be amalgamated into a single exponent. In the other six columns the exponents commute, so the order is free, and — the discrete signs and reflections of $\mathbb{R}$, $\mathbb{D}$ and $\mathbb{D}'$ excepted, these not being exponentials at all — the word is a single exponential. The six are the columns in which a non-scalar exponent is central or is the only non-scalar exponent of the word; the two are the columns in which two non-scalar exponents with a non-vanishing bracket occur together. Over $60$ random elements the largest coefficient of the bracket of the non-commuting exponents is $3.58$ in the biquaternion column and $6.59$ in the split-quaternion column, and in neither case does the sum rule hold.

## The Polar Parametrisation

The following table compares the polar parametrisation of the eight algebras: the modulus, the unit factor, the number of factors, the domain of the decomposition and the series to which the algebra belongs. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| modulus | $\lvert a\rvert$ | $\sqrt{N}$ | $\sqrt{\lvert N\rvert}$ | $\lvert a\rvert$ | $\sqrt{N}$ | $\sqrt{\lvert N\rvert}$ | $\sqrt{\lvert N\rvert}$ | $\rho_\pm=\lvert A\pm A'\rvert$, scale $\lambda=\sqrt{\rho_+\rho_-}$ |
| unit factor | $\{\pm1\}$ | $U(1)$ | $\{N=\pm1\}$ | $1+\mathrm{M}$ | $Sp(1)$ | $\{N=\pm1\}$ | $U(1)\cdot B_+\cdot Sp(1)$ | $\exp(j\tau)\cdot(\mathrm{Sp}(1)\times\mathrm{Sp}(1))$ |
| number of factors | $2$ | $2$ | $2$ | $2$ | $2$ | $2$ | $4$ | $2$ |
| domain | $\mathbb{R}\setminus\{0\}$ | $\mathbb{C}\setminus\{0\}$ | $N\neq0$ | $a\neq0$ | $\mathbb{H}\setminus\{0\}$ | $N\neq0$ | $N\neq0$ | all elements |
| series | definite | definite | indefinite | indefinite | definite | indefinite | definite | indefinite |

The table records the two-factor shape of the decomposition in seven columns and its sharpening in the eighth.

- **The modulus.** It is the square root of the norm — the absolute value of it when the form is indefinite — and it is positive real except in $\mathbb{B}$, where the norm is complex-valued, and in $\mathbb{H}_{\mathbb{D}}$, where it is the pair $\rho_\pm=\lvert A\pm A'\rvert$ of the idempotent components whose geometric mean is the positive scale $\lambda$ (*Real Polar Element Representation*; *Complex Polar Element Representation*; *Split-Complex Polar Element Representation*; *Dual-Numbers Polar Element Representation*; *Quaternion Polar Element Representation*; *Split-Quaternion Polar Element Representation*; *The Polar Element Representation of Biquaternions*; *Split-Biquaternion Polar Element Representation*).
- **The unit factor.** It is the set of **unit elements**, that is, of elements of norm one for the norm in view, up to the sign when the norm is indefinite (*Conventions in Mathematics*, §*The Unitary Convention*); it is not the **group of units**, which is the wider set of invertible elements treated in *Comparison of Norms and Invertibility*.
- **The domain.** The decomposition $a=\rho u$ exists exactly on the elements of non-vanishing norm, so its domain is the complement of the origin in $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, the complement of the null cone in $\mathbb{D}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$, the complement of the maximal ideal in $\mathbb{D}'$, and the whole algebra in $\mathbb{H}_{\mathbb{D}}$, whose modulus needs no branch and whose decomposition exists for every element (*Split-Biquaternion Polar Element Representation*, §*The Theorem*).
- **The number of factors** is two in seven columns. $\mathbb{B}$ is the one column with four factors, the scale, the central phase, the hyperbolic rotation in the Hermitian subspace and the rotor; $\mathbb{H}_{\mathbb{D}}$ has the two factors of the central modulus and the rotor, the scale and the hyperbolic phase together forming the central factor (*The Polar Element Representation of Biquaternions*; *Split-Biquaternion Polar Element Representation*, §*Why Two Factors*).
- **The series.** The columns divide into the definite series $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$ and the indefinite series $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$.

## The Factors and Their Groups

The following table compares the factor groups of the polar decomposition of the eight algebras: the positive scale, the elliptic, hyperbolic and parabolic phases, the hyperbolic rotation and the rotor. The eight algebras are the columns, in the fixed order, with the marker **—** where a factor does not occur.

| factor | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| scale | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ | $\mathbb{R}_{>0}$ |
| elliptic phase | — | $U(1)$ | — | — | — | — | $U(1)$ | — |
| hyperbolic phase | — | — | $\exp(\phi j)$ | — | — | — | — | $\exp(j\tau)$ |
| parabolic phase | — | — | — | $1+\mathrm{M}$ | — | — | — | — |
| hyperbolic rotation | — | — | — | — | — | yes | yes | — |
| rotor | $\{\pm1\}$ | — | — | — | $Sp(1)$ | $U(1)$ | $Sp(1)$ | $\mathrm{Sp}(1)\times\mathrm{Sp}(1)$ |

The table shows how the four slots of the family are occupied.

- **The positive scale $\mathbb{R}_{>0}$ is present in every column**, and the factors that carry the compact topology are the phases and the rotors.
- **In the definite series the rotor is compact**: the discrete sign group $\{\pm1\}$ in $\mathbb{R}$, the circle $U(1)$ in $\mathbb{C}$, and the sphere $Sp(1)=\{\tilde q\in\mathbb{H}:\tilde q\tilde q^{\natural}=1\}$ of unit real quaternions in $\mathbb{H}$.
- **$\mathbb{B}$ adds a non-compact factor.** Besides its compact central phase $\exp(i\alpha)$ and its compact rotor $Sp(1)$, it carries a non-compact **hyperbolic rotation** in the Hermitian subspace $\mathbb{M}_+$ of real dimension three, so that its four factors have dimensions $1+1+3+3=8$ (*Real Polar Element Representation*, §*What the Two Factors Are*; *Complex Polar Element Representation*, §*What the Two Factors Are*; *Quaternion Polar Element Representation*, §*The Modulus and the Unit Factor*; *The Polar Element Representation of Biquaternions*, §*The Scale*).

The hyperbolic rotation of $\mathbb{B}$ is the one occurrence of a hyperbolic rotation in the definite series, and it is present because the complex norm of $\mathbb{B}$ is indefinite while its Hermitian scalar part is positive definite.

In the indefinite series the unit factor is genuinely non-compact.

- **Split complex.** The unit factor is a hyperbolic $\exp(\phi j)$ and there is no elliptic one, because the algebra has no root of $-1$ (*Split-Complex Polar Element Representation*, §*Position and Signature*).
- **Dual numbers.** The unit factor is the parabolic $1+\mathrm{M}=\{1+s\varepsilon\}$, a shear with a globally defined angle (*Dual-Numbers Polar Element Representation*, §*The Factors and Their Meanings*).
- **Split quaternions.** The unit factor is a hyperbolic rotation in $\operatorname{span}\{1,e_2,e_3\}$, together with a one-parameter rotor $U(1)$ from the elliptic direction $e_1$ and a discrete reflection component (*Split-Quaternion Polar Element Representation*, §*The Polar Decomposition*).
- **Split biquaternions.** The unit factor is a rotor $\mathrm{Sp}(1)\times\mathrm{Sp}(1)$ of dimension six in place of a hyperbolic rotation, together with a central hyperbolic phase $\exp(j\tau)$, the scale and the phase being the two components of the split complex modulus (*Split-Biquaternion Polar Element Representation*, §*The Factors and Their Meanings*).

The split biquaternion column is the only one whose polar data has no hyperbolic rotation, and it is the only column whose decomposition exists on the whole algebra, the rotor alone degenerating on the zero divisors.

## Summary

Every element of non-vanishing norm has a polar decomposition $a=\rho u$ into a modulus and a unit factor, and the modulus is the square root of the norm — its absolute value when the form is indefinite, and a pair of real absolute values in $\mathbb{H}_{\mathbb{D}}$. The decomposition has two factors in seven columns and four in $\mathbb{B}$, the scale, the central phase, the hyperbolic rotation in the Hermitian subspace and the rotor; in $\mathbb{H}_{\mathbb{D}}$ the two factors are the central modulus, whose scale and hyperbolic phase are the components of the split complex modulus, and the rotor $\mathrm{Sp}(1)\times\mathrm{Sp}(1)$.

The factor groups are

- the positive scale $\mathbb{R}_{>0}$, present in every column;
- the elliptic phase $U(1)$ of $\mathbb{C}$ and $\mathbb{B}$;
- the hyperbolic phase $\exp(\phi j)$ of $\mathbb{D}$ and $\exp(j\tau)$ of $\mathbb{H}_{\mathbb{D}}$;
- the parabolic phase $1+\mathrm{M}$ of $\mathbb{D}'$;
- the hyperbolic rotation of $\mathbb{H}_{\mathrm{s}}$ and of $\mathbb{B}$;
- the rotor, discrete in $\mathbb{R}$, the circle $U(1)$ in $\mathbb{H}_{\mathrm{s}}$, and the sphere $Sp(1)$ or the product $\mathrm{Sp}(1)\times\mathrm{Sp}(1)$ in $\mathbb{H}$, $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$.

The decompositions fall into the definite series $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$ and the indefinite series $\mathbb{D}, \mathbb{D}', \mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$, and only the last column has the whole algebra as its domain.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\rho$ | the modulus of the polar decomposition |
| $\lambda$ | the positive scale of $\mathbb{H}_{\mathbb{D}}$, $\sqrt{\rho_+\rho_-}$ |
| $u$ | the unit factor of the decomposition |
| $\rho_\pm=\lvert A\pm A'\rvert$ | the two idempotent components of the modulus of $\tilde Q=A+jA'$ |
| $U(1)$ | the unit circle, the compact elliptic phase of $\mathbb{C}$ and $\mathbb{B}$ |
| $\mathrm{Sp}(1)=\{\tilde q\in\mathbb{H}:\tilde q\tilde q^{\natural}=1\}$ | the unit real quaternions, the compact rotor of $\mathbb{H}$ and $\mathbb{B}$ |
| $\exp(\phi j),\exp(j\tau)$ | the hyperbolic phase of $\mathbb{D}$ and of $\mathbb{H}_{\mathbb{D}}$ |
| $1+\mathrm{M}$ | the parabolic phase of $\mathbb{D}'$, $\mathrm{M}=(\varepsilon)$ |
| $B_+$ | the Hermitian positive subspace of $\mathbb{B}$ carrying the hyperbolic rotation |
| $U(1)$ | the rotor of $\mathbb{H}_{\mathrm{s}}$ from the elliptic direction $e_1$ |
| $N$ | the norm of the algebra |
| `—` | an empty cell, stated and never filled |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the polar decomposition of a matrix and its uniqueness on the invertible elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the polar forms of the low-dimensional real algebras and their indefinite refinements.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the modulus, the unit factor and the norm-one group of a quaternion algebra.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the compact subgroups and the exponential parametrisation of an element.
