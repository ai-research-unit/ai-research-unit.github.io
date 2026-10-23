# __Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions__

## Introduction

Of the four products of *The Four Products, Their Forms and Their Algebraic Norms*, exactly one makes the underlying complex space of $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ an associative unital $\mathbb{C}$-algebra; the algebra is *Introduction to the Algebra of the Reduced Biquaternions*, and its multiplication is the general plain bilinear product of two reduced biquaternions, $\breve Q_{1}\breve Q_{2}$. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\Xi\in\mathbb{B}_{\mathrm{r}}$ with

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
1,\qquad -1,\qquad j,\qquad -j,
$$

and there are no others. The two **trivial roots** $\pm1$ give the trivial idempotents $1$ and $0$; the two **non-trivial roots** $\pm j$ give the standard idempotents

$$
\Pi_{\pm}=\tfrac12(1\pm j).
$$

The trivial idempotents are Hermitian, fixed by the star; the standard idempotents are non-Hermitian, exchanged by it. Every idempotent is one of the four $0,1,\Pi_{+},\Pi_{-}$; there are no positive-dimensional families, because the root equation reduces to the two complex equations $\Xi_{+}^{2}=1$ and $\Xi_{-}^{2}=1$, each with two solutions, hence four roots. The roots of $+1$ form the four-element group $(\mathbb{Z}/2\mathbb{Z})^{2}$ under multiplication, and every root is a unit. The roots of $-1$ are the four elements $\pm i$ and $\pm ij$, the roots of $+1$ multiplied by $i$; they are not the roots of $+1$.

The following table collects the results at a glance.

| Item | Result | Size |
|---|---|---|
| Roots of $+1$ | $1,-1,j,-j$ | four elements |
| Roots of $-1$ | $i,-i,ij,-ij$ | four elements |
| Root set | group $(\mathbb{Z}/2\mathbb{Z})^{2}$ | four elements |
| Idempotents | $0,1,\Pi_{+},\Pi_{-}$ | four elements |
| Hermitian idempotents | $0,1$, the star fixing them | two elements |
| Non-Hermitian idempotents | $\Pi_{+},\Pi_{-}$, the star exchanging them | two elements |
| Halving map | bijection $H(\Xi)=\tfrac12(1+\Xi)$ | two-to-one on unordered pairs |
| Standard pair | $\Pi_{\pm}=\tfrac12(1\pm j)$, central, primitive, complete and orthogonal | two elements |
| Zero divisors | the non-trivial idempotents and their nonzero complex multiples | two lines |
| Involutions | the tessarine sign and the star exchange $\Pi_{+}$ and $\Pi_{-}$; the bar fixes both; the flat sends each to the negative of the other | four involutions |

The article is algebraic. It does not treat the roots of the general quadratic $\Xi^{2}=Q$, which is *Square Roots of a General Element in the Algebra of the Reduced Biquaternions*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Algebra of the Reduced Biquaternions*; the structure of the zero-divisor set, which is *Zero Divisors of the Algebra of the Reduced Biquaternions*; or the ideals the standard idempotents generate, which are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*. The subsection §*The Roots of Minus One* records the roots of $-1$; it is a remark, it is used nowhere, and it opens nothing.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*, and the general definition of an idempotent, with the orthogonal, complete and primitive families, the Hermitian idempotent and the Peirce decomposition, is the same article. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other three general products are *The Four Products, Their Forms and Their Algebraic Norms*.

## The Roots of One

**The roots of $+1$ are exactly $\pm1$ and $\pm j$; there are no others.**

A **root of $+1$** is an element $\Xi\in\mathbb{B}_{\mathrm{r}}$ with $\Xi^{2}=1$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in the idempotent coordinates,

$$
\Xi=\Xi_{+}\Pi_{+}+\Xi_{-}\Pi_{-},\qquad \Xi_{\pm}=\Xi_{\blacktriangle}\pm\Xi_{\blacktriangledown},
$$

with $\Xi_{\blacktriangle},\Xi_{\blacktriangledown}\in\mathbb{C}$. Because the product is componentwise in the idempotent basis and $\Pi_{\pm}^{2}=\Pi_{\pm}$, $\Pi_{+}\Pi_{-}=0$, the square is

$$
\Xi^{2}=\Xi_{+}^{2}\Pi_{+}+\Xi_{-}^{2}\Pi_{-}.
$$

The equation $\Xi^{2}=1=\Pi_{+}+\Pi_{-}$ is therefore equivalent to the **pair of complex equations**

$$
\Xi_{+}^{2}=1,\qquad \Xi_{-}^{2}=1.
$$

The two equations are collected in the table.

