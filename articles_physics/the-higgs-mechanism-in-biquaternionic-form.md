# __The Higgs Mechanism in Biquaternionic Form__

## Introduction

The **Higgs mechanism** is the statement that a gauge symmetry which is exact in the action can be hidden by the vacuum, and that the hiding is not free. A gauge-field mass term, $m^2A_\mu A^\mu$, is forbidden: it is not invariant under the transformation law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ that the companion articles derive for the connection. The mass is generated instead from the one place the symmetry permits — the **kinetic term of the scalar field**, evaluated at a vacuum expectation value that does not respect the symmetry. The gauge field acquires a mass whose square is the coefficient of the quadratic term that the kinetic term thereby produces, and the would-be Goldstone mode of the scalar, which the vacuum makes massless, is absorbed into the gauge field as its longitudinal polarization. Both facts follow from the same coupling. Neither is a term written into the action by hand, and avoiding that is the whole content of the mechanism.

This article works the mechanism inside the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in the notation of the companion articles. The pieces are already in the read list. *The Gauge Principle in Biquaternionic Form* localizes the central phase of the algebra and produces the connection $\tilde{A}$, the covariant derivative $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$, and the transformation law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$; it also identifies the **complex scalar** $\tilde{\Phi} = \varphi\,e_0$ as the realization of the symmetry that survives a mass term. *The Covariant Derivative and Gauge Connection in Biquaternionic Form* studies $D$ as an operator and records the covariant square. *Non-Abelian Gauge Fields in Biquaternionic Form* exhibits the compact algebra $\mathfrak{su}(2)$ inside the material sector and reports the reality condition on the connection as a gap. *Chiral Fermions in the Biquaternion Framework* derives the selection rule that a bare fermion mass requires equal left and right charges, and names the present article as the companion in which the compensating scalar is to be treated.

The essential step is short enough to state before it is computed. At a non-zero vacuum expectation value $\langle\tilde{\Phi}\rangle = \langle\varphi\rangle e_0$ that is **constant**, the ordinary derivative annihilates the vacuum and the covariant derivative does not:

$$
D_\mu\tilde{\Phi}\Big|_{\langle\tilde{\Phi}\rangle} \;=\; \frac{iq}{\hbar}\,A_\mu\,\langle\tilde{\Phi}\rangle .
$$

The covariant derivative is *linear in the gauge field* when evaluated at the vacuum. The scalar kinetic term is quadratic in $D_\mu\tilde{\Phi}$, so at the vacuum it becomes **quadratic in the gauge field** — a mass term for $\tilde{A}$ — with a coefficient proportional to $|\langle\varphi\rangle|^2$. The vacuum value that makes this happen is the one that minimizes the potential, and it is not gauge invariant; that is why the mass term, which the symmetry forbids as an explicit term, is allowed to appear from the kinetic term. The rest of the article makes each step explicit and checks it.

The division between what is established and what is interpretation is kept explicit, as in the companion articles.

- **Established, and recomputed below.** The framework's scalar is the complex central field $\tilde{\Phi} = \varphi\,e_0$; the potential $V(\varphi^*\varphi)$ has a circle of minima at $|\varphi| = v/\sqrt{2}$, which the central $U(1)$ moves and therefore does not leave invariant; the covariant derivative at the vacuum is $\frac{iq}{\hbar}A_\mu\langle\tilde{\Phi}\rangle$; the scalar kinetic term therefore produces the gauge-field quadratic form $-\frac{q^2v^2}{2\hbar^2}\,\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$, which is a Proca mass term with mass-squared $M_A^2 = q^2v^2/\hbar^2$; the kinetic term is gauge invariant while a put-in mass term is not; and the degree-of-freedom count balances, $2+2 = 1+3$.
- **Interpretation.** Reading the phase of $\varphi$ as a would-be Goldstone mode, the set of minima as a circle of degenerate vacua, and the removal of the phase as the unitary gauge is the standard reading of the algebra. It is labelled as interpretation where it occurs.
- **Gap, left visible.** The framework supplies its scalar in the **center** $\mathbb{C}_{\mathbb{B}}$, where it is a singlet of the non-abelian factor $\mathfrak{su}(2)$ of the material sector; a central scalar cannot break $SU(2)$. The framework does not supply a scalar in a non-trivial representation, an electroweak doublet, or the hypercharge assignments of the Standard Model, and the reality condition on a non-abelian connection is itself open. The non-abelian and electroweak Higgs mechanism is therefore **not constructed here**, and no quantum numbers are invented to bridge the gap.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, which is the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The connection is $\tilde{A} = \sum_{\mu=0}^{3}A_\mu e_\mu = i\phi/c\,e_0 + \mathbf{A} \in \mathbb{M}_-$, with $A_0 = i\phi/c$ purely imaginary and $A_1, A_2, A_3$ real; it transforms as $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ under a real gauge function $\Gamma$; and the coupling is written $\kappa = q/\hbar$, so that $D = \tilde{\nabla} + i\kappa\tilde{A}$ and $D_\mu = \partial_\mu + i\kappa A_\mu$. The scalar of this article is the **complex central field** $\tilde{\Phi} = \varphi\,e_0$, with $\varphi$ a complex scalar function; the amplitude symbol $\varphi$ is used to keep it distinct from the connection's scalar potential $\phi$. The scalar part is $\mathrm{Sc}$, the matrix trace is $\mathrm{Tr} = 2\,\mathrm{Sc}$, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ its vacuum value. The $ict$ coordinates are $x_\mu = (ict, x, y, z)$, so $\partial_0 = \partial_{ict} = -i\partial_t/c$, and the Lorentz-invariant contraction of two four-vectors is $g^{\mu\nu}U_\mu^*V_\nu$ with $g = \mathrm{diag}(-1, +1, +1, +1)$ on these coordinates — the same convention in which the Maxwell density is $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$.

