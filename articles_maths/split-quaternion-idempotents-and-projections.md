
# __Split-Quaternion Idempotents and Projections__

## Introduction

The algebra article defined the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$, its basis $1, e_1, e_2, e_3$, its conjugation, its central product $\tilde q\bar{\tilde q}$ and its distinguished subspaces. This article treats the **idempotents** of $\mathbb{H}_{\mathrm{s}}$ — the elements $\tilde\pi$ with $\tilde\pi^2 = \tilde\pi$ — and the projections and direct sum decompositions they carry.

Idempotents are the algebraic form of a projection, and in $\mathbb{H}_{\mathrm{s}}$ they do four jobs at once:

1. they give direct sum decompositions of the algebra into left ideals, and in particular the two minimal left ideals;
2. they are the non-scalar solutions of the quadratic equation $\tilde\pi^2 = \tilde\pi$, and they are in bijection with the roots of $+1$ in the vector part;
3. they account for the non-nilpotent part of the zero divisor set;
4. they drive the Peirce decomposition and the matrix-unit model of the algebra.

The last two items are developed in the companion articles *Split-Quaternion Zero Divisors* and *Split-Quaternion Ideals and Peirce Decomposition*; here they enter only as forward pointers.

**Placement.** The article is third in the Algebra group, after the algebra and before the roots of $-1$, the zero divisors and the ideals, because the ideals and the zero divisors both use the idempotents. Its proofs use only the algebra article and the algebraic product $\tilde q\bar{\tilde q}$; the classification of the non-scalar idempotents is proved here from the quadratic equation, so nothing is quoted from the roots of $-1$ article, which is the companion classification of the opposite sign.

**Conventions.** The algebra is $\mathbb{H}_{\mathrm{s}} = \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$, with basis $1, e_1, e_2, e_3$, the relations $e_1^2 = -1$, $e_2^2 = +1$, $e_3 = e_1 e_2$ and $e_1 e_2 = -e_2 e_1$. A general element is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, its scalar part is $q_0 = \operatorname{Sc}(\tilde q)$ and its vector part is $\mathbf{v} = q_1 e_1 + q_2 e_2 + q_3 e_3$. The conjugation is $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$. The product $\tilde q\bar{\tilde q}$ lies in the centre and is written

$$
N(\tilde q) = \tilde q\bar{\tilde q} = q_0^2 + q_1^2 - q_2^2 - q_3^2 ;
$$

it is formed and evaluated here as an algebraic product, and its metrical reading — the signature of the pairings, their isotropy and the group of units — is in *Split-Quaternion Norm and Invertibility*. The scalar subspace is $S = \mathbb{R}\cdot 1$ and the vector subspace is $V = \operatorname{span}\{e_1, e_2, e_3\}$; on $V$ the square of an element is minus that product, $\mathbf{v}^2 = -N(\mathbf{v})$.

## Idempotents in an Algebra

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$. Idempotents encode direct summands: for an idempotent $e$,

$$
A = Ae \oplus A(1-e) \quad (\text{left}), \qquad A = eA \oplus (1-e)A \quad (\text{right}),
$$

and every decomposition of the regular module into a direct sum of two submodules arises from an idempotent. Two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$; then $e + f$ is again idempotent. A family $\{e_1, \dots, e_n\}$ is pairwise orthogonal if $e_i e_j = 0$ for $i \neq j$, and **complete** if in addition $\sum_i e_i = 1$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents. The criterion used throughout, valid for a semisimple algebra $A$, is

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

The algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ is simple, hence semisimple, so the criterion applies to it, and it is the reason the idempotent and the ideal theories of this category are two views of one subject.

## The Standard Idempotents of $\mathbb{H}_{\mathrm{s}}$

Put

$$
\tilde\pi_+ = \tfrac{1}{2}(1 + e_2), \qquad \tilde\pi_- = \tfrac{1}{2}(1 - e_2).
$$

Since $e_2^2 = +1$, one has $\tilde\pi_+^2 = \tilde\pi_+$, $\tilde\pi_-^2 = \tilde\pi_-$ and

$$
\tilde\pi_+ \tilde\pi_- = \tilde\pi_- \tilde\pi_+ = \tfrac{1}{4}(1 - e_2^2) = 0, \qquad \tilde\pi_+ + \tilde\pi_- = 1.
$$

