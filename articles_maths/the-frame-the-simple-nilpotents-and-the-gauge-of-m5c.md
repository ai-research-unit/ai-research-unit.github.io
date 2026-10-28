# __The Frame, the Simple Nilpotents and the Gauge of $M_5(\mathbb{C})$__

## Introduction

A root $H$ fixes five spectral lines, not five vectors. The choice of a vector in each line is a **frame**, and a frame turns the algebra into an array of matrix units

$$
E_{ij}=v_iv_j^{\vee},\qquad E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

The units $E_{12},E_{23},E_{34},E_{45}$ are the **simple nilpotents**: each squares to zero, and every other unit is a product of consecutive simple ones. The frame is not canonical. Rescaling the vectors by $t_1,\dots,t_5\in\mathbb{C}^\times$ sends

$$
E_{ij}\longmapsto\frac{t_i}{t_j}E_{ij},
$$

which is conjugation by the diagonal matrix $D_t=\sum_it_iE_{ii}$. The scalars act trivially, so the effective group is the torus $(\mathbb{C}^\times)^4$. Writing $\lambda_k=t_k/t_{k+1}$ for the four simple nilpotents, the composite $E_{ij}$ is rescaled by the product $\lambda_i\lambda_{i+1}\cdots\lambda_{j-1}$. The product around the closed chain is one, and there is **no fifth independent scalar**: the four $\lambda_k$ are the whole gauge, one per simple nilpotent, and the composites are fixed by the cocycle.

The gauge leaves every idempotent of the frame untouched, $D_tE_{ii}D_t^{-1}=E_{ii}$, and in particular it leaves the Lagrange projectors $P_k$ untouched. **It rescales the nilpotents, not the idempotents.** This is the precise sense in which the frame is a choice of coordinates inside a fixed root, and why the count of the frame is the count of the root plus the count of the gauge: $20+4=24=\dim PGL_5$.

The article assumes the root, the idempotents $P_k$ and the Peirce lines $A_{kl}$ of *Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$* and *The Peirce Decomposition of $M_5(\mathbb{C})$*. It uses no form, no involution and no topology. The rank-two split and the partial flags are later articles; the adjoint action, where the gauge appears as a stabiliser, is *The Adjoint Action, the Orbits and the Flag Variety of $M_5(\mathbb{C})$*.

## The Frame

### The Definition

**Definition.** A **frame** of $V=\mathbb{C}^5$ is an ordered basis $\mathcal{V}=(v_1,\dots,v_5)$. Its **dual frame** is the basis $(v_1^{\vee},\dots,v_5^{\vee})$ of the dual space defined by $v_j^{\vee}(v_i)=\delta_{ij}$.

In the identification $V\cong\mathbb{C}^5$ by the frame, the vector $v_i$ is the $i$-th standard basis vector and $v_j^{\vee}$ is the $j$-th coordinate functional. The frame is a matrix $V=(v_1|\cdots|v_5)\in GL_5(\mathbb{C})$, and the dual frame is the matrix $V^{-1}$ read by rows.

**Definition.** The **matrix units** of the frame are

$$
E_{ij}=v_iv_j^{\vee}\in M_5(\mathbb{C}),\qquad 1\le i,j\le5 .
$$

In the frame, $E_{ij}$ is the matrix with a $1$ in position $(i,j)$ and zeros elsewhere.

**Proposition.** The matrix units satisfy

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad \sum_{i=1}^{5}E_{ii}=I,\qquad E_{ii}E_{jj}=\delta_{ij}E_{ii},
$$

and they form a basis of $M_5(\mathbb{C})$: every $A$ has the unique expansion $A=\sum_{i,j}a_{ij}E_{ij}$ with $a_{ij}=v_i^{\vee}Av_j$.

**Proof.** The product is

$$
E_{ij}E_{kl}=v_iv_j^{\vee}v_kv_l^{\vee}=v_i\,\delta_{jk}\,v_l^{\vee}=\delta_{jk}E_{il},
$$

because $v_j^{\vee}(v_k)=\delta_{jk}$. The sum $\sum_iE_{ii}$ acts on $v_j$ as $v_j$, so it is the identity. The twenty-five units are linearly independent because their matrices in the frame are the standard matrix units, and they span because every matrix is a linear combination of them.

