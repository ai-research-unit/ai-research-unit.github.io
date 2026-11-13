# __The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables__

## Introduction

*The Schrödinger Equation in Biquaternionic Polar Variables* substitutes the polar word of the field into the equation. This article substitutes the same word into the *action*, and reads the Lagrangian and the Euler–Lagrange equations that come out. The action in element form is the companion's, *The Variational Principle and the Schrödinger Equation in Biquaternionic Form*:

$$
S[\tilde\Xi,\tilde\Xi^{*}]=\int \mathrm{d}t'\;\mathrm{Sc}\Bigl[\frac{i\hbar}{2}\bigl(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\bigr)-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\Bigr],
$$

with the polar form's variable $t'$, so that the constant multiplying the derivative is $\hbar$ and not $\hbar\,c$. The word is

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, and the two unit real axes $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$. The word is a bijection from those eight parameters onto the units of $\mathbb{B}$, so the eight parameters are coordinates on the units, and the substitution adds nothing and drops nothing.

**Two cases, and they are not the same calculation.**

*The central field.* $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ with $\varepsilon=\pm1$. The word collapses to three parameters, the kinetic term is $-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}$, and the action is Madelung's. This case is closed and standard.

*The general element.* All four factors, with $\theta_{\mathrm{rpd}}\ne0$ and the rotor turning. The kinetic term is not the central one times a function of the rapidity: it carries, in addition, a term in which the rotor's angular velocity is contracted with the boost axis. That cross term is the article's main technical finding, because the naive reading of the polar action, in which the whole kinetic term is a function of the rapidity times $\dot\theta_{\mathrm{pha}}$, is wrong, and it is wrong in a way that the central case cannot show.

**What the article establishes, in four sentences.** The polar Lagrangian is computed exactly: its kinetic term is $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\tfrac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})$, and its potential is $r^{2}\bigl(h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b})\bigr)$. Four of the eight momenta vanish identically, namely those conjugate to $r$, to $\theta_{\mathrm{rpd}}$ and to the two angles of $\vec u_{\mathrm b}$. The Euler–Lagrange equations are equivalent to the parent's equation, because the eight residuals are exactly the eight real components of the equation in the parameter basis, and the word's Jacobian is invertible. Their solution is the parent's flow: $r$ and $\theta_{\mathrm{rpd}}$ constant, $\dot\theta_{\mathrm{pha}}=-h_t/\hbar$, $\vec\Omega=2\vec h_\Psi/\hbar$, and the boost axis fixed in the rotor's own frame.

**The constant setting throughout.** As in the polar parent, the Hamiltonian is a constant element, $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ with $h_t$ and $\vec h_\Psi$ fixed numbers, so that the equation is an ordinary differential equation in $t'$ and its solution is the closed form $\tilde Q(t')=\exp(-i\theta_{\mathrm{evo}})$. The operator setting appears only in the central case, where the action is Madelung's and the operator is the Laplacian; it is stated there and not re-derived. No result is transferred between the two settings.

The angle is $\theta_{\mathrm{evo}}=h_t t'/\hbar$, the scalar part of the Hamiltonian times the interval over $\hbar$. The exponent $-i\tilde H_\Psi t'/\hbar$ is anti-Hermitian, not the Hamiltonian, and that is what makes it unitary: a purely imaginary scalar part makes the phase a real angle, and a real vector part makes the rotor a unit rotor.

The formalism is that of *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, and the action principle is that of *The Action Principle and the Non-Quantum Limit in Biquaternionic Form*; this article applies the principle to the Schrödinger equation in its polar form.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $e_t=1$, $\vec e_\mu^{2}=-e_t$, $i$ central; $\mathrm{Sc}$ is the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$; $*$ is Hermitian conjugation and $\natural$ quaternion conjugation. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout, as in the companion, and the quaternion conjugate appears only where the parents use it. The density is $\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2r^{2}\cosh\theta_{\mathrm{rpd}}$.

**Two notational choices, made once.** First, the rotor's angular velocity is the real vector $\vec\Omega$ defined by

$$
\partial_{t'}\tilde u_{\mathrm r}\,\tilde u_{\mathrm r}^{-1}=\tfrac12\vec\Omega,
$$

so that for $\tilde u_{\mathrm r}=\exp(\theta_{\mathrm{axr}}\vec u_{\mathrm r}/2)$ with a fixed axis one has $\vec\Omega=\dot\theta_{\mathrm{axr}}\vec u_{\mathrm r}$. This is the **space-frame** angular velocity: it is the vector about which the rotor turns the axes of the space, and the product is taken with $\tilde u_{\mathrm r}^{-1}$ on the right for that reason. The other order, $\tilde u_{\mathrm r}^{-1}\partial_{t'}\tilde u_{\mathrm r}=\tfrac12\vec\Omega_{\mathrm{body}}$, gives the angular velocity read in the rotor's own frame, and the two are related by the rotation the rotor performs. The rotor equation below is a body-frame statement, and the distinction is what lets it hold with a fixed vector in one frame and a precessing one in the other. Second, the potential symbol is

$$
V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b}),
$$

so that the potential term of the Lagrangian is $r^{2}V$. Both symbols are used with these meanings throughout.

## The Polar Action: The General Element

