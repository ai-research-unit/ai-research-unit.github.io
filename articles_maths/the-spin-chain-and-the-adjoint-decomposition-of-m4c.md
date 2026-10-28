# __The Spin Chain and the Adjoint Decomposition of $M_4(\mathbb{C})$__

## Introduction

**The carrier of the category $M_4(\mathbb{C})$ is $\mathbb{C}^4=\operatorname{Sym}^3(\mathbb{C}^2)$, the spin-$\tfrac32$ module of $\mathfrak{sl}_2(\mathbb{C})$, and the adjoint representation of that $\mathfrak{sl}_2$ on the algebra decomposes as $1+3+5+7$.** The chain of simple nilpotents $E_{12},E_{23},E_{34}$ is the weight chain of the carrier, and the coefficients of the ladder operators are $\sqrt3,2,\sqrt3$. The decomposition is the Clebsch–Gordan decomposition of $\mathbb{C}^4\otimes(\mathbb{C}^4)^*$.

The article defines the three generators $J_3,J_+,J_-$, proves the commutation relations and the ladder coefficients, identifies the carrier with the symmetric cube, computes the weights of the sixteen matrix units, and decomposes the adjoint representation into four irreducible modules with highest weight vectors $E_{14}$, $E_{13}+E_{24}$, $J_+$ and $I$. It also states precisely how the Peirce chain mixes the two chiralities, and how it differs from the chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*.

The root and the idempotents are *Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$*; the Peirce lines are *The Peirce Decomposition of $M_4(\mathbb{C})$*; the frame and the simple nilpotents are *The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$*; the chirality is *The Two Chiralities of $M_4(\mathbb{C})$*. The representation theory of $\mathfrak{sl}_2$ is *Representations of Lie Algebras*.

## The Carrier and the Generators

**Definition.** On $\mathbb{C}^4$ with the standard basis $e_1,e_2,e_3,e_4$, define

$$
J_3=\operatorname{diag}\left(\frac32,\frac12,-\frac12,-\frac32\right),
$$

$$
J_+=\sqrt3\,E_{12}+2\,E_{23}+\sqrt3\,E_{34},
$$

$$
J_-=J_+^{\mathsf T}=\sqrt3\,E_{21}+2\,E_{32}+\sqrt3\,E_{43}.
$$

The matrices are

$$
J_3=\begin{pmatrix}\frac32&0&0&0\\0&\frac12&0&0\\0&0&-\frac12&0\\0&0&0&-\frac32\end{pmatrix},
\quad
J_+=\begin{pmatrix}0&\sqrt3&0&0\\0&0&2&0\\0&0&0&\sqrt3\\0&0&0&0\end{pmatrix},
\quad
J_-=\begin{pmatrix}0&0&0&0\\\sqrt3&0&0&0\\0&2&0&0\\0&0&\sqrt3&0\end{pmatrix}.
$$

**Proposition.** The three matrices satisfy

$$
[J_3,J_+]=J_+,\qquad [J_3,J_-]=-J_-,\qquad [J_+,J_-]=2J_3.
$$

