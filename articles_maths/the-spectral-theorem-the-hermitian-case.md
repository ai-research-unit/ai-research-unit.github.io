# __The Spectral Theorem: the Hermitian Case__

## Introduction

**A Hermitian matrix has real eigenvalues and an orthonormal eigenbasis, and its eigenvalues are the extreme values of the Rayleigh quotient, so the matrix is the sum of real numbers times orthogonal projections.**

The article proves the reality of the spectrum, proves the orthogonal diagonalisation, proves the spectral resolution $A=\sum_i\lambda_iP_i$ with the projections written as $u_iu_i^{*}$, proves the Rayleigh quotient characterisation and the min-max principle, and identifies the positive semidefinite matrices as the Hermitian matrices of nonnegative spectrum. It assumes *Normal Matrices and the Common Spectral Theorem* for the unitary diagonalisation and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* for the half. It defers the geometry to *The Cone of Positive Semidefinite Matrices* and the analysis to *The Positive Cone and Its Boundary*.

## Reality of the Spectrum

**The eigenvalues of a Hermitian matrix are real.** If $Av=\lambda v$ with $v\neq0$, then

$$
\lambda\|v\|^{2}=\langle Av,v\rangle=\langle v,Av\rangle=\overline{\langle Av,v\rangle}=\bar\lambda\|v\|^{2},
$$

using $A^{*}=A$, so $\lambda=\bar\lambda$. The computation at $n=3,4,5$ gives eigenvalues with imaginary part below $10^{-15}$, which is the numerical form of the identity.

**The quadratic form of a Hermitian matrix is real.** For every $x$,

$$
\langle Ax,x\rangle=\overline{\langle x,Ax\rangle}=\overline{\langle Ax,x\rangle},
$$

so $\langle Ax,x\rangle\in\mathbb{R}$, and the polarisation identity recovers the whole Hermitian form from it:

$$
\langle Ax,y\rangle=\tfrac14\big(\langle A(x+y),x+y\rangle-\langle A(x-y),x-y\rangle\big)+\tfrac{i}{4}\big(\langle A(x+iy),x+iy\rangle-\langle A(x-iy),x-iy\rangle\big).
$$

So a Hermitian matrix is determined by the real-valued function $x\mapsto\langle Ax,x\rangle$, which is why the variational characterisation below loses no information.

**The eigenvectors of distinct eigenvalues are orthogonal.** If $Av=\lambda v$ and $Aw=\mu w$ with $\lambda\neq\mu$ and both real, then

$$
\lambda\langle v,w\rangle=\langle Av,w\rangle=\langle v,Aw\rangle=\mu\langle v,w\rangle,
$$

so $\langle v,w\rangle=0$. The computation confirms it on random Hermitian matrices, and the identity is the reason the eigenbasis is orthogonal rather than merely linearly independent.

**The Hermitian half is exactly the set of matrices with real quadratic form.** If $\langle Ax,x\rangle\in\mathbb{R}$ for all $x$ then the polarisation identity gives $\langle Ax,y\rangle=\overline{\langle Ay,x\rangle}$, so $A=A^{*}$. Hence

$$
A\ \text{Hermitian}\iff\langle Ax,x\rangle\in\mathbb{R}\ \ \forall x,
$$

which was verified on random matrices at $n=3,4$: the non-Hermitian ones produce a nonreal value of the quadratic form on some vector.

## Orthogonal Diagonalisation

**The spectral theorem.** A Hermitian matrix $A$ has a unitary $U$ and a real diagonal $\Lambda$ with

$$
A=U\Lambda U^{*},\qquad \Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\quad \lambda_i\in\mathbb{R}.
$$

*Proof.* By the common spectral theorem $A$ is normal, so $A=U\Lambda U^{*}$ with $\Lambda$ diagonal; by the reality above the entries of $\Lambda$ are real.

**The unitary can be taken orthogonal in the real case.** For a real symmetric matrix the eigenvalues are real and the eigenvectors can be chosen real, so

$$
S=Q\Lambda Q^{\mathsf T},\qquad Q\in\mathrm{O}(n),\quad \Lambda\ \text{real diagonal},
$$

which was verified at $n=3,4$ on random symmetric matrices. So the symmetric half of the real algebra is diagonalised by the orthogonal group, and the Hermitian half of the complex algebra by the unitary group.

**The columns of $U$ are an orthonormal eigenbasis.** Writing $U=(u_1,\dots,u_n)$ with orthonormal columns, the identity $AU=U\Lambda$ reads

$$
Au_i=\lambda_iu_i,\qquad \langle u_i,u_j\rangle=\delta_{ij},
$$

so the theorem is the existence of an orthonormal basis of eigenvectors. The computation confirms $AU=U\Lambda$ and $U^{*}U=\mathrm{I}$ to machine precision at $n=5$.

