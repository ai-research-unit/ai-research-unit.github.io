# __Length Contraction and Time Dilation: Projections, Not Deformations__

## Introduction

A moving rod is shorter and a moving clock is slow. Both statements are true, and both are statements about a comparison between two frames and not about a change in the object. Nothing acts on the rod, no force compresses it, and its own length is exactly what it was. The contraction is a statement about which pairs of events an observer calls simultaneous, and the dilation is the same statement read on the time axis.

This article states the two effects, gives their measurement protocols, explains why they are not deformations, writes the invariant reading that replaces them, and resolves the three standard pseudo-paradoxes.

The article assumes *The Lorentz Transformation as a Biquaternionic Rotation* for the transformation, *The Cartan Decomposition: Every Lorentz Transformation as a Boost and a Rotation* for the frame, *The Rest Frame and the Exceptional Point* for the rest frame, and *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* for the velocity picture.

## The Two Effects

### The Definitions

- **Length contraction**: a rod of proper length $L_0$ has length $L_0/\gamma$ in a frame in which it moves with speed $\beta c$ along its axis.
- **Time dilation**: a clock's proper interval $\Delta_\Phi\tau$ is observed as $\Delta t=\gamma\Delta_\Phi\tau$ in a frame in which it moves with speed $\beta c$.

Both use $\gamma=(1-\beta^{2})^{-1/2}$.

### The Formulae

$$
L=\frac{L_0}{\gamma}=L_0\sqrt{1-\beta^{2}},
\qquad
\Delta t=\gamma\,\Delta_\Phi\tau=\frac{\Delta_\Phi\tau}{\sqrt{1-\beta^{2}}} .
$$

The two factors are reciprocal, and that reciprocity is the reason the effects look paradoxical when they are stated without their protocols.

### The Numbers

| $\beta$ | $\gamma$ | a $10$ m rod | a $2.2$ µs lifetime |
|---|---|---|---|
| $0.6$ | $1.25$ | $8$ m | $2.75$ µs |
| $0.8$ | $1.667$ | $6$ m | $3.67$ µs |
| $0.999$ | $22.366$ | $0.447$ m | $49.21$ µs |

The last row is the muon: a lifetime of $2.2$ µs becomes $49.21$ µs, and at $\beta=0.999$ that is a flight distance of $14.7$ km, which is why cosmic-ray muons reach the ground.

### The Common Reading

The common reading is that the rod "is compressed" and the clock "runs slow". Both readings are pictures, and both are misleading in the same way: they attach the effect to the object rather than to the frame. The rest of this article replaces them.

## Length Contraction

### The Protocol

To measure the length of a moving rod, an observer marks the positions of the two ends **at the same time in the observer's frame**, and measures the distance between the marks. That is the whole protocol, and the phrase "at the same time" is its content.

### The Result

Let the rod be at rest in $S'$ with ends at $x'=0$ and $x'=L_0$, and let $S'$ move at $\beta$ along $+x$ relative to $S$. The transformation is

$$
x=\gamma(x'+\beta c\,t'),\qquad t=\gamma\bigl(t'+\beta x'/c\bigr).
$$

The observer in $S$ takes the two ends at the same $t$, which is **not** the same $t'$:

$$
\Delta t=0\ \Longrightarrow\ \Delta t'=-\beta\,\Delta x'/c,
$$

and substituting,

$$
L=\Delta x=\gamma\bigl(\Delta x'+\beta c\,\Delta t'\bigr)=\gamma\bigl(L_0-\beta^{2}L_0\bigr)=\frac{L_0}{\gamma}.
$$

So the factor $1/\gamma$ comes out of the simultaneity condition, and it comes out as $1-\beta^{2}$ times $\gamma$, which is exactly $1/\gamma$.

### What Contracts

The rod's proper length does not contract: measured in $S'$, the endpoints are still $L_0$ apart. What changes is the *set of event pairs* that the observer in $S$ compares. The rod's world-sheet is a two-dimensional strip; the $S$-observer's simultaneity slice cuts it along a segment of length $L_0/\gamma$, and the $S'$-observer's slice cuts it along a segment of length $L_0$.

So the contraction is a statement about the slope of the slice and not about the width of the strip.

### Why the Transverse Directions Do Not Contract

A rod perpendicular to the motion has the same length in both frames, because the transformation leaves the transverse coordinates alone. That asymmetry is what makes the effect a contraction along the motion and not a scale transformation of space: a scale transformation would shrink all three directions.

## Time Dilation

### The Time-Dilation Protocol

To compare two clocks, one takes a clock at rest in $S'$ and reads it at two events on its world-line, and one compares with clocks of $S$ that are **synchronised in $S$**. The moving clock's readings are compared with two different $S$-clocks, one at each event.

