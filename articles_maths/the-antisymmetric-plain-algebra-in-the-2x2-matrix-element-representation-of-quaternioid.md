# __The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the cross product
$\tilde q_1\times\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$ of
*Introduction to the Antisymmetric Plain Algebra*. This article reads the operation on
the embedding $\mathbb{H}\hookrightarrow M_2(\mathbb{C})$ of *Introduction to the $2\times2$ Matrix
Element Representation $M_2(\mathbb{C})$ of Quaternions*, where the plain product becomes the matrix
product and the antisymmetrization becomes the **halved commutator**. It gives the matrix of the cross
product, the structure constants in matrix form, the invariants, the trace form and the comparison with
the plain algebra on the same model.

The reading is the standard one: the commutator of two matrix images is the image of the bracket, its
image is the trace-free part, and the trace form on that part is the Killing form of the block.

**This is not the algebra $\mathbb{H}$.** The model is an algebra embedding of the plain product; the
antisymmetric block is read on it as the commutator and is not the matrix product. Throughout, the
natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because
$\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives
nothing new.

The model itself, its basis images and the multiplicativity are *Introduction to the $2\times2$ Matrix
Element Representation $M_2(\mathbb{C})$ of Quaternions* and *The General Plain Algebra in the
$2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the bracket and its structure are
*Introduction to the Antisymmetric Plain Algebra*, *The Lie Algebra of the
Antisymmetric Plain Algebra* and *The Killing Form of the Antisymmetric Plain Algebra*, below this
article in this category. The companion article is *The Antisymmetric Plain Algebra in the
$4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category.

$$
\mathsf{M}_2(\tilde q)=\begin{pmatrix}q_t-iq_z & -iq_x-q_y\\ -iq_x+q_y & q_t+iq_z\end{pmatrix},
$$

with $\mathsf{M}_2(e_t)=\mathrm{I}_2$, $\mathsf{M}_2(\vec e_x)=-i\sigma_1$, $\mathsf{M}_2(\vec e_y)=-i\sigma_2$,
$\mathsf{M}_2(\vec e_z)=-i\sigma_3$, the Pauli matrices; the plain product is the matrix product,
$\mathsf{M}_2(\tilde q_1\tilde q_2)=\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)$, and the conjugation is
the Hermitian adjoint, $\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}$. The
**quaternion form** is $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=q_{1t}q_{2t}+\vec q_1\cdot\vec q_2$ and the **plain form**
$\langle\tilde q_1,\tilde q_2\rangle=q_{1t}q_{2t}-\vec q_1\cdot\vec q_2$.

## The Model

**Proposition.** The map $\mathsf{M}_2$ is an injective $\mathbb{R}$-algebra homomorphism into
$M_2(\mathbb{C})$, with $\operatorname{Tr}\mathsf{M}_2(\tilde q)=2q_t$ and determinant
$\det\mathsf{M}_2(\tilde q)=q_t^2+|\vec q|^2=\langle\tilde q\rangle_{\natural}$, the quaternion norm. The
pure elements have trace-free images, and the image of the vector subspace is a three-dimensional real
subspace of the trace-free matrices.

*Proof.* The multiplicativity and the trace are *Introduction to the $2\times2$ Matrix Element
Representation $M_2(\mathbb{C})$ of Quaternions*; the determinant of the displayed matrix is
$(q_t-iq_z)(q_t+iq_z)-(-iq_x-q_y)(-iq_x+q_y)=q_t^2+q_x^2+q_y^2+q_z^2$. The trace of the displayed
matrix is $2q_t$, which vanishes exactly on the pure elements.

## The Commutator Identity

**Theorem (the bracket is the halved commutator).**

$$
\boxed{\;\mathsf{M}_2(\tilde q_1\times\tilde q_2)=\tfrac12\bigl[\mathsf{M}_2(\tilde q_1),\mathsf{M}_2(\tilde q_2)\bigr]
=\tfrac12\bigl(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)-\mathsf{M}_2(\tilde q_2)\mathsf{M}_2(\tilde q_1)\bigr)\;}.
$$

*Proof.* The model is multiplicative, so
$\mathsf{M}_2(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)-\mathsf{M}_2(\tilde q_2)\mathsf{M}_2(\tilde q_1)$,
and half of it is the image of the bracket, the model being real-linear.

**Remark (the block is the commutator of the model).** The antisymmetric plain algebra is, in this
model, the halved commutator of the two by two complex matrices; the plain product is the product, the
symmetric half is the halved anticommutator, and the three are the two products and the bracket of the
matrix algebra. The model exhibits the split $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ as the identity
$XY=\tfrac12(XY+YX)+\tfrac12(XY-YX)$.

