# __The Variational Principle and the Dirac Equation in Biquaternionic Polar Variables__

## Introduction

*The Dirac Equation in Biquaternionic Polar Variables* substitutes the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ into the equation. This article substitutes the same word into the *action*, and reads the Lagrangian and the Euler–Lagrange equations that come out.

The action is the element-form companion's:

$$
S=\frac{\hbar c}{2}\int\mathrm{d}^4r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_\Phi\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr].
$$

The word is a bijection from eight parameters onto the units of $\mathbb{B}$, so the substitution adds nothing and drops nothing: the eight parameters are coordinates on the carrier, and the polar action is the element action in those coordinates.

**Two things are found, and they are the article's content.**

*First, the kinetic term comes out in closed form, and the closed form settles the momentum table.* Writing $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$ for the rotor's body angular velocity and $\hat n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ for the boost axis carried into the body frame, the kinetic term is $\hbar c\,r^{2}(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r})$. The momentum conjugate to the angle is $\hbar c\,r^{2}\cosh\theta_{\mathrm{rpd}}$, the density times the Lorentz factor; the momenta conjugate to the scale, to the rapidity and to the two boost-axis angles are absent from the display and are therefore zero identically, on every configuration and not merely on the parent's flow; and the rotor's momentum is $-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$, a closed form rather than a projector.

*Second, the mass term needs a fixed direction.* Written on the frame's parts, the element-form mass bilinear vanishes identically, because the two parts sit in complementary right ideals and $\mathrm{Sc}$ is cyclic. The mass returns only when the bilinear carries a fixed unit direction inside it, which is the parent's value-consistent display $\tilde\Xi_R\mapsto\tilde\Xi_Ri\vec v$. The polar action therefore carries a direction that the element action does not, and the direction is the price of writing the two parts as values. The direction is not free: only the directions perpendicular to the frame's third direction give a mass.

**Why this differs from the Schrödinger companion.** The two kinetic terms have the same shape and the opposite sign, and the rotor enters here through the boost axis carried into the body frame. The difference that matters is the factor $\sinh\theta_{\mathrm{rpd}}$: the spin's momentum is proportional to the boost, so it vanishes in the rest frame, however fast the rotor turns. The canonical structure is therefore a statement about a boosted frame. At rest the spin joins the scale and the velocity in having no momentum, and the action's dynamical content is the phase alone.

**The constant setting throughout.** As in the polar parent, the Hamiltonian is a constant element and the equation is an ordinary differential equation in $t'$. The spatial derivatives are set to zero: the field is homogeneous, which is the setting in which the polar flow is the parent's flow. The operator setting is not treated; it is the Madelung case of the scalar theory and its variational principle is in the classical literature.

