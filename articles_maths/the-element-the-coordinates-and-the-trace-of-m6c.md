# __The Element, the Coordinates and the Trace__

## Introduction

An element of $M_6(\mathbb{C})$ is a $6\times6$ array of complex numbers, a linear map $\mathbb{C}^6\to\mathbb{C}^6$, and a bilinear form on $\mathbb{C}^6$. The three readings are the same object, and each carries its own structures: the coordinates carry the product rule, the linear map carries the rank and the determinant, the bilinear form carries the transpose and the symmetric–alternating split.

The article develops the $36$ complex coordinates, the scalar–traceless split

$$
A=\frac{\operatorname{tr}A}{6}I_6+A_0,
\qquad
\operatorname{tr}A_0=0,
$$

the trace pairing $\langle A,B\rangle=\operatorname{tr}(AB)$, the real and imaginary parts, and the Jordan decomposition $A=S+N$ into commuting semisimple and nilpotent parts. The split is orthogonal for the trace pairing, and the trace pairing is the nondegenerate invariant form that identifies the algebra with its dual.

The article assumes only the definition of the matrix algebra of *The Matrix Algebra $M_6(\mathbb{C})$*. It uses no form and no topology. The Hermitian form $\operatorname{tr}(A^*B)$ is *The Involution and the Hermitian Structure*; the spectral strata are *The Sextic and the Spectral Strata*; the Killing form is *The Matrix Algebra $M_6(\mathbb{C})$*.

## The Coordinates

### The Thirty-Six Coordinates

**Definition.** The **coordinates** of $A\in M_6(\mathbb{C})$ are the $36$ entries $a_{ij}\in\mathbb{C}$, $1\le i,j\le6$. The **matrix units** are

$$
(E_{ij})_{kl}=\delta_{ik}\delta_{jl}.
$$

**Proposition.** The $36$ matrix units form a basis of $M_6(\mathbb{C})$:

$$
A=\sum_{i,j=1}^{6}a_{ij}E_{ij},
$$

and the real dimension is $72$.

**Proof.** The matrix units are linearly independent (the $(i,j)$ entry of a linear combination is its coefficient), and they span (every matrix is its array of entries). Each complex coordinate is two real coordinates.

### The Product Rule

**Theorem.** The product is

$$
(AB)_{ij}=\sum_{k=1}^{6}a_{ik}b_{kj},
$$

and the matrix units multiply by

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

**Proof.** The $(i,j)$ entry of $AB$ is the $i$-th row of $A$ against the $j$-th column of $B$. The matrix unit $E_{ij}$ sends $e_j$ to $e_i$ and kills the other basis vectors; the composition $E_{ij}E_{kl}$ sends $e_l$ to $e_i$ if $j=k$, and to zero otherwise.

**Corollary (the structure constants).** In the basis $E_{ij}$,

$$
E_{ij}E_{kl}=\sum_{m,n}c_{(ij),(kl)}^{(mn)}E_{mn},
\qquad
c_{(ij),(kl)}^{(mn)}=\delta_{jk}\delta_{im}\delta_{ln}.
$$

**Proof.** Compare with $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

**Remark (the product is not commutative).** $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$; the two products are different. The algebra is associative but not commutative.

### The Trace

**Definition.** The **trace** is

$$
\operatorname{tr}A=\sum_{i=1}^{6}a_{ii}.
$$

**Theorem.** The trace is linear, and

$$
\operatorname{tr}(AB)=\sum_{i,j=1}^{6}a_{ij}b_{ji}=\operatorname{tr}(BA),
\qquad
\operatorname{tr}(ABC)=\operatorname{tr}(BCA)=\operatorname{tr}(CAB).
$$

**Proof.** $\operatorname{tr}(AB)=\sum_i\sum_k a_{ik}b_{ki}=\sum_{k,i}b_{ki}a_{ik}=\operatorname{tr}(BA)$; the cyclic property follows by iterating.

**Corollary (the trace in coordinates).** The trace is the contraction of the two indices; the trace pairing is

$$
\operatorname{tr}(AB)=\sum_{i,j}a_{ij}b_{ji}.
$$

**Proof.** Substitute the product rule and set $i=j$.

### The Scalar–Traceless Split

**Theorem.** Every $A$ has a unique decomposition

$$
A=\frac{\operatorname{tr}A}{6}I_6+A_0,
\qquad
\operatorname{tr}A_0=0,
$$

