# __$M_4(\mathbb{C})_L$ Model : The Centraliser and the Double Centraliser__

## Introduction

The centraliser of a regular matrix is larger than the centraliser of the corresponding $2\times2$ matrix, because the regular representation contains two copies of the defining module. The extra freedom is the mixing of the two copies. The relative centraliser inside the image is smaller, and the double centraliser of the whole image is the right regular image.

This article computes the three objects, their dimensions in each spectral type, and the eigenbasis ambiguity they describe. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant*. Write $M=\mathsf{M}_4(\tilde Q)$, $A=\mathsf{M}_2(\tilde Q)$, and use the Peirce basis in which $M=\mathrm I_2\otimes A$. The centraliser of $M$ in $M_4(\mathbb{C})$ is written $C(M)$; the relative centraliser in the image is $C_{L}(M)$; the image and the right image are $M_4(\mathbb{C})_L$ and $M_4(\mathbb{C})_R$.

**Boundaries.** The right image and the double centraliser of the whole image are treated in §*The Right Regular Image* below; the eigenbasis is *$M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix*; the $2\times2$ commutant is *$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser*.

## The Commutant

**Theorem.** In the Peirce basis,
$$
C(M)=\{B\in M_4(\mathbb{C}):B(\mathrm I_2\otimes A)=(\mathrm I_2\otimes A)B\}
=M_2(\mathbb{C})\otimes C(A),
$$
where $C(A)=\{X\in M_2(\mathbb{C}):XA=AX\}$. Consequently,

| Type of $\tilde Q$ | $C(A)$ | $\dim_{\mathbb{C}}C(M)$ |
|---|---|---|
| scalar | $M_2(\mathbb{C})$ | $16$ |
| non-scalar | $\mathbb{C}[A]$, of dimension $2$ | $8$ |

*Proof.* Write $B$ as a $2\times2$ block matrix with blocks $B_{ij}\in M_2(\mathbb{C})$. The condition $BM=MB$ is $B_{ij}A=AB_{ij}$ for every pair $(i,j)$, so each block lies in $C(A)$. The block matrix is therefore an element of $M_2(\mathbb{C})\otimes C(A)$, and the dimension is $4\dim C(A)$. For a scalar $A=\lambda\mathrm I_2$, $C(A)=M_2(\mathbb{C})$; otherwise $C(A)=\mathbb{C}[A]$, of dimension two. $\square$

**The meaning.** The tensor factor $M_2(\mathbb{C})$ acts on the multiplicity space of the two copies, and the factor $C(A)$ acts on the values. A matrix in $C(M)$ can mix the two copies arbitrarily and can act on each by a polynomial in $A$. The mixing is the new phenomenon of the regular model; in the $2\times2$ model there is no multiplicity space, and the commutant is only $C(A)$, of dimension $2$.

**Explicit form.** When $A$ has distinct eigenvalues, $C(A)$ is the algebra of diagonal matrices in the eigenbasis. In the eigenbasis of $A$, write $B$ in $2\times2$ blocks; each block is diagonal, so
$$
B=\begin{pmatrix}
\alpha_1&0&\beta_1&0\\
0&\alpha_2&0&\beta_2\\
\gamma_1&0&\delta_1&0\\
0&\gamma_2&0&\delta_2
\end{pmatrix}
$$
in the order (first copy, second copy), with eight free complex parameters. When $A$ is a Jordan block, each block is a polynomial in $A$, still with eight parameters.

**Definition.** The **relative centraliser** is the part of the commutant that lies in the image:
$$
C_L(M)=\{X\in M_4(\mathbb{C})_L:XM=MX\}.
$$

**Theorem.**
$$
C_L(M)=L(C(\tilde Q))=\{\mathsf{M}_4(\tilde R):\tilde R\tilde Q=\tilde Q\tilde R\},
\qquad
\dim_{\mathbb{C}}C_L(M)=
\begin{cases}4,&\tilde Q\text{ scalar},\\2,&\tilde Q\text{ non-scalar}.\end{cases}
$$

