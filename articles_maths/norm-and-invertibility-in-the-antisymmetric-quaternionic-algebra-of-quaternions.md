# __Norm and Invertibility in the Antisymmetric Quaternionic Algebra__

## Introduction

This article studies the algebraic norm and the invertibility of the antisymmetric quaternionic multiplication

$$
\tilde p\diamond\tilde q=\tfrac12\bigl(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p\bigr)
=p_0\vec q-q_0\vec p-\vec p\times\vec q,
$$

the antisymmetric part of the general quaternionic product $\tilde p^{\natural}\tilde q$ (*Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*). The operation is $\mathbb{R}$-bilinear, alternating and vector valued, and it has no unit on either side.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*). For the block the scalar part vanishes identically, because every value is a pure vector; the algebraic norm of the operation is therefore the zero function, and the block is counted with **no algebraic norm** rather than with a zero one. The invertibility is a second and independent absence: the block has **no unit on either side**, hence no inverse and an empty group of units.

Two quadratic objects survive the loss of the scalar part. The first is the scalar-part form $\varphi(\tilde p,\tilde q)=p_0q_0$, of rank one and invariant, whose radical and isotropic cone are the vector subspace; the second is the operator trace form $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})=3A_0B_0-2(\vec A,\vec B)$, non-degenerate of signature $(1,3)$ and not invariant. Neither is central-valued, and the multiplicativity equation fails for both, and for the quaternion form $N$, at the single pair $(e_0,e_0)$.

**Conventions.** Throughout, $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ name elements of $\mathbb{H}$ with real coefficients, $(\vec p,\vec q)$ is the dot product and $\vec p\times\vec q$ the cross product of the vector parts, and $\tilde q^{\natural}=q_0e_0-\vec q$ is the quaternion conjugation; the bar is the identity and the star coincides with the natural conjugation, and the operation is written $\diamond$ and never $\wedge^{\natural}$ outside a citation. The image of the operation is the vector subspace $\mathrm{Vect}(\mathbb{H})$, of real dimension three, and the centre is $\mathbb{R}e_0$. The quaternion form is $N(\tilde p)=p_0^2+\lvert\vec p\rvert^2$; the operator $L_{\tilde p}$ is the left multiplication $\tilde x\mapsto\tilde p\diamond\tilde x$; and unqualified *unit* and *inverse* mean the unit and the inverse of $\diamond$.

**Boundaries.** The operation is *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, the definitions are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the unit table is *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the invariant forms are *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, the operator $L_{\tilde p}$ is *Annihilators of the Antisymmetric Quaternionic Algebra*, and the algebraic norm $N$ of the parent is the different form of *Norm and Invertibility in the General Quaternionic Algebra*.

## The Relative Definitions

**Definition (unit and inverse).** Let $\star$ be a product on $\mathbb{H}$. An element $\tilde e$ is a **left unit of $\star$** when $\tilde e\star\tilde x=\tilde x$ for every $\tilde x$, a **right unit** when $\tilde x\star\tilde e=\tilde x$ for every $\tilde x$, and a **unit** when it is both. When a unit exists, the **inverse of $\tilde x$** is the element $\tilde y$ with $\tilde x\star\tilde y=\tilde y\star\tilde x=\tilde e$, and the invertible elements form the **group of units**; without a two-sided unit the word inverse is not used, and an element is **regular** for a one-sided unit (*Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*).

## The Absence of a Unit

**Theorem (no unit).** The operation $\diamond$ has no left unit and no right unit; there is no $\tilde e$ with $\tilde e\diamond\tilde x=\tilde x$ for every $\tilde x$, and none with $\tilde x\diamond\tilde e=\tilde x$ for every $\tilde x$. Hence there is no two-sided unit.

*Proof.* The value of the operation is a sum of pure terms, $p_0\vec q$, $-q_0\vec p$ and $-\vec p\times\vec q$, so $\operatorname{Sc}(\tilde p\diamond\tilde q)=0$ for every pair. A left unit $\tilde e$ gives at $\tilde x=e_0$ the value $\tilde e\diamond e_0=-\vec e$, of zero scalar part, which would have to equal $e_0$, of scalar part one; impossible. A right unit gives at the same argument the value $e_0\diamond\tilde e=\vec e$, again of zero scalar part, which would have to equal $e_0$; impossible. So no element is a left unit and none is a right unit.