### The Time-Dilation Result

With the clock at rest in $S'$ at $x'=0$,

$$
\Delta t=\gamma\Delta t',
$$

so the moving clock records less time between the two events than the $S$-clocks do. The factor is $\gamma>1$, and it is the same $\gamma$ as before.

### What Dilates

Nothing dilates in the clock. The clock's proper interval is a single number, the length of its world-line, and it is the same number computed in any frame. What differs is the *projection* of that world-line onto the frame's time axis: a tilted world-line has a longer time coordinate between its endpoints than its proper length, by exactly the factor $\gamma$.

### The Reciprocity

$S'$'s observer says the $S$-clocks are slow, and both are right, because each compares with a different pair of the other's clocks. There is no contradiction: the two statements are about different pairs of events, and the difference between the pairs is the relativity of simultaneity.

## Why Not a Deformation

### The Object and the Frame

A deformation is a change in an object caused by something acting on it: a stress, a temperature, a field. Length contraction has no cause of that kind. It happens to a rod that is untouched, and it happens to a single electron, which has no structure to deform.

So the word "contraction" is a name for a coordinate effect and not for a physical process. The rod's proper length is a Lorentz scalar; the coordinate length is not.

### The Invariant Length

The invariant statement is

$$
L_0^{2}=\bigl(\Delta x\bigr)^{2}\ \text{in the rest frame},
$$

i.e. the proper length is the interval between the endpoints' world-lines measured on a slice orthogonal to them. In any frame,

$$
L_0=\gamma L
$$

with $L$ the coordinate length. So the pair $(L,\beta)$ has one invariant, $L_0$, and the contraction is the statement that $L$ and $\gamma$ move together.

### The Fluid Analogy

A useful contrast: a fluid's density does change when it is compressed, and the change is accompanied by a stress and by work done. The relativistic length contraction has no stress and does no work. A rod that is accelerated to a new speed and then measured has its proper length unchanged (if the acceleration is applied uniformly in its own frame) or changed (if applied otherwise) — and the change in the second case is a real deformation, physically distinct from the contraction.

That distinction is the sharpest statement of the article's title: contraction is not a deformation, and the deformations that acceleration can cause are a different phenomenon.

### The Failure of the "Compression" Picture

If the contraction were a compression, the rod would have to be compressed *more* the faster it moves, in every frame at once, and by a different amount in each — which is not a state any material can be in. The picture fails because it attributes a frame-dependent quantity to the object.

## The Measurement Protocols

### The Two Measurements of Length

There are two ways to measure a moving rod's length, and they are different measurements:

- **Simultaneous marking**: mark both ends at one time of the observer's frame. This gives $L_0/\gamma$ and it is the coordinate length.
- **Photography**: record the light arriving at one time at the camera. This gives the *apparent* shape, and for a rod it is not a contraction at all but a rotation, because the light from the far end left earlier and the rod has moved in the meantime.

The two answers differ and neither is wrong. The photographic image of a moving object is rotated, not squeezed, and the rotation is the Terrell–Penrose effect; a sphere photographs as a sphere. A reader who mixes the two gets the confusion that the literature calls the "length paradox", in which an object seems simultaneously contracted and not.

### The Two Measurements of Time

Similarly, there are two ways to compare rates:

- **One clock against many**: compare the moving clock with a lattice of synchronised clocks. This gives dilation by $\gamma$, and it is a statement about one frame's coordinate time.
- **Two clocks passing each other**: read both dials at the crossing events. This is symmetric, and each observer sees the other's dial lag by the same factor.

The first is a comparison of a proper time with a coordinate time; the second is a comparison of two proper times at two events. They agree when the protocols are kept apart, and the apparent conflict between them is the reciprocity of the dilation.

### The Simultaneity

Everything above is the relativity of simultaneity in disguise. The Lorentz transformation mixes $x$ and $t$, and the mixing is what makes "the same time" frame-dependent. A frame is a choice of simultaneity slices, and the contraction and dilation are the two ways that choice shows up.

## The Invariant Reading

### The Proper Interval

The invariant object is the interval

$$
s^{2}=t^{2}-x^{2}
$$

(with lengths in units of $c$ times a time and velocities in units of $c$), and every frame computes the same value. The proper length and the proper time are the interval evaluated on the appropriate slice, and the coordinate length and coordinate time are its projections.

### The Proper Time

Along a timelike world-line the invariant is

$$
\tau=\int\sqrt{1-\beta^{2}(t)}\,dt ,
$$

which is the proper time. It is maximal for the straight world-line between two events — the twin paradox's content — and the dilation is the statement that any other world-line is shorter.

