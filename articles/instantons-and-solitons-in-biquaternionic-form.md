# __Instantons and Solitons in Biquaternionic Form__

## Introduction

The companion article *Non-Abelian Gauge Fields in Biquaternionic Form* closes with an open question: whether the biquaternion framework supplies a preferred connection with finite action and nonzero topological charge, and whether the zero-divisor structure of $\mathbb{M}_-$ plays any role in it. This article takes that question up. Its subject is **localised finite-energy solutions** of the framework's field equations, and it treats the two families that the phrase covers separately, because they differ in three things at once — signature, boundary conditions, and what makes them stable.

- **Instantons** are **Euclidean** objects. They are defined on the Euclidean continuation of spacetime, they are classified by an integer topological charge, and the classical route to them is the **self-duality** condition $F=\star F$, which replaces the second-order equation of motion by a first-order equation. The word "instanton" is not a synonym for "localised solution of the Lorentzian theory"; an instanton is not a configuration that propagates in time.
- **Solitons** are **Lorentzian** objects. They are static, finite-energy, localised field configurations of the Lorentzian theory. Calling one *stable* is a claim that requires an argument — a conserved topological sector or a Bogomolny bound — and this article gives the argument or records its absence; it does not call a configuration stable for being stationary.

The distinction is not a matter of taste. In Lorentzian signature the Hodge star on two-forms satisfies $\star^2=-1$, so $F=\star F$ forces $F=0$ on real fields: there are no nonzero real self-dual two-forms, and therefore no instantons, in the Lorentzian theory. In Euclidean signature the star satisfies $\star^2=+1$, the six-dimensional space of two-forms splits into a self-dual and an anti-self-dual three-dimensional half, and the instanton exists. The framework's own $ict$ convention makes the point concrete: the factor $i$ in the time coordinate *is* the Lorentzian structure, and the Wick rotation of the companion article — the identification of $\mathbb{M}_-$ with the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ by relabelling $ict$ as a real coordinate — is exactly the passage from the Lorentzian star to the Euclidean one.

The article is organised around four questions, and it keeps the affirmative answers and the gaps apart.

- **The density and its primitivity.** The topological charge is the integral of a density. Section *The Topological Charge and Its Density* writes the density for the abelian and non-abelian cases; Section *The Density Is a Total Derivative* shows that it is a total derivative, which is what makes the charge topological rather than dynamical, and verifies the identity explicitly.
- **What self-duality buys.** Section *Self-Duality in Euclidean Signature* states $F=\star F$, shows that it turns the Bianchi identity into the equation of motion, and derives the Bogomolny bound $S\ge 8\pi^2|Q|/g^2$ that makes the self-dual configurations the minimisers of the action in each topological sector.
- **Do the framework's invariants supply the density?** Section *Do the Framework's Invariants Supply the Density?* checks this against $I_1$ and $I_2$, the two invariants of the field-strength article. The answer is yes in the abelian case — the imaginary part of the norm form *is* the Pontryagin density — and no in the non-abelian case, where the density needs a matrix trace that the framework's rank-two norm form does not supply. The second is stated as a gap.
- **The concrete solution and the soliton gap.** Section *The BPST Instanton and Its Equation of Motion* exhibits the standard $SU(2)$ instanton inside the framework's $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}$ and checks by substitution that it solves the equation of motion. Section *Solitons: What Stability Requires* shows that the framework's only topological charge — the magnetic charge of the monopole article — has no finite-energy configuration to occupy it, so the framework has no soliton of its own; the reasons are stated rather than smoothed over.

**Conventions.** We use those of the companion articles throughout, unchanged. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_1e_2=e_3$, and $i$ is the scalar imaginary, $i^2=-1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb R}\{e_0,ie_0\}$ is the complex scalar subspace, the center of the algebra. The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}}=e_0\partial_{ict}-e_1\partial_x-e_2\partial_y-e_3\partial_z$, and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}$. The abelian field strength is $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$ and its invariants are $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$, with $\mathbf{B}=\mu\mathbf{H}$ and $c=1/\sqrt{\epsilon\mu}$. The non-abelian connection and curvature of the parent are $\mathcal{A}_\mu=\mathcal{A}_\mu^a e_a\in\mathfrak{su}(2)$ and $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, with $\kappa=q/\hbar$ and the biquaternion representative $\mathcal{F}=\tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged; where a matrix trace on the gauge factor is meant it is written $\mathrm{Tr}$ and distinguished from it, as the non-abelian article does. Because the two parents use $F_{\mu\nu}$ for the abelian field components and for the non-abelian components, the same symbol is used here with the context made explicit in each section; the biquaternion objects are $\tilde{F}$ in the abelian case and $\mathcal{F}$ in the non-abelian case. Throughout, $\partial_0=\partial_{ict}$ and $\partial_k=\partial_{x_k}$.

## Two Signatures, Two Kinds of Localised Solution

The framework's differential operators are Lorentzian. With the material coordinates $(ict,x,y,z)$,

$$
\tilde{\nabla}=e_0\,\partial_{ict}+e_1\,\partial_x+e_2\,\partial_y+e_3\,\partial_z,
\qquad
\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\partial_x^2+\partial_y^2+\partial_z^2
=-\frac{1}{c^2}\partial_t^2+\nabla^2,
$$

where $\partial_{ict}=\partial/\partial(ict)$, so that $\partial_{ict}^2=-c^{-2}\partial_t^2$. The operator $\Box$ is hyperbolic, its characteristic cone is the zero-divisor cone of $\mathbb{M}_-$, and the Lorentzian field equations of the framework live here. This is the setting for **solitons**.

The **Wick rotation** is the substitution $t\mapsto-i\tau$, under which the material coordinate $\tilde{Q}_-=ict\,e_0+xe_1+ye_2+ze_3$ becomes the real-quaternion element