So $\tilde\pi_+$ and $\tilde\pi_-$ are orthogonal idempotents summing to the unit. They are **not central**: the element $e_1$ anticommutes with $e_2$, hence

$$
e_1 \tilde\pi_+ = \tfrac{1}{2}(e_1 + e_3), \qquad \tilde\pi_+ e_1 = \tfrac{1}{2}(e_1 - e_3),
$$

and the two differ, which is the non-centrality of $\tilde\pi_\pm$ in the algebra; the two idempotents are the idempotents of the split-complex subalgebra $\operatorname{span}\{1, e_2\}$.

Neither is central: an element commuting with $\tilde\pi_+$ commutes with $e_2 = 2\tilde\pi_+ - 1$, and the centraliser of $e_2$ in $\mathbb{H}_{\mathrm{s}}$ is the split-complex plane $\operatorname{span}\{1, e_2\}$, since $e_1$ and $e_3$ anticommute with $e_2$. Both idempotents are primitive: if $\tilde\pi_+ = p + q$ with $p, q$ orthogonal idempotents, then $p$ and $q$ commute with $\tilde\pi_+$ and so lie in $\operatorname{span}\{1, e_2\}$, whose only idempotents are $0, 1, \tilde\pi_+, \tilde\pi_-$, and no nontrivial orthogonal pair among these sums to $\tilde\pi_+$. Unlike the biquaternion case, where the two idempotents are the diagonal idempotents on which the central unit acts, here the two idempotents carry opposite eigenvalues of $e_2$, namely $\tilde\pi_+ e_2 = \tilde\pi_+$ and $\tilde\pi_- e_2 = -\tilde\pi_-$.

Left multiplication by $e_1, e_2, e_3$ acts on $\tilde\pi_+$ as

$$
e_2 \tilde\pi_+ = \tilde\pi_+, \qquad e_1 \tilde\pi_+ = \tfrac{1}{2}(e_1 + e_3), \qquad e_3 \tilde\pi_+ = \tfrac{1}{2}(e_3 + e_1) = e_1 \tilde\pi_+,
$$

so the four products $e_\mu \tilde\pi_+$ reduce to $\tilde\pi_+$ and $e_1 \tilde\pi_+$, and $\{\tilde\pi_+, e_1 \tilde\pi_+\}$ spans $\mathbb{H}_{\mathrm{s}} \tilde\pi_+$ over $\mathbb{R}$. The analogous identities for $\tilde\pi_-$ read $e_2 \tilde\pi_- = -\tilde\pi_-$ and $e_3 \tilde\pi_- = -\tfrac{1}{2}(e_1 - e_3) = -e_1 \tilde\pi_-$, so $\{\tilde\pi_-, e_1 \tilde\pi_-\}$ spans $\mathbb{H}_{\mathrm{s}} \tilde\pi_-$.

## The Classification of the Idempotents

**Theorem.** Every idempotent of $\mathbb{H}_{\mathrm{s}}$ is either trivial ($0$ or $1$) or of the form

$$
\tilde\pi = \tfrac{1}{2}(1 + \eta),
$$

where $\eta \in V$ is a root of $+1$, i.e. $\eta^2 = 1$, equivalently $N(\eta) = -1$. There are no other idempotents in $\mathbb{H}_{\mathrm{s}}$.

**Proof.** Write $\tilde\pi = q_0 + \mathbf{u}$ with $q_0 \in \mathbb{R}$ and $\mathbf{u} \in V$. Since $\mathbf{u}^2 = -N(\mathbf{u})$ for a vector,

$$
\tilde\pi^2 = q_0^2 + 2q_0\mathbf{u} + \mathbf{u}^2 = \big(q_0^2 - N(\mathbf{u})\big) + 2q_0\mathbf{u}.
$$

Equating to $\tilde\pi = q_0 + \mathbf{u}$ and separating the scalar and vector parts gives the two equations

$$
q_0^2 - N(\mathbf{u}) = q_0, \qquad 2q_0\mathbf{u} = \mathbf{u}.
$$

