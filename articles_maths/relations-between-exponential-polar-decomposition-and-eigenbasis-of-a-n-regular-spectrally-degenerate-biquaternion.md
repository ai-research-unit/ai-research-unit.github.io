# __Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

On the N-regular, spectrally degenerate sector $\Sigma_{10}$ an element has one eigenvalue, not two. It therefore has no eigenbasis. The spectral reading does not vanish; it collapses to a Jordan reading. This article compares the exponential polar word with that Jordan reading and states exactly what the collapse preserves and what it destroys.

The element is written in the normal form of *The N-Regular, Spectrally Degenerate Sector*,

$$
\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\vec\Upsilon^2=0,
\qquad
Q_t\neq0,
$$

with $\vec\Upsilon$ a complex null vector. The reduced product is $N=Q_t^2$, the modulus is $\Rho$ with $\Rho^2=N$, and the unit factor is

$$
\tilde U=\frac{\tilde Q}{\Rho}=\varepsilon\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1.
$$

The polar word of *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion* is

$$
\tilde Q=r e^{i\alpha}\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\varepsilon$ and $\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$. The two decompositions are compared below.

## The Spectral Problem

**Proposition (one eigenvalue, no eigenbasis).** Let $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$ and $\vec\Upsilon\neq0$. Then $\tilde Q$ has the single eigenvalue $Q_t$, and it has no eigenbasis.

*Proof.* The characteristic polynomial of $\tilde Q$ is $(X-Q_t)^2$, because $\vec\Upsilon$ is nilpotent. If a basis of eigenvectors existed, the matrix of $\tilde Q$ in that basis would be the scalar matrix $Q_tI$, so $\tilde Q=Q_te_t$ and $\vec\Upsilon=0$. $\square$

The eigenvalue is $Q_t$, of algebraic multiplicity two and geometric multiplicity one. In the matrix model

$$
\mathsf M(\tilde Q)=Q_t\bigl(I+N\bigr),
\qquad
N=\mathsf M(\vec\Upsilon),
\qquad
N^2=0,
\qquad
N\neq0,
$$

the matrix is $Q_t$ times a single unipotent Jordan block. The eigenline is $\ker N$; it is one complex line, not a basis.

The scalar line $\vec\Upsilon=0$ is the exception. There $\tilde Q=Q_te_t$ is central, every basis is an eigenbasis, and the polar word is central. The rest of the article concerns the Jordan part $\vec\Upsilon\neq0$.

## The Jordan Basis

**Proposition (the Jordan chain).** Let $\vec\Upsilon\neq0$ with $\vec\Upsilon^2=0$. There are elements $\xi,\eta$ with

$$
\vec\Upsilon\xi=0,
\qquad
\vec\Upsilon\eta=\xi,
$$

and $(\xi,\eta)$ is a basis. In that basis the matrix of $\tilde Q$ is

$$
\mathsf M_{(\xi,\eta)}(\tilde Q)
=
Q_t
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$

*Proof.* In the matrix model choose $v\in\operatorname{im}N$ with $v\neq0$. Since $N^2=0$, $v\in\ker N$. Choose $w$ with $Nw=v$. Then $v\neq0$ and $w\notin\ker N$, so $(v,w)$ is a basis. The matrix of $N$ in that basis has first column $0$ and second column $v$, which is the nilpotent Jordan block. $\square$

The chain is not unique for the product alone. The vector $\xi$ is determined up to a nonzero scalar, and $\eta$ is determined up to $\eta\mapsto\eta+c\xi$. The Jordan basis is therefore a spectral object of the element, but not a canonical one from the product alone; the definite Hermitian form selects one chain, with $\xi=\vec Q$ and $\eta=\tilde\Pi_-=\vec Q^*\vec Q/(2\langle\vec Q\rangle_*)$, in *The Jordan Basis of a Spectrally Degenerate Biquaternion*. It is a basis of the generalized eigenspace, not a polar frame.

## The Polar Word and the Jordan Flag

The unit factor is a polynomial in $\tilde Q$,

$$
\tilde U=\varepsilon\bigl(e_t+\vec\Upsilon\bigr)=\frac{\tilde Q}{Q_t},
$$

so it preserves the Jordan flag $\mathbb{C}\xi\subset\mathbb{C}^2$. In the Jordan basis its matrix is the unipotent block

