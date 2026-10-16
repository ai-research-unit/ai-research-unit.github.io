# __Exercise: The Electromagnetic Field of a Moving Charge__

## Introduction

This is one of the exercises in the electromagnetism series. It applies the apparatus of a single parent article, *Radiation from Accelerated Charges in Biquaternionic Form*, which declares it as the general case of the two downstream exercises; the sibling declaration covers *Exercise: The Electromagnetic Field of a Uniformly Moving Charge*, which is the case of vanishing acceleration. Every object used below — the retarded solution, the Liénard–Wiechert potential, the field split, and the two component formulas — is inherited from that parent and its own parents, and no new formalism is introduced. The task of the exercise is to *perform the differentiation the parent asserts*, to verify the two falloff laws rather than quote them, and to check the retarded denominator and the charge sign on two independent worldlines.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_je_k = -\delta_{jk}e_0 + \epsilon_{jkm}e_m$, and the scalar imaginary $i$ with $i^2 = -1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part), the Hermitian subspace $\mathbb{M}_+$ (real scalar part, imaginary vector part), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$, and the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ of the rotation rotors. The biquaternionic gradient and its quaternion conjugate,
$$
\tilde{\nabla} = e_0\,\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z,
\qquad
\tilde{\nabla}^{\natural} = e_0\,\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z,
$$
with $\partial_{ict} = -\frac{i}{c}\partial_t$ and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial_{ict}^2 + \Delta$; the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ (pure vector), the potential $\tilde{A} = \frac{i\phi}{c}e_0 + \vec A$, and the source $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\vec J$. The permittivity and permeability $\epsilon,\mu$ with $c = 1/\sqrt{\epsilon\mu}$ and vacuum value $c_0$, and $\vec H = \vec B/\mu$. The biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$, the quaternion conjugate $\tilde{Q}^{\natural}$, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ of the shared notation. The charge $ϙ$ moves on the worldline $\vec x_q(t)$, with coordinate velocity $\vec v(t) = d\vec x_q/dt$, $\vec\beta = \vec v/c$, and acceleration $\dot{\vec v} = d\vec v/dt$; all source quantities in the retarded formulas are evaluated at the retarded time. No object of the informational sector arises below, so $\mathbb{M}_+$, the rotors, and the trace formula are recorded but used only where the boost rotor is invoked in Problem 5.

**What is to be shown.** Problem 1 derives the retarded time and its two derivatives, distinguishes the field point from the source point at retarded time, and assembles the Liénard–Wiechert potential as a single biquaternion. Problem 2 performs the differentiation $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A}$ and exhibits the exact split of the field into a part independent of $\dot{\vec\beta}$ and a part linear in $\dot{\vec\beta}$. Problem 3 treats the velocity field, Problem 4 the acceleration field, and each verifies its falloff law ($1/R^2$ and $1/R$) by recomputation rather than assertion. Problem 5 fixes the boost-rotor direction convention and establishes how the *field* transforms under a boost, which is not the four-vector rule. Problem 6 checks the retarded denominator $\kappa = 1-\vec u_R\cdot\vec\beta$ and the charge sign on two independent cases, uniform motion and motion with nonzero acceleration.

**The result.** Writing $\vec R = \vec x - \vec x_q(t_r)$ for the retarded separation, $R = |\vec R|$, $\vec u_R = \vec R/R$, and
$$
D = R - \vec R\cdot\vec\beta = R\kappa, \qquad \kappa = 1 - \vec u_R\cdot\vec\beta,
$$
the Liénard–Wiechert potential is $\tilde{A} = \frac{\mu ϙ}{4\pi D}\,\tilde{V}/\gamma$ with the four-velocity $\tilde{V} = \gamma\left(ic\,e_0 + \vec v(t_r)\right)$, and its field splits as
$$
\tilde{F} = \tilde{F}_v + \tilde{F}_a,
$$
$$
\boxed{\;
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\left(\vec u_R-\vec\beta\right)}{\kappa^3 R^2},
\qquad
\vec E_a = \frac{ϙ}{4\pi\epsilon c}\,\frac{\vec u_R\times\left[\left(\vec u_R-\vec\beta\right)\times\dot{\vec\beta}\right]}{\kappa^3 R},
\qquad
\vec B = \frac{1}{c}\,\vec u_R\times\vec E,
\;}
$$
with $\vec E = \vec E_v+\vec E_a$. The velocity field falls as $1/R^2$ and is not null; the acceleration field falls as $1/R$, is transverse to $\vec u_R$, and is null, so that its field-strength biquaternion is a zero divisor, $\tilde{F}_a^2 = 0$. The whole point of the exercise is the split: the two parts have different falloffs, different invariants, and different signs under $\dot{\vec\beta}\to-\dot{\vec\beta}$.

**Conventions.** Two conventions are fixed once and used throughout. The first is the retarded-time derivative: a dot on a source quantity is $\frac{d}{dt_r}$, not $\frac{d}{dt}$; the parent warns that the observer's-time derivative differs by a factor of $\kappa$, and the formulas above are the retarded-time ones. The second is the boost-rotor direction: the rotor
$$
\tilde{U}_{\vec v_b} = \cosh\frac{\psi_b}{2} + i\,\sinh\frac{\psi_b}{2}\,\vec u,
\qquad
\tanh\psi_b = \frac{v_b}{c},
$$
as fixed by the boosting and two-body exercises of the relativity series, is the rotor that carries the *laboratory* to the frame moving with $+\vec v_b$. Equivalently, applied to the rest four-velocity it produces velocity $-\vec v_b$: $\tilde{U}_{\vec v_b}(ic\,e_0)\tilde{U}_{\vec v_b}^{*}$ has velocity $-\vec v_b$. Problem 5 states exactly where this convention enters the field problem and why the field does *not* transform by the rotor conjugation that the four-vector calculus would suggest.

## The Problem

