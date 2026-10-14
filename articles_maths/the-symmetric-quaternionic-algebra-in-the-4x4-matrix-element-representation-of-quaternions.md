# __The Symmetric Quaternionic Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

The quaternion algebra acts on itself by left multiplication, and the resulting $4\times4$ real matrices form its left regular representation. In that model the symmetrisation of the transposed products is again a scalar matrix, and the coefficient form is a quarter of the trace pairing. This article reads the block on the regular representation: the realization and its invariants, the product as a symmetrisation, the trace pairing, the transported operator on the regular matrices and on the whole matrix space, and the comparison with the other blocks on the same model.

**Boundaries.** The regular representation is *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$*; the product is *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the form is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, above this article in this category; the operators are *The Multiplication Operators of the Symmetric Quaternionic Algebra*, above this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde q=q_0e_0+\vec q$. The **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\vec q$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$; the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. The realization $\mathsf{M}_4$ is the **left regular representation**: $\mathsf{M}_4(\tilde q)$ is the matrix of the map $\tilde x\mapsto\tilde q\tilde x$, with columns the images of the basis elements, so that the entries are real and

$$
\mathsf{M}_4(\tilde p\tilde q)=\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q).
$$

## The Realization and Its Invariants

**Proposition (the invariants of the regular model).** For every $\tilde q$,

$$
\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0,\qquad
\det\mathsf{M}_4(\tilde q)=N(\tilde q)^{2},\qquad
\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q)^{\mathsf T}.
$$

*Proof.* The left multiplications are a faithful representation of $\mathbb{H}$; the trace is the sum of the diagonal entries of the matrix of $\tilde x\mapsto\tilde q\tilde x$, each coordinate contribution carrying $q_0$ once, giving $4q_0$; the determinant of a left multiplication by $\tilde q$ is its norm power $N(\tilde q)^{2}$, the algebra being $4$-dimensional over $\mathbb{R}$, as *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$* records; the transpose identity is checked on the basis, where left multiplication by $e_k$ is skew and by $e_0$ is the identity, so transposition exchanges $e_k$ and $-e_k$.

**Remark (trace and determinant in the two dimensions).** The regular model has $\operatorname{Tr}=4q_0$ and $\det=N^{2}$, against $\operatorname{Tr}=2q_0$ and $\det=N$ in the $2\times2$ complex model; the factor is the dimension of the algebra over the field of the model, and the transpose replaces the conjugate transpose.

## The Product Read on the Model

**Theorem (the product is the symmetrisation of the transposed products).** For all $\tilde p,\tilde q$,

$$
\tfrac12\bigl(\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q)+\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde p)\bigr)
=\mathsf{M}_4(\tilde p\star\tilde q)=N(\tilde p,\tilde q)\,I_4 .
$$

*Proof.* The transpose identity gives $\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q)=\mathsf{M}_4(\tilde p^{\natural})\mathsf{M}_4(\tilde q)=\mathsf{M}_4(\tilde p^{\natural}\tilde q)$ by multiplicativity; the half-sum is $\mathsf{M}_4\bigl(\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)\bigr)=\mathsf{M}_4(N(\tilde p,\tilde q)e_0)=N(\tilde p,\tilde q)I_4$.

**Corollary (the value is a scalar matrix).** The value of the block in the regular model is a real multiple of $I_4$, and the transposition of the regular matrix plays the role of the quaternion conjugation.

*Proof.* The theorem displays the value as $N(\tilde p,\tilde q)I_4$, and the transpose identity identifies the transposition with the conjugation.

## The Trace Pairing

**Theorem (the form is a quarter of the trace pairing).** For all $\tilde p,\tilde q$,

$$
N(\tilde p,\tilde q)=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q)\bigr).
$$

*Proof.* $\operatorname{Tr}(\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q))=\operatorname{Tr}\mathsf{M}_4(\tilde p^{\natural}\tilde q)=4\,\mathrm{Sc}(\tilde p^{\natural}\tilde q)=4N(\tilde p,\tilde q)$.

**Corollary (the quadratic form is the square root of the determinant).** The quadratic form of the block is the positive square root of the determinant of the regular matrix, $N(\tilde q)=\sqrt{\det\mathsf{M}_4(\tilde q)}$.

*Proof.* The determinant is $N(\tilde q)^{2}$ and $N(\tilde q)\geq0$; the square root is the nonnegative one.

**Remark (the transpose is a trace complement on the image).** On the regular matrices the transpose is an involution with $\mathsf{M}_4(\tilde q)^{\mathsf T}=\mathsf{M}_4(\tilde q^{\natural})$, and the symmetrisation of the two transposed products collapses to the scalar matrix; the same computation in the $2\times2$ model uses the adjugate, which in dimension two is the same involution.

## The Transported Operator

**Theorem (the operator on the regular matrices).** For fixed $\tilde p$ the map

$$
X\longmapsto\tfrac12\bigl(\mathsf{M}_4(\tilde p)^{\mathsf T}X+X^{\mathsf T}\mathsf{M}_4(\tilde p)\bigr)
$$

restricted to the regular matrices $\mathsf{M}_4(\tilde q)$ has image the real scalar matrices $\mathbb{R}I_4$, rank $1$, trace $p_0$ and kernel the regular matrices $\mathsf{M}_4(\tilde p^{\perp})$.

*Proof.* On $X=\mathsf{M}_4(\tilde q)$ the map is $N(\tilde p,\tilde q)I_4$ by the theorem, so the image is $\mathbb{R}I_4$, the rank is $1$ for $\tilde p\neq0$, the trace is the coefficient of the image of $I_4=\mathsf{M}_4(e_0)$, namely $N(\tilde p,e_0)=p_0$, and the kernel is $\mathsf{M}_4(\tilde p^{\perp})$; the argument is the same as in the $2\times2$ model.