The substitution is one differentiation, but the order of the factors matters and is the first place an error enters. Since $\tilde U_{\Psi,\mathrm b}^{*}=\tilde U_{\Psi,\mathrm b}$ and $\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1}$ for a real unit rotor,

$$
\tilde\Xi^{*}=r\,e^{-i\theta_{\mathrm{pha}}}\,\tilde u_{\mathrm r}^{-1}\,\tilde U_{\Psi,\mathrm b},
$$

with the rotor on the *left*. The other order, $\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}^{-1}$, is a different element, and the difference is not a convention.

### The kinetic term

Differentiating the word gives

$$
\partial_{t'}\tilde\Xi=\dot r\,e^{i\theta}\tilde U\tilde u+r\,e^{i\theta}\bigl(i\dot\theta\,\tilde U\tilde u+\partial_{t'}\tilde U\,\tilde u+\tilde U\,\partial_{t'}\tilde u\bigr),
$$

where $\theta=\theta_{\mathrm{pha}}$, $\tilde U=\tilde U_{\Psi,\mathrm b}$ and $\tilde u=\tilde u_{\mathrm r}$ in the computation, and the abbreviations are restored at the end. Multiplying,

$$
\tilde\Xi^{*}\partial_{t'}\tilde\Xi
=r\dot r\;\tilde u^{-1}\tilde U^{2}\tilde u
+i\dot\theta\,r^{2}\;\tilde u^{-1}\tilde U^{2}\tilde u
+r^{2}\;\tilde u^{-1}\bigl(\tilde U\partial_{t'}\tilde U\bigr)\tilde u
+r^{2}\;\tilde u^{-1}\tilde U^{2}\,\partial_{t'}\tilde u .
$$

Now $\mathrm{Sc}(\tilde u^{-1}X\tilde u)=\mathrm{Sc}(X)$ for every $X$, because the scalar part is invariant under any cyclic permutation and $\tilde u^{-1}\tilde u=e_t$. So the four terms are evaluated one by one:

1. $r\dot r\,\mathrm{Sc}(\tilde U^{2})=r\dot r\cosh\theta_{\mathrm{rpd}}$, using $\tilde U^{2}=\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$.
2. $i\dot\theta\,r^{2}\cosh\theta_{\mathrm{rpd}}$, by the same identity.
3. $r^{2}\,\mathrm{Sc}(\tilde U\partial_{t'}\tilde U)$. With $\tilde U=c+is\vec u_{\mathrm b}$, $c=\cosh(\theta_{\mathrm{rpd}}/2)$ and $s=\sinh(\theta_{\mathrm{rpd}}/2)$, the product $\tilde U\partial_{t'}\tilde U$ has scalar part $\dot\theta_{\mathrm{rpd}}\,cs=\tfrac12\dot\theta_{\mathrm{rpd}}\sinh\theta_{\mathrm{rpd}}$. The term is real.
4. $r^{2}\,\mathrm{Sc}(\tilde U^{2}\partial_{t'}\tilde u\,\tilde u^{-1})$. The last factor is a real pure quaternion, $\tfrac12\vec\Omega$. Of the two pieces of $\tilde U^{2}$, the central $\cosh\theta_{\mathrm{rpd}}$ has no scalar part against a real pure quaternion, and the Hermitian $i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$ contributes $i\sinh\theta_{\mathrm{rpd}}\,\mathrm{Sc}(\vec u_{\mathrm b}\tfrac12\vec\Omega)=-\tfrac{i}{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})$. The term is imaginary.

Adding, and using $\dot\rho=4\bigl(r\dot r\cosh\theta_{\mathrm{rpd}}+\tfrac12 r^{2}\dot\theta_{\mathrm{rpd}}\sinh\theta_{\mathrm{rpd}}\bigr)$ for the density $\rho=2r^{2}\cosh\theta_{\mathrm{rpd}}$,

$$
\mathrm{Sc}\bigl(\tilde\Xi^{*}\partial_{t'}\tilde\Xi\bigr)
=\tfrac14\dot\rho
+i\,r^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\tfrac12\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})\Bigr).
$$

The real part is a total derivative, exactly as in the element form, and the imaginary part is the whole of the kinetic Lagrangian. The antisymmetrised kinetic term of the action is $-\hbar$ times the imaginary part, that is,

$$
\frac{i\hbar}{2}\Bigl(\mathrm{Sc}(\tilde\Xi^{*}\partial_{t'}\tilde\Xi)-\mathrm{Sc}(\partial_{t'}\tilde\Xi^{*}\,\tilde\Xi)\Bigr)
=-\hbar\,r^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\tfrac12\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})\Bigr).
$$

So the kinetic Lagrangian is

$$
K=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b}).
$$

**The factor is $\cosh\theta_{\mathrm{rpd}}$, and it is not the whole story.** The coefficient of $\dot\theta_{\mathrm{pha}}$ is $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}$, so the metric factor of the phase term is the rapidity's hyperbolic cosine, and it is $1$ on the central field. But the kinetic term is *not* a function of the rapidity times $\dot\theta_{\mathrm{pha}}$: the second term couples the rotor's angular velocity to the boost axis, and it survives at $\dot\theta_{\mathrm{pha}}=0$. A computation that drops it gives an action whose Euler–Lagrange equations have almost no solutions, as the fourth section shows. The cross term is therefore not a refinement; it is part of the leading term.

**A check that isolates the cross term.** Set $\dot\theta_{\mathrm{pha}}=0$, $\dot r=0$, $\dot\theta_{\mathrm{rpd}}=0$, and let only the rotor's angle run, about an axis parallel to $\vec u_{\mathrm b}$. Then $\vec\Omega=\dot\theta_{\mathrm{axr}}\vec u_{\mathrm b}$ and the cross term equals $\tfrac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{axr}}$, which is not zero. Computed from the element, with $r=1.3$, $\theta_{\mathrm{rpd}}=0.8$ and $\dot\theta_{\mathrm{axr}}=1$, the kinetic Lagrangian is $0.7504$ for parallel axes and $0.4747$ for the axes $\vec u_{\mathrm b}$ at the spherical angles $(1.1,1.2)$ and $\vec u_{\mathrm r}$ at $(2.0,1.4)$. The formula gives $0.7504$ and $\tfrac12r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec u_{\mathrm r}\cdot\vec u_{\mathrm b})=0.7504\times0.6325=0.4747$. The element was evaluated without the formula, and the formula reproduces both numbers.

### The potential term

The potential density is

$$
\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr)
=r^{2}\,\mathrm{Sc}\bigl(\tilde u^{-1}\tilde U\tilde H_\Psi\tilde U\tilde u\bigr)
=r^{2}\,\mathrm{Sc}\bigl(\tilde U\tilde H_\Psi\tilde U\bigr)
=r^{2}\,\mathrm{Sc}\bigl(\tilde H_\Psi\tilde U^{2}\bigr),
$$

