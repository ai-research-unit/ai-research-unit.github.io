# __$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm__

## Introduction

Two matrix invariants carry the two invariants of the biquaternion algebra. The trace is twice the scalar part, and the determinant is the quaternionic norm:

$$
\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t,\qquad
\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2.
$$

The first is additive and blind to the vector part; the second is multiplicative and sees the whole element. Together they give invertibility, the zero divisors, the spectrum and the characteristic polynomial.

This article develops the two invariants and what they decide. It is the matrix form of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*The Four Algebraic Norms*, and of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Characteristic Polynomial*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*: $\tilde Q=Q_te_t+\vec Q$, $B^2=Q_x^2+Q_y^2+Q_z^2$, and $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$. The eigenvalues are written $\lambda_\pm=Q_t\pm iB$, with $B$ a chosen square root of $B^2$; the pair is unordered and the choice of $B$ exchanges the two labels.

**Boundaries.** The four forms and their norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the spectral condition is *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; the rank-one case is *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*; the polar decomposition is *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*; the groups defined by the determinant are *$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant*.

## The Trace

**The trace is twice the scalar part.** For $\mathsf{M}_2(\tilde Q)=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$
a=Q_t-iQ_z,\qquad d=Q_t+iQ_z,\qquad
\operatorname{Tr}\mathsf{M}_2(\tilde Q)=a+d=2Q_t.
$$

The trace therefore kills the vector part, and the scalar part is recovered by $Q_t=\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde Q)$. The trace is $\mathbb{C}$-linear, vanishes on the traceless matrices, and is invariant under conjugation:

$$
\operatorname{Tr}(PMP^{-1})=\operatorname{Tr}M.
$$

**The trace pairing.** The bilinear form $\langle\tilde P,\tilde Q\rangle=\tfrac12\operatorname{Tr}(XY)$ is the plain bilinear form of the algebra. Its Gram matrix on the coefficient basis is $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$, and it is non-degenerate. The trace is the invariant that makes the pairing, and the pairing is the one used to dualise the algebra.

**The trace is not the norm.** The trace is additive and complex-valued; it does not detect the vector part. An element with $Q_t=0$ is traceless whatever its vector part, and the traceless matrices are the image of the vector subspace. The statement is the matrix form of the split $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$.

## The Determinant

**The determinant is the quaternionic norm.** For the general matrix,

$$
\det\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}
=(Q_t-iQ_z)(Q_t+iQ_z)-(-iQ_x-Q_y)(-iQ_x+Q_y)
=Q_t^2+Q_x^2+Q_y^2+Q_z^2.
$$

The determinant is multiplicative:

$$
\det(XY)=\det X\det Y,
$$

which is the multiplicativity of the quaternionic norm, $\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$. It is also invariant under conjugation, $\det(PMP^{-1})=\det M$, and under transposition, $\det(M^{\mathsf T})=\det M$.

**Invertibility.** A square matrix is invertible exactly when its determinant is nonzero, so

$$
\tilde Q\text{ is a unit}\iff\langle\tilde Q\rangle_{\natural}\neq0.
$$

The inverse is

$$
\mathsf{M}_2(\tilde Q)^{-1}=\frac{\operatorname{adj}\mathsf{M}_2(\tilde Q)}{\det\mathsf{M}_2(\tilde Q)}
=\frac{1}{N}\begin{pmatrix}Q_t+iQ_z&iQ_x+Q_y\\iQ_x-Q_y&Q_t-iQ_z\end{pmatrix}.
$$

The numerator is the image of $\tilde Q^{\natural}$, and the formula is the matrix form of $\tilde Q^{-1}=\tilde Q^{\natural}/N$.

**The zero divisors.** A nonzero matrix is a zero divisor exactly when it is singular, and the singular matrices are those of rank at most one. The singular nonzero matrices form the determinantal variety $\{N=0\}$, the image of the null cone. The zero matrix is the apex. The cone is the subject of *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*.

**The determinant as a volume.** Over $\mathbb{C}$ the determinant is a complex volume. Its modulus squared is the real volume of the image of the unit square, and its argument is twice the phase of the linear map. On the Hermitian matrices the determinant is real and is the Minkowski quadratic form; on the anti-Hermitian matrices it is real with the opposite sign. The two readings are the two real forms of the same complex determinant.

## The Characteristic Polynomial

**The characteristic polynomial is the biquadratic.**

$$
\chi_M(X)=X^2-\operatorname{Tr}(M)X+\det(M)
=X^2-2Q_tX+\langle\tilde Q\rangle_{\natural}
=X^2-2Q_tX+(Q_t^2+B^2).
$$

Its roots are

$$
\lambda_\pm=Q_t\pm iB,
\qquad
\lambda_++\lambda_-=2Q_t,\qquad
\lambda_+\lambda_-=Q_t^2+B^2.
$$

The discriminant is

$$
\Delta=4Q_t^2-4(Q_t^2+B^2)=-4B^2.
$$

