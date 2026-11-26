# __The Little Group of a Null Momentum: $E(2)$__

## Introduction

A massless particle's little group is the stabiliser of a null momentum. It is not compact, and that single fact determines everything: the massless labels are one-dimensional instead of $(2j+1)$-dimensional, the spin's third component survives as the helicity while the other two components are gauged away, and a second, unphysical family of representations exists with a continuous label.

This article identifies the group, which is the double cover of the Euclidean group of the plane, exhibits its three generators and their brackets, explains what the two null rotations do and why they must act trivially on physical states, and states the helicity and continuous-spin alternatives.

The article assumes *The Little Group of a Massive Particle: $\mathrm{SU}(2)$* for the contrast, *The Null Cone: The Massless Boundary* for the orbit, *Wigner's Classification: Two Casimirs, Three Orbits* for the general framework, and *The Four Kinds of Frame Transformation* for the parabolic class that the null rotations belong to.

## The Light-Like Momentum

### The Standard Momentum

By a rotation, every future-pointing null momentum is brought to

$$
\tilde P_{0}=\tfrac{mc}{2}\bigl(e_t+i\vec e_z\bigr),
$$

whose norm is zero, $\langle\tilde P_0\rangle_{\natural}=0$. The factor $\tfrac12$ is a normalisation: it gives $\tilde P_0^{2}=m\tilde P_0$, so the element is $m$ times an idempotent, and for unit mass it is the pure spinor idempotent $\tfrac12(e_t+i\vec e_z)$.

### The Orbit

The orbit is the future cone minus the vertex, of dimension three, and it is the sky times a positive scale. The standard momentum is one representative, and every other is $\mathrm{Cg}_{\tilde U}(\tilde P_0)$ for some $\tilde U$.

### The Stabiliser

$$
G_{\tilde P_0}=\{\tilde U\in G:\mathrm{Cg}_{\tilde U}(\tilde P_0)=\tilde P_0\}.
$$

It is three-dimensional, because the orbit is three-dimensional in a six-dimensional group. Its identity component is what this article computes.

## The Stabiliser Is $E(2)$

### The Three Generators

Three independent combinations of the six Lorentz generators fix $\tilde P_0$:

$$
T_1=K_x-J_y,\qquad T_2=K_y+J_x,\qquad J_z .
$$

Here $J_{\imath}=\tfrac12\vec e_{\imath}$ is the rotation generator about $\varsigma_{\mathrm{gen}}$ and $K_{\imath}=\tfrac12 i\vec e_{\imath}$ the boost generator along $\varsigma_{\mathrm{gen}}$, in the block's normalisation, in which the rotations are real and the boosts imaginary.

### The Brackets

$$
[T_1,T_2]=0,\qquad
[J_z,T_1]=T_2,\qquad
[J_z,T_2]=-T_1 .
$$

So $T_1$ and $T_2$ commute and rotate into each other under $J_z$: the algebra of the Euclidean group of the plane, with $T_1,T_2$ as the translations and $J_z$ as the rotation. The group is $E(2)$, and its double cover is the little group of the massless particle.

All three identities are verified in the block's matrix model, together with the three parent brackets they come from, $[J_x,J_y]=J_z$, $[K_x,K_y]=-J_z$ and $[J_x,K_y]=K_z$.

### Why the Combinations Work

$K_x$ and $J_y$ each fail to fix the momentum, and their difference does, because the two failures cancel: a boost along $x$ and a rotation about $y$ tilt the closed null direction $t+z$ the same way, by equal amounts at $\tilde P_0$. The pair $K_y$ and $J_x$ cancels the same way, in the sum. That cancellation is not an accident; it is the reason the stabiliser is larger than the rotation subgroup, and it is why the massless little group has a non-compact part at all.

### The Verification

Each of $T_1$, $T_2$ and $J_z$ is exponentiated and applied to $\tilde P_0$ by the congruence; all three fix it to machine precision. $J_z$ fixes it by inspection — it rotates the $x$-$y$ plane and the momentum has no component there — and the two null combinations fix it by the cancellation above.

## The Two Null Rotations

### What They Are

The one-parameter groups $\exp(sT_1)$ and $\exp(sT_2)$ are the **null rotations**. They are not rotations and not boosts; they are the parabolic elements of *The Four Kinds of Frame Transformation*, and a finite $s$ gives a shear along the light-like direction.

### What They Do to a Frame

A null rotation keeps the null direction $\tilde P_0$ fixed and shears the transverse plane. On the celestial sphere it fixes exactly one point — the direction of the momentum — and moves every other point. So it is the unique kind of frame transformation with a single fixed null direction, and that is the geometric reason the massless little group is bigger than the massive one: the massive little group is the group of transformations fixing two null directions, the massless one fixes only one and therefore has more room.

### The Parabolic Reading

Each null rotation is a limit of boosts of infinite rapidity, conjugated into a finite shear. Its trace is exactly $\pm2$, it is conjugate to a unipotent matrix, and it is the element that the exponential chart of *The Exponential Map from Algebra to Group* reaches only in a limit. So the massless little group is where the parabolic class lives in physics.

