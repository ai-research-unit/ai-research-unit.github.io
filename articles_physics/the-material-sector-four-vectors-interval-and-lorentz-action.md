# __The Material Sector: Four-Vectors, Interval and Lorentz Action__

## Introduction

The material sector is the anti-Hermitian subspace $\mathbb{M}_-$. It is the fixed space of the reversal $\flat=-{}^{*}$, the half of the algebra in which the scalar coefficient is imaginary and the three vector coefficients are real. Its elements are the four-vectors of relativistic physics: the four-position, the four-velocity, the four-momentum, the four-wavevector, the four-potential, the four-current and the four-force. The quaternionic norm on the sector is the Minkowski interval; its zero set is the light cone; its unit group is the complement of the cone; its commutator is the Lie algebra of the spatial rotations; and the Lorentz group acts on it by rotor conjugation.

This article interprets the mathematics of that subspace. It is the counterpart, in this category, of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* in *Biquaternion Mathematical Physics*: the same sector, read here from the mathematics. It states each result in brief, links the mathematics article that owns it, and gives the physical interpretation with its boundary.

The results used are these.

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The subspace, its basis and its coordinate blocks | [Introduction to the Remarkable Subspaces](../articles_maths/introduction-to-the-remarkable-subspaces.html) |
| The norm, its signature and the inverse formula | [Norm and Invertibility in the Biquaternion Algebra](../articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.html) |
| The zero divisors and the cone | [Zero Divisors of the Biquaternion Algebra](../articles_maths/zero-divisors-of-the-biquaternion-algebra.html) |
| The unit group as the complement of the cone | [The Group of Units and the Complement of the Zero-Divisor Cone](../articles_maths/the-group-of-units-of-the-biquaternion-algebra-and-the-complement-of-the-zero-divisor-cone.html) |
| The four forms and their restrictions | [The 4 Forms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternioid-c-space.html), [Remarkable Subspaces and the Four Forms](../articles_maths/remarkable-subspaces-and-the-four-forms.html) |
| The commutator and the Lie algebra | [Lie Algebras of Sesqualgebras](../articles_maths/lie-algebras-of-sesqualgebras.html) |
| The sandwich and the adjoint action | [Two-Sided Operators on the General Plain Sesqualgebra](../articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra.html) |

## The Results It Uses

### Definition and Basis

The material sector is

$$
\mathbb{M}_-=\{\tilde Q\in\mathbb{B}:\tilde Q^{\flat}=\tilde Q\},\qquad \tilde Q^{\flat}=-{}^{*}\tilde Q,
$$

the fixed space of the reversal. In coordinates it is the set of elements with an imaginary scalar coefficient and real vector coefficients,

$$
\tilde Q=i q'_t\,e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z,
$$

with $q'_t,q_x,q_y,q_z\in\mathbb{R}$. On the physical dictionary $q'_t=c t$ and $(q_x,q_y,q_z)=(x,y,z)$, so the general element is

$$
\tilde Q=i c t\,e_t+x\vec e_x+y\vec e_y+z\vec e_z.
$$

The basis is $\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$, of real dimension four. The sector is the sum of two blocks, the imaginary scalar block $A_2=\mathbb{R}(ie_t)$ and the real vector block $B_1=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$.

The sector is **not a subalgebra**. The product of two anti-Hermitian elements is Hermitian, because ${}^{*}$ is an anti-automorphism: $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}=(-\tilde Q_2)(-\tilde Q_1)=\tilde Q_2\tilde Q_1$. The square of an element is therefore in $\mathbb{M}_+$, and a product of two elements of $\mathbb{M}_-$ is Hermitian exactly when the two commute. The commutator nevertheless stays in $\mathbb{M}_-$, so the sector is closed under the bracket; the anticommutator goes to $\mathbb{M}_+$. In coordinates,

$$
[\tilde Q_1,\tilde Q_2]=2\,\vec q\times\vec r,
$$

with $\vec q=(q_x,q_y,q_z)$ and $\vec r=(r_x,r_y,r_z)$. The time direction is central, and the bracket is the Lie algebra $\mathfrak{u}(2)=\mathbb{R}(ie_t)\oplus\mathfrak{su}(2)$.

