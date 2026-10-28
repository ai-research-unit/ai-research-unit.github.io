# __Square Roots of One and the Idempotents of the Split-Complex Algebra__

## Introduction

Of the two products of *The Two Products of the Split-Complexoid Space*, exactly one makes the underlying real space of $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=+1$, an associative unital $\mathbb{R}$-algebra; the algebra is *Split-Complex Algebra*, and its multiplication is the general plain bilinear product of two split-complex numbers, $Q_1Q_2$. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\Xi\in\mathbb{D}$ with

$$
\Xi^{2}=1 .
$$

The second is the idempotents of the algebra, the elements $\Pi$ with $\Pi^{2}=\Pi$. The two subjects are one subject, because the **halving map**

$$
H(\Xi)=\tfrac12(1+\Xi),\qquad \Xi^{2}=1,
$$

is a bijection from the roots of $+1$ onto the idempotents, with inverse $H^{-1}(\Pi)=2\Pi-1$. A root carries two idempotents and not one: the halving map picks the member attached to $+1$, and the other is its value at $-\Xi$; with $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ and $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)=\Pi_{+}(-\Xi)$, the two are a complete orthogonal pair, $\Pi_{+}(\Xi)+\Pi_{-}(\Xi)=1$ and $\Pi_{+}(\Xi)\Pi_{-}(\Xi)=0$, and the root is their difference, $\Xi=\Pi_{+}(\Xi)-\Pi_{-}(\Xi)$. The reason is a two-line computation: if $\Xi^{2}=1$ then $\Pi^{2}=\tfrac14(1+2\Xi+1)=\Pi$, and if $\Pi^{2}=\Pi$ then $(2\Pi-1)^{2}=4\Pi^{2}-4\Pi+1=1$. Every idempotent of the algebra is read through that map, on the roots of $+1$ alone, and the families of idempotents are the families of the roots of $+1$ read through it.

**The results.** The roots of $+1$ are exactly the four elements

$$
1,\qquad -1,\qquad j,\qquad -j .
$$

There are no others. The two **trivial roots** $\pm1$ give the trivial idempotents $1$ and $0$; the two **non-trivial roots** $\pm j$ give the standard idempotents

$$
\Pi_{\pm}=\tfrac12(1\pm j).
$$

The trivial idempotents are Hermitian, fixed by the conjugation; the standard idempotents are non-Hermitian, exchanged by it. Every idempotent of the algebra is one of the four $0,1,\Pi_{+},\Pi_{-}$; there are no positive-dimensional families, because the root equation reduces to the two real equations $\Xi_{+}^{2}=1$ and $\Xi_{-}^{2}=1$, each with two solutions, hence four roots. Each root carries the two idempotents $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ and $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)=1-\Pi_{+}(\Xi)$, a complete orthogonal pair whose difference is the root; the class $\{\Xi,-\Xi\}$ gives the same unordered pair. The roots of $+1$ form the four-element group $\{\pm1,\pm j\}\cong(\mathbb{Z}/2\mathbb{Z})^{2}$ under multiplication, and every root is a unit of the plain product.

The following table collects the results at a glance.

| Item | Result | Size |
|---|---|---|
| Roots of $+1$ | $1,-1,j,-j$ | four elements |
| Roots of $-1$ | none | empty |
| Root set | group $(\mathbb{Z}/2\mathbb{Z})^{2}$ | four elements |
| Idempotents | $0,1,\Pi_{+},\Pi_{-}$ | four elements |
| Hermitian idempotents | $0,1$, the conjugation fixing them | two elements |
| Non-Hermitian idempotents | $\Pi_{+},\Pi_{-}$, the conjugation exchanging them | two elements |
| Halving map | bijection $H(\Xi)=\tfrac12(1+\Xi)$ | two-to-one on unordered pairs |
| Standard pair | $\Pi_{\pm}=\tfrac12(1\pm j)$, central, primitive, complete and orthogonal | two elements |
| Zero divisors | the non-trivial idempotents and their nonzero real multiples | two lines |
| Involutions | the conjugation exchanges $\Pi_{+}$ and $\Pi_{-}$ | one involution |

The article is algebraic. It does not treat the roots of the general quadratic $\Xi^{2}=Q$, which is *Square Roots of a General Element in the Split-Complex Algebra*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Split-Complex Algebra*; or the ideals the standard idempotents generate, which are *Ideals and Peirce Decomposition of the Split-Complex Algebra*. The subsection §*The Roots of Minus One* records that the roots of $-1$ are empty; it is a remark, it is used nowhere, and it opens nothing.

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