The formalism is that of *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, and the action principle is that of *The Action Principle and the Non-Quantum Limit in Biquaternionic Form*; this article applies the principle to the Dirac equation in its polar form.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $e_t=1$, $\vec e_\mu^{2}=-e_t$, $i$ central, $\mathrm{Sc}$ the coefficient of $e_t$, $\mathrm{Tr}=2\,\mathrm{Sc}$. The conjugations are $*$ and $\natural$; the pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout, as in both element articles. Every symbol is defined where it first appears, and the table at the end collects them. The time variable is $t'$, so the derivative term is $\hbar c\,\partial_{r'_t}=\hbar\,\partial_{t'}$; the element-form companion uses $r'_t$ and the two are the same equation.

**The parameters and their ranges.** $r>0$; $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$; $\theta_{\mathrm{rpd}}\ge0$ with $\tilde U_{\Psi,\mathrm b}=\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$; $\theta_{\mathrm{axr}}\in[0,2\pi)$ with $\tilde u_{\mathrm r}=\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$; $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ unit real vectors. The density is $\rho=r^{2}$ and the Lorentz factor is $\gamma=\cosh\theta_{\mathrm{rpd}}$, so $\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2r^{2}\cosh\theta_{\mathrm{rpd}}$.

## The Substitution: The Word and the Two Parts

The element action is written on two parts, and the word is written for one element. The parts must therefore be named before the substitution can be made.

**The parts are the frame's.** The frame declares one direction, $\vec e_z$, in order to read the value of an element. The idempotents built from it are

$$
\Pi_\pm=\tfrac12\bigl(e_t\pm i\vec e_z\bigr),
\qquad
\Pi_\pm^{2}=\Pi_\pm,
\qquad
\Pi_+\Pi_-=0,
\qquad
\Pi_\pm^{*}=\Pi_\pm,
\qquad
\Pi_\pm^{\natural}=\Pi_\mp .
$$

The parts are $\tilde\Xi_L=\tilde\Xi\Pi_+$ and $\tilde\Xi_R=\tilde\Xi\Pi_-$. Each lies in a right ideal, hence is a zero divisor, hence has no polar word of its own; the word is a word for the sum. That is not an obstacle to the substitution, because the action is polynomial in the parts and the parts are polynomial in the field.

**Two identities are used, and both are exact.** First, the star conjugation fixes the idempotents, so $\tilde\Xi_{L,R}^{*}=\Pi_{\pm}\tilde\Xi^{*}$ and the kinetic terms can be written with the field on the right:

$$
\mathrm{Sc}\bigl[\tilde\Xi_{L,R}^{*}\,\dot{\tilde\Xi}_{L,R}\bigr]
=\mathrm{Sc}\bigl[\Pi_{\pm}\tilde\Xi^{*}\dot{\tilde\Xi}\Pi_{\pm}\bigr].
$$

Second, the two operators coincide in the homogeneous setting: with $\partial_\eta=0$, both $\tilde\nabla_\Phi$ and $(\tilde\nabla_\Phi)^{\natural}$ reduce to $-i\partial_{r'_t}$.

**The kinetic term in the homogeneous setting.** Substituting both identities,

$$
\boxed{\;
\mathcal{L}_{\mathrm{kin}}=\hbar c\,\mathrm{Im}\,\mathrm{Sc}\Bigl[\Pi_+\,\tilde\Xi^{*}\dot{\tilde\Xi}\,\Pi_++\Pi_-\,\tilde\Xi^{*}\dot{\tilde\Xi}\,\Pi_-\,\Bigr]\;}
$$

The display is the article's starting point. It is one line, it is exact, and it says what the kinetic term reads: the field's logarithmic derivative, projected onto the two ideals, traced, and taken imaginary. The $\mathrm{Im}$ is not a choice: the action's kinetic term is $\mathrm{Re}\,\mathrm{Sc}[\tilde\Xi_{L,R}^{*}(-i\hbar c\,\dot{\tilde\Xi}_{L,R})]$, and $\mathrm{Re}(-iZ)=\mathrm{Im}(Z)$.

**What the display does not depend on.** The projectors can be removed from it, because $\mathrm{Sc}$ is cyclic: $\mathrm{Sc}[\Pi_\pm X\Pi_\pm]=\mathrm{Sc}[\Pi_\pm^{2}X]=\mathrm{Sc}[\Pi_\pm X]$, and the two together give $\mathrm{Sc}[X]$. That is what §*The Kinetic Term* uses, and it is an identity of the trace and the idempotents rather than an approximation about the field.

**The logarithmic derivative in polar parameters.** The parent's decomposition is

$$
\tilde\Xi^{-1}\dot{\tilde\Xi}=\frac{\dot r}{r}+i\,\dot\theta_{\mathrm{pha}}
+\tilde u_{\mathrm r}^{-1}\bigl(\tilde U_{\Psi,\mathrm b}^{-1}\dot{\tilde U}_{\Psi,\mathrm b}\bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r},
$$

the scale, the phase, the boost connection and the rotor connection. Substituting this into the boxed display is the whole of the computation, and the next two sections read the result.

## The Kinetic Term

The kinetic term comes out in closed form, and the closed form settles the momentum table.

**The projector is inert on the scalar part.** $\mathrm{Sc}$ is cyclic, so $\mathrm{Sc}[\Pi_+X\Pi_+]=\mathrm{Sc}[\Pi_+^{2}X]=\mathrm{Sc}[\Pi_+X]$, and the two projected traces add to $\mathrm{Sc}[(\Pi_++\Pi_-)X]=\mathrm{Sc}[X]$. The kinetic term is therefore

$$
\mathcal{L}_{\mathrm{kin}}=\hbar c\,\mathrm{Im}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\dot{\tilde\Xi}\bigr],
$$

and the frame enters it only through the field. The projectors are what makes the two parts of the action add with the same sign; on the scalar part they do nothing.

**The closed form.** The parent's bilinear is $\tilde\Xi^{*}\tilde\Xi=r^{2}\tilde u_{\mathrm r}^{-1}\tilde U_{\Psi,\mathrm b}^{2}\tilde u_{\mathrm r}$, and $\tilde\Xi^{-1}\dot{\tilde\Xi}$ is the parent's four-bracket sum. The scalar part of the bracket is then

$$
\mathrm{Sc}\bigl[\tilde\Xi^{*}\dot{\tilde\Xi}\bigr]
=r^{2}\Bigl(\gamma\frac{\dot r}{r}+\tfrac12\dot\gamma\Bigr)
+i\,r^{2}\Bigl(\gamma\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr).
$$

Four of the five contributions are real and drop out of the imaginary part. The scale's is $\dot r/r$, real. The boost's is $\mathrm{Sc}[\tilde U_{\Psi,\mathrm b}\dot{\tilde U}_{\Psi,\mathrm b}]=\tfrac12\dot\gamma$, real because $\mathrm{Sc}[\tilde U_{\Psi,\mathrm b}^{2}]=\gamma$ is real. The rotor's diagonal part is $\mathrm{Sc}[\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}]=0$, because that connection is a pure vector. The fifth is the rotor's cross term with the boost axis, $\mathrm{Sc}[\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\dot{\tilde u}_{\mathrm r}]=-\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}$: the minus is the quaternion product of two pure vectors, $\mathrm{Sc}[\vec a\vec b]=-\vec a\cdot\vec b$, and $\dot{\tilde u}_{\mathrm r}=\tilde u_{\mathrm r}\vec\omega_{\mathrm r}$. Hence

