
# __Dual-Number Subspaces__

## Introduction

This article collects the submodule structure of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ and the relations among its distinguished submodules. It follows *Dual-Numbers Algebra* for the two conjugations and the two distinguished submodules, *Dual-Numbers Norm and Invertibility* for the norm form, and *Dual-Numbers Ideals and the Maximal Ideal* for the ideal structure. Its structural model is *Biquaternion Relations Between Subspaces*, in which a lattice of six subspaces is organized by the four conjugations; here only one nontrivial conjugation exists, and the lattice is correspondingly small.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the geometric specialisation is $R = \mathbb{R}$, and then the algebra is written $\mathbb{D}'$. A general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in R,
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, dual conjugation $\bar{Z} = a - \varepsilon b$, norm form $N(Z) = Z\bar{Z} = a^2$, and maximal ideal $\mathfrak{m} = (\varepsilon)$. The two distinguished submodules are

$$
R_{\mathbb{D}'} = R\cdot 1 = \{Z : \bar{Z} = Z\}, \qquad \varepsilon R_{\mathbb{D}'} = \varepsilon R = \{Z : \bar{Z} = -Z\}.
$$

The scope boundaries are these. This article owns the submodule lattice and the relations among the submodules. The ideals and the Peirce-type decomposition belong to *Dual-Numbers Ideals and the Maximal Ideal*; the classification of the zero divisors belongs to *Dual-Numbers Zero Divisors*. The submodules are treated here as submodules, that is, as $R$-linear objects, and the reader is referred elsewhere for their ideal-theoretic role.

## The Decompositions

### The Conjugate Decomposition

Dual conjugation $\bar{\cdot}$ is an involution of $\mathbb{D}'_R$ with eigenvalues $+1$ and $-1$, and its eigenspace decomposition is

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'}, \qquad Z = \underbrace{a}_{+1} + \underbrace{\varepsilon b}_{-1}.
$$

The two projections are $Z \mapsto \tfrac{1}{2}(Z + \bar{Z}) = \operatorname{Re}(Z)$ and $Z \mapsto \tfrac{1}{2}(Z - \bar{Z}) = \operatorname{Inf}(Z)\varepsilon$.

### The Real–Infinitesimal Decomposition

The same decomposition is the **real–infinitesimal decomposition**, written in the coordinates of the basis:

$$
Z = a + \varepsilon b, \qquad a \in R_{\mathbb{D}'}, \quad \varepsilon b \in \varepsilon R_{\mathbb{D}'}.
$$

It is not a second decomposition but the same one: the two names record the two ways of describing the same pair of eigenspaces.

### There Is No Third Decomposition

The biquaternion algebra carries four conjugations, and their eigenspaces generate six distinct subspaces, which is why *Biquaternion Relations Between Subspaces* has a lattice to organize. Over a field $k$, $\mathbb{D}'_k$ has exactly one nontrivial involution, namely dual conjugation, and hence exactly one pairing of eigenspaces. There is no analogue of the quaternion conjugation $\bar{\cdot}$, of the complex conjugation ${}^{*}$ distinct from it, or of the Hermitian and anti-Hermitian subspaces. So the single decomposition above is the whole of the submodule structure.

## The Two Submodules at a Glance

