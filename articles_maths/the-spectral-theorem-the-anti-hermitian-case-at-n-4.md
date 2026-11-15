# __The Spectral Theorem: the Anti-Hermitian Case and the Reality of the Spectrum at $n=4$__

## Introduction

**An anti-Hermitian matrix is $i$ times a Hermitian one, so its spectrum is purely imaginary and its exponential is unitary; for a real antisymmetric matrix of order four the spectrum is $\{i\theta_1,-i\theta_1,i\theta_2,-i\theta_2\}$, the two angles exist and are independent, the Pfaffian is their product, and the two summands of $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ carry the two parameters.**

The article proves the purely imaginary spectrum, identifies the exponential with the map onto the unitary group, derives the real normal form with two rotation blocks, relates the two angles to the two ideals and to the isoclinic families, computes the Pfaffian, and reads the whole picture in the biquaternion algebra as a two-sided rotation $L_{e^{\theta_1 i}}R_{e^{\theta_2 i}}$.

It assumes *Normal Matrices and the Common Spectral Theorem at $n=4$*, *The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$* and *Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$*. The model at order two is *The Spectral Theorem: the Anti-Hermitian Case and the Two Imaginary Eigenvalues*.

## The Anti-Hermitian Case

**Definition.** $A$ is **anti-Hermitian** when $A^{\ast}=-A$.

**Proposition.** $A$ is anti-Hermitian exactly when $A=iH$ with $H$ Hermitian, and then the spectrum of $A$ is $i$ times the spectrum of $H$, hence purely imaginary.

**Proof.** $H=-iA$ satisfies $H^{\ast}=iA^{\ast}=-iA=H$; the eigenvalues of $iH$ are $i\lambda$ with $\lambda$ an eigenvalue of $H$, by the spectral resolution.

**Corollary.** $A=i\sum_k\theta_kP_k$ with $\theta_k$ real and $P_k$ the spectral projectors, so an anti-Hermitian matrix is a real linear combination of commuting orthogonal projections after multiplication by $i$.

**Proof.** Insert the Hermitian resolution of $H$.

**Corollary.** The eigenvalues come in conjugate pairs when the matrix is real, since a real matrix has a real characteristic polynomial.

**Proof.** The conjugate of an eigenvalue is an eigenvalue of the conjugate matrix, which is the matrix itself.

**The real dimension.** $\mathfrak{u}(4)$ has real dimension $16$, and its anti-Hermitian part is the whole of it, since an anti-Hermitian matrix has $16$ real parameters.

**Proof.** A Hermitian matrix has $16$ real parameters, and multiplication by $i$ is a real-linear isomorphism onto the anti-Hermitian matrices.

## The Exponential onto the Unitary Group

**Theorem.** If $A$ is anti-Hermitian then $e^{A}$ is unitary, and every unitary matrix is of this form.

**Proof.** $(e^{A})^{\ast}=e^{A^{\ast}}=e^{-A}=(e^{A})^{-1}$ for anti-Hermitian $A$. Conversely a unitary $U$ has a spectral resolution $U=V\operatorname{diag}(e^{i\theta_1},\dots,e^{i\theta_4})V^{\ast}$ with real $\theta_k$, so $U=e^{iH}$ with $H=V\operatorname{diag}(\theta_1,\dots,\theta_4)V^{\ast}$ Hermitian, that is $U=e^{A}$ with $A=iH$ anti-Hermitian.

**Corollary.** The exponential maps $\mathfrak{u}(4)$ onto $U(4)$, and it is a local diffeomorphism at every point whose eigenvalues avoid the differences $2\pi i\mathbb{Z}$.

**Proof.** Surjectivity is the theorem; the derivative of the exponential is invertible exactly when no two eigenvalues of the argument differ by a nonzero multiple of $2\pi i$.

**Corollary.** $U(4)$ is connected, and it is the image of a real vector space of dimension $16$; the map is not injective.

**Proof.** The image of a connected space is connected; and $e^{A}=e^{A+2\pi i\,\mathrm I}$.

**The eigenvalues on the circle.** The spectrum of $e^{A}$ lies on the unit circle, at the points $e^{i\theta_k}$, and the angles are the eigenvalues of $-iA$.

**Proof.** The spectral mapping theorem for the exponential.

## Real Anti-Hermitian Matrices and the Two Angles

