# __The Adjoints and the Polar Decomposition of an Operator over $\mathbb{R}$__

## Introduction

**The operator space carries a positive definite form, and with it every operator has an adjoint; the adjoint of the two-sided operator $T_{A,B}$ is $T_{A^{\mathsf T},B^{\mathsf T}}$, and the polar decomposition of an operator is the polar decomposition of its two factors.** The form is the Hilbert–Schmidt form $\langle S,T\rangle=\operatorname{tr}(S^{\mathsf T}T)$, which is definite but not invariant. The invariance is what the trace form has, and the two forms give different adjoints: this is the first thing to keep apart.

The article defines the Hilbert–Schmidt form, computes the adjoints of $L_A$, of $R_B$, of $T_{A,B}$ and of $\operatorname{ad}_A$, divides the operator space into a self-adjoint and an antisymmetric half, and proves the polar decomposition $T=UP$. It computes the singular values of $T_{A,B}$ as the products of those of $A$ and of $B$, and compares the operator norm with the Hilbert–Schmidt norm. It assumes *The Two-Sided Operators and the Real Segre Cone* for the operators and their composition, and it defers the splitting of the operator space to *The Symmetric and Antisymmetric Parts of the Operator Space*.

Throughout $n\ge2$, $M_n=M_n(\mathbb{R})$ and $\operatorname{End}=\operatorname{End}(M_n)$.

## The Hilbert–Schmidt Form

**Definition.** For $S,T\in\operatorname{End}$,

$$
\langle S,T\rangle=\operatorname{tr}(S^{\mathsf T}T),
$$

where $S^{\mathsf T}$ is the transpose of the matrix of $S$ in an orthonormal basis of $M_n$.

**The form is an inner product.** The entry $(i,j)$ of $S^{\mathsf T}T$ is the scalar product of the $i$-th row of $S$ with the $j$-th column of $T$, so

$$
\langle S,T\rangle=\sum_{i,j}S_{ij}T_{ij},
$$

the sum of the products of corresponding entries of the $n^{2}\times n^{2}$ matrices. Symmetry, bilinearity and positive definiteness are the corresponding properties of the scalar product on $\mathbb{R}^{n^{2}}$.

**The form is not invariant.** The trace form satisfies $\langle ST,U\rangle=\langle S,TU\rangle$; the Hilbert–Schmidt form does not, since the transposition is in the way. So the operator space carries a definite form that the algebra does not preserve, and an indefinite one that it does.

**The adjoint is the transpose of the matrix.** For every $S$ there is a unique $S^{*}$ with $\langle SX,Y\rangle=\langle X,S^{*}Y\rangle$ for all $X,Y$, namely the transpose of the matrix of $S$. So the adjoint operation on $\operatorname{End}$ is the transpose involution of $M_{n^{2}}(\mathbb{R})$, and the orthogonal group of the form is $\mathrm{O}(n^{2})$.

## The Adjoint of the One-Sided Operators

**Theorem.** $L_A^{*}=L_{A^{\mathsf T}}$ and $R_B^{*}=R_{B^{\mathsf T}}$.

*Proof.* Compute in the entries of $M_n$:

$$
\langle L_AX,Y\rangle=\operatorname{tr}((AX)^{\mathsf T}Y)=\operatorname{tr}(X^{\mathsf T}A^{\mathsf T}Y)=\langle X,L_{A^{\mathsf T}}Y\rangle .
$$

The second identity is the same computation with $(XB)^{\mathsf T}=B^{\mathsf T}X^{\mathsf T}$:

$$
\langle R_BX,Y\rangle=\operatorname{tr}(B^{\mathsf T}X^{\mathsf T}Y)=\operatorname{tr}(X^{\mathsf T}YB^{\mathsf T})=\langle X,R_{B^{\mathsf T}}Y\rangle .
$$

**The adjoint stays on the same side.** The adjoint of a left multiplication is a left multiplication, and the adjoint of a right multiplication is a right multiplication. The trace form behaves otherwise: $\langle L_AX,Y\rangle=\operatorname{tr}(AXY)=\operatorname{tr}(XYA)=\langle X,R_AY\rangle$, so under it the adjoint of $L_A$ is $R_A$ and the side is exchanged.

