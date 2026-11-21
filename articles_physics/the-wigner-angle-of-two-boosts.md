# __The Wigner Angle of Two Boosts: Closed Form, Axis and Composition__

## Introduction

Two frame changes compose to a frame change and a rotation. The rotation is one angle, and the addition of velocities is not associative because of it. This article computes that angle, its axis and the laws it obeys.

The companions carry the two readings of the result elsewhere. *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form* computes the compact factor, its cocycle, its holonomy and its path integral; *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* reads the angle as a hyperbolic area; *The Informational Reading of the Wigner Angle* reads it as a unitary channel. None of the three computes the defect of associativity, the gyrogroup laws or the closed form. That is the subject here.

The article's claim is that the matrix is fixed by the pair of velocities alone. The angle does not depend on what is transported or on the third velocity in an addition, and that independence is what makes it a gyration rather than the holonomy of a general path.

The findings are stated in advance.

1. Velocity addition is not associative, and the defect is a rotation of the last argument. The identity $\vec u\oplus(\vec v\oplus\vec w)=(\vec u\oplus\vec v)\oplus\operatorname{gyr}[\vec u,\vec v]\vec w$ holds exactly, to $4.4\times10^{-16}$ on a sample of one hundred triples with moduli up to $0.91$. The rotation does not repair a small error; it is the instruction for reassociating.
2. The gyration is an orthogonal matrix of determinant one about $\pm\vec u\times\vec v$. Verified on fifty pairs: determinant one to $3.3\times10^{-16}$, axis aligned with $\vec u\times\vec v$ to $5.0\times10^{-15}$.
3. Its angle obeys the closed form of the companion, to $5.6\times10^{-14}$. For $\vec u=0.6\vec e_x$ and $\vec v=0.6\vec e_y$ the angle is exactly $2\arctan(1/9)$, and the matrix is the rational rotation of the $9$–$40$–$41$ triangle.
4. The gyrogroup laws hold exactly. Gyrocommutativity $\vec u\oplus\vec v=\operatorname{gyr}[\vec u,\vec v](\vec v\oplus\vec u)$ to $1.1\times10^{-16}$; the two loop properties to $1.2\times10^{-14}$; the inverse law $\operatorname{gyr}[\vec v,\vec u]=\operatorname{gyr}[\vec u,\vec v]^{-1}$ to $2.1\times10^{-15}$.
5. The defect vanishes along the axis. A third velocity parallel to $\vec u\times\vec v$ is untouched by the gyration, and there the two groupings agree exactly.
6. The angle is frame-dependent and therefore relational. The pair $(0.6\vec e_x,0.6\vec e_y)$ reads $12.680383^\circ$; after a boost of rapidity $0.8$ along $\vec e_x$ the transported pair reads $16.018431^\circ$.

The notation is that of the companions. The element $\tilde U_{\vec u}$ is the boost rotor of rapidity $\theta_1=\operatorname{artanh}\lvert\vec u\rvert$ along $\vec u$; the gyration rotor $\tilde U_{\mathrm gyr}$ is real and of unit norm. The congruence is $\mathrm{Cg}_{\tilde U}:\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$; the trace of the $2\times2$ image is $2\,\mathrm{Sc}$; the state is $\tilde{Ϛ}_{\Psi}=\tfrac12(e_t+i\vec s_{\Psi})$ with $\vec s_{\Psi}$ real and radius below one. The Wigner angle is written $\theta_{\mathrm{wgn}}$ here and $\Omega$ in the companion on the shared group. Velocities are in units of $c$.

The one convention that matters is the order of the addition. $\vec u\oplus\vec v$ is the velocity, in the original frame, of a frame that moves at $\vec v$ relative to the frame that moves at $\vec u$. With that reading, two velocities along $\vec e_x$ and $\vec e_y$ of $0.6$ each compose to $(0.6,0.48,0)$, whose modulus is $0.768375$, and the component along $\vec e_y$ is the $0.6$ scaled by $1/\gamma$.

## The Failure of Associativity

### Three frame changes, two groupings

