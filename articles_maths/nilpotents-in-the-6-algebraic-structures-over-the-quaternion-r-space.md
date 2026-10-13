# __Nilpotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

The **square-zero set** of a product $\star$ on the quaternion space $\mathbb{H}$ is the solution set of the equation

$$
\tilde\nu\star\tilde\nu=0 ,
$$

and a **square-zero element**, or **nilpotent of index two**, is a nonzero member, written $\tilde\nu$ after the convention of *Conventions in Mathematics*. The equation names a product, so the six structures of the space carry six square-zero sets, and the answer is coarse: the origin alone for four of them and the whole space for the two cross products. A nonzero square-zero element is at once a zero divisor of the structure, its own annihilating partner, and a root of the central value $0$, and where these three classes agree is the end of the article.

**The six names.** The space carries six products, so the generic definition poses six questions; this article answers them once for all six. Each product has a three-letter code: the first letter is the operation, $\mathrm G$ the general product and $\mathrm S$, $\mathrm A$ its symmetric and antisymmetric parts; the second is the product of the family, $\mathrm P$ the plain one and $\mathrm Q$ the quaternionic one, whose first slot is read through the natural conjugation; and the third letter is the same one for the six, $\mathrm A$ the algebra over $\mathbb{R}$. The six are read in the two families of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*,

| the family | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |

and every table of the article follows this order, family by family and, inside a family, general then symmetric then antisymmetric.

**Scope and owners.** This article owns the comparison of the six square-zero sets and the reading of the three classes. The sets themselves stay owned by the six articles *Nilpotents of the …*, cited one by one in §*The Six Structures and the Square-Zero Sets*. The products are *The 6 Products of the Quaternion Real Space* and the structures *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, whose codes are used throughout; the vocabulary, the nilpotent stated once for a general product, is *Definitions for the Study of the 6 Algebraic Structures*; the division property is *Norm and Invertibility in the General Plain Algebra*; the zero divisors are *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the roots of $0$ are *Square Roots of Minus One, Zero and Plus One in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* and *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; and the biquaternion case is *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** $\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_0=1$; a general element is $\tilde x=x_0e_0+\mathbf x$ with $x_0\in\mathbb{R}$ and $\mathbf x=\sum_kx_ke_k$; the natural conjugation is $\tilde x^{\natural}=x_0-\mathbf x$; the **plain square** is $\tilde x^{2}=(x_0^{2}-\lvert\mathbf x\rvert^{2})e_0+2x_0\mathbf x$, of scalar part the indefinite plain form $B(\tilde x)=x_0^{2}-\lvert\mathbf x\rvert^{2}$; and the **quaternionic square** is $\tilde x^{\natural}\tilde x=N(\tilde x)e_0$, of the definite quaternion form $N(\tilde x)=x_0^{2}+\lvert\mathbf x\rvert^{2}$. The plain product is $\tilde p\tilde q$, the Jordan product is $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$, the plain cross product is $\tilde p\wedge\tilde q=\mathbf p\times\mathbf q$, and the quaternionic cross product is $\tilde p\wedge^{\natural}\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$.

## The Six Structures and the Square-Zero Sets

The square-zero equation is the **diagonal equation**, so the square-zero set is read from the six squares, and the six around the diagonal are three:

| structure | square of $\tilde x$ | square-zero equation |
|---|---|---|
| $\mathrm{GPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $x_0^2-\lvert\mathbf x\rvert^2=0$ and $2x_0\mathbf x=0$ |
| $\mathrm{SPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $x_0^2-\lvert\mathbf x\rvert^2=0$ and $2x_0\mathbf x=0$ |
| $\mathrm{APA}$ | $0$ | satisfied identically |
| $\mathrm{GQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=0$ |
| $\mathrm{SQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=0$ |
| $\mathrm{AQA}$ | $0$ | satisfied identically |

The diagonal is the plain square for the plain product, the norm times $e_0$ for the quaternionic product, and zero for the two cross products; this is the same three-fold splitting that governs the roots of a central value, read at the value $0$.

**Theorem (the six square-zero sets; quoted).** Among the six structures the square-zero set is $\{0\}$ for $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$ and $\mathrm{SQA}$, and it is all of $\mathbb{H}$ for $\mathrm{APA}$ and $\mathrm{AQA}$. Only two square-zero sets occur, and no structure of the six has a square-zero set that is neither a point nor the whole space.

*Proof.* For the general plain structure, if $\tilde\nu^2=0$ and $\tilde\nu\neq0$ then $\tilde\nu$ is invertible and multiplication on the left by $\tilde\nu^{-1}$ gives $\tilde\nu=0$, a contradiction; hence the only solution is the origin. The plain square is indefinite, of isotropic cone real only after complexification, yet the two equations $x_0^2-\lvert\mathbf x\rvert^2=0$ and $2x_0\mathbf x=0$ together force $\tilde x=0$. For the general quaternionic structure, $\tilde\nu^{\natural}\tilde\nu=N(\tilde\nu)e_0$ and the norm is a sum of four real squares, so $N(\tilde\nu)=0$ forces $\tilde\nu=0$. The two symmetric structures have the same square on the diagonal, the Jordan square being the plain square and the symmetrised quaternionic square being the norm times $e_0$, so they keep the same one-point sets. Both cross products are alternating, so $\tilde x\wedge\tilde x=0$ and $\tilde x\wedge^{\natural}\tilde x=0$ for every element, and the square-zero equation is satisfied identically. The assertion that no third set occurs is the classification of the squares: the square of a structure of the six is the plain square, the norm times $e_0$, or zero; the norm is definite and the plain square is anisotropic over $\mathbb{R}$, of isotropic cone the origin, so the first two have the origin as their only zero.

The classification is sharp, and it reads the two ways a square can fail to be invertible away from the origin. The **alternating** square vanishes identically, so it makes every element square zero; the **plain** square and the **definite scalar** square vanish only at the origin, the first because the real space has no isotropic direction, the second because the norm is a sum of squares. The four structures of the first kind are the ones whose square is zero only at the origin, and they have no nilpotent at all.

The six are read one by one below; each names the product, its diagonal and its square-zero set, and cites the article that owns them.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde p\tilde q$, and its diagonal is the plain square, of scalar part $B(\tilde x)=x_0^{2}-\lvert\mathbf x\rvert^{2}$ and vector part $2x_0\mathbf x$. The square-zero set is $\{0\}$ alone, by the division property of the plain algebra. The article is *Nilpotents of the General Plain Algebra*.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product $\tilde p\bullet\tilde q$, and its diagonal is the plain square, $\tilde x\bullet\tilde x=\tilde x^{2}$, whose only real zero is the origin. The square-zero set is $\{0\}$ alone, element for element that of $\mathrm{GPA}$. The article is *Nilpotents of the Symmetric Plain Algebra*.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the plain cross product $\tilde p\wedge\tilde q=\mathbf p\times\mathbf q$, alternating, so its diagonal vanishes identically. The square-zero set is the whole space, and every nonzero element is a nilpotent. The article is *Nilpotents of the Antisymmetric Plain Algebra*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde p^{\natural}\tilde q$, and its diagonal is the central element $N(\tilde x)e_0$; the equation is the vanishing of the norm, a sum of four real squares, so only the origin vanishes. The square-zero set is $\{0\}$ alone. The article is *Nilpotents of the General Quaternionic Algebra*.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is $N(\tilde p,\tilde q)e_0$, the quaternion form read as a product, and its diagonal is the definite norm, $\tilde x\star\tilde x=N(\tilde x)e_0$. The square-zero set is $\{0\}$ alone, as for $\mathrm{GQA}$. The article is *Nilpotents of the Symmetric Quaternionic Algebra*.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the quaternionic cross product $\tilde p\wedge^{\natural}\tilde q$, alternating, so its diagonal vanishes identically. The square-zero set is the whole space. The article is *Nilpotents of the Antisymmetric Quaternionic Algebra*.

## Results

The six square-zero sets are collected below, and the comparison with the zero divisors and the roots of $0$ is read last.

### The Six Square-Zero Sets

| structure | product | square of $\tilde x$ | square-zero set | reason |
|---|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde p\tilde q$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $\{0\}$ | division |
| $\mathrm{SPA}$ | $\tilde p\bullet\tilde q$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $\{0\}$ | the plain square |
| $\mathrm{APA}$ | $\tilde p\wedge\tilde q$ | $0$ | $\mathbb{H}$ | alternation |
| $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | $N(\tilde x)e_0$ | $\{0\}$ | definiteness of the norm |
| $\mathrm{SQA}$ | $N(\tilde p,\tilde q)e_0$ | $N(\tilde x)e_0$ | $\{0\}$ | definiteness of the norm |
| $\mathrm{AQA}$ | $\tilde p\wedge^{\natural}\tilde q$ | $0$ | $\mathbb{H}$ | alternation |

Read down the fourth column, only two sets occur: the origin alone $\{0\}$ for the four structures whose square is the plain square or the definite norm, and the whole space $\mathbb{H}$ for the two alternating structures. The origin is the common member, and it is square zero without being a nilpotent, the nilpotents being the nonzero members. The symmetric structure of each family repeats the row of its general partner, the two squares agreeing on the diagonal.

### The Three Classes

The square-zero elements, the zero divisors and the roots of $0$ are three classes attached to a structure, and the comparison of the six structures reads them together:

| structure | square-zero set | zero-divisor set | roots of $0$ | the three agree |
|---|---|---|---|---|
| $\mathrm{GPA}$ | $\{0\}$ | $\varnothing$ | $\{0\}$ | trivial |
| $\mathrm{SPA}$ | $\{0\}$ | $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | $\{0\}$ | no |
| $\mathrm{APA}$ | $\mathbb{H}$ | $\mathbb{H}\setminus\{0\}$ | $\mathbb{H}$ | yes, off the origin |
| $\mathrm{GQA}$ | $\{0\}$ | $\varnothing$ | $\{0\}$ | trivial |
| $\mathrm{SQA}$ | $\{0\}$ | $\mathbb{H}\setminus\{0\}$ | $\{0\}$ | no |
| $\mathrm{AQA}$ | $\mathbb{H}$ | $\mathbb{H}\setminus\{0\}$ | $\mathbb{H}$ | yes, off the origin |

**Theorem (the comparison of the three classes).** For the two antisymmetric structures the three classes coincide away from the origin: a nonzero element is square zero exactly when it is a zero divisor, and the square-zero set is also the root set of $0$. For the four other structures the three classes do not coincide: the square-zero set is the origin alone, while the zero-divisor set is empty for the two general structures, the pure cone for the symmetric plain structure, and the punctured space for the symmetric quaternionic structure.

*Proof.* A nonzero square-zero element is a zero divisor, its own partner, and a root of $0$; the converse fails in the four structures whose square-zero set is the origin alone, where that set is a point while the zero-divisor set is one of the three other values computed in *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, above this article in this category. For the antisymmetric structures the square vanishes identically, so the square-zero set and the root set of $0$ are both $\mathbb{H}$, and the zero-divisor set is $\mathbb{H}$ minus the origin, which is the same set with the origin removed.

The comparison is the visible content of the classification. The three classes collapse onto one another exactly on the alternating structures, where the diagonal of the product is identically zero; they separate as soon as the diagonal does not vanish identically, and the gap between them measures the difference between the vanishing of a square and the vanishing of a product. This is the same gap the symmetric quaternionic structure exhibits most sharply, its square nonzero on every nonzero element while every nonzero element is a zero divisor: the vanishing of a *product* does not require the vanishing of a *square*.

## Summary

The square-zero set of a structure is the set of elements whose square vanishes, and the nilpotents are its nonzero members. The general plain structure has the origin alone as square-zero set, by the division property of the plain product; the symmetric plain structure keeps the same one-point set, the Jordan square being the plain square, whose only real zero is the origin; the antisymmetric plain structure, being alternating, has the whole space for square-zero set; the general quaternionic structure has the origin alone, by the definiteness of the norm; the symmetric quaternionic structure keeps the same one-point set, its square being the definite norm $N(\tilde x)e_0$; and the antisymmetric quaternionic structure has the whole space, being alternating. So only two square-zero sets occur among the six, the origin and the whole space, and no structure has an intermediate set. The three classes of the square-zero elements, the zero divisors and the roots of $0$ coincide away from the origin exactly for the two antisymmetric structures; for the four other structures the square-zero set is the origin alone while the zero-divisor set is empty, the pure cone, or the punctured space.

## Summary of Notation

| symbol | meaning |
|---|---|
| square-zero element, nilpotent of $\star$ | $\tilde\nu\neq0$ with $\tilde\nu\star\tilde\nu=0$ |
| $\{0\}$ | the square-zero set of GPA, SPA, GQA and SQA |
| $\mathbb{H}$ | the square-zero set of APA and AQA |
| $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | the plain square, the diagonal of GPA and SPA |
| $N(\tilde x)e_0$ | the quaternionic square, the diagonal of GQA and SQA |
| $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$ | the zero-divisor set of SPA, for the comparison |

## Further Reading

- The six owners, for the square-zero set of each structure: *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra-of-quaternions.md`), *Nilpotents of the Symmetric Plain Algebra* (`articles_maths/nilpotents-of-the-symmetric-plain-algebra-of-quaternions.md`) and *Nilpotents of the Antisymmetric Plain Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-plain-algebra-of-quaternions.md`); *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra-of-quaternions.md`), *Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternions.md`) and *Nilpotents of the Antisymmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`).
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the division property.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the nilpotents of the plain product.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`) and *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six structures, the six products and their laws.
- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), below this article in this category, for the nilpotent stated once for a general product.
- *Square Roots of Minus One, Zero and Plus One in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), above this article in this category, for the roots of $0$ read at the three values, and *Square Roots of a General Element in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/square-roots-of-a-general-element-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), above this article in this category, for the root equation at a general central value.
- *Zero Divisors in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-6-algebraic-structures-over-the-quaternion-r-space.md`), above this article in this category, for the zero divisors and the three classes.
- *Nilpotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/nilpotents-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), the biquaternion comparison, for the four square-zero sets and the twelve-row reading that the real space collapses here.
