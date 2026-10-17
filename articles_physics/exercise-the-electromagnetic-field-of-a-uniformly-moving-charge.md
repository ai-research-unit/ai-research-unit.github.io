# __Exercise: The Electromagnetic Field of a Uniformly Moving Charge__

## Introduction

This is an exercise in the electromagnetism series. It is the exactly solvable special case of its direct parent, *Exercise: The Electromagnetic Field of a Moving Charge*, which performs the Liénard–Wiechert differentiation for a charge on an arbitrary subluminal worldline and verifies the velocity–acceleration split; that exercise is in turn the downstream case declared by *Radiation from Accelerated Charges in Biquaternionic Form*, the theory article that supplies the retarded solution. The special case treated here is **uniform motion**, $d\vec v/dt_r \equiv 0$. Then the acceleration field vanishes identically, the field reduces to the Lorentz-boosted Coulomb field, and — this is the point of singling the case out — the retarded position can be written in **closed form**, so the entire field is available in closed form in terms of the *present* position of the charge. Nothing in the parent is changed; every object used below is inherited from it and from its own parents, and no new formalism is introduced.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$ and $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \epsilon_{\mu\nu\lambda}\vec e_\lambda$, and the scalar imaginary $i$ with $i^2 = -1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part) — the home of the four-vectors — and the Hermitian subspace $\mathbb{M}_+$ (real scalar part, imaginary vector part), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$, together with the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the scalar subspace $\mathbb{C}_{\mathbb{B}}$. The biquaternionic gradient and its quaternion conjugate,
$$
\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z,
\qquad
\tilde{\nabla}^{\natural} = e_t\,\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z,
$$
with $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t$ and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta$; the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ (pure vector), the potential $\tilde{A} = \frac{i\phi}{c}e_t + \vec A$, and the source $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_t + \sqrt{\mu}\,\vec J$ (here $\rho$ is the charge density, not a distance). The permittivity and permeability $\epsilon,\mu$ with $c = 1/\sqrt{\epsilon\mu}$, and $\vec H = \vec B/\mu$. The biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$, the quaternion conjugate $\tilde{Q}^{\natural}$, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ of the shared notation. No object of the informational sector arises below, so $\mathbb{M}_+$, the rotors, and the trace formula are recorded but the trace formula is not used; the boost rotor is invoked only in Problem 5.

**What is inherited from the parent.** The charge $ϙ$ moves on the worldline $x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z$ with coordinate velocity $\vec v(t)$ and $\vec\beta = \vec v/c$. The retarded time is defined implicitly by
$$
t_r = t - \frac{R}{c},
\qquad
R = \left|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r)\right|,
$$
and writing
$$
\vec R = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r), \qquad R = |\vec R|, \qquad \vec u_R = \frac{\vec R}{R},
\qquad
\kappa = 1 - \vec u_R\cdot\vec\beta,
\qquad
D = R\kappa,
$$
the Liénard–Wiechert potential is $\tilde{A} = \frac{\mu ϙ}{4\pi D}\tilde{V}$ with $\tilde{V} = ic\,e_t + \vec v(t_r)$. The field splits exactly into a velocity part and an acceleration part, and for the velocity part the parent's closed component formula is
$$
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\left(\vec u_R-\vec\beta\right)}{\kappa^3 R^2},
\qquad
\vec B = \frac{1}{c}\,\vec u_R\times\vec E,
\qquad
\vec E = \vec E_v + \vec E_a,
$$
with $\vec E_a$ linear in $d\vec\beta/dt_r$. The velocity field is of electric type and not null; the acceleration field falls one power of $R$ more slowly, is transverse and null, and is the zero-divisor realization of radiation. All source quantities are evaluated at the retarded time, and the derivative of a source quantity is written $\frac{d}{dt_r}$.

**The one convention used here, stated once.** The boost rotor
$$
\tilde{\Lambda}_{\vec v_b} = \cosh\frac{\psi_b}{2} + i\,\sinh\frac{\psi_b}{2}\,\vec u,
\qquad
\tanh\psi_b = \frac{v_b}{c},
$$
**carries the laboratory to the frame moving with $+\vec v_b$**: applied to the rest four-velocity it produces velocity $-\vec v_b$, i.e. $\tilde{\Lambda}_{\vec v_b}(ic\,e_t)\tilde{\Lambda}_{\vec v_b}^{*}$ has velocity $-\vec v_b$. This is the convention fixed by the boosting and two-body exercises of the relativity series and used by the parent. The field strength is rank two, and under this rotor it transforms by the **similarity** $\tilde{F}' = \tilde{\Lambda}^{\natural}_{\vec v_b}\tilde{F}\tilde{\Lambda}_{\vec v_b}$, not by the four-vector rotor conjugation $\tilde{\Lambda}\tilde{F}\tilde{\Lambda}^{*}$; that is the parent's Problem 5 and we use its result.

**New notation for this exercise.** Since the uniform case is naturally organized around the charge's *present* position, write the **present separation**
$$
\vec d = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z), \qquad d = |\vec d|, \qquad \vec u_d = \frac{\vec d}{d},
$$
with the components parallel and perpendicular to the (constant) velocity,
$$
d_\parallel = \vec u_v\cdot\vec d, \qquad d_\perp^2 = d^2 - d_\parallel^2 .
$$
The arrow on $\vec u_d$ is a unit vector; the symbol $\rho$ is reserved for the charge density, so the present distance is $d$ and never $\rho$.

**What is to be shown.** Problem 1 derives the retarded position in closed form for uniform motion, so that $R$ and $\kappa$ become explicit functions of $\vec d$; this is the step that makes the case solvable and it is done before the field is written. Problem 2 turns the parent's velocity field into the closed-form **Heaviside ellipsoid** field in the present-position variable, and checks the direction and the $1/d^2$ falloff. Problem 3 verifies the non-relativistic limit against Coulomb. Problem 4 verifies the ultrarelativistic limit, where the field flattens into a transverse pancake, and states precisely the sense in which it becomes purely transverse. Problem 5 fixes and uses the boost-rotor convention, and recovers the same field as the boost of the Coulomb field. Problem 6 checks the result on the two independent cases and quantifies the present-position fallacy, and evaluates the field invariants.