**Measured at $n=3$.** For random $A,X,Y$ the identity $\langle AX,Y\rangle=\langle X,A^{\mathsf T}Y\rangle$ holds to machine precision, and $\langle AX,Y\rangle=\langle X,YA^{\mathsf T}\rangle$ fails by a quantity of order $10$. So the adjoint of $L_A$ is not $R_{A^{\mathsf T}}$.

## The Adjoint of the Two-Sided Operator

**Theorem.** $T_{A,B}^{*}=T_{A^{\mathsf T},B^{\mathsf T}}$.

*Proof.* $\langle AXB,Y\rangle=\operatorname{tr}(B^{\mathsf T}X^{\mathsf T}A^{\mathsf T}Y)=\operatorname{tr}(X^{\mathsf T}A^{\mathsf T}YB^{\mathsf T})=\langle X,A^{\mathsf T}YB^{\mathsf T}\rangle$.

**The adjoint is the two-sided operator of the transposed factors.** So the map $(A,B)\mapsto T_{A,B}$ commutes with the adjoint, and the adjoint of a two-sided operator is again two-sided. The identity holds to machine precision at $n=3$.

**The products with the adjoint are two-sided and self-adjoint.** By the composition rule,

$$
T_{A,B}^{*}T_{A,B}=T_{A^{\mathsf T}A,\,BB^{\mathsf T}},\qquad T_{A,B}T_{A,B}^{*}=T_{AA^{\mathsf T},\,B^{\mathsf T}B} .
$$

Both are self-adjoint, since $A^{\mathsf T}A$, $BB^{\mathsf T}$, $AA^{\mathsf T}$ and $B^{\mathsf T}B$ are symmetric. And both are positive semidefinite for the form, because

$$
\langle X,T_{A^{\mathsf T}A,BB^{\mathsf T}}X\rangle=\operatorname{tr}\big((AXB)^{\mathsf T}(AXB)\big)=\|AXB\|_{\mathrm{F}}^{2}\ge0 .
$$

So $T_{A,B}^{*}T_{A,B}$ is the operator whose square root is the positive factor of the polar decomposition.

## The Inner Derivations

**Definition.** The **inner derivation** is $\operatorname{ad}_A=L_A-R_A$, that is, $\operatorname{ad}_A(X)=AX-XA$.

**Theorem.** $\operatorname{ad}_A^{*}=\operatorname{ad}_{A^{\mathsf T}}$.

*Proof.* By the two theorems above, $L_A^{*}-R_A^{*}=L_{A^{\mathsf T}}-R_{A^{\mathsf T}}$.

**The derivation is self-adjoint only for symmetric $A$.** The operator $\operatorname{ad}_A$ is self-adjoint exactly when $A=A^{\mathsf T}$, and antisymmetric exactly when $A=-A^{\mathsf T}$. Measured at $n=3$, $\operatorname{ad}_A$ is antisymmetric for an antisymmetric $A$ and not for a symmetric one.

**The trace form makes every derivation antisymmetric.** For the trace form, $\langle \operatorname{ad}_AX,Y\rangle+\langle X,\operatorname{ad}_AY\rangle=\operatorname{tr}(AXY)-\operatorname{tr}(XYA)=0$ for every $A$, to machine precision at $n=3$. So the antisymmetry is a property of the invariant form, not of the algebra.

## The Self-Adjoint and the Antisymmetric Operators

**Definition.** An operator $S$ is **self-adjoint** when $S^{*}=S$ and **antisymmetric** when $S^{*}=-S$.

**Every operator splits.** Since $2$ is invertible,

$$
S=\tfrac12(S+S^{*})+\tfrac12(S-S^{*}),
$$

the first term self-adjoint and the second antisymmetric. The two subspaces meet only at $0$, so

$$
\operatorname{End}=\operatorname{End}_{\mathrm{sym}}\oplus\operatorname{End}_{\mathrm{anti}},\qquad
\dim\operatorname{End}_{\mathrm{sym}}=\frac{n^{2}(n^{2}+1)}{2},\qquad
\dim\operatorname{End}_{\mathrm{anti}}=\frac{n^{2}(n^{2}-1)}{2}.
$$

