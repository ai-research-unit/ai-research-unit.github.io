# __The Idempotents of the Six Structures__

## Introduction

An idempotent of a structure is an element equal to its own square. The quaternion space carries six structures, and the idempotent set is read here for all six. The answer is a two-point set for four of them and the single origin for the two cross products, and the comparison with the biquaternion case explains why the answer is so coarse. The six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the products are *The 6 Products of the Quaternion Real Space*, and the general definitions are *Definitions for the Study of the 6 Algebraic Structures*, all above this article in this category.

## The Idempotents of a Structure

**Definition.** For a product $\star$ on $\mathbb{H}$ an **idempotent** is an element $\tilde\pi$ with
$$
\tilde\pi\star\tilde\pi=\tilde\pi ,
$$
and a **nontrivial** idempotent is one different from the origin. The origin is an idempotent of every structure, because the product is linear and the zero element absorbs. An idempotent of a structure without a unit has no reason to be connected with the unit of the algebra $\mathbb{H}$, and the two cross products show that it need not be.

The idempotent equation is an equation on the **square operator** $\tilde x\mapsto\tilde x\star\tilde x$, so the idempotents of the six structures are read from their six squares. The six squares are two, repeated:
$$
\tilde x\tilde x=\tilde x\bullet\tilde x=(x_0^2-|\mathbf x|^2)e_0+2x_0\mathbf x ,\qquad
\tilde x^{\natural}\tilde x=N(\tilde x)e_0=N(\tilde x,\tilde x)e_0 ,
$$
$$
\tilde x\wedge\tilde x=0 ,\qquad
\tilde x\wedge^{\natural}\tilde x=0 ,
$$
the first line because the Jordan product agrees with the plain product on the diagonal, and the quaternionic structure by the definition of the norm and of the form.

## The Four Structures with the Two-Point Set

**Theorem (the plain and quaternionic structures).** The idempotents of the general plain structure are $\{0,e_0\}$; those of the general quaternionic structure are $\{0,e_0\}$; those of the symmetric plain structure are $\{0,e_0\}$; and those of the symmetric quaternionic structure are $\{0,e_0\}$. No structure of the four has a nontrivial idempotent besides the unit.

*Proof.* For the general plain structure, $\tilde x^2=\tilde x$ reads $\tilde x(\tilde x-e_0)=0$; the plain algebra is a division algebra, so $\tilde x=0$ or $\tilde x=e_0$. For the general quaternionic structure, $\tilde x^{\natural}\tilde x=N(\tilde x)e_0=\tilde x$ puts $\tilde x$ in the scalar line, and the scalar equation $s^2=s$ gives $s\in\{0,1\}$. The symmetric plain structure has the plain square on the diagonal, $\tilde x\bullet\tilde x=\tilde x^2$, so its equation is the same as the general plain one and its set is the same. The symmetric quaternionic structure has the square $N(\tilde x)e_0$, so its equation is the same as the general quaternionic one.

**Remark (the sign of the square).** The two-point set is the set of idempotents of the scalar field $\mathbb{R}$, embedded as the scalar line; the four structures inherit it because their square operator either is the plain square, whose only central solutions are $0$ and $e_0$, or is the definite scalar $N(\tilde x)e_0$, whose only solutions are the same two. The pure elements, which are the zero divisors of the Jordan structure, have the square $-\mathbf u\cdot\mathbf u\,e_0=-|\mathbf u|^2e_0$, the negative of what a nontrivial idempotent would need: the construction $\tfrac12(e_0+\mathbf u)$ closes only if $\mathbf u$ is a root of $+e_0$, and no nonzero pure element is. So the zero divisors of the block carry no idempotent with them.

## The Two Alternating Structures

**Theorem (the cross products).** The idempotents of the plain cross product and of the quaternionic cross product are both the single origin, $\{0\}$.

*Proof.* Both products are alternating, so $\tilde x\wedge\tilde x=0$ and $\tilde x\wedge^{\natural}\tilde x=0$ for every element; the idempotent equation therefore reads $\tilde x=0$. The origin is an idempotent of every structure, and it is the only one here.

The two cross products are the only structures of the six with a one-point idempotent set, and they are also the only ones whose product is alternating, so the square vanishes identically and nothing survives the equation. The presence of a unit in the other four is what gives them the extra point $e_0$, and the two cross products, which have no unit, do not even have that point: $e_0$ is not idempotent for them, since $e_0\wedge e_0=0\neq e_0$.

