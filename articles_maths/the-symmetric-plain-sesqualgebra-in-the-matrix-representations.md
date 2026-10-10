# __The Symmetric Plain Sesqualgebra in the Matrix Representations__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural}\bigr) = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0 = H(\tilde P,\tilde Q)e_0$ (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article reads the block in the two matrix models of the chapter: the $2\times2$ realization $\mathsf{M}_2$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and the $4\times4$ left regular representation of the algebra.

The result that organises the article is that the block is a **scalar matrix** in both models. In the $2\times2$ realization the value of the product is $\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)\,I_2$, and the symmetrisation that produces it is the one that replaces the matrix product $\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$ by the half-sum with its adjugate: for a $2\times2$ matrix the identity $M + \operatorname{adj}M = (\operatorname{Tr}M)I$ converts the symmetrisation into the **trace-halving** $\tfrac12\operatorname{Tr}(M)I$, and the trace identity $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$ turns it into the Hermitian form. In the $4\times4$ regular model the block is the scalar matrix $H(\tilde P,\tilde Q)I_4$, of trace $4H$ and rank four, and its multiplication operators are the rank-one row matrices computed below.

**Boundaries.** The two models, the realization $\mathsf{M}_2$, the left regular representation, the Hilbert and Schmidt pairing and the tables of the models are *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation* and *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation*; they are cited here and not restated, and this article owns only the image of the block in them. The form $H$ is *Biquaternion Norm and Invertibility* and *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*; the multiplication operators as abstract operators are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears; positivity is stated as the positivity of the diagonal of $H$ and no norm of positive real values is named.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$. The realization is $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ with $\mathsf{M}_2(e_0) = I$, $\mathsf{M}_2(e_k) = -i\sigma_k$, so that $\mathsf{M}_2$ is multiplicative, $\mathsf{M}_2(\tilde Q^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde Q)$, $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$ and $\operatorname{Tr}\mathsf{M}_2(\tilde Q) = 2Q_0$ (*The General Plain Sesqualgebra in the $2\times2$ Matrix Representation*). The left regular representation is $\mathsf{M}_4(\tilde P)$, the matrix of $\tilde X\mapsto\tilde P\tilde X$ in the basis, with $\mathsf{M}_4(e_0) = I_4$. The block is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$.

## The Block in the $2\times2$ Realization

**Theorem (the value is a scalar matrix).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)\,I_2 ,
$$

a scalar multiple of the identity matrix; its trace is $2H(\tilde P,\tilde Q)$, its determinant $H(\tilde P,\tilde Q)^{2}$, and the rank of the matrix, as a linear map, is $2$ when $H\neq0$ and $0$ when $H = 0$. Read as an element of the block the value spans the one-dimensional centre.

*Proof.* $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ and $\mathsf{M}_2(e_0) = I$, so the value is $H I_2$; its trace is $2H$, its determinant $H^{2}$, and the rank of the nonzero scalar matrix $H I_2$ is the size, $2$, unless $H = 0$; as a central element the value spans the centre, of complex dimension one. The identity was recomputed to $4.4\times10^{-16}$. $\square$

**Theorem (the symmetrisation and the trace-halving).** Write $X = \mathsf{M}_2(\tilde P)$ and $Y = \mathsf{M}_2(\tilde Q)$, so that the general plain sesquilinear product has the matrix $XY^{\dagger}$. Then the block is the symmetrisation with the adjugate,

$$
\mathsf{M}_2(\tilde P\star\tilde Q) = \tfrac12\bigl(XY^{\dagger} + \operatorname{adj}(XY^{\dagger})\bigr) = \tfrac12\operatorname{Tr}(XY^{\dagger})\,I_2 ,
$$

and the trace identity $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$ exhibits the operation as the scalar multiple of the identity read as the Hermitian form.

