
# __Split-Quaternion Zero Divisors__

## Introduction

This article studies the zero divisors of the split-quaternion algebra. It defines them, proves the criterion $N(\tilde q) = 0$ that identifies them with the null cone, exhibits the two families of minimal one-sided ideals into which the zero divisor set splits, proves the existence of nonzero nilpotents, and describes the distribution of the zero divisors among the distinguished subspaces.

The split-quaternion algebra, its central product $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ and its idempotents $\tilde\pi_\pm$ and subspaces $S$, $V$, $\mathbb{D}_2$, $\mathbb{D}_3$ are assumed from *Split-Quaternion Algebra*, and the metrical reading of $N$ from *Split-Quaternion Norm and Invertibility*. The invertibility criterion is assumed from *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*; it is not re-proved here. The ideal theory of $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ is assumed from *Split-Quaternion Ideals and Peirce Decomposition*. Nothing physical is invoked.

## Definition and Criterion

**Definition.** A nonzero element $\tilde q \in \mathbb{H}_{\mathrm{s}}$ is a **zero divisor** if there exists a nonzero $y \in \mathbb{H}_{\mathrm{s}}$ with $\tilde q y = 0$ or a nonzero $z \in \mathbb{H}_{\mathrm{s}}$ with $z\tilde q = 0$. The **zero divisor set** is

$$
Z = \{\tilde q \in \mathbb{H}_{\mathrm{s}} : \tilde q \neq 0 \text{ and } \tilde q \text{ is a zero divisor}\}.
$$

**Theorem (The Criterion).** Let $\tilde q$ be nonzero. Then $\tilde q$ is a zero divisor if and only if $N(\tilde q) = 0$. Equivalently, the zero divisor set is the null cone with the origin removed:

$$
Z = \{\tilde q \neq 0 : N(\tilde q) = 0\}.
$$

**Proof.** The criterion is the corollary of the invertibility criterion proved in *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*: a nonzero element is a zero divisor exactly when it is not invertible, and it is invertible exactly when $N(\tilde q) \neq 0$.

The set

$$
\mathcal{N} = \{\tilde q : N(\tilde q) = 0\} = Z \cup \{0\}
$$

is the **null cone** of the product $N$. It is a cone: if $N(\tilde q) = 0$ then $N(\lambda \tilde q) = \lambda^2 N(\tilde q) = 0$ for every real $\lambda$. It has real dimension $3$, the expected dimension of one equation in four real variables. That it is closed, that its only singular point is the origin, and that the complement of $Z$ in $\mathbb{H}_{\mathrm{s}} \setminus \{0\}$ is open, dense and of full measure are topological statements and belong to *Split-Quaternion Topology* and *Split-Quaternion Norm and Invertibility*, §*Distribution of the Invertible Elements*.

That the zero divisor set is connected is a topological statement and belongs to *Split-Quaternion Topology*. What is used here is the algebraic parametrisation of *Split-Quaternion Norm and Invertibility*, §*Isotropy*: every zero divisor $\tilde q$ is a positive multiple of a vector $(\cos\alpha, \sin\alpha, \cos\beta, \sin\beta)$.

## The Annihilator of a Zero Divisor

The zero divisors are exactly the elements with a nonzero annihilator: $\tilde q \neq 0$ is a zero divisor if and only if $\{\tilde a : \tilde a\tilde q = 0\}$ or $\{\tilde a : \tilde q\tilde a = 0\}$ is nonzero.

**Theorem (The Left Annihilator Is a Minimal Left Ideal).** Let $\tilde q \neq 0$ be a zero divisor. Then the left annihilator $P_{\tilde q} = \{\tilde a : \tilde a\tilde q = 0\}$ is a two-dimensional minimal left ideal, and the right annihilator is a two-dimensional minimal right ideal. Consequently the zero divisor set is the union of the nonzero elements of the minimal one-sided ideals, with the origin removed.

**Proof.** The left annihilator is a left ideal, since $\tilde a\tilde q = 0$ implies $\tilde b\tilde a\tilde q = 0$. It is nonzero: the central product is symmetric, $\tilde q\tilde{q}^{\natural} = \tilde{q}^{\natural}\tilde q = N(\tilde q)$, and $N(\tilde q) = 0$ by the criterion, so the conjugate $\tilde{q}^{\natural}$ is nonzero and lies in it. It is proper, because $1 \cdot \tilde q = \tilde q \neq 0$ excludes $\tilde a = 1$. In $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ every nonzero proper left ideal is a minimal left ideal and every minimal left ideal is two-dimensional, by *Split-Quaternion Ideals and Peirce Decomposition*; hence $P_{\tilde q}$ is two-dimensional and minimal. The right annihilator is the image of a left annihilator under the conjugation, which reverses the order of multiplication, so it is a two-dimensional minimal right ideal. Every nonzero element of a left annihilator $P_{\tilde q}$ satisfies $\tilde a\tilde q = 0$ with $\tilde q \neq 0$, hence is a zero divisor; conversely every zero divisor lies in its own annihilator. Since the annihilator depends only on the line $\mathbb{R}\tilde q$, the zero divisor set is the union of the nonzero elements of the minimal left and right ideals.