## The Scalar, the Phase, and the Covariant Derivative

The scalar of the framework is the complex central field

$$
\tilde{\Phi}(\tilde{X}) = \varphi(\tilde{X})\,e_0 \;\in\; \mathbb{C}_{\mathbb{B}}, \qquad \varphi \in \mathbb{C},
$$

which the gauge principle article identifies as the realization of the global symmetry that survives a mass: under the constant phase $\varphi\mapsto e^{i\alpha}\varphi$ the massive Klein–Gordon equation is invariant, because its mass term is linear in the field. This is the scalar the Higgs mechanism uses. It is **complex**, and we say so explicitly: a real scalar would be neutral under the central phase and could not break a $U(1)$ at all. The framework does supply a complex scalar, so no real-scalar assumption is forced here; the real case is mentioned only where it differs.

**The symmetry.** The global symmetry is the unitary part of the center, $\varphi\mapsto\lambda\varphi$ with $\lambda = e^{i\alpha}$ central. Localizing it means $\lambda(\tilde{X}) = e^{iq\Gamma(\tilde{X})/\hbar}$ with $\Gamma$ a real scalar function, and it forces the connection,

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma, \qquad
D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu, \qquad
D_\mu\tilde{\Phi} = \partial_\mu\tilde{\Phi} + \frac{iq}{\hbar}A_\mu\tilde{\Phi}.
$$

The covariant derivative is inherited unchanged from the read list; nothing about it is rederived here.

**Why the abelian case is the clean one.** Because the connection coefficients $A_\mu$ are complex scalars, they are central, and left and right multiplication by them agree. Acting on the scalar $\tilde{\Phi} = \varphi\,e_0$, the connection term stays proportional to $e_0$:

$$
D_\mu\tilde{\Phi} = \left(\partial_\mu\varphi + \frac{iq}{\hbar}A_\mu\varphi\right)e_0 = (D_\mu\varphi)\,e_0 .
$$

The covariant derivative of the scalar is again a **scalar** — it does not acquire vector components along $e_1, e_2, e_3$. This is exactly the property that fails in the non-abelian case, where the connection does not commute with the field and $D_\mu\tilde{\Phi}$ acquires components in directions the field did not have. It is the reason the abelian mechanism below closes, and the reason the non-abelian one is a gap (see its own section).

**The scalar Lagrangian.** The gauge-invariant density of the scalar is the kinetic term plus a potential,

$$
\mathcal{L}_\text{scalar} = -\,g^{\mu\nu}\,(D_\mu\varphi)^*(D_\nu\varphi) \;-\; V\!\left(\varphi^*\varphi\right),
$$

where the potential is a function of the single invariant $\varphi^*\varphi = \mathrm{Sc}[\tilde{\Phi}^\dagger\tilde{\Phi}]$. The kinetic term is the Lorentz-invariant contraction, in the $ict$ metric of the Conventions, of the covariant derivative with its conjugate; it is manifestly real and, as the next section uses, gauge invariant. The standard normalization is fixed by the coefficient $-1$ on the kinetic term and by the definition of $v$ in the potential.

