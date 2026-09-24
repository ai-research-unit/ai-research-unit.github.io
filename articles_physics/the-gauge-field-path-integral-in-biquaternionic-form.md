# __The Gauge Field Path Integral in Biquaternionic Form__

## Introduction

The functional integral is the series' general apparatus for the quantum theory of a field, and its general properties — the sum over field configurations weighted by $e^{iS}$, the generating functional, the effective action — are treated in the subcategory devoted to them and are not repeated here. The present article does one thing: it specializes the functional integral to the **gauge field**. That specialization is not a matter of substituting one field for another, because the gauge field's functional integral is ill-defined as it stands. The action is invariant along gauge orbits, the integrand is constant along those orbits, and the integral therefore contains an infinite factor — the volume of the gauge group — for every orbit. Making the gauge-field path integral finite is the work of the Faddeev–Popov construction, and it is that construction, in the biquaternion framework, that this article develops.

The construction has three parts. The first is the insertion of a gauge-fixing condition into the integral, together with a compensating determinant — the Faddeev–Popov determinant — whose value is what makes the insertion an identity. The second is the observation that for an abelian gauge field the determinant is field-independent and can be discarded, while for a non-abelian field it depends on the gauge field and must be represented by ghost fields; the non-abelian case is developed in the companion subcategory on gauge fields, and here only the structure is recorded. The third is the evaluation of the resulting Gaussian integral, which produces the propagator and makes explicit the two facts that matter: the gauge-fixing parameter appears only in the longitudinal part of the propagator, so that it drops out of amplitudes built from conserved currents; and the transverse part is a projector that the biquaternion algebra already supplies.

The companion article *Canonical Quantization of the Biquaternion Maxwell Field* reaches the same physics by the canonical route — the Gauss-law constraint, the first-class character of the constraints, the Gupta–Bleuler mode expansion, and the two transverse polarizations — and the treatment of BRST symmetry in this subcategory reaches it by the cohomological route. The path-integral route is the third, and its interest is that the gauge fixing appears there as a **change of variables** rather than as a subsidiary condition or a cohomology, and that the Faddeev–Popov determinant has a biquaternionic identity: for the abelian field it is a constant built from the d'Alembertian, and for the non-abelian field it is a functional of the material potential through the gauge algebra realized in the informational sector.

- Companion article *Canonical Quantization of the Biquaternion Maxwell Field*, for the canonical and Gupta–Bleuler routes to the same two physical polarizations.
- Companion article *The Photon in Biquaternionic Form*, for the massless one-particle state and the helicity content of the transverse directions.
- Companion article *The Path Integral in Biquaternionic Form*, for the sum-over-paths framework of the series.
- Companion article *The Gauge Principle in Biquaternionic Form*, for the gauge transformation, the gauge scalar, and the covariant derivative.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, central $i$, material sector $\mathbb{M}_-$ and informational sector $\mathbb{M}_+$. The gauge potential is the material four-vector $\tilde{A}=iA_0e_0+\mathbf{A}\in\mathbb{M}_-$, the field strength is $\tilde{F}=\bar{\tilde{\nabla}}\tilde{A}-\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$, the d'Alembertian is $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$, and the gauge scalar is $S=\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$. The Lagrangian is $\mathcal{L}=-\tfrac14F_{\mu\nu}F^{\mu\nu}=-\tfrac12\mathrm{Re}\,\mathrm{Sc}(\tilde{F}\bar{\tilde{F}})$, with $\tilde{F}$ the field-strength biquaternion of the Maxwell companion, the series metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$, the series momentum invariant is $p^2=\omega^2-\mathbf{p}^2$, so that $p_\mu p^\mu=-p^2$ and $p_\mu p^\mu=-\mu^2$ is the mass shell, and natural units $\hbar=c=1$ are used for the integral. The integral is over $\tilde{A}$-configurations, the measure being written $\mathcal{D}\tilde{A}$; in components it is the fourfold product of measures for $A_0,A_1,A_2,A_3$. The gauge coupling is $g$ and, where a non-abelian structure is indicated, its generators are realized in $\mathbb{M}_+$ as in the BRST construction.

## The Functional Integral for a Gauge Field

### The Integral and Its Gauge Invariance

The vacuum amplitude for the free Maxwell field is