*Proof.* An element of the image is $\mathsf{M}_4(\tilde R)$, and it commutes with $\mathsf{M}_4(\tilde Q)$ exactly when $\tilde R$ commutes with $\tilde Q$, by injectivity. The centraliser of a non-scalar element of $M_2(\mathbb{C})$ is the algebra it generates, of dimension two; the centraliser of a scalar is the whole algebra, of dimension four. $\square$

**The gap.** For a non-scalar element the full commutant has dimension eight and the relative commutant has dimension two. The six extra dimensions are the mixing of the two copies: they are visible in $M_4(\mathbb{C})$ but not in the image. For a scalar element the full commutant is all of $M_4(\mathbb{C})$, dimension sixteen, while the relative commutant is the four-dimensional image.

**The minimal polynomial.** The same computation reads
$$
\mathbb{C}[M]\cong\mathbb{C}[t]\big/\bigl(m_M(t)\bigr),
$$
where $m_M$ is the minimal polynomial. The three spectral types are the three factorisations of $m_M$.

| Type of $M$ | $m_M(t)$ | $\mathbb{C}[M]$ | Dimension over $\mathbb{C}$ |
|---|---|---|---|
| scalar | $t-\lambda$ | $\mathbb{C}$ | $1$ |
| non-scalar, distinct eigenvalues | $(t-\lambda_+)(t-\lambda_-)$ | $\mathbb{C}\times\mathbb{C}$ | $2$ |
| non-scalar, repeated eigenvalue | $(t-\lambda)^2$ | $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ | $2$ |

The third row is the algebra of dual numbers: the nilpotent $\varepsilon$ squares to zero. The minimal polynomial does not grow in the regular model, because the two blocks are equal.

## The Three Types in the Eigenbasis

**Distinct eigenvalues.** Let $A=\mathsf{M}_2(\tilde Q)=C\operatorname{diag}(\lambda_+,\lambda_-)C^{-1}$ with $\lambda_+\neq\lambda_-$. In the eigenbasis, $M=\mathrm I_2\otimes A$ and
$$
C(M)=\left\{\begin{pmatrix}a_1\mathrm I_2&b_1\mathrm I_2\\c_1\mathrm I_2&d_1\mathrm I_2\end{pmatrix}:\ a_i,b_i,c_i,d_i\in\mathbb{C}\right\}\cong M_2(\mathbb{C})\otimes\mathbb{C}^2,
$$
of dimension eight. The factor $M_2(\mathbb{C})$ mixes the two copies, and the factor $\mathbb{C}^2$ is the value on the two eigenvalues. The spectral projectors of $M$ are $\rho_\pm=\mathrm I_2\otimes\Pi_\pm$, each of rank two.

**Repeated eigenvalue.** Let $A=\lambda\mathrm I_2+N$ with $N\neq0$ and $N^2=0$. The commutant of $A$ is the dual numbers $\mathbb{C}[N]$, and
$$
C(M)=M_2(\mathbb{C})\otimes\mathbb{C}[N]=\{a\mathrm I_4+b(\mathrm I_2\otimes N)\},
$$
again of dimension eight, with $\mathrm I_2\otimes N$ the nilpotent direction. The mixing of the two copies survives, but there is no eigenbasis; the projectors are oblique.

**Scalar.** For $A=\lambda\mathrm I_2$ every matrix commutes with $M$, $C(M)=M_4(\mathbb{C})$, and $\mathbb{C}[M]=\mathbb{C}\mathrm I_4$.

**The dimensions in the three types.** The relative centraliser is the image of $C(\tilde Q)$ and has dimension four for a scalar and two otherwise; the full centraliser has dimension sixteen for a scalar and eight otherwise. The gap is the multiplicity factor $M_2(\mathbb{C})$, of dimension four, which is present in $M_4(\mathbb{C})$ and absent from the image.