| Case | Equation | Solutions |
|---|---|---|
| $\Xi_{+}$ | $\Xi_{+}^{2}=1$ | $\Xi_{+}=+1$ or $\Xi_{+}=-1$ |
| $\Xi_{-}$ | $\Xi_{-}^{2}=1$ | $\Xi_{-}=+1$ or $\Xi_{-}=-1$ |

There is no coupling between the two coordinates: the root problem splits into two independent one-dimensional root problems over $\mathbb{C}$, each with the two solutions $\pm1$. The four combinations are the four roots.

**Remark (the coordinate form).** In the basis $1,j$ the same equations read

$$
\Xi_{\blacktriangle}^{2}+\Xi_{\blacktriangledown}^{2}=1,\qquad 2\Xi_{\blacktriangle}\Xi_{\blacktriangledown}=0,
$$

because $\Xi^{2}=(\Xi_{\blacktriangle}^{2}+\Xi_{\blacktriangledown}^{2})+2\Xi_{\blacktriangle}\Xi_{\blacktriangledown}j$. Over $\mathbb{C}$ the second equation forces $\Xi_{\blacktriangle}=0$ or $\Xi_{\blacktriangledown}=0$; the first then gives $\Xi_{\blacktriangle}=\pm1$ with $\Xi_{\blacktriangledown}=0$, or $\Xi_{\blacktriangle}=0$ with $\Xi_{\blacktriangledown}=\pm1$. The four solutions are $\pm1$ and $\pm j$.

### The Trivial Roots

The two **trivial roots** are

$$
\Xi=+1,\qquad \Xi=-1 .
$$

They are the roots in the complex line $\mathbb{C}1$, and they are the only roots with vanishing $j$-part. They give the trivial idempotents $1$ and $0$ under the halving map.

### The Non-Trivial Roots

The two **non-trivial roots** are

$$
\Xi=+j,\qquad \Xi=-j .
$$

They are the roots in the line $j\mathbb{C}$, with vanishing scalar part; they are anti-fixed by the star, $\Xi^{*}=-\Xi$, hence non-Hermitian, while the bar fixes them. They give the standard idempotents $\Pi_{+}$ and $\Pi_{-}$ under the halving map.

### Statement of the Theorem

**Theorem (the roots of $+1$).** The roots of $+1$ in $\mathbb{B}_{\mathrm{r}}$ are exactly the four elements

$$
\boxed{\;
1,\qquad -1,\qquad j,\qquad -j
\;}.
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

| Family | Form | Real parameters | Size | Position | Fixed by the star? |
|---|---|---|---|---|---|
| Trivial roots | $\Xi=\pm1$ | none | two elements | the complex line $\mathbb{C}1$ | yes |
| Non-trivial roots | $\Xi=\pm j$ | none | two elements | the line $j\mathbb{C}$ | no |

### Verification

The four roots are checked by squaring.

| Family | Square | Value |
|---|---|---|
| Trivial roots | $(\pm1)^{2}$ | $1$ |
| Non-trivial roots | $(\pm j)^{2}$ | $1$ |

The verification is the whole computation: the split sign $j^{2}=+1$ is what makes $j$ a root of $+1$ and not a root of $-1$.

### The Roots of Minus One

**Proposition (the roots of $-1$).** The equation $\Xi^{2}=-1$ has the four solutions

$$
\Xi=+i,\qquad \Xi=-i,\qquad \Xi=+ij,\qquad \Xi=-ij .
$$

**Proof.** In the idempotent coordinates the equation is $\Xi_{+}^{2}=-1$ and $\Xi_{-}^{2}=-1$, so $\Xi_{+}\in\{+i,-i\}$ and $\Xi_{-}\in\{+i,-i\}$. The four combinations are

$$
(i,i)=i,\qquad (i,-i)=ij,\qquad (-i,i)=-ij,\qquad (-i,-i)=-i,
$$

where the second and third use $j=(1,-1)$ and $i=(i,i)$ in the idempotent coordinates, so $ij=(i,-i)$. There are no others.

The result is collected in the table.

| Equation | Solutions | Size | Relation to the roots of $+1$ |
|---|---|---|---|
| $\Xi^{2}=-1$ | $i,-i,ij,-ij$ | four elements | $i\{1,-1,j,-j\}$ |

The four roots of $-1$ are the roots of $+1$ multiplied by $i$:

$$
i\{1,-1,j,-j\}=\{i,-i,ij,-ij\},
$$

and they lie in the real plane $i\mathbb{R}\{1,j\}$ of the algebra. The roots of $+1$ are not the roots of $-1$, and the distinction is stated here because the two families are both four.

### Status of the Roots

**Proposition (the roots form a group).** The set

$$
\mathcal{R}_{+1}=\{1,-1,j,-j\}
$$

is a subgroup of the group of units of the plain product, isomorphic to $(\mathbb{Z}/2\mathbb{Z})^{2}$.