$$
\boxed{\;\mathcal{L}_{\mathrm{kin}}=\hbar c\,r^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr).\;}
$$

with $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$ the rotor's body angular velocity and $\hat n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ the boost axis carried into the body frame.

**The momenta follow by inspection.** The display contains the rates of $r$, of $\theta_{\mathrm{rpd}}$ and of $\vec u_{\mathrm b}$ nowhere: those three enter through $r^{2}$, $\cosh\theta_{\mathrm{rpd}}$ and $\hat n_{\mathrm{rot}}$ alone. So

$$
p_r=0,\qquad p_{\theta_{\mathrm{rpd}}}=0,\qquad p_{u_{\mathrm b}}=0\ \text{(two components)},
$$

identically, for every configuration and every velocity. The other four are

$$
p_{\theta_{\mathrm{pha}}}=\hbar c\,r^{2}\cosh\theta_{\mathrm{rpd}}=\hbar c\,\rho\gamma,
\qquad
\vec p_{\mathrm{spin}}=-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}},
$$

where $\vec p_{\mathrm{spin}}$ is the vector whose contraction with $\vec\omega_{\mathrm r}$ gives the rotor's three momenta. These are identities about the word and not samples: the three vanishing momenta are the absence of three rates from the display, and the two surviving ones are read off it.

**Why the scale and the boost carry no momentum.** The scale enters the scalar part as $\gamma\dot r/r$, which is real, and the boost enters as $\tfrac12\dot\gamma$, which is real too. A real contribution to $\mathrm{Sc}[\tilde\Xi^{*}\dot{\tilde\Xi}]$ is invisible to the imaginary part, and the imaginary part is the whole of the kinetic term. That is the complete reason, and it is the same reason in both cases: the two coordinates multiply the field by real factors of unit norm.

**The spin's momentum is locked to the boost.** $\vec p_{\mathrm{spin}}$ is proportional to $\sinh\theta_{\mathrm{rpd}}$. In the rest frame the rotor carries no momentum at all, however fast it turns, and the action's dynamical content is the phase alone. This is the sharpest statement the closed form makes, and it is the one the projector display could not make.