and

$$
M_6(\mathbb{C})=\mathbb{C}I_6\oplus\mathfrak{sl}_6(\mathbb{C}),
\qquad
36=1+35 .
$$

**Proof.** The scalar part is $\frac{1}{6}\operatorname{tr}(A)I_6$; subtracting it gives a traceless matrix. A matrix that is both scalar and traceless is zero, so the sum is direct. The traceless subspace is the kernel of the trace, of dimension $36-1=35$.

**Definition.** The **scalar part** of $A$ is $\frac{1}{6}\operatorname{tr}(A)I_6$; the **traceless part** is $A_0=A-\frac{1}{6}\operatorname{tr}(A)I_6$. The map $A\mapsto A_0$ is the **traceless projection**.

**Theorem (the product rule for the split).** Write $A=\alpha I_6+A_0$, $B=\beta I_6+B_0$ with $\alpha=\frac{1}{6}\operatorname{tr}A$, $\beta=\frac{1}{6}\operatorname{tr}B$. Then

$$
AB=\left(\alpha\beta+\frac{\operatorname{tr}(A_0B_0)}{6}\right)I_6
+\left(\alpha B_0+\beta A_0+A_0B_0-\frac{\operatorname{tr}(A_0B_0)}{6}I_6\right).
$$

**Proof.** Expand $AB=\alpha\beta I_6+\alpha B_0+\beta A_0+A_0B_0$. The trace of $AB$ is $6\alpha\beta+\operatorname{tr}(A_0B_0)$, because $A_0,B_0$ are traceless; the scalar part is $\frac{1}{6}\operatorname{tr}(AB)I_6$. Subtract it from $AB$ to get the traceless part.

**Corollary.** The scalar part of a product depends on the trace pairing $\operatorname{tr}(A_0B_0)$ of the traceless parts; the traceless part is not closed under multiplication, but its projection is.

**Proof.** The formula shows that the scalar part receives the term $\operatorname{tr}(A_0B_0)/6$, and the traceless part receives the correction $-\operatorname{tr}(A_0B_0)I_6/6$.

## The Trace Pairing

### Definition and Nondegeneracy

**Definition.** The **trace pairing** on $M_6(\mathbb{C})$ is

$$
\langle A,B\rangle=\operatorname{tr}(AB).
$$

**Theorem.** The trace pairing is a symmetric bilinear form, and it is nondegenerate:

$$
\langle A,B\rangle=0\ \text{for all }B
\quad\Longrightarrow\quad
A=0 .
$$

**Proof.** Bilinearity and symmetry are those of the trace and the product. If $\langle A,B\rangle=0$ for all $B$, take $B=E_{ji}$; then $\operatorname{tr}(AE_{ji})=a_{ij}$, so every entry of $A$ is zero.

**Corollary (the duality).** The trace pairing identifies $M_6(\mathbb{C})$ with its dual:

$$
A\longmapsto\langle A,\cdot\rangle
$$

is an isomorphism of vector spaces.

**Proof.** A nondegenerate bilinear form on a finite-dimensional space gives an isomorphism with the dual.

### Invariance

**Theorem.** The trace pairing is invariant under left and right multiplication:

$$
\langle AB,C\rangle=\langle A,BC\rangle,
\qquad
\langle AB,C\rangle=\langle B,CA\rangle .
$$

**Proof.** $\operatorname{tr}((AB)C)=\operatorname{tr}(A(BC))$; the second identity is the cyclic property.

**Corollary (the invariant form).** On the simple algebra $\mathfrak{sl}_6$, the trace pairing is the unique invariant bilinear form up to scale; on $\mathfrak{gl}_6$ the invariant forms are spanned by $\operatorname{tr}(XY)$ and $\operatorname{tr}(X)\operatorname{tr}(Y)$. On $\mathfrak{sl}_6$ the trace pairing is the Killing form up to the factor $12$.

**Proof.** The Killing form of $\mathfrak{gl}_6$ is $B(X,Y)=12\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$, and on the traceless subalgebra the second term vanishes, leaving $12\operatorname{tr}(XY)$. The uniqueness is the standard uniqueness of the invariant form on a simple Lie algebra up to scale.

### The Split Is Orthogonal

**Theorem.** The scalar and traceless parts are orthogonal for the trace pairing:

$$
\left\langle \alpha I_6,\ B_0\right\rangle=0
\qquad
(\operatorname{tr}B_0=0),
$$

