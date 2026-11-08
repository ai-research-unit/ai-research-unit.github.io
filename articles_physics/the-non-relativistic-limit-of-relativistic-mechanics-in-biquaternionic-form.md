# __The Non-Relativistic Limit of Relativistic Mechanics in Biquaternionic Form__

## Introduction

Relativistic mechanics in biquaternion form rests on one element and one constraint. The element is the four-velocity, $\tilde V_{\Phi}=\gamma\left(ic\,e_{t}+\vec v\right)$, a biquaternion of the material sector. The constraint is its norm, $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$, the same for every particle and in every frame. The four-momentum, the four-wave-number, the four-current and the potential of one charge are that element multiplied by a scale.

**The goal.** The article gives one approximation per element, for $\tilde V_{\Phi}$, $\tilde P_{\Phi}$, $\tilde K_{\Phi}$, $\tilde J_{\Phi}$ and $\tilde A_{\Phi}$, correct to order $\beta^{2}$ in the speed, with the coefficient of the next term stated. It attempts nothing else. There is no wave equation here, no spin, and no transformation law between frames.

**One parameter and one rule.** The two parts of the element are $\gamma c$ and $\gamma v$, and their ratio is $\beta=\lvert\vec v\rvert/c$ exactly. The limit is the statement that this ratio is small. One rule covers the five elements: **keep the excess of $\gamma$ to order $\beta^{2}$ in the temporal slot, drop it in the vector slot.** The error of the rule is a closed form, and it differs between the two slots.

**Why the velocity and not the momentum.** The four-momentum is $\tilde P_{\Phi}=m\tilde V_{\Phi}$, and the mass is a free real scale: the norm is homogeneous and the light cone is scale-invariant. A limit taken on $\tilde P_{\Phi}$ carries the mass in every coefficient, and the mass then enters by a route the constraint never authorised. Taken on $\tilde V_{\Phi}$ the limit is a statement about a dimensionless element, and the mass enters once, at the end, where the scale is attached.

**What is not new.** The algebra is that of *Relativistic Mechanics in Biquaternionic Form*, and the expansion of $1/\sqrt{1-\beta^{2}}$ is textbook. What the article isolates is the order of the moves: **write the norm in two parts, expand $\gamma$ once, keep the leading correction of the temporal slot, then attach the scale.**

**Two limits, not one.** The **kinematic** limit is the subject here: the vector part of the element is small compared with the temporal part. The **central-scalar** restriction, separated in *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*, says which directions of the algebra are occupied and holds at any speed. A slowly moving spinning top satisfies the kinematic limit and violates the central-scalar restriction.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_{t}=1, \vec e_{x}, \vec e_{y}, \vec e_{z}$ with $\vec e_{\mu}^{2}=-e_{t}$ and $\vec e_{\mu}\vec e_{\nu}=\varepsilon_{\mu\nu\lambda}\vec e_{\lambda}$, and $i$ is the scalar imaginary, central in $\mathbb{B}$. The material sector is $\mathbb{B}_{\Phi}=\mathrm{span}_{\mathbb{R}}\{ie_{t},\vec e_{x},\vec e_{y},\vec e_{z}\}$, the anti-Hermitian one, and the informational sector is $\mathbb{B}_{\Psi}=\mathrm{span}_{\mathbb{R}}\{e_{t},i\vec e_{x},i\vec e_{y},i\vec e_{z}\}$, the Hermitian one. The four-position is $\tilde R_{\Phi}=i\,r'_{t}\,e_{t}+\vec r$, both it and $\tilde V_{\Phi}$ in $\mathbb{B}_{\Phi}$. The rapidity is $\theta_{\mathrm{rpd}}$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, $c_{0}$ its vacuum value, $\beta=\lvert\vec v\rvert/c$ and $\gamma=1/\sqrt{1-\beta^{2}}$.

## The Element and Its Norm

**The element.** The coefficient of $e_{t}$ is imaginary and the vector part is real, so $\tilde V_{\Phi}$ is anti-Hermitian and lies in $\mathbb{B}_{\Phi}$. Its norm,

