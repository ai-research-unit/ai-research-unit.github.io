
# __List of Unital Algebras__

## Introduction

This article lists the algebras and the rings that carry an identity, together with the objects that do not. A unital algebra has an element $1_A$ with $1_Ax = x1_A = x$ for every $x$, with the convention $1 \neq 0$ excluding the zero ring, and the identity makes the algebra a ring and gives it a group of units; a non-unital algebra has no such element, and the unitisation adjoins one. Every entry points to the article that introduces the object.

The list is a proper subclass of *List of Algebras*: that article carries the algebras over a field of the corpus, unital or not, with their dimension, their centre and their ideals, and this one carries the unital algebras, over a field or over a commutative ring, the identity that fixes them and the unit group they acquire, and beside them the non-unital objects that fail to have an identity.

This article introduces nothing and proves nothing. It records examples and non-examples side by side, a non-example being an algebra or a ring with no identity, with the failure named and the article that records it.

## The Identity, the Canonical Map and the Unit Group

An identity for the product is an element $1_A$ with $1_Ax = x1_A = x$ for every $x$, and it is unique when it exists. The identity is what converts an algebra into a ring and makes the multiplicative structure a monoid, so the unit group and the centre are available and the homomorphisms between unital algebras can be required to preserve it.

| Object | The property it has | Introduced in |
|---|---|---|
| Unital algebra | an algebra with a two-sided identity $1_A$, and $1_A \neq 0$ | *Unital Algebras* |
| The canonical map $\eta : R \to A$, $\eta(r) = r1_A$ | a unital ring homomorphism with image in the centre $Z(A)$; a unital $R$-algebra is a ring with a unital homomorphism $R \to Z(A)$ | *Unital Algebras* |
| The unit group $A^\times$ | the invertible elements, a group under multiplication, with identity $1_A$ | *Centre, Units, Zero Divisors and Division Algebras* |
| A unit is not a zero divisor | if $u$ is invertible and $uz = 0$ then $z = 0$, and likewise on the left | *Centre, Units, Zero Divisors and Division Algebras* |
| Unital subalgebra | a subalgebra containing $1_A$; its own identity is necessarily $1_A$ | *Ideals and Quotients of Algebras* |
| The convention $1 \neq 0$ | excludes the zero ring, the one algebra in which $1 = 0$; the corpus assumes it of every ring | *Rings* |

The identity is inherited by quotients and not by ideals: the quotient of a unital algebra by a two-sided ideal is unital with identity $1 + I$, while every proper ideal of a unital algebra contains no unit, so it is non-unital as a subalgebra; it may nevertheless carry an identity of its own, an idempotent of the ambient algebra, and then it is a unital algebra.

## The Unital Algebras of the Corpus

The examples are the algebras whose identity is part of the construction, and in each case the unit group is computed in the introducing article.

| Algebra | Its identity and units | Introduced in |
|---|---|---|
| $M_n(R)$, the matrix algebra | the identity matrix $I_n$; $M_n(R)^\times = \mathrm{GL}_n(R)$ | *Matrix Algebras* |
| $k[G]$, the group algebra | the identity $1_G$ of the group, extended to the algebra | *Group Algebras* |
| $U(\mathfrak{g})$, the universal enveloping algebra | the identity of the tensor algebra $T(\mathfrak{g})$ is preserved by the quotient; the universal property lands in associative algebras | *Universal Enveloping Algebras* |
| $T(V)$, the tensor algebra | the unit $1 \in V^{\otimes 0} = R$ | *Tensor Powers and the Free Algebra* |
| $R[x_1,\dots,x_n]$, the polynomial algebra | the constant polynomial $1$; commutative | *Polynomial Algebras* |
| $kQ$, the path algebra of a finite quiver | the sum $1 = \sum_{v \in Q_0} e_v$ of the length-zero paths is the identity, so the algebra is unital exactly when the vertex set is finite | *Quiver Representations and Representation Type* |
| A division algebra $D$ | $D^\times = D\setminus\{0\}$: every nonzero element is a unit | *Division Algebras* |
| $B(H)$, the bounded operators | the identity operator $1$, so $B(H)$ is a unital $\mathrm{C}^*$-algebra | *Operator Algebras* |
| $C(X)$, continuous functions on a compact space $X$ | the constant function $1$; the commutative Gelfand–Naimark theorem identifies the unital commutative $\mathrm{C}^*$-algebras as the $C(X)$ with $X$ compact | *Operator Algebras* |
| $\mathbb{H}$, the quaternions | $\mathbb{H}^\times = \mathbb{H}\setminus\{0\}$; a unital division ring | *Quaternion Algebra* |
| $\mathbb{B} \cong M_2(\mathbb{C})$, the biquaternions | the identity of $M_2(\mathbb{C})$; $\mathbb{B}^\times = \mathrm{GL}_2(\mathbb{C})$ | *Biquaternion Algebra* |
| The augmentation ideal $I(G) \subseteq R[G]$ for $G = \mathbb{Z}/2$ | carries the identity $(1-g)/2$ when the characteristic is not $2$, an idempotent of $R[G]$ different from $1$ | *Unital Algebras* |