**Remark (the near unit $e_0$).** The element $e_0$ is not a unit, but its multiplication is the closest thing the block has to one: directly from the explicit form, $e_0\diamond\tilde q=\vec q$ and $\tilde q\diamond e_0=-\vec q$, so $e_0$ is a left identity on the vector subspace with the centre in its kernel, and on the right it is minus that projection. At $\tilde q=e_0$ both give $0$, so the unit equation $e_0\diamond e_0=e_0$ fails.

## The Absence of an Inverse

**Theorem (the inverse equation has no solution).** For no pair $\tilde x,\tilde y$ is $\tilde x\diamond\tilde y=e_0$, and for no pair is $\tilde x\diamond\tilde y$ a central element other than $0$. No element of $\mathbb{H}$ is invertible of the block, and the group of units of $\diamond$ is empty.

*Proof.* The left side is pure for every pair, so its scalar part vanishes, while $e_0$ has scalar part one; the equality $\tilde x\diamond\tilde y=e_0$ is impossible for every pair, and the same obstruction excludes every central value $ce_0$ with $c\neq0$. The inverse is defined against a two-sided unit, and the block has none, so no element is invertible and the group of units is empty.

**Remark (the image and the class of units).** The image of the operation is the whole vector subspace $\mathrm{Vect}(\mathbb{H})$, and the centre $\mathbb{R}e_0$ lies outside it except at the origin. The block is therefore **not unital** and not a division algebra; its class of units is empty, which is the reading of the entry $\mathrm{AQA}$ in the table of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

## The Algebraic Norm of the Block

**Definition (the algebraic norm of an operation).** Let $f$ be an operation on $\mathbb{H}$ with scalar-part form $\varphi(\tilde p,\tilde q)=\mathrm{Sc}\,f(\tilde p,\tilde q)$. The **algebraic norm of $f$** is the diagonal of that form, $\varphi_f(\tilde x)=\mathrm{Sc}\,f(\tilde x,\tilde x)$, and for an operation whose scalar part vanishes identically the algebraic norm is the zero function (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*).

**Theorem (the algebraic norm of the block is the zero function).** For the antisymmetric quaternionic multiplication, $\mathrm{Sc}(\tilde p\diamond\tilde q)=0$ for all $\tilde p,\tilde q$, hence $\varphi_{\diamond}(\tilde x)=0$ for all $\tilde x$. The algebraic norm of the operation is identically zero, and the block carries **no algebraic norm**.

*Proof.* The value $\tilde p\diamond\tilde q=p_0\vec q-q_0\vec p-\vec p\times\vec q$ is a sum of pure terms, hence of zero scalar part, so the diagonal $\operatorname{Sc}(\tilde x\diamond\tilde x)$ is the zero function; a vanishing quadratic form is not an algebraic norm.

**Remark (the two canonical quadratics of the block).** The operation being alternating, the square vanishes identically, $\tilde x\diamond\tilde x=0$, and the conjugated square is the pure vector $\tilde x\diamond\tilde x^{\natural}=-2x_0\vec x$. The conjugated square is central exactly when $x_0\vec x=0$, that is on the union of the centre $\mathbb{R}e_0$ and the vector subspace $\mathrm{Vect}(\mathbb{H})$, and at $\tilde x=e_0+e_1$ it takes the value $-2e_1$; neither canonical quadratic is central-valued at every element.

## The Two Surviving Quadratics

Two quadratic objects survive the loss of the scalar part, one from the scalar coordinates alone and one from the operator calculus.

**Proposition (the scalar-part form).** The form $\varphi(\tilde p,\tilde q)=p_0q_0$ is a symmetric bilinear form of $\mathbb{H}$, of rank one, invariant under the operation, $\varphi(\tilde p\diamond\tilde q,\tilde r)+\varphi(\tilde q,\tilde p\diamond\tilde r)=0$, with radical the vector subspace $\mathrm{Vect}(\mathbb{H})$ and isotropic cone the same subspace.

