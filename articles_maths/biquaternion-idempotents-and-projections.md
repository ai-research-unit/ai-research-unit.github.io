# __Biquaternion Idempotents and Projections__

## Introduction

The algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations and its six distinguished real subspaces. This article treats the **idempotents** of $\mathbb{B}$ — the elements satisfying $\tilde\Pi^2 = \tilde\Pi$ — and the projections and direct sum decompositions they carry.

Idempotents are the algebraic form of a projection, and in $\mathbb{B}$ they do four separate jobs at once:

1. they give the direct sum decompositions of the algebra into left ideals, and in particular the two minimal left ideals;
2. they classify the non-pure zero divisors, every one of which is a complex multiple of an idempotent;
3. they are in bijection with the roots of $-1$, so the classification of the idempotents is exactly the classification of those roots;
4. they drive the Peirce decomposition of the algebra.

The material here was previously distributed over the article on ideals, the article on zero divisors, the article on the roots of minus one and the worked examples. It is collected here because the four statements above are one subject: the idempotent.

**Placement.** The article is third in the Algebra group, after the algebra and the norm forms and before the roots of $-1$, the zero divisors and the ideals, because all of those use the idempotents. Its own proofs use only the algebra article: the roots of $-1$ enter as a parameter set whose classification is quoted from *Biquaternion Roots of Minus One*, and the relations to the zero divisors and to the ideals are forward pointers.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ and $e_1 e_2 = e_3$, and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$; the scalar part is $Q_0$ and $\mathbf{B}$ denotes a pure biquaternion, $\mathbf{B} = B_1 e_1 + B_2 e_2 + B_3 e_3$. On pure elements the bilinear form is

$$
(\mathbf{A}, \mathbf{B}) = \sum_{k=1}^{3} A_k B_k,
$$

so that a pure element satisfies $\mathbf{B}^2 = -(\mathbf{B}, \mathbf{B}) e_0$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ and decides invertibility. The six subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian sectors $\mathbb{M}_+$ and $\mathbb{M}_-$.

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

the first two because $e_3 \tilde\Pi_1 = (e_3 + i e_3^2)/2 = (e_3 - i)/2 = -i\,\tilde\Pi_1$ and similarly for $\tilde\Pi_2$. The consequence used in §*Idempotents and the Minimal Left Ideals* is that the four products $e_\mu \tilde\Pi_1$ reduce to $\tilde\Pi_1$ and $e_1 \tilde\Pi_1$, so that $\{\tilde\Pi_1, e_1 \tilde\Pi_1\}$ is a basis of $\mathbb{B}\tilde\Pi_1$ over $\mathbb{C}$.

## The Classification of the Idempotents

**Theorem.** Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_0$) or of the form

$$
\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi \in \mathbb{B}$ is a root of $-1$, i.e. $\xi^2 = -1$. There are no other idempotents in $\mathbb{B}$.

**Proof.** Write $\tilde\Pi = A e_0 + \mathbf{B}$ with $A \in \mathbb{C}$ and $\mathbf{B}$ pure. Then

$$
\tilde\Pi^2 = (A^2 - (\mathbf{B}, \mathbf{B})) e_0 + 2 A \mathbf{B}.
$$

Equating to $\tilde\Pi = A e_0 + \mathbf{B}$ gives the two equations

$$
A^2 - (\mathbf{B}, \mathbf{B}) = A, \qquad 2 A \mathbf{B} = \mathbf{B}.
$$

If $\mathbf{B} = 0$, then $A^2 = A$, so $A = 0$ or $A = 1$, giving the trivial idempotents. If $\mathbf{B} \neq 0$, then the second equation gives $A = 1/2$. Substituting into the first gives $1/4 - (\mathbf{B}, \mathbf{B}) = 1/2$, so $(\mathbf{B}, \mathbf{B}) = -1/4$.

Define $\xi = -2 i \mathbf{B}$. Then $\xi$ is pure, and

$$
(\xi, \xi) = \sum_{k=1}^{3} (-2 i B_k)^2 = -4 \sum_{k=1}^{3} B_k^2 = -4 (\mathbf{B}, \mathbf{B}) = 1,
$$

so $\xi^2 = -(\xi, \xi) = -1$. Thus $\xi$ is a root of $-1$, and $\mathbf{B} = \xi \cdot (i/2)$. Hence

$$
\tilde\Pi = \tfrac{1}{2} e_0 + \tfrac{1}{2} \xi i.
$$

The sign choice arises from replacing $\xi$ by $-\xi$, which is also a root of $-1$. $\square$

