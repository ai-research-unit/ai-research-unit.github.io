# __The Numerical Range and the Field of Values of $M_4(\mathbb{C})$__

## Introduction

For $A\in M_4(\mathbb{C})$ the **field of values**, or **numerical range**, is the set

$$
W(A)=\bigl\{x^*Ax:\ x\in\mathbb{C}^{4},\ x^*x=1\bigr\},
$$

the image of the unit sphere under the quadratic form of $A$. The general theory — compactness, the containment of the spectrum, the Toeplitz–Hausdorff convexity, the equivalence $\tfrac12\|A\|\le w(A)\le\|A\|$ of the numerical radius with the norm, and the Hermitian and normal cases — is *Hermitian Operators and the Numerical Range*, stated there for a bounded operator on a Hilbert space. This article does not restate it. It computes the field of values in the four-dimensional case: the support function, the elliptical range theorem of the $2\times2$ compressions with its proof, the field of values of the nilpotent Jordan block $J_4$ as the disk of radius $\cos(\pi/5)$, the rank-one case, the block-diagonal rule, and the comparison with the biquaternion model.

The spectrum and the resolvent are *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*; the singular values and the operator norm are *The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$* and *The Polar Decomposition of $M_4(\mathbb{C})$*; the Hermitian structure is *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*; the biquaternion matrix is *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*; and the two-dimensional case of the qubit is *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Spin, Qubits and the Bloch Vector*. The infinite-dimensional theory of the numerical range and the Toeplitz–Hausdorff theorem in that setting are not treated here.

## The Field of Values and Its Support Function

**Definition.** $W(A)=\{x^*Ax:\|x\|=1\}$ and $w(A)=\max_{z\in W(A)}|z|$.

**Proposition (the elementary properties).** The set $W(A)$ is compact and connected, it contains the spectrum, and it is invariant under unitary similarity, $W(UAU^*)=W(A)$ for $U\in U(4)$. For scalars $\alpha,\beta$,

$$
W(\alpha A+\beta I_4)=\alpha W(A)+\beta .
$$

**Proof.** The unit sphere is compact and the quadratic form is continuous, so the image is compact; the sphere is connected, so the image is connected. An eigenvector with eigenvalue $\lambda$ gives $\lambda\in W(A)$. The unitary invariance is the substitution $x=Uy$, and the affine rule is the computation $y^*(\alpha A+\beta I)y=\alpha y^*Ay+\beta$.

**Proposition (the Hermitian and normal cases).** For Hermitian $H$,

$$
W(H)=[\lambda_{\min}(H),\lambda_{\max}(H)] .
$$

For normal $A$,

$$
W(A)=\operatorname{conv}\bigl(\operatorname{spec}A\bigr).
$$

**Proof.** The Rayleigh quotient of a Hermitian matrix lies between the extreme eigenvalues, and both are attained, so the range is the interval. For normal $A=UDU^*$ and unit $x$ with $y=U^*x$,

$$
x^*Ax=\sum_{k=1}^{4}|y_k|^{2}\lambda_k,
$$

a convex combination of the eigenvalues because $\sum_k|y_k|^{2}=1$; every convex combination is realized by a unit vector with the prescribed moduli.

**The support function.** For a compact convex set $K\subset\mathbb{C}$ let

$$
h_K(\alpha)=\max_{z\in K}\operatorname{Re}\bigl(e^{-i\alpha}z\bigr).
$$

Then

$$
h_{W(A)}(\alpha)=\lambda_{\max}\bigl(\operatorname{Re}(e^{-i\alpha}A)\bigr),
\qquad
\operatorname{Re}M=\tfrac12(M+M^*) .
$$

**Proof.** For a unit $x$,

$$
\operatorname{Re}\bigl(e^{-i\alpha}x^*Ax\bigr)
=x^*\operatorname{Re}(e^{-i\alpha}A)x,
$$

and the maximum of the Rayleigh quotient of a Hermitian matrix is its largest eigenvalue.

**Corollary (the half-plane criterion).** $W(A)$ lies in the open right half-plane exactly when $A+A^*$ is positive definite.

**Proof.** $\operatorname{Re}(x^*Ax)=x^*\bigl(\tfrac12(A+A^*)\bigr)x$ is positive for every nonzero $x$ exactly when the Hermitian part is positive definite.

