# __The Eigenvalue Decomposition of a Matrix__

## Introduction

A matrix $A\in M_n(k)$ has an eigenvalue decomposition when it can be written

$$
A=\sum_{i=1}^{r}\lambda_i P_i,
$$

with $\lambda_1,\dots,\lambda_r$ distinct and $P_1,\dots,P_r$ nonzero idempotent matrices satisfying $P_iP_j=\delta_{ij}P_i$ and $\sum_iP_i=I$. The matrices $P_i$ are the **spectral projections** of $A$; they project onto the generalized eigenspaces of $A$ along the sum of the others. The writing is the matrix case of the eigenvalue decomposition of *The Eigenvalue Decomposition of an Element*, but the matrix case has its own content: the spectral projections can be computed by Lagrange interpolation or by a contour integral of the resolvent, their ranks are the algebraic multiplicities of the eigenvalues, their traces give the trace and the determinant of $A$, and the decomposition of the matrix algebra $M_n(k)$ by the $P_i$ is the Peirce decomposition whose diagonal part contains the centraliser of $A$.

The article separates two statements that are often conflated. The **spectral projections** exist for every matrix whose characteristic polynomial splits, including the non-diagonalisable ones; they are the residues of the resolvent and the idempotents of the primary decomposition. The **eigenvalue decomposition** $A=\sum_i\lambda_iP_i$ exists exactly when the nilpotent part vanishes, that is when $A$ is diagonalisable; otherwise $A=A_s+A_n$ is the Jordan–Chevalley decomposition, with $A_s=\sum_i\lambda_iP_i$ diagonalisable, $A_n$ nilpotent, and $A_nP_i$ the nilpotent part of the $i$-th block. The two statements coincide exactly in the semisimple case.

The article assumes the eigenvalue and diagonalisation theory of *Eigenvalues and Diagonalisation*, the general eigenvalue decomposition of *The Eigenvalue Decomposition of an Element*, the explicit projector formula of *The Lagrange–Sylvester Eigenprojector Formula*, the Jordan–Chevalley decomposition of *Nilpotent Elements and the Jordan–Chevalley Decomposition*, the centraliser and the Peirce decomposition of *The Centraliser and the Diagonal Peirce Part* and *Left and Right Multiplication on the Diagonal Peirce Part*, and the matrix algebra of *Matrix Algebras*. The spectral theorem for Hermitian and normal matrices is *The Eigenvalue Decomposition of a Self-Adjoint Element* and *Unitary Elements and Their Algebraic Decompositions*; the positivity and the orthogonality of the eigenvectors belong to Part II.

Throughout, $k$ is a field, $n\ge1$, $A\in M_n(k)$, and $V=k^n$ is the space on which $A$ acts. The characteristic polynomial is $c_A(x)=\det(xI-A)$, the minimal polynomial is $m_A(x)$, and the distinct eigenvalues are $\lambda_1,\dots,\lambda_r$. The algebraic multiplicity of $\lambda_i$ is the exponent $m_i$ of $x-\lambda_i$ in $c_A$, and the geometric multiplicity is $g_i=\dim\ker(A-\lambda_iI)$. The spectral projections are written $P_i$; the matrix units are $E_{ij}$. The field is assumed to contain the eigenvalues when the spectral projections are discussed; over a general field this means passing to a splitting field, and the decomposition over $k$ exists when $c_A$ splits over $k$.

## The Spectral Projections

### Construction by interpolation

Suppose first that $A$ is diagonalisable, so that $m_A(x)=\prod_{i=1}^{r}(x-\lambda_i)$ with the $\lambda_i$ distinct. The **spectral projection** of $\lambda_i$ is

$$
P_i=\prod_{j\neq i}\frac{A-\lambda_jI}{\lambda_i-\lambda_j}.
$$

The product is the Lagrange polynomial of *The Lagrange–Sylvester Eigenprojector Formula* evaluated at $A$. The $P_i$ are polynomials in $A$, hence commute with $A$ and with one another; they satisfy