### The Norm, the Units and the Cone

The quaternionic norm on the sector is

$$
N(\tilde Q)=\tilde Q\tilde Q^{\natural}=-(q'_t)^2+q_x^2+q_y^2+q_z^2=-c^2t^2+x^2+y^2+z^2.
$$

It is real and of signature $(3,1)$: three positive spatial directions and one negative temporal one. The inverse formula is

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)},
$$

so an element is invertible exactly when its norm is non-zero. The **unit group** is the complement of the norm-zero set. On the zero set the element is a **zero divisor**: it has no inverse, and there exists a non-zero element annihilated by it. The zero set is the **light cone**, and it is also the characteristic cone of the wave operator $\Box=\Delta-\partial_t^2/c^2$, whose principal symbol vanishes exactly on the null directions.

### The Four Forms

The four forms of the algebra are all real on $\mathbb{M}_-$. Writing $\tilde Q_1=i q'_t e_t+\vec q$ and $\tilde Q_2=i r'_t e_t+\vec r$, they read

$$
\langle\tilde Q_1,\tilde Q_2\rangle=-(q'_t r'_t)-(\vec q,\vec r),
$$

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=-(q'_t r'_t)+(\vec q,\vec r),
$$

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=+(q'_t r'_t)+(\vec q,\vec r),
$$

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=+(q'_t r'_t)-(\vec q,\vec r).
$$

The first is negative definite of signature $(0,4)$, the second is the interval of signature $(3,1)$, the third is positive definite of signature $(4,0)$, and the fourth is the negative interval of signature $(1,3)$. The two sesquilinear forms are the negatives of the two bilinear ones, because the star is minus the identity on the sector. The sector carries **no area pairing**: the alternating companion of the forms vanishes identically on it, since multiplication by the central imaginary carries $\mathbb{M}_-$ out of itself, $i\mathbb{M}_-=\mathbb{M}_+$, and no conjugate pair of directions lies inside the sector.

### The Lorentz Action

Let $\tilde U\in\mathbb{B}$ have unit quaternionic norm, $N(\tilde U)=\tilde U\tilde U^{\natural}=e_t$. The map

$$
\tilde Q\longmapsto\tilde Q'=\tilde U\tilde Q\tilde U^{*}
$$

carries $\mathbb{M}_-$ into itself and preserves the norm, $N(\tilde Q')=N(\tilde Q)$. It is a group action, $(\tilde U_2\tilde U_1)\tilde Q(\tilde U_2\tilde U_1)^{*}=\tilde U_2(\tilde U_1\tilde Q\tilde U_1^{*})\tilde U_2^{*}$. The unit-norm elements form $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group. A pure boost is a Hermitian unit-norm element,

$$
\tilde U_{\mathrm L}=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},
$$

a pure spatial rotation is a real quaternion,

$$
\tilde U_{\mathrm R}=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\,\vec u_{\mathrm r},
$$

and a general Lorentz transformation is a general unit-norm biquaternion. The sector is a **representation space** of the Lorentz group, and the rotor acts on it from outside: a boost rotor lies in $\mathbb{M}_+$, a rotation rotor in $\mathbb{H}_{\mathbb{B}}$, and only a general rotor uses the whole algebra.

## Interpretations

### The Sector Is Spacetime

The element $i c t\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$ is a spacetime event. Its norm is the squared interval,

$$
N(\tilde Q)=-c^2t^2+x^2+y^2+z^2=s^2,
$$

with the sign convention that a timelike interval is negative, a null interval is zero and a spacelike interval is positive. The interval is the norm itself, not the square of a separate norm, and the three cases are the three regions of the cone.

The temporal coordinate enters as $i c t$. The factor $i$ is what makes the time direction count with the opposite sign: $i^2=-1$, so the time term is negative while the three space terms are positive. With $c t$ real in place of $i c t$ the sector would carry a Euclidean four-coordinate space and no causal cone. The Lorentzian signature is therefore a consequence of the placement of the central imaginary, not an added axiom.

For a timelike worldline the proper time is