**Corollary.** The diagonal units $E_{11},\dots,E_{55}$ are mutually orthogonal rank-one idempotents summing to $I$. They are the projectors onto the lines $\mathbb{C}v_i$ along the sum of the other four lines.

**Proof.** $E_{ii}^2=E_{ii}$ by the product rule, $E_{ii}E_{jj}=0$ for $i\ne j$, and the sum is $I$. The image of $E_{ii}$ is the line $\mathbb{C}v_i$, and its kernel contains every $v_j$ with $j\ne i$.

**Remark.** The frame is a **complete system of matrix units**, and the five diagonal units are a complete family of orthogonal rank-one idempotents. A root supplies such a family, the Lagrange projectors $P_k$; a frame supplies the vectors inside the lines. The two data are related by $E_{kk}=P_k$ for $k=1,\dots,5$ when the frame is **spectral**, that is, when $v_k$ spans $\operatorname{im}P_k$ and the dual functional is the left eigenfunctional. A general frame need not be spectral; the matrix units and the gauge are defined for every frame, and the specialization to the spectral frame is made where the root is used.

### The Frame and the Root

Let $H$ be a root with spectral lines $L_k=\ker(H-\zeta_kI)$ for $k=1,\dots,5$, and let $v_k\in L_k$ be nonzero. The frame $(v_1,\dots,v_5)$ is **spectral** for $H$. In this frame

$$
H=\sum_{k=1}^{5}\zeta_kE_{kk},\qquad E_{kk}=P_k,
$$

and the matrix of $H$ is $\operatorname{diag}(\zeta_1,\dots,\zeta_5)$. The root determines the lines $L_k$, hence the diagonal units $E_{kk}=P_k$; it does **not** determine the vectors $v_k$, hence not the off-diagonal units $E_{ij}$ with $i\ne j$. The off-diagonal units are exactly what the gauge moves.

**Proposition.** Let $H$ be a root and let $\mathcal{V}$ be a spectral frame. A matrix $g\in GL_5(\mathbb{C})$ preserves $H$ by conjugation, $gHg^{-1}=H$, if and only if $g$ is diagonal in the frame, $g=\sum_it_iE_{ii}$ with $t_i\ne0$. The stabiliser of $H$ in $PGL_5$ is therefore the torus $T$ of the diagonal matrices modulo scalars, of dimension $4$.

**Proof.** In the spectral frame $H=\operatorname{diag}(\zeta_1,\dots,\zeta_5)$ with distinct entries. The equation $gH=Hg$ reads $g_{ij}\zeta_j=\zeta_i g_{ij}$ for $i,j=1,\dots,5$; for $i\ne j$ this forces $g_{ij}=0$. Hence $g$ is diagonal and invertible, so all $t_i=g_{ii}$ are nonzero. The scalars are the intersection with the centre, and the quotient has dimension $5-1=4$.

**Corollary.** The gauge group of the spectral frame is the stabiliser of the root. The frame is a point of $PGL_5$; the root is its image in $PGL_5/T$; the gauge is the fibre $T$. The count is

$$
\dim PGL_5=\dim(PGL_5/T)+\dim T=20+4=24 .
$$

**Proof.** The map $g\mapsto gHg^{-1}$ from $PGL_5$ to the root set has fibre the stabiliser $T$; the orbit–stabiliser theorem gives the dimension count, and the root set is $PGL_5/T$ by *Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$*.

## The Simple Nilpotents and the Composites

### The Simple Nilpotents

**Definition.** The **simple nilpotents** of the frame are

$$
N_k=E_{k,k+1},\qquad k=1,2,3,4,
$$

and the **lower simple nilpotents** are $N_k^{-}=E_{k+1,k}$ for $k=1,2,3,4$.

**Proposition.** Each simple nilpotent is square-zero, and the products of two simple nilpotents are

$$
N_k^2=0,\qquad N_jN_k=\delta_{k,j+1}E_{j,k+1}.
$$

In particular $N_kN_{k+1}=E_{k,k+2}$, and all other products of two simple nilpotents vanish. The same formulas hold for the lower simple nilpotents, with the order of the indices reversed.

**Proof.** $N_k^2=E_{k,k+1}E_{k,k+1}=0$ because the inner indices $k+1$ and $k$ differ. For the product, $E_{j,j+1}E_{k,k+1}=\delta_{j+1,k}E_{j,k+1}$; the Kronecker delta is $\delta_{k,j+1}$.

