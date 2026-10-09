# __The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase__

## Introduction

A massless element of the framework is an element of zero biquaternion norm, and its **direction** is the only datum its norm does not remove. The set of those directions is an object with a name and a long history in the relativity of the null cone: the **celestial sphere**. This article gathers the sphere, describes the two chiralities it carries, and records the reading that a massless element is a **point of the celestial sphere together with a phase**. It is deliberately short, because most of the machinery it uses is owned elsewhere: the Hopf bundle and its winding numbers belong to *The Hopf Fibration and the Biquaternion Gauge Bundle*, the metric geometry of the sphere to *The Fubini–Study Geometry and the Biquaternion Norm*, the little group and the helicity weights to *The Spinor-Helicity Formalism and Biquaternions*, and the photon's nullity to *The Photon as a Null Element: What the Cone Derives and What It Does Not*. What this article owns is the **sphere of directions of the null cone** — its definition inside the algebra, its two chiralities, and the sentence that says what a massless element physically is.

## The Null Cone of the Algebra

The null cone is the zero set of the biquaternion norm,

$$
N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0,
$$

and its nonzero elements are exactly the **zero divisors** of the algebra, the elements whose matrix image $\Phi(\tilde{Q})$ has rank one. On the material sector $\mathbb{M}_-$, with $\tilde{Q} = ict\,e_0 + \mathbf{x}$, the norm is the interval,

$$
N(\tilde{Q}) = -c^2t^2 + |\mathbf{x}|^2,
$$

so the null cone of the algebra restricts to the **light cone** of the material sector, and its nonzero elements are the lightlike four-vectors. The cone is a real three-dimensional cone in the four real dimensions of the sector; it has a single point at the origin and is otherwise regular, and its nonzero elements are the lightlike directions of the material geometry.

## The Projective Null Cone: the Celestial Sphere

The cone is a cone over its own directions. Two nonzero null elements define the **same direction** when one is a nonzero scalar multiple of the other; the set of directions is the **projectivisation** of the null cone, and on the material sector it is a two-dimensional sphere,

$$
\mathcal{C} \;=\; \bigl\{\text{null directions of }\mathbb{M}_-\bigr\} \;\cong\; S^2,
$$

which is the **celestial sphere** of the light cone: the sphere of lightlike directions at a point, the sphere a photon's momentum points along, swept by the two angles $(\theta,\varphi)$. The Lorentz group acts on it transitively: the future lightlike directions form one orbit of the proper orthochronous Lorentz group, the past directions the other, and time reversal exchanges the two. No direction is preferred, which is the statement that the sphere is a single orbit. A **massless element** is determined by its direction and its scale, and the scale is not a Lorentz datum of the direction; so the sphere, and not the cone, is the Lorentz-homogeneous object.

## The Two Chiralities: the Segre Quadric

Over the complex numbers the cone has a second structure, and it is the one the spinors see. Complexifying, the null cone of the biquaternion algebra is a complex three-dimensional cone in $\mathbb{B}\cong\mathbb{C}^4$, and its projectivisation is a **quadric in the projective three-space**, the **Segre quadric**

$$
\mathbb{P}^1\times\mathbb{P}^1 \;\subset\; \mathbb{P}^3,
$$

whose two rulings are the two families of chiral spinor lines. This is the projective null cone the corpus records in *The Null Quadric and Its Projective Geometry*, and it is the object the twistor article compares with twistor space: the quadric is a product of two complex projective lines, the two **chiral celestial spheres**, and the two rulings are the primed and the unprimed spinor families. The relation between the two pictures is a real slice: the two chiral spheres of the complex cone are complex conjugates of one another, and the real celestial sphere of the material sector is their diagonal, the fixed set of the conjugation. So the real sphere $S^2$ is one sphere and the complex cone carries two, and the pair of them, not the one, is what the complexified cone projectivises to. The complex cone comes with a circle bundle of its own: its **link** in the unit sphere is an $S^1$-bundle over the pair of chiral spheres,

$$
S^1 \;\longrightarrow\; L \;\longrightarrow\; S^2\times S^2,
$$