**The result.** Writing
$$
D = \sqrt{d_\parallel^2 + (1-\beta^2)\,d_\perp^2},
$$
the field of a charge in uniform motion is, in closed form about the **present** position,
$$
\boxed{\;
\vec E = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,\vec d}{\left(d_\parallel^2 + (1-\beta^2)\,d_\perp^2\right)^{3/2}}
= \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,\vec d}{\left(d_\parallel^2 + d_\perp^2/\gamma^2\right)^{3/2}},
\qquad
\vec B = \frac{1}{c^2}\,\vec v\times\vec E,
\;}
$$
with $\gamma = (1-\beta^2)^{-1/2}$. The electric field is radial *from the present position*, falls as $1/d^2$ at fixed direction, and is anisotropic: enhanced by $\gamma$ in the plane transverse to the motion and suppressed by $1/\gamma^2$ along it. Surfaces of constant $D$ — hence of constant scalar potential — are oblate spheroids flattened along the direction of motion, which is the "Heaviside ellipsoid" of the title.

## The Problem

The parent gives the velocity field in terms of the retarded separation $\vec R$ and the retarded denominator $\kappa$. For a charge in uniform motion that description is not the most economical one: the retarded time equation can be solved exactly, so $\vec R$, $R$ and $\kappa$ can all be eliminated in favour of the present separation $\vec d = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-(x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z)$, which is the quantity a laboratory observer actually measures. The exercise is to carry out that elimination and then to *verify* the closed form rather than assert it. The specific demands are:

1. derive the retarded position $(x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r) = x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z - \vec\beta R$ in closed form, including the quadratic that fixes $R$ and the choice of its root (the two traps being that the retarded position is **not** the present position, and that for uniform motion it nevertheless has a closed form);
2. substitute into the parent's velocity field to obtain the Heaviside ellipsoid field, and check the direction of $\vec E$ and the $1/d^2$ falloff;
3. verify the non-relativistic limit (Coulomb) and the ultrarelativistic limit (transverse pancake) — two cases chosen because the second does not follow from the first;
4. fix the boost-rotor convention and confirm the closed form as the boosted Coulomb field;
5. quantify the present-position fallacy and evaluate the field invariants.

The numerical checks quoted below were performed under `/home/hp/.venvs/verify/bin/python` on constant-velocity worldlines, with the retarded time obtained independently by Newton iteration on $t_r = t - R/c$ (the iteration uses $\partial t_r/\partial t = 1/\kappa$, so it agrees with the closed form only if the closed form is right). All reported discrepancies are componentwise maxima in units with $4\pi\epsilon = 1$ unless stated otherwise.

## Problem 1: The Retarded Position in Closed Form

**Statement.** For a charge in uniform motion, (a) integrate the worldline to show that the retarded position satisfies $(x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r) = x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z - \vec v(t-t_r)$, and hence, with $R = c(t-t_r)$, the **retarded-separation identity**
$$
\vec R = \vec d + \vec\beta R,
\qquad
\vec d = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z).
$$
(b) Square it to obtain the quadratic $(1-\beta^2)R^2 - 2\beta d_\parallel R - d^2 = 0$ and show that its physical root is
$$
R = \frac{\beta d_\parallel + \sqrt{\beta^2 d_\parallel^2 + (1-\beta^2)d^2}}{1-\beta^2},
$$
the other root being non-positive. (c) Deduce $D = R\kappa = \sqrt{d_\parallel^2 + (1-\beta^2)d_\perp^2}$ together with the **present-position identities**
$$
\vec u_R - \vec\beta = \frac{\vec d}{R},
\qquad
\vec u_R\cdot\vec d = D .
$$
(d) Quantify how far the retarded position is from the present position.

**Solution (a).** For constant $\vec v$ the worldline is $(x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r) = x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z - \vec v(t-t_r)$: between emission and observation the charge has travelled for a time $t-t_r$ at the constant velocity $\vec v$. The retarded-time definition gives $t-t_r = R/c$, so $(x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r) = x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z - \vec\beta R$, and therefore
$$
\vec R = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r) = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - (x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z) + \vec\beta R = \vec d + \vec\beta R .
$$
Two remarks belong here. First, the retarded position is **not** the present position: the two differ by $\vec\beta R$, and Problem 1(d) shows that this offset is not small. Second, the identity $\vec R = \vec d+\vec\beta R$ is exact rather than a first-order approximation — that exactness is precisely what makes uniform motion solvable.

**Solution (b).** Squaring the identity,
$$
R^2 = |\vec d+\vec\beta R|^2 = d^2 + 2R\,\vec d\cdot\vec\beta + \beta^2 R^2
= d^2 + 2\beta d_\parallel R + \beta^2 R^2,
$$
which rearranges to
$$
(1-\beta^2)R^2 - 2\beta d_\parallel R - d^2 = 0 .
$$
The quadratic formula gives
$$
R = \frac{\beta d_\parallel \pm \sqrt{\beta^2 d_\parallel^2 + (1-\beta^2)d^2}}{1-\beta^2}.
$$
Since $\sqrt{\beta^2 d_\parallel^2 + (1-\beta^2)d^2} \ge \beta|d_\parallel| \ge \beta d_\parallel$, the branch with the minus sign gives $R\le 0$, which is not a distance; the physical root is the branch with the plus sign. Thus for $\beta<1$ there is exactly one positive root, i.e. exactly one past emission event for a uniform worldline — the parent's uniqueness statement, here made explicit. The sign of $d_\parallel$ shows that $R$ can be smaller or larger than $d$: when the charge is approaching the field point ($d_\parallel>0$) it has moved closer since emitting, so the emission event is farther, $R>d$; when it is receding ($d_\parallel<0$) the emission event is nearer, $R<d$.