## The Image and the Kernel

**Theorem (the image and the kernel).** The image of the block is the trace-free part of the image of
the model,

$$
\boxed{\;\mathsf{M}_2\bigl(\mathrm{Vect}(\mathbb{H})\bigr)
=\{\mathsf{M}_2(\vec q):\ \operatorname{Tr}\mathsf{M}_2(\vec q)=0\}\;},
$$

a three-dimensional real subspace, and the kernel of the model map is $\{0\}$: the model is faithful.

*Proof.* The value $\tilde q_1\times\tilde q_2$ is pure, so its matrix is trace-free by the trace formula;
conversely a trace-free matrix of the image has $q_t=0$ by $\operatorname{Tr}\mathsf{M}_2(\tilde q)=2q_t$,
so it is the image of a pure element, and pure elements are values of the block. The model is
injective because $\mathsf{M}_2(\tilde q)=0$ forces $q_t=\dots=q_z=0$ by reading the entries.

**Remark (the two-dimensional module and the identification).** The trace-free matrices of the image
are the three-dimensional real Lie algebra $\mathfrak{su}(2)$ under the commutator, the defining
two-dimensional representation of the derived algebra; the identification of the block with
$\mathfrak{su}(2)$ is *The Lie Algebra of the Antisymmetric Plain Algebra*, below this article in this
category.

## The Structure Constants in Matrix Form

The three matrix images satisfy the commutator relations of the cross product,

$$
\tfrac12[\mathsf{M}_2(\vec e_x),\mathsf{M}_2(\vec e_y)]=\mathsf{M}_2(\vec e_z),\qquad
\tfrac12[\mathsf{M}_2(\vec e_y),\mathsf{M}_2(\vec e_z)]=\mathsf{M}_2(\vec e_x),\qquad
\tfrac12[\mathsf{M}_2(\vec e_z),\mathsf{M}_2(\vec e_x)]=\mathsf{M}_2(\vec e_y),
$$

and the reversed pairs are the negatives. In the display,

$$
\mathsf{M}_2(\vec e_x\times \vec e_y)=\tfrac12\begin{pmatrix}0&-i\\-i&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}
-\tfrac12\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\-i&0\end{pmatrix}
=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=\mathsf{M}_2(\vec e_z).
$$

The first row and the first column are zero as in the coefficient space, the scalar matrix
$\mathsf{M}_2(e_t)=\mathrm{I}_2$ entering no value.

## The Invariants

**Proposition.** The invariants of the images are

$$
\boxed{\;\operatorname{Tr}\mathsf{M}_2(\tilde q)=2q_t,\qquad
\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2\;},
$$

$$
\operatorname{Tr}\mathsf{M}_2(\tilde q_1\times\tilde q_2)=0,\qquad
\det\mathsf{M}_2(\tilde q_1\times\tilde q_2)=|\vec q_1\times\vec q_2|^2,
$$

and the images satisfy the normality relation

$$
\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde q)^{\dagger}=\langle\tilde q\rangle_{\natural}\,\mathrm{I}_2 .
$$

*Proof.* The trace and the determinant are those of the model; the value of the block is pure, so the
trace vanishes and the determinant is the norm of the pure vector part $|\vec q_1\times\vec q_2|^2$.
The normality is $\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q\tilde q^{\natural})=\langle\tilde q\rangle_{\natural}\mathrm{I}_2$.

## The Trace Form and the Killing Form

**Theorem (the trace form is the Killing form).** On the derived algebra,

$$
\boxed{\;\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)\bigr)=\kappa(\tilde q_1,\tilde q_2)=-2\,\vec q_1\cdot\vec q_2
\qquad(\tilde q_1,\tilde q_2\in\mathrm{Vect}(\mathbb{H}))\;},
$$

is the Killing form of the block, and on general elements
$\operatorname{Tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))=2\langle\tilde q_1,\tilde q_2\rangle$ and
$\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2)^{\dagger})=\langle\tilde q_1,\tilde q_2\rangle_{\natural}$.

