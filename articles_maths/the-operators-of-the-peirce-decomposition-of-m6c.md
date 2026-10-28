# __The Operators of the Peirce Decomposition__

## Introduction

The Peirce decomposition of $M_6(\mathbb{C})$ is described by four families of linear operators on the algebra:

$$
L_a(X)=aX,\qquad
R_a(X)=Xa,\qquad
T_{a,b}(X)=aXb,\qquad
\operatorname{ad}_a(X)=aX-Xa .
$$

They are the left and right multiplications, the sandwich, and the inner derivation. Each is a $36\times36$ matrix in the basis of matrix units, and each acts on the Peirce corners $A_{rs}$ by carrying them to corners determined by the Peirce labels of $a$ and $b$. The sandwich $T_{a,b}$ carries $A_{rs}$ to $A_{il}$ when $a\in A_{ij}$ and $b\in A_{kl}$ with $j=r$ and $s=k$.

The derivations of the algebra are the inner ones,

$$
\operatorname{Der}(M_6)=\mathfrak{sl}_6(\mathbb{C}),
\qquad
\dim=35,
$$

and the automorphisms are the inner ones,

$$
\operatorname{Aut}(M_6)=PGL_6(\mathbb{C}),
$$

with the transpose as an anti-automorphism and the transpose-inverse as the outer automorphism of the Lie algebra $\mathfrak{sl}_6$.

The article assumes the Peirce decomposition of *The Peirce Decomposition* and the tensor product of *The Modules and the Minimal Left Ideals*. It uses no form and no topology. The adjoint action and the orbits are *The Adjoint Action, the Orbits and the Flag Variety*; the derivations of the biquaternion algebra are *Biquaternion Automorphisms and Derivations*.

## The Multiplication Operators

### Left and Right Multiplication

**Definition.** For $a\in M_6(\mathbb{C})$,

$$
L_a:M_6\longrightarrow M_6,\quad X\longmapsto aX,
\qquad
R_a:M_6\longrightarrow M_6,\quad X\longmapsto Xa .
$$

**Theorem.** The maps $L_a$ and $R_a$ are linear, and

$$
L_aL_b=L_{ab},\qquad
R_aR_b=R_{ba},\qquad
L_aR_b=R_bL_a .
$$

**Proof.** $L_aL_b(X)=a(bX)=(ab)X$; $R_aR_b(X)=(Xb)a=X(ba)$; the left and right multiplications commute because $(aX)b=a(Xb)$.

**Corollary (the regular representation).** The map

$$
a\longmapsto L_a
$$

is an injective algebra homomorphism $M_6\to\operatorname{End}(M_6)\cong M_{36}$, and

$$
a\longmapsto R_a
$$

is an injective anti-homomorphism.

**Proof.** $L_a=0$ implies $a=L_a(I_6)=0$; the product rule is $L_aL_b=L_{ab}$. For $R$, the product rule is reversed.

**Theorem (the matrices).** With $\operatorname{vec}$ stacking the columns,

$$
L_a=I_6\otimes a,\qquad
R_a=a^{\mathsf T}\otimes I_6 .
$$

**Proof.** $\operatorname{vec}(aX)=(I_6\otimes a)\operatorname{vec}X$ and $\operatorname{vec}(Xa)=(a^{\mathsf T}\otimes I_6)\operatorname{vec}X$.

### The Sandwich

**Definition.** The **sandwich** is

$$
T_{a,b}=L_aR_b:M_6\longrightarrow M_6,\quad
X\longmapsto aXb .
$$

**Theorem.** The sandwiches compose by

$$
T_{a,b}T_{c,d}=T_{ac,db},
$$

and in the vectorised form

$$
T_{a,b}=b^{\mathsf T}\otimes a .
$$

**Proof.** $a(cXd)b=(ac)X(db)$; $\operatorname{vec}(aXb)=(b^{\mathsf T}\otimes a)\operatorname{vec}X$.

**Corollary (the sandwich monoid).** The set of sandwiches is a monoid under composition, with identity $T_{I_6,I_6}$; its group of units is

$$
(GL_6\times GL_6)/\mathbb{C}^\times,
$$

where the scalar acts diagonally.

**Proof.** $T_{a,b}$ is invertible iff $a$ and $b$ are invertible, with inverse $T_{a^{-1},b^{-1}}$. The pairs $(a,b)$ and $(\lambda a,\lambda^{-1}b)$ give the same sandwich, and this is the only ambiguity.

### The Inner Derivation

**Definition.** The **inner derivation** is

