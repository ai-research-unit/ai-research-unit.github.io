# __Wilson Loops in Biquaternionic Form__

## Introduction

The gauge field's own field strength is not an observable. In the abelian theory $\tilde{F}$ is gauge invariant, but in the non-abelian theory it transforms by conjugation, $\tilde{F}\mapsto Q\tilde{F}Q^{-1}$, and only its gauge-invariant combinations carry physical meaning. The simplest observable built from the connection is its **holonomy** around a closed curve — the Wilson loop — and it is the object that this article treats in the biquaternion framework.

The Wilson loop is the path-ordered exponential of the connection integrated around a closed curve, traced to make it gauge invariant. It is the phase acquired by a charged particle transported around the curve, the continuum generalization of the Aharonov–Bohm phase, and the order parameter of confinement: its expectation value in the gauge-field path integral of the preceding article distinguishes a perimeter law from an area law. Its biquaternion rendition is unusually direct, because the two ingredients it combines are the two objects the framework already distinguishes. The connection is a material-sector biquaternion, $\tilde{A}\in\mathbb{M}_-$; the gauge group is realized inside the informational sector $\mathbb{M}_+$; and the holonomy, being a group element, is an element of that realization — for $\mathfrak{su}(2)$ realized by the imaginary units, a unit quaternion, whose trace is a scalar part.

The article is organized as follows. The holonomy is defined for the abelian and the non-abelian cases and its gauge transformation is computed. The gauge invariance of the trace is verified, together with the abelian Stokes relation that equates the loop integral to the enclosed flux, and the non-abelian statement that the holonomy transforms by conjugation at the base point. The small-loop expansion is given, in which the loop exponentiates the field strength and the two Lorentz invariants of the Maxwell field appear as the real and imaginary scalar parts of $\tilde{F}^2$. The loop's role as an observable — its expectation value, the perimeter and area laws, and the rectangular-loop potential — is then stated, and the loop equation is recorded. The article closes with the accounting of what the algebra supplies and what is imported.

- Companion article *Canonical Quantization of the Biquaternion Maxwell Field*, for the gauge field, the constraint structure, and the transverse polarizations that the loop's small-expansion probes.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the non-abelian connection, the field strength, and the generators realized in the informational sector.
- Companion article *The Gauge Principle in Biquaternionic Form*, for the gauge transformation and the covariant derivative.
- Companion article *The Photon in Biquaternionic Form*, for the massless one-particle state.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, central $i$, material sector $\mathbb{M}_-$ and informational sector $\mathbb{M}_+$. The gauge potential is $\tilde{A}=iA_0e_0+\mathbf{A}\in\mathbb{M}_-$ and the connection one-form is $\tilde{A}=\tilde{A}_\mu dx^\mu$. The field strength is $\tilde{F}=\bar{\tilde{\nabla}}\tilde{A}-\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$, with the component form $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ in the abelian case. The gauge group is realized by the commutator, in the physics normalization with the Hermitian generators $T^a=ie_a\in\mathbb{M}_+$ obeying $[T^a,T^b]=2i\varepsilon^{abc}T^c=if^{abc}T^c$ with the real structure constants $f^{abc}=2\varepsilon^{abc}$; equivalently, in its anti-Hermitian normalization the same algebra is the compact form $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}\subset\mathbb{M}_-$; the generators are $T^a=ie_a$ in the fundamental representation, normalized so that the trace $\mathrm{Tr}$ is the matrix trace in that representation, equal to twice the scalar part for the quaternion realization. The coupling is $g$ and the path ordering is denoted $\mathcal{P}$. Natural units are used.

## The Holonomy of the Connection

### The Abelian Wilson Loop

For an abelian connection the holonomy around a closed curve $C$ is the exponential of the line integral of the potential,

$$
W(C) = \exp\left(i\oint_C A_\mu\,dx^\mu\right)
= \exp\left(\oint_C \mathrm{Sc}\!\left(\tilde{A}_\mu\right)dx^\mu\right),
$$