**Corollary.** The simple nilpotents are homogeneous of degree one for the **flag grading** by the difference of the indices: $N_k$ carries the pair $(k,k+1)$, and the product $N_jN_k$ is nonzero exactly when the pairs are consecutive, carrying the pair $(j,k+1)$.

**Proof.** The product rule of the matrix units is the rule for the composition of the elementary steps of the flag.

### The Composites

**Theorem.** For $i<j$,

$$
E_{ij}=N_iN_{i+1}\cdots N_{j-1},
$$

and for $i>j$,

$$
E_{ij}=N_{i-1}^{-}N_{i-2}^{-}\cdots N_j^{-},
$$

with the lower simple nilpotents $N_k^{-}=E_{k+1,k}$. Every matrix unit is a product of consecutive simple nilpotents, and the product is determined by the endpoints.

**Proof.** By induction on $j-i$. For $j=i+1$ the formula is the definition. If $E_{ij}=N_i\cdots N_{j-1}$, then

$$
E_{ij}N_j=N_i\cdots N_{j-1}N_j=E_{i,j+1}
$$

by the product rule, since the inner indices match. The lower case is the same induction with the reversed order, or the transpose of the upper case.

**Remark.** The four simple nilpotents, together with the five diagonal idempotents, generate the algebra: the composites give all off-diagonal units, and the diagonal units are part of the frame. The simple nilpotents alone generate the **strictly upper triangular** subalgebra, and the lower ones the strictly lower triangular subalgebra; the two together, with the diagonal, generate $M_5$.

### The Flag

The frame carries the **complete flag**

$$
0\subset V_1\subset V_2\subset\cdots\subset V_5=V,\qquad V_k=\operatorname{span}(v_1,\dots,v_k).
$$

The simple nilpotent $N_k$ moves one step down the flag,

$$
N_kv_{k+1}=v_k,\qquad N_kv_j=0\quad(j\ne k+1),
$$

and the composite $E_{ij}$ moves from $v_j$ to $v_i$. In the dual flag, $N_k$ moves the functional $v_k^{\vee}$ to $v_{k+1}^{\vee}$.

**Proposition.** The simple nilpotents are exactly the nonzero maps of the frame that lower the flag by one step and vanish on the other lines:

$$
N_k(V_{k+1})\subseteq V_k,\qquad N_k(V_k)=0,\qquad N_k(v_j)=0\ (j\ne k+1).
$$

**Proof.** $N_kv_{k+1}=E_{k,k+1}v_{k+1}=v_k$, and $N_kv_j=v_k\delta_{k+1,j}$, which vanishes for $j\ne k+1$. The image lies in $V_k$.

**Remark.** **The flag and the frame are not the same data.** The flag is the chain of subspaces; the frame is a splitting of the flag into lines, and the simple nilpotents depend on the splitting, not only on the flag. This is the same distinction as the one between the root set $PGL_5/T$ and the flag variety $GL_5/B$: the fibre of splittings has dimension $10$. The simple nilpotents are the elementary maps of a splitting; a different splitting changes them by the gauge and by the unipotent part.

## The Gauge

### The Diagonal Gauge

**Definition.** For $t=(t_1,\dots,t_5)\in(\mathbb{C}^\times)^5$, let

$$
D_t=\sum_{i=1}^{5}t_iE_{ii}\in GL_5(\mathbb{C}).
$$

The **gauge transformation** of parameter $t$ is the conjugation

$$
A\longmapsto D_tAD_t^{-1}.
$$

**Proposition.** The gauge acts on the matrix units by

$$
D_tE_{ij}D_t^{-1}=\frac{t_i}{t_j}E_{ij},
$$

and it fixes every diagonal unit: $D_tE_{ii}D_t^{-1}=E_{ii}$.

**Proof.** $D_tE_{ij}=t_iE_{ij}$ and $E_{ij}D_t^{-1}=t_j^{-1}E_{ij}$, because $E_{ij}$ is an eigenvector of the left multiplication by $D_t$ with eigenvalue $t_i$ and of the right multiplication with eigenvalue $t_j$. For $i=j$ the two eigenvalues are equal.

**Corollary.** The gauge fixes every idempotent of the form $P_S=\sum_{i\in S}E_{ii}$ for $S\subseteq\{1,\dots,5\}$, and in particular it fixes the five spectral projectors $P_k=E_{kk}$ if the frame is spectral. **The gauge rescales the off-diagonal units and leaves the diagonal idempotents unchanged.**

