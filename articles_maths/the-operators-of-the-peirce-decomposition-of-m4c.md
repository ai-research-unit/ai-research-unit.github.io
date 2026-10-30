# __The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$__

## Introduction

**The Peirce decomposition is acted on by four families of linear operators: left multiplication $L_a$, right multiplication $R_a$, the sandwich $T_{a,b}$, and the derivation $\operatorname{ad}_a$.** On the matrix units, $L_a$ moves the row index, $R_a$ moves the column index, $T_{a,b}$ moves both, and $\operatorname{ad}_a$ is the difference of the two. The derivations of $M_4$ are exactly the inner derivations, $\operatorname{Der}(M_4)\cong\mathfrak{sl}_4$, of dimension $15$; the automorphisms are exactly the inner automorphisms, $\operatorname{Aut}(M_4)\cong PGL_4$, of dimension $15$.

The article defines the four operators, computes their matrices and their action on the Peirce corners, proves the derivation and automorphism theorems, and explains the sandwich as a map of corners. The Peirce decomposition is *The Peirce Decomposition of $M_4(\mathbb{C})$*; the adjoint action is *The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$*; the frame and the gauge are *The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$*.

## The Four Operators

**Definitions.** For $a,b\in M_4(\mathbb{C})$, define

$$
L_a:M_4\to M_4,\qquad L_a(X)=aX,
$$

$$
R_a:M_4\to M_4,\qquad R_a(X)=Xa,
$$

$$
T_{a,b}:M_4\to M_4,\qquad T_{a,b}(X)=aXb,
$$

$$
\operatorname{ad}_a:M_4\to M_4,\qquad \operatorname{ad}_a(X)=[a,X]=aX-Xa.
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

**Proof.** The identities are the associativity of the product: $a(Xb)=(aX)b$ and $(ab)X=a(bX)$, while $X(ba)=(Xb)a$. The adjoint is the difference of the left and right multiplications.

**A note on the symbols.** Here $a,b\in M_4(\mathbb{C})$, the operators act on $M_4(\mathbb{C})\cong\mathbb{C}^{16}$, and the matrices below are $16\times16$. The article *$M_4(\mathbb{C})_{\mathbb{B},L}$ Representation : The Two-Sided Operators on the Biquaternion Algebra* uses the same letters for $a,b\in\mathbb{B}$, acting on $\mathbb{B}\cong\mathbb{C}^4$ and giving $4\times4$ matrices. The two are the same sandwich construction applied to $A=M_4(\mathbb{C})$ and to $A=\mathbb{B}$; the determinant is $\det T_{a,b}=\det L_a\det R_b$, which is $(\det a)^4(\det b)^4$ here and $N(a)^2N(b)^2$ there.

**The matrices.** Vectorise $M_4$ by columns, so that $X$ is a column of $16$ entries. Then

$$
L_a=a\otimes I_4,\qquad
R_b=I_4\otimes b^{\mathsf T},\qquad
T_{a,b}=a\otimes b^{\mathsf T},
$$

$$
\operatorname{ad}_a=a\otimes I_4-I_4\otimes a^{\mathsf T}.
$$

**Proof.** The column-vectorisation of $aX$ is $(a\otimes I)\operatorname{vec}X$, and the vectorisation of $Xb$ is $(I\otimes b^{\mathsf T})\operatorname{vec}X$. The sandwich is the composition. The adjoint is the difference.

**The eigenvalues and the trace.** The eigenvalues of $L_a$ are the eigenvalues $\lambda_1,\dots,\lambda_4$ of $a$, each with multiplicity $4$. The eigenvalues of $R_b$ are the eigenvalues $\mu_1,\dots,\mu_4$ of $b$, each with multiplicity $4$. The eigenvalues of $\operatorname{ad}_a$ are the differences $\lambda_i-\lambda_j$, $i,j=1,\dots,4$. Hence

$$
\operatorname{tr}L_a=4\operatorname{tr}a,\qquad
\operatorname{tr}R_b=4\operatorname{tr}b,\qquad
\operatorname{tr}\operatorname{ad}_a=0,
$$

$$
\det L_a=(\det a)^4,\qquad
\det R_b=(\det b)^4,\qquad
\det T_{a,b}=(\det a\det b)^4.
$$

**The rank of the adjoint.** The kernel of $\operatorname{ad}_a$ is the centraliser

$$
Z(a)=\{X:aX=Xa\},
$$