The trivial idempotents correspond to the degenerate roots $\xi = \pm i$: with $\xi = i$, the formula gives $\tilde\Pi = \frac{1}{2} e_0 + \frac{1}{2} i \cdot i = \frac{1}{2} e_0 - \frac{1}{2} e_0 = 0$; with $\xi = -i$, it gives $\tilde\Pi = \frac{1}{2} e_0 - \frac{1}{2} i \cdot i = \frac{1}{2} e_0 + \frac{1}{2} e_0 = e_0$.

The classification is a classification of the idempotents only because the roots of $-1$ are classified, and that classification is the subject of *Biquaternion Roots of Minus One*, which follows this article. The three families it produces — the trivial roots $\pm i$, the real quaternion roots $\pm\mu$ over unit pure real quaternions, and the non-trivial roots $b\mu + d\nu i$ — give the three families of idempotents in §*The Bijection With the Roots of Minus One*.

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

where $\xi^2 i^2 = (-1)(-1) = 1$ and $e_0$ commutes with $\xi i$. *Injective:* $\tilde\Pi_+(\xi) = \tilde\Pi_+(\xi')$ gives $\xi i = \xi' i$, hence $\xi = \xi'$. *Surjective:* the classification theorem says every idempotent is $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ for some root $\xi$, and $\tilde\Pi_-(\xi) = \tfrac{1}{2}(e_0 - \xi i) = \tilde\Pi_+(-\xi)$, while $-\xi$ is again a root of $-1$. $\square$

Consequently the **complementary pairs** $\{\tilde\Pi, e_0 - \tilde\Pi\}$ of idempotents are in bijection with the roots of $-1$ modulo the sign identification $\xi \sim -\xi$, since

$$
\tilde\Pi_+(-\xi) = \tfrac{1}{2}(e_0 - \xi i) = e_0 - \tilde\Pi_+(\xi).
$$

Thus $\tilde\Pi_+(\xi)$ and $\tilde\Pi_+(-\xi)$ are the two members of a complementary pair, and the pair corresponds to the class $\{\xi, -\xi\}$.

Substituting the classification of $\xi$ of *Biquaternion Roots of Minus One* gives the three families of idempotents:

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

A **Hermitian idempotent**, $\tilde\Pi^\dagger = \tilde\Pi$, is an **orthogonal** projection with respect to the Hermitian form, and it is the kind that occurs in the spectral decomposition of a Hermitian element. Since $\tilde\Pi^\dagger = \bar{\tilde\Pi}^{*}$, the Hermitian idempotents are the idempotents of the second family of §*The Bijection With the Roots of Minus One*, and they lie in $\mathbb{M}_+$.

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

## Idempotents and the Minimal Left Ideals

**Proposition.** The left ideals

$$
\mathbb{B}\tilde\Pi_1 = \{\tilde{Q}\tilde\Pi_1 : \tilde{Q} \in \mathbb{B}\}, \qquad \mathbb{B}\tilde\Pi_2 = \{\tilde{Q}\tilde\Pi_2 : \tilde{Q} \in \mathbb{B}\}
$$

satisfy $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ as left $\mathbb{B}$-modules, and each has dimension $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$ and is a minimal left ideal.

**Proof.** Every $\tilde{Q}$ satisfies $\tilde{Q} = \tilde{Q}(\tilde\Pi_1 + \tilde\Pi_2) = \tilde{Q}\tilde\Pi_1 + \tilde{Q}\tilde\Pi_2$, and the intersection of the two ideals is zero because $\tilde\Pi_1\tilde\Pi_2 = 0$: if $\tilde{Q}\tilde\Pi_1 = \tilde{P}\tilde\Pi_2$ then multiplying on the right by $\tilde\Pi_1$ gives $\tilde{Q}\tilde\Pi_1 = 0$. For the dimension, the relations $e_3\tilde\Pi_1 = -i\tilde\Pi_1$ and $e_2\tilde\Pi_1 = ie_1\tilde\Pi_1$ of §*The Standard Idempotents of $\mathbb{B}$* reduce the four products $e_\mu \tilde\Pi_1$ to $\tilde\Pi_1$ and $e_1\tilde\Pi_1$, and the two are independent over $\mathbb{C}$, so $\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}e_1\tilde\Pi_1$ has $\mathbb{C}$-dimension $2$ and $\mathbb{R}$-dimension $4$; the two ideals then span $4 + 4 = 8 = \dim_{\mathbb{R}}\mathbb{B}$. Minimality is the primitivity of $\tilde\Pi_1$: a left ideal $\mathbb{B}\tilde\Pi$ is minimal exactly when the idempotent $\tilde\Pi$ is primitive, which $\tilde\Pi_1$ is. $\square$

