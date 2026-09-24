# __The Klein–Gordon Equation in Biquaternionic Form__

## Introduction

The Klein–Gordon equation for a relativistic field of rest mass $m$ is

$$
\left(\Box - \frac{m^2c^2}{\hbar^2}\right)\phi = 0,
\qquad
\Box = -\frac{1}{c^2}\partial_t^2 + \Delta,
$$
<!-- CONVENTION — notation (reciprocal). This article's d'Alembertian is the series convention, □ = ∇̃∇̄̃ = ∂²_{ict} + Δ = Δ − c⁻²∂_t². It is MINUS the □ of the exercise article Chirality and the Weyl Spinors, which writes □ = ∂₀² − ∇² and therefore (□ + m²)ψ = 0. The two mass-term signs are the same equation: (□ − m²c²/ℏ²) here and (□ + m²) there have the same kernel, because □_there = −□_here. Do not "correct" either sign in isolation; the two articles differ in metric/sign convention, not in physics. -->

the wave equation for a relativistic scalar field. It is the equation that a spin-$0$ field obeys, and it is **second order in the time coordinate**. The companion article *Relativistic Mechanics in Biquaternionic Form* already recorded its biquaternion form in one line, $\left(\tilde{\nabla}\bar{\tilde{\nabla}} - m^2c^2/\hbar^2\right)\tilde{\Phi} = 0$, as one of the ten formulas of relativistic mechanics. The present article does not repeat that line for its own sake; it examines what the line does and does not carry.

Two facts about the equation drive everything below. The first is structural: being second order in time, the Klein–Gordon equation is not a single first-order evolution. Equivalently, its general solution carries a positive-frequency and a negative-frequency branch, and both $\phi$ and its complex conjugate $\phi^*$ are needed to describe it. The second is physical, and is the standard objection to the equation as a one-particle wave equation: the two branches come with energies of both signs, the conserved density is not positive definite, and the equation does not conserve particle number. Both defects are real, and the biquaternion notation does not remove either; the honest question is whether it relocates them usefully.

The framework's central algebraic fact is the decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$. The parent article, *The Schrödinger Equation in Biquaternionic Form*, showed that the first-order-in-time Schrödinger equation is organized by the **scalar imaginary** $i$: the Hermitian observable $\tilde{H}\in\mathbb{M}_+$ generates a flow whose generator $\tilde{G} = -i\tilde{H}/\hbar$ lies in the material sector $\mathbb{M}_-$, and the same central $i$ supplies the complex structure of the state module. This article asks the corresponding question for the second-order equation: **does the second-order structure fit the $\mathbb{M}_-/\mathbb{M}_+$ split naturally, or does it require a doubling that the split does not supply?** The answer worked out below is that it requires a doubling, and that the doubling is *not* $\mathbb{M}_+\oplus\mathbb{M}_-$; the sector split gives two $i$-related copies of the same equation, not the particle–antiparticle pair.

The conventions are those of the read list. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \varepsilon_{jkl}e_l$, and $i$ is the scalar imaginary, central in $\mathbb{B}$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, imaginary scalar and real vector), $\mathbb{M}_+$ (Hermitian, real scalar and imaginary vector), $\mathbb{H}_{\mathbb{B}}$ (real quaternions, the fixed points of complex conjugation), and $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_{\mathbb{R}}\{e_0, ie_0\}$ (the complex scalar line, which is the center). The gradient is $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ with $\bar{\tilde{\nabla}} = e_0\partial_{ict} - \sum_k e_k\partial_k$, so that $\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Box = \partial_{ict}^2 + \Delta$, and $\partial_{ict}^2 = -\partial_t^2/c^2$. The conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), ${}^\dagger = \bar{\cdot}^{*}$ (Hermitian), and ${}^\flat = -\dagger$ (anti-Hermitian). Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value.

## The Equation and Its Operator

Write the Klein–Gordon equation in biquaternion form as

