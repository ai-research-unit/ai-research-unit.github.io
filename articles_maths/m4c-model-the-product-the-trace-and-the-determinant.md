# __$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant__

## Introduction

The left regular matrix is the biquaternion read as a linear operator on its own four-dimensional complex space. The assignment is fixed on the basis by the multiplication table, and it is an injective algebra homomorphism whose image is a four-dimensional subalgebra of $M_4(\mathbb{C})$.

The image is not the whole of $M_4(\mathbb{C})$: the algebra has complex dimension four and the matrix algebra has sixteen. What the regular model loses in surjectivity it gains in structure: the image is the algebra acting on itself, and after a fixed change of basis it is two identical copies of the $2\times2$ model.

This article owns the assignment, the isomorphism, the signs and the Pauli matrices, the algebra in matrix form, the structure map and the real form, and the sense in which the model is a choice. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The central scalar is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$, the scalar of $\tilde Q\tilde Q^{\natural}$. The $2\times2$ model is $\mathsf{M}_2$, fixed by
$$
\mathsf{M}_2(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$

**Boundaries.** The right regular matrix is *$M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser*, §*The Right Regular Image*; the Peirce coordinates are *$M_4(\mathbb{C})_L$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*; the trace and the determinant are *$M_4(\mathbb{C})_L$ Representation : Trace, Determinant and the Biquaternion Norm*. The abstract algebra is *The Biquaternion Algebra*; the $2\times2$ model is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*.

## The Assignment on the Basis

**The four units go to four matrices, and the four coefficients go to one matrix.** The **left regular matrix** $\mathsf{M}_4^{L}(\tilde Q)$ is the $4\times4$ matrix whose $\mu$-th column is the coordinate column of the product $\tilde Q e_\mu$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$. The shorter notation $\mathsf{M}_4$ stands for $\mathsf{M}_4^{L}$. The four units go to

| Unit | Matrix | Square | Determinant |
|---|---|---|---|
| $e_t$ | $\mathrm I_4$ | $\mathrm I_4$ | $1$ |
| $\vec e_x$ | $\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |
| $\vec e_y$ | $\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |
| $\vec e_z$ | $\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |

and a general element is

$$
\boxed{\;\mathsf{M}_4(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}\;}
$$

Every entry is one coefficient of $\tilde Q$, with a sign and no sum. The four entries of each row and each column carry the four coefficients once.

**The inverse map.** Reading the coefficients back off the matrix,

$$
\mathsf{M}_4^{-1}:\begin{pmatrix}
a_{00}&a_{01}&a_{02}&a_{03}\\
a_{10}&a_{11}&a_{12}&a_{13}\\
a_{20}&a_{21}&a_{22}&a_{23}\\
a_{30}&a_{31}&a_{32}&a_{33}
\end{pmatrix}\longmapsto
Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
$$

with
$$
Q_t=\tfrac14\operatorname{Tr}\mathsf{M}_4(\tilde Q),\qquad
Q_x=a_{10},\qquad
Q_y=a_{20},\qquad
Q_z=a_{30}.
$$

The trace formula is the only one that averages; the three vector coefficients are single entries, because the first column is the coordinate column of the element.

**Example.** For $\tilde Q=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$,

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}
2+i&-1+i&-3&-i\\
1-i&2+i&-i&3\\
3&i&2+i&-1+i\\
i&-3&1-i&2+i
\end{pmatrix}.
$$

Its trace is $8+4i=4(2+i)$, and its determinant is $(11+2i)^2=117+44i$, because $11+2i=\langle\tilde Q\rangle_{\natural}$.

## The Isomorphism

**Theorem (the left regular matrix is multiplicative and injective).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)=\mathsf{M}_4(\tilde P\tilde Q),
\qquad
\mathsf{M}_4(\tilde Q)=0\iff\tilde Q=0.
$$

Hence $\mathsf{M}_4$ is an injective algebra homomorphism, and its image is a $4$-dimensional complex subalgebra of $M_4(\mathbb{C})$, isomorphic to $\mathbb{B}$ and therefore to $M_2(\mathbb{C})$.

*Proof.* On the basis, associativity gives $\tilde P(\tilde Q e_\mu)=(\tilde P\tilde Q)e_\mu$ for every $\mu$, so the two matrices agree on the four columns of the identity. The first column of $\mathsf{M}_4(\tilde Q)$ is the coordinate column of $\tilde Q$, so vanishing of the matrix forces all four coefficients to vanish. $\square$

**The image.** Write $M_4(\mathbb{C})_L=\mathsf{M}_4(\mathbb{B})$. It is a complex subspace of dimension $4$ inside the $16$ of $M_4(\mathbb{C})$, closed under multiplication and containing the identity. The inverse of an invertible element is $\mathsf{M}_4(\tilde Q)^{-1}=\mathsf{M}_4(\tilde Q^{-1})$, with $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$.

