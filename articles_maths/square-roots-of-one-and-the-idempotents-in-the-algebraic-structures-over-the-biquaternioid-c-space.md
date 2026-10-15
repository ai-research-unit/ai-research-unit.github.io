# __Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space__

## Introduction

Let $\star$ be a product on the biquaternion algebra $\mathbb{B}$. An element $\tilde\Xi$ is a **root of the central value** $\lambda e_0$ when its square in that product is the value,

$$
\tilde\Xi\star\tilde\Xi=\lambda e_0 , \qquad \lambda\in\mathbb{C},
$$

and the **root set** of the value is the set of the solutions of the equation. This article reads the value $+1$ structure by structure in the twelve structures of the space, and then reads the idempotents, which are the roots of $+1$ carried by the halving map. The root of a general value, the four existence classes of the twelve structures and the criterion that a root of a non-zero value is a unit are *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, which states them once; its companion *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* reads the value $0$. The value $-1$ is not a subject of this article: its root sets are deduced, where they exist, from the root sets of $+1$ by one map, and they are the short remark that closes §*The Roots of One*. Nothing else here uses them. The general vocabulary — the root of a central value and the idempotent stated once for a general product — is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**The twelve names.** The space carries twelve products, the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and their eight symmetric and antisymmetric parts (*The 12 Products of the Biquaternion Complex Space*). Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first slot is read through the natural conjugation; the third is the family, $\mathrm A$ the algebra over $\mathbb{C}$ and $\mathrm S$ the sesqualgebra, whose second slot carries the Hermitian conjugation. The twelve are read in the four families and the three operations of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,

| the operation | the plain algebra | the plain sesqualgebra | the quaternionic algebra | the quaternionic sesqualgebra |
|---|---|---|---|---|
| the general | $\mathrm{GPA}$ | $\mathrm{GPS}$ | $\mathrm{GQA}$ | $\mathrm{GQS}$ |
| the symmetric | $\mathrm{SPA}$ | $\mathrm{SPS}$ | $\mathrm{SQA}$ | $\mathrm{SQS}$ |
| the antisymmetric | $\mathrm{APA}$ | $\mathrm{APS}$ | $\mathrm{AQA}$ | $\mathrm{AQS}$ |

and every table of the article follows the new order: the four general structures first, then their four symmetric parts, then their four antisymmetric parts; and inside each group the plain algebra, then the plain sesqualgebra, then the quaternionic algebra, then the quaternionic sesqualgebra.

**Scope and owners.** This article owns the value $+1$ in the twelve structures, the halving map, the idempotent sets of the twelve structures, the comparison of the four idempotent sets and the position of the families in the remarkable subspaces. The root set of each structure stays owned by its article *Square Roots of One and the Idempotents of the …*, cited one by one in §*The Twelve Structures and the Roots of One*; the four-set table is *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*; the vocabulary is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the products and the names are *The 12 Products of the Biquaternion Complex Space* and *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the cone and the zero-divisor sets are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the invertibility criterion is *Norm and Invertibility in the General Quaternionic Algebra*; the group of the second product's root of $+1$ is *The Unitary Group of the Biquaternion Algebra*; the Peirce decomposition is *Ideals and Peirce Decomposition of the General Plain Algebra*; and the square-zero sets named here are *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{B}$ has basis $e_0,e_1,e_2,e_3$ over $\mathbb{C}$ with $e_1e_2=e_3$; the central imaginary is $i$, with $i^{2}=-e_0$ and $i$ commuting with every element; a general element is $\tilde\Xi=\Xi_0e_0+\vec\Xi$ with $\Xi_0\in\mathbb{C}$ and $\vec\Xi=\sum_k\Xi_ke_k$. The natural conjugation is $\tilde\Xi^{\natural}=\Xi_0-\vec\Xi$, the star is $\tilde\Xi^{*}=\overline{\tilde\Xi^{\natural}}$, the coefficientwise conjugation is $\overline{\tilde\Xi}$, the **central square** is $C(\tilde\Xi)e_0=\tilde\Xi^{\natural}\tilde\Xi=\tilde\Xi\tilde\Xi^{\natural}$ with $C(\tilde\Xi)=\sum_\mu\Xi_\mu^{2}$, the **Hermitian square** is $H(\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$, and the **Krein value** is $\Delta(\tilde\Xi)=\lvert\Xi_0\rvert^{2}-\sum_k\lvert\Xi_k\rvert^{2}$. A **central value** is an element $\lambda e_0$ with $\lambda\in\mathbb{C}$, and $\hat u$ is a real unit vector, of square $-e_0$ and of bilinear square $(\hat u,\hat u)=1$. The **halving map** is $\tilde\Xi\mapsto\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$, of inverse $\tilde\Xi=2\tilde\Pi-e_0$, the square in the map being the square of the general plain bilinear product. The root is defined in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*Powers, the Square and the Roots* as a **non-zero** element with $\tilde\Xi\star\tilde\Xi=\lambda e_0$; a root set is read here as a solution set, so the origin is counted with the roots of $0$ of §*The Twelve Structures and the Roots of One*, and at the value $+1$ the convention changes nothing, the origin being no root of it.

## The Roots of One

**Definition (the root of a central value; quoted).** Let $\star$ be a product on $\mathbb{B}$, let $\lambda\in\mathbb{C}$ and let $\tilde\Xi\in\mathbb{B}$. The element is a **root of $\lambda e_0$ of $\star$** when $\tilde\Xi\star\tilde\Xi=\lambda e_0$, and the **root set** of the value is the set of the solutions (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*Powers, the Square and the Roots*). The definition names its product, and every statement below names the product it reads.

### The Five Squares and the Twelve Structures

The square of a structure is its operation read at the two equal arguments, so the twelve structures are read from their squares, and the squares are five.