## The Potential and the Non-Zero Vacuum

Take the potential of the standard broken phase,

$$
V(\varphi^*\varphi) = \beta\left(\varphi^*\varphi - \frac{v^2}{2}\right)^2, \qquad \beta > 0,
$$

whose minimum is the circle

$$
|\varphi| = \frac{v}{\sqrt{2}}, \qquad v > 0 .
$$

Two features of this minimum are the whole content of "spontaneous" symmetry breaking.

**1. The vacuum is not unique.** Every point of the circle $|\varphi| = v/\sqrt{2}$ minimizes $V$. The action is invariant under the central phase $\varphi\mapsto e^{i\alpha}\varphi$, but no single minimum is: the phase rotates the vacuum into a different, equally good vacuum. A symmetry that is a symmetry of the action but not of the chosen vacuum is said to be **spontaneously broken**. This is a statement about the pair (action, vacuum), not about the action alone.

**2. The vacuum is a scalar with a constant magnitude.** Write

$$
\varphi(\tilde{X}) = \frac{1}{\sqrt{2}}\bigl(v + h(\tilde{X})\bigr)\,e^{\,i\theta(\tilde{X})/v},
$$

with $h$ and $\theta$ real. Here $h$ is the **radial** fluctuation away from the minimum and $\theta$ is the **angular** fluctuation along it. The potential depends on $|\varphi| = \frac{1}{\sqrt{2}}|v+h|$ alone, so it is independent of $\theta$: expanding, $V = \beta v^2h^2 + O(h^3)$, giving the radial mode the mass

$$
m_h^2 = 2\beta v^2 .
$$

The angular field $\theta$ has **no potential at all**. It is the massless mode that the vacuum's degeneracy makes inevitable — the **would-be Goldstone boson**. Its value is a coordinate on the circle of minima, and a change of $\theta$ is a gauge transformation, which is why it cannot carry a physical mass of its own. The next two sections show that it does not disappear; it is absorbed.

The two real fields $h$ and $\theta$ are the two real degrees of freedom of the complex scalar $\varphi$. Before any gauge field is considered, the scalar alone contributes $2$ real degrees of freedom, and the vacuum leaves one massive ($h$) and one massless ($\theta$).

## The Mass from the Scalar Kinetic Term

We now evaluate the kinetic term of the scalar at the vacuum. This is the step at which the gauge boson mass is produced, and it is worth doing slowly, because the temptation is to write the mass term down and quote the answer.

**No mass term may be written by hand.** Under the gauge transformation $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$, the combination

$$
A_\mu A^\mu \;\longmapsto\; \left(A_\mu - \partial_\mu\Gamma\right)\left(A^\mu - \partial^\mu\Gamma\right) \;\neq\; A_\mu A^\mu
$$

in general, so a term $m^2A_\mu A^\mu$ in the action is not gauge invariant. It is exactly the term the symmetry forbids. The mechanism must therefore generate it from something that *is* invariant, and the invariant object available is the kinetic term of the scalar.

**The vacuum value of the covariant derivative.** At the constant vacuum $\varphi = v/\sqrt{2}$, the ordinary derivative vanishes and only the connection term survives:

$$
D_\mu\varphi\Big|_{\text{vac}} = \partial_\mu\frac{v}{\sqrt{2}} + \frac{iq}{\hbar}A_\mu\frac{v}{\sqrt{2}} = \frac{iq}{\hbar}\,A_\mu\,\frac{v}{\sqrt{2}},
\qquad
D_\mu\tilde{\Phi}\Big|_{\text{vac}} = \frac{iq}{\hbar}A_\mu\,\langle\tilde{\Phi}\rangle .
$$

This is the key equation. The covariant derivative of the scalar is **proportional to the gauge field** once the scalar is frozen at its vacuum value.

**The kinetic term becomes a mass term.** Inserting this into the gauge-invariant kinetic density gives

$$
-\,g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)\Big|_{\text{vac}}
= -\,g^{\mu\nu}\left(\frac{iq}{\hbar}A_\mu\frac{v}{\sqrt{2}}\right)^{\!*}\left(\frac{iq}{\hbar}A_\nu\frac{v}{\sqrt{2}}\right)
= -\,\frac{q^2v^2}{2\hbar^2}\,g^{\mu\nu}A_\mu^*A_\nu .
$$

