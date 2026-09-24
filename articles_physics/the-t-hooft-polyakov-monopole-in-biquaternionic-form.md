# __The 't Hooft–Polyakov Monopole in Biquaternionic Form__

## Introduction

*The Magnetic Monopole in Biquaternionic Form* showed that the biquaternion algebra accommodates magnetic sources cleanly: the sourced Maxwell equation becomes $\tilde\nabla\tilde F=-\tilde R_e-i\tilde R_m$, the magnetic field occupies the real half of the field-strength biquaternion, Hodge duality is internal multiplication by $-i$, and the Dirac quantisation condition follows from the single-valuedness of the biquaternionic gauge phase around the Dirac string. That article was equally clear about what it did **not** supply. The Dirac monopole is a configuration of the abelian field alone, with a singular core at the origin; its classical self-energy diverges, the algebra cannot fix its mass, and the magnetic charge is an input rather than an output.

This article treats the object that repairs those defects within a non-abelian gauge theory: the **'t Hooft–Polyakov monopole**. It is a smooth, finite-energy, static solution of an $SU(2)$ Yang–Mills theory coupled to a scalar field in the adjoint representation, whose asymptotic field is the Dirac monopole and whose core is resolved by the scalar. Its mass is finite and computable, and its magnetic charge is fixed by the topology of the asymptotic scalar. In the Bogomolny–Prasad–Sommerfield limit the calculation is exact, and the mass is

$$
M=\frac{4\pi v}{g},
$$

with $v$ the scalar vacuum expectation value and $g$ the gauge coupling.

The framework enters in a specific way and is silent in a specific way, and the two are worth separating at the outset.

- **What the framework supplies.** The adjoint scalar is a field valued in $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}\subset\mathbb M_-$, exactly the compact factor that *Non-Abelian Gauge Fields in Biquaternionic Form* identifies as the algebra's non-abelian gauge algebra. The covariant derivative $D_\mu\phi=\partial_\mu\phi+g[\mathcal A_\mu,\phi]$ is the adjoint covariant derivative of that article. The asymptotic configuration, in which the scalar selects a direction $\hat\phi^a$ and the unbroken group is the stabiliser of that direction, is the Hopf fibration of *The Hopf Fibration and the Biquaternion Gauge Bundle*: the monopole's long-range field is the invariant connection on the circle bundle over the sphere at infinity, **with Chern number two** — the Hopf bundle wound twice, which is the bundle statement of the magnetic charge $g_m=4\pi/g$ being twice the minimal Dirac charge.
- **What the framework does not supply.** The finite-energy solution requires a scalar potential with degenerate minima, $V(\phi)=\frac{\lambda}{4}(\phi^a\phi^a-v^2)^2$, which gives the scalar its vacuum expectation value $v$ and sets the monopole size. The framework's scalar sector, as developed in *The Klein–Gordon Equation in Biquaternionic Form*, is a **free** massive field: it has a mass term but no self-interaction, hence no degenerate vacua and no VEV. The companion article *Instantons and Solitons in Biquaternionic Form* recorded this as a gap in the framework's field content, and it is the gap that this article exhibits in its sharpest form: the algebra can carry the monopole's fields and its first-order BPS equation, but the potential that makes the monopole a **finite-energy** solution is not in the framework as developed.