## The Two Families

**Definition.** For a zero-divisor line $L = \mathbb{R}\tilde q$, the **left annihilator** and the **right annihilator** are

$$
\mathcal{K}_L = \{\tilde a : \tilde a\tilde q = 0\}, \qquad \mathcal{R}_L = \{\tilde a : \tilde q\tilde a = 0\},
$$

and each depends only on the line $L$ and not on the chosen representative $\tilde q$.

**Theorem (The Two Families).** For every zero-divisor line $L$ the subspaces $\mathcal{K}_L$ and $\mathcal{R}_L$ are two-dimensional minimal one-sided ideals. Every minimal left ideal of $\mathbb{H}_{\mathrm{s}}$ is a $\mathcal{K}_L$ and every minimal right ideal is an $\mathcal{R}_L$. The collections

$$
\mathcal{K} = \{\mathcal{K}_L\}, \qquad \mathcal{R} = \{\mathcal{R}_L\},
$$

each parametrised by the projective line, are the **two families**; the two families are disjoint.

**Proof.** The left annihilator is the minimal left ideal $P_{\tilde q}$ of the preceding theorem, hence two-dimensional. The right annihilator is the image of the left annihilator of $\tilde{q}^{\natural}$ under the conjugation, which reverses the order of multiplication and preserves $N$, so it has the same properties. The condition $\tilde a(\lambda\tilde q) = 0$ for $\lambda \neq 0$ is the condition $\tilde a\tilde q = 0$, so the annihilator depends only on the zero-divisor line. The algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ has two families of minimal one-sided ideals, the left and the right, each parametrised by the projective line, by *Split-Quaternion Ideals and Peirce Decomposition*. The two annihilator constructions realise the two families.

**Corollary (Each Zero-Divisor Line Lies in One Ideal of Each Family).** Through each zero-divisor line pass exactly two minimal one-sided ideals, one from each family; the zero divisor set is the union of their nonzero elements. Two ideals of opposite families meet in a line, and two distinct ideals of the same family meet only at the origin.

**Proof.** Every zero-divisor line consists of the multiples of one zero divisor, which by the preceding theorem has a two-dimensional annihilator in each family; the incidence is that of the one-sided ideals of $M_2(\mathbb{R})$ (*Split-Quaternion Ideals and Peirce Decomposition*).

**Corollary (The Minimal Ideals Are Members of the Families).** Both minimal left ideals $\mathbb{H}_{\mathrm{s}}\tilde\pi_\pm$ are members of the family $\mathcal{K}$, and both minimal right ideals $\tilde\pi_\pm\mathbb{H}_{\mathrm{s}}$ are members of the family $\mathcal{R}$.

**Proof.** A left ideal is closed under left multiplication, so $\mathbb{H}_{\mathrm{s}}\tilde\pi_\pm$ is the left annihilator of a zero-divisor line; it is a two-dimensional minimal left ideal by *Split-Quaternion Ideals and Peirce Decomposition*. The right ideals are the images of left ideals under the conjugation and lie in $\mathcal{R}$.

**Corollary (The Anti-Automorphism $\tau$ Swaps the Families).** The assignment on the generators

$$
\tau(e_1) = -e_1, \qquad \tau(e_2) = e_2, \qquad \tau(e_3) = e_3
$$

extends to an involutive algebra anti-automorphism that preserves $N$ and interchanges the two families: $\tau(\mathcal{K}_L) \in \mathcal{R}$ and $\tau(\mathcal{R}_L) \in \mathcal{K}$ for every zero-divisor line $L$.

**Proof.** As for the conjugation the relations are checked on the generators, giving an anti-automorphism with $\tau^2 = \mathrm{id}$; and $N(\tau(\tilde q)) = q_0^2 + q_1^2 - q_2^2 - q_3^2 = N(\tilde q)$ for $\tilde q = q_0 + q_1e_1 + q_2e_2 + q_3e_3$, so $\tau$ preserves $N$. An anti-automorphism carries a left ideal to a right ideal and preserves minimality, so it carries a member of $\mathcal{K}$ to a member of $\mathcal{R}$; being an involution, it interchanges the families.