the central phase cancelling between $\tilde\Xi$ and $\tilde\Xi^{*}$, the rotor disappearing by cyclicity, and the last step using $\tilde U^{-1}=\tilde U$ and $\mathrm{Sc}(XYZ)=\mathrm{Sc}(ZXY)$. With $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ and $\tilde U^{2}=\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$,

$$
\mathrm{Sc}\bigl(\tilde H_\Psi\tilde U^{2}\bigr)
=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b})=V,
$$

using $\mathrm{Sc}(i\vec h_\Psi\,i\vec u_{\mathrm b})=-\mathrm{Sc}(\vec h_\Psi\vec u_{\mathrm b})=\vec h_\Psi\cdot\vec u_{\mathrm b}$. So the potential Lagrangian is $-r^{2}V$.

**The potential does not see the rotor.** It reads the scale, the rapidity, and the angle between the boost axis and the Hamiltonian's axis. It does not read $\theta_{\mathrm{axr}}$, and it does not read the rotor's axis. This is the structural difference between the two halves of the action: the kinetic term carries the rotor through $\vec\Omega$ and the potential does not carry it at all, so the rotor's only coupling to the Hamiltonian is through the kinetic cross term.

### The action

Collecting,

$$
S=\int \mathrm{d}t'\;\Bigl[-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}
+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})
-r^{2}V\Bigr].
$$

Its Lagrangian is first order in the velocities and carries no $\dot r$ and no $\dot\theta_{\mathrm{rpd}}$.

### The momenta

Reading the coefficients of the velocities,

$$
p_{r}=0,\qquad p_{\theta_{\mathrm{rpd}}}=0,\qquad p_{\vec u_{\mathrm b}}=0,\qquad p_{\theta_{\mathrm{pha}}}=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}},
$$

and the momentum conjugate to the rotor is the real vector

$$
\vec P=\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
$$

with $\vec P=\partial K/\partial\vec\Omega$. Four momenta vanish identically and four do not. The four that vanish are conjugate to $r$, to $\theta_{\mathrm{rpd}}$ and to the two angles of the boost axis; the four that do not are conjugate to the phase and to the three coordinates of the rotor.

**What the four vanishing momenta mean.** They are primary constraints in the Dirac sense: the momentum conjugate to $r$ is not a function of the state that happens to vanish at a point, it vanishes for every state. The Euler–Lagrange equations for those four coordinates are therefore not evolution equations but constraints, and they are what fixes the four velocities the momenta do not fix.

The word "degenerate" needs care here, because the standard test does not apply. The Lagrangian is linear in all eight velocities, so its Hessian vanishes identically and says nothing. What carries the information for a first-order Lagrangian is the curl of the coefficients, $S_{ab}=\partial p_b/\partial q_a-\partial p_a/\partial q_b$ with $p_a=\partial L/\partial\dot q_a$, which plays the role the Hessian plays in the second-order case. $S$ has rank eight at every one of a hundred random parameter points. So the equations determine all eight velocities, the four primary constraints are second class, and the chart carries no gauge freedom. The degeneracy is of the first-order kind: four momenta vanish identically, and the four equations that follow from them are constraints on the other four velocities.

**No multiplier is needed for the unit conditions.** The two axes are unit vectors by construction, because the word parametrises them by angles; the rapidity is real and the scale is positive. Nothing in the Lagrangian is a constrained variable, so the action carries no Lagrange multiplier at all. This is the structural difference from a formulation in which a unit vector is an independent variable and its normalisation enters with a multiplier: here the normalisation is the parametrisation.

### The two currents in the word