The two equations are collected in the table.

| Case | Equation | Solutions |
|---|---|---|
| $\Xi_{+}$ | $\Xi_{+}^{2}=1$ | $\Xi_{+}=+1$ or $\Xi_{+}=-1$ |
| $\Xi_{-}$ | $\Xi_{-}^{2}=1$ | $\Xi_{-}=+1$ or $\Xi_{-}=-1$ |

There is no coupling between the two coordinates: the root problem splits into two independent one-dimensional root problems, each with the two solutions $\pm1$. The four combinations are the four roots.

**Remark (the scalar form).** In the basis $1,j$ the same equations read

$$
x^{2}+x'^{2}=1,\qquad 2xx'=0,
$$

because $\Xi^{2}=(x^{2}+x'^{2})+2xx'j$. The second equation forces $x=0$ or $x'=0$; the first then gives $x=\pm1$ with $x'=0$, or $x=0$ with $x'=\pm1$. The four solutions are $\pm1$ and $\pm j$.

### The Trivial Roots

The two **trivial roots** are

$$
\Xi=+1,\qquad \Xi=-1 .
$$

They are the roots in the real line $\mathbb{R}_{\mathbb{D}}$, and they are the only roots fixed by the conjugation, $\bar\Xi=\Xi$. They give the trivial idempotents $1$ and $0$ under the halving map.

### The Non-Trivial Roots

The two **non-trivial roots** are

$$
\Xi=+j,\qquad \Xi=-j .
$$

They are the imaginary roots, in the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, and the conjugation exchanges them, $\overline{+j}=-j$; they are therefore non-Hermitian for the conjugation. They give the standard idempotents $\Pi_{+}$ and $\Pi_{-}$ under the halving map.

### Statement of the Theorem

**Theorem (the roots of $+1$).** The roots of $+1$ in $\mathbb{D}$ are exactly the four elements

$$
\boxed{\;1,\qquad -1,\qquad j,\qquad -j\;}.
$$

**Proof.** The reduction gives $\Xi_{+}^{2}=1$ and $\Xi_{-}^{2}=1$, hence $\Xi_{+}\in\{+1,-1\}$ and $\Xi_{-}\in\{+1,-1\}$. The four combinations are

$$
\Xi=1\Pi_{+}+1\Pi_{-}=1,\qquad
\Xi=1\Pi_{+}-1\Pi_{-}=j,\qquad
\Xi=-1\Pi_{+}+1\Pi_{-}=-j,\qquad
\Xi=-1\Pi_{+}-1\Pi_{-}=-1,
$$

where the second and third use $2\Pi_{+}-1=j$ and $2\Pi_{-}-1=-j$. There are no others, because the reduction is an equivalence.

The roots fall into the two following families.

| Family | Form | Real parameters | Size | Position | Fixed by the conjugation? |
|---|---|---|---|---|---|
| Trivial roots | $\Xi=\pm1$ | none | two elements | the real line $\mathbb{R}_{\mathbb{D}}$ | yes |
| Non-trivial roots | $\Xi=\pm j$ | none | two elements | the split imaginary line $j\mathbb{R}_{\mathbb{D}}$ | no |

### Verification

The four roots are checked by squaring.

| Family | Square | Value |
|---|---|---|
| Trivial roots | $(\pm1)^{2}$ | $1$ |
| Non-trivial roots | $(\pm j)^{2}$ | $1$ |

The verification is the whole computation: the split sign $j^{2}=+1$ is what makes $j$ a root of $+1$ and not a root of $-1$.

### The Roots of Minus One

**Proposition (the roots of $-1$).** The equation $\Xi^{2}=-1$ has **no solution** in $\mathbb{D}$.

**Proof.** In the idempotent coordinates the equation is $\Xi_{+}^{2}=-1$ and $\Xi_{-}^{2}=-1$, impossible over $\mathbb{R}$; in the scalar coordinates it is $x^{2}+x'^{2}=-1$ and $2xx'=0$, and the first equation is impossible because the left side is non-negative.

The result is collected in the table.

| Equation | Solutions | Size | Relation to the roots of $+1$ |
|---|---|---|---|
| $\Xi^{2}=-1$ | none | empty | no root of $+1$ produces one; the complex unit $i$ is absent |

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
\boxed{\;\langle\pm1\rangle_{*}=1,\qquad \langle\pm j\rangle_{*}=-1\;},
$$

so the real roots are timelike units and the imaginary roots are spacelike units.

**Proof.** $\langle q+jq'\rangle_{*}=q^{2}-q'^{2}$; at $\pm1$ the pair is $(\pm1,0)$ and at $\pm j$ it is $(0,\pm1)$.

The status of the roots is collected in the table.

| Property | Result |
|---|---|
| Closed under multiplication? | yes, the product of two roots is a root |
| Group? | yes, $(\mathbb{Z}/2\mathbb{Z})^{2}$ |
| Units? | yes, $\Xi^{-1}=\Xi$ |
| Zero divisors? | no |
| Norm | $\langle\pm1\rangle_{*}=1$, $\langle\pm j\rangle_{*}=-1$ |
| Position | the real roots on the real line, the imaginary roots on the split imaginary line |

No root of $+1$ is a zero divisor, because every root is a unit; the real roots $\pm1$ lie on the real axis, on the unit hyperbola $\langle Q\rangle_{*}=1$, and the imaginary roots $\pm j$ lie on the split imaginary axis, on the hyperbola $\langle Q\rangle_{*}=-1$; none lies on the null cone. The shell of the plain algebraic norm at $1$ is exactly this four-element set (*Norm and Invertibility in the Split-Complex Algebra*).

## The Idempotents

**The idempotents of $\mathbb{D}$ are exactly the four elements $0,1,\Pi_{+},\Pi_{-}$; the standard pair is orthogonal, complete, central and primitive, and every idempotent is the image of exactly one root of $+1$ under the halving map.**

The **idempotents** of $\mathbb{D}$ are the elements satisfying $\Pi^{2}=\Pi$, the square being the one of the plain product. They correspond to projectors under multiplication, and in $\mathbb{D}$ they do four separate jobs at once: they give the direct sum decompositions of the algebra into the two idempotent lines, and in particular the two minimal ideals; they classify the zero divisors, every nonzero one of which is a real multiple of an idempotent; they are in bijection with the roots of $+1$ through the halving map, each root carrying a complete orthogonal pair, so their classification is the classification of those roots; and they carry the Peirce decomposition of the algebra. The definition and the families are the general ones of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, read on this two-dimensional member of the family.

### The Definition

**Definition.** Let $\mathbb{D}$ be the split-complex algebra. An element $\Pi\in\mathbb{D}$ is an **idempotent of the split-complex algebra** when

$$
\Pi^{2}=\Pi .
$$

The element $0$ is an idempotent, and so is the unit $1$; the two are the **trivial idempotents**. The equation names a product, and the notion is relative to it: throughout this article the product is the general plain bilinear product, the multiplication of the algebra.

Two idempotents $\Pi,\Pi'$ are **orthogonal** when $\Pi\Pi'=\Pi'\Pi=0$; a family is **pairwise orthogonal** when its members are pairwise orthogonal, and **complete** when in addition their sum is $1$. A nonzero idempotent is **primitive** when it is not the sum of two nonzero orthogonal idempotents. The definitions are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Idempotent, the Hermitian Idempotent and the Peirce Decomposition*, read on this two-dimensional member of the family.

### The Two Idempotents of a Root

**A root $\Xi$ of $+1$ carries the two idempotents $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ and $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)=1-\Pi_{+}(\Xi)$; they are complete and orthogonal, and their difference is the root.**