## Nonzero Nilpotents

**Definition.** A nonzero element $\tilde q$ is **nilpotent** if $\tilde q^2 = 0$.

**Theorem (The Nilpotents).** A nonzero element $\tilde q$ is nilpotent if and only if

$$
\tilde q \in V \quad \text{and} \quad N(\tilde q) = 0,
$$

that is, if and only if $\tilde q$ is a nonzero vector of the vector subspace lying on the level set $N = 0$, $q_1^2 = q_2^2 + q_3^2$. The set of nilpotents is therefore a two-dimensional cone, and in particular

$$
(e_1 + e_3)^2 = e_1^2 + e_1 e_3 + e_3 e_1 + e_3^2 = -1 + 0 + 1 = 0 .
$$

Every nilpotent is a zero divisor, and the nilpotents form a proper subset of the zero divisor set.

**Proof.** Write $\tilde q = q_0 + \mathbf v$ with $q_0 \in S$ and $\mathbf v \in V$. Since $e_1, e_2, e_3$ are traceless and the product of two distinct generators is the third with a sign, the square is

$$
\tilde q^2 = q_0^2 + 2q_0\mathbf v + \mathbf v^2 = q_0^2 + 2q_0\mathbf v - N(\mathbf v),
$$

where $\mathbf v^2 = -N(\mathbf v)$ is the identity for pure vectors recorded in (*Split-Quaternion Norm and Invertibility*, §*The Split-Quaternion Norm*). If $\tilde q^2 = 0$, then comparing the components in $S$ and in $V$ gives $2q_0\mathbf v = 0$, so $q_0 = 0$ or $\mathbf v = 0$. If $\mathbf v = 0$ then $q_0^2 = 0$, so $q_0 = 0$ and $\tilde q = 0$, excluded by hypothesis; hence $q_0 = 0$ and $\tilde q = \mathbf v \in V$. Then $\tilde q^2 = -N(\tilde q)$, so $\tilde q^2 = 0$ exactly when $N(\tilde q) = 0$. Conversely every such $\tilde q$ has $\tilde q^2 = 0$. The computation for $e_1 + e_3$ uses $e_1 e_3 = -e_3 e_1$ and $e_1^2 = -1$, $e_3^2 = +1$. Every nilpotent satisfies $N(\tilde q)^2 = N(\tilde q^2) = 0$, hence $N(\tilde q) = 0$, so it is a zero divisor; the element $1 + e_2$ is a zero divisor with $N(1+e_2) = 0$ but $(1+e_2)^2 = 2(1+e_2) \neq 0$, so the inclusion is proper.

The nilpotent set is the level set $N = 0$ in $V$; by *Split-Quaternion Norm and Invertibility*, §*Isotropy*, its lines are the curve $\mathbb{R}(e_1 + \cos\theta\, e_2 + \sin\theta\, e_3)$.

### The Contrast with the Division Algebras

The existence of nilpotents is the sharpest structural contrast the category has.

**Theorem (No Nilpotents in the Division Algebras).** The quaternion algebra $\mathbb{H}$ has no nonzero nilpotent, and the eight-dimensional $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ has no nonzero nilpotent.

**Proof.** The quaternion algebra is a division algebra by *Quaternion Algebra*, so $\tilde q \neq 0$ implies $\tilde q$ invertible, and $\tilde q^2 = 0$ would give $\tilde q = 0$ after multiplying by $\tilde q^{-1}$. The eight-dimensional algebra is a product of two copies of $\mathbb{H}$ by the dictionary of *The Number Systems as Clifford Algebras*, and a nilpotent in a product of algebras would have a nilpotent component in one of the factors; a division algebra has none, so the product has none.

**Remark.** The comparison isolates the phenomenon. A **simple** real algebra with nilpotents, such as $\mathbb{H}_{\mathrm{s}}$, and a **semisimple, non-simple** product of division algebras without nilpotents, such as $\mathbb{H}_{\mathbb{D}}$, lie on opposite sides of the line that the nilpotent draws. The eight-dimensional algebra is treated later in Part V, under Split-Biquaternions; nothing of it is used here beyond the identification already stated in *The Number Systems as Clifford Algebras*.

## Distribution of the Zero Divisors

The zero divisors are distributed over the distinguished subspaces as follows. The subspaces are those of *Split-Quaternion Algebra*.

