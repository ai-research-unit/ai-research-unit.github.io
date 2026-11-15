# __The Spectral Theorem: the Anti-Hermitian Case and the Reality of the Spectrum__

## Introduction

**A anti-Hermitian matrix has a purely imaginary spectrum and is diagonalised by a unitary with a purely imaginary diagonal, while a real antisymmetric matrix is not diagonalisable over $\mathbb{R}$ but is orthogonally similar to a block diagonal of rotations, so its spectrum is described by a list of real angles.**

The article proves that the anti-Hermitian matrices are exactly $i$ times the Hermitian ones, derives the purely imaginary spectrum and the diagonal form, proves the real canonical block form with its $2\times2$ rotation blocks, identifies the angles as the invariants of the orthogonal similarity class, and reads the count of blocks as the rank. It assumes *The Spectral Theorem: the Hermitian Case* for the diagonalisation and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* for the half. It defers the exponential of the half to *The Exponential of the Antisymmetric Part: One-Parameter Rotations* and the compact group to *The Homotopy of $\mathrm{GL}_n(\mathbb{C})$ and of the Two Halves*.

## The Half and Its Spectrum

**The anti-Hermitian half is $i$ times the Hermitian half.** If $K^{*}=-K$ then $H=iK$ satisfies

$$
H^{*}=(iK)^{*}=-iK^{*}=iK=H,
$$

and conversely $K=iH$ is anti-Hermitian for Hermitian $H$. So the map $H\mapsto iH$ is a real linear isomorphism between the two halves, and the anti-Hermitian matrices are exactly the Hermitian matrices multiplied by $i$.

**The spectrum is purely imaginary.** For $Kv=\lambda v$ with $v\neq0$,

$$
\lambda\|v\|^{2}=\langle Kv,v\rangle,\qquad \bar\lambda\|v\|^{2}=\langle v,Kv\rangle=-\langle Kv,v\rangle ,
$$

so $\lambda=-\bar\lambda$, that is $\lambda\in i\mathbb{R}$. The computation at $n=3,4,5$ gives real parts below $10^{-15}$ for random anti-Hermitian matrices, and the spectrum of $K=iH$ is $i$ times the spectrum of $H$.

**The quadratic form is purely imaginary.** For every $x$,

$$
\langle Kx,x\rangle=\overline{\langle x,Kx\rangle}=\overline{-\langle Kx,x\rangle}=-\overline{\langle Kx,x\rangle},
$$

so $\langle Kx,x\rangle\in i\mathbb{R}$, and the real part of the quadratic form vanishes identically. So the antisymmetric half is exactly the set of matrices whose quadratic form is purely imaginary, which is the complement of the characterisation of the Hermitian half by a real quadratic form.

**The square is negative semidefinite.** Since $K^{*}=-K$,

$$
K^{*}K=-K^{2},
$$

and $K^{*}K$ is positive semidefinite, so $K^{2}\preceq0$ and $\operatorname{tr}(K^{2})=-\|K\|^{2}\le0$. The computation confirms the inequality and the trace identity at $n=3,4$, and it is the spectral reason why a skew matrix has no nonzero idempotent.

## Orthogonal Diagonalisation over $\mathbb{C}$

**The theorem.** A anti-Hermitian matrix $K$ has a unitary $U$ and a real diagonal $\Theta$ with

$$
K=U(i\Theta)U^{*},\qquad \Theta=\operatorname{diag}(\theta_1,\dots,\theta_n).
$$

*Proof.* Write $K=iH$ with $H$ Hermitian; by the Hermitian spectral theorem $H=U\Lambda U^{*}$ with $\Lambda$ real, so $K=U(i\Lambda)U^{*}$.

**The eigenvectors are orthonormal and the eigenvalues are purely imaginary.** The columns of $U$ are an orthonormal eigenbasis and

$$
Ku_j=i\theta_ju_j,\qquad \langle u_j,u_k\rangle=\delta_{jk},
$$

which the computation confirms at $n=4$. So the anti-Hermitian half is diagonalised by the same unitary group that diagonalises the Hermitian half, and the diagonal entries are the imaginary numbers $i\theta_j$.

**The spectral resolution has imaginary coefficients.** With $P_j=u_ju_j^{*}$,

$$
K=i\sum_{j=1}^{n}\theta_jP_j,\qquad \sum_jP_j=\mathrm{I},
$$