**Proof.** On the matrix units, $[J_3,E_{ij}]=(m_i-m_j)E_{ij}$ with $m=(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$. The only nonzero terms of $J_+$ are $E_{12},E_{23},E_{34}$, each of weight $1$; hence $[J_3,J_+]=J_+$. The same computation with $E_{k+1,k}$ gives $[J_3,J_-]=-J_-$. For the last relation, compute the commutator of the two sums term by term. The only nonzero products are

$$
[E_{12},E_{21}]=E_{11}-E_{22},\qquad
[E_{23},E_{32}]=E_{22}-E_{33},\qquad
[E_{34},E_{43}]=E_{33}-E_{44},
$$

and the cross terms vanish because the inner indices do not match. Hence

$$
[J_+,J_-]=3(E_{11}-E_{22})+4(E_{22}-E_{33})+3(E_{33}-E_{44})
=3E_{11}+E_{22}-E_{33}-3E_{44}=2J_3.
$$

**The Hermitian generators.** Put

$$
J_1=\frac{J_++J_-}{2},\qquad J_2=\frac{J_+-J_-}{2i}.
$$

Then $J_1,J_2,J_3$ are Hermitian, and the relations become

$$
[J_1,J_2]=iJ_3,\qquad [J_2,J_3]=iJ_1,\qquad [J_3,J_1]=iJ_2 .
$$

**Proof.** $J_+^{\mathsf T}=J_-$, so $J_1$ is real symmetric and $J_2$ is real skew-symmetric divided by $i$, hence Hermitian. The commutators follow from the three relations above by taking real and imaginary parts. The complex span of $J_1,J_2,J_3$ is the three-dimensional Lie algebra $\mathfrak{sl}_2(\mathbb{C})$.

**The representation is $*$-unitary.** The generators $J_1,J_2,J_3$ are Hermitian, so the one-parameter groups $e^{itJ_a}$ are $*$-unitary and the representation of $SU(2)$ on $\mathbb{C}^4$ is $*$-unitary. The weights of $J_3$ are real, as they must be.

## The Weights and the Ladder

**Definition.** A vector $v$ has **weight** $m$ if $J_3v=mv$. The **ladder** is the chain

$$
e_1\ \xrightarrow{\ J_-\ } \ e_2\ \xrightarrow{\ J_-\ } \ e_3\ \xrightarrow{\ J_-\ } \ e_4,
$$

with the raising operators acting in the reverse direction.

**Proposition.** The standard basis vectors are weight vectors:

$$
J_3e_1=\frac32e_1,\quad
J_3e_2=\frac12e_2,\quad
J_3e_3=-\frac12e_3,\quad
J_3e_4=-\frac32e_4.
$$

The ladder acts by

$$
J_+e_1=0,\qquad J_+e_2=\sqrt3\,e_1,\qquad J_+e_3=2\,e_2,\qquad J_+e_4=\sqrt3\,e_3,
$$

$$
J_-e_1=\sqrt3\,e_2,\qquad J_-e_2=2\,e_3,\qquad J_-e_3=\sqrt3\,e_4,\qquad J_-e_4=0.
$$

**Proof.** These are the entries of the matrices $J_\pm$. The coefficient of $J_+e_{k+1}$ is $\sqrt{k(4-k)}$ for $k=1,2,3$: $\sqrt3$, $\sqrt{4}=2$, $\sqrt3$. The same coefficients occur in the lowering direction because $J_-=J_+^{\mathsf T}$.

**The coefficients are the standard spin-$\tfrac32$ ladder coefficients.** For $J_+e_{k+1}$ the weight is $m=\tfrac32-k$ and the spin is $j=\tfrac32$, and the standard coefficient is

$$
\sqrt{(j-m)(j+m+1)}=\sqrt{k(4-k)}.
$$

The three values are $\sqrt3,2,\sqrt3$. They are not all equal: the chain is not the unweighted shift of the simple nilpotents. The simple nilpotents $E_{12},E_{23},E_{34}$ are the steps of the chain with coefficient $1$; the ladder operators of the spin structure are the weighted sums with coefficients $\sqrt3,2,\sqrt3$. The two structures are different: the nilpotents are the Peirce chain, the ladder is the spin chain. The article *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$* develops the comparison.

### Irreducibility

**Theorem.** The representation of $\mathfrak{sl}_2$ on $\mathbb{C}^4$ is irreducible.

**Proof.** Let $W\subseteq\mathbb{C}^4$ be a nonzero invariant subspace. Because $J_3$ is diagonalizable on $W$, the space $W$ contains a weight vector. Let $m$ be the maximal weight occurring in $W$, and let $w\ne0$ be a vector of weight $m$. If $m<\tfrac32$, then $J_+w$ is a nonzero vector of weight $m+1$ in $W$ (the ladder coefficients are nonzero for $m<\tfrac32$), contradicting maximality. Hence $m=\tfrac32$, and $w$ is a multiple of $e_1$. Applying $J_-$ repeatedly gives nonzero multiples of $e_2,e_3,e_4$, so $W=\mathbb{C}^4$. The representation is irreducible.

**Corollary.** The carrier is the unique irreducible representation of dimension $4$, namely the spin-$\tfrac32$ module. Every nonzero vector generates it.

## The Symmetric Cube

**Theorem.** The carrier is isomorphic to $\operatorname{Sym}^3(\mathbb{C}^2)$.

**Proof.** Let $x,y$ be a basis of $\mathbb{C}^2$, and let $\mathfrak{sl}_2$ act on homogeneous polynomials of degree $3$ by

$$
J_3=\frac12\left(x\frac{\partial}{\partial x}-y\frac{\partial}{\partial y}\right),\qquad
J_+=x\frac{\partial}{\partial y},\qquad
J_-=y\frac{\partial}{\partial x}.
$$

The monomials

$$
e_1=x^3,\qquad e_2=\sqrt3\,x^2y,\qquad e_3=\sqrt3\,xy^2,\qquad e_4=y^3
$$

are a basis of $\operatorname{Sym}^3(\mathbb{C}^2)$, and the action is

$$
J_3e_1=\frac32e_1,\quad J_3e_2=\frac12e_2,\quad J_3e_3=-\frac12e_3,\quad J_3e_4=-\frac32e_4,
$$

$$
J_+e_2=\sqrt3\,e_1,\quad J_+e_3=2\,e_2,\quad J_+e_4=\sqrt3\,e_3,
$$

which is the action of §*The Weights and the Ladder*. The two representations have the same dimension and the same ladder, so they are isomorphic.

**The normalization.** The factor $\sqrt3$ on $x^2y$ and $xy^2$ is the normalization that makes $J_+$ and $J_-$ transpose to each other. Without it, the ladder coefficients would be $1,2,3$ in the raising direction and $3,2,1$ in the lowering direction; the symmetric normalization is the one in which the two directions have the same coefficients and the representation is self-dual.

**The general pattern.** For $M_n(\mathbb{C})$ the carrier is $\mathbb{C}^n=\operatorname{Sym}^{n-1}(\mathbb{C}^2)$, the spin-$\frac{n-1}{2}$ module. For $n=4$ the spin is $\tfrac32$; for $n=2$ it is $\tfrac12$; for $n=3$ it is $1$. The dimension of the spin-$s$ module is $2s+1=n$. This is the reason the carrier dimension and the matrix size agree.

## The Adjoint Representation

**Definition.** The **adjoint representation** of $\mathfrak{sl}_2$ on $M_4(\mathbb{C})$ is

$$
\operatorname{ad}_{J_a}(X)=[J_a,X],\qquad a=1,2,3.
$$

The weights of $\operatorname{ad}_{J_3}$ are the differences of the weights of the carrier: for the matrix unit $E_{ij}$,

$$
\operatorname{ad}_{J_3}(E_{ij})=(m_i-m_j)E_{ij}.
$$

**The weight table.** The weights of the sixteen matrix units are

| $i\backslash j$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|
| $1$ | $0$ | $1$ | $2$ | $3$ |
| $2$ | $-1$ | $0$ | $1$ | $2$ |
| $3$ | $-2$ | $-1$ | $0$ | $1$ |
| $4$ | $-3$ | $-2$ | $-1$ | $0$ |

The multiplicity of the weight $m$ is the number of pairs $(i,j)$ with $m_i-m_j=m$:

| $m$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| multiplicity | $1$ | $2$ | $3$ | $4$ | $3$ | $2$ | $1$ |

**Theorem.** The adjoint representation decomposes as

$$
M_4(\mathbb{C})=\mathcal{V}_0\oplus\mathcal{V}_1\oplus\mathcal{V}_2\oplus\mathcal{V}_3,
$$

where $\mathcal{V}_k$ is the irreducible representation of spin $k$, of dimension $2k+1$. The dimensions are

$$
1+3+5+7=16.
$$

The highest weight vectors are

$$
w_3=E_{14}\quad(\text{weight }3),\qquad
w_2=E_{13}+E_{24}\quad(\text{weight }2),
$$

$$
w_1=J_+\quad(\text{weight }1),\qquad
w_0=I\quad(\text{weight }0).
$$

Each is killed by $\operatorname{ad}_{J_+}$, and the cyclic module generated by $w_k$ under $\operatorname{ad}_{J_-}$ is $\mathcal{V}_k$.

**Proof.** The weights and multiplicities of the right-hand side are those of the left-hand side. The irreducible spin-$k$ module has weights $-k,-k+1,\dots,k$, each with multiplicity one, so the sum $\mathcal{V}_0\oplus\cdots\oplus\mathcal{V}_3$ has multiplicity $4$ at weight $0$, $3$ at weights $\pm1$, $2$ at weights $\pm2$, and $1$ at weights $\pm3$, exactly the table above. The four vectors $w_k$ have the indicated weights, and a direct computation gives

$$
\operatorname{ad}_{J_+}(E_{14})=0,\qquad
\operatorname{ad}_{J_+}(E_{13}+E_{24})=0,
$$

$$
\operatorname{ad}_{J_+}(J_+)=0,\qquad
\operatorname{ad}_{J_+}(I)=0.
$$

For example, $\operatorname{ad}_{J_+}(E_{14})=J_+E_{14}-E_{14}J_+=(J_+e_1)e_4^{\mathsf T}-e_1(J_+^{\mathsf T}e_4)^{\mathsf T}$; the first term is $0$ because $J_+e_1=0$, and the second is $0$ because $J_+^{\mathsf T}e_4=J_-e_4=0$. For the sum,
$$
\operatorname{ad}_{J_+}(E_{13})=-\sqrt3\,E_{14},\qquad
\operatorname{ad}_{J_+}(E_{24})=\sqrt3\,E_{14},
$$
so the two terms cancel. The remaining two are immediate: $[J_+,J_+]=0$ and $[J_+,I]=0$. The lowering chain from $w_k$ has nonzero coefficients (the ladder coefficients are nonzero), so the cyclic module has dimension $2k+1$. The four cyclic modules are independent because their highest weights are distinct; the dimension count $7+5+3+1=16$ shows that they span the algebra.

**The adjoint of $\mathfrak{sl}_4$.** The centre $\mathbb{C}I$ is the module $\mathcal{V}_0$. The adjoint representation of $\mathfrak{sl}_4(\mathbb{C})$ is the traceless part,

$$
\mathfrak{sl}_4(\mathbb{C})=\mathcal{V}_1\oplus\mathcal{V}_2\oplus\mathcal{V}_3,
\qquad 3+5+7=15,
$$

and the full algebra adds the centre:

$$
M_4(\mathbb{C})=\mathfrak{sl}_4(\mathbb{C})\oplus\mathbb{C}I.
$$

**The highest weight vectors in the Peirce table.** The vector $w_3=E_{14}$ is the corner $\mathcal{A}_{14}$, of weight $3$. The vector $w_2=E_{13}+E_{24}$ is the sum of the two corners of weight $2$. The vector $w_1=J_+$ is the sum of the three simple nilpotents with coefficients $\sqrt3,2,\sqrt3$. The vector $w_0=I$ is the sum of the four diagonal corners. The four highest weight vectors are therefore explicit elements of the Peirce decomposition, but the modules they generate are not corners: they are seven-, five-, three- and one-dimensional subspaces, and the adjoint module is not a Peirce line.

## The Chain and the Chirality

**The Peirce chain is the weight chain.** The simple nilpotents

$$
E_{12},\quad E_{23},\quad E_{34}
$$

have weights $+1,+1,+1$; the composites

$$
E_{13}=E_{12}E_{23},\quad E_{24}=E_{23}E_{34},\quad E_{14}=E_{12}E_{23}E_{34}
$$

have weights $+2,+2,+3$. The chain of maps

$$
V_4\longrightarrow V_3\longrightarrow V_2\longrightarrow V_1
$$

is the chain of the flag, read from the lowest weight line to the highest. The raising operator $J_+$ is the sum of the three steps with coefficients $\sqrt3,2,\sqrt3$; the lowering operator is the transpose.

**The chain mixes chirality.** The chirality involution is

$$
\Gamma=H^2=\operatorname{diag}(1,-1,1,-1).
$$

The Cartan generator $J_3=\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$ commutes with $\Gamma$, because both are diagonal. The raising and lowering operators do not:

$$
J_+e_2=\sqrt3\,e_1,\qquad J_+e_4=\sqrt3\,e_3,
$$

and $e_2,e_4$ have chirality $-1$ while $e_1,e_3$ have chirality $+1$. The operator $J_+$ changes the chirality; $J_-$ changes it back. The carrier is irreducible under the Peirce $\mathfrak{sl}_2$, so there is no proper invariant subspace that is one chirality. The chain is a spin-$\tfrac32$ chain that runs through both chiralities, not a pair of independent spin-$\tfrac12$ chains.

**The chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ is different.** The traceless block-diagonal subalgebra that commutes with $\Gamma$ is $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ acting on the two planes $\mathbb{C}^2_+$ and $\mathbb{C}^2_-$. It is six-dimensional, and each chirality is a spin-$\tfrac12$ module for one of its two factors. The full centraliser of $\Gamma$ in $\mathfrak{sl}_4$ is spanned by this algebra and $\Gamma$, of dimension $7$; the chiral algebra is the six-dimensional traceless part. The Peirce $\mathfrak{sl}_2$ is three-dimensional and irreducible; it is not contained in the chiral $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, because its raising and lowering operators are odd with respect to $\Gamma$. The two chains are different structures on the same carrier. The precise comparison, with the branching rules, is *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*.

**The $n=2$ case.** For the biquaternion algebra $M_2(\mathbb{C})$ the carrier is $\mathbb{C}^2=\operatorname{Sym}^1(\mathbb{C}^2)$, the spin-$\tfrac12$ module. The generators are

$$
J_3=\operatorname{diag}\left(\frac12,-\frac12\right),\qquad
J_+=E_{12},\qquad
J_-=E_{21},
$$

with ladder coefficient $1$. The adjoint decomposes as

$$
M_2(\mathbb{C})=\mathcal{V}_0\oplus\mathcal{V}_1,\qquad 1+3=4,
$$

with highest weight vectors $I$ (weight $0$) and $E_{12}$ (weight $1$). The spin chain has two steps; the Peirce chain has one nilpotent. The pattern $1+3+5+\cdots+(2n-1)=n^2$ begins at $n=2$ with $1+3=4$ and at $n=4$ with $1+3+5+7=16$.

**The general pattern.** For $M_n(\mathbb{C})$ the carrier is $\operatorname{Sym}^{n-1}(\mathbb{C}^2)$, of spin $\frac{n-1}{2}$, and the adjoint decomposes as

$$
M_n(\mathbb{C})=\bigoplus_{k=0}^{n-1}\mathcal{V}_k,\qquad
\dim_\mathbb{C}=\sum_{k=0}^{n-1}(2k+1)=n^2 .
$$

The highest weight vectors are $E_{1n}$ (weight $n-1$), the sums along the weight diagonals, the ladder operator $J_+$ (weight $1$), and $I$ (weight $0$). For $n=4$ this is the four-term decomposition of the theorem.

## Summary

The carrier $\mathbb{C}^4$ is the spin-$\tfrac32$ module of $\mathfrak{sl}_2(\mathbb{C})$, with generators $J_3=\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$ and $J_\pm$ having ladder coefficients $\sqrt3,2,\sqrt3$. The adjoint representation on $M_4(\mathbb{C})$ has weights $m_i-m_j$ with multiplicities $1,2,3,4,3,2,1$, and decomposes as

$$
M_4(\mathbb{C})=\mathcal{V}_0\oplus\mathcal{V}_1\oplus\mathcal{V}_2\oplus\mathcal{V}_3,
\qquad 1+3+5+7=16,
$$

with highest weight vectors $I$, $J_+$, $E_{13}+E_{24}$ and $E_{14}$. The Peirce chain $E_{12},E_{23},E_{34}$ is the weight chain; its composites have weights $2,2,3$. The Peirce $\mathfrak{sl}_2$ is irreducible and mixes the two chiralities; the chiral $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ preserves $\Gamma$ and acts as spin-$\tfrac12$ on each chirality. At $n=2$ the chain is the spin-$\tfrac12$ chain with adjoint $1+3$.

$$
\boxed{\ M_4(\mathbb{C})=\mathcal{V}_0\oplus\mathcal{V}_1\oplus\mathcal{V}_2\oplus\mathcal{V}_3,\qquad 1+3+5+7=16,\qquad \text{spin}=\frac32.\ }
$$

| Object | Dimension |
|---|---|
| Carrier $\mathbb{C}^4=\operatorname{Sym}^3(\mathbb{C}^2)$ | $4$ |
| Spin | $\tfrac32$ |
| Ladder coefficients | $\sqrt3,2,\sqrt3$ |
| Adjoint weights | $m_i-m_j$, multiplicities $1,2,3,4,3,2,1$ |
| Adjoint decomposition | $\mathcal{V}_0\oplus\mathcal{V}_1\oplus\mathcal{V}_2\oplus\mathcal{V}_3$ |
| Dimensions | $1+3+5+7=16$ |
| Adjoint of $\mathfrak{sl}_4$ | $3+5+7=15$ |
| Centre | $\mathcal{V}_0=\mathbb{C}I$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J_3,J_+,J_-$ | the spin-$\tfrac32$ generators on $\mathbb{C}^4$ |
| $e_1,\dots,e_4$ | the weight basis, weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ |
| $\mathcal{V}_k$ | the irreducible $\mathfrak{sl}_2$ module of spin $k$, dimension $2k+1$ |
| $m_i$ | the weight of $e_i$ |
| $w_k$ | a highest weight vector of weight $k$ |
| $\operatorname{ad}_{J_a}$ | the adjoint action $X\mapsto[J_a,X]$ |
| $\Gamma=H^2$ | the chirality involution |
| $\mathbb{C}^2_\pm$ | the two chiralities, the $\pm1$ eigenspaces of $\Gamma$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the representation theory of $\mathfrak{sl}_2$ and the Clebsch–Gordan decomposition.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the symmetric powers $\operatorname{Sym}^{n-1}(\mathbb{C}^2)$ and their weights.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the matrix units and the commutator.
- [Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), for the root and the chirality involution.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the corners that the matrix units span.
- [The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m4c.html), for the chain of simple nilpotents.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the $2+2$ split.
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the comparison of the two chains.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-in-the-biquaternion-algebra.html), for the biquaternion case $n=2$.
