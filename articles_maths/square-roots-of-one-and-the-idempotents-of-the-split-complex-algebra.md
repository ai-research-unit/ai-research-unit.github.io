# __Square Roots of One and the Idempotents of the Split-Complex Algebra__

## Introduction

Of the two products of *The Two Products of the Split-Complexoid Space*, exactly one makes the underlying real space of $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=+1$, an associative unital $\mathbb{R}$-algebra; the algebra is *Split-Complex Algebra*, and its multiplication is the general plain bilinear product of two split-complex numbers, $Q_1Q_2$. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\Xi\in\mathbb{D}$ with

$$
\Xi^{2}=1 .
$$

The second is the idempotents of the algebra, the elements $\Pi$ with $\Pi^{2}=\Pi$. The two subjects are one subject, because the **halving map**

$$
\Xi\longmapsto\Pi=\tfrac12(1+\Xi),\qquad \Xi^{2}=1,
$$

is a bijection from the roots of $+1$ onto the idempotents, with inverse $\Xi=2\Pi-1$. A root carries two idempotents and not one: with $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ and $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)$, the two are a complete orthogonal pair, $\Pi_{+}(\Xi)+\Pi_{-}(\Xi)=1$ and $\Pi_{+}(\Xi)\Pi_{-}(\Xi)=0$, and the root is their difference, $\Xi=\Pi_{+}(\Xi)-\Pi_{-}(\Xi)$. The reason is a two-line computation: if $\Xi^{2}=1$ then $\Pi^{2}=\tfrac14(1+2\Xi+1)=\Pi$, and if $\Pi^{2}=\Pi$ then $(2\Pi-1)^{2}=4\Pi^{2}-4\Pi+1=1$. Every idempotent of the algebra is read through that map, on the roots of $+1$ alone, and the families of idempotents are the families of the roots of $+1$ read through it.

**The results.** The roots of $+1$ are exactly the four elements

$$
+1,\qquad -1,\qquad +j,\qquad -j .
$$

There are no others. The two central roots $\pm1$ give the trivial idempotents $1$ and $0$; the two non-central roots $\pm j$ give the standard idempotents

$$
\Pi_{\pm}=\tfrac12(1\pm j).
$$

Every idempotent of the algebra is one of the four $0,1,\Pi_{+},\Pi_{-}$; there are no positive-dimensional families, because the root equation reduces to the two real equations $\Xi_{+}^{2}=1$ and $\Xi_{-}^{2}=1$, each with two solutions, hence four roots. Each root carries the two idempotents $\Pi_{+}=\tfrac12(1+\Xi)$ and $\Pi_{-}=\tfrac12(1-\Xi)=1-\Pi_{+}$, a complete orthogonal pair whose difference is the root; the class $\{\Xi,-\Xi\}$ gives the same unordered pair. The roots of $+1$ form the four-element group $\{\pm1,\pm j\}\cong(\mathbb{Z}/2\mathbb{Z})^{2}$ under multiplication, and every root is a unit of the plain product.

The article is algebraic. It does not treat the roots of the general quadratic $\Xi^{2}=Q$, which is *Square Roots of a General Element in the Split-Complex Algebra*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Split-Complex Algebra*; or the ideals the standard idempotents generate, which are *Ideals and Peirce Decomposition of the Split-Complex Algebra*. The paragraph of §*The Roots of Minus One* records that the roots of $-1$ are empty; it is a remark, it is used nowhere, and it opens nothing.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[j]$, with basis $1,j$ and $j^{2}=+1$. A general element is $Q=q+jq'$ with $q,q'\in\mathbb{R}$, the conjugation is $\bar Q=q-jq'$, and the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, with idempotent coordinates $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ and $Q_{\pm}=q\pm q'$. The algebraic norm of the plain product is $\langle Q\rangle=Q^{2}$ (*Norm and Invertibility in the Split-Complex Algebra*), and the algebraic norm of the sesquilinear product is $\langle Q\rangle_{*}=Q\bar Q=q^{2}-q'^{2}$ (*Norm and Invertibility in the General Split-Complex Algebra*). A root of a central value is written $\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\Pi$ (§*The Idempotent Convention*), the two members of a complete pair with the two signs, $\Pi_{+}$ and $\Pi_{-}$, the subscript $+$ naming the member attached to $+1$, and a generic element $Q$.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*, and the general definition of an idempotent, with the orthogonal, complete and primitive families, the Hermitian idempotent and the Peirce decomposition, is the same article. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other product of the space carries roots and idempotents of its own, and they are *Relations and Comparison Between the Two Products of the Split-Complexoid Space*.

