# __Aberration and the Sky: The Boost as a Möbius Flow__

## Introduction

The sky is the sphere of light directions. A boost does not deform it: it moves every direction by a Möbius map, and the map's fixed points are the two points on the boost axis. The angle between two stars is not preserved, but the *conformal* structure is: the boost rescales the round metric by a factor that depends on the direction, so shapes are distorted and angles between directions at the same point are preserved.

This article states the sky's geometry, derives the aberration formula from the block's congruence action, exhibits the boost as a one-parameter Möbius flow, computes the conformal factor, and takes the two limits.

The article assumes *The Null Cone: The Massless Boundary* for the sky, *The 2×2 Matrix Model: What It Computes and What It Cannot Show* for the spinor coordinates, *The Group of Unit-Norm Biquaternions* for the congruence action, and *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* for the related hyperbolic picture on the other side of the correspondence.

## The Sky

### The Sphere of Directions

A light direction is a future-pointing null vector up to positive scale. The set of them is the two-sphere:

$$
\text{sky}=\{[\tilde X]:N(\tilde X)=0,\ X_t>0\}\cong S^{2}.
$$

Every observer sees the sky in this way, and two observers' skies are related by the boost that separates them. Aberration is that relation.

### The Stereographic Coordinate

A point of the sky is a spinor up to phase, so a coordinate is a ratio of the spinor's two components:

$$
w=\frac{\xi_2}{\xi_1}\in\mathbb{CP}^{1},
\qquad
\lvert w\rvert=\cot\frac{\theta}{2},
$$

with $\theta$ the angle from the chosen axis and $\arg w$ the azimuth. The favourable coordinate for boosts along that axis is

$$
z=\cot\frac{\theta}{2}\,e^{i\theta_{\mathrm{azm}}},
$$

which sends the forward direction to infinity and the backward direction to zero.

### Why This Coordinate

The two poles of the coordinate are the two points of the axis, and they are exactly the fixed points of a boost along the axis. So the coordinate is adapted to the boost, and a boost acts on it by the simplest possible Möbius map. That is the computational reason: the geometry picks the coordinate, and the coordinate makes the flow trivial.

### The Möbius Group

The Lorentz group acts on the sky by

$$
z\longmapsto\frac{az+b}{cz+d},
\qquad
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb{C}),
$$

and this action is the projective version of the defining action on the spinor: the matrix multiplies $\binom{\xi_1}{\xi_2}$ and the ratio transforms by the fractional linear map.

So the sky's symmetry group is $PGL_2(\mathbb{C})\cong PSL_2(\mathbb{C})$, and the block's group covers it two-to-one.

## Aberration

### The Statement

Let an observer move with velocity $\beta c$ along the $z$ axis. A light ray that the rest observer sees at angle $\theta$ from the axis is seen by the moving observer at angle $\theta'$ with

$$
\cos\theta'=\frac{\cos\theta+\beta}{1+\beta\cos\theta}.
$$

The sign convention is that the moving observer sees the stars crowd toward the direction of motion. The inverse relation is the same formula with $\beta\to-\beta$.

### The Derivation From the Congruence

Take the null element

$$
\tilde X=\tfrac12\bigl(e_t+i\sin\theta\,\vec e_x+i\cos\theta\,\vec e_z\bigr)
$$

and apply the boost $\tilde B=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+\,i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec e_z$ by the congruence, with $\tanh\theta_{\mathrm{rpd}}=\beta$:

$$
\tilde X'=\mathrm{Cg}_{\tilde B}(\tilde X)=\tilde B\tilde X\tilde B^{*}.
$$

The transformed element is again null, and its time component is $\tfrac12(\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\cos\theta)$. Dividing the $z$ component by the time component gives

$$
\cos\theta'=\frac{\cos\theta+\beta}{1+\beta\cos\theta},
$$

which is the aberration formula. The computation is verified numerically in the block's model at three angles with $\beta=0.6$: $\theta=0.2$ gives $\theta'=0.100250626$, $\theta=1$ gives $\theta'=0.533293254$, $\theta=2.5$ gives $\theta'=1.968525471$, each matching the formula to nine digits.

