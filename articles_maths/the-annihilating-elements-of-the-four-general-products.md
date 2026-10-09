# __The Annihilating Elements of the Four General Products__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, and the four preceding groups of the chapter read one product each: the general plain bilinear product as the multiplication of an associative algebra with unit (*Introduction to the General Plain Algebra of Biquaternions*), the general quaternionic bilinear product (*Introduction to the General Quaternionic Algebra of Biquaternions*), the general plain sesquilinear product as the multiplication of a sesqualgebra (*Introduction to the General Plain Sesqualgebra of Biquaternions*), and the general quaternionic sesquilinear product (*Introduction to the General Quaternionic Sesqualgebra of Biquaternions*). Each group developed the element theory of its own product: the square of an element, the idempotents, the square-zero elements and the units of the multiplication. This article reads the four element theories together, through the one algebraic invariant that governs all four and through the annihilators each product attaches to an element.

The invariant is the **central square**

$$
\tilde Q\tilde Q^{\natural} = \tilde Q^{\natural}\tilde Q = c(\tilde Q)e_0 , \qquad c(\tilde Q) = \sum_{\mu=0}^{3}Q_\mu^{2} .
$$

It is the second-order invariant the algebra carries, and its vanishing is the criterion of invertibility. Three facts organise the article. First, the central square is multiplicative for each of the four general products, by two laws, one for the bilinear pair and one for the sesquilinear pair; the four laws are one law read through the conjugation each product carries. Second, the elements that admit a nonzero annihilating factor are the same elements for the four general products, exactly the vanishing set of the central square; the article proves this and reads it in the matrix model, where the set is the rank-one elements, and in coordinates, where it is a complex cone of complex dimension three. Third, that one set of elements does **not** determine the theory: the annihilators of one fixed annihilated element, the square-zero sets, the idempotent sets and the unit structures differ from one product to the next, and the article tabulates the four readings with the owner of each entry named.

The article owns the central square and its four multiplicative laws, the identity of the annihilated set with the vanishing set of the central square, the rank-one reading of that set in the matrix model, its cone structure, and the comparison of the four annihilators of one fixed annihilated element. It repeats the four square-zero sets, the four idempotent sets and the four unit structures as a synthesis of the four groups, and it closes on the boundary the annihilated set carries: the set $\{c = 0\}$ is **not** the isotropic cone of the general plain bilinear form $\mathrm{Sc}(\tilde P\tilde Q)$, which belongs to *The Isotropic Structure of the General Plain Bilinear Form*. The restriction of the whole picture to the six distinguished subspaces is *The Six Subspaces and the Four General Products*.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ and central scalar imaginary $i$, $i^2=-1$; a general element is $\tilde Q = \sum_{\mu=0}^{3}Q_\mu e_\mu = Q_0e_0+\mathbf Q$ with $Q_0\in\mathbb{C}$ and $\mathbf Q = \sum_{k=1}^{3}Q_ke_k$. The four general products and their notation are those of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*: $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$, with the natural conjugation $\tilde Q^{\natural} = Q_0-\mathbf Q$ and the star $\tilde Q^{*} = \overline{Q_0}-\overline{\mathbf Q}$, so that ${}^{*} = \bar{\cdot}\circ{}^{\natural}$. The **central square** is $\tilde Q\tilde Q^{\natural} = \tilde Q^{\natural}\tilde Q = c(\tilde Q)e_0$ with $c(\tilde Q) = \sum_\mu Q_\mu^{2}$, a central element, and $(\mathbf P,\mathbf Q) = \sum_k P_kQ_k$ is the general plain bilinear form of the two vector parts.

## The Central Square and the Matrix Model

The central square is the second-order invariant of the algebra.

**Proposition.** For every $\tilde Q\in\mathbb{B}$ the central square is

$$
\tilde Q\tilde Q^{\natural} = c(\tilde Q)e_0 , \qquad c(\tilde Q) = Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2} ,
$$

and it vanishes exactly when the matrix $\Phi(\tilde Q) = Q_0 I - iQ_1\sigma_1 - iQ_2\sigma_2 - iQ_3\sigma_3$ of the element in the model $\mathbb{B}\cong M_2(\mathbb{C})$ is singular.

