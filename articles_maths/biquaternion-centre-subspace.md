# __Biquaternion Centre Subspace__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four linear involutions, and each of them splits $\mathbb{B}$ into a fixed space and an anti-fixed space. Six of the eight spaces so obtained are distinct and are called the **six distinguished subspaces** of $\mathbb{B}$: four of dimension four, together with the two-dimensional centre and the six-dimensional vector subspace. This article treats the smallest of them, the **centre subspace** $\mathbb{C}_{\mathbb{B}}$, on its own: its definition, its basis, its algebra and module structure, the restriction of the algebraic square $N$ to it, the action of the four involutions upon it, and its place among the particular cases of the algebra. The other five are treated in the companion articles *Biquaternion Vector Subspace*, *Biquaternion Quaternion Subspace*, *Biquaternion Anti-Quaternion Subspace*, *Biquaternion Hermitian Subspace* and *Biquaternion Anti-Hermitian Subspace*; their relations with one another are collected in *Biquaternion Relations Between Subspaces*, and the involutions themselves in *Biquaternion Involution Lattice*.

Nothing below is a physical statement. The elements are written $\tilde{Q}, \tilde{R}, \tilde{P}, \dots$, their complex coefficients $Q_0, Q_1, Q_2, Q_3$, and the real and imaginary parts of a coefficient $Q_\mu = q_\mu + i q'_\mu$; no other coordinates are used.

## Definition and Basis

### The Defining Involution

**Definition.** The **centre subspace** is the fixed space of quaternion conjugation,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = \tilde{Q} \right\} ,
$$

where quaternion conjugation is $\tilde{Q}^{\natural} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3$.

Since ${}^{\natural}$ is an involution, it has eigenvalues $\pm 1$ and $\mathbb{B}$ is the direct sum of its fixed space and its anti-fixed space; the anti-fixed space is the vector subspace $\mathrm{Vect}(\mathbb{B})$, treated in the companion article.

### The Condition in Coordinates

Writing $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ and comparing the two sides of $\tilde{Q}^{\natural} = \tilde{Q}$ coefficient by coefficient:

- the coefficient of $e_0$ gives $Q_0 = Q_0$, which is no condition;
- the coefficient of $e_k$ gives $-Q_k = Q_k$, that is $Q_k = 0$, for each $k = 1, 2, 3$.

The centre subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_0 e_0 , \qquad Q_0 \in \mathbb{C} .
$$

### Basis and Dimension

**Proposition.** The centre subspace is a real vector space of dimension $2$, with basis $e_0, ie_0$. In terms of the real coordinates of $\mathbb{B}$ it is the coordinate plane

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} : q_1 = q_2 = q_3 = q'_1 = q'_2 = q'_3 = 0 \right\} ,
$$

in which the two free parameters are $q_0$ and $q'_0$.

**Proof.** The four complex coefficients of $\tilde{Q}$ reduce to $Q_0$ alone, and a complex number is a real pair, $Q_0 = q_0 + i q'_0$; the two elements $e_0$ and $ie_0$ are linearly independent over $\mathbb{R}$ and span the set.

The dimension count is recorded once and used throughout: of the six distinguished subspaces, $\mathbb{C}_{\mathbb{B}}$ is the only one of dimension $2$, the vector subspace $\mathrm{Vect}(\mathbb{B})$ is the only one of dimension $6$, and the remaining four are of dimension $4$.

## Algebra and Module Structure

### It Is the Centre of the Algebra

**Theorem.** $\mathbb{C}_{\mathbb{B}}$ is the centre of $\mathbb{B}$,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}\tilde{R} = \tilde{R}\tilde{Q} \ \text{for every} \ \tilde{R} \in \mathbb{B} \right\} .
$$

**Proof.** An element commutes with every other element if and only if it commutes with the basis elements $e_1, e_2, e_3$, and $Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ commutes with all three precisely when $Q_1 = Q_2 = Q_3 = 0$; the central elements are then the $\mathbb{C}$-multiples of $e_0$, which is the fixed space of ${}^{\natural}$ computed above.