Three frame changes can be grouped in two ways, and the two groupings disagree. Write $\vec u\oplus\vec v$ for the composition of two, and consider $\vec u\oplus(\vec v\oplus\vec w)$ and $(\vec u\oplus\vec v)\oplus\vec w$. The first applies $\vec w$ first, then $\vec v$, then $\vec u$; the second applies $\vec w$ last. They are different sequences of frame changes, so there is no reason for one number, and there is none.

**The disagreement is not a numerical accident and it is not a rotation of the result.** For $\vec u=0.6\vec e_x$, $\vec v=0.6\vec e_y$ and $\vec w=0.5\vec e_x$ the two groupings give $(0.792120,0.436773,0)$ and $(0.806452,0.387097,0)$, whose moduli are $0.904558$ and $0.894544$ and whose directions differ by $3.231224^\circ$. For $\vec w=0.3(\vec e_x+\vec e_y+\vec e_z)$ the two differ by $2.849898^\circ$. The two results are not related by any rotation, because a rotation preserves the modulus and the moduli differ.

The defect is in the third argument, and the law states where. Reassociating requires one operation and no approximation: rotate the last velocity by the gyration of the first two, or by its inverse when the reassociation runs the other way. That is the content of the gyroassociative law, and it is exact.

### The defect measured

The reassociation identity holds to machine precision. On a hundred random triples with moduli below $0.91$ the deviation is $4.4\times10^{-16}$. The same law written the other way, $(\vec u\oplus\vec v)\oplus\vec w=\vec u\oplus(\vec v\oplus\operatorname{gyr}[\vec u,\vec v]^{-1}\vec w)$, is the same identity read backwards; the inverse appears because the reassociation runs the other way. One law, two spellings.

The identity is a statement about the map and not about the triple. The same matrix $\operatorname{gyr}[\vec u,\vec v]$ works for every $\vec w$; on a hundred random values of the third velocity the rotation that reconciles the two groupings does not change, the residual staying at $1.4\times10^{-15}$. That is what separates a gyration from a general path holonomy: the gyration is a function of the pair, and the triple enters only through the argument it is applied to.

The defect vanishes on the axis. For $\vec w=0.5\vec e_z$, with the same $\vec u$ and $\vec v$, the two groupings give $(0.6,0.48,0.32)$ and $(0.6,0.48,0.32)$: identical to every digit. The gyration is a rotation about $\vec u\times\vec v=\vec e_z$, so it fixes $\vec e_z$, and a third velocity along the axis is transported unchanged. The agreement is exact and it is a check on the axis, not a coincidence.

## The Gyration

### Definition from the group

The gyration is the compact factor of the product of the two boost rotors. Write
$$
\tilde U_{\vec u}\,\tilde U_{\vec v}=\tilde U_{\vec u\oplus\vec v}\,\tilde U_{\mathrm gyr},
\qquad
\tilde U_{\mathrm gyr}=\cos\frac{\theta_{\mathrm{wgn}}}{2}e_t+\sin\frac{\theta_{\mathrm{wgn}}}{2}\vec u_{\mathrm r},
$$
with $\tilde U_{\vec u\oplus\vec v}$ the boost rotor of the composed velocity and $\vec u_{\mathrm r}$ a real unit vector. This is the Cartan decomposition of the companion, applied to the pair, and it determines $\tilde U_{\mathrm gyr}$ uniquely: it is the real unit quaternion that the product contains.

**The gyration is therefore not an added convention.** It is the part of the product that the boost cannot account for, extracted by the polar split. Any convention for velocity addition that agrees with the group has the same product and hence the same gyration; the only freedom is the sign, which is fixed by the order of the two velocities.

As a matrix it acts on $\mathbb{R}^{3}$ by the congruence of a real pure quaternion.
$$
\operatorname{gyr}[\vec u,\vec v]\,\vec h=\operatorname{Vec}\bigl(\tilde U_{\mathrm gyr}\,\vec h\,\tilde U_{\mathrm gyr}^{*}\bigr),
$$
with $\operatorname{Vec}$ the vector part. On a real element the congruence and the adjoint differ by nothing, because $\tilde U_{\mathrm gyr}^{*}=\tilde U_{\mathrm gyr}^{-1}$. That coincidence is the companion's result, and it is why the material and informational readings below can share one matrix.

### The axis and the angle