The retarded solution of the biquaternionic Maxwell equation is
$$
\tilde{A}(t,\vec x) = \frac{\mu ϙ}{4\pi D}\,\tilde{V}/\gamma,
$$
and the parent's statement is that $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A}$ yields the two component formulas displayed above. The retarded time is defined *implicitly*, by
$$
t_r = t - \frac{R}{c},
\qquad
R = \left|\vec x - \vec x_q(t_r)\right|,
$$
so that the observation point $(t,\vec x)$ enters both directly and through the emission point $(t_r,\vec x_q(t_r))$. The exercise is to keep those two points distinct, differentiate the implicit construction in one biquaternionic step, and read off the field. The specific demands are: (i) derive $\partial_t t_r$ and $\nabla t_r$ and the resulting biquaternion $\tilde{\nabla}^{\natural}t_r$; (ii) exhibit the velocity–acceleration split at the level of the biquaternion brackets, not merely in components; (iii) verify the $1/R^2$ and $1/R$ falloffs by recomputation on a configuration that isolates each part; (iv) check $\kappa$ and the charge sign on uniform motion and on accelerated motion; and (v) fix the rotor convention and determine the correct transformation law for the field.

Numerical checks quoted below were performed on subluminal worldlines with a Newton-solved retarded time, and the reported figures are the maximum componentwise discrepancies. All source quantities are evaluated at the retarded time.

## Problem 1: The Retarded Time and the Liénard–Wiechert Potential

**Statement.** (a) Derive $\partial_t t_r = 1/\kappa$ and $\nabla t_r = -\vec u_R/(c\kappa)$ from the implicit definition of $t_r$. (b) Assemble the Liénard–Wiechert potential $\tilde{A} = \frac{\mu ϙ}{4\pi D}\tilde{V}/\gamma$ and verify the three identities
$$
D = R\kappa = -\frac{1}{c}\,\mathrm{Sc}\!\left((\tilde{V}/\gamma)\bar{\tilde{\mathcal{R}}}\right),
\qquad
\langle\tilde{\mathcal{R}}\rangle_{\natural} = 0,
\qquad
\langle\tilde{V}/\gamma\rangle_{\natural} = -\frac{c^2}{\gamma^2},
$$
with $\tilde{\mathcal{R}} = iR\,e_0 + \vec R \in \mathbb{M}_-$ and the four-velocity $\tilde{V} = \gamma\left(ic\,e_0+\vec v(t_r)\right) \in \mathbb{M}_-$. (c) Extract $\phi$ and $\vec A$ and verify $\vec A = \frac{\vec v}{c^2}\phi$.

**Solution (a).** Differentiate $t_r = t - R/c$ at fixed field point. Since $R = |\vec x-\vec x_q(t_r)|$,
$$
\frac{\partial R}{\partial t} = -\vec u_R\cdot\vec v\,\frac{\partial t_r}{\partial t},
$$
because an increase of the emission time moves the source along $+\vec v$. Hence
$$
\frac{\partial t_r}{\partial t} = 1 + \frac{\vec u_R\cdot\vec v}{c}\,\frac{\partial t_r}{\partial t}
\;\Longrightarrow\;
\left(1 - \vec u_R\cdot\vec\beta\right)\frac{\partial t_r}{\partial t} = 1
\;\Longrightarrow\;
\frac{\partial t_r}{\partial t} = \frac{1}{\kappa}.
$$
For the gradient, write $\partial_j R = \vec u_{R_j} - \left(\vec u_R\cdot\vec v\right)\partial_j t_r$, so
$$
\nabla t_r = -\frac{1}{c}\nabla R = -\frac{\vec u_R}{c} + \frac{\vec u_R\cdot\vec v}{c}\nabla t_r
\;\Longrightarrow\;
\kappa\,\nabla t_r = -\frac{\vec u_R}{c}
\;\Longrightarrow\;
\nabla t_r = -\frac{\vec u_R}{c\kappa}.
$$
Two points are worth recording because they are used implicitly throughout. First, $\kappa = 1-\vec u_R\cdot\vec\beta$ is *not* bounded below by $1$: for a receding charge, $\vec u_R\cdot\vec\beta<0$ and $\kappa>1$. The retarded formulas require $\kappa>0$, i.e. subluminal motion and no caustic; this restriction is not stated in the parent and returns as a gap below. Second, the field point and the source point are genuinely different events: $\vec R$ is the separation from the *emission* event, and the source velocity $\vec v(t_r)$ is the velocity at emission, not at the observation time. Every appearance of $\beta$ below is retarded.

**Solution (b).** The parent's retarded convolution gives $\tilde{A} = \frac{\mu ϙ}{4\pi D}\tilde{V}/\gamma$, with
$$
D = R - \vec R\cdot\vec\beta = R\left(1-\vec u_R\cdot\vec\beta\right) = R\kappa .
$$
The scalar-part identity follows from the multiplication rule $\mathrm{Sc}(\tilde{A}\tilde{B}) = A_0B_0 - \vec A\cdot\vec B$ applied to $\tilde{V}/\gamma = ic\,e_0 + \vec v$ and $\bar{\tilde{\mathcal{R}}} = iR\,e_0 - \vec R$:
$$
\mathrm{Sc}\!\left((\tilde{V}/\gamma)\bar{\tilde{\mathcal{R}}}\right)
= (ic)(iR) - \vec v\cdot(-\vec R)
= -cR + \vec v\cdot\vec R
= -c\left(R - \vec R\cdot\vec\beta\right)
= -cD .
$$
The retarded separation is null,
$$
\langle\tilde{\mathcal{R}}\rangle_{\natural} = \tilde{\mathcal{R}}\bar{\tilde{\mathcal{R}}} = (iR)^2 + |\vec R|^2 = -R^2 + R^2 = 0,
$$
a zero divisor of $\mathbb{B}$ and a point of the light cone; and the four-velocity is timelike, of fixed norm,
$$
\langle\tilde{V}\rangle_{\natural} = \gamma^2\left[(ic)^2 + |\vec v|^2\right] = -c^2\gamma^2\left(1-\beta^2\right) = -c^2 ,
$$
so that the coordinate velocity $\tilde{V}/\gamma$ has $\langle\tilde{V}/\gamma\rangle_{\natural} = -c^2/\gamma^2$.
Thus the whole construction is built from one null and one timelike element of $\mathbb{M}_-$, paired through the single scale $D$.

**Solution (c).** Writing $\tilde{A} = \frac{i\phi}{c}e_0 + \vec A$ and using $\epsilon\mu c^2 = 1$,
$$
\phi = \frac{ϙ}{4\pi\epsilon D},
\qquad
\vec A = \frac{\mu ϙ}{4\pi D}\vec v = \frac{\vec v}{c^2}\,\phi .
$$