**Theorem (the two idempotents of a root).** Every root $\Xi$ of $+1$ carries the two idempotents

$$
\Pi_{+}(\Xi)=\tfrac12(1+\Xi),\qquad \Pi_{-}(\Xi)=\tfrac12(1-\Xi),
$$

and they satisfy the identities of the table.

| Identity | Value |
|---|---|
| $\Pi_{+}^{2}$ | $\Pi_{+}$ |
| $\Pi_{-}^{2}$ | $\Pi_{-}$ |
| $\Pi_{+}\Pi_{-}$ | $0$ |
| $\Pi_{+}+\Pi_{-}$ | $1$ |
| $\Pi_{+}-\Pi_{-}$ | $\Xi$ |

**Proof.** The first two identities are the halving computation applied to $\Xi$ and to $-\Xi$, which is also a root. The product is

$$
\Pi_{+}\Pi_{-}=\tfrac14(1+\Xi)(1-\Xi)=\tfrac14(1-\Xi^{2})=0,
$$

and the sum is $\tfrac12(1+\Xi)+\tfrac12(1-\Xi)=1$. The difference is $\tfrac12(1+\Xi)-\tfrac12(1-\Xi)=\Xi$.

### The Arithmetic of the Pair

**The pair of a root is complete and orthogonal, its difference is the root, and multiplication by the root acts by $+1$ on $\Pi_{+}$ and $-1$ on $\Pi_{-}$.**

