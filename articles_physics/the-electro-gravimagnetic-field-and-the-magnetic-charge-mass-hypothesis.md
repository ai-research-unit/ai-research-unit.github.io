# __The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis__

## Introduction

The biquaternionic formulation of Maxwell's equations is usually presented as a rewriting: one equation, one field strength, no new physics. The companion article *Maxwell's Equations in the Biquaternionic Formulation* takes that view, and its section on the A-field is explicit that the complex three-vector $\boldsymbol{\mathcal A} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H}$ is the Hodge-dual field strength and not an independent object. The companion article *The Magnetic Monopole in Biquaternionic Form* likewise treats magnetic charge as the source half of the dual, and stops at the algebra.

A different reading is possible. If magnetic charge is not merely admitted but **identified with gravitational mass**, then the complex magnetic field acquires a gravitational half: its potential part is a gravitational field and its solenoidal part is the magnetic field. The combined complex field then couples to both electric and gravitational charge, and the algebra of the dual field becomes a candidate language for a unified electro-gravimagnetic dynamics, with laws modelled on Newton's.

This article records that programme, due to L. A. Alexeyeva, in the form the corpus can state and bound. It is a record of an **external programme**, not a development of the framework: the identification of magnetic charge with gravitational mass is a hypothesis of its author, not a consequence of the algebra, and the framework's own epistemic standard — that elegance and covariance are not evidence — applies to it in full. The programme was also **revised by its author**: the 2009 paper found that the charge–current conservation law fails to be Lorentz invariant when fields interact, and repaired it with a scalar resistance field and a modified, open, Maxwell system. The 2007 forms are given below, and the revision is developed in its own section.

Two sources are recorded. The 2007 preprint is Russian and its text layer is degraded; the 2009 sequel exists in a clean English version (arXiv:1104.1483v1) and it is the source of the revision, of the stress pseudotensor and of the Cauchy theory recorded here. Wherever the two disagree, the disagreement is a sign or a normalisation and it is stated rather than smoothed over: the power–force biquaternion $\tilde{\mathcal F} = M - i\mathbf{F}$ is defined the same way in both, but the source biquaternion is $\tilde{\Theta} = i\rho + \mathbf{J}$ in 2007 and $\tilde{\Theta} = -i\rho - \mathbf{J}$ in 2009, while the Maxwell equation $\tilde{\nabla}^+\boldsymbol{\mathcal A} = -(i\rho + \mathbf{J})$ is the same in both. Coefficients are quoted only where they close: the force split is carried in the companion article on the density force, where the one coefficient that does not close is flagged, and the stress pseudotensor below is carried as a structure without its coefficients.

## The A-Field and Its Content

Write the field as one complex three-vector with the medium's constants absorbed,

$$
\boldsymbol{\mathcal A} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H},
\qquad
c = \frac{1}{\sqrt{\epsilon\mu}},
\qquad
\tau = ct .
$$

The symmetrized Maxwell system for this object is one complex equation and one complex scalar equation,

$$
\partial_\tau \boldsymbol{\mathcal A} + i\,\mathrm{rot}\,\boldsymbol{\mathcal A} + \mathbf J = 0,
\qquad
\rho = \mathrm{div}\,\boldsymbol{\mathcal A} = \frac{\rho_E}{\sqrt{\epsilon}} - i\,\frac{\rho_H}{\sqrt{\mu}},
\qquad
\mathbf J = \sqrt{\mu}\,\mathbf{j}_E - i\sqrt{\epsilon}\,\mathbf{j}_H .
$$

Here $\rho_E = \epsilon\,\mathrm{div}\,\mathbf{E}$ and $\rho_H = -\mu\,\mathrm{div}\,\mathbf{H}$ are the electric and magnetic charge densities, and $\mathbf{j}_E$, $\mathbf{j}_H$ the corresponding currents. This is the A-field of the Maxwell article in the source's sign convention: the Maxwell article writes the same equation as $-c^{-1}\partial_t\boldsymbol{\mathcal A} - i\,\mathrm{rot}\,\boldsymbol{\mathcal A} = \mathbf{j}$ with $\mathbf{j} = \sqrt{\mu}\,\mathbf{j}_E - i\sqrt{\epsilon}\,\mathbf{j}_H$, which is the present equation multiplied by $-1$ with the same $\mathbf J$. The two conventions must not be mixed.

The energy density and the energy flux are read off the A-field directly,

$$
W = \tfrac{1}{2}\,\|\boldsymbol{\mathcal A}\|^2 = \tfrac{1}{2}\left(\epsilon\,\|\mathbf{E}\|^2 + \mu\,\|\mathbf{H}\|^2\right),
\qquad
\mathbf{P} = \tfrac{1}{2}\,i\,\boldsymbol{\mathcal A}\times\boldsymbol{\mathcal A}^* = c^{-1}\,\mathbf{E}\times\mathbf{H},
$$