| Submodule | Description | $R$-rank | Generator | Square in itself | Closed under $Z \mapsto \varepsilon Z$ |
|---|---|---|---|---|---|
| $R_{\mathbb{D}'}$ | $+1$-eigenspace of $\bar{\cdot}$ | $1$ | $1$ | yes (it is a subalgebra) | no ($\varepsilon \notin R_{\mathbb{D}'}$) |
| $\varepsilon R_{\mathbb{D}'}$ | $-1$-eigenspace of $\bar{\cdot}$ | $1$ | $\varepsilon$ | yes (it squares to $0$) | yes (it is an ideal) |

The two submodules have the same rank, and they differ in every structural respect that matters: one contains the identity and is a subalgebra, the other is nilpotent and is an ideal.

### The Basis and the Dimension

**Proposition.** $\{1, \varepsilon\}$ is an $R$-basis of $\mathbb{D}'_R$, and $\{1\}$, $\{\varepsilon\}$ are $R$-bases of $R_{\mathbb{D}'}$ and $\varepsilon R_{\mathbb{D}'}$ respectively. Hence $\dim_R R_{\mathbb{D}'} = \dim_R \varepsilon R_{\mathbb{D}'} = 1$ and $\dim_R \mathbb{D}'_R = 2$.

**Proof.** $R[\varepsilon]/(\varepsilon^2)$ has $\{1, \varepsilon\}$ as a free basis by construction, and the two eigenspaces are spanned by the two basis vectors. $\square$

## The Coordinate Blocks

With respect to the basis $(1, \varepsilon)$, the group $\mathbb{D}'_R$ is the free module $R \oplus R$, and a general element is the coordinate pair $(a, b)$:

$$
Z = a + \varepsilon b \;\longleftrightarrow\; (a, b) \in R \oplus R.
$$

The two submodules are the coordinate axes: $R_{\mathbb{D}'} = \{b = 0\}$ and $\varepsilon R_{\mathbb{D}'} = \{a = 0\}$. Multiplication in coordinates is

$$
(a, b)(c, d) = (a c,\; a d + b c),
$$

the truncated polynomial product. The conjugation is the coordinatewise sign change $(a, b) \mapsto (a, -b)$, and the norm form is $N(a, b) = a^2$, the square of the first coordinate. So the submodule structure is the coordinate structure of the free module $R^2$ together with the diagonal sign action of the involution.

## The Intersections

**Proposition.** $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$; this is the only intersection of distinct positive-dimensional submodules, and it is the intersection of the two eigenspaces of an involution.

**Proof.** An element of the intersection has $b = 0$ and $a = 0$, hence is $0$. $\square$

**Proposition.** The intersections with the maximal ideal are

$$
R_{\mathbb{D}'} \cap \mathfrak{m} = \{0\}, \qquad \varepsilon R_{\mathbb{D}'} \cap \mathfrak{m} = \varepsilon R_{\mathbb{D}'}.
$$

**Proof.** $\mathfrak{m} = \varepsilon R_{\mathbb{D}'}$, so the second identity is immediate; the first is the preceding proposition. $\square$

So the maximal ideal coincides with one of the two submodules and meets the other only at the origin.

## The Sums

**Proposition.** $R_{\mathbb{D}'} + \varepsilon R_{\mathbb{D}'} = \mathbb{D}'_R$, and the sum is direct. The maximal ideal satisfies $\mathfrak{m} + R_{\mathbb{D}'} = \mathbb{D}'_R$.

**Proof.** Direct from the basis $\{1, \varepsilon\}$ and the identity $\mathfrak{m} = \varepsilon R_{\mathbb{D}'}$. $\square$

**Corollary.** Every element of $\mathbb{D}'_R$ is uniquely a sum of an element of $R_{\mathbb{D}'}$ and an element of $\varepsilon R_{\mathbb{D}'}$; the uniqueness is the statement that the sum is direct, and it is equivalent to the intersection being zero.

## The Involutions as Sign Patterns

An $R$-linear involution $s$ that is also an algebra automorphism fixes $1$ and, by the automorphism theorem of *Dual-Numbers Automorphisms and Derivations*, is $\varphi_c$ with $\varphi_c(\varepsilon) = \varepsilon c$ for some $c \in R^\times$; it is an involution exactly when $c^2 = 1$. Over a field (or, more generally, an integral domain) this gives $c = \pm 1$, so the involutions are the sign patterns

$$
(+,+) : (a, b) \mapsto (a, b) \qquad \text{(identity)}, \qquad (+,-) : (a, b) \mapsto (a, -b) \qquad \text{(dual conjugation)}.
$$

There are exactly two over a field, and the second is the unique nontrivial one; over a general commutative ring there may be further involutions, one for every unit $c$ with $c^2 = 1$. The biquaternion algebra has four conjugations, whose sign patterns on the six subspaces fill a richer table; the reason for the difference is that $\mathbb{D}'_R$ has only one unit $\varepsilon$ of square zero up to scaling, whereas $\mathbb{B}$ has the two independent quaternion units and the scalar imaginary, giving four independent sign choices.

**Remark.** The sign pattern $(+,+)$ fixes both submodules pointwise, and $(+,-)$ fixes $R_{\mathbb{D}'}$ pointwise while negating $\varepsilon R_{\mathbb{D}'}$. Only the diagonal entries are free; an automorphism of $\mathbb{D}'_R$ cannot exchange the two submodules, because $1$ must be fixed and $\varepsilon$ must go to a multiple of $\varepsilon$. This is the submodule-theoretic content of the automorphism group $\operatorname{Aut}(\mathbb{D}'_R) \cong R^\times$ computed in *Dual-Numbers Automorphisms and Derivations*.

## How the Operations Act on the Splits

### Multiplication by $\varepsilon$

The operator $E = \varepsilon\cdot$ acts on the two submodules as

$$
E : R_{\mathbb{D}'} \longrightarrow \varepsilon R_{\mathbb{D}'}, \qquad a \mapsto \varepsilon a, \qquad E : \varepsilon R_{\mathbb{D}'} \longrightarrow 0, \qquad \varepsilon b \mapsto 0.
$$

So $E$ has $\ker E = \varepsilon R_{\mathbb{D}'}$ and $\operatorname{im}E = \varepsilon R_{\mathbb{D}'}$: the kernel and the image coincide. This is the submodule form of the nilpotence $\mathfrak{m}^2 = 0$.

### The Norm Form on the Splits

The norm form is additive on the direct sum and depends only on the first summand:

$$
N(a + \varepsilon b) = N(a) + N(\varepsilon b) = a^2 + 0 = a^2.
$$

On the two submodules,

$$
N(R_{\mathbb{D}'}) \subseteq R_{\mathbb{D}'}, \qquad N(\varepsilon R_{\mathbb{D}'}) = 0.
$$

So the norm form restricts to a multiplicative form on the real submodule and vanishes identically on the infinitesimal submodule; this is the submodule statement of the degeneracy of $N$.

### The Product and the Bracket

Since $\mathbb{D}'_R$ is commutative, the commutator bracket vanishes: $[Z, W] = ZW - WZ = 0$ for all $Z, W$. The product respects the splits in the sense that

$$
R_{\mathbb{D}'} \cdot R_{\mathbb{D}'} \subseteq R_{\mathbb{D}'}, \qquad R_{\mathbb{D}'} \cdot \varepsilon R_{\mathbb{D}'} \subseteq \varepsilon R_{\mathbb{D}'}, \qquad \varepsilon R_{\mathbb{D}'} \cdot \varepsilon R_{\mathbb{D}'} = 0.
$$

So the real submodule is a subalgebra, the infinitesimal submodule is an ideal, and the product of two infinitesimal elements vanishes.

## Worked Verifications

### The Decomposition

For $Z = 2 + 3\varepsilon$ the conjugate decomposition is $Z = 2 + 3\varepsilon$ with $2 \in R_{\mathbb{D}'}$ and $3\varepsilon \in \varepsilon R_{\mathbb{D}'}$; the projections are $\tfrac{1}{2}(Z + \bar{Z}) = 2$ and $\tfrac{1}{2}(Z - \bar{Z}) = 3\varepsilon$.

### An Intersection

$R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = \{0\}$: the element $a + \varepsilon b$ lies in both submodules only if $b = 0$ and $a = 0$.

### A Pair That Spans the Algebra

$1 \in R_{\mathbb{D}'}$ and $\varepsilon \in \varepsilon R_{\mathbb{D}'}$ are linearly independent and span $\mathbb{D}'$.

### A Mixed Element and Its Blocks

For $Z = -4 + \varepsilon$ the blocks are $\operatorname{Re}(Z) = -4$ and $\operatorname{Inf}(Z)\varepsilon = \varepsilon$; the norm form is $N(Z) = (-4)^2 = 16$, read from the real block alone.

## Summary

The dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ carries exactly one nontrivial involution, dual conjugation, and hence exactly one decomposition into eigenspaces,

$$
\mathbb{D}'_R = R_{\mathbb{D}'} \oplus \varepsilon R_{\mathbb{D}'},
$$

the real and infinitesimal submodules, of $R$-rank one each. The only intersection of the two positive-dimensional submodules is $R_{\mathbb{D}'} \cap \varepsilon R_{\mathbb{D}'} = 0$, and their sum is the whole algebra; the maximal ideal $\mathfrak{m} = \varepsilon R_{\mathbb{D}'}$ coincides with the infinitesimal submodule and meets the real submodule only at the origin. Multiplication by $\varepsilon$ has kernel and image both equal to $\varepsilon R_{\mathbb{D}'}$, the submodule form of $\mathfrak{m}^2 = 0$; the norm form restricts multiplicatively to $R_{\mathbb{D}'}$ and vanishes on $\varepsilon R_{\mathbb{D}'}$. The lattice of six subspaces that organizes the biquaternion article has no analogue here: with a single nontrivial involution there are only two submodules and the two sign patterns $(+,+)$ and $(+,-)$, so a six-subspace lattice is unavailable for structural reasons and not for lack of interest.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation, the unique nontrivial involution |
| $R_{\mathbb{D}'} = R\cdot 1$ | Real submodule, $+1$-eigenspace of $\bar{\cdot}$ |
| $\varepsilon R_{\mathbb{D}'} = \varepsilon R$ | Infinitesimal submodule, $-1$-eigenspace of $\bar{\cdot}$ |
| $\mathfrak{m} = (\varepsilon)$ | Maximal ideal, equal to $\varepsilon R_{\mathbb{D}'}$ |
| $N(Z) = a^2$ | Norm form, vanishes on $\varepsilon R_{\mathbb{D}'}$ |
| $E = \varepsilon\cdot$ | Nilpotent operator, $\ker E = \operatorname{im}E = \varepsilon R_{\mathbb{D}'}$ |

## Further Reading

- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the decomposition of the dual-number algebra into its real and infinitesimal parts.
- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the submodule structure of the two-dimensional real algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the subalgebra and ideal lattices of the low-dimensional real algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, New York, 2001), for eigenspace decompositions of involutions and their relation to Peirce decompositions.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Berlin, 1991), for the restriction of a quadratic form to a subspace and to its radical.