| Subspace | Zero divisors | Description |
|---|---|---|
| $S = \mathbb{R}\cdot 1$ | none | every nonzero scalar is a unit |
| $V$ | the nonzero vectors with $q_1^2 = q_2^2 + q_3^2$ | the level set $N = 0$, a two-dimensional cone, every nonzero point of which is nilpotent |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$ | the nonzero multiples of $1 \pm e_2$ | two zero-divisor lines |
| $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | the nonzero multiples of $1 \pm e_3$ | two zero-divisor lines |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$, $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ | the whole subspace minus the origin | four minimal one-sided ideals |
| $\tilde\pi_\pm$ themselves | $\tilde\pi_+$ and $\tilde\pi_-$ | the two non-central idempotents |

The table is completed by the following observations.

**The vector subspace.** On $V$ the zero divisors are exactly the lightlike vectors, and by *Nonzero Nilpotents* they are exactly the nonzero nilpotents. Every zero divisor of $V$ has square zero; this is peculiar to the traceless part and does not hold in the whole algebra.

**The idempotents.** The idempotents $\tilde\pi_\pm = \tfrac12(1 \pm e_2)$ are zero divisors with $\tilde\pi_+ \tilde\pi_- = 0$; they are not nilpotent, since $\tilde\pi_\pm^2 = \tilde\pi_\pm \neq 0$. Together with $0$ and $1$ they are two of the idempotents of the algebra: the general non-scalar idempotent is $\tfrac12(1 \pm \eta)$ for a root $\eta$ of $+1$ in the vector subspace, a one-sheeted hyperboloid's worth of idempotents, as recorded in *Split-Quaternion Roots of Minus One*.

**The splitting.** The zero divisor set is the union of the planes of the two families of *The Two Families*. The nilpotent set is the two-dimensional subcone of $V$, and the non-scalar idempotents form a further two-dimensional set of points of the zero divisor set lying outside that subcone.

**Measure.** That the zero divisor set is closed, that it has measure zero in $\mathbb{R}^4$, and that the units are open and dense are topological and measure-theoretic statements and belong to *Split-Quaternion Topology*; what is used here is only that the zero divisor set is the vanishing set of the single polynomial $N$.

## Summary

A nonzero split-quaternion is a zero divisor exactly when $N(\tilde q) = 0$, that is, when $\tilde q\tilde{q}^{\natural} = 0$, and the zero divisor set is the null cone with the origin removed, the union of the minimal one-sided ideals with the origin removed.

The zero divisor set splits into the two families of minimal one-sided ideals, each parametrised by the projective line; each ideal is two-dimensional and minimal, and the two families are the two rulings of the projective zero set. Every zero-divisor line lies in exactly one member of each family, the two families are exchanged by the anti-automorphism $\tau$, and the four minimal ideals of the algebra are members of the families.

The algebra has nonzero nilpotents: a nonzero element is nilpotent exactly when it lies in the vector subspace and on the level set $N = 0$, and $(e_1 + e_3)^2 = 0$. The quaternion algebra and the eight-dimensional $\mathbb{H}_{\mathbb{D}}$ have no nonzero nilpotent, the first because it is a division algebra and the second because it is a product of division algebras. The zero divisor set is a connected three-dimensional cone of measure zero, the nilpotents form its two-dimensional subcone inside $V$, and the two non-central idempotents are two further points of it.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $Z$ | the zero divisor set $\{\tilde q \neq 0 : N(\tilde q) = 0\}$ | this article |
| $\mathcal{N}$ | the null cone $\{\tilde q : N(\tilde q) = 0\}$ | this article |
| $\mathbb{R}\tilde q$, $[\tilde q]$ | a zero-divisor line of the projective zero set $Q$ | this article |
| $\mathcal{R}$, $\mathcal{K}$ | the two families of minimal one-sided ideals | this article |
| $\mathcal{K}_L$, $\mathcal{R}_L$ | the left and right annihilators of a zero-divisor line $L$ | this article |
| $\tau$ | the anti-automorphism $e_1 \mapsto -e_1$, $e_2, e_3 \mapsto e_2, e_3$ | this article |
| nilpotent | nonzero $\tilde q$ with $\tilde q^2 = 0$ | this article |
| $\tilde\pi_\pm = \tfrac12(1 \pm e_2)$ | the non-central idempotents | *Split-Quaternion Algebra* |
| $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ | the central product, formed algebraically; the metrical reading is in *Split-Quaternion Norm and Invertibility* | *Split-Quaternion Algebra* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the coquaternions, their idempotents and their nilpotents.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for maximal isotropic subspaces and the ruling of the null quadric.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for isotropic forms, the inertia law and the geometry of the null cone.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split composition algebras and their zero divisors.
