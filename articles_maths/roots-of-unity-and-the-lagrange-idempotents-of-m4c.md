# __Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$__

## Introduction

**One element of order four with simple spectrum produces the four idempotents of the frame.** The element is a matrix $H\in M_4(\mathbb{C})$ with $H^4=I$ and four distinct eigenvalues; the idempotents are the Lagrange projectors of its spectrum. They are polynomials in $H$, they are orthogonal and complete, and no second element is needed to produce them. This is the root-first construction of the category $M_4(\mathbb{C})$.

The article states the spectral resolution $H=\sum_k\zeta_kP_k$, proves the interpolation formula, gives the four explicit polynomials, reads the $\mathbb{Z}/4$ grading that conjugation by $H$ defines, identifies the chirality involution $\Gamma=H^2$, and counts the root set. It specializes the general construction of *Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$* to $n=4$.

The Peirce decomposition that the idempotents produce is *The Peirce Decomposition of $M_4(\mathbb{C})$*; the vectors inside the resulting lines and the gauge that acts on them are *The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$*; the two chiralities are *The Two Chiralities of $M_4(\mathbb{C})$*; the orbit of the root and the flag variety are *The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$*. The algebra itself is *The Matrix Algebra $M_4(\mathbb{C})$*. No form, no norm and no topology are used.

## The Fourth Roots of Unity

The four roots of $x^4-1$ are

$$
1,\quad i,\quad -1,\quad -i .
$$

Write

$$
\zeta_k=i^{k-1},\qquad k=1,2,3,4,
$$

so that $\zeta_1=1$, $\zeta_2=i$, $\zeta_3=-1$ and $\zeta_4=-i$. The roots are distinct, and they satisfy

$$
\zeta_{k+2}=-\zeta_k,\qquad \zeta_{k+1}=i\zeta_k,\qquad \sum_{k=1}^{4}\zeta_k=0,\qquad \prod_{k=1}^{4}\zeta_k=-1 .
$$

The polynomial factors as

$$
x^4-1=(x-1)(x+1)(x-i)(x+i)=(x^2-1)(x^2+1).
$$

| Root | $\zeta_k$ | Real part | Imaginary part | $\zeta_k^2$ | $\zeta_k^3$ |
|---|---|---|---|---|---|
| $\zeta_1$ | $1$ | $1$ | $0$ | $1$ | $1$ |
| $\zeta_2$ | $i$ | $0$ | $1$ | $-1$ | $-i$ |
| $\zeta_3$ | $-1$ | $-1$ | $0$ | $1$ | $-1$ |
| $\zeta_4$ | $-i$ | $0$ | $-1$ | $-1$ | $i$ |

The squaring map $\zeta\mapsto\zeta^2$ sends the four roots onto $\{1,-1\}$, each value twice: $\zeta_1^2=\zeta_3^2=1$ and $\zeta_2^2=\zeta_4^2=-1$. This is the quotient $\mathbb{Z}/4\to\mathbb{Z}/2$ that becomes the chirality in §*The Chirality Involution*. The conjugation $\zeta\mapsto\bar\zeta$ is the inversion $\zeta\mapsto\zeta^{-1}$; it fixes $\zeta_1=1$ and $\zeta_3=-1$ and exchanges $\zeta_2\leftrightarrow\zeta_4$.

## The Root

**Definition.** A **root of unity of order four** in $M_4(\mathbb{C})$ is an element $H$ with

$$
H^4=I
$$

and four distinct eigenvalues. Equivalently, the minimal polynomial of $H$ is $x^4-1$.

**Proposition.** If $H^4=I$ then $H$ is diagonalizable and its eigenvalues lie among the fourth roots of unity. It has simple spectrum if and only if each of the four roots occurs exactly once, if and only if its minimal polynomial is $x^4-1$.

**Proof.** The polynomial $x^4-1$ has the four distinct roots $\zeta_k$ and no repeated factor, so it is square-free. The minimal polynomial of $H$ divides $x^4-1$, hence is square-free. A matrix whose minimal polynomial is square-free is diagonalizable (*The Jordan–Chevalley Decomposition of a Matrix*). Its eigenvalues are roots of $x^4-1$. There are four eigenvalues counted with multiplicity and four roots in all, so simple spectrum is the statement that each root occurs once. The minimal polynomial then has the four distinct roots, hence is $x^4-1$.

