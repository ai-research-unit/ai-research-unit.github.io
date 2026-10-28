# __The Operators of the Peirce Decomposition of $M_3(\mathbb{C})$__

## Introduction

**The Peirce decomposition is acted on by four families of linear operators: the left multiplication $L_a$, the right multiplication $R_a$, the sandwich $T_{a,b}$ and the derivation $\operatorname{ad}_a$.** On the matrix units, $L_a$ moves the row index, $R_a$ moves the column index, $T_{a,b}$ moves both, and $\operatorname{ad}_a$ is the difference of the two. The derivations of $M_3(\mathbb{C})$ are exactly the inner derivations, $\operatorname{Der}(M_3)\cong\mathfrak{sl}_3(\mathbb{C})$, of complex dimension $8$; the automorphisms are exactly the inner automorphisms, $\operatorname{Aut}(M_3)\cong PGL_3(\mathbb{C})$, of complex dimension $8$. The transpose, the conjugate transpose and the entrywise conjugation are not complex-linear automorphisms: they are anti-automorphisms or conjugate-linear maps.

The article defines the four operators, computes their matrices and their action on the Peirce corners, proves the derivation and automorphism theorems, and explains the sandwich as a map of corners. The Peirce decomposition and the corners $A_{ij}=\mathbb{C}E_{ij}$ are *The Peirce Decomposition of $M_3(\mathbb{C})$*; the coarse split by a rank-one idempotent is *The Rank-Two Split of $M_3(\mathbb{C})$*; the conjugation action and its orbits are *The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$*; the frame and the gauge are *The Frame, the Simple Nilpotents and the Gauge of $M_3(\mathbb{C})$*.

## The Four Operators

**Definition.** For $a,b\in M_3(\mathbb{C})$, define the linear maps $M_3(\mathbb{C})\to M_3(\mathbb{C})$ by

$$
L_a(X)=aX,\qquad
R_a(X)=Xa,\qquad
T_{a,b}(X)=aXb,\qquad
\operatorname{ad}_a(X)=[a,X]=aX-Xa .
$$

The operator $T_{a,b}$ is the **sandwich**; $\operatorname{ad}_a$ is the **adjoint** or **inner derivation**.

**Proposition.** The operators satisfy

$$
T_{a,b}=L_aR_b=R_bL_a,\qquad
\operatorname{ad}_a=L_a-R_a,
$$

and

$$
L_aL_b=L_{ab},\qquad
R_aR_b=R_{ba},\qquad
L_aR_b=R_bL_a .
$$

**Proof.** The identities are the associativity of the product: $a(Xb)=(aX)b$ and $(ab)X=a(bX)$, while $X(ba)=(Xb)a$. The adjoint is the difference of the left and the right multiplications.

**The matrices.** Vectorise $M_3$ by rows, so that $X$ is a column of nine entries, ordered $X_{11},X_{12},X_{13},X_{21},\dots,X_{33}$. Then

$$
L_a=a\otimes I_3,\qquad
R_b=I_3\otimes b^{\mathsf T},\qquad
T_{a,b}=a\otimes b^{\mathsf T},
$$

$$
\operatorname{ad}_a=a\otimes I_3-I_3\otimes a^{\mathsf T}.
$$

**Proof.** The row vectorisation of $aX$ is $(a\otimes I_3)\operatorname{vec}X$, because the $(i,j)$ entry of $aX$ is $\sum_k a_{ik}X_{kj}$. The row vectorisation of $Xb$ is $(I_3\otimes b^{\mathsf T})\operatorname{vec}X$, because the $(i,j)$ entry of $Xb$ is $\sum_l X_{il}b_{lj}$. The sandwich is the composition, and the adjoint is the difference.