$$
P_i^2=P_i, \qquad P_iP_j=0 \ (i\neq j), \qquad \sum_{i=1}^{r}P_i=I,
$$

and $AP_i=P_iA=\lambda_iP_i$. The last identity is the reason for the name: on the image of $P_i$, the matrix $A$ acts as the scalar $\lambda_i$.

*Proof.* The Lagrange polynomial $h_i(x)=\prod_{j\neq i}(x-\lambda_j)/(\lambda_i-\lambda_j)$ satisfies $h_i(\lambda_j)=\delta_{ij}$, and $h_i(A)h_k(A)=(h_ih_k)(A)$ because the polynomials commute. The product $h_ih_k$ has the values $\delta_{ij}\delta_{kj}$ at the $r$ eigenvalues; its reduction modulo the squarefree polynomial $m_A$ is the interpolation polynomial of those values, because the evaluation map $k[x]/(m_A)\to k^r$ is an isomorphism. That interpolation polynomial is $\delta_{ik}h_i$, so $P_iP_k=\delta_{ik}P_i$. The sum $\sum_ih_i$ reduces modulo $m_A$ to the interpolation polynomial of the constant $1$, so $\sum_iP_i=I$. Finally, $xh_i(x)-\lambda_ih_i(x)$ vanishes at every eigenvalue, hence is divisible by $m_A$, so $AP_i-\lambda_iP_i=0$.

### Construction by the resolvent

The interpolation formula needs distinct eigenvalues. The resolvent gives a construction that survives the repeated case. For $z$ not an eigenvalue, the **resolvent** is $R(z)=(zI-A)^{-1}$.

**Theorem (partial fractions).** Let $A$ have the spectral projections $P_1,\dots,P_r$ of the diagonalisable case. Then

$$
(zI-A)^{-1}=\sum_{i=1}^{r}\frac{P_i}{z-\lambda_i}
$$

for every $z$ not an eigenvalue.

*Proof.* Multiply the right side by $zI-A=\sum_i(z-\lambda_i)P_i$. The product is $\sum_iP_i=I$, using the orthogonality. The two sides are rational matrix functions with the same poles and the same product with $zI-A$; hence they are equal wherever both are defined.

**Corollary (contour formula).** Over $k=\mathbb{C}$, let $\gamma_i$ be a small positively oriented circle around $\lambda_i$ enclosing no other eigenvalue. Then

$$
P_i=\frac{1}{2\pi i}\oint_{\gamma_i}(zI-A)^{-1}\,dz.
$$

*Proof.* Integrate the partial fraction over $\gamma_i$. The term $P_i/(z-\lambda_i)$ has residue $P_i$; every other term is holomorphic inside $\gamma_i$.

**Remark.** The contour formula defines the spectral projection for every matrix over $\mathbb{C}$, including the non-diagonalisable ones. The integral is the residue at $\lambda_i$ of the resolvent; it is the matrix analogue of the Cauchy integral formula for the eigenprojectors. The formula is the starting point of the holomorphic functional calculus of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Resolvent and the Contour Integral*.

### The primary decomposition

For a general matrix over a splitting field, the **primary decomposition** is

$$
V=\bigoplus_{i=1}^{r}V_i, \qquad V_i=\ker(A-\lambda_iI)^{m_i}=\ker(A-\lambda_iI)^{e_i},
$$

where $m_i$ is the algebraic multiplicity and $e_i$ is the multiplicity of $\lambda_i$ in the minimal polynomial. The equality of the two kernels holds because $e_i\le m_i$ and the nilpotent index of $A-\lambda_iI$ on $V_i$ is $e_i$. The subspaces $V_i$ are the **generalized eigenspaces**, they are stable under $A$, and the restriction of $A-\lambda_iI$ to $V_i$ is nilpotent of index $e_i$. The **spectral projection** $P_i$ is the projection onto $V_i$ along the sum of the other $V_j$. It is a polynomial in $A$ (the Chinese remainder idempotent of the primary factors $(x-\lambda_j)^{e_j}$ of $m_A$), it satisfies the orthogonality and resolution identities, and it commutes with $A$.