**Corollary.** A root of order four is invertible, with $H^{-1}=H^3$, and it is not a scalar. Its four eigenspaces

$$
V_k=\ker(H-\zeta_kI)=\operatorname{im}P_k
$$

are lines, and

$$
\mathbb{C}^4=V_1\oplus V_2\oplus V_3\oplus V_4 .
$$

**Standing hypothesis.** For the rest of the article $H$ is a root of order four with simple spectrum, and $P_k$ is the projector onto $V_k$.

## The Lagrange Projectors

**Definition.** The **Lagrange projector** of $\zeta_k$ is

$$
P_k=\prod_{l\ne k}\frac{H-\zeta_lI}{\zeta_k-\zeta_l},\qquad k=1,2,3,4 .
$$

Each factor is a polynomial in $H$, so $P_k$ is a polynomial in $H$ of degree at most three.

**Theorem.** The four elements $P_k$ are idempotent, orthogonal and complete:

$$
P_k^2=P_k,\qquad P_kP_l=0\quad(k\ne l),\qquad \sum_{k=1}^{4}P_k=I,
$$

and they satisfy

$$
HP_k=P_kH=\zeta_kP_k .
$$

They are the spectral projectors of $H$. Conversely, a complete orthogonal family $Q_1,\dots,Q_4$ with $H=\sum_k\zeta_kQ_k$ is this family.

**Proof.** Let $v\in V_m$. Every factor acts on $v$ by a scalar,

$$
\frac{H-\zeta_lI}{\zeta_k-\zeta_l}v=\frac{\zeta_m-\zeta_l}{\zeta_k-\zeta_l}v ,
$$

so

$$
P_kv=\prod_{l\ne k}\frac{\zeta_m-\zeta_l}{\zeta_k-\zeta_l}v .
$$

If $m=k$ every factor is $1$, and if $m\ne k$ the factor with $l=m$ has numerator $0$. Hence $P_kv=\delta_{km}v$. Therefore $P_k$ is the identity on $V_k$ and $0$ on the other three lines. The three properties follow, and $HP_kv=\zeta_kP_kv$ for every $v$.

For the converse, let $v\in\operatorname{im}Q_m$. Then $Hv=\sum_k\zeta_kQ_kQ_mv=\zeta_mv$, so $\operatorname{im}Q_m\subseteq V_m$. The images of the $Q_m$ are independent and sum to $\mathbb{C}^4$, and the $V_m$ are four lines summing to $\mathbb{C}^4$; hence $\operatorname{im}Q_m=V_m$, and $Q_m$ is the projector onto $V_m$ along the sum of the other lines, which is $P_m$.

**Corollary (interpolation).** For every polynomial $f$ of degree at most three,

$$
f(H)=\sum_{k=1}^{4}f(\zeta_k)P_k .
$$

In particular,

$$
I=\sum_kP_k,\qquad H=\sum_k\zeta_kP_k,\qquad H^2=\sum_k\zeta_k^2P_k,\qquad H^3=\sum_k\zeta_k^3P_k .
$$

**Proof.** Both sides are polynomials in $H$ of degree at most three. On $V_m$ the right-hand side is $f(\zeta_m)$, and the left-hand side is $f(H)v=f(\zeta_m)v$. Two polynomials in $H$ that agree on the four lines agree on their sum $\mathbb{C}^4$.

**Corollary (a basis of $\mathbb{C}[H]$).** The projectors $P_1,\dots,P_4$ are a basis of the commutative algebra $\mathbb{C}[H]$, which is isomorphic to $\mathbb{C}^4$. The map

$$
f\longmapsto\bigl(f(1),f(i),f(-1),f(-i)\bigr)
$$

is an isomorphism $\mathbb{C}[x]/(x^4-1)\to\mathbb{C}^4$, and the matrix of the roots is the Vandermonde matrix of $1,i,-1,-i$, which is invertible.

**Proof.** The four evaluation maps are linearly independent: a polynomial of degree at most three vanishing at the four roots is zero. Both spaces have dimension four, so the map is an isomorphism. The projectors are the images of the four indicator polynomials, hence a basis.

### The Explicit Polynomials

The Lagrange formula is the discrete Fourier transform of the powers of $H$. Because the four roots are the fourth roots of unity,

$$
P_k=\frac14\sum_{m=0}^{3}\zeta_k^{-m}H^m,\qquad k=1,2,3,4 .
$$

