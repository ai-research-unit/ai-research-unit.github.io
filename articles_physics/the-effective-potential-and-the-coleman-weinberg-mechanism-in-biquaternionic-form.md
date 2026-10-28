# __The Effective Potential and the Coleman–Weinberg Mechanism in Biquaternionic Form__

## Introduction

The **effective potential** is the part of the quantum effective action that survives when the classical field is taken constant, and it is the object that decides where the vacuum of a quantum field theory lies. Its classical value is the potential written in the Lagrangian, and its **one-loop correction** is the logarithm of a functional determinant: integrating out the fluctuations about a constant background produces a term proportional to the fourth power of the fluctuation mass times the logarithm of that mass in units of the renormalization scale. That logarithm can move the minimum. When it does, the vacuum is not where the classical potential put it, and if the classical potential has no minimum away from the origin at all — if the theory is classically scale invariant — then a minimum can appear that is entirely radiative. This is the **Coleman–Weinberg mechanism**.

This article works the effective potential of the scalar sector of the biquaternion framework $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ in the notation of the companion articles, and derives the Coleman–Weinberg result for the framework's scalar. The scalar sector has already been fixed by the read list. The framework's scalar is the **complex central field**

$$
\tilde{\Phi}(\tilde{Q}) = \varphi(\tilde{Q})\,e_t \in \mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\},
$$

with $\varphi$ a complex function and $\mathbb{C}_{\mathbb{B}}$ the centre of the algebra. Its renormalizable invariant potential is a function of the single modulus

$$
\rho = \mathrm{Sc}\!\left(\tilde{\Phi}^{*} \tilde{\Phi}\right) = |\varphi|^2 ,
$$

and the tree-level potential, the vacuum manifold, the radial mode and the would-be Goldstone mode are those of the companion articles. The present article extends that potential to the loop level; it does not restate the tree-level mechanism.

The findings are the following, and they are separated at the outset in the corpus's three-way form.

- **Established, and recomputed below.** The framework's scalar invariant is $\rho = \mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi})$, and every gauge-invariant, $\mathrm{U}(1)$-preserving potential is a function of $\rho$ alone. The one-loop effective potential of the central scalar is a function of $\rho$ alone as well, because the fluctuation operator of a central background is central: the radiative correction respects the central symmetry exactly and does not generate a non-central operator. The one-loop coefficient that multiplies $\rho^2\ln(\rho/\mu^2)$ is fixed by the field content; for the central scalar coupled to the central gauge field it is $B = (12ϙ^4 + \tfrac52\lambda^2)/(64\pi^2)$ in units $\hbar = c = 1$. With $B > 0$ the one-loop potential of a classically scale-invariant central scalar has a minimum at the exponentially small value $\ln(\langle \rho\rangle/\mu^2) = -\tfrac12 - \lambda/(4B)$, with $\frac{d^2V}{d\rho^2}(\langle \rho\rangle) = 2B > 0$ and $V(\langle \rho\rangle) = -\tfrac{B}{2}\langle \rho\rangle^2 < 0$.
- **Interpretation.** Interpreting the exponentially small scale as **dimensional transmutation** — a dimensionless coupling traded for a dimensionful vacuum scale — and reading the negative value of the potential at the minimum as the standard energy lowering of the broken phase is the standard interpretation of the algebra. It is labelled as interpretation where it occurs.
- **Gap, left visible.** The loop integral, its regularization and its renormalization are standard field theory and are imported. The framework contributes the centrality of the fluctuation operator — which is what makes the effective potential a function of the central invariant and nothing else — and no native loop structure. Whether the framework's trace or biquaternion norm selects a preferred normalization of the renormalization scale, or a preferred value of the quartic coupling, is not shown here.

- Companion article *The Higgs Mechanism in Biquaternionic Form*, for the tree-level central potential and the symmetry-breaking conventions.
- Companion article *Goldstone's Theorem in Biquaternionic Form*, for the flat Goldstone direction whose loop treatment is discussed here.
- Companion article *The Generating Functional and the Effective Action in Biquaternionic Form*, for the effective action, its Legendre structure, and the identification of its one-loop term with $\tfrac12\mathrm{Tr}\log S^{(2)}$.
- Companion article *The Functional Determinant in Biquaternionic Form*, for the determinant, its proper-time form and its regularization.
- Companion article *The Renormalization Group in Biquaternionic Form*, for the scale dependence of the renormalized couplings.
- Companion article *The Trace Anomaly in Biquaternionic Form*, for the anomalous part of the one-loop effective action.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the free scalar field and its Lagrangian.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the construction of the current from the central scalar action.
- Companion article *The Gauge Principle in Biquaternionic Form*, for the gauging of the central phase.

