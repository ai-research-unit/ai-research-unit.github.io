# __The Element, the Coordinates and the Trace__

## Introduction

**An element of $M_4(\mathbb{C})$ is a linear map of $\mathbb{C}^4$, a matrix of sixteen complex coordinates, a bilinear form, and a pair of real matrices; the trace is the invariant linear functional that reads the scalar part.** This article fixes the element and its coordinates, splits it into the scalar and traceless parts, states the Jordan decomposition, distinguishes the real and imaginary parts of the coordinates from the Hermitian decomposition, and describes the element as a linear map and as a bilinear form.

The algebra is *The Matrix Algebra $M_4(\mathbb{C})$*; the involution and the positive definite form are *The Involution and the Hermitian Structure*; the spectral theory is *Spectral Theory and the Spectral Projectors*; the Peirce decomposition is *The Peirce Decomposition*.

## The Coordinates

**The sixteen coordinates.** In the basis of matrix units,

$$
A=\sum_{i,j=1}^{4}A_{ij}E_{ij}
=\begin{pmatrix}
A_{11}&A_{12}&A_{13}&A_{14}\\
A_{21}&A_{22}&A_{23}&A_{24}\\
A_{31}&A_{32}&A_{33}&A_{34}\\
A_{41}&A_{42}&A_{43}&A_{44}
\end{pmatrix}.
$$

The entries $A_{ij}$ are the **coordinates** of $A$. There are sixteen complex coordinates, hence thirty-two real coordinates.

**The product rule.** The product is

$$
(AB)_{il}=\sum_{j=1}^{4}A_{ij}B_{jl}.
$$

In coordinates, the product is the matrix product; the coordinate of the product is a sum of four products of coordinates. The trace is

$$
\operatorname{tr}(AB)=\sum_{i=1}^{4}(AB)_{ii}=\sum_{i,j=1}^{4}A_{ij}B_{ji}.
$$

**The real and imaginary parts.** Write

$$
A=X+iY,\qquad X,Y\in M_4(\mathbb{R}),
$$

with

$$
X=\frac{A+\bar A}{2},\qquad Y=\frac{A-\bar A}{2i}.
$$

The matrices $X,Y$ are real, and the map $A\mapsto(X,Y)$ is an $\mathbb{R}$-linear isomorphism

$$
M_4(\mathbb{C})\longrightarrow M_4(\mathbb{R})\oplus M_4(\mathbb{R}),
\qquad 32=16+16.
$$

The **real part** is $X$, and the **imaginary part** is $Y$. The real part of the coordinates is not the Hermitian part of the element: the Hermitian part is

$$
\frac{A+A^*}{2}=\frac{X+X^{\mathsf T}}{2}+i\frac{Y-Y^{\mathsf T}}{2},
$$

which involves the transposes of $X$ and $Y$. For example, for $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ (in the upper-left block), $X=A$ is not Hermitian; the Hermitian part is $\begin{pmatrix}0&\frac12\\\frac12&0\end{pmatrix}$.

**The conjugation.** The coordinate conjugation is

$$
\bar A=X-iY,
$$

the entrywise complex conjugate. It is $\mathbb{C}$-antilinear and an automorphism of the real algebra. The conjugate transpose is $A^*=\bar A^{\mathsf T}$, which is the composition of the conjugation and the transpose; it is the subject of *The Involution and the Hermitian Structure*.

## The Scalar and Traceless Parts

**Definition.** The **scalar part** of $A$ is

$$
A_{\mathrm{sc}}=\frac14(\operatorname{tr}A)I,
$$

and the **traceless part** is

$$
A_0=A-\frac14(\operatorname{tr}A)I.
$$

**Proposition.** The decomposition

$$
M_4(\mathbb{C})=\mathbb{C}I\oplus\mathfrak{sl}_4(\mathbb{C}),
\qquad
A=A_{\mathrm{sc}}+A_0,
$$

is direct and canonical. The scalar part is invariant under conjugation, the traceless part is traceless, and the dimensions are

$$
1+15=16.
$$

**Proof.** The trace of $A_{\mathrm{sc}}$ is $\operatorname{tr}A$, and the trace of $A_0$ is $\operatorname{tr}A-\operatorname{tr}A=0$. The intersection $\mathbb{C}I\cap\mathfrak{sl}_4$ is zero because a scalar $\lambda I$ has trace $4\lambda$, which vanishes only if $\lambda=0$. The dimensions add because $\mathfrak{sl}_4$ is the kernel of the trace, of dimension $16-1=15$.

