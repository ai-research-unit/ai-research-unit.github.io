# __The Temporal Dimension: Why the Temporal Unit Is the Identity__

## Introduction

The base of the biquaternion algebra is written

$$
e_t = 1, \qquad \vec e_x, \qquad \vec e_y, \qquad \vec e_z,
$$

and the three vector units satisfy $\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t$, with $\vec e_x\vec e_y = \vec e_z$ and its cyclic companions. One of the four units is therefore unlike the other three: it is the identity, it squares to itself, and it commutes with everything, while the three vector units anticommute with one another and each squares to the negative of the first.

The question of this article is what that asymmetry **means**. Is $e_t = 1$ a harmless choice of notation, a name given to the identity for bookkeeping, or is it a statement about the temporal dimension itself? The answer the corpus takes is the second. In the biquaternion framework the temporal direction is the **scalar** direction, and $e_t = 1$ is the algebraic expression of that fact. Time is the dimension along which the algebra multiplies an element without turning it.

The article reads the consequence twice. Read on the **material** sector, where the biquaternion is the four-position of a relativistic system, the temporal coefficient is imaginary — it is $ict'$ — and the imaginary unit is what makes time a coordinate that is measured but not touched. Read on the **informational** sector, where the biquaternion is an observable or a state, the temporal coefficient is real — it is $ct$ — and this article proposes the reading that the real temporal coefficient of the informational sector is its **storage direction**: the record can be touched and recovered because $ct$ is real, and the time cannot because $ict'$ is imaginary.

The two halves of the article are of different standing, and the difference is kept throughout. The algebraic facts — that $e_t$ is the identity, that the temporal direction is the centre, that the material coefficient is imaginary and the informational one real — are established and are verified in the companion articles. The material reading is the interpretation already recorded in *The Material Sector: Four-Vectors, Interval and Lorentz Action*. The **storage reading** of $ct$ is an interpretation offered here, subject to the standing hypothesis that the informational sector is physically realised, and it is stated as a reading and not as a result.

The conventions are those of the series. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ and $\vec e_k^2 = -e_t$; the conjugations are the complex conjugation $\bar{\cdot}$, the quaternion conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and the anti-Hermitian conjugation ${}^{\flat} = -{}^{*}$. The biquaternionic gradient is $\tilde{\nabla} = \sum_{\mu\in\{t,x,y,z\}} e_\mu\,\partial/\partial Q_\mu$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$.

## The Unit That Is the Identity

Three properties single out $e_t$ among the four basis units. The third is the one the physics of the following sections reads.

**It is the identity.** For every element $\tilde Q$ of the algebra,

$$
e_t\,\tilde Q = \tilde Q\,e_t = \tilde Q .
$$

Multiplication by $e_t$ is the operation that does nothing. The temporal unit is the unit of the algebra in the strict sense: it is the neutral element of the product, and every other unit is a departure from it.

**It is fixed by the natural, complex and Hermitian conjugations.** The natural, complex and Hermitian conjugations all leave $e_t$ alone,

$$
e_t^{\natural} = \bar{e_t} = e_t^{*} = e_t ,
$$

while each of the three vector units changes sign under the natural conjugation, $\vec e_k^{\natural} = -\vec e_k$. The temporal direction is the direction fixed by the natural, complex and Hermitian conjugations. Only the anti-Hermitian conjugation $\flat = -{}^{*}$ negates $e_t$, $e_t^{\flat} = -e_t$, while fixing the three vector units.

**It is the direction the rotations fix and the boosts move.** The Lorentz action is rotor conjugation, $\tilde Q \mapsto \tilde U\tilde Q\tilde U^{*}$ for $\tilde U$ in the norm-one group $\mathbb{B}^\times_1 = \{\tilde U : \langle\tilde U\rangle_{\natural} = e_t\}$. A **rotation** is a unit real quaternion, an element of $Sp(1) \subset \mathbb{B}^\times_1$, and it fixes the temporal unit,

$$
\tilde u\,e_t\,\tilde u^{*} = e_t ,
$$