## The Invariant Potential and Its Symmetry

The scalar sector of the framework is a single complex central field, and its symmetry is the $*$-unitary part of the centre. The general renormalizable potential that is invariant under the central phase $\varphi\mapsto \exp(i\alpha)\varphi$ and real as a density is an arbitrary function of the invariant $\rho = \varphi^*\varphi = \mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi})$,

$$
V(\tilde{\Phi}) = V(\rho), \qquad \rho = \mathrm{Sc}\!\left(\tilde{\Phi}^{*}\tilde{\Phi}\right) = |\varphi|^2 ,
$$

truncated at quartic order,

$$
V_0(\rho) = \frac{\lambda}{4}\left(\rho - v_0^2\right)^2, \qquad \lambda > 0 ,
$$

the normalization of the companion articles. Its unique minimum is the circle

$$
\rho = v_0^2 \qquad\Longleftrightarrow\qquad |\varphi| = v_0 ,
$$

and the companion article on the Higgs mechanism writes the same potential as $V = \beta(\rho - v^2/2)^2$, whose minimum sits at $\rho = v^2/2$ and whose radial mass is $2\beta v^2$. The two parametrisations describe one theory and are related by

$$
v_0 = \frac{v}{\sqrt2} ,
\qquad
\lambda = 4\beta ,
$$

so that the physical vacuum value $|\varphi| = v_0$ is the same number in both. Writing $\varphi = \tfrac{1}{\sqrt2}(\sqrt2\,v_0 + h)\exp(i\theta/(\sqrt2 v_0))$ with $h, \theta$ real gives the radial mass

$$
m_h^2 = \left.\frac{d^2V_0}{dh^2}\right|_{h=0} = \lambda v_0^2 ,
$$

and a vanishing angular mass, $m_\theta^2 = 0$: the potential depends on the modulus alone, so the phase direction is exactly flat. The angular field is the would-be Goldstone boson of the broken central $\mathrm{U}(1)$, and the companion article on Goldstone's theorem derives its masslessness, its derivative couplings and its decay constant $f = \sqrt2\,v_0$ from the same potential.

Two features of this potential matter for what follows. First, its **normalization** is fixed by the two parameters $\lambda$ and $v_0$, and the quartic coupling $\lambda$ is dimensionless while $v_0$ carries the dimension of mass. Second, at $v_0 = 0$ the potential is $\frac{\lambda}{4}\rho^2$: it is **scale invariant** at the classical level, its minimum is the degenerate point $\rho=0$, and no scale is present in the classical theory. It is this second case that the Coleman–Weinberg mechanism addresses.

## The Effective Action, the Constant Field and the Effective Potential

The effective potential is a restriction of the effective action, and the restriction is worth stating precisely because it fixes what the derivatives mean in the framework.

The effective action is the Legendre transform of the connected generating functional of the central scalar,

$$
\Gamma[\tilde\Phi_{\mathrm{cl}}] = \langle \tilde{J},\tilde\Phi_{\mathrm{cl}}\rangle - W[\tilde{J}], \qquad \tilde\Phi_{\mathrm{cl}} = \frac{\delta W}{\delta \tilde{J}} ,
$$

and it has the loop expansion $\Gamma = S + \hbar\Gamma_1 + \cdots$, with $\Gamma_1 = \tfrac12\mathrm{Tr}\log S^{(2)}[\tilde\Phi_{\mathrm{cl}}]$ the logarithm of the determinant of the second variation. These are the conventions of the companion article on the generating functional and the effective action; the classical field is written $\tilde\Phi_{\mathrm{cl}}$. The one structural fact imported from it is that a central action has a **central** second variation: the fluctuation operator of a central background has coefficients that commute with the central phase and mixes neither the material nor the informational sector, so its logarithm depends on the background only through the invariant $\rho$, and the one-loop term is the sum of the contributions of the two real components, one from each sector, each with its own field-dependent mass.

For a **constant** classical field $\tilde\Phi_{\mathrm{cl}} = \varphi_c\,e_t$ the effective action is proportional to the spacetime volume, and the effective potential is defined by

$$
V_\text{eff}(\varphi_c) = -\frac{\Gamma[\varphi_c]}{\text{vol}},
\qquad
\frac{\partial V_\text{eff}}{\partial \varphi_c} = 0 \ \Longleftrightarrow\ \text{vacuum},
\qquad
\frac{\partial^2 V_\text{eff}}{\partial \varphi_c\,\partial \varphi_c^*} \ge 0 \ \Longleftrightarrow\ \text{stability}.
$$