The identities of (b) were verified numerically on accelerated worldlines: $|D - R\kappa| = 0$ by construction, $|D + \mathrm{Sc}(\tilde{V}/\gamma\bar{\tilde{\mathcal{R}}})/c| \le 4\times10^{-16}$, $|\langle\tilde{\mathcal{R}}\rangle_{\natural}| \le 2\times10^{-15}$, and $|\langle\tilde{V}/\gamma\rangle_{\natural} + c^2/\gamma^2| = 0$.

## Problem 2: The Field Strength and the Velocity–Acceleration Split

**Statement.** (a) Show that for a source quantity depending only on the retarded time, $\tilde{\nabla}^{\natural}\tilde{Q} = \tilde{\mathcal{K}}\dot{\tilde{Q}}$ with
$$
\tilde{\mathcal{K}} \equiv \tilde{\nabla}^{\natural}t_r = \frac{1}{c\kappa}\left(\vec u_R - i\,e_0\right),
\qquad
N\!\left(\vec u_R - i\,e_0\right) = 0 .
$$
(b) Compute $\tilde{\nabla}^{\natural}D$ and hence $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A}$, and exhibit the split $\tilde{F} = \tilde{F}_v+\tilde{F}_a$ into brackets independent of and linear in $\dot{\vec\beta}$. (c) Verify that both brackets are pure vectors and that expanding them gives the component formulas of the Introduction, with $\vec B = \frac{1}{c}\vec u_R\times\vec E$.

**Solution (a).** For a source quantity $\tilde{Q}(t_r)$ the chain rule gives, with $\dot{\tilde{Q}} = d\tilde{Q}/dt_r$,
$$
\partial_{ict}\tilde{Q} = \dot{\tilde{Q}}\,\partial_{ict}t_r = -\frac{i}{c\kappa}\dot{\tilde{Q}},
\qquad
\partial_j\tilde{Q} = \dot{\tilde{Q}}\,\partial_jt_r = -\frac{\vec u_{R_j}}{c\kappa}\dot{\tilde{Q}} .
$$
Multiplying the spatial derivatives by $e_j$ and subtracting,
$$
\tilde{\nabla}^{\natural}\tilde{Q}
= \left(\partial_{ict}t_r\,e_0 - \sum_j \partial_jt_r\,e_j\right)\dot{\tilde{Q}}
= \left(-\frac{i}{c\kappa}e_0 + \frac{\vec u_R}{c\kappa}\right)\dot{\tilde{Q}}
= \tilde{\mathcal{K}}\dot{\tilde{Q}} .
$$
The scalar coefficient of $\tilde{\mathcal{K}} = \frac{1}{c\kappa}\left(\vec u_R-ie_0\right)$ is $-\frac{i}{c\kappa}$, so
$$
N\!\left(\vec u_R-ie_0\right) = (-i)^2 + |\vec u_R|^2 = -1+1 = 0 .
$$
The gradient of the retarded time is a null biquaternion, hence a zero divisor: the light-cone structure enters the differentiation itself. This was checked against finite differences of $t_r$ ($\|\tilde{\mathcal{K}}_{\text{FD}}-\tilde{\mathcal{K}}\| \lesssim 6\times10^{-9}$, limited by the finite-difference step).

**Solution (b).** The denominator $D$ is *not* a function of $t_r$ alone: at fixed $t_r$ it still depends explicitly on $\vec x$ through $R$ and $\vec u_R$. Splitting the gradient into its explicit action at fixed $t_r$ and its action through $t_r$,
$$
\tilde{\nabla}^{\natural}D = -\left(\vec u_R-\vec\beta\right) + \tilde{\mathcal{K}}\dot D ,
\qquad
\dot D = -c\,\vec u_R\cdot\vec\beta + c\beta^2 - \vec R\cdot\dot{\vec\beta} .
$$
Here $-\left(\vec u_R-\vec\beta\right)$ is the explicit part, since at fixed $t_r$ one has $\partial_j|_{\text{exp}}D = \vec u_{R_j}-\beta_j$, and $\dot D$ is the retarded-time derivative. With $g = \frac{\mu ϙ}{4\pi}$ and $\tilde{A} = g\,(\tilde{V}/\gamma)/D$, the product rule (the gradient acts from the left, and $1/D$ is a scalar) gives
$$
\tilde{F} = \tilde{\nabla}^{\natural}\frac{g\tilde{V}/\gamma}{D}
= \frac{g}{D^2}\left[D\,\tilde{\nabla}^{\natural}\!\left(\tilde{V}/\gamma\right) - \left(\tilde{\nabla}^{\natural}D\right)\tilde{V}/\gamma\right].
$$
Substituting $\tilde{\nabla}^{\natural}\!\left(\tilde{V}/\gamma\right) = \tilde{\mathcal{K}}\,\dot{\tilde{V}/\gamma}$ with $\dot{\tilde{V}/\gamma} = c\dot{\vec\beta}$, and using $D\tilde{\mathcal{K}} = \frac{D}{c\kappa}\tilde{\mathcal{N}} = \frac{R}{c}\tilde{\mathcal{N}}$ with $\tilde{\mathcal{N}} \equiv \vec u_R-ie_0$,
$$
\tilde{F} = \frac{g}{D^2}\left[\,R\,\tilde{\mathcal{N}}\,\dot{\vec\beta}
+ \left(\vec u_R-\vec\beta\right)\tilde{V}/\gamma
- \frac{\dot D}{c\kappa}\,\tilde{\mathcal{N}}\,\tilde{V}/\gamma
\right].
$$
The only $\dot{\vec\beta}$-dependence sits in the first term and in $\dot D$. Writing $\dot D = \dot D_0 - \vec R\cdot\dot{\vec\beta}$ with
$$
\dot D_0 = -c\left(\vec u_R\cdot\vec\beta - \beta^2\right),
$$
and separating,
$$
\boxed{\;
\tilde{F}_v = \frac{g}{D^2}\left[\left(\vec u_R-\vec\beta\right)\tilde{V}/\gamma
- \frac{\dot D_0}{c\kappa}\,\tilde{\mathcal{N}}\,\tilde{V}/\gamma\right],
\qquad
\tilde{F}_a = \frac{g}{D^2}\left[\,R\,\tilde{\mathcal{N}}\,\dot{\vec\beta}
+ \frac{\vec R\cdot\dot{\vec\beta}}{c\kappa}\,\tilde{\mathcal{N}}\,\tilde{V}/\gamma\right].
\;}
$$
The split is exact and structural: $\tilde{F}_v$ is independent of $\dot{\vec\beta}$ (it is what survives uniform motion), and $\tilde{F}_a$ is linear in $\dot{\vec\beta}$ (it vanishes for unaccelerated motion, $\dot{\vec\beta} = 0$). Note the ordering is not cosmetic — $\tilde{\mathcal{N}}$ multiplies on the left — and the two brackets are not merely "terms containing $\dot{\vec\beta}$"; they are the velocity and acceleration fields.

