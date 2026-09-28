
# __Split-Quaternion Algebra__

## Introduction

This article introduces the split-quaternion algebra as an algebraic structure. It defines the algebra, describes the conjugations and their fixed-point subspaces, the idempotents and the distinguished subspaces, and the Lie algebra structure. It closes with a comparison with the quaternions $\mathbb{H}$ and with the split-biquaternions $\mathbb{H}_{\mathbb{D}}$.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The inner product of the algebra is formed and evaluated here as an algebraic pairing — its scalar, its vanishing and its non-degeneracy; nothing is measured with it, and the theory of norms, forms and signatures belongs to the Topology group (*Split-Quaternion Norm and Invertibility*). The quaternion algebra is assumed from *Quaternion Algebra*; the split-complex algebra and its idempotents from *Split-Complex Algebra*; the Clifford algebra $\mathrm{Cl}_{p,q}$ and its low-dimensional classification from *Clifford Algebras in Finite Dimensions* and *The Number Systems as Clifford Algebras*. The rotations, the Lorentz group and the hyperbolic geometry that the algebra carries are not treated here; they belong to *Split-Quaternion Rotations and the Lorentz Group*, *Split-Quaternion Geometry* and *Split-Quaternions and Hyperbolic Geometry*.

## The Split-Quaternion Algebra

### Definition

The **split-quaternion algebra** $\mathbb{H}_{\mathrm{s}}$ is the four-dimensional real algebra with basis

$$
1, \qquad e_1, \qquad e_2, \qquad e_3,
$$

and multiplication rules

$$
e_1^2 = -1, \qquad e_2^2 = +1, \qquad e_3 = e_1 e_2, \qquad e_1 e_2 = -e_2 e_1.
$$

A general split-quaternion is written in developed form as

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R},
$$

or, more compactly, as

$$
\tilde q = \sum_{\mu=0}^{3} q_\mu e_\mu, \qquad e_0 = 1.
$$

The real number $q_0$ is the **scalar part**, and the triple $(q_1, q_2, q_3)$ is the **vector part**. We also write

$$
\tilde q = q_0 + \mathbf{v}, \qquad \mathbf{v} = q_1 e_1 + q_2 e_2 + q_3 e_3,
$$

and we write $\operatorname{Sc}(\tilde q) = q_0$ and $\operatorname{Vec}(\tilde q) = \mathbf{v}$ for the two components.

The four elements $1, e_1, e_2, e_3$ are linearly independent over $\mathbb{R}$ by definition, so $\dim_{\mathbb{R}} \mathbb{H}_{\mathrm{s}} = 4$. The unit is $1$, and every element is a real linear combination of the basis elements.

### The Multiplication Table

The rules of the definition determine the whole multiplication table. From $e_3 = e_1 e_2$ and $e_1 e_2 = -e_2 e_1$ one computes

$$
e_3^2 = e_1 e_2 e_1 e_2 = -e_1^2 e_2^2 = -(-1)(+1) = +1,
$$

$$
e_2 e_3 = e_2 e_1 e_2 = -e_1 e_2^2 = -e_1, \qquad e_3 e_2 = e_1 e_2 e_2 = +e_1,
$$

$$
e_3 e_1 = e_1 e_2 e_1 = -e_1^2 e_2 = +e_2, \qquad e_1 e_3 = e_1 e_1 e_2 = -e_2.
$$

The products are collected in the following table, whose entry in row $i$ and column $j$ is $e_i e_j$.

| | $1$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $1$ | $1$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-1$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $+1$ | $-e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $e_1$ | $+1$ |

The table is read off from the definition; the entry $e_1 e_3 = -e_2$, for instance, is the identity $e_1 e_3 = e_1 e_1 e_2 = -e_2$.

### Basic Properties

**Associative.** Split-quaternion multiplication is associative. It suffices to check the associativity of the generating products, since the product is defined by bilinear extension of the table; the four elements $1, e_1, e_2, e_3$ satisfy the relations of the Clifford algebra $\mathrm{Cl}_{1,1}$, and every Clifford algebra is associative.

