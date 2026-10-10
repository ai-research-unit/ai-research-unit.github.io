# __Each Sector Is the Other's Clock: the Sector Exchange as Relational Time__

## Introduction

The framework has no external time parameter. The material time is the imaginary coefficient $ict$ of an element of the anti-Hermitian sector $\mathbb{M}_-$, the informational time is the real coefficient $ct'$ of an element of the Hermitian sector $\mathbb{M}_+$, and multiplication by the central imaginary $i$ exchanges the two sectors. The exchange is therefore an operation of the algebra on the two times, and the question of this article is what that operation is worth as a **clock**.

The answer, in one sentence: the exchange supplies the reference of a clock and its period, and it supplies neither the arrow nor the rate. The three readings that follow from that sentence are these. The two times are the real and the imaginary parts of one central coordinate, so the material time is not defined against anything outside the algebra but against the phase of the informational sector — each sector is the other's clock. The exchange is a quarter turn of the plane of that coordinate, so a tick is a quarter turn and the period of the clock is a full central rotation. And the exchange is invertible and of order four, so the algebra offers both senses of the rotation and no rule that selects one; the direction of the tick remains a choice of slice, which is the framework's problem of time.

The article is kinematic throughout. It reads the central map that *Conventions in the Biquaternion Universe* identifies as one generator on remarkable subspaces, and it reads it on the one carrier that is a time. What it adds to that map is the clock, the reference that the clock supplies, and the exact statement of what a clock needs and does not get.

## The Two Times in One Plane

The conventions are those of the series. The algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ and $e_1^2 = e_2^2 = e_3^2 = -e_0$; the conjugations are the quaternion conjugation ${}^{\natural}$, the complex conjugation $\bar{\cdot}$, and the adjoint ${}^{*} = {}^{\natural}\circ\bar{\cdot}$.

The two sectors are the two halves of the algebra under the adjoint,

$$
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\}, \qquad \mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\},
$$

the anti-Hermitian material sector and the Hermitian informational sector. In coordinates,

$$
\tilde{Q}_- = ict\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 \in \mathbb{M}_-, \qquad \tilde{Q}_+ = ct'\,e_0 + i\bigl(x'e_1 + y'e_2 + z'e_3\bigr) \in \mathbb{M}_+,
$$

with $t, \mathbf{x}, t', \mathbf{x}'$ real. The verification of the two inclusions is the pair of computations in *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, and the reading of the coefficients is the $ict$ dictionary of *Conventions in the Biquaternion Universe*.

The centre of the algebra is $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$, and it is the complex time sector of *Other Remarkable Subspaces*. The two times are its two real coordinates: writing

$$
z = ct' + i\,ct,
$$

the centre is the complex plane of the coordinate $z$, the informational time is the real part of $z$ and the material time is $i$ times its imaginary part. This is the sense in which the framework has no external parameter: both times are coordinates of elements, and there is no slot outside the algebra for a parametric time to occupy. The plane is also the plane in which the global phase acts: the one-parameter group of the centre is $e^{i\theta}e_0$, and its action on $z$ is the rotation of the plane.

## The Exchange as a Quarter Turn

Multiplication by the central imaginary is the map of the algebra that exchanges the two sectors. On a material element, using $\bar{i} = -i$ and $\tilde{Q}_-^{*} = -\tilde{Q}_-$,

$$
(i\tilde{Q}_-)^{*} = \bar{i}\,\tilde{Q}_-^{*} = (-i)(-\tilde{Q}_-) = i\tilde{Q}_- ,
$$

so $i\tilde{Q}_- \in \mathbb{M}_+$, and the same computation run backwards sends $\mathbb{M}_+$ to $\mathbb{M}_-$. In coordinates the exchange is

$$
i\bigl(ict\,e_0 + \mathbf{x}\bigr) = -ct\,e_0 + i\mathbf{x} \in \mathbb{M}_+, \qquad i\bigl(ct'\,e_0 + i\mathbf{x}'\bigr) = ict'\,e_0 - \mathbf{x}' \in \mathbb{M}_- .
$$

Read on the coefficients, the material element $(t, \mathbf{x})$ is carried to the informational element $(t' = -t,\ \mathbf{x}' = \mathbf{x})$, and the informational element $(t', \mathbf{x}')$ is carried to the material element $(t = t',\ \mathbf{x} = -\mathbf{x}')$. The two times therefore exchange roles, with the sign that a quarter turn carries, and the two spaces exchange roles in the same movement. On the central coordinate the exchange is one application of the generator,

$$
z \mapsto i z = -ct + i\,ct' ,
$$

which is the quarter turn of the complex time plane: the informational time becomes the material coordinate, and the material time becomes minus the informational one.

Two properties of the map fix what a clock built on it can be. The first is the order. The square of the generator is $-e_0$, the antipodal map of the plane and not the identity, and the fourth power is $e_0$; the orbit of a central coordinate under the generator is therefore the four-element cycle

$$
z \ \longrightarrow\ iz \ \longrightarrow\ -z \ \longrightarrow\ -iz \ \longrightarrow\ z .
$$