**Proof.** The product of two roots is a root, because $(\Xi B)^{2}=\Xi^{2}B^{2}=1$ and the algebra is commutative; the unit is $1$; and each element is its own inverse, $\Xi^{2}=1$. The group is abelian of order four with every non-identity element of order two, hence $(\mathbb{Z}/2\mathbb{Z})^{2}$.

**Proposition (the roots are units).** Every root of $+1$ is a unit, with $\Xi^{-1}=\Xi$, and no root is a zero divisor.

**Proof.** $\Xi^{2}=1$ reads $\Xi\Xi=1$, so $\Xi$ is invertible with inverse $\Xi$. A unit is not a zero divisor.

**Corollary (the real form).** In the real coordinates the roots are $1=(1,0,0,0)$, $-1=(-1,0,0,0)$, $j=(0,0,1,0)$ and $-j=(0,0,-1,0)$; all four lie in the real subalgebra $\mathbb{R}\{1,j\}$.

The status of the roots is collected in the table.

| Property | Result |
|---|---|
| Closed under multiplication? | yes, the product of two roots is a root |
| Group? | yes, $(\mathbb{Z}/2\mathbb{Z})^{2}$ |
| Units? | yes, $\Xi^{-1}=\Xi$ |
| Zero divisors? | no |
| Position | all four in the real subalgebra $\mathbb{R}\{1,j\}$ |

## The Idempotents

**The idempotents of $\mathbb{B}_{\mathrm{r}}$ are exactly the four elements $0,1,\Pi_{+},\Pi_{-}$; the standard pair is orthogonal, complete, central and primitive, and every idempotent is the image of exactly one root of $+1$ under the halving map.**

The **idempotents** of $\mathbb{B}_{\mathrm{r}}$ are the elements satisfying $\Pi^{2}=\Pi$, the square being the one of the general plain bilinear product. They correspond to projectors under multiplication, and in $\mathbb{B}_{\mathrm{r}}$ they do four separate jobs at once: they give the direct sum decompositions of the algebra into the two idempotent lines, and in particular the two minimal ideals; they classify the zero divisors, every nonzero one of which is a complex multiple of an idempotent; they are in bijection with the roots of $+1$ through the halving map, each root carrying a complete orthogonal pair, so their classification is the classification of those roots; and they carry the Peirce decomposition of the algebra. The definition and the families are the general ones of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, read here in the general plain bilinear product.

### The Definition

**Definition.** An element $\Pi$ of $\mathbb{B}_{\mathrm{r}}$ is an **idempotent of the algebra of the reduced biquaternions** when

$$
\Pi^{2}=\Pi .
$$

The element $0$ is an idempotent, and so is the unit $1$; the two are the **trivial idempotents**. The equation names a product, and the notion is relative to it: throughout this article the product is the general plain bilinear product, the multiplication of the algebra, and another product is named where it is meant. The other three general products are *The Four Products, Their Forms and Their Algebraic Norms*.

Two idempotents $\Pi,\Pi'$ are **orthogonal** when $\Pi\Pi'=\Pi'\Pi=0$; a family is **pairwise orthogonal** when its members are pairwise orthogonal, and **complete** when in addition their sum is $1$. A nonzero idempotent is **primitive** when it is not the sum of two nonzero orthogonal idempotents.

Idempotents encode direct summands of the algebra: an idempotent $\Pi$ and its complement $1-\Pi$ split the underlying $\mathbb{C}$-module,

$$
\mathbb{B}_{\mathrm{r}}=\mathbb{B}_{\mathrm{r}}\Pi\oplus\mathbb{B}_{\mathrm{r}}(1-\Pi),\qquad \mathbb{B}_{\mathrm{r}}=\Pi\mathbb{B}_{\mathrm{r}}\oplus(1-\Pi)\mathbb{B}_{\mathrm{r}},
$$

the same on the left and on the right because the algebra is commutative. Every idempotent is the member attached to $+1$ of the pair of a root: for $\Pi$ idempotent the element $\Xi=2\Pi-1$ is a root of $+1$, and $\Pi_{+}(\Xi)=\Pi$ while $\Pi_{-}(\Xi)=1-\Pi$.

### The Two Idempotents of a Root

**A root $\Xi$ of $+1$ carries the two idempotents $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ and $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)=1-\Pi_{+}(\Xi)$; they are complete and orthogonal, their difference is the root, and the value of the pair map is an ordered complete orthogonal pair.**

**Theorem (the two idempotents of a root).** For a root $\Xi$ of $+1$, the elements

$$
\Pi_{+}(\Xi)=\tfrac12(1+\Xi),\qquad \Pi_{-}(\Xi)=\tfrac12(1-\Xi)
$$

are idempotent, complete and orthogonal; the identities are collected in the table.