$$
\mathsf M_{(\xi,\eta)}(\tilde U)
=
\varepsilon
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$

The polar factors do not preserve the flag in general.

**Proposition (the factors leave the flag).** On the Jordan part, the positive factor $\tilde U_{\mathrm b}$ and the rotor $\tilde u_{\mathrm r}$ do not preserve the eigenline $\mathbb{C}\xi$ unless the element lies on the scalar line. Their product $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ does preserve it.

*Proof.* The product is $\tilde U$, which is upper triangular in the Jordan basis. If both factors preserved the flag, both would be upper triangular in that basis. The worked example below shows that they are not; the general statement follows because the polar factors are functions of $\tilde U$ and $\tilde U^{*}$, and $\tilde U^{*}$ does not preserve the flag of $\tilde U$ on the Jordan part. $\square$

The eigenvalues of the factors are not degenerate. The positive factor has eigenvalues $e^{\psi/2}$ and $e^{-\psi/2}$, and the rotor has eigenvalues $e^{i\theta/2}$ and $e^{-i\theta/2}$. Their product has the double eigenvalue $\varepsilon$. The polar decomposition therefore splits a defective element into two diagonalizable factors whose product is defective. The defect is carried by the off-diagonal entries, not by the spectrum.

This is the precise sense in which the Jordan reading and the polar reading are transverse. The Jordan basis triangularizes the element and the unit factor. The polar word diagonalizes neither the element nor the unit factor; it separates the element into a positive and a $*$-unitary factor, and only their product is unipotent.

## The Dictionary

The spectral data and the polar data carry different real information.

| Object | Spectral / Jordan reading | Polar reading |
|---|---|---|
| domain | $N\neq0$, $B^2=0$ | the same |
| decomposition of | the element $\tilde Q$ | the unit factor $\tilde U$ |
| factors | $Q_te_t+\vec\Upsilon$, a scalar and a nilpotent | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, positive times $*$-unitary |
| eigenvalues | $Q_t$, double | $\varepsilon$, double for $\tilde U$; $e^{\pm\psi/2}$ and $e^{\pm i\theta/2}$ for the factors |
| basis | a Jordan chain, not unique | an orthogonal frame $\vec u_{\mathrm b}\perp\vec u_{\mathrm r}$, up to degeneracies |
| real data | $Q_t$ (2) and $\vec\Upsilon$ (4) | $r,\alpha$ (2), $\psi,\theta$ (2), frame (2), relation (1) |
| what the spectrum fixes | $Q_t$ and $\varepsilon$ | $r,\alpha,\varepsilon$ |
| survives $B^2\to0$ | the Jordan chain does | the word does |

The spectrum fixes only the scalar $Q_t$ and the sign $\varepsilon$. It does not fix the rapidity, the rotor angle or the two axes. The nilpotent $\vec\Upsilon$ fixes the word, because the element is fixed and the word is unique up to the axis degeneracies; but the passage from $\vec\Upsilon$ to $(\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r})$ is nonlinear. The Jordan chain and the polar frame are two different bases of the same two-dimensional complex space, and neither is determined by the other without extra choices.

## The Boundary

Seen from the regular sector $\Sigma_{11}$, the locus $B^2=0$ is the wall at which the two eigenvalues $\lambda_\pm=Q_t\pm iB$ coalesce. The eigenprojectors

$$
\tilde\Pi_\pm=\frac12\bigl(e_t\mp i\vec Q/B\bigr)
$$

diverge as $B\to0$, because $\vec Q/B$ diverges. Their sum is $e_t$, which remains finite. The eigenbasis has no limit. The polar word has a limit, and the limit is the word of this article; this is proved in *Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*, §*The Boundary*.

The Jordan chain is the limit of a rescaled eigenbasis. If $\xi_\pm$ are normalized eigenvectors of $\tilde Q$ with eigenvalues $\lambda_\pm$, then $\xi_+\to\xi$ and $(\xi_+-\xi_-)/(\lambda_+-\lambda_-)\to\eta$ after a choice of normalization. The chain records the rate at which the two eigenlines merge. It is a spectral remnant of the regular basis, not a polar object.

## Worked Example

Take

$$
\tilde Q=e_t+\vec e_x+i\vec e_y.
$$

