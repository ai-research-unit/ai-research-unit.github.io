# __The Lagrangian and the Weak Interaction__

## Introduction

This article writes the charged-current weak interaction as an extremum of an action, and shows that eliminating the $W$ from that action produces the four-fermion contact with the coefficient $G_F$ fixed. It is the action-first companion of *The Weak Interaction in Biquaternionic Form*, which states the currents and the rates; this article asks what functional produces the $V-A$ vertex, and why the contact approximation is as good as it is.

Its place in the sector. The action here is the charged-current term of the sector's functional, [The Lagrangian and the Electroweak Theory](the-lagrangian-and-the-electroweak-theory.html), with the $W$ already massive and the neutral sector dropped. The elimination below is exact only in that truncated setting, and the article says where.

The equation. The parent's equation is the $W$'s own equation with the charged current as source,

$$
D_\nu W^{+}_{\mu\nu}-M_W^2 W^{+}_\mu=\frac{g}{2\sqrt2}J^{+}_\mu ,
$$

together with its conjugate, in a gauge where the kinetic term is the Proca one. The article asks what action has this equation and what becomes of it below the $W$'s mass.

Three things are established.

*First, the action.* With $J^{+}_\mu=\bar{\tilde\Xi}_{\mathrm u}\,\gamma_\mu(1-\gamma_5)\tilde\Xi_{\mathrm d}$,

$$
S=\int d^4r\;\Bigl[-\tfrac12\sum_{\mu,\nu}W^{+}_{\mu\nu}W^{-}_{\mu\nu}+M_W^2\sum_\mu W^{+}_\mu W^{-}_\mu-\frac{g}{2\sqrt2}\sum_\mu\bigl(W^{+}_\mu J^{+}_\mu+W^{-}_\mu J^{-}_\mu\bigr)\Bigr],
$$

the stationarity conditions are the parent's equations, and the vertex is the third term.

*Second, the variation eliminates the field.* Varying $W^{+}_\mu$ gives its equation; solving it at low momentum and substituting back gives the contact action

$$
S_{\mathrm{eff}}=-\frac{G_F}{\sqrt2}\int d^4r\;\sum_\mu J^{+}_\mu J^{-}_\mu ,
\qquad
\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2} .
$$

The elimination is not an approximation to the action; it is an exact Gaussian integration, and the momentum expansion is the approximation applied to the resulting non-local term.

*Third, the algebra carries the vertex and not the mass.* The $V-A$ structure is the chiral projection of the algebra's own bilinear, and it is exact; the $W$'s mass is transcribed from the electroweak sector. The article's honesty statement is that boundary.

What is not new. The charged current, its $V-A$ form and every rate in the parent are standard. What the corpus contributes is the identification of the projection with the algebra's chirality and the exactness statement for the contact in the element notation.

## Conventions

The conventions are restated here so that every sign below is checkable from this page. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\eta^{2}=-e_t$; the fermions are elements $\tilde\Xi\in\mathbb{B}$ and the bilinear pairing is $\bar{\tilde\Xi}=\tilde\Xi^{\dagger}iC_0$.

The current. $J^{+}_\mu=\bar{\tilde\Xi}_{\mathrm u}iR_{\vec e_z}\gamma_\mu(1-\gamma_5)\tilde\Xi_{\mathrm d}$, with $\mathrm u$ the upper and $\mathrm d$ the lower member of a doublet; $J^{-}_\mu=(J^{+}_\mu)^{\dagger}$. The right multiplication by $\vec e_z$ is the corpus's chirality insertion, and the factor $(1-\gamma_5)$ is its component form.

The $W$. $W^{\pm}_\mu$ are complex vector fields with mass $M_W=80.377$ GeV; the curvature is $W^{+}_{\mu\nu}=\partial_\mu W^{+}_\nu-\partial_\nu W^{+}_\mu$. The coupling is $g$, and the Fermi constant is $G_F=1.1663787\times10^{-5}$ GeV$^{-2}$.

The sign convention. The mass term enters with a plus sign after the corpus's sign rule and the curvature term with $-\tfrac12$; the interaction term carries the minus of the coupling. Every sign below follows from that choice.

## The Action in Element Form

The three pieces. The $W$'s kinetic and mass terms and one interaction term,

$$
\mathcal{L}=\mathcal{L}_{W}+\mathcal{L}_{\mathrm{int}},
\qquad
\mathcal{L}_W=-\tfrac12\sum_{\mu,\nu}W^{+}_{\mu\nu}W^{-}_{\mu\nu}+M_W^2\sum_\mu W^{+}_\mu W^{-}_\mu ,
\qquad
\mathcal{L}_{\mathrm{int}}=-\frac{g}{2\sqrt2}\sum_\mu\bigl(W^{+}_\mu J^{+}_\mu+W^{-}_\mu J^{-}_\mu\bigr).
$$

