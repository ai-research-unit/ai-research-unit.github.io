# __The Antisymmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

The antisymmetric quaternionic algebra of $\mathbb{H}$ is the operation
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\mathbf q-q_0\mathbf p-\mathbf p\times\mathbf q$ of *Introduction to the Antisymmetric Quaternionic
Algebra of Quaternions*. This article reads it on the **left regular representation**
$M_4(\mathbb{R})_L$ of *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$
of Quaternions*, where the parent product becomes the product with the transposed first factor and the
antisymmetrization becomes the **halved conjugated commutator** of the regular matrices. It is the second
of the two representation articles of the block, and its companion *The Antisymmetric Quaternionic
Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* repeats the reading on the
model $\mathbb{H}\cong$ a real subalgebra of $M_2(\mathbb{C})$. The article treats the operation in the
model, the image and the kernel on the matrices, the operator and its invariants, the two commuting
copies, the trace form and the comparison with the quaternionic algebra on the model.

**This is not the algebra $\mathbb{H}$.** The model is a faithful algebra morphism of the plain product;
the antisymmetric quaternionic block is read on it through the transpose, which is the conjugation, and
is not the matrix product. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation,
the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with
the natural sign and gives nothing new. The symbol $\diamond$ is reserved for this block.

The model and its multiplicativity are *Introduction to the $4\times4$ Matrix Element Representation
$M_4(\mathbb{R})_L$ of Quaternions* and *The General Quaternionic Algebra in the $4\times4$ Matrix
Element Representation $M_4(\mathbb{R})_L$*; the block and its failure are *Introduction to the
Antisymmetric Quaternionic Algebra of Quaternions* and *The Jacobi Failure and the Associator Defect of
the Antisymmetric Quaternionic Algebra*, below this article in this category; the operator is *The
Adjoint Operators of the Antisymmetric Quaternionic Algebra* and the form is *The Invariant Bilinear
Forms of the Antisymmetric Quaternionic Algebra*, both below this article in this category. The
companions are *The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation
$M_4(\mathbb{R})_L$*, above this article in this category, and *The Antisymmetric Quaternionic Algebra in
the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, above this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; the left regular representation is the map $\mathsf{M}_4$ sending $\tilde q$ to
the matrix of the left multiplication $r\mapsto\tilde q r$ in the basis $(e_0,e_1,e_2,e_3)$, and
$\mathsf{R}_4$ is the right regular representation. The model is multiplicative,
$\mathsf{M}_4(\tilde p\tilde q)=\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)$, the conjugation is the
transpose, $\mathsf{M}_4(\tilde q^{\natural})=\mathsf{M}_4(\tilde q)^{\mathsf T}$, and
$\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0$, $\det\mathsf{M}_4(\tilde q)=N(\tilde q)^2$. The
**quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$ and the **plain form**
$B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q$.

## The Operation in the Model

**Theorem (the halved conjugated commutator).**

$$
\mathsf{M}_4(\tilde p\diamond\tilde q)
=\tfrac12\bigl(\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q)-\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde p)\bigr)
=\tfrac12\bigl[\mathsf{M}_4(\tilde p)^{\mathsf T},\mathsf{M}_4(\tilde q)\bigr].
$$

*Proof.* The model is multiplicative and carries the conjugation to the transpose, so
$\mathsf{M}_4(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q)-\mathsf{M}_4(\tilde q)^{\mathsf T}\mathsf{M}_4(\tilde p)$,
and half of it is the image of the block. The plain antisymmetric block on the same model is the halved
**plain** commutator, the difference being the transpose on the first factor.

## The Image and the Kernel on the Matrices

**Theorem (the image).** The image of the block is the **traceless** part of the image of the model,

$$
\mathsf{M}_4\bigl(\mathbb{H}\diamond\mathbb{H}\bigr)=\{\mathsf{M}_4(\mathbf q):\operatorname{Tr}\mathsf{M}_4(\mathbf q)=0\},
$$

a three-dimensional real subspace, and the model is injective, so the kernel of the model map is $\{0\}$.

*Proof.* The values of the block are pure, so their matrices are traceless by
$\operatorname{Tr}\mathsf{M}_4(\tilde q)=4q_0$; conversely a traceless matrix of the image has $q_0=0$
by the same formula, so it is the image of a pure element, and the pure elements are values of the
block.