**Theorem.** Let $A$ have the primary decomposition over a splitting field. Then the spectral projections $P_i$ exist, are polynomials in $A$, satisfy

$$
\boxed{\;P_i^2=P_i, \qquad P_iP_j=\delta_{ij}P_i, \qquad \sum_iP_i=I\;},
$$

and the matrix

$$
A_s=\sum_{i=1}^{r}\lambda_iP_i
$$

is diagonalisable, the matrix $A_n=A-A_s$ is nilpotent, and $A_sA_n=A_nA_s$. The decomposition $A=A_s+A_n$ is the Jordan–Chevalley decomposition of $A$.

*Proof.* The Chinese remainder theorem applied to the factorization $m_A=\prod_i(x-\lambda_i)^{e_i}$ gives idempotents $P_i\in k[A]$ with $P_i\equiv1\pmod{(x-\lambda_i)^{e_i}}$ and $P_i\equiv0\pmod{(x-\lambda_j)^{e_j}}$ for $j\neq i$. They satisfy the orthogonality and resolution identities. On $V_i$, $A-\lambda_iI$ is nilpotent, so $A_s=\lambda_iI$ on $V_i$ and $A_n=A-\lambda_iI$ is nilpotent there; summing over $i$ gives $A_s$ diagonalisable with the distinct eigenvalues $\lambda_i$ and $A_n$ nilpotent. The two commute because both are polynomials in $A$. The uniqueness is that of the Jordan–Chevalley decomposition.

**Corollary.** The eigenvalue decomposition $A=\sum_i\lambda_iP_i$ exists exactly when $A_n=0$, that is exactly when $A$ is diagonalisable.

*Proof.* If $A_n=0$, then $A=A_s=\sum_i\lambda_iP_i$ is the eigenvalue decomposition. Conversely, if $A$ has an eigenvalue decomposition, then $m_A$ is split with distinct roots by *The Eigenvalue Decomposition of an Element*, so $A$ is diagonalisable, and the uniqueness of the Jordan–Chevalley decomposition gives $A_n=0$.

## Rank, Trace and Determinant

### The rank is the algebraic multiplicity

**Theorem.** Let $P_i$ be the spectral projection of $\lambda_i$ in the primary decomposition. Then

$$
\operatorname{rk}P_i=m_i, \qquad \operatorname{Tr}P_i=m_i,
$$

where $m_i$ is the algebraic multiplicity of $\lambda_i$. Consequently

$$
\boxed{\;\operatorname{Tr}A=\sum_{i=1}^{r}\lambda_im_i, \qquad \det A=\prod_{i=1}^{r}\lambda_i^{m_i}\;}.
$$

*Proof.* The projection $P_i$ is the identity on $V_i$ and zero on $V_j$ for $j\neq i$. Hence its rank is $\dim V_i=m_i$, and its trace is the trace of the identity on $V_i$, which is $m_i$. On $V_i$ the matrix has the form $\lambda_iI+N_i$ with $N_i$ nilpotent, so its trace is $\lambda_im_i$ and its determinant is $\lambda_i^{m_i}$; the trace and the determinant of $A$ are the sum and the product of the contributions of the primary blocks.

**Corollary.** The characteristic polynomial is

$$
c_A(x)=\prod_{i=1}^{r}(x-\lambda_i)^{m_i}=\prod_{i=1}^{r}(x-\lambda_i)^{\operatorname{rk}P_i}.
$$

