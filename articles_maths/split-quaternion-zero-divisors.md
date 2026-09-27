
# __Split-Quaternion Zero Divisors__

## Introduction

This article studies the zero divisors of the split-quaternion algebra. It defines them, proves the criterion that identifies them with the null cone of the norm form, exhibits the two families of maximal totally isotropic subspaces into which the null cone splits, proves the existence of nonzero nilpotents, and describes the distribution of the zero divisors among the distinguished subspaces.

The split-quaternion algebra, its norm form $N$, its idempotents $\tilde\pi_\pm$ and its subspaces $S$, $V$, $\mathbb{D}_2$, $\mathbb{D}_3$ are assumed from *Split-Quaternion Algebra*. The invertibility criterion is assumed from *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*; it is not re-proved here. The inertia law and the ruling of a quadric of a form of signature $(2,2)$ are assumed from *Quadratic Forms and Polarisation*. Nothing physical is invoked.

## Definition and Criterion

**Definition.** A nonzero element $\tilde q \in \mathbb{H}_{\mathrm{s}}$ is a **zero divisor** if there exists a nonzero $y \in \mathbb{H}_{\mathrm{s}}$ with $\tilde q y = 0$ or a nonzero $z \in \mathbb{H}_{\mathrm{s}}$ with $z\tilde q = 0$. The **zero divisor set** is

$$
Z = \{\tilde q \in \mathbb{H}_{\mathrm{s}} : \tilde q \neq 0 \text{ and } \tilde q \text{ is a zero divisor}\}.
$$

**Theorem (The Criterion).** Let $\tilde q$ be nonzero. Then $\tilde q$ is a zero divisor if and only if $N(\tilde q) = 0$. Equivalently, the zero divisor set is the null cone of the norm form with the origin removed:

$$
Z = \{\tilde q \neq 0 : N(\tilde q) = 0\}.
$$

**Proof.** The criterion is the corollary of the invertibility criterion proved in *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*: a nonzero element is a zero divisor exactly when it is not invertible, and it is invertible exactly when $N(\tilde q) \neq 0$. $\square$

The set

$$
\mathcal{N} = \{\tilde q : N(\tilde q) = 0\} = Z \cup \{0\}
$$

is the **null cone** of $N$. It is a cone: if $N(\tilde q) = 0$ then $N(\lambda \tilde q) = \lambda^2 N(\tilde q) = 0$ for every real $\lambda$. It is closed, it has real dimension $3$, and its only singular point is the origin; away from the origin it is a smooth three-dimensional cone. The complement of $Z$ in $\mathbb{H}_{\mathrm{s}} \setminus \{0\}$ is the set of units, an open dense set of full measure by *Split-Quaternion Norm and Invertibility*, §*Distribution of the Invertible Elements*.

The zero divisor set is **connected**. Indeed, every isotropic vector $\tilde q$ is a positive multiple of a vector $(\cos\alpha, \sin\alpha, \cos\beta, \sin\beta)$ by *Split-Quaternion Norm and Invertibility*, §*Isotropy*, and the parametrisation is continuous in the pair of angles; the set of isotropic vectors is therefore homeomorphic to a cone on a connected base, and removing the vertex leaves it connected.

## The Null Cone and the Maximal Isotropic Subspaces

The null cone is the union of the maximal totally isotropic subspaces of $N$.

**Definition.** A subspace $P \subseteq \mathbb{H}_{\mathrm{s}}$ is **totally isotropic** for $N$ if $N(\tilde q) = 0$ for every $\tilde q \in P$; it is **maximal** with that property if it is not contained in a larger totally isotropic subspace.

**Theorem (The Zero Divisors Lie in the Maximal Isotropic Subspaces).** A nonzero element is a zero divisor if and only if it lies in a maximal totally isotropic subspace, and every maximal totally isotropic subspace is two-dimensional. Consequently the zero divisor set is the union of the maximal totally isotropic subspaces with the origin removed.