because the square of the A-field has the dimensions of energy density — which is why the source calls it an **energetic** field. Both identities are pure algebra in the definitions and were checked numerically (residuals below $2\times10^{-15}$ at forty random field points; the Maxwell article's convention without the $1/c$, $\tfrac{1}{2}ic\,\boldsymbol{\mathcal A}\times\boldsymbol{\mathcal A}^* = \mathbf{E}\times\mathbf{H}$, holds as well). The A-field's Green tensor, its retarded solution and the shock-inclusive Cauchy theory are the Maxwell article's and are not repeated here.

**A notational warning about the star, because the source uses it two ways.** The source's involution is defined on the algebra by $F^* = \bar f - \bar F$, and the elements with $F^* = F$ — real scalar part, purely imaginary vector part — are what it calls **unitary**; they are exactly the elements $f_1 + iF_2$ of the corpus's Hermitian subspace $\mathbb{M}_+$. So the source's star is the corpus's Hermitian conjugation ${}^{*}$, **not** the corpus's $\bar{\tilde Q}$, which conjugates the coefficients alone; the two agree only on fields with real scalar and vector parts. The energy and Poynting display above, however, uses the star for the coefficient conjugate, $\boldsymbol{\mathcal A}^* = \sqrt{\epsilon}\,\mathbf{E} - i\sqrt{\mu}\,\mathbf{H}$, and on a field with vanishing scalar part the two differ by $-1$. Consequently the source's printed product identity for the energy–momentum, $\tilde\Pi = \tfrac12\boldsymbol{\mathcal A}^*\circ\boldsymbol{\mathcal A} = \tfrac12(\bar{\boldsymbol{\mathcal A}},\boldsymbol{\mathcal A}) - \tfrac12[\boldsymbol{\mathcal A},\bar{\boldsymbol{\mathcal A}}] = W + i\mathbf P$, does not close under either reading: recomputed from the product rule, the paper's own conjugation gives $W - i\mathbf P$ and the coefficient conjugation of its energy display gives $-W + i\mathbf P$. The last two expressions, $\tfrac12(\bar{\boldsymbol{\mathcal A}},\boldsymbol{\mathcal A}) = W$ and $-\tfrac12[\boldsymbol{\mathcal A},\bar{\boldsymbol{\mathcal A}}] = i\mathbf P$, are each correct, so the printed $W + i\mathbf P$ is right as a statement about the energy density and the flux separately; what fails is the chain that writes them as one product. The corpus keeps the energy display's convention and states $W$ and $\mathbf P$ directly.

## The Magnetic-Charge–Mass Hypothesis

The programme rests on one identification.

**The hypothesis.** The density of magnetic charge is the density of gravitational mass, $\rho_H \leftrightarrow \rho_{\mathrm{grav}}$ (up to a constant fixed by units).

Its reading of the field follows. Since $\rho_H = -\mu\,\mathrm{div}\,\mathbf{H}$, the **potential** part of $\mathbf{H}$ is sourced by mass and is the gravitational field; the **solenoidal** part of $\mathbf{H}$ is the magnetic field. The complex combination $\mathbf{H}$ is therefore a **gravimagnetic** field, and $\boldsymbol{\mathcal A}$, which pairs it with the electric field, is **electro-gravimagnetic**.

Three things must be said about the hypothesis, and the corpus says them plainly.

- **It is a hypothesis, not a derivation.** Nothing in the algebra of $\mathbb{B}$ selects the identification. The corpus's monopole article admits magnetic charge as the symmetric completion of the sources and derives the Dirac quantisation condition as a consistency requirement; that is an algebraic statement, and it does not force the mass identification. The programme's own summary calls the identification a hypothesis and offers physical consequences as consequences to be tested.
- **It is the reason the programme exists.** Without it, the A-field is the dual field strength and nothing more. With it, the dual field strength is a two-sector field, and its interaction equations are candidate laws for charged and massive matter at once. The corpus records it because a reader meeting the A-field should know which reading is which.
- **It was revised.** The 2009 paper reports that under field interaction the charge–current conservation law is not the standard one — the coupled system is **open** — and repairs it by adding a scalar resistance field $a(\tau,\mathbf{x})$ to the scalar part of the strength, giving a modified Maxwell system for an open system. A later paper proves the interaction equations Poincaré–Lorentz invariant. The natural reading, which the corpus states as an open question rather than as established, is that the invariance holds for the modified (open) system and that the $a$ term is what makes it work; the later paper does not itself say so. Any corpus statement about the programme must carry both halves.

## The Mutual Complex Gradients

The programme's generating device is a pair of first-order operators, called the **mutual complex gradients**,

$$
D^+ = \partial_\tau + i\nabla,
\qquad
D^- = \partial_\tau - i\nabla,
\qquad
\Box = D^-D^+ = D^+D^- ,
$$

which the source calls unitary because each is fixed by the algebra's involution, $(D^\pm)^* = D^\pm$ — the elements with $F^* = F$ are the source's **unitary** biquaternions, exactly those of the form $f_1 + iF_2$, and they are the corpus's Hermitian subspace $\mathbb{M}_+$. Applied repeatedly to the potential biquaternion in the Lorenz gauge they generate the field strength, the charge–current, the conservation law and the wave equation; the first-order equation $D^+\boldsymbol{\mathcal A} + \tilde{\Theta} = 0$ is the source's symmetrized Maxwell system, and it reads the charge–current as the complex gradient of the A-field strength — charges and currents are, on this reading, simply the physical manifestation of that gradient.

The pair is not a new operator for the corpus; it is the corpus gradient in another sign convention. With the corpus's gradient $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ and its quaternion conjugate $\tilde{\nabla}^{\natural}$,

| Source operator | Corpus operator | Composition |
|---|---|---|
| $D^+ = \partial_\tau + i\nabla$ | $D^+ = i\,\tilde{\nabla}$ | $D^-D^+ = \partial_\tau^2 - \Delta$ |
| $D^- = \partial_\tau - i\nabla$ | $D^- = i\,\tilde{\nabla}^{\natural}$ | $\Box_{\mathrm{corpus}} = \tilde{\nabla}\tilde{\nabla}^{\natural} = -\,D^-D^+$ |

The dictionary is exact, and it was checked numerically on a smooth test function (residuals at machine precision). The sign in the last column is the whole of the difference: the corpus works in the $ict$ (Euclidean) convention, where $\partial_{ict} = -i\,\partial_\tau$ and $\Box = \partial_{ict}^2 + \Delta$ is elliptic, while the programme works in the $\tau = ct$ (hyperbolic) convention, where $\Box = \partial_\tau^2 - \Delta$ is the wave operator. The two dictionaries differ by $i$ and by an overall sign; neither is more fundamental, but a formula copied from one into the other without the factor $i$ and the sign will fail.

**The homogeneous biwave equation as an external-field transformation.** The fourth paper of the *Differential algebra of biquaternions* series reads the same gradients with a coefficient. It takes

$$
\nabla^\pm B + F\circ B = G, \qquad \nabla^\pm = \partial_\tau \pm i\,\nabla,
$$

with a **constant** structural coefficient $F = f + \mathbf{F}$, and it observes that in the vector-coefficient case the homogeneous equation can also be read as the equation of transformation of mass-charges and of electric and gravimagnetic currents in an **external** electro-gravimagnetic field, whose strength is the vector $\mathbf{F}$ itself. The reading is a special case of the programme's own, and it is worth separating from the programme's statements. The objects that transform are exactly the ones this article has built — the charge–current biquaternion $\tilde\Theta = i\rho + \mathbf J$ and the power–force biquaternion $\tilde{\mathcal F} = M - i\mathbf F$ — and the coefficient is the **external** field's, taken constant, with no back-reaction of the current on the field it sits in. In the programme's interaction equations the field and the sources determine each other; here the field is given and the equation is linear in $B$, so the transformation is of a test current, not of a self-consistent pair. The source states the reading as a route open to its solutions rather than as a derivation, and it postpones the general case — a coefficient with both a scalar and a vector part, so that the external strength carries a scalar component as well — to the last paper of its cycle. The corpus records the route and the postponement and rests on neither. The solutions the reading concerns are the source's **twistors**, catalogued in *Twistor Theory and Biquaternions*; the stationary kernel and the operator's second-order form are in *The Yang–Mills Equation in Biquaternionic Form*, and the factorisation they make possible is in *The Klein–Gordon Equation in Biquaternionic Form*.

## The Postulates, and the Classical Limit

The 2016 *Law of Inertia* paper states its basis as **three postulates**, and it repays separating what each supplies. **Postulate 1** is the bigradiental connection $D^+\boldsymbol{\mathcal A} + \tilde{\Theta} = 0$ established in the preceding section: charge and current are the complex gradient of the strength. Taken alone it is **not a closed system**, and the source says so explicitly — the one equation determines the field from the sources and the sources from the field, with nothing to decide between the two. **Postulate 2** adds the free-source law $D^-\tilde{\Theta} = 0$, the first Newton law of the next section, and it is what closes the pair. **Postulate 3** asserts that these two equations together describe the free charge–current and the EGM field it generates. The EGM equation is hyperbolic and its four-component system is connected, which the classical Maxwell system is not, and the source offers this as its reason for preferring the bigradiental form. The count and the numbering belong to this paper: the 2019 statement of the model keeps Postulate 1 as the same bigradiental connection but makes its Postulate 2 the action–reaction (third) law and its Postulate 3 the second law, so "the postulates" must be read with the paper they come from.

The source attaches a **remark** to the classical comparison, recorded here as the programme's. The ordinary Maxwell scalar equation, taken with a time-dependent charge, is in the author's reading incompatible with the wave character of the field; it holds only when the charges and currents are time-independent. The same restriction is said to apply to the gravitational Poisson equation, which holds only for static mass. On this reading the classical equations are the static limit of the EGM system rather than an equal partner of it, and the scalar field the bigradiental form retains is what that limit discards.

## Field Analogues of Newton's Laws

From the free-field and interaction equations the programme builds a law structure that mimics Newton's three laws and adds a thermodynamic analogue.

### The first law: the free field

In the absence of other fields the force vanishes, and the interaction equation reduces to the inertia equation

$$
D^-\tilde{\Theta} = (\partial_\tau - i\nabla)\,\tilde{\Theta} = 0,
\qquad
\tilde{\Theta} = i\rho + \mathbf{J}.
$$

Its scalar and vector parts are

$$
\partial_\tau\rho + \mathrm{div}\,\mathbf{J} = 0,
\qquad
\nabla\rho + \partial_\tau\mathbf{J} - i\,\mathrm{rot}\,\mathbf{J} = 0 .
$$

This is verified by expanding the product in the algebra; the scalar equation is the conservation of the combined charge–current, and the vector equation couples the charge gradient to the currents, the solenoidal gravimagnetic current feeding the electric current and conversely. Taking the divergence or the curl of the vector equation and using the scalar equation gives homogeneous wave equations for $\rho$ and $\mathbf{J}$: in a free field the charges and currents **disperse** at speed $c$. The author names this the analogue of inertia — a free field carries its charges as waves, with nothing holding them together.

### The free source in components and as a spinor

The free first-law equation can be split into its real electric and gravimagnetic parts, and the source also writes its general solution as a spinor. The split gives the four equations

$$
\partial_t\rho_E + \mathrm{div}\,\mathbf{j}_E = 0,
\qquad
\partial_t\rho_H + \mathrm{div}\,\mathbf{j}_H = 0,
$$

$$
\partial_\tau\mathbf{j}_E = \sqrt{\epsilon/\mu}\;\mathrm{rot}\,\mathbf{j}_H - c\,\mathrm{grad}\,\rho_E,
\qquad
\partial_\tau\mathbf{j}_H = -\sqrt{\mu/\epsilon}\;\mathrm{rot}\,\mathbf{j}_E - c\,\mathrm{grad}\,\rho_H .
$$

The first pair says that in a free field the electric and the gravimagnetic charge are separately conserved; the second says that each current is driven by the curl of the *other* current and by the gradient of its own charge. Both pairs were checked against the expansion of $D^-\tilde{\Theta}=0$, with residuals at machine precision ($5\times10^{-16}$).

The source draws two further consequences for a free field, and the corpus records them as the programme's. The electric and the gravimagnetic charge density can each be of either sign; and under a **stationary vibration** — the monochromatic free solutions of the same law, developed in *Harmonic Elementary Particles and the Periodic System of Atoms* — the electric charge is said to pass into the gravimagnetic charge and back. The second claim sits in visible tension with the two separate conservation laws displayed just above, which forbid such an interchange in a free field; the source does not reconcile the two, and it gives no rate and no selection rule for the transfer.

The source also writes the free charge–current as a **spinor**, $\tilde\Theta = D^-\psi_0 + i\sum_j D^-(\psi_j e_j)$ with $\Box\psi_j = 0$, naming a **pulsar** for a scalar potential and a **spinor** for a vector potential, and adding convolutions it calls **fibers**, **tissue** and **body** for matter on a line, on a surface and over a volume. That construction, its closed forms and its particle reading are developed in *Harmonic Elementary Particles and the Periodic System of Atoms*, which builds them from the same free-field law; the physical content of the free field recorded here is the pair of equations above.

### The second law: the interaction equation

A field's charge–current is changed by the field of the other charges, in the direction of the power–force biquaternion. The proposed equations are

$$
\kappa\,D^-\tilde{\Theta} = -\,\tilde{\Theta}\circ\tilde{\mathcal A}',
\qquad
\kappa\,D^-\tilde{\Theta}' = -\,\tilde{\Theta}'\circ\tilde{\mathcal A},
$$

together with the third-law relation below and the Maxwell equation $D^+\tilde{\mathcal A} + \tilde{\Theta} = 0$ for each field. Here $\kappa$ is a single dimensional coupling constant and $\tilde{\mathcal A}$ is the A-field biquaternion of the field. The system is closed and nonlinear, and its right-hand side is the force density of the *other* field — the model deliberately makes a field act on other charges, never on its own. When one field dominates, $W' \gg W$, the pair collapses to a single equation for the weaker field's charge–current with the stronger field's A-field as a known input, which is the form in which the programme's applications are stated.

The scalar part of the second-law equation, together with charge conservation, forces the source's conclusion $M = 0$, i.e.

$$
(\mathbf{E}',\mathbf{j}_E) + (\mathbf{H}',\mathbf{j}_H) = 0,
\qquad
(\mathbf{B}',\mathbf{j}_E) - (\mathbf{D}',\mathbf{j}_H) = 0,
$$

with $\mathbf{B} = \mu\mathbf{H}$ and $\mathbf{D} = \epsilon\mathbf{E}$. The author offers these two relations as experimentally checkable, and they are recorded here as the programme's claim.

**This conclusion is superseded by the programme's own later work.** The 2009 paper drops the assumption on which it rests — that the force density vanishes, so that the right-hand side of the scalar equation is zero. For an open system it is not zero, the conservation law of a single source acquires the external power as its source term, and the assumption that it can be postulated in the traditional form turns out to be the error the revision exists to correct. The revision is developed below, in *The 2009 Revision*.

### The third law: action and reaction

The analogue of Newton's third law is the algebraic relation

$$
\tilde{\Theta}\circ\tilde{\mathcal A}' = -\,\tilde{\Theta}'\circ\tilde{\mathcal A}.
$$

Its scalar part requires the equality of the two power densities — the power delivered by the first field to the second equals the power delivered by the second to the first, in the sense of the force biquaternion of the next section. The author compares this to the **reciprocity identity of Betti** in continuum mechanics, which states the same equality of virtual works for a linearly elastic body. The comparison is the programme's, and it is an analogy of form, not a proven structural identity.

### The thermodynamic analogue

For the charge–current field the programme defines an energy density and a flux of its own,

$$
Q = \tfrac{1}{2}\|\mathbf{J}\|^2 = \tfrac{1}{2}\left(\mu\,\|\mathbf{j}_E\|^2 + \epsilon\,\|\mathbf{j}_H\|^2\right),
\qquad
\mathbf{P}_J = \tfrac{1}{2}\,i\,\mathbf{J}\times\mathbf{J}^* ,
$$

where $Q$ contains the Joule heat $\|\mathbf{j}_E\|^2$ and the kinetic energy of the mass current $\|\mathbf{j}_H\|^2$. The vector $\mathbf{P}_J$ is the current-field analogue of the Poynting vector and vanishes when the two currents are parallel or one is absent. The balance law has the shape of the first law of thermodynamics,

$$
\kappa\left(\partial_\tau Q - \mathrm{div}\,\mathbf{P}_J + \mathrm{Re}(\nabla\rho,\mathbf{J}^*)\right) = \mathrm{Im}\big(\tilde{\mathcal F},\mathbf{J}^*\big),
$$

with $\tilde{\mathcal F}$ the power–force biquaternion. The left side is the rate of change of the current energy, minus its flux, and one further term; the right side is the power supplied by the external force, which can increase or decrease that rate. The source presents this as the field analogue of the first law, with the extra term playing the part of the internal-energy change that an external work can offset. The sign of the flux term is fixed by the derivation — the inner product of the second-law equation with $i\bar{\mathbf J}$ gives $-c^{-1}\,\mathrm{div}(\mathbf{j}_H\times\mathbf{j}_E)$ and no other sign — and it is worth recording that the 2007 preprint prints the same law with $+\mathrm{div}\,\mathbf{P}_J$ while the 2009 paper prints the minus; the corpus takes the minus.

**The free field specializes the law to a decay.** With no other field the right side vanishes and the balance becomes

$$
\partial_\tau Q = -\mathcal U ,
$$

with $\mathcal U$ the sum of the current-field flux divergence and the two charge-gradient terms (the source's $U$; the corpus writes $\mathcal U$ to keep the boost biquaternion's $U$ free). The source presents this as the first law of a free source and asserts $\mathcal U \geq 0$: an isolated charge–current field loses its energy density at a rate it does not bound, which is the dissipative half of the inertia reading of the next section and is consistent with the dispersal of the free field's charges. The corpus carries the shape of the statement and not the coefficients of $\mathcal U$: recomputed from the paper's own definitions of $\rho$ and $\mathbf J$, the two medium factors are placed differently in the printed expression, and the sign of the charge-gradient pair depends on which of the paper's two uses of the star is taken. The inequality $\mathcal U \geq 0$ is asserted, not proved.

## The 2009 Revision: Transformations, the Scalar Field and the Open System

The 2007 forms above assume that the charge–current of a field is conserved. The 2009 paper reports that the assumption fails for an open system and repairs it. Four things change, and each is stated here in the corpus's notation.

**The transformation law is the corpus's rotor.** The programme builds its Lorentz transformation from the biquaternion

$$
U = \cosh\theta + i\sinh\theta\,\hat{\mathbf u},
\qquad
\|\hat{\mathbf u}\| = 1,
\qquad
U\bar{U} = 1,
$$

and its own formula for the power–force biquaternion is written with the *doubled* angle, $\mathrm{ch}\,2\theta$ and $\mathrm{sh}\,2\theta$. The consistent reading is therefore that $\theta$ is the **half-rapidity**,

$$
\cosh 2\theta = \gamma = \frac{1}{\sqrt{1-v^2}},
\qquad
\sinh 2\theta = \gamma v,
\qquad
\theta = \tfrac12\,\mathrm{artanh}\,v,
$$

so that $U$ is exactly the corpus's boost rotor $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf u}$ with $\psi$ the rapidity. Read as a full rapidity the transformations do not reproduce the standard boost; read as a half-rapidity they do. Since the rotor is Hermitian, $U^\dagger = U$, so the model's transformation is the corpus's conjugation

$$
\tilde{Q}' = \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*},
$$

the law the corpus already uses for four-vectors of either sector. The paper states it for the Hermitian coordinate $\tau + i\mathbf{x}$ as $\tilde{Z}' = U\tilde{Z}U$, which is the corpus's law because $U^\dagger = U$; on that coordinate it returns

$$
\tau' = \gamma\left(\tau + v\,\hat{\mathbf u}\cdot\mathbf{x}\right),
\qquad
\mathbf{x}' = \mathbf{x}_{\perp} + \gamma\left(\hat{\mathbf u}\cdot\mathbf{x} + v\tau\right)\hat{\mathbf u},
$$

the standard boost, and on the material-type coordinate $i\tau + \mathbf{x}$ the same expressions with $v \to -v$, which is one direction convention and not a second law. On the power–force biquaternion $M - i\mathbf{F}$ — Hermitian for real $M$ and $\mathbf{F}$, and the material-type element up to a central factor — it gives

$$
M' = \gamma\left(M - v\,\hat{\mathbf u}\cdot\mathbf{F}\right),
\qquad
\mathbf{F}' = \mathbf{F}_{\perp} + \gamma\left(\mathbf{F}_{\parallel} - vM\,\hat{\mathbf u}\right),
$$

So the model's covariance is not a new law requiring a new proof: it is the corpus's rotor action, and the paper's own intermediate display agrees with it term for term. Its final display of $M'$ prints $+\gamma v\,\hat{\mathbf u}\cdot\mathbf{F}$, which contradicts both that intermediate line and its own $\mathbf{F}'$ line, since $(M,\mathbf{F})$ transforms as a four-vector only with the relative minus; the corpus takes the sign that closes.

**Slips in the source, recorded so that a reader returning to it is not misled.** The transformation lemma is correct as printed and needs no repair, and the reversal of the sign of $\tilde{\Theta}$ between the two papers is a convention, not a contradiction. What does not close is the component split of the force, treated in the companion article on the density force, where the source's second half is short by one factor of $c$ in one term; and the printed $M'$ just noted. The paper's rewrite of the second law as the divergence of a stress pseudotensor, recorded below, inherits the same component line and does not reproduce it term for term either. None of these reaches the structural statements the corpus carries, and none of them is the transformation law.

**The conservation law is not Lorentz invariant for an open source.** With the four-vector law above, $M = 0$ together with $\mathbf{F} \neq 0$ in one frame gives $M' = -\gamma\,v\,\hat{\mathbf u}\cdot\mathbf{F} \neq 0$ in a boosted frame, unless the force happens to be perpendicular to the boost. A four-vector whose time component vanishes in one frame does not have a vanishing time component in another; only the trivial four-vector does. So the statement "$M = 0$", which is the assertion that the source is conserved, is not a Lorentz-invariant statement for an open system.

The interpretation of this fact matters, and the corpus states it carefully. The programme does not say that electric charge is not conserved. It says that the charge–current of a single field is not conserved *by itself*: the missing charge–current is exchanged with the other field, and the source field is not closed. The total of a collection of interacting fields is conserved, which is the "law of the single field" recorded above. The failure is the failure of a subsystem to be closed, and the statement is about which components of the source biquaternion are available to vanish, not about observer-dependence of physics.

**The scalar field and the modified Maxwell equations.** The repair is to let the field strength carry a scalar part. Write

$$
\tilde{F} = i\,a + \mathbf{F},
$$

with $a = a(\tau,\mathbf{x})$ the **scalar resistance field**. The modified Maxwell system then reads, in the programme's own symbols,

$$
\mathbf J = -\,\partial_\tau\boldsymbol{\mathcal A} - i\,\mathrm{rot}\,\boldsymbol{\mathcal A} + \mathrm{grad}\,a,
\qquad
\rho = \mathrm{div}\,\boldsymbol{\mathcal A} - \partial_\tau a,
$$

which is the pair of the first section with $\mathrm{grad}\,a$ added to the current and $-\partial_\tau a$ added to the charge, and which reduces to that pair precisely when $a = 0$ and the system is closed. Those two additions are the only two places the complex-gradient structure can put a scalar, so the modification is forced once $a$ is admitted: there is no third term to choose.

**The integrability reading.** In the corpus's language the ordinary conservation law is the integrability condition of the sourced Maxwell equation. Applying $\mathrm{Sc}\,\tilde{\nabla}^{\natural}$ to $\tilde{\nabla}\tilde{F} = -\tilde{R}$ annihilates the left side, because $\tilde{\nabla}^{\natural}\tilde{\nabla}$ is the scalar d'Alembertian and $\tilde{F}$ has no scalar part; what survives is $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R}) = 0$. With the scalar part $ia$ retained, the same calculation gives

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{R}\right) = -\,\Box\,(i a)
\qquad\Longleftrightarrow\qquad
\Box\,a \;\propto\; M,
$$

