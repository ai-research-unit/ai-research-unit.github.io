# __The Four Conjugations Are All $\mathbb{R}$-Linear__

## Introduction

The biquaternion algebra carries five distinguished maps: the identity, the quaternion conjugation $\natural$, the complex conjugation $\bar{\cdot}$, the Hermitian conjugation ${}^{*}$, and the reversal $\flat = -{}^{*}$. The last four are the **four conjugations**; the first four are the **four involutions**, the Klein four-group of *The Group of Involutions*. Over $\mathbb{C}$ these maps are of two kinds: some are $\mathbb{C}$-linear and the others are $\mathbb{C}$-antilinear, and the two kinds are not interchangeable there. Read over $\mathbb{R}$ the distinction disappears, because the conjugate of a real scalar is itself and the $\mathbb{C}$-antilinear maps become ordinary $\mathbb{R}$-linear maps like the rest. This article states that collapse precisely: it lists the five maps on the eight real coordinates, proves that all of them are $\mathbb{R}$-linear, and then divides them by their behaviour over $\mathbb{C}$, where the division is real and is read off from the commutator with the complex structure $J$.

The article owns the real-linear character of the maps. It does not define the conjugations, which are *Biquaternions as a Vector Space over $\mathbb{C}$*; it does not compute their fixed spaces, which are the remarkable subspaces (*Introduction to the Remarkable Subspaces*, *Comparison of the Remarkable Subspaces*); it does not prove the group laws, which are *The Group of Involutions*; and it does not treat the algebra automorphisms and derivations, which are *The Automorphisms and Derivations of the Real Biquaternion Algebra*. The complex structure $J$ is that of *Biquaternions as a Vector Space over $\mathbb{R}$*.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ over $\mathbb{R}$. A general element is $\tilde Q = \sum_\mu Q_\mu e_\mu$ with $Q_\mu = q_\mu + i q'_\mu$, and its eight real coordinates are
$$
(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3) .
$$
The complex structure is $J(\tilde Q) = i\tilde Q$, so that $J^2 = -\mathrm{id}$. A map is $\mathbb{C}$-**linear** if $T(\lambda\tilde Q) = \lambda\,T(\tilde Q)$ for all $\lambda \in \mathbb{C}$ and $\mathbb{C}$-**antilinear** if $T(\lambda\tilde Q) = \bar\lambda\,T(\tilde Q)$; over $\mathbb{R}$ both conditions reduce to $\mathbb{R}$-linearity, $T(r\tilde Q) = r\,T(\tilde Q)$ for $r \in \mathbb{R}$.

## The Five Maps on the Real Coordinates

**Definition.** On the complex coefficients the five maps act by
$$
(\tilde Q^{\mathrm{id}})_\mu = Q_\mu , \qquad
(\tilde Q^{\natural})_\mu = \varepsilon_\mu Q_\mu , \qquad
(\tilde Q^{*})_\mu = \varepsilon_\mu \bar Q_\mu , \qquad
(\bar{\tilde Q})_\mu = \bar Q_\mu , \qquad
(\tilde Q^{\flat})_\mu = -\varepsilon_\mu \bar Q_\mu ,
$$
where $\varepsilon = (1,-1,-1,-1)$ is the sign vector of the quaternion conjugation. Equivalently, on the eight real coordinates each is a signed permutation:

| map | $(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)\mapsto$ | order |
|---|---|---|
| $\mathrm{id}$ | $(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)$ | $1$ |
| ${}^{\natural}$ | $(q_0,-q_1,-q_2,-q_3,q'_0,-q'_1,-q'_2,-q'_3)$ | $2$ |
| $\bar{\cdot}$ | $(q_0,q_1,q_2,q_3,-q'_0,-q'_1,-q'_2,-q'_3)$ | $2$ |
| ${}^{*}$ | $(q_0,-q_1,-q_2,-q_3,-q'_0,q'_1,q'_2,q'_3)$ | $2$ |
| ${}^{\flat}$ | $(-q_0,q_1,q_2,q_3,q'_0,-q'_1,-q'_2,-q'_3)$ | $2$ |

The table is the coordinate form of the conjugations of *The Group of Involutions*, §*The Extra Involution*; here it is the starting point.

## All Five Are $\mathbb{R}$-Linear

**Theorem.** Each of the five maps is an $\mathbb{R}$-linear map $\mathbb{B} \to \mathbb{B}$, and as an operator on the eight-dimensional real space it is the diagonal matrix
$$
D_\sigma = \operatorname{diag}(\sigma_0,\sigma_1,\sigma_2,\sigma_3,\ \tau\sigma_0,\tau\sigma_1,\tau\sigma_2,\tau\sigma_3), \qquad \sigma_\mu = \pm 1,\ \tau = \pm 1 ,
$$
with the signs of the last four coordinates equal to those of the first four for $\mathrm{id}$ and ${}^{\natural}$ ($\tau = +1$), and opposite to them for $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat}$ ($\tau = -1$).