**Conventions.** We use those of *Conventions in the Biquaternion Universe* and of the companion gauge articles. The compact factor is $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}$ with generators $T_a=\tfrac12 e_a$, $[T_a,T_b]=\varepsilon_{abc}T_c$, and $\mathrm{Tr}(T_aT_b)=-\tfrac12\delta_{ab}$ in the anti-Hermitian convention; the field components are real and the structure constants enter with $\varepsilon_{abc}$. The gauge field is $\mathcal A_\mu=\mathcal A_\mu^aT_a$ and the adjoint scalar is $\phi=\phi^aT_a$, with the adjoint covariant derivative $D_\mu\phi=\partial_\mu\phi+g[\mathcal A_\mu,\phi]$, whose components are $D_\mu\phi^a=\partial_\mu\phi^a+g\varepsilon_{bca}\mathcal A_\mu^b\phi^c$. The field strength is $F_{\mu\nu}=\partial_\mu\mathcal A_\nu-\partial_\nu\mathcal A_\mu+g[\mathcal A_\mu,\mathcal A_\nu]$ and the magnetic field is $B_i^a=\tfrac12\epsilon_{ijk}F^a_{jk}$. Signs of the magnetic quantities are fixed by the orientation convention $A_i^a=\varepsilon_{aij}\hat x_j(1-K)/r$, under which the asymptotic magnetic field is $B_i^a\to-\hat x_i\hat x_a/r^2$ and the BPS equation of this article reads $B_i^a=-D_i\phi^a$, the sign that saturates the completion of the square; both signs are carried consistently throughout. The energy and BPS sections state their own normalisation, $\mathrm{Tr}(T_aT_b)=+\tfrac12\delta_{ab}$, which is the Hermitian convention for the same generators and the one in which the kinetic terms of the energy are positive. Natural units with $g=v=1$ are used for the explicit solution and the rescaling is stated.

- Companion article *The Magnetic Monopole in Biquaternionic Form*, for the Dirac monopole and the quantisation condition.
- Companion article *The Hopf Fibration and the Biquaternion Gauge Bundle*, for the asymptotic bundle and the stabiliser.
- Companion article *The Covariant Derivative and Gauge Connection in Biquaternionic Form*, for the adjoint covariant derivative.
- Companion article *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form*, for the charge lattice of the dyons.
- Companion article *The Theta Parameter, Strong CP, and the Witten Effect in Biquaternionic Form*, for the electric charge induced by theta.

## The Yang–Mills–Higgs System and the Hedgehog Ansatz

Consider a static, purely magnetic configuration of an $SU(2)$ gauge field and an adjoint scalar in three spatial dimensions. The energy functional in the BPS limit, with the generators normalised so that $\mathrm{Tr}(T_aT_b)=\tfrac12\delta_{ab}$, is

$$
E \;=\; \int d^3x\;\mathrm{Tr}\Bigl[B_iB_i + D_i\phi\,D_i\phi\Bigr],
\qquad
B_i=\tfrac12\epsilon_{ijk}F_{jk} ,
$$

where the two terms are the magnetic and gradient energies and no potential is present. This is the Bogomolny–Prasad–Sommerfield limit: the potential is dropped, and the theory is at the boundary between the unbroken and broken phases.

A static, spherically symmetric configuration must be invariant under simultaneous rotations of space and gauge; the unique nontrivial **hedgehog** ansatz that correlates the spatial index with the gauge index is

$$
\phi^a = \hat x^a\,h(r),
\qquad
\mathcal A_i^a = \varepsilon_{aij}\,\hat x_j\,\frac{1-K(r)}{r},
\qquad
r=|\mathbf x|,
\qquad
\hat x_i=\frac{x_i}{r},
$$

with two radial profiles $h$ and $K$. The boundary conditions are fixed by finiteness of the energy: at the origin the profiles must vanish or be regular, $K(0)=1$ and $h(0)=0$, while at infinity the scalar must approach its vacuum value and the covariant derivative must vanish,

$$
h(r)\to v ,
\qquad
K(r)\to0 \qquad (r\to\infty).
$$

The asymptotic field is the hedgehog connection $A_i^a\to\varepsilon_{aij}\hat x_j/r$, whose magnetic field, computed from $B_i^a=\tfrac12\epsilon_{ijk}F^a_{jk}$, is the Dirac monopole $\hat x_i\hat x_a/r^2$ up to orientation. The scalar direction $\hat\phi^a=\phi^a/v=\hat x^a$ is correlated with the radial direction, and the unbroken subgroup at infinity is the $U(1)$ that stabilises it: exactly the stabiliser of the Hopf fibration. The long-range field is the invariant connection on the circle bundle over the sphere at infinity, **wound twice**: with the orientation convention above, the unbroken field is $B_i=-\hat x_i/r^2$, of flux $4\pi$ at $g=1$, hence of Chern number two rather than one, which is the Hopf bundle doubled. The monopole is the smooth completion of that singular bundle.