**Proof.** Directly, $\tilde Q\tilde Q^{\natural} = (Q_0+\mathbf Q)(Q_0-\mathbf Q) = Q_0^{2}-\mathbf Q^{2} = \sum_\mu Q_\mu^{2}\,e_0$, since $\mathbf Q^{2} = -\sum_k Q_k^{2}\,e_0$. The vanishing of the central square is the singularity of $\Phi(\tilde Q)$ by the invertibility criterion (*Biquaternion Norm and Invertibility*), read through the isomorphism. $\square$

The central square is the reason the second-order theory does the work of the whole element theory. Since $\Phi$ is an isomorphism of $\mathbb{C}$-algebras, an element is a unit exactly when $\Phi(\tilde Q)$ is invertible, that is exactly when $c(\tilde Q)\neq0$; and an element is a zero divisor exactly when $\Phi(\tilde Q)$ is singular. The model converts the algebra's element theory into the linear algebra of a complex two-by-two matrix, and it is the frame of the next two sections. The quadratic form the algebra carries, its signature and its norm are read in *Biquaternion Norm and Invertibility*.

**Proposition.** The central square is multiplicative for the plain product, $c(\tilde P\tilde Q) = c(\tilde P)c(\tilde Q)$, and the central square of a conjugation is the conjugated central square: $c(\tilde Q^{\natural}) = c(\tilde Q)$ and $c(\tilde Q^{*}) = \overline{c(\tilde Q)}$.

**Proof.** $c(\tilde P\tilde Q)e_0 = \tilde P\tilde Q(\tilde P\tilde Q)^{\natural} = \tilde P\tilde Q\tilde Q^{\natural}\tilde P^{\natural} = \tilde P\,c(\tilde Q)e_0\,\tilde P^{\natural}$, and $c(\tilde Q)e_0$ is central, so the value is $c(\tilde Q)\tilde P\tilde P^{\natural} = c(\tilde P)c(\tilde Q)e_0$. For the conjugations, $\tilde Q^{\natural}\tilde Q = c(\tilde Q)e_0$ and $\tilde Q\tilde Q^{\natural} = c(\tilde Q)e_0$ are the same statement with $\tilde Q$ replaced by $\tilde Q^{\natural}$, and $c(\tilde Q^{*}) = \overline{c(\tilde Q)}$ is the conjugation of the coefficients, $\sum_\mu\overline{Q_\mu}^{2} = \overline{\sum_\mu Q_\mu^{2}}$. $\square$

## The Four Multiplicative Laws of the Central Square

Each of the four general products multiplies the central square by one of two laws, and the law is the one the second slot carries.

**Theorem (the four laws).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
c(\tilde P\tilde Q) = c(\tilde P)\,c(\tilde Q) , \qquad c(\tilde P^{\natural}\tilde Q) = c(\tilde P)\,c(\tilde Q) ,
$$

$$
c(\tilde P\tilde Q^{*}) = c(\tilde P)\,\overline{c(\tilde Q)} , \qquad c(\tilde P^{\natural}\tilde Q^{*}) = c(\tilde P)\,\overline{c(\tilde Q)} .
$$

**Proof.** The two bilinear laws are the multiplicativity of the previous section together with $c(\tilde P^{\natural}) = c(\tilde P)$. For the two sesquilinear products the second factor carries the star, and $c(\tilde Q^{*}) = \overline{c(\tilde Q)}$; the value read in the plain product, of which the central square is the second-order invariant, is then $c(\tilde P)\overline{c(\tilde Q)}$ in both cases, the natural conjugation of the first factor leaving its own central square alone. $\square$

The two laws are one law with a choice in each slot, and the choice is the same one that separates the four general products in the comparison table: a slot read without a conjugation contributes the central square, a slot read through the conjugated star contributes the conjugate of the central square, and the natural conjugation, being $\mathbb{C}$-linear, contributes the central square. The laws are the algebraic face of the fact that the four general products are the four insertions of the two conjugations into the matrix product.