Written with the corpus's norm form, using $g^{\mu\nu}A_\mu^*A_\nu = \mathrm{Sc}(\bar{\tilde{A}}\tilde{A}) = \sum_{\mu}A_\mu^2$ for the connection $\tilde{A}\in\mathbb{M}_-$ (whose $A_0$ is imaginary, so $A_0^2 = -|A_0|^2$),

$$
-\,g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)\Big|_{\text{vac}}
= -\,\frac{q^2v^2}{2\hbar^2}\,\mathrm{Sc}\!\left(\bar{\tilde{A}}\tilde{A}\right).
$$

This is a quadratic form in the connection — a **Proca mass term**. Comparing with the standard normalization $-\tfrac12 M_A^2\,\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ for a massive vector field, the mass-squared is

$$
\boxed{\;M_A^2 = \frac{q^2v^2}{\hbar^2}\;},
\qquad\text{i.e.}\qquad
M_A = \frac{qv}{\hbar} \quad (\hbar = 1:\ M_A = qv).
$$

This is the standard abelian-Higgs result. It reproduces the textbook value: with $\langle|\varphi|\rangle = v/\sqrt{2}$ the conventional complex scalar, $|D_\mu\varphi|^2$ at the minimum gives $\frac{1}{2}q^2v^2A_\mu A^\mu$, so the pole mass is $M_A = qv$ (in units $\hbar = 1$), exactly as for the Higgs mechanism of scalar electrodynamics. The larger $\hbar$ is, the smaller the mass, as the factor $q/\hbar$ requires.

**What produced the mass, and what did not.** Three things about the derivation are worth stating, because each is a trap avoided.

- **The mass came from the kinetic term.** The potential $V$ was used only to supply the vacuum value $v$; its curvature at the minimum gives the *scalar* mass $m_h^2 = 2\beta v^2$, not the gauge mass. The gauge mass $M_A$ does not involve $\beta$ at all, and would be unchanged if the potential were flatter or steeper while keeping the same $v$. That is the signature that the gauge mass is generated by the kinetic term.
- **No gauge mass term was written by hand.** The derivation began from $-g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)$, which is gauge invariant, and produced $\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ only after substituting a vacuum that is *not* gauge invariant. The non-invariance of the result is inherited from the non-invariance of the vacuum, not inserted.
- **The kinetic term itself remains gauge invariant.** Under $\varphi\mapsto\lambda\varphi$ and $\tilde{A}'\mapsto\tilde{A}-\tilde{\nabla}\Gamma$, $D_\mu\varphi\mapsto\lambda D_\mu\varphi$, so $(D_\mu\varphi)^*(D_\mu\varphi)\mapsto|\lambda|^2(D_\mu\varphi)^*(D_\mu\varphi) = (D_\mu\varphi)^*(D_\mu\varphi)$ because $|\lambda| = 1$.

**Verification.** The algebra above was recomputed independently. Writing the connection as $A_0 = i a_0$ with $a_0$ real and $A_k = a_k$ real, the exact symbolic evaluation of the kinetic density at the vacuum returns

$$
-\,g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)\Big|_{\text{vac}}
= \frac{q^2v^2}{2\hbar^2}\left(a_0^2 - a_1^2 - a_2^2 - a_3^2\right)
= -\,\frac{q^2v^2}{2\hbar^2}\,\mathrm{Sc}\!\left(\bar{\tilde{A}}\tilde{A}\right),
$$

the middle expression being the $ict$ form of the norm form and the last the corpus's packaging. The standard cross-check $\langle|\varphi|\rangle = v/\sqrt{2}$ is what fixes the factor $1/2$ and gives the textbook $M_A^2 = q^2v^2/\hbar^2$. Because a coefficient can be checked on the case that suggested it — here, the single component $A_0$ — the coefficient was *also* checked on a **generic**, non-axis-aligned connection direction and on a **second, independent** parameter set $(q', v')$: in both cases the induced quadratic form divided by $\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ equals $-q^2v^2/2\hbar^2$ to a relative error below $10^{-15}$. The gauge invariance of the kinetic density was checked with a non-constant gauge function on a generic connection, with residuals at the level of the floating-point round-off ($\sim 10^{-17}$), while the put-in mass term $A_1^2$ was found to change by a nonzero amount well above round-off under the same transformation, confirming that it is the symmetry that forbids it.

## The Would-Be Goldstone Mode and the Count

