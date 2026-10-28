# __The Spin Chain and the Adjoint Decomposition__

## Introduction

The carrier of $M_5(\mathbb{C})$ is the five-dimensional space $V=\mathbb{C}^5$, and it carries the irreducible representation of $\mathfrak{sl}_2$ of highest weight $4$:

$$
V\cong\operatorname{Sym}^4(\mathbb{C}^2),\qquad \dim V=5,\qquad \text{spin }2 .
$$

In the weight basis $e_1,\dots,e_5$ the diagonal generator is $J_3=\operatorname{diag}(2,1,0,-1,-2)$, the raising generator is

$$
J_+=\sum_{k=1}^{4}\sqrt{k(5-k)}\,E_{k,k+1},
$$

with the ladder coefficients $2,\sqrt6,\sqrt6,2$, and $J_-=J_+^{\dagger}$. The triple satisfies the relations of $\mathfrak{sl}_2$, the Casimir is $6I=2(2+1)I$, and the representation is the spin-two module. The adjoint representation of the same triple on $\mathfrak{gl}_5$ decomposes as

$$
\mathfrak{gl}_5=V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4,
\qquad 1+3+5+7+9=25,
$$

and the traceless part $\mathfrak{sl}_5$ is $3+5+7+9=24$. This is the **adjoint decomposition** $1+3+5+7+9$.

The chain is read on the Peirce frame of *The Peirce Decomposition*: the idempotents $P_k=E_{kk}$ project onto the weight vectors, the simple nilpotents $E_{k,k+1}$ are the elementary steps of the chain, and the weights are the labels $2,1,0,-1,-2$. The four gauge parameters of *The Frame, the Simple Nilpotents and the Gauge* rescale the simple nilpotents and hence the ladder coefficients; in the orthonormal spectral gauge the coefficients are the positive numbers $2,\sqrt6,\sqrt6,2$.

The article assumes the matrix algebra, the root and the Peirce decomposition. It uses the trace form only to define the adjoint $J_+^{\dagger}$ and to identify the compact real form; the algebraic decomposition is independent of the form. The comparison with $n=2$ is the biquaternion case, where the carrier is the spinor; for $n=5$ there are no spinors, and the carrier is the symmetric power. The spin-two chain is developed explicitly in *The Spin-Two Chain and the Adjoint $1+3+5+7+9$*; the present article states the chain, the relations and the decomposition.

## The Carrier

### The Weight Basis

**Definition.** The **carrier** is $V=\mathbb{C}^5$ with the basis $e_1,\dots,e_5$. The **weight** of $e_k$ is

$$
m_k=3-k,
$$

so that the weights are $2,1,0,-1,-2$. The **diagonal generator** is

$$
J_3=\sum_{k=1}^{5}m_kE_{kk}=\operatorname{diag}(2,1,0,-1,-2).
$$

**Definition.** The **raising generator** is

$$
J_+=\sum_{k=1}^{4}c_kE_{k,k+1},\qquad c_k=\sqrt{k(5-k)},
$$

so that $J_+e_{k+1}=c_ke_k$ and $J_+e_1=0$. The **lowering generator** is $J_-=J_+^{\dagger}=J_+^{\mathsf T}$, so that $J_-e_k=c_ke_{k+1}$ for $k=1,\dots,4$ and $J_-e_5=0$.

The coefficients are

$$
c_1=2,\qquad c_2=\sqrt6,\qquad c_3=\sqrt6,\qquad c_4=2 .
$$

**Remark.** The choice of the square roots is the choice of a real positive normalization. A gauge transformation of *The Frame, the Simple Nilpotents and the Gauge* replaces $E_{k,k+1}$ by $\lambda_kE_{k,k+1}$ and hence $c_k$ by $\lambda_kc_k$; the four $\lambda_k$ are pure gauge. The normalized chain is the one in which the frame is orthonormal for the trace form and the coefficients are positive.

### The Matrices

In the basis $e_1,\dots,e_5$,

