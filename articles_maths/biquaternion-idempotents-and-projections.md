# __Biquaternion Idempotents and Projections__

## Introduction

The algebra article defined the biquaternion algebra $\mathbb{B}$, its conjugations and its six distinguished real subspaces. This article treats the **idempotents** of $\mathbb{B}$ — the elements satisfying $\tilde{P}^2 = \tilde{P}$ — and the projections and direct sum decompositions they carry.

Idempotents are the algebraic form of a projection, and in $\mathbb{B}$ they do four separate jobs at once:

1. they give the direct sum decompositions of the algebra into left ideals, and in particular the two minimal left ideals;
2. they classify the non-pure zero divisors, every one of which is a complex multiple of an idempotent;
3. they are in bijection with the roots of $-1$, so the classification of the idempotents is exactly the classification of those roots;
4. they drive the Peirce decomposition and the matrix-unit model of the algebra.

The material here was previously distributed over the article on ideals, the article on zero divisors, the article on the roots of minus one and the worked examples. It is collected here because the four statements above are one subject: the idempotent.

**Placement.** The article is third in the Algebra group, after the algebra and the norm forms and before the roots of $-1$, the zero divisors and the ideals, because all of those use the idempotents. Its own proofs use only the algebra article: the roots of $-1$ enter as a parameter set whose classification is quoted from *Biquaternion Roots of Minus One*, and the relations to the zero divisors and to the ideals are forward pointers.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ and $e_1 e_2 = e_3$, and central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$; the scalar part is $Q_0$ and $\mathbf{B}$ denotes a pure biquaternion, $\mathbf{B} = B_1 e_1 + B_2 e_2 + B_3 e_3$. On pure elements the bilinear form is

$$
(\mathbf{A}, \mathbf{B}) = \sum_{k=1}^{3} A_k B_k,
$$

so that a pure element satisfies $\mathbf{B}^2 = -(\mathbf{B}, \mathbf{B}) e_0$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ and decides invertibility. The six subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and anti-quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian sectors $\mathbb{M}_+$ and $\mathbb{M}_-$.

## 1. Idempotents in an Algebra

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$. Idempotents encode direct summands: for an idempotent $e$,

$$
A = Ae \oplus A(1-e) \quad (\text{left}), \qquad A = eA \oplus (1-e)A \quad (\text{right}),
$$

and every such decomposition of the regular module arises from an idempotent. Two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$; then $e+f$ is again idempotent. A family $\{e_1, \dots, e_n\}$ is pairwise orthogonal if $e_i e_j = 0$ for $i \neq j$, and **complete** if in addition $\sum_i e_i = 1$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents. The criterion used throughout, valid for a semisimple algebra $A$, is

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

Since $\mathbb{B} \cong M_2(\mathbb{C})$ is semisimple, the criterion applies to it, and it is the reason the idempotent and the ideal theories of this series are two views of one subject.

## 2. The Standard Idempotents of $\mathbb{B}$

Over $\mathbb{C}$, put

$$
p = \frac{e_0 + i e_3}{2}, \qquad q = \frac{e_0 - i e_3}{2}.
$$

Since $i$ is central and $(i e_3)^2 = i^2 e_3^2 = (-1)(-1) = 1$, one has $p^2 = p$, $q^2 = q$ and

$$
pq = qp = \frac{e_0 - (i e_3)^2}{4} = 0, \qquad p + q = e_0.
$$

So $p$ and $q$ are orthogonal idempotents summing to the unit. They are not central: $e_1$ anticommutes with $i e_3$, hence does not commute with $p$ or $q$. Under $\mathbb{B} \cong M_2(\mathbb{C})$ they correspond to the diagonal matrix units,

$$
\Phi(p) = \tfrac{1}{2}(I_2 + \sigma_3) = \operatorname{diag}(1,0) = E_{11}, \qquad \Phi(q) = \tfrac{1}{2}(I_2 - \sigma_3) = \operatorname{diag}(0,1) = E_{22},
$$

and each is primitive. These two are the standard idempotents of the algebra.

Left multiplication by $e_3$ and by $e_2$ acts on them as

$$
e_3 p = -i p, \qquad e_3 q = i q, \qquad e_2 p = i e_1 p,
$$

the first two because $e_3 p = (e_3 + i e_3^2)/2 = (e_3 - i)/2 = -i\,p$ and similarly for $q$. The consequence used in Section 7 is that the four products $e_\mu p$ reduce to $p$ and $e_1 p$, so that $\{p, e_1 p\}$ is a basis of $\mathbb{B}p$ over $\mathbb{C}$.

## 3. The Classification of the Idempotents

**Theorem.** Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_0$) or of the form

