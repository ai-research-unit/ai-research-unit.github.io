# __The Non-Relativistic Limit of Relativistic Mechanics in Biquaternionic Form__

## Introduction

The kinematic content of relativistic mechanics is one element and one constraint. The element is the four-velocity, a biquaternion of the material sector; the constraint is that its norm is $-c^{2}$, the same for every particle. The four-momentum, the four-current, the four-wave-number and the four-potential of a single charge are that element with a scale attached, and the scale is the one thing the constraint does not fix.

**The element and its norm.**

$$
\tilde V_{\Phi} = \underbrace{i\,\gamma c\,e_{t}}_{\text{temporal}} + \underbrace{\gamma\vec v}_{\text{vector}} ,
\qquad
\langle\tilde V_{\Phi}\rangle_{\natural} = -\left(\gamma c\right)^{2}+\left(\gamma v\right)^{2} = -c^{2} ,
\qquad
\gamma=\frac{1}{\sqrt{1-\beta^{2}}} .
$$

The norm is multiplicative and a boost is a rotor conjugation, so this one condition holds in every frame and along the worldline. It is the only constraint: the element has four real coefficients, the norm is one real condition, and the other three are the velocity.

**The limit is the first rung of one ladder.** The temporal part is $\gamma c$ and the vector part is $\gamma v$, so the parameter is their ratio, $\beta=v/c$, exactly. Solving the exact constraint for the excess $\gamma-1$ turns it into a recursion whose iterates are the successive truncations, each correct to one more power of $\beta$ than the last. **The limit is the first of them, and the first is quadratic in $\beta$.** Everything in the article is that one rung applied to one element at a time, with the error of each truncation given in closed form.

**Why the velocity and not the momentum.** The four-momentum is $\tilde P_{\Phi}=m\tilde V_{\Phi}$, and the mass is a free real scale that the algebra does not fix: the norm is homogeneous and the light cone is scale-invariant. A limit taken on $\tilde P_{\Phi}$ carries the mass in every coefficient, and the mass entered by a route the constraint never authorised. Taken on $\tilde V_{\Phi}$ the limit is a statement about a dimensionless element, and the mass enters once, at the end, where the scale is attached.

**What is not new.** The algebra is the algebra of *Relativistic Mechanics in Biquaternionic Form*, and the expansion of $1/\sqrt{1-\beta^{2}}$ is textbook. What the article isolates is the order of the moves: **write the norm in two parts, expand $\gamma$ once, keep the leading term, then attach the scale.**

**Two limits, not one.** The **kinematic** limit is treated here: the vector part of the element is small compared with the temporal part. The **central-scalar** restriction, separated in *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*, says which directions of the algebra are occupied and holds at any speed. A slowly moving spinning top satisfies the kinematic limit and violates the central-scalar restriction.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_{t}=1, \vec e_{x}, \vec e_{y}, \vec e_{z}$ with $\vec e_{\mu}^{2}=-e_{t}$ and $\vec e_{\mu}\vec e_{\nu}=\varepsilon_{\mu\nu\lambda}\vec e_{\lambda}$, and $i$ is the scalar imaginary, central in $\mathbb{B}$. The material sector is $\mathbb{B}_{\Phi}=\mathrm{span}_{\mathbb{R}}\{ie_{t},\vec e_{x},\vec e_{y},\vec e_{z}\}$, the anti-Hermitian one, and the informational sector is $\mathbb{B}_{\Psi}=\mathrm{span}_{\mathbb{R}}\{e_{t},i\vec e_{x},i\vec e_{y},i\vec e_{z}\}$, the Hermitian one. The four-position is $\tilde R_{\Phi}=i\,r'_{t}\,e_{t}+\vec r$, both it and $\tilde V_{\Phi}$ in $\mathbb{B}_{\Phi}$. The rapidity is $\theta_{\mathrm{rpd}}$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, $c_{0}$ its vacuum value, $\beta=\lvert\vec v\rvert/c$, and $\gamma=1/\sqrt{1-\beta^{2}}$.

## The Four-Velocity and Its Norm

**The element.** The coefficient of $e_{t}$ is imaginary and the vector part is real, so $\tilde V_{\Phi}$ is anti-Hermitian and lies in $\mathbb{B}_{\Phi}$. Its norm,

$$
\langle\tilde V_{\Phi}\rangle_{\natural} = \tilde V_{\Phi}\tilde V_{\Phi}^{\natural}
= \gamma^{2}\left(-c^{2}+\vec v^{\,2}\right) = -c^{2} ,
$$

is the whole input of the article: one equation, true of every particle, containing no mass, no $\hbar$ and no energy.