**The image is not everything.** Every two-by-two complex matrix is the image of exactly one biquaternion, but not every four-by-four matrix is. The image has dimension four, the ambient algebra has dimension sixteen, and the twelve missing dimensions are the multiplicity of the two copies. The regular model is therefore an isomorphism onto a subalgebra, not onto the matrix algebra, and the difference is the subject of the rest of the series.

**The left action.** The coefficient space $\mathbb{C}^4$ carries the left action $\tilde Q\cdot x=\mathsf{M}_4(\tilde Q)x$. The space is the algebra $\mathbb{B}$ itself, with left multiplication as the action.

## The Signs and the Pauli Matrices

**The factor $i$ is forced.** The images of the vector units are real matrices squaring to $-\mathrm I_4$, and the image of $i\vec e_k$ is their multiple by $i$. The Hermitian matrices obtained this way are the Pauli matrices repeated in the two copies:

$$
\Sigma_k=\mathsf{M}_4(i\vec e_k)=i\mathsf{M}_4(\vec e_k),\qquad
\mathsf{M}_4(\vec e_k)=-i\Sigma_k,
$$

and in the block basis of §*The Algebra in Matrix Form*
$$
\Sigma_1=\operatorname{diag}(\sigma_1,\sigma_1),\qquad
\Sigma_2=\operatorname{diag}(\sigma_2,\sigma_2),\qquad
\Sigma_3=\operatorname{diag}(\sigma_3,\sigma_3).
$$

In the fixed coefficient basis the same matrices are $S\Sigma_kS^{-1}$, the conjugate block form. Each $\Sigma_k$ is Hermitian and squares to $\mathrm I_4$, so $\mathsf{M}_4(\vec e_k)$ squares to $-\mathrm I_4$. The three anticommute, and their products reproduce the quaternion relations with the correct signs. The factor $i$ is not optional: a real matrix squaring to $-\mathrm I_4$ carries no real line to itself, and the complex structure it defines is the multiplication by $i$ that the representation carries.

**The signs are forced by the cross-relations.** With the assignment above,

$$
\mathsf{M}_4(\vec e_x)\mathsf{M}_4(\vec e_y)=\mathsf{M}_4(\vec e_z),
$$

not its negative, because $\vec e_x\vec e_y=\vec e_z$ and $\mathsf{M}_4$ is multiplicative. The alternative assignment $\vec e_k\mapsto-\mathsf{M}_4(\vec e_k)$ preserves the squares and reverses every cross-product; it is the composition of $\mathsf{M}_4$ with the anti-automorphism that negates the vector part, so it is an anti-isomorphism, not an algebra isomorphism on the same basis. The sign pattern is determined once the images of the three units are fixed, and the three are determined up to conjugation.

**The Pauli algebra.** The matrices satisfy
$$
\Sigma_i\Sigma_j=\delta_{ij}\mathrm I_4+i\epsilon_{ijk}\Sigma_k,
$$
the Pauli algebra read twice. The commutator is anti-Hermitian and lies in the image of the anti-Hermitian subspace; the anticommutator is Hermitian and lies in the image of the Hermitian subspace. The two readings differ by the factor $i$, exactly as in the $2\times2$ model.

## The Algebra in Matrix Form

**The block change.** The block reduction uses the four elements
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
with the fixed axis $\vec e_z$. They satisfy
$$
\tilde\Pi_+^2=\tilde\Pi_+,\quad \tilde\Pi_-^2=\tilde\Pi_-,\quad \tilde\Pi_+\tilde\Pi_-=0,\quad
\vec\Upsilon_\pm^2=0,\quad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\quad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
$$
and the change matrix with these four elements as columns is
$$
S=\begin{pmatrix}
\tfrac12&0&0&\tfrac12\\
0&\tfrac{i}{2}&\tfrac{i}{2}&0\\
0&\tfrac12&-\tfrac12&0\\
\tfrac{i}{2}&0&0&-\tfrac{i}{2}
\end{pmatrix},
\qquad
S^{-1}=\begin{pmatrix}
1&0&0&-i\\
0&-i&1&0\\
0&-i&-1&0\\
1&0&0&i
\end{pmatrix},
\qquad
\det S=-\tfrac14.
$$

**Theorem (the block reduction).** For every $\tilde Q\in\mathbb{B}$,
$$
\boxed{\;S^{-1}\mathsf{M}_4(\tilde Q)S=
\begin{pmatrix}
\mathsf{M}_2(\tilde Q)&0\\
0&\mathsf{M}_2(\tilde Q)
\end{pmatrix}=\mathrm I_2\otimes\mathsf{M}_2(\tilde Q)\;}
$$

