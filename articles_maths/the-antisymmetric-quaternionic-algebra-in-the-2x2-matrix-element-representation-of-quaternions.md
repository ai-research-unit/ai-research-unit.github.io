# __The Antisymmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The antisymmetric quaternionic algebra of $\mathbb{H}$ is the operation
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\mathbf q-q_0\mathbf p-\mathbf p\times\mathbf q$ of *Introduction to the Antisymmetric Quaternionic
Algebra of Quaternions*. This article reads it on the embedding $\mathbb{H}\hookrightarrow M_2(\mathbb{C})$
of *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions*, where
the parent product becomes the **conjugated product** $\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)$
and the antisymmetrization becomes the **conjugated commutator**. It gives the matrix form, the image,
the invariants, the invariant forms and the comparison with the other blocks on the same model.

The reading is the conjugated twin of the plain one: the plain antisymmetrization is the commutator of
the matrix images, and the antisymmetrisation of the parent is the halved conjugated commutator, whose
values are the **anti-Hermitian** matrices.

**This is not the algebra $\mathbb{H}$.** The model is an algebra embedding of the plain product; the
antisymmetric quaternionic block is read on it through the conjugation of the first factor and is not
the matrix product. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar
is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the
natural sign and gives nothing new. The symbol $\diamond$ is reserved for this block.

The model and its multiplicativity are *Introduction to the $2\times2$ Matrix Element Representation
$M_2(\mathbb{C})$ of Quaternions*; the block and its failure are *Introduction to the Antisymmetric
Quaternionic Algebra of Quaternions* and *The Jacobi Failure and the Associator Defect of the
Antisymmetric Quaternionic Algebra*, below this article in this category; the form is *The Invariant
Bilinear Forms of the Antisymmetric Quaternionic Algebra*, below this article in this category. The
companion articles are *The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation
$M_2(\mathbb{C})$*, above this article in this category, and *The Antisymmetric Quaternionic Algebra in
the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; the model is

$$
\mathsf{M}_2(\tilde q)=\begin{pmatrix}q_0-iq_3 & -iq_1-q_2\\ -iq_1+q_2 & q_0+iq_3\end{pmatrix},
$$

with $\mathsf{M}_2(e_0)=\mathrm{I}_2$, $\mathsf{M}_2(e_1)=-i\sigma_1$, $\mathsf{M}_2(e_2)=-i\sigma_2$,
$\mathsf{M}_2(e_3)=-i\sigma_3$, the Pauli matrices. The plain product is the matrix product,
$\mathsf{M}_2(\tilde p\tilde q)=\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)$, the parent product is
$\mathsf{M}_2(\tilde p^{\natural}\tilde q)=\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)$, and
the conjugation is the Hermitian adjoint, $\mathsf{M}_2(\tilde q^{\natural})=\mathsf{M}_2(\tilde q)^{\dagger}$.
The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$ and the **plain form**
$B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q$.

## The Model and the Conjugated Commutator

**Theorem (the bracket is the halved conjugated commutator).**

$$
\mathsf{M}_2(\tilde p\diamond\tilde q)=\tfrac12\bigl(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)-\mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde p)\bigr)
=\tfrac12\bigl[\mathsf{M}_2(\tilde p)^{\dagger},\mathsf{M}_2(\tilde q)\bigr] .
$$

*Proof.* The model is multiplicative and the conjugation is the Hermitian adjoint, so
$\mathsf{M}_2(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)-\mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde p)$,
and half of it is the image of the block.

**Remark (the contrast with the plain block on the same model).** The plain antisymmetrization is the
halved plain commutator $\tfrac12[\mathsf{M}_2(\tilde p),\mathsf{M}_2(\tilde q)]$, of values the
traceless matrices of the image; the antisymmetrization of the parent is the halved **conjugated**
commutator, of values the anti-Hermitian matrices. The two agree on the pure elements up to sign, since
$\mathsf{M}_2(\mathbf u)^{\dagger}=-\mathsf{M}_2(\mathbf u)$ for a pure $\mathbf u$.