**Non-commutative.** Split-quaternion multiplication is not commutative: $e_1 e_2 = e_3$ while $e_2 e_1 = -e_3$. The centre is computed in *The Centre and Simplicity* below, and it is one-dimensional.

**Not a division algebra.** The element $1 + e_2$ is nonzero and

$$
(1 + e_2)(1 - e_2) = 1 - e_2^2 = 0,
$$

so $1 + e_2$ and $1 - e_2$ are nonzero zero divisors. The algebra therefore has zero divisors and is not a division algebra. Frobenius' theorem, recalled in *Normed Division Algebras and the Hurwitz Theorem*, states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$; the split-quaternion algebra is a fourth four-dimensional associative real algebra, and the failure of the division property is exactly the appearance of the zero divisors above. The zero divisor set is the subject of *Split-Quaternion Zero Divisors*.

**The matrix model.** The algebra is isomorphic to the algebra of $2\times2$ real matrices: the low-dimensional Clifford classification gives

$$
\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})
$$

(*The Number Systems as Clifford Algebras*), and this abstract identification is used throughout the category, in the ideal theory of *Split-Quaternion Ideals and Peirce Decomposition*, in the idempotent theory of *Split-Quaternion Idempotents and Projections*, and in the spectral and exponential theory of the later articles.

## Conjugations and Fixed-Point Subspaces

### The Conjugation

**Definition.** The **split-quaternion conjugation** is the map

$$
\bar{\tilde q} = q_0 - q_1 e_1 - q_2 e_2 - q_3 e_3 .
$$

It negates the three vector basis elements and fixes the scalars.

**Proposition.** The conjugation is an involutive algebra anti-automorphism: it is $\mathbb{R}$-linear, it satisfies $\overline{\tilde q y} = \bar{y}\, \bar{\tilde q}$ and $\overline{\bar{\tilde q}} = \tilde q$, and its fixed-point set is the scalar line $\mathbb{R}$.

**Proof.** Linearity and the second identity are immediate from the definition. For the anti-automorphism property it suffices to check the generators: $\overline{e_1 e_2} = \overline{e_3} = -e_3$, while $\bar{e}_2 \bar{e}_1 = (-e_2)(-e_1) = e_2 e_1 = -e_3$, and the other products are similar. The fixed points satisfy $q_1 e_1 + q_2 e_2 + q_3 e_3 = -(q_1 e_1 + q_2 e_2 + q_3 e_3)$, hence $q_1 = q_2 = q_3 = 0$.

### The Two Eigenspaces

Since $\bar{\cdot}$ is an involutive linear map, the algebra decomposes into its $+1$ and $-1$ eigenspaces:

$$
\mathbb{H}_{\mathrm{s}} = S \oplus V, \qquad
S = \{\tilde q : \bar{\tilde q} = \tilde q\} = \mathbb{R} \cdot 1, \qquad
V = \{\tilde q : \bar{\tilde q} = -\tilde q\} = \operatorname{span}\{e_1, e_2, e_3\}.
$$

The **scalar subspace** $S$ is one-dimensional and is a subalgebra isomorphic to $\mathbb{R}$; it is the centre, as *The Centre and Simplicity* below shows. The **vector subspace** $V$ is three-dimensional, it is not a subalgebra, and it is the natural home of the geometry of the system. Every element decomposes uniquely as

$$
\tilde q = \tfrac{1}{2}(\tilde q + \bar{\tilde q}) + \tfrac{1}{2}(\tilde q - \bar{\tilde q}),
$$

the first summand lying in $S$ and the second in $V$.

### The Other Two Involutions

Two further involutions act on the algebra, and they are recorded here because the subspaces of *Split-Quaternion Subspaces and the Involutions* are cut out by them. The **principal involution** $\alpha$ is the algebra automorphism defined on the generators by

$$
\alpha(e_1) = -e_1, \qquad \alpha(e_2) = -e_2, \qquad \alpha(e_3) = e_3,
$$

and the **reversal** $\rho$ is the algebra anti-automorphism defined by

