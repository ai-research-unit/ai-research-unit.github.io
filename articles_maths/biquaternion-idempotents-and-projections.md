# __Biquaternion Idempotents and Projections__

## Introduction

The algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations and its six distinguished real subspaces. This article treats the **idempotents** of $\mathbb{B}$ — the elements satisfying $\tilde\Pi^2 = \tilde\Pi$ — and the projections and direct sum decompositions they carry.

Idempotents are the algebraic form of a projection, and in $\mathbb{B}$ they do four separate jobs at once:

1. they give the direct sum decompositions of the algebra into left ideals, and in particular the two minimal left ideals;
2. they classify the non-pure zero divisors, every one of which is a complex multiple of an idempotent;
3. they are in bijection with the roots of $-1$, so the classification of the idempotents is exactly the classification of those roots;
4. they drive the Peirce decomposition of the algebra.

The material here was previously distributed over the article on ideals, the article on zero divisors, the article on the roots of minus one and the worked examples. It is collected here because the four statements above are one subject: the idempotent.

**Placement.** The article is second in the Algebra group, after the algebra and before the ideals, the roots of $-1$ and the zero divisors, because all of those use the idempotents. Its own proofs use only the algebra article: the roots of $-1$ enter as a parameter set whose classification is quoted from *Biquaternion Square Roots of Minus One, Zero and Plus One*, and the relations to the zero divisors and to the ideals are forward pointers.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ and $e_1 e_2 = e_3$, and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$; the scalar part is $Q_0$ and $\mathbf{B}$ denotes a pure biquaternion, $\mathbf{B} = B_1 e_1 + B_2 e_2 + B_3 e_3$. On pure elements the product is $\mathbf{A}\mathbf{B} = -\sum_{k} A_k B_k\, e_0 + \mathbf{A}\times\mathbf{B}$, so that a pure element satisfies $\mathbf{B}^2 = -(\sum_k B_k^2) e_0$. That the product $\tilde{Q}\bar{\tilde{Q}}$ decides invertibility, and the forms it defines, belong to Topology (*Biquaternion Norm and Invertibility*). The six subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian sectors $\mathbb{M}_+$ and $\mathbb{M}_-$.

## Idempotents in an Algebra

Let $A$ be an associative unital algebra. An element $\tilde\Pi \in A$ is an **idempotent** if $\tilde\Pi^2 = \tilde\Pi$. Idempotents encode direct summands: for an idempotent $\tilde\Pi$,

$$
A = A\tilde\Pi \oplus A(1-\tilde\Pi) \quad (\text{left}), \qquad A = \tilde\Pi A \oplus (1-\tilde\Pi)A \quad (\text{right}),
$$

and every such decomposition of the regular module arises from an idempotent. Two idempotents $\tilde\Pi, \tilde\Pi'$ are **orthogonal** if $\tilde\Pi\tilde\Pi' = \tilde\Pi'\tilde\Pi = 0$; then $\tilde\Pi+\tilde\Pi'$ is again idempotent. A family $\{\tilde\Pi_1, \dots, \tilde\Pi_n\}$ is pairwise orthogonal if $\tilde\Pi_i \tilde\Pi_j = 0$ for $i \neq j$, and **complete** if in addition $\sum_i \tilde\Pi_i = 1$. A nonzero idempotent $\tilde\Pi$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents. The criterion used throughout, valid for a semisimple algebra $A$, is

$$
\tilde\Pi \text{ primitive} \iff A\tilde\Pi \text{ is a minimal left ideal} \iff \tilde\Pi A\tilde\Pi \text{ is a division ring}.
$$

Since $\mathbb{B}$ is semisimple, the criterion applies to it, and it is the reason the idempotent and the ideal theories of this series are two views of one subject.

## The Standard Idempotents of $\mathbb{B}$

Over $\mathbb{C}$, put

$$
\tilde\Pi_1 = \frac{e_0 + i e_3}{2}, \qquad \tilde\Pi_2 = \frac{e_0 - i e_3}{2}.
$$

Since $i$ is central and $(i e_3)^2 = i^2 e_3^2 = (-1)(-1) = 1$, one has $\tilde\Pi_1^2 = \tilde\Pi_1$, $\tilde\Pi_2^2 = \tilde\Pi_2$ and

$$
\tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = \frac{e_0 - (i e_3)^2}{4} = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = e_0.
$$