of dimension $\sum_i m_i^2$, where $m_i$ are the multiplicities of the distinct eigenvalues of $a$. Hence

$$
\operatorname{rank}\operatorname{ad}_a=16-\sum_i m_i^2.
$$

For a generic $a$ with four distinct eigenvalues, the centraliser is the algebra of polynomials in $a$, of dimension $4$, and the rank is $12$.

**The rank of the sandwich.** The sandwich $T_{a,b}=a\otimes b^{\mathsf T}$ has rank

$$
\operatorname{rank}T_{a,b}=\operatorname{rank}a\cdot\operatorname{rank}b.
$$

Its kernel is the set of $X$ with $aXb=0$, and its image is the set of matrices whose columns lie in $\operatorname{im}a$ and whose rows lie in $\operatorname{im}b^{\mathsf T}$.

## The Action on the Matrix Units

**The left multiplication.** On the matrix units,

$$
L_a(E_{ij})=aE_{ij}=\sum_{k=1}^{4}a_{ki}E_{kj}.
$$

The column index $j$ is fixed, and the row index is transformed by $a$. The left multiplication acts on the **row index** of the unit.

**The right multiplication.** On the matrix units,

$$
R_b(E_{ij})=E_{ij}b=\sum_{l=1}^{4}b_{jl}E_{il}.
$$

The row index $i$ is fixed, and the column index is transformed by $b$. The right multiplication acts on the **column index** of the unit.

**The sandwich.** On the matrix units,

$$
T_{a,b}(E_{ij})=aE_{ij}b=\sum_{k,l=1}^{4}a_{ki}b_{jl}E_{kl}.
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

**The corner matrix.** The four-by-four grid of Peirce corners $A_{ij}=\mathbb{C}E_{ij}$ is acted on by the sandwich as

$$
A_{rs}\longmapsto\sum_{i,l}a_{ir}b_{sl}A_{il}.
$$

The row index of the corner is transformed by $a$, the column index by $b$. The sandwich is the tensor product of the two actions, and its matrix on the $16$-dimensional space of corners is $a\otimes b^{\mathsf T}$.

**The adjoint on the units.** The adjoint is

$$
\operatorname{ad}_a(E_{ij})=aE_{ij}-E_{ij}a
=\sum_{k}a_{ki}E_{kj}-\sum_{l}a_{jl}E_{il}.
$$

The first term changes the row index, the second changes the column index; the difference is the commutator. On the diagonal units, $\operatorname{ad}_a(E_{ii})=aE_{ii}-E_{ii}a$ has zero diagonal; its off-diagonal entries are $a_{ki}$ in row $k$ and $-a_{ik}$ in column $k$.

## The Derivations

**Definition.** A **derivation** of $M_4$ is a linear map $D:M_4\to M_4$ with

$$
D(XY)=D(X)Y+XD(Y).
$$

The derivations form a Lie algebra $\operatorname{Der}(M_4)$ under the commutator.

**Proposition.** Every inner derivation $\operatorname{ad}_a$ is a derivation:

$$
\operatorname{ad}_a(XY)=aXY-XYa
=(aX-Xa)Y+X(aY-Ya)
=\operatorname{ad}_a(X)Y+X\operatorname{ad}_a(Y).
$$

The map $a\mapsto\operatorname{ad}_a$ is linear, with kernel the centre $\mathbb{C}I$, so the inner derivations form a Lie algebra isomorphic to

$$
M_4/\mathbb{C}I\cong\mathfrak{sl}_4(\mathbb{C}),
$$

of dimension $15$.

**Theorem (inner derivations).** Every derivation of $M_4(\mathbb{C})$ is inner:

$$
\operatorname{Der}(M_4)=\operatorname{ad}_{M_4}\cong\mathfrak{sl}_4(\mathbb{C}),
\qquad
\dim_\mathbb{C}\operatorname{Der}(M_4)=15.
$$

**Proof.** A derivation is determined by its values on the matrix units. The inner derivations act transitively on the possible values compatible with the Leibniz rule: for any derivation $D$, the element

$$
a=\frac14\sum_{i,j=1}^{4}D(E_{ij})E_{ji}
$$

satisfies $D=\operatorname{ad}_a$. The computation is the standard proof for central simple algebras (Pierce, *Associative Algebras*, §*Derivations*). The kernel of $a\mapsto\operatorname{ad}_a$ is the centre $\mathbb{C}I$, so the image has dimension $16-1=15$, which is $\dim\mathfrak{sl}_4$.

