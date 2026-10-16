# __The Bilinear Product on the Material Sector__

## Introduction

The material sector $\mathbb{M}_-$ carries the four-vectors of relativistic physics. An event is an
element

$$
\tilde T = ict\,e_0 + x\,e_1 + y\,e_2 + z\,e_3,
$$

an imaginary time and three real space directions, and the operations of a relativistic system act on
such elements. This article reads the restriction to that sector of the one product by which they compose
— the **general plain bilinear product** $\tilde P\tilde Q$, the multiplication of the algebra itself — and asks what
its scalar part measures there. The product on the whole algebra is *The Bilinear Product on the Biquaternion Space*; this article is its material-sector companion, the reading of the same product on
$\mathbb{M}_-$ alone.

The answer is one sentence: the scalar part

$$
\langle\tilde P,\tilde Q\rangle = \mathrm{Sc}(\tilde P\tilde Q) = P_0Q_0 - \vec P\!\cdot\!\vec Q
$$

is **negative** on a material **element**, $\langle\tilde Q,\tilde Q\rangle<0$, and **positive** on an
informational one, $\langle\tilde P,\tilde P\rangle>0$. It is the sign of the sector, and it is **not** the metric of
spacetime.

Keeping those two apart is the whole of the article. The metric is the interval,
$\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, of signature $(-,+,+,+)$ on the material sector; it belongs
to the companion quaternionic block and to *Norm and Invertibility in the General Quaternionic Algebra*, and it is cited here,
never re-proved. The point about $\langle\tilde P,\tilde Q\rangle$ is that it is **definite** where the interval is indefinite. A
definite form has no light cone, so $\langle\tilde P,\tilde Q\rangle$ cannot decide which events can influence which. What it carries
is the sign that separates the material sector from the informational one, and that sign is the whole of
its physical content.

**Placement and boundaries.** This article is the material-sector companion of *The Bilinear Product on the Biquaternion Space*, which opens the biquaternion-algebra group and states the product, its law, its scalar form $\langle\tilde P,\tilde Q\rangle$ on the whole algebra and the
restriction table. Here the same product is read on $\mathbb{M}_-$ alone: the sector sign, the sector of a
composite of two material operations, the light cone as the wall of the reversible operations, and the
absence of a material projection. The product's invertibility criterion, its group of units and its cone
are the mathematics of *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone* and the physical level data of *The Four Forms, the Four Algebraic Norms and the Change of Scalars*; the operators and
the sandwich are *The Operators of the Bilinear Product: One-Sided, Two-Sided and the Sandwich*; the
sector itself, its coordinate dictionary and its superselection interpretation are *The Anti-Hermitian
Subspace $\mathbb{M}_-$ as the Material Sector*; and the comparison of the four general products is *The
Four General Products and Their Physical Readings*. None of those is reproved here.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis
$e_0=1,e_1,e_2,e_3$ with $e_1e_2=e_3$, $e_k^{2}=-e_0$, and central scalar imaginary $i$, $i^{2}=-1$; a
general element is $\tilde Q=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ with complex coefficients; the scalar part is
$\mathrm{Sc}(\tilde Q)=Q_0$ and the vector part is $\vec Q=Q_1e_1+Q_2e_2+Q_3e_3$. The conjugations are
the complex conjugation $\bar{\cdot}$, the natural (quaternion) conjugation ${\natural}$, and the
Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{\natural}$. The material sector is the anti-Hermitian half,
$\mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\}$, with the real basis $\{ie_0,e_1,e_2,e_3\}$; the
informational sector is the Hermitian half, $\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=+\tilde Q\}$, with the
real basis $\{e_0,ie_1,ie_2,ie_3\}$.

## What the Material Sector Carries

A material element is written in its own coordinates as

$$
\tilde T = ict\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 \in \mathbb{M}_-,
\qquad c \ \text{the speed of light}.
$$

The imaginary time is the mark of the sector: a material element is anti-fixed by the Hermitian
conjugation, $\tilde T^{*}=-\tilde T$, so the scalar coefficient carries the $i$ and the three vector
coefficients do not. The material sector is the home of the four-vectors, of the velocity, of the
momentum and of the configuration data of a relativistic system, and its own physics — the two sectors,
the coordinate dictionary and the superselection interpretation — is owned by *The Anti-Hermitian Subspace
$\mathbb{M}_-$ as the Material Sector*.