**Proof.** On $V_l$, the right-hand side acts by

$$
\frac14\sum_{m=0}^{3}\left(\frac{\zeta_l}{\zeta_k}\right)^m .
$$

The ratio $\zeta_l/\zeta_k$ is a fourth root of unity. It is $1$ exactly when $l=k$, and then the sum is $4/4=1$; otherwise it is a non-trivial fourth root, and the four terms sum to $0$. So the right-hand side is $\delta_{kl}$ on $V_l$, which is $P_k$.

Written in $H$ alone, with $H^0=I$,

$$
P_1=\frac14\bigl(I+H+H^2+H^3\bigr),
$$

$$
P_2=\frac14\bigl(I-iH-H^2+iH^3\bigr),
$$

$$
P_3=\frac14\bigl(I-H+H^2-H^3\bigr),
$$

$$
P_4=\frac14\bigl(I+iH-H^2-iH^3\bigr).
$$

The coefficients are the columns of the discrete Fourier matrix of order four. The four polynomials sum to $I$ because the coefficients of $H^m$ for $m\ge1$ sum to $0$, and the coefficient of $I$ sums to $1$.

### Rank, Trace and Canonicality

**Proposition.** Each $P_k$ has rank $1$ and trace $1$. The projectors depend only on $H$: they are fixed by the polynomial formula, with no choice of basis, no choice of gauge and no second element.

**Proof.** The image of $P_k$ is the line $V_k$, so the rank is $1$. The trace of a projector is its rank, because in a basis adapted to the decomposition $\mathbb{C}^4=\bigoplus_mV_m$ the matrix of $P_k$ is the coordinate matrix $E_{kk}$. The formula involves $H$ and the constants $\zeta_k$ alone.

**Corollary.** The four projectors are the primitive idempotents of the frame. They are not nilpotents: $P_k^2=P_k\ne0$. The nilpotents $E_{12},E_{23},E_{34}$ of *The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$* are different elements; they square to $0$, they are not polynomials in $H$, and they carry the gauge.

## The Standard Model

The **standard root** is

$$
H_0=\operatorname{diag}(1,i,-1,-i).
$$

It satisfies $H_0^4=I$ and has the four roots on the diagonal in the order $\zeta_1,\zeta_2,\zeta_3,\zeta_4$. The Lagrange formula returns the coordinate matrix units,

$$
P_k=E_{kk},\qquad k=1,2,3,4,
$$

so in the standard frame the four idempotents are the four diagonal matrix units. The spectral resolution is the identity

$$
\operatorname{diag}(1,i,-1,-i)=1\,E_{11}+i\,E_{22}-1\,E_{33}-i\,E_{44}.
$$

The chirality involution is

$$
\Gamma_0=H_0^2=\operatorname{diag}(1,-1,1,-1)=E_{11}-E_{22}+E_{33}-E_{44}.
$$

**A general root is a conjugate of the standard one.** Every root $H$ is diagonalizable with the four roots as eigenvalues, so there is $S\in GL_4(\mathbb{C})$ with

$$
H=SH_0S^{-1}.
$$

The Lagrange formula is conjugation-equivariant, so

$$
P_k=SE_{kk}S^{-1}.
$$

Write $v_k$ for the $k$-th column of $S$ and $\ell_k$ for the $k$-th row of $S^{-1}$. Then

$$
P_k=v_k\ell_k,
$$

the rank-one matrix sending $\ell_k$ to $v_k$ and killing the other dual basis vectors. The vectors $v_1,\dots,v_4$ are a basis of $\mathbb{C}^4$, the functionals $\ell_1,\dots,\ell_4$ are the dual basis, and

$$
P_kv_m=\delta_{km}v_k,\qquad \ell_k(v_m)=\delta_{km}.
$$

The frame $(v_1,\dots,v_4)$ is the subject of *The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$*. The root fixes the four lines; the frame fixes a vector in each line.

### A Non-Diagonal Root

The root need not be diagonal, and its projectors need not be Hermitian. Take the upper triangular unipotent matrix

$$
S=\begin{pmatrix}1&1&0&0\\0&1&1&0\\0&0&1&1\\0&0&0&1\end{pmatrix},
\qquad
S^{-1}=\begin{pmatrix}1&-1&1&-1\\0&1&-1&1\\0&0&1&-1\\0&0&0&1\end{pmatrix}.
$$

Then