*Proof.* The form reads the product of the scalar coordinates, so it is symmetric and bilinear, of Gram matrix $\operatorname{diag}(1,0,0,0)$ and rank one. In each term of the invariance identity the first argument is a value of the block, hence of zero scalar part, so both terms vanish and the identity holds. The radical is the set of $\tilde x$ with $x_0y_0=0$ for every real $y_0$, that is the vector subspace of dimension three, which is also the isotropic cone, where $x_0^2=0$.

**Proposition (the operator trace form).** The form $K(\tilde A,\tilde B)=\operatorname{Tr}(L_{\tilde A}L_{\tilde B})$ is a symmetric bilinear form of $\mathbb{H}$ with $K(\tilde A,\tilde B)=3A_0B_0-2\sum_{k=1}^{3}A_kB_k=3A_0B_0-2(\vec A,\vec B)$, whose Gram matrix in the basis $(e_0,e_1,e_2,e_3)$ is $\operatorname{diag}(3,-2,-2,-2)$. It is non-degenerate of signature $(1,3)$, and it is **not invariant** under the operation.

*Proof.* The left multiplication $L_{\tilde A}$ has, in the basis $(e_0,e_1,e_2,e_3)$, the matrix with columns $\tilde A\diamond e_\nu$, namely rows $(0,0,0,0)$, $(-A_1,A_0,A_3,-A_2)$, $(-A_2,-A_3,A_0,A_1)$ and $(-A_3,A_2,-A_1,A_0)$. The trace of the product is $\sum_{i,k}(L_{\tilde A})_{ik}(L_{\tilde B})_{ki}$; the scalar coordinates contribute $3A_0B_0$ and the vector coordinates the negative pairing $-2(\vec A,\vec B)$, so the Gram matrix is $\operatorname{diag}(3,-2,-2,-2)$, non-degenerate of signature $(1,3)$. The invariance fails, with defect $K(\tilde A\diamond\tilde B,\tilde C)+K(\tilde B,\tilde A\diamond\tilde C)=-4A_0(\vec B,\vec C)+2B_0(\vec A,\vec C)+2C_0(\vec A,\vec B)$, which at the triple $(e_0,e_1,e_1)$ is $-4\neq0$.

**Remark (the operator invariants).** The operator $L_{\tilde p}$ has, at every element, trace $3p_0$ and determinant $0$, and at every nonzero element rank three with kernel the real line $\mathbb{R}\tilde p$; this is the content of *Annihilators of the Antisymmetric Quaternionic Algebra*, cited here and used below through $K(e_0,e_0)=3$.

## The Multiplicativity Failure at $(e_0,e_0)$

**Definition (multiplicativity).** A quadratic object $Q$ of the space is **multiplicative** for the operation when $Q(\tilde A\diamond\tilde B)=Q(\tilde A)Q(\tilde B)$ for all $\tilde A,\tilde B$. The equation is read at the single pair $(e_0,e_0)$ for the scalar-part form $\varphi$, the operator trace form $K$ and the quaternion form $N$.

**Proposition (the failure at the pair $(e_0,e_0)$).** At the pair $(\tilde A,\tilde B)=(e_0,e_0)$ the left side $Q(e_0\diamond e_0)$ vanishes for each of the three objects and the right side is $1$, $9$ and $1$ for $\varphi$, $K$ and $N$; the multiplicativity equation fails for all three.

| $Q$ | $Q(e_0\diamond e_0)$ | $Q(e_0)Q(e_0)$ | multiplicative at $(e_0,e_0)$ |
|---|---|---|---|
| $\varphi(\tilde x)=x_0^2$ | $0$ | $1$ | no |
| $K(\tilde x,\tilde x)=3x_0^2-2\lvert\vec x\rvert^2$ | $0$ | $9$ | no |
| $N(\tilde x)=x_0^2+\lvert\vec x\rvert^2$ | $0$ | $1$ | no |