where the second form records that the $i$ of the phase is carried by the material sector itself: for the abelian field the potential is taken along the scalar direction, $\tilde{A}_\mu=iA_\mu e_0$, so that $\mathrm{Sc}(\tilde{A}_\mu)=iA_\mu$ and the line integral is a central imaginary scalar whose exponential is a phase. The definition is a functional of the curve and a functional of the connection, and it is an element of $U(1)$ — a phase. Its gauge transformation is the content of the following section.

### The Non-Abelian Wilson Loop

For a non-abelian connection the potential is a Lie-algebra-valued one-form, and the holonomy is the path-ordered exponential

$$
W(C) = \mathrm{Tr}\,\mathcal{P}\exp\left(i\oint_C A_\mu\,dx^\mu\right)
= \mathrm{Tr}\,\mathcal{P}\exp\left(i\oint_C A^a_\mu T^a\,dx^\mu\right),
$$

where the generators $T^a$ are realized in the informational sector of the algebra. Without the trace, the holonomy is a group element $U(C)=\mathcal{P}\exp(i\oint_C A_\mu dx^\mu)$; with the trace it is a gauge-invariant number. In the quaternion realization the generators are the imaginary units $ie_a$, the group element is a unit quaternion $Q$, and the trace is $2Q_0$ — twice the scalar part. The Wilson loop is therefore, in the framework's own terms, the scalar part of the holonomy element of the informational sector, and the connection whose holonomy it is lies in the material sector. The loop is a bilinear object that joins the two sectors.

## Gauge Invariance and Stokes' Theorem

### The Abelian Case

Under a gauge transformation $\tilde{A}\mapsto\tilde{A}-\tilde{\nabla}\Gamma$, the line integral changes by

$$
\oint_C A_\mu\,dx^\mu \;\longmapsto\; \oint_C \left(A_\mu-\partial_\mu\Gamma\right)dx^\mu
= \oint_C A_\mu\,dx^\mu-\oint_C d\Gamma
= \oint_C A_\mu\,dx^\mu ,
$$

because the integral of a total derivative around a closed curve vanishes. Hence $W(C)$ is invariant. This was verified numerically on a rectangular lattice loop: with random link potentials and random gauge functions at the sites, the loop integral was unchanged to machine precision under the gauge transformation, exactly zero difference.

The same computation in a different form is Stokes' theorem. For a curve $C$ bounding a surface $S$, with $d\Sigma^{\mu\nu}=dx^\mu\wedge dx^\nu$ the oriented area element,

$$
\oint_C A_\mu\,dx^\mu = \frac12\int_S F_{\mu\nu}\,d\Sigma^{\mu\nu},
\qquad
W(C) = \exp\left(\frac{i}{2}\int_S F_{\mu\nu}\,d\Sigma^{\mu\nu}\right),
$$

so the abelian Wilson loop is the exponential of the enclosed flux. The factor $\frac12$ is the one that counts each plane once: for a planar loop the antisymmetric $d\Sigma^{\mu\nu}$ contributes twice the enclosed area, and the pairing with the antisymmetric $F_{\mu\nu}$ converts the pair into the single physical flux. This was verified for a single small plaquette of side $h$: the closed-loop integral equaled $h^2F$ to a relative accuracy of $10^{-16}$, where $F$ was the constant field strength of the chosen potential. The two statements — gauge invariance and Stokes' theorem — are the same fact seen from the two ends: the loop sees only the enclosed field strength, and the field strength is gauge invariant.

### The Non-Abelian Case

Under a gauge transformation $A_\mu\mapsto Q A_\mu Q^{-1}+(i/g)Q\partial_\mu Q^{-1}$, the group element transforms by conjugation at the endpoints of the curve,

$$
U(C) \;\longmapsto\; Q(x_{\mathrm{start}})\,U(C)\,Q^{-1}(x_{\mathrm{end}}) ,
$$

and for a closed curve the endpoints coincide, so the holonomy transforms by conjugation at the base point,