$$
H=SH_0S^{-1}
=\begin{pmatrix}
1&-1+i&1-i&-1+i\\
0&i&-1-i&1+i\\
0&0&-1&1-i\\
0&0&0&-i
\end{pmatrix}.
$$

The matrix is upper triangular, so its eigenvalues are its diagonal entries $1,i,-1,-i$; it has simple spectrum. The four vectors are the columns of $S$,

$$
v_1=\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\quad
v_2=\begin{pmatrix}1\\1\\0\\0\end{pmatrix},\quad
v_3=\begin{pmatrix}0\\1\\1\\0\end{pmatrix},\quad
v_4=\begin{pmatrix}0\\0\\1\\1\end{pmatrix},
$$

and the dual functionals are the rows of $S^{-1}$,

$$
\ell_1=(1,-1,1,-1),\quad
\ell_2=(0,1,-1,1),\quad
\ell_3=(0,0,1,-1),\quad
\ell_4=(0,0,0,1).
$$

The first projector is

$$
P_1=v_1\ell_1=
\begin{pmatrix}
1&-1&1&-1\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$

It is idempotent, of rank one and trace one, and it is not Hermitian: $P_1^*\ne P_1$. The other projectors are the analogous outer products,

$$
P_2=\begin{pmatrix}0&1&-1&1\\0&1&-1&1\\0&0&0&0\\0&0&0&0\end{pmatrix},
\quad
P_3=\begin{pmatrix}0&0&0&0\\0&0&1&-1\\0&0&1&-1\\0&0&0&0\end{pmatrix},
\quad
P_4=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&1\\0&0&0&1\end{pmatrix},
$$

and their sum is $I$. The example shows that the construction depends on $H$ and not on a choice of orthonormal basis.

## The Spectral Resolution and the $\mathbb{Z}/4$ Grading

### The Resolution

**Theorem.** The root is the weighted sum of its projectors:

$$
H=\sum_{k=1}^{4}\zeta_kP_k=P_1+iP_2-P_3-iP_4,
$$

and for every integer $m\ge1$,

$$
H^m=\sum_{k=1}^{4}\zeta_k^mP_k .
$$

In particular,

$$
I=P_1+P_2+P_3+P_4,\qquad
H^2=P_1-P_2+P_3-P_4,\qquad
H^3=P_1-iP_2-P_3+iP_4 .
$$

**Proof.** The first identity is the interpolation corollary applied to the polynomial $x$; the second is the same corollary applied to $x^m$. The four displayed cases are $m=0,1,2,3$.

**Corollary.** The four elements $I,H,H^2,H^3$ are a basis of $\mathbb{C}[H]$, and the four $P_k$ are the Lagrange basis for the evaluations $f\mapsto f(\zeta_k)$ at the four roots. The matrix of the change of basis is the Vandermonde matrix of the fourth roots.

### The Grading

**Definition.** Conjugation by $H$ is the automorphism

$$
\operatorname{Ad}_H:M_4(\mathbb{C})\longrightarrow M_4(\mathbb{C}),\qquad
\operatorname{Ad}_H(X)=HXH^{-1}.
$$

Because $H^4=I$, the fourth power of $\operatorname{Ad}_H$ is the identity.

**Proposition.** For $X\in\mathcal{A}_{kl}=P_kM_4P_l$,

$$
\operatorname{Ad}_H(X)=\zeta_k\zeta_l^{-1}X=\zeta_{k-l}X .
$$

Hence $\operatorname{Ad}_H$ is diagonalizable with eigenvalues among the fourth roots of unity, and

$$
M_4(\mathbb{C})=\bigoplus_{r\in\mathbb{Z}/4\mathbb{Z}}\mathcal{M}^{(r)},\qquad
\mathcal{M}^{(r)}=\bigoplus_{k-l\equiv r\ (\mathrm{mod}\ 4)}\mathcal{A}_{kl},
$$

with

$$
\mathcal{M}^{(r)}\mathcal{M}^{(s)}\subseteq\mathcal{M}^{(r+s)} .
$$

**Proof.** On $\mathcal{A}_{kl}$, $HXH^{-1}=\zeta_kX\zeta_l^{-1}=\zeta_k\zeta_l^{-1}X$. The sum over the pairs $k-l\equiv r$ is direct because the corners $\mathcal{A}_{kl}$ are independent. If $X\in\mathcal{M}^{(r)}$ and $Y\in\mathcal{M}^{(s)}$, then $\operatorname{Ad}_H(XY)=\operatorname{Ad}_H(X)\operatorname{Ad}_H(Y)=\zeta^{r+s}XY$.