$$
\tilde{Q}_{\mathbb H}=c\tau\,e_0+x\,e_1+y\,e_2+z\,e_3\in\mathbb{H}_{\mathbb{B}},
$$

and the gradient becomes the **Euclidean gradient**

$$
\tilde{\nabla}_E=e_0\,\partial_{x_4}+e_1\,\partial_{x_1}+e_2\,\partial_{x_2}+e_3\,\partial_{x_3},
\qquad
\Box_E=\partial_{x_4}^2+\partial_{x_1}^2+\partial_{x_2}^2+\partial_{x_3}^2,
$$

with $x_4=c\tau$ and the four real coordinates $(x_4,x_1,x_2,x_3)$. The operator $\Box_E$ is elliptic. This is the setting for **instantons**. The identification of $\mathbb{M}_-$ with $\mathbb{H}_{\mathbb{B}}$ under the rotation is the subject of the companion article *The Wick Rotation in the Biquaternion Universe*; here it matters only that the rotation converts the hyperbolic operator into an elliptic one and the Lorentzian complex structure into a positive-definite real one.

The signature enters the solution theory through the **Hodge star on two-forms**. On the six-dimensional space of two-forms $\star$ is an involution up to a sign,

$$
\star^2=+1 \ \text{(Euclidean)}, \qquad \star^2=-1 \ \text{(Lorentzian)},
$$

and both signs were recomputed directly from the definition $(\star F)_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\rho\sigma}F^{\rho\sigma}$ by applying it twice to each of the six basis two-forms. The consequences are the two facts that organise this article.

- **Euclidean.** Because $\star^2=+1$, the projectors $\tfrac12(1\pm\star)$ split the two-forms into a **self-dual** three-dimensional half and an **anti-self-dual** three-dimensional half, both real. The condition $F=\pm\star F$ is a real, first-order, non-trivial condition. In the component description with $F_{4k}=E_k$ and $F_{jk}=\epsilon_{jkl}B_l$ it reads simply
$$
\text{self-dual} \iff \mathbf{B}=+\mathbf{E},
\qquad
\text{anti-self-dual} \iff \mathbf{B}=-\mathbf{E},
$$
which was checked on a generic field (the two conditions are exact identities in the two opposite cases).
- **Lorentzian.** Because $\star^2=-1$, a real two-form obeying $F=\star F$ obeys $F=\star F=\star^2F=-F$, hence $F=0$. There is no nonzero real self-dual two-form, and the self-dual route to instantons is unavailable in the Lorentzian theory. What *is* available in Lorentzian signature is the complex combination $F\pm i\star F$ — the Riemann–Silberstein halves of the field-strength article — but these are two complex halves of one real field, not independent real solutions.

This is the sharp form of the warning that governs the subject: **an instanton is a Euclidean object.** A configuration obeying $F=\star F$ on the Lorentzian slice would be, on real fields, the zero field, and calling a self-dual Euclidean configuration a solution of the Lorentzian equation of motion would be a defect of signature, not a mild abuse. The framework accommodates both signatures — the algebra $\mathbb{B}$ is the same in both, and the field strength keeps its position in the complex vector part $\mathrm{Vect}(\mathbb{B})$ — but the metric-dependent star, and with it the meaning of the field equation, is not signature-neutral.

The two families are contrasted in the following table.

| | Instanton | Soliton |
|---|---|---|
| Signature | Euclidean ($\star^2=+1$) | Lorentzian ($\star^2=-1$) |
| Coordinates | $(x_4,x_1,x_2,x_3)$ real | $(ict,x,y,z)$ |
| Defining equation | first order, $F=\pm\star F$ | second order, equation of motion |
| Boundary data | finite action; gauge field a map $S^3\to SU(2)$ at infinity | static, finite energy; fields approach vacuum at spatial infinity |
| Charge | Pontryagin number $Q\in\mathbb Z$ | topological sector; e.g. magnetic charge |
| What makes it stable | $Q$ fixed by continuity; Bogomolny bound saturated | a topological sector, or a Bogomolny bound |
| Framework home | the $\mathfrak{su}(2)$ factor inside $\mathbb{M}_-$ | the monopole sector only, and singular |

## The Topological Charge and Its Density

The charge that classifies an instanton is the integral of a four-form built from the field strength. In the non-abelian case, with $F=d\mathcal{A}+i\kappa\,\mathcal{A}\wedge\mathcal{A}$ the curvature of the parent article and $\mathrm{Tr}$ the matrix trace on the gauge factor,

$$
Q \;=\; \frac{1}{8\pi^2}\int_{\mathbb R^4}\mathrm{Tr}\!\left(F\wedge F\right)
\;=\; \frac{1}{8\pi^2}\int_{\mathbb R^4} d^4x\;\frac{1}{4}\,\epsilon^{\mu\nu\rho\sigma}\,\mathrm{Tr}\!\left(F_{\mu\nu}F_{\rho\sigma}\right),
\qquad Q\in\mathbb Z ,
$$

for configurations of finite action. The density is

$$
q(x)= \frac{1}{4}\,\epsilon^{\mu\nu\rho\sigma}\,\mathrm{Tr}\!\left(F_{\mu\nu}F_{\rho\sigma}\right)
= \frac{1}{2}\,\mathrm{Tr}\!\left(F_{\mu\nu}\star F^{\mu\nu}\right),
$$