The discriminant depends only on the vector part. This is the spectral criterion in matrix form: the eigenvalues are distinct exactly when $B^2\neq0$, and they coincide exactly when $B^2=0$.

**Cayley–Hamilton.** The matrix satisfies its own characteristic polynomial:

$$
M^2-2Q_tM+\langle\tilde Q\rangle_{\natural}\mathrm I_2=0.
$$

The identity is verified by substituting the general matrix. It is the matrix form of the quadratic relation satisfied by every biquaternion, and it is the reason the algebra is of degree two over its centre: every element generates a commutative subalgebra of dimension at most two.

**The spectrum and the trace.** The trace is the sum of the eigenvalues and the determinant is their product. For a general element the two eigenvalues are complex conjugates up to the factor $iB$; for a Hermitian element $B^2$ is negative real (up to the choice of square root) and the eigenvalues are real; for an anti-Hermitian element they are purely imaginary. The three cases are the three real forms of the same complex pair.

**The degenerate case.** When $B=0$ the two eigenvalues coalesce at $Q_t$. The matrix is then $Q_t\mathrm I_2+N$ with $N$ nilpotent, and it has a single eigenvalue. It is diagonalisable exactly when $N=0$, that is when the matrix is scalar. Otherwise it is a single Jordan block. The statement is the matrix form of the spectral-degenerate cone.

## The Determinant and the Modulus

**The modulus.** In the polar decomposition of *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*, a matrix is written

$$
M=r\,\zeta\,M_bM_r,
\qquad r>0,\quad|\zeta|=1,\quad M_b\text{ Hermitian positive of determinant }1,\quad M_r\in SU(2).
$$

Taking determinants,

$$
\det M=r^2\zeta^2,
$$

because $\det M_b=1$ and $\det M_r=1$. Hence

$$
|\det M|=r^2,\qquad r=|\det M|^{1/2},
$$

and the phase of the determinant is twice the phase $\zeta$. The modulus $r$ is the real scale of the element, and the determinant sees it squared. The factor two is the reason the determinant of left multiplication on the four-dimensional algebra is $N^2$, and the real determinant of that operator is $|N|^4$, while the modulus is $|N|^{1/2}$.

**The singular values.** The singular values of $M$ are the square roots of the eigenvalues of $MM^{\dagger}$. From $M=r\zeta M_bM_r$ and the unitarity of $M_r$,

$$
MM^{\dagger}=r^2M_b^2,
$$

so the singular values are $r e^{\eta/2}$ and $r e^{-\eta/2}$, where $e^{\pm\eta}$ are the eigenvalues of $M_b^2$. Their product is $r^2=|\det M|$. They coincide exactly when $M_b=\mathrm I_2$, that is when the element is a scalar times a unitary; otherwise the boost separates them. A general complex matrix has two singular values whose product is $|\det M|$; in the polar word the pair is $re^{\pm\eta/2}$, and the rapidity is the parameter that separates them.

**The determinant on the two halves.** On $\mathbb{M}_+$ the determinant is $q_t^2-q_x'^2-q_y'^2-q_z'^2$, of signature $(1,3)$; on $\mathbb{M}_-$ it is $-(q_t')^2+q_x^2+q_y^2+q_z^2$, of signature $(3,1)$. The two are opposite, and the sign is the matrix form of the anti-isometry between the two sectors. The statement is proved in *$M_2(\mathbb{C})$ Representation : The Six Subspaces as Matrix Conditions*.

## Summary

The trace is twice the scalar part and the determinant is the quaternionic norm. The determinant is multiplicative, nonzero exactly on the units, and zero exactly on the singular matrices, which are the zero divisors. The characteristic polynomial is $X^2-2Q_tX+N$, with discriminant $-4B^2$; the eigenvalues are $Q_t\pm iB$, distinct exactly when $B^2\neq0$. The modulus of the polar decomposition is the square root of the modulus of the determinant, and the two singular values have product $|\det M|$ and are separated by the rapidity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t$ | the trace, twice the scalar part |
| $\det\mathsf{M}_2(\tilde Q)=N=Q_t^2+B^2$ | the determinant, the quaternionic norm |
| $\chi_M(X)=X^2-2Q_tX+N$ | the characteristic polynomial |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $\Delta=-4B^2$ | the discriminant |
| $r=|\det M|^{1/2}$ | the modulus |
| $\{N=0\}$ | the null cone, the determinantal variety |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four norms
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the characteristic polynomial and the criterion
- [$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety](m2c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the singular matrices
- [$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix](m2c-representation-the-polar-decomposition-of-a-matrix.html), for the modulus
- [$M_2(\mathbb{C})$ Representation : The Six Subspaces as Matrix Conditions](m2c-representation-the-six-subspaces-as-matrix-conditions.html), for the determinants on the subspaces
- [The N-Regular Sector](the-n-regular-sector.html), for the norm on the units
- [The N-Degenerate Sector](the-n-degenerate-sector.html), for the null cone
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html)
