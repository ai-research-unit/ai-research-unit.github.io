# __The Symmetric Quaternionic Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The quaternion algebra embeds into the complex $2\times2$ matrices, and the symmetric quaternionic product becomes, in that model, the symmetrisation of the two conjugate-transposed products of the images; its value is a scalar matrix. This article reads the block on that model: the realization and its invariants, the product as a symmetrisation, the trace pairing as the coefficient form, and the comparison with the other blocks on the same model. The realization itself, with its multiplicativity, its trace and its determinant, is *Quaternion 2x2 Matrix Element Representation $M_2(\mathbb{C})$*; this article owns the reading of the product on it.

**Boundaries.** The realization is *Quaternion 2x2 Matrix Element Representation $M_2(\mathbb{C})$*; the product is *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the form is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, above this article in this category; the operators are *The Multiplication Operators of the Symmetric Quaternionic Algebra*, above this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde q=q_0e_0+\vec q$. The **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\vec q$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$; the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. The realization $\mathsf{M}_2$ is fixed on the basis by $\mathsf{M}_2(e_0)=I_2$ and $\mathsf{M}_2(e_k)=-i\sigma_k$, so that

$$
\mathsf{M}_2(\tilde q)=\begin{pmatrix}q_0-iq_3 & -iq_1-q_2\\ -iq_1+q_2 & q_0+iq_3\end{pmatrix}.
$$

## The Realization and Its Invariants

**Proposition (the invariants of the model).** The realization $\mathsf{M}_2$ is an injective algebra homomorphism $\mathbb{H}\to M_2(\mathbb{C})$ with real $4$-dimensional image; for every $\tilde q$,

$$
\operatorname{Tr}\mathsf{M}_2(\tilde q)=2q_0,\qquad
\det\mathsf{M}_2(\tilde q)=N(\tilde q),\qquad
\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}=\operatorname{adj}\mathsf{M}_2(\tilde q),
$$

where ${}^{\dagger}$ is the conjugate transpose and $\operatorname{adj}$ the adjugate.

*Proof.* The realization is the standard one, its multiplicativity, trace and determinant are *Quaternion 2x2 Matrix Element Representation $M_2(\mathbb{C})$*; the identity $\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}$ is checked on the basis, where $\mathsf{M}_2(e_k)=-i\sigma_k$ is Hermitian, and the adjugate identity follows from $\operatorname{adj}X=(\operatorname{Tr}X)I-X$ in dimension two, which gives $2q_0I-\mathsf{M}_2(\tilde q)=\mathsf{M}_2(\tilde q^{\natural})$.

The block's operator theory is therefore read on the quaternion matrices, and the extension to the whole matrix space is an extension and not part of the model.

## The Product Read on the Model

**Theorem (the product is the symmetrisation of the twisted products).** For all $\tilde p,\tilde q$,

$$
\tfrac12\bigl(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)+\mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde p)\bigr)
=\mathsf{M}_2(\tilde p\star\tilde q)=N(\tilde p,\tilde q)\,I_2 .
$$

*Proof.* The realization is multiplicative and carries the quaternion conjugation to the conjugate transpose, so $\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)=\mathsf{M}_2(\tilde p^{\natural}\tilde q)$; the half-sum is $\mathsf{M}_2\bigl(\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)\bigr)=\mathsf{M}_2(N(\tilde p,\tilde q)e_0)=N(\tilde p,\tilde q)I_2$.

**Corollary (the value is a scalar matrix).** The product value in the model is a real multiple of the identity; the model reads the centrality of the block as the scalarity of the matrix, and the vector part of the value is absent by construction.

*Proof.* The theorem displays the value as $N(\tilde p,\tilde q)I_2$.

## The Trace Pairing

**Theorem (the form is half the trace pairing).** For all $\tilde p,\tilde q$,

$$
N(\tilde p,\tilde q)=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)\bigr).
$$

*Proof.* $\operatorname{Tr}(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q))=\operatorname{Tr}\mathsf{M}_2(\tilde p^{\natural}\tilde q)=2\,\mathrm{Sc}(\tilde p^{\natural}\tilde q)=2N(\tilde p,\tilde q)$.

**Corollary (the three readings of the form in the model).** The coefficient form is the half trace pairing, the quadratic form is the determinant, and the product is the pairing on the identity:

$$
N(\tilde p,\tilde q)=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)\bigr),\qquad
N(\tilde q)=\det\mathsf{M}_2(\tilde q),\qquad
\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0\longleftrightarrow N(\tilde p,\tilde q)I_2 .
$$

*Proof.* The first two are the theorem and the determinant identity of the proposition; the third is the reading of the product on the model.

**Remark (the matrix form of the product is the trace complement).** The adjugate identity $\operatorname{adj}X=(\operatorname{Tr}X)I-X$ identifies the quaternion conjugation with the adjugate in this dimension, and it is the same identity that makes the twisted product self-adjoint; the model therefore has one involution playing three roles, the conjugation on $\mathbb{H}$, the conjugate transpose on the matrices, and the adjugate.

## The Endomorphism of the Quaternion Matrices

**Theorem (the transported operator).** For fixed $\tilde p$ the map

$$
X\longmapsto\tfrac12\bigl(\mathsf{M}_2(\tilde p)^{\dagger}X+X^{\dagger}\mathsf{M}_2(\tilde p)\bigr)
$$

on the quaternion matrices has image the real scalar matrices $\mathbb{R}I_2$, rank $1$, trace $p_0$ and kernel the quaternion matrices $\mathsf{M}_2(\tilde p^{\perp})$.