$$
\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi \in \mathbb{B}$ is a root of $-1$, i.e. $\xi^2 = -1$. There are no other idempotents in $\mathbb{B}$.

**Proof.** Write $\tilde{P} = A e_0 + \mathbf{B}$ with $A \in \mathbb{C}$ and $\mathbf{B}$ pure. Then

$$
\tilde{P}^2 = (A^2 - (\mathbf{B}, \mathbf{B})) e_0 + 2 A \mathbf{B}.
$$

Equating to $\tilde{P} = A e_0 + \mathbf{B}$ gives the two equations

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
\tilde{P} = \tfrac{1}{2} e_0 + \tfrac{1}{2} \xi i.
$$

The sign choice arises from replacing $\xi$ by $-\xi$, which is also a root of $-1$. $\square$

The trivial idempotents correspond to the degenerate roots $\xi = \pm i$: with $\xi = i$, the formula gives $\tilde{P} = \frac{1}{2} e_0 + \frac{1}{2} i \cdot i = \frac{1}{2} e_0 - \frac{1}{2} e_0 = 0$; with $\xi = -i$, it gives $\tilde{P} = \frac{1}{2} e_0 - \frac{1}{2} i \cdot i = \frac{1}{2} e_0 + \frac{1}{2} e_0 = e_0$.

The classification is a classification of the idempotents only because the roots of $-1$ are classified, and that classification is the subject of *Biquaternion Roots of Minus One*, which follows this article. The three families it produces — the trivial roots $\pm i$, the real quaternion roots $\pm\mu$ over unit pure real quaternions, and the non-trivial roots $b\mu + d\nu i$ — give the three families of idempotents in Section 4.

## 4. The Bijection With the Roots of Minus One

**Theorem.** The map

$$
\xi \longmapsto P_+(\xi), \qquad P_+(\xi) = \tfrac{1}{2}(e_0 + \xi i),
$$

is a **bijection** from the set of roots of $-1$ onto the set of idempotents of $\mathbb{B}$.

**Proof.** *Well defined:* if $\xi^2 = -1$, then

$$
P_+(\xi)^2 = \tfrac{1}{4}(e_0 + \xi i)^2 = \tfrac{1}{4}(e_0 + 2\xi i + \xi^2 i^2) = \tfrac{1}{4}(e_0 + 2\xi i + 1) = \tfrac{1}{2}(e_0 + \xi i) = P_+(\xi),
$$

where $\xi^2 i^2 = (-1)(-1) = 1$ and $e_0$ commutes with $\xi i$. *Injective:* $P_+(\xi) = P_+(\xi')$ gives $\xi i = \xi' i$, hence $\xi = \xi'$. *Surjective:* the classification theorem says every idempotent is $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ for some root $\xi$, and $P_-(\xi) = \tfrac{1}{2}(e_0 - \xi i) = P_+(-\xi)$, while $-\xi$ is again a root of $-1$. $\square$

Consequently the **complementary pairs** $\{\tilde{P}, e_0 - \tilde{P}\}$ of idempotents are in bijection with the roots of $-1$ modulo the sign identification $\xi \sim -\xi$, since

$$
P_+(-\xi) = \tfrac{1}{2}(e_0 - \xi i) = e_0 - P_+(\xi).
$$

Thus $P_+(\xi)$ and $P_+(-\xi)$ are the two members of a complementary pair, and the pair corresponds to the class $\{\xi, -\xi\}$.

Substituting the classification of $\xi$ of *Biquaternion Roots of Minus One* gives the three families of idempotents:

- For the trivial root $\xi = \pm i$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} i \cdot i = \tfrac{1}{2} e_0 \mp \tfrac{1}{2} e_0$, giving $\tilde{P} = 0$ or $\tilde{P} = e_0$. These are the **trivial idempotents**.
- For the real root $\xi = \pm \mu$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \mu i$. Since $\mu i$ is Hermitian when $\mu$ is a unit pure real quaternion, $(\mu i)^\dagger = \mu i$, these are the **Hermitian idempotents**, and they lie in the Hermitian subspace $\mathbb{M}_+$; they are the projections that occur in the biquaternion spectral theorem, treated in *Biquaternion Spectral Theory*.
- For the non-trivial root $\xi = b\mu + d\nu i$: $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu + d\nu i) i = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} (b\mu i - d\nu)$. These idempotents combine a real scalar part, a real vector part in the direction of $\nu$ and an imaginary vector part in the direction of $\mu$. Since their vector part mixes a real and an imaginary direction, they lie in none of the four four-dimensional subspaces.

## 5. Idempotents as Projections

An idempotent $\tilde{P}$ satisfies $\tilde{P}^2 = \tilde{P}$. Its **complement** $e_0 - \tilde{P}$ is also an idempotent, and

