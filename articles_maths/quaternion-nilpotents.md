# __Nilpotents__

## Introduction

The square-zero set of a structure is the set of elements whose square in that structure vanishes, and a square-zero element, or nilpotent, is a nonzero member of it. The quaternion space carries six structures, and the set is read here for all six. It is the origin alone for four of them and the whole space for the two cross products, and the comparison with the zero divisors and the roots of $0$ is the end of the article. The products are *The 6 Products of the Quaternion Real Space*, the structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the definitions are *Definitions for the Study of the 6 Algebraic Structures*, all above this article in this category.

## Square-Zero Elements of a Structure

**Definition.** Let $\star$ be a product on $\mathbb{H}$. The **square-zero set** of $\star$ is the solution set of
$$
\tilde\nu\star\tilde\nu=0 ,
$$
and a **square-zero element**, or **nilpotent**, is a nonzero member, written $\tilde\nu$ after the convention of *Conventions in Mathematics*. A nonzero square-zero element is at once a zero divisor of the structure, its own annihilating partner, and a root of the central value $0$: the square-zero set with the origin removed lies in the zero-divisor set and in the root set of $0$. The reverse inclusions fail in general, and where they hold is the last section.

## The Six Diagonals

The square-zero equation is the diagonal equation, so the square-zero set is read from the six squares of *Idempotents*:

| structure | square of $\tilde x$ | square-zero equation |
|---|---|---|
| $\mathrm{GPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $x_0^2-\lvert\mathbf x\rvert^2=0$ and $2x_0\mathbf x=0$ |
| $\mathrm{SPA}$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $x_0^2-\lvert\mathbf x\rvert^2=0$ and $2x_0\mathbf x=0$ |
| $\mathrm{APA}$ | $0$ | satisfied identically |
| $\mathrm{GQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=0$ |
| $\mathrm{SQA}$ | $N(\tilde x)e_0$ | $N(\tilde x)=0$ |
| $\mathrm{AQA}$ | $0$ | satisfied identically |

The diagonal is the plain square for the plain product, the norm times $e_0$ for the quaternionic product, and zero for the two cross products; this is the same three-fold splitting that governs the roots of a central value, read at the value $0$.

## The Four Structures with the Origin Alone

**Theorem (the plain and quaternionic structures).** The square-zero set of the general plain structure and of the symmetric plain structure is $\{0\}$; the square-zero set of the general quaternionic structure and of the symmetric quaternionic structure is $\{0\}$. None of the four has a nilpotent.

*Proof.* For the general plain structure, if $\tilde\nu^2=0$ and $\tilde\nu\neq0$ then $\tilde\nu$ is invertible and multiplication on the left by $\tilde\nu^{-1}$ gives $\tilde\nu=0$, a contradiction; hence the only solution is the origin. For the general quaternionic structure, $\tilde\nu^{\natural}\tilde\nu=N(\tilde\nu)e_0$ and the norm is a sum of four real squares, so $N(\tilde\nu)=0$ forces $\tilde\nu=0$. The symmetric structures have the same square on the diagonal, the Jordan square being the plain square and the symmetrised quaternionic square being the norm times $e_0$, so they keep the same one-point set.

The proof is the division property, quoted from *The Specificities of the General Plain Algebra* and *Norm and Invertibility in the General Plain Algebra*, above this article in this category. The four structures are the ones whose square is zero only at the origin: the plain square is indefinite, of isotropic cone real only after complexification, yet the two equations $x_0^2-|\mathbf x|^2=0$ and $2x_0\mathbf x=0$ together force $\tilde x=0$; and $N(\tilde x)$ is a sum of four squares, positive off the origin. The origin is the only real zero of each.

## The Two Alternating Structures

**Theorem (the cross products).** The square-zero set of the plain cross product and of the quaternionic cross product is all of $\mathbb{H}$; every element is square zero, and every nonzero element is a nilpotent.

*Proof.* Both products are alternating, so $\tilde x\wedge\tilde x=0$ and $\tilde x\wedge^{\natural}\tilde x=0$ for every element; the square-zero equation is satisfied identically and the solution set is the whole space.

The two cross products are the only structures whose square-zero set is not a point, and the reason is that their square vanishes for all arguments. The set contains the origin, which is square zero but not a nilpotent, the nilpotents being the nonzero members.

## The Six Square-Zero Sets Side by Side

| structure | product | square of $\tilde x$ | square-zero set | reason |
|---|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde p\tilde q$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $\{0\}$ | division |
| $\mathrm{SPA}$ | $\tilde p\bullet\tilde q$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $\{0\}$ | the plain square |
| $\mathrm{APA}$ | $\tilde p\wedge\tilde q$ | $0$ | $\mathbb{H}$ | alternation |
| $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | $N(\tilde x)e_0$ | $\{0\}$ | definiteness of the norm |
| $\mathrm{SQA}$ | $N(\tilde p,\tilde q)e_0$ | $N(\tilde x)e_0$ | $\{0\}$ | definiteness of the norm |
| $\mathrm{AQA}$ | $\tilde p\wedge^{\natural}\tilde q$ | $0$ | $\mathbb{H}$ | alternation |

**Theorem (the six square-zero sets).** Among the six structures the square-zero set is $\{0\}$ for $\mathrm{GPA}$, $\mathrm{SPA}$, $\mathrm{GQA}$ and $\mathrm{SQA}$, and it is all of $\mathbb{H}$ for $\mathrm{APA}$ and $\mathrm{AQA}$. Only two square-zero sets occur, and no structure of the six has a square-zero set that is neither a point nor the whole space.

*Proof.* The rows of $\mathrm{SPA}$ and $\mathrm{SQA}$ repeat those of $\mathrm{GPA}$ and $\mathrm{GQA}$, the symmetric structures sharing the square of their general counterparts, and the rows of $\mathrm{APA}$ and $\mathrm{AQA}$ are the theorem of the cross products. The assertion that no third set occurs is the classification of the squares: the square of a structure of the six is the plain square, the norm times $e_0$, or zero; the norm is definite and the plain square is anisotropic over $\mathbb{R}$, of isotropic cone the origin, so the first two have the origin as their only zero.

## The Three Classes

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

*Proof.* A nonzero square-zero element is a zero divisor, its own partner, and a root of $0$; the converse fails in the four structures whose square-zero set is the origin alone, where that set is a point while the zero-divisor set is one of the three other values computed in *Zero Divisors*, above this article in this category. For the antisymmetric structures the square vanishes identically, so the square-zero set and the root set of $0$ are both $\mathbb{H}$, and the zero-divisor set is $\mathbb{H}$ minus the origin, which is the same set with the origin removed.

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

- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the division property.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the nilpotents of the plain product.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures.
- *Square Roots of Minus One, Zero and Plus One* (`articles_maths/quaternion-square-roots-of-minus-one-zero-and-plus-one.md`), above this article in this category, for the roots of $0$ read at the three values, and *Square Roots of a General Element* (`articles_maths/quaternion-square-roots-of-a-general-element.md`), above this article in this category, for the root equation at a general central value.
- *Zero Divisors* (`articles_maths/quaternion-zero-divisors.md`), above this article in this category, for the zero divisors.