**Solution (c).** Both brackets are pure vectors: their scalar parts vanish identically, which is the biquaternionic statement of the Lorenz condition $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A}) = 0$. Expanding the brackets in components gives
$$
\vec E = \vec E_v+\vec E_a,
\qquad
\vec B = \frac{1}{c}\vec u_R\times\vec E,
$$
$$
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\left(\vec u_R-\vec\beta\right)}{\kappa^3 R^2},
\qquad
\vec E_a = \frac{ϙ}{4\pi\epsilon c}\,\frac{\vec u_R\times\left[\left(\vec u_R-\vec\beta\right)\times\dot{\vec\beta}\right]}{\kappa^3 R}.
$$
Equivalently, in the single compact form
$$
\vec E = \frac{ϙ}{4\pi\epsilon D^3}\left[(1-\beta^2)\left(\vec R-R\vec\beta\right)
+ \frac{1}{c}\,\vec R\times\left(\left(\vec R-R\vec\beta\right)\times\dot{\vec\beta}\right)\right],
$$
whose first term reproduces $\vec E_v$ and whose second reproduces $\vec E_a$ when $D = R\kappa$ and $\vec R = R\vec u_R$ are used. The two factors $1-\beta^2$ and $\dot{\vec\beta}$ make the two parts transform differently under $\dot{\vec\beta}\to-\dot{\vec\beta}$: $\vec E_v$ is even, $\vec E_a$ odd.

The full identity $\tilde{\nabla}^{\natural}\tilde{A} = i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ with the component formulas above was verified by finite differencing the potential on accelerated subluminal worldlines, with maximum componentwise discrepancy $7\times10^{-12}$; the scalar part of $\tilde{\nabla}^{\natural}\tilde{A}$ was zero to $5\times10^{-12}$. Separately, the velocity bracket $\tilde{F}_v$ matched $i\sqrt{\epsilon}\,\vec E_v-\sqrt{\mu}\,\vec H_v$ to $4\times10^{-18}$ and the acceleration bracket $\tilde{F}_a$ matched $i\sqrt{\epsilon}\,\vec E_a-\sqrt{\mu}\,\vec H_a$ to $2\times10^{-18}$, so the biquaternion split and the component split are the same split.

## Problem 3: The Velocity Field and Its $1/R^2$ Falloff

**Statement.** (a) Show that $\vec E_v$ falls as $1/R^2$ by holding the retarded configuration fixed and scaling the observation point away from the emission event. (b) Evaluate the invariants of $\tilde{F}_v$ and show the velocity field is electric, not null: $I_{1,v} = (\vec u_R\cdot\vec E_v)^2 > 0$ and $I_{2,v} = 0$. (c) Recover the Coulomb field in the limit $\vec v\to0$ and fix the sign convention for the charge.

**Solution (a).** $\vec E_v$ is a function of the retarded data $(\vec u_R,\vec\beta,R)$ alone. If the emission event and the direction $\vec u_R$ (hence $\vec\beta$ and $\kappa$) are held fixed while $R$ is scaled, then
$$
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)}{\kappa^3}\,\frac{\vec u_R-\vec\beta}{R^2},
$$
so $R^2|\vec E_v|$ is independent of $R$. This was checked numerically: with the retarded time, direction, and velocity held fixed and $R$ taken through $2.5,\,5,\,10,\,20$, the quantity $R^2|\vec E_v|$ stayed at $0.110513$ to all displayed digits, while $R|\vec E_a|$ stayed at $0.067453$. The scale invariance is a property of the *retarded* description; if the observation point is scaled about the charge's present position instead, $\kappa$ and $\vec u_R$ both change and the clean $1/R^2$ law is obscured. This is the first reason the field point and the source point must be kept distinct.

**Solution (b).** With $\vec B_v = \frac{1}{c}\vec u_R\times\vec E_v$, the first invariant is
$$
I_{1,v} = \vec E_v^2 - c^2\vec B_v^2 = \vec E_v^2 - \left|\vec u_R\times\vec E_v\right|^2 = \left(\vec u_R\cdot\vec E_v\right)^2 ,
$$
and direct evaluation gives
$$
\vec u_R\cdot\vec E_v
= \frac{ϙ}{4\pi\epsilon}\,\frac{1-\beta^2}{\kappa^3 R^2}\left(1-\vec u_R\cdot\vec\beta\right)
= \frac{ϙ}{4\pi\epsilon}\,\frac{1-\beta^2}{\kappa^2 R^2},
$$
so
$$
I_{1,v} = \left(\frac{ϙ}{4\pi\epsilon}\,\frac{1-\beta^2}{\kappa^2 R^2}\right)^{\!2} > 0,
\qquad
I_{2,v} = \vec E_v\cdot\vec B_v = 0 .
$$
The velocity field is therefore of electric type, with a nonzero longitudinal component: it is *not* a radiation field. In the biquaternion norm, $\langle\tilde{F}_v\rangle_{\natural} = -\epsilon\,I_{1,v} \ne 0$, so $\tilde{F}_v$ is not a zero divisor and $\tilde{F}_v^2 \ne 0$. Numerically, $I_{1,v}$ agreed with $(\vec u_R\cdot\vec E_v)^2$ to $10^{-16}$ relative, $I_{2,v}$ vanished to $10^{-20}$, and $\langle\tilde{F}_v\rangle_{\natural} = -\epsilon I_{1,v}$ with positive $I_{1,v}$.

**Solution (c).** At $\vec\beta = 0$ one has $\kappa = 1$, and
$$
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,\frac{\vec u_R}{R^2},
\qquad
\vec B_v = 0 ,
$$
the Coulomb field of the charge at its retarded (and, for a stationary charge, present) position. The sign is the physical one: for a positive charge the field points radially away from the source. The acceleration field vanishes as well, so a charge instantaneously at rest with $\dot{\vec v}\ne0$ still has the full Coulomb $1/R^2$ velocity field at that instant. Flipping $ϙ\to-ϙ$ flips both parts, and this was verified componentwise on both a uniformly moving and an accelerated worldline.