The mass term above was obtained in the gauge in which $\varphi$ is real and constant — the tree-level vacuum. In a generic gauge the scalar still has its angular mode $\theta$, and it is worth seeing where it goes. The answer is the second half of the mechanism.

**The phase is a gauge direction.** The parametrization $\varphi = \frac{1}{\sqrt{2}}(v+h)e^{i\theta/v}$ exhibits the phase as a field. But a phase rotation is precisely a gauge transformation: choosing

$$
\Gamma(\tilde{X}) = -\,\frac{\hbar}{qv}\,\theta(\tilde{X})
$$

gives $\varphi\mapsto e^{iq\Gamma/\hbar}\varphi = e^{-i\theta/v}\varphi = \frac{1}{\sqrt{2}}(v+h)$, which is real — the angular field is removed. This choice is the **unitary gauge** for this abelian model. In it the scalar is a single real field $h$, and the potential gives it the mass $m_h^2 = 2\beta v^2$.

**Where the phase went.** The gauge transformation that removes $\theta$ also shifts the connection,

$$
A_\mu' = A_\mu - \partial_\mu\Gamma = A_\mu + \frac{\hbar}{qv}\,\partial_\mu\theta ,
$$

so the combination $A_\mu + \frac{\hbar}{qv}\partial_\mu\theta$ is gauge invariant and the mass term depends on it, not on $A_\mu$ alone. The two terms are not separately physical: what the gauge field gained as a mass is exactly the longitudinal component it did not have as a massless field, and $\partial_\mu\theta$ is that component. The would-be Goldstone boson is **absorbed** by the gauge field, which is why it does not appear in the physical spectrum, and why the counting below balances.

**The degree-of-freedom count.** Count the real, physical, on-shell degrees of freedom before and after the breaking, in four dimensions.

*Before (symmetric phase, $\langle\tilde{\Phi}\rangle = 0$):*

- The complex scalar $\varphi$ has $2$ real components, both massless.
- The gauge field $A_\mu$ is massless. A massless vector in four dimensions has $4$ field components, and gauge invariance removes $2$ of them, leaving $2$ transverse polarizations.
- Total: $2 + 2 = 4$.

*After (broken phase, $\langle|\varphi|\rangle = v/\sqrt{2}$):*

- The scalar has $1$ real physical component, the radial mode $h$, which is massive.
- The phase mode $\theta$ is not an independent physical field; it is the longitudinal polarization of the gauge field.
- The gauge field is massive. A massive vector has no residual gauge symmetry, so its $4$ components are all physical up to the equation of motion, giving $3$ polarizations: $2$ transverse and $1$ longitudinal.
- Total: $1 + 3 = 4$.

The count balances, $4 = 4$, and it balances *only because* the gauge field gained one polarization and the scalar lost one mode. This is the degree-of-freedom bookkeeping of the Goldstone theorem: the number of would-be Goldstone bosons equals the number of broken generators, here $1$ (the single generator of the broken $U(1)$), and each is absorbed by a gauge field that becomes massive and acquires the longitudinal polarization.

**The count is not automatic.** It is a check on the whole construction, not a restatement of it. The equality $2+2 = 1+3$ holds because exactly one scalar mode ceased to be an independent physical field and exactly one gauge polarization was gained; the two events are the same event. If the potential had left the $U(1)$ unbroken ($v = 0$), the scalar would keep $2$ real massless components and the gauge field its $2$ transverse polarizations, again $4$ — but with no absorption and a different distribution. What the count confirms is that the broken phase has neither lost nor gained a degree of freedom: the Goldstone mode was moved, not created, and it moved into the gauge field. Balances of this kind are the standard guard against a mechanism that has quietly dropped a mode, and this one balances.

**A note on the Higgs mass.** The radial mode's mass $m_h^2 = 2\beta v^2$ is a second prediction of the same potential, independent of $M_A$. Both follow from the single configuration $V = \beta(\varphi^*\varphi - v^2/2)^2$: the gauge mass from the shape of the kinetic term at the vacuum, the scalar mass from the curvature of the potential. The framework reproduces the standard relation between them through $\beta$, which it does not fix.

## What the Framework Does Not Supply: The Non-Abelian and Electroweak Case

The mechanism above is the abelian one. The physically realized Higgs mechanism of the Standard Model is non-abelian: it breaks $SU(2)_L\times U(1)_Y$ to $U(1)_{\mathrm{em}}$, giving mass to the $W^\pm$ and $Z$ and leaving the photon massless. This section states, without smoothing it over, why the biquaternion framework as developed in the read list does not yet supply that structure. It is a gap, and leaving it labelled is the honest position.

