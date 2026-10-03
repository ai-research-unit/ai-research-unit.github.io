
# __Split-Complex Idempotents and Projections__

## Introduction

The algebra article defined the split-complex algebra $\mathbb{D}$, its conjugation and its two idempotents $\Pi_\pm = \tfrac12(1\pm j)$. This article treats the **idempotents** of $\mathbb{D}$ — the elements satisfying $A^2 = A$ — and the projections and direct-sum decompositions they carry. It is the two-dimensional counterpart of *Biquaternion Idempotents and Projections*, and the contrast is sharp: the biquaternion algebra has a two-parameter family of idempotents in bijection with the roots of $-1$, while $\mathbb{D}$ has no root of $-1$ at all and exactly four idempotents.

Idempotents are the algebraic form of a projection, and in $\mathbb{D}$ they do three jobs at once:

1. they give the direct-sum decomposition of the algebra into its two minimal ideals;
2. they characterise the zero divisors, each of which is a real multiple of $\Pi_1$ or of $\Pi_2$;
3. they exhibit the algebra isomorphism $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$ as the indicator-function decomposition of a two-point set.

**Placement.** The article is second in the Algebra group, after *Split-Complex Algebra* and before *Split-Complex Ideals and Peirce Decomposition*, *Split-Complex Zero Divisors* and *Worked Examples in the Split-Complex Algebra*, all of which use the idempotents. Its proofs use only the algebra article; the norm and the invertibility criterion belong to *Split-Complex Norm and Invertibility* in the Topology group.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, with basis $1$, $j$, $j^2 = +1$. A general element is $A = a+ja'$ with $a, a' \in \mathbb{R}$, the conjugate is $\bar A = a-ja'$, and the idempotents are $\Pi_\pm = \tfrac12(1\pm j)$, with $A = A_+\Pi_1 + A_-\Pi_2$ and $A_\pm = a\pm a'$. The base field is $\mathbb{R}$, so $2$ is invertible.

## Idempotents in an Algebra

Let $A$ be an associative unital algebra over a commutative ring. An element $e \in A$ is an **idempotent** if

$$
e^2 = e.
$$

Idempotents encode direct summands: for an idempotent $e$ of a unital algebra,

$$
A = Ae \oplus A(1-e) \quad (\text{left}), \qquad A = eA \oplus (1-e)A \quad (\text{right}),
$$

and every such decomposition of the regular module arises from an idempotent.

**Definition.** Two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$; then $e+f$ is again idempotent. A family $\{j,\dots,e_n\}$ is **pairwise orthogonal** if $e_ie_j = 0$ for $i \neq j$, and **complete** if in addition $\sum_i e_i = 1$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents.

For a semisimple algebra $A$ the criterion used throughout is

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

The algebra $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$ is semisimple, being a product of two fields, so the criterion applies; it is the reason the idempotent theory and the ideal theory of this category are two views of one subject.

## The Standard Idempotents of $\mathbb{D}$

Put

$$
\Pi_1 = \frac{1+j}{2}, \qquad \Pi_2 = \frac{1-j}{2}.
$$

Since $j^2 = +1$, one has

$$
\Pi_1^2 = \frac{1+2j+j^2}{4} = \frac{2+2j}{4} = \Pi_1, \qquad \Pi_2^2 = \Pi_2,
$$

and

$$
\Pi_1 \Pi_2 = \frac{(1+j)(1-j)}{4} = \frac{1-j^2}{4} = 0, \qquad \Pi_1 + \Pi_2 = 1.
$$

So $\Pi_1$ and $\Pi_2$ are orthogonal idempotents summing to the unit of the algebra. They are **central**: $\mathbb{D}$ is commutative, so every element commutes with both. This is a systematic difference from the biquaternion algebra, where the standard idempotents $\tilde\Pi_1 = \tfrac12(1 + ie_3)$ and $\tilde\Pi_2 = \tfrac12(1 - ie_3)$ are not central, and it removes at once all the off-diagonal structure that the non-central case supports.

Both $\Pi_1$ and $\Pi_2$ are primitive. Indeed

$$
\Pi_1 \mathbb{D} \Pi_1 = \mathbb{R} \Pi_1 \cong \mathbb{R},
$$

a field, so the criterion above applies; the same computation gives $\Pi_2\mathbb{D}\Pi_2 = \mathbb{R}\Pi_2 \cong \mathbb{R}$. These two are the standard idempotents of $\mathbb{D}$.