$$
\operatorname{ad}_a=L_a-R_a:M_6\longrightarrow M_6,\quad
X\longmapsto aX-Xa .
$$

**Theorem.** $\operatorname{ad}_a$ is a derivation:

$$
\operatorname{ad}_a(XY)=\operatorname{ad}_a(X)Y+X\operatorname{ad}_a(Y),
$$

and in the vectorised form

$$
\operatorname{ad}_a=I_6\otimes a-a^{\mathsf T}\otimes I_6 .
$$

**Proof.** $aXY-XYa=(aX-Xa)Y+X(aY-Ya)$. The matrix form is the difference of the matrices of $L_a$ and $R_a$.

**Corollary (the invariants).** The operators have

$$
\operatorname{tr}L_a=\operatorname{tr}R_a=6\operatorname{tr}a,
\qquad
\operatorname{tr}T_{a,b}=\operatorname{tr}(a)\operatorname{tr}(b),
\qquad
\operatorname{tr}\operatorname{ad}_a=0,
$$

and

$$
\det L_a=\det R_a=(\det a)^6,
\qquad
\det T_{a,b}=(\det a\det b)^6,
$$

and

$$
\operatorname{rank}L_a=6\operatorname{rank}a,
\qquad
\operatorname{rank}T_{a,b}=\operatorname{rank}(a)\operatorname{rank}(b),
\qquad
\operatorname{rank}\operatorname{ad}_a=36-\dim Z(a),
$$

where $Z(a)$ is the centralizer of $a$. The eigenvalues of $\operatorname{ad}_a$ are the differences $\lambda_i-\lambda_j$ of the eigenvalues of $a$.

**Proof.** The trace and determinant of a Kronecker product; the rank of $L_a$ is $6$ times the rank of $a$ because $X\mapsto aX$ has kernel of dimension $6\dim\ker a$; the kernel of $\operatorname{ad}_a$ is the centralizer. On the eigenbasis of $a$, $\operatorname{ad}_a(E_{ij})=(\lambda_i-\lambda_j)E_{ij}$.

**Corollary (the kernel).** $\operatorname{ad}_a=0$ if and only if $a$ is scalar.

**Proof.** $a$ commutes with every $X$ if and only if $a\in\mathbb{C}I_6$.

## The Action on the Peirce Corners

### The Corner Labels

Let $P_1,\dots,P_6$ be the Lagrange projectors and $A_{rs}=P_rM_6P_s$ the fine Peirce lines.

**Theorem.** For $a\in A_{ij}$ and $X\in A_{rs}$,

$$
aX\in A_{is}\ \text{if }j=r,\qquad
aX=0\ \text{otherwise}.
$$

For $b\in A_{kl}$ and $X\in A_{rs}$,

$$
Xb\in A_{rl}\ \text{if }s=k,\qquad
Xb=0\ \text{otherwise}.
$$

For the sandwich with $a\in A_{ij}$ and $b\in A_{kl}$,

$$
T_{a,b}(A_{rs})\subseteq A_{il}
\ \text{if }j=r\text{ and }s=k,\qquad
T_{a,b}(A_{rs})=0\ \text{otherwise}.
$$

**Proof.** The product $A_{ij}A_{rs}$ is contained in $\delta_{jr}A_{is}$ by the Peirce multiplication rule; the right multiplication is the same on the other side; the sandwich is the composition.

**Corollary (the corner matrix).** In the Peirce basis, $T_{a,b}$ has a single nonzero block, from the corner $A_{rs}$ to the corner $A_{il}$, whenever $a\in A_{ij}$, $b\in A_{kl}$ with $j=r$, $s=k$. All other blocks vanish.

**Proof.** The theorem gives the only nonzero corner map; the matrix is the corresponding block.

### The Peirce Operators

**Definition.** The **Peirce operators** are

$$
E_{rs}=L_{P_r}R_{P_s},
\qquad
E_{rs}(X)=P_rXP_s .
$$

**Theorem.** The Peirce operators are the corner projectors:

$$
E_{rs}^2=E_{rs},\qquad
E_{rs}E_{tu}=\delta_{st}E_{ru},\qquad
\sum_{r,s=1}^{6}E_{rs}=I_{36},
$$

and

$$
E_{rs}(M_6)=A_{rs},\qquad
\dim A_{rs}=1 .
$$

**Proof.** $P_r^2=P_r$, $P_rP_s=\delta_{rs}P_r$; the composition of the corner projections is the corner projection when the intermediate labels agree. The sum over all corners is the identity because the Peirce decomposition is direct and complete.

