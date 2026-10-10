
# __Split-Biquaternion Idempotents and Projections__

## Introduction

The algebra article defined the split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$, its four conjugations and its four distinguished real subspaces. This article treats the **idempotents** of $\mathbb{H}_{\mathbb{D}}$ — the elements satisfying $\tilde P^2 = \tilde P$ — together with the projections and the direct sum decompositions they carry.

The treatment is purely mathematical. Every claim is either proved or stated as a definition. No physics is invoked. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ is assumed from the basic algebra article, together with its four conjugations, its four fixed-point subspaces $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ and its idempotent decomposition. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. The quaternion algebra $\mathbb{H}$ is assumed to be a division algebra.

Throughout, a split biquaternion is written $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu = q_\mu + j q'_\mu$ and $q_\mu, q'_\mu \in \mathbb{R}$. The quaternion conjugate is $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$, the split complex conjugate is $\bar{\tilde{Q}} = \bar{Q_0} e_0 + \mathbf{Q}^*$ with $Q_{\bar{\mu}} = q_\mu - j q'_\mu$, the Hermitian conjugate is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^{*}$. The split-biquaternion norm $N(\tilde{Q}) = \tilde{Q} \tilde{Q}^{\natural}$ is the form of *Split-Biquaternion Norm and Invertibility*, which this article names and does not use.

The result that shapes the whole article is that $\mathbb{H}_{\mathbb{D}}$ has **exactly four idempotents**, and that all of them are central. This is a strict contrast with the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, whose idempotents form a four-dimensional family in bijection with the roots of $-1$. The reason is structural: $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ is a product of two division algebras, and a product of division algebras admits only the idempotents that are constant on each factor. This article records that rigidity and its consequences; the parallel study of the *ideals* of the algebra, and of the resulting Peirce decomposition and $\mathbb{H} \oplus \mathbb{H}$ splitting, is the subject of *Split-Biquaternion Ideals and Peirce Decomposition*.

## Idempotents in an Algebra

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$. Idempotents encode direct summands: for an idempotent $e$,

$$
A = Ae \oplus A(1 - e) \quad (\text{left}), \qquad A = eA \oplus (1 - e)A \quad (\text{right}),
$$

and conversely every decomposition of $A$ into complementary left ideals (or complementary right ideals) arises from an idempotent in this way. Two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$; then $e + f$ is again idempotent. A family $\{e_1, \dots, e_n\}$ is **pairwise orthogonal** if $e_i e_j = 0$ for $i \neq j$, and **complete** if in addition $\sum_i e_i = 1$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents. The criterion used throughout, valid for a semisimple algebra $A$, is

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

The algebra $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ is a product of two division algebras and is therefore semisimple, so the criterion applies to it. The idempotents of a product of division algebras are easy to describe: if $e = (e_1, e_2) \in D_1 \oplus D_2$ with $D_1, D_2$ division rings, then $e^2 = e$ forces $e_1^2 = e_1$ and $e_2^2 = e_2$, and a division ring has only the idempotents $0$ and $1$. Hence a product of two division algebras has exactly four idempotents, all central. This is the phenomenon that the rest of the article realises in $\mathbb{H}_{\mathbb{D}}$.

## The Idempotents of the Split Complex Centre

The idempotents of the split complex algebra $\mathbb{D}$ are

$$
\tilde\Pi_1 = \tfrac{1}{2}(1 + j), \qquad \tilde\Pi_2 = \tfrac{1}{2}(1 - j).
$$

They satisfy

$$
\tilde\Pi_1^2 = \tilde\Pi_1, \qquad \tilde\Pi_2^2 = \tilde\Pi_2, \qquad \tilde\Pi_1 \tilde\Pi_2 = \tilde\Pi_2 \tilde\Pi_1 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = 1.
$$

So $\{\tilde\Pi_1, \tilde\Pi_2\}$ is a complete family of pairwise orthogonal idempotents of $\mathbb{D}$. Since $j$ is central in $\mathbb{H}_{\mathbb{D}}$, so are $1$ and $j$, and therefore so are $\tilde\Pi_1$ and $\tilde\Pi_2$: they lie in the centre of $\mathbb{H}_{\mathbb{D}}$, which is the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$. The pair $\{\tilde\Pi_1, \tilde\Pi_2\}$ is a basis of the centre over $\mathbb{R}$, and the map

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \to \mathbb{R} \oplus \mathbb{R}, \qquad a \tilde\Pi_1 + b \tilde\Pi_2 \mapsto (a, b)
$$