The form that carries the physics of the sector is the **interval**

$$
\langle\tilde T,\tilde T\rangle_{\natural} = \mathrm{Sc}\!\left(\tilde T^{\natural}\tilde T\right) = -c^{2}t^{2} + x^{2}+y^{2}+z^{2},
$$

of signature $(-,+,+,+)$ on $\mathbb{M}_-$; its zero set is the light cone, its level set
$N=-m^{2}c^{2}$ is the mass shell, and both are owned by *The Four Forms, the Four Algebraic Norms and the Change of Scalars*. The
interval is the **general quaternionic bilinear form**, the scalar part of the second of the four general products, and it
is quoted here only to be kept apart from $\langle\tilde P,\tilde Q\rangle$. Two forms of opposite type sit on the same sector, and the
rest of the article is about the one that does not carry the interval.

## The Product of Two Material Operations

The general plain bilinear product $\tilde P\tilde Q$ is the multiplication of the algebra, read in full in *The Bilinear Product on the Biquaternion Space*. The material sector is not closed under it, and the way it
fails is the sharpest consequence of the anti-fixedness $\tilde Q^{*}=-\tilde Q$. The Hermitian
conjugation is an anti-automorphism, $(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}$, so for two
material operations it returns the reversed product,

$$
(\tilde P\tilde Q)^{*}=\tilde Q^{*}\tilde P^{*}=(-\tilde Q)(-\tilde P)=\tilde Q\tilde P,
$$

and the composite therefore splits into its Hermitian and anti-Hermitian parts,

$$
\tilde P\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)+\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr),
$$

that is, into the **anticommutator**, which is an element of $\mathbb{M}_+$, and the **commutator**,
which is an element of $\mathbb{M}_-$. The material sector is therefore not closed under composition, and which half survives is decided by
which relation holds: the composite is **material exactly when the two anticommute**,
$\{\tilde P,\tilde Q\}=0$, so that the informational half vanishes, and **informational exactly when
the two commute**, $[\tilde P,\tilde Q]=0$, so that the material half vanishes. A generic pair of
material operations composes to an element with one part in each sector: the informational part is the
order-independent half $\tfrac12\{\tilde P,\tilde Q\}$, and the order dependence is carried by the
material half $\tfrac12[\tilde P,\tilde Q]$, which changes sign when the two operations are
exchanged.

**Remark (verified).** $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ is fixed by the dagger and the
commutator $\tfrac12(\tilde P\tilde Q-\tilde Q\tilde P)$ is anti-fixed, both to machine precision, and
their sum is the composite $\tilde P\tilde Q$.

**Proposed interpretation, labelled as such.** The order dependence has a sector signature. For two
material operations the anticommutator is the informational half and the commutator the material one, so
**the half of the composite that carries the order is the half that stays material**.

## The Scalar Part Is the Sector Sign

The form $\langle\tilde P,\tilde Q\rangle$ is negative on a material **element** and positive on an informational one, that is at the
two equal arguments, and that is the fact this article is built on. On the material basis
$\{ie_0,e_1,e_2,e_3\}$ the diagonal entries are
$B(ie_0,ie_0)=-1$ and $B(e_k,e_k)=-1$ with all cross terms zero, so

$$
B\big|_{\mathbb{M}_-}=-\mathrm{I}_4,\ \text{signature }(0,4);
\qquad
B\big|_{\mathbb{M}_+}=+\mathrm{I}_4,\ \text{signature }(4,0);
$$

the two sectors are the two definite half-spaces of one form, with opposite signs. Written out on the
coordinates, with $\tilde Q=ib_0e_0+\vec q$ material ($b_0\in\mathbb{R}$, $\vec q$ real) and
$\tilde Q=a_0e_0+i\vec p$ informational ($a_0\in\mathbb{R}$, $\vec p$ real),

$$
\langle\tilde Q,\tilde Q\rangle=-b_0^{2}-\lvert\vec q\rvert^{2}<0,
\qquad
\langle\tilde Q,\tilde Q\rangle=a_0^{2}+\lvert\vec p\rvert^{2}>0 .
$$