$$
\langle\tilde V_{\Phi}\rangle_{\natural} = \tilde V_{\Phi}\tilde V_{\Phi}^{\natural}
= \gamma^{2}\left(-c^{2}+\vec v^{\,2}\right) = -c^{2} ,
$$

is the whole input: one equation, true of every particle, containing no mass, no $\hbar$ and no energy.

**The constraint is conserved, and it is complete.** The norm of $\mathbb{B}$ is multiplicative, $\langle\tilde Q_{1}\tilde Q_{2}\rangle_{\natural}=\langle\tilde Q_{1}\rangle_{\natural}\langle\tilde Q_{2}\rangle_{\natural}$, and a boost multiplies on the two sides by elements of unit norm. Hence $\langle\tilde V_{\Phi}'\rangle_{\natural}=-c^{2}$ in every frame and along the worldline: the group preserves the constraint rather than the constraint being imposed after the fact. The element has four real coefficients and the norm is one real condition. The three that remain are the three components of the velocity.

## One Expansion and One Rule

**The excess, defined once.** Write the temporal part as its rest value plus what the motion adds, in units of $c$:

$$
\tfrac{1}{c}\left\lvert i\gamma c\,e_{t}\right\rvert=\gamma=1+\varepsilon ,
\qquad
\varepsilon:=\gamma-1 .
$$

Nothing is approximated in that line; $\varepsilon$ is defined, not expanded into. It vanishes at rest and grows without bound as $\lvert\vec v\rvert\to c$. Squaring the constraint and dividing by $c^{2}$ gives the exact difference of squares,

$$
\gamma^{2}\beta^{2}=\gamma^{2}-1=\left(\gamma-1\right)\left(\gamma+1\right)
\qquad\Longleftrightarrow\qquad
\left(1+\varepsilon\right)^{2}\beta^{2}=\varepsilon\left(2+\varepsilon\right) ,
$$

so the square of the vector part, in units of $c^{2}$, is twice the excess plus the square of the excess. Solving that relation for $\varepsilon$ and iterating from $\varepsilon_{0}=0$ gives $\varepsilon=\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\frac{5\beta^{6}}{16}+\cdots$, and the first term is the whole limit.

**The rule.** Keep the temporal slot to its first correction and the vector slot to its zeroth:

$$
\tilde V_{\Phi}=\gamma\left(i\,c\,e_{t}+\vec v\right)
\quad\longrightarrow\quad
\tilde V_{\Phi,1}=i\,c\left(1+\frac{\beta^{2}}{2}\right)e_{t}+\vec v .
$$

The two slots are truncated differently on purpose. The temporal slot decides the energy, so its correction of order $\beta^{2}$ is the kinetic energy and must be kept. The vector slot is already of order $\beta$, so its correction of relative order $\beta^{2}$ is of order $\beta^{3}$ in the element and lies beyond the order kept.

**The error, in closed form, and it differs between the slots.** Comparing each slot with the exact one,

$$
\frac{\frac{1}{2}\beta^{2}}{\gamma-1}=\frac{\gamma+1}{2\gamma^{2}}=1-\frac{3}{4}\beta^{2}-\frac{1}{16}\beta^{4}+\cdots,
\qquad
\frac{v}{\gamma v}=\frac{1}{\gamma}=1-\frac{1}{2}\beta^{2}-\frac{1}{8}\beta^{4}+\cdots .
$$

Both ratios are exact at every speed; their series give the truncation order. The temporal slot undershoots by $\frac{3}{4}\beta^{2}$ and the vector slot by $\frac{1}{2}\beta^{2}$, so **the rule is exact to order $\beta^{2}$ and its leading error is of order $\beta^{4}$ in the element.**

