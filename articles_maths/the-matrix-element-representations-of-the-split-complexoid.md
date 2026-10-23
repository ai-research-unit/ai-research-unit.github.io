# __The Matrix Element Representations of the Split-Complexoid__

## Introduction

This article reads the split-complex numbers in the **real matrix algebras**: the $2\times2$ model, in which an element becomes the matrix $\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$ of hyperbolic type, and the $4\times4$ model, the doubling of the first, together with the commutant of each and the equivalence of the two. The $2\times2$ model exhibits the algebra inside $M_2(\mathbb{R})$ as the two-dimensional subalgebra $\{qI+q'J\}$ with $J=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $J^2=I$; the $4\times4$ model writes the same element as a block-diagonal matrix with two copies of the $2\times2$ on the diagonal and adds nothing. The two models are the two-dimensional real shadow of the complex matrix representations, and their degeneracy — the $2\times2$ is already the regular representation, and the $4\times4$ only doubles it — is the matrix face of the commutativity of $\mathbb{D}$.

The **element reading** of the $2\times2$ matrix, its Cayley form, its multiplicativity, the determinant as the norm, the trace, the characteristic polynomial, the idempotent diagonalisation and the identification of the unit-norm elements with the hyperbolic rotations are *Split-Complex Regular Element Representation*, which owns them; this article states the model and cites that article rather than repeating it. The two algebraic norms are *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*; the invertibility criterion and the group of units are *Norm and Invertibility in the General Split-Complex Algebra*. The degeneracy of the models is *The Specificities of the Split-Complex Algebra*, and the general representation theory is *Split-Complex Element Representations*.

## The $2\times2$ Model

**Definition.** The **$2\times2$ matrix model** is the $\mathbb{R}$-linear map

$$
\mathsf{M}_2 : \mathbb{D} \longrightarrow M_2(\mathbb{R}), \qquad Q = q+jq' \longmapsto \mathsf{M}_2(Q) = \begin{pmatrix} q & q' \\ q' & q \end{pmatrix},
$$

fixed by its values on the basis, $\mathsf{M}_2(1)=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ and $\mathsf{M}_2(j)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.

**Theorem.** $\mathsf{M}_2$ is an injective algebra homomorphism; its image is the commutative subalgebra

$$
\boxed{\; M_2(\mathbb{D}) = \left\{ \begin{pmatrix} q & q' \\ q' & q \end{pmatrix} : q, q' \in \mathbb{R} \right\} = \{qI+q'J\} \cong \mathbb{R}[J]/(J^2-I) \;},
$$

of real dimension two, and $\mathbb{D}\cong M_2(\mathbb{D})$ as algebras.

**Proof.** The two basis images satisfy $I^2=I$ and $J^2=I$, so the assignment extends to an algebra homomorphism; the matrix of a general element is the displayed one, and the map is injective because $q$ and $q'$ are read off the first column. The image is $\{qI+q'J\}$, of real dimension two, isomorphic to $\mathbb{R}[J]/(J^2-I)\cong\mathbb{R}[x]/(x^2-1)\cong\mathbb{D}$.