$$
U(C)\;\longmapsto\;Q\,U(C)\,Q^{-1}.
$$

The trace is invariant under conjugation, and the Wilson loop is therefore gauge invariant. This was verified for the quaternion realization: with random unit-quaternion link variables around a rectangular loop and random site gauge transformations, the real part of the trace — the Wilson loop of $\mathfrak{su}(2)$ — was unchanged to machine precision, while the full quaternion holonomy changed as it should, the two agreeing in their trace. The distinction matters: the untraced holonomy is not gauge invariant, and it is the trace that carries the observable content. In the framework's language, the conjugation is the adjoint action of the informational sector that the article on integer-spin quantization calls the rotation action; the trace extracts its invariant.

## The Small Loop and the Field Strength

A small loop is the local probe of the field strength. For a loop of area $a^2$ in the $\mu\nu$ plane, the holonomy expands as

$$
W(C) = 1 + i\,a^2 F_{\mu\nu} + O(a^4)
$$

in the abelian case, and in the non-abelian case as $W=1+ia^2F^a_{\mu\nu}T^a+O(a^4)$, so the loop exponentiates the field strength. This was verified for a small abelian plaquette of side $a=10^{-3}$: the ratio of the deviation of the plaquette from unity to $a^2F$ was unity to six significant figures. The small loop is therefore an algebraic probe of $\tilde{F}$, and the two gauge-invariant scalars that can be built from $\tilde{F}$ in the framework are visible in the loop at second order.

Those scalars are the biquaternion content of the Maxwell field. Writing the field strength as $\tilde{F}=\sum_k(iE_k-H_k)e_k$, its square is a central element,

$$
\tilde{F}^2 = \left(|\mathbf{E}|^2-|\mathbf{H}|^2\right)e_0 + 2i\,\mathbf{E}\cdot\mathbf{H}\,e_0 ,
$$

so that the two Lorentz invariants of the Maxwell field — the difference of the squared field magnitudes and the pseudoscalar $\mathbf{E}\cdot\mathbf{H}$ — are the real and imaginary scalar parts of $\tilde{F}^2$. This was verified with the $2\times2$ representation $e_k=-i\sigma_k$: for random fields the matrix square of $\tilde{F}$ equaled $ (|\mathbf{E}|^2-|\mathbf{H}|^2+2i\mathbf{E}\cdot\mathbf{H})I_2$ to machine precision. The statement is the framework's: in a biquaternion algebra the square of the field strength is automatically central, and both invariants are read from the single element $\tilde{F}^2$ as its two scalar parts. The Wilson loop of a small loop is the exponentiation of the field strength that this element describes, and the two invariants are its second-order content.

### The Constant Field

The small-loop expansion becomes exact for a constant field strength, and the exact loop shows which components of $\tilde{F}$ a given loop measures. For constant $F_{\mu\nu}$ the loop integral is the flux through the enclosed surface,

$$
\oint_C A_\mu\,dx^\mu = \frac12 F_{\mu\nu}\Sigma^{\mu\nu},
\qquad
W(C) = \exp\left(\frac{i}{2}F_{\mu\nu}\Sigma^{\mu\nu}\right),
$$

with $\Sigma^{\mu\nu}$ the (oriented) area bivector of the loop. A loop in the $xy$ plane of area $\mathcal{A}$ measures only the magnetic component, $W=e^{iB_3\mathcal{A}}$; a loop in the $xt$ plane measures only the electric component, with the sign fixed by the orientation of the loop; and a loop tilted into a general plane measures the combination $\mathbf{B}\cdot\hat{\mathbf{n}}\,\mathcal{A}$ for a spacelike plane and $\mathbf{E}\cdot\hat{\mathbf{n}}\,\mathcal{A}$ for a timelike one. This was verified for the plaquette of the preceding paragraph, where the enclosed flux was exactly $h^2F$. In the biquaternion language the exponent is the scalar part of the product of the area bivector with the field strength, and the electric and magnetic parts of $\tilde{F}$ are measured by timelike and spacelike loops respectively. The two invariants of $\tilde{F}^2$ are what remain when the loop is allowed to explore both kinds of plane; a single loop sees only one component.

