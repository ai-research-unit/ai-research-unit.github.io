# __The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** The spin-half carrier is the plane of multiples of a rank-one projection and its closures are the minimal left ideals. What is the determinant on these spaces, and is any element of a single ideal N-regular?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-Half Bispinors and N Norm Regularity](the-spin-half-bispinor-spaces-and-n-norm-regularity.html). There the norm is $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ and the null plane is $\mathbb{C}\tilde\Pi_+$; here the norm is $\det A$, the plane is $\mathbb{C}P$ and the ideal is $M_2P$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That $\det P=0$ and $\det(Y\!P)=0$ for every $Y$, so the plane and both ideals are null. That the ideals are maximal isotropic, of complex dimension two, half of four. That on the bispinor the determinant is the pairing, $\det(X_++X_-)=2B(X_+,X_-)$. That the pairing is nondegenerate and that the polar form is $\sum_\mu x_\mu y_\mu$ in the coefficient basis. The comparison with the other two carriers.

**What the article does not do.** It does not treat the discriminant on these spaces, which is [The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-spectral-regularity-in-m2c.html); it does not treat the four sectors in full, which is [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $Q_t=\tfrac12\operatorname{tr}A$ and $N(\tilde Q)=\det A$. The coefficient basis is $(\mathrm I_2,E_x,E_y,E_z)$ with $E_k=-i\sigma_k$ and coefficient tuple $x=(x_0,x_1,x_2,x_3)$. The polar form is $B(X,Y)=\tfrac12(\det(X+Y)-\det X-\det Y)$. The Hermitian form is $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$, a different object.

**Boundaries.** The spaces are [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html). The Dirac pairing is [Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$](spinors-and-dirac-spinors-in-the-biquaternion-algebra-in-m2c.html). The norm in general is [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $P$ a rank-one projection, $P_{\perp}=\mathrm I_2-P$, $S_\pm=M_2P^{(\perp)}$, $x$ a coefficient tuple, $B$ the polar form, $\langle\cdot,\cdot\rangle$ the Hermitian form.

## The Norm of the Projection

**The formula.** In coefficients $P=\tfrac12(\mathrm I_2+n_1E_1+n_2E_2+n_3E_3)$ because $\sigma_k=iE_k$, so
$$
\det P=\frac14\left(1-\sum_k n_k^2\right)=0,
$$
the cancellation being $|n|=1$. Verified exactly.

**The two squares.** The scalar coordinate contributes $\tfrac14$ and the vector coordinates contribute $-\tfrac14|n|^2$. The cancellation is the unit length of the axis written as an identity.

**An idempotent of determinant zero.** From $P^2=P$, multiplicativity gives $(\det P)^2=\det P$, so the determinant of an idempotent is $0$ or $1$. The rank-one projections are the case $0$.

## The Plane and the Ideals Are Null

**The plane.** $\det(\lambda P)=\lambda^2\det P=0$ for every $\lambda$: the whole plane lies in the singular locus.

**The ideal.** For every $Y$,
$$
\det(YP)=\det Y\det P=0 .
$$
So both ideals $M_2P$ and $M_2P_{\perp}$ lie in the singular locus, and no element of a single ideal is invertible.

**Verified.** On a hundred random elements of the plane and of the ideal the determinant vanishes to $8\cdot10^{-16}$.

**The closure does not repair the nullity.** The ideal repairs the invariance of the plane but stays inside the singular locus; the two notions are independent.

## The Isotropic Dimension

**The definition.** A subspace is isotropic when the determinant vanishes on it and totally isotropic when the polar form vanishes on it in both arguments.

**The ideals are totally isotropic.** $B(XP,YP)=\tfrac12(\det((X+Y)P)-0-0)=0$, verified for all pairs in the basis. Each ideal is isotropic of complex dimension two.

**The maximality.** For a nondegenerate quadratic form on a space of dimension $N$ an isotropic subspace has dimension at most $N/2$. Here $N=4$, so the bound is $2$, and the ideals attain it: they are maximal isotropic.

**The plane is isotropic and not maximal.** It has complex dimension one, and it is totally isotropic as well, since $B(\lambda P,\mu P)=\lambda\mu\det P=0$. The dimension, and not the total isotropy, separates it from the ideals.

## The Bispinor Read

**The pairing.** For $X=X_++X_-$ with $X_\pm=XP^{(\perp)}$,
$$
\det X=2B(X_+,X_-),
$$
because the two pure terms vanish. Verified on a hundred random pairs to $10^{-15}$.

**The criterion.** $X$ is invertible exactly when its two parts pair non-trivially.

**The nondegeneracy.** In the coefficient basis the Gram matrix of $B$ is the identity, verified: $B$ has rank four and no radical. So the pairing $S_+\times S_-\to\mathbb{C}$ is nondegenerate, and the two ideals are dual to each other under $B$.

**The coefficient formula.** $B(X,Y)=\sum_{\mu=0}^{3}x_\mu y_\mu$ and $\det X=\sum_\mu x_\mu^2$, both verified on a hundred random pairs to $2.4\cdot10^{-15}$ and $4.5\cdot10^{-15}$. These are the source's $N=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ and its polar form, in the matrix coefficients.

**The form is complex-bilinear, not Hermitian.** $B(P,P)=0$ while $\langle P,P\rangle=\tfrac12$: the two forms have the same Gram matrix on the basis and differ off the real span, because $B(iX,iY)=-B(X,Y)$ and $\langle iX,iY\rangle=\langle X,Y\rangle$.

**The two ideals are dual.** The determinant restricted to the bispinor is the duality pairing of $S_+$ with $S_-$; in a basis of one and its dual basis of the other the pairing is the identity matrix, up to the factor two. Neither ideal carries a norm of its own.

## The Pairing and the Axis

**The pairing moves with the axis.** Both ideals move, so the pairing does; every statement holds at every axis, and the axis is a parameter.

**The pairing is symmetric.** $B(X_+,X_-)=B(X_-,X_+)$, so the order of the two parts does not matter.

## The Three Carriers Compared

| carrier | $\det$ on it | singular locus in it |
|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $\lambda^2$ | $\{0\}$ |
| plane and ideals | $0$ | the whole space |
| vector part $\mathfrak{su}(2)$ | $\lvert v\rvert^2$ | $\{0\}$ |

**Where the carrier sits.** The plane away from the origin lies in $\Sigma_{01}$: singular and spectrally regular. The centre lies in $\Sigma_{10}$ and the vector part in $\Sigma_{11}$.

## Worked Example

**The axis $e_3$.** $P=\operatorname{diag}(1,0)$, $P_{\perp}=\operatorname{diag}(0,1)$, and $S_+$ is the set of matrices with second column zero.

**An element of the ideal.** $X=\begin{pmatrix}2&0\\3&0\end{pmatrix}$: $\det=0$, rank one, non-zero, singular.

**A bispinor.** $X=\begin{pmatrix}2&0\\3&1\end{pmatrix}=X_++X_-$ with $X_+=\begin{pmatrix}2&0\\3&0\end{pmatrix}$ and $X_-=\begin{pmatrix}0&0\\0&1\end{pmatrix}$; $\det=2$ and $2B(X_+,X_-)=2$, verified.

## Where $n=2$ Differs

**The isotropic dimension.** At $n=2$ the ideals are maximal isotropic of complex dimension two, half of four. At order $n$ the maximal isotropic subspaces of the determinant on $M_n(\mathbb{C})$ have dimension $\lfloor n^2/2\rfloor$, and the minimal left ideals have dimension $n$, which is smaller for $n\ge3$.

**The pairing.** At $n=2$ the bispinor is a sum of two ideals and the determinant is their pairing. At order $n$ the two Peirce halves are blocks of sizes $1$ and $n-1$ for a rank-one projection, and the determinant of their sum is the product of the two block determinants, so the pairing is replaced by a product of a scalar and an $(n-1)$-minor.

**What does not differ.** The nullity of the ideal, $\det(Y\!P)=0$, holds at every order, because the rank of $YP$ is at most one.

## Summary

The determinant of a rank-one projection vanishes, and multiplicativity gives $\det(Y\!P)=0$ for every $Y$: the plane and both minimal left ideals are null, and no element of a single ideal is invertible. The ideals are totally isotropic of complex dimension two, which is maximal for a quadratic form on four dimensions.

On the bispinor the determinant becomes the pairing, $\det(X_++X_-)=2B(X_+,X_-)$, and the pairing is nondegenerate: in the coefficient basis $B$ has the identity Gram matrix, and $B(X,Y)=\sum x_\mu y_\mu$. The Hermitian form $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$ is a different form, complex-linear in both arguments versus conjugate-linear in one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P,\ P_{\perp}$ | a rank-one projection and its complement |
| $S_\pm=M_2P^{(\perp)}$ | the two minimal left ideals |
| $x=(x_0,x_1,x_2,x_3)$ | the coefficient tuple in $(\mathrm I_2,E_x,E_y,E_z)$ |
| $B(X,Y)$ | the polar form of the determinant |
| $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$ | the Hermitian form |

## Further Reading

- [The Spin-Half Bispinors and N Norm Regularity](the-spin-half-bispinor-spaces-and-n-norm-regularity.html), for the source's isotropy argument.
- [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html), for the plane and the ideals.
- [The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-spectral-regularity-in-m2c.html), for the discriminant on the same spaces.
- [Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$](spinors-and-dirac-spinors-in-the-biquaternion-algebra-in-m2c.html), for the Dirac pairing read as the determinant.
- [The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-n-norm-regularity-in-m2c.html), for the opposite extreme on the centre.