## The Helicity

### The One-Dimensional Representations

The finite-dimensional unitary representations of $E(2)$ are one-dimensional: the translations act trivially and the rotation acts by a phase,

$$
D_h\bigl(m(\theta_{\mathrm{axr}})a\,n\bigr)=e^{ih\theta_{\mathrm{axr}}},
\qquad h\in\tfrac12\mathbb{Z}.
$$

The label $h$ is the **helicity**.

### Why They Are the Physical Ones

The physical requirement is that a finite number of states sit over each momentum. Since $T_1$ and $T_2$ are non-compact, a representation in which they act nontrivially has a continuous spectrum and infinitely many states. So finiteness forces the translations to act trivially, and the representation collapses to $D_h$.

### The Gauge Argument

There is a second route to the same conclusion, and it is the one used in field theory. A massless field has a local symmetry, and the local transformation shifts the polarisation along the momentum and along one transverse direction: the two directions that the null rotations move. So imposing the fixing condition is imposing $T_1=T_2=0$ on the physical states, and the surviving label is the eigenvalue of $J_z$.

That is why the massless count is two and not three for a spin-1 particle: the three polarisations of the massive case become two helicities plus one gauge mode, and the gauge mode is exactly the orbit of the null rotations.

### The Invariance

$h$ is invariant under the whole Lorentz group — not merely under the little group — because a Lorentz transformation moves the momentum and adjusts the frame, and the helicity is the projection of the spin on the momentum, which is a scalar under that combined operation. So the helicity is a Lorentz label and not a frame-dependent one, in contrast to the spin's third component in the massive case.

### The Sign

The two signs $\pm h$ are related by parity, which reverses the momentum and leaves the spin. So a parity-invariant theory needs both, and a chiral theory may have only one. The block's statement that the massless labels are $(0,h)$ with both signs present in a parity-invariant theory is exactly this.

## The Continuous Spin

### The Infinite-Dimensional Case

If the translations act nontrivially, the representation is infinite-dimensional and labelled by a continuous parameter: the invariant length of the "translation" part, which is the spacelike component of the Pauli–Lubanski vector. These are Wigner's **continuous-spin** representations.

### Why It Is Not Seen

No particle is known to carry a continuous spin. The reason is not in the group theory: nothing in Wigner's classification forbids the family, and it is perfectly unitary. The reason is dynamical — such a particle would have a continuum of helicities and would radiate them — and the block states the group-theoretic possibility and does not explain its absence.

### What Would Show It

A continuous-spin particle would show a continuous distribution of angular momentum about its direction of motion, instead of two discrete helicities. Experiments bound the continuous-spin parameter to be small, and the bound is consistent with zero. So the physical case is the one-dimensional one, and the continuous-spin family is a boundary that nature does not seem to use.

### Why the Block Needs It

It is needed for the classification to be complete, and it is needed to make the statement "the massless representations are the ones with trivial null rotations" a *choice* and not a tautology. A reader who never sees the alternative will think the helicity is forced by the group, and it is forced only by the finiteness of the fibre.

## The Null Rotations in the Algebra

### The Nilpotence

Both null generators square to zero:

$$
T_1^{2}=0,\qquad T_2^{2}=0,\qquad N(T_1)=N(T_2)=0,
$$

so each is a null element of the algebra and each is nilpotent of index two. Both statements are checked in the matrix model: the squares vanish identically and the norms are zero.

### The Two-Term Exponential

Because $T^{2}=0$, the exponential series terminates after one term:

$$
\exp\bigl(sT_1\bigr)=e_t+sT_1,\qquad \exp\bigl(sT_2\bigr)=e_t+sT_2 .
$$

So a finite null rotation is the identity plus a null element, which is the *unipotent* form of *The Four Kinds of Frame Transformation*: a parabolic element written without a limit. That is the algebraic reason the null rotations are the easiest infinite-rapidity limits to compute: their exponential is a polynomial.

### The Shear on the Spinor

Acting on a spinor, $e_t+sT_1$ is the shear

$$
\begin{pmatrix}\xi_1\\ \xi_2\end{pmatrix}\longmapsto
\begin{pmatrix}\xi_1\\ \xi_2+s\xi_1\end{pmatrix},
$$

up to the normalisation of the basis: one component is unchanged and the other is shifted by it. A shear fixes the direction of the first component and moves everything else, which is the matrix form of the single fixed null direction.

### The Fixed Direction

The fixed null direction is the one the sheared spinor still points along, and the shear's parameter $s$ measures how far the transverse plane has been dragged. So the three parameters of $E(2)$ are: the rotation angle about the momentum, and the two shear parameters. That is the same three-parameter count as the massive little group, with two angles replaced by two shears.

## The Helicity as an Invariant

### The Casimir of $E(2)$

The Casimir of the Euclidean algebra is

$$
C_{E(2)}=T_1^{2}+T_2^{2},
$$

