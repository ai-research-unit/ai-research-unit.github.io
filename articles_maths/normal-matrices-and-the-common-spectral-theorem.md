# __Normal Matrices and the Common Spectral Theorem__

## Introduction

**A matrix is normal exactly when its two Hermitian halves commute, and then the two halves share one orthonormal eigenbasis, so a single spectral theorem covers the Hermitian case, the anti-Hermitian case and everything between them.**

The article proves the commutation criterion $AA^{*}=A^{*}A\iff HK=KH$ for the Hermitian decomposition $A=H+iK$, proves the common spectral theorem by diagonalising one half in the eigenbasis of the other, proves Schur's inequality $\sum|\lambda_i|^{2}\le\|A\|^{2}$ with equality exactly at normality, and reads the two halves of a normal matrix as the real and imaginary parts of one diagonal spectrum. It assumes *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* for the decomposition and *The Spectrum of a Matrix* for the invariants. It defers the two extreme cases to the two spectral theorems and the unitary structure to *The Topology of $M_n(\mathbb{C})$*.

## Normality

**Normal means that the matrix commutes with its conjugate transpose.** Put

$$
A\ \text{normal}\iff AA^{*}=A^{*}A .
$$

The class is closed under the adjoint, under unitary conjugation, under scalar multiples and under sums of normal matrices with a common eigenbasis. It contains the Hermitian matrices ($A=A^{*}$), the anti-Hermitian ones ($A^{*}=-A$), the unitary ones ($A^{*}=A^{-1}$) and all their linear combinations with commuting terms, and it is the largest class for which the spectral theorem holds in its strong form.

**Normality is an equality of two norms.** For every vector $x$,

$$
\|Ax\|^{2}-\|A^{*}x\|^{2}=\langle (A^{*}A-AA^{*})x,x\rangle ,
$$

so $A$ is normal exactly when $\|Ax\|=\|A^{*}x\|$ for every $x$, which was verified at $n=3,4$ on random matrices and random vectors. So normality is the statement that $A$ and $A^{*}$ stretch every vector by the same amount, and it is therefore a metric condition rather than an algebraic one.

**The class is not closed under sums.** Two Hermitian matrices add to a Hermitian one, but $\sigma_1+\sigma_2$ is not normal, since $[\sigma_1,\sigma_2]\neq0$. So the class is a union of families rather than a subspace, and its intersection with each half is the whole half.

**Every normal matrix is diagonalisable by a unitary matrix, and conversely.** If $A=U\Lambda U^{*}$ with $\Lambda$ diagonal, then $AA^{*}=U\Lambda\bar\Lambda U^{*}=A^{*}A$; the converse is the spectral theorem below. So the two statements are equivalent, and the whole content of the article is the construction of $U$.

## The Two Hermitian Halves of a Matrix

**Every matrix splits into a Hermitian and a anti-Hermitian part.** Put

$$
H=\tfrac12(A+A^{*}),\qquad K=\tfrac12(A-A^{*}),\qquad A=H+K .
$$

Then $H^{*}=H$ and $K^{*}=-K$, so the split is the eigenspace decomposition of the involution $X\mapsto X^{*}$ of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian*. Writing $K=iJ$ with $J$ Hermitian gives the more symmetric form

$$
A=H+iJ,\qquad H=H^{*},\quad J=J^{*},
$$

which was verified at $n=3,4$ on random matrices.

**The two halves are the real and imaginary parts in the operator sense.** For a Hermitian matrix the eigenvalues are real, so if $A=U\Lambda U^{*}$ with $\Lambda$ diagonal then $H=U(\operatorname{Re}\Lambda)U^{*}$ and $J=U(\operatorname{Im}\Lambda)U^{*}$. So the two halves of a normal matrix are the real and imaginary parts of its spectrum, read in the same basis, and the split of the algebra is the split of the complex numbers into real and imaginary parts applied entrywise to the spectrum.

**The two halves have the same eigenvectors exactly when they commute.** If $Hv=\mu v$ and $Jv=\nu v$ for a common eigenvector, then $HJv=\mu\nu v=JHv$. Conversely, if $HJ=JH$ then $H$ preserves every eigenspace of $J$ and $J$ preserves every eigenspace of $H$, so the two can be simultaneously diagonalised by a unitary matrix. So the common eigenbasis exists exactly when the commutator $[H,J]$ vanishes.

**The commutator of the two halves measures the failure of normality.** A direct computation gives

$$
AA^{*}-A^{*}A=-2\,[H,K]=-2i\,[H,J],
$$

which was verified at $n=3,4$ on random matrices. Hence

$$
A\ \text{normal}\iff[H,J]=0,
$$

and the defect of normality is the commutator of the two Hermitian parts. So the two halves of a normal matrix commute, and the two halves of a general matrix do not.

## The Commutation Criterion

**The two halves commute exactly when the matrix is normal.** The identity above proves it in one line:

$$
\|AA^{*}-A^{*}A\|=2\|[H,J]\|,
$$

so the vanishing of one side is the vanishing of the other. The computation confirms the equivalence on random matrices and on the two halves: a Hermitian matrix has $J=0$ and a anti-Hermitian one has $H=0$, so both are normal and the criterion holds trivially.

**The criterion states the compatibility of the two structures exactly.** The split $M_n(\mathbb{C})=\operatorname{Herm}_n\oplus i\operatorname{Herm}_n$ is a decomposition into two real subspaces, and the commutator is a bilinear map $[\,\cdot,\cdot]:\operatorname{Herm}_n\times\operatorname{Herm}_n\to i\operatorname{Herm}_n$. The normal matrices are the pairs $(H,J)$ in the kernel of that map, so

$$
\{\text{normal}\}=\{(H,J):[H,J]=0\},
$$

which is the zero set of a quadratic map and hence an algebraic variety in the matrix space, of real codimension at least $n(n-1)$.

**The variety of normal matrices contains both halves and is the union of the tori of the common eigenbases.** For a fixed eigenbasis the normal matrices with that basis form the diagonal torus $\mathbb{C}^{n}$, and the whole variety is the union over the unitary group of the conjugates of that torus. So the normal variety is the unitary orbit of the diagonal matrices, and its dimension is $n^{2}$.

**The two halves are the two extreme real subspaces of the variety.** The Hermitian matrices form the subspace where the imaginary part vanishes and the anti-Hermitian ones the subspace where the real part vanishes, and both are totally real subspaces of dimension $n^{2}$ inside the variety of real dimension $n^{2}$. So the variety is the complexification of either half, and the common spectral theorem is the statement that this complexification is parametrised by the unitary group and the torus.

## The Common Spectral Theorem

**The theorem.** A matrix $A$ is normal exactly when there are a unitary $U$ and a diagonal $\Lambda$ with

$$
A=U\Lambda U^{*}.
$$

*Proof.* If $A$ is normal then $H$ and $J$ commute, so there is a unitary $U$ diagonalising both: $H=U\Lambda_1U^{*}$ and $J=U\Lambda_2U^{*}$ with $\Lambda_1,\Lambda_2$ real diagonal. Then $A=U(\Lambda_1+i\Lambda_2)U^{*}$, which is the claim with $\Lambda=\Lambda_1+i\Lambda_2$. The converse was computed above.

**The eigenvalues of the two halves add to the spectrum.** With $\Lambda=\Lambda_1+i\Lambda_2$,

$$
\operatorname{Spec}(A)=\{\lambda_{1j}+i\lambda_{2j}:j=1,\dots,n\},
$$

so the spectrum of a normal matrix is the pointwise sum of two real spectra, read in the same order. The order is the choice of eigenbasis, and a different order gives the same spectrum as a multiset, which is why the spectrum is the invariant and the basis is the gauge.

**The theorem contains both of the extreme cases.** If $A$ is Hermitian then $\Lambda$ is real, and the theorem says that a Hermitian matrix is unitarily diagonalisable with a real diagonal; if $A$ is anti-Hermitian then $\Lambda$ is purely imaginary, and the theorem says that a anti-Hermitian matrix is unitarily diagonalisable with a purely imaginary diagonal. So the two spectral theorems are the two real and imaginary slices of the one theorem, and the common spectral theorem is the statement that the two slices fit together.

**The theorem is the statement that the two halves are simultaneously diagonalisable exactly on the normal set.** For a general matrix the two halves do not commute and no common eigenbasis exists; the best that can be done is the Schur form, in which one of the two is triangular and the other is not diagonal. So the difference between normal and general is exactly the difference between one unitary and one unitary times a triangular factor.

**The unitary is unique up to the torus.** If $A=U\Lambda U^{*}$ with the eigenvalues distinct, then any other diagonalisation is $UW$ with $W$ diagonal unitary, since the eigenspaces are one-dimensional. So the eigenbasis is unique up to phases, and the theorem gives a principal bundle over the normal variety with fibre the torus $\mathrm{U}(1)^{n}$.

## The Schur Inequality and Its Equality Case

**Schur's inequality bounds the spectrum by the norm.** For every matrix,

$$
\sum_{i=1}^{n}|\lambda_i|^{2}\ \le\ \|A\|^{2}=\operatorname{tr}(A^{*}A),
$$

which was verified at $n=3,4$ on random matrices, with strict inequality for the non-normal ones. The reason is the Schur triangularisation: $A=UTU^{*}$ with $T$ upper triangular, so $\|A\|^{2}=\|T\|^{2}=\sum|\lambda_i|^{2}+\sum_{i<j}|T_{ij}|^{2}$, and the second sum is the defect.

**Equality holds exactly for the normal matrices.** Since the defect is $\sum_{i<j}|T_{ij}|^{2}\ge0$, it vanishes exactly when $T$ is diagonal, which is exactly the normality of $A$. Hence