**Proposition.** The minimal left ideal $\mathbb{B}\tilde\Pi_1$ has $\mathbb{C}$-basis $\{\tilde\Pi_1, e_1\tilde\Pi_1\}$, and the central element $i$ acts on it as multiplication by $i$.

**Proof.** Every element of $\mathbb{B}\tilde\Pi_1$ is uniquely $\alpha \tilde\Pi_1 + \beta e_1 \tilde\Pi_1$ with $\alpha, \beta \in \mathbb{C}$ by the basis above. Left multiplication by a biquaternion $\tilde{Q}'$ sends $\tilde{Q}\tilde\Pi_1$ to $(\tilde{Q}'\tilde{Q})\tilde\Pi_1$, again an element of $\mathbb{B}\tilde\Pi_1$; the ideal is stable under left multiplication. Since $i$ is central, $i(\alpha \tilde\Pi_1 + \beta e_1\tilde\Pi_1) = (i\alpha)\tilde\Pi_1 + (i\beta)e_1\tilde\Pi_1$, so $i$ acts as multiplication by $i$. $\square$

**Corollary (the module structure).** $\mathbb{B}$ is a free left module of rank one over itself — the unit $e_0$ is a basis — and, as a module, it decomposes as $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$; each summand is a simple left $\mathbb{B}$-module, and since $\mathbb{B}$ is simple all its simple left modules are isomorphic, so the two summands are isomorphic.

The two ideals here are the minimal left ideals of the projective line of left ideals of *Biquaternion Ideals and Peirce Decomposition*.

## The Dimension of the Set of Idempotents

The idempotents correspond bijectively to the roots of $-1$, so they inherit the size of that set. The roots form a stratified space of real dimension $4$ — the non-trivial family $b\mu + d\nu i$ — with a two-dimensional boundary stratum (the real roots, $S^2$) and two isolated points (the trivial roots, $\pm i$).

The trivial roots $\pm i$ map to the trivial idempotents $0$ and $e_0$, which are excluded from the non-trivial idempotents, so there are no isolated points among the non-trivial idempotents: they form a set of real dimension $4$ with a two-dimensional boundary stratum inherited from the real roots. The non-trivial idempotents sit inside the six-real-dimensional zero divisor set of $\mathbb{B}$, the trivial ones outside it. The dimension statements for the roots themselves are in *Biquaternion Roots of Minus One*.

## Summary

An idempotent of $\mathbb{B}$ is an element $\tilde\Pi$ with $\tilde\Pi^2 = \tilde\Pi$. The algebra has the standard orthogonal idempotents

$$
\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3), \qquad \tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3), \qquad \tilde\Pi_1\tilde\Pi_2 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = e_0,
$$

and they give the decomposition $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$ into two minimal left ideals.

Every idempotent is either trivial or of the form $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ with $\xi^2 = -1$, and the map $\xi \mapsto \tfrac{1}{2}(e_0 + \xi i)$ is a bijection from the roots of $-1$ onto the idempotents, under which complementary pairs of idempotents correspond to the classes $\{\xi, -\xi\}$. The three families of roots — trivial, real and non-trivial — give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and idempotents lying in none of the four four-dimensional subspaces. Every non-pure zero divisor $\tilde{Q}$ with $Q_0 \neq 0$ satisfies $\tilde{Q}^2 = 2Q_0\tilde{Q}$ and is the complex multiple $\tilde{Q} = 2Q_0\tilde\Pi$ of an idempotent; the development of that family is in *Biquaternion Zero Divisors*. Idempotents and their complements split the algebra as $\mathbb{B} = \tilde\Pi\mathbb{B} \oplus (e_0-\tilde\Pi)\mathbb{B}$, which is the algebraic form of a projection and its complementary projection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi$ | Idempotent, $\tilde\Pi^2 = \tilde\Pi$ (of $\mathbb{B}$, or of a general associative unital algebra) |
| $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3)$ | The standard orthogonal idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = e_0$ |
| $\xi$ | A root of $-1$, $\xi^2 = -1$ |
| $\tilde\Pi_+(\xi) = \tfrac{1}{2}(e_0 + \xi i)$ | The idempotent of the root $\xi$; $\xi \mapsto \tilde\Pi_+(\xi)$ is a bijection |
| $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The two minimal left ideals |
| $(\mathbf{A}, \mathbf{B}) = \sum_k A_k B_k$ | Bilinear form on the pure part; $\mathbf{B}^2 = -(\mathbf{B},\mathbf{B})e_0$ |
| $\mathbb{M}_+$ | Hermitian subspace, containing the Hermitian idempotents |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form, deciding invertibility |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the idempotents of the biquaternion algebra and its matrix model.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the idempotent structure in the applied setting.