The four products of the pair are collected in the multiplication table.

| $\cdot$ | $\Pi_{+}$ | $\Pi_{-}$ |
|---|---|---|
| $\Pi_{+}$ | $\Pi_{+}$ | $0$ |
| $\Pi_{-}$ | $0$ | $\Pi_{-}$ |

so the pair is orthogonal and each member is idempotent.

For a root $\Xi$ and the two idempotents $\Pi_{\pm}=\tfrac12(1\pm\Xi)$, the root acts on the pair by the two signs:

$$
\Xi\Pi_{+}=\Pi_{+},\qquad \Xi\Pi_{-}=-\Pi_{-}.
$$

**Proof.** $\Xi\Pi_{+}=\tfrac12(\Xi+\Xi^{2})=\tfrac12(\Xi+1)=\Pi_{+}$ and $\Xi\Pi_{-}=\tfrac12(\Xi-\Xi^{2})=\tfrac12(\Xi-1)=-\Pi_{-}$.

The action is collected in the table.

| Multiplication by $\Xi$ | On $\Pi_{+}$ | On $\Pi_{-}$ |
|---|---|---|
| left or right | $+1$ | $-1$ |

So the root is $+1$ on the first idempotent and $-1$ on the second, and the algebra decomposes under multiplication by $\Xi$ into the two eigenspaces $\mathbb{R}\Pi_{+}$ and $\mathbb{R}\Pi_{-}$ with eigenvalues $+1$ and $-1$. The pair $\Pi_{\pm}$ is the spectral resolution of the root.

### The Standard Idempotents

**The algebra carries the standard idempotents $\Pi_{+}=\tfrac12(1+j)$ and $\Pi_{-}=\tfrac12(1-j)$, the two idempotents of the root $j$, with $\Pi_{+}\Pi_{-}=0$ and $\Pi_{+}+\Pi_{-}=1$; each is central and primitive.**

Put

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

are fields. The properties of the pair are collected in the table.

| Property | $\Pi_{+},\Pi_{-}$ |
|---|---|
| Orthogonal | $\Pi_{+}\Pi_{-}=0$ |
| Complete | $\Pi_{+}+\Pi_{-}=1$ |
| Central | yes, the algebra is commutative |
| Primitive | yes, $\Pi_{\pm}\mathbb{D}\Pi_{\pm}=\mathbb{R}\Pi_{\pm}$ |
| Hermitian idempotent | no, $\overline{\Pi_{+}}=\Pi_{-}$ and $\overline{\Pi_{-}}=\Pi_{+}$ |
| Zero divisor | yes, $\Pi_{+}\Pi_{-}=0$ |
| Minimal ideals | $\mathbb{D}\Pi_{\pm}=\mathbb{R}\Pi_{\pm}$ |

### The Classification of the Idempotents

**The idempotents of $\mathbb{D}$ are exactly $0$, $1$, $\Pi_{+}$ and $\Pi_{-}$; there are no others.**

**Theorem (the idempotents).** The idempotents of $\mathbb{D}$ are exactly

$$
\boxed{\;0,\qquad 1,\qquad \Pi_{+}=\frac{1+j}{2},\qquad \Pi_{-}=\frac{1-j}{2}\;}.
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

**The halving map $H(\Xi)=\tfrac12(1+\Xi)$ is a bijection from the roots of $+1$ onto the idempotents; the pair map $\Xi\mapsto(\Pi_{+}(\Xi),\Pi_{-}(\Xi))$ is a bijection from the roots of $+1$ onto the ordered complete orthogonal pairs of idempotents; and the class $\{\Xi,-\Xi\}$ gives the same unordered pair.**

**Theorem (the halving map).** The map

$$
H(\Xi)=\tfrac12(1+\Xi)
$$

is a bijection from the roots of $+1$ onto the idempotents of $\mathbb{D}$, with inverse

$$
H^{-1}(\Pi)=2\Pi-1 .
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