$$
Z = \int\mathcal{D}\tilde{A}\;e^{iS[\tilde{A}]},
\qquad
S[\tilde{A}] = \int d^4x\left(-\tfrac14F_{\mu\nu}F^{\mu\nu}\right)
= -\tfrac12\int d^4x\;\mathrm{Re}\,\mathrm{Sc}\!\left(\tilde{F}\bar{\tilde{F}}\right),
$$

the second form being the bilinear writing of the companion article. The action depends on $\tilde{A}$ only through $\tilde{F}$, and $\tilde{F}$ is invariant under the gauge transformation

$$
\tilde{A}\;\longmapsto\;\tilde{A}^{\Gamma}=\tilde{A}-\tilde{\nabla}\Gamma,
\qquad
S[\tilde{A}^{\Gamma}] = S[\tilde{A}].
$$

The integration measure is invariant as well, because the transformation is a shift in field space with unit Jacobian: $\mathcal{D}\tilde{A}^{\Gamma}=\mathcal{D}\tilde{A}$. Therefore the integrand is constant on each gauge orbit, the set of $\tilde{A}$ related to one another by a gauge transformation, and the integral factorizes into an integral over the orbit and an integral along it,

$$
Z = \left(\int\mathcal{D}\tilde{A}\;e^{iS[\tilde{A}]}\right)
= \left(\mathrm{Vol}(\mathcal{G})\right)\times
\left(\int_{\text{orbits}}\mathcal{D}\tilde{A}_{\text{rep}}\;e^{iS}\right),
$$

with $\mathrm{Vol}(\mathcal{G})$ the volume of the gauge group — an infinite factor, since there is one gauge transformation for every function $\Gamma$. The factor is not physical, but it is present, and the integral as written cannot be normalized or evaluated mode by mode. This is the pathology that gauge fixing removes, and it is worth noting that it is a property of the measure, not of the action: the same action, integrated over a space of fields in which the gauge orbit is represented once, is finite.

### The Biquaternion Form of the Measure

The measure is a product over the four material components. Because the material sector decomposes as $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0\}\oplus V$ with $V$ the vector part, the measure can be written as a product over the scalar-direction component and the three vector-direction components,

$$
\mathcal{D}\tilde{A} = \mathcal{D}A_0\;\mathcal{D}\mathbf{A},
\qquad
\tilde{A} = iA_0e_0+\sum_{k=1}^{3}A_ke_k ,
$$

with $A_0$ and $A_k$ the real component fields in the $ict$ convention. The gradient part of the gauge transformation is $\tilde{\nabla}\Gamma=e_0\partial_{ict}\Gamma+\sum_ke_k\partial_k\Gamma$, so the orbit direction is spanned by the four derivatives of the single gauge function $\Gamma$; this is why the orbit is one-dimensional at each spacetime point and why a single gauge-fixing condition suffices.

## Gauge Fixing: The Faddeev–Popov Construction

### The Delta Functional and the Determinant

The Faddeev–Popov trick inserts unity into the integral in the form

$$
1 = \Delta[\tilde{A}]\int\mathcal{D}\Gamma\;\delta\!\left(G[\tilde{A}^{\Gamma}]\right),
$$

where $G[\tilde{A}]=0$ is the gauge-fixing condition and $\Delta[\tilde{A}]$ is the Faddeev–Popov determinant, defined by this identity. The determinant depends on $\tilde{A}$ in general. The crucial simplification is that it is **gauge invariant**,

$$
\Delta[\tilde{A}^{\Gamma}] = \Delta[\tilde{A}],
$$

because the composition of two gauge transformations is a gauge transformation. One may therefore shift the integration variable $\tilde{A}\to\tilde{A}^{\Gamma^{-1}}$ at fixed $\Gamma$, use the invariance of the measure and of $\Delta$ and of $S$, and obtain

$$
Z = \int\mathcal{D}\tilde{A}\;\Delta[\tilde{A}]\;\delta\!\left(G[\tilde{A}]\right)\;e^{iS[\tilde{A}]},
$$

in which the gauge-group integral has been absorbed and only the gauge-fixed configurations contribute. This is the content of the construction: the infinite factor has been traded for a delta functional and a determinant, both of which depend on the gauge-fixing condition but neither of which depends on the volume of the gauge group.

### The Abelian Determinant

For the abelian theory the gauge-fixing condition can be taken linear and covariant,

$$
G[\tilde{A}] = \partial_\mu A^\mu-\omega,
\qquad
S=\partial_\mu A^\mu ,
$$