The two names of the subspace are therefore the same object described in two ways: it is the fixed space of one involution, and it is the centre of the algebra. Its elements are the **central elements**, and in the corpus's notation a central element is written $A e_0$ with $A \in \mathbb{C}$, or $\rho e_0$ when a modulus is in play.

### Subalgebra, Commutativity, Field Structure

**Proposition.** $\mathbb{C}_{\mathbb{B}}$ is a subalgebra of $\mathbb{B}$, it is commutative, and as a real algebra it is isomorphic to $\mathbb{C}$ by $Q_0 e_0 \mapsto Q_0$.

**Proof.** For two central elements, $Q_0 e_0 \cdot R_0 e_0 = (Q_0 R_0) e_0$, which lies in the subspace; commutativity is the commutativity of $\mathbb{C}$; and the displayed map is a bijective ring homomorphism because $e_0$ is the unit.

It is one of exactly two of the six distinguished subspaces that are subalgebras, the other being the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. Both are division algebras: $\mathbb{C}_{\mathbb{B}}$ is a field and $\mathbb{H}_{\mathbb{B}}$ is a division algebra. The centre subspace is also the only commutative one of the six.

### Ideals and Modules

Being the centre and a field, $\mathbb{C}_{\mathbb{B}}$ supports the simplest possible module and ideal structure: $\mathbb{B}$ is a free module of rank four over $\mathbb{C}_{\mathbb{B}}$, with basis $e_0, e_1, e_2, e_3$; and $\mathbb{C}_{\mathbb{B}}$ is not a proper two-sided ideal of $\mathbb{B}$, since $\mathbb{B}$ is simple and its only two-sided ideals are $0$ and $\mathbb{B}$ itself. The one-sided ideal theory of $\mathbb{B}$ is developed in *Biquaternion Ideals and Peirce Decomposition* and involves the idempotents, not the centre.

### Multiplication Tables

The products within the subspace and the products with the vector units that generate the whole algebra are

| product | value | product | value |
|---|---|---|---|
| $e_0 \cdot e_0$ | $e_0$ | $e_0 \cdot e_k$ | $e_k$ |
| $(ie_0) \cdot e_0$ | $ie_0$ | $(ie_0) \cdot e_k$ | $ie_k$ |
| $e_0 \cdot (ie_0)$ | $ie_0$ | $e_k \cdot e_0$ | $e_k$ |

for $k = 1, 2, 3$. The table is the statement that $\mathbb{C}_{\mathbb{B}}$ multiplies into every subspace and is multiplied into by every subspace, with no sign change: multiplication by a central element is a scalar extension, and the four subspaces $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ and the two sectors are all modules over $\mathbb{C}_{\mathbb{B}}$.

### The Jordan Remark

The centre **is closed under the symmetrized product**. For two central elements, $\tilde{P}=P_0e_0$ and $\tilde{R}=R_0e_0$,

$$
\tilde{P}\bullet\tilde{R} = \tfrac{1}{2}\bigl(\tilde{P}\tilde{R}+\tilde{R}\tilde{P}\bigr) = P_0R_0\,e_0 ,
$$

with $e_0$ the unit of the Jordan algebra. The centre is therefore one of the two subspaces closed under both halves of the product, the quaternion subspace being the other; the classification is in *Biquaternion Jordan Algebra*.

### The Lie Remark

The centre **is closed under the commutator**, the bracket vanishing identically on it: it is the centre of the Lie algebra and an abelian ideal. The detail is in §*The Lie Algebra Structure* below, and the general account in *Biquaternion Lie Algebra*.


## Units and Zero Divisors

**Proposition.** On the centre subspace the algebraic operation $N$ is the square of the coefficient,

$$
N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = Q_0^2 , \qquad \tilde{Q} = Q_0 e_0 .
$$