and

$$
\left\langle \alpha I_6+A_0,\ \beta I_6+B_0\right\rangle
=6\alpha\beta+\operatorname{tr}(A_0B_0).
$$

**Proof.** $\operatorname{tr}(\alpha I_6B_0)=\alpha\operatorname{tr}B_0=0$; the scalar–scalar pairing is $\operatorname{tr}(\alpha\beta I_6)=6\alpha\beta$; the traceless–traceless pairing is $\operatorname{tr}(A_0B_0)$.

**Corollary.** The restriction of the trace pairing to $\mathfrak{sl}_6$ is nondegenerate, and the scalar line is its orthogonal complement.

**Proof.** The whole form is nondegenerate, and the two summands are orthogonal; the restriction to each is therefore nondegenerate.

**Remark (the trace form is not definite).** Over $\mathbb{C}$ the trace pairing is a complex bilinear form; it has isotropic vectors. For example, $E_{12}$ is isotropic: $\operatorname{tr}(E_{12}^2)=\operatorname{tr}(0)=0$. The positive definite form is the Hermitian form $\operatorname{tr}(A^*B)$ of *The Involution and the Hermitian Structure*, not the complex bilinear trace pairing.

## The Element as a Linear Map

### The Action

**Definition.** An element $A\in M_6(\mathbb{C})$ acts on $\mathbb{C}^6$ by

$$
x\longmapsto Ax,
\qquad
(Ax)_i=\sum_j a_{ij}x_j .
$$

**Theorem (the rank–nullity).** The kernel and the image satisfy

$$
\dim\ker A+\dim\operatorname{im}A=6,
\qquad
\operatorname{rank}A=\dim\operatorname{im}A .
$$

The element is invertible if and only if $\ker A=0$, if and only if $\det A\neq0$.

**Proof.** The rank–nullity theorem for a linear map; invertibility is equivalent to trivial kernel, and the determinant is nonzero exactly then.

**Corollary (the two-sided reading).** The same $A$ acts on the left on column vectors and on the right on row vectors:

$$
A:\mathbb{C}^6\longrightarrow\mathbb{C}^6,\qquad
x\longmapsto Ax,
\qquad
A^*:\mathbb{C}^6\longrightarrow\mathbb{C}^6,\qquad
y\longmapsto y^{\mathsf T}A,
$$

and the two actions are the two regular modules of *The Modules and the Minimal Left Ideals*.

**Proof.** The column action is the defining action; the row action is the transpose action on the dual.

### The Element as a Bilinear Form

**Definition.** The **bilinear form of $A$** is

$$
b_A(x,y)=x^{\mathsf T}Ay=\sum_{i,j}a_{ij}x_iy_j .
$$

**Theorem.** The map $A\mapsto b_A$ is an isomorphism $M_6(\mathbb{C})\cong\operatorname{Bil}(\mathbb{C}^6)$; $b_A$ is nondegenerate if and only if $\det A\neq0$; $b_A$ is symmetric if and only if $A=A^{\mathsf T}$; $b_A$ is alternating if and only if $A=-A^{\mathsf T}$.

**Proof.** The entries of $A$ are the values $b_A(e_i,e_j)$; the form determines the matrix and conversely. Nondegeneracy is the nondegeneracy of the matrix. Symmetry is $a_{ij}=a_{ji}$; alternation is $a_{ij}=-a_{ji}$ and $a_{ii}=0$.

**Corollary (the symmetric–alternating split).**

$$
M_6(\mathbb{C})=\operatorname{Sym}^2(\mathbb{C}^6)\oplus\Lambda^2(\mathbb{C}^6),
\qquad
36=21+15,
$$

with

$$
\operatorname{Sym}^2=\{A:A^{\mathsf T}=A\},\qquad
\Lambda^2=\{A:A^{\mathsf T}=-A\}.
$$

The two summands are orthogonal for the trace pairing.

**Proof.** Every matrix is the sum of its symmetric and alternating parts, $A=\frac{1}{2}(A+A^{\mathsf T})+\frac{1}{2}(A-A^{\mathsf T})$. The dimensions are $6\cdot7/2=21$ and $6\cdot5/2=15$. If $A$ is symmetric and $B$ alternating, $\operatorname{tr}(AB)=\operatorname{tr}((AB)^{\mathsf T})=\operatorname{tr}(B^{\mathsf T}A^{\mathsf T})=-\operatorname{tr}(BA)=-\operatorname{tr}(AB)$, so the pairing vanishes.