$$
\left(\tilde{\nabla}\bar{\tilde{\nabla}} - \frac{m^2c^2}{\hbar^2}\right)\tilde{\Phi} = 0,
\qquad \tilde{\Phi} = \Phi_0 e_0 + \Phi_1 e_1 + \Phi_2 e_2 + \Phi_3 e_3 .
$$

The operator $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$ is a **central scalar** differential operator with real coefficients. Because $\Box$ is central and scalar, it acts on a biquaternion-valued field component by component:

$$
\Box\tilde{\Phi} = \sum_{\mu=0}^{3}(\Box\Phi_\mu)\,e_\mu .
$$

There is no term that mixes the four coefficients. Consequently the biquaternion Klein–Gordon equation on $\mathbb{B}$-valued $\tilde{\Phi}$ is **four decoupled copies** of the complex scalar Klein–Gordon equation, one per coefficient. Nothing in the algebra couples them. If the intended field is a single Lorentz scalar, the right host is the center $\mathbb{C}_{\mathbb{B}}$, and then the biquaternion form and the ordinary complex form say the same thing.

The operator is nevertheless the natural object to name, because it is the composition of $\tilde{\nabla}$ with its quaternion conjugate,

$$
\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Box ,
$$

which is a genuine algebraic statement: the d'Alembertian is the **norm form** of the gradient biquaternion, exactly as $\tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ is the norm form of a biquaternion. The wave operator is the square of an element of the algebra, and the mass-shell condition below is the same norm form evaluated on the four-wavevector. That is the structural content the biquaternion writing makes visible.

## Second Order in Time and the Conjugate Pair

An equation second order in $t$ does not determine the field from its value alone: two data, $\tilde{\Phi}$ and $\partial_t\tilde{\Phi}$, are required. Equivalently, the operator $\Box - m^2c^2/\hbar^2$ has no first-order scalar square root inside the algebra, and the obstruction is elementary. Attempt the factorisation

$$
\left(\bar{\tilde{\nabla}} + \mu\right)\left(\tilde{\nabla} - \mu\right)
= \Box - \mu\bar{\tilde{\nabla}} + \mu\tilde{\nabla} - \mu^2
= \Box + 2\mu\,\boldsymbol{\nabla} - \mu^2,
\qquad \mu = \frac{mc}{\hbar},
$$

where $\boldsymbol{\nabla} = e_1\partial_x + e_2\partial_y + e_3\partial_z$ is the vector part of the gradient. The cross term $2\mu\boldsymbol{\nabla}$ is a first-order differential operator and does not vanish, and general constant biquaternion coefficients do not remove it. For constant $A$ and $B$,

$$
\left(\bar{\tilde{\nabla}} + A\right)\left(\tilde{\nabla} + B\right)
= \Box + (A + B)\,\partial_{ict} + \sum_{j=1}^{3}\left(A e_j - e_j B\right)\partial_j + AB,
$$

so cancellation of the first-order terms requires $B = -A$ together with $Ae_j + e_jA = 0$ for $j = 1, 2, 3$. An element that anticommutes with all three units $e_j$ must vanish: the condition for $j=1$ forces the $e_0$ and $e_1$ coefficients of $A$ to zero, and the conditions for $j=2$ and $j=3$ remove the remaining two coefficients. With $A = 0$ the constant term is $AB = -A^2 = 0$, which cannot equal $-\mu^2$ for $\mu \neq 0$. Hence the scalar Klein–Gordon operator does not factor into first-order scalar operators in $\mathbb{B}$.

The physical counterpart of this algebraic obstruction is the conjugate pair. The equation has real coefficients, so whenever $\tilde{\Phi}$ is a solution, so is its complex conjugate $\tilde{\Phi}^*$:

$$
\left(\Box - \mu^2\right)\tilde{\Phi} = 0
\qquad\Longrightarrow\qquad
\left(\Box - \mu^2\right)\tilde{\Phi}^* = 0 ,
$$

because $\Box$ is real and therefore commutes with ${}^*$. For the complex scalar field this is the familiar statement that $\phi$ and $\phi^*$ are independent data; the general solution is a superposition of the two frequency branches, and a complete description needs both. This conjugacy, not the sector decomposition, is what "second order" buys.