If $\mathbf{u} = 0$, then $q_0^2 = q_0$, so $q_0 = 0$ or $q_0 = 1$, giving the trivial idempotents. If $\mathbf{u} \neq 0$, the second equation gives $q_0 = \tfrac{1}{2}$. Substituting into the first gives $\tfrac{1}{4} - N(\mathbf{u}) = \tfrac{1}{2}$, so $N(\mathbf{u}) = -\tfrac{1}{4}$.

Define $\eta = 2\mathbf{u}$. Then $\eta \in V$, and

$$
N(\eta) = 4N(\mathbf{u}) = -1, \qquad \eta^2 = 4\mathbf{u}^2 = -4N(\mathbf{u}) = 1,
$$

where the second identity uses $\mathbf{u}^2 = -N(\mathbf{u})$ for a vector. Thus $\eta$ is a root of $+1$ in the vector subspace, and $\tilde\pi = \tfrac{1}{2} + \mathbf{u} = \tfrac{1}{2}(1 + \eta)$.

The roots of $+1$ in $V$ are the vectors of the **spacelike unit hyperboloid** $N = -1$, a one-sheeted hyperboloid of two real dimensions, as recorded in *Split-Quaternion Roots of Minus One*, §*The Roots of $+1$*. The standard idempotents correspond to $\eta = e_2$ and $\eta = -e_2$, both of which satisfy $N = -1$.

## The Bijection With the Roots of $+1$

**Theorem.** The map

$$
\eta \longmapsto \tilde\pi(\eta), \qquad \tilde\pi(\eta) = \tfrac{1}{2}(1 + \eta),
$$

is a **bijection** from the set $\{\eta \in V : \eta^2 = 1\}$ of roots of $+1$ in the vector subspace onto the set of non-scalar idempotents of $\mathbb{H}_{\mathrm{s}}$.

**Proof.** *Well defined:* if $\eta^2 = 1$, then

$$
\tilde\pi(\eta)^2 = \tfrac{1}{4}(1 + 2\eta + \eta^2) = \tfrac{1}{4}(1 + 2\eta + 1) = \tfrac{1}{2}(1 + \eta) = \tilde\pi(\eta),
$$