## The Classification of the Idempotents

**Theorem.** The idempotents of $\mathbb{D}$ are exactly the four elements

$$
0, \qquad 1, \qquad \Pi_1 = \frac{1+j}{2}, \qquad \Pi_2 = \frac{1-j}{2}.
$$

**Proof.** Write $A = a+ja'$ with $a, a' \in \mathbb{R}$ and impose $A^2 = A$. Since

$$
A^2 = (a+j a')^2 = a^2 + 2a a'j + a'^2 j^2 = (a^2+a'^2) + 2a a' j,
$$

the equation $A^2 = A = a + j a'$ is equivalent to the two real equations

$$
a^2 + a'^2 = a, \qquad 2a a' = a'.
$$

The second factors as $a'(2a-1) = 0$:

- If $a' = 0$, the first becomes $a^2 = a$, so $a = 0$ or $a = 1$: the idempotents $0$ and $1$.
- If $a' \neq 0$, then $a = 1/2$, and the first becomes $\tfrac14 + a'^2 = \tfrac12$, so $a'^2 = \tfrac14$ and $a' = \pm\tfrac12$: the idempotents $\Pi_1$ and $\Pi_2$.

There are no others. The set of idempotents is finite, of four elements, and in particular there is no positive-dimensional family. This is the exact opposite of the biquaternion situation, and its cause is visible in the proof: there the idempotent equation forces the scalar part to be $1/2$ and reduces to the equation $\xi^2 = -1$ on the vector part, which has a two-sphere of real solutions and a four-real-dimensional family of complex ones; here the same reduction produces $a'^2 = +1/4$, whose solution set is the two points $a' = \pm 1/2$, because $\mathbb{D}$ has no root of $-1$ and no vector part to vary independently.

## The Idempotents as Indicator Functions

The classification has a transparent form under the algebra isomorphism