**Theorem (the pair map).** The map
$$
\Xi\longmapsto(\Pi_{+}(\Xi),\Pi_{-}(\Xi))
$$
is a bijection from the roots of $+1$ onto the ordered pairs of idempotents that are complete and orthogonal, $\Pi_{+}+\Pi_{-}=1$ and $\Pi_{+}\Pi_{-}=0$.

**Proof.** The pair of a root is complete and orthogonal by §*The Two Idempotents of a Root*, so the map is well defined. It is injective because the root is recovered from the pair, $\Xi=\Pi_{+}(\Xi)-\Pi_{-}(\Xi)$. It is surjective because an ordered complete orthogonal pair $(\Pi_{+},\Pi_{-})$ gives $\Xi=\Pi_{+}-\Pi_{-}$, and
$$
\Xi^{2}=\Pi_{+}^{2}-\Pi_{+}\Pi_{-}-\Pi_{-}\Pi_{+}+\Pi_{-}^{2}=\Pi_{+}+\Pi_{-}=1,
$$
so $\Xi$ is a root of $+1$ and the pair is its pair.

The pair map is a bijection, so the idempotent classification and the root classification are the same classification read through it. The four roots and the two idempotents they carry correspond as follows.

| Family | Root $\Xi$ | $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ | $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)$ | Unordered pair |
|---|---|---|---|---|
| Trivial roots | $1$ | $1$ | $0$ | $\{0,1\}$ |
| Trivial roots | $-1$ | $0$ | $1$ | $\{0,1\}$ |
| Non-trivial roots | $j$ | $\Pi_{+}$ | $\Pi_{-}$ | $\{\Pi_{+},\Pi_{-}\}$ |
| Non-trivial roots | $-j$ | $\Pi_{-}$ | $\Pi_{+}$ | $\{\Pi_{+},\Pi_{-}\}$ |

The root column is a bijection onto the idempotents; the last column is two-to-one. The root is recovered from the ordered pair as the difference of its members, and the unordered pair loses the sign of the root and nothing else.

### The Families of Idempotents

**The idempotents fall into two families, the trivial idempotents $0,1$ and the standard idempotents $\Pi_{\pm}$; both are finite.**

The idempotents fall into the two following families.

| Family | Form | Real parameters | Size | Position | Fixed by the conjugation? |
|---|---|---|---|---|---|
| Trivial idempotents | $0,1$ | none | two elements | the scalar line | yes |
| Standard idempotents | $\Pi_{\pm}=\tfrac12(1\pm j)$ | none | two elements | the two idempotent lines | no |

The idempotents form a **finite set of four elements**, not a positive-dimensional family. The reason is visible in the classification: the idempotent equation factors as $q'(2q-1)=0$, a product of two real scalars, so each factor gives a finite set of values; there is no vector part to vary independently. In the four-dimensional biquaternion algebra the non-trivial idempotents form a two-real-parameter Hermitian family and a four-real-parameter non-Hermitian family; here the non-trivial idempotents collapse to the two points $\Pi_{+},\Pi_{-}$. The idempotents are the indicator functions of the subsets of a two-point set under $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$:

$$
0\longmapsto(0,0),\qquad \Pi_{+}\longmapsto(1,0),\qquad \Pi_{-}\longmapsto(0,1),\qquad 1\longmapsto(1,1).
$$

The four are the empty set, the two singletons and the whole set; the power set of $\{+,-\}$ has $2^{2}=4$ elements.

### Idempotents and Their Projectors

**Every idempotent is the member attached to $+1$ of the pair of a root, and its complement the member attached to $-1$; the two standard idempotents carry the two projections that resolve the identity.**

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

the two complementary rank-one projectors of the plane. A projector in the split-complex algebra is an idempotent operator, and $P_{\pm}$ select the two coordinates of the isomorphism with $\mathbb{R}\oplus\mathbb{R}$. The two projectors are collected in the table.

| Projector | Formula | Image | Kernel |
|---|---|---|---|
| $P_{+}$ | $Q\mapsto Q\Pi_{+}$ | $\mathbb{R}\Pi_{+}$ | $\mathbb{R}\Pi_{-}$ |
| $P_{-}$ | $Q\mapsto Q\Pi_{-}$ | $\mathbb{R}\Pi_{-}$ | $\mathbb{R}\Pi_{+}$ |

### Idempotents and the Zero Divisors