**Proof.** The diagonal idempotents are sums of diagonal units, and each diagonal unit is fixed.

### The Effective Torus

**Proposition.** The kernel of the map $t\mapsto D_t$ into $GL_5$ is the diagonal of the scalars, $\{(\lambda,\dots,\lambda):\lambda\in\mathbb{C}^\times\}\cong\mathbb{C}^\times$. The effective gauge group is therefore

$$
(\mathbb{C}^\times)^5/\mathbb{C}^\times\cong(\mathbb{C}^\times)^4,
$$

a complex torus of dimension $4$.

**Proof.** $D_t$ is the scalar matrix $\lambda I$ exactly when all $t_i=\lambda$. The quotient of the five-dimensional torus by the one-dimensional diagonal has dimension $4$.

**Corollary.** The gauge has four complex parameters, not five. The failure of the fifth parameter to be independent is the statement that the overall scale of the frame is immaterial: rescaling every $v_i$ by the same $\lambda$ rescales every $E_{ij}$ by $\lambda/\lambda=1$.

### The Four Parameters

**Definition.** For $k=1,2,3,4$, the **gauge parameter of the simple nilpotent** $N_k=E_{k,k+1}$ is

$$
\lambda_k=\frac{t_k}{t_{k+1}}\in\mathbb{C}^\times .
$$

**Theorem.** The map $t\mapsto(\lambda_1,\lambda_2,\lambda_3,\lambda_4)$ identifies the effective gauge group with $(\mathbb{C}^\times)^4$, and the action on the simple nilpotents is

$$
N_k\longmapsto\lambda_kN_k .
$$

The action on a composite is

$$
E_{ij}\longmapsto\Bigl(\prod_{k=i}^{j-1}\lambda_k\Bigr)E_{ij}\quad(i<j),
\qquad
E_{ij}\longmapsto\Bigl(\prod_{k=j}^{i-1}\lambda_k\Bigr)^{-1}E_{ij}\quad(i>j).
$$

**Proof.** The four equations $t_k/t_{k+1}=\lambda_k$ determine $t$ from $t_1$ by $t_{k+1}=t_k/\lambda_k$; the common scale $t_1$ is immaterial, so the map is an isomorphism onto $(\mathbb{C}^\times)^4$. The action on $E_{k,k+1}$ is the definition of $\lambda_k$ and the proposition on the matrix units. The composite is the product of the simple ones, and the scaling is multiplicative.

**Corollary (the cocycle).** The scalings of the composites are fixed by the four $\lambda_k$ and satisfy

$$
\lambda_{ij}\lambda_{jk}=\lambda_{ik},\qquad \lambda_{ij}\lambda_{ji}=1,\qquad \lambda_{ii}=1,
$$

where $\lambda_{ij}=t_i/t_j$. The product around the closed chain is

$$
\prod_{k=1}^{5}\frac{t_k}{t_{k+1}}=1 .
$$

Hence the four simple parameters are independent and the fifth ratio is their inverse product; there is no fifth independent scalar.

**Proof.** The identities are the multiplicativity of the ratios. The product around the cycle telescopes. If one tries to add a fifth parameter $\mu$ rescaling all $E_{ij}$ by $\mu$, it would have to equal $t_i/t_j$ for all pairs, which forces $t_i=\mu t_j$ for all $i,j$, hence all $t_i$ equal after a common rescaling, hence $\mu=1$. The fifth direction is the scalar, which acts trivially.

**Remark.** **The gauge parameters are attached to the four simple nilpotents, one per edge of the chain, never to the five idempotents.** The idempotents are fixed by the gauge; the four $\lambda_k$ move the four elementary steps. The composites $E_{13},E_{14},E_{15}$ and the lower units are not independent: their scalings are the products along the chain. This is the content of the cocycle.

## The Count of the Frame

### The Root Plus the Gauge

**Theorem.** The frame is the pair of a root and a gauge:

$$
\{\text{frames}\}/\mathbb{C}^\times\cong PGL_5,\qquad
\{\text{roots}\}\cong PGL_5/T,\qquad
\{\text{gauges}\}\cong T .
$$

The dimensions are

$$
\underbrace{20}_{\text{root}}+\underbrace{4}_{\text{gauge}}=\underbrace{24}_{\text{frame}} .
$$