$$
\varphi : \mathbb{D} \to \mathbb{R}\oplus\mathbb{R}, \qquad \varphi(a+j a') = (a+a', a-a').
$$

The four idempotents map to the four vectors

$$
0 \longmapsto (0,0), \qquad \Pi_1 \longmapsto (1,0), \qquad \Pi_2 \longmapsto (0,1), \qquad 1 \longmapsto (1,1).
$$

These are exactly the **indicator functions** of the four subsets of the two-point set $\{+,-\}$: the empty set, the singleton $\{+\}$, the singleton $\{-\}$, and the whole set. Since on $\mathbb{R}\oplus\mathbb{R}$ the idempotents are precisely the pairs $(\epsilon_+,\epsilon_-)$ with each $\epsilon_\sigma \in \{0,1\}$, the correspondence is a bijection

$$
\{\text{idempotents of } \mathbb{D}\} \;\longleftrightarrow\; \{\text{subsets of } \{+,-\}\}, \qquad e \longleftrightarrow \{\sigma : e_\sigma \neq 0\},
$$

with $2^2 = 4$ elements. The idempotent $e$ is the projection onto the coordinates selected by its subset, and $1-e$ is the projection onto the complementary subset; the two complementary pairs are $\{0,1\}$ and $\{\Pi_1,\Pi_2\}$.

In the biquaternion algebra the corresponding bijection is with the roots of $-1$; here there is no root of $-1$ to parametrise, and the parametrising set is instead the two-point set itself, whose power set has four elements.

## Idempotents as Projections

An idempotent $e$ satisfies $e^2 = e$, so it acts as the identity on its image and annihilates its kernel; it is a **projection**. Its complement $1-e$ is also an idempotent, and

$$
e(1-e) = e - e^2 = 0,
$$

so the pair $\{e, 1-e\}$ gives a direct-sum decomposition of the underlying real vector space,

$$
\mathbb{D} = \mathbb{D}e \oplus \mathbb{D}(1-e),
$$

and equally $\mathbb{D} = e\mathbb{D}\oplus(1-e)\mathbb{D}$ on the other side; since the algebra is commutative the two decompositions coincide.

For the standard pair $\{\Pi_1, \Pi_2\}$ the projections are the coordinate projections of $\mathbb{R}\oplus\mathbb{R}$:

$$
P_+ : A \longmapsto A_+ = a+a', \qquad P_- : A \longmapsto A_- = a-a',
$$

with

$$
P_+^2 = P_+, \qquad P_-^2 = P_-, \qquad P_+P_- = P_-P_+ = 0, \qquad P_+ + P_- = \mathrm{id}.
$$

So $P_+$ is the projection onto $\mathbb{R}\Pi_1$ along $\mathbb{R}\Pi_2$, and $P_-$ the complementary projection. A projection in the split-complex algebra is the same thing as an idempotent, and the projections $P_\pm$ select the two coordinates of the isomorphism with $\mathbb{R}\oplus\mathbb{R}$.

## Idempotents and the Zero Divisors

A nontrivial idempotent is a zero divisor, since

$$
\Pi_1(1-\Pi_1) = 0, \qquad \Pi_1 \neq 0, \qquad 1-\Pi_1 = \Pi_2 \neq 0,
$$

and symmetrically for $\Pi_2$. Conversely, every zero divisor of $\mathbb{D}$ is a real multiple of an idempotent:

**Theorem.** A nonzero element $A$ is a zero divisor if and only if $A = \lambda \Pi_1$ or $A = \lambda \Pi_2$ for some $\lambda \in \mathbb{R}^\times$.

**Proof.** If $A = \lambda \Pi_1$ then $A \Pi_2 = 0$ with $\Pi_2 \neq 0$, so $A$ is a zero divisor, and similarly for $\Pi_2$. Conversely, if $AB = 0$ with $A, B \neq 0$, write both in the idempotent basis; then $AB = A_+B_+\Pi_1 + A_-B_-\Pi_2 = 0$ gives $A_+B_+ = 0$ and $A_-B_- = 0$. Since $B \neq 0$ at least one of $B_+, B_-$ is nonzero, and the corresponding coordinate of $A$ vanishes; hence $A \in \mathbb{R}\Pi_1$ or $A \in \mathbb{R}\Pi_2$.

In the idempotent coordinates this is the statement that the zero divisors are the elements lying on the coordinate axes of the decomposition $\mathbb{D} = \mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$: an element $A = A_+\Pi_1 + A_-\Pi_2$ is a zero divisor exactly when one of the two coordinates vanishes, and it is then supported on the corresponding idempotent. The classification of the null cone and the form of the zero-divisor set are the subject of *Split-Complex Zero Divisors*; the present statement is the piece of it that belongs to the idempotents.

## Idempotents and the Minimal Ideals

**Proposition.** The principal ideals

$$
\mathbb{D}\Pi_1 = \mathbb{R}\Pi_1, \qquad \mathbb{D}\Pi_2 = \mathbb{R}\Pi_2
$$

are the two nontrivial minimal ideals of $\mathbb{D}$, and

$$
\mathbb{D} = \mathbb{D}\Pi_1 \oplus \mathbb{D}\Pi_2
$$

as a direct sum of ideals, the two summands being the two copies of $\mathbb{R}$.

**Proof.** Every $A$ satisfies $A = A(\Pi_1 + \Pi_2) = A\Pi_1 + A\Pi_2$, so the two ideals span; their intersection is zero because $\Pi_1\Pi_2 = 0$: if $A\Pi_1 = B\Pi_2$ then multiplying by $\Pi_1$ gives $A\Pi_1 = 0$. Each has real dimension $1$. For minimality, a nonzero ideal contained in $\mathbb{D}\Pi_1$ contains some $\lambda \Pi_1$ with $\lambda \neq 0$, hence contains $\Pi_1$ and equals $\mathbb{R}\Pi_1$; so each is minimal.

The two ideals are also the two **minimal ideals** in the sense of the lattice of all ideals, and they are the images of the two projection idempotents. The lattice of the ideals of $\mathbb{D}$, the Peirce decomposition of the algebra with respect to an idempotent, and the failure of simplicity that these two minimal ideals express are developed in *Split-Complex Ideals and Peirce Decomposition*.

## The Set of Idempotents

The set of idempotents of $\mathbb{D}$ has four elements, with coordinates in the basis $1, j$

$$
0 = (0,0), \quad 1 = (1,0), \quad \Pi_1 = \tfrac12(1,1), \quad \Pi_2 = \tfrac12(1,-1).
$$

It is a finite set, and its parametrisation by the subsets of $\{+,-\}$ makes the finiteness structural rather than accidental. This is again the opposite of the biquaternion case, where the idempotents form a positive-dimensional family in bijection with the roots of $-1$; here the parametrising set is the two-point set, so the whole set is finite. Of the four idempotents only $1$ is a unit: each of $0, \Pi_1, \Pi_2$ has a vanishing idempotent coordinate, so each is a non-unit, and the two nontrivial ones are the zero divisors.

## The Two-Dimensional Analogue of the Idempotent Theory of $\mathbb{B}$

| feature | $\mathbb{B}$ | $\mathbb{D}$ |
|---|---|---|
| standard idempotents | $\tilde\Pi_1 = \tfrac12(1+ie_3)$, $\tilde\Pi_2 = \tfrac12(1-ie_3)$ | $\Pi_1 = \tfrac12(1+j)$, $\Pi_2 = \tfrac12(1-j)$ |
| central? | no | yes (the algebra is commutative) |
| parametrising set of idempotents | roots of $-1$ (a large stratified set) | subsets of $\{+,-\}$ (four points) |
| number of idempotents | a continuum of nontrivial ones | $4$ in all |
| minimal left ideals | $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$, of dimension $2$ over $\mathbb{C}$, $4$ over $\mathbb{R}$ | $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$, of dimension $1$ |
| decomposition | $\mathbb{B} = \mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$ | $\mathbb{D} = \mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$ |
| zero divisors via idempotents | every non-pure zero divisor is a complex multiple of one | every zero divisor is a real multiple of $\Pi_1$ or $\Pi_2$ |

The table is the summary of the systematic degeneration: the two-dimensional algebra retains the direct-sum decomposition, the complementary pair and the classification of the zero divisors by idempotents, and loses the non-central off-diagonal elements, the bijection with the roots of $-1$ and the positive-dimensional family of idempotents, simply because its two idempotents are central and its vector part has no room to vary.

## Summary

An idempotent of $\mathbb{D}$ is an element $A$ with $A^2 = A$. The algebra has exactly four: $0$, $1$, and the standard pair $\Pi_\pm = \tfrac12(1\pm j)$. The standard pair is orthogonal, complete and primitive, and it is central because $\mathbb{D}$ is commutative. Under the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ the four idempotents are the four indicator functions of the two-point set $\{+,-\}$, so the set of idempotents is finite and corresponds to the power set of $\{+,-\}$ rather than to a family of roots of $-1$.

The idempotents are projections: $A = A_+\Pi_1 + A_-\Pi_2$, with $A_\pm = A\Pi_\pm$ the two components, and $\Pi_1 + \Pi_2 = 1$, $\Pi_1\Pi_2 = 0$ give the direct-sum decomposition $\mathbb{D} = \mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2 \cong \mathbb{R}\oplus\mathbb{R}$, whose summands are the two minimal ideals. The nontrivial idempotents are zero divisors, and conversely every zero divisor is a real multiple of $\Pi_1$ or of $\Pi_2$: in the idempotent basis the zero divisors are exactly the elements supported on a single idempotent, that is, the elements with one vanishing coordinate. This is the two-dimensional analogue of the idempotent theory of $\mathbb{B}$, with the vector part missing and the non-commutativity gone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $A = a + j a'$ | General split complex number |
| $A^2 = A$ | Idempotence condition |
| $\Pi_1 = \tfrac12(1+j)$ | Standard positive idempotent |
| $\Pi_2 = \tfrac12(1-j)$ | Standard negative idempotent |
| $\Pi_\pm$ | Orthogonal, complete, central, primitive pair |
| $A = A_+\Pi_1 + A_-\Pi_2$ | Idempotent decomposition, $A_\pm = a\pm a'$ |
| $P_+, P_-$ | Projections $A \mapsto A_+$, $A \mapsto A_-$; $P_+ + P_- = \mathrm{id}$ |
| $\mathbb{D}\Pi_1, \mathbb{D}\Pi_2$ | The two minimal ideals, $\cong \mathbb{R}$ |
| $\varphi(a+j a') = (a+a', a-a')$ | Isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$ |
| $\mathbb{R}\Pi_1, \mathbb{R}\Pi_2$ | The two null lines of zero divisors |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, Peirce decompositions and the structure of finite-dimensional algebras.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, Mathematical Association of America, 1968), for idempotents, orthogonal families and the theory of the radical.
- John Voight, *Quaternion Algebras* (Springer, Graduate Texts in Mathematics 288, 2021), for idempotents and zero divisors in real algebras of small dimension.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for primitive idempotents and minimal ideals.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the elementary classification of the idempotents of a product of fields.