**Remark (verified).** The form $\langle\tilde P,\tilde Q\rangle$ is real and strictly negative on every material element and real and
strictly positive on every informational one; the Gram matrices on the two bases are exactly
$-\mathrm{I}_4$ and $+\mathrm{I}_4$. The full restriction table of $\langle\tilde P,\tilde Q\rangle$ over the six remarkable subspaces
is in *The Bilinear Product on the Biquaternion Space*.

**Proposed interpretation, labelled as such.** $\langle\tilde P,\tilde Q\rangle$ is read as the **sector sign**: to say "this element is
material" and to say "$\langle\tilde P,\tilde Q\rangle$ is negative on it" are the same statement. The sign of $\langle\tilde Q,\tilde Q\rangle$ is the same for every element of a sector, so it is invisible to a
computation that stays inside one sector; on a pair the form returns a varying real number, and it is the
sign of its algebraic norm that marks the sector, with no metric content at all.

**Proposed interpretation, labelled as such.** Under the composition the four material directions are
**indistinguishable by sign**: $B(ie_0,ie_0)=B(e_k,e_k)=-1$, all four negative definite, so $\langle\tilde P,\tilde Q\rangle$ alone
does not separate time from space. What separates them is **commutation**: $ie_0$ is central and the
three $e_k$ are not, so **in the material sector time is the central direction and space is the vector
directions**. The Lorentzian sign of the interval is carried by the quaternion conjugation $\natural$ instead, which
fixes the central direction $e_0$ and reverses the three vector directions, so that $\langle ie_0\rangle_{\natural}=-1$ and
$\langle e_k\rangle_{\natural}=+1$; time is the material direction that conjugation cannot see.

**Proposed interpretation, labelled as such.** Write $\tilde P=\tilde P_-+\tilde P_+$ for the split of an
element into its material and informational parts, $\tilde P_\pm\in\mathbb{M}_\pm$. On each sector $\langle\tilde P,\tilde Q\rangle$ is
real; off them it is complex, and its imaginary part is exactly the pairing of the two sectors,
$\mathrm{Im}\,\langle\tilde P,\tilde Q\rangle=\mathrm{Im}\,\mathrm{Sc}(\tilde P_-\tilde Q_++\tilde P_+\tilde Q_-)$,
so $\langle\tilde P,\tilde Q\rangle$ is real on any pair drawn from one sector, and a nonzero imaginary part marks a pair drawn from two
different sectors. Read physically, **a composition of like elements carries no imaginary part, and an
imaginary part is the mark of a composition of a material operation with an informational state.**

## The Light Cone as the Wall of the Reversible Operations

The general plain bilinear product composes material operations, and the first thing a composition asks of its factors
is which of them can be undone. On the material sector the answer is the light cone. The algebraic
criterion, the partition of the algebra and the group structure are *The Bilinear Product on the Biquaternion Space*, *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone* and *The Four Forms, the Four Algebraic Norms and the Change of Scalars*; what is read here is the form they take on
$\mathbb{M}_-$.

**The units and the cone.** The invertibility of the general plain bilinear product is decided by the multiplicative
norm $\langle\cdot\rangle_{\natural}$, not by the sector sign $\langle\tilde P,\tilde Q\rangle$,

$$
\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde Q^{\natural}\tilde Q\bigr)=\sum_{\mu=0}^{3}Q_\mu^{2},
\qquad
\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural},
$$

so that the invertible elements are the elements of non-vanishing norm, forming the **group of units**
$\mathbb{B}^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}$ with the inverse
$\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, and the non-invertible ones are the elements of the
**zero-divisor cone** $\mathcal{C}=\{\langle\tilde Q\rangle_{\natural}=0\}$. The algebra is the disjoint union of the units and
the cone, the origin lying in the cone and being the one element that is neither a unit nor a zero
divisor. On the material sector the norm is the interval, $\langle\tilde T\rangle_{\natural}=-c^{2}t^{2}+x^{2}+y^{2}+z^{2}$,
so the cone cuts the sector in the **light cone** and the group of units cuts it in the **off-light-cone
four-vectors**. The mass shell is the level set $N=-m^{2}c^{2}$: for $m\neq0$ a mass shell lies inside
the group, and the boundary of the group is the massless shell $N=0$. The inverse of a material unit is
material, since $\tilde Q^{\natural}$ is anti-Hermitian with $\tilde Q$ and $\langle\tilde Q\rangle_{\natural}$ is then a real
scalar; but the product of two material units is material only when the two anticommute, by §*The Product
of Two Material Operations*, so the reversibility survives the composition while the sector need not. On
the informational sector the norm is $a_0^{2}-\lvert\vec p\rvert^{2}$ of signature $(1,3)$, and the
wall there is the cone $a_0^{2}=\lvert\vec p\rvert^{2}$; the Hermitian form $+\mathrm{I}_4$ has no
cone, and the form $\langle\tilde P,\tilde Q\rangle$ has no cone on either sector.