**Remark.** The theorem is the matrix form of the statement that the spectral projection of an eigenvalue carries its algebraic multiplicity. In the diagonalisable case, $m_i$ is also the dimension of the eigenspace $V_i=\ker(A-\lambda_iI)$; in the non-diagonalisable case, the eigenspace is a proper subspace of the generalized eigenspace, and its dimension $g_i$ is smaller than $m_i$. The difference $m_i-g_i$ measures the nilpotent part of the block.

### The geometric multiplicity

**Proposition.** Let $g_i=\dim\ker(A-\lambda_iI)$ be the geometric multiplicity. Then

$$
1\le g_i\le m_i,
$$

and $g_i=m_i$ for every $i$ exactly when $A$ is diagonalisable.

*Proof.* The eigenspace is contained in the generalized eigenspace, so $g_i\le m_i$; it is nonzero because $\lambda_i$ is an eigenvalue. If $g_i=m_i$, the eigenspace equals the generalized eigenspace for every $i$, and the sum of the eigenspaces is $V$; conversely, if $A$ is diagonalisable, the generalized eigenspace is the eigenspace.

**Corollary.** $A$ is diagonalisable if and only if $m_A$ has distinct roots, if and only if $A_s=A$, if and only if the spectral projections have rank equal to the geometric multiplicities.

*Proof.* The equivalence of the first three is the criterion of *Eigenvalues and Diagonalisation* and the Jordan–Chevalley decomposition above. The last is the proposition.

**Remark.** The geometric multiplicity is the number of Jordan blocks of $\lambda_i$, and the algebraic multiplicity is the sum of their sizes. The spectral projection $P_i$ sees the generalized eigenspace but not the block sizes: two matrices with the same characteristic polynomial and the same generalized eigenspaces but different Jordan block sizes have the same spectral projections. The block sizes are the data of the nilpotent part $A_nP_i$, not of $A_s$.

## The Block Form and the Peirce Decomposition

### The adapted basis

Choose a basis of $V$ adapted to the primary decomposition $V=\bigoplus_iV_i$, with the first $m_1$ vectors a basis of $V_1$, the next $m_2$ a basis of $V_2$, and so on. In this basis,

$$
A=\begin{pmatrix}A_1&0&\cdots&0\\0&A_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&A_r\end{pmatrix}, \qquad
P_i=\begin{pmatrix}0&&&\\&\ddots&&\\&&I_{m_i}&\\&&&\ddots&\\&&&0\end{pmatrix},
$$

where $A_i$ is an $m_i\times m_i$ matrix with the single eigenvalue $\lambda_i$, and $P_i$ is the identity on the $i$-th block and zero elsewhere. The matrices $A_i$ are the **primary blocks** of $A$.

### The Peirce decomposition of the matrix algebra

The spectral projections give the Peirce decomposition of the algebra $M_n(k)$:

$$
M_n(k)=\bigoplus_{i,j=1}^{r}P_iM_n(k)P_j, \qquad P_iM_n(k)P_j=\{X:P_iX=X, XP_j=X\}.
$$

The corner $P_iM_nP_i$ is isomorphic to $M_{m_i}(k)$: in the adapted basis it consists of the matrices that are zero outside the $i$-th block. The off-diagonal corner $P_iM_nP_j$ consists of the matrices that map $V_j$ into $V_i$ and annihilate the other $V_l$; its dimension is $m_im_j$. The dimensions add up:

$$
\dim M_n(k)=n^2=\sum_{i,j=1}^{r}m_im_j=\left(\sum_i m_i\right)^2.
$$

**Theorem.** In the adapted basis, the diagonal Peirce part

$$
D=\bigoplus_{i=1}^{r}P_iM_n(k)P_i
$$

is the algebra of block-diagonal matrices, of dimension $\sum_i m_i^2$. It contains the centraliser $C(A)=\{X:AX=XA\}$, and it equals the centraliser exactly when $A$ is diagonalisable. In that case the off-diagonal part is the image of the commutator operator $\operatorname{ad}_A(X)=AX-XA$, and

$$
\boxed{\;M_n(k)=C(A)\oplus\operatorname{im}\operatorname{ad}_A\;} .
$$