The laws are read on the square as the special case $\tilde P = \tilde Q$, and they are the reason the four element theories differ. The square of $\tilde Q$ in the plain product has central square $c(\tilde Q)^{2}$; in the natural product the square is the central element $c(\tilde Q)e_0$, whose central square is $c(\tilde Q)^{2}$ again; in the two sesquilinear products the square has central square $c(\tilde Q)\overline{c(\tilde Q)} = \lvert c(\tilde Q)\rvert^{2}$. The value $c^{2}$ for the two bilinear products and $\lvert c\rvert^{2}$ for the two sesquilinear ones is the second-order invariant of the four general products, and the scalar parts of the four squares, which are not the central square, are *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*.

## The Elements with an Annihilating Factor

The four general products are four multiplications of one space, and an element may or may not have a partner that multiplies it to zero. The set of elements that do is the same for the four.

**Definition.** Let $f$ be one of the four general products. An element $\tilde X\neq0$ is an **annihilating factor** of $\tilde P$ when $f(\tilde P,\tilde X) = 0$ or $f(\tilde X,\tilde P) = 0$, on one side or the other.

**Theorem (the annihilated set is the same for the four general products).** For each of the four general products the elements that admit an annihilating factor are exactly the elements of vanishing central square,

$$
\{\tilde P : \exists\,\tilde X\neq0,\ f(\tilde P,\tilde X) = 0 \ \text{or}\ f(\tilde X,\tilde P) = 0\} = \{\tilde P : c(\tilde P) = 0\} ,
$$

**Proof.** Fix a product $f$ and an element $\tilde P$, and consider the map $\tilde X\mapsto f(\tilde P,\tilde X)$, which is $\mathbb{C}$-linear for the two bilinear products and conjugate-linear for the two sesquilinear ones, and which in the matrix model is left multiplication by $\Phi(\tilde P)$ or by $\Phi(\tilde P^{\natural})$, composed with the conjugate transpose when the second slot carries the star. The map has a nonzero kernel exactly when that matrix is singular, that is exactly when $c(\tilde P) = 0$. Conversely, if $c(\tilde P) = 0$ and $\tilde P\neq0$, then $\tilde P\tilde P^{\natural} = 0$ with $\tilde P^{\natural}\neq0$ exhibits an annihilating factor in the plain product; the natural product takes the same factor, since $\tilde P^{\natural}\tilde P = c(\tilde P)e_0 = 0$; and the two products carrying the star take the conjugate $\overline{\tilde P}$, for which $\tilde P\overline{\tilde P}^{*} = \tilde P\tilde P^{\natural} = 0$ and $\tilde P^{\natural}\overline{\tilde P}^{*} = \tilde P^{\natural}\tilde P = 0$. The same argument with the roles of the two slots exchanged gives the other side. $\square$

The theorem is a statement about one set and four annihilators, and the distinction matters. The set $\{c = 0\}$ is intrinsic to the algebra; the annihilator of a point of the set is not, and the next section reads the four of them. The zero divisors of the algebra are the nonzero points of the set, classified in *Biquaternion Zero Divisors*; the proof above is the sense in which each of the four general products detects them.

## The Cone and the Rank-One Elements

Written on the coordinates, the annihilated set is one complex equation.

**Proposition (the cone).** The set $\{c(\tilde P) = 0\}$ is a complex cone of complex dimension three, hence a real cone of real dimension six in $\mathbb{B}\cong\mathbb{C}^{4}$, and its nonzero part is the zero-divisor set of the algebra.

**Proof.** The equation $Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2} = 0$ is one equation in the four complex coordinates, so its zero set is of complex dimension three away from its singular point at the origin, and a cone because the equation is homogeneous. $\square$

In the matrix model the set is the set of singular matrices, and the nonzero members of it have rank exactly one.

**Proposition (the rank-one elements).** For $\tilde P\neq0$ the following are equivalent: $c(\tilde P) = 0$; the matrix $\Phi(\tilde P)$ is singular; $\Phi(\tilde P)$ has rank one; and the left ideal $\mathbb{B}\tilde P$ is minimal, of complex dimension two.

**Proof.** A nonzero two-by-two matrix is singular exactly when it has rank one, and $c(\tilde P) = 0$ is the singularity of $\Phi(\tilde P)$ by the first section. The left ideal generated by an element of rank one is the set of matrices whose image lies in the one-dimensional image of $\Phi(\tilde P)$, of complex dimension two, and no smaller nonzero left ideal exists in $M_2(\mathbb{C})$; the modules and the ideals are *Modules over the General Plain Algebra of Biquaternions* and *Biquaternion Ideals and Peirce Decomposition*. $\square$

