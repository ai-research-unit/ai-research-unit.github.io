# __Normal $2\times2$ Matrices and the Common Spectral Theorem__

## Introduction

**A $2\times2$ matrix is normal exactly when it is unitarily diagonalisable, and a commuting family of normal matrices is diagonalised by one unitary frame.**

The article defines normality, proves the equivalence with unitary diagonalisability at order two, derives the three special cases of the Hermitian, skew-Hermitian and unitary matrices from the position of the two eigenvalues, computes the commutant of a normal matrix with simple spectrum, proves the common spectral theorem for a commuting pair, and reads normality as the equality of the two norms $\|Xv\|$ and $\|X^{*}v\|$. It assumes *The Spectrum of a $2\times2$ Matrix*, *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum* and *The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian at $n=2$*.

It defers the two halves of the spectral theorem to *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents* and *The Spectral Theorem: the Skew-Hermitian Case and the Two Imaginary Eigenvalues*.

## Normality

**Definition.** A matrix $X$ is **normal** when $XX^{*}=X^{*}X$.

**Proposition.** The Hermitian, the skew-Hermitian and the unitary matrices are normal, and every polynomial in a normal matrix is normal.

**Proof.** If $X^{*}=\pm X$ then both products equal $\pm X^{2}$; if $X$ is unitary then both products are the identity.

**Corollary.** The normal matrices are not a linear subspace: the sum of two normal matrices need not be normal.

**Proof.** Take $X=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, the rotation by a right angle, and $Y=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, a reflection; both are Hermitian or skew-Hermitian and hence normal, and the sum $\begin{pmatrix}0&2\\0&0\end{pmatrix}$ is not normal because $AA^{*}$ and $A^{*}A$ are the diagonal matrices with $4$ in the two different corners.

**Corollary.** Normality is invariant under unitary conjugation and under the star.

**Proof.** $(UXU^{*})(UXU^{*})^{*}=UXX^{*}U^{*}$ and the same with the reversed order, so the equality is preserved; and the star exchanges the two sides of the equation.

## The Spectral Theorem at Order Two

**Theorem.** A matrix is normal exactly when there is a unitary $U$ and a diagonal $\Lambda$ with $X=U\Lambda U^{*}$.

**Proof.** If $X=U\Lambda U^{*}$ then $XX^{*}=U\Lambda\bar\Lambda U^{*}=X^{*}X$. Conversely a normal matrix has the eigenvectors of *The Spectrum of a $2\times2$ Matrix*, and the eigenspaces of distinct eigenvalues are orthogonal because $\lambda_{1}\langle v_{1},v_{2}\rangle=\langle Xv_{1},v_{2}\rangle=\langle v_{1},X^{*}v_{2}\rangle=\bar\lambda_{2}\langle v_{1},v_{2}\rangle$ forces the product to vanish when the eigenvalues differ; the eigenvectors are orthonormalised and form a unitary frame.

**Corollary.** A normal matrix with distinct eigenvalues is diagonalised by every unitary frame of its eigenvectors, and the diagonal entries are the eigenvalues.

**Proof.** The two eigenspaces are orthogonal lines, and the unitary frame is unique up to the phases of the two lines.

**Corollary.** The normal matrices with simple spectrum form an open dense set in the space of normal matrices, and the exceptional set is the locus where the discriminant vanishes.

**Proof.** The discriminant is a continuous function of the entries, and it vanishes on a closed set of real codimension one inside the normal matrices; the scalars are normal, and they are the only normal matrices with a double eigenvalue that are not diagonalised in a single way.

## The Three Special Cases

**Proposition.** A normal matrix is Hermitian exactly when its two eigenvalues are real, skew-Hermitian exactly when they are purely imaginary, and unitary exactly when they have modulus one.

**Proof.** In a unitary diagonalisation the star of the matrix is the diagonal of the conjugates of the eigenvalues, so $X^{*}=\pm X$ holds exactly when each eigenvalue satisfies $\bar\lambda=\pm\lambda$; and $X^{*}X=I$ holds exactly when each eigenvalue has modulus one.

**Corollary.** Each of the three classes is described inside the normal matrices by a condition on the spectrum alone.

**Proof.** The conditions are conditions on each of the two eigenvalues, and the spectrum is the pair.

**Corollary.** The Hermitian normal matrices form a real vector space of dimension four, the skew-Hermitian ones another of dimension four, and the unitary ones a group of real dimension four.

