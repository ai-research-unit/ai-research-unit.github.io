
# __Split-Complex Idempotents and Projections__

## Introduction

The algebra article defined the split-complex algebra $\mathbb{D}$, its conjugation and its two idempotents $\Pi_\pm = \tfrac12(1\pm j)$. This article treats the **idempotents** of $\mathbb{D}$ — the elements satisfying $Q^2 = Q$ — and the direct-sum decompositions they carry. The algebra $\mathbb{D}$ has no root of $-1$ at all and exactly four idempotents.

An idempotent corresponds to a projector under its multiplication, and in $\mathbb{D}$ the idempotents do three jobs at once:

1. they give the direct-sum decomposition of the algebra into its two minimal ideals;
2. they characterise the zero divisors, each of which is a real multiple of $\Pi_+$ or of $\Pi_-$;
3. they exhibit the algebra isomorphism $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$ as the indicator-function decomposition of a two-point set.

**Placement.** The article is second in the Algebra group, after *Split-Complex Algebra* and before *Split-Complex Ideals and Peirce Decomposition*, *Split-Complex Zero Divisors* and *Worked Examples in the Split-Complex Algebra*, all of which use the idempotents. Its proofs use only the algebra article; the norm and the invertibility criterion belong to *Split-Complex Norm and Invertibility* in the Topology group.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, with basis $1$, $j$, $j^2 = +1$. A general element is $Q = q+jq'$ with $q, q' \in \mathbb{R}$, the conjugate is $\bar Q = q-jq'$, and the idempotents are $\Pi_\pm = \tfrac12(1\pm j)$, with $Q = Q_+\Pi_+ + Q_-\Pi_-$ and $Q_\pm = q\pm q'$. The base field is $\mathbb{R}$, so $2$ is invertible.

## Idempotents in an Algebra

Let $Q$ be an associative unital algebra over a commutative ring. An element $e \in Q$ is an **idempotent** if

$$
e^2 = e.
$$

Idempotents encode direct summands: for an idempotent $e$ of a unital algebra,

$$
Q = Qe \oplus Q(1-e) \quad (\text{left}), \qquad Q = eQ \oplus (1-e)Q \quad (\text{right}),
$$

and every such decomposition of the regular module arises from an idempotent.

**Definition.** Two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$; then $e+f$ is again idempotent. A family $\{j,\dots,e_n\}$ is **pairwise orthogonal** if $e_ie_j = 0$ for $i \neq j$, and **complete** if in addition $\sum_i e_i = 1$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents.

For a semisimple algebra $Q$ the criterion used throughout is

$$
e \text{ primitive} \iff Qe \text{ is a minimal left ideal} \iff eQe \text{ is a division ring}.
$$

The algebra $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$ is semisimple, being a product of two fields, so the criterion applies; it is the reason the idempotent theory and the ideal theory of this category are two views of one subject.

## The Standard Idempotents of $\mathbb{D}$

Put

$$
\Pi_+ = \frac{1+j}{2}, \qquad \Pi_- = \frac{1-j}{2}.
$$

Since $j^2 = +1$, one has

$$
\Pi_+^2 = \frac{1+2j+j^2}{4} = \frac{2+2j}{4} = \Pi_+, \qquad \Pi_-^2 = \Pi_-,
$$

and

$$
\Pi_+ \Pi_- = \frac{(1+j)(1-j)}{4} = \frac{1-j^2}{4} = 0, \qquad \Pi_+ + \Pi_- = 1.
$$

So $\Pi_+$ and $\Pi_-$ are orthogonal idempotents summing to the unit of the algebra. They are **central**: $\mathbb{D}$ is commutative, so every element commutes with both.

Both $\Pi_+$ and $\Pi_-$ are primitive. Indeed

$$
\Pi_+ \mathbb{D} \Pi_+ = \mathbb{R} \Pi_+ \cong \mathbb{R},
$$

a field, so the criterion above applies; the same computation gives $\Pi_-\mathbb{D}\Pi_- = \mathbb{R}\Pi_- \cong \mathbb{R}$. These two are the standard idempotents of $\mathbb{D}$.

## The Classification of the Idempotents

**Theorem.** The idempotents of $\mathbb{D}$ are exactly the four elements

$$
0, \qquad 1, \qquad \Pi_+ = \frac{1+j}{2}, \qquad \Pi_- = \frac{1-j}{2}.
$$

**Proof.** Write $Q = q+jq'$ with $q, q' \in \mathbb{R}$ and impose $Q^2 = Q$. Since

$$
Q^2 = (q+j q')^2 = q^2 + 2q q'j + q'^2 j^2 = (q^2+q'^2) + 2q q' j,
$$

the equation $Q^2 = Q = q + j q'$ is equivalent to the two real equations

$$
q^2 + q'^2 = q, \qquad 2q q' = q'.
$$

The second factors as $q'(2q-1) = 0$:

- If $q' = 0$, the first becomes $q^2 = q$, so $q = 0$ or $q = 1$: the idempotents $0$ and $1$.
- If $q' \neq 0$, then $q = 1/2$, and the first becomes $\tfrac14 + q'^2 = \tfrac12$, so $q'^2 = \tfrac14$ and $q' = \pm\tfrac12$: the idempotents $\Pi_+$ and $\Pi_-$.