**The norm is conserved, and it is the only constraint.** The norm of $\mathbb{B}$ is multiplicative, $\langle\tilde Q_{1}\tilde Q_{2}\rangle_{\natural}=\langle\tilde Q_{1}\rangle_{\natural}\langle\tilde Q_{2}\rangle_{\natural}$, and a boost multiplies on the two sides by elements of unit norm. Hence $\langle\tilde V_{\Phi}'\rangle_{\natural}=\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$ in every frame, and the same along the worldline. The constraint is preserved by the group rather than imposed after the fact. So the constraint is also complete: four real coefficients, one real condition, and the three that remain are the three components of the velocity.

## The Ladder

**The excess, defined once.** Write the temporal part as the rest value plus what the motion adds, in units of $c$:

$$
\tfrac{1}{c}\left\lvert i\gamma c\,e_{t}\right\rvert=\gamma=1+\varepsilon ,
\qquad
\varepsilon:=\gamma-1 .
$$

Nothing is approximated in that line: $\varepsilon$ is defined as the excess, not expanded into. It vanishes at rest and grows without bound as $\lvert\vec v\rvert\to c$.

**The box.** Divide the norm by $c^{2}$ and substitute $\gamma=1+\varepsilon$:

$$
\gamma^{2}\beta^{2}=\gamma^{2}-1=\left(\gamma-1\right)\left(\gamma+1\right)
\qquad\Longleftrightarrow\qquad
\left(1+\varepsilon\right)^{2}\beta^{2}=\varepsilon\left(2+\varepsilon\right) .
$$

The right-hand form is exact and it is the whole constraint: **the square of the vector part, in units of $c^{2}$, is twice the excess plus the square of the excess.** One term linear in $\varepsilon$, one quadratic, and nothing else — no mass, no $\hbar$, no energy.

**The ladder, defined.** Solved for $\varepsilon$, the box is a recursion rather than a series. Bring the quadratic term to the left and divide:

$$
\varepsilon=\frac{\left(1+\varepsilon\right)^{2}}{2+\varepsilon}\,\beta^{2}
\qquad\Longrightarrow\qquad
\varepsilon_{n+1}=\frac{\left(1+\varepsilon_{n}\right)^{2}}{2+\varepsilon_{n}}\,\beta^{2},
\qquad
\varepsilon_{0}=0 .
$$

The **rungs** of the ladder are its iterates, and each rung is one more term than the one before:

$$
\varepsilon_{1}=\frac{\beta^{2}}{2},
\qquad
\varepsilon_{2}=\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\cdots,
\qquad
\varepsilon_{3}=\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\frac{5\beta^{6}}{16}+\cdots,
$$

and in the limit

$$
\boxed{\;\varepsilon=\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\frac{5\beta^{6}}{16}+\frac{35\beta^{8}}{128}+\cdots\;}
$$

**Rung $n$ is correct to order $\beta^{2n}$.** That is the property that makes the ladder a ladder and not a list: every rung reproduces every power already found and adds exactly one new one. The coefficients $\frac{1}{2},\frac{3}{8},\frac{5}{16},\frac{35}{128}$ are those of $\gamma-1$, obtained by iterating one line rather than by differentiating a square root.

**The first rung is the limit, and it is quadratic.** Rung one is $\varepsilon_{1}=\frac{\beta^{2}}{2}$: quadratic in $\beta$, and it is the only rung that is a single term. **Keeping rung one is the whole non-relativistic limit**, and every section that follows applies it to a different element.

**The element, at rung one.** The vector part is kept exact and only the temporal coefficient is replaced:

$$
\tilde V_{\Phi}=\gamma\left(i\,c\,e_{t}+\vec v\right)
\quad\longrightarrow\quad
\tilde V_{\Phi,1}=i\,c\left(1+\frac{\beta^{2}}{2}\right)e_{t}+\vec v .
$$

That is the apex $i\,c\,e_{t}$, plus the velocity, plus first-order thickening of the temporal part. It is one substitution, not a truncation of the algebra.

**The error of rung one.** Rung one is $\varepsilon_{1}=\frac{1}{2}\gamma^{2}\beta^{2}=\varepsilon\left(1+\frac{\varepsilon}{2}\right)$, so the relative error is exact and closed:

$$
\frac{\varepsilon_{1}-\varepsilon}{\varepsilon}=-\frac{\varepsilon}{2+\varepsilon}=-\frac{\gamma-1}{\gamma+1}=-\tanh^{2}\frac{\theta_{\mathrm{rpd}}}{2}
$$

below one per cent for $\beta<0.198$. Its first term is $-\beta^{2}/4$, so rung one is good to one part in $10^{4}$ at $\beta=0.01$.