**Corollary (the boundary).** $W(A)$ is the intersection of the half-planes $\operatorname{Re}(e^{-i\alpha}z)\le h_{W(A)}(\alpha)$, and its boundary is the envelope of the supporting lines of these half-planes.

**Proof.** A compact convex set is the intersection of its supporting half-planes.

## The Two-Dimensional Ellipse

**Lemma (the compression).** Let $x,y$ be orthonormal, $V=\operatorname{span}\{x,y\}$, and $A_V=P_VA|_V$. Then $x^*A_Vx=x^*Ax$, $y^*A_Vy=y^*Ay$, and $W(A_V)\subset W(A)$.

**Proof.** For $v\in V$ one has $P_Vv=v$, so $v^*A_Vv=v^*Av$; every unit vector of $V$ is a unit vector of $\mathbb{C}^{4}$, which gives the inclusion.

**Theorem (the elliptical range in dimension two).** Let $T\in M_2(\mathbb{C})$ have eigenvalues $\lambda_1,\lambda_2$. Then $W(T)$ is the closed ellipse with foci $\lambda_1,\lambda_2$ and semi-minor axis

$$
b=\frac12\sqrt{\operatorname{tr}(T^*T)-|\lambda_1|^{2}-|\lambda_2|^{2}} .
$$

In particular, if $T$ has the single eigenvalue $\lambda$ and the nilpotent part $c$, then $W(T)$ is the disk of radius $|c|/2$ centred at $\lambda$.

**Proof.** By Schur's theorem $T$ is unitarily similar to

$$
\begin{pmatrix}\lambda_1&c\\0&\lambda_2\end{pmatrix},\qquad c\ge0,
$$

so it suffices to treat this matrix. For $x=(\cos\theta,e^{i\varphi}\sin\theta)$ with $0\le\theta\le\pi/2$,

$$
x^*Tx=\lambda_1\cos^{2}\theta+\lambda_2\sin^{2}\theta
+c\,e^{i\varphi}\cos\theta\sin\theta .
$$

For fixed $\theta$ this is a circle with centre $s(\theta)=\lambda_1\cos^{2}\theta+\lambda_2\sin^{2}\theta$ and radius $c|\cos\theta\sin\theta|$, and the phase is free. Hence the support function of $W(T)$ is

$$
h(\alpha)=\max_{\theta}\Bigl[\operatorname{Re}\bigl(e^{-i\alpha}s(\theta)\bigr)
+c|\cos\theta\sin\theta|\Bigr].
$$

Put $u=\cos^{2}\theta$ and $t=2u-1$, so that $|\cos\theta\sin\theta|=\tfrac12\sqrt{1-t^{2}}$, and write $m=\tfrac12(\lambda_1+\lambda_2)$, $f=\tfrac12(\lambda_1-\lambda_2)$. Then $s=m+ft$ and

$$
h(\alpha)=\operatorname{Re}(e^{-i\alpha}m)
+\max_{|t|\le1}\Bigl[t\operatorname{Re}(e^{-i\alpha}f)+\tfrac{c}{2}\sqrt{1-t^{2}}\Bigr].
$$

The maximum is $\sqrt{\operatorname{Re}(e^{-i\alpha}f)^{2}+(c/2)^{2}}$, by the Cauchy–Schwarz inequality applied to $(t,\sqrt{1-t^{2}})$ and $(\operatorname{Re}(e^{-i\alpha}f),c/2)$. This is the support function of the ellipse with centre $m$, foci $m\pm f$ and semi-minor axis $c/2$. Two compact convex sets with the same support function coincide, so $W(T)$ is that ellipse. Finally,

$$
\operatorname{tr}(T^*T)=|\lambda_1|^{2}+|\lambda_2|^{2}+c^{2},
$$

so $c=\sqrt{\operatorname{tr}(T^*T)-|\lambda_1|^{2}-|\lambda_2|^{2}}$ and the semi-minor axis is $c/2$. When $\lambda_1=\lambda_2=\lambda$ the foci coincide and the ellipse is the disk of radius $c/2$.

**Corollary (the two-dimensional classification).** For $T\in M_2(\mathbb{C})$ the field of values determines the unitary orbit: its foci are the eigenvalues and twice its semi-minor axis is the modulus of the Schur parameter.