The cone has two algebraic families, and the classification is the algebra's, not the article's.

**Theorem (the two families, quoted).** The zero divisors of $\mathbb{B}$ are of exactly two kinds (*Biquaternion Zero Divisors*). The **pure** ones have vanishing scalar part, are the nonzero solutions of $(\mathbf P,\mathbf P) = 0$, are square-zero, and form a cone of real dimension four; the **non-pure** ones have nonzero scalar part, satisfy $c = 0$ with $Q_0\neq0$, are exactly the nonzero complex multiples of the nontrivial idempotents of the algebra, and fill the rest of the six-dimensional cone.

The two families are read in the six subspaces in *Introduction to the Six Subspaces*: the pure ones fill the nilpotent cone of the vector subspace, the non-pure ones the double cones of the two Hermitian subspaces, and a generic point of the cone lies in none of the six.

## The Four Annihilators of One Annihilated Element

Fix an element of the annihilated set, $\tilde P\neq0$ with $c(\tilde P) = 0$. Each of the four general products has two one-sided annihilators of it, the set of $\tilde X$ with $f(\tilde P,\tilde X) = 0$ and the set of $\tilde X$ with $f(\tilde X,\tilde P) = 0$, and each is a complex plane, so that the four general products carry eight planes, each of complex dimension two.

**Theorem (dimension of the annihilators).** Let $f$ be any of the four general products and let $\tilde P\neq0$. Then $\{\tilde X : f(\tilde P,\tilde X) = 0\}$ and $\{\tilde X : f(\tilde X,\tilde P) = 0\}$ are each of complex dimension two when $c(\tilde P) = 0$, and each $0$ when $c(\tilde P)\neq0$. For the natural product the two planes contain $\tilde P$, because $\tilde P^{\natural}\tilde P = \tilde P\tilde P^{\natural} = c(\tilde P)e_0$ vanishes there; for the other three products $\tilde P$ lies in its own annihilator exactly when it is square-zero in that product, which for $\tilde P\neq0$ happens for the plain and the fourth product and never for the general plain sesquilinear one (the square-zero table below).

**Proof.** In the model the two conditions are the two kernels of the singular matrix $\Phi(\tilde P)$ or of its transpose with the conjugations, and a rank-one matrix has a two-dimensional kernel; for the natural product $\tilde P$ lies in its own annihilator on both sides because $\tilde P\tilde P^{\natural}$ and $\tilde P^{\natural}\tilde P$ are both $c(\tilde P)e_0 = 0$. $\square$

The planes are not the same for the four general products, and the way they differ is the conjugation each product carries.

**Theorem (how the four annihilators are related).** Let $\tilde P$ be annihilated. Writing $A_f(\tilde P) = \{\tilde X : f(\tilde P,\tilde X) = 0\}$ and $B_f(\tilde P) = \{\tilde X : f(\tilde X,\tilde P) = 0\}$, the three planes $A_\natural,A_*,A_{\natural*}$ are the planes of the plain product of $\tilde P$ and of $\tilde P^{\natural}$ and their star-images,

$$
A_{\natural}(\tilde P) = A_{\text{plain}}(\tilde P^{\natural}) , \qquad A_{*}(\tilde P) = A_{\text{plain}}(\tilde P)^{*} , \qquad A_{\natural*}(\tilde P) = A_{\text{plain}}(\tilde P^{\natural})^{*} ,
$$

and the two sides coincide for the natural product and for the general plain sesquilinear product, $A_\natural = B_\natural$ and $A_* = B_*$, while for the plain product and for the general quaternionic sesquilinear product they differ in general.