so that over the complexified cone the phase is a circle over the two spheres together, as *The Topology of the Zero-Divisor Cone* records, whereas over the real sphere the phase is the circle of the Hopf fibration below.

## The Spinor Coordinates

The sphere and the spinors are the same object in two coordinates. A null element of the material sector, carried to the informational sector by the central rotation, $\tilde H = -i\tilde P \in \mathbb{M}_+$, is a rank-one Hermitian element, and a **positive** such element is a product of a spinor with its conjugate,

$$
\tilde{\Pi}_\xi = \xi\,\xi^{\dagger}, \qquad \xi \in \mathbb{C}^2,
$$

with $\tilde{\Pi}_\xi$ of rank one exactly when $\xi\neq0$, and idempotent when $\xi$ is normalised. The sign is the direction of time: a future-pointing null element gives a positive-semidefinite matrix and a past-pointing one gives its negative, so the two orbits of the sphere are the two signs, and the positive case is the one the spinor-helicity factorisation uses (*The Spinor-Helicity Formalism and Biquaternions*). The **direction** of $\tilde{\Pi}_\xi$ depends on the spinor only through its **ray**: replacing $\xi$ by $e^{i\alpha}\xi$ multiplies $\xi\xi^{\dagger}$ by $e^{i\alpha}e^{-i\alpha} = 1$ and leaves the element unchanged, so the direction is a **spinor up to a phase**, and

$$
\mathcal{C} \;\cong\; \mathbb{C}\mathbb{P}^1 \;\cong\; S^2.
$$

This is the standard identification of the Riemann sphere with the celestial sphere: the spinor $\xi$ is a pair of complex numbers, its ray is a point of $\mathbb{C}\mathbb{P}^1$, and the transition between the two presentations is the stereographic projection of the sphere. The metric the sphere carries in this presentation, and the transition probability between two of its rays, are *The Fubini–Study Geometry and the Biquaternion Norm*; this article records only the identification of the object.

## The Little Group and the Phase

A null direction is fixed by a subgroup of the Lorentz group, its **little group**, and the little group is what attaches the phase to the point. On the spinor $\xi$ the direction is invariant under the phase $\xi\mapsto e^{i\alpha}\xi$, which is the compact $U(1)$ part of the little group; a massless field of **helicity** $h$ transforms under that phase by

$$
\xi \;\longmapsto\; e^{i\alpha}\xi, \qquad \text{the field} \;\longmapsto\; e^{i h\alpha}\,\text{the field},
$$

so the helicity is the **weight** of the central $U(1)$ carried at the point of the sphere. The full statement of the little group, the two helicities of the photon and the weights of the massless amplitudes, are *The Spinor-Helicity Formalism and Biquaternions*; the bundle the phase describes, the unit spinors over the sphere with fibre a circle, is the Hopf fibration of the algebra, and it is *The Hopf Fibration and the Biquaternion Gauge Bundle*. What the celestial sphere supplies here is only the **base**: the point of $S^2$ at which the phase sits.

## The Reading

The reading is one sentence and it is the reason the sphere is worth naming. **A massless element is a point of the celestial sphere together with a phase**: the point is its direction, the phase is the little-group $U(1)$ the helicity weights, and the norm — which is zero — has removed only the scale. Read physically, the sphere is the **sky of a photon**: the direction of propagation is a point of $S^2$, the two helicities are the two weights of the phase over that point, and the transitive action of the Lorentz group on the sphere is the statement that no direction is preferred. The two chiralities make the statement spinorial: the complexified sphere is the product of the two chiral spheres, and a massless field of definite chirality lives on one of the two rulings while the real, physical directions are the diagonal on which the two are conjugate.

The reading also fixes the boundary of the object. The sphere is the set of **directions** and not of momenta: it carries no scale, and the norm that would give the scale vanishes on all of it. It carries no dynamics: the helicity is a weight, and a weight is a representation datum and not an equation of motion. And it is the **real** light cone's sphere when the physics is the real light cone; the two chiral spheres belong to the complexified cone, and the real diagonal of the pair is the physical sphere. A reader who wants the metric, the bundle or the little group is sent to the three articles that own them; a reader who wants the object and its name has it here.

## What the Reading Does Not Claim