**There are no outer derivations.** The theorem says that the outer derivation space is zero. The derivation algebra is exactly the inner one, and its dimension is $15$.

**The Lie algebra structure.** The bracket of inner derivations is

$$
[\operatorname{ad}_a,\operatorname{ad}_b]=\operatorname{ad}_{[a,b]},
$$

so the map $\mathfrak{sl}_4\to\operatorname{Der}(M_4)$ is an isomorphism of Lie algebras. The derivations act on $M_4$ by the adjoint action, and the decomposition of $M_4$ under $\mathfrak{sl}_4$ is the adjoint decomposition $1+3+5+7$ under the principal $\mathfrak{sl}_2$.

**The biquaternion case.** For $M_2(\mathbb{C})$, the same theorem gives

$$
\operatorname{Der}(M_2)\cong\mathfrak{sl}_2(\mathbb{C}),
\qquad
\dim=3.
$$

The inner derivations are the adjoint action of $\mathfrak{sl}_2$ on $M_2$; the kernel is the centre $\mathbb{C}I$, and the image is $\mathfrak{sl}_2$. There are no outer derivations.

## The Automorphisms

**Definition.** An **automorphism** of $M_4$ is an invertible linear map $\Phi$ with

$$
\Phi(XY)=\Phi(X)\Phi(Y).
$$

The automorphisms form the group $\operatorname{Aut}(M_4)$.

**Theorem (Skolem–Noether).** Every automorphism of $M_4(\mathbb{C})$ is inner:

$$
\operatorname{Aut}(M_4)\cong PGL_4(\mathbb{C})=GL_4(\mathbb{C})/\mathbb{C}^\times I,
\qquad
\dim_\mathbb{C}=15.
$$

**Proof.** The automorphism sends the matrix units to a set of matrix units of the same type: a complete system of $4\times4$ matrix units. By the Skolem–Noether theorem for central simple algebras, any two complete systems of matrix units are conjugate by an invertible matrix. Hence $\Phi(X)=SXS^{-1}$ for some $S\in GL_4$, and the matrix $S$ is determined up to a scalar by the centre theorem. The group is $PGL_4$, of dimension $16-1=15$.

**The inner automorphisms.** The conjugation

$$
\Phi_S(X)=SXS^{-1}
$$

is an automorphism for every $S\in GL_4$. It preserves the trace, the determinant, the characteristic polynomial, the rank and the Jordan type. The kernel of $S\mapsto\Phi_S$ is the centre $\mathbb{C}^\times I$, so the automorphism group is $PGL_4$.

**There are no outer automorphisms.** For the complex algebra $M_4(\mathbb{C})$, the outer automorphism group is trivial. The "outer" operations that appear in the theory are not complex-linear automorphisms:

- the **transpose** $X\mapsto X^{\mathsf T}$ is an anti-automorphism, $\Phi(XY)=\Phi(Y)\Phi(X)$;
- the **conjugate transpose** $X\mapsto X^*$ is a conjugate-linear anti-automorphism;
- the **entrywise conjugation** $X\mapsto\bar X$ is a conjugate-linear automorphism.

These are real-linear or conjugate-linear maps, not elements of $\operatorname{Aut}_\mathbb{C}(M_4)$. The real algebra $M_4(\mathbb{C})$ has the conjugation as an automorphism of the real algebra, and the transpose as an anti-automorphism; they are "outer" only in the real sense.

**The Lie algebra.** The automorphism group $PGL_4$ has Lie algebra $\mathfrak{sl}_4$, and the adjoint action of the group on $M_4$ is the exponentiation of the adjoint action of the Lie algebra. The orbit of an element is its conjugacy class; the orbit classification is *The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$*.

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

The elementary corner maps are the matrix units of the space of corner maps; the general sandwich is a linear combination with coefficients $a_{ir}b_{sl}$.

**The inner automorphism.** For $b=a^{-1}$,

$$
T_{a,a^{-1}}(X)=aXa^{-1}
$$

is the inner automorphism $\Phi_a$. On the corners, it sends $A_{rs}$ to a linear combination of the corners $A_{il}$ with coefficients $a_{ir}(a^{-1})_{sl}$. The inner automorphism preserves the trace and the determinant but not the individual corners in general: it preserves each corner line exactly when $a$ is diagonal in the frame, and a permutation matrix permutes the spectral lines.