**A non-trivial idempotent is a zero divisor, and conversely every zero divisor is a nonzero real multiple of one of the two non-trivial idempotents.**

A non-trivial idempotent is a zero divisor, since

$$
\Pi_{+}(1-\Pi_{+})=\Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}\neq0,\qquad 1-\Pi_{+}=\Pi_{-}\neq0,
$$

and symmetrically for $\Pi_{-}$. Conversely, every zero divisor is a nonzero real multiple of one of the two idempotents:

$$
\mathcal{Z}=\mathbb{R}^{\times}\Pi_{+}\cup\mathbb{R}^{\times}\Pi_{-}.
$$

The two kinds of zero divisor are collected in the table.

| Zero divisor | Form | Relation to the idempotents |
|---|---|---|
| Non-trivial idempotents | $\Pi_{+},\Pi_{-}$ | the primitive zero divisors |
| All nonzero multiples | $\mathbb{R}^{\times}\Pi_{+}\cup\mathbb{R}^{\times}\Pi_{-}$ | every zero divisor |

That statement, with its proof and the structure of the zero-divisor set, is *Zero Divisors of the Split-Complex Algebra*; the present article records only that the non-trivial idempotents are the primitive zero divisors.

### Idempotents and the Minimal Ideals

**The standard idempotents generate the two non-trivial minimal ideals, and the algebra is their direct sum.**

The principal ideals

$$
\mathbb{D}\Pi_{+}=\mathbb{R}\Pi_{+},\qquad \mathbb{D}\Pi_{-}=\mathbb{R}\Pi_{-}
$$

are the two non-trivial minimal ideals, and

$$
\mathbb{D}=\mathbb{D}\Pi_{+}\oplus\mathbb{D}\Pi_{-}
$$

is the direct sum of the two copies of $\mathbb{R}$. The two ideals are collected in the table.

| Ideal | Generator | Form | Minimality |
|---|---|---|---|
| Two-sided | $\Pi_{+}$ | $\mathbb{D}\Pi_{+}=\mathbb{R}\Pi_{+}$ | yes |
| Two-sided | $\Pi_{-}$ | $\mathbb{D}\Pi_{-}=\mathbb{R}\Pi_{-}$ | yes |

The minimality is proved in *Ideals and Peirce Decomposition of the Split-Complex Algebra*, where the idempotents, the Peirce decomposition and the failure of simplicity are developed together.

### Idempotents and the Involutions

**The conjugation exchanges the two standard idempotents, and it exchanges the two non-trivial roots of $+1$.**

The only non-identity involution of the split-complex algebra is the conjugation $\bar{\cdot}$. It is $\mathbb{R}$-linear and multiplicative, and it acts on the basis by $\bar 1=1$ and $\bar j=-j$. The idempotents $\Pi_{\pm}=\tfrac12(1\pm j)$ are therefore exchanged, $\overline{\Pi_{+}}=\Pi_{-}$ and $\overline{\Pi_{-}}=\Pi_{+}$; the trivial idempotents $0$ and $1$ are fixed.

The action of the involutions on the idempotents is collected in the table.

| Involution | $0$ | $1$ | $\Pi_{+}$ | $\Pi_{-}$ |
|---|---|---|---|---|
| conjugation $\bar{\cdot}$ | $0$ | $1$ | $\Pi_{-}$ | $\Pi_{+}$ |

On the roots, the conjugation fixes $\pm1$ and exchanges $j$ with $-j$. Since $j$ and $-j$ carry the same unordered pair $\{\Pi_{+},\Pi_{-}\}$, the conjugation preserves the unordered pair and exchanges the two members of the ordered pair, $\overline{\Pi_{+}(j)}=\Pi_{-}(j)$ and $\overline{\Pi_{-}(j)}=\Pi_{+}(j)$.

## Summary

| Item | Result |
|---|---|
| Roots of $+1$ | $1,-1,j,-j$ |
| Roots of $-1$ | none |
| Root set | group $(\mathbb{Z}/2\mathbb{Z})^{2}$, every non-identity element of order $2$ |
| Idempotents | $0,1,\Pi_{+},\Pi_{-}$ |
| Hermitian idempotents | $0,1$, the conjugation fixing them |
| Non-Hermitian idempotents | $\Pi_{+},\Pi_{-}$, the conjugation exchanging them |
| Halving map | bijection $H(\Xi)=\tfrac12(1+\Xi)$, inverse $H^{-1}(\Pi)=2\Pi-1$ |
| Standard pair | central, primitive, complete and orthogonal; $\mathbb{D}=\mathbb{R}\Pi_{+}\oplus\mathbb{R}\Pi_{-}$ |
| Zero divisors | the non-trivial idempotents and their nonzero real multiples |
| Involutions | the conjugation exchanges $\Pi_{+}$ and $\Pi_{-}$ |