| Identity | Value |
|---|---|
| $\Pi_{+}(\Xi)^{2}$ | $\Pi_{+}(\Xi)$ |
| $\Pi_{-}(\Xi)^{2}$ | $\Pi_{-}(\Xi)$ |
| $\Pi_{+}(\Xi)\Pi_{-}(\Xi)$ | $0$ |
| $\Pi_{+}(\Xi)+\Pi_{-}(\Xi)$ | $1$ |
| $\Pi_{+}(\Xi)-\Pi_{-}(\Xi)$ | $\Xi$ |

**Proof.** The idempotence is the two-line computation of the introduction; the sum is $\tfrac12(1+\Xi)+\tfrac12(1-\Xi)=1$; the product is $\tfrac14(1-\Xi^{2})=0$; and the difference is $\tfrac12(1+\Xi)-\tfrac12(1-\Xi)=\Xi$.

**Corollary (the standard pair).** The standard idempotents are the pair of the root $j$: $\Pi_{+}(j)=\Pi_{+}$ and $\Pi_{-}(j)=\Pi_{-}$.

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

The action is collected in the table.

| Multiplication by $\Xi$ | On $\Pi_{+}$ | On $\Pi_{-}$ |
|---|---|---|
| left or right | $+1$ | $-1$ |

So the root is $+1$ on the first idempotent and $-1$ on the second, and the algebra decomposes under multiplication by $\Xi$ into the two eigenspaces $\mathbb{C}\Pi_{+}$ and $\mathbb{C}\Pi_{-}$ with eigenvalues $+1$ and $-1$. The pair $\Pi_{\pm}$ is the spectral resolution of the root.

The subalgebra spanned by the pair and the root is therefore the algebra $\mathbb{C}\Pi_{+}\oplus\mathbb{C}\Pi_{-}\cong\mathbb{C}\times\mathbb{C}$, and the root is the element $(+1,-1)$ of that algebra. In the idempotent coordinates the pair is $(1,0)$ and $(0,1)$, and the root is $(1,-1)$; the four roots are the four sign choices on the two coordinates.

### The Standard Idempotents

**The algebra carries the standard idempotents $\Pi_{+}=\tfrac12(1+j)$ and $\Pi_{-}=\tfrac12(1-j)$, the two idempotents of the root $j$, with $\Pi_{+}\Pi_{-}=0$ and $\Pi_{+}+\Pi_{-}=1$; each is central and primitive.**

Put

$$
\Pi_{+}=\tfrac12(1+j),\qquad \Pi_{-}=\tfrac12(1-j).
$$

They are the pair of the root $j$ of $+1$, and they are the two solutions of the idempotent equation that are different from $0$ and $1$. Since $j^{2}=+1$,

$$
\Pi_{+}^{2}=\frac{1+2j+j^{2}}{4}=\frac{2+2j}{4}=\Pi_{+},\qquad \Pi_{-}^{2}=\Pi_{-},
$$

and

$$
\Pi_{+}\Pi_{-}=\frac{(1+j)(1-j)}{4}=\frac{1-j^{2}}{4}=0,\qquad \Pi_{+}+\Pi_{-}=1.
$$

They are **central**, because the algebra is commutative, and **primitive**, because the corner algebras $\Pi_{\pm}\mathbb{B}_{\mathrm{r}}\Pi_{\pm}=\mathbb{C}\Pi_{\pm}$ are fields, isomorphic to $\mathbb{C}$. The properties of the pair are collected in the table.

| Property | $\Pi_{+},\Pi_{-}$ |
|---|---|
| Orthogonal | $\Pi_{+}\Pi_{-}=0$ |
| Complete | $\Pi_{+}+\Pi_{-}=1$ |
| Central | yes, the algebra is commutative |
| Primitive | yes, $\Pi_{\pm}\mathbb{B}_{\mathrm{r}}\Pi_{\pm}=\mathbb{C}\Pi_{\pm}$ |
| Hermitian idempotent | no for the star, which exchanges them; both are fixed by the bar |
| Zero divisor | yes, $\Pi_{+}\Pi_{-}=0$ |
| Minimal ideals | $\mathbb{B}_{\mathrm{r}}\Pi_{\pm}=\mathbb{C}\Pi_{\pm}$ |

### The Classification of the Idempotents

**The idempotents of $\mathbb{B}_{\mathrm{r}}$ are exactly $0$, $1$, $\Pi_{+}$ and $\Pi_{-}$; there are no others.**

**Theorem (the idempotents).** The solutions of $\Pi^{2}=\Pi$ are

$$
\boxed{\; \Pi=0,\qquad \Pi=1,\qquad \Pi=\Pi_{+}=\tfrac12(1+j),\qquad \Pi=\Pi_{-}=\tfrac12(1-j) \;},
$$