Then $Q_t=1$, $\vec\Upsilon=\vec e_x+i\vec e_y$, $\vec\Upsilon^2=0$, $N=1$, $\Rho=1$, $r=1$, $\alpha=0$ and $\varepsilon=1$. The word is

$$
\psi=2\operatorname{arcosh}\sqrt2,
\qquad
\theta=\frac{\pi}{2},
\qquad
\vec u_{\mathrm b}=\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\vec u_{\mathrm r}=\frac{\vec e_t+\vec e_x}{\sqrt2},
$$

and the polar factors are

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

In the matrix model,

$$
N=\mathsf M(\vec\Upsilon)=
\begin{pmatrix}
0 & -2i\\
0 & 0
\end{pmatrix}.
$$

A Jordan chain is $\xi=(2i,0)$ and $\eta=(0,-1)$; then $\xi=(2i,0)$ is the eigenvector and $N\eta=\xi$. In the basis $(\xi,\eta)$,

$$
\mathsf M_{(\xi,\eta)}(\tilde Q)
=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix},
\qquad
\mathsf M_{(\xi,\eta)}(\tilde U_{\mathrm b})
=
\frac{1}{\sqrt2}
\begin{pmatrix}
3 & \tfrac12\\
2 & 1
\end{pmatrix},
\qquad
\mathsf M_{(\xi,\eta)}(\tilde u_{\mathrm r})
=
\frac{1}{\sqrt2}
\begin{pmatrix}
1 & \tfrac12\\
-2 & 1
\end{pmatrix}.
$$

The two factor matrices are not triangular, and neither preserves the eigenline $\mathbb{C}(1,0)$. Their product is

$$
\frac12
\begin{pmatrix}
3 & \tfrac12\\
2 & 1
\end{pmatrix}
\begin{pmatrix}
1 & \tfrac12\\
-2 & 1
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix},
$$

which is the unipotent block. The example shows the two readings side by side: the Jordan basis gives the element a triangular form, and the polar word gives it a positive and a $*$-unitary factor, neither of which is triangular in that basis.

## Summary

### Main Results

| Result | Statement |
|---|---|
| spectrum | one eigenvalue $Q_t$, algebraic multiplicity two, geometric multiplicity one |
| eigenbasis | none on the Jordan part; every basis on the scalar line |
| replacement | a Jordan chain $\xi,\eta$ with $\vec\Upsilon\xi=0$ and $\vec\Upsilon\eta=\xi$ |
| matrix form | $Q_t\begin{pmatrix}1&1\\0&1\end{pmatrix}$ in the chain |
| polar factors | $\tilde U_{\mathrm b}$ and $\tilde u_{\mathrm r}$ do not preserve the chain in general |
| factor eigenvalues | $e^{\pm\psi/2}$ and $e^{\pm i\theta/2}$; the product has the double eigenvalue $\varepsilon$ |
| data carried by the spectrum | only $Q_t$ and $\varepsilon$ |
| data carried by the word | the two angles and the orthogonal frame, with the rigidity relation |

### What the Example Shows

- The Jordan chain exists and is explicit, but it is not unique.
- The polar factors are full matrices in the chain, not diagonal or triangular ones.
- The product of the two factor matrices is the unipotent block, so the defect of the element is invisible in the spectrum but visible in the off-diagonal entries of the factors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product |
| $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$ | the vector form |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\vec\Upsilon=\vec Q/Q_t$ | the null vector of the normal form |
| $\Rho$ | the modulus, principal square root of $N$ |
| $\tilde U=\tilde Q/\Rho=\varepsilon(e_t+\vec\Upsilon)$ | the unit factor |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the positive factor and the rotor |
| $\psi,\theta$ | the rapidity and the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the two axes, orthogonal on the Jordan part |
| $\varepsilon=\pm1$ | the sign of the scalar part of the unit factor |
| $\xi,\eta$ | a Jordan chain, $\vec\Upsilon\xi=0$, $\vec\Upsilon\eta=\xi$ |
| $\mathsf M(\tilde Q)$ | the matrix $Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z$ |

## Further Reading

- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the word, the existence theorem and the exact logarithm.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of a N-Regular, Spectrally Degenerate Biquaternion](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the Jordan chains of the eight cases.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Regular Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-n-regular-spectrally-regular-biquaternion.html), for the regular side of the wall.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the normal forms and the two strata.