**Proof.** By the table, each map sends a coordinate to a coordinate or to its negative and never mixes coordinates: it is a signed permutation of the eight real coordinates. A signed permutation of the coordinates is additive, $T(x+y) = T(x)+T(y)$, and homogeneous over every real scalar, $T(rx) = rT(x)$ for $r \in \mathbb{R}$, because $\mathbb{R}$ is fixed by the sign changes. Hence each map is $\mathbb{R}$-linear, with the displayed diagonal matrix. $\square$

**Remark (why the complex reading distinguishes them).** Over $\mathbb{C}$ the same maps do not all satisfy $T(\lambda \tilde Q) = \lambda T(\tilde Q)$ for complex $\lambda$: the coordinate table uses complex conjugation, which is not the identity on $\mathbb{C}$, and it is exactly the maps with an odd number of bars in their definition that fail complex linearity. The real reading has no complex scalars to test, so the failure is invisible and all five maps are ordinary linear operators of an eight-dimensional real space.

### The Two Kinds of Linear Map as Operators

**Proposition.** Each of the five maps is invertible, with determinant $+1$, and each of the four nontrivial ones is a reflection with eigenvalues $+1$ and $-1$, each of multiplicity four. The group generated by ${}^{\natural}$ and ${}^{*}$ is the Klein four-group $\{\mathrm{id}, {}^{\natural}, \bar{\cdot}, {}^{*}\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, and ${}^{\flat} = -{}^{*}$ is an involution outside it.

**Proof.** A diagonal matrix $\operatorname{diag}(\pm 1)$ is its own inverse and has determinant the product of its signs. For each of the four nontrivial maps the table exhibits exactly four entries $+1$ and four entries $-1$, so the determinant is $(-1)^4 = +1$ and the eigenvalues are $+1$ and $-1$ with multiplicity four each. The group law is *The Group of Involutions*, §*The Group of Involutions*; the map $\flat = -{}^{*}$ is an involution whose products with the group elements introduce $-\mathrm{id}$, so it is not a member of the order-four group. $\square$

**Remark (the fixed spaces are the remarkable subspaces).** The eigenspace of $\pm 1$ for each of the four nontrivial maps is a fixed or anti-fixed subspace of real dimension four, and the eight labelled spaces reduce to the remarkable subspaces; the lattice is *Comparison of the Remarkable Subspaces*, and it is not restated here.

## $\mathbb{C}$-Linearity and the Commutator with $J$

The distinction between the two kinds of map is recovered, over the real reading, by a single operator.

**Theorem (the criterion).** Let $T$ be an $\mathbb{R}$-linear map of $\mathbb{B}$. Then $T$ is $\mathbb{C}$-linear if and only if $TJ = JT$, and $T$ is $\mathbb{C}$-antilinear if and only if $TJ = -JT$; here $J(\tilde Q) = i\tilde Q$ is left multiplication by the central element $i$.

**Proof.** For all $\tilde Q$ one has $J(\tilde Q) = i\tilde Q$. If $T$ is $\mathbb{C}$-linear then $T(J\tilde Q) = T(i\tilde Q) = i\,T(\tilde Q) = J(T\tilde Q)$, so $TJ = JT$. Conversely, if $TJ = JT$ then for $\lambda = a + bi$,
$$
T(\lambda \tilde Q) = T(a\tilde Q + bJ\tilde Q) = a\,T(\tilde Q) + b\,TJ(\tilde Q) = a\,T(\tilde Q) + b\,J T(\tilde Q) = \lambda\,T(\tilde Q),
$$
so $T$ is $\mathbb{C}$-linear; the antilinear case is the same computation with $TJ = -JT$ and $\lambda \mapsto \bar\lambda$. $\square$

**Remark (the criterion is the real-reading form of the distinction).** The operator $J$ is the scalar $i$ acting on the algebra, and it is available inside the ring, so the criterion expresses the $\mathbb{C}$-linearity of a real-linear map without appealing to complex scalars: a map is $\mathbb{C}$-linear or $\mathbb{C}$-antilinear according to whether it commutes or anticommutes with $J$.

### The Table of the Two Kinds

**Theorem.** Among the five maps, the $\mathbb{C}$-linear ones are exactly $\mathrm{id}$ and ${}^{\natural}$, and the $\mathbb{C}$-antilinear ones are exactly $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat}$.

**Proof.** In the real basis the operator $J$ has the block form
$$
J = \begin{pmatrix} 0 & -I_4 \\ I_4 & 0 \end{pmatrix}
$$
in the four-dimensional blocks of the coordinates $q_\mu$ and $q'_\mu$. A diagonal map $\operatorname{diag}(A,B)$ with the first block $A$ and the second $B$ satisfies $TJ = JT$ exactly when $B = A$ and $\mathbb{C}$-antilinear exactly when $B = -A$; comparing with the table, the conditions correspond to the last four coordinates carrying the same signs, respectively the opposite signs, as the first four. By the table the first case holds for $\mathrm{id}$ and ${}^{\natural}$, the second for $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat}$. $\square$