## The Adjugate and the Dagger in the Commutant

**The transpose.** If $B$ commutes with $M$, then $B^{\mathsf T}$ commutes with $M^{\mathsf T}$, not with $M$. Hence
$$
C(M)^{\mathsf T}=C(M^{\mathsf T})=C(\mathsf{M}_4(\tilde Q^{\natural})),
$$
which is the centraliser of the quaternion conjugate. The two centralisers coincide only when $\tilde Q^{\natural}$ is a polynomial in $\tilde Q$, that is, when $\tilde Q$ is scalar or lies in a two-dimensional subalgebra closed under conjugation.

**The dagger.** The same argument gives
$$
C(M)^{\dagger}=C(M^{\dagger})=C(\mathsf{M}_4(\tilde Q^{*})),
$$
and the commutant is stable under the dagger exactly when $M$ is normal, because then $M^{*}$ is a polynomial in $M$. For a normal element the spectral projectors lie in the commutant; for a non-normal element they do not.

**The adjugate.** The adjugate is $N M^{\mathsf T}$, so it lies in $C(M)$ exactly when $M^{\mathsf T}$ does. For a quaternion element, $M^{\mathsf T}$ is proportional to $M^{-1}$ and therefore commutes with $M$; the adjugate then lies in the commutant, as it does in the $2\times2$ model.

## The Eigenbasis and Its Ambiguity

**The diagonalising matrices.** A matrix $C$ diagonalises $M$ when $C^{-1}MC$ is diagonal. Two diagonalising matrices differ by an element of the commutant of the diagonal form:
$$
C'=CG,\qquad G\in C(\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)).
$$

**The ambiguity.** When $\lambda_+\neq\lambda_-$, the diagonal form has two eigenvalues, each of multiplicity two, and its commutant is
$$
GL_2(\mathbb{C})\times GL_2(\mathbb{C}),
$$
of complex dimension eight. The two factors are the changes of basis inside the two eigenspaces. In the $2\times2$ model the same eigenvalues have multiplicity one, and the ambiguity is only $GL_1\times GL_1$, of dimension two. The extra six parameters are the mixing of the two copies.

**The degenerate case.** When $\lambda_+=\lambda_-$, a diagonalisable $M$ is scalar and its commutant is all of $GL_4(\mathbb{C})$; a non-scalar $M$ with repeated eigenvalue is a Jordan block, has no eigenbasis, and its projectors are oblique.

## The Double Centraliser

**Theorem (the bicommutant of an element).**
$$
C(C(M))=\mathbb{C}[M]=\operatorname{span}\{\mathrm I_4,M\}.
$$
The dimension is one when $\tilde Q$ is scalar and two otherwise.

*Proof.* If $A$ is non-scalar, $C(M)=M_2(\mathbb{C})\otimes C(A)$ with $C(A)=\mathbb{C}[A]$ commutative. The centraliser of $M_2(\mathbb{C})$ in $M_2(\mathbb{C})$ is the scalar line, and the centraliser of $C(A)$ in $M_2(\mathbb{C})$ is $C(A)$ itself, because $C(A)$ is a maximal commutative subalgebra. Hence the centraliser of the tensor product is $\mathrm I_2\otimes C(A)$, which is exactly the algebra generated by $\mathrm I_2\otimes A=M$. If $A$ is scalar, $C(M)=M_4(\mathbb{C})$ and its centraliser is the scalar line, which is again $\mathbb{C}[M]$. $\square$

**The two double centralisers.** The theorem is not the double centraliser theorem of the whole image, which is proved in §*The Right Regular Image*. There are three distinct statements:

| Object | Centraliser | Double centraliser |
|---|---|---|
| the element $M$ | $C(M)$, dimension $8$ or $16$ | $\mathbb{C}[M]$, dimension $2$ or $1$ |
| the left image $M_4(\mathbb{C})_L$ | $M_4(\mathbb{C})_R$, dimension $4$ | $M_4(\mathbb{C})_L$ |
| the right image $M_4(\mathbb{C})_R$ | $M_4(\mathbb{C})_L$, dimension $4$ | $M_4(\mathbb{C})_R$ |