**The strongest objection: why not keep the norm exact?** The two slots are one degree of freedom short of the constraint, so one can instead fix $\vec v$ and solve $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$ for the temporal coefficient, which gives $c\sqrt{1+\beta^{2}}=c\left(1+\frac{\beta^{2}}{2}-\frac{\beta^{4}}{8}+\cdots\right)$. That element satisfies the norm exactly at every speed. It is not the one to keep, because the norm is not the observable: the energy is, and the coefficient $\frac{1}{2}\beta^{2}$ is what makes $\mathcal{E}$ equal both $\frac{1}{2}mv^{2}$ and $\frac{p^{2}}{2m}$ in the same scheme. The two choices agree at the order kept and part at order $\beta^{4}$; the truncated element of the rule has $\langle\tilde V_{\Phi,1}\rangle_{\natural}=-c^{2}\left(1+\frac{\beta^{4}}{4}\right)$, a relative error of $2.5\times10^{-9}$ at $\beta=0.01$.

**The same statement in the rapidity.** With $\gamma=\cosh\theta_{\mathrm{rpd}}$ and $\gamma\beta=\sinh\theta_{\mathrm{rpd}}$, the constraint reads $\cosh^{2}\theta_{\mathrm{rpd}}-\sinh^{2}\theta_{\mathrm{rpd}}=1$, and the series is $\gamma-1=\frac{\theta_{\mathrm{rpd}}^{2}}{2}+\frac{\theta_{\mathrm{rpd}}^{4}}{24}+\cdots$. **The limit is the statement that the rapidity is small**, and the excess is the squared rapidity, halved at leading order.

## The Scale

**One multiplication.** Let $\tilde X_{\Phi}=\lambda\tilde V_{\Phi}$, with $\lambda$ real and the same for every state, and $\tilde X_{\Phi,1}=\lambda\tilde V_{\Phi,1}$. Then

$$
\tilde X_{\Phi}=\lambda\gamma\left(ic\,e_{t}+\vec v\right),
\qquad
\langle\tilde X_{\Phi}\rangle_{\natural}=-\lambda^{2}c^{2},
\qquad
\tilde X_{\Phi}-\tilde X_{\Phi,1}=\lambda\left(\tilde V_{\Phi}-\tilde V_{\Phi,1}\right) .
$$

The norm scales as a square and the error as the first power. **The limit transfers by one multiplication, so no member of the family needs its own expansion.** That is why the five elements below form one table and not five derivations.

## The Approximations

**The table.** Every row is $\lambda\gamma\left(ic\,e_{t}+\vec v\right)$, truncated by the one rule. The last column is what the truncation drops, and in every row it is the same two pieces: $\frac{3}{8}$ of the temporal slot at order $\beta^{4}$ and $\frac{1}{2}\beta^{2}$ of the vector slot.

| Element | $\lambda$ | Exact | Order $\beta^{2}$ | Next term |
|---|---|---|---|---|
| $\tilde V_{\Phi}$ | $1$ | $\gamma\left(ic\,e_{t}+\vec v\right)$ | $ic\left(1+\frac{\beta^{2}}{2}\right)e_{t}+\vec v$ | $\frac{3}{8}ic\,\beta^{4}e_{t}+\frac{\beta^{2}}{2}\vec v$ |
| $\tilde P_{\Phi}$ | $m$ | $i\frac{E}{c}e_{t}+\vec p$ | $imc\left(1+\frac{\beta^{2}}{2}\right)e_{t}+m\vec v$ | $\frac{3}{8}imc\,\beta^{4}e_{t}+\frac{\beta^{2}}{2}m\vec v$ |
| $\tilde K_{\Phi}$ | $k_m/c$ | $ik'_{t}e_{t}+\vec k_{\Phi}$ | $ik_m\left(1+\frac{\beta^{2}}{2}\right)e_{t}+k_m\vec\beta$ | $\frac{3}{8}ik_m\beta^{4}e_{t}+\frac{\beta^{2}}{2}k_m\vec\beta$ |
| $\tilde J_{\Phi}$ | $\rho_{0}$ | $ic\rho\,e_{t}+\vec j$ | $ic\rho_{0}\left(1+\frac{\beta^{2}}{2}\right)e_{t}+\rho_{0}\vec v$ | $\frac{3}{8}ic\rho_{0}\beta^{4}e_{t}+\frac{\beta^{2}}{2}\rho_{0}\vec v$ |
| $\tilde A_{\Phi}$ | $a'_{t,0}/c$ | $ia'_{t}e_{t}+\vec A$ | $ia'_{t,0}\left(1+\frac{\beta^{2}}{2}\right)e_{t}+a'_{t,0}\frac{\vec v}{c}$ | $\frac{3}{8}ia'_{t,0}\beta^{4}e_{t}+\frac{\beta^{2}}{2}a'_{t,0}\frac{\vec v}{c}$ |

