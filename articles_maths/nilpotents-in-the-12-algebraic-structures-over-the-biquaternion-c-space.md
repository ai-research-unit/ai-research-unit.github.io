# __Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space__

## Introduction

A **nilpotent of index two** of a product $\star$ on the biquaternion space $\mathbb{B}$ is a nonzero element whose product with itself vanishes, $\tilde\Pi\star\tilde\Pi=0$, and the corpus calls it a **square-zero** element. The **square-zero set** of the structure is the solution set of the equation, the origin included, so that a nilpotent is a nonzero member of it. The equation names a product, so the twelve structures of the space carry twelve square-zero sets, and they range from the origin alone to the whole space.

**The twelve names.** The space carries twelve products, the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and their eight symmetric and antisymmetric parts (*The 12 Products of the Biquaternion Complex Space*). Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first slot is read through the natural conjugation; the third is the family, $\mathrm A$ the algebra over $\mathbb{C}$ and $\mathrm S$ the sesqualgebra. The twelve are read in the four families of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** This article owns the four square-zero sets and their closed forms, the self-annihilation reading, the order theorem, the twelve-row table and the gap between the square-zero set and the zero-divisor set. The cone and the zero-divisor sets are *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the two one-sided annihilators are *Annihilators in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the general vocabulary, the nilpotent stated once for a general product, is *Definitions for the Study of the 12 Algebraic Structures*; the squares the sets are read from are *Relations Between the Four General Products*, *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* and *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*; the twelve readings stay owned one by one by the twelve *Nilpotents of the …* articles, cited in §*The Twelve Structures and the Square-Zero Sets* and in §*Further Reading*; and the products and the structures are *The 12 Products of the Biquaternion Complex Space* and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, whose codes are used throughout.

**Conventions.** $\mathbb{B}$ has basis $e_0,e_1,e_2,e_3$ over $\mathbb{C}$ with $e_1e_2=e_3$; a general element is $\tilde P=P_0e_0+\mathbf P$ with $P_k\in\mathbb{C}$ and $\mathbf P=\sum_kP_ke_k$; the natural conjugation is $\tilde P^{\natural}=P_0-\mathbf P$; the star is $\tilde P^{*}=\overline{\tilde P^{\natural}}$; the **central square** is $\tilde P^{\natural}\tilde P=\tilde P\tilde P^{\natural}=C(\tilde P)e_0$, a central element, written $C$ and equal to the reduced norm $\mathrm{Norm}(\tilde P)=\sum_\mu P_\mu^{2}$; and the **zero-divisor cone** is $\mathcal{C}=\{\tilde P:\mathrm{Norm}(\tilde P)=0\}$. The four general products are written $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$ and $\tilde P^{\natural}\tilde Q^{*}$, and the two one-sided annihilators of one element for a product $\star$ are $A_\star(\tilde P)$ and $B_\star(\tilde P)$.

## The Square-Zero Sets of the Four General Products

The square-zero sets are the self-annihilation part of the theory: an element is square-zero when it annihilates itself. The four equations are

$$
\tilde P\tilde P=0 , \qquad \tilde P^{\natural}\tilde P=0 , \qquad \tilde P\tilde P^{*}=0 , \qquad \tilde P^{\natural}\tilde P^{*}=0 ,
$$

one to a general product, and they range from a single point to the whole cone.

**Theorem (the four square-zero sets).** Write $Z_1,Z_2,Z_3,Z_4$ for the square-zero sets of the plain, the natural, the general plain sesquilinear and the general quaternionic sesquilinear product. Then

$$
Z_1=\{P_0=0,\ (\mathbf P,\mathbf P)=0\} , \qquad Z_2=\mathcal{C} , \qquad Z_3=\{0\} , \qquad Z_4=\{\tilde P:\overline{\tilde P}\tilde P=0\} ,
$$

and $Z_1$ is the **pure isotropic cone**, of real dimension four; $Z_2$ is the whole cone; $Z_3$ is the origin alone; and $Z_4$ is a proper subfamily of the cone, containing the nonzero element $e_0+ie_1$.