**Solution (c).** From $D = R - \vec R\cdot\vec\beta$ and the identity,
$$
D = R - \vec d\cdot\vec\beta - \beta^2 R = R(1-\beta^2) - \beta d_\parallel .
$$
Substituting the root and simplifying,
$$
D = \sqrt{\beta^2 d_\parallel^2 + (1-\beta^2)d^2}
= \sqrt{d_\parallel^2 + (1-\beta^2)d_\perp^2},
$$
where $d^2 = d_\parallel^2+d_\perp^2$ was used in the last step. Equivalently $D = \sqrt{d_\parallel^2 + d_\perp^2/\gamma^2}$. For the first present-position identity, divide the retarded-separation identity by $R$:
$$
\vec u_R - \vec\beta = \frac{\vec R - R\vec\beta}{R} = \frac{\vec d}{R}.
$$
This is the key to the whole exercise: the retarded combination $\vec u_R-\vec\beta$ that appears in the parent's velocity field is **parallel to the present separation**. For the second, $\vec u_R\cdot\vec d = (\vec d/R+\vec\beta)\cdot\vec d = d^2/R + \beta d_\parallel$, which equals $D$ by the quadratic.

**Solution (d).** The charge has moved a distance
$$
\left|x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z - (x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r)\right| = \beta R
$$
along $\vec u_v$ since emission. This is not a small correction at relativistic speeds. For the representative case $\vec\beta = 0.9\,(1,1,1)/\sqrt{3}$, $x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z = \vec\beta c t$ and observation at $ct = 3$, $(x,y,z)=(2,-1.3,0.7)$ (units $c=1$), the closed form gives
$$
R = 2.362563, \qquad \kappa = 0.910632, \qquad D = 2.151426, \qquad d = 3.0175, \qquad \beta R = 2.1263 :
$$
the emission event is $2.13$ away from the present position while the field point is $3.02$ away, so the offset is about $70\%$ of $d$.

## Problem 2: The Field in Closed Form — the Heaviside Ellipsoid

**Statement.** (a) Substitute the present-position identities of Problem 1 into the parent's velocity field to obtain
$$
\vec E = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,\vec d}{D^3},
\qquad
\vec B = \frac{1}{c^2}\,\vec v\times\vec E,
$$
and note that $\vec E\parallel\vec d$. (b) Show that the field falls as $1/d^2$ at fixed direction and identify the Heaviside ellipsoid. (c) Confirm that the acceleration field vanishes identically and that the field is of electric type, not null.

**Solution (a).** Insert $\vec u_R-\vec\beta = \vec d/R$ and $\kappa R = D$ into $\vec E_v$:
$$
\vec E_v = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)}{\kappa^3 R^2}\,\frac{\vec d}{R}
= \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,\vec d}{\kappa^3 R^3}
= \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,\vec d}{D^3},
$$
so $\vec E$ is **parallel to the present separation** $\vec d$: the field points radially away from the charge's *present* position even though it propagated from the retarded one. For the magnetic field, write $\vec u_R = \vec d/R + \vec\beta$; then
$$
\vec u_R\times\vec E = \frac{\vec d}{R}\times\vec E + \vec\beta\times\vec E = \vec\beta\times\vec E,
$$
because $\vec E\parallel\vec d$, and hence $\vec B = \frac{1}{c}\vec u_R\times\vec E = \frac{1}{c}\vec\beta\times\vec E = \frac{1}{c^2}\vec v\times\vec E$. It follows that $\vec B\perp\vec E$ for every configuration.

**Solution (b).** At a fixed direction $\vec u_d$ one has $D = d\sqrt{\cos^2\theta + \sin^2\theta/\gamma^2}$, where $\theta$ is the angle between $\vec d$ and $\vec v$, so $D\propto d$ and
$$
|\vec E| = \frac{ϙ}{4\pi\epsilon}\,\frac{1-\beta^2}{d^2\left(\cos^2\theta + \sin^2\theta/\gamma^2\right)^{3/2}} \propto \frac{1}{d^2}.
$$
The falloff is therefore inverse-square about the present position, with no residual $\kappa$-dependence once the direction is held fixed. The surfaces of constant scalar potential, $\phi = \frac{ϙ}{4\pi\epsilon D} = \text{const}$, are
$$
d_\parallel^2 + \frac{d_\perp^2}{\gamma^2} = D_0^2 ,
$$
ellipsoids of revolution about the velocity axis with semiaxis $D_0$ along the motion and $\gamma D_0$ transverse to it: flattened along the direction of motion, the **Heaviside ellipsoid**. The same flattening is visible in the field: it is enhanced in the transverse plane and suppressed along the motion, as Problem 4 makes quantitative.

**Solution (c).** Since $d\vec\beta/dt_r = 0$ identically, the parent's acceleration field $\vec E_a$, which is linear in $d\vec\beta/dt_r$, vanishes at every event; the uniform field is entirely the velocity field. With $\vec B = \frac{1}{c^2}\vec v\times\vec E$ one has $\vec E\perp\vec B$ and, using $\vec u_R\cdot\vec E = \frac{ϙ}{4\pi\epsilon}\frac{1-\beta^2}{D^2}$ (from Problem 1(c) and the parent),
$$
I_1 = \vec E^2 - c^2\vec B^2 = \left(\vec u_R\cdot\vec E\right)^2
= \left(\frac{ϙ}{4\pi\epsilon}\,\frac{1-\beta^2}{D^2}\right)^{\!2} > 0,
\qquad
I_2 = \vec E\cdot\vec B = 0 .
$$
The field is of electric type with a nonzero longitudinal component and is **not** null: $\langle\tilde{F}\rangle_{\natural} = -\epsilon I_1 \ne 0$ and $\tilde{F}^2 \ne 0$. It is therefore not a radiation field — consistent with $d\vec\beta/dt_r=0$ — and this is the qualitative difference from the parent's acceleration field, which is a zero divisor.

**Evidence.** On the same set of constant-velocity worldlines, the present-position closed form and the parent's retarded formula $\vec E_v$ agreed componentwise to better than $10^{-15}$ (quoted discrepancies ranged from $7\times10^{-21}$ to $2.2\times10^{-16}$); $|\vec E\times\vec d|$ and $|\vec B - \vec v\times\vec E/c^2|$ never exceeded $2\times10^{-17}$; and $d^2|\vec E|$ at fixed direction was constant to eight significant figures under $d\mapsto 2d,4d,8d$. The invariance of $d^2|\vec E|$ at fixed direction is the numerical form of the $1/d^2$ law.