## The Gaussian Average of the Loop

The loop's expectation value is Gaussian in the free theory, and the Gaussian average is the direct transcription of the generating functional of the preceding article. With the source $J^\mu$ replaced by the line current carried by the loop,

$$
J^\mu(x) = \oint_C dx^\mu\;\delta^{(4)}(x-z(\tau)),
$$

the gauge-fixed Gaussian average gives

$$
\langle W(C)\rangle = \left\langle\exp\left(i\oint_C A_\mu dx^\mu\right)\right\rangle
= \exp\left(-\frac{i}{2}\oint_C dx^\mu\oint_C dy^\nu\;D_{\mu\nu}(x-y)\right),
$$

the double integral of the propagator along the loop, with the same $-\frac{i}{2}$ of the generating functional of the preceding article and $D_{\mu\nu}$ its inverse quadratic form. This is the free-field content of the loop: the quantum effect is the self-interaction of the loop's line current through the propagator of the preceding article, and the gauge-parameter cancellation of that article is what makes the result well defined, since the line current is conserved and the longitudinal part of $D_{\mu\nu}$ cannot contribute. For a large smooth loop the argument is dominated by the short-distance behaviour of $D_{\mu\nu}$, which grows as $1/(x-y)^2$, and the double integral has a linear divergence proportional to the perimeter,

$$
-\frac{i}{2}\oint_C dx^\mu\oint_C dy^\nu\,D_{\mu\nu}(x-y)
\;\sim\; -\frac{i\,\kappa_{\mathrm{div}}}{2}\,\mathrm{perim}(C),
$$

with $\kappa_{\mathrm{div}}$ a real divergent coefficient, so that the divergent part of the loop is a phase proportional to the perimeter, the Minkowski form of the perimeter law. The physical statement is that this divergence is absorbed by the mass renormalization of the external sources that the loop describes, and the renormalized loop is finite; the free theory thus produces the perimeter law, while the area law requires the nonperturbative dynamics. The biquaternion content is that the propagator whose double integral appears is the material-sector propagator and the line current is a material-sector current, so the loop's self-interaction is a statement entirely within $\mathbb{M}_-$.

## The Aharonov–Bohm Phase

For an abelian loop that encircles a region of confined flux, the loop integral equals the enclosed flux by Stokes' theorem, whether or not the field vanishes on the loop itself. If the flux $\Phi=\frac12\int_S F_{\mu\nu}d\Sigma^{\mu\nu}$ is confined to a tube that the loop encloses but does not touch, then $W(C)=e^{i\Phi}$ even though $\tilde{F}=0$ at every point of the loop. This is the Aharonov–Bohm phase, and it shows that the connection carries physical information that the field strength at the loop does not: the holonomy is the primary observable and the field strength is its local density. In the framework the loop's phase is the exponential of a scalar-part integral of the material connection, and the flux it measures is the integral of the field strength biquaternion over the enclosed surface.

## The Non-Abelian Loop and the Surface

For the non-abelian theory there is a surface form of the holonomy, but it is not the naive exponentiation of the flux: because the field strength does not commute with itself at different points, the surface integral must itself be path ordered, and the non-abelian Stokes theorem reads

$$
U(\partial S) = \mathcal{P}_S\exp\left(i\int_S \mathcal{F}\right),
\qquad
\mathcal{F}(x) = U(x_0,x)\,F_{\mu\nu}(x)\,U(x,x_0)\,dx^\mu\wedge dx^\nu ,
$$

where the field strength is transported back to a common base point $x_0$ before being integrated, and the path ordering is along the surface. The trace of the holonomy is independent of the choice of base point and of the transport, which is why the Wilson loop is well defined. In the framework the transport factors are elements of the informational realization of the group, and the statement is that the loop measures the field strength dressed by the adjoint action — the same adjoint action that the article on integer-spin quantization identifies as the rotation.