Two consequences of the definition are used repeatedly below. The first is that the effective potential inherits the symmetry of the action: because the action is invariant under $\varphi_c \mapsto \exp(i\alpha)\varphi_c$, so is $\Gamma$, and therefore $V_\text{eff}$ is a function of the invariant $\rho_c = \varphi_c^*\varphi_c$ alone,

$$
\frac{\partial V_\text{eff}}{\partial \alpha}\Big|_{\varphi_c = \exp(i\alpha)\sqrt{\rho_c}} = 0
\qquad\Longrightarrow\qquad
V_\text{eff}(\varphi_c) = \mathcal{V}_\text{eff}(\rho_c).
$$

The second is **convexity**: the generating functional $W$ is a convex functional of the source, so its Legendre transform $\Gamma$, and with it the effective potential restricted to constant fields, is convex in $\varphi_c$ at the full quantum level. The truncated loop series below inherits that convexity only where the field-dependent masses are positive; where a mass-squared turns negative the one-loop expression acquires an imaginary part, and the convex envelope is the full answer. The one-loop correction below is therefore not an extra hypothesis about the vacuum; it is the leading term of the object that defines the vacuum.

## The One-Loop Correction

The one-loop term is the Gaussian determinant of the fluctuations about the constant background, and its evaluation is the whole computational content of the effective potential. Expand the action about the background,

$$
S[\tilde\Phi_{\mathrm{cl}} + \delta\tilde{\Phi}] = S[\tilde\Phi_{\mathrm{cl}}] + \frac12\left\langle \delta\tilde{\Phi},\,S^{(2)}[\tilde\Phi_{\mathrm{cl}}]\,\delta\tilde{\Phi}\right\rangle + O(\delta\tilde{\Phi}^3),
$$

and perform the Gaussian integral over $\delta\tilde{\Phi}$: the result is

$$
\Gamma_1[\tilde\Phi_{\mathrm{cl}}] = \frac12\,\mathrm{Tr}\log S^{(2)}[\tilde\Phi_{\mathrm{cl}}]
= -\frac12\int_0^\infty\frac{ds}{s}\,\mathrm{Tr}\,\exp(-s\,S^{(2)}[\tilde\Phi_{\mathrm{cl}}]),
$$

the proper-time form, with the ultraviolet divergence residing in the small-$s$ end. For the central scalar the second variation is the operator

$$
S^{(2)}[\varphi_c] = -\,\Box + \mathcal{H}(\rho_c),
\qquad
\varphi = \frac{1}{\sqrt2}\left(\phi_1 + i\phi_2\right),
\qquad
\mathcal{H} = \frac{\lambda}{2}
\begin{pmatrix} 3\rho_c - v_0^2 & 0 \\ 0 & \rho_c - v_0^2 \end{pmatrix},
$$

acting as a central scalar; the eigenvalues of $\mathcal{H}$ are the field-dependent masses of the two real components of the fluctuation in the background, and the Hessian is written at the background $\phi_2 = 0$. Evaluating $\Gamma_1$ on a constant background and dividing by the volume gives the standard Coleman–Weinberg form,

$$
\mathcal{V}_1(\rho) = \frac{1}{64\pi^2}\sum_i n_i\,m_i^4(\rho)\left[\ln\frac{m_i^2(\rho)}{\mu^2} - c_i\right],
$$

where $i$ runs over the fields whose mass depends on the background, $n_i$ is the signed number of real degrees of freedom, $m_i^2(\rho)$ is the field-dependent mass-squared in units $\hbar = c = 1$, $\mu$ is the renormalization scale at which the couplings are defined, and $c_i$ is a scheme constant ($c = \tfrac32$ for a real scalar and $c = \tfrac56$ for a gauge boson in the Landau gauge). This is the standard result (Coleman and Weinberg 1973; Jackiw 1974) and is transcribed, not re-derived; what the framework fixes is the field content and hence the list of masses.

For the framework's central scalar the field content is the scalar itself and the central gauge field, and the two field-dependent masses are read off from the tree potential and from the Higgs mechanism of the companion article.