**Proposition (the kernel of the operator).** The kernel of the left multiplication operator of the
block, read in the model, is the image of the kernel in the coefficient space, which for $\tilde p\neq0$
is the line $\mathbb{R}\tilde p$: the matrices annihilated by the operator are the multiples of
$\mathsf{M}_4(\tilde p)$.

*Proof.* The model is an isomorphism of vector spaces intertwining the operator with its image, so
kernels correspond; the kernel in the coefficient space is the line of the element (*The Adjoint
Operators of the Antisymmetric Quaternionic Algebra*, below this article in this category).

## The Operator of the Block on the Matrices

**Proposition (the operator on the matrices).** In the model the operator acts by

$$
L^{\diamond}_{\tilde p}\mathsf{M}_4(\tilde r)
=\tfrac12\bigl(\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde r)-\mathsf{M}_4(\tilde r)^{\mathsf T}\mathsf{M}_4(\tilde p)\bigr),
$$

antisymmetric in the two matrix arguments; it is the difference of the multiplication by the fixed matrix
in the twisted product and its reverse.

**Theorem (the invariants of the operator).** The model invariants are

$$
\operatorname{Tr}L^{\diamond}_{\tilde p}=3p_0=\tfrac34\operatorname{Tr}\mathsf{M}_4(\tilde p),\qquad
\det L^{\diamond}_{\tilde p}=0,\qquad
\operatorname{rank}L^{\diamond}_{\tilde p}=3\ \text{for}\ \tilde p\neq0,
$$

with the kernel the line $\mathbb{R}\tilde p$ and the image the whole vector subspace.

*Proof.* The coefficient-space values are those of *The Adjoint Operators of the Antisymmetric
Quaternionic Algebra*, below this article in this category; the trace converts by
$\operatorname{Tr}\mathsf{M}_4(\tilde p)=4p_0$, and the determinant, the rank and the kernel are
basis-independent properties carried over by the intertwining isomorphism.

## The Two Commuting Copies

**Proposition (the two regular copies).** The left and the right regular representations commute,
$\mathsf{M}_4(\tilde p)\mathsf{R}_4(\tilde q)=\mathsf{R}_4(\tilde q)\mathsf{M}_4(\tilde p)$, with the
product the two-sided operator $r\mapsto\tilde p r\tilde q$. The left copy carries the block, the right
copy carries the conjugate block.

*Proof.* The associativity of the plain product gives $(\tilde p r)\tilde q=\tilde p(r\tilde q)$ for
every $r$, which is the equality of the two operators; the block is built from the left copy alone, and
the right copy commutes with it because it commutes with $\mathsf{M}_4(\tilde p)$ and the transpose of
that matrix.

**Remark (what the four by four model adds).** The two by two model carries the left representation
alone, the right one being its conjugate; the regular model carries both copies at once, and the
commuting pair is the whole operator algebra of the two-sided multiplications. For the block the
enrichment is idle: the operation uses the transposed left factor only, and the right copy is a
spectator.

## The Trace Form and the Invariant Form on the Matrices

**Theorem (the forms on the model).**

$$
\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)\bigr)=4B(\tilde p,\tilde q),\qquad
\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)^{\mathsf T}\bigr)=4N(\tilde p,\tilde q),
$$

the unique invariant form of the block reads the scalar parts,
$\varphi(\tilde p,\tilde q)=p_0q_0=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde p)\operatorname{Tr}\mathsf{M}_4(\tilde q)$,
and the operator trace form is
$K(\tilde p,\tilde q)=3p_0q_0-2\,\mathbf p\cdot\mathbf q=\tfrac18\bigl(5\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))+\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)^{\mathsf T})\bigr)$.

*Proof.* The model is multiplicative, so
$\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))=\operatorname{Tr}\mathsf{M}_4(\tilde p\tilde q)=4\mathrm{Sc}(\tilde p\tilde q)=4B(\tilde p,\tilde q)$
and $\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)^{\mathsf T})=\operatorname{Tr}\mathsf{M}_4(\tilde p\tilde q^{\natural})=4N(\tilde p,\tilde q)$;
the trace of the model is $4q_0$, whence $\varphi$; the combination is the operator trace form of *The
Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, below this article in this
category, and equals $3p_0q_0-2\,\mathbf p\cdot\mathbf q$ because
$\tfrac18(5\cdot4B+4N)=\tfrac12(N+5B)$.