$$
\rho(e_1) = e_1, \qquad \rho(e_2) = e_2, \qquad \rho(e_3) = -e_3 .
$$

Both are involutions, they commute, and their composite is the conjugation: $\bar{\tilde q} = \alpha(\rho(\tilde q)) = \rho(\alpha(\tilde q))$. Because they commute, each preserves the eigenspaces of the other, and the algebra decomposes into their common eigenspaces. The two involutions do not separate $e_1$ from $e_2$, however: $\alpha$ acts as $-1$ on the whole plane $\operatorname{span}\{e_1,e_2\}$, and $\rho$ acts as $+1$ on that plane, so the common eigenspaces are

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R} \cdot 1 \oplus \operatorname{span}\{e_1,e_2\} \oplus \mathbb{R} e_3,
$$

of dimensions $1, 2, 1$, the sign pair $(\alpha,\rho)$ being $(+,+)$ on $\mathbb{R}\cdot 1$, $(-,+)$ on $\operatorname{span}\{e_1,e_2\}$ and $(+,-)$ on $\mathbb{R}e_3$. This is the finest decomposition produced by the three involutions: on $\operatorname{span}\{e_1,e_2\}$ all three act as $-1$, so no eigenspace of any of them splits that plane. The eigenspaces of the involutions taken one at a time are the ones used in *Split-Quaternion Analysis*: the principal involution has $+1$ on $\operatorname{span}\{1,e_3\}$ and $-1$ on $\operatorname{span}\{e_1,e_2\}$; the reversal has $+1$ on $\operatorname{span}\{1,e_1,e_2\}$ and $-1$ on $\mathbb{R}e_3$; and the conjugation has $+1$ on $\mathbb{R}\cdot 1$ and $-1$ on $V$.

## The Inner Product

The **inner product** of two split-quaternions is the real scalar

$$
B(\tilde q, y) = \operatorname{Sc}(\tilde q\, \bar y) = q_0 q_0' + q_1 q_1' - q_2 q_2' - q_3 q_3',
$$

for $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ and $y = q_0' e_0 + q_1' e_1 + q_2' e_2 + q_3' e_3$. It is symmetric and bilinear, and it is **non-degenerate**: if $B(\tilde q, y) = 0$ for every $y$, then $\tilde q = 0$, since testing against the units gives $q_\mu = 0$.

Forming the inner product, evaluating it to a scalar and asking when it vanishes is all that is done with it here. Its diagonal value is the product

$$
B(\tilde q, \tilde q) = \tilde q \bar{\tilde q} = q_0^2 + q_1^2 - q_2^2 - q_3^2,
$$

which lies in the centre $S$ and is multiplicative, $(\tilde q y)\overline{(\tilde q y)} = (\tilde q\bar{\tilde q})(y\bar y)$, because $\tilde q\bar{\tilde q}$ is central. The equation $\tilde q\bar{\tilde q} = 0$, equivalently $B(\tilde q,\tilde q) = 0$, is the algebraic condition that decides the zero divisors, and the elements on which it holds are studied in *Split-Quaternion Zero Divisors*. No length, no sign and no orthogonal or orthonormal decomposition is read from the inner product in this article; the metrical reading — the signature of the pairings, their isotropy, the resulting classification of the elements and the group of units — is in *Split-Quaternion Norm and Invertibility*.

## The Idempotents and the Split-Complex Subspaces

### The Idempotents

**Definition.** The two elements

$$
\tilde\pi_+ = \tfrac{1}{2}(1 + e_2), \qquad \tilde\pi_- = \tfrac{1}{2}(1 - e_2)
$$

are the **split-quaternion idempotents**.

**Theorem.** The elements $\tilde\pi_+$ and $\tilde\pi_-$ satisfy

$$
\tilde\pi_+^2 = \tilde\pi_+, \qquad \tilde\pi_-^2 = \tilde\pi_-, \qquad \tilde\pi_+ \tilde\pi_- = \tilde\pi_- \tilde\pi_+ = 0, \qquad \tilde\pi_+ + \tilde\pi_- = 1,
$$