*Proof.* On $X=\mathsf{M}_2(\tilde q)$ the map is $N(\tilde p,\tilde q)I_2$ by the theorem, so its image is contained in $\mathbb{R}I_2$ and it is surjective onto that line because $N(\tilde p,e_0)=p_0$ can be chosen nonzero; the rank is $1$ for $\tilde p\neq0$. The trace of the operator in the basis $\mathsf{M}_2(e_\mu)$ is the coefficient of the image of $\mathsf{M}_2(e_0)$, namely $p_0$. The kernel is the set of quaternion matrices with $N(\tilde p,\tilde q)=0$, that is $\mathsf{M}_2(\tilde p^{\perp})$.

**Remark (the same shape as the abstract operator).** The transported operator is the matrix picture of $L_{\tilde p}$ of *The Multiplication Operators of the Symmetric Quaternionic Algebra*: rank one, scalar image, kernel the form-perpendicular hyperplane, trace the scalar coordinate. The model adds nothing to the abstract operator and exhibits its rank as the scalarity of the matrix.

## The Comparison with the Other Blocks on the Same Model

**Proposition (the six products in the $2\times2$ model).** With $\mathsf{M}=\mathsf{M}_2$, the six operations of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space* read

| structure | product in the model | value |
|---|---|---|
| $\mathrm{GPA}$ | $\mathsf{M}(\tilde p)\mathsf{M}(\tilde q)$ | a quaternion matrix |
| $\mathrm{SPA}$ | $\tfrac12(\mathsf{M}(\tilde p)\mathsf{M}(\tilde q)+\mathsf{M}(\tilde q)\mathsf{M}(\tilde p))$ | a quaternion matrix |
| $\mathrm{APA}$ | $\tfrac12(\mathsf{M}(\tilde p)\mathsf{M}(\tilde q)-\mathsf{M}(\tilde q)\mathsf{M}(\tilde p))$ | a quaternion matrix |
| $\mathrm{GQA}$ | $\mathsf{M}(\tilde p)^{\dagger}\mathsf{M}(\tilde q)$ | a quaternion matrix |
| $\mathrm{SQA}$ | $\tfrac12(\mathsf{M}(\tilde p)^{\dagger}\mathsf{M}(\tilde q)+\mathsf{M}(\tilde q)^{\dagger}\mathsf{M}(\tilde p))$ | the scalar matrix $N(\tilde p,\tilde q)I_2$ |
| $\mathrm{AQA}$ | $\tfrac12(\mathsf{M}(\tilde p)^{\dagger}\mathsf{M}(\tilde q)-\mathsf{M}(\tilde q)^{\dagger}\mathsf{M}(\tilde p))$ | a quaternion matrix |

and the block is the only row whose value is always a scalar matrix.

*Proof.* Each row is the realization of the corresponding product, by multiplicativity of $\mathsf{M}$ in the plain cases and by the conjugation identity $\mathsf{M}(\tilde p^{\natural})=\mathsf{M}(\tilde p)^{\dagger}$ in the quaternionic cases; the block's row is the theorem of §*The Product Read on the Model*. The last clause is the isolation theorem of *The Specificities of the Symmetric Quaternionic Algebra*.

The invariants $\operatorname{Tr}=2Q_0$ and $\det=N$, and the adjugate identity, have the same form in the two blocks; the trace pairing is the same formula over the two fields.

## Summary

In the $2\times2$ complex model the quaternion algebra is the space of quaternion matrices, with $\operatorname{Tr}\mathsf{M}_2(\tilde q)=2q_0$, $\det\mathsf{M}_2(\tilde q)=N(\tilde q)$ and $\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}=\operatorname{adj}\mathsf{M}_2(\tilde q)$. The symmetric quaternionic product is the symmetrisation of the two conjugate-transposed products, $\tfrac12(\mathsf{M}(\tilde p)^{\dagger}\mathsf{M}(\tilde q)+\mathsf{M}(\tilde q)^{\dagger}\mathsf{M}(\tilde p))=N(\tilde p,\tilde q)I_2$, a scalar matrix; the coefficient form is the half trace pairing, $N(\tilde p,\tilde q)=\tfrac12\operatorname{Tr}(\mathsf{M}(\tilde p)^{\dagger}\mathsf{M}(\tilde q))$, and the quadratic form is the determinant. The transported operator $X\mapsto\tfrac12(\mathsf{M}(\tilde p)^{\dagger}X+X^{\dagger}\mathsf{M}(\tilde p))$ has rank one, image the real scalar matrices, trace $p_0$ and kernel $\mathsf{M}_2(\tilde p^{\perp})$. Among the six operations read in the same model the block is the only one whose value is always scalar.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathsf{M}_2$ | the realization, $\mathsf{M}_2(e_0)=I_2$, $\mathsf{M}_2(e_k)=-i\sigma_k$ |
| $\mathsf{M}_2(\tilde q)=\begin{pmatrix}q_0-iq_3 & -iq_1-q_2\\ -iq_1+q_2 & q_0+iq_3\end{pmatrix}$ | the matrix of a quaternion |
| $\operatorname{Tr}=2q_0$, $\det=N(\tilde q)$ | the two invariants |
| $\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}=\operatorname{adj}\mathsf{M}_2(\tilde q)$ | the three roles of the involution |
| $N(\tilde p,\tilde q)=\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q))$ | the trace pairing |
| $\tfrac12(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)+\mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde p))=N(\tilde p,\tilde q)I_2$ | the block in the model |

## Further Reading

- *Quaternion 2x2 Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/quaternion-2x2-matrix-element-representation.md`), for the realization and its invariants
- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the product
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the abstract operator whose matrix picture is the transported operator
- *The Symmetric Quaternionic Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-4x4-matrix-element-representation-of-quaternions.md`), for the companion model