**Proof.** Let $\tilde q \neq 0$ be isotropic. The left annihilator $P_{\tilde q} = \{\tilde a : \tilde a\tilde q = 0\}$ is a left ideal, since $\tilde a\tilde q = 0$ implies $\tilde b\tilde a\tilde q = 0$; it contains $\bar{\tilde q} \neq 0$, because $\tilde q\bar{\tilde q} = N(\tilde q) = 0$; and it is proper, because $\tilde q \neq 0$ excludes $\tilde a = 1$. A nonzero proper left ideal of $\mathbb{H}_{\mathrm{s}}$ is two-dimensional by *Split-Quaternion Ideals and Peirce Decomposition*, so $\dim P_{\tilde q} = 2$. Every $\tilde a \in P_{\tilde q}$ satisfies $\tilde a\tilde q = 0$ with $\tilde q \neq 0$, so $\tilde a$ is a left zero divisor or zero and $N(\tilde a) = 0$; hence $P_{\tilde q}$ is totally isotropic. Since the form has signature $(2,2)$ its Witt index is $2$, and no totally isotropic subspace exceeds dimension $2$ by the inertia law of *Quadratic Forms and Polarisation*, so $P_{\tilde q}$ is maximal and the isotropic line $\mathbb{R}\tilde q$ lies in one. Conversely an element of a totally isotropic subspace is isotropic, hence a zero divisor or zero. $\square$

## The Two Families

**Definition.** For an isotropic line $L = \mathbb{R}\tilde q$, the **left annihilator** and the **right annihilator** are

$$
\mathcal{K}_L = \{\tilde a : \tilde a\tilde q = 0\}, \qquad \mathcal{R}_L = \{\tilde a : \tilde q\tilde a = 0\},
$$

and each depends only on the line $L$ and not on the chosen representative $\tilde q$.

**Theorem (The Two Families).** For every isotropic line $L$ the subspaces $\mathcal{K}_L$ and $\mathcal{R}_L$ are two-dimensional, totally isotropic and maximal. Every maximal totally isotropic subspace of $\mathbb{H}_{\mathrm{s}}$ is a $\mathcal{K}_L$ or an $\mathcal{R}_L$. The collections

$$
\mathcal{K} = \{\mathcal{K}_L\}, \qquad \mathcal{R} = \{\mathcal{R}_L\},
$$

each parametrised by the projective line, are the **two families** of the null cone; the two families are disjoint.

**Proof.** The left annihilator is the left ideal $P_{\tilde q}$ of the preceding theorem, hence two-dimensional and totally isotropic. The right annihilator is the image of the left annihilator of $\bar{\tilde q}$ under the conjugation, which reverses the order of multiplication and preserves $N$, so it has the same properties. The condition $\tilde a(\lambda\tilde q) = 0$ for $\lambda \neq 0$ is the condition $\tilde a\tilde q = 0$, so the annihilator depends only on the isotropic line. A non-degenerate form of signature $(2,2)$ on $\mathbb{R}^4$ has Witt index $2$, and its two-dimensional totally isotropic subspaces fall into two families, each parametrised by a projective line; this is the standard ruling of a quadric of signature $(2,2)$ (*Quadratic Forms and Polarisation*). The two annihilator constructions realise the two families. $\square$

**Corollary (Each Isotropic Line Lies in One Plane of Each Family).** Through each isotropic line pass exactly two maximal totally isotropic subspaces, one from each family; the null cone is the union of the planes of the two families. Two planes of opposite families meet in a line, and two distinct planes of the same family meet only at the origin.

**Proof.** Every isotropic line consists of the multiples of one zero divisor, which by the preceding theorem lies in a maximal totally isotropic subspace; the incidence is the standard incidence of the ruling of the quadric of a form of signature $(2,2)$ (*Quadratic Forms and Polarisation*). $\square$

**Corollary (The Minimal Ideals Are Members of the Families).** Both minimal left ideals $\mathbb{H}_{\mathrm{s}}\tilde\pi_\pm$ are members of the family $\mathcal{K}$, and both minimal right ideals $\tilde\pi_\pm\mathbb{H}_{\mathrm{s}}$ are members of the family $\mathcal{R}$.

**Proof.** A left ideal is closed under left multiplication, so $\mathbb{H}_{\mathrm{s}}\tilde\pi_\pm$ is a left annihilator of the isotropic line it determines; it is two-dimensional by *Split-Quaternion Ideals and Peirce Decomposition* and totally isotropic by *Split-Quaternion Norm and Invertibility*, §*The Minimal Left and Right Ideals*. The right ideals are the images of left ideals under the conjugation and lie in $\mathcal{R}$. $\square$

**Corollary (The Anti-Automorphism $\tau$ Swaps the Families).** The assignment on the generators

$$
\tau(e_1) = -e_1, \qquad \tau(e_2) = e_2, \qquad \tau(e_3) = e_3
$$

extends to an involutive algebra anti-automorphism that preserves $N$ and interchanges the two families: $\tau(\mathcal{K}_L) \in \mathcal{R}$ and $\tau(\mathcal{R}_L) \in \mathcal{K}$ for every isotropic line $L$.