and there are no others.

**Proof.** In the idempotent coordinates the equation is the pair $Q_{+}^{2}=Q_{+}$ and $Q_{-}^{2}=Q_{-}$; a complex number satisfies $z^{2}=z$ if and only if $z=0$ or $z=1$. The four pairs $(Q_{+},Q_{-})$ give, by $Q_{\blacktriangle}=\tfrac12(Q_{+}+Q_{-})$ and $Q_{\blacktriangledown}=\tfrac12(Q_{+}-Q_{-})$,

$$
(0,0)\to \Pi=0,\quad (1,1)\to \Pi=1,\quad (1,0)\to \Pi=\Pi_{+},\quad (0,1)\to \Pi=\Pi_{-}.
$$

### The Correspondence with the Roots of One

**The halving map $H(\Xi)=\tfrac12(1+\Xi)$ is a bijection from the roots of $+1$ onto the idempotents; the pair map $\Xi\mapsto(\Pi_{+}(\Xi),\Pi_{-}(\Xi))$ is a bijection from the roots of $+1$ onto the ordered complete orthogonal pairs of idempotents; and the class $\{\Xi,-\Xi\}$ gives the same unordered pair.**

**Theorem (the halving map).** The map

$$
H(\Xi)=\tfrac12(1+\Xi)
$$

restricts to a bijection from the roots of $+1$ onto the idempotents, with

$$
H(1)=1,\qquad H(-1)=0,\qquad H(j)=\Pi_{+},\qquad H(-j)=\Pi_{-},
$$

and the inverse on the idempotents is $\Pi\mapsto 2\Pi-1$.

**Proof.** The four values are direct: $\tfrac12(1+1)=1$, $\tfrac12(1-1)=0$, $\tfrac12(1+j)=\Pi_{+}$, $\tfrac12(1-j)=\Pi_{-}$. If $\Xi^{2}=1$ then $H(\Xi)^{2}=\tfrac14(1+2\Xi+\Xi^{2})=\tfrac14(2+2\Xi)=H(\Xi)$, so $H$ maps roots of $+1$ into idempotents; if $\Pi^{2}=\Pi$ then $2\Pi-1$ has $(2\Pi-1)^{2}=4\Pi^{2}-4\Pi+1=1$, so $2\Pi-1$ is a root of $+1$; and the two maps are inverse, since $H(2\Pi-1)=\tfrac12(1+2\Pi-1)=\Pi$.

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

The root column is a bijection onto the idempotents; the last column is two-to-one. The root is recovered from the ordered pair as the difference of its members, $\Xi=\Pi_{+}(\Xi)-\Pi_{-}(\Xi)$, and the unordered pair loses the sign of the root and nothing else. The roots of $+1$ and the idempotents meet in the single element $1$, the fixed point of the halving map.

### The Families of Idempotents

**The idempotents fall into two families, the trivial idempotents $0,1$ and the standard idempotents $\Pi_{\pm}$; both are finite.**

The idempotents fall into the two following families.

| Family | Form | Real parameters | Size | Position | Fixed by the star? |
|---|---|---|---|---|---|
| Trivial idempotents | $0,1$ | none | two elements | the scalar line | yes |
| Standard idempotents | $\Pi_{\pm}=\tfrac12(1\pm j)$ | none | two elements | the two idempotent lines | no |

The idempotents form a **finite set of four elements**, not a positive-dimensional family. The reason is visible in the classification: the idempotent equation forces $Q_{+}\in\{0,1\}$ and $Q_{-}\in\{0,1\}$, because each idempotent coordinate is a scalar and the equation $X^{2}=X$ has only the solutions $0$ and $1$; there is no vector part to vary independently. In the four-dimensional biquaternion algebra the non-trivial idempotents form a two-real-parameter Hermitian family and a four-real-parameter non-Hermitian family; here the non-trivial idempotents collapse to the two points $\Pi_{+},\Pi_{-}$. The idempotents are the indicator functions of the subsets of a two-point set under $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$:

$$
0\longmapsto(0,0),\qquad \Pi_{+}\longmapsto(1,0),\qquad \Pi_{-}\longmapsto(0,1),\qquad 1\longmapsto(1,1).
$$

### Idempotents and Their Projectors

**Every idempotent is the member attached to $+1$ of the pair of a root, and its complement the member attached to $-1$; the two standard idempotents carry the two projections that resolve the identity.**

An idempotent $\Pi$ acts by multiplication as a **projector**: $\Pi^{2}=\Pi$, so $L_{\Pi}$ is the identity on its image and annihilates its kernel. Its complement $1-\Pi$ is also an idempotent, and $\Pi(1-\Pi)=0$, so the pair gives the direct-sum decomposition