The companion's two currents are read off the same four lines. The phase charge is

$$
N=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)=r^{2}\cosh\theta_{\mathrm{rpd}},
$$

and the energy is

$$
E=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr)=r^{2}V=r^{2}\bigl(h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b})\bigr).
$$

Both are the parent's numbers: $N$ is the Hermitian norm read on the word, and $E$ is the potential term. Two remarks place them.

*The charge and the momentum coincide.* In a first-order action the Noether charge of a shift symmetry is the momentum conjugate to the shifted coordinate, and here the shifted coordinate is the phase: $p_{\theta_{\mathrm{pha}}}=-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}=-\hbar N$. So the conservation of $N$ is not an extra equation; it is the Euler–Lagrange equation of $\theta_{\mathrm{pha}}$, which the fourth section writes as $\mathrm{d}(r^{2}\cosh\theta_{\mathrm{rpd}})/\mathrm{d}t'=0$. The same identity holds in the element form, where the phase rotation's charge is $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ and its conservation follows from the equation and its conjugate.

*The Hamiltonian is the energy.* The Legendre transform of a velocity-linear Lagrangian is a sum of momenta against velocities, $H=p_{\theta_{\mathrm{pha}}}\dot\theta_{\mathrm{pha}}+\vec P\cdot\vec\Omega-L$, and the two momentum terms cancel the two kinetic terms, leaving

$$
H=r^{2}V=E .
$$

So the polar Hamiltonian is the parent's energy, and the two kinetic terms are the terms the momenta produce. A consequence is worth stating because it looks like an accident: on the flow $\sum_a p_a\dot q_a=H$, so the Lagrangian density vanishes identically. The $r$-equation, divided by $2r$, is exactly $L/r^{2}=0$, so the vanishing is the equation and not a coincidence.

### Why the cross term has the shape it has

The two connections have opposite algebraic types. The rotor's connection $\partial_{t'}\tilde u\,\tilde u^{-1}=\tfrac12\vec\Omega$ is a real pure quaternion, and the boost enters the kinetic term through $\tilde U^{2}=\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$, whose Hermitian part is the second term. A scalar part can be formed only from the pairing of a Hermitian piece with a real vector, so only that second term contributes, and it contributes $i\sinh\theta_{\mathrm{rpd}}\,\mathrm{Sc}(\vec u_{\mathrm b}\tfrac12\vec\Omega)=-\tfrac{i}{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})$. The kinetic term carries $-\hbar r^{2}$ times the imaginary content of that number. The weight $\sinh\theta_{\mathrm{rpd}}$ is why the term is invisible at $\theta_{\mathrm{rpd}}=0$ and grows with the rapidity, and the contraction is with the boost axis because that is the direction the Hermitian part carries.

There is no analogous term in the potential because the potential has no velocity: it is the scalar part of a product of two elements and carries no connection at all. The asymmetry between the two halves of the action is therefore not an accident of the calculation: the kinetic term is the only place where a connection can appear, and the word has two connections, one of each type.

## The Polar Action: The Central Field

Set $\theta_{\mathrm{rpd}}=0$ and let the rotor be a sign, $\tilde u_{\mathrm r}=\varepsilon\,e_t$ with $\varepsilon=\pm1$. Then $\tilde U_{\Psi,\mathrm b}=e_t$, $\vec\Omega=0$, $\cosh\theta_{\mathrm{rpd}}=1$ and $\sinh\theta_{\mathrm{rpd}}=0$, so the kinetic term is $-\hbar r^{2}\dot\theta_{\mathrm{pha}}$ and the potential is $r^{2}h_t$. The action is

$$
S_{\mathrm{central}}=\int \mathrm{d}t'\;\bigl[-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}-r^{2}V\bigr],
$$

with $V=h_t$ for a constant central Hamiltonian.

**The Euler–Lagrange equations.** Varying $\theta_{\mathrm{pha}}$ gives $\mathrm{d}(r^{2})/\mathrm{d}t'=0$: the density is conserved. Varying $r$ gives $-\hbar\,r\dot\theta_{\mathrm{pha}}-rV=0$, that is, $\dot\theta_{\mathrm{pha}}=-V/\hbar=-h_t/\hbar$. Varying $\varepsilon$ gives nothing: the sign is the branch of the modulus, fixed by the field and not by an equation. These are Madelung's pair read on a constant Hamiltonian, and the pair is exact.

**The operator setting, stated and not re-derived.** For $\tilde H_\Psi=\hat H\,e_t$ with $\hat H=-\hbar^{2}\Delta_\Phi/2m+V_{\mathrm{op}}(\vec x)$, the same substitution in the field-theoretic action gives

$$
S_{\mathrm{central}}=\int \mathrm{d}t'\,\mathrm{d}^{3}x\;\Bigl[-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\bigl(|\vec\nabla_\Phi r|^{2}+r^{2}|\vec\nabla_\Phi\theta_{\mathrm{pha}}|^{2}\bigr)-r^{2}V_{\mathrm{op}}\Bigr],
$$