$$
J_3=\begin{pmatrix}
2&0&0&0&0\\
0&1&0&0&0\\
0&0&0&0&0\\
0&0&0&-1&0\\
0&0&0&0&-2
\end{pmatrix},
$$

$$
J_+=\begin{pmatrix}
0&2&0&0&0\\
0&0&\sqrt6&0&0\\
0&0&0&\sqrt6&0\\
0&0&0&0&2\\
0&0&0&0&0
\end{pmatrix},
\qquad
J_-=\begin{pmatrix}
0&0&0&0&0\\
2&0&0&0&0\\
0&\sqrt6&0&0&0\\
0&0&\sqrt6&0&0\\
0&0&0&2&0
\end{pmatrix}.
$$

The matrices are real, $J_3$ is Hermitian, $J_+$ is the transpose of $J_-$, and $J_+$ and $J_-$ are nilpotent of index $5$: $J_+^5=J_-^5=0$.

## The $\mathfrak{sl}_2$ Relations

### The Commutation Relations

**Theorem.** The triple $(J_3,J_+,J_-)$ satisfies

$$
[J_3,J_+]=J_+,\qquad [J_3,J_-]=-J_-,\qquad [J_+,J_-]=2J_3 .
$$

**Proof.** On the basis vector $e_{k+1}$ with $1\le k\le4$,

$$
J_3J_+e_{k+1}=c_kJ_3e_k=c_k(3-k)e_k,\qquad
J_+J_3e_{k+1}=c_k(2-k)e_k,
$$

because $J_3e_{k+1}=(2-k)e_{k+1}$ and $J_3e_k=(3-k)e_k$. The difference is $c_ke_k=J_+e_{k+1}$. The relation with $J_-$ is the transpose, or the same computation with the indices reversed. For the last relation, compute on $e_k$:

$$
J_+J_-e_k=c_k^2e_k,\qquad J_-J_+e_k=c_{k-1}^2e_k,
$$

with the conventions $c_0=c_5=0$. Hence

$$
[J_+,J_-]e_k=(c_k^2-c_{k-1}^2)e_k .
$$

The coefficients satisfy $c_k^2=k(5-k)$, so

$$
c_k^2-c_{k-1}^2=k(5-k)-(k-1)(6-k)=5k-k^2-(6k-6-k^2+k)=6-2k=2(3-k)=2m_k .
$$

The right-hand side is $2J_3e_k$. The three relations hold on the basis, hence everywhere.

### The Coefficients Are Forced

**Proposition.** The commutation relations force the ladder coefficients, up to signs: if $J_+e_{k+1}=c_ke_k$ and $J_-=J_+^{\mathsf T}$, then

$$
c_k^2-c_{k-1}^2=2(3-k),\qquad c_0=0,\qquad c_k^2=k(5-k).
$$

**Proof.** The relation $[J_+,J_-]=2J_3$ gives the recurrence $c_k^2-c_{k-1}^2=2(3-k)$. With $c_0=0$, the solution is the telescoping sum

$$
c_k^2=\sum_{j=1}^{k}2(3-j)=2\Bigl(3k-\frac{k(k+1)}{2}\Bigr)=k(5-k).
$$

The signs of the $c_k$ are fixed by the choice of the positive square roots; changing a sign is the gauge $\lambda_k=-1$ on the corresponding simple nilpotent.

**Corollary.** The coefficients are $2,\sqrt6,\sqrt6,2$. The top and bottom coefficients are $2$, the two central ones are $\sqrt6$; the symmetry $c_k=c_{5-k}$ is the symmetry of the weights $m_k=-m_{6-k}$.

### The Casimir

**Definition.** The **Casimir element** of the triple is

$$
C=J_3^2+\frac12(J_+J_-+J_-J_+).
$$

**Proposition.** On the carrier, $C=6I=2(2+1)I$.

**Proof.** The products are

$$
J_+J_-=\operatorname{diag}(4,6,6,4,0),\qquad
J_-J_+=\operatorname{diag}(0,4,6,6,4),
$$