so the scalar field is sourced by the external power — the very quantity whose presence breaks the conservation law — and propagates as a wave. This is the cleanest form of the revision. Where the corpus's definition of the field strength discards the scalar part of $\tilde{\nabla}^{\natural}\tilde{\mathcal A}$ as gauge, the programme retains it, and the retained scalar is exactly the field whose d'Alembertian absorbs the failure of conservation.

**The word "modified" is not this corpus's modification, and the two must not be conflated.** The programme's repair adds a scalar field to the field strength and turns the Maxwell system into an **open** one: the source is no longer closed, and the added scalar is what absorbs the failure of conservation. The corpus has a modification of its own, in *Electromagnetism in Media: The Local Complex Structure at Work*, where the local complex structure of a material slice changes the constitutive relations — the medium, not the conservation law, is what is modified there. The two are different modifications, of different objects, for different reasons: one changes whether the source is closed, the other changes how the field and the medium are tied. The corpus's own Maxwell article and the entries of *the-field-strength-biquaternion-and-its-invariants* are unaffected by the programme's revision, and a reader who carries the programme's open system into them will change what the corpus states. The one thing that does transfer is negative and stated above: the corpus's own definition of the field strength discards the scalar part of $\tilde{\nabla}^{\natural}\tilde{\mathcal A}$ as gauge, and the programme's revision is exactly the choice to retain it. That contrast is the content; the modification itself is the programme's.

**Verification.** The following were recomputed in the course of recording this revision, symbolically or to machine precision: the dictionary $D^\pm = i\tilde{\nabla}, i\tilde{\nabla}^{\natural}$ and the sign $\Box_{\mathrm{corpus}} = -D^-D^+$; the power density $M$ against its component form; the current-field density $Q$ and flux $\mathbf{P}_J$; the equivalence of the second law with its two displayed components; the half-rapidity rotor, the four-vector law for $(M,\mathbf{F})$, and the transformation of the coordinate in the paper's own form $\tilde{Z}' = U\tilde{Z}U$, which returns the standard boost with residuals at machine precision; the charge–current interaction energy of the next section but one; and the integrability relation $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R}) = -\Box(ia)$, which returns the ordinary integrability condition when $a = 0$. The two papers' conventions were checked against each other rather than assumed, since they differ in the sign of $\tilde{\Theta}$.