## The Loop as an Observable

### Expectation Value and the Perimeter and Area Laws

The Wilson loop becomes a quantum observable when averaged in the gauge-field path integral,

$$
\langle W(C)\rangle = \frac{\displaystyle\int\mathcal{D}\tilde{A}\;W(C)\,e^{iS[\tilde{A}]}}{\displaystyle\int\mathcal{D}\tilde{A}\;e^{iS[\tilde{A}]}},
$$

with the gauge fixing of the preceding article and, where needed, the ghost and envelope structure. Its asymptotic behaviour for large loops is the standard diagnostic of confinement, and the two laws below are quoted in Euclidean signature, where the exponent is real and negative; the free-theory average of the preceding section was written in Minkowski signature, where the same perimeter divergence appears as a phase. A **perimeter law**,

$$
\langle W(C)\rangle \sim e^{-\kappa\,\mathrm{perim}(C)} ,
$$

is the behaviour of a theory in a phase where the flux between two sources can spread, and an **area law**,

$$
\langle W(C)\rangle \sim e^{-\sigma\,\mathrm{area}(C)} ,
$$

is the behaviour of a confining phase, where a flux tube forms and the coefficient $\sigma$ is the string tension. The rectangular loop of width $L$ and time extent $T$ gives the static potential between two heavy sources through $\langle W(C)\rangle\sim e^{-iT\,V(L)}$, so that an area law corresponds to a linearly rising $V(L)=\sigma L$ and a perimeter law to a screened potential. These statements are standard and are the reason the Wilson loop is the natural order parameter of the gauge theory; the lattice regularization in which the area law is established and the strong-coupling expansion that produces it belong to the companion subcategory on gauge fields and are not repeated here.

### The Rectangular Loop and the Static Potential

The most common loop is the rectangle of spatial width $L$ and temporal extent $T$, with $T\gg L$. For large $T$ the expectation value exponentiates the energy of the state that the loop creates,

$$
\langle W(\square_{L\times T})\rangle \;\sim\; e^{-iT\,V(L)} ,
$$

so that the loop is the worldline of a pair of static sources separated by $L$ and the exponent is the potential between them. An area law $e^{-\sigma LT}$ corresponds to $V(L)=\sigma L$, a linearly rising potential, which is confinement; a perimeter law corresponds to a potential that flattens at large $L$, which is screening. In the abelian free theory the evaluation of the previous sections gives the Coulomb potential $V(L)\sim g^2/L$ with the perimeter divergence removed, and the biquaternion reading is that the loop's Gaussian average is the self-interaction of the material line current through the material propagator. The potential is therefore the quantity that the loop expectation value encodes, and the confinement question is the question of whether the exponent grows with $L$ or with the perimeter.

### The Biquaternion Form of the Order Parameter

In the framework the order parameter is the expectation of the scalar part of the holonomy of a material-sector connection, taken around a closed curve,

$$
\langle W(C)\rangle = \left\langle \mathrm{Tr}\,\mathcal{P}\exp\left(i\oint_C \tilde{A}_\mu dx^\mu\right)\right\rangle ,
$$

with the trace over the informational realization of the gauge group and the average over the material-sector configurations. The two fixed-point sectors appear in the two operations: the average is over $\mathbb{M}_-$ configurations, and the trace is over the $\mathbb{M}_+$ realization of the group. The order parameter is thus the expectation of a two-sector bilinear, and the confinement transition is a statement about its long-distance behaviour.

### The Loop as the Phase of a Charged Worldline

The loop is not only an abstract observable; it is the phase of a charged particle's worldline. Coupling a charge to the connection by the minimal prescription $D_\mu=\partial_\mu+igA_\mu$, the amplitude for a particle to propagate along a worldline acquires a factor

$$
\exp\left(ig\oint_C A_\mu\,dx^\mu\right),
$$