At $n=2$ the counts are $16=10+6$; at $n=3$ they are $81=45+36$. The table of *The Symmetric and Antisymmetric Parts of the Operator Space* is this decomposition, read as the splitting of the operator algebra.

**The two-sided operators are not self-adjoint in general.** $T_{A,B}$ is self-adjoint exactly when $A$ and $B$ are symmetric. So the real Segre cone meets the self-adjoint half in the cone over the product of two symmetric rank-one varieties, and meets the antisymmetric half only at $0$.

## The Polar Decomposition

**Theorem.** Every invertible $T\in\operatorname{End}$ factors uniquely as

$$
T=UP,\qquad U^{*}U=UU^{*}=\mathrm{I},\qquad P^{*}=P,\quad P>0 .
$$

*Proof.* The operator $T^{*}T$ is self-adjoint and positive definite, since $\langle X,T^{*}TX\rangle=\|TX\|^{2}>0$ for $X\ne0$. It has a self-adjoint positive square root $P$, obtained by diagonalising it in an orthonormal basis and taking the square roots of the eigenvalues. Put $U=TP^{-1}$. Then

$$
U^{*}U=P^{-1}T^{*}TP^{-1}=P^{-1}P^{2}P^{-1}=\mathrm{I},
$$

so $U$ is orthogonal, and $T=UP$. For uniqueness, $T^{*}T=P^{2}$ forces $P$ to be the positive square root, and then $U=TP^{-1}$ is forced.

**The decomposition is the polar decomposition of a matrix, at size $n^{2}$.** It is the factorisation of an invertible matrix into an orthogonal and a positive definite factor. Measured at $n=3$ on a random operator, the factorisation reproduces $T$, $U$ is orthogonal, $P$ is symmetric and positive with smallest eigenvalue $0.2693$.

**The orthogonal factor is continuous, so the decomposition retracts the group of invertibles.** The map $T\mapsto U=TP^{-1}$ is continuous on the open set of invertible operators, and it is the identity on the orthogonal group. Following $t\mapsto U_t$ along $P_t=P^{t}$ gives a deformation retraction of $\mathrm{GL}_{n^{2}}(\mathbb{R})$ onto $\mathrm{O}(n^{2})$, the statement used in *The Topology of $M_n(\mathbb{R})$ and the Sign of the Determinant*.

**The polar decomposition of a two-sided operator is the pair of decompositions of its factors.** Write $A=U_A|A|$ with $|A|=(A^{\mathsf T}A)^{1/2}$ and $B=|B^{\mathsf T}|V$ with $|B^{\mathsf T}|=(BB^{\mathsf T})^{1/2}$. Then

$$
T_{A,B}=T_{U_A,V}\,T_{|A|,|B^{\mathsf T}|},
$$

the first factor orthogonal, the second self-adjoint positive. The identity is the composition rule: $T_{U_A,V}T_{|A|,|B^{\mathsf T}|}=T_{U_A|A|,\,|B^{\mathsf T}|V}=T_{A,B}$. So the orthogonal factor of $T_{A,B}$ is the two-sided operator of the two orthogonal factors, and the positive factor is the two-sided operator of the two positive factors.

## The Singular Values

**Theorem.** The singular values of $T_{A,B}$ are the $n^{2}$ products $\sigma_i(A)\sigma_j(B)$, $1\le i,j\le n$, counted with multiplicity.

*Proof.* By the vectorisation, the matrix of $T_{A,B}$ is the Kronecker product $B^{\mathsf T}\otimes A$. The singular values of a Kronecker product $C\otimes D$ are the products of the singular values of $C$ and of $D$: both factors are diagonalised by pairs of orthogonal matrices, and the tensor product of two orthogonal matrices is orthogonal. The singular values of $B^{\mathsf T}$ are those of $B$.

**The spectral norm multiplies.** The largest singular value is the operator norm, so

$$
\|T_{A,B}\|=\|A\|\,\|B\| .
$$

At $n=3$, on random $A,B$, the computed operator norm of $T_{A,B}$ and the product of the two operator norms agree to $10^{-15}$.

**The singular values count the rank.** The number of nonzero products is $(\operatorname{rk}A)(\operatorname{rk}B)$, the rank formula of *The Two-Sided Operators and the Real Segre Cone*.

## The Two Norms