*Proof.* $\mathsf{M}_2(\tilde P\tilde Q^{*}) = XY^{\dagger}$ because $\mathsf{M}_2$ is multiplicative and $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$; and $\mathsf{M}_2\bigl((\tilde P\tilde Q^{*})^{\natural}\bigr) = \operatorname{adj}\bigl(XY^{\dagger}\bigr)$ because $(\,\cdot\,)^{\natural}$ is carried to the adjugate. The identity $M + \operatorname{adj}M = (\operatorname{Tr}M)I$ for a $2\times2$ matrix $M$ gives the middle expression; and $\operatorname{Tr}(XY^{\dagger}) = \operatorname{Tr}\mathsf{M}_2(\tilde P\tilde Q^{*}) = 2\,\mathrm{Sc}(\tilde P\tilde Q^{*}) = 2H(\tilde P,\tilde Q)$, giving the last. The two identities were verified on random pairs to $0$ and $1.4\times10^{-15}$. $\square$

**Remark (the two involutions in the model).** The realization carries the two involutions of the product to the two operations of the model: the Hermitian conjugation ${}^{*}$ to the conjugate transpose, $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$, and the natural conjugation ${}^{\natural}$ to the adjugate, $\mathsf{M}_2(\tilde Q^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde Q)$. The product $\tilde P\tilde Q^{*}$ is the matrix product with the conjugate transpose in the second slot, and its symmetrisation is the half-sum with the adjugate; the pairing of the two involutions is what makes the value central, since $M + \operatorname{adj}M$ is the scalar $(\operatorname{Tr}M)I$ while $M + M^{\dagger}$ is not.

**Proposition (the form and its positivity in the model).** For all $\tilde P,\tilde Q$,

$$
H(\tilde P,\tilde Q) = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) , \qquad H(\tilde Q,\tilde Q) = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde Q)\bigr) > 0 \ \ (\tilde Q\neq0) ,
$$

so the form is the Hilbert and Schmidt pairing of the matrices, positive definite, and its Gram matrix on the basis is the identity.

*Proof.* The trace identity above and the positivity of the Hilbert and Schmidt pairing, which is the sum $\sum_\mu\lvert Q_\mu\rvert^{2}$ (*The General Plain Sesqualgebra in the $2\times2$ Matrix Representation*). $\square$

## The Block in the $4\times4$ Regular Representation

**Theorem (the value is a scalar matrix).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_4(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)\,I_4 ,
$$

of trace $4H(\tilde P,\tilde Q)$ and rank $4$ when $H\neq0$, and zero when $H = 0$.

*Proof.* $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ and $\mathsf{M}_4$ is multiplicative with $\mathsf{M}_4(e_0) = I_4$; so the regular matrix of the value is the scalar matrix $H I_4$. The identity was recomputed to $2.2\times10^{-16}$. $\square$

**Proposition (the multiplication operators in the regular model).** The two multiplication operators of the block are rank-one row matrices, in the conjugate-linear convention for the left family:

$$
L^{\star}_{\tilde R} \;\longleftrightarrow\; \sum_{j=0}^{3} R_j\,E_{0j} , \qquad R^{\star}_{\tilde R} \;\longleftrightarrow\; \sum_{j=0}^{3} \overline{R_j}\,E_{0j} ,
$$

where $E_{0j}$ is the matrix unit with the single non-zero entry $1$ in row $0$, column $j$; the left matrix acts on the conjugate of the coordinate vector, the map being conjugate-linear. Each operator has rank one for $\tilde R\neq0$, its image is the first coordinate line and its kernel the hyperplane $H(\tilde R,\cdot\,) = 0$.

*Proof.* $L^{\star}_{\tilde R}e_j = \tilde R\star e_j = H(\tilde R,e_j)e_0 = R_je_0$, so the $j$-th column of the matrix is $R_j$ in row $0$; and $R^{\star}_{\tilde R}e_j = e_j\star\tilde R = H(e_j,\tilde R)e_0 = \overline{R_j}e_0$, so the $j$-th column is $\overline{R_j}$ in row $0$. Both were verified to $0$. $\square$

**Remark (the two-sided symmetrised operator).** The regular model also carries the **two-sided** symmetrisation

$$
\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*}) + \mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*})\bigr) ,
$$