**Proof.** A frame modulo a common scalar is an element of $PGL_5$; the root is the image under $g\mapsto gH_0g^{-1}$; the fibre is the stabiliser $T$, which is the gauge. The dimensions are those of *Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$*: $24-4=20$ for the root and $4$ for the torus. The sum is $24$.

**Corollary.** The four gauge parameters are the four coordinates of the fibre of the frame bundle $PGL_5\to PGL_5/T$. They are not additional degrees of freedom of the algebra, the root or the idempotents: they are the redundancy of the choice of a vector in each spectral line.

**Remark.** **The count $20+4=24$ is the whole count of the frame, and it is not $20+5$.** The naive count of five vector rescalings overcounts by the common scalar, which acts trivially. The correct count is four, the dimension of $T$. The four $\lambda_k$ are a convenient set of coordinates on $T$; the five $t_i$ are redundant by the common scale.

### The Real Gauge

The trace form of *The Involution and the Hermitian Structure of $M_5(\mathbb{C})$* is positive definite, and in an **orthonormal** spectral frame the gauge parameters of the $*$-unitary structure satisfy $|t_k|=1$. The compact gauge is then the real torus $U(1)^4$, of real dimension $4$. The complex gauge $(\mathbb{C}^\times)^4$ is the algebraic gauge; the real torus is the subgroup that preserves the Hermitian structure. The four complex parameters have eight real dimensions, the four phases four, and the four moduli of the $t_k$ (the radial parts) are the non-$*$-unitary part of the algebraic gauge. The distinction is used in *The Polar Decomposition of $M_5(\mathbb{C})$* and *The Exponential and the Lie Group of $M_5(\mathbb{C})$*.

**Proof.** A diagonal matrix $D_t$ is $*$-unitary exactly when $|t_k|=1$ for every $k$; the quotient by the common scalar has real dimension $4$. The complex torus $(\mathbb{C}^\times)^4$ has real dimension $8$, and the modulus map $(\mathbb{C}^\times)^4\to(\mathbb{R}_{>0})^4$ is the four-dimensional non-$*$-unitary part.

## Worked Example

### The Standard Frame

Take $v_i=e_i$, the standard basis, so $E_{ij}$ is the standard matrix unit. The four simple nilpotents are

$$
N_1=E_{12}=\begin{pmatrix}0&1&0&0&0\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\end{pmatrix},
\qquad
N_4=E_{45}=\begin{pmatrix}0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&0&0\\0&0&0&1&0\end{pmatrix},
$$

and $N_2=E_{23}$, $N_3=E_{34}$ are the two intermediate units. The composites are

$$
E_{13}=N_1N_2,\qquad E_{14}=N_1N_2N_3,\qquad E_{15}=N_1N_2N_3N_4 .
$$

### A Numerical Gauge

Take $\lambda_1=2$, $\lambda_2=3$, $\lambda_3=5$, $\lambda_4=7$. The frame parameters are $t_1=1$, $t_2=\lambda_1^{-1}=1/2$, $t_3=(\lambda_1\lambda_2)^{-1}=1/6$, $t_4=1/30$, $t_5=1/210$, so

$$
D_t=\operatorname{diag}\Bigl(1,\frac12,\frac16,\frac1{30},\frac1{210}\Bigr).
$$

Then

$$
D_tN_1D_t^{-1}=2N_1,\quad D_tN_2D_t^{-1}=3N_2,\quad D_tN_3D_t^{-1}=5N_3,\quad D_tN_4D_t^{-1}=7N_4,
$$

and the composite $E_{15}$ is rescaled by

$$
\frac{t_1}{t_5}=210=2\cdot3\cdot5\cdot7=\lambda_1\lambda_2\lambda_3\lambda_4 .
$$

The diagonal units are unchanged: $D_tE_{kk}D_t^{-1}=E_{kk}$ for every $k$. The product around the cycle is

$$
\frac{t_1}{t_2}\frac{t_2}{t_3}\frac{t_3}{t_4}\frac{t_4}{t_5}\frac{t_5}{t_1}=1,
$$

and the fifth ratio $t_5/t_1=1/210$ is the inverse product, not an independent parameter.

**Remark.** The uniform choice $\lambda_1=\lambda_2=\lambda_3=\lambda_4=\lambda$ is the one-parameter subgroup $t_k=\lambda^{-(k-1)}$; it rescales $E_{ij}$ by $\lambda^{j-i}$. It is a single direction inside the four-dimensional gauge, not a fifth parameter. The general gauge is the four-dimensional torus, and the uniform direction is its diagonal.