because $e_t$ is central and a unit real quaternion has $\tilde u^{*} = \tilde u^{\natural} = \tilde u^{-1}$; a rotation moves the three vector units among themselves and leaves $e_t$ where it is. A **boost** is the other kind of rotor, and on the temporal unit it is not trivial. A pure boost of rapidity $\psi$ along the unit real vector $\vec u$ is $B(\psi,\vec u) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec u$, and on the temporal unit it acts as

$$
B\,e_t\,B^{*} = \cosh\psi\,e_t + i\sinh\psi\,\vec u \in \mathbb{M}_+ ,
$$

which is Hermitian of unit biquaternion norm: the boost carries the unit out of the centre and into the informational sector. The temporal direction is therefore fixed by the rotations and moved by the boosts, and it is the axis the rotations share. The boost does not exchange $e_t$ for one of the vector units; it mixes the temporal direction with a spatial one, and that mixing is what makes the temporal direction a coordinate of the element rather than a parameter outside the algebra.

The algebraic content of the three properties is one statement: **$e_t$ spans the real line in the centre of the algebra.** The centre of $\mathbb{B}$ is the complex plane

$$
\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\} = \{Q_t\,e_t : Q_t \in \mathbb{C}\},
$$

which *Conventions in the Biquaternion Universe* calls the complex time sector and *The Biquaternion Space, the Group of Involutions and the Six Subspaces* lists among the remarkable subspaces. The centre is the set of elements that commute with the whole algebra, its real direction is $e_t$, and its complex coordinate is the one the next sections read. The temporal dimension, in this framework, is not one of four peers; it is the direction along which the element is a **scalar**, the direction every rotation fixes.

## What $e_t = 1$ Says About Time

Four consequences follow from the identification, and they are the article's algebraic content.

**1. The scalar part of an element is its temporal coefficient.** For a general element $\tilde Q = Q_t e_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$, the scalar part is $\mathrm{Sc}(\tilde Q) = Q_t$. Asking for the time coordinate of a biquaternion is asking for its scalar part; the two questions are the same. The three vector directions are the non-scalar part, and it is exactly the part the vector units generate.

**2. The temporal unit is the axis the rotations share and the direction the boosts mix.** The rotation part of the Lorentz group fixes $e_t$ and acts on the three vector units; the boost part moves $e_t$ into the informational sector, through the imaginary structure of the temporal coefficient. The Lorentz group therefore does not leave the temporal direction alone: the rotations fix it, and the boosts mix it with a chosen spatial one. No other unit of the basis is fixed by the rotations. Both facts are read off the same element $e_t = 1$: it is central, so a rotation cannot move it, and its complex coefficient is what a boost mixes.

**3. The temporal coefficient is not itself invariant; the norm is.** The Lorentz action preserves the biquaternion norm,

$$
\boxed{\;\bigl\langle \tilde U\tilde Q_3\tilde U^{*} \bigr\rangle_{\natural} = \langle \tilde Q_3\rangle_{\natural}\;},
$$

so the invariant the action carries is the norm $\sum_\mu Q_\mu^2$ and not the temporal coefficient. A boost changes the temporal coefficient $Q_t$ by mixing it with the spatial ones, which is what a Lorentz transformation of a four-vector does. The temporal coordinate is a coordinate, and it transforms; the interval built from the four coefficients is what stays.

**4. The signature is carried by the coefficients and not by the units.** The biquaternion norm is

$$
\langle\tilde Q\rangle_{\natural} = \tilde Q\tilde Q^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 ,
$$

a sum of four squares of the complex coefficients, with no modulus taken and no sign inserted. Every term enters with the same sign, and the signature of the norm is not put in by hand: it comes from the values of the four complex coefficients. The temporal term enters as $Q_t^2$ and the spatial ones as $Q_k^2$, and the difference between them — the Lorentzian signature — is carried entirely by the **coefficients**. The unit $e_t = 1$ contributes the square $Q_t^2$; the units $\vec e_k$ contribute $Q_k^2$.

The four statements are one statement: **time is the scalar dimension.** It is the direction of the identity, the direction whose coefficient is the scalar part of the element, the direction the rotations fix and the boosts mix with space; and what the action carries is the norm of the four coefficients, while what carries the signature is the value placed on the temporal coefficient.

## The Material Reading: Time Is Imaginary