$$
d\tau=\frac{1}{c}\sqrt{-N(d\tilde Q)}=\sqrt{dt^2-\frac{dx^2+dy^2+dz^2}{c^2}},
$$

and it is the parameter along the worldline. For a null worldline the proper time vanishes, and the worldline is a light ray. The causal structure is the sign of the norm; the future and past cones are its two sheets.

The speed of light is local. In a material medium $c=1/\sqrt{\epsilon\mu}$ varies from point to point, so the cone, and with it the dictionary, varies; the vacuum value $c_0$ is the limiting case. The sector is a kinematic space: it carries the events, the intervals and the transformations, not the field equations.

**The boundary.** The article does not derive a dynamics. The interval is a kinematic invariant, the cone is a set, and the identification of the sector with the spacetime of a physical theory is the corpus's interpretation. The anti-Hermitian convention is a convention; the Hermitian convention gives the same geometry with the opposite sign.

### The Seven Four-Vectors

The sector carries the standard four-vectors of relativistic physics. The table gives the element, its components and its invariant.

| Four-vector | Element | Components | Norm |
| --- | --- | --- | --- |
| four-position | $\tilde R=i c t\,e_t+\vec x$ | $(ct,x,y,z)$ | $s^2=-c^2t^2+\lvert\vec x\rvert^2$ |
| four-velocity | $\tilde V=i\gamma c\,e_t+\gamma\vec v$ | $(\gamma c,\gamma\vec v)$ | $-c^2$ |
| four-momentum | $\tilde P=i\frac{E}{c}\,e_t+\vec p$ | $(E/c,\vec p)$ | $-m^2c^2$ |
| four-wavevector | $\tilde K=i\frac{\omega}{c}\,e_t+\vec k$ | $(\omega/c,\vec k)$ | $0$ for light |
| four-potential | $\tilde A=i\frac{\varphi}{c}\,e_t+\vec A$ | $(\varphi/c,\vec A)$ | gauge-dependent |
| four-current | $\tilde J=i c\rho\,e_t+\vec j$ | $(c\rho,\vec j)$ | not fixed |
| four-force | $\tilde K_{\mathrm f}=i\frac{\gamma\vec f\cdot\vec v}{c}\,e_t+\gamma\vec f$ | $(\gamma\vec f\cdot\vec v/c,\gamma\vec f)$ | not fixed |

Every entry has the same structure: an imaginary scalar part, which is the time component, and a real vector part, which is the spatial one. Every entry transforms by rotor conjugation, with a boost rotor for a change of velocity and a rotation rotor for a change of spatial frame. The norm is the invariant of the entry: the interval for the position, $-c^2$ for the velocity, $-m^2c^2$ for the momentum, zero for the wavevector of light.

The **mass shell** is the level set $N(\tilde P)=-m^2c^2$, that is $E^2/c^2-\lvert\vec p\rvert^2=m^2c^2$. A massive particle lies on a two-sheeted hyperboloid, one sheet for each sign of the energy; a massless particle lies on the cone. The **four-potential** is defined up to a gauge transformation $\tilde A\mapsto\tilde A+\partial\chi$, and its norm is not gauge invariant; the field strength built from it is. The **four-current** satisfies the continuity equation $\partial_\mu J^\mu=0$, which in the sector is the statement that the divergence of the four-vector vanishes. The **four-force** $\tilde K_{\mathrm f}$ is orthogonal to the four-velocity when it does not change the rest mass, $\tilde K_{\mathrm f}\cdot\tilde V=0$, and then the norm $N(\tilde V)=-c^2$ is preserved. A force with a non-zero $\tilde K_{\mathrm f}\cdot\tilde V$ changes the rest mass.

**The boundary.** The table is a dictionary, not a derivation. The field equations, the Lorentz force law and the Dirac equation are not results of the algebra; the algebra supplies the carrier space and the invariant. The identification of an algebraic element with a physical four-vector is the interpretive step, and it is the same step as in the standard four-vector formalism.

### The Light Cone Is the Zero-Divisor Cone

The norm-zero set of the sector is exactly its set of zero divisors. A null four-vector has $N(\tilde Q)=0$, so the inverse formula fails and the element has no inverse; equivalently, there is a non-zero element annihilated by it. The **light cone** of Minkowski space is therefore the **zero-divisor cone** of the biquaternion algebra, a structural identity and not an additional assumption.