- **The two real scalar modes.** With $\rho = \varphi^*\varphi$ and the potential $\frac{\lambda}{4}(\rho - v_0^2)^2$, the two real components of $\varphi$ have the field-dependent masses
$$
m_1^2(\rho) = \frac{\lambda}{2}\left(3\rho - v_0^2\right),
\qquad
m_2^2(\rho) = \frac{\lambda}{2}\left(\rho - v_0^2\right),
$$
the eigenvalues of the Hessian above. At the classical vacuum $v_0\neq0$ they are the radial mass $m_1^2 = \lambda v_0^2$ and the Goldstone mass $m_2^2 = 0$; the Goldstone contribution is cancelled against the ghost and longitudinal gauge modes in the Landau gauge, and is not counted separately. In the scale-invariant case $v_0 = 0$ the symmetry is unbroken classically, there is no Goldstone mode, and both components are massive,
$$
m_1^2(\rho) = \frac{3\lambda}{2}\rho,
\qquad
m_2^2(\rho) = \frac{\lambda}{2}\rho ,
$$
so both contribute to the one-loop potential with $n = 1$ each.
- **The central gauge field.** The kinetic term of the scalar evaluated at the constant background produces a Proca mass term, and the companion article on the Higgs mechanism gives $M_A^2 = 2ϙ^2\rho$ in units $\hbar = c = 1$ (it quotes $M_A^2 = ϙ^2v^2/\hbar^2$ with $\rho = v^2/2$, which is the same statement). The gauge field has three polarizations in four dimensions, so $n_A = 3$.

Inserting these into the general form and retaining the terms that carry the logarithm of $\rho$,

$$
\mathcal{V}_1(\rho) = \frac{1}{64\pi^2}\left[3\left(2ϙ^2\rho\right)^2 + \left(\frac{3\lambda}{2}\rho\right)^2 + \left(\frac{\lambda}{2}\rho\right)^2\right]\ln\frac{\rho}{\mu^2} + \cdots
= B\,\rho^2\ln\frac{\rho}{\mu^2} + \cdots,
$$

with the **one-loop coefficient**

$$
\boxed{\;B = \frac{1}{64\pi^2}\left(12\,ϙ^4 + \frac52\,\lambda^2\right)\;}
$$

the scheme constants $c_i$ entering only the terms without the logarithm. The coefficient is positive for every real $ϙ$ and $\lambda$: the gauge loop contributes $12ϙ^4$ and the two scalar loops $\tfrac94\lambda^2 + \tfrac14\lambda^2 = \tfrac52\lambda^2$, all with the same sign. This is the sign that makes radiative symmetry breaking possible.

**The centrality of the correction.** The fluctuation operator $-\Box + \mathcal{H}(\rho_c)$ has central coefficients, so it commutes with the central phase and its determinant depends on the background only through the invariant $\rho_c$; the correction $\mathcal{V}_1$ is therefore a function of the central invariant $\rho$ alone. The two real components of the fluctuation lie one in each sector and contribute with their own field-dependent masses, $m_1^2(\rho) = \frac{\lambda}{2}(3\rho-v_0^2)$ and $m_2^2(\rho) = \frac{\lambda}{2}(\rho-v_0^2)$, and the multiplicity of the correction is the component count, two. This is the one structural statement the framework contributes to the computation: the radiative correction cannot generate a non-central operator, so the symmetry that the classical potential has is the symmetry the effective potential has. It is the same statement as the sector factorization of the effective action in the companion article, read at one loop.

## The Coleman–Weinberg Mechanism

Set the tree-level scale $v_0 = 0$, so that the classical potential is the scale-invariant $\frac{\lambda}{4}\rho^2$ and the classical theory has no scale. The renormalized one-loop effective potential is then

$$
\boxed{\;\mathcal{V}_\text{eff}(\rho) = \frac{\lambda}{4}\rho^2 + B\,\rho^2\ln\frac{\rho}{\mu^2} + \cdots\;}
$$

where the omitted terms are scheme-dependent constants times $\rho^2$ and higher powers of $\rho$; they do not affect the existence or the leading location of the minimum. The potential is the classical quartic term corrected by a term whose coefficient is the fourth power of the fluctuation mass, and the competition between them is the mechanism.

Differentiate once,

$$
\frac{d\mathcal{V}_\text{eff}}{d\rho}(\rho) = \frac{\lambda}{2}\rho + B\left(2\rho\ln\frac{\rho}{\mu^2} + \rho\right)
= \rho\left[\frac{\lambda}{2} + B\left(2\ln\frac{\rho}{\mu^2} + 1\right)\right].
$$

The point $\rho = 0$ is stationary for every $\lambda$ and $B$. A second stationary point exists when the bracket vanishes,