It is worth separating three operations that are easy to conflate at this point, because the rest of the article turns on keeping them apart:

- **Multiplication by the scalar imaginary $i$** is central and is a real-linear isomorphism exchanging the sectors, $i\mathbb{M}_+ = \mathbb{M}_-$ and $i\mathbb{M}_- = \mathbb{M}_+$.
- **Complex conjugation ${}^*$** acts on the coefficients and is an algebra automorphism. Because ${}^*$ commutes with ${}^\dagger$ (the two generate the Klein four-group of conjugations together with $\bar{\cdot}$), it **preserves each sector**: if $\tilde{H}^\dagger = \tilde{H}$ then $(\tilde{H}^*)^\dagger = (\tilde{H}^\dagger)^* = \tilde{H}^*$, and likewise for $\mathbb{M}_-$.
- **Hermitian conjugation ${}^\dagger$** is the conjugation whose $\pm1$ eigenspaces *define* $\mathbb{M}_\pm$; it is neither $i$-multiplication nor ${}^*$.

The distinction is concrete. Take $\tilde{\Phi} = e_0 + i e_1 \in \mathbb{M}_+$. Then

$$
\tilde{\Phi}^* = e_0 - i e_1 \in \mathbb{M}_+,
\qquad
i\tilde{\Phi} = i e_0 - e_1 \in \mathbb{M}_- ,
$$

and the two results are different elements of the algebra. Complex conjugation stays inside the sector that contains $\tilde{\Phi}$; multiplication by $i$ leaves it. So the conjugate pair $(\tilde{\Phi}, \tilde{\Phi}^*)$ does **not** realize the pair $(\mathbb{M}_+, \mathbb{M}_-)$, and the sector-exchanging operation $i$ is not the conjugation that produces the second solution.

The trap here is the sharper version of the trap in the parent article. There, the error was to conflate the central $i$ with a non-central root of $-1$ and ask a quaternion unit to play the role of the complex structure. Here the error is to conflate the central $i$ with complex conjugation: the two both involve "the imaginary," both connect the pieces of the second-order structure in a loose verbal sense, and both are written with an $i$-like symbol, but one preserves the sectors and reverses frequency while the other exchanges the sectors and preserves frequency. Reading the Klein–Gordon conjugate pair as a sector pair is precisely the conflation.

## Plane Waves and the Dispersion Relation

The plane-wave solutions are written with the four-wavevector of the read list,

$$
\tilde{K} = i\frac{\omega}{c}e_0 + \mathbf{k}\in\mathbb{M}_-,
\qquad
\tilde{X} = ict\,e_0 + \mathbf{x}\in\mathbb{M}_- ,
$$

and the phase is the scalar part of the product of the wave biquaternion with the conjugate four-position, $\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})$, the convention of the companion articles. Using $\mathbf{k}\cdot\mathbf{x} = \sum_j k_jx_j$ and $i^2 = -1$,

$$
\mathrm{Sc}\!\left(\tilde{K}\bar{\tilde{X}}\right)
= \left(i\frac{\omega}{c}\right)(ict) + \mathbf{k}\cdot\mathbf{x}
= -\omega t + \mathbf{k}\cdot\mathbf{x},
$$

which is real. A plane wave of positive frequency is $\tilde{\Phi} = \tilde{\Phi}_0\,e^{\,i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})}$ with $\omega>0$; the exponent $i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})$ is a purely imaginary central element, so the exponential is central and commutes with everything. With the exponential central, differentiation is elementary: $\partial_t\tilde{\Phi} = -i\omega\,\tilde{\Phi}$ and $\partial_{x_j}\tilde{\Phi} = ik_j\,\tilde{\Phi}$, so

$$
\Box\tilde{\Phi} = \left(-\frac{1}{c^2}(-i\omega)^2 + (i\mathbf{k})^2\right)\tilde{\Phi}
= \left(\frac{\omega^2}{c^2} - \mathbf{k}^2\right)\tilde{\Phi}.
$$

