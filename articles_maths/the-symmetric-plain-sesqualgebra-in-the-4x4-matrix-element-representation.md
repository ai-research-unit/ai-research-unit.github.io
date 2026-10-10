# __The Symmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural}\bigr) = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0 = H(\tilde P,\tilde Q)e_0$ (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article reads the block in the $4\times4$ left regular representation of the algebra of *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; it is the second of the two representation articles of the block, and its companion *The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* repeats the reading on the realization $\mathsf{M}_2$.

The result that organises the article is that the block is a **scalar matrix** in the model. The value of the product is $\mathsf{M}_4(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)\,I_4$, of trace $4H$ and rank four; its multiplication operators are the rank-one row matrices computed below; and the two-sided symmetrised operator of a pair of factors is a rank-four operator distinct from the value. The regular model carries the central image of the product to a scalar matrix just as the realization does, but with the dimension of the module in place of the dimension of the coefficient space.

**Boundaries.** The model, the left regular representation, the Hilbert and Schmidt pairing and the tables of the model are *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; they are cited here and not restated, and this article owns only the image of the block in the model. The form $H$ is *Biquaternion Norm and Invertibility* and *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*; the multiplication operators as abstract operators are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears; positivity is stated as the positivity of the diagonal of $H$ and no norm of positive real values is named.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$. The left regular representation is $\mathsf{M}_4(\tilde P)$, the matrix of $\tilde X\mapsto\tilde P\tilde X$ in the basis, with $\mathsf{M}_4(e_0) = I_4$ and $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf T}$; the right regular matrix of an element $\tilde X$ is written $\mathsf{M}_4^{R}(\tilde X)$ (*The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*). The block is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$.

## The Block in the Regular Representation

**Theorem (the value is a scalar matrix).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_4(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)\,I_4 ,
$$

of trace $4H(\tilde P,\tilde Q)$ and rank $4$ when $H\neq0$, and zero when $H = 0$.

*Proof.* $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ and $\mathsf{M}_4$ is multiplicative with $\mathsf{M}_4(e_0) = I_4$; so the regular matrix of the value is the scalar matrix $H I_4$. Verified on the model. $\square$

**Proposition (the multiplication operators in the regular model).** The two multiplication operators of the block are rank-one row matrices, in the conjugate-linear convention for the left family:

$$
L^{\star}_{\tilde R} \;\longleftrightarrow\; \sum_{j=0}^{3} R_j\,E_{0j} , \qquad R^{\star}_{\tilde R} \;\longleftrightarrow\; \sum_{j=0}^{3} \overline{R_j}\,E_{0j} ,
$$

where $E_{0j}$ is the matrix unit with the single non-zero entry $1$ in row $0$, column $j$; the left matrix acts on the conjugate of the coordinate vector, the map being conjugate-linear. Each operator has rank one for $\tilde R\neq0$, its image is the first coordinate line and its kernel the hyperplane $H(\tilde R,\cdot\,) = 0$.

*Proof.* $L^{\star}_{\tilde R}e_j = \tilde R\star e_j = H(\tilde R,e_j)e_0 = R_je_0$, so the $j$-th column of the matrix is $R_j$ in row $0$; and $R^{\star}_{\tilde R}e_j = e_j\star\tilde R = H(e_j,\tilde R)e_0 = \overline{R_j}e_0$, so the $j$-th column is $\overline{R_j}$ in row $0$. Verified on the model. $\square$

**Theorem (the symmetrisation and the transpose-halving).** Write $X = \mathsf{M}_4(\tilde P)$ and $Y = \mathsf{M}_4(\tilde Q)$, so that the general plain sesquilinear product has the matrix $XY^{\dagger}$. Then the block is the symmetrisation with the transpose,

$$
\mathsf{M}_4(\tilde P\star\tilde Q) = \tfrac12\bigl(XY^{\dagger} + (XY^{\dagger})^{\mathsf T}\bigr) = \tfrac14\operatorname{Tr}(XY^{\dagger})\,I_4 = H(\tilde P,\tilde Q)\,I_4 ,
$$

the analogue of the adjugate symmetrisation of the realization, with the transpose in place of the adjugate.