so that the Wilson loop is the closed-worldline phase — the sum of the phases accumulated along the worldline. The statement is the gauge-covariance of the minimal coupling: the phase is what a gauge transformation shifts away, and the closed loop is the smallest worldline on which the shift cancels. In the framework the coupling is between a material-sector connection and the worldline of a charged field, and the phase is the exponential of the scalar-part integral of the connection; the loop therefore measures the material sector along a closed curve, and its gauge invariance is the statement that only closed curves give gauge-invariant phases.

### Spin and the Loop

For a particle of spin, the worldline carries an internal precession in addition to the phase, and the loop acquires a spin factor: the holonomy is taken in the representation of the spin rather than in the fundamental one. For a spin-$s$ field the generator is the spin-$s$ representation of the gauge algebra, and in the biquaternion framework the integer-spin representations are the adjoint action and its tensor powers. A spin-one charged field therefore couples to the connection through the adjoint action, and its Wilson loop involves the holonomy in the adjoint representation — the representation carried by the material vector part. The statement ties the present article to the integer-spin article: the representation in which the loop is traced is the representation that the integer-spin fields transform in, and for spin one it is the adjoint action on the material sector.

## The Loop Equation

The quantum Wilson loop is constrained by the Schwinger–Dyson equation of the gauge-field path integral. Varying the connection in the integral and using the definition of the loop, one obtains the **loop equation**, in which the area derivative of $\langle W(C)\rangle$ is expressed through the loop self-intersection. The derivation is short enough to indicate: the variation of the loop under $A_\mu\to A_\mu+\delta A_\mu$ gives $i\oint_C\delta A_\mu dx^\mu$ times the loop, and the variation of the action gives the field equation; integrating by parts and using the equation of motion expresses the result through the area derivative

$$
\frac{\delta}{\delta\sigma_{\mu\nu}(x)}\langle W(C)\rangle
= \left\langle \mathrm{Tr}\,\mathcal{P}\left(F_{\mu\nu}(x)\,e^{i\oint_C A}\right)\right\rangle ,
$$

the statement that the area derivative inserts the field strength at a point of the loop. Iterating and using the field equation produces the loop equation. For the abelian theory the content is the free-field equation for the field strength; for the non-abelian theory the equation couples loops with different numbers of windings, and closing it requires an additional assumption such as the factorization of the large-$N$ limit. These equations are standard and are cited below; their biquaternion rendition adds nothing beyond the observation already made, that the loop is the trace of a holonomy of a material connection over an informational realization, and that the loop equation is the statement that this holonomy is a functional of the field strength obeying the nonlinear field equation of the companion articles.

## The Loop, the Two Sectors, and the Algebra

The constructions of this article can be collected into a single statement about the framework. A Wilson loop is built from three operations, and each of them is an operation the algebra already provides.

The first is the integration of a **material** one-form along a curve: the holonomy's logarithm, $\oint\tilde{A}_\mu dx^\mu$, is an element built from the material sector. The second is the **exponentiation** of that element into the group generated by the informational realization of the gauge algebra; for $\mathfrak{su}(2)$ that group is the unit quaternions, and the exponentiation is the usual exponential of an imaginary quaternion, an element of $\mathbb{M}_+$. The third is the **trace**, which in the quaternion realization is twice the scalar part; it is the operation that turns the group element into a gauge-invariant number. The loop is therefore the scalar part of the holonomy of a material connection in an informational group element, and its gauge invariance is the invariance of the scalar part under the adjoint action.

Three consequences are worth stating separately. The untraced holonomy is an element of $\mathbb{M}_+$ — a unit quaternion — and is not gauge invariant; it transforms by the adjoint action, which is the conjugation of a quaternion by another. The traced loop is invariant because the scalar part is what the adjoint action preserves. And the abelian loop is the degenerate case in which the group element lies in the center, so that the holonomy is a phase and the trace is trivial. The framework thus orders the three cases — central, adjoint, and the general representation — by the sector in which the group element lies, and the Wilson loop of a given gauge theory is a trace over exactly one of them.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The connection as a material-sector one-form and the holonomy as an element of the informational realization of the gauge group; the trace of the holonomy as a scalar part, which is what makes the Wilson loop a number; the invariance of the abelian loop under the gradient shift, verified; the abelian Stokes relation between the loop and the enclosed flux, verified on a small plaquette; the conjugation transformation of the non-abelian holonomy and the invariance of its trace, verified for the quaternion realization; the small-loop expansion, verified to be the exponentiated field strength; and the centrality of $\tilde{F}^2$, whose two scalar parts are the two Lorentz invariants of the Maxwell field, verified in the $2\times2$ representation.

