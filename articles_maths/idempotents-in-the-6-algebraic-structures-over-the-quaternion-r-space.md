# __Idempotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

An **idempotent** of a product $\star$ on the quaternion space $\mathbb{H}$ is an element $\tilde x$ with

$$
\tilde x\star\tilde x=\tilde x ,
$$

the equation read in that product, and the **idempotent set** of the structure is the set of its solutions. The equation is the algebraic form of a projection, and it names a product, so the six structures of the space answer it six times. The answer is coarse: a two-point set for four of them and the single origin for the two cross products, and the coarseness comes from the real field itself, which has no scalar imaginary and no isotropic direction, so that the two-parameter and four-parameter families of the biquaternion plain product collapse to the trivial pair.

**The six names.** The space carries six products, so the generic definition poses six questions; this article answers them once for all six. Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first slot is read through the natural conjugation; and the third letter is the same one for the six, $\mathrm A$ the algebra over $\mathbb{R}$. The six are read in the two families of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** This article owns the comparison of the six idempotent sets and the reading of the collapse against the biquaternion case. The sets themselves stay owned by the six articles *Idempotents of the …*, cited one by one in §*The Six Structures and the Idempotents*. The products are *The 6 Products of the Quaternion Real Space* and the structures *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, whose codes are used throughout; the vocabulary, the idempotent stated once for a general product, is *Definitions for the Study of the 6 Algebraic Structures*; the division property is *Norm and Invertibility in the General Plain Algebra*; the square-zero sets are *Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the root problems are *Square Roots of Minus One, Zero and Plus One in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* and *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; and the biquaternion case that §*The Contrast with the Biquaternion Case* reads is *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_0=1$; a general element is $\tilde x=x_0e_0+\mathbf x$ with $x_0\in\mathbb{R}$ and $\mathbf x=\sum_kx_ke_k$; the natural conjugation is $\tilde x^{\natural}=x_0-\mathbf x$; the **plain square** is $\tilde x^{2}=(x_0^{2}-\lvert\mathbf x\rvert^{2})e_0+2x_0\mathbf x$, of scalar part the plain form $B(\tilde x)=x_0^{2}-\lvert\mathbf x\rvert^{2}$; and the **quaternionic square** is $\tilde x^{\natural}\tilde x=N(\tilde x)e_0$, of the definite quaternion form $N(\tilde x)=x_0^{2}+\lvert\mathbf x\rvert^{2}$. The plain product is $\tilde x\tilde y$, the Jordan product is $\tilde x\bullet\tilde y=\tfrac12(\tilde x\tilde y+\tilde y\tilde x)$, the plain cross product is $\tilde x\wedge\tilde y=\tfrac12(\tilde x\tilde y-\tilde y\tilde x)=\mathbf x\times\mathbf y$, and the quaternionic cross product is $\tilde x\wedge^{\natural}\tilde y=\tfrac12(\tilde x^{\natural}\tilde y-\tilde y^{\natural}\tilde x)$.

## The Six Structures and the Idempotents

The idempotent equation is an equation on the **square operator** $\tilde x\mapsto\tilde x\star\tilde x$, so the six idempotent sets are read from the six squares, and the six squares are three:

| the square | the structures | at the two equal arguments |
|---|---|---|
| the plain square | $\mathrm{GPA}$, $\mathrm{SPA}$ | $(x_0^{2}-\lvert\mathbf x\rvert^{2})e_0+2x_0\mathbf x$ |
| the central square | $\mathrm{GQA}$, $\mathrm{SQA}$ | $N(\tilde x)e_0$ |
| the vanishing square | $\mathrm{APA}$, $\mathrm{AQA}$ | $0$ |

The origin is an idempotent of every structure, the product being linear and the zero element absorbing; the unit $e_0$ is an idempotent of the four structures that are not alternating, and it fails for the two cross products, whose square vanishes at the two equal arguments.

**Theorem (the six idempotent sets; quoted).** Among the six structures of the quaternion real space the idempotents are $\{0,e_0\}$ for $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$ and $\mathrm{SQA}$, and $\{0\}$ for $\mathrm{APA}$ and $\mathrm{AQA}$. Only two idempotent sets occur, the origin belongs to both, and no nontrivial idempotent exists except the unit $e_0$ of the four non-alternating structures.

*Proof.* For the general plain structure, $\tilde x^{2}=\tilde x$ reads $\tilde x(\tilde x-e_0)=0$; the plain algebra is a division algebra, so $\tilde x=0$ or $\tilde x=e_0$. For the general quaternionic structure, $\tilde x^{\natural}\tilde x=N(\tilde x)e_0=\tilde x$ puts $\tilde x$ in the scalar line, and the scalar equation $s^{2}=s$ gives $s\in\{0,1\}$. The symmetric plain structure has the plain square on the diagonal, $\tilde x\bullet\tilde x=\tilde x^{2}$, so its equation is the same as the general plain one and its set is the same; the symmetric quaternionic structure has the square $N(\tilde x)e_0$, so its equation is the same as the general quaternionic one. The two cross products are alternating, so $\tilde x\wedge\tilde x=0$ and $\tilde x\wedge^{\natural}\tilde x=0$ for every element, and the idempotent equation reads $\tilde x=0$.