and $\tilde\pi(\eta)$ is non-scalar because $\eta \neq 0$. *Injective:* $\tilde\pi(\eta) = \tilde\pi(\eta')$ gives $\eta = \eta'$. *Surjective:* the classification theorem says every non-scalar idempotent is $\tfrac{1}{2}(1+\eta)$ for a root $\eta$ of $+1$ in $V$.

The **complementary pairs** $\{\tilde\pi, 1 - \tilde\pi\}$ of non-scalar idempotents are in bijection with the roots of $+1$ modulo the sign identification $\eta \sim -\eta$, since

$$
\tilde\pi(-\eta) = \tfrac{1}{2}(1 - \eta) = 1 - \tilde\pi(\eta).
$$

Thus $\tilde\pi(\eta)$ and $\tilde\pi(-\eta)$ are the two members of a complementary pair, and the pair corresponds to the class $\{\eta, -\eta\}$. The two standard idempotents $\tilde\pi_\pm$ are the pair of the class $\{\pm e_2\}$.

## Idempotents as Projections

An idempotent $\tilde\pi$ satisfies $\tilde\pi^2 = \tilde\pi$. Its **complement** $1 - \tilde\pi$ is also an idempotent, and

$$
\tilde\pi(1 - \tilde\pi) = \tilde\pi - \tilde\pi^2 = 0,
$$

so the pair $\{\tilde\pi, 1 - \tilde\pi\}$ gives a **direct sum decomposition** of the underlying real vector space:

$$
\mathbb{H}_{\mathrm{s}} = \tilde\pi\,\mathbb{H}_{\mathrm{s}} \oplus (1 - \tilde\pi)\,\mathbb{H}_{\mathrm{s}},
$$

and equally $\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi \oplus \mathbb{H}_{\mathrm{s}}(1 - \tilde\pi)$ on the other side. This is the algebraic content of the statement that idempotents correspond to projections: the idempotent is the projection, its complement is the complementary projection, and the algebra splits as a module into the image of one and the image of the other.

For the standard pair this reads

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_-, \qquad
\mathbb{H}_{\mathrm{s}} \tilde\pi_+ = \operatorname{span}\{\tilde\pi_+, e_1 \tilde\pi_+\}, \qquad
\mathbb{H}_{\mathrm{s}} \tilde\pi_- = \operatorname{span}\{\tilde\pi_-, e_1 \tilde\pi_-\},
$$

each summand of real dimension $2$. The decomposition is a decomposition of the underlying module. It is **not** an algebra decomposition: since $\tilde\pi_+$ is not central, the off-diagonal product $\tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_-$ does not vanish. Indeed

$$
\tilde\pi_+ e_3 \tilde\pi_- = \tfrac{1}{2}(e_3 - e_1) \neq 0,
$$

so an element of the first summand times an element of the second need not lie in either, and the sum is not closed as a product of subalgebras. This is the precise sense in which a non-central idempotent gives a module splitting without giving an algebra splitting; the algebra-level decomposition of a central idempotent, in which the off-diagonal corners vanish and the sum is a product of algebras, does not occur in the simple algebra $\mathbb{H}_{\mathrm{s}}$.

## Idempotents and the Zero Divisors

A nontrivial idempotent is a zero divisor, since

$$
\tilde\pi(1 - \tilde\pi) = \tilde\pi - \tilde\pi^2 = 0,
$$

and both factors are nonzero unless $\tilde\pi$ is $0$ or $1$. The direct verification is the product

$$
\tilde\pi_\pm \bar{\tilde\pi}_\pm = \tfrac{1}{4}(1 \pm e_2)(1 \mp e_2) = \tfrac{1}{4}(1 - e_2^2) = 0,
$$

and for a general non-scalar idempotent $\tilde\pi = \tfrac{1}{2}(1+\eta)$ with $\eta \in V$ and $\eta^2 = 1$,

$$
\tilde\pi \bar{\tilde\pi} = \tfrac{1}{4}(1 + \eta)(1 - \eta) = \tfrac{1}{4}(1 - \eta^2) = 0,
$$

so the whole idempotent family lies on the zero divisor set $\{\tilde q : \tilde q\bar{\tilde q} = 0\}$. The idempotents are the non-nilpotent points of that set: $\tilde\pi^2 = \tilde\pi \neq 0$, whereas the nilpotents of the algebra are exactly the nonzero vectors of $V$ whose square vanishes, treated in *Split-Quaternion Zero Divisors*, §*Nonzero Nilpotents*.

## Idempotents and the Minimal Left Ideals

**Proposition.** The left ideals

$$
\mathbb{H}_{\mathrm{s}} \tilde\pi_+ = \{\tilde q \tilde\pi_+ : \tilde q \in \mathbb{H}_{\mathrm{s}}\}, \qquad \mathbb{H}_{\mathrm{s}} \tilde\pi_- = \{\tilde q \tilde\pi_- : \tilde q \in \mathbb{H}_{\mathrm{s}}\}
$$

satisfy $\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_-$ as left $\mathbb{H}_{\mathrm{s}}$-modules, and each has real dimension $2$ and is a minimal left ideal.

**Proof.** Every $\tilde q$ satisfies $\tilde q = \tilde q(\tilde\pi_+ + \tilde\pi_-) = \tilde q \tilde\pi_+ + \tilde q \tilde\pi_-$, and the intersection of the two ideals is zero because $\tilde\pi_+ \tilde\pi_- = 0$: if $\tilde q \tilde\pi_+ = y \tilde\pi_-$ then multiplying on the right by $\tilde\pi_+$ gives $\tilde q \tilde\pi_+ = 0$. For the dimension, the reduction $e_3 \tilde\pi_+ = e_1 \tilde\pi_+$ above shows that the four products $e_\mu \tilde\pi_+$ lie in $\operatorname{span}\{\tilde\pi_+, e_1 \tilde\pi_+\}$, and the two are independent, so $\mathbb{H}_{\mathrm{s}} \tilde\pi_+$ has dimension $2$; the two summands then span $2 + 2 = 4 = \dim_{\mathbb{R}} \mathbb{H}_{\mathrm{s}}$. Minimality is the standard fact that the left ideal generated by a primitive idempotent of a ring is a minimal left ideal (*Rings*), applied to the primitive idempotent $\tilde\pi_+$.

**Proposition.** Each minimal left ideal is a two-dimensional real vector space, and the two ideals are isomorphic to one another as left $\mathbb{H}_{\mathrm{s}}$-modules.

**Proof.** Every element of $\mathbb{H}_{\mathrm{s}} \tilde\pi_+$ is uniquely $\alpha \tilde\pi_+ + \beta e_1 \tilde\pi_+$ with $\alpha, \beta \in \mathbb{R}$, so the assignment $\alpha \tilde\pi_+ + \beta e_1 \tilde\pi_+ \mapsto (\alpha, \beta)$ is a bijection onto $\mathbb{R}^2$, exhibiting the ideal as a two-dimensional real vector space. Left multiplication by $\tilde q'$ sends $\tilde q \tilde\pi_+$ to $(\tilde q' \tilde q) \tilde\pi_+$, again an element of $\mathbb{H}_{\mathrm{s}} \tilde\pi_+$, with coordinates linear in $(\alpha, \beta)$; hence it is an isomorphism of left $\mathbb{H}_{\mathrm{s}}$-modules. The same argument applies to $\tilde\pi_-$; since the algebra is simple, all its simple left modules are isomorphic, so the two ideals are isomorphic.