*Proof.* The first is the vanishing of the plain square, $\bigl(P_0^{2}-(\mathbf P,\mathbf P)\bigr)e_0+2P_0\mathbf P$, whose central coefficient and vector coefficient must vanish separately: $P_0\mathbf P=0$ gives $P_0=0$ or $\mathbf P=0$, and $\mathbf P=0$ forces $P_0=0$, so $P_0=0$ and $(\mathbf P,\mathbf P)=0$, a real cone of real dimension four (*Zero Divisors of the General Plain Algebra*). The second is the vanishing of the central square, which is the norm. The third is the definiteness of $\sum_\mu\lvert P_\mu\rvert^{2}$, the scalar part of the Hermitian square $\tilde P\tilde P^{*}$ (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*), so only the origin vanishes. The fourth is the equation $\overline{\tilde P}\tilde P=0$, equivalent to $\tilde P^{\natural}\tilde P^{*}=0$ through ${}^{\natural}$, and it is satisfied by $e_0+ie_1$ while its scalar part $\lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$ vanishes there, so it lies on the cone (*The Square of the General Quaternionic Sesquilinear Product and the Two Halves*).

**Corollary (self-annihilation).** For each of the four general products the square-zero set is the set of elements that lie in their own annihilator,

$$
\tilde P\star\tilde P=0 \iff \tilde P\in A_\star(\tilde P) \iff \tilde P\in B_\star(\tilde P) ,
$$

the annihilator being read in the same product. The natural product gives the converse that fails for the fourth: for the natural product every element of the cone lies in its own annihilator, while for the fourth the element $ie_0+e_1+e_2+ie_3$ does not.

**Theorem (the order of the sets).** With $Z_1,Z_2,Z_3,Z_4$ the square-zero sets above,

$$
Z_3=\{0\}\subsetneq Z_1\subsetneq Z_2 , \qquad Z_3\subsetneq Z_4\subsetneq Z_2 , \qquad Z_1\cap Z_4=\{0\} ,
$$

so that $Z_1$ and $Z_4$ are incomparable, and the four sets are ordered only by the two chains through $Z_2$.

*Proof.* The inclusions $Z_1\subseteq Z_2$ and $Z_4\subseteq Z_2$ are the theorem above, and both are strict: $e_0+ie_1$ lies in $Z_2$ and not in $Z_1$, so $Z_1\subsetneq Z_2$, while $ie_0+e_1+e_2+ie_3$ lies in $Z_2$ and not in $Z_4$, so $Z_4\subsetneq Z_2$. The sets $Z_1$ and $Z_4$ are non-empty beyond the origin, $e_1+ie_2$ and $e_0+ie_1$ being witnesses, and $Z_1\cap Z_4=\{0\}$ because a pure element of $Z_4$ has $\sum_k\lvert P_k\rvert^{2}=0$, hence vanishes.

## The Twelve Structures and the Square-Zero Sets

The four products are four of the twelve structures of the space, and the equation $\tilde P\star\tilde P=0$ is written in the operation of the structure, so each of the twelve carries a square-zero set of its own. The set is the self-annihilation part of the zero-divisor theory, and it is read in the same family order.

**Theorem (the twelve square-zero sets).** Among the twelve structures the square-zero set is the whole space for $\mathrm{APA}$ and $\mathrm{AQA}$; the whole cone $\mathcal{C}$ for $\mathrm{GQA}$ and $\mathrm{SQA}$; the pure isotropic cone for $\mathrm{GPA}$ and $\mathrm{SPA}$; a proper subfamily of the cone for $\mathrm{GQS}$ and $\mathrm{SQS}$; the origin alone for $\mathrm{GPS}$ and $\mathrm{SPS}$; and a subfamily outside the cone, containing the unit, for $\mathrm{APS}$ and $\mathrm{AQS}$.