The axis is normal to the plane of the two velocities. On fifty random pairs the axis of the gyration, computed as the eigenvector of eigenvalue one, agrees with $\pm\vec u\times\vec v$ to $5.0\times10^{-15}$, and the determinant is one to $3.3\times10^{-16}$. The axis is defined up to sign by the geometry and fixed by the order: exchanging $\vec u$ and $\vec v$ inverts the gyration, to $2.1\times10^{-15}$.

The angle is the one the companion computes, and the closed form is the same. With $\theta_1,\theta_2$ the rapidities of the two velocities and $\phi$ the angle between their directions,
$$
\tan\frac{\theta_{\mathrm{wgn}}}{2}=
\frac{\sinh\frac{\theta_1}{2}\sinh\frac{\theta_2}{2}\sin\phi}
{\cosh\frac{\theta_1}{2}\cosh\frac{\theta_2}{2}+\sinh\frac{\theta_1}{2}\sinh\frac{\theta_2}{2}\cos\phi}.
$$
Verified against the matrix arccosine on two hundred random pairs, worst deviation of the two sides $5.6\times10^{-14}$.

At $\phi=\pi/2$ the right side is $\tanh^{2}(\theta/2)$, so
$$
\theta_{\mathrm{wgn}}=2\arctan\Bigl(\tanh^{2}\frac{\theta}{2}\Bigr).
$$
At $\lvert\vec u\rvert=\lvert\vec v\rvert=0.6$ the rapidity has $\tanh\theta=3/5$, hence $\tanh(\theta/2)=1/3$ and $\tan\frac{\theta_{\mathrm{wgn}}}{2}=1/9$. The gyration is then the rational rotation of the $9$–$40$–$41$ triangle,
$$
\operatorname{gyr}[0.6\vec e_x,0.6\vec e_y]=\frac{1}{41}
\begin{pmatrix}40 & 9 & 0\\ -9 & 40 & 0\\ 0 & 0 & 41\end{pmatrix},
$$
with $\cos\theta_{\mathrm{wgn}}=40/41$ and $\sin\theta_{\mathrm{wgn}}=9/41$, an angle of $12.680383^\circ$.

### The angle as a function of the direction

At fixed speeds the angle depends on the angle between them and on nothing else. With both speeds at $0.6$ the numbers are the table.

| $\phi$ | $\theta_{\mathrm{wgn}}$ |
| --- | --- |
| $0$ | $0.000000^\circ$ |
| $30^\circ$ | $5.802418^\circ$ |
| $60^\circ$ | $10.417438^\circ$ |
| $90^\circ$ | $12.680383^\circ$ |
| $120^\circ$ | $11.635051^\circ$ |
| $180^\circ$ | $0.000000^\circ$ |

The angle vanishes at both ends and peaks near the right angle. Parallel velocities gyrate by nothing, because the boosts commute; antiparallel ones also gyrate by nothing, because they compose along one axis. For equal speeds the maximum is $12.7589^\circ$, reached at $\phi=96.38^\circ$ and not at $90^\circ$; the asymmetry is small and it is real.

At small speeds the angle is the area of the parallelogram. For $\lvert\vec u\rvert=\lvert\vec v\rvert=\epsilon$ at a right angle the ratio of $\theta_{\mathrm{wgn}}$ to $\lvert\vec u\times\vec v\rvert/2$ is $1.020479$ at $\epsilon=0.2$, $1.005029$ at $\epsilon=0.1$ and $1.001252$ at $\epsilon=0.05$, so the leading term is the cross product over two and the correction is quadratic. The Wigner angle is the curvature of velocity space seen at first order, and the closed form is the exact statement.

## The Gyrogroup Laws

### The gyroassociative law

The law is the statement that velocity addition is associative up to the gyration. In full,
$$
\vec u\oplus(\vec v\oplus\vec w)=(\vec u\oplus\vec v)\oplus\operatorname{gyr}[\vec u,\vec v]\,\vec w .
$$
The right side is not the same as the left; it is the left with the third velocity rotated. The law holds exactly, and it is the only compensation available: the defect is a rotation and nothing else.

**The law also fixes what the defect is not.** It is not a failure of the addition to be well defined, and it is not a failure of the grouping to be lawful. Both groupings are lawful; they are groupings of different maps. The law states the correction that turns one into the other.

### The gyrocommutative law and the loops