**Proof.** The first identity is $\tilde P^{\natural}\tilde X = 0$ read as the plain product of $\tilde P^{\natural}$ and $\tilde X$. For the second, the substitution $\tilde X = \tilde Y^{*}$ turns $\tilde P\tilde X^{*} = 0$ into $\tilde P\tilde Y = 0$, and ${}^{*}$ is a bijection, so the plane is the star-image of the plane of the plain product; the third is the first and the second composed. For the coincidence of the two sides, the natural product's is the theorem of *The Nilpotents and the Zero Divisors of the Quaternionic Product*, and the general plain sesquilinear product's is the identity $(\tilde X\tilde P^{*})^{*} = \tilde P\tilde X^{*}$, which makes the two conditions the same. For the plain product the two planes are the kernels of a rank-one matrix and of its transpose, which differ as soon as the matrix is not symmetric; the fourth product carries a conjugation in each slot and its two planes differ for the same reason on the generic element. $\square$

**Example.** For the pure zero divisor $\tilde Q = e_1+ie_2$, the plane of the plain product is $\mathbb{C}\{e_1+ie_2,\ e_3-ie_0\}$: both displayed vectors are annihilated by $e_1+ie_2$ on the left, and the plane is the one computed in *The Nilpotents and the Zero Divisors of the Quaternionic Product* for the natural product, whose two sides coincide. The star-images of the two generators are $-e_1+ie_2$ and $ie_0-e_3$, so the plane of the general plain sesquilinear product is $\mathbb{C}\{-e_1+ie_2,\ ie_0-e_3\}$. The two planes are different although the element is pure: the plane $\mathbb{C}\{e_1+ie_2,\ e_3-ie_0\}$ is the annihilator of the plain and of the natural product, because the natural conjugate of a pure element is its negative, and the star-image $\mathbb{C}\{-e_1+ie_2,\ ie_0-e_3\}$ is the annihilator of the two sesquilinear products. The point of the example is that the annihilator of one annihilated element is not an object of the algebra alone but an object of the product.

## The Four Square-Zero Sets

The square of an element, and with it the equation $\tilde Q\star\tilde Q = 0$, separates the four general products sharply. The sets are tabulated in *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*, and each column is proved in the article of its product.

| product | square-zero elements | owner |
|---|---|---|
| $\tilde P\tilde Q$ | the pure isotropic cone $\{P_0 = 0,\ (\mathbf P,\mathbf P) = 0\}$ | *Biquaternion Square Roots of Minus One, Zero and Plus One* |
| $\tilde P^{\natural}\tilde Q$ | the whole cone $\{c(\tilde P) = 0\}$ | *The Nilpotents and the Zero Divisors of the Quaternionic Product* |
| $\tilde P\tilde Q^{*}$ | only $\tilde P = 0$ | *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* |
| $\tilde P^{\natural}\tilde Q^{*}$ | a proper subfamily of $\{c(\tilde P) = 0\}$, the solutions of $\overline{\tilde P}\tilde P = 0$ | *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* |

The four columns are the four ways the annihilated set meets the square: the plain product's square vanishes exactly on the pair $P_0 = 0$, $(\mathbf P,\mathbf P) = 0$, so its square-zero set is the four-dimensional pure subcone, strictly inside the six-dimensional cone; the natural product's square is the central element $c(\tilde P)e_0$, so its square-zero set is the whole cone, the largest of the four; the general plain sesquilinear square has the non-negative scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$, so its square-zero set is the smallest possible; and the general quaternionic sesquilinear square has the indefinite Krein scalar part $\lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$, so its square-zero set is a proper subfamily of the cone strictly larger than $\{0\}$ and incomparable with the pure cone. The four sets sit inside the cone as the two chains of the display, the plain set crossing the fourth instead of nesting inside it,

$$
\{0\} \subsetneq \{\overline{\tilde P}\tilde P = 0\} \subsetneq \{c(\tilde P) = 0\} , \qquad \{P_0 = 0,\ (\mathbf P,\mathbf P) = 0\} \subsetneq \{c(\tilde P) = 0\} ,
$$

with the plain and the fourth of the four incomparable: $e_1+ie_2$ lies in the pure cone and not in the subfamily $\{\overline{\tilde P}\tilde P = 0\}$, and $e_0+ie_1$ lies in the subfamily and not in the pure cone, so that the plain and the general quaternionic sesquilinear sets meet only at the origin.

## The Four Idempotent Sets

The idempotent equation $\tilde Q\star\tilde Q = \tilde Q$ is the other element equation the four general products read differently, and its solutions separate more sharply than the square-zero sets. The table is the one of *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*, and the four columns are owned by *Biquaternion Idempotents and Projections*, *Idempotents of the Quaternionic Product*, *Projections of the Biquaternion Sesqualgebra* and *Idempotents of the General Quaternionic Sesquilinear Product*.