and they are not central. Moreover

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_-
$$

is a direct sum of two minimal left ideals of real dimension $2$, and the corresponding statement holds on the right, $\mathbb{H}_{\mathrm{s}} = \tilde\pi_+ \mathbb{H}_{\mathrm{s}} \oplus \tilde\pi_- \mathbb{H}_{\mathrm{s}}$. The decomposition is a decomposition of left modules and not of algebras: the subalgebra generated by $\tilde\pi_+$ and $\tilde\pi_-$ is two-dimensional and is not the whole algebra.

**Proof.** The four identities are the computation

$$
\tilde\pi_+^2 = \tfrac{1}{4}(1 + 2e_2 + e_2^2) = \tfrac{1}{4}(2 + 2e_2) = \tilde\pi_+,
$$

and its analogue for $\tilde\pi_-$, together with $\tilde\pi_+\tilde\pi_- = \tfrac14(1 - e_2^2) = 0$ and $\tilde\pi_+ + \tilde\pi_- = 1$. For non-centrality, $e_1 \tilde\pi_+ = \tfrac12(e_1 + e_3)$ while $\tilde\pi_+ e_1 = \tfrac12(e_1 - e_3)$, so $e_1 \tilde\pi_+ \neq \tilde\pi_+ e_1$. An element $\tilde q \tilde\pi_+$ of the first summand is fixed by right multiplication by $\tilde\pi_+$, since $\tilde q \tilde\pi_+ \tilde\pi_+ = \tilde q \tilde\pi_+$, and the map $\tilde q \mapsto \tilde q \tilde\pi_+$ has image of dimension $2$ because its kernel is $\mathbb{H}_{\mathrm{s}} \tilde\pi_-$. The sum $\mathbb{H}_{\mathrm{s}} \tilde\pi_+ + \mathbb{H}_{\mathrm{s}} \tilde\pi_-$ is all of $\mathbb{H}_{\mathrm{s}}$, since $\tilde q = \tilde q(\tilde\pi_+ + \tilde\pi_-)$, and the intersection is zero: if $\tilde q \tilde\pi_+ = y \tilde\pi_-$ then multiplying on the right by $\tilde\pi_+$ gives $\tilde q \tilde\pi_+ = 0$. Hence the sum is direct, and each summand is a minimal left ideal, as the idempotent theory of *Split-Quaternion Idempotents and Projections* shows. The final claim holds because $\tilde\pi_+ \tilde\pi_- = 0$ and the span of $\tilde\pi_+, \tilde\pi_-$ has dimension $2$.

### The Split-Complex Subspaces

The line $\mathbb{R} \cdot 1$ together with either of the two square-$+1$ generators spans a copy of the split-complex algebra inside $\mathbb{H}_{\mathrm{s}}$:

$$
\mathbb{D}_2 = \operatorname{span}\{1, e_2\} \cong \mathbb{D}, \qquad
\mathbb{D}_3 = \operatorname{span}\{1, e_3\} \cong \mathbb{D},
$$

where $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ is the split-complex algebra of *Split-Complex Algebra*. Both are commutative subalgebras, both have the two idempotents $\tfrac12(1 \pm e_2)$ and $\tfrac12(1 \pm e_3)$ respectively, and both carry the zero divisors $1 \pm e_2$ and $1 \pm e_3$. The whole algebra is generated by $\mathbb{D}_2$ together with the single element $e_1$:

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{D}_2 \oplus \mathbb{D}_2 e_1 , \qquad e_1 d = \bar{d} e_1 \ \ (d \in \mathbb{D}_2),
$$

which exhibits $\mathbb{H}_{\mathrm{s}}$ as a two-dimensional module over the split-complex algebra with a conjugation-twisted multiplication. The idempotents $\tilde\pi_\pm$ of the algebra are the idempotents of the subalgebra $\mathbb{D}_2$; they are non-central in $\mathbb{H}_{\mathrm{s}}$ precisely because $e_1$ does not commute with $e_2$.

## The Centre and Simplicity