the matrix of the map $\tilde X\mapsto\tfrac12\bigl(\tilde P\tilde X\tilde Q^{*} + \tilde Q\tilde X\tilde P^{*}\bigr)$ on the module; for generic parameters its rank is $4$, and it is not the scalar matrix $H I_4$. The distinction is the one between a two-sided action on the module and the one-sided value of a central product: the block's *element* is the scalar matrix $H I_4$, and a two-sided action of its two factors is the operator above.

## The Invariance of the Symmetric Part

**Theorem (the value is invariant under the adjoint operation and under the change of model).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_2(\tilde P\star\tilde Q)^{\dagger} = \mathsf{M}_2(\tilde Q\star\tilde P) , \qquad \mathsf{M}_4(\tilde P\star\tilde Q) = \overline{\mathsf{M}_4(\tilde Q\star\tilde P)} ,
$$

and the scalar matrix $\mathsf{M}_2(\tilde P\star\tilde Q) = HI_2$ is fixed by conjugation by every invertible matrix of the model; a scalar matrix has no preferred basis, and the symmetric part of the block is therefore invariant under the choice of coordinates in the model.

*Proof.* $\mathsf{M}_2(\tilde P\star\tilde Q)^{\dagger} = \overline{H}I_2 = \mathsf{M}_2(\tilde Q\star\tilde P)$ because $H(\tilde Q,\tilde P) = \overline{H(\tilde P,\tilde Q)}$; likewise $\mathsf{M}_4(\tilde P\star\tilde Q) = HI_4 = \overline{\overline{H}I_4} = \overline{\mathsf{M}_4(\tilde Q\star\tilde P)}$; and $U(HI_2)U^{-1} = HI_2$ for every invertible $U$. $\square$

**Remark (the invariance in the two models at once).** The same scalar matrix is the image of the block in each model, so the block is a **central** element of the model algebra $M_2(\mathbb{C})$ and of $M_4(\mathbb{C})$: its image lies in the centre, which is the scalars, in both. The invariance of the symmetric part is the statement that the image is central, and it is the model form of the central image of the product.

## The Comparison with the Other Blocks

**The symmetric plain block (SPA).** Its product in the $2\times2$ model is $\tfrac12(XY+YX)$, the symmetrisation of the plain matrix product with no conjugate transpose; its value is not a scalar matrix, is not central, and its model reading is the ordinary matrix symmetrisation. The block of this article symmetrises with the **conjugate transpose and the adjugate**, and its value is a scalar matrix; the two symmetrisations differ by the whole involution layer, and in particular the SPA product has a unit in the model, the identity, while the block's value $HI_2$ is the identity only when $H = 1$.

**The general plain sesqualgebra (GPS).** Its product is $\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$, a general matrix; the block is its half-sum with the adjugate, which is the scalar matrix $\tfrac12\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})I_2$. The reconstruction $\mathrm{GPS} = \mathrm{SPS} + \mathrm{APS}$ reads in the model as the decomposition of a $2\times2$ matrix into its scalar (trace) part and its traceless part.

**The four models.** In the $4\times4$ regular model the same picture holds with $I_4$ in place of $I_2$: the block is the scalar matrix $HI_4$, its multiplication operators are the rank-one row matrices, and the trace is $4H$ instead of $2H$. The factor is the dimension, and the form is the same, which is the content of the two trace identities $\tfrac12\operatorname{Tr}_{2} = \tfrac14\operatorname{Tr}_{4} = H$.

## Worked Examples

**The basis in the $2\times2$ model.** $\mathsf{M}_2(e_\mu\star e_\nu) = \delta_{\mu\nu}I_2$; the sixteen products of the basis are the scalar matrices $I_2$ on the diagonal of the table and $0$ off it.

**A Hermitian element.** For $\tilde Q = e_0 + ie_3$ one has $H(\tilde Q,\tilde Q) = 1 + 1 = 2$, so $\mathsf{M}_2(\tilde Q\star\tilde Q) = 2I_2$, of trace $4$ and determinant $4$, the determinant being $H^{2} = 4$ as required. Here $\mathsf{M}_2(\tilde Q) = \begin{pmatrix}2&0\\0&0\end{pmatrix}$, not a scalar, while its symmetrised square is the scalar $2I_2$.