is an isomorphism of real algebras. The two idempotents are the units of the two copies of $\mathbb{R}$ in this decomposition, and they are the only nontrivial idempotents of the centre.

The idempotents $\tilde\Pi_{1,2}$ are exchanged by the split complex conjugation and fixed by the quaternion conjugation. Indeed $\bar{\tilde\Pi_{1,2}} = \tilde\Pi_{1,2}$ because the coefficients of $\tilde\Pi_{1,2}$ are real, while $j^* = -j$ gives

$$
\tilde\Pi_1^* = \tilde\Pi_2, \qquad \tilde\Pi_2^* = \tilde\Pi_1.
$$

Consequently

$$
\tilde\Pi_1^{*} = \tilde\Pi_2, \qquad \tilde\Pi_2^{*} = \tilde\Pi_1, \qquad \tilde\Pi_1^\flat = -\tilde\Pi_2, \qquad \tilde\Pi_2^\flat = -\tilde\Pi_1,
$$

so the Hermitian and anti-Hermitian conjugations swap the two idempotents (up to sign). The idempotents $\tilde\Pi_{1,2}$ are therefore **not** Hermitian: $\tilde\Pi_1^{*} = \tilde\Pi_2 \neq \tilde\Pi_1$, and likewise with the two exchanged.

## The Classification of the Idempotents

**Theorem.** The idempotents of $\mathbb{H}_{\mathbb{D}}$ are exactly $0$, $\tilde\Pi_1$, $\tilde\Pi_2$ and $1$. There are no others.

**Proof.** Write an idempotent in the idempotent basis as $\tilde P = \tilde P_1 \tilde\Pi_1 + \tilde P_2 \tilde\Pi_2$ with $\tilde P_{1,2} = \tilde P \tilde\Pi_{1,2} \in \mathbb{H}$. Since $\tilde\Pi_1^2 = \tilde\Pi_1$, $\tilde\Pi_2^2 = \tilde\Pi_2$ and $\tilde\Pi_1 \tilde\Pi_2 = 0$, the square is

$$
\tilde P^2 = \tilde P_1^2 \tilde\Pi_1 + \tilde P_2^2 \tilde\Pi_2.
$$

Hence $\tilde P^2 = \tilde P$ is equivalent to the pair of equations $\tilde P_1^2 = \tilde P_1$ and $\tilde P_2^2 = \tilde P_2$ in the quaternion algebra $\mathbb{H}$. Each $\tilde P_{1,2}$ is therefore an idempotent of $\mathbb{H}$.

The quaternion algebra is a division algebra, so its only idempotents are $0$ and $1$: if $\tilde q = a + \mathbf{v}$ with $a \in \mathbb{R}$ and $\mathbf{v}$ pure, then $\tilde q^2 = \tilde q$ gives $2a\mathbf{v} = \mathbf{v}$ and $a^2 - |\mathbf{v}|^2 = a$; if $\mathbf{v} = 0$ then $a^2 = a$, so $a \in \{0, 1\}$; if $\mathbf{v} \neq 0$ then $a = 1/2$ and then $|\mathbf{v}|^2 = -1/4$, which is impossible. Hence $\tilde P_{1,2} \in \{0, 1\}$, and the four combinations give

$$
\tilde P = 0, \qquad \tilde P = \tilde\Pi_1, \qquad \tilde P = \tilde\Pi_2, \qquad \tilde P = \tilde\Pi_1 + \tilde\Pi_2 = 1.
$$

These four are idempotent, and there are no others.

**Corollary.** Every idempotent of $\mathbb{H}_{\mathbb{D}}$ is central, and every idempotent lies in the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$. The set of idempotents is $\{0, \tilde\Pi_1, \tilde\Pi_2, 1\}$, a discrete set of four points.

**Proof.** The four idempotents are real combinations of $1$ and $j$, hence lie in the centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$.

A nonzero idempotent is primitive exactly when it cannot be written as a sum of two nonzero orthogonal idempotents. From the four idempotents, the only orthogonal pairs are $\{\tilde\Pi_1, \tilde\Pi_2\}$ and $\{0, \tilde\Pi_{1,2}\}$. Hence $\tilde\Pi_1$ and $\tilde\Pi_2$ are **primitive**, while $0$ is excluded (it is not nonzero) and $1 = \tilde\Pi_1 + \tilde\Pi_2$ is **not** primitive. Thus $\{\tilde\Pi_1, \tilde\Pi_2\}$ is a complete family of primitive orthogonal idempotents, and it is the only one.