**Corollary (the left and right Peirce operators).** The operators $L_{P_r}$ and $R_{P_s}$ are the sums of the corner projectors in their row and column:

$$
L_{P_r}=\sum_{s=1}^{6}E_{rs},
\qquad
R_{P_s}=\sum_{r=1}^{6}E_{rs}.
$$

**Proof.** $P_rX=\sum_sP_rXP_s$ because $\sum_sP_s=I_6$; the same on the right.

**Corollary (the grading derivation).** The derivation $\operatorname{ad}_{P_r}$ acts on the corner $A_{st}$ by

$$
\operatorname{ad}_{P_r}(A_{st})=(\delta_{rs}-\delta_{rt})A_{st}.
$$

**Proof.** $P_rP_sP_t-P_sP_tP_r=(\delta_{rs}-\delta_{rt})P_sP_t$.

**Remark (the corner algebra).** The Peirce operators generate the commutative algebra of diagonal operators in the Peirce basis, of dimension $36$; the left and right multiplications generate the full endomorphism algebra $\operatorname{End}(M_6)\cong M_{36}$.

## The Derivations

### The Inner Derivations

**Theorem.** Every derivation of $M_6(\mathbb{C})$ is inner:

$$
\operatorname{Der}(M_6)=\{\operatorname{ad}_a:a\in M_6\}.
$$

**Proof.** This is the standard theorem that every derivation of a central simple algebra over a field is inner; $M_6(\mathbb{C})$ is central simple over $\mathbb{C}$. The inner derivations form the subspace $\{\operatorname{ad}_a\}$, isomorphic to $\mathfrak{gl}_6/\mathbb{C}I_6\cong\mathfrak{sl}_6$, of dimension $35$; the theorem says that this subspace is all of $\operatorname{Der}(M_6)$.

**Theorem.** The map

$$
\mathfrak{sl}_6(\mathbb{C})\longrightarrow\operatorname{Der}(M_6),
\qquad
a\longmapsto\operatorname{ad}_a,
$$

is an isomorphism of Lie algebras, and

$$
\dim\operatorname{Der}(M_6)=35 .
$$

**Proof.** $\operatorname{ad}_{[a,b]}=[\operatorname{ad}_a,\operatorname{ad}_b]$; the kernel is the scalars, which are exactly the traceless condition after removing the center: $\operatorname{ad}_a=0$ iff $a\in\mathbb{C}I_6$, and the traceless part is the complement. The dimension is $36-1=35$.

**Corollary (the exact sequence).**

$$
0\longrightarrow\mathbb{C}I_6\longrightarrow\mathfrak{gl}_6
\overset{\operatorname{ad}}{\longrightarrow}\operatorname{Der}(M_6)\longrightarrow0
$$

is exact, and $\operatorname{Der}(M_6)\cong\mathfrak{sl}_6$.

**Proof.** The kernel of ad is the center $\mathbb{C}I_6$; the image is all derivations; the quotient $\mathfrak{gl}_6/\mathbb{C}I_6\cong\mathfrak{sl}_6$.

### The Derivations of the Peirce Algebra

**Theorem.** The derivation $\operatorname{ad}_{P_r}$ has eigenvalues $0,\pm1$ on the Peirce corners, and the derivations $\operatorname{ad}_{P_1},\dots,\operatorname{ad}_{P_5}$ span the Cartan subalgebra of the diagonal torus of $\mathfrak{sl}_6$.

**Proof.** The corner $A_{st}$ is an eigenline with eigenvalue $\delta_{rs}-\delta_{rt}$; the five independent differences span the diagonal traceless matrices.

**Corollary (the Peirce grading).** The $\mathbb{Z}^6$-grading by the labels is the joint eigenspace decomposition of the commuting derivations $\operatorname{ad}_{P_1},\dots,\operatorname{ad}_{P_6}$; the corner $A_{st}$ has weight $e_s-e_t$.

**Proof.** The derivations commute because the $P_r$ commute; the eigenvalues are the differences of the basis vectors.

## The Automorphisms

### The Inner Automorphisms

**Theorem (Skolem–Noether).** Every automorphism of $M_6(\mathbb{C})$ is inner:

$$
\operatorname{Aut}(M_6)\cong PGL_6(\mathbb{C}),
\qquad
\Phi_a(X)=aXa^{-1}.
$$

**Proof.** The algebra is a central simple algebra; an automorphism sends the minimal left ideal $M_6P$ to another minimal left ideal, and the induced map is implemented by an invertible matrix, unique up to the center. The center acts trivially, giving the projective quotient.