**The framework has a non-abelian algebra but not a settled non-abelian connection.** *Non-Abelian Gauge Fields in Biquaternionic Form* shows that the vector part of the material sector, $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$, is $\mathfrak{su}(2)$ under the commutator, and that the material sector decomposes as $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$ — an abelian factor and a compact simple factor. But the reality condition on the *connection* is obstructed in the time direction by the $ict$ derivative, and the representation carried by the matter field is not fixed. Until those are settled, a non-abelian covariant derivative on the scalar is not available to evaluate.

**The framework's scalar is a singlet of the non-abelian factor.** This is the sharpest obstacle. The scalar the framework supplies, $\tilde{\Phi} = \varphi\,e_0$, lies in the center; it commutes with every element, and in particular it is annihilated by the $SU(2)$ action (left multiplication by a unit real quaternion $U$ acts on $\varphi e_0$ as $U\varphi e_0 = \varphi U$; a scalar is by definition the singlet). A field that is invariant under a group **cannot break it** — the vacuum $\langle\varphi\rangle e_0$ is invariant under $SU(2)$, so it is not a vacuum of broken $SU(2)$, and no $SU(2)$ gauge boson acquires a mass from it. To break the non-abelian factor one needs a scalar that transforms non-trivially — in the adjoint $\tilde{\Phi}\mapsto U\tilde{\Phi}U^{-1}$, or in a module of $\mathbb{B}$ — and the framework does not supply a canonical one. This is not a technicality to be papered over; it is the statement that the scalar that gives mass must carry the same symmetry the gauge fields carry, and the central scalar does not.

**There is no electroweak doublet and no hypercharge assignment.** The Standard Model scalar is an $SU(2)_L$ doublet with hypercharge $Y = 1/2$, whose components are arranged so that one neutral component can acquire a vacuum expectation value while leaving the electromagnetic $U(1)$ unbroken. Nothing in the read-list construction produces a doublet, a hypercharge operator, or the $SU(2)_L\times U(1)_Y$ group with its quantum numbers. The biquaternion algebra is $\mathbb{B}\cong M_2(\mathbb{C})$, which has a natural two-dimensional module $S$, so a doublet-shaped object is available algebraically; but the assignment of hypercharge, the relative $U(1)$ inside the electroweak group, and the coupling of the doublet to the $W$ and $B$ fields are not determined by the algebra. **Writing those assignments down here would be inventing them**, and the assignment is exactly what the electroweak sector is made of. They are therefore not written.

**The fermion masses are likewise not constructed.** *Chiral Fermions in the Biquaternion Framework* proves the selection rule that a bare Dirac mass is gauge invariant only when the left and right charges are equal, so a chiral fermion has no bare mass and must obtain one from a compensating scalar through a Yukawa coupling. That article names the present one as the place where the compensating scalar is to be treated. What can be said here is the negative: the framework's own mass term is the linear chirality coupling, a Dirac mass that the selection rule admits only when $q_L = q_R$ and that therefore cannot supply a chiral fermion's mass; the framework's abelian gauge group is central and so does not distinguish the two chiral halves; and no Yukawa coupling of the framework's scalar to those halves is constructed.

Whether the framework's scalar can play the role of the Standard Model Higgs in giving fermion masses is therefore open, and is not settled by the mechanism above.

What the abelian construction *does* establish is the **structure** the non-abelian one must reproduce: a scalar whose vacuum is not invariant under the gauge group, a kinetic term that turns the vacuum value of the covariant derivative into a quadratic form in the connection, a mass-squared equal to the coefficient of that form, and a degree-of-freedom count that balances by absorbing the Goldstone modes. The electroweak sector is the same mechanism with a scalar in the right representation; finding that representation inside $\mathbb{B}$ is the open problem, not the mechanism.

## Open Questions

1. **Which representation of $SU(2)$ can the scalar occupy?** The framework's canonical scalar is central and therefore an $SU(2)$ singlet, which cannot break $SU(2)$. Is there a biquaternion-valued scalar field in a non-trivial representation — the adjoint $\tilde{\Phi}\mapsto U\tilde{\Phi}U^{-1}$, or a field valued in the spinor module $S$ — that the algebra naturally supplies, and does it have a potential that can be minimized off the symmetric point? This is the prerequisite for a non-abelian Higgs mechanism.