*Proof.* A matrix commuting with $A$ preserves each generalized eigenspace $V_i$, because $V_i$ is the kernel of $(A-\lambda_iI)^{m_i}$ and $X(A-\lambda_iI)^{m_i}=(A-\lambda_iI)^{m_i}X$. Hence it is block diagonal, so $C(A)\subseteq D$. If $A$ is diagonalisable, $A=\lambda_iI$ on each $V_i$, and every block-diagonal matrix commutes with $A$, so $C(A)=D$. Conversely, if $C(A)=D$, then every matrix of the corner $P_iM_nP_i$ commutes with $A$. The corner is isomorphic to $M_{m_i}(k)$ and acts faithfully on $V_i$; the only matrices commuting with all endomorphisms of $V_i$ are the scalars, so $A$ is scalar on $V_i$ for every $i$, and $A$ is diagonalisable. In the diagonalisable case $\operatorname{ad}_A$ acts on $P_iM_nP_j$ by multiplication by $\lambda_i-\lambda_j$, which is nonzero for $i\neq j$; hence the kernel is the diagonal part $D=C(A)$ and the image is the off-diagonal part, and the decomposition follows from the rank–nullity theorem.

**Remark.** In the non-diagonalisable case the centraliser is strictly smaller than the diagonal Peirce part whenever some nilpotent part $N_i$ is nonzero, and the image of $\operatorname{ad}_A$ is not a complement of the centraliser. The Jordan block $J=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ is the smallest example: $D=M_2(k)$, the centraliser is $k[J]$, of dimension $2$, and the image of $\operatorname{ad}_J$ is the set of matrices $\begin{pmatrix}c&e\\0&-c\end{pmatrix}$, which meets $k[J]$ in the strictly upper triangular matrices. The sum is not direct and does not fill $M_2(k)$. The Peirce decomposition is treated in *The Centraliser and the Diagonal Peirce Part* and *Left and Right Multiplication on the Diagonal Peirce Part*; the matrix case is the concrete model.

### The corner dimensions

The diagonal corner $P_iM_nP_i$ has dimension $m_i^2$, the off-diagonal corner $P_iM_nP_j$ has dimension $m_im_j$, and the sum is $n^2$. If $A$ is diagonalisable with distinct eigenvalues, then $m_i=1$ for all $i$ and the $P_i$ are the rank-one projections onto the eigenspaces; the diagonal corners are one-dimensional, and the off-diagonal corners are one-dimensional as well. If $A$ has a repeated eigenvalue, the corresponding corner is larger, and the spectral projection does not distinguish the individual eigenvectors inside the eigenspace.

## The Jordan–Chevalley Decomposition

### The semisimple and nilpotent parts

The decomposition $A=A_s+A_n$ of §*The primary decomposition* is the **Jordan–Chevalley decomposition**: $A_s$ is diagonalisable (semisimple), $A_n$ is nilpotent, and $A_sA_n=A_nA_s$. It is unique. In the adapted basis, $A_s=\operatorname{diag}(\lambda_1I_{m_1},\dots,\lambda_rI_{m_r})$ and $A_n=\operatorname{diag}(N_1,\dots,N_r)$ with $N_i=A_i-\lambda_iI_{m_i}$ nilpotent.

**Theorem.** The following are equivalent:

1. $A$ has an eigenvalue decomposition;
2. $A$ is diagonalisable;
3. $A_n=0$;
4. $m_A$ has distinct roots;
5. the spectral projections have rank equal to the geometric multiplicities.

*Proof.* The equivalence of 1 and 2 is the corollary of §*The primary decomposition*; the equivalence of 2, 3 and 4 is the criterion of *Eigenvalues and Diagonalisation* and the uniqueness of the Jordan–Chevalley decomposition; the equivalence of 2 and 5 is the proposition of §*The geometric multiplicity*.

### The Jordan form