**Proof.** The Hermitian matrices are the fixed points of the star, a real-linear involution of the eight-dimensional real space, so each eigenspace has dimension four; the unitary matrices are the solutions of $X^{*}X=I$, which is a group of real dimension four.

## The Commutant

**Proposition.** The commutant of a matrix with simple spectrum is the two-dimensional algebra of polynomials in the matrix, and for a normal matrix it is the algebra of the two spectral projections.

**Proof.** Commuting with $X$ preserves each eigenspace, which is a line, so the commutant is the set of matrices diagonal in the frame of the eigenvectors; that set is spanned by the two projections, which are polynomials in $X$ by *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum*.

**Corollary.** The commutant of a matrix with simple spectrum is commutative and consists of the normal matrices exactly when the two projections are orthogonal.

**Proof.** The commutant is spanned by the two projections, and it is commutative because the projections are orthogonal idempotents; the projections are Hermitian exactly when the frame is unitary.

**Corollary.** The commutant of a scalar is the whole algebra, so the simple-spectrum hypothesis cannot be dropped.

**Proof.** The scalar commutes with everything.

## The Common Spectral Theorem

**Theorem.** If $X$ and $Y$ are normal and commute, then there is one unitary frame in which both are diagonal.

**Proof.** The eigenspaces of $X$ are preserved by $Y$ because $Y$ commutes with $X$: for $Xv=\lambda v$ one has $X(Yv)=YXv=\lambda Yv$, so $Yv$ lies in the same eigenspace. On each eigenspace of $X$, which is one line, $Y$ acts as a scalar; choosing a unit vector in each eigenspace diagonalises $X$ and $Y$ at once.

**Corollary.** A commuting family of normal matrices is simultaneously diagonalisable, and the family is contained in one commutative algebra of dimension at most two.

**Proof.** Apply the theorem to each pair; the common frame diagonalises every member, and the diagonal matrices in two dimensions form a commutative algebra of dimension two.

**Corollary.** Two normal matrices commute exactly when they are simultaneously diagonalisable by one unitary.

**Proof.** The forward direction is the theorem, and the reverse direction is the commutativity of diagonal matrices.

## Normality as an Isometry Condition

**Proposition.** A matrix is normal exactly when $\|Xv\|=\|X^{*}v\|$ for every vector $v$.

**Proof.** The difference of the two squared norms is $v^{*}(X^{*}X-XX^{*})v$, which vanishes for every $v$ exactly when the matrix in the middle is zero.

**Corollary.** The kernel of a normal matrix is the kernel of its star, and the image of a normal matrix is the image of its star.

**Proof.** The equality of the norms makes the two kernels equal, and the images are the orthogonal complements of the two kernels.

**Corollary.** A normal matrix with a one-dimensional kernel has the star with the same kernel, so the two mixed lines of the frame coincide.

**Proof.** The kernel of $X$ is a line, and the kernel of $X^{*}$ is the orthogonal complement of the image of $X$, which is the same line.

## Summary

A $2\times2$ matrix is normal when it commutes with its star, and that holds exactly when it is unitarily diagonalisable. The three classical classes sit inside the normal matrices as conditions on the two eigenvalues: real for Hermitian, purely imaginary for skew-Hermitian, of modulus one for unitary, each of real dimension four.

The commutant of a matrix with simple spectrum is the two-dimensional algebra of polynomials in it, spanned by the two spectral projections, and a commuting family of normal matrices is diagonalised by one unitary frame. Normality is also the equality of the two norms $\|Xv\|$ and $\|X^{*}v\|$ for every vector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X^{*}$ | the conjugate transpose |
| $U,\Lambda$ | the unitary frame and the diagonal form |
| $\rho_{\pm}$ | the spectral projections |
| $\operatorname{Com}(X)$ | the commutant of $X$ |
| $\lambda_{\pm}$ | the two eigenvalues |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for normal matrices and the spectral theorem.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for the spectral theorem and simultaneous diagonalisation.
- [The Spectrum of a $2\times2$ Matrix](the-spectrum-of-a-2x2-matrix.html), for the eigenvalues and the eigenspaces.
- [The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian at $n=2$](the-two-halves-over-c-hermitian-and-skew-hermitian-at-n-2.html), for the two halves as the fixed points of the star.
- [Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum](lagrange-idempotents-of-a-2x2-matrix-with-simple-spectrum.html), for the projections that span the commutant.
