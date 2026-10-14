# __The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

The antisymmetric plain algebra of $\mathbb{H}$ is the cross product
$\tilde p\times\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$ of
*Introduction to the Antisymmetric Plain Algebra of Quaternions*. This article reads the operation on
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

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; the left regular representation is the map $\mathsf{M}_4$ sending $\tilde q$ to
the matrix of the left multiplication $r\mapsto\tilde q r$ in the basis $(e_0,e_1,e_2,e_3)$, and the
right regular representation is $\mathsf{R}_4$, the matrix of $r\mapsto r\tilde q$. The **quaternion
form** is $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$ and the **plain form**
$B(\tilde p,\tilde q)=p_0q_0-\vec p\cdot\vec q$.

## The Left Regular Model

**Proposition.** The map $\mathsf{M}_4$ is an injective $\mathbb{R}$-algebra homomorphism,

$$
\mathsf{M}_4(\tilde p\tilde q)=\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q),\qquad
\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q)^{\mathsf T},
$$

with $\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0$ and
$\det\mathsf{M}_4(\tilde q)=N(\tilde q)^2$. On the basis,

$$
\mathsf{M}_4(e_0)=\mathrm{I}_4,\qquad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

*Proof.* The multiplicativity is the associativity of the plain product read in the regular
representation; the transpose is the conjugation because the basis is orthonormal for the norm and the
conjugation is the adjoint of the left multiplication. The trace is $4q_0$, the diagonal of
$\mathsf{M}_4(\tilde q)$ being $(q_0,q_0,q_0,q_0)$; the determinant is the fourth power of the
characteristic scale of the left multiplication, $N(\tilde q)^2$.

## The Commutator Identity

**Theorem (the bracket is the halved commutator).**

$$
\mathsf{M}_4(\tilde p\times\tilde q)=\tfrac12\bigl[\mathsf{M}_4(\tilde p),\mathsf{M}_4(\tilde q)\bigr].
$$

*Proof.* The model is multiplicative, so
$\mathsf{M}_4(\tilde p\tilde q-\tilde q\tilde p)=\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)-\mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde p)$,
and half of it is the image of the bracket.

## The Image and the Kernel

**Theorem.** The image of the block is the trace-free part of the image of the model,

$$
\mathsf{M}_4\bigl(\mathrm{Vect}(\mathbb{H})\bigr)
=\{\mathsf{M}_4(\vec q):\ \operatorname{Tr}\mathsf{M}_4(\vec q)=0\},
$$

a three-dimensional real subspace, and the kernel of the model map is $\{0\}$.

*Proof.* The values of the block are pure, so their matrices are trace-free by
$\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0$; conversely a trace-free matrix of the image has
$q_0=0$ by the same trace formula, so it is the image of a pure element, and the pure elements are
values of the block. The injectivity is the faithfulness of the regular representation.

## The Structure Constants

The regular matrices of the pure units satisfy the commutator relations of the cross product,

$$
\tfrac12[\mathsf{M}_4(e_1),\mathsf{M}_4(e_2)]=\mathsf{M}_4(e_3),\qquad
\tfrac12[\mathsf{M}_4(e_2),\mathsf{M}_4(e_3)]=\mathsf{M}_4(e_1),\qquad
\tfrac12[\mathsf{M}_4(e_3),\mathsf{M}_4(e_1)]=\mathsf{M}_4(e_2),
$$

with the reversed pairs the negatives: the commutator of the regular matrices is the regular matrix of
the cross product, which is the multiplicativity of the model at the units.

## The Commuting Copies

**Theorem (the two regular copies commute).** The left and the right regular representations commute,

$$
\mathsf{M}_4(\tilde p)\mathsf{R}_4(\tilde q)=\mathsf{R}_4(\tilde q)\mathsf{M}_4(\tilde p),
$$

and their product is the two-sided operator $r\mapsto\tilde p r\tilde q$. The left copy carries the
block, the right copy carries the conjugate block, and the two commute because the plain product is
associative.

*Proof.* The associativity of the plain product gives $(\tilde p r)\tilde q=\tilde p(r\tilde q)$ for
every $r$, which is the equality of the two operators; read in the basis it is the commutation of the
matrices.