**A non-real value.** For $\tilde P = e_0$, $\tilde Q = ie_0$, $H = -i$, so $\mathsf{M}_2(\tilde P\star\tilde Q) = -iI_2$, of trace $-2i$ and determinant $-1$; the matrix is scalar and non-real, and its conjugate transpose is $\mathsf{M}_2(\tilde Q\star\tilde P) = iI_2$.

**A regular operator.** For $\tilde R = e_1 + ie_2$ the coordinates are $(R_0,R_1,R_2,R_3) = (0,1,i,0)$, so $L^{\star}_{\tilde R}\leftrightarrow E_{01} + iE_{02}$, of rank one; its kernel is the hyperplane $H(\tilde R,\cdot\,) = 0$, that is $\overline{X_1} + i\overline{X_2} = 0$ in the coordinates $\tilde X$ of the argument.

## Summary

In the $2\times2$ realization the block is the scalar matrix $\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_2$, obtained as the symmetrisation $\tfrac12\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger} + \operatorname{adj}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})\bigr)$ of the general plain sesquilinear product with the adjugate — the half-sum being the trace-halving $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr)I_2$ by the $2\times2$ identity $M + \operatorname{adj}M = (\operatorname{Tr}M)I$ — and identified with the Hermitian form through the trace identity $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$. Its trace is $2H$, its determinant $H^{2}$ and its rank $2$ as a matrix ($1$ as a central coordinate); the Hermitian conjugation is the conjugate transpose and the natural conjugation is the adjugate, and the pairing of the two involutions is what makes the value central. In the $4\times4$ regular representation the block is the scalar matrix $\mathsf{M}_4(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_4$, of trace $4H$ and rank $4$; the multiplication operators are the rank-one row matrices $\sum_j R_jE_{0j}$ and $\sum_j\overline{R_j}E_{0j}$; and the two-sided symmetrised operator $\tfrac12(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*}) + \mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*}))$ is generically of rank $4$ and is then distinct from the value. The block is **central** in both model algebras, so its image in each is a scalar matrix, invariant under the change of coordinates; the form $H$ is the Hilbert and Schmidt pairing in the $2\times2$ model and its positive definite diagonal is $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde Q)\bigr) = \sum_\mu\lvert Q_\mu\rvert^{2}$. The scalar matrix is the model form of the central image of the product, and the difference from the symmetric plain block is the involution layer of the symmetrisation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf{M}_2(e_0)=I_2$, $\mathsf{M}_2(e_k)=-i\sigma_k$ | the $2\times2$ realization |
| $\mathsf{M}_2(\tilde Q^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde Q)$, $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$ | the two involutions in the model |
| $\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_2$ | the block in the $2\times2$ model |
| $\tfrac12\bigl(XY^{\dagger} + \operatorname{adj}(XY^{\dagger})\bigr) = \tfrac12\operatorname{Tr}(XY^{\dagger})I_2$ | the symmetrisation is the trace-halving |
| $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$ | the trace identity |
| $\mathsf{M}_4(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_4$ | the block in the $4\times4$ regular model |
| $\sum_j R_jE_{0j}$, $\sum_j\overline{R_j}E_{0j}$ | the regular matrices of $L^{\star}_{\tilde R}$, $R^{\star}_{\tilde R}$; rank one |
| $\tfrac12(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*}) + \mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*}))$ | the two-sided symmetrised operator; generically rank four, not $HI_4$ |
| $HI_2$, $HI_4$ central | the invariance of the symmetric part |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product and its central image.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the abstract operators of which the matrices above are the regular reading.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-representation.md`), for the realization $\mathsf{M}_2$, the Hilbert and Schmidt pairing and the model tables.
- *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-plain-sesqualgebra-in-the-4x4-matrix-representation.md`), for the left regular representation and its tables.
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and the two involutions in it.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form $H$, its Gram matrix and its positivity.
- *The Symmetric Plain Algebra in the Matrix Representations* (`articles_maths/the-symmetric-plain-algebra-in-the-matrix-representations.md`), the sibling whose symmetrisation carries no conjugate transpose.