**Proof.** The unitary orbit of a $2\times2$ matrix is determined by its eigenvalues and by $|c|$ in the Schur form; the phases of $c$ are removed by conjugation by a diagonal unitary. The ellipse gives the eigenvalues as its foci and $|c|=2b$.

**Corollary (the compression argument).** Every segment between two points of $W(A)$ lies in $W(A)$, because it lies in the field of values of a two-dimensional compression, which is an ellipse, and that ellipse is contained in $W(A)$.

**Proof.** Apply the lemma to the two unit vectors that realize the two points; the compression is $2\times2$, so its field of values is convex by the theorem.

## The Nilpotent Chain

Let

$$
J_4=\sum_{k=1}^{3}E_{k,k+1}
=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\0&0&0&0\end{pmatrix}.
$$

**Theorem.** The field of values of $J_4$ is the closed disk

$$
W(J_4)=\bigl\{z\in\mathbb{C}:|z|\le\cos(\pi/5)\bigr\},
\qquad \cos(\pi/5)=\frac{1+\sqrt5}{4}.
$$

**Proof.** Write $x_k=r_ke^{i\theta_k}$ with $r_k\ge0$ and $\sum_k r_k^{2}=1$. Then

$$
x^*J_4x=\sum_{k=1}^{3}\bar x_kx_{k+1}
=\sum_{k=1}^{3}r_kr_{k+1}\,e^{i(\theta_{k+1}-\theta_k)} .
$$

The differences $\delta_k=\theta_{k+1}-\theta_k$ are arbitrary: choose $\theta_1=0$ and $\theta_{k+1}=\theta_k+\delta_k$. Hence, for fixed radii, the set of values is the Minkowski sum of the three circles of radii $r_1r_2$, $r_2r_3$, $r_3r_4$, which is the closed disk of radius

$$
\rho(r)=r_1r_2+r_2r_3+r_3r_4 .
$$

The field of values is therefore the union of the disks of radii $\rho(r)$ over the unit sphere; because $\rho$ is continuous on a connected sphere, the set of its values is an interval $[0,\rho_{\max}]$, and the union is the disk of radius $\rho_{\max}$. Now $2\rho(r)=r^{\mathsf T}Ar$ with $A$ the adjacency matrix of the path $P_4$, whose eigenvalues are $2\cos(k\pi/5)$, $k=1,2,3,4$. The largest is $2\cos(\pi/5)$, so $\rho_{\max}=\cos(\pi/5)$.

**Corollary.** $w(J_4)=\cos(\pi/5)\approx0.809$, while $\|J_4\|=1$ and $\rho(J_4)=0$.

**Proof.** The numerical radius is the radius of the disk; the operator norm of the shift is one; the only eigenvalue is zero.

**Theorem (the general chain).** For the nilpotent Jordan block $J_n$ of size $n\ge2$,

$$
W(J_n)=\Bigl\{z:|z|\le\cos\frac{\pi}{n+1}\Bigr\}.
$$

**Proof.** The same computation gives the union of disks of radii $\sum_{k=1}^{n-1}r_kr_{k+1}$, which is half the quadratic form of the adjacency matrix of the path $P_n$; its largest eigenvalue is $2\cos(\pi/(n+1))$.

**The three radii.** The nilpotent chain separates the three invariants: $\rho(J_4)=0$, $w(J_4)=\cos(\pi/5)$ and $\|J_4\|=1$. The spectral radius is blind to the nilpotent part, the operator norm sees the whole chain, and the field of values sees the length of the chain through the adjacency spectrum.

## The Rank-One and the Block Cases

**Proposition (the rank-one case).** Let $A=uv^*$ with $u,v\ne0$. Then $W(A)$ is the ellipse with foci $0$ and $v^*u$ and semi-minor axis

$$
b=\frac12\sqrt{\|u\|^{2}\|v\|^{2}-|v^*u|^{2}} .
$$