**Theorem.** A real antisymmetric matrix of order four has a real orthogonal $Q$ and real numbers $\theta_1,\theta_2$ with
$$
A=Q\begin{pmatrix}R_{\theta_1}&0\\0&R_{\theta_2}\end{pmatrix}Q^{\mathsf T},\qquad R_\theta=\begin{pmatrix}0&-\theta\\ \theta&0\end{pmatrix}.
$$

**Proof.** The real eigenvalues of a real antisymmetric matrix are zero, since a real eigenvalue $\lambda$ satisfies $\lambda=-\lambda$; the complex ones come in conjugate pairs, and a conjugate pair $\pm i\theta$ spans a real two-dimensional invariant plane on which the matrix is $\theta$ times a rotation by a quarter turn. Two such planes exhaust the four dimensions.

**Corollary.** The spectrum is $\{i\theta_1,-i\theta_1,i\theta_2,-i\theta_2\}$, and the eigenvalues are purely imaginary and come in pairs of opposite sign.

**Proof.** The eigenvalues of $R_\theta$ are $\pm i\theta$.

**Corollary.** $\det A=\theta_1^{2}\theta_2^{2}\ge0$, so a real antisymmetric matrix of order four has a nonnegative determinant, and it is singular exactly when one angle vanishes.

**Proof.** The determinant is the product of the four eigenvalues.

**The count of the angles.** The number of independent angles is $\lfloor4/2\rfloor=2$: the first order at which there are two, and the first at which the generic rotation is not simple.

**Proof.** One angle per invariant plane, and the four dimensions give two planes.

## The Two Summands and the Two Parameters

**Theorem.** $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ as the self-dual and the anti-self-dual parts, and in the normal form the two parts are
$$
\tfrac12(A+\ast A)=\theta_1J_1,\qquad \tfrac12(A-\ast A)=\theta_2J_2,
$$
with $J_1=e_1\wedge e_2+e_3\wedge e_4$ self-dual and $J_2=e_1\wedge e_2-e_3\wedge e_4$ anti-self-dual, so each summand carries exactly one of the two angles.

**Proof.** In the normal form $A=\theta_1J_1+\theta_2J_2$ because $R_{\theta_1}\oplus R_{\theta_2}=\theta_1J_1+\theta_2J_2$; the Hodge star fixes $J_1$ and reverses $J_2$, since $*e_1\wedge e_2=e_3\wedge e_4$.

**Corollary.** A rotation is isoclinic exactly when $|\theta_1|=|\theta_2|$, that is when the two components have equal size, and the two isoclinic families are $\theta_1=\theta_2$ and $\theta_1=-\theta_2$.

**Proof.** Isocliny is the equality of the two angles up to sign, which is the equality of the sizes of the two components.

**Corollary.** Each summand is a copy of $\mathfrak{sl}_2$ with its single angle, and the covering group of the rotation group is $SU(2)\times SU(2)$ modulo the pair $(-1,-1)$.

**Proof.** Each summand exponentiates onto a copy of $SU(2)$, the two copies act independently, and the pair $(-1,-1)$ acts trivially.

**The Killing form.** $K=8\operatorname{tr}(XY)$ on $\mathfrak{so}(4)$ is negative definite, and the two summands are orthogonal.

**Proof.** Every element is traceless, and the product of a self-dual and an anti-self-dual matrix has zero trace.

## The Pfaffian