## The Roots of One

**The roots of $+1$ are exactly $\pm1$ and $\pm j$; there are no others.**

A **root of $+1$** is an element $\Xi\in\mathbb{D}$ with $\Xi^{2}=1$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in the idempotent coordinates,

$$
\Xi=\Xi_{+}\Pi_{+}+\Xi_{-}\Pi_{-},\qquad \Xi_{\pm}=x\pm x',
$$

with $x,x'\in\mathbb{R}$. Because the product is componentwise in the idempotent basis and $\Pi_{\pm}^{2}=\Pi_{\pm}$, $\Pi_{+}\Pi_{-}=0$, the square is

$$
\Xi^{2}=\Xi_{+}^{2}\Pi_{+}+\Xi_{-}^{2}\Pi_{-}.
$$

The equation $\Xi^{2}=1=\Pi_{+}+\Pi_{-}$ is therefore equivalent to the **pair of real equations**

$$
\Xi_{+}^{2}=1,\qquad \Xi_{-}^{2}=1.
$$

There is no coupling between the two coordinates: the root problem splits into two independent one-dimensional root problems, each with the two solutions $\pm1$. The four combinations are the four roots.

**Remark (the scalar form).** In the basis $1,j$ the same equations read

$$
x^{2}+x'^{2}=1,\qquad 2xx'=0,
$$