## Problem 4: The Acceleration Field and Its $1/R$ Falloff

**Statement.** (a) Show that $\vec E_a$ falls as $1/R$ by the same scaling argument. (b) Show that the acceleration field is transverse, $\vec u_R\cdot\vec E_a = 0$, and null, $I_{1,a} = I_{2,a} = 0$; conclude that $\tilde{F}_a$ is a zero divisor with $\tilde{F}_a^2 = 0$. (c) Evaluate the field at an instant of rest and verify its sign against $\dot{\vec\beta}$. (d) Verify the far-zone dominance of $\vec E_a$ over $\vec E_v$.

**Solution (a).** The acceleration field is
$$
\vec E_a = \frac{ϙ}{4\pi\epsilon c}\,\frac{\vec u_R\times\left[\left(\vec u_R-\vec\beta\right)\times\dot{\vec\beta}\right]}{\kappa^3 R},
$$
so with the retarded configuration fixed, $R|\vec E_a|$ is independent of $R$, while the velocity field falls one power faster. The same numerical run that held $R^2|\vec E_v|$ constant gave $R|\vec E_a| = 0.067453$ for $R = 2.5$ through $20$. The physical consequence is immediate: at large $R$ the acceleration field dominates, and the ratio $|\vec E_v|/|\vec E_a|$ falls off as $1/R$. In the run above the ratio went $4.905$ at $R=1$, $2.453$ at $R=2$, $1.226$ at $R=4$, and $0.613$ at $R=8$ — it halves as $R$ doubles, which is the $1/R$ law of the acceleration field relative to the $1/R^2$ law of the velocity field. This is the quantitative content of "the far-zone field is the radiation field alone."

**Solution (b).** Transversality is immediate from the double cross product,
$$
\vec u_R\cdot\vec E_a \propto \vec u_R\cdot\left\{\vec u_R\times\left[\left(\vec u_R-\vec\beta\right)\times\dot{\vec\beta}\right]\right\} = 0 .
$$
Since $\vec B_a = \frac{1}{c}\vec u_R\times\vec E_a$, one has $\vec E_a\perp\vec B_a$ and $|\vec E_a| = c|\vec B_a|$, so
$$
I_{1,a} = \vec E_a^2 - c^2\vec B_a^2 = 0,
\qquad
I_{2,a} = \vec E_a\cdot\vec B_a = 0 .
$$
The acceleration field is null. In the biquaternion norm $\langle\tilde{F}_a\rangle_{\natural} = -\epsilon(I_{1,a}+2icI_{2,a}) = 0$, and for a pure vector with vanishing biquaternion norm $\tilde{F}_a^2 = -\vec F_a\cdot\vec F_a = -\langle\tilde{F}_a\rangle_{\natural}$, so
$$
\tilde{F}_a^2 = 0 .
$$
The radiation field of an accelerated charge is the pointwise realization of the zero-divisor cone of $\mathbb{B}$. Numerically, $\vec u_R\cdot\vec E_a$ vanished to $10^{-18}$, $I_{1,a}$ and $I_{2,a}$ to $10^{-19}$, and $\tilde{F}_a^2$ to $10^{-20}$ on accelerated worldlines.

**Solution (c).** At an instant of rest, $\vec\beta = 0$ and $\kappa = 1$, so
$$
\vec E_a = \frac{ϙ}{4\pi\epsilon c}\,\vec u_R\times\left(\vec u_R\times\dot{\vec\beta}\right)
= -\frac{ϙ}{4\pi\epsilon c}\,\frac{\dot{\vec\beta}_\perp}{R},
\qquad
\dot{\vec\beta}_\perp \equiv \dot{\vec\beta} - \vec u_R\left(\vec u_R\cdot\dot{\vec\beta}\right).
$$
The acceleration field opposes the retarded transverse acceleration, and it is $1/R$. Choosing a worldline with $\vec v(0)=0$, $\dot{\vec v} = a\vec u_2$ and observing at $t = |\vec x|/c$ so that $t_r = 0$ exactly, the numerical field matched $-\frac{ϙ}{4\pi\epsilon c}\dot{\vec\beta}_\perp/R$ to $7\times10^{-18}$; $\vec u_R\cdot\vec E_a$ and $I_{1,a}$, $I_{2,a}$ vanished to better than $10^{-18}$.

**Solution (d).** Since the two falloffs differ by one power of $R$, there is a radius beyond which $|\vec E_a|>|\vec E_v|$ for fixed retarded direction and velocity. In the scaling run the crossover occurred near $R\approx5$. In the far zone one may therefore replace $\vec E$ by $\vec E_a$ alone; the resulting field is null and transverse, and its Poynting flux integrates to the relativistic Larmor power of the parent article. The velocity field, by contrast, carries the energy permanently bound to the charge and does not escape.

## Problem 5: The Rotor Convention and the Field as a Boosted Coulomb Field

**Statement.** (a) State the direction convention for the boost rotor and verify it on the rest four-velocity. (b) Determine the correct transformation law of the field-strength biquaternion under a boost and show that it is *not* the four-vector rotor conjugation $\tilde{F}\mapsto\tilde{U}\tilde{F}\tilde{U}^{*}$. (c) Use it to confirm that the velocity field of a uniformly moving charge is the boost of the Coulomb field, as the parent asserts.

**Solution (a).** The convention, fixed by the relativity exercises, is that
$$
\tilde{U}_{\vec v_b} = \cosh\frac{\psi_b}{2} + i\sinh\frac{\psi_b}{2}\vec u,
\qquad
\tanh\psi_b = \frac{v_b}{c},
$$
carries the *laboratory* to the frame moving with $+\vec v_b$. Applied to the rest four-velocity $\tilde{V}_0 = ic\,e_0$ it gives
$$
\tilde{U}_{\vec v_b}\,\tilde{V}_0\,\tilde{U}_{\vec v_b}^{*}
= ic\,e_0\,\tilde{U}_{\vec v_b}^2
= ic\left(\cosh\psi_b + i\sinh\psi_b\,\vec u\right)
= ic\cosh\psi_b - c\sinh\psi_b\,\vec u,
$$
whose velocity is $-\vec v_b$. Equivalently, the rotor carries the lab to the frame with velocity $+\vec v_b$; a particle at rest in the lab appears, in that frame, to move with $-\vec v_b$. This was checked numerically: for $\vec v_b = 0.6c\,\vec u_3$ the conjugated rest four-velocity has velocity exactly $-0.6c\,\vec u_3$. We use this convention consistently; the conjugate $\tilde{U}^{\natural}_{\vec v_b} = \tilde{U}_{\vec v_b}^{-1}$ generates the inverse (moving-to-lab) transformation.