**Proof.** $\tilde{Q}^{\natural} = \tilde{Q}$ on the subspace, so $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = \tilde{Q}^2 = Q_0^2 e_0$, read as the scalar $Q_0^2$.

**Theorem.** For $\tilde{Q} = Q_0 e_0$, the following are equivalent:

1. $\tilde{Q}$ is a unit;
2. $N(\tilde{Q}) \neq 0$;
3. $Q_0 \neq 0$.

The inverse is $\tilde{Q}^{-1} = Q_0^{-1} e_0 = \dfrac{\bar{Q_0}}{|Q_0|^2} e_0$.

**Proof.** $N(Q_0e_0) = Q_0^2$ vanishes exactly when $Q_0 = 0$; the inverse formula is verified directly, $Q_0 e_0 \cdot (Q_0^{-1} e_0) = e_0$, and $Q_0^{-1} = \bar{Q_0}/|Q_0|^2$ is the standard expression of the complex inverse.

**Corollary.** The only zero divisor in $\mathbb{C}_{\mathbb{B}}$ is $0$, and the only non-unit is $0$.

**Proof.** A zero divisor is a non-zero element with $N(\tilde{Q}) = 0$; on the subspace $N(\tilde{Q}) = Q_0^2$, which vanishes only at $Q_0 = 0$.

The corollary is the statement that $\mathbb{C}_{\mathbb{B}}$ is a field, and it is the reason the centre subspace carries none of the degeneracy phenomena — null elements, idempotents with $N=0$, unbounded families — that the vector subspace and the zero divisors exhibit. The **idempotents** of the subspace are the solutions of $Q_0^2 = Q_0$, namely $Q_0 \in \{0, 1\}$: the zero element and the unit. In particular $\mathbb{C}_{\mathbb{B}}$ contains no non-trivial idempotent, while $\mathbb{B}$ contains many, all of them away from the centre.

## The Four Involutions on It

The four involutions of the algebra are quaternion conjugation ${}^{\natural}$, complex conjugation $\bar{\cdot}$, Hermitian conjugation ${}^{*} = \bar{\cdot} \circ {}^{\natural} = {}^{\natural} \circ \bar{\cdot}$, and reversal $\flat = -{}^{*}$. Their action on $\mathbb{C}_{\mathbb{B}}$, in the basis $e_0, ie_0$, is diagonal:

| involution | $\tilde{Q} = Q_0e_0$ | matrix on $e_0, ie_0$ |
|---|---|---|
| ${}^{\natural}$ | $Q_0 e_0$ | $\operatorname{diag}(1, 1)$ |
| $\bar{\cdot}$ | $\bar{Q_0} e_0$ | $\operatorname{diag}(1, -1)$ |
| ${}^{*}$ | $\bar{Q_0} e_0$ | $\operatorname{diag}(1, -1)$ |
| $\flat$ | $-\bar{Q_0} e_0$ | $\operatorname{diag}(-1, 1)$ |

The subspace is invariant under all four, since each of them preserves the conditions $Q_1 = Q_2 = Q_3 = 0$; and the table has a content that is worth stating separately: **complex conjugation acts on the centre subspace as the non-trivial involution of $\mathbb{C}$**, exchanging the two real directions $e_0$ and $ie_0$. Hermitian conjugation acts on it in exactly the same way, while reversal negates $e_0$ and fixes $ie_0$. Complex conjugation is the reason $\bar{\cdot}$ is not an inner automorphism of $\mathbb{B}$: an inner automorphism fixes the centre pointwise, while $\bar{\cdot}$ acts on it by the Galois involution $i \mapsto -i$. The point is developed in *Biquaternion Involution Lattice* and in *Biquaternion Automorphisms and Derivations*.

## Relations to the Other Five Subspaces

The intersections of $\mathbb{C}_{\mathbb{B}}$ with the other five distinguished subspaces are, with dimensions,