| product | idempotents |
|---|---|
| $\tilde P\tilde Q$ | $0$, $e_0$, and $\tfrac12(e_0+\xi i)$ for a root $\xi$ of $-e_0$ |
| $\tilde P^{\natural}\tilde Q$ | $0$ and $e_0$ alone |
| $\tilde P\tilde Q^{*}$ | $0$, $e_0$, and the Hermitian idempotents $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors |
| $\tilde P^{\natural}\tilde Q^{*}$ | $0$, $e_0$, and $-\tfrac12e_0+\mu$ over the real vectors with $(\mu,\mu) = \tfrac34$ |

The four sets are of four different kinds, and the central square separates them. The trivial pair $0,e_0$ belongs to all four. Beyond the pair, the plain product's family is of real dimension four and every nonzero member of it has vanishing central square, so the nontrivial idempotents of the algebra are zero divisors; the general plain sesquilinear family is the family of the Hermitian idempotents, whose nonzero members also have vanishing central square; the natural product has nothing beyond the pair; and the general quaternionic sesquilinear family, the family $-\tfrac12e_0+\mu$, has central square $e_0$ on every member, so its nontrivial idempotents are **units**, the only nontrivial idempotents among the four multiplications that are. The plain family is the trivial pair, the Hermitian family of the general plain sesquilinear product, and a four-parameter family of non-trivial idempotents, each lying in none of the four four-dimensional subspaces (*Biquaternion Idempotents and Projections*, *Biquaternion Square Roots of Minus One, Zero and Plus One*). The Hermitian family lies in $\mathbb{M}_+$ and the family $-\tfrac12e_0+\mu$ lies in the quaternion subspace, positions read in *Introduction to the Six Subspaces*.

## The Four Unit Structures

The last separation is the unit. The algebra has one group of units, $\mathbb{B}^{\times} = \{\tilde Q : c(\tilde Q)\neq0\}$, of real dimension eight and centre $\mathbb{C}^{\times}$ (*Biquaternion Norm and Invertibility*); the four general products have four different unit structures, and only the plain product has a unit in the two-sided sense.

| product | unit |
|---|---|
| $\tilde P\tilde Q$ | $e_0$, two-sided, and the product is associative, so $\mathbb{B}^{\times}$ is the group of units of the algebra |
| $\tilde P^{\natural}\tilde Q$ | $e_0$ on the left alone; no right unit |
| $\tilde P\tilde Q^{*}$ | $e_0$ on the right alone; no left unit |
| $\tilde P^{\natural}\tilde Q^{*}$ | no unit on either side |

The four entries are read from the two identity rows of the property table of *Comparison Between the Four General Products* ($1$ is a left identity, $1$ is a right identity), and they are proved in the four group articles: the unit of the product is the fixed element of the conjugations the product inserts, and the three products other than the plain one insert a conjugation into a slot, which conjugates the candidate unit and breaks the other side. Two consequences deserve to be recorded here. First, the units of the multiplication are not the units of the algebra: an element may be a unit of $\mathbb{B}$ and have no inverse in the product it is read in, and conversely the idempotents of the fourth product are units of the algebra and idempotents of the multiplication while remaining non-invertible in the multiplication for want of a unit. Second, the absence of a unit is not an absence of structure: the natural product has a monoid of left multiplications, and the two sesquilinear products have none, which is the left-multiplication row of the comparison table (*Relations Between the Four General Products* §*The Left Multiplications*).

## The Two Cones

One warning closes the article. The set $\{c = 0\}$ has the shape of a cone, and the chapter carries a second cone on the same space, the isotropic cone of the general plain bilinear form $\langle\tilde P,\tilde Q\rangle = \mathrm{Sc}(\tilde P\tilde Q)$. They are not the same, and they must not be conflated: the central square reads $P_0^{2}+(\mathbf P,\mathbf P)$ while the diagonal of the general plain bilinear form reads $P_0^{2}-(\mathbf P,\mathbf P)$, the two exchanges of the sign of the vector part, and the element theory is built on the first, and the second is the isotropic cone of the form. The form and its isotropic cone are *The Four Pairings of the Biquaternion Algebra* and *Biquaternion Norm and Invertibility*; the article records the boundary and stops there.