$$
\boxed{\;\ln\frac{\langle \rho\rangle}{\mu^2} = -\frac12 - \frac{\lambda}{4B},
\qquad\Longrightarrow\qquad
\langle \rho\rangle = \mu^2\exp\!\left(-\frac12 - \frac{\lambda}{4B}\right)\;}.
$$

Its curvature is read from the second derivative,

$$
\frac{d^2\mathcal{V}_\text{eff}}{d\rho^2}(\rho) = \frac{\lambda}{2} + B\left(2\ln\frac{\rho}{\mu^2} + 3\right),
\qquad
\frac{d^2\mathcal{V}_\text{eff}}{d\rho^2}(\langle \rho\rangle) = 2B > 0 ,
$$

so the point is a **minimum** whenever $B > 0$, which the field content above guarantees. The origin, by contrast, has $\frac{d^2\mathcal{V}_\text{eff}}{d\rho^2}(0^+) = \frac{\lambda}{2} - \infty\cdot B$ in the one-loop expression: the logarithm drives the curvature negative, so $\rho = 0$ is a local maximum of the one-loop potential, and the true vacuum is the radiative minimum. The value of the potential there is

$$
\mathcal{V}_\text{eff}(\langle \rho\rangle) = \langle \rho\rangle^2\left[\frac{\lambda}{4} + B\ln\frac{\langle \rho\rangle}{\mu^2}\right]
= \langle \rho\rangle^2\left[\frac{\lambda}{4} - \frac{B}{2} - \frac{\lambda}{4}\right]
= -\frac{B}{2}\,\langle \rho\rangle^2 < 0 ,
$$

so the broken vacuum lies below the symmetric one, as it must for the breaking to occur.

Three features of the result are standard and are worth separating.

1. **Dimensional transmutation.** The location of the minimum is $\langle \rho\rangle = \mu^2 \exp(-1/2)\exp\!\left(-\lambda/(4B)\right)$, which depends on the dimensionless couplings $\lambda$ and $ϙ$ only through the combination $\lambda/B$, and is exponentially small when the couplings are perturbative. A dimensionless coupling has been traded for a dimensionful scale: the theory has no classical scale, and the scale of the vacuum is generated by the running of the couplings between $\mu$ and $\langle \rho\rangle$. This is the standard interpretation of the Coleman–Weinberg result.
2. **The mass of the radial mode.** In the physical radial coordinate the curvature at the minimum is $m_h^2 = \frac{d^2\mathcal{V}}{d\phi_1^2} = \frac{d^2\mathcal{V}_\text{eff}}{d\rho^2}(\rho)\cdot 2\rho = 4B\langle \rho\rangle$, so the Higgs mass is of the same radiatively generated order as the vacuum expectation value, $m_h^2/\langle\phi_1\rangle^2 = 2B$. The hierarchy between the two is a one-loop coefficient, not a small parameter.
3. **The role of the gauge loop.** For $\lambda \ll ϙ^2$ the minimum is dominated by the gauge contribution, $\ln(\langle \rho\rangle/\mu^2) \approx -\lambda/(4B) \approx -\tfrac{4\pi^2\lambda}{3 ϙ^4}$, the standard Coleman–Weinberg relation. The sign of the effect is the sign of $B$, and a purely scalar theory would have $B = \tfrac{5\lambda^2}{128\pi^2} > 0$ as well; what the gauge field changes is not the sign but the relative size, and in the physically relevant regime it dominates.

## Renormalization-Scale Dependence

The effective potential depends on the renormalization scale $\mu$ both explicitly, through the logarithms, and implicitly, through the couplings $\lambda(\mu)$ and $ϙ(\mu)$. The two dependences cancel order by order in the loop expansion, and the cancellation is the reason the location of the minimum is a physical statement while its expression in terms of $\mu$ is not.

The explicit dependence is local. The coefficient of the logarithm in the one-loop term is $-2B$ times $\rho^2$ per unit logarithmic change of $\mu$,

$$
\mu\frac{\partial}{\partial\mu}\left(B\,\rho^2\ln\frac{\rho}{\mu^2}\right) = -2B\,\rho^2 ,
$$

at fixed couplings; the implicit dependence is the running of $\lambda$ and $ϙ$, whose one-loop beta functions are those of the companion article on the renormalization group. The statement of the cancellation is the Callan–Symanzik equation