| the square | the structures | at the two equal arguments |
|---|---|---|
| the plain square | $\mathrm{GPA}$, $\mathrm{SPA}$ | $\tilde\Xi^{2}=\bigl(\Xi_0^{2}-(\vec\Xi,\vec\Xi)\bigr)e_0+2\Xi_0\vec\Xi$ |
| the Hermitian square | $\mathrm{GPS}$, $\mathrm{SPS}$ | $\tilde\Xi\tilde\Xi^{*}$, of scalar part $H$, the scalar part alone for $\mathrm{SPS}$ |
| the central square | $\mathrm{GQA}$, $\mathrm{SQA}$ | $C(\tilde\Xi)e_0$ |
| the sesquilinear square | $\mathrm{GQS}$, $\mathrm{SQS}$ | $\tilde\Xi^{\natural}\tilde\Xi^{*}$, of scalar part $\Delta$, the coefficientwise real part alone for $\mathrm{SQS}$ |
| the vanishing square | $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$ | $0$ on the two bilinear structures, a pure element on the two sesquilinear ones |

The five squares are read from *The 12 Products of the Biquaternion Complex Space* and the four group articles: the $\mathrm{SPS}$ square is the central element $\mathrm{Sc}(\tilde\Xi\tilde\Xi^{*})e_0$ (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*), and the $\mathrm{SQS}$ square is the coefficientwise real part of $\tilde\Xi^{\natural}\tilde\Xi^{*}$, a real element and not the central square of $\mathrm{GQS}$ (*The Square of the General Quaternionic Sesquilinear Product and the Two Halves*). The square of $\mathrm{SPA}$ is the plain square, the product being the Jordan product $\tfrac12(\tilde\Xi\tilde Q+\tilde Q\tilde\Xi)$, and the square of $\mathrm{SQA}$ is the central square.

### The Value One in the Four General Products

**Theorem (the four root sets of the value one).** At the value $+1$ the four general products have four different root sets:

| the product | the roots of $+1$ |
|---|---|
| $\mathrm{GPA}$, $\tilde\Xi\tilde Q$ | the central pair $\pm e_0$, and the pure elements with $(\vec\Xi,\vec\Xi)=-1$, a family of real dimension four |
| $\mathrm{GPS}$, $\tilde\Xi\tilde Q^{*}$ | the family $\{\tilde\Xi:\tilde\Xi\tilde\Xi^{*}=e_0\}$, the group of the linear maps preserving the Hermitian form, of real dimension four |
| $\mathrm{GQA}$, $\tilde\Xi^{\natural}\tilde Q$ | the quadric $C(\tilde\Xi)=+1$, of real dimension six |
| $\mathrm{GQS}$, $\tilde\Xi^{\natural}\tilde Q^{*}$ | the family $c(\hat u+it)$ at the slopes $\lvert t\rvert>1$ with $(t^{2}-1)\lvert c\rvert^{2}=1$, and the central circle $\lvert a\rvert^{2}=1$, of real dimension four |

The four descriptions are the four reductions of *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Four General Products at a General Value*, read at $\lambda=+1$: the pair and the pure quadric, the family of the linear maps preserving the form, the level set of $C$, and the two pieces of the fourth product. **The word here is *differ*, not *coincide*.** The four zero-divisor sets of the four general products are one set read four times, because the four products read the same norm; the four root sets are not, because the square of a product is not the norm of a product, even at the value $+1$ where the four sets are as near as they come. The plain set carries the pure quadric $(\vec\Xi,\vec\Xi)=-1$, on which $C=-1$; the second set is the family $\tilde\Xi\tilde\Xi^{*}=e_0$, which is a group; the third set is the quadric $C=+1$; and the fourth is the union of a slope family and a circle, which is not.

**The reading in the algebra.** For the four general products a root of $+1$ is a root of a non-zero central value, hence a unit of the algebra, by the theorem of *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Roots Are Units, or Zero Divisors*; the relation is $\mathcal R_{+1}\subseteq\mathbb{B}^{\times}$. The plane roots of the plain product are units and not zero divisors: they are pure, and the central square of a pure element is $-(\vec\Xi,\vec\Xi)e_0=C(\tilde\Xi)e_0$, equal to $e_0$ at a root of $+1$ and never zero. The reading fails for the two symmetric sesquilinear structures outside the four general products, where a root of $+1$ may lie on the cone: the witness $\tfrac{1}{\sqrt2}(e_1+ie_2)$ is a root of $+1$ in $\mathrm{SPS}$ with $C=0$, hence a zero divisor of the algebra and not a unit.

### The Existence at the Value One

Two mechanisms remove the root of $+1$ from a structure, and they are the two of *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Four Existence Classes* read at $+1$.

**Theorem (the existence at the value one; quoted).** A root of $+1$ exists for the four bilateral structures $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{SPA}$, $\mathrm{SQA}$ and for the two indefinite sesquilinear structures $\mathrm{GQS}$, $\mathrm{SQS}$; it exists for neither of the two definite sesquilinear structures $\mathrm{GPS}$, $\mathrm{SPS}$ at a negative real value, while the value $+1$ is reached there; and it does not exist for the four antisymmetric structures $\mathrm{APA}$, $\mathrm{APS}$, $\mathrm{AQA}$, $\mathrm{AQS}$, whose square takes the central value $0$ alone. The two definite sesquilinear structures reach the negative real values nowhere, because their square has non-negative scalar part, $H$ for $\mathrm{GPS}$ and the same scalar part for $\mathrm{SPS}$; the four antisymmetric structures read no central value other than $0$, their square vanishing on the two bilinear ones and being a pure element on the two sesquilinear ones.

### The Two Families of the Plain Reduction

The plain square is the plain reduction $\Xi_0^{2}-(\vec\Xi,\vec\Xi)=\lambda$ with $2\Xi_0\vec\Xi=0$, and the second equation cuts the space into two families.

**Definition.** An element is **pure** when its scalar part vanishes, $\Xi_0=0$, and **central** when its vector part vanishes, $\vec\Xi=0$.

At the value $+1$ the two families carry the two pieces of the root set.

