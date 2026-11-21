# __The Informational Reading of the Wigner Angle__

## Introduction

A frame change is not an operation on a state. It moves the observer, and the state is what it is; what the observer registers changes because the observables have been carried, not because the state has been transformed. The informational sector says something sharper than that, and it says it about the *product* of two frame changes rather than about one.

The claim. The product of two boosts is a boost times a rotation. The boost part is not a channel: it takes a state off the normalised slice. The rotation part is a channel: it is affine, trace-preserving and isometric for the Bures distance. So a composition of two frame changes contains exactly one piece that a measurement can see as a reversible operation, and that piece is the Wigner gyration.

A boost is a congruence $\mathrm{Cg}_{\tilde U}:\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ with $\tilde U$ Hermitian, and a Hermitian unit element satisfies $\tilde U^{*}=\tilde U$, not $\tilde U^{*}=\tilde U^{-1}$. The gyration rotor is real, so for it the two coincide and the congruence is also the adjoint. That single coincidence is the whole difference, and this article is its consequence.

The article uses the group theory of *The Wigner Angle of Two Boosts: Closed Form, Axis and Composition* for the angle and the axis, *The Two Actions of One Group: Adjoint and Congruence* for the coincidence theorem, and *The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics* for the ball, the slice and the two metrics. What it adds is the reading: which part of a frame change is an operation, and what that operation does to a state.

## A Boost Is Not a Channel

**The doubled scalar part is the test.** A state of the informational sector is $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ with $\vec s_\Psi$ real and $\lvert\vec s_\Psi\rvert<1$, and its doubled scalar part is one. Under a congruence by a boost of rapidity $\theta_{\mathrm{rpd}}$ whose axis makes the projection $s_\parallel$ with $\vec s_\Psi$,

$$
2\,\mathrm{Sc}\left(\mathrm{Cg}_{\tilde U_{\mathrm b}}\tilde{Ϛ}_\Psi\right)
=\cosh\theta_{\mathrm{rpd}}+s_\parallel\sinh\theta_{\mathrm{rpd}} .
$$

This is one only at $\theta_{\mathrm{rpd}}=0$. Every other boost moves the state off the slice, and a map that does not preserve the slice is not a map of the state space at all: its linear form is not trace-preserving, and the image is not a state.

The reading of that failure is not that boosts are unphysical. A boost is a change of frame, and a change of frame is not something an experimenter does to a system. The failure says exactly that: the group of frame changes contains elements that are not operations, and a boost is one of them. The informational sector is what tells the two apart.

The projective repair is available and it is not a channel. One may act on the ball by the induced map and renormalise. The renormalised map is a Möbius flow, it is not affine, and it does not preserve the Bures distance; it is the correct description of what an observer in another frame assigns, and it is not an operation any laboratory performs. The distinction between *what another frame assigns* and *what an operation does* is the distinction this article keeps.

## The Gyration Is a Channel

**The gyration rotor is real, so the congruence by it is its adjoint.** For $\tilde U_{\mathrm{gyr}}$ a real unit quaternion, $\tilde U_{\mathrm{gyr}}^{*}=\tilde U_{\mathrm{gyr}}^{\natural}=\tilde U_{\mathrm{gyr}}^{-1}$. The congruence and the adjoint therefore coincide on it, and the doubled scalar part is preserved identically:

$$
2\,\mathrm{Sc}\left(\mathrm{Cg}_{\tilde U_{\mathrm{gyr}}}\tilde{Ϛ}_\Psi\right)=2\,\mathrm{Sc}\,\tilde{Ϛ}_\Psi=1 .
$$

Verified on fifty random states to $8.9\times10^{-16}$; on the same sample the map induced on the ball equals the matrix $\operatorname{gyr}[\vec u,\vec v]$ to $3.3\times10^{-16}$, and the Bures distance of every pair is preserved to $5.8\times10^{-16}$.

So the gyration is a unitary channel. It is affine on the ball, it preserves the slice, it is invertible with an inverse of the same kind, and it is isometric for the only metric on the ball that the congruence supplies. It is, in the language of the quantum categories, a rotation of the Bloch ball realised by a unitary of the algebra, with no environment and no entropy production.

The two metrics are both preserved, and that is the coincidence again. The gyration preserves the Cayley–Klein distance because it is an element of the group, and it preserves the Euclidean radius because it is orthogonal. No boost has both properties, and the double preservation is the signature of the compact part of the group acting on the state space.

## The Same Matrix on the Bloch Ball

**The matrix that rotates the velocity ball rotates the Bloch ball.** For the pair $\vec u=0.6\vec e_x$, $\vec v=0.6\vec e_y$ the congruence by $\tilde U_{\mathrm{gyr}}$ sends a state of vector $\vec s_\Psi$ to the state of vector $\operatorname{gyr}[\vec u,\vec v]\vec s_\Psi$, verified to $3.3\times10^{-16}$. The two sectors share the matrix, not merely the angle.