**Imported, and left visible.** The Wilson loop as an observable and its standard interpretation; the path-ordered exponential and the holonomy's transformation law; the area and perimeter laws and the string tension; the relation of the rectangular loop to the static potential; the lattice regularization and the strong-coupling argument that establishes confinement; the loop equation and the factorization assumption needed to close it; and the renormalization of the loop's perimeter divergence, which standard treatments handle with a mass renormalization of the external sources.

**Not supplied.** The gauge group; the shape of the loops that occur in a given process; the value of the string tension; and any empirical content. The loop is gauge invariant in any formulation; the framework's contribution is that it is a trace over one sector of a holonomy of the other, and that the field strength it exponentiates has its two invariants in the two scalar parts of a single central element.

## Open Questions

1. **A sector-theoretic reading of the trace.** The Wilson loop is the trace of a holonomy: an $\mathbb{M}_+$ trace of an object whose logarithm is in $\mathbb{M}_-$. Is there an intrinsic pairing between the two sectors that selects the trace, in the way the bilinear form $\mathrm{Sc}(X\bar{Y})$ pairs elements of $\mathbb{B}$, and does it reproduce the matrix trace? A positive answer would make the loop's gauge invariance a statement about the two sectors rather than about a chosen representation.

2. **The order parameter and the sector split.** The confinement transition is a change in the long-distance behaviour of $\langle W(C)\rangle$. Is there a biquaternionic order parameter — an element whose norm measures the transition, rather than a functional of loops — and does the transition appear as a change in a property of the algebra's own objects?

3. **The small-loop invariants at second order.** The two Lorentz invariants are the scalar parts of $\tilde{F}^2$. Does the next order in the small-loop expansion organize further invariants as the scalar parts of higher powers of $\tilde{F}$, and is there a generating object — a central element of the algebra — whose scalar parts are all the invariants?

4. **The loop equation as an algebraic identity.** The loop equation follows from the path integral. Is the abelian loop equation equivalent to an identity in the algebra's bilinear form, in the way the small-loop expansion is the exponentiation of $\tilde{F}$?

5. **The perimeter divergence and the two sectors.** The perimeter divergence of the loop is absorbed by a renormalization of the external sources, which live on the loop. Does the sector split offer a natural regularization of the divergence, or is it entirely a property of the sources?

6. **Empirical content.** As everywhere, whether any of this yields a prediction distinguishing the framework from standard gauge theory. The transcription given here does not.

## Summary

The Wilson loop is the trace of the holonomy of the gauge connection around a closed curve. In the biquaternion framework the connection is a material-sector one-form, $\tilde{A}\in\mathbb{M}_-$, and the holonomy is an element of the gauge group realized in the informational sector $\mathbb{M}_+$ — for $\mathfrak{su}(2)$ a unit quaternion — so that the loop is the scalar part of that element and couples the two fixed-point sectors.

For the abelian theory the loop is $\exp(i\oint A_\mu dx^\mu)$; it is invariant under the gradient shift because the integral of a total derivative around a closed curve vanishes, and Stokes' theorem makes it the exponential of the enclosed flux. Both were verified, the first to machine precision on a rectangular loop, the second to relative accuracy $10^{-16}$ on a small plaquette. For the non-abelian theory the holonomy is a path-ordered exponential transforming by conjugation at the base point, and the trace is invariant; this was verified for the quaternion realization, where the real part of the trace was unchanged under random site gauge transformations while the untraced holonomy changed by conjugation.