with $\vec\beta=\vec v/c$, $k_m=mc/\hbar$, $k'_{t}=E/(\hbar c)$, $\vec k_{\Phi}=\vec p/\hbar$, $E=\gamma mc^{2}$, $\vec p=\gamma m\vec v$, $\rho$ the charge density of $\tilde J_{\Phi}$ and $\tilde A_{\Phi}=ia'_{t}e_{t}+\vec A$, the coefficient $a'_{t,0}$ being its value at rest. The readings of the three wave numbers are the subject of *The Three Wavenumbers of a Particle*. The first row is the base case; the second is its scale; the last three are the same statement in wave numbers, in a charge density and in a potential.

**The energy and the momentum.** The row for $\tilde P_{\Phi}$ reads off as

$$
E=mc^{2}\left(1+\frac{\beta^{2}}{2}\right),
\qquad
\vec p=m\vec v ,
\qquad
\mathcal{E}:=E-mc^{2}=\frac{1}{2}mv^{2} ,
$$

and the three are one statement. The kinetic energy is the leading correction of the temporal slot, the momentum is the vector slot with the scale attached, and the two agree because

$$
\frac{p^{2}}{2m}=\frac{1}{2}m\vec v^{\,2}=\mathcal{E}
$$

holds exactly in the truncated scheme. **That consistency is the warrant for truncating the two slots differently:** any other split of the corrections breaks the equality between the kinetic energy and $p^{2}/2m$.

**The alternative momentum rule, and its price.** Keeping $\vec p$ exact and setting $E=mc^{2}+p^{2}/2m$ is the other common truncation. It is closer, with

$$
\frac{p^{2}/2m}{\mathcal{E}}=\frac{\gamma+1}{2}=1+\frac{\beta^{2}}{2}+O\left(\beta^{4}\right),
$$

against $1-\frac{3}{4}\beta^{2}$ for the rule above. The price is that the vector slot then carries $\gamma$, so the truncated element is not a polynomial in $\beta$ and the family of the table is lost. **The rule above is the one truncation of the family that is polynomial at the order kept.**

**The current and the potential.** The row for $\tilde J_{\Phi}$ is $\rho=\gamma\rho_{0}$ and $\vec j=\rho\vec v$, so the truncation gives $\rho=\rho_{0}\left(1+\frac{\beta^{2}}{2}\right)$ and $\vec j=\rho_{0}\vec v$. The charge density is the temporal slot, so it keeps the correction and the current follows it. The row for $\tilde A_{\Phi}$ is the potential of one charge in uniform motion, where $\tilde A_{\Phi}\propto\tilde V_{\Phi}$: the scalar part scales as the temporal slot and the vector part as the velocity, so $\lvert\vec A\rvert/a'_{t}=\beta$ and $\lvert\vec B\rvert/\lvert\vec E\rvert=\beta/c$. **The magnetic field is a first-order effect and the electric field is zeroth order**: the vector potential appears at order $\beta$ where the scalar potential is already present at rest.

**Outside the family.** A general four-potential is a four-vector of the sector but not a multiple of one $\tilde V_{\Phi}$, and a superposition of charges is not either: their components are independent and have no limit of this kind. The field biquaternion $\tilde F$ is built from $\vec E$ and $\vec B$ and is a multiple of no $\tilde V_{\Phi}$. The boost rotor has unit norm and belongs to the group, not to the state; its limit is a degeneration, the boost becoming a shear, treated in *The Classical Free Particle and Inertial Frames in Biquaternionic Form*.