There are no others. The set of idempotents is finite, of four elements, and in particular there is no positive-dimensional family. The cause is visible in the proof: the idempotent equation produces $q'^2 = +1/4$, whose solution set is the two points $q' = \pm 1/2$, because $\mathbb{D}$ has no root of $-1$ and no vector part to vary independently.

## The Idempotents as Indicator Functions

The classification has a transparent form under the algebra isomorphism

$$
\varphi : \mathbb{D} \to \mathbb{R}\oplus\mathbb{R}, \qquad \varphi(q+j q') = (q+q', q-q').
$$

The four idempotents map to the four vectors

$$
0 \longmapsto (0,0), \qquad \Pi_+ \longmapsto (1,0), \qquad \Pi_- \longmapsto (0,1), \qquad 1 \longmapsto (1,1).
$$

These are exactly the **indicator functions** of the four subsets of the two-point set $\{+,-\}$: the empty set, the singleton $\{+\}$, the singleton $\{-\}$, and the whole set. Since on $\mathbb{R}\oplus\mathbb{R}$ the idempotents are precisely the pairs $(\epsilon_+,\epsilon_-)$ with each $\epsilon_\sigma \in \{0,1\}$, the correspondence is a bijection

$$
\{\text{idempotents of } \mathbb{D}\} \;\longleftrightarrow\; \{\text{subsets of } \{+,-\}\}, \qquad \Pi \longleftrightarrow \{\sigma : \Pi_\sigma \neq 0\},
$$

with $2^2 = 4$ elements. The idempotent $\Pi$ selects the coordinates of its subset, and $1-\Pi$ the complementary subset; the two complementary pairs are $\{0,1\}$ and $\{\Pi_+,\Pi_-\}$.

There is no root of $-1$ to parametrise, and the parametrising set is the two-point set itself, whose power set has four elements.

## Idempotents and Direct Sum Decompositions

An idempotent $\Pi$ satisfies $\Pi^2 = \Pi$, so its multiplication acts as the identity on its image and annihilates its kernel; that multiplication operator is a **projector**. Its complement $1-\Pi$ is also an idempotent, and

$$
\Pi(1-\Pi) = \Pi - \Pi^2 = 0,
$$

so the pair $\{\Pi, 1-\Pi\}$ gives a direct-sum decomposition of the underlying real vector space,

$$
\mathbb{D} = \mathbb{D}\Pi \oplus \mathbb{D}(1-\Pi),
$$

and equally $\mathbb{D} = \Pi\mathbb{D}\oplus(1-\Pi)\mathbb{D}$ on the other side; since the algebra is commutative the two decompositions coincide.

For the standard pair $\{\Pi_+, \Pi_-\}$ the projections are the coordinate projections of $\mathbb{R}\oplus\mathbb{R}$:

$$
P_+ : Q \longmapsto Q_+ = q+q', \qquad P_- : Q \longmapsto Q_- = q-q',
$$

with

$$
P_+^2 = P_+, \qquad P_-^2 = P_-, \qquad P_+P_- = P_-P_+ = 0, \qquad P_+ + P_- = \mathrm{id}.
$$

So $P_+$ is the projection onto $\mathbb{R}\Pi_+$ along $\mathbb{R}\Pi_-$, and $P_-$ the complementary projection. A projector in the split-complex algebra is an idempotent operator, and the projectors $P_\pm$ select the two coordinates of the isomorphism with $\mathbb{R}\oplus\mathbb{R}$.

## Idempotents and the Zero Divisors

A nontrivial idempotent is a zero divisor, since

$$
\Pi_+(1-\Pi_+) = 0, \qquad \Pi_+ \neq 0, \qquad 1-\Pi_+ = \Pi_- \neq 0,
$$

and symmetrically for $\Pi_-$. Conversely, every zero divisor of $\mathbb{D}$ is a real multiple of an idempotent:

**Theorem.** A nonzero element $Q$ is a zero divisor if and only if $Q = \lambda \Pi_+$ or $Q = \lambda \Pi_-$ for some $\lambda \in \mathbb{R}^\times$.

**Proof.** If $Q = \lambda \Pi_+$ then $Q \Pi_- = 0$ with $\Pi_- \neq 0$, so $Q$ is a zero divisor, and similarly for $\Pi_-$. Conversely, if $QB = 0$ with $Q, B \neq 0$, write both in the idempotent basis; then $QB = Q_+B_+\Pi_+ + Q_-B_-\Pi_- = 0$ gives $Q_+B_+ = 0$ and $Q_-B_- = 0$. Since $B \neq 0$ at least one of $B_+, B_-$ is nonzero, and the corresponding coordinate of $Q$ vanishes; hence $Q \in \mathbb{R}\Pi_+$ or $Q \in \mathbb{R}\Pi_-$.

In the idempotent coordinates this is the statement that the zero divisors are the elements lying on the coordinate axes of the decomposition $\mathbb{D} = \mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_-$: an element $Q = Q_+\Pi_+ + Q_-\Pi_-$ is a zero divisor exactly when one of the two coordinates vanishes, and it is then supported on the corresponding idempotent. The classification of the null cone and the form of the zero-divisor set are the subject of *Split-Complex Zero Divisors*; the present statement is the piece of it that belongs to the idempotents.

## Idempotents and the Minimal Ideals

**Proposition.** The principal ideals

$$
\mathbb{D}\Pi_+ = \mathbb{R}\Pi_+, \qquad \mathbb{D}\Pi_- = \mathbb{R}\Pi_-
$$

are the two nontrivial minimal ideals of $\mathbb{D}$, and

$$
\mathbb{D} = \mathbb{D}\Pi_+ \oplus \mathbb{D}\Pi_-
$$

as a direct sum of ideals, the two summands being the two copies of $\mathbb{R}$.

**Proof.** Every $Q$ satisfies $Q = Q(\Pi_+ + \Pi_-) = Q\Pi_+ + Q\Pi_-$, so the two ideals span; their intersection is zero because $\Pi_+\Pi_- = 0$: if $Q\Pi_+ = B\Pi_-$ then multiplying by $\Pi_+$ gives $Q\Pi_+ = 0$. Each has real dimension $1$. For minimality, a nonzero ideal contained in $\mathbb{D}\Pi_+$ contains some $\lambda \Pi_+$ with $\lambda \neq 0$, hence contains $\Pi_+$ and equals $\mathbb{R}\Pi_+$; so each is minimal.

The two ideals are also the two **minimal ideals** in the sense of the lattice of all ideals, and they are the images of the two idempotents. The lattice of the ideals of $\mathbb{D}$, the Peirce decomposition of the algebra with respect to an idempotent, and the failure of simplicity that these two minimal ideals express are developed in *Split-Complex Ideals and Peirce Decomposition*.

## The Set of Idempotents

The set of idempotents of $\mathbb{D}$ has four elements, with coordinates in the basis $1, j$

$$
0 = (0,0), \quad 1 = (1,0), \quad \Pi_+ = \tfrac12(1,1), \quad \Pi_- = \tfrac12(1,-1).
$$

It is a finite set, and its parametrisation by the subsets of $\{+,-\}$ makes the finiteness structural rather than accidental. The parametrising set is the two-point set, so the whole set is finite. Of the four idempotents only $1$ is a unit: each of $0, \Pi_+, \Pi_-$ has a vanishing idempotent coordinate, so each is a non-unit, and the two nontrivial ones are the zero divisors.

## Summary

An idempotent of $\mathbb{D}$ is an element $Q$ with $Q^2 = Q$. The algebra has exactly four: $0$, $1$, and the standard pair $\Pi_\pm = \tfrac12(1\pm j)$. The standard pair is orthogonal, complete and primitive, and it is central because $\mathbb{D}$ is commutative. Under the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ the four idempotents are the four indicator functions of the two-point set $\{+,-\}$, so the set of idempotents is finite and corresponds to the power set of $\{+,-\}$ rather than to a family of roots of $-1$.

The idempotents select the two summands: $Q = Q_+\Pi_+ + Q_-\Pi_-$, with $Q_\pm = Q\Pi_\pm$ the two components, and $\Pi_+ + \Pi_- = 1$, $\Pi_+\Pi_- = 0$ give the direct-sum decomposition $\mathbb{D} = \mathbb{R}\Pi_+\oplus\mathbb{R}\Pi_- \cong \mathbb{R}\oplus\mathbb{R}$, whose summands are the two minimal ideals. The nontrivial idempotents are zero divisors, and conversely every zero divisor is a real multiple of $\Pi_+$ or of $\Pi_-$: in the idempotent basis the zero divisors are exactly the elements supported on a single idempotent, that is, the elements with one vanishing coordinate. This is the idempotent theory in the lowest dimension, with no vector part and no non-commutativity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q = q + j q'$ | General split complex number |
| $Q^2 = Q$ | Idempotence condition |
| $\Pi_+ = \tfrac12(1+j)$ | Standard positive idempotent |
| $\Pi_- = \tfrac12(1-j)$ | Standard negative idempotent |
| $\Pi_\pm$ | Orthogonal, complete, central, primitive pair |
| $Q = Q_+\Pi_+ + Q_-\Pi_-$ | Idempotent decomposition, $Q_\pm = q\pm q'$ |
| $P_+, P_-$ | Projections $Q \mapsto Q_+$, $Q \mapsto Q_-$; $P_+ + P_- = \mathrm{id}$ |
| $\mathbb{D}\Pi_+, \mathbb{D}\Pi_-$ | The two minimal ideals, $\cong \mathbb{R}$ |
| $\varphi(q+j q') = (q+q', q-q')$ | Isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ |
| $\mathbb{R}\Pi_+, \mathbb{R}\Pi_-$ | The two null lines of zero divisors |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, Peirce decompositions and the structure of finite-dimensional algebras.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, Mathematical Association of America, 1968), for idempotents, orthogonal families and the theory of the radical.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for primitive idempotents and minimal ideals.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the elementary classification of the idempotents of a product of fields.