*Proof.* The plain square is that of §*The Square-Zero Sets of the Four General Products* for $\mathrm{SPA}$, and the central square for $\mathrm{SQA}$, so the two symmetric bilinear structures inherit the sets of their general partners while their zero-divisor sets enlarge. For the sesquilinear pair the symmetric parts are the central forms, so their square-zero sets are those of the general structures at the two equal arguments, and the antisymmetric parts are half the difference between the square and its conjugate transpose, which vanishes exactly when the square is fixed by that involution. Each entry is the theorem of the owner article named in §*Further Reading*.

The classification is sharp, and it reads the ways a square operator can be too large, too small, or too detached from the cone. The **two alternating** squares are the whole space, because they vanish identically; the **central** squares are the cone, because the central square is the norm; the **plain** square is the pure isotropic cone, one component of the cone singled out by the vanishing of the scalar part. The **Hermitian** square is definite and gives the origin alone, while the two **antisymmetric sesquilinear** squares give subfamilies that leave the cone altogether and contain the unit $e_0$, whose square under them vanishes because the value is fixed by the involution that halves them.

The twelve are read one by one below; each names the product, its square-zero set and the reason, and cites the article that owns them.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde P\tilde Q$, and its square is the plain square. The square-zero set is the pure isotropic cone $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$, of real dimension four, one component of the zero-divisor cone of the algebra. The article is *Nilpotents of the General Plain Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde P\bullet\tilde Q$, and its square is the plain square, $\tilde P\bullet\tilde P=\tilde P^{2}$. The square-zero set is the pure isotropic cone, element for element that of $\mathrm{GPA}$. The article is *Nilpotents of the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde P\wedge\tilde Q=\mathbf P\times\mathbf Q$, alternating, so its square vanishes identically. The square-zero set is the whole space, and every element is a nilpotent. The article is *Nilpotents of the Antisymmetric Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde P^{\natural}\tilde Q$, and its square is the central element $C(\tilde P)e_0$; the equation is the vanishing of the norm, so the square-zero set is the whole cone $\mathcal{C}$. The article is *Nilpotents of the General Quaternionic Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation $\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$, whose value is central, and its square is $C(\tilde P)e_0$; the square-zero set is the whole cone $\mathcal{C}$, as for $\mathrm{GQA}$. The article is *Nilpotents of the Symmetric Quaternionic Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the commutator $\tilde P\wedge^{\natural}\tilde Q$, alternating, so its square vanishes identically. The square-zero set is the whole space. The article is *Nilpotents of the Antisymmetric Quaternionic Algebra*.

### $\mathrm{GPS}$, the general plain sesqualgebra

The product is $\tilde P\tilde Q^{*}$, and its square is the Hermitian square, of scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$; the equation forces the origin. The square-zero set is $\{0\}$ alone. The article is *Nilpotents of the General Plain Sesqualgebra*.

### $\mathrm{SPS}$, the symmetric plain sesqualgebra

The product is the symmetric part of $\tilde P\tilde Q^{*}$, scalar-valued and non-negative, and its square is $\mathrm{Sc}(\tilde P\tilde P^{*})e_0$; the square-zero set is $\{0\}$ alone. The article is *Nilpotents of the Symmetric Plain Sesqualgebra*.

### $\mathrm{APS}$, the antisymmetric plain sesqualgebra

The product is the antisymmetric part of $\tilde P\tilde Q^{*}$, and its square is half the difference between the Hermitian square and its conjugate; the equation is therefore equivalent to $\tilde P\tilde P^{*}$ being central. The square-zero set is that subfamily, which lies outside the cone and contains $e_0$. The article is *Nilpotents of the Antisymmetric Plain Sesqualgebra*.

### $\mathrm{GQS}$, the general quaternionic sesqualgebra

The product is $\tilde P^{\natural}\tilde Q^{*}$, and its square is $\tilde P^{\natural}\tilde P^{*}$, equivalent to $\overline{\tilde P}\tilde P$. The square-zero set is the subfamily $\{\overline{\tilde P}\tilde P=0\}$, a proper subfamily of the cone containing $e_0+ie_1$. The article is *Nilpotents of the General Quaternionic Sesqualgebra*.

### $\mathrm{SQS}$, the symmetric quaternionic sesqualgebra