**Theorem (the operator on the whole matrix space).** Extended to the whole of $M_4(\mathbb{R})$, the map $X\mapsto\tfrac12(\mathsf{M}_4(\tilde p)^{\mathsf T}X+X^{\mathsf T}\mathsf{M}_4(\tilde p))$ has image the symmetric matrices and rank $10$ for every $\tilde p\neq0$.

*Proof.* Write $A=\mathsf{M}_4(\tilde p)$. The map is $X\mapsto\tfrac12(A^{\mathsf T}X+(A^{\mathsf T}X)^{\mathsf T})$, the symmetric part of $A^{\mathsf T}X$. For $\tilde p\neq0$ the matrix $A$ is invertible, so $A^{\mathsf T}X$ ranges over all of $M_4(\mathbb{R})$ as $X$ does, and its symmetric part ranges over the symmetric matrices, a space of real dimension $4\cdot5/2=10$; the rank is $10$.

**Remark (the two ranks, against a misleading reading).** The rank $1$ is the rank on the image of the regular representation, which is the block's own operator; the rank $10$ is the rank of the extension to the whole matrix space.

## The Comparison with the Other Blocks on the Same Model

**Proposition (the six products in the regular model).** With $\mathsf{M}=\mathsf{M}_4$, the six operations of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* read, for the left regular representation of the first factor,

| structure | product in the model | value |
|---|---|---|
| $\mathrm{GPA}$ | $\mathsf{M}(\tilde p)\mathsf{M}(\tilde q)$ | a regular matrix |
| $\mathrm{SPA}$ | $\tfrac12(\mathsf{M}(\tilde p)\mathsf{M}(\tilde q)+\mathsf{M}(\tilde q)\mathsf{M}(\tilde p))$ | a regular matrix |
| $\mathrm{APA}$ | $\tfrac12(\mathsf{M}(\tilde p)\mathsf{M}(\tilde q)-\mathsf{M}(\tilde q)\mathsf{M}(\tilde p))$ | a regular matrix |
| $\mathrm{GQA}$ | $\mathsf{M}(\tilde p)^{\mathsf T}\mathsf{M}(\tilde q)$ | a regular matrix |
| $\mathrm{SQA}$ | $\tfrac12(\mathsf{M}(\tilde p)^{\mathsf T}\mathsf{M}(\tilde q)+\mathsf{M}(\tilde q)^{\mathsf T}\mathsf{M}(\tilde p))$ | the scalar matrix $N(\tilde p,\tilde q)I_4$ |
| $\mathrm{AQA}$ | $\tfrac12(\mathsf{M}(\tilde p)^{\mathsf T}\mathsf{M}(\tilde q)-\mathsf{M}(\tilde q)^{\mathsf T}\mathsf{M}(\tilde p))$ | a regular matrix |

and the block is the only row whose value is always a scalar matrix.

*Proof.* Each row is the realization of the corresponding product, by the multiplicativity of $\mathsf{M}$ in the plain cases and by the transpose identity $\mathsf{M}(\tilde p^{\natural})=\mathsf{M}(\tilde p)^{\mathsf T}$ in the quaternionic cases; the block's row is the theorem of §*The Product Read on the Model*. The last clause is the isolation theorem of *The Specificities of the Symmetric Quaternionic Algebra*.

Over $\mathbb{R}$ the model is real and the value is a real scalar matrix; the invariants $\operatorname{Tr}=4q_0$ and $\det=N^{2}$ are the same powers, with the norm definite instead of indefinite.

## Summary

In the left regular representation the quaternion algebra is a space of real $4\times4$ matrices with $\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0$, $\det\mathsf{M}_4(\tilde q)=N(\tilde q)^{2}$ and $\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q)^{\mathsf T}$. The symmetric quaternionic product is the symmetrisation of the transposed products, $\tfrac12(\mathsf{M}(\tilde p)^{\mathsf T}\mathsf{M}(\tilde q)+\mathsf{M}(\tilde q)^{\mathsf T}\mathsf{M}(\tilde p))=N(\tilde p,\tilde q)I_4$, a scalar matrix; the coefficient form is a quarter of the trace pairing and the quadratic form is the square root of the determinant. The transported operator has rank one and image the real scalar matrices on the regular matrices, trace $p_0$ and kernel $\mathsf{M}_4(\tilde p^{\perp})$; extended to the whole of $M_4(\mathbb{R})$ it has image the symmetric matrices and rank $10$ for every nonzero multiplier.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf{M}_4$ | the left regular representation, columns the images of the basis |
| $\mathsf{M}_4(\tilde p\tilde q)=\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)$ | multiplicativity |
| $\operatorname{Tr}=4q_0$, $\det=N(\tilde q)^{2}$, $\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q)^{\mathsf T}$ | the invariants |
| $N(\tilde p,\tilde q)=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q))$ | the trace pairing |
| rank $1$ on the regular matrices, rank $10$ on $M_4(\mathbb{R})$ | the two ranks of the transported operator |
| $\tfrac12(\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q)+\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde p))=N(\tilde p,\tilde q)I_4$ | the block in the model |

## Further Reading

- *Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$* (`articles_maths/quaternion-4x4-matrix-element-representation.md`), for the regular representation and its invariants
- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the product
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the abstract operator whose matrix picture is the transported operator
- *The Symmetric Quaternionic Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation-of-quaternions.md`), for the companion model