**Corollary (the quadratic form).** The symmetric part defines the quadratic form

$$
q_A(x)=x^{\mathsf T}Ax=\sum_{i,j}a_{ij}x_ix_j,
$$

and the polarisation identity recovers the symmetric bilinear form.

**Proof.** For a symmetric $A$, $b_A(x,y)=\frac{1}{2}(q_A(x+y)-q_A(x)-q_A(y))$.

### The Two Readings Compared

**Proposition.** Composition of linear maps and multiplication of bilinear forms are related by

$$
b_{AB}(x,y)=b_B(A^{\mathsf T}x,y)=b_A(x,By).
$$

**Proof.** $x^{\mathsf T}ABy=(A^{\mathsf T}x)^{\mathsf T}By=x^{\mathsf T}A(By)$.

**Remark.** The linear-map reading composes on the left; the bilinear-form reading composes on the right through the transpose. The trace is the trace of the linear map; the trace pairing is the bilinear form on the space of maps, not on the carrier.

## The Real and Imaginary Parts

### The Real Structure

**Definition.** Write $A=X+\mathrm iY$ with $X,Y\in M_6(\mathbb{R})$. The **real part** is $X$, the **imaginary part** is $Y$, and the **conjugation** is $\overline A=X-\mathrm iY$.

**Theorem.** $M_6(\mathbb{C})$ is a real vector space of dimension $72$, with the complex structure

$$
J(A)=\mathrm iA,
\qquad
J^2=-I_{72},
$$

and

$$
M_6(\mathbb{C})\cong M_6(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}
$$

as real algebras.

**Proof.** A complex $6\times6$ matrix has $36$ complex entries, each with a real and an imaginary part, so $72$ real coordinates. Multiplication by $\mathrm i$ is a real-linear map with square $-1$. The tensor product identification sends $X\otimes1+\mathrm iY\otimes1$ to $X+\mathrm iY$.

**Corollary (the coordinates).** The $36$ complex coordinates $a_{ij}=x_{ij}+\mathrm iy_{ij}$ give $72$ real coordinates $x_{ij},y_{ij}$; the real and imaginary parts of the trace are

$$
\operatorname{tr}A=\operatorname{tr}X+\mathrm i\operatorname{tr}Y,
$$

and the real and imaginary parts of the product are

$$
AB=(XU-YV)+\mathrm i(XV+YU).
$$

**Proof.** Expand $(X+\mathrm iY)(U+\mathrm iV)$ and use $\mathrm i^2=-1$.

### The Real Forms of the Trace Pairing

**Theorem.** On the real space $M_6(\mathbb{C})$,

$$
\operatorname{Re}\operatorname{tr}(AB)=\operatorname{tr}(XU)-\operatorname{tr}(YV),
\qquad
\operatorname{Im}\operatorname{tr}(AB)=\operatorname{tr}(XV)+\operatorname{tr}(YU).
$$

The real part is a symmetric bilinear form of signature $(36,36)$; the imaginary part is a symmetric bilinear form of split type. The Hermitian form

$$
\operatorname{tr}(A^*B)=\operatorname{tr}(X^{\mathsf T}U)+\operatorname{tr}(Y^{\mathsf T}V)
+\mathrm i\left(\operatorname{tr}(X^{\mathsf T}V)-\operatorname{tr}(Y^{\mathsf T}U)\right)
$$

has positive definite real part.

**Proof.** Expand $\operatorname{tr}((X+\mathrm iY)(U+\mathrm iV))$ and take real and imaginary parts. On $M_6(\mathbb{R})$ the trace form $\operatorname{tr}(XU)$ has signature $(21,15)$ (positive on the symmetric matrices, negative on the alternating ones); the real part on the complexification is the difference of two copies, of signature $(21+15,15+21)=(36,36)$. The Hermitian form has real part $\sum_{ij}(x_{ij}u_{ij}+y_{ij}v_{ij})$, the Euclidean inner product of the $72$ real coordinates.

**Remark (three forms).** The complex bilinear form $\operatorname{tr}(AB)$ is the trace pairing; its real part is indefinite; the Hermitian form $\operatorname{tr}(A^*B)$ is positive definite. The three are different objects, and the article uses the first for the algebra and the third for the Hilbert-space structure.

## The Jordan Decomposition

### Statement