**The eigenvalues and the trace.** Let $\lambda_1,\lambda_2,\lambda_3$ be the eigenvalues of $a$, counted with algebraic multiplicity, and $\mu_1,\mu_2,\mu_3$ those of $b$. The eigenvalues of $L_a$ are $\lambda_1,\lambda_2,\lambda_3$, each with multiplicity $3$; those of $R_b$ are $\mu_1,\mu_2,\mu_3$, each with multiplicity $3$; those of $T_{a,b}$ are the nine products $\lambda_i\mu_j$; and those of $\operatorname{ad}_a$ are the nine differences $\lambda_i-\lambda_j$. Hence

$$
\operatorname{tr}L_a=3\operatorname{tr}a,\qquad
\operatorname{tr}R_b=3\operatorname{tr}b,\qquad
\operatorname{tr}T_{a,b}=\operatorname{tr}a\operatorname{tr}b,\qquad
\operatorname{tr}\operatorname{ad}_a=0,
$$

$$
\det L_a=(\det a)^3,\qquad
\det R_b=(\det b)^3,\qquad
\det T_{a,b}=(\det a)^3(\det b)^3.
$$

**Proof.** The eigenvalues of $a\otimes b^{\mathsf T}$ are the pairwise products of the eigenvalues of $a$ and of $b^{\mathsf T}$, which are those of $b$; the trace is the sum of the products, $\operatorname{tr}a\operatorname{tr}b$, and the determinant is their product, $(\det a)^3(\det b)^3$. The assertions for $L_a$ and $R_b$ are the cases $b=I$ and $a=I$. For the adjoint, $a\otimes I$ and $I\otimes a^{\mathsf T}$ commute, and their eigenvalues on the common eigenbasis are $\lambda_i$ and $\lambda_j$, so the difference has eigenvalues $\lambda_i-\lambda_j$. The trace is $\sum_{i,j}(\lambda_i-\lambda_j)=3\operatorname{tr}a-3\operatorname{tr}a=0$.

**The rank of the adjoint.** The kernel of $\operatorname{ad}_a$ is the centraliser

$$
Z(a)=\{X\in M_3:aX=Xa\}.
$$

For a semisimple element with eigenvalue multiplicities $m_1,m_2,m_3$, the centraliser is the direct sum of the full matrix algebras on the eigenspaces, and $\dim Z(a)=\sum_i m_i^2$. In general the centraliser of a Jordan form is computed block by block, and

$$
\operatorname{rank}\operatorname{ad}_a=9-\dim Z(a).
$$

For an element with three distinct eigenvalues the centraliser is the algebra of polynomials in $a$, of dimension $3$, and the rank is $6$. For a scalar the centraliser is all of $M_3$, of dimension $9$, and the rank is $0$. For the principal nilpotent $J_3(0)$ the centraliser is the three-dimensional algebra $\mathbb{C}[N]$, and the rank is again $6$. For the subregular nilpotent $E_{12}$ the centraliser is five-dimensional, so the rank is $4$ and the orbit is the minimal nilpotent orbit.

**Proof.** A matrix commuting with a Jordan block of size $d$ is upper triangular Toeplitz on that block; a block mapping one Jordan block to another with the same eigenvalue is Toeplitz of the smaller size. The count is the standard one, in Horn and Johnson, *Matrix Analysis*, Chapter 4. The rank is $9-\dim\ker$.

**The rank of the sandwich.** The sandwich $T_{a,b}=a\otimes b^{\mathsf T}$ has rank

$$
\operatorname{rank}T_{a,b}=\operatorname{rank}a\cdot\operatorname{rank}b .
$$

Its kernel is the set of $X$ with $aXb=0$, and its image is the set of matrices whose columns lie in $\operatorname{im}a$ and whose rows lie in the row space of $b$.

**Worked example: a diagonal element.** Take $a=\operatorname{diag}(1,2,4)$ and $b=\operatorname{diag}(3,5,7)$. Then $T_{a,b}$ is diagonal in the basis of matrix units, with the nine entries $3,5,7,6,10,14,12,20,28$; its trace is $105=7\cdot15$, and its determinant is $(\det a)^{3}(\det b)^{3}=8^{3}\cdot105^{3}=592\,704\,000$. The adjoint $\operatorname{ad}_a$ is diagonal with the nine entries