**Corollary (the two that change character).** For the four involutions $\mathrm{id}, {}^{\natural}, \bar{\cdot}, {}^{*}$, exactly two are $\mathbb{C}$-linear, the identity and the quaternion conjugation, and exactly two are $\mathbb{C}$-antilinear, the complex conjugation and the Hermitian conjugation. Over $\mathbb{R}$ all four are ordinary $\mathbb{R}$-linear maps, so the two that change character in the passage between the readings are the complex conjugation and the Hermitian conjugation: maps that are conjugate-linear over $\mathbb{C}$ and plain linear over $\mathbb{R}$. The reversal ${}^{\flat}$ is the same kind as those two, with the extra sign $-1$ that places it outside the involution group.

**Remark (the row of coincidences).** The coincidence of $\mathrm{id}$ and ${}^{\natural}$ over $\mathbb{C}$ is the statement that the quaternion conjugation is the unique nontrivial conjugation that is $\mathbb{C}$-linear, and it is the same statement as the commutation with $J$: in the coefficient formula $\natural$ acts by the sign vector $\varepsilon = (1,-1,-1,-1)$, so it fixes the central element $i = ie_0$, and a map fixing $i$ commutes with the operator $J$ of multiplication by $i$. The complex conjugation $\bar{\cdot}$, which sends $i$ to $-i$, is the opposite case and anticommutes with $J$. Over $\mathbb{R}$ the row becomes a coincidence of kind and not of definition: all five maps are $\mathbb{R}$-linear, and only the commutator with $J$ remembers the complex reading.

## Summary

The five distinguished maps of $\mathbb{B}$, the identity and the four conjugations ${}^{\natural}, \bar{\cdot}, {}^{*}$ and ${}^{\flat}$, act on the eight real coordinates by signed permutations, hence are $\mathbb{R}$-linear operators, each of determinant $+1$, the four nontrivial ones being reflections with eigenvalues $+1$ and $-1$ of multiplicity four. Read over $\mathbb{C}$ the same maps are again linear maps, but of two kinds: $\mathbb{C}$-linear for the identity and ${}^{\natural}$, $\mathbb{C}$-antilinear for $\bar{\cdot}$, ${}^{*}$ and ${}^{\flat}$.

$$
\boxed{\ \text{Over } \mathbb{R} \text{ all four conjugations are ordinary linear maps; over } \mathbb{C} \text{ only } {}^{\natural} \text{ is } \mathbb{C}\text{-linear, and } \bar{\cdot}, {}^{*}, {}^{\flat} \text{ are conjugate-linear.}\ }
$$

The distinction is recovered over the real reading by the commutator with the complex structure $J$, a map commuting with $J$ being $\mathbb{C}$-linear and one anticommuting with it being $\mathbb{C}$-antilinear; of the four involutions of the Klein four-group, the identity and the quaternion conjugation commute with $J$ and the complex and Hermitian conjugations anticommute with it. The real reading draws no such distinction, because the conjugate of a real scalar is itself.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{id}, {}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | the identity, quaternion, complex, Hermitian and reversal maps |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | the four conjugations |
| $\mathrm{id}, {}^{\natural}, \bar{\cdot}, {}^{*}$ | the four involutions, the Klein four-group |
| $\varepsilon = (1,-1,-1,-1)$ | the sign vector of the quaternion conjugation on the coefficients |
| $J : \tilde Q \mapsto i\tilde Q$ | the complex structure, $J = \begin{pmatrix} 0 & -I_4 \\ I_4 & 0\end{pmatrix}$, $J^2 = -\mathrm{id}$ |
| $D_\sigma = \operatorname{diag}(\sigma_0,\sigma_1,\sigma_2,\sigma_3,\tau\sigma_0,\tau\sigma_1,\tau\sigma_2,\tau\sigma_3)$ | the diagonal form of a conjugation, $\sigma_\mu = \pm 1$, $\tau = \pm 1$ |
| $TJ = JT$ | criterion for $\mathbb{C}$-linearity of a real-linear $T$ |
| $TJ = -JT$ | criterion for $\mathbb{C}$-antilinearity of a real-linear $T$ |

## Further Reading

- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the coefficient formulas, the group laws and the reversal.
- *Biquaternions as a Vector Space over $\mathbb{R}$* (`articles_maths/biquaternions-as-a-vector-space-over-r.md`), for the complex structure $J$ and the commutator criterion.
- *Comparison of the Remarkable Subspaces* (`articles_maths/comparison-of-the-remarkable-subspaces.md`) and *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the fixed spaces of the conjugations.
- *The Change of Scalars from $\mathbb{C}$ to $\mathbb{R}$* (`articles_maths/the-change-of-scalars-from-c-to-r.md`), for the general statement that conjugate-linearity is the only property the passage to real scalars removes.
- *The Automorphisms and Derivations of the Real Biquaternion Algebra* (`articles_maths/the-automorphisms-and-derivations-of-the-real-biquaternion-algebra.md`), for the maps that are algebra homomorphisms and not merely additive.