The cone carries three physical readings. First, it is the set of light rays: a null displacement is the displacement of a signal travelling at $c$. Second, it is the characteristic cone of the wave operator: the principal symbol of $\Box$ vanishes exactly on the null directions, so a discontinuity propagates along the cone. Third, it is the boundary of the unit group: on one side of the cone the elements are invertible, on the cone they are not, and the group of units is the complement of the cone.

The cone also separates the two sheets of the future and the past. The sign of the time component selects the sheet, and the Lorentz group preserves the sheet because it preserves the sign of the time component for a timelike or null vector. A null four-potential is a zero divisor, which is the algebraic form of the statement that a radiation field has no rest frame; a null four-current is the current of a massless charge.

The same cone is the boundary of the positive cone of the informational sector. The Bloch ball is the trace-one slice of the future light cone of the norm, so the causal cone of the material sector and the positivity cone of the informational sector have one and the same boundary. This is the structural link between causality and probability in the framework.

**The boundary.** The cone is a set of elements; the propagation of a field along it is a dynamical statement, not an algebraic one. The zero-divisor property is exact; the identification of the zero-divisor cone with the physical light cone is the interpretation.

### The Lorentz Group Acts by Rotor Conjugation

The action $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ is the Lorentz action on the sector. A boost rotor is Hermitian, a rotation rotor is a real quaternion, and a general rotor is a unit-norm biquaternion. The action preserves the sector and the norm, and it is the reason the sector is a representation space rather than a group: the group acts on it from outside.

The norm condition is $\tilde U\tilde U^{\natural}=e_t$, which is the condition of $SL(2,\mathbb{C})$. It is not the same as the matrix-unitary condition $\tilde U\tilde U^{*}=e_t$, which defines $U(2)$ and preserves the trace of a state. A boost satisfies the first and not the second; a rotation satisfies both. The distinction is the reason the Lorentz action on four-vectors and the evolution of states are two different actions of two different slices of the same algebra.

The rotor is defined up to a sign: $\tilde U$ and $-\tilde U$ induce the same action on the sector, because the sign cancels between the two factors. This is the double cover of the Lorentz group by $SL(2,\mathbb{C})$, read on the sector.

**The boundary.** Rotor conjugation is the action; the article does not derive the Lorentz group from the algebra. The choice of the proper orthochronous component is a choice of the physical transformation group, and the sign ambiguity is unobservable on the sector.

### The Bracket Is the Lie Algebra of the Spatial Part

The commutator of two material elements is twice the cross product of their spatial parts,

$$
[\tilde Q_1,\tilde Q_2]=2\,\vec q\times\vec r.
$$

It has no time component, so the time direction is central, and the bracket is the Lie algebra $\mathfrak{u}(2)=\mathbb{R}(ie_t)\oplus\mathfrak{su}(2)$. The commutator stays in $\mathbb{M}_-$, and the anticommutator goes to $\mathbb{M}_+$; the product of two material elements is Hermitian exactly when their spatial parts are collinear, because the cross product vanishes then and only then.

The bracket is the Lie algebra of the spatial rotations, not of the full Lorentz group. The boost generators do not lie in $\mathbb{M}_-$; they lie in $\mathbb{M}_+$ as the Hermitian elements $i\vec h$, and the full Lorentz algebra is generated by the rotations of $\mathbb{M}_-$ together with the boosts of $\mathbb{M}_+$. The material sector is therefore a Lie algebra for the compact part and not for the full group.