**The graded pieces.** The four pieces have equal dimension. The pairs $(k,l)$ with $k-l\equiv r$ are, for each $r$, the four pairs obtained by translating both indices:

| $r$ | pairs $(k,l)$ | $\dim_\mathbb{C}\mathcal{M}^{(r)}$ | reading |
|---|---|---|---|
| $0$ | $(1,1),(2,2),(3,3),(4,4)$ | $4$ | the centraliser $\mathbb{C}[H]$ |
| $1$ | $(2,1),(3,2),(4,3),(1,4)$ | $4$ | the cyclic lower block |
| $2$ | $(3,1),(4,2),(1,3),(2,4)$ | $4$ | the chiral off-diagonal block |
| $3$ | $(4,1),(1,2),(2,3),(3,4)$ | $4$ | the cyclic upper block |

Each row has four pairs, so each graded piece is four-dimensional. The even part

$$
\mathcal{M}^{(0)}\oplus\mathcal{M}^{(2)}
$$

is the fixed space of $\operatorname{Ad}_\Gamma$, where $\Gamma=H^2$, and the odd part

$$
\mathcal{M}^{(1)}\oplus\mathcal{M}^{(3)}
$$

is the $-1$ eigenspace of $\operatorname{Ad}_\Gamma$. The even part is the centraliser of $\Gamma$, of dimension $8$; the odd part is the mass block, of dimension $8$. The grading is coarser than the Peirce decomposition: the latter has sixteen lines, the former four pieces of dimension four.

**Corollary.** The centraliser of $H$ in $M_4(\mathbb{C})$ is $\mathbb{C}[H]$, of dimension $4$. It consists of the matrices that preserve each spectral line.

**Proof.** A matrix commuting with $H$ preserves each eigenspace of $H$, because the eigenvalues are distinct; such a matrix is diagonal in the frame, so it is a combination of the $P_k$, hence lies in $\mathbb{C}[H]$. Conversely every polynomial in $H$ commutes with $H$. The dimension is four.

## The Chirality Involution

**Definition.** The **chirality involution** of the root is

$$
\Gamma=H^2 .
$$

**Proposition.** $\Gamma$ is an involution, $\Gamma^2=I$, with eigenvalues $+1$ on $V_1\oplus V_3$ and $-1$ on $V_2\oplus V_4$. It has trace $0$, its $+1$ eigenspace and its $-1$ eigenspace both have dimension $2$, and

$$
\Gamma=P_1-P_2+P_3-P_4 .
$$

**Proof.** $\Gamma^2=H^4=I$. On $V_k$, $\Gamma$ acts by $\zeta_k^2$, which is $+1$ for $k=1,3$ and $-1$ for $k=2,4$. The trace is $1-1+1-1=0$, and each eigenspace is the sum of two spectral lines, hence has dimension $2$. The displayed formula is the case $m=2$ of the spectral resolution.

The two eigenspaces

$$
\mathbb{C}^2_+=\operatorname{im}P_+,\qquad P_+=\frac12(I+\Gamma)=P_1+P_3,
$$

$$
\mathbb{C}^2_-=\operatorname{im}P_-,\qquad P_-=\frac12(I-\Gamma)=P_2+P_4,
$$

are the **two chiralities** of the root. Each is a plane. The involution $\Gamma$ is the $\mathbb{Z}/2$ quotient of the $\mathbb{Z}/4$ grading: on $\mathcal{M}^{(r)}$ it acts by $(-1)^r$ under $\operatorname{Ad}_\Gamma$. The two chiralities, the block decomposition and the mass block are *The Two Chiralities of $M_4(\mathbb{C})$* and *The Rank-Two Split of $M_4(\mathbb{C})$*.

**The root and the chirality.** The map $H\mapsto\Gamma=H^2$ forgets the choice of which line in each chirality carries $+1$ rather than $-1$, or $i$ rather than $-i$: on $\mathbb{C}^2_+$ the root restricts with eigenvalues $+1,-1$ on the two lines, and on $\mathbb{C}^2_-$ with eigenvalues $i,-i$. The fibre of the map is the space of ordered decompositions of the two planes into their spectral lines, of complex dimension four (real dimension eight); the four eigenvalue assignments are the discrete labels attached to the two lines in each plane, and they do not add to the dimension. The image is the conjugacy class of involutions with spectrum $(1,1,-1,-1)$, of complex dimension $8$; the fibre has dimension $4$; the root set has dimension $12$, as §*The Root Set* confirms.