## Problem 3: The Non-Relativistic Limit Must Reduce to Coulomb

**Statement.** Take $\beta\to0$ at fixed present separation $\vec d$ and show that the closed form reduces to the Coulomb field $\vec E = \frac{ϙ}{4\pi\epsilon}\vec u_d/d^2$, that the magnetic field vanishes linearly in $\beta$, and that the leading correction is of order $\beta^2$. Confirm that the retarded and present positions coincide in this limit.

**Solution.** As $\beta\to0$ one has $D = \sqrt{d_\parallel^2+(1-\beta^2)d_\perp^2}\to d$ and $1-\beta^2\to1$, so
$$
\vec E \to \frac{ϙ}{4\pi\epsilon}\,\frac{\vec d}{d^3} = \frac{ϙ}{4\pi\epsilon}\,\frac{\vec u_d}{d^2},
\qquad
\vec B = \frac{1}{c^2}\vec v\times\vec E \to 0 .
$$
This is Coulomb's law, radial from the charge, and the magnetic field vanishes as $\beta$. The retarded position converges to the present one as well: from the quadratic, as $\beta\to0$ the negative root tends to $-d$ and the physical root to $+d$, so $R\to d$; equivalently $\vec u_R = \vec d/R+\vec\beta\to\vec u_d$, and the offset $\beta R$ vanishes. The distinction between the two positions is a relativistic effect of order $\beta$.

For the correction, write $\theta$ for the angle between $\vec d$ and $\vec v$, so that $D = d\sqrt{1-\beta^2\sin^2\theta}$. Then
$$
\frac{|\vec E|}{E_C} = \frac{1-\beta^2}{\left(1-\beta^2\sin^2\theta\right)^{3/2}}
= 1 + \beta^2\left(\tfrac{3}{2}\sin^2\theta - 1\right) + O(\beta^4),
$$
where $E_C = \frac{ϙ}{4\pi\epsilon d^2}$ is the Coulomb field at the same distance. There is **no term linear in $\beta$**: the field depends on the velocity only through $\beta^2$ and the fixed direction $\vec u_v$. The leading correction is $O(\beta^2)$, is anisotropic, and sits entirely in the magnitude — the direction is already the radial direction at every $\beta$. It is a suppression of relative size $\beta^2$ along the motion ($\theta=0$) and an enhancement of relative size $\tfrac12\beta^2$ in the transverse plane ($\theta=\pi/2$), the first glimpse of the flattening that dominates at the other end of the range.

**Evidence.** The maximum relative deviation from Coulomb over the sphere was computed exactly, and at $\beta = 0.1,\,0.01,\,0.001$ it equalled $\beta^2$ to six decimals, attained at $\theta=0$; the transverse value was $1+\tfrac12\beta^2+O(\beta^4)$ (e.g. $1.005038$ at $\beta=0.1$). The direction test $|\vec E\times\vec d| = 0$ held for every $\beta$, not only in the limit, and the retarded offset $\beta R$ vanished as $\beta\to0$. This limit is the familiar static anchor and therefore the check a reader reaches for first; by itself it could not distinguish the closed form from any other expression with the same static limit, which is why Problem 4 and Problem 5 are checked as well.

## Problem 4: The Ultrarelativistic Limit — the Transverse Pancake

**Statement.** (a) With $\theta$ the angle between $\vec d$ and $\vec v$, write the field magnitude as
$$
|\vec E| = \frac{ϙ}{4\pi\epsilon d^2}\,\frac{1}{\gamma^2\left(1-\beta^2\sin^2\theta\right)^{3/2}},
$$
and show that it is peaked at $\theta=\pi/2$, enhanced by $\gamma$ over the Coulomb field at the same distance, suppressed by $1/\gamma^2$ at $\theta=0$, and of angular width of order $1/\gamma$. (b) Determine in exactly what sense the field becomes purely transverse. (c) Show that the $1/d^2$ law and the radial direction survive the limit.

**Solution (a).** With $d_\parallel = d\cos\theta$ and $d_\perp = d\sin\theta$,
$$
D = d\sqrt{\cos^2\theta + \frac{\sin^2\theta}{\gamma^2}} = d\sqrt{1-\beta^2\sin^2\theta},
$$
so
$$
\frac{|\vec E|}{E_C} = \frac{1}{\gamma^2\left(1-\beta^2\sin^2\theta\right)^{3/2}},
\qquad
E_C = \frac{ϙ}{4\pi\epsilon d^2}.
$$
At $\theta=\pi/2$ the factor is $1/(\gamma^2(1-\beta^2)^{3/2}) = 1/(\gamma^2\gamma^{-3}) = \gamma$: the transverse field is larger than the Coulomb field at the same distance by $\gamma$. At $\theta=0$ it is $1/\gamma^2$. The profile is monotone in $\theta\in[0,\pi/2]$ and symmetric about the transverse plane. Expanding near $\theta=\pi/2$, with $\delta = \pi/2-\theta$,
$$
\frac{|\vec E|}{E_C} \approx \frac{1}{\gamma^2\left(\delta^2+\gamma^{-2}\right)^{3/2}},
$$
so the half-maximum condition gives $\delta_{1/2}^2 = (2^{2/3}-1)/\gamma^2$, i.e.
$$
\delta_{1/2} = \frac{\sqrt{2^{2/3}-1}}{\gamma} \approx \frac{0.766}{\gamma}.
$$
The field is therefore concentrated into a **pancake** of angular half-width $\sim 1/\gamma$ about the plane perpendicular to the motion, while the peak is enhanced by $\gamma$.

**Solution (b).** Since $\vec E\parallel\vec d$ for every $\beta$, at a *fixed direction* $\theta$ the longitudinal fraction of the field is $\cos\theta$ and the transverse fraction is $\sin\theta$, both independent of $\gamma$. So it is **not** true that $\vec E$ is transverse at every fixed direction: on the axis it is purely longitudinal, and at $45^\circ$ its two components are equal, however large $\gamma$ is. The correct statements are the following two, and they are exact.