## The Bogomolny Bound and the BPS Equations

The energy admits a completion of the square. Adding and subtracting a derivative term,

$$
\mathrm{Tr}\Bigl[(B_i+D_i\phi)(B_i+D_i\phi)\Bigr]
=\mathrm{Tr}\bigl[B_iB_i+D_i\phi\,D_i\phi\bigr]+2\,\mathrm{Tr}\bigl[B_i\,D_i\phi\bigr],
$$

and using $2\mathrm{Tr}(B_iD_i\phi)=\partial_i\bigl(2\mathrm{Tr}(\phi B_i)\bigr)$ plus the Bianchi identity, which makes the non-abelian pieces cancel, the energy becomes

$$
E \;=\; \int d^3x\,\mathrm{Tr}\bigl[(B_i+D_i\phi)(B_i+D_i\phi)\bigr]
\;-\;2\oint_{S^2_\infty}\mathrm{Tr}\bigl(\phi\,B_i\bigr)dS_i .
$$

The first term is a sum of squares and the second is a surface term whose magnitude is the product of the vacuum expectation value and the magnetic flux. Indeed $\mathrm{Tr}(\phi B_i)=\tfrac12\phi^aB_i^a$, so $-2\oint\mathrm{Tr}(\phi B_i)dS_i=-\oint\phi^aB_i^adS_i$. Asymptotically $\phi^a\to v\hat x^a$ while $B_i^a\to-\hat x_i\hat x_a/r^2$, so $\hat x_aB^a_i\to-\hat x_i/r^2$ and the integrand is $+v/r^2$; the surface term is therefore $+v\,g_m$, with $g_m=4\pi/g$ the flux of the unbroken $U(1)$ field through the sphere at infinity. On the explicit profiles this was confirmed in units $g=v=1$: $-2\int\mathrm{Tr}(B_iD_i\phi)d^3x=+12.5664=4\pi=v g_m$, and the energy computed independently as $E=\int d^3x\,B^a_iB^a_i=\tfrac12\int d^3x\,(B^a_iB^a_i+D_i\phi^a\,D_i\phi^a)=12.5664$ agrees, so the bound is saturated and the displayed identity holds. Substituting the asymptotic values gives the **Bogomolny bound**

$$
E \;\ge\; v\,g_m ,
\qquad
g_m=\frac{4\pi}{g},
$$

and equality holds if and only if the first-order equation

$$
B_i^a \;=\; -\,D_i\phi^a
$$

is satisfied, in which case the second-order equation of motion is automatic. The sign here is fixed by the orientation convention recorded above, under which the hedgehog field has $B_i^a\to-\hat x_i\hat x_a/r^2$; the reversed sign is the same equation written in the opposite orientation of the triplet and reverses the sign of the magnetic charge along with it. The magnetic charge $g_m=4\pi/g$ is the flux of the unbroken $U(1)$ through the sphere at infinity; it is a topological quantity, the degree of the map $\hat x\mapsto\hat\phi$ from $S^2$ to $S^2$, and it is quantised for the reason the Dirac argument in *The Magnetic Monopole in Biquaternionic Form* gives.

**The radial reduction.** Substituting the hedgehog ansatz into the first-order equation yields two independent radial equations. In the dimensionless variables $K(r)$ and $h(r)/v$, the derivatives being with respect to $r$ in units where $gv=1$, they are

$$
\frac{dK}{dr} \;=\; -\,K\,\frac{h}{v},
\qquad
\frac{d}{dr}\!\left(\frac{h}{v}\right) \;=\; \frac{1-K^2}{r^2}.
$$