**Proof.** As for the conjugation the relations are checked on the generators, giving an anti-automorphism with $\tau^2 = \mathrm{id}$; and $N(\tau(\tilde q)) = q_0^2 + q_1^2 - q_2^2 - q_3^2 = N(\tilde q)$ for $\tilde q = q_0 + q_1e_1 + q_2e_2 + q_3e_3$, so $\tau$ preserves $N$. An anti-automorphism carries a left ideal to a right ideal and preserves total isotropy, so it carries a member of $\mathcal{K}$ to a member of $\mathcal{R}$; being an involution, it interchanges the families. $\square$

## Nonzero Nilpotents

**Definition.** A nonzero element $\tilde q$ is **nilpotent** if $\tilde q^2 = 0$.

**Theorem (The Nilpotents).** A nonzero element $\tilde q$ is nilpotent if and only if

$$
\tilde q \in V \quad \text{and} \quad N(\tilde q) = 0,
$$

that is, if and only if $\tilde q$ is a nonzero vector of the vector subspace lying on the light cone $q_1^2 = q_2^2 + q_3^2$. The set of nilpotents is therefore a two-dimensional cone, and in particular

$$
(e_1 + e_3)^2 = e_1^2 + e_1 e_3 + e_3 e_1 + e_3^2 = -1 + 0 + 1 = 0 .
$$

Every nilpotent is a zero divisor, and the nilpotents form a proper subset of the zero divisor set.

**Proof.** Write $\tilde q = q_0 + \mathbf v$ with $q_0 \in S$ and $\mathbf v \in V$. Since $e_1, e_2, e_3$ are traceless and the product of two distinct generators is the third with a sign, the square is

$$
\tilde q^2 = q_0^2 + 2q_0\mathbf v + \mathbf v^2 = q_0^2 + 2q_0\mathbf v - N(\mathbf v),
$$

where $\mathbf v^2 = -N(\mathbf v)$ is the identity for pure vectors recorded in (*Split-Quaternion Algebra*, §*The Restricted Form on the Vector Subspace*). If $\tilde q^2 = 0$, then comparing the components in $S$ and in $V$ gives $2q_0\mathbf v = 0$, so $q_0 = 0$ or $\mathbf v = 0$. If $\mathbf v = 0$ then $q_0^2 = 0$, so $q_0 = 0$ and $\tilde q = 0$, excluded by hypothesis; hence $q_0 = 0$ and $\tilde q = \mathbf v \in V$. Then $\tilde q^2 = -N(\tilde q)$, so $\tilde q^2 = 0$ exactly when $N(\tilde q) = 0$. Conversely every such $\tilde q$ has $\tilde q^2 = 0$. The computation for $e_1 + e_3$ uses $e_1 e_3 = -e_3 e_1$ and $e_1^2 = -1$, $e_3^2 = +1$. Every nilpotent satisfies $N(\tilde q)^2 = N(\tilde q^2) = 0$, hence $N(\tilde q) = 0$, so it is a zero divisor; the element $1 + e_2$ is a zero divisor with $N(1+e_2) = 0$ but $(1+e_2)^2 = 2(1+e_2) \neq 0$, so the inclusion is proper. $\square$

The nilpotent set is the light cone of the signature-$(2,1)$ form of $V$; by *Split-Quaternion Norm and Invertibility*, §*Isotropy*, its lines are the circle $\mathbb{R}(e_1 + \cos\theta\, e_2 + \sin\theta\, e_3)$.

### The Contrast with the Division Algebras

The existence of nilpotents is the sharpest structural contrast the category has.

**Theorem (No Nilpotents in the Division Algebras).** The quaternion algebra $\mathbb{H}$ has no nonzero nilpotent, and the eight-dimensional $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ has no nonzero nilpotent.

**Proof.** The quaternion algebra is a division algebra by *Quaternion Algebra*, so $\tilde q \neq 0$ implies $\tilde q$ invertible, and $\tilde q^2 = 0$ would give $\tilde q = 0$ after multiplying by $\tilde q^{-1}$. The eight-dimensional algebra is a product of two copies of $\mathbb{H}$ by the dictionary of *The Number Systems as Clifford Algebras*, and a nilpotent in a product of algebras would have a nilpotent component in one of the factors; a division algebra has none, so the product has none. $\square$

**Remark.** The comparison isolates the phenomenon. A **simple** real algebra with nilpotents, such as $\mathbb{H}_{\mathrm{s}}$, and a **semisimple, non-simple** product of division algebras without nilpotents, such as $\mathbb{H}_{\mathbb{D}}$, lie on opposite sides of the line that the nilpotent draws. The eight-dimensional algebra is treated later in Part V, under Split-Biquaternions; nothing of it is used here beyond the identification already stated in *The Number Systems as Clifford Algebras*.