because $\Xi^{2}=(x^{2}+x'^{2})+2xx'j$. The second equation forces $x=0$ or $x'=0$; the first then gives $x=\pm1$ with $x'=0$, or $x=0$ with $x'=\pm1$. The four solutions are $\pm1$ and $\pm j$.

### The Trivial Roots

The two **central roots** are

$$
\Xi=+1,\qquad \Xi=-1 .
$$

They are the roots in the real line $\mathbb{R}_{\mathbb{D}}$, and they are the only roots fixed by the conjugation, $\bar\Xi=\Xi$. They give the trivial idempotents $1$ and $0$ under the halving map.

### The Non-Trivial Roots

The two **non-central roots** are

$$
\Xi=+j,\qquad \Xi=-j .
$$

They are the roots in the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, and the conjugation exchanges them, $\overline{+j}=-j$. They give the standard idempotents $\Pi_{+}$ and $\Pi_{-}$ under the halving map.

### Statement of the Theorem

**Theorem (the roots of $+1$).** The roots of $+1$ in $\mathbb{D}$ are exactly the four elements

$$
1,\qquad -1,\qquad j,\qquad -j .
$$

**Proof.** The reduction gives $\Xi_{+}^{2}=1$ and $\Xi_{-}^{2}=1$, hence $\Xi_{+}\in\{+1,-1\}$ and $\Xi_{-}\in\{+1,-1\}$. The four combinations are

$$
\Xi=1\Pi_{+}+1\Pi_{-}=1,\qquad
\Xi=1\Pi_{+}-1\Pi_{-}=j,\qquad
\Xi=-1\Pi_{+}+1\Pi_{-}=-j,\qquad
\Xi=-1\Pi_{+}-1\Pi_{-}=-1,
$$

where the second and third use $2\Pi_{+}-1=j$ and $2\Pi_{-}-1=-j$. There are no others, because the reduction is an equivalence.

### Verification

The four roots are checked by squaring:

$$
1^{2}=1,\qquad (-1)^{2}=1,\qquad j^{2}=+1,\qquad (-j)^{2}=j^{2}=+1.
$$

The verification is the whole computation: the split sign $j^{2}=+1$ is what makes $j$ a root of $+1$ and not a root of $-1$.

### The Roots of Minus One

**Proposition (the roots of $-1$).** The equation $\Xi^{2}=-1$ has **no solution** in $\mathbb{D}$.

**Proof.** In the idempotent coordinates the equation is $\Xi_{+}^{2}=-1$ and $\Xi_{-}^{2}=-1$, impossible over $\mathbb{R}$; in the scalar coordinates it is $x^{2}+x'^{2}=-1$ and $2xx'=0$, and the first equation is impossible because the left side is non-negative.

The absence is the sharp difference from the complex field: the complex unit $i$ is a root of $-1$, while the split unit $j$ is a root of $+1$. There is no central imaginary in $\mathbb{D}$ and no multiplication of the roots of $+1$ by one that would produce roots of $-1$; the two root problems have different solution sets, one of four elements and one empty.

### Status of the Roots

**Proposition (the roots form a group).** The set

$$
\mathcal{R}_{+1}=\{1,-1,j,-j\}
$$

is a subgroup of the group of units of the plain product, isomorphic to $(\mathbb{Z}/2\mathbb{Z})^{2}$.

**Proof.** The product of two roots is a root, because $(\Xi B)^{2}=\Xi^{2}B^{2}=1$; the unit is $1$; and each element is its own inverse, $\Xi^{2}=1$. The group is abelian of order four with every non-identity element of order two, hence $(\mathbb{Z}/2\mathbb{Z})^{2}$.

**Proposition (the norms of the roots).** The algebraic norm of the sesquilinear product takes the values

$$
\langle\pm1\rangle_{*}=1,\qquad \langle\pm j\rangle_{*}=-1,
$$

so the central roots are timelike units and the non-central roots are spacelike units.

**Proof.** $\langle q+jq'\rangle_{*}=q^{2}-q'^{2}$; at $\pm1$ the pair is $(\pm1,0)$ and at $\pm j$ it is $(0,\pm1)$.

No root of $+1$ is a zero divisor, because every root is a unit; the central roots $\pm1$ lie on the real axis, on the unit hyperbola $\langle Q\rangle_{*}=1$, and the non-central roots $\pm j$ lie on the split imaginary axis, on the hyperbola $\langle Q\rangle_{*}=-1$; none lies on the null cone. The shell of the plain algebraic norm at $1$ is exactly this four-element set (*Norm and Invertibility in the Split-Complex Algebra*).

## The Idempotents

**The idempotents of $\mathbb{D}$ are exactly the four elements $0,1,\Pi_{+},\Pi_{-}$; the standard pair is orthogonal, complete, central and primitive, and every idempotent is the image of exactly one root of $+1$ under the halving map.**

### The Definition

Let $\mathbb{D}$ be the split-complex algebra. An element $\Pi\in\mathbb{D}$ is an **idempotent** when

$$
\Pi^{2}=\Pi .
$$

Two idempotents $\Pi,\Pi'$ are **orthogonal** when $\Pi\Pi'=\Pi'\Pi=0$; a family is **pairwise orthogonal** when its members are pairwise orthogonal, and **complete** when in addition their sum is $1$. A nonzero idempotent is **primitive** when it is not the sum of two nonzero orthogonal idempotents. The definitions are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Idempotent, the Hermitian Idempotent and the Peirce Decomposition*, read on this two-dimensional member of the family.

### The Two Idempotents of a Root

**Theorem (the halving map).** The map

$$
\Xi\longmapsto\Pi=\tfrac12(1+\Xi)
$$

is a bijection from the roots of $+1$ onto the idempotents of $\mathbb{D}$, with inverse

$$
\Pi\longmapsto\Xi=2\Pi-1 .
$$

**Proof.** If $\Xi^{2}=1$ then

$$
\Pi^{2}=\tfrac14(1+2\Xi+\Xi^{2})=\tfrac14(2+2\Xi)=\tfrac12(1+\Xi)=\Pi .
$$

Conversely, if $\Pi^{2}=\Pi$ then

$$
(2\Pi-1)^{2}=4\Pi^{2}-4\Pi+1=1 .
$$

The two maps are inverse to each other: $\tfrac12(1+(2\Pi-1))=\Pi$ and $2\cdot\tfrac12(1+\Xi)-1=\Xi$.

**Theorem (the two idempotents of a root).** Every root $\Xi$ of $+1$ carries the two idempotents

$$
\Pi_{+}(\Xi)=\tfrac12(1+\Xi),\qquad \Pi_{-}(\Xi)=\tfrac12(1-\Xi),
$$

and they satisfy

$$
\Pi_{+}^{2}=\Pi_{+},\qquad \Pi_{-}^{2}=\Pi_{-},\qquad \Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}+\Pi_{-}=1,\qquad \Xi=\Pi_{+}-\Pi_{-}.
$$