**Corollary (the dimension).** $\dim PGL_6=35$, and the inner automorphism group is the adjoint group of $\mathfrak{sl}_6$.

**Proof.** $GL_6$ has dimension $36$; the center is one-dimensional; the quotient has dimension $35$. The Lie algebra of $PGL_6$ is $\mathfrak{sl}_6$.

### The Outer Automorphisms

**Theorem.** The transpose

$$
X\longmapsto X^{\mathsf T}
$$

is an anti-automorphism of $M_6(\mathbb{C})$, not an automorphism; it is not inner.

**Proof.** $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$, so the order is reversed. An inner automorphism $\Phi_a$ preserves products, $\Phi_a(XY)=\Phi_a(X)\Phi_a(Y)$; the transpose reverses them, so it is not an automorphism and hence not inner. It is an anti-automorphism.

**Theorem (the automorphisms of the Lie algebra).** For $n=6$,

$$
\operatorname{Aut}(\mathfrak{sl}_6)=PGL_6\rtimes\mathbb{Z}/2,
$$

where the nontrivial coset is represented by the **outer automorphism**

$$
X\longmapsto-X^{\mathsf T}.
$$

**Proof.** The automorphism group of the Dynkin diagram $A_5$ is $\mathbb{Z}/2$; the corresponding outer automorphism is the negative transpose. It preserves the bracket:

$$
[-X^{\mathsf T},-Y^{\mathsf T}]
=X^{\mathsf T}Y^{\mathsf T}-Y^{\mathsf T}X^{\mathsf T}
=(YX-XY)^{\mathsf T}
=-[X,Y]^{\mathsf T},
$$

so $X\mapsto-X^{\mathsf T}$ is a Lie algebra automorphism. It is not inner for $n\ge3$.

**Corollary (the two kinds).** The inner automorphisms are the conjugations $\Phi_a$; the outer one is the negative transpose. The associative algebra has only the inner automorphisms; the Lie algebra has the extra outer involution.

**Proof.** The first statement is Skolem–Noether; the second is the Dynkin diagram symmetry.

## The Sandwich as a Map of Corners

### The Corner Map

**Theorem.** The sandwich $T_{a,b}$ restricts to a linear map

$$
T_{a,b}:A_{rs}\longrightarrow A_{il},
\qquad
a\in A_{ij},\quad b\in A_{kl},\quad j=r,\quad s=k,
$$

and to zero on all other corners. In the Peirce basis it is the single block

$$
A_{rs}\longrightarrow A_{il},
\qquad
X\longmapsto aXb .
$$

**Proof.** This is the corner action of the theorem above.

**Corollary (the corner multiplication).** The sandwich gives the multiplication map

$$
A_{ij}\times A_{kl}\longrightarrow\operatorname{Hom}(A_{rs},A_{il}),
\qquad
(a,b)\longmapsto T_{a,b},
$$

with $j=r$, $s=k$. In the rank-one case all four corners are one-dimensional, and the sandwich is a scalar.

**Proof.** The domain of $T_{a,b}$ is $A_{rs}$; the target is $A_{il}$; the map is bilinear in $(a,b)$.

### The Sandwich Matrix

**Theorem.** In the basis of matrix units $E_{rs}$,

$$
T_{a,b}(E_{rs})=aE_{rs}b=\sum_{i,l}a_{ir}b_{sl}\,E_{il},
$$

so the matrix of $T_{a,b}$ has entries

$$
(T_{a,b})_{(il),(rs)}=a_{ir}b_{sl}.
$$

**Proof.** Expand $a$ and $b$ in the matrix units:

$$
aE_{rs}b
=\sum_{ijkl}a_{ij}b_{kl}E_{ij}E_{rs}E_{kl}
=\sum_{ijkl}a_{ij}b_{kl}\delta_{jr}\delta_{sk}E_{il}
=a_{ir}b_{sl}E_{il}.
$$

Hence the entry in the $(il),(rs)$ position is $a_{ir}b_{sl}$.

**Corollary (the rank).** $\operatorname{rank}T_{a,b}=\operatorname{rank}(a)\operatorname{rank}(b)$.

**Proof.** $T_{a,b}=b^{\mathsf T}\otimes a$; the rank of a Kronecker product is the product of the ranks.

**Corollary (the invertible sandwiches).** $T_{a,b}$ is invertible iff $a$ and $b$ are invertible; the group of invertible sandwiches is $(GL_6\times GL_6)/\mathbb{C}^\times$.