**One coefficient that does not close, and is therefore not carried.** The source expands the vector part of the power–force biquaternion into two real halves, $\mathbf{F}_H$ and $\mathbf{F}_E$, and lists four named terms in $\mathbf{F}_H$ (Coulomb, gravitational, Lorentz, electromass). The scalar part closes exactly, and the split closes once the factor of $i$ that the source suppresses is placed correctly, which is done in the companion article on the density force; the single coefficient that does not close there is the second term of $\mathbf{F}_E$, which the derivation gives as $c\,\rho_H\mathbf{D}'$. The 2009 paper prints $\mathbf{F}_E$ twice and inconsistently — $c\,\rho_E\mathbf{B}' - \rho_H\mathbf{D}' + c^{-1}(\cdots)$ in §8 and $\rho_E\mathbf{B}' - \rho_H\mathbf{D}' + c^{-1}(\cdots)$ in §12 — so one factor of $c$ sits in a different term in each place, while the derivation puts it on both terms. Every named force sits in the half that closes and is unaffected. See the companion article for the properties and the `.context` for the residuals. The programme's 2019 statement of the same product carries **five** named terms rather than four: it keeps the four above, adds the **resistance–attraction force** $-\mathrm{Im}(\alpha\mathbf{J})$, built from the attraction–resistance scalar $\alpha$, and renames the fourth term — the corpus's **electromass force** $\mathbf{j}_H\times\mathbf{D}'$ — the **gravielectric force**. The author marks the gravielectric and the resistance–attraction terms as the model's **new forces**, the ones offered for an experimental test. The 2019 paper writes $\tilde{\Theta}$ with the opposite overall sign to the 2007/2009 pair, so its printed list is the negative of the expansion above term by term; the names and the count are what the corpus takes from it.

**What the corpus takes from the revision.** From the revision itself, two things, and no more. The transformation thread is a genuine addition to the programme's record: the model is covariant in the corpus's rotor sense and needs no new transformation law. The conservation thread is a structurally complete mechanism — a failure of integrability, a scalar field that repairs it, and a wave equation for that scalar — expressible in the same algebra as the rest of the corpus, and it is the reason the programme's own earlier conservation claim had to be withdrawn. Neither thread supplies a prediction. The 2009 revision introduces one more field and no new coupling strength; the author's 2016 paper fixes the field constant only in the static limit and only in terms of $G$, as the next section records. The total charge of a closed system is conserved in every experiment, so the modification cannot be detected by watching charge appear or disappear. The same paper supplies three further items, recorded in their own sections below and separate from the revision: the interaction energy of a pair of *sources*, which collapses to a central scalar; the non-symmetric stress pseudotensor with its hydrodynamic reading; and the Cauchy theory, in which the first-order operator is inverted by a first-order operator and the interaction becomes an integral equation.

## The 2017 Invariance Theorem

The 2009 revision recorded above leaves one thread of the programme's relativistic treatment open. The transformation of the fields is there, and so is the failure of the conservation law; a proof that the *interaction equations themselves* keep their form under a Lorentz transformation is not. The author's 2017 paper supplies that proof: the charges–currents interaction system — the two second-law equations, the third-law reciprocity $A'\circ\Theta = -A\circ\Theta'$, and the two Maxwell equations — is invariant under the group of Poincaré–Lorentz transformations, and with it the paper derives the relativistic formulae for the densities of electric and gravimagnetic charges and currents, for the active power and for the forces.

**The transformation is the corpus's rotor.** The paper builds its transformation from $L = UW$, the boost $U$ compounded with the spatial rotation $W$, and states the law on the coordinate biquaternion as a rotor sandwich — for the unit-norm rotor, the corpus's conjugation. The reading recorded in the revision applies unchanged: $U$ is the corpus's boost rotor with $\theta$ the half-rapidity, $\cosh 2\theta = \gamma$ and $\sinh 2\theta = \gamma v$, and since the rotor is unit-norm the law is the corpus's rotor conjugation $\tilde{Q}' = \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ on the four-vectors of either sector. The charge–current biquaternion $\tilde{\Theta} = i\rho + \mathbf J$ and the power–force biquaternion $\tilde{\mathcal F} = M - i\mathbf F$ are four-vectors of the programme, and the theorem says that each transforms by that conjugation.

**The transformation formulae.** For a boost in the direction $\hat{\mathbf u}$ with speed $v$ the theorem gives

$$
\rho' = \gamma\bigl(\rho + v\,(\hat{\mathbf u},\mathbf J)\bigr),
\qquad
\mathbf J' = \mathbf J_{\perp} + \gamma\bigl(\mathbf J_{\parallel} + v\rho\,\hat{\mathbf u}\bigr),
$$

which is exactly the transformation of the four-current of *Relativistic Mechanics in Biquaternionic Form*: the combined density and current form a four-vector and $\rho^2 - \|\mathbf J\|^2$ is preserved. The power–force biquaternion transforms the same way,

$$
M' = \gamma\bigl(M - v\,(\hat{\mathbf u},\mathbf F)\bigr),
\qquad
\mathbf F' = \mathbf F_{\perp} + \gamma\bigl(\mathbf F_{\parallel} - vM\,\hat{\mathbf u}\bigr),
$$

and this is the line the 2009 paper prints inconsistently: the 2017 paper prints the sign that closes, and the correction the revision adopted is thereby confirmed. Both pairs were recomputed here (100 random boosts each) — the four-vector laws against the standard boost, their composition, and the preservation of the Minkowski invariants $\rho^2 - \|\mathbf J\|^2$ and $M^2 - \|\mathbf F\|^2$ — all at machine precision. Under a pure rotation the scalar parts are untouched, $\rho' = \rho$ and $M' = M$, as they must be.

The electric and the gravimagnetic halves separate. The paper writes the same four-vector law for the electric density and current pair and for the gravimagnetic pair, each with its own factor of $c$. The gravimagnetic mass density is where the hypothesis is felt: its transform carries the Einstein factor $\gamma\rho_H$ together with a term proportional to the electric current, so that a boost can either raise or lower the gravimagnetic mass density according to the direction of the electric current, the components of both currents transverse to the boost being unchanged. The paper reads the first term as the relativistic increase of mass; the corpus records the statement and the reading and nothing further, since neither is a prediction.

**Why the equations are invariant.** The proof is the covariance recorded in *The Poincaré Group and the Biquaternion Frame*. A unit-norm rotor conjugates the algebra, and conjugation is an automorphism,
$$
(LAL^{*})(L\Theta L^{*}) = L\,(A\Theta)\,L^{*},
$$
while the mutual bigradients transform by the same conjugation — the paper's Lemma 5.1, whose corpus form is the covariance identity of that article — so the gradient of a transformed field is the transform of the gradient. Every term of the interaction system therefore acquires the same pair of rotor factors, and the equation is form-invariant. Both facts were checked independently on random rotors and random biquaternions: the automorphism, and the unit norm $L\circ L^{*} = 1$ that makes $L^{*}$ an inverse.

**The reconciliation with the 2009 finding.** The corpus records both results and states the reading that makes them compatible. The 2009 finding is about a *condition*: the statement $M = 0$, that a single source is closed, is not a Lorentz-invariant statement, because a four-vector whose time component vanishes in one frame has a non-vanishing one in another. The 2017 theorem is about *equations*: the interaction system is covariant. An open system's equations can be covariant while the condition that a subsystem be closed is not, and the two statements are then about different objects. The 2009 scalar field $a$ is the programme's mechanism for the second and does not enter the 2017 proof of the first. The paper itself does not mention the 2009 conservation finding, so the corpus states this reading as its own and leaves open whether the invariance theorem is intended for the modified system.

**The Lorentz condition, in a different role.** The 2017 paper fixes the representation by requiring the potential to satisfy the Lorentz condition $\partial_\tau\phi = \mathrm{div}\,\boldsymbol\Phi$, imposed rather than chosen, and the ordinary Maxwell case $\alpha = 0$, $\rho_H = 0$ is recovered once it holds. The corpus's own Maxwell article treats the same condition as a free gauge fixing — "a choice of gauge, not a physical condition", with the scalar $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ a gauge artifact. The formula is the same; the logical role is not, and the corpus records the difference without choosing between the two. The gauge section of *Maxwell's Equations in the Biquaternionic Formulation* carries the cross-reference.

**Verification.** The following were recomputed in the course of recording this theorem: the four-vector laws for $(\rho,\mathbf J)$ and for $(M,\mathbf F)$ against the standard boost; the preservation of both Minkowski invariants; the addition of rapidities under composed boosts; that the unit-norm rotor conjugation is an algebra automorphism; and, on the coordinate biquaternion, that the rotor form reproduces the paper's component boost (the sandwich is $U Z U$ in the paper's normalisation, the unit-norm conjugation being the same law on the four-vectors). The one class of statement not carried is the paper's explicit component display of the electric and gravimagnetic split, whose extracted text does not close: its structure is recorded, its coefficients are not.

## The Static Limit and the Coupling

The revision adds the scalar field to the strength, and with it the model can be compared with Newtonian gravity in the static case. The static form of the modified system is

$$
\mathrm{rot}\,\mathbf{H} + c^2\,\mathrm{grad}\,\alpha_1 = \mathbf{j}_E,
\qquad
\mathrm{rot}\,\mathbf{E} - c^2\,\mathrm{grad}\,\alpha_2 = \mathbf{j}_H,
\qquad
\epsilon\,\mathrm{div}\,\mathbf{E} = \rho_E,
\qquad
\mu\,\mathrm{div}\,\mathbf{H} = -\rho_H ,
$$

with $\alpha = \alpha_1 + i\alpha_2$, the two real weights being the source's $a_1, a_2$ in $\alpha = i\,a_1/\epsilon + a_2/\mu$, so that $\alpha_1 = a_2/\mu$ and $\alpha_2 = a_1/\epsilon$. The last equation is the one that carries gravity. Writing the potential part of $\mathbf{H}$ as the negative gradient of a Newtonian potential, $\mathbf{H} = -\mathrm{grad}\,\phi$, it becomes