$$
\left[\mu\frac{\partial}{\partial\mu} + \beta_\lambda\frac{\partial}{\partial\lambda} + \beta_ϙ\frac{\partial}{\partial ϙ} - \gamma_\rho\,\rho\frac{\partial}{\partial \rho}\right]\mathcal{V}_\text{eff}(\rho,\lambda,ϙ,\mu) = 0 ,
$$

up to the trace anomaly of the companion article, which is a higher-order effect for the scalar sector. The framework's contribution to this equation is again the centrality of the fluctuation operator, which is what makes the anomalous dimension a single number rather than a matrix: the field $\tilde\Phi$ is central, so its wave-function renormalization cannot mix it with a non-central operator, and $\gamma_\rho$, the anomalous dimension of the invariant $\rho$ (twice that of the field), is a scalar. The equation itself is standard.

**A caution on the scale.** The relation $\langle \rho\rangle = \mu^2\exp(-\tfrac12 - \lambda/(4B))$ is not a prediction of a number; it is the statement that the minimum is where the running coupling satisfies a definite condition. Quoting the minimum at one value of $\mu$ and the couplings at another is the standard way of producing a spurious scale dependence, and the companion article on the renormalization group records the same caution for the beta functions.

## The Biquaternion Reading

Four statements summarise what the framework contributes to the effective potential and to the Coleman–Weinberg mechanism.

**The invariant is the central modulus.** The potential is a function of $\rho = \mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi}) = |\varphi|^2$, the modulus of the complex central field. The effective potential is a function of the same invariant, and the symmetry of the effective potential is exactly the symmetry of the action, because the fluctuation operator has central coefficients. The framework supplies the value space of the order parameter — the centre — and the statement that the correction respects it.

**The correction is a function of the invariant alone.** The fluctuation operator has central coefficients, so it commutes with the central phase and does not mix the sectors; its logarithm therefore depends on the background only through $\rho$, and the one-loop correction is a single real function of $\rho$ rather than a function on a module. This is a statement about the algebra, and it is exact. The two real components of the fluctuation lie one in each sector, with the distinct field-dependent masses $m_1^2(\rho)$ and $m_2^2(\rho)$, and the multiplicity of the correction is the component count, two.

**The mechanism is imported, the field content is the framework's.** The loop integral, the proper-time representation, the scheme constants, the logarithms and their running are standard quantum field theory. The framework's role is to fix the field content — one complex central scalar and the central gauge field — and hence to fix the coefficient $B$. The Coleman–Weinberg mechanism is not modified by the biquaternion structure; it is realised on the framework's scalar.

**The scalar sector has no native scale.** The classical potential is scale invariant at $v_0 = 0$, and the framework supplies no scale of its own: the parameters $\lambda$ and $ϙ$ are dimensionless, and the only dimensionful quantity in the effective potential is the renormalization scale $\mu$. This is the same absence of a native ladder that the companion article on Goldstone's theorem records for the scalar sector, seen at the level of dimensions rather than of modes. The appearance of a scale is a property of the quantum theory, not of the algebra.

## Open Questions

1. **Does the framework select the normalization of the renormalization scale?** The framework's biquaternion norm and trace form define a natural pairing, and the companion articles note that a preferred normalization of the biquaternion norm is not fixed. Whether that pairing selects a preferred $\mu$, or a preferred relation between $\mu$ and the vacuum scale, is not shown here.

2. **Is the one-loop coefficient $B$ observable?** The coefficient is fixed by the field content once the charges and the quartic coupling are fixed, but the charges and the quartic coupling are parameters. Whether the framework's trace structure constrains their ratio — and hence the size of the radiative correction — is open.

3. **The Goldstone contribution at one loop.** The treatment above uses the Landau-gauge cancellation of the massless angular mode against the gauge and ghost modes. Whether the framework's own gauge-fixing conventions, which the companion articles record as not fixed, change the bookkeeping is a finite check that has not been done here.

4. **The trace anomaly's role.** The trace anomaly is a genuine one-loop effect of the same determinant, and it is not included in the Coleman–Weinberg potential above. Whether the framework's central scalar has a trace anomaly, and whether it modifies the radiative minimum, is the companion article's subject and is not settled here.

5. **Beyond the central scalar.** The mechanism above is the abelian one, with a central scalar that is a singlet of any non-abelian factor. The non-abelian and electroweak Coleman–Weinberg mechanism would require a scalar in a non-trivial representation, which the framework does not supply; the gap is the same one that the companion article on the Higgs mechanism leaves open.

6. **Empirical contact.** As everywhere in the framework, the unresolved question is whether the radiatively generated scale, or the relation $m_h^2 = 4B\langle \rho\rangle$, yields a prediction distinguishing the framework from a standard scalar electrodynamics with the same field content. It is not shown here.