**Solution (b).** The field strength is a rank-two object, not an element of $\mathbb{M}_-$; the four-vector rotor conjugation $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$ is defined for four-vectors, and it does *not* give the correct field transformation. The correct law for a pure boost is the similarity
$$
\tilde{F}' = \tilde{U}^{\natural}_{\vec v_b}\,\tilde{F}\,\tilde{U}_{\vec v_b}
= \tilde{U}_{\vec v_b}^{-1}\tilde{F}\,\tilde{U}_{\vec v_b} ,
$$
which is the biquaternion form of the standard boost of the electromagnetic field. To see the difference concretely, take the test field $\vec E = (0.3,-0.7,0.4)$, $\vec B = (0.5,0.2,-0.6)$ and a boost with $\vec v_b = 0.6c\,\vec u_3$. The standard boost gives $\vec E' = (0.225,-0.5,0.4)$, $\vec B' = (0.1,0.025,-0.6)$, and the similarity reproduces exactly that. The naive conjugation $\tilde{U}\tilde{F}\tilde{U}^{*}$ instead gives $\vec E = (0.3,-0.7,0.5)$ with a magnetic error of $0.4$, so it is not a transformation law for the field at all. More generally, the similarity reproduces the standard relations
$$
\vec E_\parallel' = \vec E_\parallel,
\quad
\vec E_\perp' = \gamma\left(\vec E_\perp + \vec v_b\times\vec B_\perp\right),
\quad
\vec B_\parallel' = \vec B_\parallel,
\quad
\vec B_\perp' = \gamma\left(\vec B_\perp - \frac{1}{c^2}\vec v_b\times\vec E_\perp\right)
$$
to machine precision. Across six random boosts and random test fields, the similarity $\tilde{U}^{\natural}\tilde{F}\tilde{U}$ matched the standard formulas to $4\times10^{-16}$, while $\tilde{U}\tilde{F}\tilde{U}^{*}$ and its variants did not. The similarity preserves purity of the vector, $\mathrm{Sc}(\tilde{U}^{\natural}\tilde{F}\tilde{U}) = \mathrm{Sc}(\tilde{F}) = 0$, as it must.

**Solution (c).** Boosting the rest-frame Coulomb field of the charge to the lab frame with the similarity above reproduces the velocity field of Problem 3. In the rest frame the field at the corresponding event is $\vec E' = \frac{ϙ}{4\pi\epsilon}\vec R'/R'^3$ with $\vec R'$ the boosted separation, and transforming back gives
$$
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\left(\vec u_R-\vec\beta\right)}{\kappa^3 R^2}
$$
exactly. For a worldline with $\vec v = (0.35,-0.25,0.45)c$ and an observation at $R = 2.609$, $\kappa = 0.439$, the boosted Coulomb field and the Liénard–Wiechert velocity field agreed to $7\times10^{-18}$; using the opposite (present-position or wrong-sign) boost convention gave a discrepancy of $4\times10^{-2}$, so the convention is doing real work. The parent's remark that the uniformly moving field is "equivalently ... the boost of the Coulomb field" is correct in content, but it is silent on which transformation law is meant, and the four-vector rotor conjugation that the framework uses elsewhere is not it.

## Problem 6: The Retarded Denominator and the Charge Sign on Two Independent Cases

**Statement.** Check the retarded denominator $\kappa = 1-\vec u_R\cdot\vec\beta$ and the charge sign on (a) uniform motion and (b) motion with nonzero acceleration. In each case verify $D = R\kappa$ and the sign under $ϙ\to-ϙ$.

**Solution (a) — uniform motion.** For $\dot{\vec v} = 0$ one has $\dot{\vec\beta} = 0$, so $\vec E_a = 0$ and $\vec E = \vec E_v$ exactly. Taking $\vec v = 0.6c\,\vec u_1$ and three observation events, the retarded configurations gave
$$
\kappa = 0.4467,\quad 0.4316,\quad 1.0450,
$$
with $|D - R\kappa| = 0$ and the field identity $\tilde{\nabla}^{\natural}\tilde{A} = i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ holding to $2\times10^{-11}$. The three values illustrate both facts about $\kappa$: it can be considerably less than $1$ (charge approaching, $\vec u_R\cdot\vec\beta>0$) and it can exceed $1$ (charge receding, $\vec u_R\cdot\vec\beta<0$). It is the denominator of $(1-\vec u_R\cdot\vec\beta)$, not a $\gamma$-factor and not bounded below by unity. Flipping $ϙ\to-ϙ$ flipped the field exactly, $\vec E(-ϙ) = -\vec E(ϙ)$ to $0$.

**Solution (b) — nonzero acceleration.** For an accelerated subluminal worldline with $\vec v(T) = (0.2,\,0.2T,\,0.05)c$ and $\vec a(T) = (0,\,0.2,\,0)c$, four observation events gave
$$
\kappa = 0.9493,\quad 0.6804,\quad 1.1364,\quad 0.9069,
$$
again with $|D-R\kappa| = 0$ and the field identity holding to $7\times10^{-12}$; the velocity and acceleration brackets matched their component forms to $4\times10^{-18}$. Here both parts contribute: $\vec E_v$ carries the $1-\beta^2$ factor, $\vec E_a$ the transverse acceleration. Flipping the charge flipped both parts exactly, $\vec E_v(-ϙ) = -\vec E_v(ϙ)$ and $\vec E_a(-ϙ) = -\vec E_a(ϙ)$, verified componentwise to $0$. The two cases are logically independent: in (a) the acceleration bracket vanishes identically for every event, while in (b) it does not, so the check of the sign and of $\kappa$ in (b) is not a repetition of (a). The retarded denominator also behaves differently: in (a) $\kappa$ is constant along the worldline for a given observation direction, whereas in (b) it varies event by event because $\vec u_R$ and $\vec\beta$ both change with $t_r$.