$$
\Delta\phi = \frac{\rho_H}{\mu},
$$

so the potential of the gravitational field obeys Poisson's equation and the field $\mathbf{H} = -\mathrm{grad}\,\phi$ points towards its source: for a positive mass density the static field is **attractive**. At this point the identification $\rho_H \leftrightarrow \rho_{\text{mass}}$ becomes quantitative, because the strength of the Poisson equation fixes the field constant of the medium. The source states the choice,

$$
\mu = \frac{1}{4\pi G},
$$

with $G$ the gravitational constant (the source writes $\gamma$ for it), which is the ordinary Poisson equation $\Delta\phi = 4\pi G\,\rho_{\text{mass}}$.

This closes a gap the corpus had recorded. The identification of magnetic charge with mass is a choice, but once it is made the constant $\mu$ of the A-field is no longer free: reading $\rho_H$ as the mass density and demanding the Poisson limit ties $\mu$ to Newton's constant and fixes the sign of the static force as attraction. What it does **not** do is predict gravity. The value of $G$ enters by hand through $\mu$, exactly as the electric charge enters by hand through $\rho_E$; no relation in the model determines the strength of the gravitational coupling from the algebra. The revision fixes the identification and the sign, not the number.

Both steps were checked numerically. For a Gaussian mass density of unit total mass, the Newtonian potential $\phi(r) = -(G M/r)\,\mathrm{erf}\big(r/(\sqrt2\,\sigma)\big)$ satisfies $\Delta\phi = 4\pi G\rho$ to the finite-difference floor, and with $\mu = 1/(4\pi G)$ and $\mathbf{H} = -\mathrm{grad}\,\phi$ the static field satisfies $\mu\,\mathrm{div}\,\mathbf{H} = -\rho_H$ to $10^{-8}$.

## The Unified Field and the Interaction Energy

Summing the second-law equations over $M$ interacting fields cancels the force terms pairwise, because each pair contributes a force and its reaction. The total charge–current therefore satisfies

$$
D^-\Big(\sum_{k=1}^{M}\tilde{\Theta}_k\Big) \equiv 0,
$$

so the **combined field is free**: all forces are internal, exactly as in the mechanics of interacting bodies. The author calls this the law of the single field.

The energy–momentum of the combined field separates the same way. With the energy–momentum biquaternion of each field written $\tilde{\Pi}_k$,

$$
\tilde{\Pi} = \sum_{k}\tilde{\Pi}_k + \delta\tilde{\Pi},
\qquad
\delta\tilde{\Pi} = \sum_{k\ne l}\tilde{\Pi}_{kl},
\qquad
\tilde{\Pi}_{kl} = \tfrac{1}{2}\left(\tilde{\mathcal A}_k\circ\tilde{\mathcal A}_l^* + \tilde{\mathcal A}_l\circ\tilde{\mathcal A}_k^*\right),
$$

where $\tilde{\Pi}_{kl}$ is the **interaction energy–momentum** of the pair and the star is the source's conjugation, defined in the 2007 paper by $F^* = \bar f - \bar F$ (the corpus's ${}^{*}$, not the coefficient conjugate of the energy display; see the notational warning above). Its scalar part $\delta W$ is the interaction energy and its vector part the interaction momentum, tied to the change of the Poynting vector. Since the total energy $W$ is real and non-negative, $\delta W > 0$ is energy released and $\delta W < 0$ is energy absorbed in the interaction, and $\delta\tilde\Pi = 0$ means the pair conserves energy–momentum exactly. This is a clean statement of "interaction = exchange of energy–momentum between fields" in a single algebraic form, and it is the programme's most transferable contribution to the corpus's conservation-law material.

**The 2009 revision moves the same construction from the strengths to the sources.** The 2007 paper forms the interaction energy–momentum from the A-fields, as above; the 2009 paper keeps the same definition and applies it to the charge–current biquaternions instead,

$$
\tilde{\Xi}_{kl} = \tfrac{1}{2}\left(\tilde{\Theta}_k\circ\tilde{\Theta}_l^* + \tilde{\Theta}_l\circ\tilde{\Theta}_k^*\right),
\qquad
\tilde{\Xi} = \sum_k\tilde{\Xi}_k + \sum_{k\ne l}\tilde{\Xi}_{kl},
$$

so that the total energy–momentum of the combined source separates into per-field pieces and pair terms. Recomputed with the paper's definitions of $\rho$ and $\mathbf{J}$ in the coefficient convention of the energy display, the pair term is

$$
\tilde{\Xi}_{kl}
= \tfrac{1}{2}\left(\rho_k\rho_l^* + \rho_l\rho_k^*\right)
- \tfrac{1}{2}\left[\left(\mathbf J_k,\mathbf J_l^*\right) + \left(\mathbf J_l,\mathbf J_k^*\right)\right]
+ \tfrac{1}{2}i\left(\rho_k\mathbf J_l^* + \rho_l\mathbf J_k^* - \rho_l^*\mathbf J_k - \rho_k^*\mathbf J_l\right)
+ \tfrac{1}{2}\left(\left[\mathbf J_k,\mathbf J_l^*\right] + \left[\mathbf J_l,\mathbf J_k^*\right]\right),
$$

and it has a simplifying property worth recording: **for a purely electric charge and current, $\rho_H = 0$ and $\mathbf{j}_H = 0$ in both fields, the vector part vanishes identically and the pair term is the central real scalar**

$$
\tilde{\Xi}_{kl} = \rho_k\rho_l - \left(\mathbf J_k,\mathbf J_l\right),
$$

the Minkowski pairing of the two charge–current four-vectors under the signature $(+,-,-,-)$ — the same bilinear pairing that the algebra's pseudonorm is built from. The interaction energy of a pair of sources is thus the pairing of the sources, with the central scalar that the algebra's own bilinear form supplies and no new object. With magnetic charge present the cancellation fails and the pair term carries a vector part; the corpus records the general form above and the central special case, which was verified exactly.

The two papers' second-law postulates differ by the sign of $\tilde{\Theta}$, and the two interaction energies differ accordingly in the sign of their cross terms while their per-field pieces agree; the corpus quotes each in its own paper's convention. The **conjugation convention must also be fixed before the two papers' pair terms are compared term by term**: recomputed with the 2007 paper's own conjugation $F^* = \bar f - \bar F$ instead of the coefficient conjugate, the same pair term has a real scalar part and a purely imaginary vector part, so the two are different objects and not sign multiples of one another. The expansion above is the coefficient-convention one, which is the convention in which this article writes the energy display.

## The Integrated Laws and the Rigid-Body Analogue

The programme's conservation laws can be written in integral form, and the second law can be integrated over a fixed volume into a law for a body.

The source's Theorem 1.1 states that a solution of the A-field equation satisfies $\partial_\tau\rho + \mathrm{div}\,\mathbf{J} = 0$ and $\partial_\tau W + \mathrm{div}\,\mathbf{P} = c^{-1}(\mathbf{j}_H\!\cdot\!\mathbf{H} - \mathbf{j}_E\!\cdot\!\mathbf{E})$. The divergence theorem and Stokes' theorem then give the integral balances over a fixed domain $D^-$ with outward unit normal $\mathbf{n}$: the enclosed charge changes only through the flux of $\mathbf{J}$ across the boundary, the enclosed energy only through the flux of the Poynting vector plus the work of the currents on their own field, and two further relations express the A-field through its boundary values and its current,

$$
\int_{D^-}\!\big(\rho(\mathbf{x},\tau)-\rho(\mathbf{x},0)\big)\,dV + \int_0^\tau\! d\tau\!\int_{\partial D^-}\!(\mathbf{n},\mathbf{J})\,dS = 0,
$$

$$
\int_{D^-}\!\big(A(\mathbf{x},\tau)-A(\mathbf{x},0)\big)\,dV + i\int_0^\tau\! d\tau\!\int_{\partial D^-}\![\mathbf{n},A]\,dS + \int_0^\tau\! d\tau\!\int_{D^-}\!\mathbf{J}\,dV = 0 .
$$

The second is the integrated form of the A-field equation: the A-field in a volume is fixed by its earlier value, by its boundary values and by the current that has flowed through the volume.

Integrating the second law over a fixed volume gives the momentum law. Write $m_{D^-}(t)$ and $q_{D^-}(t)$ for the total gravimagnetic (mass) and electric charge in $D^-$. Using the divergence theorem, and taking the two field values on the right at a fixed point of $D^-$ by the mean-value theorem,

$$
\kappa\sqrt{\epsilon}\,\partial_\tau\!\int_{D^-}\!\mathbf{j}_H\,dV
+ \kappa\!\int_{\partial D^-}\!\Big(\frac{\rho_H}{\sqrt{\mu}}\,\mathbf{n} + \sqrt{\mu}\,(\mathbf{n},\mathbf{j}_E)\Big)dS(x)
= q_{D^-}\tilde{\mathbf{E}}' + m_{D^-}\tilde{\mathbf{H}}'
+ \int_{D^-}\!\big(\mathbf{j}_E\times\mathbf{B}' - \mathbf{j}_H\times\mathbf{D}'\big)dV .
$$

When the enclosed mass density and the electric current vanish on the boundary the surface term drops, and the relation becomes the programme's **rigid-body analogue of Newton's second law**: the rate of change of the total gravimagnetic momentum of the volume equals the total charge times the acting electric field, plus the total mass times the acting gravimagnetic field, plus the volume integral of the two current–current forces. It is the closest the programme comes to an equation of motion for matter, and it is a balance of the same kind as the others — obtained from the field and the assumed interaction equation rather than from a new dynamical principle. The divergence-theorem step was checked numerically on smooth test functions.

The corpus's own conserved currents and their integral forms are in *Stress–Energy Conservation Laws and the Field Action in Biquaternionic Form*; what is recorded here is the programme's application of the same theorems to its own A-field and source.

## The Stress Pseudotensor and the Hydrodynamics Reading

The 2009 paper reads its own second law as a momentum balance of a continuum. It introduces a **stress pseudotensor** for each half of the field,

$$
\sigma^{H}_{ik} = -\,\kappa\,\frac{\rho_H}{\sqrt{\mu}}\,\delta_{ik} + \sqrt{\mu}\,\mathbf{j}^E_l\,\epsilon_{ikl},
\qquad
\sigma^{E}_{ik} = -\,\kappa\,\frac{\rho_E}{\sqrt{\epsilon}}\,\delta_{ik} - \sqrt{\epsilon}\,\mathbf{j}^H_l\,\epsilon_{ikl},
\qquad i,k,l = 1,2,3,
$$