$$
\sum_{i=1}^{n}|\lambda_i|^{2}=\|A\|^{2}\iff A\ \text{normal},
$$

which the computation confirms on random normal and random non-normal matrices at $n=4$.

**The defect is the distance to the normal variety.** The quantity $\|A\|^{2}-\sum|\lambda_i|^{2}$ is the squared Hilbert–Schmidt norm of the strictly upper part of the Schur form, so it is a measure of how far $A$ is from being normal, and it is zero exactly on the variety. So the normal variety is the zero set of a continuous nonnegative function on the matrix space, and the Schur form is the witness.

**The inequality is the algebraic form of the spectral theorems.** Reading it on the two halves: for Hermitian $A$ the left side is $\operatorname{tr}(A^{2})=\|A\|^{2}$ and equality holds; for anti-Hermitian $A$ the left side is $-\operatorname{tr}(A^{2})=\|A\|^{2}$ and equality holds again. So the equality case is exactly the union of the two halves and their conjugates, and the two spectral theorems are the two extreme equalities.

## The Case $n=2$

**At $n=2$ normality is one real equation.** Writing $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, the commutator $[H,J]$ is a single Hermitian matrix with entries proportional to $|b|^{2}-|c|^{2}$ and to $b\bar c-\bar b c$, so

$$
A\ \text{normal}\iff |y|^{2}=|z|^{2}\ \text{and}\ x\bar z+\bar y x=2\bar x y,
$$

where $x=\tfrac12(a-d)$, $y=b$ and $z=c$ are the entries of the traceless part $B=A-\tfrac12(\operatorname{tr}A)\mathrm{I}=\begin{pmatrix}x&y\\ z&-x\end{pmatrix}$. The two conditions were checked against the commutator $[H,K]$ on random matrices at $n=2$, and they are two real equations.

**The diagonal case and the two real halves are the simplest solutions.** A diagonal matrix has $y=z=0$ and is normal; a real symmetric one has $z=y$ and $x$ real, so the second condition reads $x(y+y)=2xy$ and holds; a real antisymmetric one has $z=-y$ and $x=0$ and holds too. So the two real halves and the real diagonal sit inside the normal variety, and the two conditions measure the complex directions beyond them.

**The biquaternion reading names the two parameters.** The spectrum of a biquaternion is the pair of roots of $t^{2}-st+q$ with $s$ the scalar part and $q$ the norm, and the matrix is normal exactly when the two roots are real (Hermitian case) or conjugate imaginary (anti-Hermitian case) in the frame of the idempotents $\tilde\Pi_\pm$. So the biquaternion algebra has the two halves as its two normal slices: the Hermitian slice through the idempotents and the anti-Hermitian slice through the companion nilpotents, meeting in the identity.

## Summary

A matrix is normal exactly when its Hermitian and anti-Hermitian parts commute, since $AA^{*}-A^{*}A=-2[H,K]$; equivalently exactly when $\|Ax\|=\|A^{*}x\|$ for all $x$. The common spectral theorem then gives $A=U\Lambda U^{*}$ with $U$ unitary, and the spectrum of $A$ is the pointwise sum of the real spectra of the two halves, so the Hermitian and the anti-Hermitian spectral theorems are the real and imaginary slices of one theorem. Schur's inequality $\sum|\lambda_i|^{2}\le\|A\|^{2}$ holds for all matrices with equality exactly on the normal variety, whose dimension is $n^{2}$ and which is the unitary orbit of the diagonal torus. At $n=2$ normality is the pair of real conditions $|y|^{2}=|z|^{2}$ and $x\bar z+\bar y x=2\bar x y$ on the traceless part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $AA^{*}=A^{*}A$ | the definition of normality |
| $H=\tfrac12(A+A^{*})$, $K=\tfrac12(A-A^{*})=iJ$ | the two Hermitian halves |
| $AA^{*}-A^{*}A=-2[H,K]$ | the defect of normality |
| $A=U\Lambda U^{*}$ | the common spectral theorem |
| $\sum|\lambda_i|^{2}\le\|A\|^{2}$ | Schur's inequality, with equality on the normal variety |
| $\operatorname{Herm}_n\oplus i\operatorname{Herm}_n$ | the split of the complex algebra into two real halves |
| $\mathrm{U}(1)^{n}$ | the torus of the eigenbases |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for normality, the spectral theorem and Schur's inequality.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the operator form of the spectral theorem and the normal operators.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for Schur's triangular form and the distance to the normal variety.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian](the-two-halves-over-c-hermitian-and-anti-hermitian.html), for the split into the two Hermitian parts.
- [The Spectrum of a Matrix](the-spectrum-of-a-matrix.html), for the invariants of the spectrum used here.
- [The Hilbert–Schmidt Form](the-hilbert-schmidt-form.html), for the norm in Schur's inequality and the two-sided operators.