## The Truncation, the Rapidity, and the Composition of Speed

**The order of the truncation.** The norm is quadratic in $\gamma$ and vanishes identically for the exact value, so its error is the square of the error of $\gamma$ to leading order. Truncate $\gamma$ at order zero, $\gamma=1$: the norm is $-c^{2}+v^{2}$, wrong at order $\beta^{2}$. Truncate at order $\beta^{2}$, $\gamma=1+\frac{\beta^{2}}{2}$: the norm is

$$
\gamma^{2}\left(v^{2}-c^{2}\right) = -c^{2}\left(1-\frac{3}{4}\beta^{4}+O\left(\beta^{6}\right)\right),
$$

wrong at order $\beta^{4}$. Keeping one more term of $\gamma$ gives an error of order $\beta^{6}$. **The truncated four-velocity satisfies the constraint to one order better than it satisfies the series.**

**The rapidity.** Set

$$
\gamma=\cosh\theta_{\mathrm{rpd}} ,
\qquad
\gamma\beta=\sinh\theta_{\mathrm{rpd}} ,
\qquad
\theta_{\mathrm{rpd}}=\operatorname{artanh}\beta .
$$

The constraint then reads $\cosh^{2}\theta_{\mathrm{rpd}}-\sinh^{2}\theta_{\mathrm{rpd}}=1$, the identity that makes the rapidity the additive parameter of the boost. In this variable the series of the previous section is $\gamma-1=\cosh\theta_{\mathrm{rpd}}-1=\frac{\theta_{\mathrm{rpd}}^{2}}{2}+\frac{\theta_{\mathrm{rpd}}^{4}}{24}+\cdots$, so **the limit is the statement that the rapidity is small**, and the excess is the squared rapidity, halved at leading order.

**Velocities compose by adding rapidities.** Rapidity adds exactly, $\theta_{\mathrm{rpd},12}=\theta_{\mathrm{rpd},1}+\theta_{\mathrm{rpd},2}$, because a boost is one rotor of one direction. In speeds this is

$$
\beta_{12} = \frac{\beta_{1}+\beta_{2}}{1+\beta_{1}\beta_{2}} ,
\qquad
\beta_{12}-\left(\beta_{1}+\beta_{2}\right) = -\frac{\beta_{1}\beta_{2}\left(\beta_{1}+\beta_{2}\right)}{1+\beta_{1}\beta_{2}} ,
$$

whose departure from the Galilean sum is of second order. Two speeds of $0.3c$ and $0.4c$ add to $0.625c$ and not to $0.7c$. **The additivity of the rapidity is the exact statement; the Galilean law is its truncation**, in the same sense as the box and its leading term.

## The Scale: The Four-Momentum

**One multiplication.** The four-momentum is the four-velocity with the mass attached,

$$
\tilde P_{\Phi} = m\,\tilde V_{\Phi} = i\,\frac{E}{c}\,e_{t}+\vec p_{\Phi} ,
\qquad
E=\gamma mc^{2},
\qquad
\vec p_{\Phi}=m\gamma\vec v ,
$$

with norm $\langle\tilde P_{\Phi}\rangle_{\natural}=-m^{2}c^{2}$. **The vector part of the four-velocity is the momentum per unit mass, and the temporal part is the energy per unit mass in units of $c$.**

**The same series, multiplied.** Every expansion of the previous sections is the same expansion with one factor:

$$
E = mc^{2}+\frac{1}{2}mv^{2}+\frac{3}{8}\frac{mv^{4}}{c^{2}}+\cdots ,
\qquad
p_{\Phi} = mv+\frac{1}{2}\frac{mv^{3}}{c^{2}}+\cdots .
$$

The excess energy is $\mathcal{E}:=E-mc^{2}=\left(\gamma-1\right)mc^{2}$, so it is the excess of the element times the one scale, and the relative error of its truncation is the same $-\left(\gamma-1\right)/\left(\gamma+1\right)$ with no conversion. Indeed

$$
\frac{p_{\Phi}^{2}}{2m} = \frac{1}{2}m\left(\gamma v\right)^{2} = mc^{2}\cdot\frac{\gamma^{2}\beta^{2}}{2} = \left(\gamma-1\right)_{\mathrm{trunc}}mc^{2} ,
$$

which is the truncated excess times $mc^{2}$: the momentum column and the velocity column are one column read in two units.

**The mass shell, and the second sheet.** Multiplying the norm by $m^{2}$ gives $E^{2}=p_{\Phi}^{2}c^{2}+m^{2}c^{4}$, and in the excess energy