with $\omega$ a fixed function. Under a gauge transformation $S\mapsto S-\Box\Gamma$, so the condition $G[\tilde{A}^\Gamma]=0$ is $S-\Box\Gamma-\omega=0$, i.e., $\Box\Gamma=S-\omega$. The Faddeev–Popov determinant is the Jacobian of the map $\Gamma\mapsto G[\tilde{A}^\Gamma]$, which is the operator $-\Box$ acting on $\Gamma$; the identity $1=\Delta[\tilde{A}]\int\mathcal{D}\Gamma\,\delta(G[\tilde{A}^\Gamma])$ fixes it to be the determinant of that variation, the reciprocal of the factor the delta functional alone would contribute:

$$
\Delta[\tilde{A}] = \det\left(\frac{\delta G[\tilde{A}^\Gamma]}{\delta\Gamma}\right)
= \det\left(-\Box\right),
$$

up to a sign convention. This is **independent of $\tilde{A}$**: it is a constant functional, built from the central scalar d'Alembertian, and it can be absorbed into the normalization of the integral. For the abelian gauge field there are therefore no ghost fields in the path integral: the determinant is a constant, and the gauge-fixing delta functional is all that survives. The result is the biquaternion statement that the Faddeev–Popov determinant of the Maxwell field is a power of the central scalar operator $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$, and that its only biquaternionic content is the centrality of that operator.

The delta functional is represented by introducing the Nakanishi–Lautrup field $B$ and writing

$$
\delta\!\left(\partial_\mu A^\mu-\omega\right)
= \int\mathcal{D}B\;e^{i\int d^4x\,B(\partial_\mu A^\mu-\omega)},
$$

and the $\omega$-dependence is removed by averaging over $\omega$ with the Gaussian weight

$$
w(\omega) = \exp\left(-\frac{i\,\omega^2}{2\xi}\right),
$$

which reproduces the gauge-fixing Lagrangian of the BRST construction. Completing the square in the combined $B,\omega$ integral, $-\omega^2/(2\xi)-B\omega=-\frac{1}{2\xi}(\omega+\xi B)^2+\tfrac{\xi}{2}B^2$, leaves precisely

$$
\mathcal{L}_{\mathrm{gf}} = B\,\partial_\mu A^\mu + \tfrac{\xi}{2}B^2 ,
$$

the term of the BRST companion, and its elimination of $B$ returns $-\tfrac{1}{2\xi}(\partial_\mu A^\mu)^2$, whose momentum-space quadratic form $K^{\mu\nu}=p^2\eta^{\mu\nu}+(1-\xi^{-1})p^\mu p^\nu$ is the one inverted below. The two routes — the canonical subsidiary condition and the path-integral gauge fixing — therefore rejoin at the same Lagrangian.

### The Non-Abelian Determinant

For a non-abelian theory the determinant is not constant. With the gauge-fixing condition $G^a[\tilde{A}]=\partial_\mu A^{a\mu}-\omega^a$, the variation under a gauge transformation is

$$
\frac{\delta G^a[\tilde{A}^\Gamma]}{\delta\Gamma^b} = \partial_\mu(D^\mu)^{ab},
\qquad
(D_\mu)^{ab}=\partial_\mu\delta^{ab}+g f^{abc}A_\mu^c ,
$$

so the determinant is a functional of the potential through the structure constants,

$$
\Delta[\tilde{A}] = \det\left(\partial_\mu D^\mu\right),
$$

and it must be represented by ghost fields: the Gaussian representation of the determinant as an integral over anticommuting $c,\bar{c}$ gives the ghost Lagrangian $-\bar{c}^a\partial_\mu(D^\mu c)^a$ of the BRST construction. The gauge algebra here is realized in the biquaternion framework by the commutator on a subspace of $\mathbb{M}_+$, so the structure constants are those of that realization, and the field-dependence of the determinant is the statement that the gauge algebra is non-abelian. The detailed non-abelian construction — the loop expansion of the determinant, the ghost loops, the renormalization — is the subject of the companion subcategory on gauge fields, and is not repeated here.

## The Gaussian Integral and the Propagator

### The Quadratic Action

With the gauge fixed, the action is quadratic in the potential, and the integral is Gaussian. Writing the gauge-fixed quadratic form in momentum space as