$$
\mathbb{B}_{\mathrm{r}}=\mathbb{B}_{\mathrm{r}}\Pi\oplus\mathbb{B}_{\mathrm{r}}(1-\Pi),
$$

the same on the left and on the right because the algebra is commutative.

For the standard pair the projections are the projections onto the two idempotent lines,

$$
P_{+}:\breve Q\longmapsto \breve Q\Pi_{+}=Q_{+}\Pi_{+},\qquad
P_{-}:\breve Q\longmapsto \breve Q\Pi_{-}=Q_{-}\Pi_{-},
$$

with

$$
P_{+}^{2}=P_{+},\qquad P_{-}^{2}=P_{-},\qquad P_{+}P_{-}=P_{-}P_{+}=0,\qquad P_{+}+P_{-}=\mathrm{id}.
$$

The identity $P_{+}+P_{-}=\mathrm{id}$ is the **resolution of the identity**, and the two projections are the Peirce projections of the algebra. The images are the two lines, which meet only at the origin. The two projectors are collected in the table.

| Projector | Formula | Image | Kernel |
|---|---|---|---|
| $P_{+}$ | $\breve Q\mapsto \breve Q\Pi_{+}$ | $\mathbb{C}\Pi_{+}$ | $\mathbb{C}\Pi_{-}$ |
| $P_{-}$ | $\breve Q\mapsto \breve Q\Pi_{-}$ | $\mathbb{C}\Pi_{-}$ | $\mathbb{C}\Pi_{+}$ |

The decomposition of a general element reads

$$
\breve Q=P_{+}(\breve Q)+P_{-}(\breve Q)=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_{+}+(Q_{\blacktriangle}-Q_{\blacktriangledown})\Pi_{-},
$$

the idempotent coordinates of *Reduced Biquaternion Space*. The Peirce decomposition of a pair of idempotents, with the four subspaces $\Pi\mathbb{B}_{\mathrm{r}}\Pi$, $\Pi\mathbb{B}_{\mathrm{r}}(1-\Pi)$, $(1-\Pi)\mathbb{B}_{\mathrm{r}}\Pi$ and $(1-\Pi)\mathbb{B}_{\mathrm{r}}(1-\Pi)$, is *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; here only the two projections and the two lines they carry are read.

### Idempotents and the Zero Divisors

**A non-trivial idempotent is a zero divisor, and conversely every zero divisor is a nonzero complex multiple of one of the two non-trivial idempotents.**

A non-trivial idempotent is a zero divisor, since

$$
\Pi_{+}(1-\Pi_{+})=\Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}\neq0,\qquad 1-\Pi_{+}=\Pi_{-}\neq0,
$$

and symmetrically for $\Pi_{-}$. Conversely, every zero divisor is a nonzero complex multiple of one of the two non-trivial idempotents:

$$
\mathcal{Z}=\mathbb{C}^{\times}\Pi_{+}\cup\mathbb{C}^{\times}\Pi_{-}.
$$

The two kinds of zero divisor are collected in the table.

| Zero divisor | Form | Relation to the idempotents |
|---|---|---|
| Non-trivial idempotents | $\Pi_{+},\Pi_{-}$ | the primitive zero divisors |
| All nonzero multiples | $\mathbb{C}^{\times}\Pi_{+}\cup\mathbb{C}^{\times}\Pi_{-}$ | every zero divisor |

That statement, with its proof and the structure of the zero-divisor set, is *Zero Divisors of the Algebra of the Reduced Biquaternions*; the present article records only that the non-trivial idempotents are the primitive zero divisors.

### Idempotents and the Minimal Ideals

**The standard idempotents generate the two non-trivial minimal ideals, and the algebra is their direct sum.**

The principal ideals

$$
\mathbb{B}_{\mathrm{r}}\Pi_{+}=\mathbb{C}\Pi_{+},\qquad \mathbb{B}_{\mathrm{r}}\Pi_{-}=\mathbb{C}\Pi_{-}
$$

are the two non-trivial minimal ideals, and

$$
\boxed{\; \mathbb{B}_{\mathrm{r}}=\mathbb{B}_{\mathrm{r}}\Pi_{+}\oplus\mathbb{B}_{\mathrm{r}}\Pi_{-} \;}
$$

is the direct sum of the two copies of $\mathbb{C}$. The two ideals are collected in the table.

| Ideal | Generator | Form | Minimality |
|---|---|---|---|
| Two-sided | $\Pi_{+}$ | $\mathbb{B}_{\mathrm{r}}\Pi_{+}=\mathbb{C}\Pi_{+}$ | yes |
| Two-sided | $\Pi_{-}$ | $\mathbb{B}_{\mathrm{r}}\Pi_{-}=\mathbb{C}\Pi_{-}$ | yes |