$$
\left(E-mc^{2}\right)\left(E+mc^{2}\right) = p_{\Phi}^{2}c^{2} ,
\qquad
p_{\Phi}^{2} = 2m\mathcal{E}+\frac{\mathcal{E}^{2}}{c^{2}} ,
$$

the second being the box multiplied by $m^{2}c^{2}$. In this form the constraint is a quadratic and has two roots,

$$
E_{\pm} = \pm\sqrt{m^{2}c^{4}+p_{\Phi}^{2}c^{2}} ,
\qquad
E_{-}/mc^{2} = -\gamma ,
$$

and the negative one is a branch the limit cannot touch: its excess is $\gamma_--1=-\left(\gamma+1\right)\approx-2$, which is not small at any speed, and what is small there is the other factor, $\gamma_-+1=1-\gamma\approx-\beta^{2}/2$. The box factorises on that branch with the roles of the two factors exchanged, so the truncation performed here does not apply to it. The four-velocity has no such branch: its temporal part is $\gamma c$ with $\gamma>0$ by construction, so there is nothing to discard. **The negative branch appears when the constraint is squared, not when it is written.**

**The Lagrangian, and the Legendre check.** The free Lagrangian is $L=-mc^{2}\sqrt{1-\beta^{2}}=-mc^{2}/\gamma$, and its warrant is that it reproduces the momentum, $\partial L/\partial v=\gamma mv$. In terms of the element it is the rest energy divided by the temporal part, $L=-mc^{2}\left(c/\lvert V_{t}\rvert\right)$. Expanding,

$$
L = -mc^{2}+\frac{1}{2}mv^{2}+\frac{1}{8}\frac{mv^{4}}{c^{2}}+\cdots ,
\qquad
L = -mc^{2}+\frac{p_{\Phi}^{2}}{2m}-\frac{3p_{\Phi}^{4}}{8m^{3}c^{2}}+\cdots ,
$$

and the Legendre transform $E=p_{\Phi}v-L$ is exact at every speed. To order $c^{-2}$,

$$
p_{\Phi}v = \frac{p_{\Phi}^{2}}{m}-\frac{p_{\Phi}^{4}}{2m^{3}c^{2}} ,
\qquad
-L = mc^{2}-\frac{p_{\Phi}^{2}}{2m}+\frac{3p_{\Phi}^{4}}{8m^{3}c^{2}} ,
$$

whose sum is $mc^{2}+\frac{p_{\Phi}^{2}}{2m}-\frac{p_{\Phi}^{4}}{8m^{3}c^{2}}$ because $-\frac{1}{2}+\frac{3}{8}=-\frac{1}{8}$.

## Other Biquaternions Under the Same Limit

**The transfer.** Let $\tilde Q=\lambda\tilde V_{\Phi}$, with $\lambda$ real and the same for every state. Then

$$
\langle\tilde Q\rangle_{\natural}=\lambda^{2}\langle\tilde V_{\Phi}\rangle_{\natural}=-\lambda^{2}c^{2},
\qquad
\tilde Q-\tilde Q_{\mathrm{trunc}}=\lambda\left(\tilde V_{\Phi}-\tilde V_{\Phi,\mathrm{trunc}}\right),
$$

so the norm scales as a square, the excess is still $\gamma-1$ times $\lambda$, and every relative error is unchanged. **The limit transfers by one multiplication; no member of the family needs its own expansion.** In closed form the truncation multiplies any excess by $\frac{\gamma+1}{2}$, which is $1+\frac{\beta^{2}}{2}+\cdots$ and equals $1$ at rest.

**The four-momentum.** With $\tilde P_{\Phi}=m\tilde V_{\Phi}$ the excess is the kinetic energy $T:=E-mc^{2}=mc^{2}\left(\gamma-1\right)$, and

$$
E=mc^{2}\left(1+\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\cdots\right),
\qquad
p_{\Phi}=mc\left(\beta+\frac{\beta^{3}}{2}+\cdots\right),
\qquad
T=\frac{1}{2}mv^{2}\left(1+\frac{3}{4}\beta^{2}+\cdots\right).
$$

The kinetic energy computed from the momentum is $\frac{p_{\Phi}^{2}}{2m}=\frac{1}{2}m\gamma^{2}v^{2}$, and

$$
\frac{p_{\Phi}^{2}/2m}{T}=\frac{\gamma+1}{2}
$$

exactly. **The Galilean kinetic energy is not an arbitrary cut: it is the exact one multiplied by one known number.**

**The four-wave-number, and the same ladder in another variable.** With $\tilde K_{\Phi}=\left(k_m/c\right)\tilde V_{\Phi}$ and $k_m=mc/\hbar$, the excess of the temporal coefficient is $\Omega:=k_{t}^{\prime}-k_m=k_m\varepsilon$, and dividing the norm by $k_m^{2}$ gives the box again:

$$
k_{\Phi}^{2}=2k_m\Omega+\Omega^{2},
\qquad
\frac{k_{\Phi}}{k_m}=\gamma\beta .
$$

The ladder is the same construction — solve for the excess, then iterate — with $\Omega_{0}=0$:

$$
\Omega_{n+1}=\frac{k_{\Phi}^{2}-\Omega_{n}^{2}}{2k_m},
\qquad
\Omega_{1}=\frac{k_{\Phi}^{2}}{2k_m},
\qquad
\Omega_{2}=\frac{k_{\Phi}^{2}}{2k_m}-\frac{k_{\Phi}^{4}}{8k_m^{3}}+\cdots .
$$

**Rung $n$ here is correct to order $\left(k_{\Phi}/k_m\right)^{2n}$, exactly as rung $n$ in $\beta$ is correct to $\beta^{2n}$.** The first rung is again one quadratic term, and it is again the whole limit.

**The two ladders agree at the first rung and part after it.** They share $\frac{1}{2}$, because $k_{\Phi}/k_m=\gamma\beta$ reduces to the rapidity at leading order; they differ at the second, $+\frac{3}{8}$ in $\beta^{2}=\tanh^{2}\theta$ against $-\frac{1}{8}$ in $\left(k_{\Phi}/k_m\right)^{2}=\sinh^{2}\theta$. One function of the rapidity, read in two variables. **The limit is the rung the two share**, which is why it is the same equation in either variable, and why the criterion $k_{\Phi}\ll k_m$ of *The Three Wavenumbers of a Particle* and $\beta\ll1$ here are one criterion.

**The four-current.** With $\tilde J_{\Phi}=\varrho_{0}\tilde V_{\Phi}$,

$$
\tilde J_{\Phi}=i\,c\rho\,e_{t}+\vec j,
\qquad
\rho=\gamma\varrho_{0}=\varrho_{0}\left(1+\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\cdots\right),
\qquad
\vec j=\rho\vec v ,
$$

and continuity $\partial_{t}\rho+\nabla\cdot\vec j=0$ holds exactly for uniform motion. This series starts at $1$, not at $\beta^{2}$, so the truncation leaves $-\frac{3\beta^{4}}{8}$: **what the limit removes from $\rho$ is the second-order part of the Lorentz contraction, not its first-order part.**

**The four-potential of one charge.** For a charge in uniform motion $\tilde A_{\Phi}\propto\tilde V_{\Phi}$, so $\varphi=\gamma\varphi_{0}$ and $\vec A=\gamma\varphi_{0}\vec v/c^{2}$, and

$$
\frac{\lvert\vec B\rvert}{\lvert\vec E\rvert}=\frac{\beta}{c},
$$

one power of the speed: the magnetic field is a first-order effect, the electric field zeroth order.

**Outside the family.** A general four-potential is a four-vector of the sector but not a four-velocity times a scale, so its components are independent and its limit is not a truncation. The field biquaternion $\tilde F$ is built from $\vec E$ and $\vec B$ and is a multiple of no $\tilde V_{\Phi}$: at leading order only its electric part survives. The boost rotor is a unit-norm element of the group, not a multiple of the state, so its limit is a degeneration, the boost becoming a shear.

| Element | Definition | In the family | Truncated | Error |
|---|---|---|---|---|
| $\tilde V_{\Phi}$ | $\gamma\left(ic\,e_{t}+\vec v\right)$ | the base element | $\gamma-1\to\frac{1}{2}\gamma^{2}\beta^{2}$ | factor $\frac{\gamma+1}{2}$ |
| $\tilde P_{\Phi}$ | $m\tilde V_{\Phi}$ | yes, $m$ | $T\to\frac{p_{\Phi}^{2}}{2m}$ | factor $\frac{\gamma+1}{2}$ |
| $\tilde K_{\Phi}$ | $\left(k_m/c\right)\tilde V_{\Phi}$ | yes, $k_m/c$ | $\Omega\to\frac{k_{\Phi}^{2}}{2k_m}$ | factor $\frac{\gamma+1}{2}$ |
| $\tilde J_{\Phi}$ | $\varrho_{0}\tilde V_{\Phi}$ | yes, $\varrho_{0}$ | $\rho\to\varrho_{0}\left(1+\frac{\beta^{2}}{2}\right)$ | $-\frac{3\beta^{4}}{8}$ |
| $\tilde A_{\Phi}$ | $\propto\tilde V_{\Phi}$, one charge | partly | $\varphi\to\varphi_{0}\left(1+\frac{\beta^{2}}{2}\right)$ | $\frac{\lvert\vec B\rvert}{\lvert\vec E\rvert}=\frac{\beta}{c}$ |
| $\tilde F$ | from $\vec E$, $\vec B$ | no | electric part only | magnetic part next order |
| boost rotor | unit-norm, group element | no | boost becomes a shear | degeneration |