using the definition of the star. The trace here is the **matrix trace** on the $\mathfrak{su}(2)$ factor, the one the parent article uses for the gauge-invariant density $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$; it is *not* the informational trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, which pairs a Hermitian state with a Hermitian observable, not two gauge-algebra elements. The integer character of $Q$ is the statement that $\pi_3(SU(2))=\mathbb Z$: a finite-action gauge field on $\mathbb R^4$ is classified at infinity by a map from the three-sphere to the gauge group, and the density's integral is the degree of that map. The density is a total derivative, as the next section shows, so $Q$ is unchanged by any continuous deformation of the connection that keeps the boundary data fixed; this is the content of the next section.

In the abelian case the same object collapses to the framework's second invariant. With the field-strength biquaternion $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$ and its components, the density is

$$
\frac{1}{4}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
= \frac{1}{2}\,F_{\mu\nu}\star F^{\mu\nu}
=
\begin{cases}
\dfrac{2i}{c}\,I_2 & \text{(Lorentzian, } ict\text{ convention)},\\[2mm]
2\,I_2 & \text{(Euclidean)},
\end{cases}
\qquad
I_2=\mathbf{E}\cdot\mathbf{B},
$$

which was recomputed symbolically from the component matrix of the field-strength article in both signatures. Thus in the Maxwell sector the topological density *is* a function of the framework's invariant $I_2$ alone; no new invariant is required. That is the affirmative half of the answer to the parent's question, and it is developed in Section *Do the Framework's Invariants Supply the Density?*. The non-abelian density, by contrast, is not a function of $I_2$; it requires the matrix trace and has no norm-form expression, which is the gap of that section.

The parity of the density is worth recording. The quantity $\epsilon^{\mu\nu\rho\sigma}\mathrm{Tr}(F_{\mu\nu}F_{\rho\sigma})$ is a pseudoscalar under the Lorentz group, and in the abelian case it is proportional to $I_2=\mathbf{E}\cdot\mathbf{B}$, which the field-strength article identifies as the pseudoscalar invariant (parity-even $I_1$, parity-odd $I_2$). The topological charge is therefore an integral of a pseudoscalar density; under a parity transformation it changes sign, so it labels an orientation as well as a bundle. This is the standard statement that instantons carry a handedness, and it is the reason the self-dual and anti-self-dual sectors have charges $+1$ and $-1$.

## The Density Is a Total Derivative

The reason the integral $Q$ is topological rather than dynamical is that the density is a total derivative. In the abelian case the identity is elementary. If $F=dA$, then $F\wedge F=d(A\wedge F)$ because $dF=0$, and in components

$$
F_{\mu\nu}\star F^{\mu\nu}=\partial_\mu K^\mu,
\qquad
K^\mu=\epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}.
$$

This identity was verified symbolically, not quoted: taking a general smooth $A_\mu(x)$ in four flat coordinates, forming $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, and computing both sides, one finds

$$
\partial_\mu K^\mu=\frac{1}{2}\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=F_{\mu\nu}\star F^{\mu\nu}
$$

as an identity in the derivatives of $A_\mu$, with every second derivative cancelling. The computation was done first in the flat Euclidean coordinates and then in the $ict$ convention, with the same result; the cancellation of the second derivatives is what the two computations establish. The current $K^\mu$ is **gauge dependent**: under $A_\mu\mapsto A_\mu+\partial_\mu\Gamma$ it changes by a term whose divergence vanishes by the antisymmetry of $\epsilon$ and the Bianchi identity $\partial_{[\mu}F_{\nu\rho]}=0$, so the *density* $\partial_\mu K^\mu$ is gauge invariant even though $K^\mu$ is not. This is why the density can be an observable and the current cannot.

The non-abelian identity is the same statement one integration by parts further along. With $F=d\mathcal{A}+i\kappa\,\mathcal{A}\wedge\mathcal{A}$,

$$
\mathrm{Tr}\!\left(F\wedge F\right)=d\,\Omega_{\mathrm{CS}},
\qquad
\Omega_{\mathrm{CS}}=\mathrm{Tr}\!\left(\mathcal{A}\wedge d\mathcal{A}+\tfrac{2}{3}\,i\kappa\,\mathcal{A}\wedge\mathcal{A}\wedge\mathcal{A}\right),
$$

the Chern–Simons three-form, so the topological charge is a surface integral,

$$
Q=\frac{1}{8\pi^2}\oint_{\partial(\mathbb R^4)}\Omega_{\mathrm{CS}},
$$

and the boundary is the three-sphere at infinity. The total-derivative property is what makes the charge topological in the precise sense: a variation $\delta\mathcal{A}$ that is local and single valued, and that vanishes at infinity, changes the integrand of $Q$ by a total derivative and therefore changes $Q$ by nothing. Only the boundary data — the winding of the gauge function on $S^3_\infty$ — can change $Q$, and that winding is an integer, the degree of a map $S^3\to SU(2)$. The charge is thus insensitive to the local shape of the configuration, depends on no metric, and cannot be changed by any continuous finite-energy deformation; it is a topological invariant in the strict sense. It is in this way that the density being a total derivative, rather than merely being conserved, is what makes the charge **topological rather than dynamical**: a conserved charge would be the integral of a divergence-free current and would forbid only a continuous loss, whereas a total-derivative density means the charge is fixed by the boundary and is blind to everything else.

Two consequences deserve to be stated because they are the traps of the subject.