- In the **transverse plane** $d_\parallel=0$, one has $\vec E\parallel\vec d_\perp\perp\vec v$ and $\vec B = \frac{1}{c^2}\vec v\times\vec E$ perpendicular to both, so both fields are purely transverse there, with
$$
|\vec E| = \frac{\gamma\,ϙ}{4\pi\epsilon\,d_\perp^2}.
$$
- At a fixed **impact parameter** $b = d_\perp$, the field is concentrated in $|d_\parallel|\lesssim b/\gamma$. The transverse peak at $d_\parallel = 0$ is $\gamma ϙ/(4\pi\epsilon b^2)$, while the longitudinal component has a $\gamma$-independent maximum. From
$$
E_\parallel = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,d_\parallel}{\left(d_\parallel^2+b^2/\gamma^2\right)^{3/2}},
$$
the maximum occurs at $d_\parallel = -b/(\sqrt{2}\gamma)$ and equals
$$
\max_{d_\parallel}|E_\parallel| = \frac{ϙ}{4\pi\epsilon b^2}\,\frac{1}{\sqrt{2}\,(3/2)^{3/2}}
= \frac{0.3849\,ϙ}{4\pi\epsilon b^2}.
$$
Hence
$$
\frac{\max_{d_\parallel}|E_\parallel|}{|E_\perp(d_\parallel=0)|} = \frac{0.3849}{\gamma} \to 0 .
$$
In this precise sense — the pancake at fixed impact parameter — the ultrarelativistic field becomes **purely transverse**: the longitudinal component is a factor $1/\gamma$ down, and the field in the transverse plane is exactly perpendicular to the motion. The weaker interpretation ("$\vec E$ is transverse at every point") is false at every finite $\gamma$ and is not what the limit delivers; we record the caveat rather than smooth it over.

**Solution (c).** At fixed $\theta$ the magnitude is $E_C/(\gamma^2(1-\beta^2\sin^2\theta)^{3/2}) \propto 1/d^2$: the inverse-square law about the present position is untouched by the limit, which only moves magnitude from the axis into the transverse plane. Because $\vec E\parallel\vec d$ for every $\beta$, the field remains radial from the present position; in the transverse plane that radial direction is itself perpendicular to $\vec v$.

**Evidence.** For $\beta = 0.9,\,0.99,\,0.999,\,0.9999$ (i.e. $\gamma = 2.294$ through $70.712$), the transverse field in the plane $d_\parallel=0$ equalled $\gamma$ times the Coulomb field and the axial field $1/\gamma^2$ times it, to the displayed digits; the ratio $E_\parallel/E_\perp$ at $45^\circ$ was $1.000000$ for every $\gamma$; the half-width from the exact profile matched $0.766/\gamma$; and at fixed $b=1$ the ratio $\max|E_\parallel|/E_\perp$ was $1.68\times10^{-1},\,5.43\times10^{-2},\,1.72\times10^{-2},\,5.44\times10^{-3}$ as $\gamma$ grew, i.e. proportional to $1/\gamma$ with the analytic coefficient $0.385$, while $\max|E_\parallel| = 0.030629 = 0.3849/(4\pi)$ was $\gamma$-independent. The $1/d^2$ falloff at fixed direction was verified separately by scaling $d$ by $2,4,8$.

## Problem 5: The Boost Rotor and the Field as a Boosted Coulomb Field

**Statement.** (a) State the rotor-direction convention and verify it on the rest four-velocity. (b) Give the correct transformation law of the field strength under a boost and use it to recover the closed form of Problem 2 as the boost of the Coulomb field, identifying the rest-frame separation. (c) State the sense in which the result is exactly, not merely asymptotically, the boosted Coulomb field.

**Solution (a).** We use the convention of the Introduction and of the parent: the rotor
$$
\tilde{\Lambda}_{\vec v_b} = \cosh\frac{\psi_b}{2} + i\,\sinh\frac{\psi_b}{2}\,\vec u,
\qquad
\tanh\psi_b = \frac{v_b}{c},
$$
**carries the laboratory to the frame moving with $+\vec v_b$**. On the rest four-velocity $\tilde{V}_0 = ic\,e_t$, using $\tilde{\Lambda}_{\vec v_b}^{*} = \tilde{\Lambda}_{\vec v_b}$ (a pure boost is Hermitian),
$$
\tilde{\Lambda}_{\vec v_b}\,\tilde{V}_0\,\tilde{\Lambda}_{\vec v_b}^{*}
= ic\,\tilde{\Lambda}_{\vec v_b}^2
= ic\left(\cosh\psi_b + i\sinh\psi_b\,\vec u\right)
= ic\cosh\psi_b - c\sinh\psi_b\,\vec u,
$$
whose velocity is $-c\tanh\psi_b\,\vec u = -\vec v_b$. So the rotor built with $+\vec v_b$ carries the lab to the frame moving with $+\vec v_b$; a particle at rest in the lab appears in that frame to move with $-\vec v_b$.

**Solution (b).** The field strength is a rank-two object, not a four-vector, so the rotor conjugation $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*}$ that acts on $\mathbb{M}_-$ does **not** apply. As established by the parent's Problem 5, a pure boost acts on the field by the **similarity**
$$
\tilde{F}' = \tilde{\Lambda}^{\natural}_{\vec v_b}\,\tilde{F}\,\tilde{\Lambda}_{\vec v_b}
= \tilde{\Lambda}_{\vec v_b}^{-1}\tilde{F}\,\tilde{\Lambda}_{\vec v_b}
\qquad(\text{laboratory}\to\text{moving frame}),
$$
and inversely
$$
\tilde{F} = \tilde{\Lambda}_{\vec v_b}\,\tilde{F}'\,\tilde{\Lambda}^{\natural}_{\vec v_b}
\qquad(\text{moving frame}\to\text{laboratory}),
$$
because $\tilde{\Lambda}^{\natural}_{\vec v_b} = \tilde{\Lambda}_{\vec v_b}^{-1}$ for a unit-norm rotor.