**The sign, and the overall factor.** The Dirac kinetic term is $+\hbar c\,\mathrm{Im}\,\mathrm{Sc}[\tilde\Xi^{*}\dot{\tilde\Xi}]$; the Schrödinger one is $-\hbar c\,\mathrm{Im}\,\mathrm{Sc}[\tilde\Xi^{*}\dot{\tilde\Xi}]$. The difference is one operator and one antisymmetrization. The Dirac term is $\mathrm{Re}\,\mathrm{Sc}[\tilde\Xi^{*}(-i\hbar c\,\partial_{t'})\tilde\Xi]$, and $-i\hbar c\,\partial_{t'}$ is self-adjoint, so its expectation has a real part and no symmetrization is needed. The Schrödinger term is $\mathrm{Re}\,\mathrm{Sc}[\tilde\Xi^{*}(i\hbar c\,\partial_{r'_t})\tilde\Xi]$, and $i\hbar c\,\partial_{r'_t}$ is anti-self-adjoint, so its expectation is purely imaginary and the action must antisymmetrize: $\tfrac{i\hbar c}{2}(\tilde\Xi^{*}\dot{\tilde\Xi}-\dot{\tilde\Xi}^{*}\tilde\Xi)$ has scalar part $-\hbar c\,\mathrm{Im}\,\mathrm{Sc}[\tilde\Xi^{*}\dot{\tilde\Xi}]$, which is where the minus comes from. The sign is a fact about the two equations and not a convention, while the factor $r^{2}\cosh\theta_{\mathrm{rpd}}$ is common to both and is the physical statement.

## The Mass Term and the Fixed Direction

The mass term of the element action is off-diagonal in the parts, and on the frame's parts it vanishes.

**The vanishing, in one line.** With $\tilde\Xi_L=\tilde\Xi\Pi_+$ and $\tilde\Xi_R=\tilde\Xi\Pi_-$,

$$
\mathrm{Sc}\bigl[\tilde\Xi_L^{*}\tilde\Xi_R\bigr]
=\mathrm{Sc}\bigl[\Pi_+\tilde\Xi^{*}\tilde\Xi\Pi_-\bigr]
=\mathrm{Sc}\bigl[\Pi_-\Pi_+\tilde\Xi^{*}\tilde\Xi\bigr]=0,
$$

using $\Pi_+^{*}=\Pi_+$, the cyclicity of $\mathrm{Sc}$, and $\Pi_-\Pi_+=0$. The conjugate term vanishes the same way. Nothing is assumed here beyond the idempotents and the trace property, so the vanishing needs no sample.

**What the vanishing means.** It is the variational form of the parent's warning. The parent says that reading the pair's letters as values gives no non-zero solution, and that the value-consistent display carries the direction $i\vec v$. The action says the same thing from the other side: a mass term that couples two complementary ideals is zero, so a value-split action has no mass at all, and the mass must come back through an element that reverses the value.

**The repair, and its form.** Right multiplication by $i\vec v$ with $\vec v$ a fixed unit spatial direction reverses the value, because $\vec v\vec e_z=-\vec e_z\vec v$ for $\vec v\perp\vec e_z$. So

$$
\mathrm{Sc}\bigl[\tilde\Xi_L^{*}\tilde\Xi_R\,i\vec v\bigr]\ne0
\qquad\text{for }\vec v\perp\vec e_z,
$$

and it is zero for $\vec v\parallel\vec e_z$, so the direction is fixed by the frame's third direction and is not a free choice: only the directions that reverse the value give a mass. The mass term of the polar action is therefore

$$
\mathcal{L}_{\mathrm{mass}}=-\hbar c\,k_m\,r^{2}\,\mathcal{V},
\qquad
\mathcal{V}=\frac{2}{r^{2}}\,\mathrm{Re}\,\mathrm{Sc}\bigl[\tilde\Xi_L^{*}\tilde\Xi_R\,i\vec v\bigr],
$$

with $\mathcal{V}$ a function of the boost, of the rotor and of the fixed direction, and with no dependence on $r$ or on $\theta_{\mathrm{pha}}$. The direction sits on the same side in both halves of the bilinear: the star of $\tilde\Xi_Ri\vec v$ is $i\vec v\,\tilde\Xi_R^{*}$, because $i\vec v$ is Hermitian, so the second half is $i\vec v\,\tilde\Xi_R^{*}\tilde\Xi_L$ and the two halves are conjugates. Writing the direction on the right in both halves, as an earlier version did, cancels the real part and makes the mass term vanish; the direction belongs to the element, and the conjugation moves it.

**The polar action, in full.**

$$
\boxed{\;
S=\int\mathrm{d}t'\;\hbar c\,\Bigl\{r^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr)-r^{2}k_m\,\mathcal{V}\Bigr\}\;}
$$

The scale enters as $r^{2}$ in both terms. The phase enters only through its velocity. The boost enters through $\cosh\theta_{\mathrm{rpd}}$, through $\sinh\theta_{\mathrm{rpd}}$ and through the axis $\hat n_{\mathrm{rot}}$, and not through its own rate. The rotor enters through its body angular velocity and through the axis it carries. Nothing else enters.

**The overall factor.** The element action carries $\hbar c/2$; the box has $\hbar c$. The factor is a convention on the action and cancels from every Euler–Lagrange equation, and the article writes it this way so that the phase momentum comes out $\hbar c\rho\gamma$, the time component of the density current and the normalization of the standard Dirac action, whose kinetic term carries no $\tfrac12$. The sign, and the reason it is opposite to the Schrödinger companion's, is in §*The Kinetic Term*.

## The Euler–Lagrange Equations

The Lagrangian is a one-form plus a potential, and that single fact is the constraint structure.

**The Lagrangian is a one-form plus a potential.** Every velocity enters the display linearly, so

$$
\mathcal{L}=A_x(q)\,\dot q^{x}-U(q),\qquad
U=\hbar c\,k_m\,r^{2}\,\mathcal V,
$$

with the eight coordinates $q=(r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}}$, two angles of $\vec u_{\mathrm b}$, three of $\tilde u_{\mathrm r})$, and with the one-form

$$
A=\hbar c\,r^{2}\Bigl[\cosh\theta_{\mathrm{rpd}}\,d\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\bigl(\tilde u_{\mathrm r}^{-1}d\tilde u_{\mathrm r}\bigr)\Bigr].
$$

The eight momenta are the components of $A$: $p_x=A_x(q)$. That is why three of them vanish, and it is also why no velocity can be recovered from a momentum — the Hessian $\partial^{2}\mathcal L/\partial\dot q^{x}\partial\dot q^{y}$ vanishes identically.

**The equations are $\Omega\dot q=\mathrm{d}U$.** With $\Omega=\mathrm{d}A$ the exterior derivative, a closed two-form because $\mathrm{d}^{2}=0$, the Euler–Lagrange equations of a linear Lagrangian are

$$
\Omega_{xy}\,\dot q^{y}=\partial_x U .
$$

There are eight of them and they are first order. Three of them can be written at once.

**Vary the phase.** The angle appears only through $\dot\theta_{\mathrm{pha}}$, and $\mathcal V$ does not depend on it, so

$$
\frac{\mathrm{d}}{\mathrm{d}t'}\Bigl(r^{2}\cosh\theta_{\mathrm{rpd}}\Bigr)=0,
$$

the conservation of the phase momentum, which is the polar form of the electric charge.

**Vary the scale.** The scale appears as $r^{2}$ in every term, and the rotor term carries the same $r^{2}$ as the phase term, so the equation is

$$
\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}=k_m\,\mathcal V .
$$

An earlier version of this article carried a term $\partial(\hbar c\,\mathcal L_{\mathrm{rot}})/\partial r$ here. That term is zero: the rotor's kinetic term depends on $r$ only through the common factor $r^{2}$, which is what makes the whole Lagrangian a one-form. What the scale's equation carries instead is the rotor term itself, at the same weight as in the kinetic display.

**Vary the rapidity.** The rapidity appears through $\cosh\theta_{\mathrm{rpd}}$ and $\sinh\theta_{\mathrm{rpd}}$, so its equation is

$$
\sinh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\cosh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}=k_m\,\frac{\partial\mathcal V}{\partial\theta_{\mathrm{rpd}}}.
$$

**The two together fix the phase rate.** The pair is linear in $\dot\theta_{\mathrm{pha}}$ and in $\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}$, and its determinant is $\cosh^{2}\theta_{\mathrm{rpd}}-\sinh^{2}\theta_{\mathrm{rpd}}=1$. Hence

$$
\dot\theta_{\mathrm{pha}}=k_m\Bigl(\cosh\theta_{\mathrm{rpd}}\,\mathcal V-\sinh\theta_{\mathrm{rpd}}\,\frac{\partial\mathcal V}{\partial\theta_{\mathrm{rpd}}}\Bigr),
\qquad
\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}=k_m\Bigl(\sinh\theta_{\mathrm{rpd}}\,\mathcal V-\cosh\theta_{\mathrm{rpd}}\,\frac{\partial\mathcal V}{\partial\theta_{\mathrm{rpd}}}\Bigr).
$$

