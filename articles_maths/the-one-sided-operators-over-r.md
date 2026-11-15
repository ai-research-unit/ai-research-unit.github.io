# __The One-Sided Operators__

## Introduction

**The map $X\mapsto AX$ is an operator on the $n^{2}$-dimensional matrix space whose invariants are read off from $A$ without any computation: its rank is $n$ times the rank of $A$, its spectrum is the spectrum of $A$ repeated $n$ times, and its adjoint is the left multiplication by $A^{\mathsf T}$.** The right multiplication behaves the same way, with the transpose in the parameter.

The article computes the kernel and the image, the rank, the spectrum and the Hilbert–Schmidt adjoint of $L_A$ and $R_B$, identifies the group of invertible left multiplications with $\mathrm{GL}_n(\mathbb{R})$ and its orbits, and shows that the two families are exchanged by the transpose of the argument. It assumes *$\operatorname{End}(M_n(\mathbb{R}))$ as an Algebra: the Regular Representation* for the algebra of operators and the commutant, and *The Matrix Algebra $M_n(\mathbb{R})$* for the rank and the spectrum.

## The Two Families

**Definition.** For $A,B\in M_n(\mathbb{R})$ put

$$
L_A(X)=AX,\qquad R_B(X)=XB .
$$

Both are linear maps of $M_n(\mathbb{R})$ into itself, hence elements of $\operatorname{End}(M_n(\mathbb{R}))$, which has dimension $n^{4}$.

**They are different operators.** $L_A$ multiplies on the left and mixes the rows of $X$; $R_B$ multiplies on the right and mixes the columns. For $n\ge2$ neither family contains the other: $L_A=R_B$ forces $A=B=\lambda\mathrm{I}$.

**In a basis they are Kronecker products.** Stack the columns of $X$ into a column of length $n^{2}$. Then $\operatorname{vec}(AX)=(\mathrm{I}_n\otimes A)\operatorname{vec}X$ and $\operatorname{vec}(XB)=(B^{\mathsf T}\otimes\mathrm{I}_n)\operatorname{vec}X$, so

$$
[L_A]=\mathrm{I}_n\otimes A,\qquad [R_B]=B^{\mathsf T}\otimes\mathrm{I}_n .
$$

Every computation below is a computation with one of these two matrices.

## Composition and Inverses

**Theorem.** $L_AL_B=L_{AB}$ and $R_BR_C=R_{CB}$.

*Proof.* Apply both sides to $X$: $L_AL_B(X)=A(BX)=(AB)X$ and $R_BR_C(X)=(XC)B=X(CB)$.

**The left family is a copy of the algebra, the right family a copy of the opposite algebra.** So $A\mapsto L_A$ is an algebra isomorphism and $B\mapsto R_B$ is an algebra anti-isomorphism. Both maps are injective, since $L_A=0$ or $R_B=0$ forces the parameter to vanish by evaluation at $\mathrm{I}$.

**Corollary.** $L_A$ is invertible if and only if $A$ is invertible, and then $L_A^{-1}=L_{A^{-1}}$. The same holds on the right, with $R_B^{-1}=R_{B^{-1}}$.

*Proof.* If $A$ is invertible, $L_AL_{A^{-1}}=L_{\mathrm{I}}=\mathrm{id}$. Conversely, if $L_A$ is invertible with inverse $T$, then $A\,T(\mathrm{I})=L_A(T(\mathrm{I}))=\mathrm{I}$, so $A$ has a right inverse and is invertible.

**Nilpotence is preserved.** If $A^{k}=0$ then $L_A^{k}=L_{A^{k}}=0$, and conversely $L_A^{k}=0$ gives $A^{k}=L_A^{k}(\mathrm{I})=0$. So $L_A$ is nilpotent exactly when $A$ is, with the same index.

## Kernel and Image

**Theorem.** $\ker L_A=\{X:AX=0\}$ is the set of matrices whose columns lie in $\ker A$, and

$$
\dim\ker L_A=n\,(n-\operatorname{rk}A).
$$