## Distribution of the Zero Divisors

The zero divisors are distributed over the distinguished subspaces as follows. The subspaces are those of *Split-Quaternion Algebra*.

| Subspace | Zero divisors | Description |
|---|---|---|
| $S = \mathbb{R}\cdot 1$ | none | every nonzero scalar is a unit |
| $V$ | the nonzero vectors with $q_1^2 = q_2^2 + q_3^2$ | the light cone, a two-dimensional cone, every nonzero point of which is nilpotent |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ | the nonzero multiples of $1 \pm e_2$ | two isotropic lines |
| $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | the nonzero multiples of $1 \pm e_3$ | two isotropic lines |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$, $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ | the whole subspace minus the origin | four maximal isotropic planes |
| $\tilde\pi_\pm$ themselves | $\tilde\pi_+$ and $\tilde\pi_-$ | the two non-central idempotents |

The table is completed by the following observations.

**The vector subspace.** On $V$ the zero divisors are exactly the lightlike vectors, and by *Nonzero Nilpotents* they are exactly the nonzero nilpotents. Every zero divisor of $V$ has square zero; this is peculiar to the traceless part and does not hold in the whole algebra.

**The idempotents.** The idempotents $\tilde\pi_\pm = \tfrac12(1 \pm e_2)$ are zero divisors with $\tilde\pi_+ \tilde\pi_- = 0$; they are not nilpotent, since $\tilde\pi_\pm^2 = \tilde\pi_\pm \neq 0$. Together with $0$ and $1$ they are two of the idempotents of the algebra: the general non-scalar idempotent is $\tfrac12(1 \pm \eta)$ for a root $\eta$ of $+1$ in the vector subspace, a one-sheeted hyperboloid's worth of idempotents, as recorded in *Split-Quaternion Roots of Minus One*.

**The splitting.** The zero divisor set is connected, and it is the union of the planes of the two families of *The Two Families*. The nilpotent set is the two-dimensional subcone of $V$, and the non-scalar idempotents form a one-sheeted hyperboloid of points of the zero divisor set lying outside that subcone.

**Measure.** The zero divisor set is closed and has Lebesgue measure zero in $\mathbb{R}^4$, since it is the zero set of a nonconstant polynomial; the units are its open dense complement.

## Summary

A nonzero split-quaternion is a zero divisor exactly when $N(\tilde q) = 0$, and the zero divisor set is the null cone of the norm form with the origin removed, the union of the maximal totally isotropic subspaces with the origin removed.

The null cone splits into the two families of maximal totally isotropic subspaces, each parametrised by the projective line; each plane is two-dimensional and totally isotropic, and the two families are the two rulings of the projective null quadric. Every isotropic line lies in exactly one member of each family, the two families are exchanged by the anti-automorphism $\tau$, and the four minimal ideals of the algebra are members of the families.

The algebra has nonzero nilpotents: a nonzero element is nilpotent exactly when it lies in the vector subspace and on its light cone, and $(e_1 + e_3)^2 = 0$. The quaternion algebra and the eight-dimensional $\mathbb{H}_{\mathbb{D}}$ have no nonzero nilpotent, the first because it is a division algebra and the second because it is a product of division algebras. The zero divisor set is a connected three-dimensional cone of measure zero, the nilpotents form its two-dimensional subcone inside $V$, and the two non-central idempotents are two further points of it.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $Z$ | the zero divisor set $\{\tilde q \neq 0 : N(\tilde q) = 0\}$ | this article |
| $\mathcal{N}$ | the null cone $\{\tilde q : N(\tilde q) = 0\}$ | this article |
| $\mathbb{R}\tilde q$, $[\tilde q]$ | an isotropic line of the projective null quadric $Q$ | this article |
| $\mathcal{R}$, $\mathcal{K}$ | the two families of maximal isotropic subspaces | this article |
| $\mathcal{K}_L$, $\mathcal{R}_L$ | the left and right annihilators of an isotropic line $L$ | this article |
| $\tau$ | the anti-automorphism $e_1 \mapsto -e_1$, $e_2, e_3 \mapsto e_2, e_3$ | this article |
| nilpotent | nonzero $\tilde q$ with $\tilde q^2 = 0$ | this article |
| $\tilde\pi_\pm = \tfrac12(1 \pm e_2)$ | the non-central idempotents | *Split-Quaternion Algebra* |
| $N(\tilde q)$ | the norm form, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the coquaternions, their idempotents and their nilpotents.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for maximal isotropic subspaces and the ruling of the null quadric.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic forms, the inertia law and the geometry of the null cone.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split composition algebras and their zero divisors.