**The eigenvalues are the diagonal entries in the eigenbasis, and the trace and determinant are their sum and product.** Taking traces in $S=Q\Lambda Q^{\mathsf T}$ gives $\operatorname{tr}S=\sum\lambda_i$ and taking determinants gives $\det S=\prod\lambda_i$, consistently with *The Spectrum of a Matrix*. So the two spectral invariants are read off the diagonal of the diagonal form.

## The Spectral Resolution

**The matrix is the sum of its eigenvalues times orthogonal projections.** Put $P_i=u_iu_i^{*}$, the orthogonal projection onto the line spanned by $u_i$. Then

$$
P_i^{2}=P_i,\qquad P_i^{*}=P_i,\qquad P_iP_j=\delta_{ij}P_i,\qquad \sum_iP_i=\mathrm{I},
$$

and the diagonalisation reads

$$
A=\sum_{i=1}^{n}\lambda_iP_i .
$$

The identity was verified at $n=4$ on a random Hermitian matrix, together with the four properties of the family $(P_i)$.

**Grouping equal eigenvalues gives the spectral projections.** If $\lambda$ occurs with multiplicity $m$, put

$$
P_{(\lambda)}=\sum_{\lambda_i=\lambda}P_i,
$$

the orthogonal projection onto the eigenspace $E_\lambda$. Then $P_{(\lambda)}P_{(\mu)}=\delta_{\lambda\mu}P_{(\lambda)}$, the sum over the distinct eigenvalues is the identity, and

$$
A=\sum_{\lambda}\lambda\,P_{(\lambda)},
$$

which is the spectral resolution in the form used by the functional calculus. The rank of $P_{(\lambda)}$ is the multiplicity $m_\lambda$, and the geometric and algebraic multiplicities agree because the matrix is diagonalisable.

**Every polynomial in $A$ has the same projections.** For any polynomial $p$,

$$
p(A)=\sum_{\lambda}p(\lambda)P_{(\lambda)},
$$

so the spectral projections are the common eigenvectors of the whole commutative algebra generated by $A$. That algebra is isomorphic to the algebra of functions on the spectrum, which is the finite-dimensional model of the functional calculus of *The Analysis on $M_n(\mathbb{C})$*.

**The projections are the derivatives of the resolvent.** For $\lambda$ not in the spectrum,

$$
(A-\lambda\mathrm{I})^{-1}=\sum_{\mu}\frac{1}{\mu-\lambda}P_{(\mu)},
$$

so the spectral resolution is the partial fraction decomposition of the resolvent, and the projection $P_{(\lambda)}$ is the residue at $\mu=\lambda$. So the spectral theorem and the resolvent are the same statement read in two ways.

## The Rayleigh Quotient

**The Rayleigh quotient is bounded by the extreme eigenvalues.** For $x\neq0$ put

$$
R_A(x)=\frac{\langle Ax,x\rangle}{\langle x,x\rangle}.
$$

Writing $x=\sum c_iu_i$ in the eigenbasis gives $\langle Ax,x\rangle=\sum\lambda_i|c_i|^{2}$ and $\langle x,x\rangle=\sum|c_i|^{2}$, hence

$$
\lambda_{\min}\le R_A(x)\le\lambda_{\max},
$$

with equality exactly on the corresponding eigenspaces. The bound was verified at $n=4$ on random Hermitian matrices and random vectors.

**The extremes are attained.** Taking $x=u_{\min}$ gives $R_A=\lambda_{\min}$ and $x=u_{\max}$ gives $R_A=\lambda_{\max}$, so

$$
\lambda_{\min}=\min_{x\neq0}R_A(x),\qquad \lambda_{\max}=\max_{x\neq0}R_A(x).
$$

So the extreme eigenvalues are the extreme values of a smooth function on the sphere, and the variational problem has an exact solution.

**The intermediate eigenvalues are min-max values.** For $1\le k\le n$,

$$
\lambda_k=\min_{\dim V=k}\ \max_{x\in V,\,x\neq0}R_A(x)=\max_{\dim W=k-1}\ \min_{x\perp W,\,x\neq0}R_A(x),
$$

the minimum over $k$-dimensional subspaces and the maximum over $(k-1)$-dimensional ones. The identity was verified at $n=4$ by scanning subspaces spanned by coordinate eigenvectors, and it is the Courant–Fischer principle.

**The quotient is a complete invariant of the Hermitian matrix.** Two Hermitian matrices have the same Rayleigh quotient function exactly when they are equal, since the function determines the Hermitian form by polarisation. So the spectral theorem says that the function $R_A$ on the sphere determines $A$, and the eigenvalues are its critical values.

## Positive Semidefiniteness

**The spectrum decides the sign of the quadratic form.** For Hermitian $A$ with spectrum $\lambda_1,\dots,\lambda_n$,

$$
\langle Ax,x\rangle=\sum_i\lambda_i|c_i|^{2},
$$

so $A$ is positive semidefinite exactly when all $\lambda_i\ge0$, positive definite exactly when all $\lambda_i>0$, and indefinite exactly when the spectrum has both signs. The statement was verified on random Hermitian matrices at $n=3,4$ with spectra of both types.