**Theorem (Jordan–Chevalley).** Every $A\in M_6(\mathbb{C})$ has a unique decomposition

$$
A=S+N,
\qquad
SN=NS,
$$

where $S$ is semisimple (diagonalizable over $\mathbb{C}$) and $N$ is nilpotent. Moreover $S$ and $N$ are polynomials in $A$.

**Proof.** Let $\chi_A(t)=\prod_{i=1}^{r}(t-\lambda_i)^{m_i}$ with distinct $\lambda_i$. The Chinese remainder theorem gives a polynomial $S(t)$ of degree less than six with

$$
S(t)\equiv\lambda_i\pmod{(t-\lambda_i)^{m_i}},
\qquad i=1,\dots,r .
$$

Set $S=S(A)$ and $N=A-S$. On the generalized eigenspace of $\lambda_i$, $S$ acts by $\lambda_i$ and $N$ by $A-\lambda_iI$, which is nilpotent of order at most $m_i$. Hence $S$ is semisimple, $N$ is nilpotent, and both are polynomials in $A$, so they commute. Uniqueness: in any decomposition, $S$ commutes with $A$, and on the generalized eigenspace of $\lambda_i$ the semisimple part must act by $\lambda_i$ (the only semisimple element commuting with a nilpotent and with the same spectrum); so $S$ is determined, and $N=A-S$.

**Corollary (the eigenvalues).** The eigenvalues of $S$ are the eigenvalues of $A$, with the same multiplicities; the eigenvalues of $N$ are all zero.

**Proof.** $S$ acts by $\lambda_i$ on the generalized eigenspace; $N$ is nilpotent.

### The Jordan Form

**Theorem.** There is a basis in which

$$
A=\bigoplus_{i=1}^{r}\bigoplus_{j=1}^{s_i}J_{m_{ij}}(\lambda_i),
\qquad
S=\bigoplus_{i=1}^{r}\lambda_iI_{m_i},
\qquad
N=\bigoplus_{i=1}^{r}\bigoplus_{j=1}^{s_i}N_{m_{ij}},
$$

where $J_m(\lambda)=\lambda I_m+N_m$ and $N_m$ is the nilpotent shift.

**Proof.** The Jordan normal form theorem; $S$ is the diagonal part and $N$ the off-diagonal part.

**Corollary (the invariants).** The characteristic polynomial is

$$
\chi_A(t)=\prod_i(t-\lambda_i)^{m_i},
$$

and the minimal polynomial is

$$
m_A(t)=\prod_i(t-\lambda_i)^{\ell_i},
$$

where $\ell_i$ is the size of the largest Jordan block of $\lambda_i$. The semisimple part has minimal polynomial $\prod_i(t-\lambda_i)$.

**Proof.** The characteristic polynomial is the product of the diagonal entries; the minimal polynomial is the least common multiple of the elementary divisors $(t-\lambda_i)^{m_{ij}}$.

### Properties

**Theorem.** The trace and the determinant see only the semisimple part:

$$
\operatorname{tr}S=\operatorname{tr}A,
\qquad
\operatorname{tr}N=0,
\qquad
\det S=\det A .
$$

More generally, every symmetric function of the eigenvalues is the same for $S$ and $A$.

**Proof.** $N$ is nilpotent, so its trace is zero and its determinant is zero; the eigenvalues of $S$ are those of $A$.

**Theorem (functoriality).** For $g\in GL_6(\mathbb{C})$,

$$
gAg^{-1}=(gSg^{-1})+(gNg^{-1})
$$

is the Jordan decomposition of $gAg^{-1}$. For a polynomial $f$,

$$
f(A)=f(S)+\bigl(f(A)-f(S)\bigr)
$$

is the Jordan decomposition of $f(A)$.

**Proof.** Conjugation preserves semisimplicity, nilpotence and commutation. For a polynomial, $f(S)$ is semisimple (functional calculus of a diagonalizable matrix), $f(A)-f(S)$ is nilpotent (it is a polynomial in $N$ with no constant term, by the interpolation), and the two commute.

### The Jordan Decomposition and the Spectral Projectors

**Theorem.** Let $P_i$ be the spectral projector onto the generalized eigenspace of $\lambda_i$, given by the contour integral of *The Sextic and the Spectral Strata*. Then

$$
S=\sum_{i=1}^{r}\lambda_iP_i,
\qquad
N=A-\sum_{i=1}^{r}\lambda_iP_i,
\qquad
\sum_{i=1}^{r}P_i=I_6 .
$$