and writes the second law in the shape the momentum equation of a continuous medium has,

$$
\frac{\partial \sigma^{H}_{ik}}{\partial x_k} + F^{H}_i = \partial_\tau \Pi^{H}_i,
\qquad
\frac{\partial \sigma^{E}_{ik}}{\partial x_k} + F^{E}_i = \partial_\tau \Pi^{E}_i,
$$

with the density of mass forces $F^H$ the four-term half of the power–force biquaternion, a further resistance term when the scalar $a$ is present, and the momentum densities $\Pi^H = \kappa\sqrt{\epsilon}\,\mathbf{j}_H$, $\Pi^E = \kappa\sqrt{\mu}\,\mathbf{j}_E$ as the second-law component form normalises them. The 2009 display prints a different coefficient on the right side, one of the discrepancies recorded in this article, and the corpus carries the second law's own normalization. Two structural features are worth recording, and they are the reason the object is called a *pseudotensor*.

The first is that it is **not symmetric**. The isotropic term is symmetric, and the antisymmetric part is entirely the current term,

$$
\tfrac{1}{2}\left(\sigma^{H}_{ik} - \sigma^{H}_{ki}\right) = \sqrt{\mu}\,\mathbf{j}^E_l\,\epsilon_{ikl},
$$

so the asymmetry is dual to a vector: the paper records only that the object is the analogue of the stress tensor of a liquid and that the traditional index symmetry $\sigma_{ik} \ne \sigma_{ki}$ fails, and the continuum-mechanics reading of the antisymmetric part is the corpus's — in a medium, an antisymmetric stress is the **torque (couple) density**, and a pseudotensor of this shape is the stress of a medium with couple stresses rather than of a simple fluid. The corpus's own electromagnetic stress–energy tensor, by contrast, is the *improved* one and is symmetric and traceless, so this object is not that tensor and cannot be obtained from it: it is a medium stress built from the charges and currents rather than from the field strengths, and the antisymmetric piece is what the improvement discards.

The second is that the trace is fixed by the charge, $\mathrm{tr}\,\sigma^H = -3\kappa\rho_H/\sqrt{\mu}$, so the isotropic term is a hydrostatic pressure proportional to the mass density — the pressure reading of a gravitational potential rather than a stress of the field.

**The coefficients are not carried.** The rewrite as a divergence is a *form*, and it does not reproduce the component form of the second law that the same paper prints a few sections earlier: recomputed term by term, the divergence form and the component form differ in the sign of the curl term and in the placement of $\kappa$, so no normalization of the two pseudotensors makes the displayed line an identity. What the corpus records is therefore the structure — a two-term medium stress, an antisymmetric piece dual to the electric current, a hydrostatic piece proportional to the mass density, and a momentum balance in continuum form — and not the coefficients, which is also the status of the force split it is built from.

## The Cauchy Problem and the Interaction as an Integral Equation

The programme's differential algebra gives it a solution theory that is shorter than the field's. Because the wave operator factorises, $\Box = D^-D^+ = D^+D^-$, the equation

$$
D^{\pm}K = G
$$

is solved by applying the conjugate bigradient to the source and convolving with the fundamental solution of the wave equation,

$$
K = D^{\mp}G * \psi,
\qquad
\Box\psi = \delta(\tau)\delta(\mathbf{x}),
$$

and with the **simple layer on the light cone** $\psi = (4\pi\|\mathbf{x}\|)^{-1}\delta(\tau - \|\mathbf{x}\|)$ the convolution vanishes at $\tau = 0$, which is what makes the Cauchy data separable. This is the programme's route to its Cauchy problem: the inverse of a *first-order* operator is another first-order operator applied to the scalar wave kernel, so no second-order Green tensor is needed for the bigradient equations themselves, and the Green tensor of *Maxwell's Equations in the Biquaternionic Formulation* enters only when the three-vector A-field is extracted from the biquaternion solution. For given charge–current and initial data the A-field is then an integral of the source over its past cone,

$$
4\pi\,\boldsymbol{\mathcal A}(\tau,\mathbf{x}) = -D^-\!\int_{\|\mathbf{y}-\mathbf{x}\|\le \tau}\frac{\tilde{\Theta}(\tau-r,\mathbf{y})}{r}\,dV(\mathbf{y}) + \tau^{-1}\!\int_{r=\tau}\!\boldsymbol{\mathcal A}_0\,dS - \tau^{-1}\!\int_{r=\tau}\!\tilde{\Theta}(0,\mathbf{y})\,dS,
\qquad r = \|\mathbf{y}-\mathbf{x}\|,
$$

which is the Kirchhoff formula of the scalar wave equation written for the biquaternion source; the layer and jump calculus behind the last two terms is that of *Distributions on Surfaces, Layers, and Jump Conditions*.

The interaction is treated the same way and becomes a **system of integral equations**. Applying the inversion to the second law gives, for the source of one field,

$$
\kappa\,\tilde{\Theta} = D^{+}\!\left\{H(\tau)\tilde{\mathcal F} * \psi\right\} + \tilde{\mathcal F}(0,\cdot) *_{x}\psi + \kappa\,D^{+}\!\left\{\tilde{\Theta}_0 *_{x}\psi\right\},
$$

with the convolution taken over the spatial variables only and $H$ the Heaviside function. The right side contains $\tilde{\Theta}$ itself, through the force $\tilde{\mathcal F} = \tilde{\Theta}\circ\tilde{\mathcal A}'$, so the equation is the integral form of the nonlinear second law and is solved by iteration; when one field dominates, the second field's equation is left out and the remaining one is linear in the weaker source, which is the form the programme's applications take. The corpus adds nothing here — the factorization $\Box = D^-D^+$, the simple-layer kernel and the Kirchhoff formula are standard, and the corpus's own Cauchy and layer material is in the article just named — but the transfer is exact, and it shows that the programme's nonlinear law is an integral equation of the second kind rather than a new evolution equation.

## The Shock Waves of the Charge–Current Field

The charge–current field has its own shock waves, distinct from the A-field shocks of *Shock Electromagnetic Waves*. The free-field system above is hyperbolic. In the source's reading its characteristic equation is read off the three-vector part, the scalar part entering as a constraint on the divergence, and is

$$
\nu_t\left(\nu_t^2 - c^2\|\boldsymbol{\nu}\|^2\right) = 0 :
$$

the two speeds $\nu_t = \pm c\|\boldsymbol{\nu}\|$ and the **simple** null root $\nu_t = 0$, so the stationary surfaces are characteristic and the characteristic cone is the same as Maxwell's. The source prints the equation as $\nu_4(\nu_4^2-\nu_1^2-\nu_2^2-\nu_3^2)=0$ in the Hamiltonian-form paper it cites; the 2016 paper's restatement carries a squared time factor, which the corpus's recomputation does not support — the determinant of the $3\times3$ symbol $\nu_t I + i[\boldsymbol{\nu}]_\times$ is exactly $\nu_t(\nu_t^2-\|\boldsymbol{\nu}\|^2)$, checked numerically, a simple root and not a double one. On a wave front $F_\tau$ with unit normal $\mathbf{m}$, the jump conditions of the system are

$$
[\rho]_{F_\tau} = \big(\mathbf{m}, [\mathbf{J}]_{F_\tau}\big),
\qquad
[\mathbf{J}]_{F_\tau} = \mathbf{m}\,[\rho]_{F_\tau} - i\,\mathbf{m}\times[\mathbf{J}]_{F_\tau} .
$$

The second condition fixed the tangential jumps; taking its inner product with $\mathbf{m}$ recovers the first, so the pair is consistent (checked numerically). The qualitative difference from the A-field is immediate. Dotting the second relation with $\mathbf{m}$ shows that the longitudinal part of the current jump equals the charge jump:

$$
\big(\mathbf{m}, [\mathbf{J}]_{F_\tau}\big) = [\rho]_{F_\tau}.
$$

Hence the **shocks of the charge–current field are generally not transverse** — they become transverse only when the charge jump vanishes, in which case the pair reduces to the transverse condition of the A-field. A-field shocks are transverse, $\Theta$-field shocks need not be; the source states the contrast explicitly and the corpus's shock article now records it.

## The General Front Condition of the Biwave Equation

The two front systems above are specializations of one statement, and it is worth recording because it is the general theorem behind both. For an arbitrary bipotential $\tilde K$ of the biwave equation $\tilde\nabla^{\pm}\tilde K = \tilde G$ — the equation the A-field and the charge–current field both satisfy — the layer calculus of *Distributions on Surfaces, Layers, and Jump Conditions* gives, for a field with a finite gap on a front $S$,

$$
\tilde\nabla^{\pm}\hat{\tilde K} = \tilde\nabla^{\pm}\tilde K + (n_{ict} + \mathbf n)\circ[\tilde K]_S\,\delta_S ,
$$

with $n_{ict}$ the normal's time component and $\mathbf n$ its spatial part, in the corpus's $ict$ normalization that the introduction records as $D^\pm$ up to $i$ and a sign. On a non-characteristic front the normal is invertible and the jump vanishes. On a **characteristic** front, $n_{ict}^2 + \|\mathbf n\|^2 = 0$, the normal is a zero divisor and $(n_{ict} + \mathbf n)\circ[\tilde K]_S = 0$ has nontrivial solutions. Writing $\mathbf m = \mathbf n/\|\mathbf n\|$ for the unit spatial normal and $[\tilde K]_S = [k]_S + [\mathbf K]_S$ for the scalar and vector parts of the jump, it is the null relation

$$
[\tilde K]_S = i\,\mathbf m\circ[\tilde K]_S ,
\qquad\text{equivalently}\qquad
[\tilde k]_S = -i\,(\mathbf m, [\mathbf K]_S),
\quad
[\mathbf K]_S = i\,\mathbf m\,[\tilde k]_S + i\,[\mathbf m, [\mathbf K]_S].
$$