Why they can share it is the coincidence theorem. The adjoint and the congruence differ by the inverse, and for a real unit quaternion the inverse is the star. On the compact part of the group the two actions are therefore one action, and an element that acts on velocities by a rotation acts on states by the same rotation. This is the only place in the group where that happens, and the gyration is the only element of a frame change that sits there.

| | the material reading | the informational reading |
| --- | --- | --- |
| the object | a rotation of the velocity ball | a rotation of the Bloch ball |
| the matrix | $\operatorname{gyr}[\vec u,\vec v]$ | $\operatorname{gyr}[\vec u,\vec v]$ |
| the metric preserved | Klein and Euclidean | Klein and Bures |
| $2\,\mathrm{Sc}$ | not applicable | preserved |
| the category | a motion of the ball | a unitary channel |
| what registers it | a closed path of boosts | a comparison of two states |

What each sector can measure differs, and the angle does not. The material sector measures the angle by watching a velocity return rotated after a closed path; the informational sector measures it by watching a state rotate, which needs two states or one state before and after. That is a difference of observables, not of the angle.

## What a Measurement Can See of a Frame Change

**The answer is: the gyration, and only the gyration.** A single boost is invisible to every metric of the state space, because it is not in the category those metrics measure. A pair of boosts is not invisible: it imprints a rotation, and a rotation is a measurement-visible reversible operation. So the observational content of a frame change is positive and narrow.

The relational character follows. No single state registers the gyration, because a rotation about a line fixes the line and the centre; what registers it is a comparison of two states. No single velocity registers it either, because a gyration is a function of a pair. The angle is a property of a relation between two frames, and both sectors say so.

What the reading does not give. It gives no dynamics: the gyration is kinematic, and Thomas precession needs an orbit and an acceleration, supplied by *Exercise: The Thomas Precession*. It gives no second physical effect: the two readings are one matrix read through two families of observables, and a reader who counts them as two results has double-counted. And it does not make a frame change into a channel: the product of a non-channel and a channel is not a channel, and the split into factors is the Cartan split, not a decomposition into operations performed one after the other.

## Summary

The product of two boosts is a boost times a gyration. The boost is a congruence by a Hermitian element and takes a state off the normalised slice; the gyration is a congruence by a real element, so it is simultaneously the adjoint, and it preserves the slice, the ball, both metrics and the Bures distance. It is therefore the one piece of a frame change that is a unitary channel, and the only piece a measurement can see as a reversible operation. The same matrix acts on the velocity ball and on the Bloch ball, and it does so because on the compact part of the group the two actions of the group coincide.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde U_{\mathrm b}$, $\tilde U_{\mathrm{gyr}}$ | the boost rotor, Hermitian of unit norm, and the gyration rotor, real of unit norm |
| $\mathrm{Cg}_{\tilde U}(\tilde Q)=\tilde U\tilde Q\tilde U^{*}$ | the congruence |
| $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ | the state, of doubled scalar part one |
| $\vec s_\Psi$, $\lvert\vec s_\Psi\rvert<1$ | the Bloch vector and the radius |
| $\operatorname{gyr}[\vec u,\vec v]$ | the gyration matrix of the pair of velocities |
| $2\,\mathrm{Sc}$ | the doubled scalar part, the test of the slice |
| $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{wgn}}$ | the rapidity of a boost and the angle of a gyration |

## Further Reading

In this category. [The Wigner Angle of Two Boosts: Closed Form, Axis and Composition](the-wigner-angle-of-two-boosts.html) fixes the angle, the axis and the composition law; its two readings are this article and a section of [Velocity Space as Hyperbolic Geometry in Biquaternionic Form](velocity-space-as-hyperbolic-geometry-in-biquaternionic-form.html). [The Two Actions of One Group: Adjoint and Congruence](the-two-actions-of-one-group-adjoint-and-congruence.html) proves the coincidence that makes the gyration a channel. [The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics](the-lorentz-group-on-the-bloch-ball.html) supplies the ball, the slice, the two metrics and the projective action. [The Fubini–Study Geometry and the Biquaternion Norm](the-fubini-study-geometry-and-the-biquaternion-norm.html) supplies the distance that the channel preserves, and [Bures Isometries of the Bloch Ball: Rotations, the Slice and the Conformal Boundary](bures-isometries-of-the-bloch-ball.html) states which isometries the congruence supplies.

The companions outside the category. [The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form](the-wigner-rotation-and-the-information-content-of-a-boost-in-biquaternionic-form.html) computes the compact factor, its cocycle, its holonomy and its path integral, which this article reads as a channel.