The matrices of the image are the **real matrices of hyperbolic type**: symmetric, with equal diagonal entries $q$ and equal off-diagonal entries $q'$. Against the complex field the only difference is the sign of the square of the generator: $\mathbb{C}$ embeds as $\{aI+a'K\}$ with $K=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $K^2=-I$, and $\mathbb{D}$ as $\{qI+q'J\}$ with $J^2=+I$, the sign $j^2=+1$ against $i^2=-1$ appearing as the sign of the square of the generator matrix.

**The determinant and the trace.** For $Q=q+jq'$,

$$
\boxed{\; \det \mathsf{M}_2(Q) = q^2-q'^2 = \langle Q\rangle_{*}, \qquad \operatorname{Tr} \mathsf{M}_2(Q) = 2q = q_+ + q_- \;}.
$$

The determinant is the **second algebraic norm** $\langle Q\rangle_{*}=Q\bar Q$ of *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*, and the trace is twice the scalar part, the sum of the two eigenvalues. The **first algebraic norm** $\langle Q\rangle=Q^2$ appears not as a determinant or a trace but as the square of the matrix, $\mathsf{M}_2(Q)^2=\mathsf{M}_2(Q^2)$, which is the multiplicativity of $\mathsf{M}_2$ read on the square. The eigenvalues of $\mathsf{M}_2(Q)$ are the idempotent coordinates $q_+=q+q'$ and $q_-=q-q'$, both real, and the characteristic polynomial factors as $(\lambda-q_+)(\lambda-q_-)$.

**Invertibility.** The matrix $\mathsf{M}_2(Q)$ is invertible exactly when $\det\mathsf{M}_2(Q)=\langle Q\rangle_{*}\neq0$; the elements of $\mathbb{D}$ therefore correspond to the invertible matrices of hyperbolic type, and $\mathsf{M}_2(Q)^{-1}=\mathsf{M}_2(Q^{-1})=\frac{1}{\langle Q\rangle_{*}}\begin{pmatrix}q&-q'\\-q'&q\end{pmatrix}$. The criterion and the group of units are *Norm and Invertibility in the General Split-Complex Algebra*.

**The idempotent diagonalisation and the hyperbola.** In the idempotent basis the model is diagonal, $\mathsf{M}_2(Q)\big|_{\{\Pi_1,\Pi_2\}}=\operatorname{diag}(q_+,q_-)$, and the unit-norm elements $\langle Q\rangle_{*}=1$ are the matrices of determinant one in $M_2(\mathbb{D})$, the two branches of the hyperbola $q^2-q'^2=1$, the identity component of which is the group of **hyperbolic rotations** $R_j(t)=\begin{pmatrix}\cosh t&\sinh t\\\sinh t&\cosh t\end{pmatrix}$. The diagonalisation, the eigenvalue reading and the identification of the unit-norm group are *Split-Complex Regular Element Representation*, and the matrix group is read as the group of linear maps preserving the form in *The Versors and the Orthogonal Group of the Split-Complex Numbers*.

## The $4\times4$ Model

**Definition.** The **$4\times4$ matrix model** is the left regular representation of $\mathbb{D}$ on the doubled coefficient space $\mathbb{D}\oplus\mathbb{D}$, written in the basis $(1,j,1,j)$:

$$
\mathsf{M}_4 : \mathbb{D} \longrightarrow M_4(\mathbb{R}), \qquad
\mathsf{M}_4(Q) = \begin{pmatrix} \mathsf{M}_2(Q) & 0 \\ 0 & \mathsf{M}_2(Q) \end{pmatrix}
= \begin{pmatrix} q & q' & 0 & 0 \\ q' & q & 0 & 0 \\ 0 & 0 & q & q' \\ 0 & 0 & q' & q \end{pmatrix}.
$$

It is the block-diagonal sum of two copies of the $2\times2$ model.

**Theorem.** $\mathsf{M}_4$ is an injective algebra homomorphism, and

$$
\det \mathsf{M}_4(Q) = \langle Q\rangle_{*}^2, \qquad \operatorname{Tr} \mathsf{M}_4(Q) = 4q = 2\operatorname{Tr}\mathsf{M}_2(Q).
$$

**Proof.** $\mathsf{M}_4$ is built from $\mathsf{M}_2$ blockwise, so multiplicativity and injectivity follow from the $2\times2$ case. The determinant of a block-diagonal matrix is the product of the determinants of its blocks, whence $\det\mathsf{M}_4(Q)=\det\mathsf{M}_2(Q)^2=\langle Q\rangle_{*}^2$, and the trace is the sum of the traces of the blocks, $\operatorname{Tr}\mathsf{M}_4(Q)=2\operatorname{Tr}\mathsf{M}_2(Q)=4q$.

The model is the regular representation of $\mathbb{D}$ on the free module of rank two: it is the direct sum of two copies of the regular module, and its image is the subalgebra

$$
M_4(\mathbb{D})_L = \left\{ \operatorname{diag}(X, X) : X \in M_2(\mathbb{D}) \right\}
$$

of real dimension two inside the sixteen of $M_4(\mathbb{R})$. Every entry is a single coefficient of $Q$ up to sign, in each block exactly as in the $2\times2$ model, and the two blocks carry the same element.

## The Commutants

The two models are told apart by their **commutants**, the matrices that commute with the whole image.

**The $2\times2$ commutant.** The commutant of $M_2(\mathbb{D})=\{qI+q'J\}$ in $M_2(\mathbb{R})$ is $M_2(\mathbb{D})$ itself: a matrix $\begin{pmatrix}p&u\\r&s\end{pmatrix}$ commuting with $J=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ satisfies $u=r$ and $p=s$, hence is $pI+uJ\in M_2(\mathbb{D})$, and every element of $M_2(\mathbb{D})$ commutes with the whole (commutative) image. So the $2\times2$ image is its own commutant and its own bicommutant, a maximal commutative subalgebra of $M_2(\mathbb{R})$ of dimension two. This is *Split-Complex Regular Element Representation*.

**The $4\times4$ commutant.** A matrix $C=\begin{pmatrix}P_{11}&P_{12}\\P_{21}&P_{22}\end{pmatrix}$, written in $2\times2$ blocks, commutes with every $\operatorname{diag}(X,X)$, $X\in M_2(\mathbb{D})$, exactly when $P_{11}X=XP_{11}$, $P_{12}X=XP_{12}$, $P_{21}X=XP_{21}$ and $P_{22}X=XP_{22}$ for all such $X$, that is exactly when each of the four blocks lies in the commutant of $M_2(\mathbb{D})$, namely in $M_2(\mathbb{D})$. Hence

$$
\boxed{\; \{C \in M_4(\mathbb{R}) : C\,\mathsf{M}_4(Q)=\mathsf{M}_4(Q)\,C \text{ for all } Q\} = \left\{ \begin{pmatrix} P_{11} & P_{12} \\ P_{21} & P_{22} \end{pmatrix} : P_{11},P_{12},P_{21},P_{22} \in M_2(\mathbb{D}) \right\} \cong M_2(M_2(\mathbb{D})) \cong M_2(\mathbb{D}) \;},
$$

of real dimension **eight**, four times the dimension two of the image. The commutant of the $4\times4$ image is therefore strictly larger than the image, unlike the $2\times2$ case, and it is the ring of $2\times2$ matrices over the commutative ring $\mathbb{D}$: the doubling of the module and the doubling of the commutant are the same fact.

| model | image | commutant | dimension of the commutant |
|---|---|---|---|
| $2\times2$ | $M_2(\mathbb{D})=\{qI+q'J\}$ | $M_2(\mathbb{D})$ itself | $2$ |
| $4\times4$ | $\{\operatorname{diag}(X,X)\}$ | $M_2(\mathbb{D})$-valued blocks $\cong M_2(\mathbb{D})$ | $8$ |

## The Two Models Compared

The $4\times4$ model is the doubling of the $2\times2$ model and carries no information the $2\times2$ does not: it is the direct sum of two copies of it, its image is the diagonal of two copies of the $2\times2$ image, and every invariant doubles in the predictable way,

$$
\det\mathsf{M}_4(Q) = \bigl(\det\mathsf{M}_2(Q)\bigr)^2, \qquad \operatorname{Tr}\mathsf{M}_4(Q) = 2\operatorname{Tr}\mathsf{M}_2(Q) .
$$

So the two models are **equivalent** as representations of $\mathbb{D}$: each is a direct sum of copies of the regular module, the $2\times2$ being one copy and the $4\times4$ two, and the $4\times4$ extends the $2\times2$ by exactly the two nothing-adding dimensions of the second copy. The essential model is the $2\times2$; the $4\times4$ is recorded only to show that it adds nothing.

**Remark.** The relation between the two models here is a doubling and not a second structure: because $\mathbb{D}$ is commutative, its regular representation is two-dimensional and its $2\times2$ matrix is symmetric, so the "left" and "right" regular representations coincide and there is no second copy to compare with. In the four-dimensional algebra the regular representation is four-dimensional, the $4\times4$ matrix is block diagonal with two blocks each conjugate to the $2\times2$ one, and the two blocks are the two minimal ideals; here the two blocks are two copies of the whole algebra, since the minimal ideals are one-dimensional. The degeneracy is the one recorded in *The Specificities of the Split-Complex Algebra*.

## Summary

The split-complex algebra is realised in the real matrix algebras by two models. The $2\times2$ model sends $Q=q+jq'$ to the hyperbolic matrix $\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$, an injective homomorphism onto the commutative subalgebra $M_2(\mathbb{D})=\{qI+q'J\}$ with $J^2=I$; the determinant is the second algebraic norm $\langle Q\rangle_{*}=q^2-q'^2$, the trace is $2q$, the square of the matrix is the first algebraic norm $Q^2$, the eigenvalues are the idempotent coordinates, and the unit-norm elements are the hyperbolic rotations. The model is the regular representation of $\mathbb{D}$ on itself, and its commutant in $M_2(\mathbb{R})$ is the image itself.

The $4\times4$ model writes the same element block-diagonally with two copies of the $2\times2$ matrix on the diagonal; it is the regular representation on $\mathbb{D}\oplus\mathbb{D}$, its determinant is $\langle Q\rangle_{*}^2$, its trace is $4q$, and its commutant in $M_4(\mathbb{R})$ is the ring $M_2(\mathbb{D})$ of $2\times2$ matrices over $\mathbb{D}$, of real dimension eight. The two models are equivalent, the $4\times4$ being the doubling of the $2\times2$ and adding two dimensions in which no new structure appears; the essential model is the $2\times2$, and the doubling is the matrix expression of the commutativity of $\mathbb{D}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$ | the $2\times2$ matrix of $Q=q+jq'$ |
| $\mathsf{M}_4(Q)=\operatorname{diag}(\mathsf{M}_2(Q),\mathsf{M}_2(Q))$ | the $4\times4$ matrix of $Q$ |
| $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, $J=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | the generators of the image, $J^2=I$ |
| $M_2(\mathbb{D})=\{qI+q'J\}$ | the image of the $2\times2$ model, $\cong\mathbb{D}$ |
| $\det\mathsf{M}_2(Q)=q^2-q'^2=\langle Q\rangle_{*}$ | the second algebraic norm, the determinant |
| $\operatorname{Tr}\mathsf{M}_2(Q)=2q$ | the trace, the sum of the eigenvalues |
| $\mathsf{M}_2(Q)^2=\mathsf{M}_2(Q^2)$ | the first algebraic norm $Q^2$ as the square of the matrix |
| $\det\mathsf{M}_4(Q)=\langle Q\rangle_{*}^2$ | the determinant of the $4\times4$ model |
| $\operatorname{Tr}\mathsf{M}_4(Q)=4q=2\operatorname{Tr}\mathsf{M}_2(Q)$ | the trace of the $4\times4$ model |
| $\operatorname{diag}(X,X)$, $X\in M_2(\mathbb{D})$ | the image of the $4\times4$ model |
| $\cong M_2(\mathbb{D})$ | the commutant of the $4\times4$ image, real dimension $8$ |
| $R_j(t)=\begin{pmatrix}\cosh t&\sinh t\\\sinh t&\cosh t\end{pmatrix}$ | the hyperbolic rotation, $\mathsf{M}_2(\exp(jt))$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the regular representation and the double centralizer theorem.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for matrix rings over a commutative ring and their commutants.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex numbers as hyperbolic $2\times2$ matrices.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the regular representations of low-dimensional algebras.
- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for the matrix groups of determinant one and the hyperbolic rotations.
