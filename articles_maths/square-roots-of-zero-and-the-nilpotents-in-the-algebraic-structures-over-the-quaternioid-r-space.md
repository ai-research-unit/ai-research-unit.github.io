# __Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space__

## Introduction

Let $\star$ be a product on the quaternion space $\mathbb{H}$. An element $\tilde\xi$ is a **root of the central value** $0$ when its square in that product vanishes,

$$
\tilde\xi\star\tilde\xi=0 ,
$$

and the **root set of $0$** is the set of its solutions. The root set of $0$ is at once the **square-zero set** of the structure, and its nonzero members are the **square-zero elements**, or **nilpotents of index two**. The two names are one computation: this article reads the root set of $0$ of the three companion structures, and then reads the nilpotents, which are its nonzero members, together with the two other classes a nonzero square-zero element belongs to, the zero divisors and its own annihilations. The algebra product is named once for the contrast and cited, not restated.

The value $0$ is central, the centre of the quaternion space over $\mathbb{R}$ being the real line, so it is the value $\lambda e_t$ at $\lambda=0$. The two signed values are the subject of *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, where the value $+1$ and the idempotents are read and the value $-1$ is a closing remark; the general value $\lambda$ is *Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

**The three companion structures.** The companion products of *The 6 Products of the Quaternioid Real Space* carry three structures, named in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*:

$$
\mathrm{SPA} , \qquad \mathrm{APA} , \qquad \mathrm{GQA} ,
$$

the **symmetric plain algebra** of the Jordan product, the **antisymmetric plain algebra** of the cross product and the **general quaternionic algebra** of the product $\tilde\xi^{\natural}\tilde q$. Every table of the article follows this order.

**Scope and owners.** This article owns the comparison of the three root sets of $0$ and of the three square-zero sets, the cone reading of the root set of $0$, the comparison of the three classes of the square-zero elements, the zero divisors and the roots of $0$, and the nilpotent as the nonzero member of the set. The per-structure results stay owned by their articles, cited one by one below: for the general quaternionic algebra *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, for the symmetric plain algebra *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, and for the antisymmetric plain algebra *Introduction to the Antisymmetric Plain Algebra*; the algebra-product result is owned by *Square Roots of Zero and the Nilpotents of the Quaternion Algebra* in the *Quaternions* category. The products are *The 6 Products of the Quaternioid Real Space*; the vocabulary stated once for a general product, the root of a central value and the nilpotent, is *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the two forms are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*; the zero divisors and the one-sided inverse equations are *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the annihilating partners are *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; and the biquaternion case is *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{H}$ has basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t=1$; a general element is $\tilde\xi=\xi_te_t+\vec\xi$ with $\xi_t\in\mathbb{R}$ and $\vec\xi=\sum_k\xi_k\vec e_k$; the natural conjugation is $\tilde\xi^{\natural}=\xi_t-\vec\xi$; the **plain form** is $\langle\tilde\xi\rangle=\xi_t^{2}-\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{2})$; and the **quaternion form** is $\langle\tilde\xi\rangle_{\natural}=\xi_t^{2}+\lvert\vec\xi\rvert^{2}=\mathrm{Sc}(\tilde\xi^{\natural}\tilde\xi)$, the norm. The algebra product is $\tilde\xi\tilde q$, the general quaternionic product is $\tilde\xi^{\natural}\tilde q$, the Jordan product is $\tilde\xi\bullet\tilde q=\tfrac12(\tilde\xi\tilde q+\tilde q\tilde\xi)$, and the plain cross product is $\tilde\xi\wedge\tilde q=\tfrac12(\tilde\xi\tilde q-\tilde q\tilde\xi)=\vec\xi\times\vec q$. The **root of a central value** is defined in *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* §*The Element Vocabulary* as an element $\tilde\xi$ with $\tilde\xi^{2}=c$ for a central $c$, the class of them being the set of its solutions, with no nonzero requirement; the **nilpotent** is defined in the same section as a nonzero square-zero element.

## The Roots of Zero in the Three Companion Structures

The square of a structure is its operation read at the two equal arguments, so each of the three carries a root problem of its own, and the three squares are two. They are read off the squares of *Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* §*The Two General Products at a General Value*, recalled here:

| the square | the structure | at the two equal arguments |
|---|---|---|
| the plain square | $\mathrm{SPA}$ | $(\xi_t^{2}-\lvert\vec\xi\rvert^{2})e_t+2\xi_t\vec\xi$ |
| the central square | $\mathrm{GQA}$ | $\langle\tilde\xi\rangle_{\natural}e_t$ |
| the vanishing square | $\mathrm{APA}$ | $0$ |

The algebra product of the space carries the plain square as well, and that reading is owned by the *Quaternions* category.

**Definition.** The **root set of $0$** in the structure $\star$ is

$$
\mathcal R_0=\{\tilde\xi:\tilde\xi\star\tilde\xi=0\} ,
$$

and it is the square-zero set of the structure.

**Definition.** A subset of $\mathbb{H}$ is a **cone** when it contains $\mu\tilde\xi$ for every $\tilde\xi$ it contains and every real $\mu$. Its **apex** is the origin.

**Proposition (the root set of $0$ is the cone, and the root sets of the two signed values carry no apex).** The set $\mathcal R_0$ is a cone whose apex is the origin: a real multiple of a root of $0$ is again a root of $0$. It is the origin alone for the two structures whose square vanishes only there, and the whole space, a cone with the origin as apex, for the antisymmetric plain structure. The sets of roots of the two signed values carry no apex: a scaling by $\mu$ carries the value $\lambda$ to $\mu^{2}\lambda$, so no nonzero multiple of a root of $\lambda$ is again a root of $\lambda$ unless $\mu^{2}=1$.

*Proof.* The square of a scaled element is $\mu^{2}(\tilde\xi\star\tilde\xi)$, the three companion products being bilinear over $\mathbb{R}$, so the vanishing of the square is preserved by every $\mu$ and a signed value is preserved by $\mu=\pm1$ alone. The root set of $0$ of the plain square is the origin and not the cone of the plain form, because the two equations of the pair must hold together: the cone $\langle\cdot,\cdot\rangle=0$ meets the vector subspace at the origin alone, and the other branch is the centre.

**Theorem (the three root sets of $0$).** Among the three companion structures the root set of $0$ is the origin alone $\{0\}$ for the symmetric plain algebra and the general quaternionic algebra, and it is the whole space $\mathbb{H}$ for the antisymmetric plain algebra. Only two root sets occur, and no companion structure has a root set of $0$ that is neither a point nor the whole space. The algebra product of the same space has the origin alone, as owned by the *Quaternions* category.

*Proof.* For the symmetric plain structure the pair $\langle\tilde\xi\rangle=0$, $2\xi_t\vec\xi=0$ forces the origin: the second equation gives $\xi_t=0$ or $\vec\xi=0$, the pure branch gives $\lvert\vec\xi\rvert^{2}=0$ and the central branch $\xi_t^{2}=0$, and the isotropic cone of the plain form, real though it is, does not lie in the root of $0$, since at an isotropic element the vector part $2\xi_t\vec\xi$ does not vanish. For the general quaternionic structure the equation is $\langle\tilde\xi\rangle_{\natural}=0$ with $\langle\cdot\rangle_{\natural}$ a sum of four real squares, so the origin alone vanishes. The antisymmetric plain product is alternating, so $\tilde\xi\wedge\tilde\xi=0$ for every element, and the equation is satisfied identically. The assertion that no third set occurs is the classification of the squares: the square of a companion structure is the plain square, the norm times $e_t$, or zero, and the first two have the origin as their only real zero.

