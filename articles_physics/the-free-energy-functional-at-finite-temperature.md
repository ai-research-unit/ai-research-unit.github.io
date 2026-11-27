# __The Free-Energy Functional at Finite Temperature__

## Introduction

**The claim.** The closure of this corpus's chain — from the fluid's equations to its thermodynamics — needs one object that the chain has been assuming and never writing: a functional whose stationarity is the fluid's state and whose value is its thermodynamic potential. That object is the **free-energy functional**, the Legendre transform of $\log Z$ at inverse temperature $\beta$, and in the effective-action language it is $\Gamma_\beta$. **It is the finite-temperature face of the action**: the same stationarity, one Legendre transform later, with the thermodynamic potential as the on-shell value.

**What is established.** Four things. First, the construction, and the double role — stationarity gives the field equation at temperature, and the value gives the pressure. Second, the response functions are its derivatives, so Euler's relation, Gibbs–Duhem and the Maxwell relations are not extra laws but its calculus. Third, the three tests of the local thermal state become three properties of one object: integrability is that there is one functional, consistency is that the response functions are its derivatives, and determinacy is that the functional is local to a stated derivative order. Fourth, the one-loop form puts the corpus's split $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ at the zeroth and second orders of one expansion, so the split is a truncation and not a definition.

**What is not new.** The effective action is standard, and the corpus already has [the generating functional and the effective action](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html) at zero temperature, [the one-loop effective potential of the scalar matrix](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html), and [the partition function](the-partition-function-in-biquaternionic-form.html). **What the corpus did not have is the article that puts the three together and says what the fluid's closure was missing** — and this is it.

**Why it is the missing variational principle.** The ledger article states which of the fluid's thermodynamic relations are derived and which are assumed, and the answer has been: the identities are assumed, the equation of state is separate, and nothing generates them. **A thermodynamic potential generates all of them.** Writing it is what turns the ledger's *assumed* column into *derived*.

## From the Partition Function to the Functional

**The generating functional and its logarithm.** With a source $J$ coupled to the field,

$$
Z_\beta[J]=\int_{\text{periodic}}\mathcal D\tilde\Xi\;\exp\Bigl(-S_E[\tilde\Xi]+\int d^4r\;J\,\tilde\Xi\Bigr),
\qquad
W_\beta[J]=\log Z_\beta[J],
$$

the integral taken over fields periodic on the thermal circle of circumference $\beta$. **$W_\beta$ is the free energy in the presence of the source**, and its derivatives are the connected correlators.

**The Legendre transform, and the functional the fluid needs.** Define

$$
\Gamma_\beta[\varrho]:=W_\beta[J]-\int d^4r\;J\,\varrho,
\qquad
\varrho:=\frac{\delta W_\beta}{\delta J},
$$

with $\varrho$ the amplitude whose square is the proper density, $\varrho^{2}=\rho_{\mathrm{num}}$. **$\Gamma_\beta$ is the effective action at temperature $\beta$**, and its two properties are the article's whole content:

$$
\boxed{\;\frac{\delta\Gamma_\beta}{\delta\varrho}\Big|_{\varrho=\varrho_*}=0\ \Longleftrightarrow\ \text{the field equation at }\beta,
\qquad
\Omega_\beta:=-p_{\mathrm{th}}V_0=\Gamma_\beta[\varrho_*]\;}
$$

**Stationarity and value, one object.** The left statement is that the physical configuration is a stationary point of the functional; the right is that the thermodynamic potential is its value there. **The first is the fluid's equation of state as a variational principle; the second is the pressure.**

**Why the Legendre transform and not the action.** The action's stationarity gives the equation of motion; it does not give the pressure, because the action is not the potential whose derivatives are the response functions. **The Legendre transform is what converts a functional of the configuration into a functional whose value is a thermodynamic potential** — which is why the closure needs $\Gamma$ and not $S$.

**The source, read as the fluid's own variables.** The source $J$ is conjugate to the amplitude, so it plays the role of an external potential. Setting $J=0$ after the transform is the statement that the fluid is closed; keeping it is the statement that the fluid sits in an external field, and $\Gamma$'s dependence on $\varrho$ at $J\ne0$ is the response. **The grand-canonical version replaces $J$ by a chemical potential**, which is the same construction with the charge coupled instead of the amplitude; [the chemical potential article](the-chemical-potential-is-the-phases-frequency.html) says what that coupling is.

## What the Functional Reproduces