which commutes with $T_1$, $T_2$ and $J_z$ — verified in the matrix model. Its eigenvalue separates the two families:

| family | $C_{E(2)}$ | label |
|---|---|---|
| physical (trivial translations) | $0$ | helicity $h$ |
| continuous spin | nonzero | continuous parameter |

So the helicity's family is the one on which the Casimir vanishes and the other Casimir-like label $\exp(2\pi iJ_z)$ is the identity's phase.

### The Commutator With the Momentum

$J_z$ commutes with nothing outside the little group, but its eigenvalue on a state is a Lorentz scalar because the momentum is parallel to the axis of $J_z$ and the whole configuration is invariant under the combined transformation. That is the invariance of the helicity stated earlier in this article: it is a little-group label that survives the induction to the Poincaré group because the little group's compact part is normalised by the momentum itself.

### The Two Labels of the Block

The corpus's massless labels are $(0,h)$: a zero in the mass slot and a half-integer in the helicity slot. The zero is $C_1$'s value, and $h$ is the phase of $J_z$ on the one-dimensional fibre. Nothing else survives: the scale of the momentum is a gauge, the two shear parameters are gauged away, and the direction is the orbit's own coordinate.

## The Contrast With the Massive Case

### Compact and Non-Compact

| | massive | massless |
|---|---|---|
| little group | $SU(2)$ | double cover of $E(2)$ |
| compact? | yes | no |
| labels | $(m,j)$ | $(0,h)$ |
| states per momentum | $2j+1$ | one per helicity sign |
| second Casimir | $m^{2}c^{2}\frac{h^{2}}{4\pi^{2}}j(j+1)$ | $0$ |

The compactness is the whole difference. A compact little group has finite-dimensional unitary representations with a discrete label; a non-compact one has mostly infinite-dimensional ones, and the finite-dimensional survivors are one-dimensional.

### The Count of States

The massive count $2j+1$ is the dimension of an $SU(2)$ module; the massless count is the number of one-dimensional $E(2)$ modules that are realised, which is one per sign of $h$. So the "loss" of states from $2j+1$ to $1$ is not a loss at all: it is the fixing condition, and the states that are removed were never physical.

### The Limit

The group $E(2)$ *is* a contraction of $SU(2)$: the Wigner–İnönü contraction takes the rotation group to the Euclidean group as the rotation's curvature goes to zero. But that contraction is not what the $m\to0$ limit of a particle does. The limit keeps the momentum's scale and sends the momentum to the cone, and the stabiliser there is three-dimensional with a non-compact part, whereas $SU(2)$ has none. So the limit is a jump in the pair (group, momentum) and not a continuous deformation, and the correct statement is the one in *The Null Cone: The Massless Boundary*: the little group grows, it does not shrink.

### What Is Continuous

The one continuous thing is the momentum's scale along the null direction, and it is a pure gauge for a massless particle: a null momentum has no rest frame, so its scale cannot be measured by going to a rest frame, and the physical content is the direction and the helicity. So the massless labels are a direction and a half-integer, and that is the smallest label set in the block.

## Summary

The stabiliser of a null momentum is generated by $J_z$ and the two null rotations $T_1=K_x-J_y$ and $T_2=K_y+J_x$, with brackets $[T_1,T_2]=0$, $[J_z,T_1]=T_2$ and $[J_z,T_2]=-T_1$ — the algebra of $E(2)$, verified in the block's matrix model together with the fixing of the momentum by all three generators. The finite-dimensional unitary representations are one-dimensional, with the translations acting trivially and the rotation acting by $e^{ih\theta_{\mathrm{axr}}}$, and $h$ is the helicity, invariant under the whole Lorentz group. The triviality of the null rotations is the fixing condition that removes the longitudinal mode, which is why a massless spin-1 particle has two helicities and not three. The alternative, with the null rotations acting nontrivially, is the continuous-spin family: unitary, unobserved, and necessary for the classification to be complete.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P_0=\tfrac{mc}{2}(e_t+i\vec e_z)$ | the standard null momentum |
| $T_1=K_x-J_y$, $T_2=K_y+J_x$ | the null rotations |
| $J_z$ | the rotation about the momentum |
| $h$ | the helicity |
| $D_h$ | the one-dimensional little-group representation |
| continuous spin | the family with $T_{1,2}$ acting nontrivially |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* 40 (1939) 149 — the null orbit and the $E(2)$ little group.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.5 — the null little group, the helicity and the gauge argument.
- L. H. Ryder, *Quantum Field Theory*, 2nd ed., Cambridge University Press, 1996, chapter 2 — the little groups worked out for the massive and massless cases side by side.
- V. Bargmann and E. P. Wigner, "Group theoretical discussion of relativistic wave equations", *Proceedings of the National Academy of Sciences* 34 (1948) 211 — the continuous-spin representations and their field equations.
- *The Little Group of a Massive Particle: $\mathrm{SU}(2)$* — the compact case this article contrasts with.
- *The Null Cone: The Massless Boundary* — the orbit and the growth of the little group at the boundary.