**Proof.** Let $V=\operatorname{span}\{u,v\}$. The matrix $A$ maps $\mathbb{C}^{4}$ into $\mathbb{C}u\subset V$ and vanishes on $V^{\perp}$, because $v^*w=0$ for $w\perp v$; hence $A=P_VAP_V$ and $W(A)=W(A|_V)$. On $V$ the matrix is a $2\times2$ matrix of rank one with trace $v^*u$ and determinant zero, so its eigenvalues are $v^*u$ and $0$. The elliptical range theorem gives the foci, and $\operatorname{tr}(A^*A)=\|u\|^{2}\|v\|^{2}$ gives the semi-minor axis.

**Corollary.** If $v^*u=0$, then $W(uv^*)$ is the disk of radius $\|u\|\,\|v\|/2$ centred at the origin. If $u=v$ is a unit vector, then $W(uv^*)=[0,1]$.

**Proof.** The first statement is the rank-one formula with $v^*u=0$. The second is the Hermitian case for the orthogonal projector of rank one.

**Proposition (the block-diagonal rule).** For $A\in M_m(\mathbb{C})$ and $B\in M_n(\mathbb{C})$,

$$
W(A\oplus B)=\operatorname{conv}\bigl(W(A)\cup W(B)\bigr).
$$

**Proof.** A unit vector of the direct sum splits as $(x,y)$ with $t=\|x\|^{2}$ and $1-t=\|y\|^{2}$; if both are nonzero,

$$
(x,y)^*(A\oplus B)(x,y)=t\,\frac{x^*Ax}{\|x\|^{2}}+(1-t)\,\frac{y^*Ay}{\|y\|^{2}},
$$

a convex combination of a point of $W(A)$ and a point of $W(B)$, and the endpoint cases are the points themselves. Conversely every convex combination is realized by choosing the norms.

**Corollary (the failure of completeness in dimension four).** The matrices $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus0_2$ have the same field of values, the disk of radius $1/2$, and they are not unitarily similar.

**Proof.** For $T=J_2(0)$ the field of values is the disk of radius $1/2$ by the elliptical range theorem. The block rule gives the disk for both matrices, because $0$ lies in that disk. The ranks are two and one.

## The Place in the Category

**The spectrum and the singular values.** The field of values contains the spectrum and lies in the disk of radius $\|A\|$; the numerical radius lies between the spectral radius and the operator norm. The singular values give the radius of the image of the unit sphere, the field of values the radius of the image of the quadratic form. The gap measures the departure from normality: for a normal matrix $w(A)=\|A\|=\rho(A)$, while for the nilpotent chain $\rho(J_4)=0$, $w(J_4)=\cos(\pi/5)$ and $\|J_4\|=1$.

**The Hermitian decomposition.** The support function of $W(A)$ is the largest eigenvalue of $\operatorname{Re}(e^{-i\alpha}A)$, so each supporting line is fixed by the spectrum of a Hermitian matrix built from $A$. The Hermitian part $A+A^*$ gives the directions $0$ and $\pi/2$. The field of values does not determine $A$: $J_2(0)$ and $e^{i\varphi}J_2(0)$ have the same disk for every phase, while their Hermitian parts differ.

**The biquaternion model.** For $\tilde Q\in\mathbb{B}$ the matrix $\mathsf{M}_2(\tilde Q)$ has the ellipse of the elliptical range theorem as its field of values. The left regular matrix is $L_{\tilde Q}=S\bigl(I_2\otimes\mathsf{M}_2(\tilde Q)\bigr)S^{-1}$, and $W(I_2\otimes M)=W(M)$ for every $M$: a unit vector of the tensor product expands as $x=\sum_j e_j\otimes y_j$ with $\sum_j\|y_j\|^{2}=1$, so $x^*(I_2\otimes M)x=\sum_j y_j^*My_j$ is a convex combination of values of $M$. So the field of values of the left regular matrix is the field of values of the $2\times2$ matrix. The Hermitian elements of $\mathbb{M}_+$ have real intervals, and the elements of $\mathbb{M}_-$ have intervals on the imaginary axis. For the two-sided operator $T_{a,b}$ the field of values is that of a different matrix, and it is not determined by the two factors separately.

**The convexity.** The Toeplitz–Hausdorff theorem is the reason the field of values is a convex body; in the finite-dimensional case its only non-trivial input is the ellipse of the two-dimensional compression. In dimension four the body is the envelope of the ellipses of the compressions to the two-dimensional subspaces, and for the nilpotent chain the envelope is a disk.

## Summary