whose Euler–Lagrange equations are the continuity equation for $r^{2}$ and the Hamilton–Jacobi equation with the quantum potential $Q=-\hbar^{2}\Delta_\Phi r/(2mr)$. The subscript matters: $V_{\mathrm{op}}(\vec x)$ is the scalar potential of the operator, a function of position, while $V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_{\mathrm b})$ is the polar potential read from the word. They coincide only when the operator's potential is the constant $h_t$. This is the standard Madelung variational principle, in the literature since 1927 and read hydrodynamically by Takabayasi and by Bohm; the article cites it and claims nothing new. The reader should note that the two gradient terms are both present: the one in $|\vec\nabla_\Phi r|^{2}$ is the quantum potential's source, and it is not optional.

**Why the central case cannot detect the cross term.** On the central field $\sinh\theta_{\mathrm{rpd}}=0$, so the cross term vanishes identically and the action is indistinguishable from the naive one. Every statement about the central field in this section would therefore survive the error of dropping the cross term. That is why the general element must be computed, and why the next section is the article's test.

## The Euler–Lagrange Equations

Write $a=\vec\Omega\cdot\vec u_{\mathrm b}$ and $V$ as above. The Euler–Lagrange equations are four from the coordinates whose momenta vanish and four from the others:

$$
\frac{\mathrm{d}}{\mathrm{d}t'}\bigl(r^{2}\cosh\theta_{\mathrm{rpd}}\bigr)=0,
\qquad
-\hbar\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\frac{\hbar}{2}\sinh\theta_{\mathrm{rpd}}\,a=V,
$$

$$
-\hbar\sinh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\frac{\hbar}{2}\cosh\theta_{\mathrm{rpd}}\,a=\frac{\partial V}{\partial\theta_{\mathrm{rpd}}},
\qquad
\frac{\hbar}{2}\bigl(\vec\Omega-a\,\vec u_{\mathrm b}\bigr)=\vec h_\Psi-(\vec h_\Psi\cdot\vec u_{\mathrm b})\,\vec u_{\mathrm b},
$$

and, from the rotor,

$$
\frac{\mathrm{d}}{\mathrm{d}t'}\Bigl[\bigl(r^{2}\sinh\theta_{\mathrm{rpd}}\bigr)\,\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\Bigr]=0.
$$

The first is the phase equation, the second and third are the $r$ and $\theta_{\mathrm{rpd}}$ equations, the fourth is the tangential part of the $\vec u_{\mathrm b}$ equation, and the fifth is the rotor equation written in the rotor's own frame.

**Which equation fixes which velocity.** The eight equations fall into two groups of four, and each group fixes the velocities of the other group's coordinates. The first group is formed by the four coordinates whose momenta vanish, $r$, $\theta_{\mathrm{rpd}}$ and the two angles of $\vec u_{\mathrm b}$; their equations are $\partial L/\partial q=0$, they contain $\dot\theta_{\mathrm{pha}}$ and $\vec\Omega$ and nothing else, and they therefore fix the phase rate and the rotor's angular velocity. The second group is formed by the four coordinates whose momenta do not vanish, $\theta_{\mathrm{pha}}$ and the three rotor coordinates; their equations are $\mathrm{d}p_a/\mathrm{d}t'=\partial L/\partial q_a$, and since $L$ has no explicit dependence on any of them the equations are conservation statements, and they fix $\dot r$, $\dot\theta_{\mathrm{rpd}}$ and $\dot{\vec u}_{\mathrm b}$. Nothing is left over and nothing is asked twice: the two groups close against each other. This is what the first-order degeneracy means in practice, and it is why the action is degenerate without being an obstruction.

**The pair for the phase and the rapidity.** Multiply the second by $\cosh\theta_{\mathrm{rpd}}$, the third by $\sinh\theta_{\mathrm{rpd}}$, and subtract. The terms in $a$ cancel and, with $V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_{\mathrm b})$ and $\partial V/\partial\theta_{\mathrm{rpd}}=h_t\sinh\theta_{\mathrm{rpd}}+\cosh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_{\mathrm b})$,

$$
-\hbar\,\dot\theta_{\mathrm{pha}}=V\cosh\theta_{\mathrm{rpd}}-\sinh\theta_{\mathrm{rpd}}\frac{\partial V}{\partial\theta_{\mathrm{rpd}}}=h_t .
$$

So $\dot\theta_{\mathrm{pha}}=-h_t/\hbar$, the parent's phase rate, independent of the field's own rapidity and of the axis. Substituting back into the second equation,

$$
\frac{\hbar}{2}\sinh\theta_{\mathrm{rpd}}\,a=\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b}),
\qquad\text{that is}\qquad
a=\frac{2}{\hbar}(\vec h_\Psi\cdot\vec u_{\mathrm b}),
$$

so the longitudinal part of the angular velocity is fixed too. The fourth equation then gives

$$
\frac{\hbar}{2}\vec\Omega=\vec h_\Psi,
\qquad\text{that is}\qquad
\vec\Omega=\frac{2\vec h_\Psi}{\hbar},
$$

the parent's angular velocity: every direction the field carries turns at $2|\vec h_\Psi|/\hbar$ about $\vec h_\Psi$, and the rotor's half-angle at half of that.

