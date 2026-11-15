# __The Exponential of $\operatorname{Skew}_2$: the Single Rotation Plane__

## Introduction

**The antisymmetric matrices at order two form one plane, spanned by the right-angle rotation $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, and the exponential of $tJ$ is the rotation by the angle $t$ in the direction fixed by $J$, so the exponential of $\operatorname{Skew}_2$ is the whole rotation group $\mathrm{SO}(2)$.**

The article identifies the antisymmetric line, proves the Euler formula $e^{tJ}=(\cos t)I+(\sin t)J$, reads the angle, the period $2\pi$ and the kernel, computes the image as the rotation group, and passes to the complex line where the image is the complex quadric $X^{\mathsf T}X=I$ with determinant one. It assumes *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian*, *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* and *The Exponential of a $2\times2$ Matrix and Its Image*.

It is the real model that the biquaternion article *The Polar Decomposition of a Biquaternion* reads through the rotor.

## The Antisymmetric Line

**The real antisymmetric matrices form a line, and the complex ones form a complex line, both spanned by $J$.**

**Definition.** Let $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$.

**Proposition.** The real antisymmetric matrices are $\{tJ:t\in\mathbb{R}\}$ and the complex antisymmetric matrices are $\{tJ:t\in\mathbb{C}\}$; the square of $J$ is $-I$.

**Proof.** A real antisymmetric two-by-two matrix has the entries $a_{11}=a_{22}=0$ and $a_{21}=-a_{12}$, which is $tJ$ with $t=a_{12}$; the same computation over $\mathbb{C}$ gives the complex line; and $J^{2}=-I$ by direct multiplication.

**Corollary.** The exponential of the antisymmetric line is the set of matrices $\cos t\,I+\sin t\,J$, which is a circle in the real case and a complex circle in the complex case.

**Proof.** Since $J^{2}=-I$, the powers of $tJ$ alternate between $(-1)^{k}t^{2k}I$ and $(-1)^{k}t^{2k+1}J$, and the series separate into the cosine and the sine.

**Corollary.** The exponential of the antisymmetric line is commutative, and $e^{sJ}e^{tJ}=e^{(s+t)J}$.

**Proof.** All the matrices involved are polynomials in the single matrix $J$.

## The Euler Formula

**Theorem.** For every complex number $t$,

$$
e^{tJ}=\begin{pmatrix}\cos t&\sin t\\ -\sin t&\cos t\end{pmatrix}.
$$

**Proof.** The even powers of $tJ$ give $\cos t$ on the diagonal and the odd powers give $\sin t$ on the two off-diagonal entries with the signs shown, by the separation used above.

**Corollary.** The columns of $e^{tJ}$ are unit vectors and orthogonal, so $e^{tJ}$ is a rotation for real $t$.

**Proof.** The columns are $(\cos t,-\sin t)$ and $(\sin t,\cos t)$, of norm one and with vanishing inner product.

**Corollary.** The transpose of $e^{tJ}$ is $e^{-tJ}$, and the inverse is the exponential of the negative angle.

**Proof.** The matrix is orthogonal, and the inverse of a rotation is the rotation by the opposite angle.

## The Angle

**Proposition.** For real $t$ the matrix $e^{tJ}$ is a rotation, and its angle is $t$ measured in the direction of $J$: the matrix $J$ sends the first basis vector to $-e_{2}$, and $e^{tJ}$ sends it to $(\cos t,-\sin t)$, a quarter turn in the same direction followed by the additional angle.

**Proof.** The first column of $e^{tJ}$ is the image of the first basis vector, and a rotation is determined by the image of one vector together with the orientation; at $t=\pi/2$ the image is $-e_{2}$, which is the direction that $J$ itself produces.

**Corollary.** The angle is recovered from the matrix as $t=\arctan\bigl(x_{12}/x_{11}\bigr)$ modulo $\pi$, and its cosine from the trace as $\operatorname{tr}e^{tJ}=2\cos t$.

**Proof.** The entries are the cosine and the sine of the angle, and the trace is twice the cosine.

**Corollary.** The determinant of $e^{tJ}$ is one for every $t$, and the trace lies in the interval $[-2,2]$ in the real case.

**Proof.** The determinant is $e^{\operatorname{tr}(tJ)}=e^{0}=1$ by the determinant formula, and the trace is twice a cosine.

## The Period and the Kernel

**Proposition.** The exponential of the antisymmetric line is periodic with period $2\pi J$, and its kernel on the real line is $2\pi\mathbb{Z}J$.