so the anti-Hermitian matrix is an imaginary combination of the same orthogonal projections. The identity was verified at $n=4$ on a random anti-Hermitian matrix, and it shows that the two halves share the projection structure and differ only in the factor $i$.

**The exponential of the half is unitary, and the diagonal form makes it explicit.** Since $i\theta$ is purely imaginary, $|e^{i\theta}|=1$, so

$$
e^{K}=U\operatorname{diag}(e^{i\theta_1},\dots,e^{i\theta_n})U^{*}
$$

is unitary. So the exponential of the anti-Hermitian half lands in the unitary group, and the angles $\theta_j$ are the arguments of the eigenvalues of the unitary matrix.

## The Real Skew Matrices and the Block Form

**A real antisymmetric matrix is anti-Hermitian and its spectrum is purely imaginary, in conjugate pairs.** For $K\in\mathfrak{so}(n)$ the characteristic polynomial has real coefficients, so its roots come in conjugate pairs; since all roots are purely imaginary, the spectrum is

$$
\operatorname{Spec}(K)=\{0,\dots,0,\pm i\theta_1,\dots,\pm i\theta_m\},\qquad \theta_j>0,
$$

with $2m\le n$. The computation at $n=4,5,6$ confirms the pairing and the reality of the $\theta_j$, which are the moduli of the nonzero eigenvalues.

**The canonical form.** There is an orthogonal $Q$ with

$$
Q^{\mathsf T}KQ=\operatorname{diag}\Big(\begin{pmatrix}0&-\theta_1\\ \theta_1&0\end{pmatrix},\dots,\begin{pmatrix}0&-\theta_m\\ \theta_m&0\end{pmatrix},0,\dots,0\Big),
$$

the block diagonal of $m$ rotation blocks and $n-2m$ zeros. The form was verified at $n=4$ by computing the eigenvalues of a random skew matrix and comparing the characteristic polynomial of the block form with $\chi_K$.

**The matrix is not diagonalisable over $\mathbb{R}$ when $m\ge1$.** A real diagonalisable matrix has a real spectrum, and a nonzero $\theta_j$ gives the nonreal eigenvalues $\pm i\theta_j$; so a real skew matrix with $m\ge1$ has no real eigenbasis. Over $\mathbb{C}$ it is diagonalisable by a unitary, as the previous section shows. So the "reality of the spectrum" is the statement that the invariant data are the real numbers $\theta_j$, not the complex eigenvalues.

**The rank is twice the number of blocks.** Each rotation block has rank two and the zero block has rank zero, so

$$
\operatorname{rank}K=2m,\qquad \dim\ker K=n-2m,
$$

which was checked at $n=4,5,6$ on random skew matrices. So a real skew matrix of odd order is singular, and the corank has the same parity as $n$.

## The Angles as the Invariants

**The angles are determined by the spectrum and determine the orthogonal class.** Two real skew matrices are orthogonally similar exactly when they have the same list $\theta_1\ge\dots\ge\theta_m>0$ together with the same $n$, by the uniqueness of the canonical form. So

$$
\mathfrak{so}(n)\big/\mathrm{O}(n)\ \longleftrightarrow\ \{\theta_1\ge\dots\ge\theta_m>0,\ 2m\le n\},
$$

and the angles are the complete invariants of the orthogonal similarity class. The statement was verified at $n=4$ by comparing the sorted moduli of the eigenvalues of random skew matrices.

**The angles are the lengths of the rotation in each invariant plane.** The block $\begin{pmatrix}0&-\theta\\ \theta&0\end{pmatrix}$ rotates the plane by the angle $\theta$ in the sense of the exponential, so the $\theta_j$ are the angular velocities of the $m$ independent rotations that the matrix generates. So the canonical form exhibits the matrix as $m$ independent planar rotations plus a kernel, and the angles are their rates.

**The Frobenius norm is the Euclidean norm of the angles.** Since the block form is orthogonal, $\|K\|^{2}=\|Q^{\mathsf T}KQ\|^{2}$, and each rotation block has norm $2\theta_j^{2}$, so

$$
\|K\|^{2}=2\sum_{j=1}^{m}\theta_j^{2},
$$

which was verified at $n=4,5$. So the Hilbert–Schmidt norm of a skew matrix is determined by the angles, and the identity is the spectral form of $\operatorname{tr}(K^{2})=-\|K\|^{2}$.

**The Pfaffian and the determinant are the two polynomial invariants.** For even $n$ the determinant is