| pair | intersection | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}} \cap \mathrm{Vect}(\mathbb{B})$ | $\{0\}$ | $0$ |
| $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}}$ | $\mathbb{R} e_0$ | $1$ |
| $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{R} e_0$ | $1$ |
| $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_+$ | $\mathbb{R} e_0$ | $1$ |
| $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_-$ | $i\mathbb{R} e_0$ | $1$ |

The two lines $\mathbb{R}e_0$ and $i\mathbb{R}e_0$ that appear are the **coordinate blocks** of the algebra; the centre subspace is their direct sum,

$$
\mathbb{C}_{\mathbb{B}} = \mathbb{R}e_0 \oplus i\mathbb{R}e_0 ,
$$

the first line being its intersection with the quaternion and Hermitian subspaces at once, the second its intersection with the anti-quaternion and anti-Hermitian subspaces at once. This is the pattern that *Biquaternion Relations Between Subspaces* records for all six subspaces. The centre subspace is complementary to the vector subspace, $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, which is the scalar–vector decomposition of the algebra; with each of the other four subspaces it has intersection of dimension one, so none of those pairs spans $\mathbb{B}$.

## The Subspace in the Algebra

The section places the subspace among the particular cases that the Algebra articles treat one by one — the idempotents, the ideals and the Peirce decomposition, the roots of minus one, the zero divisors and the commutator bracket — each stated for the subspace and referred to its article.

### Idempotents

**Proposition.** The idempotents of $\mathbb{C}_{\mathbb{B}}$ are $0$ and $e_0$; the centre contains no non-trivial idempotent.

**Proof.** For a central element $\tilde{Q} = Q_0 e_0$ the equation $\tilde{Q}^2 = \tilde{Q}$ reads $Q_0^2 = Q_0$, whose solutions are $Q_0 = 0$ and $Q_0 = 1$.

The classification of *Biquaternion Idempotents and Projections* produces every non-trivial idempotent as $\tilde\Pi = \tfrac12 e_0 \pm \tfrac12 \xi i$, of scalar part $\tfrac12$; a central element is a $\mathbb{C}$-multiple of $e_0$ and has no vector part, so no non-trivial idempotent is central. The standard idempotents $\tilde\Pi_1, \tilde\Pi_2$ are the first instance: they are not central, since $e_1$ anticommutes with $ie_3$ and therefore does not commute with either.

### Ideals and the Peirce Decomposition

Being the centre, $\mathbb{C}_{\mathbb{B}}$ enters the ideal theory of $\mathbb{B}$ in the two-sided version only. The algebra is simple, so its two-sided ideals are $0$ and $\mathbb{B}$, and the centre, a proper subalgebra, is neither of them; over $\mathbb{C}_{\mathbb{B}}$ the algebra is a free module of rank four, with basis $e_0, e_1, e_2, e_3$. The one-sided theory is carried by the primitive idempotents, which are not central: in the Peirce decomposition of *Biquaternion Ideals and Peirce Decomposition* the diagonal corner $\tilde\Pi\mathbb{B}\tilde\Pi$ is the line $\mathbb{C}\tilde\Pi$ and the two off-diagonal corners are spanned by the nilpotents $\tilde T = \tfrac12(ie_1 - e_2)$ and $\tilde S = \tfrac12(ie_1 + e_2)$, and the minimal left ideal $\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi \oplus \mathbb{C}\tilde S$ meets the centre only at the origin. In the language of that article, no corner of the Peirce decomposition is central: the case of a *central* idempotent, for which the off-diagonal corners vanish and the sum is a product of algebras, is excluded because no non-trivial idempotent of $\mathbb{B}$ is central.

### The Roots of Minus One

**Proposition.** The centre contains exactly two roots of $-1$, namely $\pm ie_0$; these are the two trivial roots.

**Proof.** One has $(Q_0 e_0)^2 = Q_0^2 e_0$, which equals $-e_0$ if and only if $Q_0^2 = -1$, that is $Q_0 = \pm i$.