The roots of $+1$ in the split-complex algebra are exactly the four elements $1,-1,j,-j$; there are no others and there are no roots of $-1$. The roots form the group $(\mathbb{Z}/2\mathbb{Z})^{2}$, and the two real roots are timelike units while the two imaginary roots are spacelike units.

The idempotents are exactly $0,1,\Pi_{+}=\tfrac12(1+j),\Pi_{-}=\tfrac12(1-j)$. The **halving map** $H(\Xi)=\tfrac12(1+\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $H^{-1}(\Pi)=2\Pi-1$; each root carries the complete orthogonal pair $\Pi_{\pm}(\Xi)=\tfrac12(1\pm\Xi)$, whose difference is the root, and the class $\{\Xi,-\Xi\}$ gives the same unordered pair. The standard pair is central, primitive and complete, and it carries the direct-sum decomposition $\mathbb{D}=\mathbb{R}\Pi_{+}\oplus\mathbb{R}\Pi_{-}\cong\mathbb{R}\oplus\mathbb{R}$ and the two complementary projectors $P_{\pm}$. The trivial idempotents are Hermitian, fixed by the conjugation, and the non-trivial ones are non-Hermitian, exchanged by it. The non-trivial idempotents are the primitive zero divisors, and every zero divisor is a nonzero real multiple of one of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=+1$ | The split-complex algebra |
| $\bar{\cdot}$ | The conjugation, the intrinsic involution |
| $\Xi$ | A root of $+1$, $\Xi^{2}=1$ |
| $\mathcal{R}_{+1}=\{1,-1,j,-j\}$ | The four roots of $+1$, a group $(\mathbb{Z}/2\mathbb{Z})^{2}$ |
| $\Pi$ | An idempotent, $\Pi^{2}=\Pi$ |
| Hermitian idempotent | An idempotent fixed by the conjugation, $\overline{\Pi}=\Pi$ |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The standard idempotents |
| $\Pi_{\pm}(\Xi)=\tfrac12(1\pm\Xi)$ | The two idempotents carried by the root $\Xi$ |
| $\Pi_{+}(\Xi)+\Pi_{-}(\Xi)=1$, $\Pi_{+}(\Xi)\Pi_{-}(\Xi)=0$ | Completeness and orthogonality of the pair |
| $\Xi=\Pi_{+}(\Xi)-\Pi_{-}(\Xi)$ | The root as the difference of its pair |
| $H(\Xi)=\tfrac12(1+\Xi)$ | The halving map from the roots of $+1$ to the idempotents |
| $H^{-1}(\Pi)=2\Pi-1$ | The inverse halving map |
| $P_{\pm}:Q\mapsto Q\Pi_{\pm}=Q_{\pm}\Pi_{\pm}$ | The two complementary projections |
| $\mathbb{D}\Pi_{\pm}=\mathbb{R}\Pi_{\pm}$ | The two minimal ideals |

## Further Reading

- [Split-Complex Algebra](split-complex-algebra.html), for the product, its unit and the element theory of the algebra.
- [Square Roots of Zero and the Nilpotents of the Split-Complex Algebra](square-roots-of-zero-and-the-nilpotents-of-the-split-complex-algebra.html), for the companion central value $0$ and the absence of nonzero nilpotents.
- [Square Roots of a General Element in the Split-Complex Algebra](square-roots-of-a-general-element-in-the-split-complex-algebra.html), for the roots of $\Xi^{2}=Q$.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the zero divisors as the nonzero real multiples of the two idempotents.
- [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), for the two minimal ideals and the Peirce decomposition.
- [Norm and Invertibility in the Split-Complex Algebra](norm-and-invertibility-in-the-split-complex-algebra.html), for the shell of the plain algebraic norm at $1$.
- [Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions](square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), the complex commutative case, where the same four-point pattern is read over $\mathbb{C}$ and the roots of $-1$ are four.
- [Idempotents](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), the non-commutative case, where the roots of $+1$ and the idempotents form larger families.