The three are read one by one below; each names the product, its square and its root set of $0$, and cites the article that owns it.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde\xi^{\natural}\tilde q$, and its square is the central element $\langle\tilde\xi\rangle_{\natural}e_t$, so the root equation is the single real equation $\langle\tilde\xi\rangle_{\natural}=0$. The norm is a sum of four real squares, so it vanishes at the origin alone. The root set of $0$, and the square-zero set, is $\{0\}$, and there is no nilpotent. The article is *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde\xi\bullet\tilde q=\tfrac12(\tilde\xi\tilde q+\tilde q\tilde\xi)$, and its square is the plain square, $\tilde\xi\bullet\tilde\xi=\tilde\xi^{2}$, of scalar part $\langle\tilde\xi\rangle=\xi_t^{2}-\lvert\vec\xi\rvert^{2}$ and vector part $2\xi_t\vec\xi$. The root equation is the pair $\langle\tilde\xi\rangle=0$, $2\xi_t\vec\xi=0$: the second equation forces $\xi_t=0$ or $\vec\xi=0$, the pure branch gives $\lvert\vec\xi\rvert^{2}=0$ and the central branch gives $\xi_t^{2}=0$, so the origin alone solves. The root set of $0$, and the square-zero set, is $\{0\}$, and there is no nilpotent. The article is *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator $\tilde\xi\wedge\tilde q=\vec\xi\times\vec q$, alternating, so at the two equal arguments it vanishes, $\tilde\xi\wedge\tilde\xi=0$, for every element. The root equation is satisfied identically, and the root set of $0$, the square-zero set, is the whole space $\mathbb{H}$. The nilpotents are all the nonzero elements. The article is *Introduction to the Antisymmetric Plain Algebra*.

**The algebra product and the general quaternionic product at $0$.** At the value $0$ the two structures agree: both root sets are the origin alone, and neither has a nilpotent. This is the value at which the two products agree, while at $+1$ they differ, the algebra product reading the pair $\pm e_t$ and the general quaternionic product the sphere $S^{3}$.

## The Nilpotents

A nilpotent of index two is a nonzero root of $0$; the nilpotent set of the structure is the square-zero set with the origin removed.

| the structure | the square-zero set | the nilpotents |
|---|---|---|
| $\mathrm{GQA}$ | $\{0\}$ | none |
| $\mathrm{SPA}$ | $\{0\}$ | none |
| $\mathrm{APA}$ | $\mathbb{H}$ | every nonzero element |

The two structures whose square vanishes only at the origin have no nilpotent; the antisymmetric plain structure, whose square vanishes identically, has every nonzero element for a nilpotent. The nilpotent, where it exists, is its own annihilating partner in its structure, and it is a zero divisor of that structure (*Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*).

## Results

The set is collected once below, with the two readings of the roots of $0$ and the square-zero sets held together, and the three classes are compared last.

### The Three Root Sets of $0$, Which Are the Three Square-Zero Sets

| the structure | the square | the square-zero equation | the root set of $0$, the square-zero set | the nilpotents |
|---|---|---|---|---|
| $\mathrm{GQA}$ | $\langle\tilde\xi\rangle_{\natural}e_t$ | $\langle\tilde\xi\rangle_{\natural}=0$ | $\{0\}$ | none |
| $\mathrm{SPA}$ | $\tilde\xi^{2}$ | $\langle\tilde\xi\rangle=0$, $2\xi_t\vec\xi=0$ | $\{0\}$ | none |
| $\mathrm{APA}$ | $0$ | satisfied identically | $\mathbb{H}$ | every nonzero element |

Read down the fourth column, only two sets occur: the origin alone $\{0\}$ for the two structures whose square is the plain square or the definite scalar $\langle\tilde\xi\rangle_{\natural}e_t$, and the whole space $\mathbb{H}$ for the one whose square vanishes identically. The origin is the common member, and it is square zero without being a nilpotent, the nilpotents being the nonzero members. The root set of $0$ is a cone in all three structures: the origin, a degenerate cone with the origin as apex, in the two, and the whole space, a cone with the origin as apex, in the third.

### The Three Classes

| structure | square-zero set | zero-divisor set | roots of $0$ | the three agree |
|---|---|---|---|---|
| $\mathrm{GQA}$ | $\{0\}$ | $\varnothing$ | $\{0\}$ | trivially, at the origin |
| $\mathrm{SPA}$ | $\{0\}$ | $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | $\{0\}$ | no |
| $\mathrm{APA}$ | $\mathbb{H}$ | $\mathbb{H}\setminus\{0\}$ | $\mathbb{H}$ | yes, away from the origin |