The material sector is the fixed space of the anti-Hermitian conjugation, $\mathbb{M}_- = \{\tilde Q : \tilde Q^{\flat} = \tilde Q\}$, and its general element is the four-position of a relativistic system,

$$
\tilde Q_- = ict'\,e_t + x\,\vec e_x + y\,\vec e_y + z\,\vec e_z \in \mathbb{M}_- ,
$$

with $t', x, y, z$ real. This is the $ict'$ dictionary of *Conventions in the Biquaternion Universe* and of *Why Complexify Spacetime?*: the temporal coefficient is $ict'$, purely imaginary, and the three spatial coefficients are real.

Two features of the placement carry the physical reading.

**The imaginary unit on the time coordinate produces the signature.** The norm of the material element is

$$
\boxed{\;\langle\tilde Q_-\rangle_{\natural} = (ict')^2 + x^2 + y^2 + z^2 = -c^2{t'}^2 + x^2 + y^2 + z^2\;},
$$

the Minkowski interval. The minus sign is not inserted into a metric: it is $i^2$, the square of the coefficient the time direction carries. In the framework the signature is algebraic, and it is the imaginary character of the temporal coefficient that carries it. This is the content of the $ict'$ convention that *Why Complexify Spacetime?* records: the geometry says *what* the interval is, and the placement of the $i$ says *why*.

**The real part of the element is the spatial part.** The material element is imaginary in its scalar coefficient and real in its three vector coefficients. The real coordinates are the three spatial ones; the one imaginary coordinate is time.

This is the mirror, in the material sector, of the statement that time is the scalar dimension. The material element is anti-Hermitian, so the conjugation forces its scalar coefficient to be imaginary and its three vector coefficients to be real. Read on the temporal coordinate, the sector condition requires that coefficient to be imaginary; the minus sign of the interval is its square.

## Why Time Is Not Touched

The material interpretation of the imaginary coefficient is already recorded in *The Material Sector: Four-Vectors, Interval and Lorentz Action*, and this article states it in the terms that the rest of the article needs.

The three real coefficients $x, y, z$ are the directions in which a material object **extends**. An extended object has a size in each of them; it can be displaced along any of them; it can be held, and one can move through it. The three vector directions are, for that reason, the directions a material body occupies. They are the part of the coordinate that a body fills.

The one imaginary coefficient $ict'$ is the direction the object does not extend along. A material body has a position in time but no size in it; it is *at* a time, not *in* time the way it is in space. The imaginary character of the coefficient is the algebraic mark of that difference: the coordinate exists, it is written in the same element and it enters the same norm, but it is not a coordinate a body occupies. Time is measured — by the change of the other coordinates, by the rate at which things happen — but it is measured and not touched. It cannot be held, it cannot be displaced along, and it cannot be revisited. **Measured but not touched** is the material reading of the $i$ on $ct'$.

The reading is an interpretation, and the mathematics beneath it is only the placement of one letter: the coefficient of $e_t$ in the material sector carries $i$ and the coefficients of the $\vec e_k$ do not. Whether the placement *explains* the difference between time and space is a further step, taken by the article that owns the interpretation and repeated here because the second reading of this article is built on it.

## The Second Temporal Coefficient

There is a second temporal coefficient in the framework, and it belongs to the other sector. The centre of the algebra is the complex plane of the single coordinate $Q_t$,

$$
Q_t = ct + ict' ,
$$

whose real part is the informational time and whose imaginary part is the material time, in the dictionary of *Conventions in the Biquaternion Universe* that reads the two parameters $q_t$ and $q'_t$ of the complex coefficient $Q_t = q_t + iq'_t$ as $q_t = ct$ and $q'_t = ct'$. The reading of the plane as a clock — the exchange by the central imaginary as a quarter turn, the two times as the two projections of one hand — is *Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*.

The informational sector is the fixed space of the Hermitian conjugation, $\mathbb{M}_+ = \{\tilde Q : \tilde Q^{*} = \tilde Q\}$, and its general element is