**Theorem (The Centre).** The centre of $\mathbb{H}_{\mathrm{s}}$ is the scalar line:

$$
Z(\mathbb{H}_{\mathrm{s}}) = \{\tilde q : \tilde q y = y\tilde q \ \text{for all} \ y\} = \mathbb{R} \cdot 1 .
$$

**Proof.** The scalars are central. Conversely, suppose $\tilde q = q_0 + \mathbf{v}$ is central. Commuting $\tilde q$ with $e_1$ gives

$$
0 = \tilde q e_1 - e_1 \tilde q .
$$

The scalar part of $\tilde q$ commutes with everything, so the condition is $\mathbf{v} e_1 - e_1 \mathbf{v} = 0$. Writing $\mathbf{v} = q_1 e_1 + q_2 e_2 + q_3 e_3$ and using the table,

$$
\mathbf{v} e_1 = -q_1 - q_2 e_3 + q_3 e_2, \qquad e_1 \mathbf{v} = -q_1 + q_2 e_3 - q_3 e_2,
$$

so $\mathbf{v} e_1 - e_1 \mathbf{v} = -2q_2 e_3 + 2q_3 e_2 = 0$, giving $q_2 = q_3 = 0$. Commuting with $e_2$ similarly gives $q_1 = 0$. Hence $\mathbf{v} = 0$ and $\tilde q = q_0$ is scalar.

**Theorem (Simplicity).** The split-quaternion algebra is **simple**: it has no two-sided ideal other than $0$ and the algebra itself.

**Proof.** Let $I \neq 0$ be a two-sided ideal and let $0 \neq x \in I$. If $x\bar{x} \neq 0$ then $x$ is a unit, by the invertibility criterion of *Split-Quaternion Norm and Invertibility*, so $I = \mathbb{H}_{\mathrm{s}}$. If $x\bar{x} = 0$, then for every real $\lambda$ the element $x + \lambda$ lies in $I$ and

$$
(x + \lambda)\overline{(x + \lambda)} = x\bar{x} + 2\lambda \operatorname{Sc}(x) + \lambda^2 = \lambda\big(2\operatorname{Sc}(x) + \lambda\big),
$$

which is nonzero for every $\lambda$ outside the two-element set $\{0, -2\operatorname{Sc}(x)\}$. Choosing such a $\lambda$ exhibits a unit in $I$, so again $I = \mathbb{H}_{\mathrm{s}}$. Hence the only two-sided ideals are $0$ and the algebra.

The algebra is thus **associative, non-commutative, simple**, with centre $\mathbb{R}$, and it is **not** a division algebra. The combination — associative, non-commutative, simple, centre $\mathbb{R}$, and not a division algebra — is the one the comparisons below set against the quaternions and the split-biquaternions.

## The Lie Algebra Structure

The algebra carries the commutator bracket $[\tilde q, y] = \tilde q y - y\tilde q$, which makes it a real Lie algebra. The bracket of two elements of $V$ lies in $V$, since

$$
[e_1, e_2] = 2 e_3, \qquad [e_2, e_3] = -2 e_1, \qquad [e_3, e_1] = 2 e_2 .
$$

So $V$ is a three-dimensional Lie subalgebra of $\mathbb{H}_{\mathrm{s}}$, and the displayed relations are those of the three-dimensional simple real Lie algebra $\mathrm{SL}_2(\mathbb{R})$; the bracket algebra on $V$ is therefore $\mathrm{SL}_2(\mathbb{R})$. This is the algebraic origin of the relation between the split-quaternions and the Lorentz group: the vector subspace is a Lie algebra of infinitesimal Lorentz transformations, and the exponential of the bracket gives the rotations of *Split-Quaternion Rotations and the Lorentz Group*.

The scalar line $S$ is the centre of $\mathbb{H}_{\mathrm{s}}$ and therefore contributes nothing to the bracket. The full Lie algebra $\mathbb{H}_{\mathrm{s}}$ is the direct sum of the bracket algebra on $V$ and a central scalar line.

## Comparison with $\mathbb{H}$ and with $\mathbb{H}_{\mathbb{D}}$