The matrix algebra and the group algebra are unital by construction, and their unit groups are the general linear group and the group of units of the group ring; the enveloping algebra inherits its identity from the tensor algebra, of which it is a quotient. The division algebras are the unital algebras in which the unit group is as large as possible, and their unit group is the punctured algebra.

## The Rings with Identity Read as Algebras

The corpus fixes the identity as an axiom of every ring, so the rings it meets are unital algebras over $\mathbb{Z}$.

| Ring | The identity it carries | Introduced in |
|---|---|---|
| A ring with identity $A$ | the corpus's rings are associative and unital by axiom (A4), with $1 \neq 0$ | *Rings* |
| $A$ as a $\mathbb{Z}$-algebra | the canonical map $n \mapsto n1_A$; every associative ring with identity is a unital $\mathbb{Z}$-algebra in exactly one way | *Unital Algebras* |
| $Z(A)$, the centre | a commutative subring containing $1_A$ | *Centre, Units, Zero Divisors and Division Algebras* |
| $M_n(D)$ over a division ring $D$ | the identity matrix; unit group $\mathrm{GL}_n(D)$ | *Simple and Semisimple Modules* |
| $\mathbb{Z}/n\mathbb{Z}$, the residue ring | the identity $1 + n\mathbb{Z}$ | *Modular Arithmetic and the Ring of Residues* |
| $\mathbb{Z}$, the integers | the multiplicative identity $1$; $\mathbb{Z}^\times = \{\pm1\}$ | *The Integers* |

The passage from a ring to an algebra is not a change of axioms but a change of what may be asserted, and the identity is common to both: every unital $R$-algebra is a ring with a homomorphism $R \to Z(A)$, and conversely a ring homomorphism from $R$ into the centre of a ring makes that ring a unital $R$-algebra.

## The Unitisation of a Non-Unital Algebra

The unitisation is the construction that adjoins an identity to an algebra that has none, and it is the reason a non-unital algebra can be studied through the unital theory.

| Object | The property it has | Introduced in |
|---|---|---|
| The unitisation $A^+ = A \oplus R$ | product $(a,r)(b,s) = (ab + rb + sa,\,rs)$; unital with identity $(0,1)$ | *Unital Algebras* |
| $A$ as an ideal of $A^+$ | a two-sided ideal, with $A^+/A \cong R$ | *Unital Algebras* |
| The universal property of $A^+$ | every algebra homomorphism from $A$ into a unital algebra factors uniquely through the inclusion $A \to A^+$ | *Unital Algebras* |
| The unitisation of an already unital algebra | $A \oplus R$ with the product that makes $A$ an ideal; unital, and it contains $A$ as a proper ideal | *Unital Algebras* |

The unitisation of a unital algebra is unital for a degenerate reason, and the construction is used throughout the analysis articles: the GNS construction for a $\mathrm{C}^*$-algebra without identity is applied to its unitisation, and in *K-Theory of Operator Algebras* the unitisation map extends the definitions from the unital to the general case.

## Homomorphisms and the Identity