## What the Limit Does Not Do

**No branch is selected.** The temporal part is $\gamma c$ with $\gamma>0$ by construction, so the velocity form has no second branch to exclude. A second root appears only when the constraint is squared into $E^{2}=p^{2}c^{2}+m^{2}c^{4}$, and that root is not a second kind of four-velocity. No solution has been thrown away.

**The constant is not a knob.** The limit is taken on the state, not on $c$. Setting $c\to\infty$ would contradict the Maxwell equations the constant comes from. Only $\gamma-1$ goes to zero.

**It does not produce spin or antiparticles.** The constraint is one equation on one element, and intrinsic angular momentum needs a multicomponent field. The corpus reaches the spinor case through the square root of the wave operator, and the negative branch of the energy through second quantisation.

**It does not produce a wave equation.** A velocity is not an operator. Only a scaled element carrying $\hbar$ is, and only then does the truncation of the energy become the free Schrödinger equation: that is the subject of *The Schrödinger Equation in Biquaternionic Form*, and, for the Dirac field, of *The Foldy–Wouthuysen Transformation in Biquaternionic Form*. **The wave equation is the scale's consequence, not the limit's.**

**It does not re-derive Galilean kinematics.** What is expanded here is the state, not the transformation law between frames.

## Case Checked

**The two slots.** The first three columns are exact, and the last two are the closed-form ratios, which their series must reproduce.

| $\beta$ | $\gamma$ | $\gamma-1$ | $\frac{1}{2}\beta^{2}$ | $\frac{\gamma+1}{2\gamma^{2}}$ | $1/\gamma$ |
|---|---|---|---|---|---|
| $0.01$ | $1.00005000$ | $5.0004\times10^{-5}$ | $5.0000\times10^{-5}$ | $0.999925$ | $0.999950$ |
| $0.10$ | $1.00503782$ | $5.0378\times10^{-3}$ | $5.0000\times10^{-3}$ | $0.992494$ | $0.994987$ |
| $0.50$ | $1.15470054$ | $1.5470\times10^{-1}$ | $1.2500\times10^{-1}$ | $0.808013$ | $0.866025$ |
| $0.90$ | $2.29415734$ | $1.2942$ | $4.0500\times10^{-1}$ | $0.312945$ | $0.435890$ |

The fourth column over the third is the fifth, and the fifth equals $1-\frac{3}{4}\beta^{2}-\frac{1}{16}\beta^{4}$; the sixth equals $1-\frac{1}{2}\beta^{2}-\frac{1}{8}\beta^{4}$. The residual is of order $\beta^{6}$ in each case. The limit is for the first row and not for the last: at $\beta=0.5$ the temporal slot already costs nineteen per cent.

**With the scale attached**, for the electron, $mc^{2}=510998.95\ \mathrm{MeV}$:

| $\beta$ | $E\ (\mathrm{MeV})$ | $\mathcal{E}\ (\mathrm{MeV})$ | $\frac{1}{2}mv^{2}\ (\mathrm{MeV})$ | ratio |
|---|---|---|---|---|
| $0.01$ | $511024.50$ | $25.5519$ | $25.5499$ | $0.999925$ |
| $0.10$ | $513573.27$ | $2574.32$ | $2554.99$ | $0.992494$ |
| $0.50$ | $590050.76$ | $79051.81$ | $63874.87$ | $0.808013$ |
| $0.90$ | $1172311.99$ | $661313.04$ | $206954.57$ | $0.312945$ |

The ratio column is the same in the two tables, as it must be: the scale multiplies the exact and the truncated excess alike.

**The identities.** The difference of squares, the two ratios $\frac{\gamma+1}{2\gamma^{2}}$ and $1/\gamma$, and the truncated norm $-c^{2}\left(1+\frac{\beta^{4}}{4}\right)$ were evaluated at one hundred speeds spanning $\beta=10^{-2}$ to $0.99$ and hold to $10^{-13}$ relative, which is the arithmetic. The norm-exact alternative $c\sqrt{1+\beta^{2}}$ holds to the same accuracy.