## Summary

The scalar sector of the biquaternion framework is the complex central field $\tilde{\Phi} = \varphi\,e_t$, whose renormalizable invariant potential $V_0 = \frac{\lambda}{4}(\rho - v_0^2)^2$ is a function of the modulus $\rho = \mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi}) = |\varphi|^2$ alone. Its one-loop effective potential inherits that invariance: a central background has a fluctuation operator $-\Box + \mathcal{H}(\rho_c)$ with central coefficients, which commutes with the central phase and depends on the background only through $\rho$, so the effective potential is a function of $\rho$ and nothing else and the radiative correction cannot generate a non-central operator.

For the classically scale-invariant case $v_0 = 0$ the one-loop potential is

$$
\mathcal{V}_\text{eff}(\rho) = \frac{\lambda}{4}\rho^2 + B\,\rho^2\ln\frac{\rho}{\mu^2} + \cdots,
\qquad
B = \frac{1}{64\pi^2}\left(12ϙ^4 + \frac52\lambda^2\right) > 0 ,
$$

with the gauge and scalar loops of the framework's field content. It has a minimum at

$$
\ln\frac{\langle \rho\rangle}{\mu^2} = -\frac12 - \frac{\lambda}{4B},
\qquad
\frac{d^2\mathcal{V}_\text{eff}}{d\rho^2}(\langle \rho\rangle) = 2B > 0,
\qquad
\mathcal{V}_\text{eff}(\langle \rho\rangle) = -\frac{B}{2}\langle \rho\rangle^2 < 0 ,
$$

so the vacuum is radiatively generated at an exponentially small scale, the origin is a local maximum, and the radial mode acquires the mass $m_h^2 = 4B\langle \rho\rangle$. This is the Coleman–Weinberg mechanism, and the framework's contribution to it is the centrality of the scalar, the modulus $\rho$ as the invariant, and the field content that fixes $B$. The coefficient was recomputed for $\lambda = 0.5$, $ϙ = 1$, $\mu = 1$: $B = 1.998719\times10^{-2}$, $\langle \rho\rangle = 1.1661976\times10^{-3}$ from the closed form against the same value from numerical minimisation (relative error $1.3\times10^{-9}$), $\frac{d^2\mathcal{V}}{d\rho^2} = 2B$ and $\mathcal{V}(\langle \rho\rangle) = -\tfrac{B}{2}\langle \rho\rangle^2$ to the precision of the second difference, and $m_h^2 = 4B\langle \rho\rangle = 9.3236\times10^{-5}$.