These were checked on 100 random characteristic normals and their right-null spaces. Two readings follow. A **pure-vector** bipotential, of which the A-field is the case, has $[\tilde k]_S = 0$, so the scalar relation forces $(\mathbf m, [\mathbf A]_S) = 0$ and the vector relation reduces to $[\mathbf A]_S = -i\,[\mathbf A]_S\times\mathbf m$: the jump is transverse and the null relation has one complex solution, the single complex amplitude of the two transverse polarisations — the same wave-front condition *Shock Electromagnetic Waves* derives. A bipotential with a **non-vanishing scalar part**, of which the charge–current field is the case, is generally longitudinal: the scalar jump is fixed by the longitudinal vector jump, the qualitative content of the section above. The source prints the null form with the sign of its operator $\nabla^{+} = \partial_\tau + i\nabla$; that operator differs from the $ict$-normalized $\tilde\nabla$ by the central factor $-i$, and the corpus states the relation in the $ict$ normalization above, the sign verified in both articles.

## Longitudinal Fronts and Plane-Wave Spinors

The scalar field of the revision is not only the device that closes the system. In the programme it is also what makes the field's fronts and its plane waves longitudinal.

On the front of an EGM shock the jumps of the field satisfy, in the source's form,

$$
([\mathbf{E}]_{F_t},\mathbf{m}) = c\,[\alpha_2],
\qquad
([\mathbf{H}]_{F_t},\mathbf{m}) = c\,[\alpha_1],
$$

together with the two transverse relations. The normal (longitudinal) components of the electric and magnetic jumps are therefore exactly the jumps of the two real parts of the scalar field; when $[\alpha]=0$ both vanish and the fronts are transverse, which is the classical Maxwell case. The source reads this as the statement that the scalar field "describes the property of attraction–resistance of the EGM-field to the movement of external charges and currents", and the corpus keeps the name **attraction–resistance field** for it. This is the mirror of the $\tilde\Theta$-fronts: those are longitudinal when the charge jump is non-zero, and the A-field fronts are longitudinal when the scalar-field jump is non-zero.

At the level of smooth solutions the programme constructs the corresponding waves from scalar plane potentials. Take $\psi_j = f(\eta)$ with $\eta = (\mathbf{k},\mathbf{x}) - \omega\tau$ and $\|\mathbf{k}\| = \omega$, and $A = D^-\psi_j$; the four modes are

| Mode | Potential | $(\mathbf{E},\mathbf{k})$ | $(\mathbf{H},\mathbf{k})$ |
|---|---|---|---|
| Longitudinal magnetic | $f$ | $0$ | $-\|\mathbf{k}\|^2 f'/\sqrt{\mu}$ |
| Longitudinal electric | $if$ | $\|\mathbf{k}\|^2 f'/\sqrt{\epsilon}$ | $0$ |
| Tesla's wave | $f e_1$ | $-\omega k_1 f'/\sqrt{\epsilon}$ | $0$ |
| Torsion wave | $if e_1$ | $0$ | $-\omega k_1 f'/\sqrt{\mu}$ |

the first two being pure longitudinal electric and magnetic waves, and the last two the modes the source names after Etkin. Applying $D^-$ to the potential gives the field directly; the construction was checked, and the longitudinal properties of all four modes follow from it with residuals at machine precision, as do the exact components of the Tesla mode. The source attributes the physical longitudinal electromagnetic waves to Hvorostenko and to Etkin and offers the modes as their EGM explanation; the corpus records the construction and the attribution. One printed result does not reproduce: the torsion-mode components in the source disagree with the source's own construction in one sign and one omitted term, while the other three modes reproduce exactly, so a reader returning to the PDF should confirm that one line. The exact derived form is $A = f'(-k_1 - i\omega e_1 + k_3 e_2 - k_2 e_3)$.

## The Programme's Empirical Claims

The programme's conclusion offers four consequences to be tested, and the corpus records them as claims, attributed and not endorsed.

- **Solenoidal electric field from rotating mass.** Constant rotating electric currents produce solenoidal magnetic fields; by the electric–magnetic symmetry of the model, rotating masses should produce solenoidal electric fields. The author offers this as an explanation of the Earth's electric axis — the solenoidal part of the Earth's electric field arising from the rotation of its mass — and expects the same for other planets. The same paper adds that, the Earth carrying a negative electric charge, its rotation is what produces the Earth's solenoidal magnetic field; the corpus records the clause with the bullet.
- **Orbital shift from the electromass force.** The Sun's electric field is said to exert an electromass force on the planets, shifting their orbits. This is the force term $D'\times\mathbf{j}_H$ of the power–force biquaternion.
- **A comparison with cogravity.** The author compares the electromass force to the "cogravity" term that Matos and Tajmar added to the two-body Newtonian equations to account for the anomalous perihelion advance of Mercury, noting that the two forces are of the same form. The comparison is the author's; it is not a derivation of one from the other.
- **Chemical regularities.** The equations for the change of charges and currents and the energy–momentum transformation laws are said to be able to describe "some regularities of chemical reactions". No reaction, rate or selection rule is named, so this remains a programmatic sentence rather than a claim with content.

The 2019 paper states the claim in the author's own words: the model recovers the known gravitational, electric and magnetic forces, and thereby yields **new forces** which it offers as the targets for an experimental test. The two it names are the **gravielectric force** $\mathbf{D}'\times\mathbf{j}_H$ (the electromass term of the bullet above) and the **resistance–attraction force** $\mathrm{Im}(\alpha\mathbf{J})$, the term the scalar $\alpha$ field adds. The corpus records the identification and no more: neither term comes with a predicted magnitude, and the second depends on a field whose strength the model leaves free, so there is still nothing here for an experiment to falsify.

The corpus's standing objection applies with full force. A field identified with gravity must pass the equivalence-principle and torsion-balance tests that constrain any fifth force; the programme states no range and no independent coupling strength of its own — where it meets gravity it fixes the field constant as $\mu = 1/(4\pi G)$, a re-expression of Newton's constant rather than a prediction of it — so nothing is yet constrained and nothing is distinguished from the standard theory. A solenoidal electric field of the Earth, or an electromass orbital shift, would be a large effect if it existed; the absence of a quantitative prediction is the programme's principal weakness, and the 2009 revision shows that even its internal consistency was provisional.

The programme's later formulation goes further and reads the **monochromatic** solutions of its free charge–current field as elementary particles and atoms, classifying them by their density at the origin and placing them on the just-intonation musical scale as a periodic system. That construction is a separate body of material — it needs the Helmholtz factorisation of the free field rather than the interaction laws developed here — and it is recorded, developed and bounded in *Harmonic Elementary Particles and the Periodic System of Atoms*, with which this article shares only the charge–current biquaternion, the mutual complex gradients and the inertia law.

## Summary

The programme recorded here reads the A-field of the biquaternionic Maxwell equation as an electro-gravimagnetic field, under a hypothesis of its author: that magnetic charge density and gravitational mass density are the same thing. The reading gives the potential part of $\mathbf{H}$ to gravity and its solenoidal part to magnetism, and it is a hypothesis, not a consequence of the algebra. On that hypothesis the programme constructs a law structure: mutual complex gradients $D^\pm = \partial_\tau \pm i\nabla$, which are the corpus gradient in the $ict$ convention up to $i$ and a sign; field analogues of Newton's three laws, with a free field whose charges disperse, an interaction equation whose right side is the force from the other field, and a third law whose scalar part equates two power densities and is compared to Betti's reciprocity identity; a thermodynamic analogue for the current field with density $Q = \tfrac{1}{2}\|\mathbf{J}\|^2$ and flux $\mathbf{P}_J = \tfrac{1}{2}i\,\mathbf{J}\times\mathbf{J}^*$, which in the free field becomes the decay $\partial_\tau Q = -\mathcal U$ with the source's asserted $\mathcal U \geq 0$; and a law of the single field, in which the sum of interacting fields is free and their interaction energy–momentum is the pairwise sum $\tilde{\Pi}_{kl} = \tfrac{1}{2}(\tilde{\mathcal A}_k\circ\tilde{\mathcal A}_l^* + \tilde{\mathcal A}_l\circ\tilde{\mathcal A}_k^*)$ (star = the source's conjugation $F^* = \bar f - \bar F$, the corpus's ${}^{*}$; the energy display's coefficient conjugate is a second use of the same symbol, and the two conventions must not be mixed). The 2009 revision moves that construction to the sources, $\tilde{\Xi}_{kl} = \tfrac{1}{2}(\tilde{\Theta}_k\circ\tilde{\Theta}_l^* + \tilde{\Theta}_l\circ\tilde{\Theta}_k^*)$, where for a purely electric charge and current the pair term collapses to the central scalar $\rho_k\rho_l - (\mathbf J_k,\mathbf J_l)$, the Minkowski pairing of the two four-currents. The charge–current field also has shock waves, generally non-transverse, with the longitudinal current jump equal to the charge jump; and its solution theory is short — the first-order operator $D^\pm$ is inverted by $D^\mp$ followed by convolution with the simple layer on the light cone, and the interaction becomes a system of integral equations. The 2009 paper's continuum reading of the second law, with its non-symmetric stress pseudotensor whose antisymmetric part is dual to the electric current, is recorded with its structure but not with its coefficients, which do not close.

The 2017 paper completes the programme's relativistic treatment on the equation side. It proves the charges–currents interaction system invariant under the Poincaré–Lorentz group and derives the four-vector transformation of the charge–current and of the power–force biquaternion, from which the electric and gravimagnetic density and current formulae follow. The invariance is of the *equations* and is compatible with the non-invariance of the *closedness condition* recorded in the revision, since the two are statements about different objects; whether the invariance theorem is meant for the modified, open system the paper does not say, and the corpus leaves the question open. The same paper imposes the Lorentz condition on the potential rather than treating it as a gauge choice, a difference of logical role from the corpus's own Maxwell article that is recorded above and not resolved.