**The field equation, as the stationarity condition.** Varying $\Gamma_\beta$ with respect to the amplitude gives the finite-temperature gap equation: the same equation the classical variation gives, with the thermal corrections summed into its coefficients. **At one loop the correction is the thermal mass**, and the gap equation is the statement that the mass the field sees is its own.**

**The response functions, as derivatives.** From $\Omega_\beta=\Gamma_\beta[\varrho_*]$,

$$
p_{\mathrm{th}}=-\frac{\Omega_\beta}{V_0},\qquad
s_{\mathrm{ent}}=-\frac{\partial\Omega_\beta}{\partial T},\qquad
n_{\mathrm{num}}=-\frac{\partial\Omega_\beta}{\partial\mu_{\mathrm{chm}}},\qquad
w_{\mathrm{fl}}=\Omega_\beta+Ts_{\mathrm{ent}}+\mu_{\mathrm{chm}}n_{\mathrm{num}} .
$$

**The four displays are one function's derivatives**, which is what makes Euler's relation an identity rather than a constraint: the last line is the first three substituted into the Legendre structure, and it is Euler's relation because a homogeneous function's derivatives reconstruct it.

**Gibbs–Duhem, as the statement that the derivatives are not independent.** Differentiating the Euler relation and using the first law gives $dp_{\mathrm{th}}=s_{\mathrm{ent}}dT+n_{\mathrm{num}}d\mu_{\mathrm{chm}}$. **In the functional's language this is trivial**: $dp_{\mathrm{th}}$ is the differential of $-\Omega/V_0$, whose independent variables are $(T,\mu)$, and its partial derivatives are the two response functions. **A reader who wants to know why Gibbs–Duhem holds should be told that it is the chain rule.**

**The Maxwell relations, as the symmetry of second derivatives.** $\partial^{2}\Omega/\partial T\partial\mu=\partial^{2}\Omega/\partial\mu\partial T$ gives $\partial s_{\mathrm{ent}}/\partial\mu=\partial n_{\mathrm{num}}/\partial T$. **This is the third test of the local thermal state**, and it holds because there is one functional. A pressure written down as a formula with no $\Omega$ behind it satisfies Euler and Gibbs–Duhem by construction and violates a Maxwell relation somewhere: **the violation is the signature of a fit**, and it is invisible in the two identities alone.

## The Three Tests, Property by Property

**The correspondence is exact, and it is the reason this article belongs before the ledger.**

| test of the local state | what it asks | what it is in $\Gamma_\beta$ | when it fails |
| --- | --- | --- | --- |
| determinacy | the pressure at an event is a function of that event's data | $\Gamma_\beta$ is local to a stated derivative order | the derivative expansion is truncated; the next order is a gradient correction |
| consistency | the local fields satisfy Euler and Gibbs–Duhem | the response functions are $\Gamma_\beta$'s derivatives | the thermal and quantum parts are mixed in one symbol |
| integrability | one potential generates the response functions | $\Gamma_\beta$ is one functional | the pressure is fitted, and a Maxwell relation fails |

**Determinacy is the interesting row, and the corpus already knows its answer.** $\Gamma_\beta$ is nonlocal in general — it is the Legendre transform of a nonlocal $W_\beta$ — so a strictly local equation of state cannot come from it. **What is local is its derivative expansion**, and the expansion's first two orders are the corpus's own split: the zeroth order is $p_{\mathrm{th}}$, the second is $p_{\mathrm{qnt}}$, and the statement that the effective pressure is local to order $\frac{h^{2}}{4\pi^{2}}$ is the statement that the expansion is truncated there. **The split is a truncation, and this article is where that becomes visible.**

**Consistency's failure mode is a labelling failure.** $p_{\mathrm{qnt}}$ does not satisfy the Euler and Gibbs–Duhem relations, and it must not be made to: it is a gradient correction, and its "entropy" would be spurious. **The functional makes the reason structural** — the gradient orders are not homogeneous in the extensive data at fixed $\beta$, so Euler's theorem does not apply to them.

**Integrability's failure mode is the one the corpus's ledger has been recording.** Where a relation is assumed rather than derived, the ledger says so; **the functional is what would derive it**, and every entry the ledger marks assumed is an entry where the functional is either unknown or truncated.

## The One-Loop Form, and Where the Quantum Part Sits

**The standard one-loop expression.** Splitting the field into a background and a fluctuation and integrating the fluctuation,