### Comparison with the Quaternions

The split-quaternions and the quaternions are the two real forms of the same complexified algebra, and they differ in the sign of one generator. The following table collects the contrast; the quaternion column is supported by *Quaternion Algebra*.

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ |
|---|---|---|
| basis and squares | $e_1^2=e_2^2=e_3^2=-1$ | $e_1^2=-1$, $e_2^2=e_3^2=+1$ |
| diagonal product $\tilde q\bar{\tilde q}$ | $q_0^2+q_1^2+q_2^2+q_3^2$ | $q_0^2+q_1^2-q_2^2-q_3^2$ |
| zero divisors | none | yes |
| nonzero nilpotents | none | yes |
| division algebra | yes | no |
| centre | $\mathbb{R}$ | $\mathbb{R}$ |
| vector subspace | $\mathbb{R}^3$, $\mathrm{SO}(3)$ | $V$, $\mathrm{SL}_2(\mathbb{R})$ |
| scalar group attached | $Sp(1) \cong SU(2)$ | $\mathrm{SL}_2(\mathbb{R})$ |

The decisive difference is the sign in the diagonal product. For a nonzero quaternion the diagonal product is positive, so the elements of diagonal product $1$ form the compact three-sphere $Sp(1) \cong SU(2)$, double-covering $\mathrm{SO}(3)$. For a nonzero split-quaternion the diagonal product takes both signs, so the elements of diagonal product $1$ form the non-compact group $\mathrm{SL}_2(\mathbb{R})$. The change of a single sign turns a compact three-sphere into a non-compact three-dimensional group. The metrical statements that follow from this — the signatures, the definiteness in the quaternion case and the indefiniteness in the split case, and the groups they define — are treated in *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Rotations and the Lorentz Group*.

### Comparison with the Split-Biquaternions

The name *split quaternions* is used in the classical literature for the four-dimensional algebra $\mathrm{Cl}_{1,1}$ of this article, and it is not the algebra that the corpus writes $\mathbb{H}_{\mathbb{D}}$. The corpus reserves $\mathbb{H}_{\mathbb{D}}$ for the eight-dimensional tensor product $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$, the **split-biquaternions**; the distinction is stated once, in *The Number Systems as Clifford Algebras*, and is recorded again in *Examples of Algebras* and in *List of Algebras by Dimension*. The two algebras must not be identified, and the following table records why.

| | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|
| dimension over $\mathbb{R}$ | $4$ | $8$ |
| isomorphic to | $\mathrm{Cl}_{1,1}$ | $\mathrm{Cl}_{0,3}$ |
| simple | yes | no |
| centre | $\mathbb{R}$ | $\mathbb{D}$ |
| idempotents | non-central only | central, $e_\pm$ |
| nonzero nilpotents | yes | no |

The two rows that separate the algebras most sharply are the last two. A nilpotent is an element $\tilde q \neq 0$ with $\tilde q^2 = 0$, and the split-quaternion algebra has them: $(e_1 + e_3)^2 = e_1^2 + e_1e_3 + e_3e_1 + e_3^2 = -1 + 0 + 1 = 0$, since $e_1 e_3 = -e_3 e_1$. An algebra that is a product of two division algebras, as $\mathbb{H}_{\mathbb{D}}$ is by the dictionary of *The Number Systems as Clifford Algebras*, has no nilpotents at all, because a nilpotent would have a nilpotent component in one of the factors and a division algebra has none. Simultaneously, the split-quaternion algebra is **simple**, while a product of two algebras is not. A **simple** algebra with nilpotents and non-central idempotents is therefore entirely different from a **semisimple, non-simple** product of two division algebras with central idempotents and no nilpotents.

The eight-dimensional relative of the corpus is treated later in Part V, under Split-Biquaternions; nothing in it is used here. What is stated here is stated from the algebra of this article and from the conventions: a four-dimensional simple real algebra with zero divisors and non-central idempotents, on the one hand, and the eight-dimensional $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table, on the other.