$$
0,\ -1,\ -3,\ 1,\ 0,\ -2,\ 3,\ 2,\ 0,
$$

in the order $E_{11},E_{12},E_{13},E_{21},E_{22},E_{23},E_{31},E_{32},E_{33}$. Its rank is $6$, its kernel is the diagonal algebra of dimension $3$, and its trace is $0$.

**Worked example: a non-diagonal element.** Take

$$
a=\begin{pmatrix}1&2&0\\0&3&1\\0&0&1\end{pmatrix},
\qquad
b=\begin{pmatrix}0&1&0\\1&0&0\\0&0&2\end{pmatrix}.
$$

Then $aE_{12}=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix}$ and

$$
T_{a,b}(E_{12})=aE_{12}b=E_{11},
\qquad
T_{a,b}(E_{13})=2E_{13}.
$$

The first identity is an elementary corner map: the unit $E_{12}$ is carried to $E_{11}$, not to a multiple of itself. The adjoint gives

$$
\operatorname{ad}_a(E_{12})=aE_{12}-E_{12}a
=\begin{pmatrix}0&-2&-1\\0&0&0\\0&0&0\end{pmatrix}
=-2E_{12}-E_{13},
$$

which is the difference of a row move and a column move.

## The Action on the Matrix Units

**The left multiplication.** On the matrix units,

$$
L_a(E_{ij})=aE_{ij}=\sum_{k=1}^{3}a_{ki}E_{kj}.
$$

The column index $j$ is fixed, and the row index is transformed by $a$. The left multiplication acts on the **row index** of the unit.

**The right multiplication.** On the matrix units,

$$
R_b(E_{ij})=E_{ij}b=\sum_{l=1}^{3}b_{jl}E_{il}.
$$

The row index $i$ is fixed, and the column index is transformed by $b$. The right multiplication acts on the **column index** of the unit.

**The sandwich.** On the matrix units,

$$
T_{a,b}(E_{ij})=aE_{ij}b=\sum_{k,l=1}^{3}a_{ki}b_{jl}E_{kl}.
$$

The coefficient of $E_{kl}$ is $a_{ki}b_{jl}$: the row index is transformed by $a$ and the column index by $b$, independently. This is the **corner map**: the unit $E_{ij}$ is sent to a linear combination of the units $E_{kl}$, and the coefficient factorises into a row factor and a column factor.

**The elementary sandwich.** For $a=E_{ir}$ and $b=E_{sl}$,

$$
T_{a,b}(E_{rs})=E_{ir}E_{rs}E_{sl}=E_{il}.
$$

The sandwich with two elementary matrices carries the corner $A_{rs}$ to the corner $A_{il}$:

$$
E_{ir}E_{rs}E_{sl}=E_{il}.
$$

The general sandwich is a linear combination of these elementary corner maps, with coefficients $a_{ir}b_{sl}$.

**The corner matrix.** The three-by-three grid of Peirce corners $A_{ij}=\mathbb{C}E_{ij}$ is acted on by the sandwich as

$$
A_{rs}\longmapsto\sum_{i,l}a_{ir}b_{sl}A_{il}.
$$

The row index of the corner is transformed by $a$, the column index by $b$. The sandwich is the tensor product of the two actions, and its matrix on the nine-dimensional space of corners is $a\otimes b^{\mathsf T}$.

**The adjoint on the units.** The adjoint is

$$
\operatorname{ad}_a(E_{ij})=aE_{ij}-E_{ij}a
=\sum_{k}a_{ki}E_{kj}-\sum_{l}a_{jl}E_{il}.
$$

The first term changes the row index, the second changes the column index; the difference is the commutator. On the diagonal units, $\operatorname{ad}_a(E_{ii})=aE_{ii}-E_{ii}a$ has zero diagonal; its off-diagonal entries are $a_{ki}$ in row $k$ and $-a_{ik}$ in column $k$.