**Proof.** The Kronecker product is invertible iff both factors are; the scalar ambiguity is the diagonal.

### The Sandwich Monoid

**Theorem.** The map

$$
M_6\times M_6\longrightarrow\operatorname{End}(M_6),
\qquad
(a,b)\longmapsto T_{a,b},
$$

is a monoid homomorphism with kernel the diagonal scalars, and its image is the proper submonoid of the decomposable operators.

**Proof.** The composition law $T_{a,b}T_{c,d}=T_{ac,db}$; the pairs $(a,b)$ and $(\lambda a,\lambda^{-1}b)$ give the same sandwich. The image is not all of $\operatorname{End}(M_6)$: the sum of two decomposable operators need not be decomposable.

**Remark (the corner reading).** The sandwich is the only operator that sees two Peirce labels at once: $L_a$ sees the left label, $R_b$ the right label, and $T_{a,b}$ the pair. **The sandwich is the corner map of the Peirce decomposition.**

## Summary

The four operator families are

$$
L_a(X)=aX,\qquad
R_a(X)=Xa,\qquad
T_{a,b}(X)=aXb,\qquad
\operatorname{ad}_a(X)=aX-Xa,
$$

with matrices

$$
L_a=I_6\otimes a,\qquad
R_a=a^{\mathsf T}\otimes I_6,\qquad
T_{a,b}=b^{\mathsf T}\otimes a,\qquad
\operatorname{ad}_a=I_6\otimes a-a^{\mathsf T}\otimes I_6 .
$$

On the Peirce corners, $L_a$ carries $A_{rs}$ to $A_{is}$ when $a\in A_{ij}$ with $j=r$; $R_b$ carries $A_{rs}$ to $A_{rl}$ when $b\in A_{kl}$ with $s=k$; and $T_{a,b}$ carries $A_{rs}$ to $A_{il}$ when $a\in A_{ij}$, $b\in A_{kl}$ with $j=r$, $s=k$.

$$
\boxed{\ T_{a,b}:A_{rs}\to A_{il},\qquad \operatorname{Der}(M_6)=\mathfrak{sl}_6,\qquad \operatorname{Aut}(M_6)=PGL_6 .\ }
$$

The derivations are the inner ones $\operatorname{ad}_a$, with kernel the scalars and image $\mathfrak{sl}_6$, of dimension $35$. The automorphisms are the inner conjugations $PGL_6$; the transpose is an anti-automorphism, and the negative transpose is the outer automorphism of the Lie algebra $\mathfrak{sl}_6$.

| Operator | Matrix | Corner action |
|---|---|---|
| $L_a$ | $I_6\otimes a$ | $A_{rs}\to A_{is}$ if $a\in A_{ij}$, $j=r$ |
| $R_b$ | $b^{\mathsf T}\otimes I_6$ | $A_{rs}\to A_{rl}$ if $b\in A_{kl}$, $s=k$ |
| $T_{a,b}$ | $b^{\mathsf T}\otimes a$ | $A_{rs}\to A_{il}$ if $a\in A_{ij}$, $b\in A_{kl}$, $j=r$, $s=k$ |
| $\operatorname{ad}_a$ | $I_6\otimes a-a^{\mathsf T}\otimes I_6$ | $\lambda_s-\lambda_t$ on $A_{st}$ for diagonal $a=\sum_k\lambda_kE_{kk}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a$ | left multiplication $X\mapsto aX$ |
| $R_a$ | right multiplication $X\mapsto Xa$ |
| $T_{a,b}$ | sandwich $X\mapsto aXb$ |
| $\operatorname{ad}_a$ | inner derivation $X\mapsto aX-Xa$ |
| $E_{rs}=L_{P_r}R_{P_s}$ | Peirce corner projector |
| $\operatorname{Der}(M_6)$ | the derivations, isomorphic to $\mathfrak{sl}_6$ |
| $\operatorname{Aut}(M_6)$ | the automorphisms, isomorphic to $PGL_6$ |
| $\Phi_a$ | the inner automorphism $X\mapsto aXa^{-1}$ |

## Further Reading

- [The Peirce Decomposition](the-peirce-decomposition-of-m6c.html), for the corners and the multiplication rule.
- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the derivations and the automorphisms.
- [The Adjoint Action, the Orbits and the Flag Variety](the-adjoint-action-the-orbits-and-the-flag-variety-of-m6c.html), for the inner automorphisms as a group action.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the left and right regular modules.
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the rank-one case.