## The Root of $+1$ as the Order-Two Case

**At $n=2$ the same construction is the biquaternion algebra $M_2(\mathbb{C})$.** The roots of $x^2-1$ are $+1$ and $-1$, and the Lagrange projectors are

$$
P_+=\frac{I+H}{2},\qquad P_-=\frac{I-H}{2},\qquad H=P_+-P_- .
$$

These are the idempotents $\tilde\Pi_\pm=(e_t\pm\tilde\Xi)/2$ of *The Peirce Decomposition of $M_4(\mathbb{C})$*, with $H=\tilde\Xi$ and $I=e_t$. The order-two root is the biquaternion root of $+1$; it is the case $n=2$ of the order-four construction, not a separate principle.

**The old "second root" is the gauge.** In the biquaternion article the frame was presented as a root of $+1$ together with a second root anticommuting with it. The second element does not produce new idempotents: the two idempotents are already produced by the first root. What it supplies is a vector in each mixed Peirce line, equivalently the normalisation of the two nilpotents. That is the gauge parameter $\lambda$ of *The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$*, and at $n=2$ it is one complex number. There is no second primitive element. For $n=4$ the gauge has three parameters, one per simple nilpotent, and no single second root plays the role of $\lambda$.

**The count in the two cases.** For $n=2$ the root set is $PGL_2/T$, of complex dimension $2$, and the gauge is one complex dimension; the frame modulo scale has dimension $3$, which is six real dimensions. For $n=4$ the root set is $PGL_4/T$, of complex dimension $12$, and the gauge is three complex dimensions; the frame modulo scale has dimension $15$.

## The Root Set

**Definition.** Let

$$
\mathcal{R}_4=\bigl\{H\in M_4(\mathbb{C}):H^4=I,\ \text{the eigenvalues of }H\text{ are distinct}\bigr\}.
$$

**Theorem.** The set $\mathcal{R}_4$ is a single orbit of $PGL_4(\mathbb{C})$ under conjugation. It is isomorphic to $PGL_4(\mathbb{C})/T$, where $T$ is the diagonal torus, and

$$
\dim_\mathbb{C}\mathcal{R}_4=15-3=12,\qquad \dim_\mathbb{R}\mathcal{R}_4=24 .
$$

**Proof.** Every $H\in\mathcal{R}_4$ is diagonalizable with the four roots as eigenvalues, so it is conjugate to $H_0=\operatorname{diag}(1,i,-1,-i)$; the action is transitive. The stabiliser of $H_0$ in $GL_4(\mathbb{C})$ is the set of invertible matrices commuting with $H_0$. A matrix commuting with a matrix with distinct eigenvalues preserves each eigenspace, hence is diagonal in the standard basis. The stabiliser is the diagonal torus $\tilde T\cong(\mathbb{C}^\times)^4$, and in $PGL_4$ its image is $T=\tilde T/\mathbb{C}^\times I$, of dimension $3$. The orbit has dimension $\dim PGL_4-\dim T=15-3=12$. The real dimension is twice the complex dimension.

**Corollary.** The root set is connected and of complex dimension $12$. It is not the flag variety: the flag variety $GL_4/B$ has complex dimension $6$.

### The Weyl Group and the Flag

The normaliser of $T$ in $PGL_4$ is $T\rtimes S_4$, so the Weyl group $S_4$ acts on $\mathcal{R}_4$ by permuting the four eigenlines. The action is free, because a root has four distinct eigenvalues and a permutation fixing the root fixes each line. The quotient $\mathcal{R}_4/S_4$ is the space of unordered spectral decompositions into four lines, of the same dimension $12$, and the quotient map is a covering of degree

$$
4!=24 .
$$

The **full flag variety** $GL_4/B$ is the space of chains

$$
0\subset F_1\subset F_2\subset F_3\subset\mathbb{C}^4,\qquad \dim F_k=k,
$$

of complex dimension $6$. The map $\mathcal{R}_4\to GL_4/B$ that records the flag

$$
F_k=V_1\oplus\cdots\oplus V_k
$$