The two ideals here are the two minimal left ideals of the projective line of left ideals of *Split-Quaternion Ideals and Peirce Decomposition*, where the Peirce corners and the matrix units are computed. The corresponding right ideals are $\tilde\pi_+ \mathbb{H}_{\mathrm{s}}$ and $\tilde\pi_- \mathbb{H}_{\mathrm{s}}$.

## The Dimension of the Set of Idempotents

The non-scalar idempotents correspond bijectively to the roots of $+1$ in $V$, namely the level set $\{\eta \in V : \eta^2 = 1\}$, equivalently $\{N = -1\}$. That level set has real dimension $2$; the complementation $\eta \mapsto -\eta$ acts on it freely with quotient the set of **pairs** of complementary idempotents. Hence the set of non-scalar idempotents has real dimension $2$, and the set of complementary pairs has dimension $2$ as well.

The trivial idempotents $0$ and $1$ are the two isolated points of the idempotent set, and they are excluded from the non-scalar family. This is the first structural difference from the biquaternion case, where the idempotents correspond to roots of $-1$ and form a set of real dimension $4$. The reason is the opposite sign: in $\mathbb{H}_{\mathrm{s}}$ the idempotents are parametrised by the level set $\eta^2 = 1$ of the vector subspace, which is not compact, while in $\mathbb{B}$ they are parametrised by a compact set of extra parameters.

## Comparison With the Neighbouring Algebras

The contrast with the biquaternion idempotent theory is the contrast of the two signs. In the biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$, the standard idempotents

$$
\tilde\Pi_1 = \tfrac{1}{2}(e_0 + i e_3), \qquad \tilde\Pi_2 = \tfrac{1}{2}(e_0 - i e_3)
$$

are likewise non-central, but for a different reason: $\mathbb{B}$ is simple, so its only central idempotents are $0$ and $e_0$, and the nontrivial idempotents are obtained from the roots of $-1$ by $\xi \mapsto \tfrac{1}{2}(e_0 + \xi i)$ written with the central unit $i$ of $\mathbb{B}$. The biquaternion idempotents are therefore parametrised by the roots of $-1$, a set of real dimension $4$, whereas the split-quaternion idempotents are parametrised by the roots of $+1$ in $V$, a level set of real dimension $2$.

The algebra in which the idempotents are genuinely **central** is not $\mathbb{B}$ but the eight-dimensional split-biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table, whose central split-complex unit $j$ carries the idempotents $e_\pm = \tfrac{1}{2}(1 \pm j)$. Those are central, they commute with every element, and their complementary pair decomposes $\mathbb{H}_{\mathbb{D}}$ as a product of two algebras. Nothing of this kind occurs in $\mathbb{H}_{\mathrm{s}}$: its idempotents are non-central, and the companion article *Split-Quaternion Ideals and Peirce Decomposition* records that the corresponding decomposition is a module decomposition and not an algebra decomposition. The same central-idempotent phenomenon is what the commutative split-complex algebra $\mathbb{D}$ exhibits, and the split-quaternion idempotents $\tilde\pi_\pm$ are precisely the images of the idempotents of $\mathbb{D}$ inside the non-commutative algebra $\mathbb{H}_{\mathrm{s}}$, where they cease to be central.

## Summary