$$
\tilde Q_+ = ct\,e_t + i\bigl(x'\vec e_x + y'\vec e_y + z'\vec e_z\bigr) = ct\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z) \in \mathbb{M}_+ ,
$$

with $t, x', y', z'$ real. The placement of the $i$ is the mirror of the material one: here the **temporal** coefficient is real and the three **spatial** coefficients are imaginary. The scalar direction carries a real number and the vector directions carry imaginary ones, exactly opposite to the material element $ict'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$.

Two norms of the informational element are read together, and they place the informational time on the positive side of both.

The first is the biquaternion norm, which on $\mathbb{M}_+$ is

$$
\boxed{\;\langle\tilde Q_+\rangle_{\natural} = (ct)^2 - {x'}^2 - {y'}^2 - {z'}^2\;},
$$

of signature $(1,3)$: the temporal direction is the single positive one and the three spatial directions are the negative ones. This is the reverse of the material sector, where the temporal direction is the negative one; the reversal is the reversal of who carries the $i$.

The second is the Hermitian form, which on the sector is the plain form and carries the probability,

$$
\langle\tilde Q_+,\tilde Q_+\rangle_{*} = \mathrm{Sc}\bigl(\tilde Q_+\tilde Q_+^{*}\bigr) = (ct)^2 + {x'}^2 + {y'}^2 + {z'}^2 ,
$$

which is positive definite, with every direction counting with a plus and the temporal term the first. On the informational sector the two forms agree in sign on the temporal direction and disagree on the spatial ones; the plain form weights the informational time with a square, as it weights everything, and the temporal direction is the one both forms make positive.

## The Informational Reading: The Record in $ct$

This section is an interpretation, and it is the reason the article was written. It is stated as a reading and its boundaries are given in the section that follows.

The informational sector is the state space of the framework. Its Hermitian elements are the observables, its positive elements normalised by $\langle\tilde{Ϛ},e_t\rangle_{*}=\tfrac12$ (trace one in the image) are the states, the idempotents are the pure states, the positive cone and the Bloch ball organise the mixtures, and the normalised Hermitian form $\operatorname{Tr}(\tilde{Ϛ}\tilde H^{*})=\operatorname{Tr}(\tilde{Ϛ}\tilde H) = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$, read as the trace formula, is the Born rule; the star is inert on $\mathbb{M}_+$ and the unstarred trace is real, and non-negative when $\tilde H\ge0$ (*The Informational Sector: States, Observables and Probability*, *POVMs and the Positive Cone in Biquaternionic Form*, *Roots, Idempotents and Observables*). A state is what an apparatus prepares and what a measurement reads; it is, in the plain sense, a **record**.

The reading this article adds concerns the temporal coordinate of that record. The four coordinates of the informational element are $(ct, x', y', z')$ — one temporal and real, three spatial and imaginary — and the vector directions $i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ are the ones the biquaternion norm reads *negatively*. The temporal direction $ct$ is the one both forms of the sector weigh with a plus: it is the single positive direction of the natural norm and a positive direction of the Hermitian form.

**Reading (the storage direction).** The real temporal coefficient $ct$ of the informational sector is its **storage direction**: the direction along which the record of the sector is held. Information is stored in the informational time.

The argument for the reading is the placement of the two signs, and it is short. A quantity can be ordered and compared only if it is real; the operations by which information is held and read — the positive cone, the trace, the comparison of the weight of a record — are operations on a real scalar. The informational time $ct$ is real, and its contribution to every form of the sector is positive: it is the one direction that can be added up without cancellation, the one the positive cone includes on the same side as the state itself. The material time, by contrast, is imaginary, and its contribution to the material norm is negative; it is the direction that subtracts. The framework therefore places **the recoverable quantity on the real time and the irrecoverable one on the imaginary time**: the informational coordinate $ct$ is the one a record can be built from, and the material coordinate $ict'$ is the one that only accumulates and passes.

Read in the two hands of the clock (*Each Sector Is the Other's Clock*), the statement is that the two times are the two projections of one central coordinate $Q_t = ct + ict'$, and the exchange is a quarter turn that swaps which projection is real. The reading of this article says what the swap is worth physically: the quarter turn carries the record to the elapsed side, where it can no longer be held, and carries the elapsed time to the record side, where it appears as the phase of a state.

**The record can be touched and recovered ($ct$ real); the time cannot ($ict'$ imaginary).** The record is carried by the real coefficient $ct$, and a real quantity can be added up, held and read back. The elapsed time is carried by the imaginary coefficient $ict'$, and an imaginary quantity cannot be held: it enters the norm negatively, it subtracts, and no operation of the algebra returns it. The asymmetry is the asymmetry of the two coefficients, and it completes the material reading of the earlier section: the same imaginary character that makes the material time measured and not touched makes it unrecoverable, while the real character of the informational time is what makes the record touchable and recoverable.

The reading is offered as a physical interpretation of the algebraic placement, and not as a derivation of memory from the algebra. It is the same kind of step as the material reading of the imaginary coefficient: the mathematics fixes where the real and the imaginary coefficients sit, and the reading says what the placement is worth.

## What the Reading Does Not Claim

**It does not claim that the informational sector is observed.** The physical realisation of $\mathbb{M}_+$ as a sector of the world is the standing **hypothesis** of *The Informational Sector: States, Observables and Probability*, and this article inherits it. The mathematics of the sector is established; whether the world carries it as a distinct sector is not.

**It does not claim that a memory is a coordinate.** The reading says that the temporal coefficient of the informational sector is the direction along which records are held; it does not identify a particular psychological or biological memory with the coordinate $ct$, and it offers no dynamics by which a record is written or read. The informational sector has no specified dynamics beyond the quantum formalism itself, as the sector article states.

**It does not claim an arrow of time.** The clock article's result is that the exchange supplies a reference and a period and neither an arrow nor a rate; the direction of the tick remains a choice of slice. The storage reading does not repair that: it places the record on the real time and the passage on the imaginary one, and it selects no direction of the passage.

**It does not claim that the material time is unreal.** The material time is a coordinate of the algebra, it enters the interval, and the framework's physics is written on it. Its being imaginary is a statement about its algebraic character and not about its existence, and the reading of *Why Complexify Spacetime?* — that the real slice is a projection of the complex structure — is unchanged.

## Physical Readings

The temporal dimension of the biquaternion framework reads in three ways, and the three readings are the three placements of one letter.

- **The scalar-dimension reading.** $e_t = 1$ says that the temporal direction is the scalar direction: the identity of the algebra, the axis the rotations share and leave alone, the coefficient a boost mixes with space. Time is the direction along which an element is a number rather than a vector, and the framework's time is a scalar coordinate rather than one of four peers. The reading is the article's own and is the algebraic content of the base.
- **The imaginary-coefficient reading.** On the material sector the temporal coefficient is $ict'$, and the imaginary unit is the source of the Lorentzian signature and the mark of a coordinate that is measured but not touched. The reading is *The Material Sector: Four-Vectors, Interval and Lorentz Action*'s and is repeated here because the storage reading is its mirror. Boundary: the mathematics fixes the placement of the $i$; the reading of the placement as the difference between time and space is an interpretation.
- **The storage reading.** On the informational sector the temporal coefficient is $ct$, real, the single positive direction of the sector's natural norm and a positive direction of its probability form, and the article reads it as the direction along which the sector's records are held: the record can be touched and recovered because $ct$ is real, and the elapsed time cannot because $ict'$ is imaginary. Boundary: the reading inherits the informational-sector hypothesis, adds no dynamics, and does not claim an arrow.

The three readings are independent of one another and rest on one algebraic fact each: the three properties of $e_t$ among the basis units, the imaginary coefficient of the material element, and the real coefficient of the informational one.

## Summary

The base of the biquaternion algebra carries one unit unlike the others. The temporal unit is the identity, $e_t = 1$; it commutes with the whole algebra, it is fixed by the natural, complex and Hermitian conjugations, and it is fixed by every rotation, while the boosts carry it into the informational sector and the three vector units anticommute among themselves and each square to $-e_t$. The temporal direction is therefore the **scalar** direction — the centre of the algebra's action on itself, the direction along which an element is a number rather than a vector, the axis of the framework's rotations. This is the algebraic content of the writing $e_t = 1$, and the article's first claim is that it is a statement about the temporal dimension and not a bookkeeping choice.

On the material sector the temporal coefficient is imaginary. The four-position is $ict'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, the signature of the interval is the square of the imaginary coefficient, and the reading already recorded in *The Material Sector: Four-Vectors, Interval and Lorentz Action* is that the imaginary coefficient is the mark of a coordinate that is measured but not touched: the three real coefficients are the directions a material body extends along, and the one imaginary coefficient is the direction it is merely at.

The framework carries a second temporal coefficient, the real $ct$ of the informational sector, whose element is $ct\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ — the mirror of the material one, with the $i$ on the spatial directions instead of the temporal one. The informational time $ct$ is the single positive direction of the sector's natural norm and a positive direction of its probability form, and the reading this article offers is that it is the sector's **storage direction**: the record can be touched and recovered because $ct$ is real, and the time cannot because $ict'$ is imaginary. The reading is an interpretation, it inherits the informational-sector hypothesis, it adds no dynamics, and it claims no arrow.

All of the mathematics the article uses is verified: $e_t$ is the identity and central, the rotations fix it while the boosts carry it into $\mathbb{M}_+$ and the Lorentz action preserves the norm, the material element is anti-Hermitian with imaginary scalar coefficient, the informational element is Hermitian with real scalar coefficient, the natural norm has the signatures claimed on the two sectors, and the Hermitian form is positive definite with the informational time positive. What remains an interpretation is what the placements are worth physically, and that is what the article's three readings state.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | The quaternion base; the temporal unit is the identity, $\vec e_k^2 = -e_t$ |
| $\mathbb{C}_{\mathbb{B}} = \{Q_te_t\} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra, the complex time sector; parameters $q_t = ct$ and $q'_t = ct'$ |
| $Q_t = ct + ict'$ | The central coordinate, the coefficient of $Q_te_t$: real part the informational time $ct$, imaginary part the material time $ict'$ |
| $\tilde Q_- = ict'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Material element, $\mathbb{M}_-$: imaginary scalar coefficient, real vector coefficients |
| $\tilde Q_+ = ct\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)$ | Informational element, $\mathbb{M}_+$: real scalar coefficient, imaginary vector coefficients |
| $\mathbb{M}_- = \{\tilde Q : \tilde Q^{\flat} = \tilde Q\}$ | Anti-Hermitian subspace, the material sector |
| $\mathbb{M}_+ = \{\tilde Q : \tilde Q^{*} = \tilde Q\}$ | Hermitian subspace, the informational sector |
| $\langle\tilde Q\rangle_{\natural} = \tilde Q\tilde Q^{\natural}$ | Biquaternion norm; $(1,3)$ on $\mathbb{M}_+$, the temporal direction positive |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | Hermitian (probability) form; positive definite, $\sum_\mu\lvert Q_\mu\rvert^2$ |
| $\mathrm{Sc}(\tilde Q) = Q_t$ | Scalar part, the temporal coefficient of the element |
| $\tilde U \in \mathbb{B}^\times_1$, $\langle\tilde U\rangle_{\natural} = e_t$ | Rotor of the Lorentz action $\tilde Q \mapsto \tilde U\tilde Q\tilde U^{*}$, which preserves $\langle\tilde Q\rangle_{\natural}$ |
| $B(\psi,\vec u) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec u$ | Boost rotor of rapidity $\psi$ along the unit real vector $\vec u$; the rotation fixes $e_t$ and the boost carries it into $\mathbb{M}_+$ |
| $\partial/\partial Q_t$ | The temporal derivative in the biquaternionic gradient |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the union of space and time and the origin of the $ict'$ convention.
- Charles W. Misner, Kip S. Thorne, John A. Wheeler, *Gravitation* (Freeman, 1973), §2.3, for the history and the technical fate of $ict'$.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 11 and 18, for the complex structure of spacetime and the place of time among the coordinates.
- Cornelius Lanczos, *The Variational Principles of Mechanics* (Dover, 1970), for the reading of time as a parameter against a coordinate.
- Rolf Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development* **5** (1961) 183–191, for the physical reading of information as something stored and erased, the standing reference for any reading of a storage direction.
- The corpus articles cited above: [Why Complexify Spacetime?](why-complexify-spacetime.html), [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), [Each Sector Is the Other's Clock: the Sector Exchange as Relational Time](each-sector-is-the-others-clock-the-sector-exchange-as-relational-time.html), and [The Biquaternion Space, the Group of Involutions and the Six Subspaces](the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.html), for the conventions, the two sector readings and the clock.
