# __The General Plain Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

The left regular representation of $\mathbb{H}$ is the map that sends a quaternion to the matrix of left multiplication by it in the basis $e_0,e_1,e_2,e_3$. On that image the plain product is the product of the regular matrices, the plain form is a quarter of the trace pairing, the invariants are the trace $4q_0$ and the determinant $N(\tilde q)^2$, the transpose corresponds to the natural sign, and the centraliser of the image is the second, commuting copy of the algebra, namely the right regular representation of the opposite. This article reads the block's objects in that model and compares with the complex case. The plain product is *Introduction to the General Plain Algebra of Quaternions*, above this article in this category; the form and the transpose calculus are *Association and the Transpose on the General Plain Algebra*, above this article in this category; the enveloping algebra and the two commuting copies are *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, above this article in this category; the complex matrix model is *The General Plain Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, above this article in this category.

## The Left Regular Representation

**Definition.** The **left regular representation** is the map

$$
\mathsf M_4:\mathbb{H}\to M_4(\mathbb{R}),\qquad \mathsf M_4(\tilde q)(\tilde r)=\tilde q\tilde r,
$$

the matrix of the operator $L_{\tilde q}$ in the basis $e_0,e_1,e_2,e_3$; its entries are the coordinates of the products, $(\mathsf M_4(\tilde q))_{ij}=$ the $e_i$-coordinate of $\tilde q e_j$.

**Theorem.** $\mathsf M_4$ is an injective algebra homomorphism, $\mathsf M_4(\tilde p\tilde q)=\mathsf M_4(\tilde p)\mathsf M_4(\tilde q)$, and its image has real dimension $4$.

*Proof.* The left multiplications satisfy $L_{\tilde p}L_{\tilde q}=L_{\tilde p\tilde q}$, and the matrix of a composite is the product of the matrices; injectivity is $L_{\tilde q}(e_0)=\tilde q$, so only $0$ has the zero matrix, and the dimension is $4$.

**Example.** For the basis elements,

$$
\mathsf M_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
\mathsf M_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},
$$

and $\mathsf M_4(e_3)=\mathsf M_4(e_1)\mathsf M_4(e_2)$, $\mathsf M_4(e_0)=\mathrm I_4$.

## Standard Forms and Conventions

**Conventions of the block.** The generic product is written by juxtaposition, never with the bracket $[\,]$; the basis is $e_0,e_1,e_2,e_3$ with $e_0$ the unit; the generic element is $\tilde q$; the natural sign is ${}^{\natural}$, the quaternion conjugation; $L_{\tilde a}$ and $R_{\tilde b}$ are the left and right multiplications; and $\tilde a[\,]\tilde b$ is Conway's sandwich $\tilde q\mapsto\tilde a\tilde q\tilde b$. Each name is used in one sense only.

*Remark.* The conventions are collected here because the article is the last of the block and uses the whole apparatus: a reader who meets a symbol above reads its fixed sense here. The list is a convention and not a mathematical result.

## The Product

**Theorem.** On the image, the plain product is the matrix product: $\mathsf M_4(\tilde p\tilde q)=\mathsf M_4(\tilde p)\mathsf M_4(\tilde q)$. In particular the image is a four-dimensional subalgebra of $M_4(\mathbb{R})$ isomorphic to $\mathbb{H}$, with the identity matrix for unit.

*Proof.* The homomorphism property above.

## The Form

**Theorem.** The plain form is a quarter of the trace pairing:

$$
\mathrm B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)=\tfrac14\operatorname{tr}\bigl(\mathsf M_4(\tilde p)\mathsf M_4(\tilde q)\bigr).
$$

*Proof.* $\operatorname{tr}\mathsf M_4(\tilde q)=4q_0$: the diagonal entry $(\mathsf M_4(\tilde q))_{ii}$ is the $e_i$-coordinate of $\tilde qe_i$, and summing over $i$ the contribution of the scalar part of $\tilde q$ is $4q_0$ while the vector contributions cancel pairwise; hence $\operatorname{tr}(\mathsf M_4(\tilde p\tilde q))=4(\tilde p\tilde q)_0=4\,\mathrm{Sc}(\tilde p\tilde q)$.

**Theorem (the same Gram matrix).** $G_{\mu\nu}=\tfrac14\operatorname{tr}(\mathsf M_4(e_\mu)\mathsf M_4(e_\nu))=\operatorname{diag}(1,-1,-1,-1)=D$, of signature $(1,3)$, the same matrix as in the $2\times2$ model.

*Proof.* $\operatorname{tr}\mathsf M_4(e_0)=4$ and $\operatorname{tr}\mathsf M_4(e_k^2)=\operatorname{tr}(-\mathrm I_4)=-4$, with the cross traces $0$; the computation is the one of the trace of the product of the four basis matrices.

## The Two Commuting Copies

**Definition.** The **right regular representation** is $\mathsf R_4(\tilde q)(\tilde r)=\tilde r\tilde q$, the matrix of $R_{\tilde q}$; it is an anti-homomorphism, $\mathsf R_4(\tilde p\tilde q)=\mathsf R_4(\tilde q)\mathsf R_4(\tilde p)$, and an algebra map on $\mathbb{H}^{\mathrm{op}}$.

**Theorem.** The two images commute: $\mathsf M_4(\tilde p)\mathsf R_4(\tilde q)=\mathsf R_4(\tilde q)\mathsf M_4(\tilde p)$ for all $\tilde p,\tilde q$, and the image of $\mathsf M_4$ and the image of $\mathsf R_4$ are two commuting four-dimensional algebras inside $M_4(\mathbb{R})$.

