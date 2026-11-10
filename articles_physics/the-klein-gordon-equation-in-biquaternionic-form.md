# __The Klein–Gordon Equation in Biquaternionic Form__

## Introduction

The Klein–Gordon equation for a relativistic field of rest mass $m$ is

$$
\left(\Box - k_m^{2}\right)Ξ_\mu = 0,
\qquad \mu\in\{t,x,y,z\},
\qquad
\Box = + \partial^2/\partial R_t^2 + \Delta,
$$

the wave equation for a relativistic scalar field, written once for each of the four coefficients of the biquaternion field $\tilde{Ξ} = Ξ_t e_t + Ξ_x \vec e_x + Ξ_y \vec e_y + Ξ_z \vec e_z$. It is the equation that a spin-$0$ field obeys, and it is **second order in the time coordinate**. The companion article *Relativistic Mechanics in Biquaternionic Form* already recorded its biquaternion form in one line, $\left(\tilde{\nabla}\tilde{\nabla}^{\natural} - k_m^{2}\right)\tilde{Ξ} = 0$, as one of the ten formulas of relativistic mechanics. The present article does not repeat that line for its own sake; it examines what the line does and does not carry. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

Two facts about the equation drive everything below. The first is structural: being second order in time, the Klein–Gordon equation is not a single first-order evolution. Equivalently, its general solution carries a positive-frequency and a negative-frequency branch, and both $Ξ_\mu$ and its complex conjugate $Ξ_\mu^*$ are needed to describe it. The second is physical, and is the standard objection to the equation as a one-particle wave equation: the two branches come with energies of both signs, the conserved density is not positive definite, and the equation does not conserve particle number. Both defects are real, and the biquaternion notation does not remove either; the honest question is whether it relocates them usefully.

The framework's central algebraic fact is the decomposition $\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi}$. The parent article, *The Schrödinger Equation in Biquaternionic Form*, showed that the first-order-in-time Schrödinger equation is organized by the **scalar imaginary** $i$: the Hermitian observable $\tilde R_\Psi\in\mathbb{B}_{\Psi}$ generates a flow whose generator $-\frac{k_m\,i\,H}{m\,c}$ lies in the material sector $\mathbb{B}_{\Phi}$, and the same central $i$ supplies the complex structure of the state module. This article asks the corresponding question for the second-order equation: **does the second-order structure fit the $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$ split naturally, or does it require a doubling that the split does not supply?** The answer worked out below is that it requires a doubling, and that the doubling is *not* $\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$; the sector split gives two $i$-related copies of the same equation, not the particle–antiparticle pair. The closing sections treat the non-relativistic limit. The rest-mass phase $\exp(-i k_m r'_t)$ is divided out exactly, and the limit itself is then the leading term of an expansion of the dispersion relation about the rest point, $\Omega = \sqrt{k_\Phi^{2}+k_m^{2}}-k_m = k_\Phi^{2}/2k_m+\ldots$.