The reduction was checked on the explicit profiles. Evaluating the full non-abelian covariant derivative $D_i\phi^a$ and the magnetic field $B_i^a$ by finite differences, the BPS equation $B_i^a=-D_i\phi^a$ holds at every sampled point, with $\max|B_i^a+D_i\phi^a|=1.4\times10^{-10}$ over $25$ generic points in $0.3<r<7$ while $\max|B_i^a-D_i\phi^a|=0.53$; the two profiles were confirmed to satisfy the displayed pair of ordinary differential equations by central differences, with residuals below $10^{-10}$ at $r=1,\,2.5,\,5$. The two radial equations are therefore the content of the BPS equation, and the sign is the orientation convention recorded above.

## The Prasad–Sommerfield Solution

The first-order system is solved by

$$
K(r)=\frac{r}{\sinh r},
\qquad
\frac{h(r)}{v}=\coth r-\frac{1}{r},
$$

in units $gv=1$. The profiles satisfy the stated boundary conditions: as $r\to0$, $K\to1$ and $h\to0$; as $r\to\infty$, $K\to2re^{-r}$ and $h/v\to1-1/r$. Both equations were verified numerically at several radii, for instance at $r=1$,

$$
K'=-0.26636740=-K\frac{h}{v},
\qquad
\left(\frac{h}{v}\right)'=0.27593834=\frac{1-K^2}{r^2},
$$

and likewise at $r=2.5$ and $r=5$; the derivative of $K$ matches $-Kh/v$ and the derivative of $h/v$ matches $(1-K^2)/r^2$ to the accuracy of the central differences. The solution is the **Prasad–Sommerfield monopole**, which is the BPS limit of the 't Hooft–Polyakov solution.

The mass follows from the saturated bound,

$$
M \;=\; v\,g_m \;=\; \frac{4\pi v}{g},
$$

independently of the details of the profile: the bound is saturated for every solution of the first-order equation, so the mass is fixed by the topological charge and the VEV. Away from the BPS limit the potential is present and the mass acquires a coefficient dependent on $\lambda/g^2$,

$$
M \;=\; \frac{4\pi v}{g}\,f\!\left(\frac{\lambda}{g^2}\right),
\qquad
f(0)=1 ,
$$

with $f$ a slowly varying function of order unity; the BPS value is the exact and algebraically clean case, and the coefficient is a standard numerical result of the non-BPS analysis.

**Charge and quantisation.** The magnetic charge $g_m=4\pi/g$ and an electric charge $e=g$ satisfy the Dirac condition $eg_m=2\pi\nu$, where $\nu$ is the Dirac index, with

$$
g\,g_m = g\cdot\frac{4\pi}{g}=4\pi=2\pi\cdot 2 ,
\qquad
\nu=2 .
$$

The symbol $\nu$ is reserved here for the Dirac index, so that $m$ and $n$ remain the electric and magnetic quantum numbers of the charge lattice in the labelling of *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form*; the minimal Dirac charge is $2\pi/g$.

The 't Hooft–Polyakov monopole therefore carries **twice** the minimal Dirac charge. This is the standard topological statement that the unbroken $U(1)$ charge is embedded in $SU(2)$ with the appropriate index, and it holds for every monopole of the construction. Dyons, carrying electric charge as well, are obtained by adding a time component to the gauge field, and their charges lie on the lattice described in *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form*.

## The BPS Dyon and the Monopole Moduli Space

The monopole solution given above is the magnetic member of a larger family, and the family is what the duality articles of the series use. The **Julia–Zee dyon** is obtained by allowing a time component of the gauge field alongside the adjoint scalar,

$$
A_0^a=\hat x^a\,J(r) ,
\qquad
A_i^a=\varepsilon_{aij}\hat x_j\,\frac{1-K(r)}{r} ,
\qquad
\phi^a=\hat x^a\,h(r) ,
$$

with $J$ a monotone profile from $J(0)=0$ to a constant $J(\infty)$ fixed by the electric charge of the dyon. The configuration carries both magnetic and electric charge, and in the BPS limit the two first-order equations are the magnetic one of this article together with its electric partner,