The minimality is proved in *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, where the idempotents, the Peirce decomposition and the failure of simplicity are developed together.

### Idempotents and the Involutions

**The tessarine sign and the star both exchange the two non-trivial idempotents, and only the bar fixes every idempotent.**

**Theorem.** $\Pi_{+,\mathrm{ts}}=\Pi_{-}=\Pi_{+}^{*}$, $\Pi_{-,\mathrm{ts}}=\Pi_{+}=\Pi_{-}^{*}$, and $\overline{\Pi_{+}}=\Pi_{+}$, $\overline{\Pi_{-}}=\Pi_{-}$; the flat sends each idempotent to the negative of the other, $\Pi_{+}^{\flat}=-\Pi_{-}$ and $\Pi_{-}^{\flat}=-\Pi_{+}$, which is not an idempotent.

**Proof.** $\Pi_{+,\mathrm{ts}}=\tfrac12(1+j)_{\mathrm{ts}}=\tfrac12(1-j)=\Pi_{-}$, and $\Pi_{-,\mathrm{ts}}=\Pi_{+}$ (*The Two Involutions and the Group of Involutions*); the bar conjugates the coefficients of $\Pi_{\pm}=\tfrac12\pm\tfrac12 j$, which are real, so it fixes each idempotent; the star is $\bar{\cdot}\circ{}_{\mathrm{ts}}$, so $\Pi_{+}^{*}=\overline{\Pi_{+,\mathrm{ts}}}=\overline{\Pi_{-}}=\Pi_{-}$ and $\Pi_{-}^{*}=\Pi_{+}$, the star exchanging the two as the tessarine sign does. The flat is $-{}^{*}$, so it sends each idempotent to the negative of the other.

The action of the involutions on the idempotents is collected in the table.

| Involution | $0$ | $1$ | $\Pi_{+}$ | $\Pi_{-}$ |
|---|---|---|---|---|
| bar $\bar{\cdot}$ | $0$ | $1$ | $\Pi_{+}$ | $\Pi_{-}$ |
| tessarine sign ${}_{\mathrm{ts}}$ | $0$ | $1$ | $\Pi_{-}$ | $\Pi_{+}$ |
| star ${}^{*}$ | $0$ | $1$ | $\Pi_{-}$ | $\Pi_{+}$ |
| flat ${}^{\flat}$ | $0$ | $-1$ | $-\Pi_{-}$ | $-\Pi_{+}$ |

The trivial idempotents $0$ and $1$ are fixed by the bar, the tessarine sign and the star; the flat fixes $0$ and sends $1$ to $-1$.

**Corollary (the involution swaps the two lines).** The tessarine sign restricts to a $\mathbb{C}$-linear exchange of the two idempotent lines, $\mathbb{C}\Pi_{+}\leftrightarrow\mathbb{C}\Pi_{-}$, and the two lines are therefore conjugate under the intrinsic conjugate.

## Summary

| Item | Result |
|---|---|
| Roots of $+1$ | $1,-1,j,-j$ |
| Roots of $-1$ | $i,-i,ij,-ij$ |
| Root set | group $(\mathbb{Z}/2\mathbb{Z})^{2}$, every non-identity element of order $2$ |
| Idempotents | $0,1,\Pi_{+},\Pi_{-}$ |
| Hermitian idempotents | $0,1$, the star fixing them |
| Non-Hermitian idempotents | $\Pi_{+},\Pi_{-}$, the star exchanging them |
| Halving map | bijection $H(\Xi)=\tfrac12(1+\Xi)$, inverse $H^{-1}(\Pi)=2\Pi-1$ |
| Standard pair | central, primitive, complete and orthogonal; $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{+}\oplus\mathbb{C}\Pi_{-}$ |
| Zero divisors | the non-trivial idempotents and their nonzero complex multiples |
| Involutions | the tessarine sign and the star exchange $\Pi_{+}$ and $\Pi_{-}$; the bar fixes both; the flat sends each to the negative of the other |

The roots of $+1$ in the general plain algebra are the four elements

$$
1,\qquad -1,\qquad j,\qquad -j,
$$

and they form the group $(\mathbb{Z}/2\mathbb{Z})^{2}$ under multiplication; they all lie in the real subalgebra $\mathbb{R}\{1,j\}$, and every root is a unit. The roots of $-1$ are the four elements $\pm i$ and $\pm ij$, the roots of $+1$ multiplied by $i$.

The idempotents are the four elements

$$
0,\qquad 1,\qquad \Pi_{+}=\tfrac12(1+j),\qquad \Pi_{-}=\tfrac12(1-j),
$$

and the two non-trivial ones are complementary, orthogonal and zero divisors,