**Remark (the coefficient form vanishes).** The values of the block are traceless, so
$\operatorname{Tr}\mathsf{M}_4(\tilde p\diamond\tilde q)=0$ and the trace form of the block is the zero
form; the only invariant form of the block remains the degenerate scalar-part form $\varphi$.

## The Comparison with the Quaternionic Algebra on the Model

| | the quaternionic algebra | the antisymmetric quaternionic block |
|---|---|---|
| the operation in the model | $\mathsf{M}_4(\tilde p)^{\mathsf T}\mathsf{M}_4(\tilde q)$ | the halved conjugated commutator |
| the image | the four-dimensional algebra of the regular matrices | the traceless part, of dimension three |
| the trace of a value | $4\,\mathrm{Sc}(\tilde p^{\natural}\tilde q)=4N(\tilde p,\tilde q)$ | $0$ |
| the conjugation | the transpose on the first factor | the same, antisymmetrised |
| the two copies | the left copy carries the product | the left copy carries the block |

**Remark (the reading of the table).** The quaternionic product on the regular model is the matrix
product with the transposed first factor, and the block is its halved antisymmetrisation; the plain
products on the same model are the matrix product and the halved plain commutator. The block shares with
the plain antisymmetric block the traceless image, and differs in that its commutator is conjugated, so
its values are the differences of a twisted product rather than of the plain one; over $\mathbb{C}$ the
values carry the Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ on the traceless regular matrices, and over
$\mathbb{R}$ the three-dimensional traceless part of $M_4(\mathbb{R})$, whose operation is the cross
product up to sign. The comparison with the companion blocks is *The Antisymmetric Plain Algebra in the
$4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, above this article in this category, and

## Summary

In the four by four left regular model the antisymmetric quaternionic block is the halved conjugated
commutator,
$\mathsf{M}_4(\tilde p\diamond\tilde q)=\tfrac12[\mathsf{M}_4(\tilde p)^{\mathsf T},\mathsf{M}_4(\tilde q)]$,
with the transpose the conjugation. Its image is the traceless part of the image of the model, a
three-dimensional real subspace, the pure elements being exactly the traceless regular matrices, and its
operator $L^{\diamond}_{\tilde p}$ acts on a matrix as the difference of the twisted product and its
reverse, of trace $3p_0=\tfrac34\operatorname{Tr}\mathsf{M}_4(\tilde p)$, determinant zero, rank three
off the origin and kernel the line of the element. The left and the right regular copies commute, and
the block uses the left one alone. The trace of the model reads the plain form,
$\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))=4B(\tilde p,\tilde q)$, the trace with
the transpose reads the quaternion form, the unique invariant form is
$\varphi=p_0q_0=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde p)\operatorname{Tr}\mathsf{M}_4(\tilde q)$,
and the operator trace form is
$\tfrac18(5\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))+\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)^{\mathsf T}))=3p_0q_0-2\,\mathbf p\cdot\mathbf q$.
The quaternionic product on the same model is the matrix product with the transposed first factor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde q)$ | the left regular matrix of $\tilde q$ |
| $\mathsf{M}_4(\tilde p)^{\mathsf T}=\mathsf{M}_4(\tilde p^{\natural})$ | the transpose, the conjugation |
| $\mathsf{M}_4(\tilde p\diamond\tilde q)=\tfrac12[\mathsf{M}_4(\tilde p)^{\mathsf T},\mathsf{M}_4(\tilde q)]$ | the block as the halved conjugated commutator |
| traceless part of the image | the image of the block, dimension three |
| $\operatorname{Tr}L^{\diamond}_{\tilde p}=3p_0$, rank $3$ | the invariants of the operator |
| $\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q))=4B$ | the plain form |
| $\operatorname{Tr}(\mathsf{M}_4(\tilde p)\mathsf{M}_4(\tilde q)^{\mathsf T})=4N$ | the quaternion form |
| $\varphi=p_0q_0=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde p)\operatorname{Tr}\mathsf{M}_4(\tilde q)$ | the unique invariant form |

## Further Reading

- *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$ of Quaternions*, for the model, its basis matrices, the trace and the multiplicativity.
- *The General Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, for the parent product on the model.
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* and *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, both below this article in this category, for the operator and the forms.
- *The Antisymmetric Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$* and *The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, both above this article in this category, for the companion readings.
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the failure behind the conjugated commutator.