In the classification of *Biquaternion Square Roots of Minus One, Zero and Plus One* the trivial roots $\pm i$ are the two isolated points of the root set, while the two-real-dimensional family of real roots and the four-real-dimensional family of non-trivial roots lie elsewhere; the centre contains none of the roots that generate non-central idempotents. Under the bijection $\xi \mapsto \tfrac12(e_0 + \xi i)$ of *Biquaternion Idempotents and Projections* the two trivial roots give exactly the two trivial idempotents $0$ and $e_0$, and nothing else of the idempotent set.

### Zero Divisors

**Proposition.** The only zero divisor in $\mathbb{C}_{\mathbb{B}}$ is $0$; the centre is a field.

**Proof.** A zero divisor is a non-zero element with $N=0$, and on the centre $N(\tilde{Q}) = Q_0^2$ vanishes only at $Q_0 = 0$.

In the distribution of *Biquaternion Zero Divisors* the centre is the first of the three subspaces free of zero divisors, with $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$; it is the degenerate case of that distribution in which the only null element is the origin.

### The Lie Algebra Structure

Under the commutator $[\tilde{P},\tilde{Q}] = \tilde{P}\tilde{Q} - \tilde{Q}\tilde{P}$ the centre is the centre of the Lie algebra,

$$
\mathrm{Z}(\mathrm{G}) = \mathbb{C}e_0 = \mathbb{C}_{\mathbb{B}} ,
$$

and the bracket vanishes on it identically: it is an abelian Lie subalgebra and an abelian ideal. It is the complement of the derived subalgebra, $\mathrm{G} = \mathrm{B}_0 \oplus \mathbb{C}_{\mathbb{B}}$ with $[\mathrm{G},\mathrm{G}] = \mathrm{B}_0 = \mathrm{Vect}(\mathbb{B})$, so the abelianisation $\mathrm{G}/[\mathrm{G},\mathrm{G}]$ is the centre, of complex dimension $1$. The two uses of the word coincide here — the centre of the associative algebra and the centre of the Lie algebra are the same subspace — which is a property of $\mathbb{B}$ and not of algebras in general. The trace $\mathrm{Tr}(\tilde{Q}) = 2Q_0$ restricts to the centre as $2Q_0$, a complex-linear functional identifying the centre with the dual of the abelianisation; the details are in *Biquaternion Lie Algebra*.

## Examples

### A Central Element and Its Invariants

Take $\tilde{Q} = (3 + 4i)e_0$. Its algebraic square is

$$
N(\tilde{Q}) = (3+4i)^2 = -7 + 24i , \qquad |N(\tilde{Q})| = 25 = |3+4i|^2 ,
$$

so $\tilde{Q}$ is a unit, with inverse $\tilde{Q}^{-1} = \frac{3-4i}{25} e_0$. Complex conjugation acts on it by $\bar{\tilde{Q}} = (3-4i)e_0$, which is a different element of the subspace; quaternion conjugation leaves it unchanged, since $Q_1 = Q_2 = Q_3 = 0$ makes $\tilde{Q}^{\natural} = \tilde{Q}$, while Hermitian conjugation acts on it exactly as complex conjugation, $\tilde{Q}^{*} = \bar{Q_0}e_0 = (3-4i)e_0$.

### The Unit and the Idempotents

The element $e_0$ has $N=1$ and is the unit of the algebra; $ie_0$ has $N=-1$ and satisfies $(ie_0)^2 = -e_0$, so the subspace contains the copy of the imaginary unit. The idempotents of $\mathbb{C}_{\mathbb{B}}$ are $0$ and $e_0$ only: the equation $Q_0^2 = Q_0$ has no other complex solution. No non-trivial idempotent of $\mathbb{B}$ is therefore central. The standard pair of non-trivial idempotents is

$$
\frac{e_0 + ie_1}{2} , \qquad \frac{e_0 - ie_1}{2} ,
$$