The Klein–Gordon equation therefore requires $\omega^2/c^2 - \mathbf{k}^2 = m^2c^2/\hbar^2$. Since the norm form of the four-wavevector is $N(\tilde{K}) = \tilde{K}\bar{\tilde{K}} = -\omega^2/c^2 + \mathbf{k}^2$, this is exactly the mass-shell condition

$$
N(\tilde{K}) = -\frac{m^2c^2}{\hbar^2}
\qquad\Longleftrightarrow\qquad
-\frac{\omega^2}{c^2} + \mathbf{k}^2 = -\frac{m^2c^2}{\hbar^2},
$$

that is,

$$
\omega^2 = c^2\mathbf{k}^2 + \frac{m^2c^4}{\hbar^2}.
$$

This is the standard relativistic dispersion relation $E^2 = \mathbf{p}^2c^2 + m^2c^4$ under $E = \hbar\omega$, $\mathbf{p} = \hbar\mathbf{k}$, and in biquaternion language it is exactly the mass-shell condition $\tilde{K}\bar{\tilde{K}} = -m^2c^2/\hbar^2$ — the norm form of the four-wavevector fixed to a negative constant, the same statement as $\tilde{P}\bar{\tilde{P}} = -m^2c^2$ for the four-momentum. The two roots

$$
\omega = \pm\sqrt{c^2\mathbf{k}^2 + m^2c^4/\hbar^2}
$$

are the two frequency branches. They are the same dispersion relation with opposite signs, not two different equations, and no choice of $\mathbf{k}$ or $m$ makes the negative root disappear.

**Case checked.** As a case chosen independently of the derivation, take dimensionless units $\hbar = 1$, $c = 2$, $m = 0.7$, $\mathbf{k} = (0.9,-0.5,0.3)$. Then $c^2\mathbf{k}^2 = 4(1.15) = 4.6$, $m^2c^4/\hbar^2 = 0.49\cdot16 = 7.84$, so $\omega^2 = 12.44$ and $\omega \approx 3.5270$. Substituting $\tilde{\Phi} = \cos(\mathbf{k}\cdot\mathbf{x}-\omega t)$ and $\cos(\mathbf{k}\cdot\mathbf{x}+\omega t)$ into $\Box\tilde{\Phi} - \mu^2\tilde{\Phi}$ by second-order finite differences on a grid with step $10^{-4}$ gives a residual of order $10^{-7}$ at random points for **both** branches, which is the discretization error $O(h^2)$ and confirms that both signs solve the equation. The check was made on a numerically chosen case and not on the special value $\mathbf{k} = 0$, where the two branches coincide up to sign and a sign error would hide.

## The Conserved Current and the Two Defects

The Klein–Gordon equation carries a conserved four-current. For a complex scalar field $\tilde{\Phi}=\phi\,e_0\in\mathbb{C}_{\mathbb{B}}$, define

$$
\tilde{J} = ic\,\rho\,e_0 + \mathbf{j}\in\mathbb{M}_-,
\qquad
\rho = \frac{i\hbar}{2mc^2}\left(\tilde{\Phi}^*\partial_t\tilde{\Phi} - \tilde{\Phi}\,\partial_t\tilde{\Phi}^*\right),
\qquad
\mathbf{j} = -\frac{i\hbar}{2m}\left(\tilde{\Phi}^*\nabla\tilde{\Phi} - \tilde{\Phi}\,\nabla\tilde{\Phi}^*\right).
$$

The current lies in the material sector, its imaginary scalar component being $ic\rho$ and its vector component $\mathbf{j}$, exactly as the four-current of relativistic mechanics does. Conservation takes the framework form

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = 0,
\qquad\text{equivalently}\qquad
\partial_t\rho + \nabla\cdot\mathbf{j} = 0 .
$$

Verifying the equivalence is a one-line computation: $\bar{\tilde{\nabla}}\tilde{J}$ has scalar part $\partial_{ict}(ic\rho) - \mathrm{Sc}(\boldsymbol{\nabla}\mathbf{j}) = \partial_t\rho + \nabla\cdot\mathbf{j}$, and the vector part is not set to zero. So the continuity equation is the scalar projection of the biquaternion conservation law, and it holds; numerically, on the plane wave used above the combination $\partial_t\rho + \nabla\cdot\mathbf{j}$ vanishes to finite-difference accuracy ($\sim10^{-6}$).