$$
\Gamma_\beta[\varrho]=S_E[\varrho]+\tfrac12\,\mathrm{STr}\log\Bigl(\frac{\delta^{2}S_E}{\delta\tilde\Xi\,\delta\tilde\Xi^{*}}\Bigr)\Big|_{\tilde\Xi=\varrho}+\cdots,
$$

the **effective potential** when $\varrho$ is uniform: $V_{\mathrm{eff}}(\varrho)=V_0(\varrho)+\tfrac12\mathrm{STr}\log\bigl(\hat K(\varrho)\bigr)$, with $\hat K$ the fluctuation operator. **The finite-temperature part is the thermal sum** over the Matsubara frequencies, and the zero-temperature part is the corpus's one-loop article.

**Three readings of one display, and the corpus uses all three.**

- *The minimum is the state.* $\partial V_{\mathrm{eff}}/\partial\varrho=0$ at $\varrho=\varrho_*$ is the gap equation, and $V_{\mathrm{eff}}(\varrho_*)=-p_{\mathrm{th}}$ is the pressure.
- *The curvature is the mass.* $\partial^{2}V_{\mathrm{eff}}/\partial\varrho^{2}$ at the minimum is the thermal mass, which is the coefficient the fluid's linear response sees.
- *The difference is the quantum pressure.* $V_{\mathrm{eff}}-V_0$ is the sum of the gradient and vacuum corrections, so the split $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ is the split of $V_{\mathrm{eff}}$ into its thermal and its zero-temperature-plus-gradient parts.

**Why the one-loop form is the right level for this corpus.** Every functional integral the corpus writes is one-loop or Gaussian; the determinant is its one-loop coefficient; the trace is the corpus's own scalar part at $2\times2$. **So the free-energy functional is not a new formalism for the corpus but the assembly of three objects it already has**, and the assembly is what the closure was missing.

## Two Faces: Imaginary Time and the Closed Time Path

**One $Z$, two functionals.** The functional above is built on the thermal circle, so it is the **imaginary-time** face: it gives the equilibrium potential and nothing about real-time response. The **real-time** face is built on the closed time path, where the field is doubled, and [the closed-time-path article](the-closed-time-path-action-one-action-on-two-branches.html) writes it. **The two are analytic continuations of one another**, and the corpus's Schwinger–Keldysh article is the real-time side of the same $Z$.

**What each face can do.** The imaginary-time face gives $p$, $s$, $n$, $w$ and the Maxwell relations — the whole equilibrium thermodynamics, exactly. The real-time face gives the response functions at finite frequency and the dissipation, which the imaginary-time face cannot. **A reader who wants the equation of state wants the first; a reader who wants the transport coefficients wants the second.**

**Why the fluid's closure needs only the first.** The closure's subject is the state and its functionals, not the departures. **The departures are the next subsection's subject**, and they need the doubled functional; the state needs the circle. This is the cleanest division in the block, and it is the reason the two articles are separate.

**The continuation, stated so that it is not a mystery.** The Matsubara sum becomes an integral over real frequencies by deforming the contour, and the poles that are crossed are the thermal excitations. **The continuation is where the $i\epsilon$ of the real-time propagator comes from**, and it is why the two faces are two readings of one object rather than two theories.

## What It Does Not Give

**It does not give the transport coefficients.** Those are the real-time face's, and they require the doubled functional and a gradient expansion of it.

**It does not give the exact nonlocal functional in closed form.** It gives the construction and the one-loop term; the exact $\Gamma_\beta$ is a sum to all orders, and the corpus truncates, as every treatment does.

**It does not resolve a first-order transition.** $\Gamma_\beta$ is convex, so a first-order transition makes it non-analytic and its minimum jumps: the two phases' minima cross, and the equation of state in between is a mixture. **The Maxwell construction is the convex hull of the functional**, and a fluid whose equation of state is a family in that region is the corpus's *family of fluids* read thermodynamically. This article states the mechanism and does not carry out a construction.

**It does not fix the renormalisation.** The one-loop term is divergent and needs the same subtraction the corpus's zero-temperature articles perform; **the finite-temperature part is finite**, because the thermal sum's ultraviolet behaviour is the zero-temperature one. That split — divergent vacuum part, finite thermal part — is why the thermal pressure can be quoted without a counterterm and the vacuum energy cannot.

## Summary