The nilpotent part $A_n$ is not determined by the spectral projections alone; its Jordan block sizes are the **Jordan invariants** of $A$. The Jordan form is

$$
A\sim\bigoplus_{i=1}^{r}\bigoplus_{k=1}^{s_i}J_{m_{i,k}}(\lambda_i),
$$

where $J_m(\lambda)$ is the $m\times m$ Jordan block with eigenvalue $\lambda$, the $m_{i,k}$ are the block sizes, $\sum_k m_{i,k}=m_i$, and $s_i=g_i$ is the number of blocks. The spectral projection $P_i$ is the identity on the sum of the blocks of $\lambda_i$ and zero on the others; it does not see the individual block sizes. The sizes are the data of $A_nP_i$, or equivalently of the ranks of the powers $(A-\lambda_iI)^k$.

**Proposition.** For the eigenvalue $\lambda_i$, the number of Jordan blocks of size at least $k$ is

$$
\operatorname{rk}(A-\lambda_iI)^{k-1}-\operatorname{rk}(A-\lambda_iI)^k,
$$

and the number of blocks of size exactly $k$ is the difference of these numbers for $k$ and $k+1$.

*Proof.* On a Jordan block of size $m$, the rank of $(J_m(0))^{k-1}$ minus the rank of $(J_m(0))^k$ is $1$ for $k\le m$ and $0$ for $k>m$; summing over the blocks gives the count.

**Remark.** The proposition is the standard way to read the Jordan form from the ranks of the powers of $A-\lambda_iI$. It is also the concrete form of the statement that the spectral projection sees the generalized eigenspace but not its nilpotent structure.

## The Functional Calculus

### Polynomials

**Theorem.** Let $A$ be diagonalisable with spectral projections $P_i$. Then for every polynomial $f\in k[x]$,

$$
f(A)=\sum_{i=1}^{r}f(\lambda_i)P_i .
$$

*Proof.* The identity holds for $f=x$ by the eigenvalue decomposition, and both sides are linear in $f$ and multiplicative: $f(A)g(A)=(fg)(A)$ and $\sum_i f(\lambda_i)P_i\sum_jg(\lambda_j)P_j=\sum_i f(\lambda_i)g(\lambda_i)P_i$. Hence it holds for every polynomial.

**Corollary (spectral mapping).** The eigenvalues of $f(A)$ are $f(\lambda_1),\dots,f(\lambda_r)$, with the algebraic multiplicity of $f(\lambda_i)$ equal to the sum of the $m_j$ over the $j$ with $f(\lambda_j)=f(\lambda_i)$. If $f$ is injective on the spectrum, the spectral projections of $f(A)$ are the same $P_i$.

*Proof.* The formula gives $f(A)P_i=f(\lambda_i)P_i$ and $f(A)=\sum_if(\lambda_i)P_i$; the distinct values of $f(\lambda_i)$ are the eigenvalues, and the projector of a value is the sum of the $P_i$ over the preimage. If $f$ is injective, each preimage is a singleton.

### The resolvent and the exponential

The partial fraction of the resolvent gives, for $z$ not an eigenvalue,

$$
(zI-A)^{-1}=\sum_i\frac{P_i}{z-\lambda_i},
$$

and the matrix exponential is

$$
e^{tA}=\sum_i e^{t\lambda_i}P_i
$$

in the diagonalisable case. More generally, the holomorphic functional calculus is

$$
f(A)=\sum_{i=1}^{r}\frac{1}{2\pi i}\oint_{\gamma_i}f(z)(zI-A)^{-1}\,dz,
$$

with $\gamma_i$ a small circle around $\lambda_i$; the integral is the sum of the residues, and in the repeated case it produces the Hermite interpolation terms of *The Lagrange–Sylvester Eigenprojector Formula*, §*The Repeated-Root Case*.