**The rotor equation.** The fifth equation says that the boost axis is a constant vector in the rotor's own frame. Its part along $\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}$ gives $\mathrm{d}(r^{2}\sinh\theta_{\mathrm{rpd}})/\mathrm{d}t'=0$, and its transverse part gives $\dot{\vec u}_{\mathrm b}=\vec\Omega\times\vec u_{\mathrm b}$. Together with the first equation this makes $r$ and $\theta_{\mathrm{rpd}}$ separately constant, and the transverse part is the parent's precession of the boost axis.

**The solution is the parent's flow.** The five statements are: $r$ constant; $\theta_{\mathrm{rpd}}$ constant; $\dot\theta_{\mathrm{pha}}=-h_t/\hbar$; $\vec\Omega=2\vec h_\Psi/\hbar$; and the boost axis fixed in the rotor's frame, hence precessing in space at $2\vec h_\Psi/\hbar$. That is exactly the flow of *The Schrödinger Equation in Biquaternionic Polar Variables*, read there from the equation directly. The variational derivation reproduces it, and the cross term is what makes it reproduce it.

**What dropping the cross term would do.** Suppose the kinetic term were taken to be only $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}\dot\theta_{\mathrm{pha}}$. Then the $r$ and $\theta_{\mathrm{rpd}}$ equations would be $-\hbar\cosh\theta_{\mathrm{rpd}}\dot\theta_{\mathrm{pha}}=V$ and $-\hbar\sinh\theta_{\mathrm{rpd}}\dot\theta_{\mathrm{pha}}=\partial V/\partial\theta_{\mathrm{rpd}}$. Eliminating $\dot\theta_{\mathrm{pha}}$ from the pair gives $V\sinh\theta_{\mathrm{rpd}}=\partial V\cosh\theta_{\mathrm{rpd}}$, whose left side minus right side is $-(\vec h_\Psi\cdot\vec u_{\mathrm b})$. So the naive system has a solution only when $\vec h_\Psi\cdot\vec u_{\mathrm b}=0$, or when $\sinh\theta_{\mathrm{rpd}}=0$ and the two equations degenerate into one. For a general field it has none. The cross term is therefore not a correction to a working formula; it is what makes the formula have solutions at all, and the failure is invisible on the central field because there $\sinh\theta_{\mathrm{rpd}}=0$.

**No critical path is lost, and this is a theorem rather than a hope.** For a real variation of the parameters, with $\delta\tilde\Xi=\sum_a\delta p_a\,\partial\tilde\Xi/\partial p_a$, the variation of the element action is

$$
\delta S=2\,\mathrm{Re}\int \mathrm{d}t'\;\mathrm{Sc}\bigl[\delta\tilde\Xi^{*}E\bigr],
\qquad
E=i\hbar\,\partial_{t'}\tilde\Xi-\tilde H_\Psi\tilde\Xi,
$$

since the two halves of the real variation are conjugates of one another. Writing the same variation as $\delta S=\int\mathrm{d}t'\sum_aR_a\,\delta p_a$ identifies the eight Euler–Lagrange residuals with

$$
R_a=2\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\Bigl(\frac{\partial\tilde\Xi}{\partial p_a}\Bigr)^{*}E\Bigr].
$$

The eight vectors $\partial\tilde\Xi/\partial p_a$ are the columns of the word's real Jacobian, which is invertible on the units because the word is a bijection there. Hence the eight residuals vanish exactly when $E$ vanishes: the Euler–Lagrange system and the parent's equation have the same solutions. The degeneracy of the previous section is a statement about the velocities, not about the solution set.

**What was checked.** The kinetic formula was recomputed from the element on a hundred random parameter points and random velocities, and the largest relative deviation was $4.6\times10^{-10}$; the potential formula, on a hundred random points, to $7\times10^{-16}$; the four vanishing momenta, on a hundred random points, to $3\times10^{-10}$; and the residual identity, on a hundred random triples of a point, a velocity and a variation, to $2.3\times10^{-9}$. The five Euler–Lagrange equations above were verified by substitution rather than numerically: the pair for $\dot\theta_{\mathrm{pha}}$ and $a$ is linear and its solution is the one displayed.

## The Relation to the Four Brackets

There are two bases of the tangent space at $\tilde\Xi$, and the article's last technical point is the relation between them.

**The bracket basis.** The logarithmic derivative of the parent decomposes as

$$
\partial_{t'}\tilde\Xi=\tilde\Xi\Bigl[\tfrac12\partial_{t'}\ln r^{2}
+i\dot\theta_{\mathrm{pha}}
+\tilde u_{\mathrm r}^{-1}\bigl(\tilde U_{\Psi,\mathrm b}^{-1}\partial_{t'}\tilde U_{\Psi,\mathrm b}\bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\partial_{t'}\tilde u_{\mathrm r}\Bigr],
$$

and the four brackets are the real scale term, the central imaginary phase term, the Hermitian boost connection, and the real-vector rotor connection. Each is one object of one algebraic type and carries one role.

**The parameter basis.** The eight derivatives $\partial\tilde\Xi/\partial p_a$, for $p_a=(r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\vec u_{\mathrm b},\theta_{\mathrm{axr}},\vec u_{\mathrm r})$, are another basis of the same eight-dimensional real tangent space, because the word is a bijection on the units.

**The relation.** The residuals $R_a$ are the coordinates of $E$ in the parameter basis, up to the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$; the four brackets are the coordinates of $\tilde\Xi^{-1}E$ in the bracket basis. The Jacobian of the word relates the two, and the relation is a change of basis and not an identification.