The free-energy functional is the Legendre transform of $\log Z$ at inverse temperature, and it has two roles: its stationarity is the field equation at temperature, and its value is the thermodynamic potential, $\Omega_\beta=-p_{\mathrm{th}}V_0=\Gamma_\beta[\varrho_*]$. **It is the variational principle the fluid-to-thermodynamics closure was missing.**

Its derivatives are the response functions, so Euler's relation is its homogeneity, Gibbs–Duhem is its chain rule, and the Maxwell relations are the symmetry of its second derivatives. **The three tests of the local thermal state are three properties of the one object**: integrability is that it exists, consistency is that the response functions are its derivatives, determinacy is that its derivative expansion is truncated at a stated order.

The one-loop form is $V_{\mathrm{eff}}=V_0+\tfrac12\mathrm{STr}\log\hat K$, whose minimum is the state, whose curvature is the thermal mass, and whose deviation from $V_0$ is the quantum pressure. **The corpus's split $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ is the zeroth and second orders of one expansion**, so the split is a truncation and not a definition.

It comes in two faces, imaginary time for the equilibrium potential and the closed time path for the response, and the fluid's closure needs only the first. It gives no transport coefficients, no closed exact form, no transition resolution and no renormalisation. It gives the potential, and the potential is what generates the ledger.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $Z_\beta[J]$ | The partition function with a source, integrated over fields periodic on the thermal circle |
| $W_\beta[J]=\log Z_\beta[J]$ | The free energy in the source; its derivatives are the connected correlators |
| $\varrho=\delta W_\beta/\delta J$ | The amplitude conjugate to the source; $\varrho^{2}=\rho_{\mathrm{num}}$ |
| $\Gamma_\beta[\varrho]=W_\beta[J]-\int J\varrho$ | The effective action at temperature $\beta$; the free-energy functional |
| $\delta\Gamma_\beta/\delta\varrho=0$ | The field equation at $\beta$, as a stationarity condition |
| $\Omega_\beta=-p_{\mathrm{th}}V_0=\Gamma_\beta[\varrho_*]$ | The thermodynamic potential as the functional's value at the stationary point |
| $s_{\mathrm{ent}},n_{\mathrm{num}},w_{\mathrm{fl}}$ | Entropy density, number density, energy density; $-\partial_T\Omega$, $-\partial_\mu\Omega$, and the Euler combination |
| $V_{\mathrm{eff}}=V_0+\tfrac12\mathrm{STr}\log\hat K$ | The one-loop effective potential; $\hat K$ the fluctuation operator |
| $\mathrm{STr}$ | The supertrace, the corpus's scalar part at $2\times2$ |
| $p_{\mathrm{th}},p_{\mathrm{qnt}}$ | The thermal and quantum parts of the pressure, the zeroth and second orders of the expansion |
| $\beta=\frac{h}{2\pi k_BT}$ | The thermal period; the circumference of the imaginary-time circle |

## Further Reading

- Joseph I. Kapusta and Charles Gale, *Finite-Temperature Field Theory* (2nd ed., Cambridge University Press, 2006), for the effective potential at finite temperature, the thermal sum and the renormalisation split.
- Michel Le Bellac, *Thermal Field Theory* (Cambridge University Press, 1996), for the imaginary-time and real-time formulations and the analytic continuation between them.
- Sidney Coleman and Erick Weinberg, "Radiative corrections as the origin of spontaneous symmetry breaking," *Physical Review D* 7 (1973), 1888–1910, for the one-loop effective potential and the minimum as the state.
- L. Dolan and R. Jackiw, "Symmetry behavior at finite temperature," *Physical Review D* 9 (1974), 3320–3341, for the thermal part of the one-loop potential.
- Alexander L. Fetter and John Dirk Walecka, *Quantum Theory of Many-Particle Systems* (McGraw-Hill, 1971), for the grand potential, its derivatives and the Maxwell relations in the many-body setting.
- [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html), whose $\log Z$ this article Legendre-transforms.
- [The Generating Functional and the Effective Action in Biquaternionic Form](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), the zero-temperature version of the same construction.
- [The One-Loop Effective Potential of the Scalar Matrix at Sixteen Real Components](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html), the one-loop term in the corpus's letters.
- [The Chemical Potential Is the Phase's Frequency](the-chemical-potential-is-the-phases-frequency.html), for the $\mu$ that the grand-canonical version couples.
- [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html), whose three tests this article derives from one functional.
- [The Closed-Time-Path Action: One Action on Two Branches](the-closed-time-path-action-one-action-on-two-branches.html), the real-time face of the same $Z$.