**Example (a lightlike and an off-cone material element).** The lightlike material element $ie_0+e_1$,
with $N=-1+1=0$, is a zero divisor: it squares to $-2e_0+2ie_1$ and the partner $ie_0-e_1$ annihilates it,
$(ie_0+e_1)(ie_0-e_1)=(ie_0)^{2}-e_1^{2}=-e_0+e_0=0$. The off-cone element $ie_0+2e_1$, spacelike with
$N=-1+4=3$, is a unit, and its inverse is $(ie_0-2e_1)/3$.

**Proposed interpretation, labelled as such.** Read as the composition of material operations,
*invertible* reads **reversible**: the inverse $\tilde Q^{-1}$ is the operation that undoes $\tilde Q$,
the group of units is the set of the reversible operations, and the cone is the wall of the reversible
region. A four-vector on the light cone is an operation that cannot be undone, a mass-shell four-vector
$N=-m^{2}c^{2}$ with $m\neq0$ is a reversible one, and the massless shell is the boundary between them:
**the cone is at once the locus of lightlike propagation and the wall between the reversible and the
irreversible**. The sector statement and the algebraic statement are the same sentence, read in two
vocabularies.

**Proposed interpretation, labelled as such.** A nonzero lightlike element is not merely non-invertible: it
is a **zero divisor**, there is a nonzero partner that it annihilates, and by the multiplicativity of the
norm a lightlike factor forces a lightlike composite. Read physically, **a lightlike operation annihilates
a partner and makes every composite lightlike: the massless operation cannot be undone, and it cannot be
composed into a massive one.** The origin is the boundary case with the opposite reading: it is on the
cone and it is no zero divisor, the null operation that annihilates nothing and still cannot be undone.

**Proposed interpretation, labelled as such.** The norm is a homomorphism, $\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$, so the interval is a **character of the group of reversible operations** and the mass shell
is a level set of that character. This is the sense in which a mass read through this product is a value of a
multiplicative quantity rather than an eigenvalue, and it is the sharp form of the reading proposed in
*Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*; multiplicativity is not
conservation, and the interval of a composite is the product of the intervals and not their sum.

**Proposed interpretation, labelled as such.** The centre reaches the cone at the origin alone: on the
central line the character is $\langle Ae_0\rangle_{\natural}=A^{2}$, whose vanishing set there is $A=0$, so **no central element
is lightlike and the phase never sits on the wall**; only the vector directions reach it. The reversal is
two-valued on the phase, the loop around the cone being a generator of $\pi_1(\mathbb{B}^{\times})\cong\mathbb{Z}$ while the central circle is twice a generator (*The Biquaternion Unit Group as a Topological
Group*): the same two-to-one that the spinor carries, read here as the doubling of the phase under the
reversal. What is proved is the generator and the doubling; the identification with the two-valuedness of
the material reversal is an interpretation.

**Remark (the sector sign is not the reversibility).** The criterion is the norm and the interval, and not
the algebraic norm of the plain product: $\langle\tilde P,\tilde Q\rangle$ is not multiplicative and decides no invertibility, the
element $e_0+e_1$ being a unit with $B=0$ and the element $e_0+ie_1$ a zero divisor with $B=2$
(*The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*). The form
$\langle\tilde P,\tilde Q\rangle$ carries the sector sign of §*The Scalar Part Is the Sector Sign*; the reversibility is carried by the
interval, and the two must not be exchanged.

## No Material Projection: the Reference State Comes from the Informational Sector

A relativistic theory resolves a field by projecting it, and a projection is an element equal to its own
square, $\tilde\Pi^{2}=\tilde\Pi$. The material sector contains none.

**Proposition.** If $\tilde\Pi\in\mathbb{M}_-$ and $\tilde\Pi^{2}=\tilde\Pi$ then $\tilde\Pi=0$.