The classification is sharp, and it reads the two ways a square operator can be too coarse to have a nontrivial solution. The **alternating** square vanishes identically, so it destroys the equation entirely and leaves the origin; the **definite scalar** square and the **plain** square vanish only at the origin, so the only solutions are the two idempotents of the scalar field, $0$ and $1$, read on the scalar line. The unit enters the equation because the square of $e_0$ is $e_0$ in the four structures that are not alternating, and it does not for the two cross products: $e_0\wedge e_0=0\neq e_0$.

The six are read one by one below; each names the product, its square and its idempotent set, and cites the article that owns them.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde x\tilde y$, and its square is the plain square, of scalar part $B(\tilde x)=x_0^{2}-\lvert\mathbf x\rvert^{2}$ and vector part $2x_0\mathbf x$. The idempotents are $0$ and $e_0$ alone: the equation $\tilde x(\tilde x-e_0)=0$ meets the division property of the plain algebra, and no isotropic direction of the plain form is real. The article is *Idempotents of the General Plain Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde x\bullet\tilde y$, and its square is the plain square, $\tilde x\bullet\tilde x=\tilde x^{2}$; the idempotent set is $\{0,e_0\}$, element for element that of $\mathrm{GPA}$, although the Jordan structure is not associative. The article is *Idempotents of the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the plain cross product $\tilde x\wedge\tilde y=\mathbf x\times\mathbf y$, alternating, so its square vanishes identically. The idempotent set is the origin alone, and $e_0$ is not an idempotent here. The article is *Idempotents of the Antisymmetric Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde x^{\natural}\tilde y$, and its square is the central element $N(\tilde x)e_0$; an idempotent is therefore central, $\tilde x=se_0$, and the equation on the centre, $s^{2}=s$, leaves $s\in\{0,1\}$. The idempotent set is the trivial pair. The article is *Idempotents of the General Quaternionic Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $N(\tilde x,\tilde y)e_0$, the quaternion form read as a product, and its square is the definite form, $\tilde x\star\tilde x=N(\tilde x)e_0$; the idempotent set is $\{0,e_0\}$, as for $\mathrm{GQA}$. The article is *Idempotents of the Symmetric Quaternionic Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the quaternionic cross product $\tilde x\wedge^{\natural}\tilde y$, alternating, so its square vanishes identically. The idempotent set is the origin alone. The article is *Idempotents of the Antisymmetric Quaternionic Algebra*.

**Remark (the sign of the square).** The two-point set is the set of idempotents of the scalar field $\mathbb{R}$, read on the scalar line, and the four structures inherit it because their square operator is the plain square or the definite scalar $N(\tilde x)e_0$, and neither has a real solution beyond the two. The pure elements, which are the zero divisors of the Jordan structure, have the square $-\lvert\mathbf x\rvert^{2}e_0$, of the wrong sign for a nontrivial idempotent: the construction $\tfrac12(e_0+\mathbf u)$ closes only if $\mathbf u$ is a root of $+e_0$, and a pure vector squares to $-\lvert\mathbf u\rvert^{2}e_0$, which is $+e_0$ for no real $\mathbf u$. So the zero divisors of the Jordan structure carry no idempotent with them.

## Results

The six idempotent sets are collected below, and the collapse against the biquaternion case is read last.

### The Six Idempotent Sets

| structure | product | square of $\tilde x$ | idempotents |
|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde x\tilde x$ | $(x_0^{2}-\lvert\mathbf x\rvert^{2})e_0+2x_0\mathbf x$ | $\{0,e_0\}$ |
| $\mathrm{SPA}$ | $\tilde x\bullet\tilde x$ | $(x_0^{2}-\lvert\mathbf x\rvert^{2})e_0+2x_0\mathbf x$ | $\{0,e_0\}$ |
| $\mathrm{APA}$ | $\tilde x\wedge\tilde x$ | $0$ | $\{0\}$ |
| $\mathrm{GQA}$ | $\tilde x^{\natural}\tilde x$ | $N(\tilde x)e_0$ | $\{0,e_0\}$ |
| $\mathrm{SQA}$ | $N(\tilde x,\tilde x)e_0$ | $N(\tilde x)e_0$ | $\{0,e_0\}$ |
| $\mathrm{AQA}$ | $\tilde x\wedge^{\natural}\tilde x$ | $0$ | $\{0\}$ |