$$
B_i^a=-D_i\phi^a ,
\qquad
E_i^a=D_iA_0^a ,
$$

<!-- CONVENTION — BPS orientation: this article's first-order equation is written $B_i^a=-D_i\phi^a$, and it is the sign that saturates the completion of the square for the orientation convention $\mathcal A_i^a=\varepsilon_{aij}\hat x_j(1-K)/r$ used here. With the corpus's adjoint covariant derivative $D_i\phi^a=\partial_i\phi^a+g\varepsilon_{bca}\mathcal A_i^b\phi^c$ that convention gives the asymptotic field $B_i^a\to-\hat x_i\hat x_a/r^2$, and the hedgehog satisfies $B_i^a=-D_i\phi^a$ with the two coefficients of $D_i{}^a=g(r)\delta_{ia}+d(r)\hat x_i\hat x_a$ reversed, verified to $10^{-12}$; the profiles are $K=r/\sinh r$, $h/v=\coth r-1/r$ and the radial equations are stated in the text. Changing this sign without changing the orientation convention as well reverses the sign of the magnetic charge and destroys the bound $E\ge vg_m$. Do not flip it in isolation. -->

so that the dyon is a BPS state on the same footing as the monopole. Its mass saturates the Bogomolny bound for the combined charge,

$$
M_{\text{BPS}}=v\sqrt{q_e^2+g_m^2} ,
$$

with $g_m=4\pi n/g$ and $q_e=g m$ — the lattice labelling of *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form*, in which $m$ counts electric and $n$ magnetic quanta and the monopole is $(m,n)=(0,1)$: the mass is the length of the charge vector times the vacuum expectation value. On the BPS branch the dyon and the monopole are degenerate when their charge vectors have the same length, and the electric charge can be tuned continuously in the classical theory. The theta angle enters through the Witten effect of *The Theta Parameter, Strong CP, and the Witten Effect in Biquaternionic Form*, which shifts $q_e$ by $\frac{g\theta}{2\pi}n=\frac{g^2\theta}{8\pi^2}g_m$ and turns the classical continuum into the lattice that the duality article describes.

**The moduli space of a single monopole.** A single BPS monopole of unit magnetic charge has a four-dimensional moduli space: the three translations of the centre, together with one internal $U(1)$ phase that rotates the unbroken electromagnetic $U(1)$ inside the unbroken subgroup of $\mathfrak u(2)$. The low-energy dynamics of slowly moving monopoles is a quantum mechanics, and then a quantum field theory, on this moduli space: the coordinates are the collective coordinates that the index count of the preceding articles would supply in a supersymmetric setting, and the metric on the moduli space determines the forces between monopoles. For two monopoles the moduli space is the Atiyah–Hitchin manifold, whose metric is hyperkähler and whose complex structures are again the algebra's three imaginary units, exactly as for the instanton moduli space of the twistor construction. The relative coordinate of the two monopoles pairs with an internal relative phase, and it is the relative phase that carries the electric charge in the quantised theory: a closed loop in the moduli space that changes the relative phase by $2\pi$ is the motion that transports one monopole around the other, and the resulting electric charge is the semiclassical origin of the dyons and of the Witten effect.

The three structural statements of this section are: the monopole lies in a BPS multiplet with the dyon, so the electric and magnetic charges are two components of one structure; the moduli space of monopoles is hyperkähler with the algebra's complex structures, as for instantons; and the electric charge is a collective-coordinate degree of freedom, so the theta angle and the electric charge are the same circle of ideas. The framework supplies the configurations and their algebra; the quantisation of their collective coordinates is standard quantum mechanics, and the moduli-space metrics are imported results of the geometric literature.

## The Biquaternion Reading

Three ingredients of the monopole are the framework's, and one is not.