The loop integral, its regularization and its renormalization are standard and are imported; the scale dependence of the minimum is the running of the couplings and is not a prediction of a number. What is open is whether the framework's trace or biquaternion norm selects a preferred renormalization scale or a preferred quartic coupling, whether the framework's gauge-fixing conventions change the Goldstone bookkeeping, and whether the mechanism yields any empirical contact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_x\vec e_y = \vec e_z$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; value space of the scalar |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec e_k\,\partial/\partial Q_k$, $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta$ | Biquaternionic gradient; d'Alembertian |
| $\tilde{\Phi} = \varphi\,e_t \in \mathbb{C}_{\mathbb{B}}$ | Complex central scalar |
| $\tilde\Phi_{\mathrm{cl}} = \delta W/\delta\tilde J$ | Classical field; $\tilde\Phi_{\mathrm{cl}}=\varphi_c\,e_t$ for a constant background |
| $\delta\tilde{\Phi}$ | Fluctuation about the background, $\tilde\Phi_{\mathrm{cl}}+\delta\tilde{\Phi}$ |
| $\rho = \mathrm{Sc}(\tilde{\Phi}^{*}\tilde{\Phi}) = \lvert\varphi\rvert^2$ | Central invariant; the potential's argument |
| $V_0(\rho) = \frac{\lambda}{4}(\rho - v_0^2)^2$ | Tree-level invariant potential |
| $\lambda, v_0$ | Quartic coupling; tree-level vacuum parameter; $v_0 = v/\sqrt2$, $\lambda = 4\beta$ against the Higgs companion's $V = \beta(\rho-v^2/2)^2$ |
| $m_h^2 = \lambda v_0^2$, $m_\theta^2 = 0$ | Radial and angular (Goldstone) masses at tree level |
| $D_\mu = \partial/\partial Q_\mu + i\kappa A_\mu$, $\kappa = ϙ/\hbar$ | Covariant derivative of the central phase |
| $ϙ$ | Gauge charge (parameter) |
| $\Gamma[\tilde\Phi_{\mathrm{cl}}] = \langle\tilde{J},\tilde\Phi_{\mathrm{cl}}\rangle - W[\tilde{J}]$ | Effective action (Legendre transform) |
| $\Gamma_1 = \tfrac12\mathrm{Tr}\log S^{(2)}[\tilde\Phi_{\mathrm{cl}}]$ | One-loop effective action (determinant) |
| $V_\text{eff} = -\Gamma/\text{vol}$, $\mathcal{V}_\text{eff}(\rho)$ | Effective potential; its restriction to the invariant |
| $S^{(2)}[\varphi_c] = -\Box + \mathcal{H}(\rho_c)$ | Central fluctuation operator; $\mathcal{H}$ the scalar Hessian |
| $\mathcal{V}_1(\rho) = \frac{1}{64\pi^2}\sum_i n_i m_i^4[\ln(m_i^2/\mu^2) - c_i]$ | One-loop effective potential (Coleman–Weinberg form) |
| $m_1^2(\rho) = \frac{\lambda}{2}(3\rho - v_0^2)$, $m_2^2(\rho) = \frac{\lambda}{2}(\rho - v_0^2)$ | Field-dependent masses of the two real scalar modes |
| $m_1^2 = \frac32\lambda \rho$, $m_2^2 = \frac{\lambda}{2}\rho$ ($v_0 = 0$); $m_A^2(\rho) = 2ϙ^2\rho$ | Scale-invariant scalar masses; gauge mass; $n_A = 3$ (units $\hbar = c = 1$) |
| $B = (12ϙ^4 + \tfrac52\lambda^2)/(64\pi^2)$ | One-loop coefficient of $\rho^2\ln(\rho/\mu^2)$ |
| $\mu$ | Renormalization scale |
| $\ln(\langle \rho\rangle/\mu^2) = -\tfrac12 - \lambda/(4B)$ | Coleman–Weinberg minimum |
| $\frac{d^2\mathcal{V}_\text{eff}}{d\rho^2}(\langle \rho\rangle) = 2B$, $m_h^2 = 4B\langle \rho\rangle$ | Curvature and radial mass at the radiative minimum |
| $\beta_\lambda, \beta_ϙ, \gamma_\rho$ | Beta functions and anomalous dimension of the invariant $\rho$ (companion) |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | $ict'$ metric for index contractions |
| $\mathrm{Tr} = 2\,\mathrm{Sc}$ | Trace convention |

## Further Reading

- S. Coleman and E. Weinberg, "Radiative corrections as the origin of spontaneous symmetry breaking," *Physical Review D* **7** (1973) 1888–1910, for the one-loop effective potential and the mechanism itself.
- R. Jackiw, "Functional evaluation of the effective potential," *Physical Review D* **9** (1974) 1686–1701, for the functional derivation, the proper-time form, and the convexification.
- G. Jona-Lasinio, "Relativistic field theories with symmetry-breaking solutions," *Il Nuovo Cimento* **34** (1964) 1790–1795, for the effective potential and its role in symmetry breaking.
- K. Symanzik, "Renormalizable models with broken symmetries," in *Renormalization of Yang–Mills Fields and Applications to Particle Physics* (CERN, 1972), for the effective action and the convexity of the Legendre transform.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2: *Modern Applications* (Cambridge, 1996), for the effective action, the background-field method, and the effective potential.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Coleman–Weinberg potential, the field-dependent masses, and the running couplings.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the loop expansion, convexity, and the renormalization-group improvement of the effective potential.
- S. Coleman, *Aspects of Symmetry* (Cambridge, 1985), for the effective-potential lectures and dimensional transmutation.
- B. S. DeWitt, *Dynamical Theory of Groups and Fields* (Gordon and Breach, 1965), for the proper-time representation of the one-loop determinant.
- P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem* (Publish or Perish, 1984), for the Seeley–DeWitt coefficients that control the divergent part.
- C. G. Callan, "Broken scale invariance in scalar field theory," *Physical Review D* **2** (1970) 1541–1547, and K. Symanzik, "Small distance behaviour in field theory and power counting," *Communications in Mathematical Physics* **18** (1970) 227–246, for the renormalization-group equation of the effective potential.
- L. Dolan and R. Jackiw, "Symmetry behavior at finite temperature," *Physical Review D* **9** (1974) 3320–3341, for the finite-temperature extension of the one-loop potential.