The current is conserved, but its time component $\rho$ is **not positive definite**. For the positive-frequency plane wave $\tilde{\Phi}=N e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ with $\omega>0$, direct substitution gives

$$
\rho = \frac{\hbar\omega}{mc^2}\,|N|^2 > 0 ,
$$

while for the negative-frequency branch, that is the same expression with $\omega<0$, the same computation gives $\rho<0$ with the same magnitude. The two branches therefore carry charges of opposite sign, and $\rho$ cannot be read as a probability density. This is the negative-probability problem, and it is a property of the conserved current itself, not of the notation: every step above was made from the equation and the definitions.

The second defect is that the equation is not a single-particle equation. The reason is the same one, stated more broadly: a one-particle interpretation requires a positive conserved probability and a stable notion of "the particle at a place." The Klein–Gordon field provides neither. The resolution in standard physics is to stop reading $\phi$ as a wave function and read it as a **field operator**, with $\phi$ and $\phi^*$ becoming the operators that annihilate and create the particle and the antiparticle; the conserved charge becomes the difference of particle number and antiparticle number, which may have either sign, and the negative-frequency branch is reinterpreted as the antiparticle. The biquaternion form of the equation does not change this. In particular, the current sits in $\mathbb{M}_-$ and is conserved, but the sign of its scalar component is not fixed by membership in $\mathbb{M}_-$.

## Does the Second-Order Structure Fit $\mathbb{M}_-/\mathbb{M}_+$?

Now the central question. The framework offers the decomposition $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$, and the parent article used it to organize the first-order Schrödinger equation. Do the second-order structure and its conjugate pair fit the same decomposition?

Write a solution as $\tilde{\Phi} = \tilde{\Phi}_+ + \tilde{\Phi}_-$ with $\tilde{\Phi}_\pm\in\mathbb{M}_\pm$. Since $\Box$ is central, real, and scalar, it preserves each sector:

$$
\Box\tilde{\Phi}_\pm = (\Box\tilde{\Phi})_\pm ,
$$

so $\tilde{\Phi}$ solves the Klein–Gordon equation if and only if $\tilde{\Phi}_+$ and $\tilde{\Phi}_-$ each solve it separately. There is no equation coupling the two sectors, and the decomposition is not a decomposition into interacting parts. Worse for the hoped-for reading, the two sectors are not independent: because $i$ is central and commutes with $\Box$, multiplication by $i$ maps Klein–Gordon solutions in $\mathbb{M}_+$ to Klein–Gordon solutions in $\mathbb{M}_-$,

$$
\left(\Box-\mu^2\right)\tilde{\Phi}_+ = 0
\qquad\Longrightarrow\qquad
\left(\Box-\mu^2\right)(i\tilde{\Phi}_+) = i\left(\Box-\mu^2\right)\tilde{\Phi}_+ = 0,
\qquad i\tilde{\Phi}_+\in\mathbb{M}_- .
$$

So every $\mathbb{M}_-$-valued solution is the $i$-image of an $\mathbb{M}_+$-valued one, and the two sectors host two copies of the same real solution space, exchanged by multiplication by $i$. The sector split of a Klein–Gordon field is therefore the real/imaginary-part decomposition of a complex field — the statement that a complex scalar splits into a part in the real scalar direction and a part in the imaginary scalar direction, with $i$ the map between them — and not the particle–antiparticle pairing of the previous section. The particle–antiparticle pairing is complex conjugation, which we have seen preserves both sectors, so it acts *within* a sector rather than across them.

What, then, is the doubling that the second-order structure actually needs? Two candidates are worth separating.