*Proof.* $\mathsf{M}_4(\tilde P\tilde Q^{*}) = XY^{\dagger}$ because $\mathsf{M}_4$ is multiplicative and $\mathsf{M}_4(\tilde Q^{*}) = \mathsf{M}_4(\tilde Q)^{\dagger}$; and $\mathsf{M}_4\bigl((\tilde P\tilde Q^{*})^{\natural}\bigr) = (XY^{\dagger})^{\mathsf T}$ because the natural conjugation is carried to the transpose. On a regular matrix $M=\mathsf{M}_4(\tilde X)$ one has $\tfrac12(M+M^{\mathsf T}) = \tfrac12\mathsf{M}_4(\tilde X+\tilde X^{\natural}) = \mathsf{M}_4(X_0e_0) = X_0 I_4$, the average of an element and its natural conjugate being the scalar $X_0e_0$; at $M=XY^{\dagger}=\mathsf{M}_4(\tilde P\tilde Q^{*})$ the scalar is $H(\tilde P,\tilde Q)$, and $\tfrac14\operatorname{Tr}(M)=H(\tilde P,\tilde Q)$ because $\operatorname{Tr}\mathsf{M}_4=4\,\mathrm{Sc}$. Verified on random pairs. $\square$

**Remark (the two involutions in the regular model).** The regular model carries both involutions of the product to operations on the matrix: the natural conjugation to the transpose, $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf T}$, and the Hermitian conjugation to the conjugate transpose, $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$. The two identities hold together because the structure constants of the basis are real, so that conjugate coefficients give conjugate matrices, $\mathsf{M}_4(\overline{\tilde X})=\overline{\mathsf{M}_4(\tilde X)}$: the conjugate transpose is the composition of the transpose and the coefficientwise conjugation, and it is the matrix of ${}^{*}$. The pairing of the two involutions is what makes the value central, the average $\tfrac12(M+M^{\mathsf T})$ being the scalar $X_0I_4$ for a regular matrix.

**Remark (the two-sided symmetrised operator).** The regular model also carries the **two-sided** symmetrisation

$$
\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*}) + \mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*})\bigr) ,
$$

the matrix of the map $\tilde X\mapsto\tfrac12\bigl(\tilde P\tilde X\tilde Q^{*} + \tilde Q\tilde X\tilde P^{*}\bigr)$ on the module; for generic parameters its rank is $4$, and it is not the scalar matrix $H I_4$. The distinction is the one between a two-sided action on the module and the one-sided value of a central product: the block's *element* is the scalar matrix $H I_4$, and a two-sided action of its two factors is the operator above.

## The Invariance of the Symmetric Part

**Theorem (the value is invariant under the change of model).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_4(\tilde P\star\tilde Q) = \overline{\mathsf{M}_4(\tilde Q\star\tilde P)} ,
$$

and the scalar matrix $\mathsf{M}_4(\tilde P\star\tilde Q) = HI_4$ is fixed by conjugation by every invertible matrix of the model; a scalar matrix has no preferred basis, and the symmetric part of the block is therefore invariant under the choice of coordinates in the model.

*Proof.* $\mathsf{M}_4(\tilde P\star\tilde Q) = HI_4 = \overline{\overline{H}I_4} = \overline{\mathsf{M}_4(\tilde Q\star\tilde P)}$ because $H(\tilde Q,\tilde P) = \overline{H(\tilde P,\tilde Q)}$; and $U(HI_4)U^{-1} = HI_4$ for every invertible $U$. Verified on the model. $\square$

**Remark (the value is central).** The same scalar matrix is the image of the block in the regular model, so the block is a **central** element of the matrix algebra $M_4(\mathbb{C})$: its image lies in the centre, which is the scalars. The invariance of the symmetric part is the statement that the image is central, and it is the model form of the central image of the product.

## Worked Examples

**The basis in the regular model.** $\mathsf{M}_4(e_\mu\star e_\nu) = \delta_{\mu\nu}I_4$; the sixteen products of the basis are the scalar matrices $I_4$ on the diagonal of the table and $0$ off it.

**A regular operator.** For $\tilde R = e_1 + ie_2$ the coordinates are $(R_0,R_1,R_2,R_3) = (0,1,i,0)$, so $L^{\star}_{\tilde R}\leftrightarrow E_{01} + iE_{02}$, of rank one; its kernel is the hyperplane $H(\tilde R,\cdot\,) = 0$, that is $\overline{X_1} + i\overline{X_2} = 0$ in the coordinates $\tilde X$ of the argument.

**A Hermitian element.** For $\tilde Q = e_0 + ie_3$ one has $H(\tilde Q,\tilde Q) = 2$, so $\mathsf{M}_4(\tilde Q\star\tilde Q) = 2I_4$, of trace $8$ and determinant $16$, the determinant being $H^{4} = 16$ as required; the scalar matrix is the value of the block, while the two-sided operator of the pair is generically of rank four and distinct from it.