Read down the last column, only two sets occur: the trivial pair $\{0,e_0\}$ for the four structures whose square is the plain square or the definite scalar, and the origin alone $\{0\}$ for the two whose square vanishes identically. The origin is the common member, and the unit $e_0$ is an idempotent of the four and of no other. The symmetric structure of each family repeats the row of its general partner, the two squares agreeing on the diagonal.

### The Contrast with the Biquaternion Case

The idempotent theory is coarser over $\mathbb{R}$ than over $\mathbb{C}$ because the real field has no scalar imaginary and the plain form is anisotropic.

| | the biquaternion space $\mathbb{B}$ | the quaternion space $\mathbb{H}$ |
|---|---|---|
| the plain product | $0$, $e_0$, $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$: a two-parameter family and a four-parameter family | $0$ and $e_0$ alone |
| the two cross products | $0$ alone | $0$ alone |

In the biquaternion space the plain product has the family $\tfrac12(e_0+\tilde\Xi i)$, where $\tilde\Xi$ runs over the roots of $-e_0$ and $i$ is the central imaginary of the coefficients, and the plain square therefore acquires a nontrivial idempotent for every isotropic direction; over $\mathbb{R}$ the central imaginary is absent and no isotropic direction exists, so the equation $\tilde x^{2}=\tilde x$ has only its central solutions, $0$ and $e_0$, and the family of the biquaternion plain structure collapses to the two-point set. The collapse is the same one the chapter records for the roots of a central value, in *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, above this article in this category, where the four-parameter root sets of the biquaternion sesqualgebras fall to the origin alone over $\mathbb{R}$.

## Summary

The idempotent of a structure is the element equal to its own square, and the six structures of the quaternion real space answer the equation with two sets alone. The general plain structure has the two-point set $\{0,e_0\}$, by the division property of the plain algebra; the symmetric plain structure keeps the same two points, the Jordan square being the plain square; the general quaternionic structure has the two-point set $\{0,e_0\}$, its square being the definite scalar $N(\tilde x)e_0$, whose only zeros are the two central ones; the symmetric quaternionic structure keeps the same two points, its square being the same definite scalar; and the two cross products have the origin alone, their square vanishing identically, so that $e_0$ is not an idempotent for them.

Only two idempotent sets occur among the six, the origin belongs to both, and no nontrivial idempotent exists except the unit $e_0$ of the four non-alternating structures. The theory is coarser than over the biquaternion complex space because the real field has no scalar imaginary and the plain form has no real isotropic direction: the biquaternion plain product carries a two-parameter family and a four-parameter family of nontrivial idempotents, and the quaternion plain product carries neither, though both have the same two cross products with the origin alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde x\star\tilde x=\tilde x$ | the idempotent equation of the structure $\star$ |
| $\{0,e_0\}$ | the idempotents of $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$ and $\mathrm{SQA}$ |
| $\{0\}$ | the idempotents of $\mathrm{APA}$ and $\mathrm{AQA}$ |
| $(x_0^{2}-\lvert\mathbf x\rvert^{2})e_0+2x_0\mathbf x$ | the plain square, the square of $\mathrm{GPA}$ and $\mathrm{SPA}$ |
| $N(\tilde x)e_0$ | the quaternionic square, the square of $\mathrm{GQA}$ and $\mathrm{SQA}$ |
| $0$ | the alternating square, the square of $\mathrm{APA}$ and $\mathrm{AQA}$ |
| $\tfrac12(e_0+\mathbf u)$ | the construction that would give a pure idempotent, and that closes for no real $\mathbf u$ |

## Further Reading

- The six owners, for the idempotent set of each structure: *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), *Idempotents of the Symmetric Plain Algebra* (`articles_maths/idempotents-of-the-symmetric-plain-algebra-of-quaternions.md`) and *Idempotents of the Antisymmetric Plain Algebra* (`articles_maths/idempotents-of-the-antisymmetric-plain-algebra-of-quaternions.md`); *Idempotents of the General Quaternionic Algebra* (`articles_maths/idempotents-of-the-general-quaternionic-algebra-of-quaternions.md`), *Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-symmetric-quaternionic-algebra-of-quaternions.md`) and *Idempotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`).
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`) and *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six structures, the six products and their laws.
- *Norm and Invertibility in the General Plain Algebra of Quaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), for the division property that leaves the plain idempotents at $0$ and $e_0$.
- *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/idempotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), the biquaternion comparison, for the two-parameter and four-parameter families that collapse here.
- *Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/nilpotents-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), below this article in this category, for the elements whose square vanishes.
- *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), above this article in this category, for the root equation at a general central value, and *Square Roots of Minus One, Zero and Plus One in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), above this article in this category, for the three named values.