**Proof.** The first two identities are the halving computation applied to $\Xi$ and to $-\Xi$, which is also a root. The product is

$$
\Pi_{+}\Pi_{-}=\tfrac14(1+\Xi)(1-\Xi)=\tfrac14(1-\Xi^{2})=0,
$$

and the sum is $\tfrac12(1+\Xi)+\tfrac12(1-\Xi)=1$. The difference is $\tfrac12(1+\Xi)-\tfrac12(1-\Xi)=\Xi$.

**Corollary (the four roots and the four pairs).** The four roots give the four ordered complete orthogonal pairs

$$
1\longmapsto(1,0),\qquad -1\longmapsto(0,1),\qquad j\longmapsto(\Pi_{+},\Pi_{-}),\qquad -j\longmapsto(\Pi_{-},\Pi_{+}),
$$

and the map from roots to ordered pairs is bijective. The two roots $\Xi$ and $-\Xi$ give the same **unordered** pair, so the four roots give the two unordered pairs $\{1,0\}$ and $\{\Pi_{+},\Pi_{-}\}$.

### The Arithmetic of the Pair

For a root $\Xi$ and the two idempotents $\Pi_{\pm}=\tfrac12(1\pm\Xi)$, the root acts on the pair by the two signs:

$$
\Xi\Pi_{+}=\Pi_{+},\qquad \Xi\Pi_{-}=-\Pi_{-}.
$$

**Proof.** $\Xi\Pi_{+}=\tfrac12(\Xi+\Xi^{2})=\tfrac12(\Xi+1)=\Pi_{+}$ and $\Xi\Pi_{-}=\tfrac12(\Xi-\Xi^{2})=\tfrac12(\Xi-1)=-\Pi_{-}$.

So the root is $+1$ on the first idempotent and $-1$ on the second, and the algebra decomposes under multiplication by $\Xi$ into the two eigenspaces $\mathbb{R}\Pi_{+}$ and $\mathbb{R}\Pi_{-}$ with eigenvalues $+1$ and $-1$. The pair $\Pi_{\pm}$ is the spectral resolution of the root.

### The Standard Idempotents

The two **standard idempotents** are

$$
\Pi_{+}=\frac{1+j}{2},\qquad \Pi_{-}=\frac{1-j}{2}.
$$

They are the idempotents attached to the root $j$: $\Pi_{+}=\Pi_{+}(j)$ and $\Pi_{-}=\Pi_{-}(j)$. Since $j^{2}=+1$,

$$
\Pi_{+}^{2}=\frac{1+2j+j^{2}}{4}=\frac{2+2j}{4}=\Pi_{+},\qquad
\Pi_{-}^{2}=\Pi_{-},
$$

and

$$
\Pi_{+}\Pi_{-}=\frac{(1+j)(1-j)}{4}=\frac{1-j^{2}}{4}=0,\qquad
\Pi_{+}+\Pi_{-}=1.
$$

They are **central**, because the algebra is commutative, and **primitive**, because

$$
\Pi_{+}\mathbb{D}\Pi_{+}=\mathbb{R}\Pi_{+}\cong\mathbb{R},\qquad
\Pi_{-}\mathbb{D}\Pi_{-}=\mathbb{R}\Pi_{-}\cong\mathbb{R}
$$

are fields.

### The Classification of the Idempotents

**Theorem (the idempotents).** The idempotents of $\mathbb{D}$ are exactly