2. **The electroweak quantum numbers.** No hypercharge assignment, doublet structure, or $SU(2)_L\times U(1)_Y$ action is derived in this series. Is there a biquaternionic origin for them — for instance a decomposition of the traceless subspace of $\mathbb{B}$ that separates the neutral and charged directions — or must they be imposed from outside? The present article deliberately does not invent them.

3. **The reality condition on the connection.** The non-abelian article leaves open the Hermitian-conjugation class of the non-abelian connection under the $ict$ derivative. Its resolution is a prerequisite for the non-abelian covariant derivative, and hence for the non-abelian kinetic term, and hence for the non-abelian mass.

4. **The scalar kinetic term in the framework's own normalization.** The scalar Lagrangian used here takes the Lorentz-invariant contraction of $D_\mu\varphi$ with its conjugate. The corpus's Noether article writes the free scalar kinetic term as the norm form $-\sum_\mu(\partial_\mu\varphi^*)(\partial_\mu\varphi)$, contracting the two factors without a relative metric sign. Because the $ict$ time derivative is imaginary, $(\partial_{ict}\varphi)^*=-\partial_{ict}\varphi^*$, so this metric-free contraction already carries the Lorentzian sign and equals the Lorentz-invariant combination $-g^{\mu\nu}(\partial_\mu\varphi)^*(\partial_\nu\varphi)$: for the free scalar the two normalisations coincide, for a complex scalar as much as for a real one, and the metric-free form is not the Euclidean modulus. The two part company only once the derivative is gauged, where the all-plus contraction is Euclidean and the metric contraction is the one that yields a Proca mass. Which normalization the framework intends for the charged scalar — and whether the difference has content — is not settled here and is recorded in the companion.

5. **The Yukawa coupling.** How does the framework's scalar couple to the chiral spinor halves so as to generate fermion mass after breaking? The chiral-fermions article poses the question and this article does not answer it.

6. **The number of broken generators.** In a general non-abelian model the Goldstone count is $\dim(G/H)$, and the balance of degrees of freedom is the same argument run with more gauge fields. Does the biquaternion framework constrain $G$ and $H$, and hence the count?

7. **Empirical contact.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from the standard Higgs mechanism. The abelian construction above is a reformulation of scalar electrodynamics; the question of empirical contact is untouched by it.

## Summary

The Higgs mechanism in biquaternionic form, in the abelian sector the framework supplies, is the following chain. The scalar is the complex central field $\tilde{\Phi} = \varphi\,e_0$; the potential $V = \beta(\varphi^*\varphi - v^2/2)^2$ has a circle of minima at $|\varphi| = v/\sqrt{2}$ that the central $U(1)$ rotates but no single point of which it preserves, so the vacuum breaks the symmetry spontaneously. At that vacuum the covariant derivative is proportional to the connection,

$$
D_\mu\tilde{\Phi}\Big|_{\text{vac}} = \frac{iq}{\hbar}A_\mu\langle\tilde{\Phi}\rangle ,
$$

and the gauge-invariant scalar kinetic term therefore reduces to a quadratic form in the connection,

$$
-\,g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)\Big|_{\text{vac}}
= -\,\frac{q^2v^2}{2\hbar^2}\,\mathrm{Sc}\!\left(\bar{\tilde{A}}\tilde{A}\right),
$$

which is a Proca mass term with

$$
M_A^2 = \frac{q^2v^2}{\hbar^2}.
$$

No mass term was written by hand: a term $m^2A_\mu A^\mu$ is not gauge invariant, while the kinetic term is, and the mass appears only after the non-invariant vacuum is substituted. The mass does not involve the quartic coupling $\beta$; the radial mode's mass $m_h^2 = 2\beta v^2$ does. The angular mode of the scalar is a would-be Goldstone boson with no potential; a gauge transformation removes it (the unitary gauge), and the connection acquires it as its longitudinal polarization. The degree-of-freedom count balances, $2 + 2 = 1 + 3$.

The coefficient and the count were recomputed: the induced quadratic form equals $-q^2v^2/2\hbar^2$ times $\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ on a generic connection direction and on two independent parameter sets (relative error below $10^{-15}$); the kinetic density is gauge invariant to round-off while a put-in mass term changes by a nonzero amount well above round-off; and the count balances only when the Goldstone mode is absorbed.