- **No abelian instanton on $\mathbb R^4$.** For a smooth abelian field of finite action, $A_\mu$ falls off at infinity and $K^\mu$ falls off faster, so the surface term at infinity vanishes and $Q=0$ for every such field. Equivalently, the density integrates to zero on $\mathbb R^4$ (or on its one-point compactification $S^4$, where $H^2(S^4;\mathbb Z)=0$). A nonzero abelian charge requires a nontrivial line bundle, which a four-sphere does not admit; it can occur only on a manifold with nonzero second cohomology, such as $\mathbb{CP}^2$, where the field is not a single globally defined connection. On the framework's flat background, therefore, the Maxwell sector has **no instanton**. Instantons are intrinsically non-abelian, and in this framework they live in the $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}\subset\mathbb{M}_-$ factor, not in the $U(1)$ scalar sector.
- **The charge is metric independent.** The density $\mathrm{Tr}(F\wedge F)$ is built from the field strength and the totally antisymmetric symbol alone; no metric enters. The action $\int\mathrm{Tr}(F\wedge\star F)$, by contrast, uses the star and hence the metric. The charge is therefore the same on any conformally related metric, which is one way to see why the instanton problem is conformally invariant and why the moduli of instantons on $\mathbb R^4$ and on $S^4$ coincide.

## Self-Duality in Euclidean Signature

On the Euclidean slice the self-duality condition is

$$
F_{\mu\nu}=\pm\,\star F_{\mu\nu},
\qquad
\star F_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\rho\sigma}F^{\rho\sigma},
$$

with $\star^2=+1$. It is a first-order differential equation for the connection, and in the component description it reads $\mathbf{B}=\pm\mathbf{E}$ (verified exactly on a generic Euclidean field strength, as recorded above). Its value is that it does two things at once: it implies the equation of motion, and it saturates the action bound in a topological sector.

**Self-duality plus Bianchi implies the equation of motion.** The Bianchi identity $dF=0$ is, in components, $\partial_{[\mu}F_{\nu\rho]}=0$, and it is equivalent to the statement that the *dual* is divergence free,

$$
\partial_\mu\star F^{\mu\nu}=0 .
$$

This was verified symbolically for a general abelian field strength $F=dA$: the divergence of the dual vanishes identically, whereas the divergence of $F$ itself does not. Now if $F=\pm\star F$, then

$$
\partial_\mu F^{\mu\nu}=\pm\,\partial_\mu\star F^{\mu\nu}=0,
$$

so every self-dual finite-action field is automatically a source-free solution of the second-order equation. The non-abelian statement is the same with $\partial_\mu$ replaced by the covariant derivative $D_\mu=\partial_\mu+i\kappa[\mathcal{A}_\mu,\;\cdot\;]$: the Bianchi identity is $D_{[\mu}F_{\nu\rho]}=0$, equivalently $D_\mu\star F^{\mu\nu}=0$, and self-duality turns it into the Yang–Mills equation $D_\mu F^{\mu\nu}=0$. The economy is exact: a second-order equation has been replaced by a first-order one, and every solution of the first-order equation is a solution of the second-order one. The converse is false — not every solution is self-dual — so self-duality selects a distinguished subclass, the one that is also a minimiser, as the next paragraph shows.

**Self-duality saturates the Bogomolny bound.** The pointwise identity

$$
\left|F\mp\star F\right|^2 = 2\,\mathrm{Tr}\!\left(F_{\mu\nu}F^{\mu\nu}\right) \mp 2\,\mathrm{Tr}\!\left(F_{\mu\nu}\star F^{\mu\nu}\right),
$$

was verified symbolically on a generic Euclidean field strength (both signs). The left side is a sum of squares; integrating on $\mathbb R^4$ gives

$$
0\le\int|F\mp\star F|^2
=2\int\mathrm{Tr}\!\left(F_{\mu\nu}F^{\mu\nu}\right)\mp 2\int\mathrm{Tr}\!\left(F_{\mu\nu}\star F^{\mu\nu}\right),
$$

hence

$$
\int\mathrm{Tr}\!\left(F_{\mu\nu}F^{\mu\nu}\right)\;\ge\;\left|\int\mathrm{Tr}\!\left(F_{\mu\nu}\star F^{\mu\nu}\right)\right| = 16\pi^2\,|Q| ,
$$

and therefore, with the Euclidean action $S=\frac{1}{2g^2}\int\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ of the non-abelian sector (Hermitian generators, $\mathrm{Tr}(T_aT_b)=\tfrac12\delta_{ab}$),

$$
S\;\ge\;\frac{8\pi^2}{g^2}\,|Q| ,
$$

with equality if and only if $F=\pm\star F$. The bound is the Bogomolny argument transposed from the Lorentzian soliton to the Euclidean instanton: the *same* completing-the-square mechanism that will be described in Section *Solitons: What Stability Requires* is what makes the instanton the minimiser of the action in its topological sector. Two remarks complete the statement. First, the minimising configuration is stable within the sector: any finite-energy variation that keeps the boundary data fixed keeps $Q$, and the bound says the action cannot fall below $\frac{8\pi^2}{g^2}|Q|$, so the self-dual configuration is the bottom of its sector. Second, the bound is a lower bound, not an existence theorem; the existence of the minimiser is the separate content of the explicit solution of the next section.

## Do the Framework's Invariants Supply the Density?

The field-strength article identifies exactly two independent local, derivative-free invariants of the abelian field, the real and imaginary parts of the norm form

$$
I_1=\mathbf{E}^2-c^2\mathbf{B}^2,
\qquad
I_2=\mathbf{E}\cdot\mathbf{B},
\qquad
N(\tilde{F})=\tilde{F}\bar{\tilde{F}}=-\epsilon\left(I_1+2ic\,I_2\right),
$$

and shows that any other algebraic invariant is a function of these two. The question raised at the start of this article is whether these invariants suffice to build the topological density, or whether the density lies outside the framework's invariant calculus.

**The abelian case: yes.** Section *The Topological Charge and Its Density* established that

$$
F_{\mu\nu}\star F^{\mu\nu}=\frac{4i}{c}\,I_2 \ \ (\text{Lorentzian}),
\qquad
F_{\mu\nu}\star F^{\mu\nu}=4\,I_2 \ \ (\text{Euclidean}),
$$