*Proof.* From $\tilde\Pi^{2}=\tilde\Pi$ the eigenvalues of $\tilde\Pi$ lie in $\{0,1\}$. From
$\tilde\Pi^{*}=-\tilde\Pi$ the element $i\tilde\Pi$ is Hermitian, so the eigenvalues of $\tilde\Pi$ lie on
the imaginary axis. Their intersection is $\{0\}$, and an idempotent all of whose eigenvalues vanish is
zero.

The same argument in reverse says what does carry the projections: an idempotent that is a sector element
is Hermitian, and the nontrivial ones are the minimal projections
$\tilde\Pi=\tfrac12(e_0\pm i\vec u)$ with $\vec u$ a real unit vector, a two-sphere's worth, of which
the six the coordinate basis displays are $\tfrac12(e_0\pm ie_k)$. These are the pure states of the
informational sector. The classification of the idempotents is the mathematics of *Square Roots of One and the Idempotents of the Biquaternion Algebra*.

**Proposed interpretation, labelled as such.** A material field is split against a **reference state** and not
against a material background. The reference idempotent cannot be material — there is none — so it is an
element of $\mathbb{M}_+$: a state, a pure state or the vacuum. The field decomposes into the part the
reference **resolves**, the component commuting with the projection, and the part it **does not**, the
component that flips the projection into its complement. What is proved is the absence of a nonzero
material idempotent; the identification of the resolved and unresolved parts with the measured and
unmeasured components is an interpretation. The idempotent in physics is owned by *The Biquaternion Vacuum as a
Minimal Idempotent* and *Decoherence as Idempotent Projection*, and the decomposition that the projection
induces is the mathematics of *Ideals and Peirce Decomposition of the Biquaternion Algebra*.

**Remark (verified).** On unit Euclidean elements of $\mathbb{M}_-$ the residual
$\lVert\tilde\Pi^{2}-\tilde\Pi\rVert_E$ is at least $\sqrt2$, so the idempotent equation fails on the
whole sector and its failure is bounded away from zero. On the other side $\tfrac12(e_0\pm ie_k)$ is
idempotent and Hermitian for $k=1,2,3$ and both signs, while $\tfrac12(e_0\pm e_k)$ is neither.

## A Worked Case

Take one material element and one informational element,

$$
\tilde Q=ie_0+2e_1\in\mathbb{M}_-,
\qquad
\tilde P=3e_0+ie_1\in\mathbb{M}_+ .
$$

The two scalar forms give

$$
\langle\tilde Q,\tilde Q\rangle=-5,\qquad \langle\tilde P,\tilde P\rangle=+10,\qquad \langle\tilde Q,\tilde Q\rangle_{\natural}=+3,\qquad \langle\tilde P,\tilde P\rangle_{\natural}=+8 .
$$

Read row by row, the case displays the whole distinction at once. $\langle\tilde P,\tilde Q\rangle$ changes sign between the two
elements, $-5$ material and $+10$ informational, so it is $\langle\tilde P,\tilde Q\rangle$ that carries the sector sign, and the
values are the negative squares $-1^{2}-2^{2}$ and $3^{2}+1^{2}$ of the coordinate dictionary. The
interval is positive on both, $+3$ and $+8$, so it does not separate the sectors. And $\langle\tilde P,\tilde Q\rangle$ and the interval differ by twice the complex square of the vector part,
$\langle\tilde Q,\tilde Q\rangle_{\natural}-2\,\vec Q\!\cdot\!\vec Q$ with the coefficient square
$\vec Q\!\cdot\!\vec Q=Q_1^{2}+Q_2^{2}+Q_3^{2}$, which on the two elements reads
$-5=+3-2(4)$ and $+10=+8-2(-1)$: the two forms agree only when the vector part vanishes, that is on the
scalar line, and the difference $-2\,\vec Q\!\cdot\!\vec Q$ is real of a fixed sign on each sector,
negative on $\mathbb{M}_-$ and positive on $\mathbb{M}_+$.

## The Bound

The article states the restriction to the material sector of the product and its scalar form, and the
boundary of what it must declare is the boundary of the sector.