| | pure, $\Xi_0=0$ | central, $\Xi_0\neq0$ |
|---|---|---|
| the reduction $2\Xi_0\vec\Xi=0$ | satisfied identically | forces $\vec\Xi=0$ |
| the roots of $+1$ | the quadric $(\vec\Xi,\vec\Xi)=-1$, four parameters | the pair $\pm e_0$ |
| the real dimension | $4$ | the two points |

The pure roots of $+1$ of the plain product are the quadric of the vector subspace, of real dimension four: writing $\vec\Xi=\vec p+i\vec p'$ over two real vectors, they are the pairs with $\vec p^{2}-\vec p'^{2}=-1$ and $\vec p\cdot\vec p'=0$, and they contain the purely imaginary unit vectors $\tilde\Xi$. The central pair $\pm e_0$ is the other piece, and the two pieces are disjoint.

### The Inverse Equations at One

**Theorem (the inverse equations at the value one).** Let $\star$ be one of the four general products and let $\tilde\Xi$ be a root of $+1$ of $\star$. Then each of the two equations

$$
\tilde\Xi\star\tilde X=e_0 , \qquad \tilde X\star\tilde\Xi=e_0
$$

has a solution, the inverse $\tilde\Xi^{-1}=\tilde\Xi^{\natural}/C(\tilde\Xi)$ for the plain product and one of the conjugated inverses of the one-sided table for the other three (*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The One-Sided Inverse Equations*). A root of the value $0$ has no solution on either side, and that vanishing is read with the value $0$ in *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

The value $+1$ is therefore the value at which the roots of the plain product are invertible with the explicit inverse $\tilde\Xi^{-1}=\tilde\Xi^{\natural}$, the central square being $e_0$ there: the pure roots of $+1$ have $C=e_0$, and the central pair has $C=e_0$ at $+e_0$ and $C=e_0$ at $-e_0$ as well, the central square of $-e_0$ being $e_0$.

The root sets of the value $-1$ are not read here. In the six bilinear structures the multiplication by the central imaginary flips the value of the square, $(i\tilde\Xi)\star(i\tilde\Xi)=-\tilde\Xi\star\tilde\Xi$, so the root set of $-1$ there is the $i$-multiple of the root set of $+1$, and that is the whole of its theory; the mechanism is not universal, since a scalar multiplication in a sesquilinear product returns $\lvert\hat u\rvert^{2}$ times the square and cannot flip a sign, so the root set of $-1$ there is the empty set for the two definite sesquilinear structures and the owner's set for the two indefinite ones; and the four antisymmetric structures read no signed value at all, their square vanishing or being pure. Nothing below this paragraph uses the value $-1$.

## The Twelve Structures and the Roots of One

The twelve root sets of $+1$ are read one by one, each quoted from the article that owns it. The product, the square and the root set are named for each, and the two structures with the same square have the same root set.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde\Xi\tilde Q$, and its square is the plain square, of scalar part $\Xi_0^{2}-(\vec\Xi,\vec\Xi)$ and vector part $2\Xi_0\vec\Xi$. The roots of $+1$ are the central pair $\pm e_0$ and the pure quadric $(\vec\Xi,\vec\Xi)=-1$ of real dimension four, which contains the purely imaginary unit vectors $\tilde\Xi$. The article is *Square Roots of One and the Idempotents of the General Plain Algebra*.

### $\mathrm{GPS}$, the general plain sesqualgebra

The product is $\tilde\Xi\tilde Q^{*}$, and its square is the Hermitian element $\tilde\Xi\tilde\Xi^{*}$, of scalar part $H(\tilde\Xi)$. The roots of $+1$ are the unitary family $\{\tilde\Xi:\tilde\Xi\tilde\Xi^{*}=e_0\}$, the group of the linear maps preserving the Hermitian form, of real dimension four, described as the family $e^{i\theta}w$ over the real unit quaternions $w$; it contains $e_0$, $-e_0$ and the purely imaginary unit vectors $\tilde\Xi$. **The negative values are reached nowhere**, the scalar part $H$ being non-negative. The article is *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\Xi^{\natural}\tilde Q$, and its square is the central square $C(\tilde\Xi)e_0$, so the equation of the value $+1$ is the single complex equation $C(\tilde\Xi)=1$. The root set is the quadric $C=+1$ of real dimension six, containing the central pair $\pm e_0$ and the real unit vectors $\hat u$. The article is *Square Roots of One and the Idempotents of the General Quaternionic Algebra*.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra

The product is $\tilde\Xi^{\natural}\tilde Q^{*}$, and its square has scalar part the Krein value $\Delta(\tilde\Xi)$, real for every element. The roots of $+1$ are the family $c(\hat u+it)$ at the slopes $\lvert t\rvert>1$, with $\lvert c\rvert^{2}=1/(t^{2}-1)$, of real dimension four, beside the central circle $\lvert a\rvert^{2}=1$; they contain $e_0$ and $i$, and the three intervals of the slope carry the three root sets of the structure, the middle one, $\lvert t\rvert=1$, carrying the cone $c(\hat u\pm i)$ of the roots of $0$. The article is *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\Xi\bullet\tilde Q=\tfrac12(\tilde\Xi\tilde Q+\tilde Q\tilde\Xi)$, and its square is the plain square, $\tilde\Xi\bullet\tilde\Xi=\tilde\Xi^{2}$; the root set of $+1$ is therefore that of $\mathrm{GPA}$, element for element. The article is *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra

The product is the symmetrisation $\tfrac12(\tilde\Xi\tilde Q^{*}+\overline{\tilde Q\tilde\Xi^{*}})$, whose value is central, and its square is $H(\tilde\Xi)e_0$; the equation is the single real equation $H(\tilde\Xi)=1$. The root set of $+1$ is the quadric $H=1$, that is the set $\sum_\mu\lvert\Xi_\mu\rvert^{2}=1$ in $\mathbb{C}^{4}$, of real dimension seven. **The negative values are reached nowhere**, for the same definiteness; and the root set of $+1$ is not the group of $\mathrm{GPS}$ but the quadric of the Hermitian square above it, the symmetrisation reading the scalar part of the square alone. The article is *Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q+\tilde Q^{\natural}\tilde\Xi)=C(\tilde\Xi,\tilde Q)e_0$, the form read as a product, and its square is the central square; the root set of $+1$ is the same quadric $C=+1$ as that of $\mathrm{GQA}$, of real dimension six. The article is *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra

The product is the symmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde\Xi^{*}})$, and its square is the coefficientwise real part of the unsplit square, a real element. The roots of $+1$ are the family $\mathcal R_{+1}$ of the owner, with $\lvert\alpha\rvert\geq1$, of real dimension four, containing $e_0$; the three root sets of the structure are pairwise disjoint, and the idempotents $-\tfrac12e_0+\hat u$ of §*The Idempotents* lie on none of them. The article is *Square Roots of One and the Idempotents of the Symmetric Quaternionic Sesqualgebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\Xi\wedge\tilde Q=\tfrac12(\tilde\Xi\tilde Q-\tilde Q\tilde\Xi)=\vec\Xi\times\vec Q$, alternating, so its square vanishes at the two equal arguments and the equation of the value $+1$ reads $0=e_0$. **There is no root of $+1$**, the value $0$ alone being read by the vanishing square. The article is *Square Roots of One and the Idempotents of the Antisymmetric Plain Algebra*.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra

The product is the antisymmetrisation $\tfrac12(\tilde\Xi\tilde Q^{*}-\overline{\tilde Q\tilde\Xi^{*}})$, whose values are pure elements, so the square never takes a central value. **There is no root of $+1$**, the obstruction being the purity of the value and not the vanishing of the square. The article is *Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde\Xi\wedge^{\natural}\tilde Q=\tfrac12(\tilde\Xi^{\natural}\tilde Q-\tilde Q^{\natural}\tilde\Xi)$, alternating, so its square vanishes and the equation reads $0=e_0$. **There is no root of $+1$.** The article is *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Algebra*.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra

The product is the antisymmetrisation $\tfrac12(\tilde\Xi^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde\Xi^{*}})$, whose values are pure elements, so the square never takes a central value. **There is no root of $+1$**, the unit of the parent algebra being the witness, its square under the block being zero. The article is *Square Roots of One and the Idempotents of the Antisymmetric Quaternionic Sesqualgebra*.

## The Idempotents

The idempotent is the second face of the roots of $+1$: the two are in bijection through the halving map, and everything read below rests on the roots of $+1$ alone.

**Definition (the idempotent; quoted).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi ,
$$

the equation naming the product, and the **idempotent set** of the structure is the set of the solutions (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*The Idempotent, the Projection and the Peirce Decomposition*). The equation is the algebraic form of a projection, and throughout this section the product is named in every statement; unqualified, an idempotent of an element of $\mathbb{B}$ means an idempotent of the general plain bilinear product, the multiplication of the algebra.

### The Halving Map

**Theorem (the halving map).** Let $\tilde\Pi\in\mathbb{B}$, let $\tilde\Xi=2\tilde\Pi-e_0$, and read both squares in the general plain bilinear product. Then $\tilde\Pi^{2}=\tilde\Pi$ exactly when $\tilde\Xi^{2}=e_0$. The map $\tilde\Xi\mapsto\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ is therefore a bijection from the roots of $+1$ of the plain product onto the idempotents of the plain product, of inverse $\tilde\Pi\mapsto\tilde\Xi=2\tilde\Pi-e_0$; the complementary pair $\tilde\Pi$, $e_0-\tilde\Pi$ corresponds to the pair $\tilde\Xi$, $-\tilde\Xi$; and the equation $\tilde\Xi^{2}=e_0$ is the only equation the map needs.

*Proof.* The idempotent equation reads $\tilde\Pi^{2}=\tfrac14(e_0+2\tilde\Xi+\tilde\Xi^{2})=\tfrac12(e_0+\tilde\Xi)=\tilde\Pi$, that is $\tilde\Xi^{2}=e_0$, and the two maps are inverse to each other. For the complement, $e_0-\tilde\Pi=\tfrac12(e_0-\tilde\Xi)$ is the image of $-\tilde\Xi$, which is a root of $+1$ with $\tilde\Xi$.

The map is the plain product's, and the idempotent sets of the other structures are read from their own equations; the two sesquilinear families of §*The Two Quadrics of the Two Sesquilinear Products* are the plain family's Hermitian part for one of them and the owner's displaced family for the other.

### The Five Structures with a Nontrivial Idempotent

**Theorem (the five structures with a nontrivial idempotent).** Among the twelve structures of the biquaternion complex space an idempotent other than $0$ and $e_0$ exists exactly for $\mathrm{GPA}$, $\mathrm{GPS}$, $\mathrm{GQS}$, $\mathrm{SPA}$ and $\mathrm{SQS}$. The four antisymmetric structures have the origin alone; the three structures with a scalar-valued square, $\mathrm{GQA}$, $\mathrm{SPS}$ and $\mathrm{SQA}$, have the trivial pair; and the idempotent sets of $\mathrm{GQS}$ and $\mathrm{SQS}$ coincide.