Now let the charge move with velocity $\vec v = \vec v_b$ in the lab, and let $\vec d$ be the lab separation from its present position. In the rest frame $S'$, where the charge is permanently at rest at the origin, the field is the static Coulomb field. The lab separation transforms to the rest-frame separation
$$
\vec d' = \gamma\,d_\parallel\,\vec u_v + \vec d_\perp,
\qquad
d' = \sqrt{\gamma^2d_\parallel^2+d_\perp^2} = \gamma D :
$$
the parallel component is stretched by $\gamma$, which is length contraction read in the inverse direction — the rest-frame sphere of radius $d'$ appears in the lab as the Heaviside ellipsoid of Problem 2. The rest-frame field is
$$
\vec E' = \frac{ϙ}{4\pi\epsilon}\,\frac{\vec d'}{d'^3},
\qquad
\vec B' = 0,
\qquad
\tilde{F}' = i\sqrt{\epsilon}\,\vec E' .
$$
Transforming back to the lab, $\vec E_\parallel = \vec E'_\parallel$ and $\vec E_\perp = \gamma\vec E'_\perp$ (since $\vec B'=0$), so
$$
\vec E = \frac{ϙ}{4\pi\epsilon}\,\frac{\gamma\,\vec d}{d'^3}
= \frac{ϙ}{4\pi\epsilon}\,\frac{\gamma\,\vec d}{\gamma^3 D^3}
= \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,\vec d}{D^3},
$$
which is exactly the closed form of Problem 2. The magnetic field carried back by the boost is $\vec B = \frac{1}{c^2}\vec v\times\vec E$.

**Solution (c).** Because the charge's rest frame is inertial for *all* time when the motion is strictly uniform, the rest-frame field is the static Coulomb field at every event, with no acceleration correction; the boost is therefore exact, not a near-zone or low-velocity approximation. This is why the uniform case is the solvable one: the general Liénard–Wiechert field of an accelerated charge is not a boost of any static field, but here the boost is global and the whole field follows from it.

**Evidence.** (i) Rotor direction: the conjugated rest four-velocity had velocity exactly $-\vec v_b$ for the three boosts above. (ii) Transformation law: the similarity matched the standard component formulas to $6.7\times10^{-16}$ over sixty random boosts; the conjugation did not. (iii) Boosted Coulomb: starting from $\tilde{F}' = i\sqrt{\epsilon}\,\vec E'$ with the rest-frame Coulomb field, the lab field $\tilde{F} = \tilde{\Lambda}_{\vec v_b}\tilde{F}'\tilde{\Lambda}^{\natural}_{\vec v_b}$ matched the closed form of Problem 2 to $2.1\times10^{-17}$ over twenty random configurations. Using the opposite boost sign, or the wrong transformation law, did not match.

## Problem 6: Independent Checks, the Present-Position Fallacy, and the Invariants

**Statement.** (a) Verify the closed form on two independent cases. (b) Quantify the present-position fallacy by comparing the true field with the Coulomb field of the present position and with the Coulomb field of the retarded position. (c) Evaluate the invariants $I_1, I_2$, the biquaternion norm, and $\tilde{F}^2$, and state what they imply about radiation.

**Solution (a).** The two cases of Problems 3 and 4 are logically independent. The non-relativistic limit returns Coulomb with an $O(\beta^2)$ anisotropic correction and is insensitive to the $\gamma$-dependent factor that dominates at high speed; the ultrarelativistic transverse-plane value $|\vec E| = \gamma ϙ/(4\pi\epsilon d_\perp^2)$ is not accessible from the static theory by any limit and does not follow from Problem 3. Both are reproduced by the closed form exactly, and a third independent check — the rotor boost of Problem 5, which uses the biquaternion algebra rather than the Liénard–Wiechert formula — agrees as well. None of the checks is the configuration that suggested the formula: the closed form was obtained by eliminating $\vec R$ from the parent's formula, a route that could have produced the wrong present-position dependence while still passing the Coulomb limit.

**Solution (b).** The true electric field points along $\vec d$, so it is tempting to write it as the Coulomb field of the present position. It is not: with $\theta$ the angle between $\vec d$ and $\vec v$,
$$
\vec E = \Lambda(\theta)\,\vec E_C^{\text{present}},
\qquad
\vec E_C^{\text{present}} = \frac{ϙ}{4\pi\epsilon}\,\frac{\vec d}{d^3},
\qquad
\Lambda(\theta) = \frac{1-\beta^2}{\left(1-\beta^2\sin^2\theta\right)^{3/2}} = \frac{(1-\beta^2)\,d^3}{D^3}.
$$
The scalar factor $\Lambda$ runs from $1/\gamma^2$ along the motion to $\gamma$ in the transverse plane, so the present-position Coulomb formula fails by an anisotropic factor that is not a small correction at relativistic speeds. Nor is the retarded-position Coulomb formula correct: $\vec E_C^{\text{ret}} = \frac{ϙ}{4\pi\epsilon}\vec u_R/R^2$ points along $\vec u_R$, not along $\vec d$, and its magnitude differs as well. The correct statement is the exact one of Problem 2: the field is radial *from the present position* with the Heaviside magnitude; neither the retarded nor the present position alone determines it.

**Solution (c).** With $\vec B = \frac{1}{c^2}\vec v\times\vec E$ one has $\vec E\perp\vec B$ and
$$
I_1 = \vec E^2 - c^2\vec B^2 = \left(\vec u_R\cdot\vec E\right)^2
= \left(\frac{ϙ}{4\pi\epsilon}\,\frac{1-\beta^2}{D^2}\right)^{\!2} > 0,
\qquad
I_2 = \vec E\cdot\vec B = 0 .
$$
In the biquaternion normalization, with $\tilde{F} = i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ and $\vec H=\vec B/\mu$,
$$
\langle\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural} = -\epsilon\left(I_1 + 2ic\,I_2\right) = -\epsilon I_1 < 0,
\qquad
\tilde{F}^2 = -\langle\tilde{F}\rangle_{\natural} = \epsilon I_1 > 0 .
$$
The field is of electric type, is **not** null, and is not a zero divisor: $\langle\tilde{F}\rangle_{\natural}\neq0$ and $\tilde{F}^2\neq0$. It therefore carries no radiation, in agreement with $d\vec\beta/dt_r=0$; the contrast with the parent's acceleration field, whose $\tilde{F}_a$ *is* a zero divisor, is exact.

**Evidence.** (a) The three checks just listed gave $2.1\times10^{-17}$ (rotor boost), the exact $\beta^2$ law of Problem 3, and the exact $\gamma$ and $1/\gamma^2$ laws of Problem 4. (b) The ratio $|\vec E|/|\vec E_C^{\text{present}}| = \Lambda(\theta)$ was computed at $\beta=0.5,0.9,0.99$: at $\beta=0.9$ it was $0.190$ along the motion, $0.267$ at $30^\circ$, $0.773$ at $60^\circ$, and $2.294=\gamma$ transverse; at $\beta=0.99$ it was $0.0199$, $0.0303$, $0.1459$, and $7.089$. (c) Over thirty random uniform worldlines, $|I_1-(\vec u_R\cdot\vec E)^2| \le 1.7\times10^{-18}$, $|I_2|\le 4.1\times10^{-20}$, and $|\langle\tilde{F}\rangle_{\natural}+\epsilon I_1| \le 8.7\times10^{-19}$; $\tilde{F}^2$ was nonzero (of order $10^{-3}$ in the sample), so the field is not a zero divisor.

## What the Uniform Case Adds, and What It Leaves Open

**What it adds.** The uniform case turns the parent's implicit retarded construction into explicit algebra. The retarded position is available in closed form, and the identity $\vec u_R-\vec\beta = \vec d/R$ shows *why* the parent's velocity field can be written about the present position at all: the retarded combination that appears in the numerator is always parallel to the present separation, while the denominator collapses to $D=\sqrt{d_\parallel^2+d_\perp^2/\gamma^2}$. The resulting closed form is exactly the boost of the Coulomb field, so the parent's remark that the uniformly moving field is "equivalently ... obtained by applying the boost rotor" is confirmed as an exact statement, with the similarity law doing the work. The two limits are then checked independently, and the ultrarelativistic pancake is made quantitative.

**What it leaves open, recorded rather than closed.**

1. **"Purely transverse" is a statement about the pancake, not about every direction.** The exact content is: in the transverse plane the field is exactly perpendicular to $\vec v$, and at fixed impact parameter the longitudinal component is a factor $0.385/\gamma$ below the transverse peak. At a fixed direction the longitudinal fraction is $\cos\theta$, independent of $\gamma$, so the naive interpretation is false at every finite $\gamma$. This is a clarification, not a defect, but it is the step most easily smoothed over.
2. **Strictly uniform motion only.** The exact reduction to the boosted Coulomb field requires $d\vec v/dt_r\equiv0$, so that the charge's rest frame is inertial for all time. A charge that is only *instantaneously* unaccelerated at the emission event still carries the parent's acceleration field $\vec E_a$ at that event; the uniform-motion result is the limit in which that field is absent everywhere, and we did not attempt to bound the "almost uniform" correction.
3. **The $\beta\to1$ behaviour of the closed-form retarded position.** The coefficient of $R^2$ in the quadratic degenerates as $\beta\to1$: for a field point ahead of the charge along the motion ($d_\parallel>0$) the closed form gives $R\sim2d_\parallel\gamma^2\to\infty$, while for one behind it ($d_\parallel<0$) $R\to(d_\parallel^2+d_\perp^2)/(2|d_\parallel|)$, finitely (checked numerically at $\beta$ up to $0.99999$). The present-position field is finite throughout, so the limit $\beta\to1$ does not commute with reading $R$ off the quadratic. We did not pursue the caustic $\kappa\to0$ or superluminal worldlines; that remains the parent's gap 3.
4. **The similarity law is used, not derived.** We inherited $\tilde{F}' = \tilde{\Lambda}^{\natural}\tilde{F}\tilde{\Lambda}$ from the parent and verified it numerically against the standard boost, but did not derive it from the biquaternion representation of the rank-two field. That derivation remains the parent's Further Problem 3.
5. **The overall normalization of $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A}$.** The Maxwell article records a normalization caveat for this identification; we used the parent's fixed normalization and did not re-examine it.