**The trace pairing is orthogonal for the split.** The pairing

$$
\beta(A,B)=\operatorname{tr}(AB)
$$

satisfies

$$
\beta(I,A_0)=\operatorname{tr}(A_0)=0,
$$

so the scalar line is orthogonal to the traceless subspace. The pairing is non-degenerate on each summand: on $\mathbb{C}I$, $\beta(I,I)=4\ne0$; on $\mathfrak{sl}_4$, the restriction is the trace form, which is non-degenerate because the dual of a traceless matrix under $\beta$ is again traceless.

**The trace is the unique invariant linear functional.** If $\varphi:M_4\to\mathbb{C}$ is linear and $\varphi(AB)=\varphi(BA)$ for all $A,B$, then $\varphi=c\operatorname{tr}$. The proof is in *The Matrix Algebra $M_4(\mathbb{C})$*: the commutators span $\mathfrak{sl}_4$, so $\varphi$ vanishes there and is determined by its value on $I$.

## The Trace Pairing

**Definition.** The **trace pairing** is the complex-bilinear form

$$
\beta(A,B)=\operatorname{tr}(AB).
$$

**Proposition.** The pairing is symmetric and non-degenerate:

$$
\beta(A,B)=\beta(B,A),\qquad
\beta(E_{ij},E_{kl})=\delta_{jk}\delta_{il}.
$$

The dual basis of the matrix units is

$$
E_{ij}^{\vee}=E_{ji}.
$$

**Proof.** The symmetry is $\operatorname{tr}(AB)=\operatorname{tr}(BA)$. The value on the units is the product rule: $\operatorname{tr}(E_{ij}E_{kl})=\operatorname{tr}(\delta_{jk}E_{il})=\delta_{jk}\delta_{il}$. The matrix of the pairing in the unit basis is a permutation matrix, hence invertible; the dual of $E_{ij}$ is $E_{ji}$ because $\beta(E_{ij},E_{kl})=\delta_{jk}\delta_{il}$ is $1$ exactly when $(k,l)=(j,i)$.

**The pairing is indefinite.** The trace pairing is not positive definite. For $A=\operatorname{diag}(1,i)$, $\beta(A,A)=\operatorname{tr}(A^2)=1-1=0$ with $A\ne0$. The positive definite form is

$$
\langle A,B\rangle=\operatorname{tr}(A^*B),
$$

which is a different object; it is *The Involution and the Hermitian Structure*.

**The restriction to $\mathfrak{sl}_4$.** On the traceless subspace, the trace pairing is the Killing form up to a scalar. For $\mathfrak{gl}_4$, the Killing form is