At rest the first line is $\dot\theta_{\mathrm{pha}}=k_m\mathcal V$, which is the parent's rate.

**Vary the boost axis.** The axis enters only through $\hat n_{\mathrm{rot}}$, and $\mathcal V$ depends on it as well, so its two equations are

$$
\sinh\theta_{\mathrm{rpd}}\;\frac{\partial}{\partial u_{\mathrm b}}\bigl(\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\bigr)+k_m\,\frac{\partial\mathcal V}{\partial u_{\mathrm b}}=0 .
$$

They contain $\vec\omega_{\mathrm r}$ and not $\dot\theta_{\mathrm{pha}}$, so they fix the rotor's rotation transverse to the boost axis.

**Vary the rotor.** Its three momenta do not vanish, so its three equations are dynamical. Together with the phase's equation they are four first-order equations for four coordinates; the four constraints restrict the rest.

**The constraints, and the bracket that is not zero.** The four momenta $p_r$, $p_{\theta_{\mathrm{rpd}}}$ and $p_{u_{\mathrm b}}$ vanish identically, so their four equations contain no acceleration: they are the primary constraints. They are second class, and that is a computation rather than an expectation. Take two of them, $p_r$ and $p_{\theta_{\mathrm{pha}}}-A_\theta$; the canonical bracket is