$$
S_2 = \tfrac12\int\frac{d^4p}{(2\pi)^4}\;\tilde{A}_\mu(-p)\,
K^{\mu\nu}(p)\,
\tilde{A}_\nu(p),
\qquad
K^{\mu\nu}(p) = p^2\eta^{\mu\nu} + \left(1-\frac{1}{\xi}\right)p^\mu p^\nu ,
$$

with $\xi$ the gauge parameter, the Gaussian integration gives

$$
Z_2 = \left(\det K\right)^{-1/2}
$$

up to the field-independent factors, so that the two-point function is the inverse of $K$,

$$
D_{\mu\nu}(p) = \frac{1}{p^2}\left(\eta_{\mu\nu}+\frac{(1-\xi)p_\mu p_\nu}{p^2}\right),
$$

the momentum-space propagator. The residue structure is worth separating into its two pieces. The first is the **transverse projector**

$$
P_{\mu\nu} = \eta_{\mu\nu}+\frac{p_\mu p_\nu}{p^2},
\qquad
P^{\mu}{}_\nu = \delta^\mu{}_\nu+\frac{p^\mu p_\nu}{p^2},
$$

which is idempotent, has trace three off shell, and annihilates $p^\nu$:

$$
P^2 = P,
\qquad
\mathrm{tr}\,P = 3,
\qquad
P^{\mu}{}_\nu p^\nu = 0 .
$$

These were verified at two independent off-shell momenta to machine precision. The second is the longitudinal projector $L^{\mu}{}_\nu = -p^\mu p_\nu/p^2$, the complement of $P$, which is what the gauge parameter multiplies,

$$
P+L = \delta,
\qquad
PL = LP = 0,
\qquad
D = \frac{1}{p^2}\left(P+\xi L\right),
\qquad
K = p^2\left(P+\frac{1}{\xi}L\right),
$$

and the orthogonality of the two projectors was verified together with their idempotency and their traces, three and one. The split is the whole content of the gauge-fixing parameter.

### Gauge-Parameter Independence

Because the $\xi$-dependence sits entirely in the longitudinal projector, it cancels between any two gauges when the propagator is contracted with a conserved current. The difference of the propagators at two gauge parameters is proportional to $p_\mu p_\nu$,

$$
D_{\mu\nu}(\xi)-D_{\mu\nu}(\xi') = -\frac{\xi-\xi'}{p^4}\,p_\mu p_\nu ,
$$

and a conserved current satisfies $p_\nu j^\nu=0$, so