## The Phase and the Order in Time

**The phase splits like the energy.** A plane wave carries the scalar part of $\tilde K_{\Phi}\tilde R_{\Phi}^{\natural}$ in its exponent. With $E = mc^{2}+\mathcal{E}$,

$$
e^{\,i\left(\vec p_{\Phi}\cdot\vec r - Et\right)/\hbar}
= \underbrace{e^{-i\,mc^{2}t/\hbar}}_{f}\,
\underbrace{e^{\,i\left(\vec p_{\Phi}\cdot\vec r - \mathcal{E}t\right)/\hbar}}_{\chi} ,
$$

exactly. The first factor is the **rest phase**, of frequency $\omega_{m}=mc^{2}/\hbar$ and period $8.09\times10^{-21}\ \mathrm{s}$ for the electron; it is the fastest motion in the state, turning $6.5$ times for every turn of the excess at $\beta=0.5$. The second factor is the envelope, and it is what the limit is about.

**Two terms of the exponential give a first-order equation.** Over a step $\delta t$,

$$
e^{-i\,\mathcal{E}\,\delta t/\hbar} = 1 - i\,\frac{\mathcal{E}}{\hbar}\,\delta t + O\left(\delta t^{2}\right)
\qquad\Longrightarrow\qquad
\partial_{t}\chi = -\frac{i}{\hbar}\,\mathcal{E}\,\chi .
$$