## Summary

The field of a charge in uniform motion is the exactly solvable case of the parent's Liénard–Wiechert problem, and the reason it is solvable is that the retarded position is available in closed form. With $R = c(t-t_r)$ and the present separation $\vec d = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-(x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z)$, the identity $\vec R = \vec d+\vec\beta R$ gives the quadratic $(1-\beta^2)R^2-2\beta d_\parallel R-d^2=0$, whose physical root is the plus branch; from it follow
$$
D = R\kappa = \sqrt{d_\parallel^2+(1-\beta^2)d_\perp^2}
\qquad\text{and}\qquad
\vec u_R-\vec\beta = \frac{\vec d}{R},
\qquad
\vec u_R\cdot\vec d = D .
$$
The second of these is the key: the retarded combination in the numerator of the parent's velocity field is **parallel to the present separation**, so the field can be written entirely in terms of $\vec d$. Substituting into the parent's $\vec E_v$ gives the Heaviside ellipsoid field
$$
\vec E = \frac{ϙ}{4\pi\epsilon}\,\frac{(1-\beta^2)\,\vec d}{\left(d_\parallel^2+d_\perp^2/\gamma^2\right)^{3/2}},
\qquad
\vec B = \frac{1}{c^2}\,\vec v\times\vec E,
$$
which is radial from the *present* position, falls as $1/d^2$ at fixed direction, and is flattened along the motion. The acceleration field vanishes identically, so the field is of electric type and not null: $I_1 = \left(\frac{ϙ}{4\pi\epsilon}\frac{1-\beta^2}{D^2}\right)^2>0$, $I_2=0$, $\langle\tilde{F}\rangle_{\natural}=-\epsilon I_1\neq0$, $\tilde{F}^2=\epsilon I_1\neq0$; it is never a zero divisor and never radiation.