## The Image: the Anti-Hermitian Matrices

**Theorem (the image).** Every value of the block is an **anti-Hermitian** matrix,

$$
\mathsf{M}_2(\tilde p\diamond\tilde q)^{\dagger}=-\,\mathsf{M}_2(\tilde p\diamond\tilde q),
$$

of trace zero, and the image of the block is the three-dimensional real space of anti-Hermitian
traceless matrices, which is the Lie algebra $\mathfrak{su}(2)$.

*Proof.* The conjugated commutator of two matrices $X^{\dagger}Y-Y^{\dagger}X$ is anti-Hermitian, since
its adjoint is $Y^{\dagger}X-X^{\dagger}Y$, its negative; the trace vanishes because the trace of a
commutator vanishes. The space of anti-Hermitian traceless $2\times2$ matrices is
$i\,\mathfrak{sl}(2,\mathbb{C})_{\text{Hermitian}}=\mathfrak{su}(2)$, of real dimension three, and the
image is the whole of it, the pure values generating it.

**Remark (the failure is the commutator of the failure).** The image is the Lie algebra
$\mathfrak{su}(2)$, but the operation is not the Lie bracket of the model: the model bracket would be
the plain commutator, while the block is the conjugated commutator, and it is the conjugation that
breaks the Jacobi identity (*The Jacobi Failure and the Associator Defect of the Antisymmetric
Quaternionic Algebra*, below this article in this category). The block is a Lie bracket on the image
only in the sense that its restriction to the pure elements is the cross product up to sign.

## The Invariants

**Theorem.** The image matrix $\mathsf{M}_2(\tilde p\diamond\tilde q)$ has

$$
\operatorname{Tr}\mathsf{M}_2(\tilde p\diamond\tilde q)=0,\qquad
\det\mathsf{M}_2(\tilde p\diamond\tilde q)=N(\tilde p\diamond\tilde q)=|\tilde p\diamond\tilde q|^2,
\qquad
\mathsf{M}_2(\tilde p\diamond\tilde q)^2=-N(\tilde p\diamond\tilde q)\,\mathrm{I}_2 ,
$$

the determinant being the squared norm of the value, and the matrix is anti-Hermitian.

*Proof.* The value is pure, so its matrix is traceless; an anti-Hermitian traceless $2\times2$ matrix
$X$ satisfies $X^2=-\det(X)\,\mathrm{I}_2$ and $\det X=N(X)$, the norm of the pure element, by the
model's determinant formula in *Introduction to the $2\times2$ Matrix Element Representation
$M_2(\mathbb{C})$ of Quaternions*.

## The Invariant Forms

**Theorem (the forms on the model).** The trace forms of the model read the two forms of the space,

$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger}\bigr)=N(\tilde p,\tilde q),\qquad
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)\bigr)=B(\tilde p,\tilde q),
$$

the unique invariant form of the block is the scalar-part form

$$
\varphi(\tilde p,\tilde q)=p_0q_0=\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde p)\cdot\operatorname{Tr}\mathsf{M}_2(\tilde q),
$$

and the operator trace form is the combination
$K(\tilde p,\tilde q)=\tfrac12\bigl(N(\tilde p,\tilde q)+5B(\tilde p,\tilde q)\bigr)=3p_0q_0-2\,\mathbf p\cdot\mathbf q$.

*Proof.* The model is multiplicative, so
$\operatorname{Tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger})=\operatorname{Tr}\mathsf{M}_2(\tilde p\tilde q^{\natural})=2N(\tilde p,\tilde q)$
and $\operatorname{Tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q))=2B(\tilde p,\tilde q)$, by the trace
formula of the model; the trace of the model is $2q_0$, whence $\varphi$; the combination is the
operator trace form of *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, below
this article in this category, solved in the two forms.

**Remark (the block removes the trace).** The coefficient form of the block vanishes,
$\operatorname{Tr}\mathsf{M}_2(\tilde p\diamond\tilde q)=0$, because the values are traceless; the trace
form of the block is the zero form, and the only invariant form of the block remains the degenerate
$\varphi$ of the scalar-part slot.