$$
\tilde{P}(e_0 - \tilde{P}) = \tilde{P} - \tilde{P}^2 = 0,
$$

so the pair $\{\tilde{P}, e_0 - \tilde{P}\}$ gives a **direct sum decomposition** of the underlying $\mathbb{C}$-module:

$$
\mathbb{B} = \tilde{P}\mathbb{B} \oplus (e_0 - \tilde{P})\mathbb{B},
$$

and equally $\mathbb{B} = \mathbb{B}\tilde{P} \oplus \mathbb{B}(e_0 - \tilde{P})$ on the other side. This is the algebraic content of the statement that idempotents correspond to projections: the idempotent is the projection, its complement is the complementary projection, and the algebra splits into the image of one and the image of the other.

A **Hermitian idempotent**, $\tilde{P}^\dagger = \tilde{P}$, is an **orthogonal** projection with respect to the Hermitian form, and it is the kind that occurs in the spectral decomposition of a Hermitian element. Since $\tilde{P}^\dagger = \bar{\tilde{P}}^{*}$, the Hermitian idempotents are the idempotents of the second family of Section 4, and they lie in $\mathbb{M}_+$.

## 6. Idempotents and the Non-Pure Zero Divisors

A nontrivial idempotent is a zero divisor, since

$$
\tilde{P}(e_0 - \tilde{P}) = \tilde{P} - \tilde{P}^2 = 0,
$$

and both factors are nonzero unless $\tilde{P}$ is $0$ or $e_0$. Conversely, every non-pure zero divisor — every zero divisor with $Q_0 \neq 0$ — is a complex multiple of a nontrivial idempotent,

$$
\tilde{Q} = 2 Q_0 \tilde{P}, \qquad \tilde{P} = \frac{\tilde{Q}}{2 Q_0}.
$$

The derivation, from the square relation $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$ that the non-pure family satisfies, together with the structure of the two families and their distribution among the six subspaces, is the subject of *Biquaternion Zero Divisors*, which follows this article.

## 7. Idempotents and the Minimal Left Ideals

**Proposition.** The left ideals

$$
\mathbb{B}p = \{\tilde{Q}p : \tilde{Q} \in \mathbb{B}\}, \qquad \mathbb{B}q = \{\tilde{Q}q : \tilde{Q} \in \mathbb{B}\}
$$

satisfy $\mathbb{B} = \mathbb{B}p \oplus \mathbb{B}q$ as left $\mathbb{B}$-modules, and each has dimension $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$ and is a minimal left ideal.

**Proof.** Every $\tilde{Q}$ satisfies $\tilde{Q} = \tilde{Q}(p + q) = \tilde{Q}p + \tilde{Q}q$, and the intersection of the two ideals is zero because $pq = 0$: if $\tilde{Q}p = \tilde{P}q$ then multiplying on the right by $p$ gives $\tilde{Q}p = 0$. For the dimension, the relations $e_3p = -ip$ and $e_2p = ie_1p$ of Section 2 reduce the four products $e_\mu p$ to $p$ and $e_1p$, and the two are independent over $\mathbb{C}$, so $\mathbb{B}p = \mathbb{C}p \oplus \mathbb{C}e_1p$ has $\mathbb{C}$-dimension $2$ and $\mathbb{R}$-dimension $4$; the two ideals then span $4 + 4 = 8 = \dim_{\mathbb{R}}\mathbb{B}$. Minimality is read in the matrix model: under the isomorphism $\Phi$ of *Biquaternion 2×2 Matrix Representation*, $\Phi(p) = E_{11}$ and $\Phi(q) = E_{22}$, so $\mathbb{B}p$ corresponds to the matrices whose only nonzero column is the first, which is a minimal left ideal of $M_2(\mathbb{C})$. $\square$

**Proposition.** The minimal left ideal $\mathbb{B}p$ is isomorphic to $\mathbb{C}^2$ as a left $\mathbb{B}$-module, and the central element $i$ acts on it as multiplication by $i$.

**Proof.** Every element of $\mathbb{B}p$ is uniquely $\alpha p + \beta e_1 p$ with $\alpha, \beta \in \mathbb{C}$ by the basis above, so the assignment $\alpha p + \beta e_1p \mapsto (\alpha, \beta)$ is a bijection onto $\mathbb{C}^2$. Left multiplication by a biquaternion $\tilde{Q}'$ sends $\tilde{Q}p$ to $(\tilde{Q}'\tilde{Q})p$, again an element of $\mathbb{B}p$, and the coordinates of the image depend linearly on $(\alpha, \beta)$; hence the assignment is an isomorphism of left $\mathbb{B}$-modules. Since $i$ is central, $i(\alpha p + \beta e_1p) = (i\alpha)p + (i\beta)e_1p$, so $i$ acts as multiplication by $i$. $\square$