The square of a material element is in $\mathbb{M}_+$, because $\{\tilde Q,\tilde Q\}=2\tilde Q^2$ and the two arguments lie in one sector. Its scalar part is the negative Euclidean square, $-(q'_t)^2-\lvert\vec q\rvert^2$, not the interval; the interval is the quaternionic norm, which is a different form. The two must not be conflated: the square is an informational element, and its scalar part is a Euclidean weight, not a causal interval.

**The boundary.** The bracket is not the physical composition of four-vectors. It is the Lie algebra of the spatial part, and the time direction is central to it. The failure of the material sector to be closed under the product is the algebraic reason a product of two four-vectors is not generally a four-vector.

### The Sector Is Phase-Free and Carries the Metric

All four forms are real on $\mathbb{M}_-$, so each is its own real part and the sector carries no scalar area pairing. The pairing that carries the physics is symmetric: the interval is the quaternionic form of signature $(3,1)$, the Euclidean square is the Hermitian form of signature $(4,0)$, and the two sesquilinear forms are the negatives of the two bilinear ones.

The absence of the area pairing is exact and has a simple reason: every canonical pair of directions of the framework has one leg in each sector. The two times $e_t$ and $ie_t$ form one pair, the material time being the imaginary leg; the three spatial pairs $(\vec e_k,i\vec e_k)$ form three more, the material space being the real leg. The multiplication by $i$ carries a material direction to its informational partner, so no pair lies inside the material sector. The sector is phase-free: it carries the metric and the interval, not the symplectic area.

This is not the statement that the sector has no antisymmetric structure. The **scalar-valued** alternating part of the form vanishes; the **vector-valued** antisymmetric half of the product does not, and on the informational sector it is the coherence. The two objects are different parts of the same block, and the distinction is the one made in the informational article.

**The boundary.** The area pairing is a property of the restriction of a form to a subspace; its vanishing does not remove the vector part of the product. The sector carries the metric, and the metric is symmetric.

### The Material Object Is Acted Upon

The sector is the space of configurations, and the informational sector acts on it by the sandwich $\tilde Q_-\mapsto\tilde Q_+\tilde Q_-\tilde Q_+^{*}$. The asymmetry is the physical content of the names: the material element is what is acted upon, and the informational element is what acts. A material element is the object observed, and its observable representative is $i\tilde Q\in\mathbb{M}_+$; the factor $i$ is the map from the object to the operator that reads it.

The action preserves the norm when the acting element has unit norm, and then it is the Lorentz action, a change of frame. When the acting element is an idempotent, the action is a projection, and it is a measurement; but the idempotent lies in $\mathbb{M}_+$, not in $\mathbb{M}_-$. The material sector itself owns no non-trivial idempotent: if $\tilde\Pi^2=\tilde\Pi$ and $\tilde\Pi^{*}=-\tilde\Pi$, then applying the star to the first relation gives $-\tilde\Pi=\tilde\Pi^2=\tilde\Pi$, so $\tilde\Pi=0$. The measurement projection therefore runs through the informational sector, and the material sector supplies the object, not the outcome.

**The boundary.** The action is established algebra. The interpretation of $\mathbb{M}_+$ as a distinct physical sector is the hypothesis stated in the informational article. The material sector is the acted-upon side of the action whether or not that hypothesis is realised.

## Examples

**A four-position.** Take $c=1$, $t=1$, $x=3$, $y=z=0$. Then $\tilde Q=i e_t+3\vec e_x$ and $N(\tilde Q)=-1+9=8$, a spacelike interval.

**A light ray.** Take $\tilde Q=i e_t+\vec e_x$. Then $N(\tilde Q)=-1+1=0$: the element is null and a zero divisor. The ray travels along $x$ at the speed of light.

**A boost of a rest position.** Let $\tilde U=\cosh(\psi/2)+i\sinh(\psi/2)\vec e_x$ and let $\tilde Q=i c\tau\,e_t$ be a position at rest. Then

$$
\tilde Q'=\tilde U\tilde Q\tilde U^{*}=i c\tau\cosh\psi\,e_t-c\tau\sinh\psi\,\vec e_x,
$$

the standard boost $t'=\tau\cosh\psi$, $x'=-\gamma v\tau=-c\tau\sinh\psi$, and $N(\tilde Q')=-c^2\tau^2$ is unchanged.

**A mass shell.** For $\tilde P=i(E/c)e_t+\vec p$, the norm is $N(\tilde P)=-E^2/c^2+\lvert\vec p\rvert^2=-m^2c^2$, the mass-shell relation. A massless particle has $E=\lvert\vec p\rvert c$ and lies on the cone.

**A four-velocity.** For $\tilde V=i\gamma c\,e_t+\gamma\vec v$, the norm is $N(\tilde V)=-\gamma^2c^2+\gamma^2v^2=-c^2$, independent of the speed. The four-velocity is the tangent to the worldline, and its norm is the same for every inertial observer.

## Limits

The article interprets the kinematics of the sector: the events, the four-vectors, the interval, the cone and the Lorentz action. It does not derive a dynamics, a field equation or a quantization. The speed of light is local, the anti-Hermitian convention is a convention, and the identification of the sector with the spacetime of a physical theory is the corpus's interpretation. The Lorentz group is assumed as the transformation group of the sector, not derived from the algebra. The four-vectors are identified with elements of the algebra; the identification is the interpretive step.

## Summary

- The material sector is the anti-Hermitian subspace $\mathbb{M}_-$, with an imaginary time and a real space, $\tilde Q=i c t\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$.
- Its norm is the Minkowski interval, of signature $(3,1)$, and its zero set is the light cone.
- The light cone is the zero-divisor cone; on it the elements have no inverse, and it is the characteristic cone of the wave operator.
- The unit group is the complement of the cone; the inverse is $\tilde Q^{\natural}/N(\tilde Q)$.
- The four forms are real on the sector: the interval, its negative, the Euclidean square and its negative; the sector carries no scalar area pairing.
- The seven four-vectors of relativistic physics are the elements of the sector, with the imaginary scalar part as the time component.
- The Lorentz group acts by rotor conjugation, with a boost rotor Hermitian, a rotation rotor a real quaternion, and a general rotor a unit-norm biquaternion.
- The commutator is twice the cross product of the spatial parts, with the time direction central; the sector is a Lie algebra for the spatial rotations.
- The sector is the acted-upon side of the action of the informational sector, and it owns no non-trivial idempotent.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{M}_-$ | the anti-Hermitian subspace, the material sector |
| $\tilde Q=i q'_t e_t+\vec q$ | a material element, with $q'_t=c t$ |
| $\tilde Q^{\flat}=-{}^{*}\tilde Q$ | the reversal, whose fixed space is $\mathbb{M}_-$ |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ | the quaternionic norm, the interval |
| $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$ | the inverse, defined off the cone |
| $\tilde U_{\mathrm L}$ | a Lorentz rotor, $\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t$ |
| $\tilde Q'=\tilde U\tilde Q\tilde U^{*}$ | the Lorentz action by rotor conjugation |
| $[\tilde Q_1,\tilde Q_2]=2\vec q\times\vec r$ | the commutator on the sector |
| $\langle\cdot,\cdot\rangle_{\natural}$ | the quaternionic form, the interval |
| $\langle\cdot,\cdot\rangle_{*}$ | the Hermitian form, the Euclidean square |

## Further Reading

- [Introduction to the Remarkable Subspaces](../articles_maths/introduction-to-the-remarkable-subspaces.html), for the definition and the basis of $\mathbb{M}_-$.
- [Norm and Invertibility in the Biquaternion Algebra](../articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.html), for the norm, its signature and the inverse formula.
- [Zero Divisors of the Biquaternion Algebra](../articles_maths/zero-divisors-of-the-biquaternion-algebra.html), for the cone and the zero divisors.
- [The Group of Units and the Complement of the Zero-Divisor Cone](../articles_maths/the-group-of-units-of-the-biquaternion-algebra-and-the-complement-of-the-zero-divisor-cone.html), for the unit group.
- [The 4 Forms over the Biquaternioid $\mathbb{C}$ Space](../articles_maths/the-4-forms-over-the-biquaternioid-c-space.html) and [Remarkable Subspaces and the Four Forms](../articles_maths/remarkable-subspaces-and-the-four-forms.html), for the four forms and their restrictions.
- [Lie Algebras of Sesqualgebras](../articles_maths/lie-algebras-of-sesqualgebras.html), for the bracket.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the same sector read in the physics category.
- *The Biquaternion Space, the Group of Involutions and the Six Subspaces*, for the place of the sector among the six subspaces.
- *The Informational Sector: States, Observables and Probability*, for the partner sector and the action on this one.