**Remark.** The functional calculus is the matrix form of the Chinese remainder decomposition: the algebra $k[A]$ is isomorphic to $\prod_i k[x]/((x-\lambda_i)^{e_i})$, and the spectral projection $P_i$ is the image of the $i$-th standard idempotent. In the diagonalisable case the factors are the fields $k$ and the calculus is evaluation at the eigenvalues; in the repeated case the factors are the truncated polynomial algebras and the calculus is Hermite interpolation.

## Examples

### Distinct eigenvalues

For

$$
A=\begin{pmatrix}1&1\\0&2\end{pmatrix},
$$

the eigenvalues are $1$ and $2$, and the spectral projections are

$$
P_1=\frac{A-2I}{1-2}=2I-A=\begin{pmatrix}1&-1\\0&0\end{pmatrix}, \qquad
P_2=\frac{A-I}{2-1}=A-I=\begin{pmatrix}0&1\\0&1\end{pmatrix}.
$$

Both have rank one and trace one, $P_1+P_2=I$, $P_1P_2=0$, and $A=1\cdot P_1+2\cdot P_2$. The trace is $1+2=3$, the determinant is $1\cdot2=2$, and the characteristic polynomial is $(x-1)(x-2)$.

### A repeated eigenvalue, diagonalisable

For

$$
A=\operatorname{diag}(2,2,3),
$$

the distinct eigenvalues are $2$ and $3$, and the spectral projections are

$$
P_2=E_{11}+E_{22}, \qquad P_3=E_{33}.
$$

The ranks are $2$ and $1$, the traces are $2$ and $1$, and $A=2P_2+3P_3$. The characteristic polynomial is $(x-2)^2(x-3)$, the trace is $2\cdot2+3=7$, and the determinant is $2^2\cdot3=12$. The eigenspace of $2$ has dimension two, equal to its algebraic multiplicity; the matrix is diagonalisable, and the spectral projection of $2$ is the projection onto the whole eigenspace.

### A Jordan block, not diagonalisable

For

$$
J=\begin{pmatrix}1&1\\0&1\end{pmatrix},
$$

the characteristic polynomial is $(x-1)^2$, the only eigenvalue is $1$, and the spectral projection is $P_1=I$: the generalized eigenspace is the whole space. The semisimple part is $J_s=1\cdot I=I$, the nilpotent part is

$$
J_n=J-I=\begin{pmatrix}0&1\\0&0\end{pmatrix}, \qquad J_n^2=0,
$$

and $J=J_s+J_n$ is the Jordan–Chevalley decomposition. The eigenvalue decomposition $J=1\cdot I$ is false; the spectral projection is the identity, but the coefficient is not the whole matrix. The geometric multiplicity of $1$ is $1$, the algebraic multiplicity is $2$, and the defect $m_1-g_1=1$ is the size of the nilpotent part.

### A rotation over the reals

For

$$
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$

over $k=\mathbb{R}$, the characteristic polynomial is $x^2+1$, which does not split; there is no real eigenvalue and no real spectral projection. Over $\mathbb{C}$ the eigenvalues are $i$ and $-i$, and the spectral projections are

$$
P_i=\frac{R+iI}{2i}=\frac12\begin{pmatrix}1&i\\-i&1\end{pmatrix}, \qquad
P_{-i}=\frac{R-iI}{-2i}=\frac12\begin{pmatrix}1&-i\\i&1\end{pmatrix}.
$$

Both have rank one and trace one, and $R=iP_i+(-i)P_{-i}$. The example is the matrix form of the second-kind self-adjoint pair of *The Eigenvalue Decomposition of a Self-Adjoint Element*: the real matrix is self-adjoint for the entrywise conjugation, the eigenvalues are exchanged by the conjugation, and the real form of the pair is the rotation.

### A rank-one matrix

Let $A=uv^{\mathsf T}$ with $u,v\in k^n$, $n\ge2$, and $\tau=v^{\mathsf T}u\neq0$. Then $A^2=\tau A$, so the minimal polynomial is $x(x-\tau)$ and the eigenvalues are $\tau$ and $0$. The spectral projections are