*Proof.* The columns of $S$ are $\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$, in that order. Left multiplication by $\tilde Q$ acts on the first two as the matrix $\mathsf{M}_2(\tilde Q)$ in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$ and on the last two as the same matrix in the basis $(\vec\Upsilon_-,\tilde\Pi_-)$. The multiplication table of the four elements gives the four entries in each block, and the two blocks coincide.

**The product is the matrix product.** For two elements $\tilde Q_1,\tilde Q_2$,
$$
\mathsf{M}_4(\tilde Q_1\tilde Q_2)=\mathsf{M}_4(\tilde Q_1)\mathsf{M}_4(\tilde Q_2),\qquad
\mathsf{M}_4(\tilde Q^n)=\mathsf{M}_4(\tilde Q)^n,\qquad
\mathsf{M}_4(\tilde Q^{-1})=\mathsf{M}_4(\tilde Q)^{-1}.
$$
The third identity holds when either side exists, that is when $\langle\tilde Q\rangle_{\natural}\neq0$.

**The invariants.** The block form turns every invariant of $\mathsf{M}_4(\tilde Q)$ into an invariant of $\mathsf{M}_2(\tilde Q)$ read twice.

| Invariant | $M_2(\mathbb{C})$ | $M_4(\mathbb{C})_L$ |
|---|---|---|
| trace | $2Q_t$ | $4Q_t$ |
| determinant | $\langle\tilde Q\rangle_{\natural}$ | $\langle\tilde Q\rangle_{\natural}^2$ |
| rank | $0,1,2$ | $0,2,4$ |

**The centre.** A matrix commuting with every element of the image is a scalar matrix. The centre of the image is the line $\mathbb{C}\mathrm I_4$, the image of the line $\mathbb{C}e_t$. It is the same line as the centre of $M_4(\mathbb{C})$, and the image is its own centraliser only when the element is scalar.

**The rank.** The rank of $\mathsf{M}_4(\tilde Q)$ is twice the rank of $\mathsf{M}_2(\tilde Q)$, because the two blocks are equal. It takes the values $0,2,4$ and never $1$ or $3$. The null cone is the set of singular regular matrices, and the rank stratification is the even refinement of the $2\times2$ one.

## The Structure Map, the Presentation and the Real Form

**The structure map.** The scalars act through
$$
\varphi:\mathbb{C}\longrightarrow Z\bigl(M_4(\mathbb{C})_L\bigr),\qquad
\varphi(A)=A\mathrm I_4,
$$
whose image is the line of scalar matrices. The scalar action is $M\mapsto AM$, and it is compatible with the product because $A\mathrm I_4$ is central. In the algebra the same map is $\varphi(A)=Ae_t$; the matrix form shows that its image is exactly the centre of the image.

**The presentation.** The images $X=\mathsf{M}_4(\vec e_x)$ and $Y=\mathsf{M}_4(\vec e_y)$ generate $M_4(\mathbb{C})_L$ as a $\mathbb{C}$-algebra with unit, because $\vec e_x$ and $\vec e_y$ generate $\mathbb{B}$ and $\mathsf{M}_4$ is injective. They satisfy
$$
X^2=Y^2=-\mathrm I_4,\qquad XY+YX=0,
$$
and these are the defining relations. The algebra with two generators and those relations is the quaternion algebra over $\mathbb{C}$, of dimension four; the map from it to the image is nonzero, hence injective because the quaternion algebra is simple, and it is onto for dimension reasons. The matrix reading is that two anticommuting complex structures generate the image, and the fourth basis element is their product.

**The real form.** Read over $\mathbb{R}$, the image has real dimension eight, and
$$
J:M_4(\mathbb{C})_L\longrightarrow M_4(\mathbb{C})_L,\qquad J(M)=iM,
$$
is a central complex structure, $J^2=-\mathrm{id}$, commuting with both one-sided multiplications. It is the image of multiplication by the central imaginary $i$ of $\mathbb{B}$, and the complex basis $(\mathrm I_4,-i\Sigma_1,-i\Sigma_2,-i\Sigma_3)$ is the image of the complex basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$; together with $i$ times it, it gives a real basis of the eight real dimensions. The realified matrix in the basis $(e_\mu,ie_\mu)$ is the block matrix
$$
\begin{pmatrix}\operatorname{Re}X&-\operatorname{Im}X\\ \operatorname{Im}X&\operatorname{Re}X\end{pmatrix},
$$
with the real and imaginary parts of $X$ in the four blocks.

**Simple and without division.** The image is isomorphic to $M_2(\mathbb{C})$, hence simple, and it is not a division algebra, since $E_{11}E_{22}=0$ with both factors nonzero in the $2\times2$ model. The regular model inherits both properties from the algebra, and the ambient $M_4(\mathbb{C})$ adds no new two-sided ideal to the image.