**Definition.** For a real antisymmetric matrix of order four, $\operatorname{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$.

**Theorem.** $\operatorname{Pf}(A)^{2}=\det A$, and in the normal form $\operatorname{Pf}(A)=\pm\theta_1\theta_2$ with the sign of $Q$.

**Proof.** Both sides are polynomials of degree four in the entries and agree on the normal form up to the square of the orthogonal change, whose determinant is $\pm1$; the square removes the sign.

**Corollary.** An invertible real antisymmetric matrix of order four has $\operatorname{Pf}\neq0$, and the sign of the Pfaffian separates the invertible ones into two components.

**Proof.** $\operatorname{Pf}^{2}=\det$, and the Pfaffian is continuous.

**Corollary.** $\operatorname{Pf}(QAQ^{\mathsf T})=\det(Q)\operatorname{Pf}(A)$, so the Pfaffian is the invariant of the antisymmetric half that changes sign under the orientation-reversing changes of frame.

**Proof.** The transformation rule of the Pfaffian under congruence by an orthogonal matrix.

**The two angles from the Pfaffian.** $|\operatorname{Pf}A|=|\theta_1\theta_2|$ is the product of the two angles, and the sum of their squares is $\tfrac12\lVert A\rVert_F^{2}$.

**Proof.** The eigenvalues are $\pm i\theta_1,\pm i\theta_2$, so the sum of the squared moduli is $2(\theta_1^{2}+\theta_2^{2})=\lVert A\rVert_F^{2}$.

## The Biquaternion Reading

**Theorem.** Every real antisymmetric matrix of order four is $A=L_u+R_v$ with $u,v$ imaginary biquaternions, and $e^{A}=L_{e^{u}}R_{e^{v}}$ is a two-sided rotation with the two one-sided unit quaternions.

**Proof.** The three left multiplications by $i,j,k$ and the three right multiplications span a six-dimensional space of real antisymmetric matrices, which is all of $\mathfrak{so}(4)$; the left and right families commute, so the exponential of the sum is the product of the exponentials.

**Corollary.** The two angles are the rotation angles of the two one-sided unit quaternions, and the isoclinic rotations are those with one of the two factors equal to a real scalar.

**Proof.** $e^{u}$ with $u=\theta i$ is $\cos\theta+i\sin\theta$, whose left multiplication rotates both planes by $\theta$; a real factor rotates nothing.

**Corollary.** The two summands of $\mathfrak{so}(4)$ are the imaginary left multiplications and the imaginary right multiplications, so the split of the Lie algebra is the split of the two one-sided families.

**Proof.** The left multiplications form a three-dimensional Lie algebra isomorphic to $\mathfrak{sl}_2$, the right ones another, and they commute.

**The reality of the spectrum in the biquaternion language.** The left multiplication by a unit biquaternion of the form $e^{u}$ with $u$ imaginary has eigenvalues $e^{\pm i\theta}$, each twice, which is the statement that the two planes rotate by the same angle.

**Proof.** The eigenvalues of the left matrix are those of the multiplication operator, computed from the $2\times2$ image.

## Summary

An anti-Hermitian matrix is $i$ times a Hermitian one, so its spectrum is purely imaginary and its exponential is unitary; every unitary matrix is the exponential of an anti-Hermitian one, and the exponential is onto but not injective.

A real antisymmetric matrix of order four has the normal form with two rotation blocks and the spectrum $\{i\theta_1,-i\theta_1,i\theta_2,-i\theta_2\}$, with $\det A=\theta_1^{2}\theta_2^{2}$, so it is singular exactly when an angle vanishes. The Pfaffian is $\pm\theta_1\theta_2$ and its square is the determinant, so the sign of the Pfaffian separates the two components of the invertible antisymmetric matrices.

The two summands of $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ carry the parameters $\theta_\pm=(\theta_1\pm\theta_2)/2$, and the isoclinic rotations are those with one parameter zero. In the biquaternion algebra the real antisymmetric matrices are the sums $L_u+R_v$, and the rotation is the two-sided action of two one-sided unit quaternions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^{\ast}=-A$ | anti-Hermitian |
| $A=iH$ | the Hermitian form of an anti-Hermitian matrix |
| $R_\theta$ | the real rotation block |
| $\theta_1,\theta_2$ | the two angles |
| $\theta_\pm$ | the two parameters of the two ideals |
| $\operatorname{Pf}A$ | the Pfaffian, with $\operatorname{Pf}^{2}=\det$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the real normal form of an antisymmetric matrix and the Pfaffian.
- [The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$](the-lie-algebra-skew-4-and-so-4.html), for the two ideals and the brackets.
- [Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$](simple-and-non-simple-rotations-one-angle-at-n-le-3-two-angles-at-n-ge-4.html), for the geometry of the two angles.
- [The Rotor as a Square Root of a Rotation: the Two Signs and the Double Cover at $n=4$](the-rotor-as-a-square-root-of-a-rotation-the-two-signs-and-the-double-cover-at-n-4.html), for the two-sided rotor.
- [The Spectral Theorem: the Anti-Hermitian Case and the Two Imaginary Eigenvalues](the-spectral-theorem-the-anti-hermitian-case-and-the-two-imaginary-eigenvalues.html), for the case at order two.