- **$\langle\tilde P,\tilde Q\rangle$ is not the metric.** It is definite on each sector and has no cone there, so it cannot define the
causal structure. The metric is the interval, of signature $(-,+,+,+)$ on $\mathbb{M}_-$.
- **$\langle\tilde P,\tilde Q\rangle$ is not the interval.** The interval, the mass shell, the four-velocity and invertibility are the
level data of the general quaternionic bilinear form, owned by *The Four Forms, the Four Algebraic Norms and the Change of Scalars*; the
worked case shows the two forms giving different numbers on the same element.
- **$\langle\tilde P,\tilde Q\rangle$ is not the reversibility.** The criterion of invertibility is the norm $\langle\cdot\rangle_{\natural}$ and not the scalar form
$\langle\tilde P,\tilde Q\rangle$: the element $e_0+e_1$ is a unit with $B=0$ and the element $e_0+ie_1$ is a zero divisor with $B=2$.
- **The material sector is not closed under the product.** A composite of two material elements is
material exactly when the two anticommute, and informational exactly when they commute; the sector is not
an algebra.
- **No material projection.** The sector contains no nonzero idempotent, so the reference state of a
material field comes from $\mathbb{M}_+$.

**What the framework does not claim.** The interpretation does not say which physical operation an element
represents, does not derive the Lorentz transformation or the measurement update from the general plain bilinear product, and does not claim that every physical process is a product. The Lorentz action is the sandwich
of *The Bilinear Product on the Biquaternion Space*, and the measurement update is an idempotent
projection; neither is re-derived here.

## The Ledger

**Proved.** The material sector is anti-fixed by the dagger, hence $\langle\tilde P,\tilde Q\rangle$ restricts to $-\mathrm{I}_4$ of
signature $(0,4)$ on $\mathbb{M}_-$ and to $+\mathrm{I}_4$ of signature $(4,0)$ on $\mathbb{M}_+$; the
product of two material elements splits into an informational anticommutator and a material commutator and
is material exactly when the two anticommute; the material sector contains no nonzero idempotent; on the
material sector the algebraic norm $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=\sum_\mu Q_\mu^{2}$
is the interval, its vanishing set is the light cone and its non-vanishing set the off-light-cone
four-vectors, the inverse of a material unit is material, and the product of two material units is a unit;
and the norm restricts to a homomorphism $\mathbb{B}^{\times}\to\mathbb{C}^{\times}$, so the mass shell
$N=-m^{2}c^{2}$, $m\neq0$, lies inside the group of units and the massless shell is its boundary.

**Interpretations.** That $\langle\tilde P,\tilde Q\rangle$ carries the **sector sign** and the interval carries the metric; that the
material geometry belongs to this block and to its quaternionic companion and not to the sesqualgebra;
that the general plain bilinear product is the **composition of material operations**; that a material field is split
against a **reference state** rather than a material background; that the imaginary part of the
composition marks a material operation paired with an informational state; that in the material sector
time is the central direction and space the vector directions; that the group of units is the set of the
**reversible** material operations and the cone the wall between the reversible and the irreversible;
that a lightlike operation is annihilated and annihilates, and forces every composite lightlike; that a
mass is a value of the multiplicative norm read as a character of the group of units; and that the phase
never lies on the wall while the reversal is two-valued on it. Each is the framework's naming of a proved
algebraic fact and is labelled as such.

## Physical Readings

The general plain bilinear product reads as the process on the material sector, and the article's own interpretation is
the composition of two operations. Two further readings follow from its two failings. The product is not
commutative, which is the orientation of a material process and the reason the two slots are not
interchangeable; and its scalar part composes operations rather than values, which is why the Born pairing
is the sesquilinear product and not this one (*The Hermitian Form as a Product: Positivity and the Real
Part of the Born Pairing*). Read on the clock, this product acts on the four-vector and carries no role
for the central phase, which is the exchange's business and not the vector part's.

## Summary

