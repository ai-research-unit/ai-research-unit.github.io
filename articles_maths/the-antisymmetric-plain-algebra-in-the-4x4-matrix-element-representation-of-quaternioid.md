# __The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the cross product
$\tilde q_1\times\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$ of
*Introduction to the Antisymmetric Plain Algebra*. This article reads the operation on
the **left regular representation** $M_4(\mathbb{R})_L$ of *Introduction to the $4\times4$ Matrix
Element Representation $M_4(\mathbb{R})_L$ of Quaternions*, where the plain product becomes the matrix
product and the antisymmetrization becomes the **halved commutator** of the regular matrices. It gives
the commutator identity, the image, the structure constants, the two commuting regular copies, the
trace form and the comparison with the plain algebra on the same model.

The reading is the regular-representation analogue of the two by two article: the commutator of the
left multiplication operators is the operator of the bracket, its image is the trace-free part, and the
model carries both regular copies at once.

**This is not the algebra $\mathbb{H}$.** The model is a faithful algebra morphism of the plain
product; the antisymmetric block is read on it as the commutator. Throughout, the natural sign
${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no
nontrivial involution, and the star coincides with the natural sign and gives nothing new.

The model and its multiplicativity are *Introduction to the $4\times4$ Matrix Element Representation
$M_4(\mathbb{R})_L$ of Quaternions* and *The General Plain Algebra in the $4\times4$ Matrix Element
Representation $M_4(\mathbb{R})_L$*; the bracket and its structure are *The Lie Algebra of the
Antisymmetric Plain Algebra* and *The Killing Form of the Antisymmetric Plain Algebra*, below this
article in this category. The companion article is *The Antisymmetric Plain Algebra in the $2\times2$
Matrix Element Representation $M_2(\mathbb{C})$*, above this article in this category.

## The Left Regular Model

**Proposition.** The map $\mathsf{M}_4$ is an injective $\mathbb{R}$-algebra homomorphism,

$$
\boxed{\;\mathsf{M}_4(\tilde q_1\tilde q_2)=\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2),\qquad
\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q)^{\mathsf T}\;},
$$

with $\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_t$ and
$\det\mathsf{M}_4(\tilde q)=\langle\tilde q\rangle_{\natural}^2$. On the basis,

$$
\mathsf{M}_4(e_t)=\mathrm{I}_4,\qquad
\mathsf{M}_4(\vec e_x)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
\mathsf{M}_4(\vec e_y)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(\vec e_z)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

*Proof.* The multiplicativity is the associativity of the plain product read in the regular
representation; the transpose is the conjugation because the basis is orthonormal for the norm and the
conjugation is the adjoint of the left multiplication. The trace is $4q_t$, the diagonal of
$\mathsf{M}_4(\tilde q)$ being $(q_t,q_t,q_t,q_t)$; the determinant is the fourth power of the
characteristic scale of the left multiplication, $\langle\tilde q\rangle_{\natural}^2$.

## The Commutator Identity

**Theorem (the bracket is the halved commutator).**

$$
\boxed{\;\mathsf{M}_4(\tilde q_1\times\tilde q_2)=\tfrac12\bigl[\mathsf{M}_4(\tilde q_1),\mathsf{M}_4(\tilde q_2)\bigr]\;}.
$$

*Proof.* The model is multiplicative, so
$\mathsf{M}_4(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)-\mathsf{M}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1)$,
and half of it is the image of the bracket.

## The Image and the Kernel

**Theorem.** The image of the block is the trace-free part of the image of the model,

$$
\boxed{\;\mathsf{M}_4\bigl(\mathrm{Vect}(\mathbb{H})\bigr)
=\{\mathsf{M}_4(\vec q):\ \operatorname{Tr}\mathsf{M}_4(\vec q)=0\}\;},
$$

a three-dimensional real subspace, and the kernel of the model map is $\{0\}$.

*Proof.* The values of the block are pure, so their matrices are trace-free by
$\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_t$; conversely a trace-free matrix of the image has
$q_t=0$ by the same trace formula, so it is the image of a pure element, and the pure elements are
values of the block. The injectivity is the faithfulness of the regular representation.

## The Structure Constants

The regular matrices of the pure units satisfy the commutator relations of the cross product,

$$
\tfrac12[\mathsf{M}_4(\vec e_x),\mathsf{M}_4(\vec e_y)]=\mathsf{M}_4(\vec e_z),\qquad
\tfrac12[\mathsf{M}_4(\vec e_y),\mathsf{M}_4(\vec e_z)]=\mathsf{M}_4(\vec e_x),\qquad
\tfrac12[\mathsf{M}_4(\vec e_z),\mathsf{M}_4(\vec e_x)]=\mathsf{M}_4(\vec e_y),
$$

with the reversed pairs the negatives: the commutator of the regular matrices is the regular matrix of
the cross product, which is the multiplicativity of the model at the units.

## The Commuting Copies

**Theorem (the two regular copies commute).** The left and the right regular representations commute,

$$
\mathsf{M}_4(\tilde q_1)\mathsf{R}_4(\tilde q_2)=\mathsf{R}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1),
$$

and their product is the two-sided operator $r\mapsto\tilde q_1 r\tilde q_2$. The left copy carries the
block, the right copy carries the conjugate block, and the two commute because the plain product is
associative.