## The Absence of a Bijection With the Roots of Minus One

In the biquaternion algebra $\mathbb{B}$, the idempotents are in bijection with the roots of $-1$: every idempotent has the form $\tfrac{1}{2}(e_0 + \xi i)$ for a unique root $\xi$ of $-1$, and the root set is large. That correspondence **fails completely** in $\mathbb{H}_{\mathbb{D}}$, and the failure is quantitative.

**Theorem.** The roots of $-1$ in $\mathbb{H}_{\mathbb{D}}$ form the set

$$
\{\xi = \mu_+ \tilde\Pi_1 + \mu_- \tilde\Pi_2 : \mu_\pm \text{ unit pure real quaternions}\},
$$

a set of real dimension $4$, parametrised by a pair of unit pure real quaternions. That the set is the topological product $S^2 \times S^2$, and its manifold structure, are established in *Split-Biquaternion Analysis*. The idempotents of $\mathbb{H}_{\mathbb{D}}$ number $4$. Hence there is no bijection between the two sets.

**Proof.** The classification of the roots of $-1$ is the content of *Split-Biquaternion Roots of Minus One*: the equation $\xi^2 = -1$, written in the idempotent basis as $\xi_+^2 \tilde\Pi_1 + \xi_-^2 \tilde\Pi_2 = -\tilde\Pi_1 - \tilde\Pi_2$, is equivalent to $\xi_\pm^2 = -1$ in $\mathbb{H}$, whose solutions are the unit pure real quaternions, a two-sphere. The product is two-dimensional over each of the two components, so the root set has real dimension $2 + 2 = 4$. Since the idempotent set is the four-point set of the previous section, no bijection exists.

The reason for the failure is the same rigidity that produced the classification theorem. In $\mathbb{B}$ the construction $\tilde P = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ turns a root $\xi$ of $-1$ into an idempotent because the central unit $i$ is available to convert the vector part into a scalar direction. In $\mathbb{H}_{\mathbb{D}}$ there is no central scalar imaginary — the only central units are $1$ and $j$, with $j^2 = +1$ — and the obstruction $|\mathbf{v}|^2 = -1/4$ in the proof above is unavailable. The idempotents of $\mathbb{H}_{\mathbb{D}}$ are therefore confined to the centre, and they cannot be parametrised by the roots of $-1$.

## Idempotents as Projections

An idempotent $\tilde P$ satisfies $\tilde P^2 = \tilde P$, and its **complement** $1 - \tilde P$ is again an idempotent with

$$
\tilde P(1 - \tilde P) = \tilde P - \tilde P^2 = 0.
$$

Because every idempotent of $\mathbb{H}_{\mathbb{D}}$ is central, the pair $\{\tilde P, 1 - \tilde P\}$ gives a direct sum decomposition of the algebra as a **two-sided** decomposition:

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{D}} \tilde P \oplus \mathbb{H}_{\mathbb{D}}(1 - \tilde P) = \tilde P \mathbb{H}_{\mathbb{D}} \oplus (1 - \tilde P) \mathbb{H}_{\mathbb{D}},
$$

and the two summands are ideals. This is the algebraic content of the statement that an idempotent is a projection: the idempotent is the projection, its complement is the complementary projection, and the algebra splits into the image of one and the image of the other. The decomposition attached to $\tilde P = \tilde\Pi_1$ is the idempotent decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2,
$$

with $\mathbb{H} \tilde\Pi_1 = \mathbb{H}_{\mathbb{D}} \tilde\Pi_1$ and $\mathbb{H} \tilde\Pi_2 = \mathbb{H}_{\mathbb{D}} \tilde\Pi_2$.

A **Hermitian idempotent** is one satisfying $\tilde{P}^{*} = \tilde P$; in $\mathbb{B}$ these are the orthogonal projections for the Hermitian form and the ones that occur in the spectral decomposition of a Hermitian element. In $\mathbb{H}_{\mathbb{D}}$ there is no nontrivial Hermitian idempotent: the calculation $\tilde\Pi_1^{*} = \tilde\Pi_2$ of the second section shows that the two nontrivial idempotents are interchanged by ${}^{*}$, and neither is fixed. The idempotent decomposition of $\mathbb{H}_{\mathbb{D}}$ is therefore a decomposition into two ideals that are exchanged by the Hermitian conjugation, not a decomposition into orthogonal projections.

## Idempotents and the Zero Divisors

A nontrivial idempotent is a zero divisor, because