is a fibre bundle with fibre $B/T\cong U$, the unipotent radical, of dimension $6$. It is not a finite cover. The degree $4!$ is the degree over the unordered decomposition, and the six dimensions of the unipotent fibre separate that quotient from the flag variety. The stable count is

$$
\underbrace{12}_{\text{root}}+\underbrace{3}_{\text{gauge}}=\underbrace{15}_{\text{frame}/\mathbb{C}^\times},
$$

the decomposition of *The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$*.

## Summary

A root $H$ of order four with simple spectrum is diagonalizable with the four roots of unity $1,i,-1,-i$ as eigenvalues, and the Lagrange polynomials in $H$ produce four primitive orthogonal idempotents $P_k$, complete and summing to $I$, with

$$
H=\sum_{k=1}^{4}\zeta_kP_k,\qquad \zeta_k=i^{k-1}.
$$

The projectors are the spectral projectors onto the four spectral lines; they are polynomials in $H$ of degree at most three, with the explicit Fourier form

$$
P_k=\frac14\sum_{m=0}^{3}\zeta_k^{-m}H^m .
$$

Conjugation by $H$ grades the algebra by $\mathbb{Z}/4$, with four graded pieces of dimension four; the even part is the centraliser of $\Gamma=H^2$, of dimension eight, and the odd part is the mass block. The involution $\Gamma=H^2$ is the chirality, with the $2+2$ split of the carrier. The root set is $PGL_4/T$, of complex dimension $12$; the gauge contributes three, and the frame modulo scale has dimension $15$. At $n=2$ the construction is the biquaternion root of $+1$, and the old second root is a point of the gauge, not a second primitive.

$$
\boxed{\ \text{One root } H \text{ of order four with simple spectrum produces all four idempotents, and } H=\sum_k\zeta_kP_k. \ }
$$

| Quantity | Value for $M_4(\mathbb{C})$ |
|---|---|
| Roots of $x^4-1$ | $1,i,-1,-i$ |
| Idempotents | $P_1,P_2,P_3,P_4$, rank $1$, trace $1$ |
| Spectral resolution | $H=P_1+iP_2-P_3-iP_4$ |
| Chirality | $\Gamma=H^2=P_1-P_2+P_3-P_4$ |
| Graded pieces | $\dim_\mathbb{C}\mathcal{M}^{(r)}=4$, $r=0,1,2,3$ |
| Root set | $PGL_4/T$, $\dim_\mathbb{C}=12$ |
| Gauge | $(\mathbb{C}^\times)^3$, $\dim_\mathbb{C}=3$ |
| Frame modulo scale | $PGL_4$, $\dim_\mathbb{C}=15$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\zeta_k=i^{k-1}$ | the four fourth roots of unity, $k=1,2,3,4$ |
| $H$ | a root of order four with simple spectrum |
| $H_0=\operatorname{diag}(1,i,-1,-i)$ | the standard root |
| $V_k=\ker(H-\zeta_kI)$ | the spectral line of $\zeta_k$ |
| $P_k$ | the Lagrange projector of $\zeta_k$, $\operatorname{rank}1$, $\operatorname{tr}1$ |
| $\Gamma=H^2$ | the chirality involution |
| $\mathcal{A}_{kl}=P_kM_4P_l$ | the Peirce corner, a line |
| $\mathcal{M}^{(r)}$ | the graded piece of degree $r\in\mathbb{Z}/4$ |
| $\mathcal{R}_4$ | the set of roots of order four with simple spectrum |
| $T$ | the diagonal torus in $PGL_4$ |
| $S$ | a matrix diagonalising $H$, $H=SH_0S^{-1}$ |
| $v_k,\ell_k$ | the frame vectors and the dual functionals, $P_k=v_k\ell_k$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectral decomposition, the Lagrange interpolation formula and the minimal polynomial.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, orthogonal families and Peirce decompositions.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the ambient algebra and its groups.
- [Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-mnc.html), for the general construction at order $n$.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-mnc.html), for the lines that the idempotents produce.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the vectors inside the lines and the gauge.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the biquaternion case $n=2$ and the parameter $\lambda$.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra of this category.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the sixteen corners of the frame.
- [The Frame, the Simple Nilpotents and the Gauge of $M_4(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m4c.html), for the frame of $M_4(\mathbb{C})$ and its three gauge parameters.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the involution $\Gamma$ and the $2+2$ split.
