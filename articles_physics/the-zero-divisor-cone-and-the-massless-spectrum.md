# __The Zero-Divisor Cone and the Massless Spectrum__

## Introduction

The biquaternion norm is $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$, and its vanishing set is the **zero-divisor cone**. Three sets live inside and around it, and the first job of this article is to keep them apart. The **roots of $0$** are the origin together with the elements of square zero. The **nilpotents** are the nonzero elements of square zero. The **cone** is strictly larger: it contains the non-pure zero divisors as well, the complex multiples of the non-trivial idempotents.

The physical reading is the one the corpus has built. On the material sector the norm is the Minkowski interval, so the cone cut by the sector is the **light cone**, and the level set of the four-momentum norm, $\langle\tilde P\rangle_{\natural}=-m^2c^2$, is the **mass shell**. The massless shell is the cone itself, and the **massless spectrum** is what the cone does and does not fix: the shell, the rank and the direction, but not the spin.

The article owns no theorem. It states the nesting, the invertibility criterion and the factorisation, each in the mathematics or physics article that proves it, and it reads them.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The zero divisors, their two families and their relation to the idempotents | [N-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| The roots of $0$, the nilpotent cone, index two and the position among the remarkable subspaces | [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](../articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html) |
| The norm, its multiplicativity, the inverse and the group of units | [N-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| The four forms, the interval and the signature on the two sectors | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| The restrictions of the forms and the norms to the material sector | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |
| The cone as a topological object, its link and the punctured cone | [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html) |
| The polar word, its logarithm and the boundary limits that select the two strata | [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html) |
| The generalized polar decomposition, the partial isometry and the rank-one form | [The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone](../articles_maths/the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html) |
| The group of units as the complement of the cone | [N-Regularity and Degeneracy in the Biquaternion Algebra, §The Group of Units](../articles_maths/n-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |

## Three Sets and One Nesting

The square and the norm separate the three sets in one computation. For $\tilde Q=Q_te_t+\vec Q$,

$$
\tilde Q^2=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)e_t+2Q_t\vec Q,
\qquad
\langle\tilde Q\rangle_{\natural}=Q_t^2+(\vec Q,\vec Q),
$$

and the two equations $\tilde Q^2=0$ and $\langle\tilde Q\rangle_{\natural}=0$ are not the same equation.

- **The roots of $0$** satisfy $\tilde Q^2=0$. The vector–scalar split gives $2Q_t\vec Q=0$ and $Q_t^2-(\vec Q,\vec Q)=0$, so a root is either a complex scalar or pure. The scalar branch returns the origin alone; the pure branch is the **nilpotent cone**, the pure elements with isotropic complex vector part.
- **The nilpotents** are the nonzero roots of $0$. They are exactly the nonzero pure elements with $(\vec Q,\vec Q)=0$, they have index two, and each lies in its own annihilator.
- **The zero-divisor cone** is the vanishing set of the norm, $\langle\tilde Q\rangle_{\natural}=0$. An element of the cone with a nonzero scalar part is a zero divisor but not a nilpotent; it is a complex multiple of a non-trivial idempotent.

| set | equation | real dimension | contains a physical null vector of $\mathbb{M}_-$ |
| --- | --- | --- | --- |
| roots of $0$ | $\tilde Q^2=0$ | $4$, plus the origin | no |
| nilpotent cone | $\tilde Q^2=0$, $\tilde Q\neq0$ | $4$ | no |
| zero-divisor cone | $\langle\tilde Q\rangle_{\natural}=0$ | $6$ | yes |

The nesting is the first physical statement, and it is a statement about which object carries which reading. The **nilpotent cone** is the algebraic locus of the lightlike *displacements*: a nonzero element whose composition with itself is nothing. The **whole cone** is the algebraic locus of the lightlike *directions*, including the ones that do not annihilate themselves. The physical light cone of the material sector is the second, not the first. A reader who identifies the two sets will misread every later statement, so the distinction is stated here once and used throughout.

## The Cone as the Wall of Invertibility

The norm is multiplicative, $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}$, and an element is invertible exactly when its norm does not vanish, with inverse

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}}.
$$

The cone is therefore the set of the non-invertible elements off the origin, and the group of units $\mathbb{B}^{\times}=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ is its complement. The cone is the **wall of the units**.

Two consequences follow, and both are physical.