For a simple spectrum, the $P_i$ are the Lagrange projectors and $N=0$.

**Proof.** The $P_i$ are the projectors onto the generalized eigenspaces, they sum to the identity, and $A$ acts on the $i$-th generalized eigenspace as $\lambda_iI+N_i$; the sum $\sum_i\lambda_iP_i$ is the semisimple part, and the difference is the nilpotent part.

**Corollary (the limit).** The Jordan decomposition is the limit of the spectral decomposition as the eigenvalues coalesce: the semisimple part is the limit of $\sum_i\lambda_iP_i$, and the nilpotent part is the limit of the weighted differences.

**Proof.** The spectral projectors and the spectral sum are continuous in the contour-integral sense; the cluster projectors extend, and the weighted differences converge to the nilpotent part, as in the example of *The Sextic and the Spectral Strata*.

## Summary

An element of $M_6(\mathbb{C})$ has $36$ complex coordinates, $72$ real coordinates, and splits uniquely as

$$
A=\frac{\operatorname{tr}A}{6}I_6+A_0,
\qquad
\operatorname{tr}A_0=0,
$$

with

$$
M_6(\mathbb{C})=\mathbb{C}I_6\oplus\mathfrak{sl}_6(\mathbb{C}),
\qquad
36=1+35 .
$$

The product in coordinates is $(AB)_{ij}=\sum_k a_{ik}b_{kj}$, and the matrix units multiply by $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

$$
\boxed{\ A=\frac{\operatorname{tr}A}{6}I_6+A_0,\qquad \langle A,B\rangle=\operatorname{tr}(AB),\qquad \langle I_6,\mathfrak{sl}_6\rangle=0 .\ }
$$

The trace pairing is symmetric, nondegenerate and invariant; it identifies the algebra with its dual; its restriction to $\mathfrak{sl}_6$ is the Killing form up to the factor $12$. The scalar line and the traceless subspace are orthogonal.

The element is a linear map $x\mapsto Ax$ and a bilinear form $b_A(x,y)=x^{\mathsf T}Ay$. The symmetric and alternating parts give

$$
M_6=\operatorname{Sym}^2\oplus\Lambda^2,
\qquad
36=21+15,
$$

orthogonal for the trace pairing.

The Jordan decomposition is $A=S+N$ with $S$ semisimple, $N$ nilpotent, $SN=NS$, unique, with $S,N$ polynomials in $A$. The semisimple part is $\sum_i\lambda_iP_i$ over the spectral projectors; the nilpotent part is the residue. The trace and the determinant are those of $S$.

| Object | Data |
|---|---|
| Coordinates | $36$ complex, $72$ real |
| Scalar–traceless | $1+35$ |
| Trace pairing | $\operatorname{tr}(AB)$, nondegenerate, invariant |
| Killing form on $\mathfrak{sl}_6$ | $12\operatorname{tr}(AB)$ |
| Symmetric–alternating | $21+15$ |
| Jordan decomposition | $A=S+N$, $SN=NS$ |
| Semisimple part | $\sum_i\lambda_iP_i$ |
| Nilpotent part | $A-S$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a_{ij}$ | the $36$ complex coordinates |
| $E_{ij}$ | the matrix units |
| $A_0$ | the traceless part $A-\frac{1}{6}\operatorname{tr}(A)I_6$ |
| $\langle A,B\rangle$ | the trace pairing $\operatorname{tr}(AB)$ |
| $\mathfrak{sl}_6$ | the traceless subspace, dimension $35$ |
| $b_A$ | the bilinear form $x^{\mathsf T}Ay$ |
| $S,N$ | the semisimple and nilpotent parts of $A$ |
| $P_i$ | the spectral projectors onto the generalized eigenspaces |

## Further Reading

- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the definition, the determinant and the Lie algebra.
- [The Sextic and the Spectral Strata](the-sextic-and-the-spectral-strata-of-m6c.html), for the characteristic polynomial and the spectral projectors.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m6c.html), for the positive definite form $\operatorname{tr}(A^*B)$.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the left and right regular modules.
- [The Polar Decomposition](the-polar-decomposition-of-m6c.html), for the multiplicative analogue of the Jordan decomposition.
- [The Forms, the Norms and the Singular Set](the-forms-the-norms-and-the-singular-set-of-m6c.html), for the Frobenius norm and the definite form.