*Proof.* The model is multiplicative, so
$\operatorname{Tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))=\operatorname{Tr}\mathsf{M}_2(\tilde q_1\tilde q_2)=2\mathrm{Sc}(\tilde q_1\tilde q_2)=2\langle\tilde q_1,\tilde q_2\rangle$;
on pure elements $\langle\cdot,\cdot\rangle=-\vec q_1\cdot\vec q_2$ and the trace is $-2\,\vec q_1\cdot\vec q_2$, the
Killing form. For the quaternion form, $\mathsf{M}_2(\tilde q)^{\dagger}=\mathsf{M}_2(\tilde q^{\natural})$
and $\operatorname{Tr}\mathsf{M}_2(\tilde q_1\tilde q_2^{\natural})=2\mathrm{Sc}(\tilde q_1\tilde q_2^{\natural})=2\langle\tilde q_1,\tilde q_2\rangle_{\natural}$.

**Remark (the two objects of the block in one model).** The model shows the two objects of the block at
once: the bracket is the commutator and the invariant form is the trace. This is the reason the block
(*Introduction to the Symmetric Plain Algebra* of

## The Comparison with the Plain Algebra on the Model

| | the plain algebra | the antisymmetric plain block |
|---|---|---|
| the operation in the model | the matrix product $XY$ | the halved commutator $\tfrac12(XY-YX)$ |
| the image | the four-dimensional real subspace $\mathsf{M}_2(\mathbb{H})$ | the trace-free part of the image |
| the kernel of the model | $\{0\}$ | $\{0\}$ |
| the trace of a value | $2\,\mathrm{Sc}(\tilde q_1\tilde q_2)$ | $0$ |
| the invariant form | $\langle\cdot,\cdot\rangle_{\natural}$, the determinant | $\kappa$, the trace form |

**Remark (the plain algebra on the same model).** The plain algebra is the matrix product on the image
of the model, of invariant form $\langle\cdot,\cdot\rangle_{\natural}$ read as the determinant, and its multiplicativity is the
multiplicativity of the model. The antisymmetric block is the commutator, of invariant form the trace
form, and its values are the trace-free matrices. The plain reading is *The General Plain Algebra in
the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*.

## Summary

In the two by two complex model the antisymmetric plain algebra is the halved commutator,
$\mathsf{M}_2(\tilde q_1\times\tilde q_2)=\tfrac12[\mathsf{M}_2(\tilde q_1),\mathsf{M}_2(\tilde q_2)]$, with
the three matrix images $-i\sigma_1,-i\sigma_2,-i\sigma_3$ satisfying the cross-product commutators. The
image of the block is the three-dimensional real subspace of trace-free matrices of the image,
identified with $\mathfrak{su}(2)$; the model is faithful, of kernel $\{0\}$. The invariants are
$\operatorname{Tr}\mathsf{M}_2(\tilde q)=2q_t$, $\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}$,
$\operatorname{Tr}\mathsf{M}_2(\tilde q_1\times\tilde q_2)=0$ and
$\det\mathsf{M}_2(\tilde q_1\times\tilde q_2)=|\vec q_1\times\vec q_2|^2$, with the normality
$\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde q)^{\dagger}=\langle\tilde q\rangle_{\natural}\mathrm{I}_2$. The trace form of the
model is the Killing form of the block on the derived algebra, and the general trace and the conjugate
trace read the plain form and the quaternion form. The plain algebra on the same model is the matrix
product, of the whole matrix algebra as image.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde q)$ | the two by two complex model of a quaternion |
| $\mathsf{M}_2(\tilde q_1\times\tilde q_2)=\tfrac12[\mathsf{M}_2(\tilde q_1),\mathsf{M}_2(\tilde q_2)]$ | the block as the halved commutator |
| $\{\operatorname{Tr}=0\}$ | the image of the block, the trace-free part |
| $\operatorname{Tr}\mathsf{M}_2(\tilde q)=2q_t$ | the trace of the model |
| $\det\mathsf{M}_2(\tilde q)=\langle\tilde q\rangle_{\natural}$ | the determinant, the quaternion norm |
| $\operatorname{Tr}(\mathsf{M}_2(\tilde q_1)\mathsf{M}_2(\tilde q_2))=-2\,\vec q_1\cdot\vec q_2$ | the trace form as the Killing form |

## Further Reading

- *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions*, for the model, the basis images and the multiplicativity.
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, for the plain product on the same model.
- [The Lie Algebra of the Antisymmetric Plain Algebra](the-lie-algebra-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the identification with $\mathfrak{su}(2)$.
- [The Killing Form of the Antisymmetric Plain Algebra](the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid.html), below this article in this category, for the invariant form read here as the trace form.
- [The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$](the-antisymmetric-plain-algebra-in-the-4x4-matrix-element-representation-of-quaternioid.html), below this article in this category, for the companion model.