## Summary

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ is the four-dimensional real algebra with basis $1, e_1, e_2, e_3$, the products $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$, the anticommutation $e_1 e_2 = -e_2 e_1$ and $e_3 = e_1 e_2$. It is associative, non-commutative and simple, with centre $\mathbb{R}$, and it is not a division algebra: $1 + e_2$ and $1 - e_2$ are nonzero and multiply to zero.

The algebra is the Clifford algebra $\mathrm{Cl}_{1,1}$, and its conjugation $\bar{\tilde q}$ is the Clifford conjugation. The diagonal product $\tilde q\bar{\tilde q} = q_0^2 + q_1^2 - q_2^2 - q_3^2$ takes both signs and vanishes exactly on the zero divisors; its metrical reading, the associated group of units and the action of the group on $V$ are treated in *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Rotations and the Lorentz Group*.

The conjugation $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ is an involutive anti-automorphism whose fixed-point subspaces are the scalar line $S$ and the vector space $V$. The principal involution and the reversal commute and cut the algebra into the scalar line, the plane $\operatorname{span}\{e_1,e_2\}$ and the line $\mathbb{R}e_3$. The idempotents $\tilde\pi_\pm = \tfrac12(1 \pm e_2)$ are non-central, sum to $1$, multiply to zero, and split the algebra as a direct sum of two minimal left ideals, and not as an algebra. The split-complex subalgebras $\operatorname{span}\{1,e_2\}$ and $\operatorname{span}\{1,e_3\}$ are copies of $\mathbb{D}$ and carry the zero divisors of the algebra.

The system is not the eight-dimensional $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table, which is neither simple nor free of nilpotents; the two are distinguished once, in *The Number Systems as Clifford Algebras*.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, $\mathrm{Cl}_{1,1}$ | this article |
| $1, e_1, e_2, e_3$ | the basis, with $e_1^2=-1$, $e_2^2=e_3^2=+1$, $e_3=e_1e_2$ | this article |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | a general split-quaternion | this article |
| $q_0 = \operatorname{Sc}(\tilde q)$ | the scalar part | this article |
| $\mathbf{v} = \operatorname{Vec}(\tilde q)$ | the vector part | this article |
| $S = \mathbb{R}\cdot1$ | the scalar subspace | this article |
| $V = \operatorname{span}\{e_1,e_2,e_3\}$ | the vector subspace | this article |
| $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ | the split-quaternion conjugation | this article |
| $\alpha$ | the principal involution, $e_1,e_2 \mapsto -e_1,-e_2$, $e_3 \mapsto e_3$ | this article |
| $\rho$ | the reversal, $e_1,e_2 \mapsto e_1,e_2$, $e_3 \mapsto -e_3$ | this article |
| $B(\tilde q,y) = \operatorname{Sc}(\tilde q\bar y) = q_0q_0'+q_1q_1'-q_2q_2'-q_3q_3'$ | the inner product, formed and evaluated algebraically | this article |
| $N(\tilde q) = \tilde q\bar{\tilde q} = q_0^2+q_1^2-q_2^2-q_3^2$ | the split-quaternion norm, named here only by forward reference | *Split-Quaternion Norm and Invertibility* |
| $\tilde\pi_\pm = \tfrac12(1 \pm e_2)$ | the non-central idempotents | this article |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$, $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | the split-complex subalgebras | this article |
| $[\tilde q,y] = \tilde q y - y\tilde q$ | the commutator bracket | this article |
| $\mathrm{SL}_2(\mathbb{R})$ | the three-dimensional simple Lie algebra of $V$ | this article |
| $\mathbb{D}$ | the split-complex numbers, $j^2=+1$ | *Split-Complex Algebra* |
| $\mathbb{H}$ | the real quaternions | *Quaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | the split-biquaternions, $\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$, a later Part V system | *The Number Systems as Clifford Algebras* |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first appearance of the algebra as the even part of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the low-dimensional classification $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ and the coquaternion terminology.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification of the classical groups of the algebra with the matrix groups.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split forms of the composition algebras and the place of the algebra among them.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the isotropic forms and their maximal totally isotropic subspaces.