$$
K(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

and on $\mathfrak{sl}_4$ the second term vanishes, so

$$
K(X,Y)=8\operatorname{tr}(XY).
$$

The trace pairing is therefore invariant and non-degenerate on $\mathfrak{sl}_4$, and it is the algebraic form behind the Killing form of *The Killing Form*.

**The symmetric and antisymmetric parts.** Every matrix splits as

$$
A=\frac{A+A^{\mathsf T}}{2}+\frac{A-A^{\mathsf T}}{2},
$$

into a symmetric and an antisymmetric part. The symmetric matrices have dimension $10$, the antisymmetric matrices dimension $6$, and

$$
10+6=16.
$$

The trace pairing is orthogonal for this split:

$$
\operatorname{tr}(SK)=0
$$

for $S$ symmetric and $K$ antisymmetric, because $\operatorname{tr}(SK)=\operatorname{tr}((SK)^{\mathsf T})=\operatorname{tr}(K^{\mathsf T}S^{\mathsf T})=-\operatorname{tr}(KS)=-\operatorname{tr}(SK)$.

## The Element as a Linear Map

**The map.** An element $A\in M_4(\mathbb{C})$ is a linear map

$$
A:\mathbb{C}^4\longrightarrow\mathbb{C}^4,\qquad v\longmapsto Av.
$$

Its **kernel** and **image** are

$$
\ker A=\{v:Av=0\},\qquad
\operatorname{im}A=\{Av:v\in\mathbb{C}^4\},
$$

and the rank–nullity theorem gives

$$
\dim\ker A+\operatorname{rank}A=4.
$$

**The rank.** The rank is the dimension of the image and the number of nonzero singular values. It is invariant under left and right multiplication by invertible matrices, and it is the size of the largest nonzero minor. The rank stratification is *The Forms, the Norms and the Singular Set*.

**Invertibility.** The following are equivalent:

- $A$ is invertible;
- $\ker A=0$;
- $\operatorname{rank}A=4$;
- $\det A\ne0$;
- $0$ is not an eigenvalue of $A$.

The inverse is the adjugate divided by the determinant, and the determinant is the product of the eigenvalues.

**The trace and the determinant are invariants of the map.** The matrix of $A$ depends on the basis, but the trace and the determinant do not:

$$
\operatorname{tr}(SAS^{-1})=\operatorname{tr}A,\qquad
\det(SAS^{-1})=\det A.
$$

The trace is the sum of the eigenvalues with algebraic multiplicity, and the determinant is their product. The characteristic polynomial is

$$
\chi_A(t)=\det(tI-A)=t^4-(\operatorname{tr}A)t^3+c_2t^2-c_1t+\det A.
$$

**The element as a bilinear form.** The same matrix defines a complex-bilinear form

$$
B_A:\mathbb{C}^4\times\mathbb{C}^4\longrightarrow\mathbb{C},\qquad
B_A(x,y)=x^{\mathsf T}Ay.
$$

The map $A\mapsto B_A$ is an isomorphism from $M_4$ to the space of bilinear forms. The symmetric part $A^{\mathsf T}=A$ gives a symmetric form, the antisymmetric part $A^{\mathsf T}=-A$ gives an alternating form, and the trace pairing is the contraction

$$
\beta(A,B)=\operatorname{tr}(AB)=\sum_{i,j}A_{ij}B_{ji}.
$$

The bilinear form is not the Hermitian form: $B_A(y,x)=y^{\mathsf T}Ax$ is not $\overline{B_A(x,y)}$ in general. The Hermitian form uses $A^*$, not $A^{\mathsf T}$.

## The Jordan Decomposition

**Theorem (Jordan–Chevalley).** Every $A\in M_4(\mathbb{C})$ has a unique decomposition

$$
A=A_s+A_n,
$$

where $A_s$ is semisimple (diagonalisable over $\mathbb{C}$), $A_n$ is nilpotent, and

$$
A_sA_n=A_nA_s.
$$

Both $A_s$ and $A_n$ are polynomials in $A$ with complex coefficients.

**Proof sketch.** Let

$$
m_A(t)=\prod_{k=1}^{r}(t-\lambda_k)^{m_k}
$$

be the minimal polynomial, with distinct eigenvalues $\lambda_1,\dots,\lambda_r$. The Chinese remainder theorem gives polynomials $p_k(t)$ with

$$
p_k\equiv1\pmod{(t-\lambda_k)^{m_k}},\qquad
p_k\equiv0\pmod{(t-\lambda_l)^{m_l}}\quad(l\ne k).
$$

The projectors $P_k=p_k(A)$ are the spectral projectors onto the generalized eigenspaces, and

$$
A_s=\sum_{k=1}^{r}\lambda_kP_k,\qquad
A_n=A-A_s .
$$

The $P_k$ are polynomials in $A$ and commute with $A$; $A_s$ is diagonalisable with eigenvalues $\lambda_k$; $A_n$ is nilpotent on each generalized eigenspace because $(A-\lambda_kI)^{m_k}=0$ there. Uniqueness follows from the uniqueness of the spectral projectors. The details are in Horn and Johnson, *Matrix Analysis*.

**The Jordan form.** In a suitable basis,

$$
A=\operatorname{diag}(J_{m_1}(\lambda_1),\dots,J_{m_r}(\lambda_r)),
\qquad
J_m(\lambda)=\lambda I_m+N_m,
$$

with $N_m$ the nilpotent shift. The semisimple part is the diagonal $\operatorname{diag}(\lambda_1I_{m_1},\dots,\lambda_rI_{m_r})$, and the nilpotent part is the off-diagonal shift. The trace is

$$
\operatorname{tr}A=\sum_{k=1}^{r}m_k\lambda_k,
$$

and the determinant is

$$
\det A=\prod_{k=1}^{r}\lambda_k^{m_k}.
$$

**Example.** For

$$
A=\begin{pmatrix}
2&1&0&0\\
0&2&0&0\\
0&0&3&0\\
0&0&0&-1
\end{pmatrix}
=\operatorname{diag}(J_2(2),J_1(3),J_1(-1)),
$$

the semisimple part is

$$
A_s=\operatorname{diag}(2,2,3,-1),
$$

and the nilpotent part is

$$
A_n=E_{12}.
$$

The two commute, $A_n^2=0$, and $A=A_s+A_n$. The trace is $2+2+3-1=6$, and the determinant is $2\cdot2\cdot3\cdot(-1)=-12$.

**The Jordan decomposition is not the Peirce decomposition.** The root $H$ is semisimple, and the simple nilpotents $E_{12},E_{23},E_{34}$ are nilpotent. But the sum $H+N$ with $[H,N]=N$ is not the Jordan decomposition of $H+N$: the Jordan parts must commute, and $H$ and $N$ do not. The Peirce decomposition is by the idempotents of $H$; the Jordan decomposition is by the minimal polynomial of the element. The two decompositions are different, and neither refines the other.

**The trace of a nilpotent is zero.** If $N$ is nilpotent, all its eigenvalues are zero, so $\operatorname{tr}N=0$. The trace of a commutator is zero, and the trace of a semisimple element is the sum of its eigenvalues. These facts are used throughout the spectral articles.

## Summary

An element $A\in M_4(\mathbb{C})$ has sixteen complex coordinates $A_{ij}$ in the matrix-unit basis, or thirty-two real coordinates through $A=X+iY$. It splits canonically as $A=\frac14(\operatorname{tr}A)I+A_0$ into a scalar part and a traceless part, of dimensions $1+15=16$, and the trace pairing $\beta(A,B)=\operatorname{tr}(AB)$ is symmetric, non-degenerate and indefinite, orthogonal for the split, and equal to the Killing form up to the factor $8$ on $\mathfrak{sl}_4$. The element is a linear map $\mathbb{C}^4\to\mathbb{C}^4$ with a kernel, an image, a rank, a determinant and a characteristic polynomial, and it is a complex-bilinear form $B_A(x,y)=x^{\mathsf T}Ay$. The Jordan decomposition $A=A_s+A_n$ into commuting semisimple and nilpotent parts exists and is unique, with both parts polynomials in $A$; it is not the Peirce decomposition. The real part $X$ of the coordinates is not the Hermitian part of $A$; the Hermitian part uses $A^*$ and is *The Involution and the Hermitian Structure*.

$$
\boxed{\ A=\frac14(\operatorname{tr}A)I+A_0,\quad \dim\mathbb{C}I=1,\quad \dim\mathfrak{sl}_4=15,\quad A=A_s+A_n,\quad [A_s,A_n]=0,\quad A_n\text{ nilpotent}. }
$$

| Object | Dimension or value |
|---|---|
| Complex coordinates | $16$ |
| Real coordinates | $32$ |
| Scalar part | $1$ |
| Traceless part | $15$ |
| Symmetric matrices | $10$ |
| Antisymmetric matrices | $6$ |
| Trace pairing | symmetric, non-degenerate, indefinite |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{ij}$ | the sixteen complex coordinates |
| $X,Y$ | the real and imaginary parts, $A=X+iY$ |
| $A_{\mathrm{sc}}=\frac14(\operatorname{tr}A)I$ | the scalar part |
| $A_0$ | the traceless part |
| $\beta(A,B)=\operatorname{tr}(AB)$ | the trace pairing |
| $B_A(x,y)=x^{\mathsf T}Ay$ | the bilinear form of $A$ |
| $A_s,A_n$ | the semisimple and nilpotent Jordan parts |
| $\chi_A(t)$ | the characteristic polynomial |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Jordan form, the Jordan–Chevalley decomposition, the trace and the determinant.
- Sheldon Axler, *Linear Algebra Done Right* (Springer, 2015), for the structure of linear maps and the characteristic polynomial.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra, the trace and the determinant.
- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m4c.html), for the positive definite trace form and the Hermitian decomposition.
- [Spectral Theory and the Spectral Projectors](spectral-theory-and-the-spectral-projectors-of-m4c.html), for the spectral projectors and the Dunford calculus.
- [The Peirce Decomposition](the-peirce-decomposition-of-m4c.html), for the idempotent decomposition, which is not the Jordan decomposition.