**The Peirce table.** The multiplication rule $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$ is read through the operators: $L_a$ carries the corner $A_{ij}$ into the sum of the corners $A_{kj}$ weighted by $a_{ki}$, and $R_b$ carries it into the sum of the corners $A_{il}$ weighted by $b_{jl}$. The sandwich is the two moves composed, and the adjoint is their difference. The coarse split of *The Rank-Two Split of $M_3(\mathbb{C})$* replaces the nine lines by the four corners $1+2+2+4$, and the same operators act on the four blocks.

## The Derivations

**Definition.** A **derivation** of $M_3$ is a linear map $D:M_3\to M_3$ with

$$
D(XY)=D(X)Y+XD(Y).
$$

The derivations form a Lie algebra $\operatorname{Der}(M_3)$ under the commutator.

**Proposition.** Every inner derivation $\operatorname{ad}_a$ is a derivation:

$$
\operatorname{ad}_a(XY)=aXY-XYa
=(aX-Xa)Y+X(aY-Ya)
=\operatorname{ad}_a(X)Y+X\operatorname{ad}_a(Y).
$$

The map $a\mapsto\operatorname{ad}_a$ is linear, with kernel the centre $\mathbb{C}I$, so the inner derivations form a Lie algebra isomorphic to $M_3/\mathbb{C}I\cong\mathfrak{sl}_3(\mathbb{C})$, of complex dimension $8$.

**Theorem (inner derivations).** Every derivation of $M_3(\mathbb{C})$ is inner:

$$
\operatorname{Der}(M_3)=\operatorname{ad}_{M_3}\cong\mathfrak{sl}_3(\mathbb{C}),
\qquad
\dim_\mathbb{C}\operatorname{Der}(M_3)=8.
$$

**Proof.** A derivation is determined by its values on the matrix units. For any derivation $D$, the element

$$
a=\frac{1}{3}\sum_{i,j=1}^{3}D(E_{ij})E_{ji}
$$

satisfies $D=\operatorname{ad}_a$; the verification is the standard computation for central simple algebras, in Pierce, *Associative Algebras*, §*Derivations*. The kernel of $a\mapsto\operatorname{ad}_a$ is the centre $\mathbb{C}I$, so the image has dimension $9-1=8$, which is $\dim\mathfrak{sl}_3$. The inner derivations are contained in $\operatorname{Der}(M_3)$ and the two spaces have the same dimension, so they are equal.

**There are no outer derivations.** The space of outer derivations is zero. The Lie algebra structure is

$$
[\operatorname{ad}_a,\operatorname{ad}_b]=\operatorname{ad}_{[a,b]},
$$

so $\mathfrak{sl}_3\to\operatorname{Der}(M_3)$ is an isomorphism of Lie algebras. The derivations act on $M_3$ by the adjoint action, and the decomposition of $M_3$ under $\mathfrak{sl}_3$ is the adjoint decomposition $1+3+5$ of *The Triplet: Spin One and the Adjoint $1+3+5$ of $M_3(\mathbb{C})$*.

**Worked example.** For $a=\operatorname{diag}(1,2,4)$ the adjoint has rank $6$ and kernel the diagonal matrices, of dimension $3$. The image is the six-dimensional space of matrices with zero diagonal, the span of the six off-diagonal units. The element $a$ is regular semisimple: its centraliser is the diagonal torus, and the derivation reaches every off-diagonal direction. For $a=I$ the adjoint is zero and the kernel is the whole algebra.

**The biquaternion case.** For $M_2(\mathbb{C})$ the same theorem gives $\operatorname{Der}(M_2)\cong\mathfrak{sl}_2(\mathbb{C})$, of dimension $3$. The passage from $n=2$ to $n=3$ raises the derivation dimension from $3$ to $8$.

## The Automorphisms

**Definition.** An **automorphism** of $M_3$ is an invertible linear map $\Phi$ with $\Phi(XY)=\Phi(X)\Phi(Y)$.

**Theorem (Skolem–Noether).** Every automorphism of $M_3(\mathbb{C})$ is inner:

$$
\operatorname{Aut}(M_3)\cong PGL_3(\mathbb{C})=GL_3(\mathbb{C})/\mathbb{C}^\times I,
\qquad
\dim_\mathbb{C}=8.
$$