## Summary

The kinematic content of relativistic mechanics is one element and one constraint: $\tilde V_{\Phi}=\gamma\left(ic\,e_{t}+\vec v\right)\in\mathbb{B}_{\Phi}$ with $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$, frame-independent and conserved because the norm is multiplicative and a boost is a rotor conjugation. The parameter is the ratio of the two parts, $\beta=v/c$, exactly.

The limit is one rule: keep the excess of $\gamma$ to order $\beta^{2}$ in the temporal slot and drop it in the vector slot. It gives $\tilde V_{\Phi,1}=ic\left(1+\frac{\beta^{2}}{2}\right)e_{t}+\vec v$, with the exact ratios $\frac{\gamma+1}{2\gamma^{2}}=1-\frac{3}{4}\beta^{2}+\cdots$ in the temporal slot and $\frac{1}{\gamma}=1-\frac{1}{2}\beta^{2}+\cdots$ in the vector slot.

The scale attaches once. Every element of the family $\tilde X_{\Phi}=\lambda\tilde V_{\Phi}$ is truncated by one multiplication, which gives $E=mc^{2}+\frac{1}{2}mv^{2}$, $\vec p=m\vec v$, $\mathcal{E}=p^{2}/2m$, and the same three statements in wave numbers, in charge density and in the potential of one charge. Only an element carrying $\hbar$ goes further, to a wave equation, and that is the scale's doing and not the limit's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde V_{\Phi} = \gamma\left(ic\,e_{t}+\vec v\right)$ | Four-velocity; the base element of the article |
| $\langle\tilde V_{\Phi}\rangle_{\natural} = -c^{2}$ | The norm; the one constraint, frame-independent and conserved |
| $\beta = \lvert\vec v\rvert/c$ | Ratio of the two parts; exact, the parameter of the limit |
| $\gamma = 1+\frac{\beta^{2}}{2}+\frac{3\beta^{4}}{8}+\cdots$ | The one expansion; every truncation is a partial sum of it |
| $\gamma-1$ | Excess of the temporal part over its rest value, in units of $c$ |
| $\frac{\gamma+1}{2\gamma^{2}}$ | Exact ratio of the truncated to the exact excess, temporal slot |
| $1/\gamma$ | Exact ratio of the truncated to the exact vector slot |
| $\tilde X_{\Phi} = \lambda\tilde V_{\Phi}$ | The family; $\lambda$ is the one scale, real and state-independent |
| $E=\gamma mc^{2}$, $\vec p=\gamma m\vec v$ | Energy and momentum; the components of $\tilde P_{\Phi}=m\tilde V_{\Phi}$ |
| $\mathcal{E} = E-mc^{2} = \left(\gamma-1\right)mc^{2}$ | Excess energy; equal to $\frac{1}{2}mv^{2}$ after truncation |
| $k_m=mc/\hbar$, $k'_{t}=E/(\hbar c)$, $\vec k_{\Phi}=\vec p/\hbar$ | The three wave numbers of $\tilde K_{\Phi}=\left(k_m/c\right)\tilde V_{\Phi}$ |
| $\rho=\gamma\rho_{0}$, $\vec j=\rho\vec v$ | Charge density and current of $\tilde J_{\Phi}=\rho_{0}\tilde V_{\Phi}$ |
| $\theta_{\mathrm{rpd}} = \operatorname{artanh}\beta$ | Rapidity; the additive parameter of the boost |
| $r'_{t} = c\,t$ | Material time |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (4th ed., Butterworth–Heinemann, 1975), §9, for the expansion of the relativistic energy and momentum.
- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics* (3rd ed., Addison–Wesley, 2002), chapter 7, for the relativistic kinetic energy and its low-speed expansion.
- John David Jackson, *Classical Electrodynamics* (3rd ed., Wiley, 1999), §11.5 and §11.10, for the same expansion on a charge in an external field.
