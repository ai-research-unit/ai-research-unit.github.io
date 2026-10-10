# __Idempotents of the General Plain Algebra__

## Introduction

The algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations and its remarkable real subspaces. This article treats the **idempotents** of $\mathbb{B}$ — the elements satisfying $\tilde\Pi^2 = \tilde\Pi$ — and the projections and direct sum decompositions they carry.

Idempotents are the algebraic form of a projection, and in $\mathbb{B}$ they do four separate jobs at once:

1. they give the direct sum decompositions of the algebra into left ideals, and in particular the two minimal left ideals;
2. they classify the non-pure zero divisors, every one of which is a complex multiple of an idempotent;
3. they are in bijection with the roots of $-1$, so the classification of the idempotents is exactly the classification of those roots;
4. they drive the Peirce decomposition of the algebra.

**Placement.** The article is the third entry of the block, after the algebra and *Biquaternion Norm and Invertibility*, and before the two root articles, the nilpotents, the zero divisors and the ideals, because all of those use the idempotents. Its own proofs use only the algebra article; the classification of the roots of $-1$ is quoted from *Biquaternion Square Roots of Minus One, Zero and Plus One*, and the relations to the zero divisors and to the ideals are forward pointers.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ and $e_1 e_2 = e_3$, and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, the scalar part is $Q_0$, and $\mathbf{B} = B_1 e_1 + B_2 e_2 + B_3 e_3$ denotes a pure biquaternion, for which $\mathbf{A}\mathbf{B} = -\sum_{k} A_k B_k\, e_0 + \mathbf{A}\times\mathbf{B}$ and $\mathbf{B}^2 = -(\sum_k B_k^2) e_0$. The product throughout is the general plain bilinear product $\tilde{Q}\tilde{R}$, the multiplication of the algebra — the only one of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* that is associative and two-sidedly unital, and the one the equation $\tilde\Pi^2 = \tilde\Pi$ presupposes. The other three products carry idempotents of their own, which are not these; the four sets are tabulated in *Comparison Between the Four General Products* and read product by product in *Definitions for the Study of the 12 Algebraic Structures*. The central square $\tilde{Q}\tilde{Q}^{\natural}$, the invertibility criterion and the forms belong to *Biquaternion Norm and Invertibility*, and the remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ are *Introduction to the Remarkable Subspaces*.

## Definition

An element $\tilde\Pi$ of $\mathbb{B}$ is an **idempotent of the general plain algebra** when

$$
\tilde\Pi^2 = \tilde\Pi ,
$$

the square being read in the general plain bilinear product. The equation names a product, so the notion is relative to it; the general definition, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, is *Definitions for the Study of the 12 Algebraic Structures*. Throughout this article the product is the general plain bilinear product, and another product is named where it is meant.

Idempotents encode direct summands of the regular module, $\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}(e_0 - \tilde\Pi)$ on the left and $\mathbb{B} = \tilde\Pi\mathbb{B} \oplus (e_0 - \tilde\Pi)\mathbb{B}$ on the right, and every such decomposition arises from an idempotent. A primitive idempotent — one that is not a sum of two nonzero orthogonal idempotents — generates a minimal left ideal; since $\mathbb{B}$ is semisimple, the corner algebra $\tilde\Pi\mathbb{B}\tilde\Pi$ is then a division ring. This is why the idempotent and the ideal theories of the series are two views of one subject.

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

the first two because $e_3 \tilde\Pi_1 = (e_3 + i e_3^2)/2 = (e_3 - i)/2 = -i\,\tilde\Pi_1$ and similarly for $\tilde\Pi_2$. The companion relations reduce the four general products $e_\mu \tilde\Pi_1$ to $\tilde\Pi_1$ and $e_1 \tilde\Pi_1$, so that $\{\tilde\Pi_1, e_1 \tilde\Pi_1\}$ is a basis of $\mathbb{B}\tilde\Pi_1$ over $\mathbb{C}$. The two ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ that these idempotents generate, their direct-sum decomposition of $\mathbb{B}$, their bases and their module structure are the subject of *Biquaternion Ideals and Peirce Decomposition*.

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
\xi \longmapsto \tilde\Pi_1(\xi), \qquad \tilde\Pi_1(\xi) = \tfrac{1}{2}(e_0 + \xi i),
$$

