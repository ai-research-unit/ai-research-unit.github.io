# __The Exceptional Point of a Boosted State__

## Introduction

A state is an element of the informational slice, and a boost acts on it by congruence. The action is not an isometry, and what it does is exact: it rescales the state by a factor that depends on the projection of the Bloch vector on the boost axis, turns the transverse part into a longitudinal one, and drives the state towards the boundary as the rapidity grows.

The article asks where that action degenerates, and the answer has two parts.

1. **The centre of the ball is the exceptional point of the state.** It is the one state whose two eigenvalues coincide, the one state with no preferred axis, the one state that every channel fixes, and the one state of maximal entropy. The degeneracy is real, it is present in every frame, and it is the point from which every thermal path starts.
2. **Every state is driven to the boundary, the centre included.** For a fixed Bloch radius below one the renormalised radius tends to one as the rapidity tends to infinity, and no finite boost reaches the boundary or the trace-zero plane. The limit is the exceptional point of the *flow*, not of the state.

There the exceptional point is a defective element — a double eigenvalue with a Jordan block — and it is reached only by complexifying the momentum. Here the degenerate element is a real state, it is semi-simple, and it is the point every observer agrees on. One sector's exceptional point is unreachable and defective; the other's is unavoidable and harmless. That difference is a fact about the two slices, not a convention.

The article uses [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) for the state and the pairing, [The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics](the-lorentz-group-on-the-bloch-ball.html) for the action and the metrics, and [The Rest Frame and the Exceptional Point](the-rest-frame-and-the-exceptional-point.html) for the material exceptional point that is compared at the end.

## The State and Its Two Eigenvalues

The state and its spectrum. A state of the informational sector is

$$
\tilde{Ϛ}_\Psi=\tfrac12\left(e_t+i\vec s_\Psi\right),\qquad \vec s_\Psi\in\mathbb{R}^{3},\qquad \lvert\vec s_\Psi\rvert<1,
$$

and its $2\times2$ image is $\tfrac12\left(I+\mathsf M_2(i\vec s_\Psi)\right)$, Hermitian of trace one. Choosing the axis of $\vec s_\Psi$ as the third direction diagonalises it, and

$$
\lambda_\pm=\tfrac12\left(1\pm r\right),\qquad r=\lvert\vec s_\Psi\rvert,
$$

so the two eigenvalues are positive, sum to one, and are separated by the radius. The characteristic polynomial is $\lambda^{2}-\lambda+\tfrac14(1-r^{2})$, whose discriminant is $r^{2}/4$: the spectrum is degenerate exactly at $r=0$.

The radius is the only spectral datum. Every state of radius $r$ has the same spectrum, and the axis is carried by the eigenvectors and not by the eigenvalues. This is the same division the material sector makes between the two eigenvalues of a rotor and the two eigenprojectors, and it is the reason the corpus writes the state in the polar form $\tfrac12(1+i\vec s)$ rather than as a matrix: the spectrum is one number, the axis is two, and the three together are the state.

The purity is a function of the radius alone. $\operatorname{tr}\tilde{Ϛ}_\Psi^{2}=\tfrac12(1+r^{2})$, so the state is pure at $r=1$ and mixed at every $r<1$. The quantity the corpus uses as the information is $\tfrac14(1-r^{2})$, the determinant, and it vanishes exactly on the boundary.

## The Centre Is the Exceptional Point of the State

The centre is the maximally mixed state, and it is degenerate in the strong sense. At $r=0$ the state is $\tilde{Ϛ}_\Psi=\tfrac12 e_t$: a scalar. Its two eigenvalues are equal to $\tfrac12$, its eigenspace is the whole of $\mathbb{C}^{2}$, and no axis is selected because no axis can be. Every other state has a unique axis and a unique orthogonal complement; the centre has neither.

It is the unique state that every channel fixes, and every boost moves it. For a rotor of unit norm $\tilde U$ the congruence of the centre is

$$
\tilde U\left(\tfrac12 e_t\right)\tilde U^{*}=\tfrac12\,\tilde U\tilde U^{*},
$$

and the factor decides the whole question. When $\tilde U$ is $*$-unitary, $\tilde U\tilde U^{*}=e_t$ and the centre is fixed exactly; that is the class of channels, and the centre is the only state fixed by all of them. When $\tilde U$ is a boost it is Hermitian and $\tilde U^{2}=\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\,\vec n$, so the image is

$$
\mathrm{Cg}_{\tilde U_{\mathrm b}}\left(\tfrac12 e_t\right)=\tfrac12\left(\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\,\vec n\right),
$$