$$
\bigl\{p_r,\;p_{\theta_{\mathrm{pha}}}-A_\theta\bigr\}
=\frac{\partial A_\theta}{\partial r}
=2\hbar c\,r\cosh\theta_{\mathrm{rpd}}\ne0
$$

for every $r>0$. One non-vanishing bracket is enough: the constraints are second class, the Dirac bracket differs from the Poisson bracket, and the Lagrangian is degenerate in the sense of Dirac rather than merely in the sense of having cyclic coordinates.

**What the system is, honestly.** Eight equations, eight parameters. Four momenta vanish identically and four do not; of the four that do not, one is the phase's and three are the rotor's. Closing the system — the Dirac bracket and the closed flow that reproduces the parent's rates — is not done here. What the closed form settles is the table, which is now an identity, the reason each entry has the value it has, and the character of the rotor's momentum, which is proportional to the boost's $\sinh$ and therefore absent at rest.

**The parent's flow, at rest.** At $\theta_{\mathrm{rpd}}=0$ the two rate equations give $\dot\theta_{\mathrm{pha}}=k_m\mathcal V$ and $\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}=-k_m\partial_{\theta_{\mathrm{rpd}}}\mathcal V$, with $r$ and the rapidity constant. The phase rate is the parent's. The rotor's rate along the boost axis comes from the potential's rapidity dependence, and the two rates transverse to it come from the rotor's own equations. Whether that reproduces the parent's gap rate is the closure question, and the article does not assume the answer.

## The Four Brackets and the Parameter Basis

Two bases of the eight-dimensional tangent space at a unit, and one change of basis.

**The bracket basis.** The parent decomposes $\tilde\Xi^{-1}\partial_\mu\tilde\Xi$ into a real scalar, a central imaginary, a Hermitian element and a real vector: four objects of four different algebraic types, each carrying one physical role — scale, phase, boost connection, rotor connection.

**The parameter basis.** The eight derivatives $\partial\tilde\Xi/\partial r$, $\partial\tilde\Xi/\partial\theta_{\mathrm{pha}}$, $\partial\tilde\Xi/\partial\theta_{\mathrm{rpd}}$, $\partial\tilde\Xi/\partial u_{\mathrm b}$, $\partial\tilde\Xi/\partial\theta_{\mathrm{axr}}$, $\partial\tilde\Xi/\partial u_{\mathrm r}$ span the same eight directions.

**Three statements about the relation.**

*The equivalence is exact.* The eight parameter equations are the eight real components of the equation in the parameter basis, and the word is a bijection, so the parameter equations and the equation are the same content. This is the Jacobian's invertibility and nothing more.

*The brackets are cleaner.* The four brackets are four objects of four types, each with one role. The parameter equations mix them, because the parameterisation is non-linear and the derivative of one parameter can carry pieces of several brackets: differentiating the word with respect to $\theta_{\mathrm{axr}}$ moves the rotor, which moves the boost axis as seen from the body frame, so the rotor's equation carries a piece of the boost connection.

*The parameter equations are not weaker.* They are the same equations in another basis, not a subset of them. A reader who finds fewer independent parameter equations than bracket equations has counted constraints as equations, which is what the four vanishing momenta are.

**What the polar action adds to this.** Nothing about the equation. The E-L equations, when closed, are the equation's components in the parameter basis; the four brackets remain the natural form, and the article does not claim that the parameter equations are simpler. The polar action's contribution is the constraint structure: it exhibits which parameters are dynamical and which are not, and that is a statement the bracket form does not make.

## Takabayasi's Multipliers and Why They Are Absent

The comparison is worth stating precisely, because the two formulations are usually confused.

**Takabayasi's tensor formulation carries three multipliers.** The spin-$1/2$ field is written with a unit vector field for the spin direction, and the unit condition $\hat s^{2}=-e_t$ is imposed by a Lagrange multiplier $A_1$. Further conditions on the velocity and on the spin's transport carry $A_2$ and $A_3$. The multipliers are not optional in that formulation: the spin direction is a vector constrained to the unit hyperboloid, and the constraint has to be imposed.

**The word absorbs the unit conditions.** The rotor is $\tilde u_{\mathrm r}=\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$ with a unit axis, so $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ satisfies $\hat s^{2}=\tilde u_{\mathrm r}\vec e_z^{2}\tilde u_{\mathrm r}^{-1}=-e_t$ identically, for every value of the three parameters. The unit condition is not imposed; it is a consequence of the parameterisation. The same holds for the boost: $\tilde U_{\Psi,\mathrm b}\tilde U_{\Psi,\mathrm b}^{\natural}=e_t$ identically.