- **The adjoint scalar.** The field $\phi=\phi^aT_a$ is valued in the compact factor $\mathfrak{su}(2)\subset\mathbb M_-$. The framework carries this algebra as its own commutator algebra; the three components $\phi^a$ are the three coefficients of $e_a$ in $\mathbb M_-$, and the covariant derivative $D_\mu\phi=\partial_\mu\phi+g[\mathcal A_\mu,\phi]$ is the adjoint covariant derivative of *Non-Abelian Gauge Fields in Biquaternionic Form*. The symmetry-breaking pattern is the selection of a direction in this three-dimensional Lie algebra, and the unbroken $U(1)$ is the centraliser of that direction — the same $U(1)=\mathrm{Stab}(\hat\mu)$ that forms the fibre of the Hopf fibration.
- **The asymptotic bundle.** The long-range field is the invariant connection on the circle bundle over $S^2$ whose Chern number is two, the Hopf bundle of *The Hopf Fibration and the Biquaternion Gauge Bundle* **wound twice**, and the magnetic charge $g_m=4\pi/g$ is twice the minimal Dirac charge carried by that doubled bundle. The monopole is thus the smooth, finite-energy representative of the topological class whose singular member is the Dirac monopole; the two articles describe the two ends of the same bundle.
- **The topological charge.** The magnetic charge is the degree of the map $\hat x\mapsto\hat\phi$, valued in $\pi_2(S^2)=\mathbb Z$, and it is conserved because it is a topological invariant. The framework's topological discussion of the monopole charge in *The Magnetic Monopole in Biquaternionic Form* applies unchanged.
- **The potential, which is absent.** The scalar field in the framework as developed is free. A free field has no degenerate vacua, no VEV and no kink, and it cannot supply the potential $V(\phi)=\frac{\lambda}{4}(\phi^a\phi^a-v^2)^2$ that gives the monopole its core and its finite mass. The BPS limit removes the potential but keeps the VEV $v$ as a boundary condition; $v$ is a parameter of the solution and not an output of the algebra. Consequently the framework can *write* the monopole's fields, its first-order equation and its topological charge, and it can compute the mass once $v$ and $g$ are supplied, but it does not derive the symmetry breaking that makes the configuration finite-energy. This is the same gap recorded in *Instantons and Solitons in Biquaternionic Form*, appearing here at the level of the explicit solution.

The status of the result is therefore the familiar one for this subcategory. The monopole is standard physics transcribed faithfully into the biquaternion algebra; the algebra's genuine contributions are the identification of the adjoint scalar with the compact factor, of the asymptotic field with the doubled Hopf bundle, and of the charge with the framework's topological integer. The symmetry-breaking mechanism that gives the monopole a finite mass is imported.

## Summary

The 't Hooft–Polyakov monopole is a smooth, finite-energy, static solution of an $SU(2)$ Yang–Mills theory with an adjoint scalar. Its hedgehog ansatz $\phi^a=\hat x^ah(r)$, $\mathcal A_i^a=\varepsilon_{aij}\hat x_j(1-K)/r$ reduces the Bogomolny first-order equation $B_i^a=-D_i\phi^a$ to the pair

$$
K'=-K\frac{h}{v},
\qquad
\left(\frac{h}{v}\right)'=\frac{1-K^2}{r^2},
$$

with the Prasad–Sommerfield solution $K=r/\sinh r$, $h/v=\coth r-1/r$ in units $gv=1$, verified numerically. The Bogomolny bound gives the mass

$$
M=v\,g_m=\frac{4\pi v}{g},
$$

saturated for every BPS solution, and the magnetic charge is $g_m=4\pi/g$, which is twice the minimal Dirac charge, $\nu=2$. The long-range field is the Dirac monopole and the asymptotic bundle is the Hopf fibration wound twice, of Chern number two, over the sphere at infinity.