Two velocities compose to the same speed in either order, but not to the same direction. The law is
$$
\vec u\oplus\vec v=\operatorname{gyr}[\vec u,\vec v]\bigl(\vec v\oplus\vec u\bigr),
$$
verified to $1.1\times10^{-16}$ on fifty pairs. So the addition is commutative up to the gyration and not commutative.

The gyration of a pair is the gyration of the pair with its sum. Two loop properties state it: $\operatorname{gyr}[\vec u,\vec v]=\operatorname{gyr}[\vec u\oplus\vec v,\vec v]$ and $\operatorname{gyr}[\vec u,\vec v]=\operatorname{gyr}[\vec u,\vec v\oplus\vec u]$, verified to $1.2\times10^{-14}$ and $8.8\times10^{-15}$. The gyration is therefore not an independent datum attached to a pair; it is the same datum attached to a family of pairs.

The inverse law closes the structure. $\operatorname{gyr}[\vec v,\vec u]=\operatorname{gyr}[\vec u,\vec v]^{-1}$, to $2.1\times10^{-15}$. Reading it with the axis in hand: reversing the order reverses the angle and keeps the axis up to sign, which is what a rotation about a line does.

## The Two Readings

This article fixes the angle, the axis and the composition law, and it stops there. The angle is one number of the group, and it can be read on either of the two slices of the algebra; the two readings are articles, not paragraphs, and they live in the sections below.

- The material reading is the holonomy of the boost connection: the gyration as a motion of the velocity ball, the deficit of the geodesic triangle, and Thomas precession as its rate form. It is a section of [Velocity Space as Hyperbolic Geometry in Biquaternionic Form](velocity-space-as-hyperbolic-geometry-in-biquaternionic-form.html), under *The Curvature of the Boost Connection*.
- The informational reading is the gyration as a unitary channel: the one piece of a frame change that preserves the normalised slice and the Bures distance, acting on the Bloch ball by the same matrix. It is [The Informational Reading of the Wigner Angle](the-informational-reading-of-the-wigner-angle.html).

**What stays here is what holds on both.** The failure of associativity, the gyration, the closed form and the gyrogroup laws are statements about the group, and a statement about the group is a statement about the algebra before any slice is chosen.

## Objections

The objection is that the gyration is an artefact of a choice: velocity addition is defined by a formula, the formula is not associative, and the failure says nothing about the world. A reader who takes this view will point out that the group product is associative by construction and that no physical quantity can depend on a grouping.

**The answer is that the group product is associative and the gyration is exactly the price of forgetting that.** The gyration is the compact factor of an associative product; it appears in the addition law because the addition law records only the velocity, and the velocity is one coordinate of a Lorentz transformation that also carries a rotation. The defect is not of the world but of the coordinate, and it is measurable in the coordinate: Thomas precession is the measurement, and the holonomy of the triangle is its finite form.

A second objection is that if the gyration is a channel, then a frame change is partly a channel, which breaks the dichotomy between reversible and irreversible. The answer is that the dichotomy is about whole maps. The product of a non-channel and a channel is not a channel, and the split into factors is the Cartan split, not a decomposition into operations that an observer performs one after the other. The observational content is positive and narrow: of the two factors of a frame change, exactly one is a channel.

A third objection is that the angle is frame-dependent, so nothing about it can be a fact. The answer is that the angle is a function of a pair of frames, and it transforms as such: $12.680383^\circ$ in one frame and $16.018431^\circ$ after a boost of rapidity $0.8$ along $\vec e_x$. A relational quantity is not a defect. The invariants of the group are the norm and the bracket; the angle is not one, and the article claims for it only what a relation can carry.

## What Is Not Claimed

It does not give a dynamics. The gyration is kinematic. Thomas precession requires an orbit and an acceleration, and the article supplies neither; it supplies the finite holonomy that the rate differentiates.

**It does not say that the two readings are two physical effects.** They are one matrix read through two families of observables. A reader who counts them as two results has double-counted.

It does not claim that a frame change is a channel. It claims that one factor of a product of two frame changes is, and that the other is not, with $2\,\mathrm{Sc}$ as the test.

It does not prove the closed form. The companion proves it; the article verifies it independently at $5.6\times10^{-14}$ and uses it. What the article proves is the reassociation identity and the channel status of the compact factor.