## The Choice of Model

**Any two models differ by a change of basis.** A model of the regular representation is a basis of $\mathbb{C}^4$. Let $C\in GL_4(\mathbb{C})$ have as columns the new basis vectors written in the old basis. The matrix of the same element in the new basis is
$$
\mathsf{M}_4^{C}(\tilde Q)=C^{-1}\mathsf{M}_4(\tilde Q)C,
\qquad
\mathsf{M}_4(\tilde Q)=C\,\mathsf{M}_4^{C}(\tilde Q)\,C^{-1}.
$$
Two changes compose,
$$
(C_1C_2)^{-1}M(C_1C_2)=C_2^{-1}\bigl(C_1^{-1}MC_1\bigr)C_2,
$$
so the models form a single orbit of $GL_4(\mathbb{C})$ acting by conjugation. The fixed coefficient basis is one representative; the block basis is the representative $C=S$ in which the matrix is block diagonal.

**What the choice fixes.** The choice fixes the four columns, the diagonal axis, the two column pairs and the explicit entries of every element. None of these is invariant under conjugation, and none of them is needed to state the algebra. The invariants — the trace and the determinant — are unchanged by the choice, and they are the subject of the articles that follow.

**The conjugations that change nothing.** A matrix $P$ that commutes with the image leaves every regular matrix unchanged, because $P^{-1}\mathsf{M}_4(\tilde Q)P=\mathsf{M}_4(\tilde Q)$. The commutant is the right regular image of *$M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser*, §*The Right Regular Image*, of dimension four. The conjugations by $GL_4(\mathbb{C})$ that do change the matrices are the changes of basis that move the image inside $M_4(\mathbb{C})$; they give equivalent models, not different algebras.

**The matrix model is a change of coordinates.** It adds no relation and loses no information. Its value is that the coordinate statements are matrix statements: the scalar part is a quarter of the trace, the central scalar is the square root of the determinant, invertibility is a nonzero determinant, the zero divisors are the singular matrices, and the two standard columns are the two pairs of columns of the model. These are collected in *$M_4(\mathbb{C})_L$ Representation : Trace, Determinant and the Biquaternion Norm* and in *$M_4(\mathbb{C})_L$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*.

## Summary

The assignment $\mathsf{M}_4$ sends $e_t$ to $\mathrm I_4$ and the three vector units to the signed permutation matrices of the multiplication table, and extends by linearity. It is an injective homomorphism of complex algebras, and its image is a four-dimensional subalgebra of $M_4(\mathbb{C})$, isomorphic to $M_2(\mathbb{C})$ but not equal to the whole matrix algebra. The unit is $\mathrm I_4$, the centre is the scalar matrices, and the inverse is the image of the quaternionic conjugate divided by the determinant. The factor $i$ and the signs of the cross-relations are forced by the quaternion relations. The Peirce change $S$ reduces the matrix to two identical $2\times2$ blocks. The model is unique up to conjugation by $GL_4(\mathbb{C})$, and the fixed choice is the one in which the Peirce basis makes the reduction visible.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis; $e_t$ the unit, $\vec e_k^2=-e_t$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element and its scalar–vector split |
| $\mathsf{M}_4=\mathsf{M}_4^{L}$ | the left regular matrix |
| $M_4(\mathbb{C})_L$ | its image in $M_4(\mathbb{C})$ |
| $\Sigma_k=\mathsf{M}_4(i\vec e_k)=-i\mathsf{M}_4(\vec e_k)$ | the Pauli matrices, repeated in the two copies |
| $S$ | the fixed block change, $\det S=-\tfrac14$ |
| $\tilde\Pi_\pm,\vec\Upsilon_\pm$ | the four block-basis elements of the fixed axis |
| $Q_t=\tfrac14\operatorname{Tr}\mathsf{M}_4(\tilde Q)$ | the scalar part as a quarter of the trace |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the central scalar, the square root of the determinant |

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and its two products
- [$M_4(\mathbb{C})_L$ Representation : Trace, Determinant and the Biquaternion Norm](m4c-representation-trace-determinant-and-the-biquaternion-norm.html), for the two invariants
- [$M_4(\mathbb{C})_L$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the coordinate model and the two blocks
- [$M_4(\mathbb{C})_L$ Representation : Worked Examples](m4c-representation-worked-examples.html), for the matrices computed in the model
- [$M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser](m4c-model-the-centraliser-and-the-double-centraliser.html), §*The Right Regular Image*, for the commutant
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the $2\times2$ model
- [Matrix Algebras](matrix-algebras.html), for the structure of $M_n(\mathbb{C})$