$$
\left(D_{\mu\nu}(\xi)-D_{\mu\nu}(\xi')\right)j^\nu = -\frac{\xi-\xi'}{p^4}\,p_\mu\,(p_\nu j^\nu)=0 .
$$

This was verified numerically: with a conserved current $j^\nu=(p_3,0,0,\omega)$ satisfying $p_\nu j^\nu=0$, the contraction of $D(1)-D(3)$ with $j^\nu$ was zero to machine precision at two momenta. The statement is not that the propagator is gauge independent — it is not — but that the piece that depends on the gauge parameter is the piece that a conserved current cannot see. Every amplitude built from the gauge field with external conserved currents, or with the external legs on shell and transverse, is therefore independent of $\xi$. This is the path-integral version of the statement that the gauge fixing is a choice and not a physical input.

The transverse projector is the biquaternion object that the algebra supplies without being asked. Its three off-shell directions are the three directions of the vector part of $\mathbb{M}_-$ orthogonal to the momentum; on shell, for a massless field, the momentum is null, the longitudinal direction of the gauge field lies on the light cone and decouples, and the two remaining directions are the two transverse polarizations of the companion articles. The count two is not visible in the trace of $P$ off shell; it emerges on shell, where one of the three directions is removed by the gauge structure and the positivity of the physical subspace. The massive Proca field is the case in which the longitudinal direction is retained and the count is three, as the preceding articles develop.

### The Generating Functional with a Source

The Gaussian integral is fixed in full by adding a source. With the gauge fixed, the action is $S_2+\int J^\mu A_\mu$ and the integral

$$
Z[J] = \int\mathcal{D}\tilde{A}\;\exp\left(iS_2[\tilde{A}]+i\int d^4x\,J^\mu A_\mu\right)
= \left(\det K\right)^{-1/2}\exp\left(-\frac{i}{2}\int\frac{d^4p}{(2\pi)^4}J^\mu(-p)D_{\mu\nu}(p)J^\nu(p)\right)
$$

is evaluated by completing the square, the shift $A_\mu\to A_\mu+D_{\mu\nu}J^\nu$ being the only ingredient beyond the definition of $D$ as the inverse of $K$. The two-point function is read off by differentiating twice with respect to the source,

$$
\langle 0|\,T\,A_\mu(x)A_\nu(y)\,|0\rangle
= -\frac{\delta^2\ln Z[J]}{\delta J^\mu(x)\,\delta J^\nu(y)}\Big|_{J=0}
= i\,D_{\mu\nu}(x-y),
$$

the second equality using $\ln Z=-\frac{i}{2}\int JDJ$, so that $\delta^2\ln Z/\delta J\delta J=-iD$ and the time-ordered product carries the overall $i$ that the $i\epsilon$ prescription supplies — the same $i$ that the scalar companion's $\Delta_F(p)=i/(p^2-\mu^2+i\epsilon)$ displays. So the propagator is the inverse of the quadratic form, times that overall $i$ and nothing else — the inverse itself being the object used above. The source identity also makes the gauge-parameter cancellation concrete: the $J$-dependent part of $\ln Z[J]$ involves $J^\mu D_{\mu\nu}J^\nu$, whose $\xi$-dependent piece is proportional to $(J^\mu p_\mu)(p_\nu J^\nu)$ and therefore vanishes for a conserved source. In this form the cancellation is an identity at the level of the generating functional rather than a statement about individual amplitudes, and the Ward identity is its statement in the quantum theory.

## The Measure, the Ghosts, and What Is Being Summed Over

The path integral sums over material-sector field configurations, and the gauge transformation is a shift along the orbit generated by $\tilde{\nabla}\Gamma$. Three structural remarks situate the construction in the framework.

First, the measure is a measure on the material sector $\mathbb{M}_-$, the sector of real vector and imaginary scalar components. There is no sum over the informational sector in the free gauge-field integral: the informational sector appears only when a non-abelian gauge algebra is realized, through the generators, and then through the ghost fields. In this precise sense the non-abelian gauge-field path integral is a construction that couples the two fixed-point sectors, and the abelian one is not.

Second, the Faddeev–Popov determinant is a functional of the potential that is built from the gauge algebra and the d'Alembertian. For the abelian case it is $\det(-\Box)$, a power of the central scalar operator. For the non-abelian case it is $\det(\partial\cdot D)$, and the covariant derivative involves the structure constants of the algebra realized in the informational sector. The biquaternion content of the determinant is thus exhausted by two facts: the centrality of $\Box$ and the realization of the gauge algebra by the commutator.

Third, the ghosts that represent the non-abelian determinant are Grassmann-odd, and the algebra has no odd elements; they live in the Grassmann envelope of the BRST construction. The path integral over the gauge field alone is an integral over $\mathbb{M}_-$-valued configurations, but the full gauge-fixed integral is over the envelope.

The gauge-fixing condition itself has a natural biquaternionic form. The gauge scalar $S=\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ is what a gauge transformation shifts, $S\mapsto S-\Box\Gamma$, and the covariant condition $\partial_\mu A^\mu=0$ is the statement that this scalar vanishes. A gauge choice is therefore a choice of value for the scalar part of $\bar{\tilde{\nabla}}\tilde{A}$ at each point, and the delta functional $\delta(\partial_\mu A^\mu-\omega)$ is a delta on that scalar. The canonical companion arrives at the same condition as a constraint — the Gauss law, which is first class and generates the gauge transformations — and the path-integral route arrives at it as a gauge-fixing function; the two are the same scalar, and the choice of gauge is the choice of its value.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The material sector as the space integrated over, with its decomposition into a scalar direction and a three-dimensional vector part; the field strength and the gauge scalar; the gauge transformation as a gradient shift and the invariance of the action; the centrality of $\Box$, which makes the abelian Faddeev–Popov determinant a constant; the transverse projector $P$, its idempotency, its trace and its transversality; and the realization of the gauge algebra in the informational sector, on which the non-abelian determinant depends.

**Imported, and left visible.** The functional-integral framework itself (the subcategory on generalities); the Faddeev–Popov trick and the delta-functional insertion; the Nakanishi–Lautrup auxiliary field and the Gaussian average over the gauge-fixing function; the Gaussian evaluation of the quadratic integral and the determinant factors; the ghost representation of the non-abelian determinant, with the Grassmann envelope; the gauge-parameter independence of amplitudes, which is the standard Ward-identity statement; and the non-abelian construction in its detail.

**Not supplied.** The choice of gauge-fixing condition and of the gauge parameter; the gauge group; the odd coordinates; the continuation to Euclidean signature and the convergence of the integral, which are properties of the general framework; and any empirical content. The path integral makes the gauge fixing a change of variables and thereby exhibits its unphysical character; it does not derive the gauge field or the gauge group.

## Open Questions

1. **A measure intrinsic to the material sector.** The measure is written in components. Is there a biquaternion measure — built from the trace form or the norm form, with the right transformation properties — that makes the fourfold component structure a single object, and does it treat the two fixed-point sectors differently?

2. **The abelian determinant as a central operator.** For the Maxwell field the Faddeev–Popov determinant is $\det(-\Box)$, a power of a central scalar. Is there a sense in which the whole abelian gauge-fixing problem is the statement that $\Box$ is central, so that the gauge-fixing delta functional and the determinant are the only objects the algebra produces without extra input?

3. **The gauge-fixing condition as a scalar part.** The natural gauge-fixing function is $G[\tilde{A}]=S=\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$, the gauge scalar. Choosing a gauge is choosing a value for the scalar part of $\bar{\tilde{\nabla}}\tilde{A}$. Is there a biquaternionic characterization of the gauges that are algebraically natural, and do they include the Lorentz-covariant gauges?

4. **The origin of the gauge parameter.** The gauge parameter multiplies the longitudinal projector and cancels in physical amplitudes. Is there an algebraic statement of the cancellation — an identity in the algebra's bilinear form — that does not require the external currents to be conserved?

5. **The non-abelian determinant and the realized algebras.** The determinant depends on the gauge algebra through the structure constants. Since the algebras realizable inside $\mathbb{B}$ are constrained by the finite dimension, does the path integral's structure select among them, or is the selection entirely empirical?

6. **Empirical content.** As everywhere, whether the gauge-field path integral in biquaternionic form yields any prediction distinguishing the framework from standard gauge theory. It does not.

## Summary

The functional integral over a gauge field is ill-defined as it stands, because the action and the measure are invariant along gauge orbits and the integral contains the infinite volume of the gauge group. The Faddeev–Popov construction inserts a gauge-fixing condition together with a determinant, $\Delta[\tilde{A}]$, which is gauge invariant; after a shift of the integration variable the integral becomes $\int\mathcal{D}\tilde{A}\,\Delta[\tilde{A}]\,\delta(G[\tilde{A}])\,e^{iS[\tilde{A}]}$, finite and normalized.

In the biquaternion framework the potential is a material-sector four-vector, the measure is a product over the scalar and vector directions of $\mathbb{M}_-$, and the gauge transformation is the gradient shift $\tilde{A}\mapsto\tilde{A}-\tilde{\nabla}\Gamma$. For the abelian field the Faddeev–Popov determinant is the determinant of the central scalar d'Alembertian, $\Delta=\det(-\Box)$, independent of the potential; it is a constant and no ghosts appear. For the non-abelian field it is $\Delta=\det(\partial\cdot D)$, a functional of the potential through the gauge algebra realized in the informational sector $\mathbb{M}_+$, and it is represented by Grassmann-odd ghosts living in the envelope of the algebra. The division between the two cases is the abelian–non-abelian division, and the biquaternion content of the determinant is exhausted by the centrality of $\Box$ and the realization of the algebra by the commutator.

The gauge-fixed quadratic action is Gaussian, and its inverse is the propagator $D_{\mu\nu}=p^{-2}(\eta_{\mu\nu}+(1-\xi)p_\mu p_\nu/p^2)$. The transverse projector $P_{\mu\nu}=\eta_{\mu\nu}+p_\mu p_\nu/p^2$ is idempotent, of trace three off shell, and annihilates the momentum; the gauge parameter multiplies only the longitudinal projector. Because the difference of two propagators is proportional to $p_\mu p_\nu$, it vanishes when contracted with a conserved current, and the gauge-parameter dependence drops out of physical amplitudes. On shell the longitudinal direction decouples for the massless field and the two transverse polarizations remain. What the algebra supplies is the carrier, the gauge transformation, the centrality that makes the abelian determinant constant, and the transverse projector; what it does not supply is the gauge group, the gauge parameter, the odd coordinates, the general functional-integral apparatus, or any empirical content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{D}\tilde{A}$ | Measure on $\mathbb{M}_-$-valued configurations; $\mathcal{D}A_0\,\mathcal{D}\mathbf{A}$ in components |
| $S[\tilde{A}]=\int d^4x\,(-\tfrac14F_{\mu\nu}F^{\mu\nu})=-\tfrac12\int\mathrm{Re}\,\mathrm{Sc}(\tilde{F}\bar{\tilde{F}})$ | Gauge-field action, component and bilinear forms |
| $\tilde{A}^\Gamma=\tilde{A}-\tilde{\nabla}\Gamma$, $S[\tilde{A}^\Gamma]=S[\tilde{A}]$ | Gauge transformation and invariance of the action |
| $\mathrm{Vol}(\mathcal{G})$ | Infinite gauge-group volume; the pathology of the naive integral |
| $G[\tilde{A}]=\partial_\mu A^\mu-\omega$ | Gauge-fixing condition |
| $1=\Delta[\tilde{A}]\int\mathcal{D}\Gamma\,\delta(G[\tilde{A}^\Gamma])$ | Faddeev–Popov identity |
| $\Delta[\tilde{A}]$ | Faddeev–Popov determinant; gauge invariant |
| $\Delta=\det(-\Box)$ (abelian) | Field-independent determinant; no ghosts |
| $\Delta=\det(\partial\cdot D)$ (non-abelian) | Field-dependent determinant; ghosts required |
| $(D_\mu)^{ab}=\partial_\mu\delta^{ab}+gf^{abc}A_\mu^c$ | Covariant derivative in the adjoint representation |
| $B$ | Nakanishi–Lautrup field representing the delta functional |
| $\xi$ | Gauge parameter; multiplies the longitudinal projector |
| $K^{\mu\nu}=p^2\eta^{\mu\nu}+(1-1/\xi)p^\mu p^\nu$ | Gauge-fixed quadratic form; $K=p^2(P+L/\xi)$ |
| $D_{\mu\nu}=p^{-2}(\eta_{\mu\nu}+(1-\xi)p_\mu p_\nu/p^2)$ | Gauge-field propagator; $D=p^{-2}(P+\xi L)$ |
| $P_{\mu\nu}=\eta_{\mu\nu}+p_\mu p_\nu/p^2$, $P^2=P$, $\mathrm{tr}P=3$, $P_{\mu\nu}p^\nu=0$ | Transverse projector (verified) |
| $L^{\mu}{}_\nu=-p^\mu p_\nu/p^2$, $L^2=L$, $\mathrm{tr}L=1$, $P+L=\delta$, $PL=LP=0$ | Longitudinal projector; carries the gauge parameter |
| $(D(\xi)-D(\xi'))_{\mu\nu}j^\nu=0$ for $p_\nu j^\nu=0$ | Gauge-parameter independence for conserved currents (verified) |

## Further Reading

- C. Becchi, A. Rouet and R. Stora, "Renormalization of Gauge Theories," *Annals of Physics* **98** (1976) 287–321, for the nilpotent symmetry of the gauge-fixed Lagrangian and the cohomological route.
- T. Kugo and I. Ojima, "Local Covariant Operator Formalism of Non-Abelian Gauge Theories and Quark Confinement Problem," *Progress of Theoretical Physics Supplement* **66** (1979) 1–130, for the physical-state condition and the cohomology of the BRST charge.
- L. D. Faddeev and V. N. Popov, "Feynman Diagrams for the Yang–Mills Field," *Physics Letters B* **25** (1967) 29–30, for the gauge-fixing identity and the determinant.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the functional-integral quantization of gauge fields, the gauge-fixing parameter, and the Ward identities.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Faddeev–Popov procedure, the gauge-fixed propagator, and the transverse projector.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Gaussian functional integral, the determinant factors, and the covariant-gauge propagators.
- L. D. Faddeev, "Feynman Integral for Singular Lagrangians," *Theoretical and Mathematical Physics* **1** (1969) 1–13, for the functional-integral treatment of gauge degeneracy.
- John C. Taylor, *Gauge Theories of Weak Interactions* (Cambridge, 1976), for the gauge-parameter independence of physical amplitudes and the Ward–Slavnov–Taylor identities.