of scalar part $\tfrac12$, with $N=0$, and lying in the Hermitian subspace — so the idempotents that generate the minimal left ideals of $\mathbb{B}$ are constructed in the sector rather than in the centre, and the centre supplies only the two trivial ones.

## Summary

The centre subspace $\mathbb{C}_{\mathbb{B}}$ is the fixed space of quaternion conjugation, the set of elements $\tilde{Q} = Q_0 e_0$ with vanishing vector part, a real vector space of dimension $2$ with basis $e_0, ie_0$. It coincides with the centre of the algebra; it is a commutative subalgebra, isomorphic to $\mathbb{C}$; it is one of the two subalgebras among the six distinguished subspaces and the only commutative one. Multiplication by its elements acts as scalar extension on every other subspace. The algebraic square $N$ restricts to $N = Q_0^2$, complex-valued on the subspace; the units are exactly the elements with $Q_0 \neq 0$, they are all invertible, and there are no zero divisors except $0$. Of the four involutions, quaternion conjugation fixes it pointwise; complex conjugation and Hermitian conjugation act on it as the non-trivial involution $i \mapsto -i$, the action that no inner automorphism can reproduce; and reversal negates $e_0$ while fixing $ie_0$. Its intersection with the vector subspace is the origin, and its intersections with each of the remaining four subspaces are the two coordinate lines $\mathbb{R}e_0$ and $i\mathbb{R}e_0$. In the algebra of particular cases the centre contributes the two trivial idempotents $0$ and $e_0$ and no non-trivial one, no Peirce corner, only the two trivial roots $\pm ie_0$, no zero divisor other than the origin, and it is the centre and the abelianisation of the Lie algebra $\mathrm{G}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, of real dimension $8$ |
| $\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | a general element, $Q_\mu \in \mathbb{C}$ |
| $Q_\mu = q_\mu + iq'_\mu$ | the real and imaginary parts of a coefficient |
| $\mathbb{C}_{\mathbb{B}}$ | the centre subspace, the fixed space of quaternion conjugation |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, the anti-fixed space of quaternion conjugation |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, \flat$ | quaternion, complex, Hermitian conjugation and reversal |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | the algebraic square $N$ |
| $\mathbb{R}e_0$, $i\mathbb{R}e_0$ | the two coordinate lines of the centre subspace |
| $\xi$ | a root of $-1$ in $\mathbb{B}$, $\xi^2 = -1$ |
| $\tilde\Pi$ | an idempotent of $\mathbb{B}$; the centre contributes only $0$ and $e_0$ |

## Further Reading

- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the three decompositions and the definitions of the six subspaces
- *Biquaternion Multiplication* (`articles_maths/biquaternion-multiplication.md`), for the product of $\mathbb{B}$
- *Biquaternion Vector Subspace* (`articles_maths/biquaternion-vector-subspace.md`), the anti-fixed companion of the present subspace
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the intersections, the sums and the coordinate blocks of the six together
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions, their composition law and the two spaces each of them defines
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the classification of the idempotents, of which the centre carries only the trivial two
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the simplicity of $\mathbb{B}$ and the Peirce corners, none of which is central
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the classification whose two trivial points are the roots of the centre
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the two families of zero divisors, the centre contributing only the origin
- *Biquaternion Lie Algebra* (`articles_maths/biquaternion-lie-algebra.md`), for the centre of the Lie algebra $\mathrm{G}$ and its abelianisation
- *The Centre Subspace under the Three Topologies* (`articles_maths/the-centre-subspace-under-the-three-topologies.md`), for the subspace read under each of the three topologies
- *Jordan Algebras* (`articles_maths/jordan-algebras.md`), for the symmetrized product that gives the Hermitian subspace its algebraic structure
- *Biquaternion Jordan Algebra* (`articles_maths/biquaternion-jordan-algebra.md`), for the symmetrized product of $\mathbb{B}$ and the classification of the six subspaces under the two halves