The material sector $\mathbb{M}_-$ carries the four-vectors, an event being
$\tilde T=ict\,e_0+x e_1+y e_2+z e_3$, and this article reads on it the general plain bilinear product $\tilde P\tilde Q$
whose full theory on the whole algebra is *The Bilinear Product on the Biquaternion Space*. Its scalar
part $B=P_0Q_0-\vec P\!\cdot\!\vec Q$, the quaternion scalar product of the two elements, is
negative definite on $\mathbb{M}_-$ with signature $(0,4)$ and positive definite on $\mathbb{M}_+$ with
signature $(4,0)$: opposite definite signs on the two sectors, so $\langle\tilde P,\tilde Q\rangle$ carries the **sector sign**. Being
definite, $\langle\tilde P,\tilde Q\rangle$ has no light cone at all and cannot be the metric; the metric is the interval, the general
quaternionic bilinear form of the companion quaternionic block, of signature $(-,+,+,+)$ on the material
sector. The composition of two material operations is material exactly when the two anticommute, its
informational part being the anticommutator and its order dependence the commutator. The reversibility of
the general plain bilinear product is carried by the norm $\langle\cdot\rangle_{\natural}$ and not by $\langle\tilde P,\tilde Q\rangle$: the invertible elements are the elements
of non-vanishing norm, forming the group $\mathbb{B}^{\times}$ with the inverse
$\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ and bounded by the zero-divisor cone, so on the material sector the
light cone is the wall of the reversible operations and the mass shell $N=-m^{2}c^{2}$ lies inside the
group. The material sector contains no nonzero idempotent, so the reference projection of a field comes
from $\mathbb{M}_+$ — a state and not a material background, which is the framework's interpretation of
the decomposition. The distinctions are labelled throughout: what is proved is the algebra restricted to
$\mathbb{M}_-$, what is proposed is the naming.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^{2}=-e_0$, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary, $i^{2}=-1$ |
| $\bar{\cdot},{\natural},{}^{*}=\bar{\cdot}\circ{\natural}$ | Complex, natural and Hermitian conjugations |
| $\mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\}$ | Material sector, basis $\{ie_0,e_1,e_2,e_3\}$ |
| $\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=+\tilde Q\}$ | Informational sector, basis $\{e_0,ie_1,ie_2,ie_3\}$ |
| $\tilde T=ict\,e_0+\vec x$ | A material event; imaginary time, real space |
| $\tilde P\tilde Q$ | General plain bilinear product; associative, unital, non-commutative |
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-\vec P\!\cdot\!\vec Q$ | General plain bilinear form; Gram $\mathrm{E}=\mathrm{diag}(1,-1,-1,-1)$ |
| $B\big|_{\mathbb{M}_-}=-\mathrm{I}_4$, $B\big|_{\mathbb{M}_+}=+\mathrm{I}_4$ | The sector sign carried by $\langle\tilde P,\tilde Q\rangle$ |
| $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | General quaternionic bilinear form; the interval; $(3,1)$ on $\mathbb{M}_-$ |
| $\tfrac12(\tilde P\tilde Q\pm\tilde Q\tilde P)$ | Anticommutator in $\mathbb{M}_+$; commutator in $\mathbb{M}_-$ |
| $\langle\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=\sum_\mu Q_\mu^{2}$ | Algebraic norm of the general plain bilinear product; the interval at equal arguments; multiplicative |
| $\mathbb{B}^{\times}=\{N\neq0\}$, $\mathcal{C}=\{N=0\}$ | Group of units of the general plain bilinear product; zero-divisor cone; the light cone on $\mathbb{M}_-$ |
| $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ | Inverse in the general plain bilinear product |
| $\tilde\Pi^{2}=\tilde\Pi$ | A projection; none nonzero in $\mathbb{M}_-$ |
| $(n,m)$ | Signature as (number of $+$, number of $-$) diagonal entries |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quaternion algebra, its
scalar part and its relation to $M_2(\mathbb{C})$.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the complex and real structures
on the biquaternion algebra and the sectors of the Hermitian conjugation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime
metric of signature $(-,+,+,+)$ and its contrast with a definite form.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw–Hill, 1980), for the four-vector,
the interval and the mass shell of the material sector.
- Companion article *The Bilinear Product on the Biquaternion Space*, for the product and the form $\langle\tilde P,\tilde Q\rangle$ on
the whole algebra and the restriction table over the remarkable subspaces.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material
sector and its own physics.
- Companion article *The Four Forms, the Four Algebraic Norms and the Change of Scalars*, for the interval, the light cone, the mass
shell and the units.
- Mathematics article *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*
(`articles_maths/the-group-of-units-of-the-biquaternion-algebra-and-the-complement-of-the-zero-divisor-cone.md`),
for the group of units, the multiplicativity of the norm and the cone as the boundary of invertibility.
- Mathematics article *Ideals and Peirce Decomposition of the Biquaternion Algebra*
(`articles_maths/ideals-and-peirce-decomposition-of-the-biquaternion-algebra.md`), for the decomposition
a reference projection induces.