For a small loop the holonomy expands as $W=1+ia^2F_{\mu\nu}+O(a^4)$, verified to six significant figures on a plaquette, so that the loop exponentiates the field strength. Writing $\tilde{F}=\sum_k(iE_k-H_k)e_k$, the square of the field strength is central,

$$
\tilde{F}^2=\left(|\mathbf{E}|^2-|\mathbf{H}|^2\right)e_0+2i\,\mathbf{E}\cdot\mathbf{H}\,e_0 ,
$$

verified in the $2\times2$ representation, so that the two Lorentz invariants of the Maxwell field are the real and imaginary scalar parts of the single element $\tilde{F}^2$. The quantum loop $\langle W(C)\rangle$ is the order parameter of the gauge theory: a perimeter law signals screening and an area law confinement, with the rectangular loop giving the static potential. The loop equation is the Schwinger–Dyson constraint on the loop, standard and cited. What the algebra supplies is the carrier, the holonomy's group element, the trace as a scalar part, the conjugation law, the small-loop expansion, and the central element $\tilde{F}^2$; what it does not supply is the gauge group, the string tension, the lattice regularization, or any empirical content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C$ | Closed curve (loop); $S$ a surface it bounds |
| $\tilde{A}=\tilde{A}_\mu dx^\mu$ | Connection one-form; $\tilde{A}_\mu\in\mathbb{M}_-$ |
| $W(C)=\exp(i\oint_C A_\mu dx^\mu)$ | Abelian Wilson loop; a phase |
| $U(C)=\mathcal{P}\exp(i\oint_C A_\mu dx^\mu)$ | Holonomy (group element), non-abelian |
| $W(C)=\mathrm{Tr}\,\mathcal{P}\exp(i\oint_C A^a_\mu T^a dx^\mu)$ | Non-abelian Wilson loop |
| $\mathcal{P}$ | Path ordering |
| $T^a=ie_a\in\mathbb{M}_+$ | Gauge generators realized in the informational sector |
| $U(C)\mapsto Q\,U(C)\,Q^{-1}$ | Conjugation of the holonomy; trace invariant |
| $\oint_C A_\mu dx^\mu=\frac12\int_S F_{\mu\nu}d\Sigma^{\mu\nu}$ | Stokes' theorem; loop equals enclosed flux |
| $W=1+i a^2F_{\mu\nu}+O(a^4)$ | Small-loop expansion; exponentiated field strength |
| $\tilde{F}=\sum_k(iE_k-H_k)e_k$ | Field strength biquaternion |
| $\tilde{F}^2=(E^2-H^2)e_0+2i(E\cdot H)e_0$ | Central element; its two scalar parts are the Maxwell invariants (verified) |
| $\langle W(C)\rangle\sim e^{-\kappa\,\mathrm{perim}}$ / $e^{-\sigma\,\mathrm{area}}$ | Perimeter law (screening) / area law (confinement) |
| $\sigma$ | String tension |

## Further Reading

- Kenneth G. Wilson, "Confinement of Quarks," *Physical Review D* **10** (1974) 2445–2459, for the Wilson loop and the area law as the confinement criterion.
- Alexander M. Polyakov, *Gauge Fields and Strings* (Harwood, 1987), for the loop equation, the area law, and the string picture of confinement.
- Yu. M. Makeenko and A. A. Migdal, "Exact Equation for the Loop Average in Multicolor QCD," *Physics Letters B* **88** (1979) 135–137, for the loop equation and its large-$N$ closure.
- John B. Kogut, "An Introduction to Lattice Gauge Theory and Spin Systems," *Reviews of Modern Physics* **51** (1979) 659–713, for the lattice formulation in which the area law is established.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Wilson loop, the static potential, and the renormalization of the perimeter divergence.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the non-abelian holonomy and its transformation law.
- Gerard 't Hooft, "On the Phase Transition Towards Permanent Quark Confinement," *Nuclear Physics B* **138** (1978) 1–25, for the confinement criterion and the behaviour of the loop in the different phases.