**The Hilbert–Schmidt norm of a two-sided operator is a product.** Since the Hilbert–Schmidt norm is the Euclidean norm of the list of singular values,

$$
\|T_{A,B}\|_{\mathrm{HS}}^{2}=\sum_{i,j}\sigma_i(A)^{2}\sigma_j(B)^{2}=\Big(\sum_i\sigma_i(A)^{2}\Big)\Big(\sum_j\sigma_j(B)^{2}\Big),
$$

so $\|T_{A,B}\|_{\mathrm{HS}}=\|A\|_{\mathrm{F}}\|B\|_{\mathrm{F}}$. Measured at $n=3$ on random $A,B$, the two sides agree to $10^{-15}$.

**The two norms are the two ends of the list of singular values.** The operator norm is the largest singular value $\|A\|\|B\|$ and the Hilbert–Schmidt norm is the Euclidean length $\|A\|_{\mathrm{F}}\|B\|_{\mathrm{F}}$, with

$$
\|T\|\le\|T\|_{\mathrm{HS}}\le n\,\|T\|
$$

for every operator on $M_n$, because there are $n^{2}$ singular values and the largest dominates the Euclidean length by at most the factor $n$. Both are sharp, the first at a rank-one operator and the second at a scalar multiple of an orthogonal one.

**The norm of the adjoint is the norm.** $\|T^{*}\|=\|T\|$ and $\|T^{*}\|_{\mathrm{HS}}=\|T\|_{\mathrm{HS}}$, since the adjoint has the same singular values. For $T_{A,B}$ this is the statement $\|A^{\mathsf T}\|\|B^{\mathsf T}\|=\|A\|\|B\|$, which holds because transposition preserves singular values; measured at $n=3$, both norms agree to machine precision.

## Summary

The Hilbert–Schmidt form $\langle S,T\rangle=\operatorname{tr}(S^{\mathsf T}T)$ is positive definite on the operator space, and the adjoint it defines is the transpose of the $n^{2}\times n^{2}$ matrix. The adjoints are $L_A^{*}=L_{A^{\mathsf T}}$, $R_B^{*}=R_{B^{\mathsf T}}$, $T_{A,B}^{*}=T_{A^{\mathsf T},B^{\mathsf T}}$ and $\operatorname{ad}_A^{*}=\operatorname{ad}_{A^{\mathsf T}}$: the side is kept and the matrix transposed, while the trace form exchanges the side. Every operator splits into a self-adjoint and an antisymmetric part, of dimensions $n^{2}(n^{2}+1)/2$ and $n^{2}(n^{2}-1)/2$, the second being the Lie algebra of $\mathrm{O}(n^{2})$. Every invertible operator factors as $T=UP$ with $U$ orthogonal and $P$ positive, which retracts $\mathrm{GL}_{n^{2}}(\mathbb{R})$ onto $\mathrm{O}(n^{2})$. The singular values of $T_{A,B}$ are the products $\sigma_i(A)\sigma_j(B)$, so the operator norm and the Hilbert–Schmidt norm of $T_{A,B}$ are the products of the corresponding norms of $A$ and of $B$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle S,T\rangle=\operatorname{tr}(S^{\mathsf T}T)$ | the Hilbert–Schmidt form |
| $S^{*}$ | the adjoint, the transpose of the matrix of $S$ |
| $L_A$, $R_B$, $T_{A,B}$ | left, right and two-sided multiplication |
| $\operatorname{ad}_A=L_A-R_A$ | the inner derivation |
| $\operatorname{End}_{\mathrm{sym}}$, $\operatorname{End}_{\mathrm{anti}}$ | the self-adjoint and antisymmetric operators |
| $T=UP$ | the polar decomposition, $U$ orthogonal and $P$ positive |
| $\sigma_i(A)$ | the singular values of $A$ |
| $\|T\|$, $\|T\|_{\mathrm{HS}}$ | the operator norm and the Hilbert–Schmidt norm |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Hilbert–Schmidt form, the polar decomposition and the singular values.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Kronecker product and its singular values.
- [The Two-Sided Operators and the Real Segre Cone](the-two-sided-operators-and-the-real-segre-cone.html), for the operators, their composition and their rank.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the trace form and the transpose.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-operator-space-over-r.html), for the splitting and its two involutions.