$$
\tilde\Pi_1 (1 - \tilde\Pi_1) = \tilde\Pi_1 \tilde\Pi_2 = 0,
$$

and both factors are nonzero. Explicitly, the annihilator of $\tilde\Pi_1$ contains $\tilde\Pi_2$, and the annihilator of $\tilde\Pi_2$ contains $\tilde\Pi_1$; since $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2$, the two annihilators are exactly

$$
\mathrm{Ann}(\tilde\Pi_1) = \mathbb{H} \tilde\Pi_2, \qquad \mathrm{Ann}(\tilde\Pi_2) = \mathbb{H} \tilde\Pi_1,
$$

each of real dimension $4$. The idempotents are therefore the two most symmetric members of the zero divisor set: the zero divisors of $\mathbb{H}_{\mathbb{D}}$ are precisely the elements with a vanishing idempotent component, $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$, that is, the union $\mathbb{H} \tilde\Pi_2 \cup \mathbb{H} \tilde\Pi_1$ with the origin deleted.

This is a different situation from the biquaternion case. In $\mathbb{B}$ every non-pure zero divisor is a complex multiple of an idempotent, so the idempotents in a sense parametrise the zero divisors. In $\mathbb{H}_{\mathbb{D}}$ the zero divisor set is the union of two four-dimensional real subspaces, while the idempotents are only four points: almost no zero divisor is a scalar multiple of an idempotent. The classification and the structure of the zero divisor set are the subject of *Split-Biquaternion Zero Divisors*.

## Idempotents and the Minimal Left Ideals

Because $\tilde\Pi_1$ and $\tilde\Pi_2$ are central, the left ideal generated by $\tilde\Pi_1$ coincides with the two-sided ideal it generates:

$$
\mathbb{H}_{\mathbb{D}} \tilde\Pi_1 = \tilde\Pi_1 \mathbb{H}_{\mathbb{D}} = \tilde\Pi_1 \mathbb{H}_{\mathbb{D}} \tilde\Pi_1 = \mathbb{H} \tilde\Pi_1.
$$

**Proposition.** The ideals $\mathbb{H} \tilde\Pi_1$ and $\mathbb{H} \tilde\Pi_2$ satisfy $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2$, each has real dimension $4$, and each is a minimal left ideal; moreover $\tilde\Pi_{1,2} \mathbb{H}_{\mathbb{D}} \tilde\Pi_{1,2} = \mathbb{H} \tilde\Pi_{1,2} \cong \mathbb{H}$ as a ring.

**Proof.** Every $\tilde{Q}$ satisfies $\tilde{Q} = \tilde{Q}(\tilde\Pi_1 + \tilde\Pi_2) = \tilde{Q} \tilde\Pi_1 + \tilde{Q} \tilde\Pi_2$, and the intersection is zero: if $\tilde{Q} \tilde\Pi_1 = \tilde P \tilde\Pi_2$, then multiplying on the right by $\tilde\Pi_1$ gives $\tilde{Q} \tilde\Pi_1 = 0$. In the idempotent basis $\tilde{Q} \tilde\Pi_1 = \tilde{Q}_+ \tilde\Pi_1$ with $\tilde{Q}_+ \in \mathbb{H}$, so $\mathbb{H} \tilde\Pi_1$ is the image of the projection $\tilde{Q} \mapsto \tilde{Q}_+ \tilde\Pi_1$, a real vector space of dimension $4$; the same holds for $\tilde\Pi_2$, and $4 + 4 = 8$ accounts for the whole algebra. For minimality, the map $\mathbb{H}_{\mathbb{D}} \to \mathbb{H} \tilde\Pi_1$, $\tilde{Q} \mapsto \tilde{Q} \tilde\Pi_1$, is onto with kernel $\mathbb{H} \tilde\Pi_2$; any nonzero left ideal contained in $\mathbb{H} \tilde\Pi_1$ therefore has a preimage that is a left ideal strictly containing $\mathbb{H} \tilde\Pi_2$, and since the quotient $\mathbb{H}_{\mathbb{D}} / \mathbb{H} \tilde\Pi_2 \cong \mathbb{H}$ is a division algebra, that ideal must be all of $\mathbb{H} \tilde\Pi_1$. Equivalently, $\tilde\Pi_1 \mathbb{H}_{\mathbb{D}} \tilde\Pi_1 = \mathbb{H} \tilde\Pi_1 \cong \mathbb{H}$ is a division ring, so $\tilde\Pi_1$ is primitive.