both recomputed from the component convention of the field-strength article. So the imaginary part of the norm form, which is $I_2$, *is* the Pontryagin density up to the stated constant. The framework does not need a new invariant to write the abelian topological charge; it already has the density, and the charge is its integral. This is a genuine affirmative finding: in the Maxwell sector the topological density is not foreign to the framework's invariant theory but is one of its two invariants.

**The non-abelian case: no, and the reason is a rank-two limitation.** The non-abelian density is $\mathrm{Tr}(F\wedge F)$, and it needs two things that the abelian density does not: the **wedge** of two algebra-valued two-forms, and the **matrix trace** over the gauge algebra. The wedge is available — the parent packs the components into the single biquaternion $\mathcal{F}=\tfrac12\sum F_{\mu\nu}\bar{e}_\mu e_\nu$ — but the trace is not, and the norm form that produces $I_1$ and $I_2$ is the wrong bilinear for it. The norm form is a **rank-two bilinear of a single algebra element**: it pairs $\tilde{F}$ with $\bar{\tilde{F}}$ through the quaternion product and produces one scalar, using its one algebra slot. The non-abelian density pairs *two* gauge-algebra-valued objects in a matrix trace, and the norm form has no second slot in which to do that. The point is not a matter of notation; it is visible in the transformation law. Under a gauge transformation with $U\in SU(2)$ the components transform as $F_{\mu\nu}\mapsto UF_{\mu\nu}U^{-1}$, which does *not* extend to a conjugation of $\mathcal{F}$, because $U^{-1}$ does not commute with the basis elements $\bar{e}_\mu e_\nu$:

$$
\mathcal{F}\;\longmapsto\;\mathcal{F}'=\tfrac12\sum_{\mu\nu}\left(UF_{\mu\nu}U^{-1}\right)\bar{e}_\mu e_\nu
\;\neq\;U\,\mathcal{F}\,U^{-1}.
$$

Consequently the norm form of the representative is not gauge invariant. This was checked numerically on a random $\mathfrak{su}(2)$-valued two-form and a random $SU(2)$ element: $N(\mathcal{F})$ changed from $17.1838$ to $17.3970$ in the sample (an exact symbolic evaluation on a rational configuration gave the same non-invariance, with the transformed value a nontrivial trigonometric expression), while the matrix-trace density $\mathrm{Tr}(F_{\mu\nu}\star F^{\mu\nu})$ was invariant to machine precision, $-24.6702$ before and after. The invariant content of the non-abelian representative is therefore the matrix trace, exactly as the parent article says for $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$, and the norm form does not supply it.

This is the point at which the framework's established **rank-two limitation** meets the topological density. The series has already recorded, in the electromagnetic energy–momentum tensor, that a single biquaternion cannot carry a rank-two tensor — the object whose components are $T^{\mu\nu}$ needs a bilinear of two field strengths, $\tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^\dagger\mathcal{E}_\nu)$, and the algebra supplies that pairing only through an explicit second field-strength factor. The same limitation appears here in the gauge-algebra direction: the topological density needs a bilinear carrying a second algebra index that the norm form does not have. A biquaternion's quadratic invariant is rank-two and single-slot; the non-abelian topological density is rank-two in spacetime and traced over a *second* algebra factor. **The framework's invariants supply the abelian topological density and do not supply the non-abelian one.** This is left as a gap rather than closed by forcing a construction: the density can be written in components, with the matrix trace, and the total-derivative identity of the previous section holds for it, but it is not an object of the norm-form invariant calculus, and no norm-form expression for it was found.

A final remark on the primitive. The abelian primitive $K^\mu=\epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$ is a four-component object, so the framework's four-vector sector has the room to carry it, and its divergence is the invariant density. But $K^\mu$ is gauge dependent, so it is not one of the framework's invariants; the invariant content is $I_2$ and not the current. The primitive is therefore a computational device in the framework, not one of its invariants, and the non-abelian Chern–Simons form $\Omega_{\mathrm{CS}}$, being gauge covariant rather than invariant, is further from the invariant calculus still. The gap is not that the framework cannot write the density; it is that the framework's *invariant* apparatus does not produce it in the non-abelian case, and that the primitive is not an invariant in either case.

## The BPST Instanton and Its Equation of Motion

The existence half of the self-duality story is an explicit solution. The standard one is the Belavin–Polyakov–Schwartz–Tyupkin instanton, and it sits inside the non-abelian factor of the framework.

Work on the Euclidean slice with the $\mathfrak{su}(2)$ basis $T_a=\tfrac12 e_a$, $a=1,2,3$, so that

$$
[T_a,T_b]=\epsilon_{abc}T_c,
\qquad
\mathrm{Tr}(T_aT_b)=-\tfrac12\delta_{ab},
$$

the second following from $e_a=-i\sigma_a$ and $\mathrm{Tr}(\sigma_a\sigma_b)=2\delta_{ab}$. Write the connection and curvature as

$$
\mathcal{A}_\mu=\mathcal{A}_\mu^a T_a,
\qquad
F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+[\mathcal{A}_\mu,\mathcal{A}_\nu].
$$

The instanton is

$$
\mathcal{A}_\mu^a(x)=2\,\eta^a_{\mu\nu}\,\frac{x_\nu}{r^2+\rho^2},
\qquad
r^2=x_4^2+x_1^2+x_2^2+x_3^2,
$$

where $\eta^a_{\mu\nu}$ are the self-dual 't Hooft symbols ($\eta^a_{jk}=\epsilon_{ajk}$ for spatial indices, $\eta^a_{4k}=\delta_{ak}$, $\eta^a_{k4}=-\delta_{ak}$), $\rho>0$ is the instanton radius, and $x_4=c\tau$ is the Euclidean time. Replacing $\eta$ by the anti-self-dual symbols $\bar{\eta}$ ($\bar{\eta}^a_{jk}=\epsilon_{ajk}$, $\bar{\eta}^a_{4k}=-\delta_{ak}$, $\bar{\eta}^a_{k4}=\delta_{ak}$) gives the anti-instanton.