is a **bijection** from the set of roots of $-1$ onto the set of idempotents of $\mathbb{B}$.

**Proof.** *Well defined:* if $\xi^2 = -1$, then

$$
\tilde\Pi_1(\xi)^2 = \tfrac{1}{4}(e_0 + \xi i)^2 = \tfrac{1}{4}(e_0 + 2\xi i + \xi^2 i^2) = \tfrac{1}{4}(e_0 + 2\xi i + 1) = \tfrac{1}{2}(e_0 + \xi i) = \tilde\Pi_1(\xi),
$$

where $\xi^2 i^2 = (-1)(-1) = 1$ and $e_0$ commutes with $\xi i$. *Injective:* $\tilde\Pi_1(\xi) = \tilde\Pi_1(\xi')$ gives $\xi i = \xi' i$, hence $\xi = \xi'$. *Surjective:* the classification theorem says every idempotent is $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ for some root $\xi$, and $\tilde\Pi_2(\xi) = \tfrac{1}{2}(e_0 - \xi i) = \tilde\Pi_1(-\xi)$, while $-\xi$ is again a root of $-1$.

Consequently the **complementary pairs** $\{\tilde\Pi, e_0 - \tilde\Pi\}$ of idempotents are in bijection with the roots of $-1$ modulo the sign identification $\xi \sim -\xi$, since

$$
\tilde\Pi_1(-\xi) = \tfrac{1}{2}(e_0 - \xi i) = e_0 - \tilde\Pi_1(\xi).
$$

Thus $\tilde\Pi_1(\xi)$ and $\tilde\Pi_1(-\xi)$ are the two members of a complementary pair, and the pair corresponds to the class $\{\xi, -\xi\}$.

Substituting the classification of $\xi$ of *Biquaternion Square Roots of Minus One, Zero and Plus One* gives the three families of idempotents:

- For the trivial root $\xi = \pm i$: $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} i \cdot i = \tfrac{1}{2} e_0 \mp \tfrac{1}{2} e_0$, giving $\tilde\Pi = 0$ or $\tilde\Pi = e_0$. These are the **trivial idempotents**.
- For the real root $\xi = \pm \mu$: $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \mu i$. Since $\mu i$ is Hermitian when $\mu$ is a unit pure real quaternion, $(\mu i)^{*} = \mu i$, these are the **Hermitian idempotents**, and they lie in the Hermitian subspace $\mathbb{M}_+$; they are the projections that occur in the biquaternion spectral theorem, treated in *Biquaternion Spectral Theory*.
- For the non-trivial root $\xi = b\mu + d\nu i$: $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu + d\nu i) i = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu i - d\nu)$. These idempotents combine a real scalar part, a real vector part in the direction of $\nu$ and an imaginary vector part in the direction of $\mu$. Since their vector part mixes a real and an imaginary direction, they lie in none of the four four-dimensional subspaces.

The idempotents inherit the size of the root set. The trivial roots $\pm i$ map to the trivial idempotents $0$ and $e_0$, so the non-trivial idempotents form a set of real dimension $4$, sitting inside the six-real-dimensional zero divisor set of $\mathbb{B}$ with the trivial idempotents outside it; the dimension statements for the roots are in *Biquaternion Square Roots of Minus One, Zero and Plus One*.

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

A **Hermitian idempotent**, $\tilde\Pi^{*} = \tilde\Pi$, is an **orthogonal** projection — orthogonality being read from the Hermitian form of *Biquaternion Norm and Invertibility*, which this article names and does not use — and it is the kind that occurs in the spectral decomposition of a Hermitian element. Since $\tilde\Pi^{*} = \overline{\tilde\Pi^{\natural}}$, the Hermitian idempotents are the idempotents of the second family of §*The Bijection With the Roots of Minus One*, and they lie in $\mathbb{M}_+$.