*Proof.* Write $X$ as the block of its columns, $X=(x_1|\dots|x_n)$. Then $AX=(Ax_1|\dots|Ax_n)$, so $AX=0$ exactly when $Ax_j=0$ for every $j$. Each column ranges over the subspace $\ker A$, of dimension $n-\operatorname{rk}A$, independently of the others, so the space of such $X$ has dimension $n(n-\operatorname{rk}A)$.

**Theorem.** $\operatorname{im}L_A=\{AX\}$ is the set of matrices whose columns lie in $\operatorname{im}A$, and its dimension is $n\operatorname{rk}A$.

*Proof.* Same block reading: every column of $AX$ is $A$ times a vector, hence lies in $\operatorname{im}A$, and every matrix with columns in $\operatorname{im}A$ is $A$ times the matrix of preimages. The columns are free, so the dimension is $n\dim\operatorname{im}A$.

**The two counts add up.** $n\operatorname{rk}A+n(n-\operatorname{rk}A)=n^{2}$, which is the rank–nullity theorem for $L_A$ and an independent check of both formulas.

**At $n=3$ with $\operatorname{rk}A=2$** the kernel has dimension $3$ and the image dimension $6$, and the numerical rank of $[L_A]$ is $6$. The three zero eigenvalues of $L_A$ are exactly the three dimensions of the kernel.

## The Rank

**Theorem.** $\operatorname{rk}L_A=n\operatorname{rk}A$.

*Proof.* It is the dimension of the image, computed above. Equivalently, a rank-$r$ matrix factors as $A=UV^{\mathsf T}$ with $U$ of size $n\times r$ and $V$ of size $n\times r$ of rank $r$, and then $X\mapsto AX=U(V^{\mathsf T}X)$ is a composition of a map onto an $r$-dimensional space of rows and a map of rank $r$; the count gives $nr$.

**The rank is multiplicative in the parameter only up to the factor $n$.** $\operatorname{rk}L_{AB}=n\operatorname{rk}(AB)\le n\min(\operatorname{rk}A,\operatorname{rk}B)$, so the rank of the product can drop, exactly as the rank of $AB$ can drop.

**The singular set is the image of the singular set.** $L_A$ is singular exactly when $A$ is, so the set $\{A:\det A=0\}$ is the preimage under $A\mapsto L_A$ of the singular operators. The dimension count is consistent: $\det L_A=(\det A)^{n}$ vanishes exactly when $\det A$ does.

## The Spectrum

**Theorem.** The eigenvalues of $L_A$ are the eigenvalues of $A$, each with multiplicity $n$.

*Proof.* In the Kronecker basis $[L_A]=\mathrm{I}_n\otimes A$. The eigenvalues of a Kronecker product $P\otimes Q$ are the products $\mu_i\nu_j$ of the eigenvalues of the factors. With $P=\mathrm{I}_n$ all $\mu_i=1$, so the eigenvalues are the $\nu_j$, each occurring $n$ times.

**The characteristic polynomial is the $n$-th power.** Over $\mathbb{C}$ the eigenvalues exist with multiplicity, and

$$
\chi_{L_A}(t)=\prod_{j=1}^{n}(t-\lambda_j)^{n}=\chi_A(t)^{n}.
$$

The identity is a polynomial identity in the entries, so it holds over $\mathbb{R}$ as well, where some of the $\lambda_j$ may be complex conjugate pairs.

**The trace and the determinant follow.** Comparing coefficients,

$$
\operatorname{tr}L_A=n\operatorname{tr}A,\qquad \det L_A=(\det A)^{n}.
$$

**The Jordan structure is repeated, not mixed.** Over $\mathbb{C}$ the operator $L_A$ is similar to the block diagonal matrix with $n$ copies of the Jordan form of $A$; the size of the largest block for an eigenvalue is unchanged. So the minimal polynomial of $L_A$ is the minimal polynomial of $A$.

## The Hilbert–Schmidt Adjoint

**Definition.** $\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)=\sum_{i,j}X_{ij}Y_{ij}$ is the Hilbert–Schmidt inner product, positive definite on $M_n(\mathbb{R})$.