The configuration was checked by substitution, not quoted. At a generic point $x=(0.4,-1.2,0.7,1.5)$ with $\rho=0.6$, the curvature was formed by central finite differences and contracted with the epsilon symbol. The results are:

- with $\eta$, $F_{\mu\nu}=+\star F_{\mu\nu}$ for every pair, with residual $\max|F-\star F|\approx 2\times10^{-11}$;
- with $\bar{\eta}$, $F_{\mu\nu}=-\star F_{\mu\nu}$, with residual $\max|F+\star F|\approx 2\times10^{-11}$;
- in both cases the equation of motion $D_\mu F^{\mu\nu}=\partial_\mu F^{\mu\nu}+[\mathcal{A}_\mu,F^{\mu\nu}]=0$ holds to the accuracy of the finite differences, $\max|D_\mu F^{\mu\nu}|\approx 5\times10^{-7}$ at step $10^{-5}$.

The residual in the self-duality check is at the level of the arithmetic, and the residual in the equation-of-motion check is the expected finite-difference error; the solution is genuine. The equation-of-motion check is a guard against sign and factor slips in the transcription; the structural reason it must hold is the previous section's argument — self-duality plus the Bianchi identity — which is the real content.

The charge, the action and the moduli are those of the standard solution. The self-dual configuration has $|Q|=1$ (the sign is the orientation of the self-dual half and depends on the sign convention for the generators and for $\epsilon$: with Hermitian generators and $Q=(1/8\pi^2)\int\mathrm{Tr}(F\wedge F)$, the self-dual representative has $Q=+1$), and by the saturated bound its action is

$$
S=\frac{8\pi^2}{g^2},
$$

with $g$ the gauge coupling. The radius $\rho$ does not appear in the action; it is a modulus, and its constancy is the conformal invariance of the Euclidean theory noted earlier. The moduli of a single instanton are the five translation and dilatation parameters $(x_0,\rho)$ together with the three global $SU(2)$ orientations, and it is this eight-dimensional family that the framework's instanton sector carries.

One convention point belongs here because it is a signature effect and not a detail. The parent article's curvature carries an explicit factor $i$ in the commutator term, $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, tied to the $ict$ structure of the Lorentzian convention. On the Euclidean slice the curvature is written without it, as above, with the $i$ either dropped or absorbed into Hermitian generators and a real coupling. Keeping the Lorentzian factor literally, on anti-Hermitian $\mathcal{A}_\mu$ and with $\kappa=1$, the BPST configuration is *not* self-dual: the same numerical check gives $\max|F-\star F|\approx 0.54$ and $\max|F+\star F|\approx 0.60$. The Euclidean continuation of the framework's non-abelian curvature is therefore fixed only up to the placement of the factor $i$, and the placement that carries the instanton is the one without it in the commutator. This is the same signature split that governs the whole article, appearing once more at the level of the equations: the factor $i$ is a Lorentzian structure, and the Euclidean solution does not carry it. The exact form of the continuation — whether the factor migrates into the generators or into the coupling — is a convention question that this article leaves visible rather than resolves.

The biquaternion packaging of the solution is the parent's, $\mathcal{F}=\tfrac12\sum F_{\mu\nu}\bar{e}_\mu e_\nu$. The representative is a single biquaternion; the instanton therefore has a biquaternionic form, and the self-duality condition can be read as a condition on it. But, as the previous section showed, the *invariant* content of $\mathcal{F}$ is its matrix trace, not its norm form: the representative is the framework's object, and the topological density is not the framework's invariant. The instanton is thus expressible in the framework, while its charge is computed by the one bilinear the framework's invariant calculus does not supply.

## Solitons: What Stability Requires

A **soliton** is a static, finite-energy, localised solution of the Lorentzian field equations that is *stable*: a solution that a small perturbation cannot disperse. The last clause is the substance. A static solution of the Lorentzian equations can always be perturbed in the direction of a modulus or of a decaying mode, and a localised configuration with no conserved obstruction generally radiates away. Stability must therefore be *argued*, and in field theory there are two standard arguments; this section states both, shows what each requires, and records which of them the framework can supply.

**Topological sector.** A charge $Q$ is topological when it is conserved by continuity: it takes discrete values, it cannot change under any continuous finite-energy deformation, and a configuration with $Q\neq0$ therefore cannot relax to the vacuum (which has $Q=0$). The mechanism is present in settings the framework touches. The magnetic charge of the monopole article,

$$
Q_m\;\propto\;\oint_{S^2}\mathbf{B}\cdot d\mathbf{A},
$$

is an integer because it is the degree of a map $S^2\to S^2$ (or $S^2\to U(1)$), so $\pi_2(S^2)=\mathbb Z$; a configuration with $Q_m=1$ cannot be deformed into one with $Q_m=0$, and in that sense it is topologically obstructed from decaying. A kink in one spatial dimension has the same structure, with $Q=\phi(+\infty)-\phi(-\infty)$ fixed by the boundary values. A topological sector alone, however, only forbids decay to the vacuum; it does not by itself give *finite energy*, and a charge-carrying configuration can still have infinite energy because of a singular core. This is exactly the situation of the framework's monopole, and it is the reason the second argument matters.

**Bogomolny bound.** A bound $E\ge|Q|$ with equality for a first-order equation both proves stability — the configuration is at the bottom of its sector — and identifies the first-order equation that the minimiser satisfies. The mechanism is the same completing of the square used for the instanton, transposed to the energy. The cleanest illustration is the one-dimensional kink of the $\phi^4$ model,