The two structures whose square-zero set is the origin alone have no nilpotent, and the antisymmetric plain structure, whose square vanishes identically, has the punctured space for nilpotent set. The three classes of the table coincide away from the origin exactly for the antisymmetric plain structure; for the two other structures the square-zero set is the origin alone while the zero-divisor set is empty for the general quaternionic structure and the punctured vector subspace for the symmetric plain structure.

A nonzero square-zero element belongs to three classes at once, and the three are the visible content of the classification. The three classes collapse onto one another exactly on the antisymmetric plain structure, where the diagonal of the product is identically zero; they separate as soon as the diagonal does not vanish identically, and the gap between them measures the difference between the vanishing of a square and the vanishing of a product.

## Summary

The root set of $0$ of a structure is the set of elements whose square vanishes, and it is the square-zero set of the structure. The symmetric plain structure has the origin alone, the plain square vanishing there alone though the plain form is indefinite; the general quaternionic structure has the origin alone, by the definiteness of the norm; and the antisymmetric plain structure, being alternating, has the whole space. So only two sets occur among the three, the origin and the whole space, and no structure has an intermediate set. The algebra product has the origin alone as well, as owned by the *Quaternions* category.

The nilpotents are the nonzero members of the square-zero sets: none in the two structures whose square vanishes only at the origin, and every nonzero element in the antisymmetric plain structure, whose square vanishes identically. The square-zero set is a cone with the origin as apex in every structure, since a real multiple of a root of $0$ is again a root of $0$; the root sets of the two signed values carry no apex, and the value $0$ is the value at which the algebra product and the general quaternionic product agree while at $\pm1$ they differ. A nonzero square-zero element is its own annihilating partner and a zero divisor of its structure, and the three classes of the square-zero elements, the zero divisors and the roots of $0$ coincide away from the origin exactly for the antisymmetric plain structure; for the two other structures the square-zero set is the origin alone while the zero-divisor set is empty or the punctured vector subspace.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\xi\star\tilde\xi=0$ | the root equation of the value $0$ in the structure $\star$ |
| $\mathcal R_0$ | the root set of $0$, which is the square-zero set |
| $\tilde\nu$ | a square-zero element, or nilpotent of index two, the nonzero member of the set |
| $\{0\}$ | the square-zero set of $\mathrm{GQA}$ and $\mathrm{SPA}$, and their nilpotent set |
| $\mathbb{H}$ | the square-zero set of $\mathrm{APA}$ |
| $\mathbb{H}\setminus\{0\}$ | the nilpotent set, and the zero-divisor set, of $\mathrm{APA}$ |
| $\langle\tilde\xi\rangle=\xi_t^{2}-\lvert\vec\xi\rvert^{2}$ | the plain form, the scalar part of the plain square |
| $\langle\tilde\xi\rangle_{\natural}=\xi_t^{2}+\lvert\vec\xi\rvert^{2}$ | the quaternion form, the square of $\mathrm{GQA}$, and the norm |
| $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set of $\mathrm{SPA}$, for the comparison |
| cone, apex | a set that contains every real multiple of each of its elements, and its origin |
| $\mathrm{SPA},\mathrm{APA},\mathrm{GQA}$ | the three companion structures of the space |

## Further Reading

- *Square Roots of One and the Idempotents in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-one-and-the-idempotents-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the two signed values, the roots of $+1$ and the idempotents, whose value $0$ is the one read here.
- *Square Roots of a General Element in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), the companion of this article, for the root equation at a general central value and the three-row table.
- *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the three companion names and the class of each.
- *The 6 Products of the Quaternioid Real Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`), for the companion products and their coordinates.
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the plain form $\langle\cdot,\cdot\rangle$ of signature $(1,3)$ and the definite quaternion form $\langle\cdot,\cdot\rangle_{\natural}$.
- *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the three zero-divisor sets and the inverse criterion.
- *Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the annihilating partner of a square-zero element.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra.md`), for the per-structure result in the general quaternionic algebra.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra-of-quaternioid.md`), for the per-structure result in the symmetric plain algebra.
- *Introduction to the Antisymmetric Plain Algebra* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-quaternioid.md`), for the per-structure result in the antisymmetric plain algebra.
- *Square Roots of Zero and the Nilpotents of the Quaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.md`), in the *Quaternions* category, for the algebra product.