*Proof.* The square of $e_0$ in the block is $e_0\diamond e_0=0$ by alternation, and every quadratic object annihilates the origin, so the left side is zero in the three rows. On the right, $\varphi(e_0)=1$ gives $1$, $K(e_0,e_0)=3$ gives $9$, and $N(e_0)=1$ gives $1$. The three right-hand values are distinct, $\varphi$ forgetting the vector part, $K$ weighting the scalar coordinate by three and the vector coordinates by minus two, and $N$ weighting all four by one; since the two sides differ in each row, none is multiplicative.

## The Invertibility Criterion Is Not Transferred

**Remark (the criterion of the parent is not read here).** The general quaternionic product $\tilde p^{\natural}\tilde q$ is left-unital with left unit $e_0$, and its invertibility is decided by the non-vanishing of its algebraic norm $N$, the diagonal of $\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q)$ (*Norm and Invertibility in the General Quaternionic Algebra*). That form belongs to a different product, and the block has neither a unit to invert against nor an algebraic norm of its own, so no criterion is transferred. The absence is total in the further sense that every nonzero element is a zero divisor of the block (*Zero Divisors of the Antisymmetric Quaternionic Algebra*), so the block is as far from a division algebra as its dimension allows.

## Summary

The antisymmetric quaternionic multiplication $\tilde p\diamond\tilde q=p_0\vec q-q_0\vec p-\vec p\times\vec q$ has no unit on either side, hence no invertible element and an empty group of units, and the inverse equation $\tilde x\diamond\tilde y=e_0$ has no solution because every value is a pure vector. The algebraic norm of the operation is the diagonal of its scalar-part form; the scalar part vanishes identically, so the diagonal is the zero function, and a vanishing quadratic form is not an algebraic norm: the block carries **no algebraic norm**. The square vanishes identically and the conjugated square is the pure vector $-2x_0\vec x$, central exactly on the centre and the vector subspace. Two quadratic objects survive: the scalar-part form $\varphi(\tilde p,\tilde q)=p_0q_0$, of rank one, invariant, radical and isotropic cone the vector subspace; and the operator trace form $K(\tilde A,\tilde B)=3A_0B_0-2(\vec A,\vec B)$, non-degenerate of signature $(1,3)$ and not invariant. Neither is multiplicative, and at $(e_0,e_0)$ the left side vanishes while the right side is $1$, $9$, $1$ for $\varphi$, $K$ and $N$. The norm $N$ of the parent product is a form of a different product; no invertibility criterion is transferred, and the place of both the norm and the inverse is taken by their absence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\vec q-q_0\vec p-\vec p\times\vec q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\mathrm{Sc}(\tilde p\diamond\tilde q)=0$ | the scalar part of the block vanishes identically |
| $\varphi_{\diamond}(\tilde x)=0$ | the algebraic norm of the block, the zero function; the block carries no algebraic norm |
| $\tilde x\diamond\tilde x=0$, $\tilde x\diamond\tilde x^{\natural}=-2x_0\vec x$ | the square vanishes; the conjugated square is a pure vector |
| $\varphi(\tilde p,\tilde q)=p_0q_0$ | the scalar-part form, rank one, invariant, radical the vector subspace |
| $K(\tilde A,\tilde B)=3A_0B_0-2(\vec A,\vec B)$ | the operator trace form, non-degenerate of signature $(1,3)$, not invariant |
| $L_{\tilde p}$: trace $3p_0$, determinant $0$, rank $3$, kernel $\mathbb{R}\tilde p$ | the left multiplication and its invariants |
| no unit, no inverse, no group of units | the absence carried by the block |

## Further Reading

- *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternion-r-space.md`), for the algebraic norm as the diagonal of a scalar-part form, and for the convention that counts a vanishing diagonal as no algebraic norm.
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the operation, its class, its image and the absence of a unit.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternions.md`), for the algebraic norm $N$ of the quaternionic product, which is not the form of this block.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the invariant forms of the block and the failure of invariance of the trace form.
- *Annihilators of the Antisymmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the left multiplication operator, its invariants and its kernel.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the unit, the inverse, the reduced norm and the trace form of a regular representation.