A homomorphism between unital algebras may or may not preserve the identity, and the distinction is visible in the corpus in the maps attached to the unitisation and to the augmentation.

| Map | Its relation to the identity | Introduced in |
|---|---|---|
| A unital (identity-preserving) homomorphism | $\varphi(1_A) = 1_B$, the corpus's default for rings and for algebra homomorphisms | *Rings* |
| The augmentation $\pi : k[G] \to k$ | unital, $\pi(1_G) = 1$; its kernel is the augmentation ideal | *Group Algebras* |
| The inclusion $A \to A^+$ | not identity-preserving when $A$ has no identity, since $A$ has none to preserve | *Unital Algebras* |
| The quotient $A^+ \to A^+/A \cong R$ | unital, with kernel $A$ | *Unital Algebras* |
| The quotient map $A \to A/I$ | unital, with identity $1 + I$ | *Rings*, §Quotient Rings |
| The idempotent $\varphi(1_A)$ | for an arbitrary homomorphism, $\varphi(1_A)$ is an idempotent of $B$, and $\varphi$ is unital exactly when $\varphi(1_A) = 1_B$ | *Unital Algebras* |
| The unital extension $\varphi^+$ | the unique unital homomorphism $A^+ \to B$ extending $\varphi : A \to B$, $\varphi^+(a,r) = \varphi(a) + r1_B$ | *Unital Algebras* |

A unital homomorphism carries units to units, so it restricts to a group homomorphism $A^\times \to B^\times$; a homomorphism that does not preserve the identity carries no such group map in general, which is the reason the corpus fixes the unital convention for rings and for algebra homomorphisms.

## The Non-Unital Algebras

The objects below are the algebras of the corpus with no identity, and each row names the article that shows the identity is absent.

| Algebra | Why it has no identity | Introduced in |
|---|---|---|
| $L^1(G)$ for a locally compact group $G$ that is not discrete | no identity when $G$ is not discrete; it has an identity only in the discrete case, where it is $\delta_e$ | *The Convolution Algebra $L^1(G)$* |
| $K(H)$, the compact operators on an infinite-dimensional Hilbert space $H$ | the identity operator is not compact; $K(H)$ is unital only when $H$ is finite-dimensional | *Operator Algebras* |
| $C_0(X)$ for a locally compact non-compact space $X$ | a continuous function vanishing at infinity has no constant $1$ to contain; $C_0(X)$ is unital exactly when $X$ is compact | *Operator Algebras* |
| $L^1(H)$ and $L^2(H)$, the trace-class and Hilbert–Schmidt operators | two-sided $*$-ideals of $B(H)$; the identity is not trace class or Hilbert–Schmidt in infinite dimension | *Operator Algebras* |
| A proper two-sided ideal $I \subsetneq A$ of a unital algebra | contains no unit of $A$, so $1_A \notin I$ and $I$ is non-unital as a subalgebra; it may carry an identity of its own, an idempotent of $A$ different from $1_A$ | *Ideals and Quotients of Algebras*; *Unital Algebras* |
| The ideal $(x) \subseteq R[x]$, the polynomials of positive degree | a proper ideal of the unital algebra $R[x]$, containing no unit, hence non-unital as a subalgebra | *Unital Algebras* |

These are the algebras of the corpus whose lack of an identity is the point of the article that introduces them, and they are the reason the unitisation is needed. The convolution algebra is the standard example: the identity it lacks for non-discrete $G$ is replaced by an approximate identity, and the whole representation theory of the group is developed from that.

## Approximate Identities in Place of a Unit

A Banach algebra without identity often has a net that behaves like an identity in the limit, and the corpus uses it wherever the unit would be used.

| Object | The property it has | Introduced in |
|---|---|---|
| A two-sided approximate identity $(u_\alpha)$ | $\lVert u_\alpha f - f\rVert \to 0$ and $\lVert f u_\alpha - f\rVert \to 0$ for every $f$ | *The Convolution Algebra $L^1(G)$* |
| The normalised approximate identity of $L^1(G)$ | $u_\alpha \geq 0$, $\int_G u_\alpha = 1$ and $\lVert u_\alpha\rVert_1 = 1$, for every locally compact $G$ | *The Convolution Algebra $L^1(G)$* |
| Reiter's property $P_1$ | an approximately invariant normalised approximate identity; equivalent to the amenability of $G$ | *The Convolution Algebra $L^1(G)$* |
| States on a $\mathrm{C}^*$-algebra without identity | the normalisation is replaced by $\lVert\omega\rVert = 1$ in the GNS construction | *Operator Algebras* |