The interaction is a product of a gauge field and a current and nothing else: no derivative of the $W$, no derivative of the current. That absence is what makes the elimination of the next section so simple.

Why the current carries the $V-A$ structure. In the algebra the projection is the right multiplication by a unit imaginary vector, and the two chiral parts of $\tilde\Xi$ are the two eigenspaces of that insertion. The corpus's Dirac bilinear $\bar{\tilde\Xi}\gamma_\mu(1-\gamma_5)\tilde\Xi$ is the component form of the object, and the algebraic statement is that the weak vertex selects one of the two chiral halves. The selection is exact: it is a projection in the algebra and not an approximation to one.

Why the $W$ is charged. $W^{+}_\mu$ carries one unit of electric charge and one unit of the weak ladder; its conjugate carries the opposite. The action is real because the two terms are conjugates of each other, and the factor $1/\sqrt2$ is the normalization of the ladder operators $\tau^{\pm}=(\tau_1\pm i\tau_2)/\sqrt2$.

The gauge-fixed form. The mass term breaks the local $SU(2)_L$ of the $W$'s own sector, so the action above is written in the unitary gauge, where the $W$'s longitudinal mode is its third polarization and there is no Goldstone. In a covariant gauge the Goldstone returns and the same physics is distributed differently; that is the gauge-fixing article's, and this article uses the unitary form throughout because the vertex does not depend on the choice.

The pairing. The pairing is the Dirac bilinear, and its reality is what makes the contact real. $J^{+}_\mu J^{-}_\mu=\lvert J^{+}_\mu\rvert^{2}$ is a squared modulus, real and non-negative term by term, so the contact action is real with a definite sign. The full action is real because the interaction term is a sum of a term and its conjugate.

Why the current is a vector and not a bilinear of two independent fields. The current is bilinear in the fermions and linear in each; the action is quartic in the fermions after the elimination, which is the defining feature of a four-fermion theory. The quartic form is real because it is the modulus squared of the current.

The type of the coefficient. One dimensionless coupling and one mass, and their ratio is the measured $G_F$. $g$ is dimensionless and $M_W$ has dimension of mass; $G_F$ has dimension of mass to the minus two and is their combination $g^2/(8M_W^2)$. The action has no dimensionful coupling of its own, and the contact's dimension comes from the mass it eliminated.

What that means for the theory's status. The contact action is non-renormalizable by power counting, because a coupling of dimension minus two requires an infinite tower of counterterms. That is not a defect of the elimination; it is the statement that the $W$ must be restored above the scale where the expansion fails, and the restoration is the electroweak action.

The selection rule. The selection rule is $SU(2)_L$ and it selects one chirality. The current contains $(1-\gamma_5)$, so only left-handed fermions couple; the right-handed components are singlets and do not. The selection is exact and it is the reason the theory is called chiral, and it is also the reason a fermion mass term is forbidden before breaking: a mass couples left to right.

**What reality does not buy. Reality does not buy a rate, a mass, or a valid high-energy completion.** Three things the reality of the action does not supply:

- *No rate without the phase-space integral.* The rate is a separate computation, and the parent performs it.
- *No fermion masses.* The chiral structure forbids them; they come from the Yukawa sector.
- *No validity above $M_W$.* The contact is an expansion, and its reality says nothing about its convergence.

## The Variation: Solving for $W$ Gives the Contact

The variation with respect to $W^{+}_\mu$. In the unitary gauge the equation is algebraic in momentum space,

$$
\bigl(-k^2+M_W^2\bigr)W^{+}_\mu(k)=\frac{g}{2\sqrt2}J^{+}_\mu(k),
$$

where the sign of the mass term makes the kernel invertible for every $k$ and the transverse projector is trivial because the mass term is a Stueckelberg term in this gauge. The solution is

$$
W^{+}_\mu(k)=\frac{g}{2\sqrt2}\frac{J^{+}_\mu(k)}{M_W^2-k^2}.
$$

**The substitution, exact.** Inserting the solution back into the action gives the non-local effective action