**So no multipliers are needed for the unit conditions, and the article says exactly that.** It does not say that the polar action has no constraints. The constraints are there, four of them, and they are Euler–Lagrange equations: the vanishing of the momenta conjugate to the scale and to the boost. Those constraints come from the *structure* of the kinetic term, not from a unit condition, and a multiplier would not remove them.

**The correspondence is exact in one respect and only one.** Takabayasi's velocity field enters the Lagrangian algebraically, without a time derivative, and so does the boost here: $p_{\theta_{\mathrm{rpd}}}=0=p_{u_{\mathrm b}}$. Takabayasi's spin direction carries a transport equation, and so does the rotor here: away from rest its three momenta are non-zero, they are $\vec p_{\mathrm{spin}}=-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$, and its three equations are dynamical. The agreement with Takabayasi is therefore an agreement about a boosted frame. At rest the spin's momentum vanishes, and the polar action's spin sector becomes constrained as well; the article states this because the closed form makes it visible, and does not claim it for Takabayasi's formulation, where the spin momentum is not proportional to a rapidity.

## What the Polar Variational Principle Adds

**Adds.** The polar form of the element action in one closed display: the kinetic term is $\hbar c\,r^{2}(\cosh\theta_{\mathrm{rpd}}\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r})$. The momentum table as an identity rather than a sample: $p_r=p_{\theta_{\mathrm{rpd}}}=p_{u_{\mathrm b}}=0$, $p_{\theta_{\mathrm{pha}}}=\hbar c\rho\gamma$ and $\vec p_{\mathrm{spin}}=-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$. The reason for each entry, which is the reality of three contributions to the scalar part. The reason the mass term needs a fixed direction, which is the variational form of the parent's value-reading warning, together with the fact that the direction must be perpendicular to the frame's third direction. The bracket that makes the four primary constraints second class, computed and not assumed.

**Does not add.** No new prediction: the equation is the parent's. No new solution: the flow is the parent's. No closure of the constrained system. No simplification of the four brackets, which remain the natural form.

**The structural statement, stated exactly.** Away from rest the canonical objects are the phase and the spin: $p_{\theta_{\mathrm{pha}}}=\hbar c\rho\gamma$ and $\vec p_{\mathrm{spin}}=-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$, both non-zero, both functions of the coordinates alone, and neither recoverable from the other. The scale and the velocity are never canonical: their momenta vanish identically in every frame.

**The qualification is part of the statement.** The spin's momentum is proportional to $\sinh\theta_{\mathrm{rpd}}$, so at rest it vanishes and the spin is not canonical either. An earlier version of this paragraph claimed the phase and the spin unconditionally. That claim was wrong at $\theta_{\mathrm{rpd}}=0$, and the closed form is what shows it: the spin enters the kinetic term only through its cross term with the boost, so a frame at rest has no spin momentum to speak of. What survives at rest is the phase alone.

## Open Questions

1. **Closure.** The four primary constraints are second class, and their consistency conditions generate further relations. Whether the Dirac bracket closes the system and reproduces the parent's flow — the gap rate for the rotor, and constant $r$ and rapidity — is not established here. The computation is now finite and explicit: the one-form is known, the constraints are known, and what remains is the bracket.

2. **The rest frame.** At $\theta_{\mathrm{rpd}}=0$ the spin's momentum vanishes with the scale's and the velocity's. The kinetic one-form then has four fewer non-zero components, and the rotor's equations become constraints. Whether the polar parameterization still describes the rest-frame flow, or whether the rest frame is a singular point of the action that requires its own treatment, is not settled. The parent's flow is regular there; the action may not be.

3. **The direction in the mass term.** The mass bilinear on the frame's parts needs a fixed unit direction $i\vec v$ with $\vec v\perp\vec e_z$. Whether the direction can be dispensed with by a different naming of the parts — one that is not the frame's — is not settled. If it cannot, then the biquaternionic Dirac action requires one declared direction, which is the same declaration the value test makes, and the requirement is a property of the algebra rather than of the formalism.

4. **The operator setting.** The article sets the spatial derivatives to zero. Whether the parameterization absorbs the constraints in the inhomogeneous case, where $\tilde\nabla_\Phi$ carries the Laplacian-like part, is not attempted.

## Summary

The polar action of the biquaternionic Dirac field is the element action of the companion with the word substituted, and its kinetic term has a closed form:

$$
S=\int\mathrm{d}t'\;\hbar c\,\Bigl\{r^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\;\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr)-r^{2}k_m\,\mathcal{V}\Bigr\}.
$$