The approximate identity is the substitute for the identity in norm estimates and in the definition of nondegenerate representations, and Reiter's property shows that the existence of an approximately invariant one is exactly the amenability of the group.

## Summary

This article has listed the unital algebras and rings of the corpus, together with the objects that fail to be unital. The identity $1_A$ is unique, it makes the algebra a ring with a unit group $A^\times$, and the canonical map $\eta : R \to A$, $\eta(r) = r1_A$, identifies a unital $R$-algebra with a ring carrying a homomorphism from $R$ into its centre. The unital examples are the matrix algebra $M_n(R)$, the group algebra $k[G]$, the universal enveloping algebra $U(\mathfrak{g})$, the tensor algebra $T(V)$, the polynomial algebra, the path algebra of a finite quiver, the division algebras, the augmentation ideal of $\mathbb{Z}/2$, and, on the operator side, $B(H)$ and $C(X)$ for compact $X$. The rings with identity are read as unital algebras over $\mathbb{Z}$ and over themselves, with the centre $Z(A)$ and the matrix ring $M_n(D)$ among them. The unitisation $A^+$ adjoins an identity, with $A$ a two-sided ideal of $A^+$ and $A^+/A \cong R$. The non-examples — $L^1(G)$ for non-discrete $G$, the compact operators on an infinite-dimensional space, $C_0(X)$ for non-compact $X$, the trace-class and Hilbert–Schmidt ideals, and a proper ideal of a unital algebra — each name the failure of the identity axiom, and the analytic ones among them carry an approximate identity in place of the unit.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $1_A$, $1$ | The identity of an algebra or a ring, with $1 \neq 0$ |
| $A^\times$ | The group of units of $A$ |
| $Z(A)$ | The centre of $A$, a commutative subring containing $1_A$ |
| $\eta : R \to A$, $\eta(r) = r1_A$ | The canonical map making a unital $R$-algebra a ring over $R$ |
| $\varphi^+$ | The unique unital extension $A^+ \to B$ of $\varphi : A \to B$, $\varphi^+(a,r) = \varphi(a) + r1_B$ |
| $\varphi(1_A)$ | An idempotent in $B$; $\varphi$ is unital exactly when it equals $1_B$ |
| $A^+ = A \oplus R$ | The unitisation, with $(a,r)(b,s) = (ab+rb+sa, rs)$ and identity $(0,1)$ |
| $I_n$, $\mathrm{GL}_n(R)$ | The identity matrix and the unit group of $M_n(R)$ |
| $M_n(D)$, $\mathrm{GL}_n(D)$ | A matrix ring over a division ring and its units |
| $k[G]$, $\pi$, $I(G)$ | Group algebra, augmentation map, augmentation ideal |
| $U(\mathfrak{g})$, $T(V)$ | Universal enveloping algebra and tensor algebra |
| $kQ$, $e_v$ | The path algebra of a quiver, and its length-zero paths |
| $L^1(G)$, $\delta_e$, $(u_\alpha)$, $P_1$ | The convolution algebra, unital exactly for discrete $G$ with identity $\delta_e$; point mass at $e$, an approximate identity, Reiter's property |
| $K(H)$, $C_0(X)$, $B(H)$ | The compact operators, non-unital for infinite-dimensional $H$ and simple; functions vanishing at infinity; the bounded operators |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the definition of a unital algebra, the unitalisation and the convention on identity-preserving homomorphisms.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for approximate identities in Banach algebras and the unitisation of an algebra without identity.
- Gerard J. Murphy, *$C^*$-Algebras and Operator Theory* (Academic Press, 1990), for the non-unital $\mathrm{C}^*$-algebras, their approximate identities and the unitisation.