which renormalises to the state of radius $\tanh\theta_{\mathrm{rpd}}$ along the boost axis. **So a boost does not fix the centre: it carries it to the axial state of its own rapidity**, which is the Gibbs state of the Hamiltonian whose axis is $\vec n$ and whose gap satisfies $\beta\omega=\theta_{\mathrm{rpd}}$. The centre is the fixed point of the compact and channel part of the group and the starting point of every thermal path, and the two properties are one statement: it is the state with no axis, so a channel has nothing to move and a boost has everything to give it.

The word names the place where a family of operators stops being diagonalisable in a stable way. At the centre the spectrum is degenerate, and the degeneracy is stable: it is not the coincidence of two eigenvalues that a perturbation splits, it is the vanishing of the only spectral datum there is. The element is semi-simple — its minimal polynomial is linear — so it is not a Jordan defect. It is the other kind of exceptional point: the one where the eigenvalue map itself has a critical point, and here the critical point is a minimum of the spread and a maximum of the entropy.

The entropy is extremal there and nowhere else. With $S=-\operatorname{tr}\tilde{Ϛ}_\Psi\ln\tilde{Ϛ}_\Psi$,

$$
S(r)=-\tfrac{1+r}{2}\ln\tfrac{1+r}{2}-\tfrac{1-r}{2}\ln\tfrac{1-r}{2},
$$

which is $\ln 2$ at $r=0$ and $0$ at $r=1$. The exceptional point is the maximum, the boundary is the minimum, and both are fixed points of the family of frame changes: the first exactly, the second as a set.

## What a Boost Does to a State

The exact action. A boost is a Hermitian rotor, $\tilde U_{\mathrm b}=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}+i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\,\vec n$, of unit quaternionic norm and not $*$-unitary. Write $\vec s_\Psi=s_\parallel\vec n+\vec s_\perp$. Then

$$
2\,\mathrm{Sc}\left(\mathrm{Cg}_{\tilde U_{\mathrm b}}\tilde{Ϛ}_\Psi\right)=\cosh\theta_{\mathrm{rpd}}+s_\parallel\sinh\theta_{\mathrm{rpd}},
$$

and the image, before normalisation, is

$$
\mathrm{Cg}_{\tilde U_{\mathrm b}}\tilde{Ϛ}_\Psi
=\tfrac12\left(\cosh\theta_{\mathrm{rpd}}+s_\parallel\sinh\theta_{\mathrm{rpd}}\right)e_t
+\tfrac12 i\left(\vec s_\perp+\left(s_\parallel\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\right)\vec n\right).
$$

The transverse part is untouched and a longitudinal part appears. The component of $\vec s_\Psi$ perpendicular to the boost axis is carried unchanged, while the axial component is replaced by $s_\parallel\cosh\theta+\sinh\theta$. At $\theta=0.8$ and $s_\parallel=0.6$ the doubled scalar part is $1.870299$, the axial coefficient becomes $0.845283$, and the renormalised radius is $0.903996$; the same boost applied to $s_\perp=0.6$ leaves the transverse coefficient at $0.300000$, creates an axial coefficient $0.444041$, and gives the renormalised radius $0.801374$. All four numbers are the two formulas above evaluated at those arguments.

The renormalised radius is a function of the pair $(r,\theta)$ and the angle to the axis. Dividing the vector part by the doubled scalar part,

$$
r'=\frac{\sqrt{s_\perp^{2}+\left(s_\parallel\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\right)^{2}}}{\cosh\theta_{\mathrm{rpd}}+s_\parallel\sinh\theta_{\mathrm{rpd}}},
$$

and the denominator is positive for every state and every finite rapidity, because $\cosh\theta>\lvert\sinh\theta\rvert$ and $\lvert s_\parallel\rvert<1$. So **no finite boost sends a state to the trace-zero plane**, and every image is a state after normalisation.

The flow drives the ball to its boundary. For fixed $r<1$ the numerator grows like $\tfrac12(1+s_\parallel)e^{\theta}$ and the denominator like $\tfrac12(1+s_\parallel)e^{\theta}$ when $s_\parallel>-1$, so the two leading terms cancel and $r'\to1$; the approach is from below and it is monotone in $\theta$. The boundary is therefore the limit set of every orbit, and no orbit is a point inside: the two ends of the axis, $\vec s_\Psi=\pm\vec n$, are the only fixed points of the boost, and they sit on the boundary from the beginning. A pure state on the axis is fixed up to normalisation — it is the eigenstate of the boost — and a state off the axis runs out to the boundary along a curve of constant perpendicular component, which is a hypercycle of the Klein ball and not a chord.