## Summary

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* share one second-order invariant, the central square $\tilde Q\tilde Q^{\natural} = \tilde Q^{\natural}\tilde Q = c(\tilde Q)e_0$ with $c(\tilde Q) = \sum_\mu Q_\mu^{2}$, and the invariant is multiplicative for all four:

$$
c(\tilde P\tilde Q) = c(\tilde P^{\natural}\tilde Q) = c(\tilde P)c(\tilde Q) , \qquad c(\tilde P\tilde Q^{*}) = c(\tilde P^{\natural}\tilde Q^{*}) = c(\tilde P)\overline{c(\tilde Q)} .
$$

The elements that admit a nonzero annihilating factor are the same elements for the four general products, exactly the vanishing set $\{c = 0\}$ of the central square, a complex cone of complex dimension three and real dimension six whose nonzero part is the zero-divisor set of the algebra; in the matrix model they are the singular matrices and, away from zero, the rank-one elements, whose left ideals are the minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$.

One set, four annihilators. Of a fixed annihilated element each product has two one-sided annihilators, each a complex plane when the central square vanishes and each $0$ when it does not; the four pairs are related by the two conjugations, the general plain sesquilinear plane being the star-image of the plane of the plain product, and the natural and the general plain sesquilinear products having their two sides coinciding for every element.

The four square-zero sets, the four idempotent sets and the four unit structures do not follow from the annihilated set and are tabulated here with their owners: the square-zero sets are the origin alone for the general plain sesquilinear product, a proper subfamily of the cone for the general quaternionic sesquilinear product, the pure isotropic cone for the plain product and the whole cone for the natural product, and the two middle sets meet only at the origin; the idempotents are the plain family of the algebra, the trivial pair alone, the family of Hermitian projectors and the family of unitary elements; and the unit belongs to the plain product alone, the natural product keeping it on the left and the general plain sesquilinear product on the right.

The set $\{c = 0\}$ is not the isotropic cone of the general plain bilinear form $\langle\tilde P,\tilde Q\rangle = \mathrm{Sc}(\tilde P\tilde Q)$; the two cones cross, and the algebra's norm cone is the other one. The restriction of the whole picture to the six distinguished subspaces is *The Six Subspaces and the Four General Products*, and the detailed readings of the four element theories are the four group articles of the chapter.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q\tilde Q^{\natural} = c(\tilde Q)e_0$ | the central square; $c(\tilde Q) = \sum_\mu Q_\mu^{2}$ |
| $\Phi(\tilde Q)$ | the matrix of the element, $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\{c = 0\}$ | the annihilated set, a complex cone of real dimension six |
| $A_f(\tilde P)$, $B_f(\tilde P)$ | the two one-sided annihilators of $\tilde P$ for the product $f$ |
| $(\mathbf P,\mathbf Q)$ | the general plain bilinear form of the two vector parts |
| $\langle\tilde P,\tilde Q\rangle = \mathrm{Sc}(\tilde P\tilde Q)$ | the general plain bilinear form, whose isotropic cone is not $\{c = 0\}$ |

## Further Reading

- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general products and their scalar–vector forms.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table, the four idempotent sets, the four square-root problems and the four unit entries.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm form, the quadratic space, the invertibility criterion and the group of units.
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, the trace and the singular matrices.
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the two families, the cone and the classification.
- *The Nilpotents and the Zero Divisors of the Quaternionic Product* (`articles_maths/the-nilpotents-and-the-zero-divisors-of-the-quaternionic-product.md`), for the square-zero set of the natural product and the coincidence of its two annihilators.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the square-zero subfamily of the fourth product.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the square of the general plain sesquilinear product and the cone it generates.
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the three central values of the plain product.
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the elements of the six subspaces, the pure cone and the non-pure families.
- *The Six Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the restriction of the forms to the six subspaces.
- *The Isotropic Structure of the General Quaternionic Algebra* (`articles_maths/the-isotropic-structure-of-the-general-quaternionic-algebra.md`), for the isotropic cones of the two bilinear forms, which are not the vanishing set of the central square.