so

$$
\tfrac12(J_+J_-+J_-J_+)=\operatorname{diag}(2,5,6,5,2),
$$

and $J_3^2=\operatorname{diag}(4,1,0,1,4)$. The sum is $\operatorname{diag}(6,6,6,6,6)$.

**Corollary.** The carrier is the irreducible module of highest weight $2$: the highest weight vector is $e_1$, of weight $2$ and annihilated by $J_+$; the Casimir eigenvalue is $j(j+1)=6$ with $j=2$; the dimension is $2j+1=5$.

**Proof.** $J_+e_1=0$ and $J_3e_1=2e_1$; the lowering operators $J_-^r e_1$ for $r=0,\dots,4$ are nonzero and independent (they have distinct weights), and $J_-^5e_1=0$; hence the module is the full $5$-dimensional space and is irreducible. The Casimir eigenvalue on an irreducible highest-weight module is $j(j+1)$.

**Remark.** **The triple $(J_3,J_+,J_-)$ generates $\mathfrak{sl}_2(\mathbb{C})$ over $\mathbb{C}$, and its compact real form $\mathfrak{su}_2$ is generated by $iJ_3$, $iJ_+$ and $iJ_-$ over $\mathbb{R}$.** The pair $(J_3,J_+)$ alone generates only the two-dimensional Borel subalgebra spanned by $J_3$ and $J_+$; the lowering generator is needed for the full three-dimensional algebra. The matrices $J_3,J_+,J_-$ are Hermitian (or real), not skew-Hermitian; the skew-Hermitian generators are their multiples by $i$. The compact group $SU(2)$ acts by $e^{itJ_3}$, $e^{it(J_++J_-)}$ and their products; the algebraic relations are those of the complexification.

## The Carrier as a Symmetric Power

### The Identification

Let $x,y$ be the standard basis of $\mathbb{C}^2$, and let $\operatorname{Sym}^4(\mathbb{C}^2)$ have the monomial basis $x^4,x^3y,x^2y^2,xy^3,y^4$. The Lie algebra $\mathfrak{sl}_2(\mathbb{C})$ acts by

$$
J_3=\frac12(x\partial_x-y\partial_y),\qquad J_+=x\partial_y,\qquad J_-=y\partial_x .
$$

**Theorem.** The map

$$
e_k\longmapsto\sqrt{\binom{4}{k-1}}\,x^{5-k}y^{k-1},\qquad k=1,\dots,5,
$$

is an isomorphism of $\mathfrak{sl}_2$-modules $V\cong\operatorname{Sym}^4(\mathbb{C}^2)$.

**Proof.** On the monomial $x^{4-j}y^j$, $J_3$ has eigenvalue $\frac12(4-j-j)=2-j$; with $j=k-1$ this is $3-k=m_k$, so the diagonal part matches. The raising operator acts by

$$
J_+\bigl(x^{4-j}y^j\bigr)=j\,x^{5-j}y^{j-1},
$$

so on the normalized basis

$$
J_+e_{j+1}=\sqrt{\binom{4}{j}}\,j\,\Bigl/\sqrt{\binom{4}{j-1}}\;e_j
=\sqrt{j(5-j)}\,e_j,
$$

which is the coefficient $c_j$. The lowering operator is the transpose. The map is injective on a basis and both spaces have dimension $5$. The highest weight vector $x^4=e_1$ has weight $2$ and is killed by $J_+$; the module is irreducible of highest weight $2$, hence spin $2$.

**Corollary.** The carrier is the symmetric fourth power of the two-dimensional module. The weights are the integers $2,1,0,-1,-2$; the module is self-dual under the invariant pairing of $\operatorname{Sym}^4$, and it has no half-integer weight.

**Proof.** The weights are the eigenvalues of $J_3$ on the basis; the self-duality is the apolar pairing $\operatorname{Sym}^4\otimes\operatorname{Sym}^4\to\mathbb{C}$, which is $\mathfrak{sl}_2$-invariant and nondegenerate. The weights are integers, so no spinorial (half-integer) weight occurs.