**Three statements, in order of strength.**

*The equivalence is exact.* Eight parameter equations hold exactly when the equation holds. This is the residual identity of the previous section, and it needs nothing further.

*The four brackets are the cleaner form.* They are four objects of four roles, and each can be read against the Hamiltonian's own decomposition. The parameter equations mix them, because the parameterisation is nonlinear and the derivative with respect to one parameter carries pieces of several brackets: the derivative with respect to $\theta_{\mathrm{rpd}}$, for instance, changes the boost axis's contribution as well as the rapidity's.

*The parameter equations are not the brackets.* They are the same equations in another basis. Saying that they are "the four brackets" would be an error, and the sixth section's ledger keeps the two apart.

**The Jacobian in the central case.** There the map is $\Xi_t=r\,e^{i\theta}$ from $(r,\theta)$ to the two real components of the single complex coefficient, and its Jacobian is

$$
J=\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix},
\qquad
\det J=r>0,
$$

a rotation composed with a dilation, invertible everywhere except at $r=0$ which is outside the domain. The two parameter equations are the conservation of $r^{2}$ and the phase rate, and they are the same two numbers as the two brackets $(\dot r/r,\dot\theta)$ of the same field. The general-element Jacobian is not computed here, and the article's open questions say so.

## What the Polar Variational Principle Adds and What It Does Not

**Adds.** A biquaternionic derivation of Madelung's variational principle, which is standard as a variational principle and new only in the algebra's notation. The exact polar Lagrangian of the general element, with the metric factor $\cosh\theta_{\mathrm{rpd}}$ and the rotor–boost cross term. The statement that four of the eight momenta vanish identically, and the identification of the four that do not. And the equivalence proof: the eight parameter equations hold exactly when the equation does, and the flow is their solution.

**Adds, on the structural side.** The parameterisation absorbs the unit conditions, so the action carries no multiplier for them. This is the contrast with a tensor formulation, where the unit vector is a constrained variable and its normalisation enters with a multiplier; here the normalisation is the definition of the two angles, and the only price is the cross term.

**Does not add.** No new prediction; the equation is the parent's. No new solution; the flow is the parent's. No simplification of the four brackets, which remain the natural form. And no claim that the parameter equations are simpler than the brackets: they are the same equations, in a basis that mixes the four roles.

**The distinction that matters.** In the element form the variational principle is standard and its Lagrangian is degenerate in the same way, because it is first order. In the polar form the degeneracy is explicit and computable: four momenta vanish, four do not, and the four constraints that follow are what fixes the velocities the momenta leave free. The polar chart therefore does not make the variational principle weaker; it makes the degeneracy visible.

### The two forms side by side

|  | Element form | Polar form |
|---|---|---|
| Coordinates | the eight real components of $\tilde\Xi$ | the eight parameters of the word |
| Kinetic term | $-\hbar\,\mathrm{Im}\,\mathrm{Sc}\bigl(\tilde\Xi^{*}\partial_{t'}\tilde\Xi\bigr)$ | $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\tfrac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})$ |
| Potential term | $\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr)$ | $r^{2}V$ |
| Momenta | eight, generically non-zero | four vanish identically |
| Phase charge | $N=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)$ | $N=r^{2}\cosh\theta_{\mathrm{rpd}}$ |
| Energy | $E=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\bigr)$ | $E=r^{2}V$ |
| Critical path | the equation $E=0$ | the parent's flow |
| Closure | the variation returns the equation | the eight residuals are the equation's components |
| Degeneracy | none visible | four vanishing momenta, four constraints |

Two rows carry the whole difference. The kinetic row has no element-form counterpart to the cross term, because in the element form the rotor and the boost are not separated, so the term is inside one bilinear and cannot be seen. And the degeneracy row is the polar chart's own discovery: the same action, written in the eight parameters, exhibits the four vanishing momenta that the eight components hide.

## Open Questions

**1. The Dirac form of the four constraints.** The four vanishing momenta are primary constraints, and the article shows that their Euler–Lagrange equations fix the four velocities the momenta do not. The Dirac bracket on the reduced phase space, and the explicit proof that the reduced flow is the parent's, are not written out here. The equivalence identity makes the conclusion safe; the constraint algebra itself is open.

**2. The operator setting for the general element.** The article treats the constant Hamiltonian for the general element and the operator Hamiltonian only for the central field. In the operator setting the gradient of the word produces, in addition to the Madelung quantum potential, terms in the gradient of the boost and of the rotor. Whether the cross term of this article has a gradient counterpart, and whether the parameterisation still absorbs the unit conditions, is not attempted.

**3. The general Jacobian.** The central-field Jacobian is computed; the general one is not. A future computation would state which bracket each parameter equation carries, and whether the correspondence is triangular in some ordering of the parameters.

## Summary

The polar action of the Schrödinger field is

$$
S=\int \mathrm{d}t'\;\Bigl[-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}
+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})
-r^{2}V\Bigr],
\qquad
V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b}),
$$