**Proof.** The automorphism sends the matrix units to a complete system of $3\times3$ matrix units. By the Skolem–Noether theorem for central simple algebras, any two complete systems of matrix units are conjugate by an invertible matrix. Hence $\Phi(X)=SXS^{-1}$ for some $S\in GL_3$, and $S$ is determined up to a scalar by the centre theorem. The group is $PGL_3$, of dimension $9-1=8$.

**The inner automorphisms.** The conjugation $\Phi_S(X)=SXS^{-1}$ is an automorphism for every $S\in GL_3$. It preserves the trace, the determinant, the characteristic polynomial, the rank and the Jordan type. The kernel of $S\mapsto\Phi_S$ is the centre $\mathbb{C}^\times I$, so the automorphism group is $PGL_3$.

**There are no complex-linear outer automorphisms.** The "outer" operations that appear in the theory are not complex-linear automorphisms:

- the **transpose** $X\mapsto X^{\mathsf T}$ is an anti-automorphism, $\Phi(XY)=\Phi(Y)\Phi(X)$;
- the **conjugate transpose** $X\mapsto X^*$ is a conjugate-linear anti-automorphism;
- the **entrywise conjugation** $X\mapsto\bar X$ is a conjugate-linear automorphism.

These are real-linear or conjugate-linear maps, not elements of $\operatorname{Aut}_\mathbb{C}(M_3)$. The star is the involution of *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*.

**The Lie algebra.** The group $PGL_3$ has Lie algebra $\mathfrak{sl}_3$, and the adjoint action of the group on $M_3$ is the exponentiation of the adjoint action of the Lie algebra. The orbit of an element is its conjugacy class; the classification is *The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$*.

## The Sandwich as a Map of Corners

**The corner map.** The sandwich $T_{a,b}$ is the most general linear map built from one left multiplication and one right multiplication. On the corners,

$$
T_{a,b}(A_{rs})=\sum_{i,l}a_{ir}b_{sl}A_{il}.
$$

The coefficient of $A_{il}$ is the product of the $(i,r)$ entry of $a$ and the $(s,l)$ entry of $b$. The map is the tensor product of the row action and the column action; it sends the corner $(r,s)$ to a linear combination of the corners $(i,l)$.

**The elementary corner maps.** The elementary sandwich $T_{E_{ir},E_{sl}}$ sends the corner $A_{rs}$ to the corner $A_{il}$:

$$
T_{E_{ir},E_{sl}}(A_{rs})=A_{il}.
$$

The elementary corner maps are the matrix units of the space of corner maps; the general sandwich is a linear combination with coefficients $a_{ir}b_{sl}$. In the worked example above, $T_{a,b}(E_{12})=E_{11}$ is the elementary map with $i=1$, $r=1$, $s=2$, $l=1$ and coefficients $a_{11}=1$, $b_{21}=1$.

**The inner automorphism.** For $b=a^{-1}$,

$$
T_{a,a^{-1}}(X)=aXa^{-1}
$$

is the inner automorphism $\Phi_a$. On the corners, it sends $A_{rs}$ to a linear combination of the corners $A_{il}$ with coefficients $a_{ir}(a^{-1})_{sl}$. The inner automorphism preserves the trace and the determinant but not the individual corners; it permutes the spectral lines only when $a$ is diagonal in the frame.

**The sandwich and the coarse Peirce table.** For the rank-two split with $\Pi=Q$, the sandwich with block-diagonal $a,b$ preserves the four corners; the sandwich with off-diagonal $a$ or $b$ mixes the corners. The mass block $uv$ is carried to the corner determined by the row of $a$ and the column of $b$.

**The operators span the endomorphisms.** The sandwiches $T_{a,b}$ span the space of linear maps $X\mapsto aXb$: the nine-by-nine matrix $a\otimes b^{\mathsf T}$ ranges over a space of dimension $81$, which is the whole $\operatorname{End}(M_3)$. The left and right multiplications alone span the subspace of maps that move only one index, of dimension $18$; the sandwiches add the mixed moves.