The second is invertibility: the generator is a rotation, so both senses are available, $e^{i\theta}$ and $e^{-i\theta}$, and the algebra contains no element that prefers one. Both properties are stated, with the other five restrictions of the same map, in *Conventions in the Biquaternion Universe*.

## The Clock Hand and Its Two Projections

A clock assigns a coordinate to an event by a repeatable motion. The framework's clock is the central coordinate itself, and its reading is a phase.

**The hand.** The hand of the clock is the complex number $z = ct' + i\,ct$ of the centre. Its magnitude and its phase are the two data the central plane carries, and its phase $\theta = \arg z$ is the reading: the material time and the informational time are the two projections of the hand,

$$
ct' = \lvert z\rvert\cos\theta, \qquad ct = \lvert z\rvert\sin\theta .
$$

The one-parameter group $e^{i\theta}e_0$ is the continuous motion of the hand, and the generator is its infinitesimal element. Read this way the global phase is not an auxiliary factor of the amplitude; it is the clock coordinate of the central plane, and the amplitude factor $e^{iS/\hbar}$ of the action articles is the same central phase read on a dynamics.

**The tick.** A tick of the clock is a quarter turn of the hand, the application of the generator. The four quarter turns are the identity, the exchange, the antipodal map and the inverse exchange,

$$
e_0 \ \text{(no tick)}, \qquad i e_0 \ \text{(the exchange)}, \qquad -e_0 \ \text{(the antipodal map)}, \qquad -i e_0 \ \text{(the inverse exchange)} ,
$$

and the period is the full rotation $2\pi$, made of four quarter turns. The four-element cycle is the whole of the clock's internal structure, and it is exact: no approximation enters, because the orbit is the orbit of a central element under a group of order four.

**Why each sector is the other's clock.** The two sector times are the two projections of one hand. The material time $ict$ is the component of the hand along the direction the informational time does not use, and conversely. A sector taken alone therefore has no time coordinate that is not a reading of the other sector's plane: the material time is defined by the angle between the hand and the informational axis, and the informational time by the angle between the hand and the material axis. This is the precise sense of the title. It is not a figure of speech: the two times are the same number read as a real and as an imaginary coefficient, and the exchange is the rotation that moves one reading into the other.

## What a Clock Needs

A clock, whether mechanical or algebraic, needs four things, and the framework's clock has two of them. The table states the accounting; the sections that follow read the two entries that are missing.

| What a clock needs | What the framework supplies |
|---|---|
| A **reference**: a direction or a subsystem against which the reading is defined | Supplied. The other sector: the material time is read against the informational axis and the reverse |
| A **period**: a repeatable tick | Supplied up to scale. The central rotation, $e^{i\theta}e_0$ with $\theta = 2\pi$ the identity, divided into four quarter turns; the period is an angle and carries no duration |
| An **arrow**: an orientation of the tick | Not supplied. The generator is invertible of order four, and $e^{i\theta}$ and $e^{-i\theta}$ are both in the algebra |
| A **rate**: a duration per tick | Not supplied. The algebra carries the phase, which is dimensionless, and no second |

**The missing arrow.** The generator is a rotation, so it is invertible, and the inverse rotation is as much an element of the algebra as the rotation itself. The exchange therefore carries no orientation: it identifies the two times and does not order them. This is the same statement that *Conventions in the Biquaternion Universe* makes in the form that the algebra offers the rotation between the two times and no rule that selects one, and it is the framework's problem of time in its kinematic form. The selection of a slice is a choice of frame, and the framework says so rather than deriving it.

**The missing rate.** The clock of the framework is angle-keeping and not duration-keeping. Its period is the full central rotation, which is the same for every element and every frame because the generator is central; nothing in the algebra attaches a physical duration to it. A physical duration enters only when a physical process is compared with the central phase, and that comparison is a dynamics; it is not a property of the exchange.

## The Relational Reading

The two entries that are supplied are what makes the reading relational, and the reading is worth separating from the two that are not.

**The time is a relation between two sectors.** The material sector alone has no time coordinate that is not a reading of the informational plane, and the informational sector alone has none that is not a reading of the material plane. Time is therefore not an absolute coordinate attached to the framework from outside, and it is not a coordinate internal to one sector either: it is a relation between the two real forms of one algebra, carried by a hand that both sectors project. This is the framework's version of the relational reading of time, and it is exact rather than formal, because the relation is a specified map of a specified algebra and the projections are its coordinates.

**The reference is global.** The generator is central, so the exchange is the same operation at every element, in every subspace and in every frame. The clock it defines is therefore a **global** clock: it supplies one reference for the whole algebra and not one reference per point. The framework is accordingly a theory with a global internal clock and no local clock of its own; local clocks, their transport, their relative rates and their synchronisation are the business of *The Relativistic Exchange of Information and Clock Synchronisation in Biquaternionic Form*, which builds them from null displacements, the radar method and the $k$-factor. The division is clean: this article supplies the reference that a clock needs and that the synchronisation article presupposes, and that article supplies the rates that this one does not.