### The Ladder Coefficients

The coefficients $2,\sqrt6,\sqrt6,2$ are the matrix elements of the raising operator between normalized weight vectors. For a highest weight $j=2$ and a weight $m=3-k$, the coefficient of $J_+$ from the weight $m-1$ to the weight $m$ is

$$
c_k=\sqrt{(j-(m-1))(j+(m-1)+1)}=\sqrt{k(5-k)} .
$$

The clean invariant statement is the recurrence of §*The Coefficients Are Forced*: the coefficients are the positive square roots of $k(5-k)$, and they are symmetric, $c_k=c_{5-k}$, because the weights are symmetric. The square roots are the normalisation of the basis: in the monomial basis $x^{4-j}y^j$ the coefficients are $j$, with no square roots; the normalised basis multiplies by $\sqrt{\binom{4}{j}}$, and the square roots appear. The gauge of the frame rescales the coefficients, so the numbers $2,\sqrt6,\sqrt6,2$ are a gauge choice, not an invariant of the abstract module.

## The Peirce Chain and the Weights

### The Two Diagonal Structures

The root $H$ and the spin generator $J_3$ are both diagonal in the spectral frame. In this article the frame is indexed $1,\dots,5$, and the projector $P_k$ of *Roots of Unity and the Lagrange Idempotents* is attached to $\zeta_{k-1}$; with this relabelling,

$$
H=\sum_{k=1}^{5}\zeta_{k-1}P_k,\qquad J_3=\sum_{k=1}^{5}(3-k)E_{kk},
\qquad P_k=E_{kk}.
$$

They commute. They are different structures on the same carrier: $H$ has the five distinct eigenvalues $\zeta_{k-1}$, and $J_3$ has the five distinct integer weights $2,1,0,-1,-2$. The Peirce idempotents are the common eigenvectors, $P_ke_k=e_k$.

**Proposition.** The simple nilpotent $E_{k,k+1}$ is homogeneous of $\mathbb{Z}/5$-grade $-1$ and of $J_3$-weight $+1$:

$$
HE_{k,k+1}H^{-1}=\zeta^{-1}E_{k,k+1},\qquad
[J_3,E_{k,k+1}]=E_{k,k+1}.
$$

More generally, the Peirce line $A_{kl}=\mathbb{C}E_{kl}$ has grade $k-l$ and weight $l-k$; the grade and the weight are opposite integers.

**Proof.** The grade is $P_kP_l$: $HE_{kl}H^{-1}=\zeta_{k-1}\zeta_{l-1}^{-1}E_{kl}=\zeta^{k-l}E_{kl}$. The weight is $[J_3,E_{kl}]=(m_k-m_l)E_{kl}=(l-k)E_{kl}$. The two exponents are opposite.

**Corollary.** The raising operator $J_+$ lies in the grade $-1$ component $M^{(4)}$, the lowering operator $J_-$ in the grade $+1$ component $M^{(1)}$, and $J_3$ in the grade zero. The spin chain is **not** a grading by the same group as the root: $J_+$ shifts the weight by $+1$ and the grade by $-1$.

**Proof.** $J_+=\sum_kc_kE_{k,k+1}$ is a sum of lines of grade $-1$; $J_-$ of grade $+1$; $J_3$ is diagonal.

**Remark.** The five Peirce lines $A_{kk}=\mathbb{C}E_{kk}$ are the weight spaces of the carrier; the adjoint weight spaces are the sums of the lines with a fixed difference $l-k$. The weight $r$ adjoint space has dimension $5-|r|$, because there are $5-|r|$ pairs $(k,l)$ with $l-k=r$ in $\{1,\dots,5\}$.

### The Weights of the Adjoint

**Proposition.** On $\mathfrak{gl}_5$, the operator $\operatorname{ad}_{J_3}$ has the eigenvalue $r$ with multiplicity $5-|r|$ for $r=-4,\dots,4$:

$$
\dim\{A:[J_3,A]=rA\}=5-|r| .
$$

**Proof.** In the basis $E_{kl}$, $\operatorname{ad}_{J_3}E_{kl}=(m_k-m_l)E_{kl}=(l-k)E_{kl}$. For a fixed $r=l-k$, the pairs are $(k,k+r)$ with $1\le k,k+r\le5$, of which there are $5-|r|$.

**Corollary.** The weight multiplicities are $1,2,3,4,5,4,3,2,1$ for $r=-4,\dots,4$.

## The Adjoint Decomposition

### The Statement

**Theorem.** As a module over the triple $(J_3,J_+,J_-)$, the algebra $\mathfrak{gl}_5$ decomposes as

$$
\mathfrak{gl}_5\cong V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4,
$$

where $V_j$ is the irreducible module of highest weight $j$ and dimension $2j+1$. Hence

$$
\dim\mathfrak{gl}_5=1+3+5+7+9=25,
\qquad
\dim\mathfrak{sl}_5=3+5+7+9=24 .
$$

The summand $V_0$ is the line $\mathbb{C}I$ of scalar matrices; the traceless part is $\mathfrak{sl}_5$.

**Proof.** The adjoint representation is the $\mathfrak{sl}_2$-module $\operatorname{End}(V)\cong V\otimes V^*$. The carrier is self-dual, $V^*\cong V$, and $V\cong V_2$; the Clebsch–Gordan rule for $V_2\otimes V_2$ gives

$$
V_2\otimes V_2\cong V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4,
$$

with dimensions $1+3+5+7+9=25$. The scalar matrices are invariant under the adjoint action, so they form the trivial summand $V_0$; the quotient by them is $\mathfrak{sl}_5$, of dimension $24$, and its decomposition is the sum of the four nontrivial summands.

**Corollary.** The highest weights $0,1,2,3,4$ occur exactly once each: **one irreducible summand for each highest weight**. The adjoint module is multiplicity-free.

**Proof.** The Clebsch–Gordan decomposition of $V_2\otimes V_2$ has one summand for each $j$ from $0$ to $4$.

### The Weight Count

The decomposition is consistent with the weight multiplicities: the character of $V_j$ is $\sum_{m=-j}^{j}t^m$, so the character of the sum is

$$
\sum_{j=0}^{4}\sum_{m=-j}^{j}t^m
=\sum_{r=-4}^{4}(5-|r|)t^r,
$$

whose coefficient at $t^r$ is $5-|r|$, the multiplicity of §*The Weights of the Adjoint*.

**Proposition.** The weight multiplicities determine the decomposition: a finite-dimensional $\mathfrak{sl}_2$-module is semisimple, and its multiplicity of $V_j$ is the difference of the multiplicities of the weight $j$ and the weight $j+1$.

**Proof.** In a direct sum of highest-weight modules, the multiplicity of the weight $r$ is $\sum_{j\ge|r|}m_j$, where $m_j$ is the multiplicity of $V_j$. Subtracting consecutive weights gives $m_j=\dim\mathfrak{gl}_5^{(j)}-\dim\mathfrak{gl}_5^{(j+1)}$ for $j\ge0$, with the weight multiplicities above: $m_0=5-4=1$, $m_1=4-3=1$, $m_2=3-2=1$, $m_3=2-1=1$, $m_4=1-0=1$. All multiplicities are one.

**Remark.** **The decomposition $1+3+5+7+9$ is the decomposition of the adjoint, not of the carrier.** The carrier is the single module $V_2=5$. The adjoint is the tensor square of the carrier, and the five summands are the five ways of coupling two spin-two objects: the scalar, the vector, the spin two, the spin three and the spin four. The scalar is the identity; the traceless part is the Lie algebra $\mathfrak{sl}_5$.

### The Highest Weight Vectors