$$
\Pi_{+}^{2}=\Pi_{+},\qquad \Pi_{-}^{2}=\Pi_{-},\qquad \Pi_{+}\Pi_{-}=0,\qquad \Pi_{+}+\Pi_{-}=1 .
$$

Each root $\Xi$ of $+1$ carries the two idempotents $\Pi_{+}(\Xi)=\tfrac12(1+\Xi)$ and $\Pi_{-}(\Xi)=\tfrac12(1-\Xi)=1-\Pi_{+}(\Xi)$, a complete orthogonal pair whose difference is the root; the **halving map** $H(\Xi)=\tfrac12(1+\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $H^{-1}(\Pi)=2\Pi-1$, and the class $\{\Xi,-\Xi\}$ gives the same unordered pair. The four roots give the two unordered pairs $\{0,1\}$ and $\{\Pi_{+},\Pi_{-}\}$.

Each idempotent $\Pi$ carries the projector $P_{\Pi}(\breve Q)=\Pi\breve Q$, with $P_{\Pi}^{2}=P_{\Pi}$, $P_{+}+P_{-}=\mathrm{id}$ and $P_{+}P_{-}=0$; the explicit projections are $P_{+}(\breve Q)=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_{+}$ and $P_{-}(\breve Q)=(Q_{\blacktriangle}-Q_{\blacktriangledown})\Pi_{-}$, and they give the resolution of the identity and the decomposition $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{+}\oplus\mathbb{C}\Pi_{-}$. The two lines are the two minimal ideals, and the standard pair is central, primitive and complete. The trivial idempotents are Hermitian, fixed by the star, and the non-trivial ones are non-Hermitian, exchanged by it. The non-trivial idempotents are the primitive zero divisors, and every zero divisor is a nonzero complex multiple of one of them. The **tessarine sign** and the **star** both exchange the two non-trivial idempotents, $\Pi_{+,\mathrm{ts}}=\Pi_{-}=\Pi_{+}^{*}$ and $\Pi_{-,\mathrm{ts}}=\Pi_{+}=\Pi_{-}^{*}$, while only the bar fixes each idempotent, $\overline{\Pi_{+}}=\Pi_{+}$ and $\overline{\Pi_{-}}=\Pi_{-}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | The reduced biquaternion algebra, with basis $1,i,j,ij$ |
| ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$ | The star, the intrinsic involution |
| $\Xi$ | A root of $+1$, $\Xi^{2}=1$ |
| $\mathcal{R}_{+1}=\{1,-1,j,-j\}$ | The four roots of $+1$, a group $(\mathbb{Z}/2\mathbb{Z})^{2}$ |
| $\Xi_{\pm}$ | The idempotent coordinates of the root $\Xi$ |
| $\Pi$ | An idempotent, $\Pi^{2}=\Pi$ |
| Hermitian idempotent | An idempotent fixed by the star, $\Pi^{*}=\Pi$ |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | The standard idempotents |
| $\Pi_{\pm}(\Xi)=\tfrac12(1\pm\Xi)$ | The two idempotents carried by the root $\Xi$ |
| $\Pi_{+}(\Xi)+\Pi_{-}(\Xi)=1$, $\Pi_{+}(\Xi)\Pi_{-}(\Xi)=0$ | Completeness and orthogonality of the pair |
| $\Xi=\Pi_{+}(\Xi)-\Pi_{-}(\Xi)$ | The root as the difference of its pair |
| $H(\Xi)=\tfrac12(1+\Xi)$ | The halving map from the roots of $+1$ to the idempotents |
| $H^{-1}(\Pi)=2\Pi-1$ | The inverse halving map |
| $P_{\Pi}(\breve Q)=\Pi\breve Q$ | The projector carried by an idempotent |
| $P_{+}+P_{-}=\mathrm{id}$ | The resolution of the identity |
| $\mathbb{C}\Pi_{+}\oplus\mathbb{C}\Pi_{-}$ | The direct sum, the two minimal ideals |

## Further Reading

- [Introduction to the Algebra of the Reduced Biquaternions](introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.html), above this article in this category, for the algebra and the idempotent coordinates.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), above this article, for the action of the four maps on the idempotents.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), above this article, for the two lines the idempotents generate.
- [Annihilators of the Algebra of the Reduced Biquaternions](annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), above this article, for the annihilators of the idempotent lines.
- [Square Roots of Zero and the Nilpotents of the Algebra of the Reduced Biquaternions](square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the companion equation $\Xi^{2}=0$.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article in this category, for the full Peirce decomposition.
- [Square Roots of One and the Idempotents of the Split-Complex Algebra](square-roots-of-one-and-the-idempotents-of-the-split-complex-algebra.html), the real commutative case, where the same four-point pattern is read over $\mathbb{R}$.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), the non-commutative counterpart, where the roots of $+1$ and the idempotents form larger families.