### The Algebra's Version

In the block's algebra the transformation is the congruence by a unit-norm element, and the two effects are read from the boost's action on the frame:

$$
\tilde X\longmapsto\mathrm{Cg}_{\tilde U}(\tilde X),
\qquad
N\bigl(\mathrm{Cg}_{\tilde U}(\tilde X)\bigr)=N(\tilde X),
$$

because the congruence preserves the norm exactly. So the invariant statement is the algebra's multiplicativity of the norm, and the "contraction" and "dilation" are the two components of the transformed element's coordinate decomposition. That is the algebraic reason the effects cannot be deformations: the norm is preserved by construction, and only the coordinates move.

### The Reading

The physical interpretation is that a frame is a coordinatisation and the effects are coordinate effects. The invariant content is the interval, the proper time and the proper length; everything else is bookkeeping.

## The Pseudo-Paradoxes

### The Pole and the Barn

A pole of proper length $10$ m moves at $\beta=0.8$ through a barn of proper length $6$ m with doors at both ends. In the barn's frame the pole is $6$ m long and fits exactly. In the pole's frame the barn is $3.6$ m long and the pole does not fit at all.

There is no contradiction, and the resolution is the order of the door events. In the barn's frame both doors are shut at one moment; in the pole's frame the far door is shut and opened before the near door is shut. The two frames disagree about which events are simultaneous, and "both doors are shut at once" is a frame-dependent statement.

The numbers: $\gamma=5/3$ at $\beta=0.8$, $10/\gamma=6$ and $6/\gamma=3.6$, both exact.

### The Twin Paradox

One twin travels and returns younger. The asymmetry is that only one twin accelerates, so only one world-line is bent; the proper time is the integral of $\sqrt{1-\beta^{2}}dt$ along each world-line, and the bent one is shorter.

The "paradox" arises from applying the dilation formula symmetrically: each twin sees the other's clock slow. That is correct while both are inertial, and the traveller's change of frame is what makes the comparison non-symmetric at the end. There is no frame in which the traveller ages more.

### The Bell Ships

Two ships accelerate identically, separated by a fixed proper distance in the original frame. In the original frame the distance between them stays constant, so a string joining them should not be stressed — yet the string breaks.

It breaks because the ships' *proper* separation grows: the constant-distance condition in the original frame means the separation in the ships' instantaneous rest frames grows by $\gamma$. So the string's proper length is stretched, and the stretch is a real deformation with a real stress. It is the one case in this article where a rod is genuinely deformed, and the deformation is caused by the acceleration protocol and not by the Lorentz contraction.

So the Bell ships are the exception that proves the rule: contraction alone does no work, and the work comes from the differing accelerations.

## Summary

A moving rod has coordinate length $L_0/\gamma$ and a moving clock has coordinate rate $1/\gamma$, both because the Lorentz transformation mixes space and time and both are statements about a frame's simultaneity slices. The rod's proper length and the clock's proper time are invariants, unchanged by the motion, and the congruence preserves the interval exactly. The effects are therefore coordinate effects and not deformations: no stress, no work, no change in the object. The protocols matter — simultaneous marking and transit timing give reciprocal answers — and the three standard pseudo-paradoxes are resolved by the relativity of simultaneity except the Bell ships, where a genuine deformation is caused by the acceleration protocol rather than by the contraction.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\beta$ | speed in units of $c$ |
| $\gamma=(1-\beta^{2})^{-1/2}$ | the Lorentz factor |
| $L_0$, $L$ | proper and coordinate length |
| $\Delta_\Phi\tau$, $\Delta t$ | proper and coordinate time |
| $s^{2}=t^{2}-x^{2}$ | the interval |
| $\mathrm{Cg}_{\tilde U}$ | the congruence, which preserves $N$ |

## Further Reading

- W. Rindler, *Relativity: Special, General, and Cosmological*, 2nd ed., Oxford University Press, 2006, chapters 2 and 3 — the two effects with their protocols stated carefully.
- E. F. Taylor and J. A. Wheeler, *Spacetime Physics*, 2nd ed., Freeman, 1992 — the ladder-and-barn and the muon, with the measurement protocols.
- J. S. Bell, "How to teach special relativity", in *Speakable and Unspeakable in Quantum Mechanics*, Cambridge University Press, 1987 — the accelerating ships and the stretched string.
- H. Reichenbach, *The Philosophy of Space and Time*, Dover, 1958 — simultaneity as a convention and the coordinate character of the contraction.
- *The Lorentz Transformation as a Biquaternionic Rotation* — the transformation whose coordinate effects these are.
- *The Rest Frame and the Exceptional Point* — the frame in which the proper quantities are read off.