The highest weight vector of $V_4$ is $E_{15}$: it has weight $2-(-2)=4$ and is killed by $\operatorname{ad}_{J_+}$, because $J_+E_{15}=0$ (the first column of $J_+$ is zero) and $E_{15}J_+=0$ (the fifth row of $J_+$ is zero). The module $V_0$ is spanned by $I$.

**Proposition.** The cyclic submodule of $E_{15}$ under the triple is irreducible of highest weight $4$, hence is the summand $V_4$ of dimension $9$.

**Proof.** The vector $E_{15}$ is a highest weight vector: it is an eigenvector of $\operatorname{ad}_{J_3}$ of weight $4$ and is annihilated by $\operatorname{ad}_{J_+}$. The submodule it generates is therefore irreducible of highest weight $4$, by the standard highest-weight theory of $\mathfrak{sl}_2$; the irreducible module of highest weight $4$ has dimension $2\cdot4+1=9$. The summand $V_4$ of the Clebsch–Gordan decomposition has the same highest weight and dimension, so the two coincide.

**Remark.** The explicit highest weight vectors of the intermediate summands are not needed for the dimension count; the Clebsch–Gordan decomposition and the weight multiplicities fix the module. The reader who wants them may use the lowering operator and the orthogonality of the weight spaces.

## The Comparison with $n=2$

### The Biquaternion Case

For $n=2$ the carrier is $V=\mathbb{C}^2$, the spinor, of highest weight $\tfrac12$:

$$
J_3=\frac12\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
J_+=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
J_-=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
$$

The ladder coefficient is $1$; the Casimir is $\tfrac34I=\tfrac12(\tfrac12+1)I$. The adjoint of $\mathfrak{gl}_2$ decomposes as $1+3$, the scalar and the traceless part; the traceless part is the three-dimensional adjoint of $\mathfrak{su}_2$. The module $\mathbb{C}^2$ is spinorial: its weights are $\pm\tfrac12$, half-integers.

**Proof.** The matrices satisfy the same relations; the weights are $\pm\tfrac12$; the adjoint $V_{1/2}\otimes V_{1/2}=V_0\oplus V_1$ has dimensions $1+3$.

### The Odd Case

For $n=5$ the carrier is the spin-two module, of integer weights; the adjoint is $1+3+5+7+9$. The general pattern for $n=2j+1$ odd is

$$
\mathbb{C}^{2j+1}\cong\operatorname{Sym}^{2j}(\mathbb{C}^2),\qquad
\mathfrak{gl}_{2j+1}\cong\bigoplus_{r=0}^{2j}V_r,
\qquad
\dim\mathfrak{gl}_{2j+1}=\sum_{r=0}^{2j}(2r+1)=(2j+1)^2 .
$$

For $j=2$ this is $5=2\cdot2+1$, $1+3+5+7+9=25$. The formula is the odd case; the even case begins at $n=2$, where the carrier is the two-dimensional spinor of weight $\tfrac12$, not a symmetric power of $\mathbb{C}^2$ of odd degree, and the weights are half-integers.

**Proof.** The identification of the carrier with the symmetric power is the theorem of §*The Carrier as a Symmetric Power* for $j=2$; the general case is the same monomial computation. The adjoint decomposition is the Clebsch–Gordan square of the spin-$j$ module, whose summands are $V_0,\dots,V_{2j}$.

**Remark.** **There is no chirality at odd $n$.** The spin-two module is self-conjugate, its weights are symmetric under $m\mapsto-m$, and there is no pair of inequivalent half-spin modules. The word *chirality* belongs to the even case, where the spinor splits into two modules of opposite chirality. For $n=5$ the carrier is a single real (self-conjugate) module, and the adjoint is multiplicity-free.

## Summary

The carrier is $\mathbb{C}^5=\operatorname{Sym}^4(\mathbb{C}^2)$, of spin $2$, with the weight basis $e_1,\dots,e_5$, the diagonal $J_3=\operatorname{diag}(2,1,0,-1,-2)$, the raising operator $J_+=\sum_{k=1}^4\sqrt{k(5-k)}E_{k,k+1}$ and the lowering operator $J_-=J_+^{\dagger}$. The ladder coefficients are $2,\sqrt6,\sqrt6,2$; the triple satisfies the $\mathfrak{sl}_2$ relations; the Casimir is $6I$.