The product is the symmetric part of $\tilde P^{\natural}\tilde Q^{*}$, and its square is the coefficientwise real part of $\tilde P^{\natural}\tilde P^{*}$; the equation is the same as for $\mathrm{GQS}$, so the square-zero set is the subfamily $\{\overline{\tilde P}\tilde P=0\}$, the same as for $\mathrm{GQS}$. The article is *Nilpotents of the Symmetric Quaternionic Sesqualgebra*.

### $\mathrm{AQS}$, the antisymmetric quaternionic sesqualgebra

The product is the antisymmetric part of $\tilde P^{\natural}\tilde Q^{*}$, and its square is half the difference between $\tilde P^{\natural}\tilde P^{*}$ and its conjugate; the equation is therefore equivalent to $\tilde P^{\natural}\tilde P^{*}$ being fixed by the coefficientwise conjugation. The square-zero set is that subfamily, which lies outside the cone and contains $e_0$. The article is *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*.

## Results

The twelve square-zero sets are collected below, the reading against the zero-divisor sets kept, and the gap between the two sets closed last.

### The Twelve Square-Zero Sets

| family | structure | the square-zero set | against its zero-divisor set |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | the pure isotropic cone, $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ | a proper subfamily of the cone |
| | $\mathrm{SPA}$ | the pure isotropic cone, $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ | a proper subfamily of the enlarged set |
| | $\mathrm{APA}$ | the whole space | the zero-divisor set, with the origin |
| the quaternionic algebra | $\mathrm{GQA}$ | the whole cone $\mathcal{C}$ | the zero-divisor set, with the origin |
| | $\mathrm{SQA}$ | the whole cone $\mathcal{C}$ | a proper subfamily of the punctured space |
| | $\mathrm{AQA}$ | the whole space | the zero-divisor set, with the origin |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\{0\}$ alone | a proper subfamily |
| | $\mathrm{SPS}$ | $\{0\}$ alone | a proper subfamily |
| | $\mathrm{APS}$ | the subfamily with $\tilde P\tilde P^{*}$ central | not inside the cone; contains $e_0$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | the subfamily $\overline{\tilde P}\tilde P=0$ | a proper subfamily of the cone |
| | $\mathrm{SQS}$ | the subfamily $\overline{\tilde P}\tilde P=0$ | a proper subfamily of the enlarged set |
| | $\mathrm{AQS}$ | the subfamily with $\tilde P^{\natural}\tilde P^{*}$ fixed by $\overline{\cdot}$ | not inside the cone; contains $e_0$ |

Read down the third column, four kinds of entry occur: the whole space, for the two alternating structures; the cone or a subfamily of it, for the six structures whose square is the plain square, the central square or the fourth product's square; the origin alone, for the two structures whose square is definite; and a subfamily outside the cone, for the two antisymmetric sesquilinear structures, the only rows whose set contains the unit.

### Where the Square Detects the Zero Divisors

A vanishing square is an annihilating factor, so the square-zero set without the origin lies in the zero-divisor set of every structure; the converse is the property that fails, and the gap is a property of the structure and not of the element. The two sets agree, origin included, exactly for the three structures whose square vanishes identically or is the central square: $\mathrm{GQA}$, whose square is the norm, and $\mathrm{APA}$ and $\mathrm{AQA}$, which are alternating. For the other nine the square-zero set is strictly smaller, and it shrinks to the origin alone on the plain sesquilinear pair $\mathrm{GPS}$ and $\mathrm{SPS}$ while their zero-divisor set is the whole punctured space.

## Summary

The square-zero sets are the self-annihilation part of the theory: an element is square-zero exactly when it lies in its own annihilator, $A_\star(\tilde P)$ on the left or $B_\star(\tilde P)$ on the right, the annihilator being read in the same product. For the four general products the plain product's set is the pure isotropic cone $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ of real dimension four, the natural product's is the whole cone $\mathcal{C}$, the general plain sesquilinear product's is the origin alone, and the general quaternionic sesquilinear product's is the proper subfamily $\overline{\tilde P}\tilde P=0$ of the cone, which contains $e_0+ie_1$ and misses $ie_0+e_1+e_2+ie_3$.