- **The cone is closed under composition.** If either factor is on the cone, the product is on the cone, because the norm of the product is the product of the norms. A lightlike element composed with anything stays lightlike. Both the timelike and the spacelike elements are units: the failure of invertibility sits on the null set alone, and a spacelike displacement is as reversible as a timelike one.
- **The units are the reversible operations.** An element of the group has a two-sided inverse, so its action can be undone; an element of the cone has none, so its action cannot. The reading of the wall is the algebraic form of the statement that a lightlike propagation is not reversible. A null element has no inverse, so it cannot label a frame: a massless particle has no rest frame.

The observables of the previous article sit on the unit side. A root of $+1$ is a unit, and the idempotents of a nontrivial root are on the cone. The nontrivial observable and its states are therefore separated by the wall: the observable is reversible, the state is not. That is the same contrast as before, now located on the cone.

The corpus also reads the wall as an **information barrier**: the boundary at which a description cannot be recovered, and the target of an erasure. That reading adds thermodynamics to the algebra and is owned by *Causality and the Light Cone as an Information Barrier in Biquaternionic Form* and *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*.

**The algebraic statement is narrower.** An element of the cone has no inverse in the algebra; that alone says nothing about entropy, about the arrow of time, or about the impossibility of a physical process.

## The Cut by the Material Sector

A material four-vector is anti-Hermitian,

$$
\tilde R=ict'\,e_t+x\vec e_x+y\vec e_y+z\vec e_z,
$$

and its norm is the interval