## Summary

The four operators on $M_3$ are the left multiplication $L_a(X)=aX$, the right multiplication $R_a(X)=Xa$, the sandwich $T_{a,b}(X)=aXb$ and the adjoint $\operatorname{ad}_a(X)=[a,X]$. They satisfy $T_{a,b}=L_aR_b=R_bL_a$ and $\operatorname{ad}_a=L_a-R_a$. On the matrix units, $L_a$ moves the row index, $R_a$ moves the column index, $T_{a,b}$ moves both, and $\operatorname{ad}_a$ is the difference. The matrices are $L_a=a\otimes I_3$, $R_b=I_3\otimes b^{\mathsf T}$, $T_{a,b}=a\otimes b^{\mathsf T}$ and $\operatorname{ad}_a=a\otimes I_3-I_3\otimes a^{\mathsf T}$; the eigenvalues are the eigenvalues of $a$, of $b$, the products $\lambda_i\mu_j$, and the differences $\lambda_i-\lambda_j$. The derivations of $M_3$ are exactly the inner derivations, $\operatorname{Der}(M_3)\cong\mathfrak{sl}_3$, of dimension $8$; the automorphisms are exactly the inner automorphisms, $\operatorname{Aut}(M_3)\cong PGL_3$, of dimension $8$. There are no outer derivations and no complex-linear outer automorphisms; the transpose and the conjugations are anti-automorphisms or conjugate-linear maps. The sandwich is the corner map $A_{rs}\mapsto\sum a_{ir}b_{sl}A_{il}$; the elementary sandwich $T_{E_{ir},E_{sl}}$ carries the corner $A_{rs}$ to the corner $A_{il}$.

$$
\boxed{\ \operatorname{Der}(M_3)\cong\mathfrak{sl}_3,\ \dim=8;\qquad \operatorname{Aut}(M_3)\cong PGL_3,\ \dim=8;\qquad \operatorname{rank}\operatorname{ad}_a=9-\dim Z(a).\ }
$$

| Operator | Matrix | Action on $E_{ij}$ | Trace |
|---|---|---|---|
| $L_a$ | $a\otimes I_3$ | row index by $a$ | $3\operatorname{tr}a$ |
| $R_b$ | $I_3\otimes b^{\mathsf T}$ | column index by $b$ | $3\operatorname{tr}b$ |
| $T_{a,b}$ | $a\otimes b^{\mathsf T}$ | both indices | $\operatorname{tr}a\operatorname{tr}b$ |
| $\operatorname{ad}_a$ | $a\otimes I_3-I_3\otimes a^{\mathsf T}$ | commutator | $0$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a$ | left multiplication $X\mapsto aX$ |
| $R_a$ | right multiplication $X\mapsto Xa$ |
| $T_{a,b}$ | sandwich $X\mapsto aXb$ |
| $\operatorname{ad}_a$ | adjoint $X\mapsto[a,X]$ |
| $\operatorname{Der}(M_3)$ | the derivation algebra, $\cong\mathfrak{sl}_3$ |
| $\operatorname{Aut}(M_3)$ | the automorphism group, $\cong PGL_3$ |
| $A_{ij}=\mathbb{C}E_{ij}$ | the Peirce corner $(i,j)$ |
| $Z(a)$ | the centraliser of $a$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for derivations, automorphisms and the Skolem–Noether theorem.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for central simple algebras and their automorphisms.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Kronecker product, vectorisation and the centraliser of a Jordan form.
- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the corners and the multiplication rule.
- [The Rank-Two Split of $M_3(\mathbb{C})$](the-rank-two-split-of-m3c.html), for the two-sided Peirce table.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m3c.html), for the conjugation action and its orbits.
- [The Triplet: Spin One and the Adjoint $1+3+5$ of $M_3(\mathbb{C})$](the-triplet-spin-one-and-the-adjoint-of-m3c.html), for the adjoint decomposition under $\mathfrak{sl}_3$.