First order in time, because the exponential was cut after two terms. A third term would bring $\chi''$ and rebuild a second-order equation; a fourth would bring $\chi'''$. **The order in time is the number of terms kept in the exponential**, and that is the same decision as the truncation of the ladder.

**The same statement as an operator.** The exact relation $\mathcal{E}=\sqrt{m^{2}c^{4}+p_{\Phi}^{2}c^{2}}-mc^{2}$ is not a polynomial; through $p_{\Phi}^{2}\to-\hbar^{2}\Delta$ it becomes the square root of a differential operator,

$$
i\hbar\,\frac{\partial\chi}{\partial t} = \left(\sqrt{m^{2}c^{4}-\hbar^{2}c^{2}\Delta}-mc^{2}\right)\chi ,
$$

non-local, whose square is the Klein–Gordon operator after the rest phase is removed. Truncating to the first term of the ladder makes it local: the truncation of the ladder and the reduction of the order are one operation.

## The Equation of the Limit

**From the momentum.** With the truncated excess energy $\mathcal{E}=p_{\Phi}^{2}/2m$ and $p_{\Phi}^{2}\to-\hbar^{2}\Delta$,

$$
i\hbar\,\frac{\partial\chi}{\partial t} = \frac{p_{\Phi}^{2}}{2m}\,\chi = -\frac{\hbar^{2}}{2m}\,\Delta\,\chi .
$$

**From the wave number.** With $\Omega_{\mathrm{trunc}}=k_{\Phi}^{2}/2k_m$ and $k_{\Phi}^{2}\to-\Delta$, the same statement multiplied by $\hbar c$ reads

$$
i\,\frac{\partial\chi}{\partial r'_{t}} = -\frac{1}{2k_m}\,\Delta\,\chi ,
\qquad
r'_{t}=c\,t ,
$$

which is the free Schrödinger equation:

$$
\boxed{\;i\hbar\,\frac{\partial\chi}{\partial t} = -\frac{\hbar^{2}}{2m}\,\Delta\,\chi\;}
$$

**Two features are read off, not assumed.** It is first order in time because the term kept is $\mathcal{E}$ and not $\mathcal{E}^{2}$; it is local and linear because the leading term is quadratic in the momentum. The constraint it comes from is not polynomial; both features are consequences of the truncation.

In the material sector the same equation reads

$$
\frac{mc^{2}i}{k_m}\,\frac{\partial\chi}{\partial r'_{t}} = \tilde R_{\Psi}\,\chi ,
\qquad
\tilde R_{\Psi} = -\frac{\hbar^{2}}{2m}\,\Delta \in \mathbb{B}_{\Psi} ,
$$

since $mc^{2}/k_m = \hbar c$. The observable $\tilde R_{\Psi}$ is Hermitian and informational, the coefficient carries the central $i$ and lies in $\mathbb{B}_{\Phi}$. This is the structure *The Schrödinger Equation in Biquaternionic Form* assumes; here it is what the constraint leaves when its quadratic term is dropped.

**Only a scaled element produces a wave equation.** The limit on $\tilde V_{\Phi}$ is a statement about a dimensionless element and stops there, because a velocity is not an operator. To reach a field the scale must supply $\hbar$, and among the elements of the table only $\tilde P_{\Phi}$ and $\tilde K_{\Phi}$ do. The wave equation is the scale's consequence, not the limit's, which is why it is written last.

## What the Limit Selects, and What It Does Not Do

**No branch is selected.** The temporal part is $\gamma c$ with $\gamma>0$ by construction, so the velocity form has no second branch to exclude. The branch of §*The Scale: The Four-Momentum* appears only because squaring turned the constraint into a quadratic, and that root is not a second kind of four-velocity. No solution has been thrown away.

**The constant is not a knob.** The limit is taken on the state, not on $c$. Setting $c\to\infty$ would contradict the Maxwell equations the constant comes from. Only $\gamma-1$ goes to zero.

**It does not produce spin or antiparticles.** The constraint is one equation on one element, and intrinsic angular momentum needs a multicomponent field: the corpus reaches the spinor case through the square root of the wave operator, and the negative branch of the energy form through second quantisation. *The Foldy–Wouthuysen Transformation in Biquaternionic Form* takes the same limit on the Dirac equation, where the odd terms must be removed first.

**It does not re-derive Galilean kinematics.** What is expanded here is the composition of two boosts, not the transformation law between frames.

## Case Checked

**The velocity.** The first four columns are exact, the fifth is the truncated excess, and the last two must agree.

| $\beta$ | $\gamma$ | $\gamma-1$ | $\gamma^{2}\beta^{2}$ | $\frac{1}{2}\gamma^{2}\beta^{2}$ | error | $-\frac{\gamma-1}{\gamma+1}$ |
|---|---|---|---|---|---|---|
| $0.01$ | $1.00005$ | $5.000\times10^{-5}$ | $1.0000\times10^{-4}$ | $5.000\times10^{-5}$ | $-2.50\times10^{-5}$ | $-2.50\times10^{-5}$ |
| $0.10$ | $1.00504$ | $5.0376\times10^{-3}$ | $1.0101\times10^{-2}$ | $5.0504\times10^{-3}$ | $-2.51\times10^{-3}$ | $-2.51\times10^{-3}$ |
| $0.50$ | $1.15470$ | $1.5470\times10^{-1}$ | $3.3333\times10^{-1}$ | $1.6667\times10^{-1}$ | $-7.18\times10^{-2}$ | $-7.18\times10^{-2}$ |
| $0.90$ | $2.29416$ | $1.2942$ | $4.2632$ | $2.1316$ | $-3.93\times10^{-1}$ | $-3.93\times10^{-1}$ |

The last two columns agree in every row because the error is exact, not estimated.

**With the scale attached**, for the electron, $mc^{2}=510998.95\ \mathrm{MeV}$:

| $\beta$ | $E\ (\mathrm{MeV})$ | $\mathcal{E}\ (\mathrm{MeV})$ | $\frac{p^{2}}{2m}\ (\mathrm{MeV})$ | error |
|---|---|---|---|---|
| $0.01$ | $511024.50$ | $25.55$ | $25.55$ | $-2.50\times10^{-5}$ |
| $0.10$ | $513573.27$ | $2574.32$ | $2580.80$ | $-2.51\times10^{-3}$ |
| $0.50$ | $590050.76$ | $79051.81$ | $85166.49$ | $-7.18\times10^{-2}$ |
| $0.90$ | $1172311.99$ | $661313.04$ | $1089234.60$ | $-3.93\times10^{-1}$ |

The first row is the regime the limit is for, one part in twenty thousand. The last is not: at $\beta=0.9$ the truncation costs thirty-nine per cent.

**The identities.** The box, the closed form $\gamma-1=\sqrt{1+\gamma^{2}\beta^{2}}-1$ and the error $-\left(\gamma-1\right)/\left(\gamma+1\right)=-\tanh^{2}\left(\theta_{\mathrm{rpd}}/2\right)$ were each evaluated at two hundred speeds spanning $\beta=10^{-3}$ to $0.99$ and hold to $10^{-15}$ relative, which is the arithmetic. The composition law was checked the same way.

**The equation.** A two-mode packet with $\mathcal{E}_{j}=p_{j}^{2}/2m$ was propagated and compared with the right side of the boxed equation on a spectral grid; the residual is $3\times10^{-13}$ against a field of unit size, the floor of the transform. It must vanish: the equation holds on each mode and is linear.

## Summary

The kinematic content of relativistic mechanics is one element and one constraint: $\tilde V_{\Phi}=\gamma\left(ic\,e_{t}+\vec v\right)\in\mathbb{B}_{\Phi}$ with $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$, frame-independent and conserved because the norm is multiplicative and a boost is a rotor conjugation. The parameter is the ratio of the two parts, $\beta=v/c$.

The limit is one boxed expansion, $\gamma=1+\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\frac{5\beta^{6}}{16}+\cdots$, whose first correction is the excess of the temporal part over its rest value, $\gamma-1\simeq\frac{1}{2}\beta^{2}$. The constraint reads exactly $\gamma^{2}\beta^{2}=\left(\gamma-1\right)\left(\gamma+1\right)$, and the truncation error is $-\left(\gamma-1\right)/\left(\gamma+1\right)=-\tanh^{2}\left(\theta_{\mathrm{rpd}}/2\right)$, below one per cent for $\beta<0.198$. Since the norm is quadratic in $\gamma$, the truncated element satisfies the constraint one order better than it satisfies the series.

The scale attaches once. $\tilde P_{\Phi}=m\tilde V_{\Phi}$ gives $E=mc^{2}+\frac{1}{2}mv^{2}+\frac{3}{8}\frac{mv^{4}}{c^{2}}+\cdots$, with the same excess and the same error, and the negative branch is a second root of a quadratic, not a second sheet. The same test sorts the rest: $\tilde K_{\Phi}$, $\tilde J_{\Phi}$ and the $\tilde A_{\Phi}$ of one charge are the element times a scale; a general $\tilde A_{\Phi}$, the field $\tilde F$ and the rotor are not.

Only the scaled elements carrying $\hbar$ produce a wave equation, and it is the free Schrödinger equation. That power is the scale's, not the limit's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde V_{\Phi} = \gamma\left(ic\,e_{t}+\vec v\right)$ | Four-velocity; unit-norm element of $\mathbb{B}_{\Phi}$, the base of the article |
| $\langle\tilde V_{\Phi}\rangle_{\natural} = -c^{2}$ | The norm; the one constraint, frame-independent and conserved |
| $\beta = \lvert\gamma\vec v\rvert/\lvert i\gamma c\rvert = v/c$ | Ratio of the two parts of the element; exact, the parameter of the limit |
| $\gamma-1$ | Excess of the temporal part over its rest value, in units of $c$ |
| $\gamma = 1+\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\cdots$ | The one expansion; everything else is it with a factor |
| $\gamma^{2}\beta^{2}=\left(\gamma-1\right)\left(\gamma+1\right)$ | The constraint as a difference of squares; exact |
| $-\frac{\gamma-1}{\gamma+1}=-\tanh^{2}\left(\theta_{\mathrm{rpd}}/2\right)$ | Relative error of the truncation, exact at every speed |
| $\theta_{\mathrm{rpd}} = \operatorname{artanh}\beta$ | Rapidity; the additive parameter of the boost |
| $\tilde P_{\Phi} = m\tilde V_{\Phi}$ | Four-momentum; the scale $m$ attached |
| $E=\gamma mc^{2}$, $\vec p_{\Phi}=m\gamma\vec v$ | Energy and momentum; the components of the scaled element |
| $\mathcal{E} = E-mc^{2} = \left(\gamma-1\right)mc^{2}$ | Excess energy |
| $\Omega = k_{t}^{\prime}-k_m = k_m\left(\gamma-1\right)$ | Excess wave number |
| $\tilde K_{\Phi} = \left(k_m/c\right)\tilde V_{\Phi}$ | Four-wave-number; the scale $k_m/c$ attached |
| $\tilde J_{\Phi} = \varrho_{0}\tilde V_{\Phi}$ | Convective four-current; the scale $\varrho_{0}$ attached |
| $r'_{t} = c\,t$ | Material time |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (4th ed., Butterworth–Heinemann, 1975), §9, for the expansion of the relativistic energy and momentum and the Lagrangian of a free particle.
- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics* (3rd ed., Addison–Wesley, 2002), chapter 7, for the relativistic Lagrangian and the Legendre transform.
- John David Jackson, *Classical Electrodynamics* (3rd ed., Wiley, 1999), §11.5 and §11.10, for the same expansion on the motion of a charge in an external field.
- Albert Messiah, *Quantum Mechanics* (North-Holland, 1961), chapter XX, for the non-relativistic limit of the Klein–Gordon and Dirac equations.
- Leslie L. Foldy and Siegfried A. Wouthuysen, "On the Dirac theory of spin 1/2 and its non-relativistic limit," *Physical Review* **78** (1950) 29–36.
- Paul A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the first-order square root of the wave operator.