$$
E=\int dx\left[\tfrac12(\partial_x\phi)^2+\tfrac{\lambda}{4}(\phi^2-v^2)^2\right],
\qquad
W(\phi)=\sqrt{\tfrac{\lambda}{2}}\left(v^2\phi-\tfrac13\phi^3\right),
$$

for which

$$
\tfrac12\left(\partial_x\phi\mp\sqrt{\tfrac{\lambda}{2}}(v^2-\phi^2)\right)^2
=\tfrac12(\partial_x\phi)^2+\tfrac{\lambda}{4}(\phi^2-v^2)^2\mp\partial_x W ,
$$

as was verified symbolically by expanding both sides. Integrating,

$$
E\;\ge\;\left|W(v)-W(-v)\right|=\frac{2\sqrt{2\lambda}}{3}\,v^3,
$$

with equality if and only if $\partial_x\phi=\pm\sqrt{\lambda/2}(v^2-\phi^2)$: the bound is saturated by the kink, whose stability is therefore proved, and not merely conjectured, within the model. The point of the example is that the bound needs two ingredients — a **potential** with degenerate minima and a **first-order equation** that the configuration satisfies — and the energy functional must contain the potential in the combination that completes the square.

**The framework's situation.** The framework's Lorentzian field content is the abelian Maxwell field, the non-abelian gauge field, and the free scalar field of the Klein–Gordon article. The Maxwell and non-abelian gauge sectors are gauge fields alone; their static finite-energy content is exhausted by the Coulomb field and the singular monopole, and neither has a potential in which a Bogomolny square could be completed. The scalar sector is a *free* massive field, with no self-interaction; a free field has no degenerate vacua and no kink, and it provides no potential of the $\phi^4$ type. Consequently:

- **The framework has a topological charge but no finite-energy configuration carrying it.** The magnetic charge $Q_m$ of the monopole article is genuinely topological, but the point monopole has a singular core and divergent energy, and no smooth finite-energy representative with $Q_m\neq0$ was exhibited in the framework. A finite-energy monopole of the 't Hooft–Polyakov type requires a scalar field in the adjoint representation with a symmetry-breaking potential, and the framework's scalar field, being free, does not supply it.
- **The framework has no Bogomolny bound for a soliton**, because there is no energy functional containing a potential to complete the square. There is therefore no configuration that this article can call a stable soliton, and it calls none. The absence is the answer to the corresponding half of the parent's question.

This is a gap in the framework's field content, not a defect in its algebra. The algebra $\mathbb{B}$ and its subspaces are capable of carrying a scalar, a gauge field and a potential; what is missing is a potential in the theory as developed. Whether a scalar potential can be built inside the framework — and whether the resulting finite-energy topological configuration is a soliton in the strong sense above — is left open. What can be said without forcing it is that the instanton and the soliton are not two cases of one construction: the instanton comes from a *first-order* Euclidean condition whose power is that it replaces the equation of motion, while the soliton would come from a *second-order* Lorentzian bound whose power is that it replaces the energy by a boundary term. The framework supplies the first and does not supply the second.

## Summary

This article has treated the localised finite-energy solutions of the biquaternion framework in the two settings in which they occur, and has kept the settings apart.