## The Comparison with the Other Blocks on the Model

The six products of the space read on the same model:

| block | the matrix form |
|---|---|
| $\mathrm{GPA}$ | $\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)$ |
| $\mathrm{SPA}$ | $\tfrac12\bigl(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)+\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p)\bigr)$ |
| $\mathrm{APA}$ | $\tfrac12\bigl(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)-\mathsf{M}_2(\tilde q)\mathsf{M}_2(\tilde p)\bigr)$ |
| $\mathrm{GQA}$ | $\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)$ |
| $\mathrm{SQA}$ | $N(\tilde p,\tilde q)\,\mathrm{I}_2$ |
| $\mathrm{AQA}$ | $\tfrac12\bigl(\mathsf{M}_2(\tilde p)^{\dagger}\mathsf{M}_2(\tilde q)-\mathsf{M}_2(\tilde q)^{\dagger}\mathsf{M}_2(\tilde p)\bigr)$ |

**Remark (the reading of the table).** The upper three rows are the products of the plain row, the lower
three the products of the conjugated row; the general products are the matrix product and the conjugated
matrix product, and within each row the symmetric and the antisymmetric halves are the corresponding
halved sums and differences. The antisymmetric quaternionic block is the lower antisymmetric entry: the
halved conjugated commutator, of anti-Hermitian values, while the plain antisymmetric block is the upper
antisymmetric entry, of traceless values. The plain reading on the same model is *The Antisymmetric
Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, above this article in
this category.

## Summary

In the two by two complex model the antisymmetric quaternionic block is the halved conjugated
commutator, $\mathsf{M}_2(\tilde p\diamond\tilde q)=\tfrac12[\mathsf{M}_2(\tilde p)^{\dagger},\mathsf{M}_2(\tilde q)]$,
whose values are the **anti-Hermitian** traceless matrices, that is the Lie algebra $\mathfrak{su}(2)$;
the block is not the commutator of the model, and it is the conjugation that breaks the Jacobi
identity. The invariants are $\operatorname{Tr}\mathsf{M}_2(\tilde p\diamond\tilde q)=0$,
$\det\mathsf{M}_2(\tilde p\diamond\tilde q)=N(\tilde p\diamond\tilde q)=|\tilde p\diamond\tilde q|^2$ and
$\mathsf{M}_2(\tilde p\diamond\tilde q)^2=-N(\tilde p\diamond\tilde q)\mathrm{I}_2$. The trace of the
model with the conjugate reads the quaternion form, $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger})=N(\tilde p,\tilde q)$,
the plain trace reads the plain form, the unique invariant form of the block is
$\varphi=p_0q_0=\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde p)\operatorname{Tr}\mathsf{M}_2(\tilde q)$,
and the operator trace form is $\tfrac12(N+5B)=3p_0q_0-2\,\mathbf p\cdot\mathbf q$. The six products are
the matrix product and its symmetric and antisymmetric halves, and the conjugated matrix product and its
halves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(\tilde q)$ | the two by two complex model |
| $\mathsf{M}_2(\tilde p\diamond\tilde q)=\tfrac12[\mathsf{M}_2(\tilde p)^{\dagger},\mathsf{M}_2(\tilde q)]$ | the block as the halved conjugated commutator |
| anti-Hermitian traceless | the image, the Lie algebra $\mathfrak{su}(2)$ |
| $\det=N(\tilde p\diamond\tilde q)$, $X^2=-N(X)\mathrm{I}_2$ | the invariants |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde p)\mathsf{M}_2(\tilde q)^{\dagger})=N(\tilde p,\tilde q)$ | the quaternion form |
| $\varphi=p_0q_0=\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde p)\operatorname{Tr}\mathsf{M}_2(\tilde q)$ | the unique invariant form |

## Further Reading

- *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions*, for the model, the basis images and the multiplicativity.
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions* and *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the block and its failure.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the unique invariant form and the operator trace form.
- *The Antisymmetric Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, above this article in this category, for the companion block on the same model.
- *The Antisymmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{R})_L$*, below this article in this category, for the companion model.