$$
S_{\mathrm{eff}}=-\frac{g^2}{8}\int d^4r\,d^4r'\;\sum_\mu J^{+}_\mu(r)\,G(r-r')\,J^{-}_\mu(r'),
$$

with $G$ the propagator of the massive vector, $G(k)=1/(M_W^2-k^2)$. The Gaussian integration is exact; no approximation has entered.

The momentum expansion, and where it is justified. For $|k^2|\ll M_W^2$, $G(k)=M_W^{-2}(1+k^2/M_W^2+\cdots)$, and the leading term gives the contact

$$
\boxed{\;S_{\mathrm{eff}}=-\frac{G_F}{\sqrt2}\int d^4r\;\sum_\mu J^{+}_\mu J^{-}_\mu+O\!\left(\frac{\partial^2}{M_W^2}\right),
\qquad
\frac{G_F}{\sqrt2}=\frac{g^2}{8M_W^2}\;}
$$

with the second term of the expansion suppressed by $k^2/M_W^2$. At a momentum transfer of $100$ MeV the ratio is $1.55\times10^{-6}$, so the contact is accurate to a part per million for nuclear beta decay, and this is why the $W$ is never seen as a propagating degree of freedom in that setting.

The coefficient, counted from the action and not remembered. The interaction carries $\frac{g}{2\sqrt2}$; squaring it gives $\frac{g^2}{8}$, and the eliminated mass supplies $M_W^{-2}$, so the contact is $-\frac{g^2}{8M_W^2}J^{+}J^{-}$ and the coefficient is $\frac{G_F}{\sqrt2}$ with no further factor. A reader who meets $\frac{4G_F}{\sqrt2}$ in a textbook is reading a current written $\bar\psi\gamma_\mu P_L\psi$: the projector $P_L$ halves the current, so the product of two such currents is four times smaller and the coefficient four times larger. With the full $(1-\gamma_5)$ current used here, the $\frac{4G_F}{\sqrt2}$ form would be wrong by that factor and the muon rate too large by sixteen. The rate computed from the coefficient above, $\Gamma=G_F^2m_\mu^5/(192\pi^3)=3.009\times10^{-19}$ GeV, is $\tau_\mu=2.187\times10^{-6}$ s against the measured $2.197\times10^{-6}$ s — $0.44\%$ short, which is the size of the radiative correction the tree-level formula omits — and that agreement is the check on the coefficient.

## The Constraints the Action Imposes: The Contact Is a Limit with a Scale

The expansion parameter. The contact is the leading term of an expansion in $k^2/M_W^2$, so the action imposes a scale below which it may be used. That scale is not a convention: it is the mass of the field that was eliminated, and every process has a momentum transfer that can be compared with it.

The unitarity bound. The contact amplitude grows with energy, and at some energy it violates unitarity. The bound is $\sqrt{s}\lesssim 4\pi M_W/g$, which is the scale at which the $W$ must be restored. The bound is a consequence of the contact's dimension and is the technical statement of the theory's upper limit.

Why the $W$'s own constraint does not appear. In the unitary gauge the $W$'s three polarizations are all physical and its constraint has been used to remove the fourth; the eliminated field carried no constraint into the contact. In a covariant gauge the Goldstone would appear in the contact's corrections, and the corrections would be gauge dependent while the rates are not.

**The bound is below the Planck scale and above the weak scale.** The window in which the contact is both accurate and unitary is wide, from nuclear momenta to the $W$ mass, and that width is why the four-fermion theory was a complete description for forty years.

## The Structural Consequence: The Vertex Is Chiral and the Coefficient Is a Ratio of Two Numbers

The statement. The interaction's structure is fixed by the algebra's chirality projection, and its strength is fixed by the ratio $g^2/M_W^2$. Neither is a new parameter: the vertex is the algebra's, and the strength is the electroweak sector's.

The consequence for the corpus's boundary. This is the one place where a weak-interaction statement is exact in the algebra and not transcribed. The projection is an algebraic operation and the current is an algebra bilinear, so the vertex is carried; the mass and the coupling are not. The article's status is therefore mixed in a precise sense, and the mix is stated rather than hidden.

What the structure predicts. The ratio $\Gamma(\pi\to e\nu_{\mathrm{neu}})/\Gamma(\pi\to\mu\nu_{\mathrm{neu}})=m_e^2/m_\mu^2$ at leading order, the $(1-m_l^2/m_\pi^2)^2$ phase space, and the $m_\mu^5$ scaling of the muon rate. All three are consequences of the $V-A$ vertex and the contact, and all three are confirmed to a few percent.

**What it does not predict.** The value of $G_F$, the value of $M_W$ and the existence of the neutral current. The first two are measurements, and the third requires the neutral-current action the Møller article treats.

## The Noether Currents: The Charged Current Is the Ladder Current

The current's origin. Before breaking, the fermion sector is invariant under global $SU(2)_L$, and the Noether currents are $J_{a,\mu}=\bar{\tilde\Xi}\gamma_\mu\tau_{a}\tilde\Xi$. The ladder combinations $J^{\pm}_\mu=J_{1,\mu}\mp iJ_{2,\mu}$ are the charged currents, and the $W$'s interaction term is the gauging of exactly these.

Conservation and its failure. The charged current is conserved in the massless limit and fails to be conserved when the fermions have mass, because a mass term couples the two chiralities and the current is one of them. The divergence is proportional to the mass, and that proportionality is the statement that the axial part alone is the one with the anomaly.

The anomaly. The axial current's divergence contains the triangle anomaly, which cancels between the doublet's members in the Standard Model; the cancellation is the anomaly article's, and this article's contribution is that the current whose anomaly is at issue is the one the action gauges.

Energy–momentum. Translation invariance gives $T_{\mu\nu}$ with the fermion and $W$ contributions; its trace is nonzero because of the mass, and the trace anomaly is again the quantum part.

**What there is not.** No conserved charge that survives the breaking except the electric charge; the weak isospin current is not conserved by the vacuum, which is the same statement as the $W$'s mass.

## What the Principle Adds and What It Relabels

Adds.

- *The elimination as a variation.* The contact is not a model of the weak interaction; it is what the action becomes when one field is solved for. The derivation is one line and it is exact up to the momentum expansion.
- *The coefficient's origin.* $G_F$ is $g^2/(8M_W^2)$ and not a fundamental constant; the action shows the ratio.
- *The natural cut-off.* The scale of the expansion is the mass of the eliminated field, and the action makes that visible.

Relabels.

- *Fermi's theory.* It is not a separate theory; it is the low-energy limit of the charged-current action.
- *The $V-A$ vertex.* It is not an empirical rule; it is the algebra's chirality projection.
- *The unitarity bound.* It is not a failure of the model; it is the statement of where the eliminated field must return.

The distinction that matters. The action is local and the effective action is not. The elimination produces a non-local term whose expansion is the contact, and the expansion's scale is the mass that was removed.

## Open Questions

Is the $(1-\gamma_5)$ projection derivable from the algebra's structure? The corpus writes it as the right multiplication by $\vec e_z$ and treats the projection as exact. Whether the choice of that unit imaginary vector is fixed by something deeper, or is a convention matching the observed chirality, is not settled.

## Summary

The action. The $W$'s Proca action plus $-\frac{g}{2\sqrt2}(W^{+}J^{+}+W^{-}J^{-})$. Varying $W$ gives its equation with the current as source; solving at low momentum gives the contact $-\frac{G_F}{\sqrt2}J^{+}J^{-}$ with $G_F/\sqrt2=g^2/(8M_W^2)$.

The three findings. The contact is an exact Gaussian elimination followed by a momentum expansion, and the expansion's scale is $M_W$. The $V-A$ structure is the algebra's chirality projection and is exact. The strength is a ratio of the electroweak coupling and mass, so the four-fermion theory has no parameter of its own.

**The boundary.** The vertex is the algebra's; the mass, the coupling and the neutral current are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi_{\mathrm u}$, $\tilde\Xi_{\mathrm d}$ | upper and lower doublet fermions |
| $J^{+}_\mu=\bar{\tilde\Xi}_{\mathrm u}\gamma_\mu(1-\gamma_5)\tilde\Xi_{\mathrm d}$ | charged current |
| $W^{\pm}_\mu$ | charged vector fields, mass $M_W$ |
| $g$ | weak coupling |
| $G_F$ | Fermi constant, $1.1663787\times10^{-5}$ GeV$^{-2}$ |
| $G(k)$ | massive-vector propagator $1/(M_W^2-k^2)$ |

## Further Reading

- [The Weak Interaction in Biquaternionic Form](the-weak-interaction-in-biquaternionic-form.html) — the parent: the contact, the rates, the pion-to-lepton ratio.
- [The Lagrangian and the W and Z Bosons](the-lagrangian-and-the-w-and-z-bosons.html) — the action the eliminated field belongs to.
- [The Lagrangian and the Electroweak Theory](the-lagrangian-and-the-electroweak-theory.html) — the charged and neutral currents in one action.
- [Møller Scattering in Biquaternionic Form](moller-scattering-in-biquaternionic-form.html) — the neutral-current counterpart of the elimination.
- [Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model: Four Conditions Become None](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) — the divergence of the axial current this action gauges.