**Theorem.** $L_A^{*}=L_{A^{\mathsf T}}$ and $R_B^{*}=R_{B^{\mathsf T}}$.

*Proof.* For all $X,Y$,

$$
\langle L_AX,Y\rangle=\operatorname{tr}\big((AX)^{\mathsf T}Y\big)=\operatorname{tr}(X^{\mathsf T}A^{\mathsf T}Y)=\langle X,A^{\mathsf T}Y\rangle=\langle X,L_{A^{\mathsf T}}Y\rangle .
$$

The adjoint is unique, so $L_A^{*}=L_{A^{\mathsf T}}$. The same computation with $Y\mapsto YB$ gives $\langle X,YB\rangle=\langle XB^{\mathsf T},Y\rangle$, that is $R_B^{*}=R_{B^{\mathsf T}}$.

**The adjoint stays in the same family.** It does not exchange left with right; it transposes the parameter. Numerically the two identities hold to $10^{-16}$ at $n=3$.

**The transpose of the argument is what exchanges the families.** For every $X$,

$$
(L_AX)^{\mathsf T}=X^{\mathsf T}A^{\mathsf T}=R_{A^{\mathsf T}}(X^{\mathsf T}),
$$

so the left multiplication by $A$, followed by the transpose of the result, is the right multiplication by $A^{\mathsf T}$ applied to the transposed argument. Written as operators, with $\tau(X)=X^{\mathsf T}$,

$$
\tau L_A\tau=R_{A^{\mathsf T}},\qquad \tau R_B\tau=L_{B^{\mathsf T}}.
$$

**$\tau$ is an anti-automorphism of $\operatorname{End}$.** It is linear and invertible, and $\tau(ST)=\tau(T)\tau(S)$ for operators $S,T$. The conjugation by an anti-automorphism turns a homomorphism into an anti-homomorphism, which is why the left family and the right family are exchanged and not preserved.

## The Group and Its Orbits

**Theorem.** $\{L_A:A\in\mathrm{GL}_n(\mathbb{R})\}$ is a subgroup of $\mathrm{GL}_{n^{2}}(\mathbb{R})$ isomorphic to $\mathrm{GL}_n(\mathbb{R})$, acting on $M_n(\mathbb{R})$ by left multiplication.

*Proof.* Invertibility of $L_A$ is equivalent to invertibility of $A$, and the product rule $L_AL_B=L_{AB}$ makes the map an isomorphism of groups.

**The orbit of the identity is the group itself.** $\{L_A(\mathrm{I}):A\in\mathrm{GL}_n(\mathbb{R})\}=\{A\}=\mathrm{GL}_n(\mathbb{R})$. Under all left multiplications, without the invertibility, the orbit of $\mathrm{I}$ is all of $M_n(\mathbb{R})$, since $L_A(\mathrm{I})=A$.

**The general orbit is classified by the kernel.** If $Y=AX$ with $A$ invertible, then $\ker Y=\ker X$: indeed $\ker Y\supseteq\ker X$, and the ranks are equal because $L_A$ preserves the rank, so the kernels have the same dimension. Conversely, if $\ker X=\ker Y$, the rule $x_j\mapsto y_j$ is well defined on the column space of $X$, because a relation among the columns of $X$ is a vector of $\ker X$, hence one of $\ker Y$. It is an isomorphism onto the column space of $Y$, and it extends to an invertible $A$ with $AX=Y$.

**The orbits are therefore indexed by subspaces.** The orbit of $X$ is the set of matrices with kernel $\ker X$, so the orbit space is the disjoint union of the Grassmannians of $(n-r)$-dimensional subspaces of $\mathbb{R}^n$ for $r=0,\dots,n$. The largest orbit is $\mathrm{GL}_n(\mathbb{R})$ itself, of dimension $n^{2}$; the smallest is $\{0\}$.

**The right action has the same structure, with the image in place of the kernel.** Right multiplication preserves the row space, and its orbits are classified by the image of the transposed matrix.