## The Two Exceptional Points, Compared

The material one requires a complex momentum; this one requires nothing. The material exceptional point is the Jordan part of the spectrum, reached when $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}=0$ with $\vec Q\neq0$. On the real slice $B^{2}$ is a sum of three real squares, so it vanishes only at $\vec Q=0$; a real four-momentum is therefore on the open stratum or on the rest line and never on the Jordan part. The informational exceptional point is $\tilde{Ϛ}_\Psi=\tfrac12 e_t$, a real element of a real three-dimensional ball, and every observer can name it.

The material one is a defect; this one is not. There the two eigenvalues coalesce *and* the eigenbasis disappears: the minimal polynomial is quadratic, the centraliser is a dual-number ring, the inverse has a double pole, and the flow is polynomial. Here the two eigenvalues coalesce and the eigenbasis becomes everything: the element is a scalar, its minimal polynomial is linear, its inverse is a multiple of itself, and its flow is the identity. The two are the two ways a spectrum can degenerate, and the sectors supply one each.

The material sector is non-compact and its degenerate locus is complexified: the interesting degeneration is off the real slice, and reaching it is a calculation. The informational sector is compact — the ball is bounded, the group acting on it is $U(2)$ — and its degenerate locus is a point of the real interior: the interesting degeneration is the one point every frame agrees on, and reaching it requires no continuation at all. A reader who wants a single notion of exceptional point for both sectors will not find one, and the reason is the sign of the norm.

| | material | informational |
| --- | --- | --- |
| the degenerate element | the Jordan part, $B^{2}=0$, $\vec Q\neq0$ | $\tilde{Ϛ}_\Psi=\tfrac12 e_t$ |
| what degenerates | the eigenvalues and the eigenbasis | the eigenvalues only |
| the minimal polynomial | quadratic | linear |
| reached by | a complex isotropic momentum | nothing; it is the centre |
| the flow there | polynomial in the parameter | the identity |
| the physical name | an exceptional point of a generator | the maximally mixed state |

## Summary

The state's spectrum is $\tfrac12(1\pm r)$ and it degenerates only at the centre, $\tilde{Ϛ}_\Psi=\tfrac12 e_t$. The centre is the unique state fixed by every channel, it is carried by every boost to the axial state of its own rapidity, it has no axis, and it maximises the entropy; it is the exceptional point of the state, and it is semi-simple. The only fixed points of the boost flow are the two axial pure states on the boundary. A boost rescales the state by $\cosh\theta+s_\parallel\sinh\theta$, leaves the transverse Bloch vector unchanged, adds the axial component $s_\parallel\cosh\theta+\sinh\theta$, and drives the renormalised radius to one as the rapidity grows. No finite boost reaches the trace-zero plane. The material exceptional point is a Jordan defect off the real slice; the informational one is a real, semi-simple, unavoidable point. The two are the two ways a spectrum degenerates, and the sectors supply one each.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ | the state, of trace one |
| $r=\lvert\vec s_\Psi\rvert$ | the Bloch radius, the only spectral datum |
| $\lambda_\pm=\tfrac12(1\pm r)$ | the two eigenvalues of the state |
| $s_\parallel$, $\vec s_\perp$ | the projections of the Bloch vector on and off the boost axis |
| $\theta_{\mathrm{rpd}}$ | the rapidity of the boost |
| $2\,\mathrm{Sc}$ | the doubled scalar part, the trace of the $2\times2$ image |
| $r'$ | the renormalised radius of the image |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the vector square whose vanishing is the material degeneration |

## Further Reading

In this category. [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) fixes the state and the pairing. [The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics](the-lorentz-group-on-the-bloch-ball.html) gives the congruence, the projective action and the two metrics. [The Thermal Circle: Inverse Temperature Is an Inverse Time](the-thermal-circle-inverse-temperature-is-an-inverse-time.html) reads the same centre as the infinite-temperature state and the same boundary as the zero-temperature one. [The Fubini–Study Geometry and the Biquaternion Norm](the-fubini-study-geometry-and-the-biquaternion-norm.html) supplies the distance whose geodesics leave the centre in every direction. [The Rest Frame and the Exceptional Point](the-rest-frame-and-the-exceptional-point.html) is the material article compared above.

In the mathematics corpus. [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) owns the material degeneration — the Jordan part, the dual-number centraliser and the polynomial flow — that the comparison uses.