The field of values $W(A)=\{x^*Ax:\|x\|=1\}$ of a matrix of $M_4(\mathbb{C})$ is compact, connected and contains the spectrum; it is convex by the Toeplitz–Hausdorff theorem, which the general theory supplies. Its support function is $\lambda_{\max}(\operatorname{Re}(e^{-i\alpha}A))$, and its boundary is the envelope of the corresponding supporting lines. For a $2\times2$ matrix it is the ellipse with foci the eigenvalues and semi-minor axis $\tfrac12\sqrt{\operatorname{tr}(T^*T)-|\lambda_1|^{2}-|\lambda_2|^{2}}$, and this ellipse classifies the unitary orbit. The nilpotent Jordan block $J_4$ has the disk of radius $\cos(\pi/5)=(1+\sqrt5)/4$ as its field of values, while its spectrum is $\{0\}$ and its operator norm is $1$; the general block $J_n$ gives the radius $\cos(\pi/(n+1))$. A rank-one matrix $uv^*$ has an ellipse with foci $0$ and $v^*u$, and a block-diagonal matrix has the convex hull of the two fields of values. The field of values is complete for the unitary orbit in dimension two and incomplete in dimension four.

| Quantity | Value for $M_4(\mathbb{C})$ |
|---|---|
| $W(A)$ | compact, connected, convex, contains $\operatorname{spec}A$ |
| support function | $\lambda_{\max}(\operatorname{Re}(e^{-i\alpha}A))$ |
| Hermitian $H$ | $W(H)=[\lambda_{\min},\lambda_{\max}]$ |
| normal $A$ | $W(A)=\operatorname{conv}(\operatorname{spec}A)$ |
| $2\times2$ ellipse | foci $\lambda_1,\lambda_2$, semi-minor $\tfrac12\sqrt{\operatorname{tr}(T^*T)-|\lambda_1|^{2}-|\lambda_2|^{2}}$ |
| $W(J_4)$ | disk of radius $\cos(\pi/5)=(1+\sqrt5)/4$ |
| $w(J_4)$ | $\cos(\pi/5)\approx0.809$ |
| $\|J_4\|$ | $1$ |
| $\rho(J_4)$ | $0$ |
| $W(J_n)$ | disk of radius $\cos(\pi/(n+1))$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $W(A)$ | the field of values, or numerical range, of $A$ |
| $w(A)$ | the numerical radius $\max_{z\in W(A)}|z|$ |
| $h_K(\alpha)$ | the support function $\max_{z\in K}\operatorname{Re}(e^{-i\alpha}z)$ |
| $\operatorname{Re}M$ | the Hermitian part $\tfrac12(M+M^*)$ |
| $\operatorname{conv}$ | the convex hull |
| $J_n$ | the nilpotent Jordan block $\sum_{k=1}^{n-1}E_{k,k+1}$ |
| $\rho(A)$ | the spectral radius |
| $A_V$ | the compression $P_VA|_{V}$ |

## Further Reading

- [Hermitian Operators and the Numerical Range](hermitian-operators-and-the-numerical-range.html), for the general theory: the Toeplitz–Hausdorff theorem, the radius bounds and the Hermitian and normal characterisations.
- [The Numerical Range of the Two-Sided Operators of $M_4(\mathbb{C})$](the-numerical-range-of-the-two-sided-operators-of-m4c.html), for the field of values of the sandwich $T_{a,b}(X)=aXb$, the product bound and its failure.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the Hermitian part and the unitary group.
- [The Polar Decomposition of $M_4(\mathbb{C})$](the-polar-decomposition-of-m4c.html), for the singular values and the operator norm.
- [The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m4c.html), for the Frobenius, operator and nuclear norms.
- [Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m4c.html), for the spectrum and the resolvent.
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the matrix representation of the biquaternion algebra.
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Spin, Qubits and the Bloch Vector](m4c-representation-spin-qubits-and-the-bloch-vector.html), for the two-dimensional case and the Bloch picture.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c.html), for the tensor product and the identity $W(I\otimes M)=W(M)$.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the field of values and the elliptical range theorem.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the numerical radius and its inequalities.
- Karl E. Gustafson and Duggirala K. M. Rao, *Numerical Range: The Field of Values of Linear Operators and Matrices* (Springer, 1997), for the general theory.