So $\tilde\Pi_1$ and $\tilde\Pi_2$ are orthogonal idempotents summing to the unit. They are not central: $e_1$ anticommutes with $i e_3$, hence does not commute with $\tilde\Pi_1$ or $\tilde\Pi_2$. Each is primitive, and these two are the standard idempotents of the algebra.

Left multiplication by $e_3$ and by $e_2$ acts on them as

$$
e_3 \tilde\Pi_1 = -i \tilde\Pi_1, \qquad e_3 \tilde\Pi_2 = i \tilde\Pi_2, \qquad e_2 \tilde\Pi_1 = i e_1 \tilde\Pi_1,
$$

the first two because $e_3 \tilde\Pi_1 = (e_3 + i e_3^2)/2 = (e_3 - i)/2 = -i\,\tilde\Pi_1$ and similarly for $\tilde\Pi_2$. The companion relations reduce the four products $e_\mu \tilde\Pi_1$ to $\tilde\Pi_1$ and $e_1 \tilde\Pi_1$, so that $\{\tilde\Pi_1, e_1 \tilde\Pi_1\}$ is a basis of $\mathbb{B}\tilde\Pi_1$ over $\mathbb{C}$. The two ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ that these idempotents generate, their direct-sum decomposition of $\mathbb{B}$, their bases and their module structure are the subject of *Biquaternion Ideals and Peirce Decomposition*.

## The Classification of the Idempotents

**Theorem.** Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_0$) or of the form

$$
\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi \in \mathbb{B}$ is a root of $-1$, i.e. $\xi^2 = -1$. There are no other idempotents in $\mathbb{B}$.

**Proof.** Write $\tilde\Pi = \Pi_0 e_0 + \boldsymbol{\Pi}$ with $\Pi_0 \in \mathbb{C}$ and $\boldsymbol{\Pi}$ pure. Then

$$
\tilde\Pi^2 = (\Pi_0^2 - (\boldsymbol{\Pi}, \boldsymbol{\Pi})) e_0 + 2 \Pi_0 \boldsymbol{\Pi}.
$$

Equating to $\tilde\Pi = \Pi_0 e_0 + \boldsymbol{\Pi}$ gives the two equations

$$
\Pi_0^2 - (\boldsymbol{\Pi}, \boldsymbol{\Pi}) = \Pi_0, \qquad 2 \Pi_0 \boldsymbol{\Pi} = \boldsymbol{\Pi}.
$$

If $\boldsymbol{\Pi} = 0$, then $\Pi_0^2 = \Pi_0$, so $\Pi_0 = 0$ or $\Pi_0 = 1$, giving the trivial idempotents. If $\boldsymbol{\Pi} \neq 0$, then the second equation gives $\Pi_0 = 1/2$. Substituting into the first gives $1/4 - (\boldsymbol{\Pi}, \boldsymbol{\Pi}) = 1/2$, so $(\boldsymbol{\Pi}, \boldsymbol{\Pi}) = -1/4$.

Define $\xi = -2 i \boldsymbol{\Pi}$. Then $\xi$ is pure, and

$$
(\xi, \xi) = \sum_{k=1}^{3} (-2 i \Pi_k)^2 = -4 \sum_{k=1}^{3} \Pi_k^2 = -4 (\boldsymbol{\Pi}, \boldsymbol{\Pi}) = 1,
$$

so $\xi^2 = -(\xi, \xi) = -1$. Thus $\xi$ is a root of $-1$, and $\boldsymbol{\Pi} = \xi \cdot (i/2)$. Hence

$$
\tilde\Pi = \tfrac{1}{2} e_0 + \tfrac{1}{2} \xi i.
$$

The sign choice arises from replacing $\xi$ by $-\xi$, which is also a root of $-1$.

The trivial idempotents correspond to the degenerate roots $\xi = \pm i$: the two signs in $\tfrac{1}{2}(e_0 \pm \xi i)$ give $\tfrac{1}{2}(e_0 + i \cdot i) = 0$ and $\tfrac{1}{2}(e_0 - i \cdot i) = e_0$.

The classification is a classification of the idempotents only because the roots of $-1$ are classified, and that classification is the subject of *Biquaternion Square Roots of Minus One, Zero and Plus One*, which follows this article. The three families it produces — the trivial roots $\pm i$, the real quaternion roots $\pm\mu$ over unit pure real quaternions, and the non-trivial roots $b\mu + d\nu i$ — give the three families of idempotents in §*The Bijection With the Roots of Minus One*.