The first is the **Hamiltonian doubling** of the second-order equation: to write it as a first-order system one introduces the conjugate momentum, so the state becomes a pair (field, rate of change of field). This is a genuine enlargement of the state space by a factor of two, and it cannot be avoided. Its relation to the sector split is only the intertwiner of the parent article: the rate $\partial_{ict}\tilde{\Phi}\in\mathbb{M}_\pm$ stays in the sector of $\tilde{\Phi}$, while $i\partial_{ict}\tilde{\Phi}$ moves to the other sector. That is the observable/generator structure of the Schrödinger article reappearing — the central $i$ converts a Hermitian object into a generator in the material sector — and it does not produce a particle–antiparticle pair. It is the same $i$-intertwiner, not a new algebraic ingredient.

The second candidate is the one the Dirac article already identifies: the **spinor-module doubling**. The scalar Klein–Gordon operator has no scalar square root (the cross term above), but it does have a first-order *spinor* square root, the biquaternion Dirac operator $\tilde{\nabla}$, whose mass term is the linear coupling of the two chiralities, $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$.

The square root acts on the minimal left ideal $\mathbb{B}\tilde{P}\cong\mathbb{C}^2$ and on its complex conjugate, whose direct sum is the four-component Dirac spinor — two spin states for the particle and two for the antiparticle. *This* is the doubling that the second-order structure needs, and it is a representation-theoretic doubling of a complex module, not the real vector-space decomposition $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$.

So the verdict on the framework's own question is the following. The second-order Klein–Gordon structure does **not** fit the $\mathbb{M}_-/\mathbb{M}_+$ split naturally: the split decomposes the field into two $i$-related copies of the same equation, while the conjugacy that the equation actually requires — and the spinor structure that its first-order square root requires — live elsewhere. A doubling is needed, and it is not the sector doubling. Whether one says the algebra "supplies" that doubling is partly a matter of bookkeeping: $\mathbb{B}$ does contain the minimal left ideal and its conjugate, so the spinor doubling is available in its representation theory, but it is not visible in the real fixed-point decomposition that the framework calls material and informational. For the scalar equation itself, the biquaternion form is a relabelling.

## The Non-Relativistic Limit

There is a check that the biquaternion Klein–Gordon equation is consistent with the parent article rather than merely alongside it. For the central field, remove the rest energy by the substitution

$$
\tilde{\Phi} = e^{-imc^2t/\hbar}\,\tilde{\psi},
$$

with the exponential central. Substituting into $\left(\Box-\mu^2\right)\tilde{\Phi}=0$ and using $\partial_t^2\!\left(e^{-imc^2t/\hbar}\tilde{\psi}\right) = e^{-imc^2t/\hbar}\left(\partial_t^2\tilde{\psi} - 2i\frac{mc^2}{\hbar}\partial_t\tilde{\psi} - \frac{m^2c^4}{\hbar^2}\tilde{\psi}\right)$ gives

$$
\frac{1}{c^2}\partial_t^2\tilde{\psi} - \frac{2im}{\hbar}\partial_t\tilde{\psi} - \Delta\tilde{\psi} = 0 ,
$$

in which the two mass terms have cancelled exactly. Dropping the term $\partial_t^2\tilde{\psi}/c^2$, which is small when the field varies slowly on the time scale $\hbar/(mc^2)$, leaves

$$
i\hbar\,\partial_t\tilde{\psi} = -\frac{\hbar^2}{2m}\Delta\tilde{\psi},
$$

the free Schrödinger equation. Its Hamiltonian $-\hbar^2\Delta/2m$ is a real scalar, hence an element of $\mathbb{M}_+$, and the equation is of the parent article's form $i\hbar\,\partial_t\tilde{\psi} = \tilde{H}\tilde{\psi}$ with the same central scalar imaginary $i$. The two articles use the same complex structure, as they must. The check is independent of the plane-wave route: expanding $\omega = mc^2/\hbar + \Omega$ in the dispersion relation gives $\hbar\Omega \to \hbar^2\mathbf{k}^2/2m$ as $c\to\infty$, which I verified numerically for increasing $c$. What the limit shows is that the biquaternion Klein–Gordon equation does not introduce a second, competing imaginary unit; the $i$ of the parent is the $i$ here.