*Proof.* The associativity of the plain product gives $(\tilde q_1 r)\tilde q_2=\tilde q_1(r\tilde q_2)$ for
every $r$, which is the equality of the two operators; read in the basis it is the commutation of the
matrices.

**Remark (the enrichment over the two by two model).** The two by two model carries the left
representation alone, the right one being its conjugate; the four by four regular model carries both
copies at once, and the commuting pair is the whole operator algebra of the two-sided multiplications
of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*.

## The Trace Form and the Invariants

**Proposition.** The trace form of the model is the plain form multiplied by four,

$$
\boxed{\;\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)\bigr)=4\langle\tilde q_1,\tilde q_2\rangle\;},
$$

which on the derived algebra is twice the Killing form,
$\operatorname{Tr}(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2))=-4\,\vec q_1\cdot\vec q_2=2\kappa(\tilde q_1,\tilde q_2)$
for pure $\tilde q_1,\tilde q_2$; and the determinant reads the quaternion norm,
$\det\mathsf{M}_4(\tilde q)=\langle\tilde q\rangle_{\natural}^2$.

*Proof.* The model is multiplicative, so
$\operatorname{Tr}(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2))=\operatorname{Tr}\mathsf{M}_4(\tilde q_1\tilde q_2)=4\mathrm{Sc}(\tilde q_1\tilde q_2)=4\langle\tilde q_1,\tilde q_2\rangle$;
on pure elements $\langle\cdot,\cdot\rangle=-\vec q_1\cdot\vec q_2$, and the Killing form is $-2\,\vec q_1\cdot\vec q_2$
(*The Killing Form of the Antisymmetric Plain Algebra*, below this article in this category).

## The Comparison with the Plain Algebra on the Model

| | the plain algebra | the antisymmetric plain block |
|---|---|---|
| the operation in the model | the matrix product $\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)$ | the halved commutator |
| the model | the algebra morphism $\mathbb{H}\to M_4(\mathbb{R})_L$ | the same, read on the commutator |
| the image | the four-dimensional algebra of the regular matrices | the trace-free part, of dimension three |
| the trace of a value | $4\,\mathrm{Sc}(\tilde q_1\tilde q_2)$ | $0$ |
| the two copies | the left and the right, commuting | the left copy alone carries the block |

**Remark (the plain algebra on the model).** The plain algebra is the matrix product on the regular
matrices, a four-dimensional algebra isomorphic to $\mathbb{H}$ and split from $M_4(\mathbb{R})$ by the
representation; the antisymmetric block is the commutator on the same matrices, of image the trace-free
part, and the right copy commutes with it without belonging to it. The plain reading is *The General
Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*.

## Summary

In the four by four left regular model the antisymmetric plain algebra is the halved commutator of the
regular matrices, $\mathsf{M}_4(\tilde q_1\times\tilde q_2)=\tfrac12[\mathsf{M}_4(\tilde q_1),\mathsf{M}_4(\tilde q_2)]$,
with the model multiplicative, $\mathsf{M}_4(\tilde q_1\tilde q_2)=\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2)$
and the conjugation the transpose. Its image is the three-dimensional real subspace of trace-free
regular matrices, its kernel of faithfulness is $\{0\}$, and the structure constants are the
commutators of the four basis matrices. The left and right regular copies commute, their product being
the two-sided operator $r\mapsto\tilde q_1 r\tilde q_2$. The trace form of the model is four times the
plain form, twice the Killing form on the derived algebra, and the determinant is the square of the
quaternion norm. The plain algebra on the same model is the matrix product, with the whole
four-dimensional regular algebra as image.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde q)$ | the left regular matrix of $\tilde q$ |
| $\mathsf{R}_4(\tilde q)$ | the right regular matrix |
| $\mathsf{M}_4(\tilde q_1\times\tilde q_2)=\tfrac12[\mathsf{M}_4(\tilde q_1),\mathsf{M}_4(\tilde q_2)]$ | the block as the halved commutator |
| $\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_t$ | the trace of the model |
| $\det\mathsf{M}_4(\tilde q)=\langle\tilde q\rangle_{\natural}^2$ | the determinant, the square of the norm |
| $\mathsf{M}_4(\tilde q_1)\mathsf{R}_4(\tilde q_2)=\mathsf{R}_4(\tilde q_2)\mathsf{M}_4(\tilde q_1)$ | the commuting regular copies |
| $\operatorname{Tr}(\mathsf{M}_4(\tilde q_1)\mathsf{M}_4(\tilde q_2))=4\langle\tilde q_1,\tilde q_2\rangle$ | the trace form |

## Further Reading

- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$ of Quaternions](introduction-to-the-4x4-matrix-element-representation-of-quaternions.html), for the model and its basis matrices, and for the plain product on the same model.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the two commuting regular copies and the two-sided operators.
- [The Lie Algebra of the Antisymmetric Plain Algebra](the-lie-algebra-of-the-antisymmetric-plain-algebra-of-quaternioid.html) and [The Killing Form of the Antisymmetric Plain Algebra](the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternioid.html), both below this article in this category, for the structure and the form read here on the model.
- [Introduction to the Symmetric Plain Algebra](introduction-to-the-symmetric-plain-algebra-of-quaternioid.html), above this article in this category, for the companion model.