**Remark (the enrichment over the two by two model).** The two by two model carries the left
representation alone, the right one being its conjugate; the four by four regular model carries both
copies at once, and the commuting pair is the whole operator algebra of the two-sided multiplications
of *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*.

## The Trace Form and the Invariants

**Proposition.** The trace form of the model is the plain form multiplied by four,

$$
\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)\bigr)=4B(\tilde p,\tilde q),
$$

which on the derived algebra is twice the Killing form,
$\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))=-4\,\vec p\cdot\vec q=2\kappa(\tilde p,\tilde q)$
for pure $\tilde p,\tilde q$; and the determinant reads the quaternion norm,
$\det\mathsf{M}_4(\tilde q)=N(\tilde q)^2$.

*Proof.* The model is multiplicative, so
$\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))=\operatorname{Tr}\mathsf{M}_4(\tilde p\tilde q)=4\mathrm{Sc}(\tilde p\tilde q)=4B(\tilde p,\tilde q)$;
on pure elements $B=-\vec p\cdot\vec q$, and the Killing form is $-2\,\vec p\cdot\vec q$
(*The Killing Form of the Antisymmetric Plain Algebra*, below this article in this category).

## The Comparison with the Plain Algebra on the Model

| | the plain algebra | the antisymmetric plain block |
|---|---|---|
| the operation in the model | the matrix product $\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)$ | the halved commutator |
| the model | the algebra morphism $\mathbb{H}\to M_4(\mathbb{R})_L$ | the same, read on the commutator |
| the image | the four-dimensional algebra of the regular matrices | the trace-free part, of dimension three |
| the trace of a value | $4\,\mathrm{Sc}(\tilde p\tilde q)$ | $0$ |
| the two copies | the left and the right, commuting | the left copy alone carries the block |

**Remark (the plain algebra on the model).** The plain algebra is the matrix product on the regular
matrices, a four-dimensional algebra isomorphic to $\mathbb{H}$ and split from $M_4(\mathbb{R})$ by the
representation; the antisymmetric block is the commutator on the same matrices, of image the trace-free
part, and the right copy commutes with it without belonging to it. The plain reading is *The General
Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*.

## Summary

In the four by four left regular model the antisymmetric plain algebra is the halved commutator of the
regular matrices, $\mathsf{M}_4(\tilde p\times\tilde q)=\tfrac12[\mathsf{M}_4(\tilde p),\mathsf{M}_4(\tilde q)]$,
with the model multiplicative, $\mathsf{M}_4(\tilde p\tilde q)=\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)$
and the conjugation the transpose. Its image is the three-dimensional real subspace of trace-free
regular matrices, its kernel of faithfulness is $\{0\}$, and the structure constants are the
commutators of the four basis matrices. The left and right regular copies commute, their product being
the two-sided operator $r\mapsto\tilde p r\tilde q$. The trace form of the model is four times the
plain form, twice the Killing form on the derived algebra, and the determinant is the square of the
quaternion norm. The plain algebra on the same model is the matrix product, with the whole
four-dimensional regular algebra as image.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde q)$ | the left regular matrix of $\tilde q$ |
| $\mathsf{R}_4(\tilde q)$ | the right regular matrix |
| $\mathsf{M}_4(\tilde p\times\tilde q)=\tfrac12[\mathsf{M}_4(\tilde p),\mathsf{M}_4(\tilde q)]$ | the block as the halved commutator |
| $\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0$ | the trace of the model |
| $\det\mathsf{M}_4(\tilde q)=N(\tilde q)^2$ | the determinant, the square of the norm |
| $\mathsf{M}_4(\tilde p)\mathsf{R}_4(\tilde q)=\mathsf{R}_4(\tilde q)\mathsf{M}_4(\tilde p)$ | the commuting regular copies |
| $\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))=4B(\tilde p,\tilde q)$ | the trace form |

## Further Reading

- *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$ of Quaternions*, for the model and its basis matrices.
- *The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, for the plain product on the same model.
- *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, for the two commuting regular copies and the two-sided operators.
- *The Lie Algebra of the Antisymmetric Plain Algebra* and *The Killing Form of the Antisymmetric Plain Algebra*, both below this article in this category, for the structure and the form read here on the model.
- *The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, above this article in this category, for the companion model.