The counterpart statement in the biquaternion algebra is different in kind. There the standard idempotents $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$ and $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3)$ are **not** central, the ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ are minimal **left** ideals only, and each is isomorphic to $\mathbb{C}^2$. Here centrality upgrades the left ideals to two-sided ideals and replaces $\mathbb{C}^2$ by the division algebra $\mathbb{H}$. The ideals themselves, their lattice, the distinction between the two summands, and the Peirce decomposition associated with them are developed in *Split-Biquaternion Ideals and Peirce Decomposition*.

## The Dimension of the Set of Idempotents

The set of idempotents of $\mathbb{H}_{\mathbb{D}}$ is the four-point set $\{0, \tilde\Pi_1, \tilde\Pi_2, 1\}$, of real dimension $0$. It is a discrete subset of the centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, whose real dimension is $2$; the four points are its extremal points, and they are exactly the idempotents that the two-dimensional algebra $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ possesses.

This is the sharpest form of the rigidity noted in the introduction. In $\mathbb{B}$ the non-trivial idempotents form a real four-dimensional family with a two-dimensional boundary stratum inherited from the roots of $-1$; in $\mathbb{H}_{\mathbb{D}}$ the corresponding set has collapsed to two isolated points. The collapse is a consequence of the classification theorem: because the algebra is a product of two division algebras, its idempotent set is finite.

## Summary

An idempotent of $\mathbb{H}_{\mathbb{D}}$ is an element $\tilde P$ with $\tilde P^2 = \tilde P$. The algebra has the two nontrivial idempotents

$$
\tilde\Pi_1 = \tfrac{1}{2}(1 + j), \qquad \tilde\Pi_2 = \tfrac{1}{2}(1 - j), \qquad \tilde\Pi_1 \tilde\Pi_2 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = 1,
$$

which are central, lie in the split complex centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, and give the idempotent decomposition $\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2$ into two minimal left ideals, each isomorphic to the quaternion division algebra $\mathbb{H}$.

There are exactly four idempotents, namely $0, \tilde\Pi_1, \tilde\Pi_2, 1$, and all of them are central; equivalently, $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ is a product of two division algebras, and a product of two division algebras has a four-point idempotent set. The nontrivial idempotents $\tilde\Pi_1$ and $\tilde\Pi_2$ are primitive and orthogonal, and together with $0$ and $1$ they exhaust the primitive idempotents. Because there is no bijection with the roots of $-1$ — that set is $S^2 \times S^2$, of dimension $4$ — the biquaternion correspondence between idempotents and roots of $-1$ does not transfer, and the idempotents are confined to the centre. The Hermitian conjugation interchanges $\tilde\Pi_1$ and $\tilde\Pi_2$, so no nontrivial idempotent is Hermitian and the idempotent decomposition is not a decomposition into orthogonal projections. Each nontrivial idempotent is a zero divisor, with annihilator the complementary ideal: $\mathrm{Ann}(\tilde\Pi_1) = \mathbb{H} \tilde\Pi_2$ and $\mathrm{Ann}(\tilde\Pi_2) = \mathbb{H} \tilde\Pi_1$, each of real dimension $4$; the zero divisors themselves form the union of the two ideals, and are treated in *Split-Biquaternion Zero Divisors*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P, e, f$ | Idempotents, $\tilde P^2 = \tilde P$ |
| $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$, $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$ | The two nontrivial idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = 1$ |
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, $\cong \mathbb{H} \oplus \mathbb{H}$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Centre, the split complex subspace; contains every idempotent |
| $\mathbb{H} \tilde\Pi_1, \mathbb{H} \tilde\Pi_2$ | The two minimal left (and two-sided) ideals, each $\cong \mathbb{H}$ |
| $\tilde\Pi_1^{*} = \tilde\Pi_2$, $\tilde\Pi_2^{*} = \tilde\Pi_1$ | The Hermitian conjugation exchanges the idempotents |
| $\mathrm{Ann}(\tilde\Pi_1) = \mathbb{H} \tilde\Pi_2$, $\mathrm{Ann}(\tilde\Pi_2) = \mathbb{H} \tilde\Pi_1$ | Annihilator of an idempotent |
| $\xi$, $\mu_\pm$ | Root of $-1$; unit pure real quaternion components |
| $S^2 \times S^2$ | The topological product form of the root set, established in *Split-Biquaternion Analysis* |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | Split-Biquaternion norm, named only; the subject of *Split-Biquaternion Norm and Invertibility* |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions and their relatives.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the algebraic structure of the split biquaternions and their idempotents.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, primitivity and the Peirce decomposition in semisimple algebras.