One qualification belongs with the limit. The field reduced here is a **scalar**, so the limit lands on the scalar Schrödinger equation, which is the spin-$0$ special case of the parent article's two-component spinor equation, not an identification of the full spinor module. The scalar sector is consistent with the parent, not identical to it.

## What the Form Adds and What It Relabels

Stated plainly, the biquaternion form of the scalar Klein–Gordon equation is a **relabelling** for the equation itself. The operator $\Box$ is central and scalar, the equation decouples into independent scalar equations, the dispersion relation is the textbook one, and no prediction is added. The field, the current, and the two defects are the standard ones.

Three things are genuinely rearranged rather than renamed.

1. **The wave operator is a norm form.** $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ is the norm form of the gradient biquaternion, and the mass-shell condition is the same norm form on the four-wavevector, $\tilde{K}\bar{\tilde{K}} = -m^2c^2/\hbar^2$. The equation and its on-shell condition are both statements about $N(\cdot)$.

2. **The current's home is explicit.** The conserved four-current lies in $\mathbb{M}_-$, and conservation is $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})=0$, the same scalar pairing that appears in the framework's $2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ trace formula. The continuity equation is a scalar projection of a stronger biquaternion equation.

3. **The two "imaginary" operations are separated.** Making the Klein–Gordon structure explicit forces the distinction between the central $i$ (sector-exchanging, frequency-preserving, the complex structure) and complex conjugation ${}^*$ (sector-preserving, frequency-reversing, the particle–antiparticle map). The framework's trap is to read the second-order conjugate pair through the sector split; writing the equations down shows the split cannot carry it.

The honest bottom line is a negative result about the framework's central structural claim in this case. The second-order relativistic equation does not organize itself by $\mathbb{M}_-/\mathbb{M}_+$; it needs the spinor doubling that the Dirac article develops, and that doubling is representation-theoretic rather than a property of the two real fixed-point subspaces. Where the sector split does appear — the $i$-intertwiner between a Hermitian object and its generator — it acts as the parent article's complex structure, and it converts the two sectors into one another rather than separating particle from antiparticle.

## Open Questions

1. **Two readings of "conjugate pair."** *Open for the author.* This article reads the conjugate pair as $(\tilde{\Phi},\tilde{\Phi}^*)$ — the particle/antiparticle pair, complex conjugation. A second reading is the Hamiltonian pair $(\tilde{\Phi},\partial_{ict}\tilde{\Phi})$ — field and conjugate momentum. The two are inequivalent, and the choice changes which part of the algebra is invoked (complex conjugation versus the $i$-intertwiner). This article takes the first reading because it is the one connected to the two physical defects, but the second is defensible and is flagged rather than decided.

2. **Would the author want a sector pairing at all?** *Open for the author.* If the intended framework claim is that $\mathbb{M}_+$ hosts $\tilde{\Phi}$ and $\mathbb{M}_-$ hosts $\tilde{\Phi}^*$, then the algebras above say this requires a convention in which complex conjugation, not Hermitian conjugation, is the sector-defining involution, and in which multiplication by $i$ does not exchange the sectors. That is a different set of fixed-point subspaces than the one the read list fixes. Adopting it would change the framework's conclusions, so it is recorded and not decided.

3. **Which first-order structure is canonical?** The scalar Klein–Gordon operator has no scalar square root in $\mathbb{B}$, but it has the spinor square root $\tilde{\nabla}$ with the linear chirality-off-diagonal mass term. Whether that is the *only* admissible first-order-isation, or whether a different one exists that stays closer to the sector split, is not settled here.

4. **The local complex structure.** The parent article leaves open whether the $i$ of the Schrödinger equation remains global when the complex structure is made local through $c=1/\sqrt{\epsilon\mu}$. The same question attaches to the Klein–Gordon imaginary unit, since the phase $i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})$ is central while $c$ is a function of position. This is inherited from the parent, not resolved here.

5. **Second quantization in the biquaternion framework.** The resolution of both defects is to quantize the field, with $\tilde{\Phi}$ and $\tilde{\Phi}^*$ becoming operators. Whether the biquaternion structure adds anything to that procedure, or is again a relabelling of the complex scalar field's second quantization, is open.