$$
0,\qquad 1,\qquad \Pi_{+}=\frac{1+j}{2},\qquad \Pi_{-}=\frac{1-j}{2}.
$$

**Proof.** Write $Q=q+jq'$ and impose $Q^{2}=Q$. Since

$$
Q^{2}=(q^{2}+q'^{2})+2qq'j,
$$

the equation is equivalent to

$$
q^{2}+q'^{2}=q,\qquad 2qq'=q'.
$$

The second factors as $q'(2q-1)=0$. If $q'=0$ the first gives $q^{2}=q$, hence $q=0$ or $q=1$: the idempotents $0$ and $1$. If $q'\neq0$ then $q=\tfrac12$, and the first gives $\tfrac14+q'^{2}=\tfrac12$, hence $q'^{2}=\tfrac14$ and $q'=\pm\tfrac12$: the idempotents $\Pi_{+}$ and $\Pi_{-}$. There are no others.

### The Correspondence with the Roots of One

The halving map is a bijection, so the idempotent classification and the root classification are the same classification read through it. The four roots and the four idempotents correspond as follows.

| root $\Xi$ | $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ | $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)$ | unordered pair |
|---|---|---|---|
| $1$ | $1$ | $0$ | $\{1,0\}$ |
| $-1$ | $0$ | $1$ | $\{1,0\}$ |
| $j$ | $\Pi_{+}$ | $\Pi_{-}$ | $\{\Pi_{+},\Pi_{-}\}$ |
| $-j$ | $\Pi_{-}$ | $\Pi_{+}$ | $\{\Pi_{+},\Pi_{-}\}$ |

The first column is a bijection onto the idempotents; the last column is two-to-one. The root is recovered from the ordered pair as the difference of its members, and the unordered pair loses the sign of the root and nothing else.

### The Families of Idempotents

The idempotents form a **finite set of four elements**, not a positive-dimensional family. The reason is visible in the classification: the idempotent equation forces $q'=0$ or $q'^{2}=\tfrac14$, a finite set of values for the second coordinate, because the base field is $\mathbb{R}$ and there is no vector part to vary independently. In the four-dimensional biquaternion algebra the corresponding equation has a four-real-parameter family; here the family collapses to four points. The idempotents are the indicator functions of the subsets of a two-point set under $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$:

$$
0\longmapsto(0,0),\qquad \Pi_{+}\longmapsto(1,0),\qquad \Pi_{-}\longmapsto(0,1),\qquad 1\longmapsto(1,1).
$$

The four are the empty set, the two singletons and the whole set; the power set of $\{+,-\}$ has $2^{2}=4$ elements.

### Idempotents and Their Projectors

An idempotent $\Pi$ acts by multiplication as a **projector**: $\Pi^{2}=\Pi$, so $L_\Pi$ is the identity on its image and annihilates its kernel. Its complement $1-\Pi$ is also an idempotent, and $\Pi(1-\Pi)=0$, so the pair gives the direct-sum decomposition

$$
\mathbb{D}=\mathbb{D}\Pi\oplus\mathbb{D}(1-\Pi),
$$

the same on the left and on the right because the algebra is commutative.

For the standard pair the projections are the projections onto the two idempotent lines,

$$
P_{+}:Q\longmapsto Q\Pi_{+}=Q_{+}\Pi_{+},\qquad
P_{-}:Q\longmapsto Q\Pi_{-}=Q_{-}\Pi_{-},
$$

with

$$
P_{+}^{2}=P_{+},\qquad P_{-}^{2}=P_{-},\qquad P_{+}P_{-}=P_{-}P_{+}=0,\qquad P_{+}+P_{-}=\mathrm{id}.
$$

In the basis $1,j$ the matrices are

$$
P_{+}=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
P_{-}=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
$$

the two complementary rank-one projectors of the plane. A projector in the split-complex algebra is an idempotent operator, and $P_{\pm}$ select the two coordinates of the isomorphism with $\mathbb{R}\oplus\mathbb{R}$.

### Idempotents and the Zero Divisors

A nontrivial idempotent is a zero divisor, since