- It does **not** claim that the celestial sphere is something the biquaternion algebra adds to relativity. The sphere of lightlike directions is standard, and it is met by every four-dimensional treatment of the null cone; the article records its place in the algebra and not a new result.
- It does **not** claim that the sphere derives the massless condition. The cone marks the massless shell and does not choose it, as *The Photon as a Null Element: What the Cone Derives and What It Does Not* records; the sphere is the geometry of the marking, not a derivation of it.
- It does **not** own the metric, the bundle or the little group. The Fubini–Study line element, the Hopf fibration with its winding numbers, and the helicity weights are delegated by name in the text.
- It does **not** claim that the direction datum and the phase are independent in every representation. The spinor presentation ties them — the direction is the ray and the phase is the remaining freedom of the representative — and the article states the tie rather than a product decomposition.

## Summary

The null cone of the biquaternion norm is the zero-divisor cone, and on the material sector it is the light cone. Its **directions**, the null elements up to scale, form the **celestial sphere** $\mathcal{C}\cong S^2$, the sphere of lightlike directions. Complexified, the projective null cone is the **Segre quadric** $\mathbb{P}^1\times\mathbb{P}^1$, the product of the two **chiral celestial spheres**, whose real diagonal is the physical sphere; the two rulings are the two chiral spinor families. In spinor coordinates a null Hermitian element is $\tilde{\Pi}_\xi = \xi\xi^{\dagger}$, its direction is the **ray** of $\xi$, and the sphere is $\mathbb{C}\mathbb{P}^1$, with the metric and the transition probability delegated to the Fubini–Study article. The little group of a direction is a $U(1)$ phase, the **helicity** is the weight of that phase, and the bundle it describes is the Hopf fibration of the algebra. The reading is that **a massless element is a point of the celestial sphere together with a phase**: the point is the direction, the phase is the helicity's $U(1)$, and the norm, being zero, has removed only the scale.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | the biquaternion norm; $N=0$ is the null cone |
| $\mathbb{M}_-$ | the material sector, $\tilde{Q} = ict\,e_0 + \mathbf{x}$ |
| $\mathcal{C} \cong S^2$ | the celestial sphere, the null directions up to scale |
| $\mathbb{P}^1\times\mathbb{P}^1$ | the Segre quadric, the projective complex null cone, the two chiral spheres |
| $\xi \in \mathbb{C}^2$ | the spinor; the direction is its ray, $\xi\mapsto e^{i\alpha}\xi$ |
| $\tilde{\Pi}_\xi = \xi\xi^{\dagger}$ | a positive rank-one Hermitian element, hence null; idempotent for unit $\xi$ |
| $h$ | the helicity, the weight of the little-group $U(1)$ |
| $\mathbb{C}\mathbb{P}^1 \cong S^2$ | the sphere in spinor coordinates |

## Further Reading

- *The Spinor-Helicity Formalism and Biquaternions* — the massless momentum as a zero divisor, rank one as factorisability, the little group and the helicity weights.
- *The Hopf Fibration and the Biquaternion Gauge Bundle* — the unit spinors over the sphere, the Hopf map and its winding numbers.
- *The Fubini–Study Geometry and the Biquaternion Norm* — the metric of the projective line and the transition probability of the pure states.
- *The Photon as a Null Element: What the Cone Derives and What It Does Not* — the massless shell as the zero-divisor cone and the limits of the derivation.
- *The Central Rotation: Phase, Duality and the Wick Rotation as One Generator* — the central imaginary that carries a material element to the informational sector, where the rank-one Hermitian element lives.
- *Twistor Theory and Biquaternions* — the projective null cone, the Segre quadric and the comparison with twistor space.
- *The Null Quadric and Its Projective Geometry* (mathematics) — the Segre embedding, the quadric $\mathbb{P}^1\times\mathbb{P}^1$, the two rulings and the automorphism group.
- *The Topology of the Zero-Divisor Cone* (mathematics) — the link of the cone as an $S^1$-bundle over the projectivised cone $S^2\times S^2$.
- *Biquaternion Rotations and Lorentz Transformations* — the Lorentz action on the lightlike directions and the null cone.