The non-relativistic limit returns Coulomb with an anisotropic $O(\beta^2)$ correction — no linear term — and the retarded position converges to the present one; the ultrarelativistic limit concentrates the field into a transverse pancake of angular half-width $\approx0.766/\gamma$, with transverse enhancement $\gamma$, axial suppression $1/\gamma^2$, and a longitudinal component at fixed impact parameter that is a factor $0.385/\gamma$ below the transverse peak, so the field becomes purely transverse in that precise (pancake) sense while remaining radial from the present position. A third, algebraically independent check boosts the rest-frame Coulomb field with the rotor $\tilde{\Lambda}_{\vec v_b}$ and recovers the same closed form to $2.1\times10^{-17}$. The convention used throughout is that the rotor built with $+\vec v_b$ carries the laboratory to the frame moving with $+\vec v_b$, and that the field transforms by the similarity $\tilde{F}' = \tilde{\Lambda}^{\natural}_{\vec v_b}\tilde{F}\tilde{\Lambda}_{\vec v_b}$, not by four-vector rotor conjugation.

Two things are recorded rather than closed. The first is a clarification: "purely transverse in the ultrarelativistic limit" is exact for the transverse plane and at fixed impact parameter, but false at every finite $\gamma$ if read as a statement about every fixed direction, where the longitudinal fraction is $\gamma$-independent. The second is that the exact reduction to the boosted Coulomb field assumes strictly uniform motion; a charge only instantaneously unaccelerated still carries an acceleration field at the emission event.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \epsilon_{\mu\nu\lambda}\vec e_\lambda$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace, scalar subspace |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}, \Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | Biquaternionic gradient, its quaternion conjugate, d'Alembertian |
| $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t$ | Temporal component of the gradient |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\tilde{A} = \frac{i\phi}{c}e_t + \vec A$ | Potential biquaternion |
| $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_t + \sqrt{\mu}\,\vec J$ | Source biquaternion; $\rho$ is the charge density |
| $\epsilon, \mu$, $c = 1/\sqrt{\epsilon\mu}$ | Permittivity, permeability, speed of light in the medium |
| $\vec H = \vec B/\mu$ | Magnetic field; $\vec B$ the magnetic induction |
| $ϙ$, $x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z$, $\vec v(t)$ | Charge, worldline, coordinate velocity |
| $t_r = t - R/c$ | Retarded time (defined implicitly) |
| $\vec R = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-(x_q\,\vec e_x+y_q\,\vec e_y+z_q\,\vec e_z)(t_r)$, $R = |\vec R|$, $\vec u_R = \vec R/R$ | Retarded separation, its length and direction |
| $\vec\beta = \vec v/c$ | Coordinate velocity over $c$ (constant in this exercise) |
| $\kappa = 1-\vec u_R\cdot\vec\beta$, $D = R\kappa$ | Retarded denominator (inherited) |
| $\vec d = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-(x_q(t)\,\vec e_x+y_q(t)\,\vec e_y+z_q(t)\,\vec e_z)$, $d = |\vec d|$, $\vec u_d = \vec d/d$ | Present separation from the charge's present position |
| $d_\parallel = \vec u_v\cdot\vec d$, $d_\perp^2 = d^2-d_\parallel^2$ | Components parallel and perpendicular to the motion |
| $D = \sqrt{d_\parallel^2+(1-\beta^2)d_\perp^2} = \sqrt{d_\parallel^2+d_\perp^2/\gamma^2}$ | Retarded denominator in closed form |
| $\gamma = (1-\beta^2)^{-1/2}$ | Lorentz factor of the (constant) velocity |
| $\vec u_R-\vec\beta = \vec d/R$, $\vec u_R\cdot\vec d = D$ | Present-position identities of Problem 1 |
| $\vec E, \vec B$ | Electric field and magnetic induction; $\vec B = \vec v\times\vec E/c^2$ |
| $I_1 = \vec E^2-c^2\vec B^2$, $I_2 = \vec E\cdot\vec B$ | Field invariants |
| $\tilde{\Lambda}_{\vec v_b} = \cosh\frac{\psi_b}{2}+i\sinh\frac{\psi_b}{2}\vec u$, $\tanh\psi_b = v_b/c$ | Boost rotor; carries the lab to the frame moving with $+\vec v_b$ |
| $\tilde{F}' = \tilde{\Lambda}^{\natural}_{\vec v_b}\tilde{F}\tilde{\Lambda}_{\vec v_b}$ | Boost of the field (similarity, not rotor conjugation) |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (recorded, not used) |

## Further Reading

The further reading of this exercise is the parent and companion articles of this series, all present in `articles_physics/`; the standard textbook references for the Liénard–Wiechert field and its uniform-motion specialization are listed in the Further Reading sections of the parent and the theory article.

- *Introduction to the Biquaternion Universe* — the algebra, the two sectors, and the local complex structure.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the four-vectors, the biquaternion norm, and the zero-divisor cone on which the retarded separation sits.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian sector, the conjugation action, and the trace formula.
- *Maxwell's Equations in the Biquaternionic Formulation* — the gradient, the field strength, the potential and source, and the retarded solution.
- *The Field-Strength Biquaternion and Its Invariants* — the invariants $I_1,I_2$ and the null/zero-divisor characterization of radiation used in Problem 6.
- *Radiation from Accelerated Charges in Biquaternionic Form* — the theory article: the retarded solution and the Liénard–Wiechert potential.
- *Exercise: The Electromagnetic Field of a Moving Charge* — the direct parent: the general velocity field specialized here, and the similarity transformation law of the field.
- *The Lorentz Transformation as a Biquaternionic Rotation* — the boost rotor, its direction convention, and the open question on higher-rank tensors.
- *Exercise: Boosting a Four-Velocity and Rapidity Composition* — the convention that the rotor with $+\vec v_b$ carries the laboratory to the moving frame.
- *Relativistic Mechanics in Biquaternionic Form* — the four-velocity conventions used in the rotor check.