## The Matrices

**The generators.** The regular model is fixed on the basis by four matrices:

$$
\mathsf{M}_4(e_0)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

A general element is the block matrix

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A&B\\-B&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_0&-Q_1\\Q_1&Q_0\end{pmatrix},\qquad
B=\begin{pmatrix}-Q_2&-Q_3\\-Q_3&Q_2\end{pmatrix},
$$

The general element has trace $4Q_0$ and determinant $N(\tilde Q)^2$.

**The trace-halving, entry by entry.** The two involutions are the conjugate transpose and the transposition, and the identity $M+M^{\mathsf T}=(\operatorname{Tr}M/2)I_4$ of the regular model halves the trace of the conjugate-transposed product, so the value is the scalar matrix

$$
\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}+\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}\bigr)^{\mathsf T}\bigr)
=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}\bigr)I_4
=H(\tilde P,\tilde Q)\,I_4 .
$$

At the pair $e_1,e_1$ the conjugate-transposed product is the identity, since $\mathsf{M}_4(e_1)^{\dagger}=-\mathsf{M}_4(e_1)$ and $\mathsf{M}_4(e_1)^2=-I_4$, so $\mathsf{M}_4(e_1)\mathsf{M}_4(e_1)^{\dagger}=I_4$ of trace four; the value is $I_4=H(e_1,e_1)I_4$.

**The two models.** The value is the scalar matrix of the form in both models, and the mechanism is the same trace-halving, the number of entries of the trace being two in the realization and four in the regular model.

## Summary

In the $4\times4$ left regular representation the block is the scalar matrix $\mathsf{M}_4(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_4$, of trace $4H$ and rank $4$, obtained as the symmetrisation $\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger} + (\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger})^{\mathsf T}\bigr)$ of the general plain sesquilinear product with the transpose, the transpose-halving $\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}\bigr)I_4$ by the identity $\tfrac12(M+M^{\mathsf T})=X_0I_4$ on a regular matrix: the regular model carries the natural conjugation to the transpose and the Hermitian conjugation to the conjugate transpose, so the transpose plays here the role the adjugate plays in the realization; the multiplication operators are the rank-one row matrices $\sum_j R_jE_{0j}$ and $\sum_j\overline{R_j}E_{0j}$, of image the first coordinate line and kernel the hyperplane $H(\tilde R,\cdot\,) = 0$; and the two-sided operator $\tfrac12(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*}) + \mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*}))$ is generically of rank $4$ and distinct from the value. The block is **central** in the matrix algebra, so its image is a scalar matrix, invariant under the change of coordinates, and the value satisfies $\mathsf{M}_4(\tilde P\star\tilde Q) = \overline{\mathsf{M}_4(\tilde Q\star\tilde P)}$. The Hilbert and Schmidt pairing is the same form as in the realization, with the trace identity $\tfrac14\operatorname{Tr}_4 = H$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde P)$ | the left regular representation, $\mathsf{M}_4(e_0)=I_4$ |
| $\mathsf{M}_4(\tilde Q^{\natural}) = \mathsf{M}_4(\tilde Q)^{\mathsf T}$, $\mathsf{M}_4(\tilde Q^{*}) = \mathsf{M}_4(\tilde Q)^{\dagger}$ | the two involutions in the regular model |
| $\mathsf{M}_4(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_4$ | the block in the regular model |
| $\tfrac12\bigl(XY^{\dagger} + (XY^{\dagger})^{\mathsf T}\bigr) = \tfrac14\operatorname{Tr}(XY^{\dagger})I_4$ | the symmetrisation is the transpose-halving |
| $\sum_j R_jE_{0j}$, $\sum_j\overline{R_j}E_{0j}$ | the regular matrices of $L^{\star}_{\tilde R}$, $R^{\star}_{\tilde R}$; rank one |
| $\tfrac12(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*}) + \mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*}))$ | the two-sided symmetrised operator; generically rank four, not $HI_4$ |
| $\mathsf{M}_4(\tilde P\star\tilde Q) = \overline{\mathsf{M}_4(\tilde Q\star\tilde P)}$ | the invariance of the symmetric part |
| $HI_4$ central | the value is a scalar matrix |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product and its central image.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the abstract operators of which the matrices above are the regular reading.
- *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-plain-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the left regular representation and its tables.
- *The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the reading on the realization.
- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the left regular representation.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form $H$, its Gram matrix and its positivity.