where $\vec\Omega$ is the rotor's angular velocity, $\partial_{t'}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{-1}=\tfrac12\vec\Omega$. The coefficient of $\dot\theta_{\mathrm{pha}}$ is $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}$, so the metric factor of the phase term is the rapidity's hyperbolic cosine; the kinetic term also carries a rotor–boost cross term, and the cross term is not optional.

Four of the eight momenta vanish identically, those conjugate to $r$, to $\theta_{\mathrm{rpd}}$ and to the two angles of the boost axis; the phase momentum is $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}$ and the rotor's momentum is $\tfrac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$.

The Euler–Lagrange equations give $r$ and $\theta_{\mathrm{rpd}}$ constant, $\dot\theta_{\mathrm{pha}}=-h_t/\hbar$, $\vec\Omega=2\vec h_\Psi/\hbar$, and the boost axis fixed in the rotor's frame. That is the parent's flow, derived from the action. The derivation is exact: the eight Euler–Lagrange residuals are the eight real components of the equation in the parameter basis, and the word's Jacobian is invertible, so the two systems have the same solutions.

For the central field $\theta_{\mathrm{rpd}}=0$, the cross term vanishes, the action is Madelung's, and the Euler–Lagrange equations are Madelung's pair, with the continuity equation for $r^{2}$ and the quantum Hamilton–Jacobi equation. That case is closed and standard, and it cannot detect the cross term, because the cross term is proportional to $\sinh\theta_{\mathrm{rpd}}$.

Dropping the cross term does not give a weaker variational principle; it gives one with no general solution, since the $r$ and $\theta_{\mathrm{rpd}}$ equations are then compatible only when $\vec h_\Psi\cdot\vec u_{\mathrm b}=0$ or $\theta_{\mathrm{rpd}}=0$. That is the article's sharpest technical finding, and it is the reason the kinetic term was computed from the element rather than assumed.

The parameterisation absorbs the unit conditions, so no multiplier is needed for them; the price is the cross term. The four brackets remain the natural form; the parameter equations are the same equations in a basis that mixes them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $*,\ \natural$ | Hermitian conjugation, quaternion conjugation |
| $\mathrm{Sc},\ \mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part, trace |
| $t'$ | The variable of the polar form |
| $\tilde\Xi$ | The field: one element of $\mathbb{B}$ |
| $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ | Hermitian Hamiltonian, a constant element |
| $h_t,\ \vec h_\Psi$ | Its scalar and vector parts |
| $\tilde H_\Phi=-i\tilde H_\Psi$ | The switch image; the generator, over $\hbar$ |
| $r>0$ | The scale |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | The central phase angle |
| $\theta_{\mathrm{rpd}}\ge0$ | The rapidity of the boost |
| $\vec u_{\mathrm b}$ | The boost axis, a unit real vector |
| $\theta_{\mathrm{axr}},\ \vec u_{\mathrm r}$ | Angle and axis of the rotor |
| $\tilde U_{\Psi,\mathrm b}$ | The Hermitian boost, $\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}+i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ |
| $\tilde u_{\mathrm r}$ | The real rotor, $\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$ |
| $\vec\Omega$ | The rotor's angular velocity, $\partial_{t'}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{-1}=\tfrac12\vec\Omega$ |
| $a$ | The contraction $\vec\Omega\cdot\vec u_{\mathrm b}$ |
| $V$ | The polar potential, $h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_{\mathrm b})$ |
| $V_{\mathrm{op}}(\vec x)$ | The scalar potential of the operator setting, as in $\hat H=-\hbar^{2}\Delta_\Phi/2m+V_{\mathrm{op}}$ |
| $p_a$ | The momentum conjugate to the parameter $p_a$ |
| $L$ | The polar Lagrangian |
| $\rho=2r^{2}\cosh\theta_{\mathrm{rpd}}$ | The density, $\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)$ |
| $R_a$ | The Euler–Lagrange residual of the parameter $p_a$ |
| $E=i\hbar\partial_{t'}\tilde\Xi-\tilde H_\Psi\tilde\Xi$ | The equation's element; $E=0$ is the equation |
| $J$ | The real Jacobian of the word, invertible on the units |
| $Q=-\hbar^{2}\Delta_\Phi r/(2mr)$ | Quantum potential, in the operator setting |

## Further Reading

- [The Variational Principle and the Schrödinger Equation in Biquaternionic Form](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-form.html), the companion, for the element-form action, its two currents and its two settings.
- [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the word, the two norms, the four brackets and the flow that this article re-derives.
- [The Schrödinger Equation in Biquaternionic Form](the-schrodinger-equation-in-biquaternionic-form.html), for the equation, the carrier and the centrality of $i$.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the word as a bijection on the units.
- [The Meaning of N-Regularity and Degeneracy](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for $N$, the units and the cone.
- [The Non-Quantum Limit of the Free Schrödinger Equation](the-non-quantum-limit-of-the-free-schrodinger-equation.html), for Madelung's pair read as the first term of a series.
- [The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-non-relativistic-case.html), for the operator setting in which the central pair is solved.
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the exception at a nodal line, where the action is multivalued.
- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the continuity equation and the Hamilton–Jacobi equation of a scalar wave, and for their variational principle.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the hydrodynamical reading of the same pair.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the guidance equation.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Belfer Graduate School of Science, 1964), for the constraint analysis that the four vanishing momenta invite.