**The other reading of the same exchange.** The exchange has a second physical reading, in the informational direction rather than the temporal one: it carries the material ledger of an element to the informational ledger, and the two ledgers are the two biquaternion norms. That reading is *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*. The clock reading and the thermodynamic reading are readings of the same map on different carriers, which is the rule of *Conventions in the Biquaternion Universe*: one map, and a physical word for each carrier.

**The boundary with the boosts.** The phase and the relativistic generators are carried by two separate parts of one element: the generator is a *scalar*, acting through the centre, and the boosts act through the quaternion directions. The clock of this article is therefore a clock of the scalar (temporal) part of an element and says nothing about spatial directions; it times the element and does not move it. This is why the exchange is not a boost and why the clock reading adds nothing to the transformation theory of the material sector.

## What the Reading Does Not Claim

- It is **not a dynamics**. No evolution equation is read off the exchange, and no rate of change of a state follows from it. The exchange is a relation between two descriptions of one element, and a dynamics is a separate object, which is the constraint analysis the framework names as missing.
- It is **not an arrow**. The generator is invertible and of order four, so both orientations are present and neither is selected; the direction of the tick is a choice of slice, and the problem of time is not solved here but restated in the temporal reading.
- It is **not a rate or a duration**. The period of the clock is the central rotation, an angle without a second; a physical duration requires a process to compare with it, and no such comparison is made here.
- It does **not identify the exchange with the analytic continuation**. The Wick rotation as the continuation $t\mapsto-i\tau$ is a relabeling of one coordinate that holds the space real; the exchange is a rotation of the element that carries the space imaginary, and the two agree on the time axis and in the sign they flip and nowhere else, as *Conventions in the Biquaternion Universe* states. The clock reading uses the rotation and not the continuation.
- It does **not claim an empirical consequence**. It reorganizes the exchange, the phase and the two times under one reading; it adds no prediction and no coupling, and it does not turn the phase into a measurable duration.

## Summary

The central imaginary generates a quarter turn of the complex time plane, $z = ct' + i\,ct \mapsto iz = -ct + i\,ct'$, and the two sector times are the two projections of the hand that this rotation moves. A material time and an informational time are therefore never read in isolation: each is read against the axis of the other sector, and that is the sense in which each sector is the other's clock. The clock's structure is the four-element orbit of the generator — no tick, the exchange, the antipodal map, the inverse exchange — with the period $2\pi$ of the central rotation, and it is exact, global, and central.

The accounting of a clock is partial, and the two missing entries are the ones the framework is explicit about. The exchange supplies the reference and the period, and it supplies neither the arrow, the generator being invertible of order four, nor the rate, the phase being dimensionless. The relational content is thus real and the dynamical content is absent: the framework has an internal relational time in the kinematic sense, with the orientation of the tick and the duration of the tick still to be supplied, and the first of the two is the problem of time in its kinematic form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | the basis, $e_1^2 = e_2^2 = e_3^2 = -e_0$ |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | quaternion conjugation, complex conjugation, adjoint $= {}^{\natural}\circ\bar{\cdot}$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | the material (anti-Hermitian) and informational (Hermitian) sectors |
| $i$ | the central imaginary, $i\,e_0$; the generator of the exchange |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | the centre, the complex time plane |
| $z = ct' + i\,ct$ | the clock hand; the central coordinate of an element |
| $ct'$, $ict$ | the informational and the material time, the two projections of the hand |
| $e^{i\theta}e_0$ | the one-parameter group of the centre, the motion of the hand |
| $i\mathbb{M}_\pm = \mathbb{M}_\mp$ | the sector exchange, the quarter turn, the tick |

## Further Reading

- *Conventions in the Biquaternion Universe* — the basis, the conjugations, the remarkable subspaces, the $ict$ dictionary, the four forms, and the exchange read on the metric.
- *Conventions in the Biquaternion Universe* — the one generator, its restrictions, the complex time plane, the order four of the rotation, and the statement that the algebra offers no rule that selects a slice.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the two sectors the exchange relates, and the coefficient dictionaries used above.
- *Other Remarkable Subspaces* — the complex time sector, the complex space sector, the real and imaginary sectors, and the exchange of the real and imaginary sectors as the Wick rotation.
- *The Relativistic Exchange of Information and Clock Synchronisation in Biquaternionic Form* — signals as null displacements, the radar method, Einstein synchronisation, the $k$-factor, clock transport and the twin effect: the local clocks, their rates and their synchronisation.
- *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* — the same exchange read on the informational direction, with the two biquaternion norms as the two ledgers.
- *The Schrödinger Equation in Biquaternionic Form* — the kinematic sector equation that a rate of change of an informational state requires, and the place a physical duration enters the framework.
- Carlo Rovelli, *Quantum Gravity*, Cambridge University Press, 2004 — the relational reading of time and the problem of time in the canonical theory.
- Don N. Page and William K. Wootters, *Evolution without evolution: dynamics described by stationary observables*, Physical Review D **27** (1983) 2885 — a clock subsystem as the reference of time in a stationary description.