The element and the whole image behave differently because the element generates only a commutative subalgebra, while the image is the whole four-dimensional simple algebra. The double centraliser theorem recovers the algebra generated by the object, not the object itself.

**The right regular image.** The right multiplication is the other side of the double centraliser. Its matrix is $\mathsf{M}_4^{R}(\tilde Q)$, the $4\times4$ matrix whose $\mu$-th column is the coordinate column of $e_\mu\tilde Q$:
$$
\boxed{\;\mathsf{M}_4^{R}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}\;}
$$
It differs from $\mathsf{M}_4(\tilde Q)$ only in the signs of the entries that mix the vector coordinates. It is anti-multiplicative,
$$
\mathsf{M}_4^{R}(\tilde P)\mathsf{M}_4^{R}(\tilde Q)=\mathsf{M}_4^{R}(\tilde Q\tilde P),
$$
injective, and its image $M_4(\mathbb{C})_R$ is the commutant of the left image. With $D=\operatorname{diag}(1,-1,-1,-1)$,
$$
\mathsf{M}_4^{R}(\tilde Q)=D\,\mathsf{M}_4(\tilde Q)^{\mathsf T}D
=D\,\mathsf{M}_4(\tilde Q^{\natural})D,
\qquad
\mathsf{M}_4(\tilde Q)^{\mathsf T}=\mathsf{M}_4(\tilde Q^{\natural}).
$$
In the Peirce basis it is not block diagonal: it mixes the two copies, while left multiplication preserves each of them. Both images have complex dimension four, and their intersection is the scalar line $\mathbb{C}\mathrm I_4$.

**The double centraliser theorem.** The commutant of the left image is the right image, and conversely:
$$
\{T:T\mathsf{M}_4(\tilde Q)=\mathsf{M}_4(\tilde Q)T\ \text{for all }\tilde Q\}=M_4(\mathbb{C})_R,
\qquad
\{T:T M_R=M_RT\ \text{for all }M_R\}=M_4(\mathbb{C})_L.
$$
If $T$ commutes with every left multiplication, then $T(\tilde X)=T(\tilde X e_t)=\tilde X\,T(e_t)$, so $T$ is right multiplication. The converse is associativity, and the second statement is the same argument with the sides exchanged.

## Summary

The full commutant of a non-scalar regular matrix is $M_2(\mathbb{C})\otimes C(A)$, of dimension eight; for a scalar it is all of $M_4(\mathbb{C})$. The relative commutant inside the image is the centraliser of the biquaternion, of dimension two or four. The right regular matrix is the anti-multiplicative matrix of right multiplication, and its image is the commutant of the left image. The bicommutant of the element is the algebra it generates, of dimension two or one, while the double centraliser of the whole image is the right image. The eigenbasis ambiguity is $GL_2\times GL_2$, larger than in the $2\times2$ model by the mixing of the two copies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C(M)$ | the commutant in $M_4(\mathbb{C})$ |
| $C_L(M)$ | the relative commutant in the image |
| $C(A)$ | the centraliser of the $2\times2$ block |
| $\mathbb{C}[M]$ | the algebra generated by $M$ |
| $GL_2\times GL_2$ | the eigenbasis ambiguity for distinct eigenvalues |
| $\mathsf{M}_4^{R}(\tilde Q)$ | the right regular matrix |
| $M_4(\mathbb{C})_R$ | the right image |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the sign matrix relating the two matrices |

## Further Reading

- [$M_4(\mathbb{C})_L$ Model : The Eigenbasis and the Diagonalising Matrix](m4c-model-the-eigenbasis-and-the-diagonalising-matrix.html), for the ambiguity
- [$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m2c-model-the-centraliser-and-the-double-centraliser.html), for the $2\times2$ version
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra generated by one element