Everything the article says about the momenta follows from that one display, by inspection rather than by sampling. The scale, the rapidity and the boost axis appear without their rates, so their three momenta vanish identically. The phase appears linearly, with coefficient $r^{2}\cosh\theta_{\mathrm{rpd}}=\rho\gamma$, so its momentum is the density times the Lorentz factor, the time component of the density current. The rotor appears through its cross term with the boost axis, so its momentum is $-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$: a closed form, and one that vanishes at rest.

The mass term needs a fixed direction, perpendicular to the frame's third direction, and the direction sits on the same side of the bilinear in both halves; with the direction on the right in both, the real part cancels and the mass term vanishes.

The Lagrangian is a one-form plus a potential, so the system is first order and constrained: four momenta vanish, their four equations are the primary constraints, and one of their brackets is $2\hbar c\,r\cosh\theta_{\mathrm{rpd}}$, so they are second class. The phase equation conserves $r^{2}\cosh\theta_{\mathrm{rpd}}$ and agrees with the parent's flow. The scale and rapidity equations together fix the phase rate at $k_m(\cosh\theta_{\mathrm{rpd}}\mathcal V-\sinh\theta_{\mathrm{rpd}}\partial_{\theta_{\mathrm{rpd}}}\mathcal V)$, which is $k_m\mathcal V$ at rest. Closing the system needs the Dirac bracket and is left open.

The four brackets remain the natural form of the equation, and the parameter equations are the Jacobian-transformed version of them. No multipliers are needed for the unit conditions, because the word imposes them identically.

**What the revision of this article rests on.** The three vanishing momenta and the spin's closed form are identities about the word, derived from the kinetic term's closed form; they do not rest on numerical checks. What rests on a computation rather than on a derivation is the second-class statement's completeness — one bracket is computed, not all of them — and what remains open is the closure and the rest frame.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $*,\ \natural$ | Hermitian and quaternion conjugation; $\Pi_\pm^{*}=\Pi_\pm$, $\Pi_\pm^{\natural}=\Pi_\mp$ |
| $\mathrm{Sc},\ \mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part; trace |
| $\tilde\nabla_\Phi,\ (\tilde\nabla_\Phi)^{\natural}$ | Gradient and its quaternion conjugate |
| $r'_t=ct'$ | Material time; the article uses $t'$ |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word |
| $r>0$, $\rho=r^{2}$ | Scale and density |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Phase; conjugate momentum $\hbar c\,r^{2}\cosh\theta_{\mathrm{rpd}}$ |
| $\theta_{\mathrm{rpd}}\ge0$, $\vec u_{\mathrm b}$ | Rapidity and boost axis; momenta zero identically |
| $\theta_{\mathrm{axr}}\in[0,2\pi)$, $\vec u_{\mathrm r}$ | Rotor angle and axis; three momenta, non-zero away from rest |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | Lorentz factor of the frame |
| $\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | Frame idempotents; the parts are $\tilde\Xi\Pi_\pm$ |
| $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$ | Rotor's body angular velocity |
| $\hat n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ | Boost axis carried into the body frame |
| $\vec p_{\mathrm{spin}}=-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$ | Spin momentum; contracts with $\vec\omega_{\mathrm r}$ |
| $A=A_x\,\mathrm{d}q^{x}$, $\Omega=\mathrm{d}A$ | Momentum one-form and its exterior derivative |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction, $\hat s^{2}=-e_t$ |
| $\mathcal{V}$ | Potential factor, the mass term divided by $-\hbar ck_mr^{2}$ |
| $k_m=mc/\hbar$ | Mass wave number |
| $\vec v$ | The fixed unit direction the mass term needs |

## Further Reading

- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), for the word, the four brackets, the mass relation $\tilde\Xi_0^{L}=-\mathcal B_\Psi\tilde\Xi_0^{R}$, and the current.
- [The Variational Principle and the Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-dirac-equation-in-biquaternionic-form.html), the companion, for the action that is substituted here, and for the proof that the split into parts is forced.
- [The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the same substitution in the second-order case, where the Lagrangian comes out in closed form.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its bijection.
- [The Meaning of N-Regularity and Degeneracy](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for $N$, the units and the cone; the parts $\tilde\Xi\Pi_\pm$ lie on the cone, which is why the word is a word for the sum.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, §8, for the tensor formulation, its three Lagrange multipliers, and the velocity and spin-transport equations this article's constraint structure reproduces.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), §9, for the spin fluid and the non-uniqueness of its transport equation.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for primary and secondary constraints, second-class brackets, and the closure this article leaves open.
- Luca Fabbri, *Dirac Theory in Hydrodynamic Form* (2023), for the several inequivalent fluid systems the same equation admits.