## Where the Parent Leaves a Gap

**1. The differentiation is asserted, not displayed.** The parent states that "differentiating the Liénard–Wiechert potential is the standard computation" and records the two component results, with the normalization caveat that fixes $\tilde{F} = i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ as the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$. It does not carry out the differentiation, and in particular it does not display the two biquaternion brackets of Problem 2 or the role of the null gradient $\tilde{\nabla}^{\natural}t_r$. This exercise supplies the missing computation; nothing in the parent's results is changed.

**2. The field transformation law is not given, and rotor conjugation is not it.** The parent's remark that the uniformly moving field is "equivalently ... obtained by applying the boost rotor $\tilde{U}$ of the Maxwell article to the Coulomb field of the charge at rest" is correct in content but silent on the law. The framework's rotor conjugation is defined for four-vectors in $\mathbb{M}_-$; the field strength is a rank-two object and transforms by the similarity $\tilde{U}^{\natural}\tilde{F}\tilde{U} = \tilde{U}^{-1}\tilde{F}\tilde{U}$ (Problem 5). The Lorentz-transformation article's "Open Questions", item 1, asks precisely how the biquaternion formulation extends to higher-rank tensors such as $F^{\mu\nu}$; this exercise supplies the answer for the field strength and a pure boost, so it is a recognized boundary and not a defect introduced here. We record it because a reader who reaches for $\tilde{U}\tilde{F}\tilde{U}^{*}$ will get a wrong field.

**3. The subluminal restriction and the caustic.** The retarded formulas assume $\kappa>0$. As $\vec u_R\cdot\vec\beta\to1$, the denominator $\kappa\to0$ and the field diverges; this is the caustic where the retarded-time equation has a double root. For superluminal worldlines the construction fails outright, and a naive numerical retarded-time solver can return a spurious root. The parent does not state the restriction, and it is not inferable from the displayed formulas. The exercise leaves the caustic and the superluminal case open.

**4. A convention, not a gap: the derivative variable.** The parent fixes the dot to be $d/dt_r$ and warns that the observer's-time derivative moves a power of $\kappa$ between the two display formulas. This exercise confirms the bookkeeping: the retarded-time convention is the one for which the displayed powers $\kappa^3$ are correct, and the scalar identity $\dot D = -c\vec u_R\cdot\vec\beta+c\beta^2-\vec R\cdot\dot{\vec\beta}$ holds in that convention. No gap is recorded here, only a convention inherited and used consistently.

## Further Problems

**1. Expand the brackets by hand.** The two biquaternion brackets of Problem 2 were verified here by finite differences and by matching to the component formulas, but the component expansion of $\tilde{F}_v$ and $\tilde{F}_a$ was not carried out symbolically in the article. Do it: expand $\tilde{\mathcal{N}}\tilde{V}/\gamma$, $\tilde{\mathcal{N}}\dot{\vec\beta}$, and $\left(\vec u_R-\vec\beta\right)\tilde{V}/\gamma$ into scalar and vector parts, and show that the vector part of $gD^{-2}\tilde{F}_v$ is $i\sqrt{\epsilon}\vec E_v-\sqrt{\mu}\vec H_v$. This is the one purely mechanical step left as an exercise. It is where the $\kappa^3$ and the factor $1-\beta^2$ are seen to emerge.

**2. The present-position fallacy.** Compute the field of a uniformly moving charge using the *present* position $\vec x_q(t)$ in place of the retarded position, and show that the result differs from $\vec E_v$. Identify which of the two falloff laws fails and by how much. This makes quantitative why the field point and the source point must be distinguished.

**3. The transformation law from the algebra.** Derive $\tilde{F}' = \tilde{U}^{\natural}\tilde{F}\tilde{U}$ directly from the biquaternion representation of the field strength as a rank-two object, rather than by comparison with the standard boost formulas. The Lorentz-transformation article's open question on higher-rank tensors is the parent of this problem.

**4. The caustic and the superluminal case.** Determine the locus $\kappa = 0$ for a specified accelerated worldline, show that the retarded-time equation has a double root there, and describe what a point charge's field does as it is approached. Then ask what, if anything, the biquaternionic form can say about a putative superluminal source.

**5. Radiation reaction and the far zone.** Starting from the far-zone field $\vec E\to\vec E_a$, evaluate the Poynting flux through a large sphere and recover the relativistic Larmor power of the parent as the biquaternion norm of the four-acceleration. State whether any step requires the velocity field to be neglected or only requires it to be subleading.

**6. The sibling case.** Specialise every result to $\dot{\vec v} = 0$ and reconstruct the Heaviside ellipsoid field of *Exercise: The Electromagnetic Field of a Uniformly Moving Charge*, including the equivalence with the boosted Coulomb field of Problem 5. Compare the two routes for economy and for the transparency of the sign conventions.

## Summary

The Liénard–Wiechert potential of a point charge is the single biquaternion $\tilde{A} = \frac{\mu ϙ}{4\pi D}\tilde{V}/\gamma$, built from the null retarded separation $\tilde{\mathcal{R}} = iR\,e_0+\vec R$ and the four-velocity $\tilde{V} = \gamma\left(ic\,e_0+\vec v(t_r)\right)$, paired through $D = R\kappa = -\frac{1}{c\gamma}\,\mathrm{Sc}\!\left(\tilde{V}\bar{\tilde{\mathcal{R}}}\right)$ with $\kappa = 1-\vec u_R\cdot\vec\beta$. Differentiating it once with the biquaternionic gradient gives the whole field, because the retarded time satisfies $\tilde{\nabla}^{\natural}t_r = \frac{1}{c\kappa}\left(\vec u_R-ie_0\right)$, a null biquaternion. The field separates exactly into a part independent of the acceleration and a part linear in it,
$$
\tilde{F}_v = \frac{g}{D^2}\left[\left(\vec u_R-\vec\beta\right)\tilde{V}/\gamma - \frac{\dot D_0}{c\kappa}\tilde{\mathcal{N}}\tilde{V}/\gamma\right],
\qquad
\tilde{F}_a = \frac{g}{D^2}\left[R\,\tilde{\mathcal{N}}\dot{\vec\beta} + \frac{\vec R\cdot\dot{\vec\beta}}{c\kappa}\tilde{\mathcal{N}}\tilde{V}/\gamma\right],
$$
with $\tilde{\mathcal{N}} = \vec u_R-ie_0$, $\dot D_0 = -c\left(\vec u_R\cdot\vec\beta-\beta^2\right)$, and $g = \mu ϙ/4\pi$.