## Summary

A frame is an ordered basis, and it produces the matrix units $E_{ij}=v_iv_j^{\vee}$ with the product rule $E_{ij}E_{kl}=\delta_{jk}E_{il}$. The simple nilpotents $N_k=E_{k,k+1}$, $k=1,2,3,4$, are square-zero, and every composite is a product of consecutive simple ones, $E_{ij}=N_iN_{i+1}\cdots N_{j-1}$ for $i<j$.

The gauge is the conjugation by $D_t=\sum_it_iE_{ii}$; it acts by $E_{ij}\mapsto(t_i/t_j)E_{ij}$, fixes every diagonal idempotent, and has effective group $(\mathbb{C}^\times)^4$. The four parameters are

$$
\lambda_k=\frac{t_k}{t_{k+1}},\qquad k=1,2,3,4,
$$

one per simple nilpotent. The composites are rescaled by the products, the cycle product is one, and there is no fifth independent scalar.

$$
\boxed{\ \text{The gauge is }(\mathbb{C}^\times)^4\text{, with one parameter per simple nilpotent }E_{k,k+1};\text{ it fixes the idempotents and the composites are fixed by the cocycle.}\ }
$$

The frame is the root plus the gauge: $20+4=24=\dim PGL_5$. The root is the base $PGL_5/T$, the gauge is the fibre $T$, and the frame modulo scalars is $PGL_5$.

| Object | Count or dimension |
|---|---|
| Frame modulo scalars | $\dim PGL_5=24$ |
| Root | $\dim PGL_5/T=20$ |
| Gauge torus $T$ | $4$ |
| Simple nilpotents | $4$, $E_{12},E_{23},E_{34},E_{45}$ |
| Gauge parameters $\lambda_k$ | $4$, one per simple nilpotent |
| Independent scalar parameters | $4$, not $5$ |
| Composite $E_{ij}$ scaling | $\prod_{k=i}^{j-1}\lambda_k$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{V}=(v_1,\dots,v_5)$ | A frame, an ordered basis of $\mathbb{C}^5$ |
| $v_j^{\vee}$ | The dual functional, $v_j^{\vee}(v_i)=\delta_{ij}$ |
| $E_{ij}=v_iv_j^{\vee}$ | The matrix units of the frame |
| $N_k=E_{k,k+1}$ | The simple nilpotent of the step $k\to k+1$, $k=1,\dots,4$ |
| $D_t=\sum_it_iE_{ii}$ | The diagonal gauge matrix |
| $t=(t_1,\dots,t_5)$ | The frame rescaling, defined modulo a common scalar |
| $\lambda_k=t_k/t_{k+1}$ | The gauge parameter of the simple nilpotent $N_k$ |
| $\lambda_{ij}=t_i/t_j$ | The scaling of the unit $E_{ij}$ |
| $T$ | The diagonal torus modulo scalars, the gauge group |
| $PGL_5/T$ | The root set, the base of the frame bundle |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for systems of matrix units, the Peirce decomposition and the inner automorphisms of a full matrix algebra.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the elementary matrices, the matrix units and the diagonal similarity $E_{ij}\mapsto(t_i/t_j)E_{ij}$.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the systems of matrix units adapted to an algebra with involution and the unitary gauge.
- [Roots of Unity and the Lagrange Idempotents of $M_5(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m5c.html), for the root, its spectral lines and the idempotents fixed by the gauge.
- [The Peirce Decomposition of $M_5(\mathbb{C})$](the-peirce-decomposition-of-m5c.html), for the lines $A_{kl}$ whose generators are moved by the gauge.
- [The Rank-Two Split of $M_5(\mathbb{C})$](the-rank-two-split-of-m5c.html), for the corners $4+6+6+9$ and the two-sided Peirce table.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_5(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m5c.html), for the gauge as the stabiliser of the root and the frame bundle $PGL_5\to PGL_5/T$.
- [The Involution and the Hermitian Structure of $M_5(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m5c.html), for the unitary gauge $U(1)^4$ and the positive definite trace form.
- [The Modules and the Minimal Left Ideals of $M_5(\mathbb{C})$](the-modules-and-the-minimal-left-ideals-of-m5c.html), for the action of the matrix units on the carrier.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the general construction at order $n$.