$$
\boxed{\ \mathbb{C}^5=\operatorname{Sym}^4(\mathbb{C}^2)\text{ is the spin-}2\text{ carrier, and }\mathfrak{gl}_5=V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4\text{ with }1+3+5+7+9=25.\ }
$$

The adjoint decomposition is multiplicity-free, one summand per highest weight $0,1,2,3,4$; the scalar summand is $\mathbb{C}I$, and the traceless part is $\mathfrak{sl}_5=3+5+7+9$, of dimension $24$. The weights of the adjoint are the differences $l-k$, with multiplicity $5-|r|$; the Peirce line $A_{kl}$ has grade $k-l$ and weight $l-k$. The chain is read on the Peirce frame; the gauge rescales the simple nilpotents and the ladder coefficients.

| Object | Value |
|---|---|
| Carrier | $\mathbb{C}^5=\operatorname{Sym}^4(\mathbb{C}^2)$ |
| Spin | $2$ |
| Weights | $2,1,0,-1,-2$ |
| Ladder coefficients | $2,\sqrt6,\sqrt6,2$ |
| Casimir | $6I=2(2+1)I$ |
| Adjoint of $\mathfrak{gl}_5$ | $1+3+5+7+9=25$ |
| Adjoint of $\mathfrak{sl}_5$ | $3+5+7+9=24$ |
| Weight multiplicities | $1,2,3,4,5,4,3,2,1$ |
| Spinors at $n=5$ | none; the carrier is the spin-two module |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\mathbb{C}^5$ | The carrier |
| $e_1,\dots,e_5$ | The weight basis, of weights $2,1,0,-1,-2$ |
| $J_3=\operatorname{diag}(2,1,0,-1,-2)$ | The diagonal (Cartan) generator |
| $J_+=\sum_{k=1}^4\sqrt{k(5-k)}E_{k,k+1}$ | The raising generator |
| $J_-=J_+^{\dagger}$ | The lowering generator |
| $c_k=\sqrt{k(5-k)}$ | The ladder coefficients $2,\sqrt6,\sqrt6,2$ |
| $C=J_3^2+\tfrac12(J_+J_-+J_-J_+)$ | The Casimir, equal to $6I$ on $V$ |
| $V_j$ | The irreducible $\mathfrak{sl}_2$-module of highest weight $j$, dimension $2j+1$ |
| $\mathfrak{gl}_5^{(r)}$ | The weight space of $\operatorname{ad}_{J_3}$ of weight $r$ |
| $A_{kl}$ | The Peirce line, of grade $k-l$ and weight $l-k$ |

## Further Reading

- Werner Greub, *Multilinear Algebra* (Springer, second edition, 1978), for the symmetric powers and the apolar pairing.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the Clebsch–Gordan decomposition, the highest-weight classification and the symmetric powers of $\mathbb{C}^2$.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the semisimplicity of finite-dimensional $\mathfrak{sl}_2$-modules, the Casimir element and the weight multiplicities.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, second edition, 2015), for the compact real form $\mathfrak{su}_2$ and the unitary generators $iJ_3,iJ_+,iJ_-$.
- [The Peirce Decomposition](the-peirce-decomposition-of-m5c.html), for the lines $A_{kl}$, the weight spaces and the multiplication rule.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m5c.html), for the gauge that rescales the simple nilpotents and the ladder coefficients.
- [The Spin-Two Chain and the Adjoint $1+3+5+7+9$](the-spin-two-chain-and-the-adjoint-of-m5c.html), for the explicit spin-two chain, the weights and the absence of chirality.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m5c.html), for the carrier as the simple module of $M_5(\mathbb{C})$ and for the distinction between the carrier and the Peirce lines.