The four sets are ordered only through the cone, $Z_3=\{0\}\subsetneq Z_1\subsetneq Z_2$ and $Z_3\subsetneq Z_4\subsetneq Z_2$, with $Z_1$ and $Z_4$ incomparable and meeting only at the origin. Among the twelve structures the square-zero set is the whole space for the two alternating derived structures $\mathrm{APA}$ and $\mathrm{AQA}$, the whole cone for $\mathrm{GQA}$ and $\mathrm{SQA}$, the pure isotropic cone for $\mathrm{GPA}$ and $\mathrm{SPA}$, a proper subfamily of the cone for $\mathrm{GQS}$ and $\mathrm{SQS}$, the origin alone for $\mathrm{GPS}$ and $\mathrm{SPS}$, and a subfamily outside the cone for $\mathrm{APS}$ and $\mathrm{AQS}$.

A vanishing square is an annihilating factor, so every square-zero set without the origin lies in the zero-divisor set of its structure, and the cone lies in every one of them. The converse fails: the two sets agree, origin included, exactly for the three structures whose square vanishes identically or is the central square, $\mathrm{GQA}$ whose square is the norm and the two alternating structures $\mathrm{APA}$ and $\mathrm{AQA}$, and the gap for the other nine is a property of the structure and not of the element.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\star$ | one of the twelve products of $\mathbb{B}$; the four general products in the theorems |
| $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | the four general products |
| square-zero, nilpotent of index two | an element with $\tilde P\star\tilde P=0$ in the product $\star$ |
| $C(\tilde P)e_0=\tilde P^{\natural}\tilde P$ | the central square of an element, the reduced norm |
| $Z_1,Z_2,Z_3,Z_4$ | the square-zero sets of the plain, natural, general plain sesquilinear and general quaternionic sesquilinear products |
| $\mathcal{C}=\{\tilde Q:\mathrm{Norm}(\tilde Q)=0\}$ | the zero-divisor cone |
| $\mathrm{Norm}(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the reduced norm, the general quaternionic bilinear algebraic norm |
| $\overline{\tilde P}\tilde P$ | the coefficientwise conjugate times the element, the square of the fourth product up to ${}^{\natural}$ |
| $A_\star(\tilde P)$, $B_\star(\tilde P)$ | the two one-sided annihilators of $\tilde P$ for the product $\star$ |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space: the four general products and their eight symmetric and antisymmetric parts |

## Further Reading

- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the cone, the twelve zero-divisor sets and their reading against the square-zero sets.
- *Annihilators in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the two one-sided annihilators of one element and their relation by the conjugations.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the nilpotent stated once for a general product.
- The four families of owners, for the square-zero set of each structure: *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), *Nilpotents of the Symmetric Plain Algebra* (`articles_maths/nilpotents-of-the-symmetric-plain-algebra.md`) and *Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-algebra.md`); *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra.md`), *Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-algebra.md`) and *Nilpotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-quaternionic-algebra.md`); *Nilpotents of the General Plain Sesqualgebra* (`articles_maths/nilpotents-of-the-general-plain-sesqualgebra.md`), *Nilpotents of the Symmetric Plain Sesqualgebra* (`articles_maths/nilpotents-of-the-symmetric-plain-sesqualgebra.md`) and *Nilpotents of the Antisymmetric Plain Sesqualgebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-sesqualgebra.md`); and *Nilpotents of the General Quaternionic Sesqualgebra* (`articles_maths/nilpotents-of-the-general-quaternionic-sesqualgebra.md`), *Nilpotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-sesqualgebra.md`) and *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/nilpotents-of-the-antisymmetric-quaternionic-sesqualgebra.md`).
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the pure family of the cone, which is the plain product's square-zero set.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the equation $\overline{\tilde P}\tilde P=0$ of the fourth set.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the definiteness that reduces the third set to the origin.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the tabulation of the four sets beside the four idempotent sets and the four unit entries.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`) and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the four general products, their eight parts, the twelve names and their three-letter codes.