## The Bijection With the Roots of Minus One

**Theorem.** The map

$$
\xi \longmapsto \tilde\Pi_+(\xi), \qquad \tilde\Pi_+(\xi) = \tfrac{1}{2}(e_0 + \xi i),
$$

is a **bijection** from the set of roots of $-1$ onto the set of idempotents of $\mathbb{B}$.

**Proof.** *Well defined:* if $\xi^2 = -1$, then

$$
\tilde\Pi_+(\xi)^2 = \tfrac{1}{4}(e_0 + \xi i)^2 = \tfrac{1}{4}(e_0 + 2\xi i + \xi^2 i^2) = \tfrac{1}{4}(e_0 + 2\xi i + 1) = \tfrac{1}{2}(e_0 + \xi i) = \tilde\Pi_+(\xi),
$$

where $\xi^2 i^2 = (-1)(-1) = 1$ and $e_0$ commutes with $\xi i$. *Injective:* $\tilde\Pi_+(\xi) = \tilde\Pi_+(\xi')$ gives $\xi i = \xi' i$, hence $\xi = \xi'$. *Surjective:* the classification theorem says every idempotent is $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ for some root $\xi$, and $\tilde\Pi_-(\xi) = \tfrac{1}{2}(e_0 - \xi i) = \tilde\Pi_+(-\xi)$, while $-\xi$ is again a root of $-1$.

Consequently the **complementary pairs** $\{\tilde\Pi, e_0 - \tilde\Pi\}$ of idempotents are in bijection with the roots of $-1$ modulo the sign identification $\xi \sim -\xi$, since

$$
\tilde\Pi_+(-\xi) = \tfrac{1}{2}(e_0 - \xi i) = e_0 - \tilde\Pi_+(\xi).
$$

Thus $\tilde\Pi_+(\xi)$ and $\tilde\Pi_+(-\xi)$ are the two members of a complementary pair, and the pair corresponds to the class $\{\xi, -\xi\}$.

Substituting the classification of $\xi$ of *Biquaternion Square Roots of Minus One, Zero and Plus One* gives the three families of idempotents:

- For the trivial root $\xi = \pm i$: $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} i \cdot i = \tfrac{1}{2} e_0 \mp \tfrac{1}{2} e_0$, giving $\tilde\Pi = 0$ or $\tilde\Pi = e_0$. These are the **trivial idempotents**.
- For the real root $\xi = \pm \mu$: $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \mu i$. Since $\mu i$ is Hermitian when $\mu$ is a unit pure real quaternion, $(\mu i)^\dagger = \mu i$, these are the **Hermitian idempotents**, and they lie in the Hermitian subspace $\mathbb{M}_+$; they are the projections that occur in the biquaternion spectral theorem, treated in *Biquaternion Spectral Theory*.
- For the non-trivial root $\xi = b\mu + d\nu i$: $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu + d\nu i) i = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu i - d\nu)$. These idempotents combine a real scalar part, a real vector part in the direction of $\nu$ and an imaginary vector part in the direction of $\mu$. Since their vector part mixes a real and an imaginary direction, they lie in none of the four four-dimensional subspaces.

## Idempotents as Projections

An idempotent $\tilde\Pi$ satisfies $\tilde\Pi^2 = \tilde\Pi$. Its **complement** $e_0 - \tilde\Pi$ is also an idempotent, and

$$
\tilde\Pi(e_0 - \tilde\Pi) = \tilde\Pi - \tilde\Pi^2 = 0,
$$

so the pair $\{\tilde\Pi, e_0 - \tilde\Pi\}$ gives a **direct sum decomposition** of the underlying $\mathbb{C}$-module:

$$
\mathbb{B} = \tilde\Pi\mathbb{B} \oplus (e_0 - \tilde\Pi)\mathbb{B},
$$

and equally $\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}(e_0 - \tilde\Pi)$ on the other side. This is the algebraic content of the statement that idempotents correspond to projections: the idempotent is the projection, its complement is the complementary projection, and the algebra splits into the image of one and the image of the other.

A **Hermitian idempotent**, $\tilde\Pi^\dagger = \tilde\Pi$, is an **orthogonal** projection — orthogonality being read from the Hermitian form of *Biquaternion Norm and Invertibility*, which this article names and does not use — and it is the kind that occurs in the spectral decomposition of a Hermitian element. Since $\tilde\Pi^\dagger = \bar{\tilde\Pi}^{*}$, the Hermitian idempotents are the idempotents of the second family of §*The Bijection With the Roots of Minus One*, and they lie in $\mathbb{M}_+$.