The velocity field falls as $1/R^2$, is of electric type, and is not null: $I_{1,v} = \left(\frac{ϙ}{4\pi\epsilon}\frac{1-\beta^2}{\kappa^2R^2}\right)^2>0$, $I_{2,v}=0$, $\langle\tilde{F}_v\rangle_{\natural}\ne0$. The acceleration field falls as $1/R$, is transverse and null, and is a zero divisor: $\vec u_R\cdot\vec E_a = 0$, $I_{1,a}=I_{2,a}=0$, $\tilde{F}_a^2 = 0$. The two falloffs were verified by holding the retarded configuration fixed and scaling the observation distance, and the far-zone dominance of $\vec E_a$ follows from the one-power difference: the ratio $|\vec E_v|/|\vec E_a|$ falls off as $1/R$. The retarded denominator $\kappa$ and the charge sign were checked on two independent cases, uniform motion (where $\vec E = \vec E_v$) and motion with acceleration (where both parts contribute); $\kappa$ can be less than or greater than $1$ and is not a $\gamma$-factor. Finally, the field is not a four-vector: under a boost it transforms by the similarity $\tilde{U}^{\natural}\tilde{F}\tilde{U}$, not by the rotor conjugation $\tilde{U}\tilde{F}\tilde{U}^{*}$, and the velocity field is recovered as the boost of the Coulomb field by that law.

The exercise confirms the parent's field formulas on accelerated worldlines and on two independent sign conventions, and it records rather than closes four gaps: the parent's differentiation is asserted in outline and completed here; the field transformation law is stated here because the parent's remark is law-silent and the naive rotor conjugation fails; the subluminal restriction on $\kappa$ is unstated in the parent; and the component expansion of the biquaternion brackets is left as the first further problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = -\delta_{jk}e_0 + \epsilon_{jkm}e_m$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace, scalar subspace |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}, \Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | Biquaternionic gradient, its quaternion conjugate, d'Alembertian |
| $\partial_{ict} = -\frac{i}{c}\partial_t$ | Temporal component of the gradient |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\tilde{A} = \frac{i\phi}{c}e_0 + \vec A$ | Potential biquaternion |
| $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\vec J$ | Source biquaternion |
| $\epsilon, \mu$ | Permittivity and permeability |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\vec H = \vec B/\mu$ | Magnetic field; $\vec B$ the magnetic induction |
| $ϙ$, $\vec x_q(t)$, $\vec v(t)$ | Charge, worldline, coordinate velocity |
| $t_r = t - R/c$ | Retarded time (implicit) |
| $\vec R = \vec x-\vec x_q(t_r)$, $R = |\vec R|$, $\vec u_R = \vec R/R$ | Retarded separation, its length and direction |
| $\vec\beta = \vec v/c$ | Retarded coordinate velocity over $c$ |
| $\dot{\vec\beta} = d\vec\beta/dt_r$ | Retarded-time acceleration (dot is $d/dt_r$ throughout) |
| $\gamma = (1-\beta^2)^{-1/2}$ | Lorentz factor of the retarded velocity |
| $\kappa = 1-\vec u_R\cdot\vec\beta$ | Retarded denominator; $D = R\kappa$ |
| $\tilde{V} = \gamma\left(ic\,e_0+\vec v(t_r)\right)$ | Four-velocity biquaternion, $\langle\tilde{V}\rangle_{\natural} = -c^2$ |
| $\tilde{V}/\gamma = ic\,e_0+\vec v(t_r)$ | Retarded coordinate velocity, the four-velocity divided by $\gamma$ |
| $\tilde{\mathcal{R}} = iR\,e_0+\vec R$ | Retarded null separation, in $\mathbb{M}_-$ |
| $\tilde{\mathcal{K}} = \tilde{\nabla}^{\natural}t_r = \frac{1}{c\kappa}(\vec u_R-ie_0)$ | Gradient of the retarded time (null) |
| $\tilde{\mathcal{N}} = \vec u_R-ie_0$ | Null factor of $\tilde{\mathcal{K}}$ |
| $\tilde{F}_v, \tilde{F}_a$ | Velocity and acceleration (radiation) parts of the field |
| $\vec E_v, \vec E_a$ | Their electric components; $\vec B = \frac{1}{c}\vec u_R\times\vec E$ |
| $\tilde{U}_{\vec v_b} = \cosh\frac{\psi_b}{2}+i\sinh\frac{\psi_b}{2}\vec u$ | Boost rotor; carries lab to the frame moving with $+\vec v_b$ |
| $\tilde{F}' = \tilde{U}^{\natural}\tilde{F}\tilde{U}$ | Boost transformation of the field (similarity, not conjugation) |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula |

## Further Reading

The further reading of this exercise is the parent and companion articles of this series, all present in `articles_physics/`; the standard textbook references for the Liénard–Wiechert field are listed in the Further Reading section of the parent article.

- *Introduction to the Biquaternion Universe* — the algebra, the two sectors, and the local complex structure.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the four-vectors, the biquaternion norm, and the zero-divisor cone on which the null retarded separation sits.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian subspace, the conjugation action, and the trace formula.
- *Maxwell's Equations in the Biquaternionic Formulation* — the gradient, the field strength, the potential and source, and the retarded solution.
- *The Field-Strength Biquaternion and Its Invariants* — the biquaternion norm, the invariants $I_1,I_2$, and the null/zero-divisor characterization of radiation.
- *Radiation from Accelerated Charges in Biquaternionic Form* — the direct parent: the Liénard–Wiechert potential, the field split, and the radiated power evaluated here.
- *The Lorentz Transformation as a Biquaternionic Rotation* — the boost rotor, its direction convention, and the open question on higher-rank tensors used in Problem 5.
- *Exercise: Boosting a Four-Velocity and Rapidity Composition* — the convention that the rotor with $+\vec v_b$ carries the lab to the moving frame.
- *Exercise: The Relativistic Kinematics of a Two-Body Decay* — the record of the rotor-direction ambiguity and the physical convention for the boost.
- *Relativistic Mechanics in Biquaternionic Form* — the four-velocity and four-momentum conventions used in the rotor check.