## Summary

The Klein–Gordon equation in biquaternionic form is

$$
\left(\tilde{\nabla}\bar{\tilde{\nabla}} - \frac{m^2c^2}{\hbar^2}\right)\tilde{\Phi} = 0,
\qquad
\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Box = \partial_{ict}^2 + \Delta,
$$

with $\tilde{\Phi}$ a biquaternion-valued field. Because $\Box$ is central and scalar, the equation decomposes into four decoupled scalar equations, and the biquaternion writing is for the scalar field a relabelling.

Being second order in time, the equation has two frequency branches and requires both $\tilde{\Phi}$ and $\tilde{\Phi}^*$. Its dispersion relation is $\omega^2 = c^2\mathbf{k}^2 + m^2c^4/\hbar^2$, which is the mass-shell condition $\tilde{K}\bar{\tilde{K}} = -m^2c^2/\hbar^2$, and the phase of a plane wave is the scalar part $\mathrm{Sc}(\tilde{K}\bar{\tilde{X}}) = \mathbf{k}\cdot\mathbf{x}-\omega t$. Both branches were checked on a case chosen independently of the derivation. The conserved current $\tilde{J} = ic\rho e_0 + \mathbf{j}$ lies in $\mathbb{M}_-$ and satisfies $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})=0$, but its scalar component $\rho$ has the sign of the frequency and is not positive definite; together with the absence of a one-particle interpretation, this is the two-fold defect the equation has always had, and the biquaternion notation neither removes nor disguises it.

The central structural question has a negative answer. The second-order structure does **not** fit the $\mathbb{M}_-/\mathbb{M}_+$ split naturally. Since $\Box$ is central, the split decouples the equation into two sectors hosting two copies of the same real solution space, exchanged by multiplication by $i$; the $\mathbb{M}_-$ part of a solution is the $i$-image of an $\mathbb{M}_+$ solution, so the pairing is the real/imaginary-part split of a complex field, not a conjugate pair. The conjugate pair is complex conjugation, which preserves both sectors, and the doubling the equation actually needs is the spinor-module doubling of the first-order square root $\tilde{\nabla}$, whose mass term is the linear coupling of the two chiralities. That doubling is representation-theoretic, not the real fixed-point decomposition. The non-relativistic limit recovers the parent article's free Schrödinger equation with the same central scalar imaginary $i$, so the two articles use one complex structure and no competing unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \varepsilon_{jkl}e_l$ |
| $i$ | Scalar imaginary, central, $i^2 = -e_0$ |
| $\mathbb{C}_{\mathbb{B}}$ | Complex scalar line $\operatorname{span}_{\mathbb{R}}\{e_0, ie_0\}$; the center |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material); home of the four-current $\tilde{J}$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational); home of the Hamiltonian |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace; fixed points of ${}^*$ |
| $\bar{\cdot},\;{}^*,\;{}^\dagger,\;{}^\flat$ | Quaternion, complex, Hermitian, anti-Hermitian conjugation |
| $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ | Biquaternionic gradient |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - \sum_k e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$ | d'Alembertian |
| $\tilde{\Phi}$ | Biquaternion-valued Klein–Gordon field |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | Four-position biquaternion |
| $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ | Four-wavevector biquaternion |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\tilde{K}\bar{\tilde{K}} = -m^2c^2/\hbar^2$ | Mass-shell condition |
| $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$ | Conserved four-current |
| $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J}) = 0$ | Conservation law |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (scalar pairing) |
| $\mu = mc/\hbar$ | Mass parameter |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |

## Further Reading

- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the standard treatment of the Klein–Gordon equation, its current, and its defects.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the negative-energy problem and the field-theoretic resolution.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I* (Cambridge, 1995), for the reinterpretation of $\phi$ and $\phi^*$ as particle and antiparticle field operators.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order square root of the wave operator.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra, its conjugations, and its fixed-point subspaces.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the wave equations and their spinor factorisation.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of relativistic wave equations.