An idempotent of $\mathbb{H}_{\mathrm{s}}$ is an element $\tilde\pi$ with $\tilde\pi^2 = \tilde\pi$. The algebra has the standard orthogonal idempotents

$$
\tilde\pi_+ = \tfrac{1}{2}(1 + e_2), \qquad \tilde\pi_- = \tfrac{1}{2}(1 - e_2), \qquad \tilde\pi_+ \tilde\pi_- = 0, \qquad \tilde\pi_+ + \tilde\pi_- = 1,
$$

which are non-central and primitive, carrying opposite eigenvalues of $e_2$. They give the module decomposition $\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} \tilde\pi_+ \oplus \mathbb{H}_{\mathrm{s}} \tilde\pi_-$ into two minimal left ideals, each of real dimension $2$.

Every idempotent is either trivial ($0$ or $1$) or of the form $\tilde\pi = \tfrac{1}{2}(1 + \eta)$ with $\eta \in V$ and $\eta^2 = 1$, equivalently $N(\eta) = -1$; the map $\eta \mapsto \tfrac{1}{2}(1+\eta)$ is a bijection from the roots of $+1$ in the vector subspace onto the non-scalar idempotents, under which complementary pairs correspond to the classes $\{\eta, -\eta\}$. Every non-scalar idempotent is a zero divisor with $N(\tilde\pi) = 0$, and none is nilpotent. The idempotents and their complements split the underlying module as $\mathbb{H}_{\mathrm{s}} = \tilde\pi\mathbb{H}_{\mathrm{s}} \oplus (1-\tilde\pi)\mathbb{H}_{\mathrm{s}}$, but not as an algebra, because the off-diagonal Peirce corner does not vanish; $\tilde\pi_+ e_3 \tilde\pi_- = \tfrac{1}{2}(e_3 - e_1) \neq 0$. The idempotents of the algebra are exactly the idempotents of its split-complex subalgebras; in particular $\tilde\pi_\pm$ are the idempotents of the subalgebra $\mathbb{D}_2 = \operatorname{span}\{1, e_2\} \cong \mathbb{D}$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ | *Split-Quaternion Algebra* |
| $\tilde\pi$ | a general idempotent, $\tilde\pi^2 = \tilde\pi$ | this article |
| $\tilde\pi_+ = \tfrac{1}{2}(1 + e_2)$, $\tilde\pi_- = \tfrac{1}{2}(1 - e_2)$ | the standard orthogonal idempotents, $\tilde\pi_+ + \tilde\pi_- = 1$ | this article |
| $\eta$ | a root of $+1$ in $V$, $\eta^2 = 1$, $N(\eta) = -1$ | this article |
| $\tilde\pi(\eta) = \tfrac{1}{2}(1 + \eta)$ | the idempotent of the root $\eta$; $\eta \mapsto \tilde\pi(\eta)$ is a bijection | this article |
| $\mathbb{H}_{\mathrm{s}} \tilde\pi_\pm$, $\tilde\pi_\pm \mathbb{H}_{\mathrm{s}}$ | the minimal left and right ideals, each $\cong \mathbb{R}^2$ | this article |
| $\tilde\pi_+ \mathbb{H}_{\mathrm{s}} \tilde\pi_-$ | the off-diagonal Peirce corner, nonzero | this article |
| $N(\tilde q) = \tilde q\bar{\tilde q}$ | the central product, formed and evaluated algebraically; the metrical reading is in *Split-Quaternion Norm and Invertibility* | this article |
| $S = \mathbb{R}\cdot 1$, $V = \operatorname{span}\{e_1,e_2,e_3\}$ | the scalar and vector subspaces | *Split-Quaternion Algebra* |
| $\mathbb{D}_2 = \operatorname{span}\{1, e_2\}$ | the split-complex subalgebra carrying $\tilde\pi_\pm$ | *Split-Quaternion Algebra* |
| $e_\pm = \tfrac{1}{2}(1 \pm j)$ | the idempotents of the split-complex algebra $\mathbb{D}$ | *Split-Complex Algebra* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for idempotents and minimal left ideals in low-dimensional Clifford algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the Peirce decomposition and the matrix-unit model of $M_2(\mathbb{R})$.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the idempotents and zero divisors of the split composition algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition relative to a family of orthogonal idempotents.