## The Numerical Check

**The invariants at $n=3$.** For a random $A$, the numerical rank of $[\mathrm{I}\otimes A]$ is $3\operatorname{rk}A$; the eigenvalues of $[\mathrm{I}\otimes A]$ are those of $A$ repeated three times, sorted, to machine precision; and the kernel has dimension $3(3-\operatorname{rk}A)$, which is $9-\operatorname{rk}L_A$.

**The degenerate case.** For a $3\times3$ matrix of rank two, built by making the third row equal the first, $L_A$ has rank $6$ and kernel dimension $3$, and three of its eigenvalues vanish, matching the three zero eigenvalues of the kernel directions.

**The adjoint.** At $n=3$ the identity $\langle AX,Y\rangle=\langle X,A^{\mathsf T}Y\rangle$ holds to $10^{-16}$, and $\langle XB,Y\rangle=\langle X,YB^{\mathsf T}\rangle$ to machine precision.

**The exchange.** The identity $\tau L_A\tau=R_{A^{\mathsf T}}$ holds exactly, to $0$ residual, and the orbit statement was checked for a pair of rank-two matrices with the same kernel: the interpolating $A$ satisfies $AX=Y$ to $1.3\times10^{-15}$.

## Summary

The left multiplication $L_A(X)=AX$ and the right multiplication $R_B(X)=XB$ are operators on the $n^{2}$-dimensional matrix space, with $[L_A]=\mathrm{I}\otimes A$ and $[R_B]=B^{\mathsf T}\otimes\mathrm{I}$. The left family is a copy of $M_n(\mathbb{R})$, the right family a copy of the opposite algebra, and $L_AL_B=L_{AB}$, $R_BR_C=R_{CB}$. The kernel of $L_A$ is the set of matrices with columns in $\ker A$, of dimension $n(n-\operatorname{rk}A)$; the image is the set of matrices with columns in $\operatorname{im}A$, of dimension $n\operatorname{rk}A$; the rank is $n\operatorname{rk}A$; the spectrum is the spectrum of $A$ with each eigenvalue repeated $n$ times, so $\operatorname{tr}L_A=n\operatorname{tr}A$ and $\det L_A=(\det A)^{n}$. For the Hilbert–Schmidt form the adjoint is $L_{A^{\mathsf T}}$, and it stays in the left family; the two families are exchanged by conjugation with the transpose of the argument, $\tau L_A\tau=R_{A^{\mathsf T}}$. The invertible left multiplications form a group isomorphic to $\mathrm{GL}_n(\mathbb{R})$, whose orbit of $\mathrm{I}$ is $\mathrm{GL}_n(\mathbb{R})$ and whose general orbits are classified by the kernel.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_A(X)=AX$ | The left multiplication by $A$ |
| $R_B(X)=XB$ | The right multiplication by $B$ |
| $[L_A]=\mathrm{I}\otimes A$ | Its matrix in the column-stacking basis |
| $[R_B]=B^{\mathsf T}\otimes\mathrm{I}$ | Its matrix in the same basis |
| $\ker L_A$ | Matrices with columns in $\ker A$, of dimension $n(n-\operatorname{rk}A)$ |
| $\operatorname{im}L_A$ | Matrices with columns in $\operatorname{im}A$, of dimension $n\operatorname{rk}A$ |
| $\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y)$ | The Hilbert–Schmidt inner product |
| $L_A^{*}=L_{A^{\mathsf T}}$ | The adjoint of $L_A$ |
| $\tau(X)=X^{\mathsf T}$ | The transpose, an anti-automorphism of $\operatorname{End}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the Kronecker product and the spectrum of $\mathrm{I}\otimes A$.
- Paul Richard Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the operator view of the regular representation.
- [$\operatorname{End}(M_n(\mathbb{R}))$ as an Algebra: the Regular Representation](end-mnr-as-an-algebra-the-regular-representation.html), for the two copies, their commutant and the dimension $2n^{2}-1$.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the rank, the trace and the determinant.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the complex case, where the same formulas hold with the conjugate transpose.