**Proof.** The cosine and the sine are periodic with period $2\pi$, so $e^{(t+2\pi)J}=e^{tJ}$; and $e^{tJ}=I$ requires $\sin t=0$ and $\cos t=1$, which is $t\in2\pi\mathbb{Z}$.

**Corollary.** The exponential of the real antisymmetric line is a bijection from the interval $[0,2\pi)$ onto the rotation group, and a covering of degree one on that interval.

**Proof.** The angle is determined modulo $2\pi$ by the matrix, and every angle in the interval gives a distinct rotation.

**Corollary.** The kernel in the complex case is $2\pi\mathbb{Z}J$ as well, and the complex exponential is surjective onto the complex quadric of the next section.

**Proof.** The same trigonometric equations hold with complex $t$, so the kernel is the same lattice; the surjectivity is proved below.

## The Image

**Theorem.** The image of the real antisymmetric line under the exponential is the rotation group $\mathrm{SO}(2)$, and the image of the complex line is the set $\{X:X^{\mathsf T}X=I,\ \det X=1\}$.

**Proof.** Every $e^{tJ}$ is orthogonal with determinant one, which gives one inclusion. Conversely a real rotation has the form of the Euler formula with $t$ its angle. In the complex case a matrix with $X^{\mathsf T}X=I$ and $\det X=1$ is $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$ with $a^{2}+b^{2}=1$, and it is $e^{tJ}$ for any $t$ with $\cos t=a$ and $\sin t=b$.

**Corollary.** The exponential of the real antisymmetric line is onto the circle, and the rotation group at order two is a circle.

**Proof.** The theorem gives the surjectivity, and the parametrisation by the angle identifies the group with the circle.

**Corollary.** In the complex case the image is the affine quadric $a^{2}+b^{2}=1$ in two complex variables, which is not compact and is diffeomorphic to a cylinder.

**Proof.** The quadric is parametrised by $t\mapsto(\cos t,\sin t)$, and the parametrisation factors through the period lattice, giving the cylinder $\mathbb{C}/2\pi\mathbb{Z}$.

## The Comparison with the Anti-Hermitian Half

**Proposition.** The real antisymmetric line is contained in the anti-Hermitian half, and the exponential of the larger anti-Hermitian half is a larger group, of real dimension four against one.

**Proof.** A real antisymmetric matrix is anti-Hermitian, and the anti-Hermitian half has real dimension four while the antisymmetric line has dimension one.

**Corollary.** The exponential of the anti-Hermitian half is the unitary group $\mathrm{U}(2)$, and the exponential of the antisymmetric line is the circle of the rotations in one real plane.

**Proof.** Every unitary matrix has a anti-Hermitian logarithm by the surjectivity of the exponential, and the antisymmetric line is the real slice whose exponential is the circle.

**Corollary.** The single rotation plane of the real picture becomes a two-parameter family of phases in the complex picture, because the anti-Hermitian half has the extra imaginary scalars and the third Pauli direction.

**Proof.** The anti-Hermitian half splits as $\mathfrak{su}(2)\oplus\mathbb{R}iI$, and the exponential of the centre is the circle of scalar phases, which is a second circle independent of the rotation.

## Summary

The antisymmetric matrices at order two form a single line spanned by $J$, whose square is $-I$. The exponential of $tJ$ is the rotation by the angle $t$, with the Euler formula $e^{tJ}=(\cos t)I+(\sin t)J$, so the exponential of the line is periodic with period $2\pi J$ and its kernel is $2\pi\mathbb{Z}J$.

The image of the real line is the circle $\mathrm{SO}(2)$, which is the whole rotation group at order two; the image of the complex line is the complex quadric $X^{\mathsf T}X=I$ with determinant one, a cylinder. The anti-Hermitian half contains the antisymmetric line and has four real dimensions, and its exponential is the whole unitary group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | the right-angle rotation $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $t$ | the angle, real or complex |
| $\operatorname{Skew}_2$ | the antisymmetric line |
| $\mathrm{SO}(2)$ | the rotation group at order two |
| $\mathrm{U}(2)$ | the unitary group |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the exponential of a antisymmetric matrix.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the classical groups at low order and their exponentials.
- [The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian](the-lie-algebra-skew-2-one-dimension-hence-abelian.html), for the bracket that vanishes on the line.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the antisymmetric line as one of the two halves.
- [The Spectral Theorem: the Anti-Hermitian Case and the Two Imaginary Eigenvalues](the-spectral-theorem-the-skew-hermitian-case-and-the-two-imaginary-eigenvalues.html), for the complex half that contains the real line.