$$
\langle\tilde R\rangle_{\natural}=-c^2{t'}^2+\lvert x\vec e_x+y\vec e_y+z\vec e_z\rvert^2,
$$

of signature $(-,+,+,+)$. The cone cut by $\mathbb{M}_-$ is the **null cone** $c^2{t'}^2=\lvert\vec r\rvert^2$.

The mass shell is a level set of the norm of the **four-momentum**, not of the position. With

$$
\tilde P=i\frac{E}{c}\,e_t+\vec p,
\qquad
\langle\tilde P\rangle_{\natural}=-\frac{E^2}{c^2}+\lvert\vec p\rvert^2,
$$

the level set

$$
\langle\tilde P\rangle_{\natural}=-m^2c^2
$$

is the **mass shell**, $E^2/c^2-\lvert\vec p\rvert^2=m^2c^2$. The mass is the value of the momentum norm, up to the sign and the factor $c^2$, and the massless case is the value zero. The level sets of the position norm are the hyperboloids of constant interval; for a timelike displacement, $c^2{t'}^2-\lvert\vec r\rvert^2=c^2\tau^2$. They are not mass shells.

Two facts about the cut carry the reading.

- **Only the massless shell is a cone.** The norm is homogeneous of degree two, $\langle\lambda\tilde P\rangle_{\natural}=\lambda^2\langle\tilde P\rangle_{\natural}$, so a level set $\langle\tilde P\rangle_{\natural}=k$ is invariant under dilation only when $k=0$. The massless shell is the only shell that is a cone; a massive shell is a hyperboloid.
- **The cone is the characteristic cone of the wave operator.** On the material sector the d'Alembertian has the cone as its characteristic set, which is the standard statement that signals propagate on the light cone. The algebraic cone and the characteristic cone are one object, and *The Material Sector: Four-Vectors, Interval and Lorentz Action* develops the identification.

The cone is three-real-dimensional inside the four real dimensions of the sector, and it has a single point at the origin. The interior of the future cone is the timelike region, the exterior the spacelike one, and the cone itself the lightlike boundary. The mass-shell reading uses the same norm and the same sign; the vector is the four-momentum and the value is $-m^2c^2$.

The cone is invariant under the rotor group, so the timelike, spacelike and null separations are unions of orbits, and no change of frame carries a point off the cone. That invariance is the algebraic form of the statement that the causal structure is frame-independent.

## The Massless Spectrum

The **massless spectrum** is the set of massless one-particle states of the framework. The cone is its common floor, and the reading is a division of labour: the cone fixes some of the data of a massless particle and leaves the rest to the representation theory.

**What the cone fixes.** A massless element has $\langle\tilde Q\rangle_{\natural}=0$; its sesquilinear square $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}$ is a positive element whose determinant is $\lvert\langle\tilde Q\rangle_{\natural}\rvert^2$, so it drops from rank two to rank one; and its direction is a point of the projective cone. The shell, the rank and the direction are therefore cone data. For a material null momentum the square is explicit:

$$
\boxed{\;\tilde P\star\tilde P=4\frac{E^2}{c^2}\,\tilde\Pi(-\vec u),\qquad
\tilde\Pi(-\vec u)=\tfrac12(e_t-i\vec u),\qquad \vec u=\frac{\vec p}{\lvert\vec p\rvert}\;},
$$

a positive multiple of the idempotent along the direction opposite to the momentum. The massless state is therefore a **pure boundary state**, not a null state: the same idempotent appears with an imaginary coefficient in the composition and with a positive coefficient in the probability. One momentum, two faces.

**What the cone does not fix.** The cone does not fix the spin. The massless particles the corpus has built are the photon of helicity $\pm1$, the graviton of helicity $\pm2$, the Rarita–Schwinger field of helicity $\pm\tfrac32$ and the chiral fermion of helicity $\pm\tfrac12$. All four have vanishing norm; the cone sees no difference between them. The rank is one for all four, so **rank is a mass label and not a spin label**: it separates the massless from the massive, and it does not separate the massless from one another.

> **The cone is the common floor of the massless spectrum, not its separator.** A massless particle is a point of the cone plus a helicity, and the cone supplies the first factor only.

The first factor has a name and a geometry. The directions of the cone are the **celestial sphere**: the punctured cone is smooth and the apex is its only singular point, so the zero four-momentum is not a direction. Over the complex numbers the projective cone is the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$ with its two rulings, the two chiral spinor families. The direction, the chirality and the phase are the subject of *The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*, and the spinor-helicity form of the same statement is *The Spinor-Helicity Formalism and Biquaternions*. This article uses the factorisation only to say why the cone leaves the spin free.

The factorisation is one line. A null element of the material sector, multiplied by $-i$, is a positive rank-one Hermitian element, and a positive rank-one element is a spinor times its conjugate:

$$
\tilde P=i\,\xi\xi^{\dagger},\qquad \xi\in\mathbb{C}^2,\qquad \xi\neq0.
$$

The direction of $\tilde P$ depends on $\xi$ only through its ray, so the phase of the spinor is not a cone datum. The helicity is the weight of that phase under the little group, and the two helicities of a massless field are the two weights. The cone therefore supplies the ray and the little group supplies the weight; the **value** of the spin is neither. It is a datum of the Lorentz type of the field, and the gauge symmetry is what removes the lower helicities of a higher-rank carrier, as the photon, graviton and Rarita–Schwinger articles show.

That division is the article's reading of the word *spectrum*. The cone is the part of the spectrum that the algebra derives; the spin and the gauge structure are the part it imports. The boundary is exact: **the cone derives no spin and no particle content.** It marks the massless shell and organises the directions, and every massless field of the corpus uses the same marking.

## The Nilpotents Are Not the Physical Null Vectors

The distinction of §*Three Sets and One Nesting* deserves its own section, because the two objects are easy to identify and the identification is wrong.

A physical null vector $\tilde P\in\mathbb{M}_-$ has $\operatorname{Sc}\tilde P\neq0$ whenever the energy is nonzero, so it is not pure and cannot be a nilpotent. What it is, exactly, is an imaginary multiple of a Hermitian idempotent:

$$
\tilde P=2i\frac{E}{c}\,\tilde\Pi(-\vec u),\qquad \vec u=\frac{\vec p}{\lvert\vec p\rvert},
$$

with $\tilde\Pi(-\vec u)$ of square one, Hermitian, trace one and norm zero. The null momentum is therefore on the **non-pure** part of the cone, the part the nilpotents do not reach.

The nilpotents are pure. They lie in the vector subspace and in neither sector: the informational and the material sectors contain no nilpotent at all, because a Hermitian or anti-Hermitian element of square zero is zero. A root of $0$ is an algebraic lightlike *displacement* — a direction that annihilates itself — and it is not a four-momentum. The four-momentum is the idempotent multiple above.

The index is two for the nilpotents: $\tilde\Upsilon^3=0$ exactly when $\tilde\Upsilon^2=0$, and there is no higher index. That rigidity is what makes the nilpotent cone a good algebraic model of a lightlike displacement: the element carries a direction, and one composition with itself is enough to erase it. It is not a model of a lightlike four-momentum, which is not erased by its own composition.

## The Generalized Decomposition on the Cone

The four-factor word stops at the cone; the two-factor Cartan pairing does not. For every element there is a unique pair

$$
\boxed{\;\tilde Q=\tilde H\tilde U,
\qquad
\tilde H=\sqrt{\tilde Q\tilde Q^{*}}\ \text{Hermitian positive semidefinite},
\qquad
\tilde U=\tilde H^{+}\tilde Q\;},
$$

with $\tilde U$ a partial isometry satisfying $\tilde U^{*}\tilde U=\tilde\Pi_{\mathrm i}$ and $\tilde U\tilde U^{*}=\tilde\Pi_{\mathrm f}$, the projections onto the initial and final subspaces of $\tilde Q$, and $\operatorname{ran}\tilde H=\operatorname{ran}\tilde Q$. Off the cone this is the Cartan pairing. On the cone it degenerates in a definite way: a nonzero null element is a positive scalar times a partial isometry,

$$
\tilde Q=\sigma\tilde U,
\qquad
\sigma=\lVert\tilde Q\rVert_{\mathrm F}>0,
\qquad
\tilde H=\sigma\tilde\Pi_{\mathrm f},
\qquad
\tilde\Pi_{\mathrm f}=\tilde U\tilde U^{*},
$$

and the two projections of $\tilde U$ are rank-one Hermitian idempotents, the pure states of the algebra. The positive factor is a scaled pure state, not a scalar.

This is the sharpest statement the cone admits. The boundary value of the word depends on the path; the generalized pair does not. The pair is canonical, and it is the limit that keeps the two lines when the unitary factor loses rank. What the cone does not have is a four-factor word, a logarithm and a continuous unitary phase; what it has is the two-factor pairing with a partial isometry.

**The reading.** The positive factor is the state on the cone, and the second factor is the isometry between the initial and final lines. The unitary phase of the invertible case has collapsed to a transition between two pure states. The rank drop is the lost reversible part.

**The boundary.** The pair is canonical only with the two projection conditions and the range condition on $\tilde H$. Without them the decomposition is not unique: $(\tilde\Pi,e_t)$ multiplies to $\tilde\Pi$ and is excluded because $e_t$ has the wrong projections. The generalized pairing is also not the four factors regrouped; the scale, the phase, the boost and the rotor do not exist on the cone.

## The Null Field

The field strength is the other physical object on the cone, and it sits on the other stratum from the null momentum.

The field-strength biquaternion is pure, $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$, and its norm is

$$
\langle\tilde F\rangle_{\natural}=-\epsilon\left(I_1+2icI_2\right),
\qquad
I_1=\vec E^{2}-c^{2}\vec B^{2},
\qquad
I_2=\vec E\cdot\vec B.
$$

The field is null exactly when $I_1=I_2=0$, that is when $\vec E\perp\vec B$ and $\lvert\vec E\rvert=c\lvert\vec B\rvert$. Because $\tilde F$ is pure, $\tilde F^{2}=-\langle\tilde F\rangle_{\natural}$, so a null field is a **nilpotent**: it lies on the nilpotent stratum, not on the idempotent stratum.

The generalized pair reads the null field as

$$
\tilde F=\sigma\tilde U,
\qquad
\sigma=\lVert\tilde F\rVert_{\mathrm F},
\qquad
\tilde H=\sigma\tilde\Pi_{\mathrm f},
\qquad
\tilde\Pi_{\mathrm f}=\tilde U\tilde U^{*},
$$

and the state $\tilde F\tilde F^{*}/2\langle\tilde F,\tilde F\rangle_{*}=\tilde\Pi_{\mathrm f}$ is pure. The field's amplitude is a pure state of weight $\sigma$, and its phase is a partial isometry between two lines.

The contrast with the massless momentum is the point. A null momentum is an imaginary multiple of a Hermitian idempotent,

$$
\tilde P=2i\frac{E}{c}\tilde\Pi(-\vec u),
$$

and it lies on the idempotent stratum. A null field is a nilpotent and lies on the nilpotent stratum. The two are on the same cone and are not the same kind of element: the momentum is a real null vector of $\mathbb{M}_-$, the field is a pure isotropic vector of the whole algebra. The cone is the common locus, not a common object.

**The reading.** The null field is the radiative field: the two invariant scalars vanish, the field is rank one, and its state is pure. The reading is the algebraic form of the statement that a null field has no rest frame and no invariant intensity; the energy density is frame-dependent.

**The boundary.** The cone fixes the nullity, not the polarization. The field's direction, its helicity and its intensity are extra data, and the cone does not separate the two helicities of a null field. The identification of the null field with a photon is a separate step, owned by the radiation articles.

## The Cone Is a Boundary Value of the Polar Word

The polar decomposition is defined off the cone and has no value on it. It has a boundary value, and the boundary values are exactly the nonzero elements of the cone.

**The boundary-value theorem.** Let $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ be unit real vectors, $\zeta$ a unit complex number and $R>0$, and set

$$
\tilde Q(\psi)=R\exp\left(-\frac{\psi}{2}\right)\zeta\exp\left(i\frac{\psi}{2}\vec u_{\mathrm b}\right)\tilde u_{\mathrm r},\qquad \psi>0.
$$

Every $\tilde Q(\psi)$ is a unit, and as $\psi\to\infty$ it converges to

$$
\boxed{\;\frac{R\zeta}{2}\left(e_t+i\vec u_{\mathrm b}\right)\tilde u_{\mathrm r}\;},
$$

a nonzero element of the cone. The limit is a complex multiple of a minimal idempotent when $\vec u_{\mathrm r}$ has a component in the plane spanned by $e_t$ and $\vec u_{\mathrm b}$, and it is a nilpotent exactly when $\vec u_{\mathrm r}$ is orthogonal to both. Every nonzero element of the cone is such a limit for some choice of the data.

The physical reading is a massive family approaching the massless wall. The scale collapses as $\exp(-\psi/2)$ while the rapidity diverges, so the norm goes to zero at the same rate as the boost grows. The direction of the boost and the rotor decide which stratum is reached. A rotor with a component in that plane gives the idempotent stratum that carries the photon, and a rotor orthogonal to both gives the nilpotent stratum, which is not a four-momentum. The stratum is selected by the rotor, not by the rate, and the rate is the same for both.

The massless limit of a massive family is the physical instance of the theorem; it is worked out, with the rate and the two strata, in [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html).

**The boundary.** The theorem is a statement about the closure of the domain, not about a value at the wall. The cone has no four-factor word and no logarithm; its canonical two-factor pairing is the generalized one above, and the boundary value is a statement about the limit, not about that pair. The word exists only as a limit. A limit taken along another path can approach a different point of the cone, so the boundary value depends on the direction of approach as well as on the element.

## Physical Readings

- **The cone is the light cone.** The interpretation is that the zero set of the norm, cut by the material sector, is the null cone of Minkowski space. The mass shells are the level sets of the four-momentum norm, not of the position norm. Boundary: the identification needs the sector cut; on the whole algebra the cone is a complex cone and not a spacetime object.
- **The cone is the wall of invertibility.** The interpretation is that the non-invertible elements are exactly the lightlike ones, so the cone is the boundary between the reversible operations and the irreversible ones. Boundary: an algebraic statement about inverses; the thermodynamic reading is separate and cited, not derived.
- **The mass is the norm.** The interpretation is that the value of the norm of the material four-momentum is $-m^2c^2$, so the mass is a level set of the norm and the massless case is the cone itself. Boundary: the value is a parameter of the element, not a prediction of a mass spectrum.
- **The massless spectrum is the cone plus a helicity.** The interpretation is that every massless particle sits on the same cone, and the cone fixes the shell, the rank and the direction while the spin and the gauge structure are imported. Boundary: the cone derives no spin value and no particle content.
- **Rank is a mass label.** The interpretation is that the sesquilinear square drops from rank two to rank one exactly on the cone, so the rank separates massless from massive and does not separate the massless particles. Boundary: a statement about the rank of one element, not about a counting of states.
- **The nilpotent is a lightlike displacement, the null vector is a lightlike momentum.** The interpretation is that the pure nilpotent cone models the displacement that annihilates itself, while the physical null momentum is an imaginary multiple of an idempotent on the non-pure part of the cone. Boundary: the two objects are on the same cone and are not the same element.

## Limits

- **Not every zero divisor squares to $0$.** The non-pure family does not, and it is the family the physical null momenta belong to. The roots of $0$ are the pure part of the cone together with the origin.
- **The metric enters only with the sector.** On the whole algebra the cone is the zero set of a complex quadratic form; the Minkowski interval appears when $\mathbb{M}_-$ is cut out. The cone is not derived from a metric.
- **No mass values and no particle spectrum.** The article reads the mass shell as a level set and the massless case as the zero level. It does not predict which masses occur, and it does not derive the particle content.
- **No spin and no gauge structure.** The cone fixes the shell, the rank and the direction. The helicity, the value of the spin and the removal of the lower helicities are representation and gauge data, owned by the particle articles.
- **The complex cone and the real cone are different objects.** The projective geometry of $\mathbb{P}^1\times\mathbb{P}^1$ is the complexified cone; the real celestial sphere is a real slice. The article uses the complex picture only for the two chiralities and sends the reader to the article that owns it.
- **The cone is pointwise.** Every statement is about one algebra at one point. In a curved background the single cone becomes a field of local cones, the metric selecting the directions and the surfaces; the algebra supplies the criterion of nullity only.

## Summary

The norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ has three nested zero sets: the roots of $0$, which are the origin and the nilpotent cone; the nilpotents, which are the nonzero pure isotropic elements of index two; and the zero-divisor cone, which is strictly larger and contains the non-pure zero divisors, the complex multiples of the non-trivial idempotents. The cone is the wall of the group of units, closed under composition and the boundary of invertibility.

Cut by the material sector, the cone is the Minkowski null cone, and the level set $\langle\tilde P\rangle_{\natural}=-m^2c^2$ of the four-momentum norm is the mass shell. Only the massless shell is a cone, because the norm is homogeneous. The **massless spectrum** is the cone plus a helicity: the cone fixes the shell, the rank and the direction, and it does not fix the spin. The photon, the graviton, the Rarita–Schwinger field and the chiral fermion all sit on the same cone; rank is a mass label and not a spin label. A null momentum is an imaginary multiple of a Hermitian idempotent, while a nilpotent is a pure lightlike displacement; the two are on the same cone and are not the same object. The polar word has no value on the cone but has boundary values there: a diverging boost with a collapsing scale reaches an idempotent multiple when the rotor has a component in the plane of $e_t$ and the boost axis, and a nilpotent when the rotor is orthogonal to both.

The cone also has a canonical two-factor decomposition, which the four-factor word cannot supply. Every element is $\tilde Q=\tilde H\tilde U$ with $\tilde H$ positive semidefinite and $\tilde U$ a partial isometry; on the cone $\tilde Q=\sigma\tilde U$ and $\tilde H=\sigma\tilde\Pi_{\mathrm f}$, a scaled pure state. The boundary value depends on the path; the generalized pair does not. The massless momentum and the null field sit on different strata of the same cone: the momentum is an imaginary multiple of an idempotent, the field is a pure nilpotent.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the biquaternion norm |
| $\mathcal Z=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the zero-divisor cone |
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon^2=0$, $\tilde\Upsilon\neq0$ |
| $\sigma=\lVert\tilde Q\rVert_{\mathrm F}$ | the Frobenius scale of a nonzero null element |
| $\tilde\Pi_{\mathrm i},\tilde\Pi_{\mathrm f}$ | the initial and final projections of the partial isometry |
| $\mathbb{M}_-$ | the material sector, $\tilde R=ict'\,e_t+\vec r$ |
| $\langle\tilde R\rangle_{\natural}=-c^2{t'}^2+\lvert\vec r\rvert^2$ | the Minkowski interval |
| $-m^2c^2$ | the mass-shell level of the four-momentum norm |
| $\mathbb{B}^{\times}=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ | the group of units |
| $\tilde P=i\frac{E}{c}\,e_t+\vec p$; $\tilde P=i\,\xi\xi^{\dagger}$ on the cone | the material four-momentum; a null momentum is an imaginary multiple of a rank-one projector |
| $\mathrm{GPA}$, $\mathrm{GPS}$ | the plain algebra and the plain sesqualgebra |

## Further Reading

- [N-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the two families and their relation to the idempotents.
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](../articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the classification, the index and the remarkable subspaces.
- [N-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for multiplicativity, the inverse and the group of units.
- [Exponential Polar Decomposition of Biquaternions](../articles_maths/exponential-polar-decomposition-of-biquaternions.html), for the polar word, the boundary-value theorem and the two strata.
- [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html), for the cone as a singular object and its projectivisation.
- [The Physical Interpretation of the 12 Products](the-physical-interpretation-of-the-12-products.html), for the zero-divisor sets of the twelve structures and the cone as the shared object of the four general products.
- [The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase](the-celestial-sphere-of-the-null-cone-null-directions-chirality-and-the-phase.html) and [The Spinor-Helicity Formalism and Biquaternions](the-spinor-helicity-formalism-and-biquaternions.html), for the direction, the chirality and the helicity weights.
- [The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone](../articles_maths/the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html), for the canonical two-factor pairing on the cone.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html), for the null field and the two invariants.
- [The Null Four-Momentum: What the Cone Derives and What It Does Not](the-null-four-momentum-what-the-cone-derives-and-what-it-does-not.html), for the element-level division.