$$
\Pi_{+}(1-\Pi_{+})=\Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}\neq0,\qquad 1-\Pi_{+}=\Pi_{-}\neq0,
$$

and symmetrically for $\Pi_{-}$. Conversely, every zero divisor is a nonzero real multiple of one of the two idempotents:

$$
\mathcal{Z}=\mathbb{R}^{\times}\Pi_{+}\cup\mathbb{R}^{\times}\Pi_{-}.
$$

That statement, with its proof and the structure of the zero-divisor set, is *Zero Divisors of the Split-Complex Algebra*; the present article records only that the nontrivial idempotents are the primitive zero divisors.

### Idempotents and the Minimal Ideals

The principal ideals

$$
\mathbb{D}\Pi_{+}=\mathbb{R}\Pi_{+},\qquad \mathbb{D}\Pi_{-}=\mathbb{R}\Pi_{-}
$$

are the two nontrivial minimal ideals, and

$$
\mathbb{D}=\mathbb{D}\Pi_{+}\oplus\mathbb{D}\Pi_{-}
$$

is the direct sum of the two copies of $\mathbb{R}$. The minimality is proved in *Ideals and Peirce Decomposition of the Split-Complex Algebra*, where the idempotents, the Peirce decomposition and the failure of simplicity are developed together.

## Summary

The roots of $+1$ in the split-complex algebra are exactly the four elements $1,-1,j,-j$; there are no others and there are no roots of $-1$. The roots form the group $(\mathbb{Z}/2\mathbb{Z})^{2}$, and the two central roots are timelike units while the two non-central roots are spacelike units.

The idempotents are exactly $0,1,\Pi_{+}=\tfrac12(1+j),\Pi_{-}=\tfrac12(1-j)$. The halving map $\Xi\mapsto\tfrac12(1+\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $\Pi\mapsto2\Pi-1$; each root carries the complete orthogonal pair $\Pi_{\pm}(\Xi)=\tfrac12(1\pm\Xi)$, whose difference is the root, and the class $\{\Xi,-\Xi\}$ gives the same unordered pair. The standard pair is central, primitive and complete, and it carries the direct-sum decomposition $\mathbb{D}=\mathbb{R}\Pi_{+}\oplus\mathbb{R}\Pi_{-}\cong\mathbb{R}\oplus\mathbb{R}$ and the two complementary projectors $P_{\pm}$. The nontrivial idempotents are the primitive zero divisors, and every zero divisor is a nonzero real multiple of one of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $\Xi$ | A root of $+1$ |
| $\Pi$ | An idempotent |
| $\mathcal{R}_{+1}=\{1,-1,j,-j\}$ | The four roots of $+1$ |
| $\Pi_{\pm}(\Xi)=\tfrac12(1\pm\Xi)$ | The two idempotents carried by the root $\Xi$ |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The standard idempotents |
| $\Pi_{+}+\Pi_{-}=1$, $\Pi_{+}\Pi_{-}=0$ | Completeness and orthogonality |
| $\Xi=\Pi_{+}-\Pi_{-}$ | The root as the difference of its pair |
| $P_{\pm}:Q\mapsto Q_{\pm}=q\pm q'$ | The two complementary projections |
| $\mathbb{D}\Pi_{\pm}=\mathbb{R}\Pi_{\pm}$ | The two minimal ideals |

## Further Reading

- [Split-Complex Algebra](split-complex-algebra.html), for the product, its unit and the element theory of the algebra.
- [Square Roots of Zero and the Nilpotents of the Split-Complex Algebra](square-roots-of-zero-and-the-nilpotents-of-the-split-complex-algebra.html), for the companion central value $0$ and the absence of nonzero nilpotents.
- [Square Roots of a General Element in the Split-Complex Algebra](square-roots-of-a-general-element-in-the-split-complex-algebra.html), for the roots of $\Xi^{2}=Q$.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the zero divisors as the nonzero real multiples of the two idempotents.
- [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), for the two minimal ideals and the Peirce decomposition.
- [Norm and Invertibility in the Split-Complex Algebra](norm-and-invertibility-in-the-split-complex-algebra.html), for the shell of the plain algebraic norm at $1$.