The corpus's relation to the programme is the same as to every external completion of the algebra: it can host the language, and it must state the cost. The identification of magnetic charge with gravitational mass is inserted, not forced. The model was revised by its author because the conservation law of a single source is not Lorentz invariant when fields interact; the revision, developed above, shows that the model's transformation law is the corpus's rotor with a half-rapidity angle, that the conservation law of an open source acquires the external power as its source term, and that the scalar field which repairs the integrability of the field equation obeys $\Box a \propto M$. In the static limit the same field gives Poisson's equation for a Newtonian potential and fixes the field constant as $\mu = 1/(4\pi G)$, so the identification carries a sign (attraction) and a coupling expressed through Newton's constant; and the free field carries, beside the transverse Maxwell waves, longitudinal plane modes whose longitudinal components are the jumps of the scalar field. The programme's physical consequences remain qualitative. Nothing here distinguishes the programme from standard physics. It is recorded because the corpus's A-field section raises the question of what the dual field strength could mean, and this is the most developed answer that has been proposed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\boldsymbol{\mathcal A} = \sqrt{\epsilon}\,\mathbf{E} + i\sqrt{\mu}\,\mathbf{H}$ | A-field (complex three-vector, dual field strength) |
| $\tilde{\mathcal A}$ | A-field as a biquaternion with vanishing scalar part |
| $\tau = ct$ | Scaled time of the programme's convention |
| $\mathbf J = \sqrt{\mu}\,\mathbf{j}_E - i\sqrt{\epsilon}\,\mathbf{j}_H$ | Combined complex current |
| $\rho = \rho_E/\sqrt{\epsilon} - i\,\rho_H/\sqrt{\mu}$ | Combined complex charge density |
| $\tilde{\Theta} = i\rho + \mathbf{J}$ | Charge–current biquaternion |
| $D^\pm = \partial_\tau \pm i\nabla$ | Mutual complex gradients |
| $\Box = D^-D^+ = D^+D^-$ | Wave operator of the programme |
| $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ | Corpus gradient ($D^+ = i\tilde{\nabla}$, $D^- = i\tilde{\nabla}^{\natural}$) |
| $\Box_{\mathrm{corpus}} = \tilde{\nabla}\tilde{\nabla}^{\natural} = -D^-D^+$ | Corpus d'Alembertian (sign-convention difference) |
| $\tilde{\mathcal F}$ | Power–force biquaternion of the programme |
| $W = \tfrac{1}{2}\|\boldsymbol{\mathcal A}\|^2$ | Energy density |
| $\mathbf{P} = \tfrac{1}{2}i\,\boldsymbol{\mathcal A}\times\boldsymbol{\mathcal A}^* = c^{-1}\mathbf{E}\times\mathbf{H}$ | Poynting vector |
| $Q = \tfrac{1}{2}\|\mathbf{J}\|^2$ | Current-field energy density |
| $\mathbf{P}_J = \tfrac{1}{2}i\,\mathbf{J}\times\mathbf{J}^*$ | Current-field flux |
| $F^* = \bar f - \bar F$ | Source's conjugation (the corpus's ${}^{*}$); the fixed elements $f_1+iF_2$ are its unitary biquaternions |
| $\mathcal U$ | Free-field decay rate of $Q$ (the source's $U$; $\partial_\tau Q = -\mathcal U$, $\mathcal U \geq 0$ asserted) |
| $\tilde{\Pi}_{kl}$ | Interaction energy–momentum of a pair of fields (from the A-fields) |
| $\tilde{\Xi}_{kl}$ | 2009 form of the same, from the charge–current biquaternions |
| $\sigma^{H}_{ik},\ \sigma^{E}_{ik}$ | Stress pseudotensors of the gravimagnetic and electric halves |
| $\psi = (4\pi\|\mathbf{x}\|)^{-1}\delta(\tau-\|\mathbf{x}\|)$ | Simple layer on the light cone, fundamental solution of $\Box$ |
| $M, \mathbf{F}$ | Power density and force density (scalar and vector parts of $\tilde{\mathcal F}$) |
| $U = \cosh\theta + i\sinh\theta\,\hat{\mathbf u}$ | Boost biquaternion of the revision, $\theta$ the half-rapidity |
| $\gamma = 1/\sqrt{1-v^2}$ | Lorentz factor, $\cosh 2\theta = \gamma$, $\sinh 2\theta = \gamma v$ |
| $\tilde{\Theta}' = L\tilde{\Theta}L^{*}$, $\tilde{\mathcal F}' = L\tilde{\mathcal F}L^{*}$ | 2017 transformation of the charge–current and the power–force (four-vectors) |
| $\rho' = \gamma(\rho + v(\hat{\mathbf u},\mathbf J))$, $\mathbf J' = \mathbf J_{\perp} + \gamma(\mathbf J_{\parallel} + v\rho\hat{\mathbf u})$ | 2017 charge–current transformation ($\rho^2-\|\mathbf J\|^2$ preserved) |
| $\kappa$ | Single dimensional coupling constant of the interaction equation |
| $\rho_E, \rho_H$ | Electric and magnetic charge densities ($\rho_H \leftrightarrow$ mass density in the hypothesis) |
| $a(\tau,\mathbf{x})$ | Scalar resistance field of the 2009 revision (open system) |
| $\alpha = \alpha_1 + i\alpha_2 = i\,a_1/\epsilon + a_2/\mu$ | Attraction–resistance scalar field of the EGM strength (source's real weights $a_1, a_2$) |
| $G$ | Newton's gravitational constant (the source writes $\gamma$; $\mu = 1/(4\pi G)$ in the static limit) |
| $m_{D^-},\ q_{D^-}$ | Enclosed gravimagnetic mass and electric charge of a fixed volume |

## Further Reading

- L. A. Alexeyeva, "One Biquaternion Model of the Electro-Gravimagnetic Field. Field Analogues of Newton's Laws", arXiv:math-ph/0703034v1 (2007), the Russian original recorded here; it is Russian only and has no English arXiv version.
- L. A. Alexeyeva, "Biquaternions algebra and its applications by solving of some theoretical physics equations", *Clifford Analysis, Clifford Algebras and Their Applications* **7**(1) (2012) 19–39 (arXiv:1302.0523), for the differential algebra behind the programme: the bigradients, the generalized solutions of the biwave equation, and the general front condition of the biwave equation recorded in *The General Front Condition of the Biwave Equation*.
- L. A. Alexeyeva, "Differential algebra of biquaternions. 4. Twistors and twistor fields", *Mathematical Journal* **13** (2013) (arXiv:1406.5347 [math-ph]), for the reading of the homogeneous biwave equation with a vector structural coefficient as the transformation equation of mass-charges and electro-gravimagnetic currents in an external field of strength $\mathbf{F}$, recorded above, and for the elementary twistors with their generating scalar potentials. The twistors are catalogued in *Twistor Theory and Biquaternions*; the stationary kernel is in *The Yang–Mills Equation in Biquaternionic Form*.
- L. A. Alexeyeva, "Newton's Laws for a Biquaternionic Model of the Electro-Gravimagnetic Field, Charges, Currents, and Their Interactions" (2009), for the finding that the charge–current conservation law is not Lorentz invariant under interaction, the scalar resistance field that repairs it, the source-level interaction energy, the stress pseudotensor and the Cauchy problem. The Russian journal version is *Hypercomplex Numbers in Geometry and Physics* **6**(1) (2009) 122–134; the English version is *Journal of Physical Mathematics* (2009), DOI 10.4303/jpm/S090604, reprinted as arXiv:1104.1483v1; the Russian-language preprint of the same work is arXiv:0904.3446v1. It is the English text that the corpus used, both Russian text layers being degraded.
- L. A. Alexeyeva, "Hamiltonian Form of the Maxwell Equations and Its Generalized Solutions", *Differential Equations* **39**(6) (2003) 807–816 (arXiv:0705.3153 is the Russian original), for the A-field, its Green tensor and the shock-inclusive Cauchy theory.
- L. A. Alexeyeva, "Relativistic Formulae for the Biquaternionic Model of Electro-Gravimagnetic Charges and Currents", *Journal of Modern Physics* **8** (2017) 1043–1052, for the Poincaré–Lorentz invariance of the charges–currents interaction equations, the transformation of the mutual bigradients (Lemma 5.1), and the four-vector transformation formulae for charge, current, active power and force; read together with the 2009 negative result, which it does not itself mention.
- L. A. Alexeyeva, "Biquaternionic Model of Electro-Gravimagnetic Field, Charges and Currents. Law of Inertia", *Journal of Modern Physics* **7** (2016) 435–444 (arXiv:1607.01268), for the static Newtonian limit, the attraction–resistance field, the longitudinal plane spinors and the spinor solutions of the free source.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions", *Mathematical Journal* **16**(2) (2016) 90–103, for the same programme’s derivation of the $\alpha$-coupled system, the longitudinal plane-wave spinors and the objection to the classical Maxwell system (recorded in *Maxwell’s Equations in the Biquaternionic Formulation*).
- L. A. Alexeyeva, "Biquaternionic Model of Electro-Gravimagnetic Fields and Interactions", *Advances in Theoretical & Computational Physics* **2**(4) (2019) 1–5 (ISSN 2639-0108), for the equations-of-motion framing of the interaction and the five-term force list that names the gravielectric and the resistance–attraction forces.
- L. A. Alexeyeva, "Biquaternionic representation of harmonic elementary particles. Periodic system of atoms", *SSRG International Journal of Applied Physics* **6**(3) (2019) 73–80, doi:10.14445/23500301/IJAP-V6I3P112, for the programme's particle and atom reading — the monochromatic standing solutions, the pulsars and spinors, the "elementary hydrogen atom" and the musical periodic system. That reading is developed and bounded in *Harmonic Elementary Particles and the Periodic System of Atoms*, where the monochromatic sector's algebra is verified and the particle, atom and mass identifications are separated from it.
- L. A. Alexeyeva, "Ether and photons in biquaternionic presentation", *SSRG International Journal of Applied Physics* **7**(1) (2020) 96–101, doi:10.14445/23500301/IJAP-V7I1P114, for the programme's reading of the field itself — the ether naming and the field-primary reading of the postulate, the monochromatic photon equation on the A-field, the elementary photon, the free plane modes with their longitudinal and tensional content, light as a spectral cloud, and the claim that no pure gravitational waves exist. That reading is developed and assessed in *The Ether and Photons in the Electro-Gravimagnetic Programme*.
- C. J. de Matos and M. Tajmar, "Advance of Mercury Perihelion Explained by Cogravity" (2003), for the cogravity term to which the programme compares its electromass force.
- N. P. Hvorostenko, "Longitudinal electromagnetic waves", *News of Higher Education Institutions. Physics* (1992) no. 3, 24–29, and V. A. Etkin, "Longitudinal electromagnetic waves as a corollary of Maxwell's equations" (2007), for the observed longitudinal electromagnetic waves that the programme's plane modes are offered to explain.
- *Maxwell's Equations in the Biquaternionic Formulation*, for the A-field, its Green tensor and the corpus's sign convention.
- *The Magnetic Monopole in Biquaternionic Form*, for magnetic charge as the symmetric source completion and the Dirac quantisation condition.
- *The Lorentz Force in Biquaternion Form*, for the power–force density biquaternion and the four-term force split.
- *Shock Electromagnetic Waves*, for the A-field jump conditions and the charge–current shock conditions recorded there.