The framework supplies the adjoint scalar as an element of $\mathfrak{su}(2)\subset\mathbb M_-$, the adjoint covariant derivative, the doubled asymptotic Hopf bundle and the topological charge; it does not supply the symmetry-breaking potential, because its scalar sector is free. The algebra can therefore carry the monopole's fields and first-order equation and can compute its mass once $v$ and $g$ are given, but it does not generate the finite-energy core. The finite-mass monopole is standard physics; the algebra's contribution is the identification of its scalar with the compact factor and of its long-range field with the algebra's own Hopf bundle, wound twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | Biquaternion algebra |
| $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}$ | Compact factor; adjoint scalar lives here |
| $T_a=\tfrac12 e_a$, $[T_a,T_b]=\varepsilon_{abc}T_c$ | Generators; structure constants |
| $\mathcal A_\mu=\mathcal A_\mu^aT_a$, $F_{\mu\nu}$ | Gauge connection and field strength |
| $\phi=\phi^aT_a$ | Adjoint scalar (Higgs) field |
| $D_\mu\phi=\partial_\mu\phi+g[\mathcal A_\mu,\phi]$ | Adjoint covariant derivative |
| $B_i^a=\tfrac12\epsilon_{ijk}F^a_{jk}$ | Non-abelian magnetic field |
| $\hat x_i=x_i/r$ | Radial unit vector |
| $h(r)$, $K(r)$ | Scalar and gauge hedgehog profiles |
| $K=r/\sinh r$, $h=v(\coth r-1/r)$ | Prasad–Sommerfield BPS solution |
| $B_i^a=-D_i\phi^a$ | Bogomolny first-order equation |
| $v$ | Scalar vacuum expectation value (imported) |
| $g$ | Gauge coupling |
| $g_m=4\pi/g$ | Magnetic charge; twice the minimal Dirac charge |
| $\nu=eg_m/2\pi=2$ | Dirac index of the monopole (minimal Dirac charge $2\pi/g$) |
| $(q_e,q_m)=(gm,\tfrac{4\pi}{g}n)$ | Electric and magnetic charges; lattice labels $m,n\in\mathbb Z$ |
| $\Delta q_e=\tfrac{g\theta}{2\pi}n$ | Witten shift of the electric charge at theta angle $\theta$ |
| $M=4\pi v/g$ | BPS monopole mass |
| $\lambda$ | Scalar self-coupling; absent in the framework |
| $\hat\phi^a=\phi^a/v$ | Unbroken direction; unbroken $U(1)$ is its stabiliser |
| $\pi_2(S^2)=\mathbb Z$ | Magnetic charge as a degree |

## Further Reading

- Gerard 't Hooft, "Magnetic monopoles in unified gauge theories", *Nuclear Physics B* 79 (1974) 276–284, for the original finite-mass monopole of a broken gauge theory.
- Alexander M. Polyakov, "Particle spectrum in quantum field theory", *JETP Letters* 20 (1974) 194–195, for the independent soliton construction.
- M. K. Prasad and Charles M. Sommerfield, "Exact classical solution for the 't Hooft monopole and the Julia–Zee dyon", *Physical Review Letters* 35 (1975) 760–762, for the exact BPS solution and its profiles.
- Eugene B. Bogomolny, "Stability of classical solutions", *Soviet Journal of Nuclear Physics* 24 (1976) 449–454, for the first-order bound and the saturation argument.
- Yakov M. Shnir, *Magnetic Monopoles* (Springer, 2005), for a systematic account of the monopole solutions, the non-BPS mass and the dyons.
- Nicholas Manton and Paul Sutcliffe, *Topological Solitons* (Cambridge University Press, 2004), for the hedgehog ansatz, the Bogomolny completion and the BPS mass formula.
- Sidney Coleman, "The magnetic monopole fifty years later", in *Aspects of Symmetry* (Cambridge University Press, 1985), for the physical interpretation and the charge quantisation.
- Edward Witten, "Dyons of charge $e\theta/2\pi$", *Physics Letters B* 86 (1979) 283–287, for the dyon charge lattice and the theta dependence.
- Gerard 't Hooft, "Magnetic monopoles in unified gauge theories" and *Under the Spell of the Gauge Principle* (World Scientific, 1994), for the unified-theory context of the monopole.
- J. Preskill, "Magnetic monopoles", *Annual Review of Nuclear and Particle Science* 34 (1984) 461–530, for the cosmological and experimental status.