*Proof.* $L_{\tilde p}R_{\tilde q}=R_{\tilde q}L_{\tilde p}$, the commutativity of the two-sided operators, read in the regular matrices.

## The Transposition Relation

**Theorem.** $\mathsf M_4(\tilde q)^{\mathsf T}=\mathsf M_4(\tilde q^{\natural})$: the transpose of the left regular matrix is the left regular matrix of the natural sign.

*Proof.* $(\mathsf M_4(\tilde q))_{ij}$ is the $e_i$-coordinate of $\tilde qe_j$, that is $\mathrm{Sc}(\tilde qe_je_i^{\natural})$ up to the sign of the basis product; transposing exchanges $i$ and $j$, and inserting the natural sign on the parameter absorbs the sign, giving the entry of $\mathsf M_4(\tilde q^{\natural})$. The identity is checked on the four basis matrices, and holds on all of them.

**Corollary.** The image is closed under transpose, and the transpose of the image is the natural sign; the transposition is the matrix form of the self-transpose operator $\natural$ of *Association and the Transpose on the General Plain Algebra*, above this article in this category.

## The Invariants

**Theorem (trace and determinant).** For every $\tilde q$,

$$
\operatorname{tr}\mathsf M_4(\tilde q)=4q_0,\qquad \det\mathsf M_4(\tilde q)=N(\tilde q)^2=(q_0^2+q_1^2+q_2^2+q_3^2)^2 .
$$

*Proof.* The trace is above. For the determinant, the operator $L_{\tilde q}$ has the complex eigenvalues $\alpha$ and $\overline{\alpha}$ with multiplicity two, where $\alpha=q_0+|\vec q|i$ is a root of the complex quadratic $\alpha^2-2q_0\alpha+N(\tilde q)=0$; hence $\det L_{\tilde q}=\alpha^2\overline{\alpha}^2=N(\tilde q)^2$. The eigenvalues are read from the minimal polynomial of $L_{\tilde q}$ in the two-dimensional subalgebra generated by $\tilde q$, which is a copy of $\mathbb{C}$.

**Corollary.** $\mathsf M_4(\tilde q)$ is invertible exactly when $\tilde q\neq0$, and $\det\mathsf M_4(\tilde q)>0$; the image of the group of units is the group of invertible matrices in the image, isomorphic to $\mathbb{H}^{\times}$.

*Proof.* $\det=N(\tilde q)^2>0$ for $\tilde q\neq0$, and the image is a subalgebra.

## The Double Centraliser

**Theorem.** The centraliser of the image of $\mathsf M_4$ in $M_4(\mathbb{R})$ is the image of $\mathsf R_4$, and the centraliser of the image of $\mathsf R_4$ is the image of $\mathsf M_4$; consequently the bicommutant of either image is itself.

*Proof.* A matrix commuting with all $\mathsf M_4(\tilde q)$ commutes with every left multiplication, hence belongs to the commutant of $L(\mathbb{H})$, which is $R(\mathbb{H}^{\mathrm{op}})$, of dimension $4$, by the double centraliser computation of *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, above this article in this category; the reverse inclusion is the commutativity above. The second statement is the mirror.

**Corollary.** The image of $\mathsf M_4$ is its own bicommutant, so it is a four-dimensional subalgebra of $M_4(\mathbb{R})$ of the division type; the enveloping algebra of the block is $M_4(\mathbb{R})$, generated by the two commuting copies.

*Proof.* The theorem and the identification of the enveloping algebra with $\operatorname{End}_\mathbb{R}(\mathbb{H})$; the two copies generate $M_4(\mathbb{R})$ because their product spans the $16$-dimensional operator algebra.

## Comparison with the Complex Case

The difference is the coefficient field and the module on which the matrices act: over $\mathbb{R}$ the standard module is the four-dimensional $\mathbb{H}$, while over $\mathbb{C}$ the left regular module of $M_2(\mathbb{C})$ is a sum of two copies of the column space.

## Summary

The left regular representation $\mathsf M_4$ with $\mathsf M_4(\tilde q)(\tilde r)=\tilde q\tilde r$ is an injective real-algebra homomorphism of $\mathbb{H}$ into $M_4(\mathbb{R})$ with four-dimensional image; on it the plain product is the matrix product, the plain form is $\mathrm B(\tilde p,\tilde q)=\tfrac14\operatorname{tr}(\mathsf M_4(\tilde p)\mathsf M_4(\tilde q))$ with the same Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ of signature $(1,3)$, and the invariants are $\operatorname{tr}\mathsf M_4(\tilde q)=4q_0$ and $\det\mathsf M_4(\tilde q)=N(\tilde q)^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_4(\tilde q)$ | Left regular matrix of $\tilde q$, $\tilde r\mapsto\tilde q\tilde r$ |
| $\mathsf R_4(\tilde q)$ | Right regular matrix, $\tilde r\mapsto\tilde r\tilde q$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | Gram matrix of the plain form |
| $\natural$ | Natural sign, the transpose of the regular matrix |
| $N(\tilde q)=\tilde q\tilde q^{\natural}$ | Quaternion norm, the square root of the determinant |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the regular representations, the trace pairing and the double centraliser theorem.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the left and right regular representations of a division ring and their commutants.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the bicommutant and the structure of matrix algebras over a division ring.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the regular matrices of the quaternion multiplication.