### Why the Formula Is a Projective One

The right-hand side is the restriction to the diagonal of a Möbius transformation: it is the projection of the Möbius map $z\mapsto\digamma_{\mathrm{mlt}} z$ onto the axis of symmetry, with $\digamma_{\mathrm{mlt}}=\sqrt{(1+\beta)/(1-\beta)}$. So aberration is not special; it is one real slice of a fractional linear map.

## The Boost as a Möbius Flow

### The Map

In the coordinate $z=\cot(\theta/2)e^{i\theta_{\mathrm{azm}}}$ a boost along $z$ is

$$
z\longmapsto\digamma_{\mathrm{mlt}} z,
\qquad
\digamma_{\mathrm{mlt}}=e^{\theta_{\mathrm{rpd}}}=\sqrt{\frac{1+\beta}{1-\beta}} .
$$

The verification is exact: at $\beta=0.6$ the ratio $z'/z$ is $2.000000000$ for three different sky points, and $\sqrt{(1+\beta)/(1-\beta)}=2$ for that velocity.

### The Flow

Letting the rapidity vary gives a one-parameter group of Möbius maps:

$$
\Phi_s(z)=e^{s}z,
\qquad s\in\mathbb{R},
$$

which is the flow of the vector field $z\partial_z$ on the sky. So the boost is a **flow**: a continuous motion of every star along a curve, generated by one vector field, with the group law $\Phi_s\circ\Phi_t=\Phi_{s+t}$ inherited from the additivity of rapidities along one axis.

### The Orbits

The flow's orbits are the rays from the origin in the $z$ plane, which are the circles through the two poles on the sphere — the meridian semicircles through the forward and backward directions. So each star moves along a meridian, from the backward pole toward the forward pole, and never leaves its own meridian.

### Why a Flow and Not a Rotation

A rotation is also a one-parameter group of Möbius maps, but its orbits are closed circles and its parameter is periodic. The boost's orbits are open arcs and its parameter is not periodic: $s\to\infty$ takes every star to the forward pole and $s\to-\infty$ to the backward one. So the two kinds of frame transformation are distinguished on the sky by the topology of their orbits, which is the fixed-point classification of *The Four Kinds of Frame Transformation* read on the sphere.

## The Fixed Direction

### The Two Fixed Points

The Möbius map $z\mapsto\digamma_{\mathrm{mlt}} z$ fixes $z=0$ and $z=\infty$: the backward and the forward direction of the boost axis. They are the two points where the axis meets the sky, and they are the only directions whose aberration is zero.

### The Flow Between Them

Every other direction moves from the backward pole toward the forward one as the rapidity grows. The star exactly at the forward pole stays there, and the star exactly at the backward pole stays there, and every other star traverses the open arc between them.

### Why Two and Not One

A boost is a hyperbolic element, and a hyperbolic Möbius transformation has exactly two fixed points. A null rotation — the parabolic case — has one, and a rotation has two as well, with closed orbits. So the fixed-point count alone does not separate rotation from boost; the orbit topology does, and the sky shows both facts at once.

### The Stability

The forward pole is attracting and the backward pole repelling, for $\digamma_{\mathrm{mlt}}>1$. So the flow has a stable and an unstable fixed point, and the stable one is the direction the observer is moving toward. That is the geometric content of "the stars crowd forward".

### The Three Kinds on the Sky

A Möbius map is classified by its fixed points and by its multiplier, and the three classes are exactly the three kinds of frame change read on the sky.

| kind | normal form | fixed points | frame change |
|---|---|---|---|
| elliptic | $z\mapsto e^{i\alpha}z$ | two, on the axis | a rotation through $\alpha$ |
| parabolic | $z\mapsto z+1$ | one, double | a null translation, the wall element |
| loxodromic | $z\mapsto\digamma_{\mathrm{mlt}} z$, $\lvert\digamma_{\mathrm{mlt}}\rvert\neq1$ | two, the axis directions | a boost times a rotation about the axis |