$$
P_\tau=\frac{A}{\tau}, \qquad P_0=I-\frac{A}{\tau},
$$

of ranks $1$ and $n-1$. The trace is $\tau$, the determinant is $0$, and the eigenvalue decomposition is $A=\tau P_\tau+0\cdot P_0$. The example is the smallest nontrivial spectral decomposition with a rank-one projection.

### A permutation matrix

Let $\sigma$ be the $3$-cycle and let $C$ be the permutation matrix of $\sigma$. Then $C^3=I$, the eigenvalues are the cube roots of unity, and the spectral projections are the Lagrange projectors of $x^3-1$. They are the matrix form of the group algebra example of *Unitary Elements and Their Algebraic Decompositions*: the permutation matrix is unitary for the transpose, the eigenvalues are not unimodular for the trivial involution, and the spectral projections of the non-real characters are exchanged by the transpose. The example shows that the spectral decomposition over $\mathbb{C}$ can be perfectly regular while the real form has no eigenvalue decomposition over $\mathbb{R}$.

## Summary

A matrix $A\in M_n(k)$ has spectral projections $P_i$ onto its generalized eigenspaces whenever its characteristic polynomial splits. The projections are polynomials in $A$, orthogonal, and sum to the identity; they can be computed by Lagrange interpolation when the eigenvalues are distinct and by the contour integral of the resolvent in general. Their ranks and traces are the algebraic multiplicities $m_i$, so $\operatorname{Tr}A=\sum_i\lambda_im_i$ and $\det A=\prod_i\lambda_i^{m_i}$. The eigenvalue decomposition $A=\sum_i\lambda_iP_i$ exists exactly when the nilpotent part $A_n=A-\sum_i\lambda_iP_i$ vanishes, that is exactly when $A$ is diagonalisable; in general $A=A_s+A_n$ is the Jordan–Chevalley decomposition, with $A_s=\sum_i\lambda_iP_i$ diagonalisable and $A_n$ nilpotent. The spectral projections give the Peirce decomposition $M_n(k)=\bigoplus_{i,j}P_iM_nP_j$, whose diagonal part contains the centraliser of $A$ and equals it exactly in the diagonalisable case. The matrix case is the concrete model of *The Eigenvalue Decomposition of an Element*, *The Lagrange–Sylvester Eigenprojector Formula*, *Nilpotent Elements and the Jordan–Chevalley Decomposition* and *The Centraliser and the Diagonal Peirce Part*; the diagonalisation theory is *Eigenvalues and Diagonalisation*, and the matrix algebra is *Matrix Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A\in M_n(k)$ | the matrix |
| $c_A(x)=\det(xI-A)$ | the characteristic polynomial |
| $m_A(x)$ | the minimal polynomial |
| $\lambda_1,\dots,\lambda_r$ | the distinct eigenvalues |
| $m_i$ | the algebraic multiplicity of $\lambda_i$ |
| $g_i=\dim\ker(A-\lambda_iI)$ | the geometric multiplicity |
| $V_i=\ker(A-\lambda_iI)^{m_i}$ | the generalized eigenspace |
| $P_i$ | the spectral projection onto $V_i$ |
| $A_s=\sum_i\lambda_iP_i$ | the semisimple part |
| $A_n=A-A_s$ | the nilpotent part |
| $J_m(\lambda)$ | the Jordan block of size $m$ and eigenvalue $\lambda$ |
| $E_{ij}$ | the matrix units |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the spectral projections, the resolvent and the Jordan form.
- Peter Lancaster and Miron Tismenetsky, *The Theory of Matrices* (Academic Press, second edition, 1985), for the contour integral of the resolvent and the functional calculus.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition of a finite-dimensional algebra and its matrix case.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Invariant Subspaces of Matrices with Applications* (Wiley, 1986), for the primary decomposition and the spectral projections in the non-diagonalisable case.