**The sandwich and the Peirce table.** The sandwich acts on the two-sided Peirce table of *The Rank-Two Split of $M_4(\mathbb{C})$* by transforming the row index with $a$ and the column index with $b$. For the rank-two split with $\Pi=P_+$, the sandwich with block-diagonal $a,b$ preserves the four corners; the sandwich with off-diagonal $a$ or $b$ mixes the corners. The mass block $\mathcal{B}$ is carried to the corner determined by the row of $a$ and the column of $b$.

## Summary

The four operators on $M_4$ are the left multiplication $L_a(X)=aX$, the right multiplication $R_a(X)=Xa$, the sandwich $T_{a,b}(X)=aXb$ and the adjoint $\operatorname{ad}_a(X)=[a,X]$. They satisfy $T_{a,b}=L_aR_b=R_bL_a$ and $\operatorname{ad}_a=L_a-R_a$. On the matrix units, $L_a$ moves the row index, $R_a$ moves the column index, $T_{a,b}$ moves both, and $\operatorname{ad}_a$ is the difference. The matrices are $L_a=a\otimes I$, $R_b=I\otimes b^{\mathsf T}$, $T_{a,b}=a\otimes b^{\mathsf T}$ and $\operatorname{ad}_a=a\otimes I-I\otimes a^{\mathsf T}$; the eigenvalues are the eigenvalues of $a$, of $b$, and the differences $\lambda_i-\lambda_j$. The derivations of $M_4$ are exactly the inner derivations, $\operatorname{Der}(M_4)\cong\mathfrak{sl}_4$, of dimension $15$; the automorphisms are exactly the inner automorphisms, $\operatorname{Aut}(M_4)\cong PGL_4$, of dimension $15$. There are no outer derivations and no complex-linear outer automorphisms; the transpose and the conjugations are anti-automorphisms or conjugate-linear maps. The sandwich is the corner map $A_{rs}\mapsto\sum a_{ir}b_{sl}A_{il}$; the elementary sandwich $T_{E_{ir},E_{sl}}$ carries the corner $A_{rs}$ to the corner $A_{il}$.

$$
\boxed{\ \operatorname{Der}(M_4)\cong\mathfrak{sl}_4,\ \dim=15;\qquad \operatorname{Aut}(M_4)\cong PGL_4,\ \dim=15;\qquad \operatorname{rank}\operatorname{ad}_a=16-\sum_i m_i^2. }
$$

| Operator | Matrix | Action on $E_{ij}$ | Trace |
|---|---|---|---|
| $L_a$ | $a\otimes I$ | row index by $a$ | $4\operatorname{tr}a$ |
| $R_b$ | $I\otimes b^{\mathsf T}$ | column index by $b$ | $4\operatorname{tr}b$ |
| $T_{a,b}$ | $a\otimes b^{\mathsf T}$ | both indices | $\operatorname{tr}a\operatorname{tr}b$ |
| $\operatorname{ad}_a$ | $a\otimes I-I\otimes a^{\mathsf T}$ | commutator | $0$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a$ | left multiplication $X\mapsto aX$ |
| $R_a$ | right multiplication $X\mapsto Xa$ |
| $T_{a,b}$ | sandwich $X\mapsto aXb$ |
| $\operatorname{ad}_a$ | adjoint $X\mapsto[a,X]$ |
| $\operatorname{Der}(M_4)$ | the derivation algebra, $\cong\mathfrak{sl}_4$ |
| $\operatorname{Aut}(M_4)$ | the automorphism group, $\cong PGL_4$ |
| $A_{ij}=\mathbb{C}E_{ij}$ | the Peirce corner $(i,j)$ |
| $Z(a)$ | the centraliser of $a$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for derivations, automorphisms and the Skolem–Noether theorem.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for central simple algebras and their automorphisms.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Kronecker product and the vectorisation of matrix equations.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the corners and the multiplication rule.
- [The Rank-Two Split of $M_4(\mathbb{C})$](the-rank-two-split-of-m4c.html), for the two-sided Peirce table.
- [The Numerical Range of the Two-Sided Operators of $M_4(\mathbb{C})$](the-numerical-range-of-the-two-sided-operators-of-m4c.html), for the field of values of $T_{a,b}$ and the product bound.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the conjugation action and its orbits.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the construction of the algebra from the sandwich map and the four-dimensional case.
- [$M_4(\mathbb{C})_{\mathbb{B},L}$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the same construction on the four-dimensional carrier.