The multiplier is the frame's spectrum read on the sky: $\lvert\digamma_{\mathrm{mlt}}\rvert=e^{\theta_{\mathrm{rpd}}}$ and $\arg\digamma_{\mathrm{mlt}}=\theta_{\mathrm{axr}}$. So a boost is the loxodromic case with $\digamma_{\mathrm{mlt}}$ real and positive, a rotation is the elliptic case with $\lvert\digamma_{\mathrm{mlt}}\rvert=1$, and the parabolic case is the one whose multiplier is $1$ with a single fixed point — the unipotent element that the exponential chart reaches only in a limit. A pure boost therefore sits in the loxodromic class, and the word "hyperbolic" used above is the name of the real-positive subcase.

### The Cross-Ratio Check

The invariant that decides whether a map of the sky is a symmetry is the cross-ratio. For four sky points with coordinates $z_1,z_2,z_3,z_4$,

$$
\mathrm{CR}=\frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)} ,
$$

and every Möbius map preserves it. That is the check that the boost's action is projective and not merely some map of the sphere: a map preserving the cross-ratio of every four points is Möbius, and the Lorentz group's action is Möbius by construction.

The check is verified numerically in the coordinate $z=\cot\frac{\theta}{2}e^{i\theta_{\mathrm{azm}}}$. Four directions with angles and azimuths $(0.3,0.2)$, $(1.0,1.1)$, $(2.0,4.0)$, $(2.6,-0.7)$ give $\mathrm{CR}=0.839076+0.192655i$; after the map $z\mapsto(3z+i)/(iz+2)$, an element of $SL_2(\mathbb{C})$ with all four coefficients nonzero and therefore a boost composed with a rotation, the same four points give the same value, the difference being $0$ to twelve digits. The dilation $z\mapsto 2z$ of the boost at $\beta=0.6$ preserves it too, as any dilation must.

## The Conformal Factor

### The Metric on the Sky

The round metric of the sphere in the coordinate $\theta,\theta_{\mathrm{azm}}$ is

$$
ds^{2}=d\theta^{2}+\sin^{2}\theta\,d\theta_{\mathrm{azm}}^{2},
$$

the round metric of the unit sphere; in the $z$ coordinate it reads

$$
ds^{2}=\frac{4\,\lvert dz\rvert^{2}}{(1+\lvert z\rvert^{2})^{2}},
$$

and the two forms agree because $\lvert dz/d\theta\rvert=\frac{1}{2\sin^{2}(\theta/2)}$ and $1+\lvert z\rvert^{2}=\csc^{2}(\theta/2)$.

### The Factor

Under a boost the metric is rescaled:

$$
g\longmapsto\Omega^{2}g,
\qquad
\Omega=\frac{\sqrt{1-\beta^{2}}}{1+\beta\cos\theta},
$$

with $g$ the round metric of the sky.

The factor is verified numerically at $\theta=1$, $\beta=0.6$: the ratio of the transformed metric to the original is $0.364993406$ in the $\theta$ direction and $0.364993406$ in the $\theta_{\mathrm{azm}}$ direction, and both equal $(1-\beta^{2})/(1+\beta\cos\theta)^{2}$.

### Why It Is the Same in Both Directions

The equality of the two ratios is the statement that the map is conformal: it distorts lengths but not angles. That is a property of Möbius maps in general, and here it says that a boost does not twist the sky.

So aberration stretches the sky in the direction of motion and compresses it in the other direction, but a small shape is taken to a similar small shape, rotated only by the map's own conformal rotation.

### What It Means Physically

The conformal factor is the reason the sky's *shape* information is not destroyed by a boost: the cosmic microwave background's acoustic peaks are shifted and rescaled by a boost, but not blurred, because the map is conformal. It is also the reason the celestial sphere's conformal structure, and not its metric, is the Lorentz-invariant object.

### The Reading

An observer's sky is a conformal sphere, and the observer's state of motion is a point of the Möbius group. So "the sky looks the same to everyone up to a Möbius map" is exact, and the group that implements it is the block's group modulo its centre.

## The Limits

### Small Angle

For small velocity, expanding the aberration formula gives

$$
\theta'\approx\theta-\beta\sin\theta ,
$$