## The Six Idempotent Sets Side by Side

| structure | product | square of $\tilde x$ | idempotents |
|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde x\tilde x$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $\{0,e_0\}$ |
| $\mathrm{GQA}$ | $\tilde x^{\natural}\tilde x$ | $N(\tilde x)e_0$ | $\{0,e_0\}$ |
| $\mathrm{SPA}$ | $\tilde x\bullet\tilde x$ | $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | $\{0,e_0\}$ |
| $\mathrm{SQA}$ | $N(\tilde x,\tilde x)e_0$ | $N(\tilde x)e_0$ | $\{0,e_0\}$ |
| $\mathrm{APA}$ | $\tilde x\wedge\tilde x$ | $0$ | $\{0\}$ |
| $\mathrm{AQA}$ | $\tilde x\wedge^{\natural}\tilde x$ | $0$ | $\{0\}$ |

**Theorem (the six idempotent sets).** Among the six structures the idempotents are $\{0,e_0\}$ for $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{SPA}$ and $\mathrm{SQA}$, and $\{0\}$ for $\mathrm{APA}$ and $\mathrm{AQA}$. Only two idempotent sets occur, and the origin belongs to both.

*Proof.* The four structures of the first group are the theorem of the plain and quaternionic structures, and the two of the second group are the theorem of the cross products; the origin is an idempotent of every structure, so the two sets contain it and the second set is a subset of the first.

**Remark (the contrast with the biquaternion case).** The idempotent theory is coarser over $\mathbb{R}$ than over $\mathbb{C}$ because the real field has no scalar imaginary and the plain form is anisotropic. In the biquaternion chapter the plain product has infinitely many idempotents, of the form $\tfrac12(e_0+\Xi i)$ with $\Xi$ a root of $-e_0$ and $i$ the central imaginary of the coefficients, and the plain square therefore acquires a nontrivial idempotent for every isotropic direction; over $\mathbb{R}$ the central imaginary is absent and no isotropic direction exists, so the equation $\tilde x^2=\tilde x$ has only its central solutions, $0$ and $e_0$, and the four-parameter family of the biquaternion plain structure collapses to the two-point set. The collapse is the same one the chapter records for the roots of a central value, in *The Square Roots of a Central Value in the Six Structures*, below this article in this category.

## Summary

The idempotent of a structure is an element equal to its square, read from the square operator. The four structures whose square is the plain square or the definite scalar $N(\tilde x)e_0$ — the general plain, the general quaternionic, the symmetric plain and the symmetric quaternionic — have the two-point idempotent set $\{0,e_0\}$, exactly the idempotents of the scalar field; the two cross products, whose square vanishes identically, have the one-point set $\{0\}$, and the unit $e_0$ is not idempotent for them. So only two idempotent sets occur among the six, the origin belongs to both, and no nontrivial idempotent is attached to a zero divisor of the Jordan structure, whose pure elements have the negative scalar square $-|\mathbf u|^2e_0$. Over $\mathbb{C}$ the plain square would acquire a nontrivial idempotent along every isotropic direction; over $\mathbb{R}$ there is no isotropic direction and no central imaginary, and the theory collapses to the two-point set.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\pi\star\tilde\pi=\tilde\pi$ | the idempotent equation of the structure $\star$ |
| $\{0,e_0\}$ | the idempotents of GPA, GQA, SPA and SQA |
| $\{0\}$ | the idempotents of APA and AQA |
| $(x_0^2-\lvert\mathbf x\rvert^2)e_0+2x_0\mathbf x$ | the plain square, the square of GPA and SPA |
| $N(\tilde x)e_0$ | the quaternionic square, the square of GQA and SQA |
| $0$ | the alternating square, the square of APA and AQA |
| $\tfrac12(e_0+\mathbf u)$ | the non-idempotent attached to a pure zero divisor $\mathbf u$ |

## Further Reading

- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra-of-quaternions.md`), for the idempotents of the plain product, folded into the block of the general plain algebra.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra-of-quaternions.md`), for the idempotents of the Jordan structure.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures and their laws.
- *The Square-Zero Elements of the Six Structures* (`articles_maths/the-square-zero-elements-of-the-six-structures.md`), below this article in this category, for the elements whose square vanishes.
- *The Square Roots of a Central Value in the Six Structures* (`articles_maths/the-square-roots-of-a-central-value-in-the-six-structures.md`), below this article in this category, for the roots of the central values.