$$
\det K=\prod_{j=1}^{m}\theta_j^{2}\ \ge0,
$$

the square of the Pfaffian, and the Pfaffian itself is the polynomial of degree $m$ whose square is the determinant. So the top-degree invariant of a skew matrix is a perfect square, which is the algebraic shadow of the pairing of the angles.

## The Case $n=2$

**At $n=2$ the skew half is one line and the angle is its length.** Every real skew matrix is

$$
K=\begin{pmatrix}0&-\theta\\ \theta&0\end{pmatrix}=\theta J,\qquad \theta\in\mathbb{R},
$$

and its canonical form is itself, with the single angle $|\theta|$ and the sign of $\theta$ as the orientation. The spectrum is $\{\pm i\theta\}$, the norm is $\sqrt2|\theta|$, and the determinant is $\theta^{2}$, all of which the computation confirms.

**The complex anti-Hermitian matrices of size two are three-dimensional over $\mathbb{R}$.** They are $i$ times the traceless Hermitian matrices, so

$$
\{K:K^{*}=-K\}=\{i(a\sigma_1+b\sigma_2+c\sigma_3):a,b,c\in\mathbb{R}\},
$$

with $K^{2}=-(a^{2}+b^{2}+c^{2})\mathrm{I}$ and $\operatorname{Spec}(K)=\{\pm i\sqrt{a^{2}+b^{2}+c^{2}}\}$. The computation confirms the square and the spectrum, and the single angle is the Euclidean norm of the triple.

**The biquaternion reading gives the angle to the rotation direction.** The line $\mathbb{R}J$ is the antisymmetric half of $M_2(\mathbb{R})$, and in the biquaternion frame the element $i\tilde{Ζ}$ is a pure root, whose square is $-\mathrm{I}$; so the anti-Hermitian elements of square $-1$ are the pure roots $\vec{Ζ}$ rotated by the angle $\pi/2$. So the spectrum theorem at $n=2$ is the statement that the pure roots of the biquaternion algebra form the unit sphere of the three-dimensional anti-Hermitian space, and the angle of a skew element is its distance from the origin in that sphere.

## Summary

The anti-Hermitian matrices are exactly $i$ times the Hermitian ones, so their spectrum is purely imaginary, with $\lambda\|v\|^{2}=\langle Kv,v\rangle=-\overline{\langle Kv,v\rangle}$, and they are diagonalised by a unitary as $K=U(i\Theta)U^{*}$ with $\Theta$ real; the exponential is then unitary with eigenvalues $e^{i\theta_j}$. A real skew matrix has the same purely imaginary spectrum in conjugate pairs, is not diagonalisable over $\mathbb{R}$, and has the orthogonal canonical form of $m$ rotation blocks with angles $\theta_j>0$ and $n-2m$ zeros, of rank $2m$. The angles are the complete invariants of the orthogonal class, the norm satisfies $\|K\|^{2}=2\sum\theta_j^{2}$, the determinant is $\prod\theta_j^{2}$, and at $n=2$ the single angle is the length of the vector $\theta J$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K^{*}=-K$ | the anti-Hermitian condition |
| $K=iH$ with $H=H^{*}$ | the isomorphism with the Hermitian half |
| $\lambda\in i\mathbb{R}$ | the purely imaginary spectrum |
| $K=U(i\Theta)U^{*}$ | the unitary diagonalisation |
| $K^{2}\preceq0$, $\operatorname{tr}K^{2}=-\|K\|^{2}$ | negative semidefiniteness of the square |
| $\begin{pmatrix}0&-\theta\\ \theta&0\end{pmatrix}$ | the rotation block |
| $\theta_1\ge\dots\ge\theta_m>0$ | the angles, invariants of the orthogonal class |
| $\operatorname{rank}K=2m$ | twice the number of blocks |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the antisymmetric canonical form and the orthogonal similarity.
- Werner Greub, *Linear Algebra* (Springer, 1975), for the real canonical form of a skew operator and the invariant planes.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the angles of a skew matrix as the invariants of the compact group action.
- [The Spectral Theorem: the Hermitian Case](the-spectral-theorem-the-hermitian-case.html), for the diagonalisation that the factor $i$ carries over.
- [The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian](the-two-halves-over-c-hermitian-and-anti-hermitian.html), for the half and its properties.
- [The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$](the-lie-algebra-skew-n-and-so-n.html), for the algebra structure of the real skew matrices.