- **Instantons are Euclidean.** The Hodge star on two-forms has $\star^2=+1$ in Euclidean signature and $\star^2=-1$ in Lorentzian signature; consequently $F=\star F$ has nonzero real solutions only in the Euclidean case, and a real self-dual Lorentzian field is the zero field. The framework's Wick rotation, the identification $\mathbb{M}_-\leftrightarrow\mathbb{H}_{\mathbb{B}}$, is the passage between the two stars, and the explicit factor $i$ of the $ict$ convention is the Lorentzian structure that the Euclidean solution does not carry.
- **The topological charge is an integral of a total derivative.** The density is $q=\tfrac14\epsilon^{\mu\nu\rho\sigma}\mathrm{Tr}(F_{\mu\nu}F_{\rho\sigma})=\tfrac12\mathrm{Tr}(F_{\mu\nu}\star F^{\mu\nu})$, and in the abelian case it equals $\partial_\mu K^\mu$ with $K^\mu=\epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$; this was verified symbolically, in both the flat Euclidean and the $ict$ conventions, with the second derivatives cancelling. In the non-abelian case $F\wedge F=d\Omega_{\mathrm{CS}}$. The primitive is what makes the charge topological: it is fixed by the boundary winding and is insensitive to the local shape.
- **The framework's invariants supply the abelian density.** $F_{\mu\nu}\star F^{\mu\nu}=4iI_2/c$ (Lorentzian) and $=4I_2$ (Euclidean) were recomputed; the imaginary part of the norm form, $I_2=\mathbf{E}\cdot\mathbf{B}$, *is* the abelian topological density. In the non-abelian case the density needs the matrix trace, and the rank-two, single-slot norm form of the biquaternion representative is not gauge invariant under $F_{\mu\nu}\mapsto UF_{\mu\nu}U^{-1}$; this was checked numerically. That the framework's invariant apparatus does not produce the non-abelian topological density is recorded as a gap.
- **There is no abelian instanton.** For finite-action abelian fields on $\mathbb R^4$ the charge is a vanishing surface term; instantons are intrinsically non-abelian, and in this framework they live in the $\mathfrak{su}(2)$ factor inside $\mathbb{M}_-$.
- **An explicit solution exists and was checked.** The $SU(2)$ BPST instanton in the framework's $\mathfrak{su}(2)$ satisfies $F=\pm\star F$ (residual at the arithmetic level) and $D_\mu F^{\mu\nu}=0$ (to finite-difference accuracy). It saturates the Bogomolny bound $S\ge 8\pi^2|Q|/g^2$ that self-duality establishes, and its charge is $|Q|=1$.
- **There is no soliton.** A soliton's stability requires a topological sector with a finite-energy representative, or a Bogomolny bound; the framework has the topological charge $Q_m$ of the monopole but only a singular, infinite-energy configuration to carry it, and its free scalar sector provides no potential in which a Bogomolny square can be completed. The absence is stated as a gap, and no configuration is called stable.
- **What is left open.** The exact placement of the factor $i$ in the Euclidean continuation of the framework's non-abelian curvature; whether a scalar potential can be constructed inside the framework so that a finite-energy topological configuration exists; and whether the zero-divisor structure of $\mathbb{M}_-$, which the parent flagged, plays any role in the instanton sector. A fourth item is the axial anomaly: the topological density derived here is the object that appears in it, and the chiral-fermion article names this article as its natural home, but the anomaly itself — its coefficient, its relation to the $\theta$-angle — is a separate subject and is not treated here. None of the items was needed for the results above, and none is closed here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb R}\mathbb{H}$ | The biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{M}_-$ | Material sector, anti-Hermitian, signature $(3,1)$ |
| $\mathbb{M}_+$ | Informational sector, Hermitian, signature $(1,3)$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, the Euclidean slice |
| $\mathbb{C}_{\mathbb{B}}$ | Complex scalar subspace, $\mathrm{span}_{\mathbb R}\{e_0,ie_0\}$ |
| $\tilde{\nabla},\bar{\tilde{\nabla}}$ | Biquaternionic gradient and its quaternion conjugate |
| $\tilde{\nabla}_E$ | Euclidean gradient on the rotated slice |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ | Lorentzian d'Alembertian, hyperbolic |
| $\Box_E$ | Euclidean Laplacian, elliptic |
| $\star$ | Hodge star on two-forms; $\star^2=+1$ Euclidean, $-1$ Lorentzian |
| $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$ | Abelian field-strength biquaternion |
| $F_{\mu\nu}$ | Field-strength components (abelian in the Maxwell sections, non-abelian in the gauge sections) |
| $I_1=\mathbf{E}^2-c^2\mathbf{B}^2,\ I_2=\mathbf{E}\cdot\mathbf{B}$ | The two field-strength invariants |
| $N(\tilde{F})=\tilde{F}\bar{\tilde{F}}=-\epsilon(I_1+2icI_2)$ | The norm form |
| $\mathcal{A}_\mu=\mathcal{A}_\mu^a e_a$ | Non-abelian connection, $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}$ |
| $\mathcal{F}=\tfrac12\sum F_{\mu\nu}\bar{e}_\mu e_\nu$ | Biquaternion representative of the non-abelian curvature |
| $T_a=\tfrac12 e_a$ | $\mathfrak{su}(2)$ generators, $[T_a,T_b]=\epsilon_{abc}T_c$ |
| $D_\mu$ | Gauge-covariant derivative |
| $\mathrm{Tr}$ | Matrix trace on the gauge factor |
| $\mathrm{Sc},\ \mathrm{Tr}(\tilde{P}\tilde{H})=2\mathrm{Sc}(\tilde{P}\tilde{H})$ | Scalar part and the inherited trace formula |
| $q=\tfrac14\epsilon^{\mu\nu\rho\sigma}\mathrm{Tr}(F_{\mu\nu}F_{\rho\sigma})$ | Topological density |
| $K^\mu=\epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$ | Abelian Chern–Simons current |
| $\Omega_{\mathrm{CS}}$ | Chern–Simons three-form, $d\Omega_{\mathrm{CS}}=\mathrm{Tr}(F\wedge F)$ |
| $Q$ | Topological (instanton) charge, $Q\in\mathbb Z$ |
| $Q_m\propto\oint_{S^2}\mathbf{B}\cdot d\mathbf{A}$ | Magnetic (topological) charge |
| $\epsilon^{\mu\nu\rho\sigma}$ | Totally antisymmetric symbol, $\epsilon^{0123}=+1$ |
| $g,\ \kappa=q/\hbar$ | Gauge coupling and the parent's coupling convention |
| $\rho$ | Instanton radius (a modulus) |

## Further Reading

- *Non-Abelian Gauge Fields in Biquaternionic Form* — the connection, curvature, gauge transformation and invariant density used throughout the non-abelian sections.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the covariant derivative $D_\mu$ and the gauge connection.
- *The Field-Strength Biquaternion and Its Invariants* — the abelian field strength, the invariants $I_1,I_2$ and the norm form $N(\tilde{F})$.
- *The Magnetic Monopole in Biquaternionic Form* — the topological magnetic charge $Q_m$ and the singular point monopole.
- *The Wick Rotation in the Biquaternion Universe* — the identification $\mathbb{M}_-\leftrightarrow\mathbb{H}_{\mathbb{B}}$ and the Euclidean slice.
- *Biquaternion Topology* — the contractibility of $\mathbb{B}$, the unit group and the null cone.
- *Maxwell's Equations in the Biquaternionic Formulation* — the field equation and the Riemann–Silberstein structure of the abelian sector.
- *The Gauge Principle in Biquaternionic Form* — the central $U(1)$ and the local gauge structure.
- *The Klein–Gordon Equation in Biquaternionic Form* — the free scalar field that supplies no potential.
- *Exercise: The Electromagnetic Energy–Momentum Tensor* — the rank-two limitation of a single biquaternion.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the sector in which the $\mathfrak{su}(2)$ factor and the Lorentzian star live.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the complementary sector.
- *Curved Spacetime and the Biquaternion Framework* — the gravitational background that the topological charge is independent of.