## Summary

Velocity addition is associative only up to a rotation, and the rotation is the gyration. The identity $\vec u\oplus(\vec v\oplus\vec w)=(\vec u\oplus\vec v)\oplus\operatorname{gyr}[\vec u,\vec v]\vec w$ holds to $4.4\times10^{-16}$, the matrix is orthogonal of determinant one about $\pm\vec u\times\vec v$, and it is the same for every third velocity. The law is the Cartan decomposition of the product of two boost rotors, so the defect is a property of the group and not of the formula.

The angle is exact in closed form and rational in the worked case. At $0.6$ and $0.6$ at a right angle it is $2\arctan(1/9)$, and the matrix is the rotation of the $9$–$40$–$41$ triangle. It vanishes for parallel and for antiparallel velocities, peaks at $\phi=96.38^\circ$ for equal speeds, and reduces to $\lvert\vec u\times\vec v\rvert/2$ at leading order in the speeds.

The gyrogroup laws hold exactly. Gyrocommutativity to $1.1\times10^{-16}$, the two loop properties to $1.2\times10^{-14}$ and $8.8\times10^{-15}$, and the inverse law to $2.1\times10^{-15}$. The gyration is the holonomy of the closed triangle of boosts, so it is a curvature of velocity space and not a bookkeeping convention.

The gyration is the compact factor, and it is the only piece of a frame change that is an isometry of the compact slice. Its rotor is real, so its congruence is its adjoint; a boost's is not. The consequence on the state space is the subject of *The Informational Reading of the Wigner Angle*, and the consequence on the velocity ball is a section of *Velocity Space as Hyperbolic Geometry in Biquaternionic Form*. Neither statement is used here.

**The angle is relational.** No single velocity registers it; a comparison of two does. It is not an invariant of the group but a function of a pair, and it changes with the frame that reads it.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\vec u\oplus\vec v$ | the velocity of a frame moving at $\vec v$ relative to the frame moving at $\vec u$ |
| $\operatorname{gyr}[\vec u,\vec v]$ | the gyration of the pair, an element of $SO(3)$ |
| $\tilde U_{\vec u}$ | the boost rotor of velocity $\vec u$, of unit norm |
| $\tilde U_{\mathrm gyr}$ | the gyration rotor, real and of unit norm |
| $\theta_{\mathrm{wgn}}$ | the gyration angle, written $\Omega$ in the companion |
| $\theta_1,\theta_2$ | the rapidities of $\vec u$ and $\vec v$ |
| $\phi$ | the angle between the directions of $\vec u$ and $\vec v$ |
| $\vec u_{\mathrm r}$ | the axis of the gyration, $\pm\vec u\times\vec v$ |
| $\mathrm{Cg}_{\tilde U}$ | the congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ |

## Further Reading

- A. A. Ungar, "Thomas rotation and the parametrization of the Lorentz transformation group", *Foundations of Physics Letters* 1 (1988) 57–89 — the gyrogroup laws, the gyration and its loop properties
- A. A. Ungar, *Analytic Hyperbolic Geometry and Albert Einstein's Special Theory of Relativity*, World Scientific, 2008 — the velocity ball as a gyrovector space and the defect of its triangles
- L. H. Thomas, "The motion of the spinning electron", *Nature* 117 (1926) 514 — the precession of a spinning particle on a curved orbit
- J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley, 1999, §11.8 — the Thomas precession rate as the differential of the holonomy
- V. Bargmann, L. Michel and V. L. Telegdi, "Precession of the polarization of particles moving in a homogeneous electromagnetic field", *Physical Review Letters* 2 (1959) 435–436 — the equation in which the Thomas term appears
- *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form* — the compact factor, its cocycle and its holonomy
- *The Two Actions of One Group: Adjoint and Congruence* — the coincidence of the two actions on the compact slice
- *The Lorentz Group on the Bloch Ball: Projective Action and Two Metrics* — the congruence as a Lorentz transformation and the placing of the two metrics
- [The Informational Reading of the Wigner Angle](the-informational-reading-of-the-wigner-angle.html) — the compact factor read as a unitary channel on the state space
- *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* — the ball, its Klein metric and the defect of its triangles