*Proof.* On the two bilinear antisymmetric structures the square vanishes at the two equal arguments, so the equation forces the origin and excludes $\mathrm{APA}$ and $\mathrm{AQA}$. On the two antisymmetric sesquilinear structures the square is a pure element, so an idempotent has a vanishing scalar part; the conjugate-alternation $\tilde X\wedge\tilde Y=-\overline{\tilde Y\wedge\tilde X}$ of the two blocks makes the square of an element purely imaginary, so an idempotent there is pure and purely imaginary, $\tilde\Pi=i\vec q$ over a real vector $\vec q$; its vector part $i\vec q$ is a complex multiple of the real direction $\vec q$, so the diagonal vanishes by the criterion of the owner (*The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*), the equation reads $i\vec q=0$, and the origin is the only solution; this excludes $\mathrm{APS}$ and $\mathrm{AQS}$. On $\mathrm{GQA}$, $\mathrm{SQA}$ and $\mathrm{SPS}$ the square is the central value $C(\tilde\Pi)e_0$, or $\mathrm{Sc}(\tilde\Pi\tilde\Pi^{*})e_0$ for the third, so an idempotent is central, $\tilde\Pi=qe_0$ with $q\in\mathbb{C}$, and the equation on the centre leaves $q=\lvert q\rvert^{2}\in\{0,1\}$ for the sesquilinear one and $q=q^{2}\in\{0,1\}$ for the two bilinear ones; this leaves the trivial pair. The five remaining rows are the theorem of §*The Plain Family and its Three Parts* together with the identity $\tilde\Pi\bullet\tilde\Pi=\tilde\Pi^{2}$ for $\mathrm{SPA}$, whose idempotents are the algebra's own; and for $\mathrm{SQS}$, whose square is a real element, the equation forces $\tilde\Pi$ real and reduces to $(\tilde\Pi^{\natural})^{2}=\tilde\Pi$, the set of the owner *Square Roots of One and the Idempotents of the Symmetric Quaternionic Sesqualgebra*.

The classification reads the ways a square operator differs from the plain square. The antisymmetric square destroys the equation, being identically zero on the two bilinear structures and a purely imaginary pure element on the two sesquilinear ones. The scalar-valued square returns a central element, so an idempotent is central and only the trivial pair survives. The symmetric plain square is the plain square itself, so $\mathrm{SPA}$ carries the whole plain family although it is not associative, and it does carry the unit $e_0$. The three structures that keep a family beyond the trivial pair are those whose square is neither identically zero nor scalar-valued: $\mathrm{GPS}$ with the Hermitian family, and $\mathrm{GQS}$ and $\mathrm{SQS}$ with the family displaced to $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$, the two families of §*The Two Quadrics of the Two Sesquilinear Products*.

### The Plain Family and its Three Parts

**Theorem (the plain family; quoted).** The idempotents of $\mathbb{B}$ are $0$, $e_0$, and the elements $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ over the roots $\tilde\Xi$ of $+1$ of the plain product; the halving map is a bijection from the roots of $+1$ onto the set; and the complementary pair is $\{\tfrac12(e_0+\tilde\Xi),\ \tfrac12(e_0-\tilde\Xi)\}$ (*Square Roots of One and the Idempotents of the General Plain Algebra*).

The classification of the roots of $+1$ organises the family in three parts, and each part has its own kind.

| the part of the roots of $+1$ | the idempotents |
|---|---|
| the central pair $\pm e_0$ | the trivial pair $0$, $e_0$ |
| the purely imaginary unit vectors $\tilde\Xi$ | the Hermitian family $\tfrac12(e_0+\tilde\Xi)$, of real dimension two |
| the non-trivial roots $\vec p+i\vec p'$, $\vec p^{2}-\vec p'^{2}=-1$, $\vec p\cdot\vec p'=0$ | the non-trivial family, four parameters |