so the displacement is proportional to the velocity and maximal at $\theta=\pi/2$, where it equals $\beta$ radians. The numerical check: at $\beta=0.001$ the ratio $(\theta-\theta')/\beta$ is $0.479215$ at $\theta=0.5$, $0.931870$ at $\theta=1.2$ and $0.675712$ at $\theta=2.4$, against $\sin\theta=0.479426$, $0.932039$ and $0.675463$.

### Why the Sine

The transverse displacement is $\beta\sin\theta$ because the boost moves the observer sideways relative to the line of sight by $\beta\sin\theta$ per unit time, and the line of sight's angle changes by that transverse displacement divided by the unit distance. The $\sin\theta$ is the only geometric factor available.

### Large Velocity

As $\beta\to1$ the whole sky crowds into a small cap around the forward direction: $\theta'\to0$ for every $\theta<\pi$. The numerical values: at $\beta=0.9999$, $\theta=1$ is seen at $0.0077$ and $\theta=3$ at $0.199$. The star exactly at $\theta=\pi$ stays at $\pi$ for every $\beta$, and that is the second fixed point surviving the limit.

### The Isotropic Point

There is no direction with zero aberration except the axis. A reader sometimes expects the direction perpendicular to the motion to be undistorted; it is not: at $\theta=\pi/2$ the aberration is $\cos\theta'=\beta$, so $\theta'=\arccos\beta$, which is a substantial displacement at high speed. What *is* undistorted at $\theta=\pi/2$ is nothing at all; the only undistorted directions are the two poles.

### The Telescopes

The aberration of starlight is a $\beta=10^{-4}$ effect for the Earth's orbital motion, of order $20$ arcseconds, and it was measured in 1728. The relativistic formula's deviations from the classical one are of order $\beta^{2}\sim10^{-8}$ for the Earth and are measured for particles, not for stars.

## Summary

The sky is the sphere of null directions, coordinatised by $z=\cot(\theta/2)e^{i\theta_{\mathrm{azm}}}$, and the Lorentz group acts on it by Möbius maps. A boost along the axis acts by $z\mapsto\digamma_{\mathrm{mlt}} z$ with $\digamma_{\mathrm{mlt}}=\sqrt{(1+\beta)/(1-\beta)}$, verified exactly; it is a flow with two fixed points at the poles of the axis, attracting forward and repelling backward, whose orbits are the meridians. The aberration formula $\cos\theta'=(\cos\theta+\beta)/(1+\beta\cos\theta)$ follows from the congruence action on a null element and is verified at three angles. The map is conformal, with the metric rescaled by $\Omega^{2}$ and $\Omega=\sqrt{1-\beta^{2}}/(1+\beta\cos\theta)$, verified to be isotropic. In the small-velocity limit the displacement is $\beta\sin\theta$; in the large-velocity limit the whole sky crowds into a cap around the forward direction, and only the two poles stay put.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\theta,\theta_{\mathrm{azm}}$ | polar angle and azimuth on the sky |
| $z=\cot(\theta/2)e^{i\theta_{\mathrm{azm}}}$ | the sky coordinate adapted to the boost |
| $\beta$ | speed in units of $c$ |
| $\theta_{\mathrm{rpd}}=\operatorname{artanh}\beta$ | rapidity |
| $\digamma_{\mathrm{mlt}}=e^{\theta_{\mathrm{rpd}}}$ | the Möbius dilation |
| $\Omega$ | the conformal factor |

## Further Reading

- J. L. Synge, *Relativity: The Special Theory*, North-Holland, 1965 — aberration, its conformal character and the celestial sphere.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984 — the sky as $\mathbb{CP}^{1}$ and the Möbius action of the Lorentz group.
- C. W. Misner, K. S. Thorne and J. A. Wheeler, *Gravitation*, Freeman, 1973, §6.6 — the aberration formula and the conformal rescaling of the sky.
- W. Pauli, *Theory of Relativity*, Pergamon, 1958, §21 and its appendix — aberration, stellar and terrestrial, with the historical references.
- *The Null Cone: The Massless Boundary* — the sky and its relation to the cone.
- *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* — the boost's action on the other space of directions.