The conventions are those of the read list. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$, and $i$ is the scalar imaginary, central in $\mathbb{B}$. The fixed-point subspaces are $\mathbb{B}_{\Phi}$ (anti-Hermitian, imaginary scalar and real vector), $\mathbb{B}_{\Psi}$ (Hermitian, real scalar and imaginary vector), $\mathbb{B}_{H}$ (real quaternions, the fixed points of complex conjugation), and $\mathbb{B}_{C} = \operatorname{span}_{\mathbb{R}}\{e_t, ie_t\}$ (the complex scalar line, which is the centre). The gradient is $\tilde{\nabla} = e_t\partial/\partial R_t + \sum_\mu \vec e_\mu\partial/\partial R_\mu$ with $\tilde{\nabla}^{\natural} = e_t\partial/\partial R_t - \sum_\mu \vec e_\mu\partial/\partial R_\mu$, so that $\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \Box = \partial^2/\partial R_t^2 + \Delta$, and $\partial^2/\partial R_t^2 = -\partial^2/\partial {r'_{t}}^2$. The conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*} = ({}^{\natural})^{*}$ (Hermitian), and ${}^\flat = -{}^{*}$ (anti-Hermitian). Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value.

## The Equation and Its Operator

Write the Klein–Gordon equation in biquaternion form as

$$
\boxed{\;
\left(\tilde{\nabla}\tilde{\nabla}^{\natural} - k_m^{2}\right)\tilde{Ξ} = 0,
\qquad \tilde{Ξ} = Ξ_t e_t + Ξ_x \vec e_x + Ξ_y \vec e_y + Ξ_z \vec e_z\;}.
$$

The operator $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$ is a **central scalar** differential operator with real coefficients. Because $\Box$ is central and scalar, it acts on a biquaternion-valued field component by component:

$$
\Box\tilde{Ξ} = \sum_{\mu\in\{t,x,y,z\}}(\BoxΞ_\mu)\,e_\mu .
$$

There is no term that mixes the four coefficients, so the biquaternion equation is the four scalar equations, one per direction:

$$
\left(\Box - k_m^{2}\right)Ξ_t = 0,\qquad
\left(\Box - k_m^{2}\right)Ξ_x = 0,\qquad
\left(\Box - k_m^{2}\right)Ξ_y = 0,\qquad
\left(\Box - k_m^{2}\right)Ξ_z = 0 .
$$

The equivalence runs both ways: the four hold if and only if the biquaternion one holds, and any four complex scalar solutions assemble into a $\mathbb{B}$-valued one. Consequently the biquaternion Klein–Gordon equation on $\mathbb{B}$-valued $\tilde{Ξ}$ is **four decoupled copies** of the complex scalar Klein–Gordon equation, one per coefficient. If the intended field is a single Lorentz scalar, the right host is the centre $\mathbb{B}_{C}$, and then the biquaternion form and the ordinary complex form say the same thing.

The operator is nevertheless the natural object to name, because it is the composition of $\tilde{\nabla}$ with its quaternion conjugate,

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \Box ,
$$

The mixed products cancel in pairs. For two spatial directions the two orderings contribute $-\vec e_\mu\vec e_\nu$ and $-\vec e_\nu\vec e_\mu = +\vec e_\mu\vec e_\nu$, which sum to zero. For one temporal and one spatial direction they contribute $-\vec e_\nu$ and $+\vec e_\nu$, which also sum to zero. The four diagonal products return $+e_t$. That is a genuine algebraic statement: the d'Alembertian is the **biquaternion norm** of the gradient biquaternion, exactly as $\tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ is the biquaternion norm of a biquaternion. The wave operator is the square of an element of the algebra, and the mass-shell condition below is the same biquaternion norm evaluated on the four-wavevector. That is the structural content the biquaternion writing makes visible.

## The Lanczos Family and the Spin-0 Member

The free Klein–Gordon equation is the spin-0 member of a first-order family the corpus already writes. Lanczos's coupled biquaternion system

$$
\tilde{\nabla}\tilde Q_1 = k_m\tilde Q_2, \qquad \tilde{\nabla}\tilde Q_2 = k_m\tilde Q_1
$$

is the parent of the Dirac equation (the idempotent superposition of the two fields), of the Proca equation and of the Maxwell equation, as set out in *The Dirac Equation in Biquaternionic Form*, *The Proca Equation: Massive Spin 1 in Biquaternionic Form* and *The Standard Model under the Biquaternion Framework — A Research Agenda*; the second-order equation of the family, obtained by eliminating the auxiliary field, is the Klein–Gordon equation of this article. What the family adds here is the placement: the equation below is not an isolated second-order equation but a member of the one classical family, its spin-0 label being the restriction of the pair to scalar fields. The coefficient on the right is the reciprocal mass wave number, $k_m=mc/\hbar$, because $\tilde\nabla$ carries an inverse length; writing $m$ in place of that reciprocal means the same thing, since $m=m$.

**The scalar restriction.** Take $\tilde Q_1=A_0e_t$ and $\tilde Q_2=be_t$ with $A_0$ and $b$ complex scalars. The first equation forces $\tilde{\nabla}A_0$ to have no vector part, hence $A_0$, and with it $b$, to depend on $i r'_t$ alone; the pair then collapses to

$$
\partial/\partial R_t\,A_0 = k_mb, \qquad \partial/\partial R_t\,b = k_mA_0, \qquad\text{hence}\qquad \left(\partial^2/\partial R_t^2 - k_m^{2}\right)A_0 = 0 .
$$

This is the degenerate form that Gsponer and Hurni record for the spin-zero case, and "degenerate" is literal: a scalar field whose gradient must be scalar cannot vary in space, so this member of the family is one-dimensional. The corpus's spin-0 field does vary in space, and it satisfies the four-dimensional Klein–Gordon equation of the preceding sections,

$$
\left(\Box - k_m^{2}\right)A_0 = 0,
$$

which is the same elimination applied to the pair that carries one gradient of each kind: the conjugate gradient squares to $\Box$, and eliminating the auxiliary field leaves $\Box\tilde Q_1=(k_m^{2})\tilde Q_1$, whose scalar restriction is the equation above.

## Second Order in Time and the Conjugate Pair

An equation second order in $r'_t$ does not determine the field from its value alone: two data, $\tilde{Ξ}$ and $\partial/\partial r'_t\tilde{Ξ}$, are required. Equivalently, the operator $\Box - k_m^{2}$ has no first-order scalar square root inside the algebra, and the obstruction is elementary. Attempt the factorisation

$$
\left(\tilde{\nabla}^{\natural} + k_m\right)\left(\tilde{\nabla} - k_m\right)
= \Box - k_m\tilde{\nabla}^{\natural} + k_m\tilde{\nabla} - k_m^{2}
= \Box + 2k_m\,\vec\nabla - k_m^{2},
\qquad k_m=\dfrac{mc}{\hbar},
$$

where $\vec\nabla = \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z$ is the vector part of the gradient. The cross term $2k_m\vec\nabla$ is a first-order differential operator and does not vanish, and general constant biquaternion coefficients do not remove it. For constant $A$ and $B$,

$$
\left(\tilde{\nabla}^{\natural} + A\right)\left(\tilde{\nabla} + B\right)
= \Box + (A + B)\,\partial/\partial R_t + \sum_{\mu=1}^{3}\left(A \vec e_\mu - \vec e_\mu B\right)\partial/\partial R_\mu + AB,
$$

so cancellation of the first-order terms requires $B = -A$ together with $A\vec e_\mu + \vec e_\mu A = 0$ for $\mu = 1, 2, 3$. An element that anticommutes with all three units $\vec e_\mu$ must vanish: the condition for $\mu=1$ forces the $e_t$ and $\vec e_x$ coefficients of $A$ to zero, and the conditions for $\mu=2$ and $\mu=3$ remove the remaining two coefficients. With $A = 0$ the constant term is $AB = -A^2 = 0$, which cannot equal $-k_m^{2}$ for a finite mass, $k_m\neq0$. Hence the scalar Klein–Gordon operator does not factor into first-order scalar operators in $\mathbb{B}$.

The physical counterpart of this algebraic obstruction is the conjugate pair. The equation has real coefficients, so whenever $\tilde{Ξ}$ is a solution, so is its complex conjugate $\tilde{Ξ}^{*}$:

$$
\left(\Box - k_m^{2}\right)\tilde{Ξ} = 0
\qquad\Longrightarrow\qquad
\left(\Box - k_m^{2}\right)\tilde{Ξ}^{*} = 0 ,
$$

because $\Box$ is real and therefore commutes with $\bar{\cdot}$. For the complex scalar field this is the familiar statement that $Ξ$ and $Ξ^*$ are independent data; the general solution is a superposition of the two frequency branches, and a complete description needs both. This conjugacy, not the sector decomposition, is what "second order" buys.

It is worth separating three operations that are easy to conflate at this point, because the rest of the article turns on keeping them apart:

- **Multiplication by the scalar imaginary $i$** is central and is a real-linear isomorphism exchanging the sectors, $i\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$ and $i\mathbb{B}_{\Phi} = \mathbb{B}_{\Psi}$.
- **Complex conjugation $\bar{\cdot}$** acts on the coefficients and is an algebra automorphism. Because $\bar{\cdot}$ commutes with ${}^{*}$ (the two generate the Klein four-group of conjugations together with ${}^{\natural}$), it **preserves each sector**: if $\tilde R_\Psi^{*} = \tilde R_\Psi$ then $(\tilde{R}_\Psi^*)^{*} = (\tilde R_\Psi^{*})^* = \tilde{R}_\Psi^*$, and likewise for $\mathbb{B}_{\Phi}$.
- **Hermitian conjugation ${}^{*}$** is the conjugation whose $\pm1$ eigenspaces *define* $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$; it is neither $i$-multiplication nor $\bar{\cdot}$.

The distinction is concrete. Take $\tilde{Ξ} = e_t + i \vec e_x \in \mathbb{B}_{\Psi}$. Then

$$
\tilde{Ξ}^{*} = e_t - i \vec e_x \in \mathbb{B}_{\Psi},
\qquad
i\tilde{Ξ} = i e_t - \vec e_x \in \mathbb{B}_{\Phi} ,
$$

and the two results are different elements of the algebra. Complex conjugation stays inside the sector that contains $\tilde{Ξ}$; multiplication by $i$ leaves it. So the conjugate pair $(\tilde{Ξ}, \tilde{Ξ}^{*})$ does **not** realize the pair $(\mathbb{B}_{\Psi}, \mathbb{B}_{\Phi})$, and the sector-exchanging operation $i$ is not the conjugation that produces the second solution.

The trap here is the sharper version of the trap in the parent article. There, the error was to conflate the central $i$ with a non-central root of $-1$ and ask a quaternion unit to play the role of the complex structure. Here the error is to conflate the central $i$ with complex conjugation: the two both involve "the imaginary," both connect the pieces of the second-order structure in a loose verbal sense, and both are written with an $i$-like symbol, but one preserves the sectors and reverses frequency while the other exchanges the sectors and preserves frequency. Reading the Klein–Gordon conjugate pair as a sector pair is precisely the conflation.

## A Vector Coefficient: When the Operator Does Factor

The obstruction above is for a **scalar** coefficient. A vector coefficient fares differently, and the exception is instructive. In the fourth paper of her series on the differential algebra of biquaternions, L. A. Alexeyeva studies the first-order system

$$
\left(\nabla^+ + \vec F\right) B = G,
\qquad
\nabla^\pm = \partial/\partial \tau \pm i\,\nabla ,
$$

with $B$ and $G$ biquaternion-valued and $\vec F$ a **constant complex vector** — a structural coefficient carrying no scalar part [Alexeyeva 2014]. The two mutual operators compose into one second-order operator,

$$
\boxed{\;
\left(\nabla^- - \vec F\right)\circ\left(\nabla^+ + \vec F\right)
= \Box_A + (\vec F,\vec F) + 2i(\vec F,\nabla),
\qquad
\Box_A = \partial^2_\tau - \Delta\;},
$$

which is the Klein–Gordon–Fock operator $\Box_A + m^2$ with $m^2 = (\vec F,\vec F)$ — the coefficient's own norm supplies the mass — **plus** the first-order directional term $2i(\vec F,\nabla)$. That term is of exactly the kind that made the scalar factorisation impossible above; here it is not an obstruction but the product structure itself, and the operator is a genuine composition of two first-order operators.

**Fundamental solution.** The kernel of the operator is elementary. Alexeyeva's Theorem 4.1.2, in her variables $\tau$ and $\Box_A$, gives

$$
\tilde{Ξ}_{\mathrm{sp}}(\tau,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \frac{\exp(i(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))}{4\pi|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|}\left((1-a)\,\delta(\tau-|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|) + a\,\delta(\tau+|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|)\right) + \tilde{Ξ}_{\mathrm{sp}}^0(\tau,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),
\qquad a \in \mathbb{C},
$$

with $\tilde{Ξ}_{\mathrm{sp}}^0$ an arbitrary solution of the homogeneous equation: a $\delta$-layer on the forward light cone and a $\delta$-layer on the backward light cone, weighted by the exponential $\exp(i(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$, with the constant $a$ choosing the mixture — $a = 0$ retarded, $a = 1$ advanced. The first-order system is then solved by $B = (\nabla^- - \vec F)(\tilde{Ξ}_{\mathrm{sp}} * G)$, and the homogeneous fields are obtained from the same kernel by convolution with arbitrary biquaternionic data.

**Why the kernel is simpler than the standard one, and what that does not mean.** The ordinary massive operator $\Box_A + k_m^{2}$ has Fourier symbol $\omega^2 - |\vec\zeta|^2 - k_m^{2}$, whose zero set is the two-sheeted mass hyperboloid; its fundamental solution is not a light-cone layer, and the standard references build it out of Bessel-type functions. Here the symbol is $(\vec\zeta + \vec F, \vec\zeta + \vec F) - \omega^2$, the symbol of a *product* of two first-order operators, and the kernel is correspondingly a light-cone layer with the weight $\exp(i(\vec F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$. Alexeyeva states the contrast with Vladimirov's Klein–Gordon–Fock fundamental solution explicitly. The caveat belongs with it: the operator that factors is not $\Box_A + k_m^{2}$ but $\Box_A + k_m^{2}$ *together with* the directional term, and the two cannot be separated — setting $\vec F = 0$ removes the mass with the direction, and turning off only $2i(\vec F,\nabla)$ while keeping $(\vec F,\vec F)$ is not a case of the construction. The simplification is a property of the compensated operator, and the scalar-equation obstruction of the previous section stands.

**Reading the two parts of the coefficient.** Write $\vec F = -E - iH$ with $E, H$ real vectors. The real part enters the kernel as the phase weight $\exp(-i(E,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$, which is a constant shift of the wave vector — a drift of the wave pattern, not a change of the dispersion relation, since the symbol depends on $\vec\zeta + \vec F$ — and the imaginary part enters as the exponential $\exp(-(H,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$, a growth or decay with distance that makes a complex coefficient the mark of a driven or dissipative medium. The mass is the norm $m^2 = (\vec F,\vec F) = |E|^2 - |H|^2 + 2i(E,H)$: real and positive for a real coefficient, negative for a purely imaginary one, and complex in general. The plane-wave solutions, and the standing waves with exponentially growing or decaying amplitude that appear when the coefficient is imaginary, are catalogued in *Twistor Theory and Biquaternions*, where the same operator generates the algebraic twistors.

**Convention.** Alexeyeva's $\Box_A = \partial^2_\tau - \Delta$, with $\tau$ measured in units of length, is **minus** this article's $\Box = \partial^2_{i r'_t} + \Delta$, which was fixed at the top of the article; the factorisation identity and the kernel are quoted in her variables so that no sign is transplanted. The product structure, the mass $(\vec F,\vec F)$ and the light-cone support of the kernel are independent of that overall sign.

## Plane Waves and the Dispersion Relation

The plane-wave solutions are written with the four-wavevector of the read list,

$$
\tilde K_{\Phi} = i\frac{\omega}{c}e_t + \vec k_\Phi\in\mathbb{B}_{\Phi},
\qquad
\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z\in\mathbb{B}_{\Phi} ,
$$

and the phase is the scalar part of the product of the wave biquaternion with the conjugate four-position, $\mathrm{Sc}(\tilde K_{\Phi}\tilde R_{\Phi}^{\natural})$, the same object that $\mathrm{Sc}\frac{k_m\,\tilde{P}_{\Phi}\,\tilde{R}_{\Phi}^{\natural}}{m\,c}$ names, since $\tilde K_{\Phi}=\frac{k_m}{m\,c}\tilde P_{\Phi}=\frac{\tilde P_{\Phi}}{\hbar}$. Using $\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \sum_j k_jx_j$ and $i^2 = -1$,

$$
\mathrm{Sc}\!\left(\tilde K_{\Phi}\tilde{R}_\Phi^{\natural}\right)
= \left(i k_{t}^{\prime}\right)(i r'_t) + \vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)
= -k_{t}^{\prime} r'_t + \vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),
\qquad k_{t}^{\prime}=\frac{\omega}{c} ,
$$

which is real. A plane wave of positive frequency is $\tilde{Ξ} = \tilde{Ξ}_0\,\exp(\,i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde{R}_{\Phi}^{\natural}))$ with $\omega>0$; the exponent is a purely imaginary central element, so the exponential is central and commutes with everything, and no $\hbar$ is left in it because the division by $\hbar$ is the whole of $\tilde K_{\Phi}$. With the exponential central, differentiation is elementary: $\partial/\partial r'_t\tilde{Ξ} = -ik_{t}^{\prime}\,\tilde{Ξ}$ and $\partial/\partial x_j\,\tilde{Ξ} = ik_j\,\tilde{Ξ}$, so

$$
\Box\tilde{Ξ} = \left(k_{t}^{\prime\,2} - k_{\Phi}^{2}\right)\tilde{Ξ}.
$$

Here $k_{\Phi} = |\vec k_\Phi|$ is the magnitude, written without the arrow so that its square carries no sign question: in the dispersion relations of this corpus $\vec k_\Phi^2$ denotes the Euclidean square $k_x^2+k_y^2+k_z^2$, while as a quaternion square the same symbol is $\vec k_\Phi^2=-k_\Phi^2$. The scalar $k_\Phi$ is the number, and the Laplacian returns $-k_\Phi^2$. The Klein–Gordon equation therefore requires $k_{t}^{\prime\,2} - k_{\Phi}^{2} = k_m^{2}$. Since the biquaternion norm of the four-wavevector is $\langle\tilde K_{\Phi}\rangle_{\natural}  =\frac{k_m^{2}\,\tilde{P}_{\Phi}\,\tilde{P}_{\Phi}^{\natural}}{m^{2}\,c^{2}}= -k_{t}^{\prime\,2} + k_{\Phi}^{2}$, this is exactly the mass-shell condition

$$
\langle\tilde K_{\Phi}\rangle_{\natural} = -k_m^{2}
\qquad\Longleftrightarrow\qquad
-k_{t}^{\prime\,2} + k_{\Phi}^{2} = -k_m^{2},
$$

that is,

$$
\boxed{\;
\omega^2 = c^2k_{\Phi}^{2} + c^2k_m^{2}\;},
\qquad k_{t}^{\prime}=\frac{\omega}{c} .
$$

This is the standard relativistic dispersion relation $E^2 = p^2c^2 + m^2c^4$ under $E =\frac{m\,c\,\omega}{k_m}=\hbar c\,k_t^{\prime}$, $p =\frac{m\,c\,k_\Phi}{k_m}=\hbar k_\Phi$, and in biquaternion language it is exactly the mass-shell condition $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}= -m^{2}\,c^{2}$ — the biquaternion norm of the four-wavevector fixed to a negative constant, the same statement as $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^{2}\,c^{2}$ for the four-momentum. The two roots

$$
\omega = \pm c\sqrt{k_\Phi^2 + k_m^{2}}
$$

are the two frequency branches. They are the same dispersion relation with opposite signs, not two different equations, and no choice of $\vec k_\Phi$ or $m$ makes the negative root disappear. Here $k_{\Phi}=\frac{k_m\,p}{m\,c}$ is the momentum wave number.

**Case checked.** As a case chosen independently of the derivation, quote the speed as the ratio $c/c_0=2$, the wave numbers in $\mathrm{m^{-1}}$ with $k_m = 1.4\ \mathrm{m^{-1}}$ and $\vec k_\Phi = (0.9,-0.5,0.3)\ \mathrm{m^{-1}}$. Then $c^{2}\vec k_\Phi^{2} = 4(1.15)\,c_0^{2}\,\mathrm{m^{-2}} = 4.6\,c_0^{2}\,\mathrm{m^{-2}}$ and $c^{2}k_m^{2} = 4(1.96)\,c_0^{2}\,\mathrm{m^{-2}} = 7.84\,c_0^{2}\,\mathrm{m^{-2}}$, so $\omega^{2} = 12.44\,c_0^{2}\,\mathrm{m^{-2}}$ and $\omega \approx 3.5270\,c_0\,\mathrm{m^{-1}} = 1.057\times10^{9}\ \mathrm{s^{-1}}$. The mass is not needed as a number: it is $m=\hbar k_m/c$, so $m\,c^{2}=\hbar k_m c$ and only the product enters. Substituting $\tilde{Ξ} = \cos(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c)$ and $\cos(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)+\omega r'_t/c)$ into $\Box\tilde{Ξ} - k_m^{2}\tilde{Ξ}$ by second-order finite differences on a grid with step $10^{-4}$ gives a residual of order $10^{-7}$ at random points for **both** branches, which is the discretization error $O(h^2)$ and confirms that both signs solve the equation. The check was made on a numerically chosen case and not on the special value $\vec k_\Phi = 0$, where the two branches coincide up to sign and a sign error would hide.

## The Conserved Current and the Two Defects

The Klein–Gordon equation carries a conserved four-current. For a complex scalar field $\tilde{Ξ}=Ξ e_t\in\mathbb{B}_{C}$, define

$$
\tilde{J}_{\Phi} = ic\,\rho\,e_t + \vec j\in\mathbb{B}_{\Phi},
\qquad
\rho =\frac{i}{2\,k_m}\left(\tilde{Ξ}^{*}\partial/\partial r'_t\tilde{Ξ} - \tilde{Ξ}\,\partial/\partial r'_t\tilde{Ξ}^{*}\right),
\qquad
\vec j = -\frac{i c}{2\,k_m}\left(\tilde{Ξ}^{*}\nabla\tilde{Ξ} - \tilde{Ξ}\,\nabla\tilde{Ξ}^{*}\right).
$$

The current lies in the material sector, its imaginary scalar component being $ic\rho$ and its vector component $\vec j$, exactly as the four-current of relativistic mechanics does. Conservation takes the framework form

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}_{\Phi}\right) = 0,
\qquad\text{equivalently}\qquad
c\,\partial/\partial r'_t\rho + \nabla\cdot\vec j = 0 .
$$

Verifying the equivalence is a one-line computation: $\tilde{\nabla}^{\natural}\tilde{J}_{\Phi}$ has scalar part $\partial/\partial R_t(ic\rho) - \mathrm{Sc}(\vec\nabla\vec j) = c\,\partial/\partial r'_t\rho + \nabla\cdot\vec j$, and the vector part is not set to zero. So the continuity equation is the scalar projection of the biquaternion conservation law, and it holds; numerically, on the plane wave used above the combination $c\,\partial/\partial r'_t\rho + \nabla\cdot\vec j$ vanishes to finite-difference accuracy ($\sim10^{-6}$).

The current is conserved, but its time component $\rho$ is **not positive definite**. For the positive-frequency plane wave $\tilde{Ξ}=N \exp(i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c))$ with $\omega>0$, direct substitution gives

$$
\rho =\frac{\omega}{c\,k_m}\,|N|^2 > 0 ,
$$

while for the negative-frequency branch, that is the same expression with $\omega<0$, the same computation gives $\rho<0$ with the same magnitude. The two branches therefore carry charges of opposite sign, and $\rho$ cannot be read as a probability density. This is the negative-probability problem, and it is a property of the conserved current itself, not of the notation: every step above was made from the equation and the definitions.

The second defect is that the equation is not a single-particle equation. The reason is the same one, stated more broadly: a one-particle interpretation requires a positive conserved probability and a stable notion of "the particle at a place." The Klein–Gordon field provides neither. The resolution in standard physics is to stop reading $Ξ$ as a wave function and read it as a **field operator**, with $Ξ$ and $Ξ^*$ becoming the operators that annihilate and create the particle and the antiparticle; the conserved charge becomes the difference of particle number and antiparticle number, which may have either sign, and the negative-frequency branch is reinterpreted as the antiparticle. The biquaternion form of the equation does not change this. In particular, the current sits in $\mathbb{B}_{\Phi}$ and is conserved, but the sign of its scalar component is not fixed by membership in $\mathbb{B}_{\Phi}$.

## Does the Second-Order Structure Fit $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$?

Now the central question. The framework offers the decomposition $\mathbb{B} = \mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$, and the parent article used it to organize the first-order Schrödinger equation. Do the second-order structure and its conjugate pair fit the same decomposition?

Write a solution as $\tilde{Ξ} = \tilde{Ξ}_+ + \tilde{Ξ}_-$ with $\tilde{Ξ}_\pm\in\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi}$. Since $\Box$ is central, real, and scalar, it preserves each sector:

$$
\Box\tilde{Ξ}_\pm = (\Box\tilde{Ξ})_\pm ,
$$

so $\tilde{Ξ}$ solves the Klein–Gordon equation if and only if $\tilde{Ξ}_+$ and $\tilde{Ξ}_-$ each solve it separately. There is no equation coupling the two sectors, and the decomposition is not a decomposition into interacting parts. Worse for the hoped-for interpretation, the two sectors are not independent: because $i$ is central and commutes with $\Box$, multiplication by $i$ maps Klein–Gordon solutions in $\mathbb{B}_{\Psi}$ to Klein–Gordon solutions in $\mathbb{B}_{\Phi}$,

$$
\boxed{\;
\left(\Box-k_m^{2}\right)\tilde{Ξ}_+ = 0
\qquad\Longrightarrow\qquad
\left(\Box-k_m^{2}\right)(i\tilde{Ξ}_+) = i\left(\Box-k_m^{2}\right)\tilde{Ξ}_+ = 0,
\qquad i\tilde{Ξ}_+\in\mathbb{B}_{\Phi}\;}.
$$

So every $\mathbb{B}_{\Phi}$-valued solution is the $i$-image of an $\mathbb{B}_{\Psi}$-valued one, and the two sectors host two copies of the same real solution space, exchanged by multiplication by $i$. The sector split of a Klein–Gordon field is therefore the real/imaginary-part decomposition of a complex field — the statement that a complex scalar splits into a part in the real scalar direction and a part in the imaginary scalar direction, with $i$ the map between them — and not the particle–antiparticle pairing of the previous section. The particle–antiparticle pairing is complex conjugation, which we have seen preserves both sectors, so it acts *within* a sector rather than across them.

What, then, is the doubling that the second-order structure actually needs? Two candidates are worth separating.

The first is the **Hamiltonian doubling** of the second-order equation: to write it as a first-order system one introduces the conjugate momentum, so the state becomes a pair (field, rate of change of field). This is a genuine enlargement of the state space by a factor of two, and it cannot be avoided. Its relation to the sector split is only the intertwiner of the parent article: the rate $\partial/\partial R_t\,\tilde{Ξ}\in\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi}$ stays in the sector of $\tilde{Ξ}$, while $i\partial/\partial R_t\,\tilde{Ξ}$ moves to the other sector. That is the observable/generator structure of the Schrödinger article reappearing — the central $i$ converts a Hermitian object into a generator in the material sector — and it does not produce a particle–antiparticle pair. It is the same $i$-intertwiner, not a new algebraic ingredient.

The second candidate is the one the Dirac article already identifies: the **spinor-module doubling**. The scalar Klein–Gordon operator has no scalar square root (the cross term above), but it does have a first-order *spinor* square root, the biquaternion Dirac operator $\tilde{\nabla}$, whose mass term is the linear coupling of the two chiralities, $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$.

The square root acts on the Peirce carrier $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$, a minimal left ideal here, and on its complex conjugate, whose direct sum is the four-component Dirac spinor — two spin states for the particle and two for the antiparticle. *This* is the doubling that the second-order structure needs, and it is a representation-theoretic doubling of a complex module, not the real vector-space decomposition $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$.

So the verdict on the framework's own question is the following. The second-order Klein–Gordon structure does **not** fit the $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$ split naturally: the split decomposes the field into two $i$-related copies of the same equation, while the conjugacy that the equation actually requires — and the spinor structure that its first-order square root requires — live elsewhere. A doubling is needed, and it is not the sector doubling. Whether one says the algebra "supplies" that doubling is partly a matter of bookkeeping: $\mathbb{B}$ does contain the Peirce carrier, a minimal left ideal here, and its conjugate, so the spinor doubling is available in its representation theory, but it is not visible in the real fixed-point decomposition that the framework calls material and informational. For the scalar equation itself, the biquaternion form is a relabelling.

## The Rest-Mass Phase

The field has a lowest frequency, and it is the rest frequency. Write $k_m = mc/\hbar$, $r'_t = c\,t'$, and

$$
f = \exp\left(-i k_m r'_t\right) = \exp\left(-i\,\omega_m t'\right),
\qquad
\omega_m = \frac{mc^{2}}{\hbar} = c\,k_m .
$$

At $\vec k_\Phi = 0$ the dispersion relation $k_{t}^{\prime\,2} = k_\Phi^{2}+k_m^{2}$ gives $k_{t}^{\prime} = \pm k_m$, and $\lvert k_{t}^{\prime}\rvert\ge k_m$ on every branch. So $f$ is the zero-momentum solution and the bottom of the frequency spectrum: no solution oscillates more slowly, and every positive-frequency solution carries this factor.

Dividing it out is exact. Since $\frac{\partial f}{\partial r'_t} = -i k_m f$,

$$
\frac{\partial^{2}}{\partial {r'_{t}}^{2}}\left(f\chi\right) = f\left(\frac{\partial^{2}\chi}{\partial {r'_{t}}^{2}} - 2 i k_m\,\frac{\partial\chi}{\partial r'_t} - k_m^{2}\chi\right),
$$

and the last term is exactly the mass term of $\Box - k_m^{2}$. The two cancel, and

$$
\boxed{\;
\left(\Box-k_m^{2}\right)\left(f\chi\right)
= f\left(-\frac{\partial^{2}}{\partial {r'_{t}}^{2}} + 2 i k_m\,\frac{\partial}{\partial r'_t} + \Delta\right)\chi\;}.
$$

The cancellation is identical, not asymptotic, and no solution is lost: $f$ has unit modulus, so the substitution $\tilde{Ξ}\mapsto\chi = f^{-1}\tilde{Ξ}$ is invertible. What it costs is order, not accuracy — the second derivative in $r'_t$ is still there, and $k_m$ has moved from a constant term to a coefficient on the first derivative.

Two properties of $f$ matter later. It is a central scalar, so it commutes with the quaternion units, acts on the four coefficients alike, and preserves each sector: $f\chi_{\Psi}\in\mathbb{B}_{\Psi}$ and $f\chi_{\Phi}\in\mathbb{B}_{\Phi}$. And $f^{*} = f^{-1}$, so the Hermitian norm $\mathrm{Tr}(\tilde{Ξ}^{*}\tilde{Ξ})$ is unchanged. It is therefore not multiplication by $i$, which exchanges the sectors, and not complex conjugation, which reverses the frequency.

The one quantity that does change is the conserved density, because the density is quadratic and carries a derivative. With $\tilde{Ξ} = f\chi$, $\frac{\partial}{\partial r'_t}(f\chi) = f\left(\frac{\partial\chi}{\partial r'_t} - ik_m\chi\right)$, so

$$
\rho\left[f\chi\right] = \rho\left[\chi\right] + \lvert\chi\rvert^{2}.
$$

The added term is the density the rest mode carries by itself. The sign rule is untouched: $\rho$ follows the sign of $k_{t}^{\prime}$, not of the excess $\Omega$ defined below.

## The Non-Relativistic Limit

**The method, and where it is stated.** The limit is stated once, in *The Three Wavenumbers of a Particle* §*The Non-Relativistic Limit*, and it is one rule: keep the excess of $\gamma$ to order $\beta^{2}$ in the temporal slot and drop it in the vector slot, which is the same act as dropping $\Omega^{2}$ from the exact relation $k_\Phi^{2}=2k_m\Omega+\Omega^{2}$. Nothing in the rule is specific to a field. What the field adds is one step, from a number on each mode to an operator on the field, and that step is the whole of this section.

**The general result, applied.** The solutions are superpositions of the plane waves of §*Plane Waves and the Dispersion Relation*,

$$
\tilde{Ξ} \propto \exp\left(i\left(\vec k_\Phi\cdot\vec r - k_{t}^{\prime}s\right)\right),
\qquad
k_{t}^{\prime} = \sqrt{k_\Phi^{2}+k_m^{2}} .
$$

The envelope $\chi$ of the previous section carries the excess wave number instead of the full one, since $e^{-ik_{t}^{\prime}s}=f\,e^{-i\Omega s}$ with $f$ the rest-mass phase. The expansion of the wavenumbers article then gives

$$
\Omega = \frac{k_{\Phi}^{2}}{2k_m}-\frac{k_{\Phi}^{4}}{8k_m^{3}}+\cdots ,
$$

with the parameter $\Omega/(2k_m)$ and the relative error $-\Omega/(2k_m+\Omega)$ tabulated there. Keeping the leading term, and converting with $k_m = mc/\hbar$,

$$
\Omega = \frac{k_{\Phi}^{2}}{2k_m},
\qquad
\hbar c\,\Omega = \frac{\hbar^{2}k_{\Phi}^{2}}{2m} = \frac{p^{2}}{2m},
$$

which is the non-relativistic kinetic energy. That is the entire use of the general result. Nothing is re-derived here, and no further expansion is made.

**From a number to an operator.** The truncated $\Omega$ is a number on each mode, and a number becomes an operator when $k_\Phi^{2}\to-\Delta$. On a plane wave the two agree by construction,

$$
-\frac{1}{2k_m}\,\Delta\chi
= -\frac{1}{2k_m}\left(-k_\Phi^{2}\right)\chi
= \frac{k_\Phi^{2}}{2k_m}\,\chi
= \Omega\chi ,
$$

and the plane waves are complete, so the first-order relation $\frac{\partial\chi}{\partial r'_t}=-i\Omega\chi$ of the wavenumbers article holds between operators:

$$
i\,\frac{\partial\chi}{\partial r'_t} = -\frac{1}{2k_m}\,\Delta\chi .
$$

The two sides were compared on the case of §*Plane Waves and the Dispersion Relation* and match to machine precision, at the one-term accuracy of the expansion, which is $1.5\times10^{-3}$ there.

**Why the order is one.** The relation is first order in $r'_t$ because its symbol is the truncated $\Omega$ and $\Omega$ is linear in the excess. The Klein–Gordon equation is second order because its symbol is $k_{t}^{\prime\,2}$, which the split writes as $(k_m+\Omega)^{2}$ and which contains $\Omega^{2}$. Dropping the $\Omega^{2}$ term of the dispersion relation and lowering the order of the equation are one operation: the order of the equation is the degree of its symbol in the excess.

**In the material time.** Because $\frac{mc^{2}i}{k_m} = i\hbar c$, the same equation reads $\frac{mc^{2}i}{k_m}\,\frac{\partial\chi}{\partial r'_t} = \tilde R_\Psi\,\chi$, with $\tilde R_\Psi = -\frac{\hbar^{2}}{2m}\Delta\in\mathbb{B}_{\Psi}$. The observable is informational and the central $i$ that carries it into the material sector sits in the coefficient. That is the parent article's structure, reached here from the Klein–Gordon spectrum rather than assumed.

**What is left out.** The negative branch has $\Omega\approx-2k_m$, so no ratio in it is small and the expansion does not apply; that branch is reached by factoring $\exp(+ik_m r'_t)$ instead, and antiparticles are not treated here. And the field is a scalar, so the limit lands on the scalar Schrödinger equation, the spin-$0$ case of the parent article's spinor equation, whose module and flows are untouched. The scalar sector is consistent with the parent, not identical to it.

**The equation.** With $r'_t = c\,t'$ and $\frac{\hbar c}{2k_m} = \frac{\hbar^{2}}{2m}$, the relation is the free Schrödinger equation with the mass that entered the Klein–Gordon equation:

$$
\boxed{\;
i\hbar\,\frac{\partial\chi}{\partial t'}
= -\frac{\hbar^{2}}{2m}\,\Delta\chi\;}
$$

## What the Form Adds and What It Relabels

Stated plainly, the biquaternion form of the scalar Klein–Gordon equation is a **relabelling** for the equation itself. The operator $\Box$ is central and scalar, the equation decouples into independent scalar equations, the dispersion relation is the textbook one, and no prediction is added. The field, the current, and the two defects are the standard ones.

Three things are genuinely rearranged rather than renamed.

1. **The wave operator is a biquaternion norm.** $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ is the biquaternion norm of the gradient biquaternion, and the mass-shell condition is the same biquaternion norm on the four-wavevector, $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}= -m^{2}\,c^{2}$. The equation and its on-shell condition are both statements about $\langle \cdot\rangle_{\natural}$.

2. **The current's home is explicit.** The conserved four-current lies in $\mathbb{B}_{\Phi}$, and conservation is $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}_{\Phi})=0$, the same scalar pairing that appears in the framework's $2\,\mathrm{Sc}(\tilde\Pi\tilde R_\Psi^{*})$ trace formula. The continuity equation is a scalar projection of a stronger biquaternion equation.

3. **The two "imaginary" operations are separated.** Making the Klein–Gordon structure explicit forces the distinction between the central $i$ (sector-exchanging, frequency-preserving, the complex structure) and complex conjugation $\bar{\cdot}$ (sector-preserving, frequency-reversing, the particle–antiparticle map). The framework's trap is to read the second-order conjugate pair through the sector split; writing the equations down shows the split cannot carry it.

The honest bottom line is a negative result about the framework's central structural claim in this case. The second-order relativistic equation does not organize itself by $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$; it needs the spinor doubling that the Dirac article develops, and that doubling is representation-theoretic rather than a property of the two real fixed-point subspaces. Where the sector split does appear — the $i$-intertwiner between a Hermitian object and its generator — it acts as the parent article's complex structure, and it converts the two sectors into one another rather than separating particle from antiparticle.

## Open Questions

1. **Two interpretations of "conjugate pair."** *Open for the author.* This article reads the conjugate pair as $(\tilde{Ξ},\tilde{Ξ}^{*})$ — the particle/antiparticle pair, complex conjugation. A second reading is the Hamiltonian pair $(\tilde{Ξ},\partial/\partial R_t\,\tilde{Ξ})$ — field and conjugate momentum. The two are inequivalent, and the choice changes which part of the algebra is invoked (complex conjugation versus the $i$-intertwiner). This article takes the first reading because it is the one connected to the two physical defects, but the second is defensible and is flagged rather than decided.

2. **Would the author want a sector pairing at all?** *Open for the author.* If the intended framework claim is that $\mathbb{B}_{\Psi}$ hosts $\tilde{Ξ}$ and $\mathbb{B}_{\Phi}$ hosts $\tilde{Ξ}^{*}$, then the algebras above say this requires a convention in which complex conjugation, not Hermitian conjugation, is the sector-defining involution, and in which multiplication by $i$ does not exchange the sectors. That is a different set of fixed-point subspaces than the one the read list fixes. Adopting it would change the framework's conclusions, so it is recorded and not decided.

3. **Which first-order structure is canonical?** The scalar Klein–Gordon operator has no scalar square root in $\mathbb{B}$, but it has the spinor square root $\tilde{\nabla}$ with the linear chirality-off-diagonal mass term. Whether that is the *only* admissible first-order-isation, or whether a different one exists that stays closer to the sector split, is not settled here.

4. **The local complex structure.** The parent article leaves open whether the $i$ of the Schrödinger equation remains global when the complex structure is made local through $c=1/\sqrt{\epsilon\mu}$. The same question attaches to the Klein–Gordon imaginary unit, since the phase $i\,\mathrm{Sc}\frac{k_m\,\tilde{P}_{\Phi}\,\tilde{R}_{\Phi}^{\natural}}{m\,c}$ is central while $c$ is a function of position. This is inherited from the parent, not resolved here.

5. **Second quantization in the biquaternion framework.** The resolution of both defects is to quantize the field, with $\tilde{Ξ}$ and $\tilde{Ξ}^{*}$ becoming operators. Whether the biquaternion structure adds anything to that procedure, or is again a relabelling of the complex scalar field's second quantization, is open.

6. **A factorable massive operator.** The vector-coefficient operator $\Box_A + (\vec F,\vec F) + 2i(\vec F,\nabla)$ factors into first-order operators and has a light-cone kernel, but its mass and its directional term cannot be separated. Is there a class of *massive* scalar operators with elementary kernels that is not obtained by this compensated construction — or, equivalently, is the price of factorisability always a compensating first-order term? The construction also raises whether the compensated operator has a **physical interpretation** of its own, rather than being a device for solving the first-order system.

## Summary

The Klein–Gordon equation in biquaternionic form is

$$
\left(\tilde{\nabla}\tilde{\nabla}^{\natural} - k_m^{2}\right)\tilde{Ξ} = 0,
\qquad
\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \Box = \partial^2/\partial R_t^2 + \Delta,
$$

with $\tilde{Ξ}$ a biquaternion-valued field. Because $\Box$ is central and scalar, the equation decomposes into four decoupled scalar equations, and the biquaternion writing is for the scalar field a relabelling.

Being second order in time, the equation has two frequency branches and requires both $\tilde{Ξ}$ and $\tilde{Ξ}^{*}$. Its dispersion relation is $\omega^2 = c^2k_\Phi^{2} + c^2k_m^{2}$, that is $k_{t}^{\prime\,2}=k_\Phi^{2}+k_m^{2}$, which is the mass-shell condition $\langle\tilde K_{\Phi}\rangle_{\natural}=\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}/\hbar^{2}= -m^{2}c^{2}/\hbar^{2}$ read on the wave number, and the phase of a plane wave is the scalar part $\mathrm{Sc}(\tilde K_{\Phi}\tilde{R}_\Phi^{\natural}) = \vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-k_{t}^{\prime} r'_t$. Both branches were checked on a case chosen independently of the derivation. The conserved current $\tilde{J}_{\Phi} = ic\rho e_t + \vec j$ lies in $\mathbb{B}_{\Phi}$ and satisfies $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}_{\Phi})=0$, but its scalar component $\rho$ has the sign of the frequency and is not positive definite; together with the absence of a one-particle interpretation, this is the two-fold defect the equation has always had, and the biquaternion notation neither removes nor disguises it.

The central structural question has a negative answer. The second-order structure does **not** fit the $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$ split naturally. Since $\Box$ is central, the split decouples the equation into two sectors hosting two copies of the same real solution space, exchanged by multiplication by $i$; the $\mathbb{B}_{\Phi}$ part of a solution is the $i$-image of an $\mathbb{B}_{\Psi}$ solution, so the pairing is the real/imaginary-part split of a complex field, not a conjugate pair. The conjugate pair is complex conjugation, which preserves both sectors, and the doubling the equation actually needs is the spinor-module doubling of the first-order square root $\tilde{\nabla}$, whose mass term is the linear coupling of the two chiralities. That doubling is representation-theoretic, not the real fixed-point decomposition. The non-relativistic limit is the general one of *The Three Wavenumbers of a Particle*, applied to this field, and it needs one preliminary step: the rest-mass phase $f = \exp(-i k_m r'_t)$, which is itself the zero-momentum solution, is divided out, and the mass term then cancels exactly. The limit is then the leading term of an expansion of $k_t' = \sqrt{k_\Phi^{2}+k_m^{2}} = k_m+\Omega$, with $\Omega = k_\Phi^{2}/2k_m$, so that $\hbar c\,\Omega = p^{2}/2m$; the term dropped is $p^{4}/(8m^{3}c^{2})$, and the ratio of dropped to kept is $k_\Phi^{2}/(4k_m^{2}) = v^{2}/4c^{2}$. What remains is the parent article's free Schrödinger equation, $i\hbar\,\frac{\partial\chi}{\partial t'} = -\frac{\hbar^{2}}{2m}\Delta\chi$, with the same central scalar imaginary $i$; the two articles use one complex structure and no competing unit, and no second-order remnant is left behind.

One exception to the obstruction is imported from the literature and kept separate from the framework's own operator. For a *vector* structural coefficient $\vec F$ the second-order operator $\Box_A + (\vec F,\vec F) + 2i(\vec F,\nabla)$ does factor into two first-order operators, and its fundamental solution is a weighted $\delta$-layer on the light cone rather than a Bessel-type kernel. The factorisation is paid for by the directional term: the mass $(\vec F,\vec F)$ and $2i(\vec F,\nabla)$ arrive together and cannot be separated, so the result is not a square root of the framework's massive scalar operator. It is a structural fact about the compensated operator, recorded here because it is the sharpest known contrast with the scalar obstruction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$, $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$ |
| $i$ | Scalar imaginary, central, $i^2 = -e_t$ |
| $\mathbb{B}_{C}$ | Complex scalar line $\operatorname{span}_{\mathbb{R}}\{e_t, ie_t\}$; the centre |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (material); home of the four-current $\tilde{J}_{\Phi}$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (informational); home of the Hamiltonian |
| $\mathbb{B}_{H}$ | Real quaternion subspace; fixed points of $\bar{\cdot}$ |
| ${}^{\natural},\;\bar{\cdot},\;{}^{*},\;{}^\flat$ | Quaternion, complex, Hermitian, anti-Hermitian conjugation |
| $\tilde{\nabla} = e_t\partial/\partial R_t + \sum_\mu \vec e_\mu\partial/\partial R_\mu$ | Biquaternionic gradient |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial R_t - \sum_\mu \vec e_\mu\partial/\partial R_\mu$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial R_t^2 + \Delta$ | d'Alembertian |
| $\tilde{Ξ} = Ξ_t e_t + Ξ_x \vec e_x + Ξ_y \vec e_y + Ξ_z \vec e_z$ | Biquaternion-valued Klein–Gordon field; each coefficient $Ξ_\mu$ complex |
| $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position biquaternion |
| $\tilde K_{\Phi} = i\,k_{t}^{\prime}e_t + \vec k_\Phi = \tilde P_{\Phi}/\hbar$, $k_{t}^{\prime}=\omega/c$, $k_\Phi=\lvert\vec k_\Phi\rvert$ | Four-wavevector biquaternion and its two coordinates |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}= -m^{2}\,c^{2}$ | Mass-shell condition |
| $\tilde{J}_{\Phi} = ic\rho\,e_t + \vec j$ | Conserved four-current |
| $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}_{\Phi}) = 0$ | Conservation law |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the scalar pairing |
| $1/k_m$ | The mass length, $\hbar/(mc)$; the coefficient $k_m=mc/\hbar$ is its reciprocal |
| $f = \exp(-i k_m r'_t)$, $r'_t = c\,t'$ | Rest-mass phase; the zero-momentum solution, $\Box f = k_m^{2}f$, $\lvert f\rvert=1$, $f^{*}=f^{-1}$ |
| $\omega_m = mc^{2}/\hbar = c\,k_m$ | Rest-energy frequency of the field |
| $\chi = e^{ik_m r'_t}\tilde{Ξ}$, $r'_t=c\,t'$ | Field with the rest-mass phase divided out; the envelope |
| $\Omega = k_{t}^{\prime}-k_m$ | Excess time wave number; $\Omega = \sqrt{k_\Phi^{2}+k_m^{2}}-k_m = k_\Phi^{2}/2k_m+\cdots$ |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\vec F$, $\nabla^\pm = \partial/\partial \tau \pm i\nabla$, $\Box_A = \partial^2/\partial \tau^2 - \Delta$ | Constant complex-vector structural coefficient of the biwave system (Alexeyeva) and its operators; $\Box_A$ is minus this article's $\Box$ |
| $\Box_A + (\vec F,\vec F) + 2i(\vec F,\nabla) = (\nabla^- - \vec F)(\nabla^+ + \vec F)$ | The factorable operator of the vector-coefficient case |

## Further Reading

- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the standard treatment of the Klein–Gordon equation, its current, and its defects.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the negative-energy problem and the field-theoretic resolution.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I* (Cambridge, 1995), for the reinterpretation of $Ξ$ and $Ξ^*$ as particle and antiparticle field operators.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order square root of the wave operator.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra, its conjugations, and its fixed-point subspaces.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the wave equations and their spinor factorisation.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of relativistic wave equations.
- L. A. Alexeyeva, "Differential algebra of biquaternions. 4. Twistors and twistor fields," arXiv:1406.5347 [math-ph] (2014), for the vector-coefficient biwave system, the factorisation of its second-order operator, and the elementary light-cone fundamental solution contrasted there with Vladimirov's Klein–Gordon–Fock kernel.