## Idempotents and the Non-Pure Zero Divisors

A nontrivial idempotent is a zero divisor, since

$$
\tilde\Pi(e_0 - \tilde\Pi) = \tilde\Pi - \tilde\Pi^2 = 0,
$$

and both factors are nonzero unless $\tilde\Pi$ is $0$ or $e_0$. Conversely, every non-pure zero divisor — every zero divisor with $Q_0 \neq 0$ — is a complex multiple of a nontrivial idempotent,

$$
\tilde{Q} = 2 Q_0 \tilde\Pi, \qquad \tilde\Pi = \frac{\tilde{Q}}{2 Q_0}.
$$

The derivation, from the square relation $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$ that the non-pure family satisfies, together with the structure of the two families and their distribution among the remarkable subspaces, is the subject of *Zero Divisors of the General Plain Algebra*, which follows this article.

## Summary

An idempotent of $\mathbb{B}$ is an element $\tilde\Pi$ with $\tilde\Pi^2 = \tilde\Pi$. The algebra carries the standard orthogonal idempotents $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$ and $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3)$, with $\tilde\Pi_1\tilde\Pi_2 = 0$ and $\tilde\Pi_1 + \tilde\Pi_2 = e_0$, and they generate the two minimal left ideals of *Biquaternion Ideals and Peirce Decomposition*.

Every idempotent is either trivial or of the form $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ with $\xi^2 = -1$, and $\xi \mapsto \tfrac{1}{2}(e_0 + \xi i)$ is a bijection from the roots of $-1$ onto the idempotents, carrying the complementary pairs to the classes $\{\xi, -\xi\}$. The three families of roots — trivial, real and non-trivial — give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and idempotents in none of the four four-dimensional subspaces; the non-trivial idempotents form a set of real dimension $4$. An idempotent and its complement split the algebra as $\mathbb{B} = \tilde\Pi\mathbb{B} \oplus (e_0 - \tilde\Pi)\mathbb{B}$, the algebraic form of a projection and its complementary projection, and every non-pure zero divisor is the complex multiple $2Q_0\tilde\Pi$ of a nontrivial idempotent, developed in *Zero Divisors of the General Plain Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi$ | Idempotent, $\tilde\Pi^2 = \tilde\Pi$ (of $\mathbb{B}$, or of a general associative unital algebra) |
| $\tilde\Pi = \Pi_0 e_0 + \boldsymbol{\Pi}$ | Scalar part $\Pi_0 \in \mathbb{C}$ and pure vector part $\boldsymbol{\Pi}$ of an element of $\mathbb{B}$ |
| $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3)$ | The standard orthogonal idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = e_0$ |
| $\xi$ | A root of $-1$, $\xi^2 = -1$ |
| $\tilde\Pi_1(\xi) = \tfrac{1}{2}(e_0 + \xi i)$ | The idempotent of the root $\xi$; $\xi \mapsto \tilde\Pi_1(\xi)$ is a bijection |
| $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The two minimal left ideals |
| $\mathbf{A}\mathbf{B} = -\sum_k A_k B_k\,e_0 + \mathbf{A}\times\mathbf{B}$ | Product of two pure elements; $\mathbf{B}^2 = -(\sum_k B_k^2)e_0$ |
| $\mathbb{M}_+$ | Hermitian subspace, containing the Hermitian idempotents |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of an idempotent, the orthogonal and primitive families and the Peirce decomposition.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`) and *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the two families of the zero-divisor set, of which the idempotents are the non-pure one.
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for the minimal left ideals the standard idempotents generate.
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the classification of the roots of $-1$ that the idempotents are in bijection with.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the idempotents of the biquaternion algebra.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the idempotent structure in the applied setting.