## Idempotents and the Non-Pure Zero Divisors

A nontrivial idempotent is a zero divisor, since

$$
\tilde\Pi(e_0 - \tilde\Pi) = \tilde\Pi - \tilde\Pi^2 = 0,
$$

and both factors are nonzero unless $\tilde\Pi$ is $0$ or $e_0$. Conversely, every non-pure zero divisor — every zero divisor with $Q_0 \neq 0$ — is a complex multiple of a nontrivial idempotent,

$$
\tilde{Q} = 2 Q_0 \tilde\Pi, \qquad \tilde\Pi = \frac{\tilde{Q}}{2 Q_0}.
$$

The derivation, from the square relation $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$ that the non-pure family satisfies, together with the structure of the two families and their distribution among the six subspaces, is the subject of *Biquaternion Zero Divisors*, which follows this article.

## The Dimension of the Set of Idempotents

The idempotents correspond bijectively to the roots of $-1$, so they inherit the size of that set. The roots have a non-trivial family of real dimension $4$, a real family of real dimension $2$, and two isolated points (the trivial roots, $\pm i$); the topological description of the set is in *Biquaternion Topology*.

The trivial roots $\pm i$ map to the trivial idempotents $0$ and $e_0$, which are excluded from the non-trivial idempotents, so there are no isolated points among the non-trivial idempotents: they form a set of real dimension $4$. The non-trivial idempotents sit inside the six-real-dimensional zero divisor set of $\mathbb{B}$, the trivial ones outside it. The dimension statements for the roots themselves are in *Biquaternion Square Roots of Minus One, Zero and Plus One*.

## Summary

An idempotent of $\mathbb{B}$ is an element $\tilde\Pi$ with $\tilde\Pi^2 = \tilde\Pi$. The algebra has the standard orthogonal idempotents

$$
\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3), \qquad \tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3), \qquad \tilde\Pi_1\tilde\Pi_2 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = e_0,
$$

and they generate the two minimal left ideals, developed in *Biquaternion Ideals and Peirce Decomposition*.

Every idempotent is either trivial or of the form $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ with $\xi^2 = -1$, and the map $\xi \mapsto \tfrac{1}{2}(e_0 + \xi i)$ is a bijection from the roots of $-1$ onto the idempotents, under which complementary pairs of idempotents correspond to the classes $\{\xi, -\xi\}$. The three families of roots — trivial, real and non-trivial — give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and idempotents lying in none of the four four-dimensional subspaces. Every non-pure zero divisor $\tilde{Q}$ with $Q_0 \neq 0$ satisfies $\tilde{Q}^2 = 2Q_0\tilde{Q}$ and is the complex multiple $\tilde{Q} = 2Q_0\tilde\Pi$ of an idempotent; the development of that family is in *Biquaternion Zero Divisors*. Idempotents and their complements split the algebra as $\mathbb{B} = \tilde\Pi\mathbb{B} \oplus (e_0-\tilde\Pi)\mathbb{B}$, which is the algebraic form of a projection and its complementary projection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi$ | Idempotent, $\tilde\Pi^2 = \tilde\Pi$ (of $\mathbb{B}$, or of a general associative unital algebra) |
| $\tilde\Pi = \Pi_0 e_0 + \boldsymbol{\Pi}$ | Scalar part $\Pi_0 \in \mathbb{C}$ and pure vector part $\boldsymbol{\Pi}$ of an element of $\mathbb{B}$ |
| $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3)$ | The standard orthogonal idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = e_0$ |
| $\xi$ | A root of $-1$, $\xi^2 = -1$ |
| $\tilde\Pi_+(\xi) = \tfrac{1}{2}(e_0 + \xi i)$ | The idempotent of the root $\xi$; $\xi \mapsto \tilde\Pi_+(\xi)$ is a bijection |
| $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The two minimal left ideals |
| $\mathbf{A}\mathbf{B} = -\sum_k A_k B_k\,e_0 + \mathbf{A}\times\mathbf{B}$ | Product of two pure elements; $\mathbf{B}^2 = -(\sum_k B_k^2)e_0$ |
| $\mathbb{M}_+$ | Hermitian subspace, containing the Hermitian idempotents |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the idempotents of the biquaternion algebra and its matrix model.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the idempotent structure in the applied setting.