**Corollary (the module structure).** $\mathbb{B}$ is a free left module of rank one over itself — the unit $e_0$ is a basis — and, as a module, it decomposes as $\mathbb{B} = \mathbb{B}p \oplus \mathbb{B}q$; each summand is a simple left $\mathbb{B}$-module isomorphic to $\mathbb{C}^2$, and since $M_2(\mathbb{C})$ is simple all its simple left modules are isomorphic, so the two summands are isomorphic and correspond to the two columns.

The two ideals here are the minimal left ideals of the projective line of left ideals of *Biquaternion Ideals and Peirce Decomposition*, and the module is the defining module used throughout the representations group. The module itself — its dual, its conjugate and the reality conditions on it — is developed in *Spinors and the Biquaternion Spinor Module*.

## 8. The Dimension of the Set of Idempotents

The idempotents correspond bijectively to the roots of $-1$, so they inherit the size of that set. The roots form a stratified space of real dimension $4$ — the non-trivial family $b\mu + d\nu i$ — with a two-dimensional boundary stratum (the real roots, $S^2$) and two isolated points (the trivial roots, $\pm i$).

The trivial roots $\pm i$ map to the trivial idempotents $0$ and $e_0$, which are excluded from the non-trivial idempotents, so there are no isolated points among the non-trivial idempotents: they form a set of real dimension $4$ with a two-dimensional boundary stratum inherited from the real roots. The non-trivial idempotents sit inside the six-real-dimensional zero divisor set of $\mathbb{B}$, the trivial ones outside it. The dimension statements for the roots themselves are in *Biquaternion Roots of Minus One*.

## Summary

An idempotent of $\mathbb{B}$ is an element $\tilde{P}$ with $\tilde{P}^2 = \tilde{P}$. The algebra has the standard orthogonal idempotents

$$
p = \tfrac{1}{2}(e_0 + ie_3), \qquad q = \tfrac{1}{2}(e_0 - ie_3), \qquad pq = 0, \qquad p + q = e_0,
$$

corresponding to the diagonal matrix units and giving the decomposition $\mathbb{B} = \mathbb{B}p \oplus \mathbb{B}q$ into two minimal left ideals, each isomorphic to $\mathbb{C}^2$ as a left $\mathbb{B}$-module.

Every idempotent is either trivial or of the form $\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$ with $\xi^2 = -1$, and the map $\xi \mapsto \tfrac{1}{2}(e_0 + \xi i)$ is a bijection from the roots of $-1$ onto the idempotents, under which complementary pairs of idempotents correspond to the classes $\{\xi, -\xi\}$. The three families of roots — trivial, real and non-trivial — give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and idempotents lying in none of the four four-dimensional subspaces. Every non-pure zero divisor $\tilde{Q}$ with $Q_0 \neq 0$ satisfies $\tilde{Q}^2 = 2Q_0\tilde{Q}$ and is the complex multiple $\tilde{Q} = 2Q_0\tilde{P}$ of an idempotent; the development of that family is in *Biquaternion Zero Divisors*. Idempotents and their complements split the algebra as $\mathbb{B} = \tilde{P}\mathbb{B} \oplus (e_0-\tilde{P})\mathbb{B}$, which is the algebraic form of a projection and its complementary projection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{P}, e, p, q$ | Idempotents, $\tilde{P}^2 = \tilde{P}$ |
| $p = \tfrac{1}{2}(e_0 + ie_3)$, $q = \tfrac{1}{2}(e_0 - ie_3)$ | The standard orthogonal idempotents, $p + q = e_0$ |
| $\xi$ | A root of $-1$, $\xi^2 = -1$ |
| $P_+(\xi) = \tfrac{1}{2}(e_0 + \xi i)$ | The idempotent of the root $\xi$; $\xi \mapsto P_+(\xi)$ is a bijection |
| $\mathbb{B}p$, $\mathbb{B}q$ | The two minimal left ideals, each $\cong \mathbb{C}^2$ |
| $(\mathbf{A}, \mathbf{B}) = \sum_k A_k B_k$ | Bilinear form on the pure part; $\mathbf{B}^2 = -(\mathbf{B},\mathbf{B})e_0$ |
| $\mathbb{M}_+$ | Hermitian subspace, containing the Hermitian idempotents |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form, deciding invertibility |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the idempotents of the biquaternion algebra and its matrix model.
- S. J. Sangwine, T. A. Ell, N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* 21 (2011) 607–636, for the idempotent structure in the applied setting.