The **Hermitian** family is the family the general plain sesquilinear product keeps, and it is a subfamily of the plain family, reached by the purely imaginary roots of $+1$. The **non-trivial** family is the largest part of the plain idempotent set: writing the root $\tilde\Xi=\vec p+i\vec p'$, the idempotent is $\tilde\Pi=\tfrac12(e_0+\vec p)+\tfrac12 i\vec p'$, whose vector part $\tfrac12(\vec p+i\vec p')$ carries both a real and an imaginary term, so the element is neither Hermitian nor anti-Hermitian and lies in no remarkable subspace. The two parts are related by the same formula and are not the same family.

### The Two Quadrics of the Two Sesquilinear Products

Beyond the trivial pair the two sesquilinear structures carry one family each, and the two families are different quadrics read off the real directions.

**Proposition (the two families).** The idempotents of the general plain sesquilinear product beyond the trivial pair are the Hermitian idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ over the real unit vectors $\hat u$, a family lying in $\mathbb{M}_+$; the idempotents of the general quaternionic sesquilinear product beyond the trivial pair are the elements $\tilde\Pi(\hat u)=-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$ over the real vectors $\hat u$ with $(\hat u,\hat u)=1$, a family lying in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and the set of $\mathrm{SQS}$ is the same set.

*Proof.* The first is *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*: applying ${}^{*}$ to $\tilde Q\tilde Q^{*}=\tilde Q$ shows $\tilde Q$ Hermitian, so the equation is $\tilde Q^{2}=\tilde Q$, and the Hermitian roots of that equation are the displayed ones; the Hermitian subfamily of the plain family is exactly this family, the purely imaginary roots of $+1$ being the $\hat u i$. The second is *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*: inside the quaternion subspace, where a real element has $\tilde Q^{*}=\tilde Q^{\natural}$, the equation $\tilde Q^{\natural}\tilde Q^{*}=\tilde Q$ becomes $(\tilde Q^{\natural})^{2}=\tilde Q$, whose solutions are the displayed ones; the argument for $\mathrm{SQS}$ is the same in the other order, its square being the coefficientwise real part of $\tilde Q^{\natural}\tilde Q^{*}$.

A real vector $\hat u$ with $(\hat u,\hat u)=1$ is $\tfrac{\sqrt3}{2}\hat u$ for a real unit vector $\hat u$, so the second family is the quadric $(\hat u,\hat u)=1$ of the real vectors, written about the point $-\tfrac12e_0$, while the first is the family about the point $+\tfrac12e_0$ with the purely imaginary parameter $\tilde\Xi$: two quadrics of the same real dimension two, of different points and different definitions, and neither is the image of the other under the parameter change. The first is the set of the Hermitian idempotents, the second the set of the real idempotents with scalar part $-\tfrac12$, and the antipode $\hat u\mapsto-\hat u$ is the complementation on the first while the map $\hat u\mapsto-\hat u$ sends the second to $\tfrac12e_0-\hat u$, which is not a member of it.

### The Central Square of an Idempotent

The central square is the invariant that separates the four idempotent sets, the second-order invariant of the plain product.

**Theorem (the central square of an idempotent).** On the idempotent sets the central square takes the values

| idempotent | central square |
|---|---|
| $0$ | $0$ |
| $e_0$ | $e_0$ |
| $\tfrac12(e_0+\tilde\Xi)$ over a root of $+1$ of the plain product, the Hermitian $\tfrac12(e_0+\tilde\Xi)$ included | $0$ |
| $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$, $(\hat u,\hat u)=1$ | $e_0$ |

*Proof.* For the plain family the root of $+1$ other than $\pm e_0$ is pure, so $\tilde\Xi^{\natural}=\tilde\Xi$ and the central square of $\tfrac12(e_0+\tilde\Xi)$ is $\tfrac14(e_0-\tilde\Xi)(e_0+\tilde\Xi)=\tfrac14(e_0-\tilde\Xi^{2})=0$; the Hermitian idempotents are the members of the family at a purely imaginary root, and the computation is the same. For the displaced family the idempotent is real, so $\tilde\Pi^{\natural}=-\tfrac12e_0-\tfrac{\sqrt3}{2}\hat u$, and $\tilde\Pi^{\natural}\tilde\Pi=\tfrac14e_0-\hat u^{2}=\tfrac14e_0+(\hat u,\hat u)e_0=e_0$, the square $\hat u^{2}$ of a real vector being $-(\hat u,\hat u)e_0$; the idempotence criterion of the owner is the plain square in the other order, $\tilde\Pi\tilde\Pi^{\natural}=\tilde\Pi$, which is a different equation.

Zero for the two families of zero divisors, $e_0$ for the unit and the displaced family: the central square decides which idempotents are units of the algebra and which are not, and it decides the plain family and the displaced family in opposite directions. The Hermitian idempotents are therefore null for the central square of the algebra although they are the pure states of the sesqualgebra, the two notions being different objects.

### The Units and the Zero Divisors Among the Idempotents

**Theorem (the units and the zero divisors among the idempotents).** Among the idempotents of the structures, the units of the algebra are $e_0$ and the displaced family $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$; the zero divisors of the algebra are the members of the plain family $\tfrac12(e_0+\tilde\Xi)$ beyond the trivial pair, the Hermitian ones included, and no other idempotent; and the origin is neither a unit nor a zero divisor.

*Proof.* The values of the central square are the previous theorem, and the criterion of invertibility is that the central square not vanish (*Norm and Invertibility in the General Quaternionic Algebra*).

The theorem is the sharpest separation of the sets. The trivial pair carries the unit $e_0$, so the smallest set, that of the natural product, has no zero divisor at all. The plain product and the general plain sesquilinear product have nontrivial idempotents, and every one of them is a zero divisor; the non-trivial plain family is a part of the zero-divisor cone that no other structure's idempotents reach. The displaced family is the only family of idempotents whose members are units, and it is a family of the general quaternionic sesquilinear product alone.

### The Antipodal Idempotent

**Proposition (the antipodal idempotent).** Let $\tilde\Pi$ be an idempotent of the plain product. Then $e_0-\tilde\Pi$ is an idempotent of the plain product, the two are orthogonal, $\tilde\Pi(e_0-\tilde\Pi)=0$, and they sum to $e_0$. On the parameter set the map is $\tilde\Xi\mapsto-\tilde\Xi$, and $\hat u\mapsto-\hat u$ on the Hermitian subfamily.

*Proof.* $(e_0-\tilde\Pi)^{2}=e_0-2\tilde\Pi+\tilde\Pi^{2}=e_0-\tilde\Pi$ and $\tilde\Pi(e_0-\tilde\Pi)=\tilde\Pi-\tilde\Pi^{2}=0$; the halving map sends $\tilde\Xi$ to $\tfrac12(e_0+\tilde\Xi)$ and $-\tilde\Xi$ to $\tfrac12(e_0-\tilde\Xi)$.

The complementation is available for the two products whose idempotent family it preserves: the plain product, whose whole family it pairs, and the general plain sesquilinear product, whose Hermitian family it pairs as the antipode of the unit vectors. It is not available for the displaced family, which the map $\hat u\mapsto-\hat u$ fails to preserve, and for the structures whose set is the trivial pair it is the exchange of the two members. The orthogonality is the display the Peirce decomposition needs, and it needs bilinearity and the unit alone, not associativity.

### The Position in the Remarkable Subspaces

**Theorem (the position of the families).** The trivial pair lies in the centre $\mathbb{C}_{\mathbb{B}}$. The Hermitian family lies in $\mathbb{M}_+$, the space of the elements with a real scalar part and a purely imaginary vector part, and in no other four-dimensional subspace. The displaced family lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and in no other four-dimensional subspace. The non-trivial plain family lies in none of the four four-dimensional subspaces.

*Proof.* The elements $0$ and $e_0$ are complex multiples of the unit, hence central. For $\tfrac12(e_0+\tilde\Xi)$ the scalar part is real and the vector part is purely imaginary, which is the definition of $\mathbb{M}_+$; the element is not pure, its scalar part is not purely imaginary, so it is not in $\mathbb{M}_-$ nor in $i\mathbb{H}_{\mathbb{B}}$, and its vector part is not real, so it is not in $\mathbb{H}_{\mathbb{B}}$. For $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$ the coefficients are real, so the element is in $\mathbb{H}_{\mathbb{B}}$; its scalar part is real and non-zero, so it is not anti-Hermitian, and its vector part is real and non-zero, so it is not Hermitian. For the non-trivial $\tilde\Pi=\tfrac12(e_0+\vec p)+\tfrac12 i\vec p'$ the vector part carries both a real term and an imaginary term and the scalar part is real, so the element is neither Hermitian, nor anti-Hermitian, nor pure, nor real.

The four sets therefore occupy four different regions: the centre for the trivial pair, $\mathbb{M}_+$ for the Hermitian family, $\mathbb{H}_{\mathbb{B}}$ for the displaced family, and no distinguished region at all for the non-trivial family, which is the point of its name. The restrictions of the products to these subspaces are *Remarkable Subspaces and the Four General Products*.

### The Peirce Data

**Theorem (the Peirce decomposition is the plain product's own).** For an idempotent $\tilde\Pi$ of the plain product the algebra splits as $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_0-\tilde\Pi)$, and the two summands are left ideals. For the idempotents of the other structures no such decomposition is available, because the products are not associative, and it is the associativity that turns the Peirce corners into ideals.

*Proof.* The decomposition and the ideal structure are *Ideals and Peirce Decomposition of the General Plain Algebra*; the display $\tilde\Pi(e_0-\tilde\Pi)=0$ of §*The Antipodal Idempotent* is the orthogonality the decomposition needs, and the associativity of the plain product is what makes the summands $\mathbb{B}\tilde\Pi$ and $\mathbb{B}(e_0-\tilde\Pi)$ left ideals, which the other three products fail.

The comparison ends with the two readings of the idempotent. The Hermitian idempotents of the general plain sesquilinear product act as projections on the positive cone and on the Hermitian module (*Square Roots of One and the Idempotents of the General Plain Sesqualgebra*), and the displaced family is the family of idempotents of the fourth product whose central square is $e_0$; the natural product has the trivial pair alone.

## Results

The three tables below collect the root sets of $+1$, the idempotent sets of the twelve structures and the halving map.

### The Twelve Root Sets at the Value One

| the family | the structure | the square | the roots of $+1$ |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\tilde\Xi^{2}$ | the pair $\pm e_0$ and the pure quadric $(\vec\Xi,\vec\Xi)=-1$, real dimension $4$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\tilde\Xi\tilde\Xi^{*}$ | the family $\tilde\Xi\tilde\Xi^{*}=e_0$, real dimension $4$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $C(\tilde\Xi)e_0$ | the quadric $C=+1$, real dimension $6$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | of scalar part $\Delta$ | the slopes $\lvert t\rvert>1$ and the central circle, real dimension $4$ |
| the plain algebra | $\mathrm{SPA}$ | $\tilde\Xi^{2}$ | the two sets of $\mathrm{GPA}$ |
| the plain sesqualgebra | $\mathrm{SPS}$ | $H(\tilde\Xi)e_0$ | the quadric $H=1$ in $\mathbb{C}^{4}$, real dimension $7$ |
| the quaternionic algebra | $\mathrm{SQA}$ | $C(\tilde\Xi)e_0$ | the quadric $C=+1$, real dimension $6$ |
| the quaternionic sesqualgebra | $\mathrm{SQS}$ | the coefficientwise real part | the family $\mathcal R_{+1}$ with $\lvert\alpha\rvert\geq1$, real dimension $4$ |
| the plain algebra | $\mathrm{APA}$ | $0$ | none |
| the plain sesqualgebra | $\mathrm{APS}$ | a pure element | none |
| the quaternionic algebra | $\mathrm{AQA}$ | $0$ | none |
| the quaternionic sesqualgebra | $\mathrm{AQS}$ | a pure element | none |

Read against the empty set, the table has two kinds of entry: the value $+1$ is refused by the four antisymmetric structures, whose square vanishes or is pure; and the value $+1$ is read by the other eight rows, the plain pair and the pure quadric, the group of the second product and the quadric $H=1$ of its symmetrisation, the quadric of $C$, and the two families of the fourth product and its symmetrisation.

### The Twelve Idempotent Sets

| structure | the square $\tilde\Pi\star\tilde\Pi$ | the idempotents |
|---|---|---|
| $\mathrm{GPA}$ | $\tilde\Pi^{2}$ | $0$, $e_0$, $\tfrac12(e_0+\tilde\Xi)$ over the roots $\tilde\Xi$ of $+1$ |
| $\mathrm{GPS}$ | $\tilde\Pi\tilde\Pi^{*}$ | $0$, $e_0$, $\tfrac12(e_0+\tilde\Xi)$ |
| $\mathrm{GQA}$ | $C(\tilde\Pi)e_0$ | $0$, $e_0$ |
| $\mathrm{GQS}$ | $\tilde\Pi^{\natural}\tilde\Pi^{*}$ | $0$, $e_0$, $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$ with $(\hat u,\hat u)=1$ |
| $\mathrm{SPA}$ | $\tilde\Pi^{2}$, the plain square | the same set as $\mathrm{GPA}$ |
| $\mathrm{SPS}$ | $\mathrm{Sc}(\tilde\Pi\tilde\Pi^{*})e_0$, real and $\geq 0$ | $0$, $e_0$ |
| $\mathrm{SQA}$ | $C(\tilde\Pi)e_0$ | $0$, $e_0$ |
| $\mathrm{SQS}$ | $\tfrac12(\tilde\Pi^{\natural}\tilde\Pi^{*}+\overline{\tilde\Pi^{\natural}\tilde\Pi^{*}})$ | $0$, $e_0$, $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$ with $(\hat u,\hat u)=1$ |
| $\mathrm{APA}$ | $0$ | $0$ alone |
| $\mathrm{APS}$ | $\tfrac12(\tilde\Pi\tilde\Pi^{*}-\overline{\tilde\Pi\tilde\Pi^{*}})$ | $0$ alone |
| $\mathrm{AQA}$ | $0$ | $0$ alone |
| $\mathrm{AQS}$ | $\tfrac12(\tilde\Pi^{\natural}\tilde\Pi^{*}-\overline{\tilde\Pi^{\natural}\tilde\Pi^{*}})$ | $0$ alone |

Read by column, the table has three kinds of entry: the origin, present in all twelve rows; the unit, present in the eight rows that are not antisymmetric; and the families beyond the trivial pair, present in the five rows of §*The Five Structures with a Nontrivial Idempotent*. The two rows that carry the displaced family are the general quaternionic sesquilinear structure and its symmetrisation, and the two rows that carry the plain family are the general plain structure and its symmetrisation. The four sets themselves are tabulated in *Comparison Between the Four General Products*.

### The Three Parts of the Halving Map

| the root of $+1$ of the plain product | the idempotent $\tfrac12(e_0+\tilde\Xi)$ |
|---|---|
| the central pair $\pm e_0$ | the trivial pair $0$, $e_0$ |
| the purely imaginary unit vectors $\tilde\Xi$ | the Hermitian family $\tfrac12(e_0+\tilde\Xi)$ |
| the non-trivial $\vec p+i\vec p'$, $\vec p^{2}-\vec p'^{2}=-1$, $\vec p\cdot\vec p'=0$ | the four-parameter family of §*The Plain Family and its Three Parts* |

The table is the whole content of the halving map: the three parts of the roots of $+1$ give the three parts of the plain idempotent set, the trivial pair, the Hermitian family that the general plain sesquilinear product keeps, and the non-trivial family that only the plain product and its symmetrisation keep.

## Summary

The root of the central value $\lambda e_0$ in a structure is the solution of the equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$, and this article reads the value $+1$. For the four general products the root sets are four different sets: the central pair $\pm e_0$ and the pure quadric $(\vec\Xi,\vec\Xi)=-1$ of the plain product, of real dimension four; the family $\tilde\Xi\tilde\Xi^{*}=e_0$, the group of the linear maps preserving the Hermitian form, of real dimension four; the quadric $C=+1$ of the natural product, of real dimension six; and the slope family at $\lvert t\rvert>1$ together with the central circle for the fourth product. A root of $+1$ is a unit of the algebra for the four general products, and the two symmetric sesquilinear structures lie outside that reading, the witness $\tfrac{1}{\sqrt2}(e_1+ie_2)$ being a root of $+1$ in $\mathrm{SPS}$ with $C=0$.

Among the twelve structures a root of $+1$ exists for the four bilateral structures, the two indefinite sesquilinear ones and the two definite sesquilinear ones; and the four antisymmetric structures read the value $0$ alone, their square vanishing or being pure. The root sets of the signed values are not a subject here beyond the remark that ends §*The Roots of One*, since in the six bilinear structures the multiplication by $i$ carries the root set of $+1$ onto that of $-1$, and the mechanism is not universal.

The idempotents are the roots of $+1$ of the plain product read through the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$, of inverse $\tilde\Pi\mapsto2\tilde\Pi-e_0$. The plain product carries the trivial pair, the Hermitian family and the four-parameter non-trivial family; its symmetrisation carries the same set; the general plain sesquilinear product carries the trivial pair and the Hermitian family; the general quaternionic sesquilinear product and its symmetrisation carry the trivial pair and the displaced family $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$ with $(\hat u,\hat u)=1$; the three scalar-valued structures carry the trivial pair; and the four antisymmetric structures carry the origin alone. The central square separates the sets, zero on the plain and Hermitian families and $e_0$ on the displaced family, so the units among the idempotents are $e_0$ and the displaced family, the zero divisors are the non-trivial plain family and its Hermitian part, and the complementation $\tilde\Pi\mapsto e_0-\tilde\Pi$ pairs the plain family and the Hermitian family alone. The families occupy the centre, $\mathbb{M}_+$, $\mathbb{H}_{\mathbb{B}}$ and no remarkable subspace, and the Peirce decomposition is the plain product's own, because it needs associativity.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lambda e_0$ | a central value, $\lambda\in\mathbb{C}$ |
| $\mathcal R_{+1}$ | the root set of the value $+1$, the solutions of $\tilde\Xi\star\tilde\Xi=e_0$ |
| $C(\tilde\Xi)e_0=\tilde\Xi^{\natural}\tilde\Xi$ | the central square, with $C(\tilde\Xi)=\sum_\mu\Xi_\mu^{2}$ |
| $H(\tilde\Xi)=\sum_\mu\lvert\Xi_\mu\rvert^{2}$ | the Hermitian square, the scalar part of the second product's square |
| $\Delta(\tilde\Xi)=\lvert\Xi_0\rvert^{2}-\sum_k\lvert\Xi_k\rvert^{2}$ | the Krein value, the scalar part of the fourth product's square |
| $\hat u$ | a real unit vector, of square $-e_0$ |
| $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$, $\tilde\Xi^{2}=e_0$ | the halving map, from the roots of $+1$ of the plain product to the idempotents |
| $-\tfrac12e_0+\tfrac{\sqrt3}{2}\hat u$, $(\hat u,\hat u)=1$ | the idempotents of the general quaternionic sesquilinear product and of its symmetrisation |
| $\tilde\Pi\mapsto e_0-\tilde\Pi$ | the complementation, or antipode, of the plain family |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space, the four general products and their eight parts |

## Further Reading

- *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), the companion of this article, for the general value, the four existence classes and the theorem that a root of a non-zero value is a unit.
- *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/square-roots-of-zero-and-the-nilpotents-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), the other companion, for the value $0$ and the square-zero sets.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the root of a central value and the idempotent stated once for a general product.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md`), and its siblings *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*, *… of the Antisymmetric Plain Algebra*, *… of the General Quaternionic Algebra*, *… of the Symmetric Quaternionic Algebra*, *… of the Antisymmetric Quaternionic Algebra*, *… of the General Plain Sesqualgebra*, *… of the Symmetric Plain Sesqualgebra*, *… of the Antisymmetric Plain Sesqualgebra*, *… of the General Quaternionic Sesqualgebra*, *… of the Symmetric Quaternionic Sesqualgebra* and *… of the Antisymmetric Quaternionic Sesqualgebra* (the twelve files of `articles_maths/` whose names begin `square-roots-of-one-and-the-idempotents-of-the-`), for the root set of each structure, quoted one by one.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`) and *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the four general products, their eight parts and the twelve names.
- *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the cone, the zero-divisor sets and the one-sided inverse equations.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the tabulation of the four root problems and the four idempotent sets.
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the root set of $+1$ of the general plain sesquilinear product.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternioid-sesqualgebra.md`) and *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the two squares of the sesquilinear families.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the criterion $C\neq0$ with which the idempotents are classified as units or zero divisors.
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.md`), for the decomposition the plain idempotents carry and the associativity it needs.
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`) and *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces in which the families are placed.