**So the positive semidefinite cone is the set of Hermitian matrices with nonnegative spectrum.** It contains the zero matrix and is closed under addition and under congruence $A\mapsto M^{*}AM$. Its interior is the positive definite set, and its boundary consists of the matrices with a zero eigenvalue. The geometry of the set is the subject of *The Cone of Positive Semidefinite Matrices*.

**The cone is the set of squares.** $A$ is positive semidefinite exactly when $A=B^{*}B$ for some $B$, and then $B$ can be taken as $A^{1/2}=U\Lambda^{1/2}U^{*}$, which is Hermitian and positive semidefinite. So

$$
\{\text{positive semidefinite}\}=\{B^{*}B:B\in M_n(\mathbb{C})\},
$$

which is the algebraic description of the cone and the complex analogue of the cone of the Jordan algebra.

**The square root is unique in the cone.** If $C$ is positive semidefinite and $C^{2}=A$, then $C$ commutes with $A$ and is diagonal in the eigenbasis of $A$, with nonnegative eigenvalues squaring to those of $A$; hence $C=A^{1/2}$. So the map $A\mapsto A^{1/2}$ is a well-defined continuous map of the cone onto itself, which is used in the polar decomposition.

## The Case $n=2$

**At $n=2$ the theorem is one rotation.** For $S=\begin{pmatrix}a&b\\b&d\end{pmatrix}$ real symmetric, the eigenvalues are

$$
\lambda_{\pm}=\frac{a+d}{2}\pm\sqrt{\Big(\frac{a-d}{2}\Big)^{2}+b^{2}},
$$

and the eigenvectors are at the angle $\theta$ with $\tan2\theta=\frac{2b}{a-d}$. The eigenvalues are real for all $a,b,d$, and the computation confirms the formula and the orthogonality of the two eigenvectors.

**The sign of the determinant decides the type.** Since $\lambda_+\lambda_-=\det S$ and $\lambda_++\lambda_-=\operatorname{tr}S$, the symmetric matrix is positive definite exactly when $\operatorname{tr}S>0$ and $\det S>0$, which is the $n=2$ description of the cone as the interior of a quadrant in the $(a,d)$-plane for each $b$.

**The biquaternion reading gives the spectral projections as idempotents.** With $\tilde\Pi_\pm=\tfrac12(\mathrm{I}\pm\tilde{Ζ})$ and $\tilde{Ζ}$ any traceless Hermitian matrix of square $\mathrm{I}$, the spectral resolution reads

$$
S=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
$$

so the two spectral projections are exactly the idempotent pair of the biquaternion frame, with $e_t=\tilde\Pi_++\tilde\Pi_-$ and $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$. So the spectral theorem at $n=2$ is the statement that every Hermitian biquaternion is a real combination of the two idempotents of a frame, which is the reality condition of *The Peirce Decomposition of the Biquaternion Algebra*.

## Summary

A Hermitian matrix has a real spectrum, because $\lambda\|v\|^{2}=\langle Av,v\rangle=\bar\lambda\|v\|^{2}$, and orthogonal eigenvectors for distinct eigenvalues, so it is diagonalised by a unitary: $A=U\Lambda U^{*}$ with $\Lambda$ real. The spectral resolution $A=\sum_\lambda\lambda P_{(\lambda)}$ writes it as a real combination of orthogonal projections, which are the residues of the resolvent and the common projections of the algebra generated by $A$. The Rayleigh quotient lies between the extreme eigenvalues, attains them on the corresponding eigenspaces, and gives the min-max formula for every eigenvalue. The quadratic form is nonnegative exactly when the spectrum is, so the positive semidefinite cone is the set of squares, with a unique square root.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=A^{*}$ | the Hermitian condition |
| $\lambda_i\in\mathbb{R}$ | the real spectrum |
| $A=U\Lambda U^{*}$ | the orthogonal diagonalisation |
| $P_i=u_iu_i^{*}$ | the rank-one spectral projections |
| $P_{(\lambda)}$ | the projection onto the eigenspace of $\lambda$ |
| $R_A(x)=\langle Ax,x\rangle/\langle x,x\rangle$ | the Rayleigh quotient |
| $\lambda_{\min}=\min R_A$, $\lambda_{\max}=\max R_A$ | the variational characterisation |
| $A^{1/2}=U\Lambda^{1/2}U^{*}$ | the unique square root in the cone |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Hermitian spectral theorem and the Rayleigh quotient.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Courant–Fischer min-max principle.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the spectral resolution and the functional calculus.
- [Normal Matrices and the Common Spectral Theorem](normal-matrices-and-the-common-spectral-theorem.html), for the unitary diagonalisation that the Hermitian case specialises.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian](the-two-halves-over-c-hermitian-and-anti-hermitian.html), for the half in which the theorem lives.
- [The Spectrum of a Matrix](the-spectrum-of-a-matrix.html), for the trace and the determinant as the sum and the product of the spectrum.