One gap is left visible and is not closed. The framework's scalar lies in the center and is therefore a **singlet of the non-abelian factor** $\mathfrak{su}(2)$ of the material sector; a singlet cannot break $SU(2)$. The framework supplies neither a scalar in a non-trivial representation, nor an electroweak doublet, nor the hypercharge assignments, and the reality condition on a non-abelian connection is itself open. The non-abelian and electroweak Higgs mechanism is therefore not constructed here, and the quantum numbers it would require are not invented. What is established is the mechanism and its counting; what is open is the representation of the scalar that the Standard Model needs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; abelian gauge factor |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient; $\partial_0 = \partial_{ict} = -i\partial_t/c$ |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | d'Alembertian |
| $\tilde{A} = \sum_\mu A_\mu e_\mu = i\phi/c\,e_0 + \mathbf{A} \in \mathbb{M}_-$ | Connection; $A_0$ imaginary, $\mathbf{A}$ real |
| $A_\mu$ | Complex connection coefficients (central, abelian) |
| $\Gamma$ | Real scalar gauge function |
| $\lambda = e^{iq\Gamma/\hbar}$ | Local central phase |
| $q, \hbar, \kappa = q/\hbar$ | Charge, reduced Planck constant, coupling |
| $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ | Gauge transformation of the connection |
| $D_\mu = \partial_\mu + i\kappa A_\mu$ | Covariant derivative |
| $\tilde{\Phi} = \varphi\,e_0 \in \mathbb{C}_{\mathbb{B}}$ | Complex central scalar field |
| $\varphi$ | Complex scalar amplitude; $|\varphi| = v/\sqrt{2}$ at the vacuum |
| $v$ | Vacuum expectation value parameter (so $\langle|\varphi|\rangle = v/\sqrt{2}$) |
| $V(\varphi^*\varphi) = \beta(\varphi^*\varphi - v^2/2)^2$ | Scalar potential; $\beta > 0$ is the quartic coupling |
| $\beta$ | Quartic self-coupling of the scalar (distinct from the phase $\lambda$) |
| $h$ | Radial (Higgs) mode, $m_h^2 = 2\beta v^2$ |
| $\theta$ | Angular (would-be Goldstone) mode |
| $g = \mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric for contractions |
| $\mathcal{L}_\text{scalar} = -g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi) - V$ | Gauge-invariant scalar Lagrangian |
| $-g^{\mu\nu}(D_\mu\varphi)^*(D_\nu\varphi)\big|_\text{vac} = -\frac{q^2v^2}{2\hbar^2}\mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$ | Kinetic term at the vacuum = mass term |
| $M_A^2 = q^2v^2/\hbar^2$ | Gauge boson mass-squared from the kinetic term |
| $\mathrm{Sc}(\bar{\tilde{A}}\tilde{A}) = \sum_\mu A_\mu^2$ | Norm form of the connection in $\mathbb{M}_-$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- *The Gauge Principle in Biquaternionic Form* — the origin of the connection, the complex scalar realization $\tilde{\Phi} = \varphi\,e_0$, the transformation law, and the covariant derivative inherited here.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the covariant derivative as an operator, the gauge orbit, the curvature, and the covariant square used in the gap discussion.
- *Non-Abelian Gauge Fields in Biquaternionic Form* — the compact algebra $\mathfrak{su}(2)$ inside $\mathbb{M}_-$, its reality gap, and the non-abelian connection whose absence bounds this article.
- *Chiral Fermions in the Biquaternion Framework* — the mass selection rule $q_L = q_R$, the charge operator, and the naming of this article as the compensating-scalar companion.
- *The Klein–Gordon Equation in Biquaternionic Form* — the free scalar equation whose gauging and vacuum this article uses.
- *Noether's Theorem in Biquaternionic Form* — the framework's scalar Lagrangian, whose complex-field normalization is discussed in the companion notes.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the sector's basis, its four-vectors, and the imaginary-scalar/real-vector structure of the connection.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian sector and the trace formula.
- *Maxwell's Equations in the Biquaternionic Form* — the abelian potential and field strength that the gauge field mass modifies.
- *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* — the left/right matter-representation question that the non-abelian scalar inherits.
- *Canonical Quantization of the Biquaternion Maxwell Field* — the framework's inability to fix the gauge, which the unitary gauge here chooses rather than derives.
- *Biquaternion Algebra* — the multiplication rule, the conjugations, and the center used throughout.
