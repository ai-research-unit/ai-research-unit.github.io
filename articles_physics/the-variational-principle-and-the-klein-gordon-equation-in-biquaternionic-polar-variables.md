# __The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables__

## Introduction

This article substitutes the polar word into the Klein–Gordon action and reads the result. The word is the one of *The Polar Decomposition of an N-Regular Biquaternion*, in the exponential form of *Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion*:

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi)$, and $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ real unit vectors. The word is a bijection from the eight parameters onto the $N$-regular set, so the parameters are coordinates on the units and the substitution loses nothing.

Three results are established, and each is a computation.

**The polar action.** The kinetic term is $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi\,\mathcal{A}_\mu\mathcal{A}^{\mu*})$ with $\mathcal{A}_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$, which is the frame density times the square of the bracket. Written in parameters it is a quadratic form with a metric that depends on the point, and the metric is computed exactly for the four scalar parameters with the two axes held fixed. The rapidity enters it twice: as the factor $\cosh\theta_{\mathrm{rpd}}$ on all four squares, and as the factor $\sinh\theta_{\mathrm{rpd}}$ on two cross terms.

**The Euler–Lagrange equations.** For the central field they are the parent's pair, exactly: the transport equation and the quantum Hamilton–Jacobi equation. For the general element they are the Klein–Gordon equation pulled back to the parameters, and the equivalence is exact because the word is a bijection with a smooth inverse. There is no constraint and no Lagrange multiplier, and §*The General Element* says why the first-order case differs.

**The relation to the four brackets.** The bracket $\mathcal{A}_\mu$ is the natural variable: the Lagrangian is quadratic in it with an algebraic weight, and the eight parameter equations are its Jacobian image. The parameter equations are not a simpler form and are not a different system.

**Scope.** The coefficient is the constant mass wave number $k_m$ throughout, as in the parent's §*The Equation in Polar Variables*, and §*The Potential Term* states the generalisation to a Hermitian coefficient in one line. The operator case, in which the coefficient varies in space and time, is the standard Madelung problem of the parent's non-relativistic limit and is not re-derived here.

The formalism is that of *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, and the action principle is that of *The Action Principle and the Non-Quantum Limit in Biquaternionic Form*; this article applies the principle to the Klein–Gordon equation in its polar form.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $\mathbb{B}_{C}$ is the centre; $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the Hermitian and anti-Hermitian fixed subspaces; $^{*}$ is Hermitian conjugation and $^{\natural}$ quaternion conjugation; $\mathrm{Sc}$ is the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$ throughout, as in the element-form companion: the quaternionic pairing gives $\mathrm{Sc}(A^{\natural}A)=\sum_\mu a_\mu^{2}$ for complex coefficients, which is not real, and it is not used. The d'Alembertian is $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r'^{2}_{t}$ with $r'_t=c\,t'$, the four-position is $\tilde R_\Phi=i r'_t e_t+\vec r$, and $k_m=mc/\hbar$. The action is a functional of the eight parameters over four-dimensional space, and the material time is $r'_t=c\,t'$ throughout, so every temporal derivative below is a derivative in a length. Every symbol is defined where it first appears, and §*Summary of Notation* collects the letters with their domains.

## The Action in Polar Variables

The element-form action of the companion is

$$
S[\tilde\Xi,\tilde\Xi^{*}]=\int\mathrm{d}^{4}x\;\mathrm{Sc}\Big[(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi-\sum_{\eta}(\partial_{r_\eta}\tilde\Xi)^{*}\partial_{r_\eta}\tilde\Xi-k_m^{2}\tilde\Xi^{*}\tilde\Xi\Big].
$$

The substitution is a change of variables in this functional. The subsections below compute the two terms, record where the rapidity sits in each of them, and assemble the action.

### The bracket form of the kinetic term

Every derivative of the word factors through one object. With $\mathcal{A}_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$,

$$
\partial_\mu\tilde\Xi=\tilde\Xi\,\mathcal{A}_\mu,
\qquad
(\partial_\mu\tilde\Xi)^{*}\partial_\mu\tilde\Xi=\mathcal{A}_\mu^{*}\tilde\Xi^{*}\tilde\Xi\,\mathcal{A}_\mu,
\qquad
\mathrm{Sc}\big[(\partial_\mu\tilde\Xi)^{*}\partial_\mu\tilde\Xi\big]=\mathrm{Sc}\big[\tilde\Xi^{*}\tilde\Xi\,\mathcal{A}_\mu\mathcal{A}_\mu^{*}\big],
$$

the last step by $\mathrm{Sc}(XYZ)=\mathrm{Sc}(ZXY)$, which moves the frame density to the front. The identity is exact and it is the reason the polar form is legible: the kinetic Lagrangian is the square of the bracket, weighted by the frame density $\tilde\Xi^{*}\tilde\Xi$.

**The bracket, split into its four types.** Substituting the word,

$$
\mathcal{A}_\mu=\partial_\mu\ln r+i\,\partial_\mu\theta_{\mathrm{pha}}+\tilde u_{\mathrm r}^{-1}\bigl(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}\bigr)\tilde u_{\mathrm r}+\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r},
$$

which is four objects of four algebraic types: a real scalar, a central imaginary, a Hermitian element along the boost axis, and a real vector. With the axes fixed, $\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}=\tfrac{i}{2}\partial_\mu\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$ and $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}=\tfrac12\partial_\mu\theta_{\mathrm{axr}}\,\vec u_{\mathrm r}$, so

$$
\mathcal{A}_\mu=\partial_\mu\ln r+i\,\partial_\mu\theta_{\mathrm{pha}}+\tfrac{i}{2}\partial_\mu\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}'+\tfrac12\partial_\mu\theta_{\mathrm{axr}}\,\vec u_{\mathrm r}
$$

with $\vec u_{\mathrm b}'=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ the boost axis carried into the rotor's frame. The dot product $\vec u_{\mathrm b}'\cdot\vec u_{\mathrm r}=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ is the one invariant the two axes have.

**The frame density.** The factor is fixed by the same word,

$$
\tilde\Xi^{*}\tilde\Xi=r^{2}\tilde U_{\Psi,\mathrm b}^{2}=r^{2}\bigl(\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}'\bigr),
\qquad
\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=r^{2}\cosh\theta_{\mathrm{rpd}},
\qquad
\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2r^{2}\cosh\theta_{\mathrm{rpd}},
$$

the scalar part of the frame density being what multiplies the squares and the Hermitian part what multiplies the cross terms. The factor $\cosh\theta_{\mathrm{rpd}}$ is the density in units of $r^{2}$, and that is the only place the rapidity's magnitude enters the kinematics.

### The parameter form: the metric

Carrying out the product gives the kinetic Lagrangian of one direction,

$$
\boxed{\;
\mathrm{Sc}\big[(\partial\tilde\Xi)^{*}\partial\tilde\Xi\big]
=r^{2}\Bigl\{\cosh\theta_{\mathrm{rpd}}\Bigl[(\partial\ln r)^{2}+(\partial\theta_{\mathrm{pha}})^{2}+\frac{(\partial\theta_{\mathrm{rpd}})^{2}}{4}+\frac{(\partial\theta_{\mathrm{axr}})^{2}}{4}\Bigr]
+\sinh\theta_{\mathrm{rpd}}\Bigl[(\partial\ln r)(\partial\theta_{\mathrm{rpd}})-(\partial\theta_{\mathrm{pha}})(\partial\theta_{\mathrm{axr}})\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}\Bigr]\Bigr\}\;}
$$

for the four scalar parameters with the two axes held fixed, where $\partial$ is any one of the four coordinate derivatives. Four features of it matter.

**Every square carries the same weight.** The four squares are multiplied by the one factor $\cosh\theta_{\mathrm{rpd}}$, which is the density ratio of the display above. The factors of $\tfrac14$ on the two angle rates are the halves of the exponents and not weights; the weight itself is one density for all four, because the frame is a unit and all of its directions are measured alike.

**The cross terms are the sinh ones, and there are two.** The amplitude gradient couples to the rapidity gradient with weight $+\sinh\theta_{\mathrm{rpd}}$, and the phase gradient couples to the rotor's angular rate with weight $-\sinh\theta_{\mathrm{rpd}}(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})$. Both vanish on the central field, and both are as large as the squares at large rapidity. A computation that keeps the cosh and drops the sinh gives an action whose Euler–Lagrange equations are not the parent's.

The count is fixed by the density. The squares multiply the scalar part of $\tilde\Xi^{*}\tilde\Xi$ and the cross terms multiply its Hermitian part $i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}'$, so a cross term survives only for a pair of brackets whose product has a component along $\vec u_{\mathrm b}'$. There are two such pairs: the real scalar with the Hermitian vector, whose product is $\vec u_{\mathrm b}'$ itself, and the central imaginary with the real vector, whose product is $i\vec u_{\mathrm b}'$. Every other pair has no component along the boost axis, and one pair has none at all.

**The mixing has unit determinant.** In the two-dimensional block spanned by $\partial\ln r$ and $\partial\theta_{\mathrm{rpd}}$ the matrix is

$$
\begin{pmatrix}\cosh\theta_{\mathrm{rpd}} & \tfrac12\sinh\theta_{\mathrm{rpd}}\\ \tfrac12\sinh\theta_{\mathrm{rpd}} & \tfrac14\cosh\theta_{\mathrm{rpd}}\end{pmatrix},
\qquad
\det=\tfrac14\bigl(\cosh^{2}\theta_{\mathrm{rpd}}-\sinh^{2}\theta_{\mathrm{rpd}}\bigr)=\tfrac14 ,
$$

so the amplitude and the rapidity mix without changing the volume, and the block is invertible for every rapidity. The identity $\cosh^{2}-\sinh^{2}=1$ appears here as a property of the parameter metric, which is why the Legendre transform of §*The Euler–Lagrange Equations* is regular.

**The metric is the induced one.** Writing $g_{ab}(p)=\mathrm{Sc}\big[(\partial\tilde\Xi/\partial p^{a})^{*}(\partial\tilde\Xi/\partial p^{b})\big]$ for the eight parameters $p^{a}$, the kinetic Lagrangian is $g_{ab}\,\partial_\mu p^{a}\partial^{\mu}p^{b}$ with the metric signs of the action, and $g$ is the pull-back of the flat Hermitian metric of $\mathbb{C}^{4}$ by the word. Since $\mathrm{Sc}(A^{*}A)=\sum_\mu\lvert a_\mu\rvert^{2}$ is a sum of squares, $g$ is positive semi-definite in every direction, and it is positive definite wherever the word's Jacobian has full rank, which is everywhere on the $N$-regular set.

**The check.** Six random parameter sets with random axes, all four angles varying, were compared against the boxed formula: the two agree to a relative $4\times10^{-10}$, which is the truncation of the difference quotient. Each term was also isolated separately: with only the amplitude, only the rapidity, only the phase or only the rotor varying, the value is $r^{2}\cosh\theta_{\mathrm{rpd}}$ times the square of that rate, and the two cross terms appear only when both of their parameters vary.

### Where the rapidity goes

The Schrödinger companion computes a kinetic term that is linear in one velocity, $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\tfrac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})$, and the factor $\cosh\theta_{\mathrm{rpd}}$ appears there multiplying the phase rate alone. Here the same factor multiplies every square, and the sinh multiplies two cross terms instead of one.

The difference is the order of the action. In a first-order action the kinetic term is $\mathrm{Sc}(i\tilde\Xi^{*}\partial\tilde\Xi)$, one bracket and not two, so the only thing the boost can do is weight that one bracket: the cosh is a coefficient of a velocity. In a second-order action the kinetic term is $\mathrm{Sc}((\partial\tilde\Xi)^{*}\partial\tilde\Xi)$, a product of two brackets, so the boost's Hermitian part can multiply either of them and the same cosh becomes a metric entry. The function of the rapidity is the same function and comes from the same place, the frame density $r^{2}\cosh\theta_{\mathrm{rpd}}$; it is the power of the velocity that differs.

### The potential term

The potential term is $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)$ with $\tilde M\in\mathbb{B}_{\Psi}$ Hermitian, and for $\tilde M=k_m^{2}e_t$ it is $k_m^{2}\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=k_m^{2}r^{2}\cosh\theta_{\mathrm{rpd}}$. For a general Hermitian coefficient the rotor drops out and the rapidity does not,

$$
\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)=r^{2}V,
\qquad
V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b}),
\qquad
\tilde M=h_t e_t+i\vec h_\Psi ,
$$

where the rotor cancels by the invariance of $\mathrm{Sc}$ under conjugation and the central phase cancels by cyclicity. The potential is real because $\tilde M$ is Hermitian, and it is a function of the rapidity and of its axis alone: the scale enters as $r^{2}$, the phase does not enter at all, and the rotor does not enter. This is the same $V$ that the Schrödinger companion writes, and it is the same function because in both articles $V$ is $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)/r^{2}$. The check is numerical: four random elements with random rapidity, axes and rotor, and a random Hermitian coefficient, reproduce the display to $10^{-12}$.

**A remark on signs.** The rapidity term in $V$ is a $\cosh$, so a coefficient with a positive $h_t$ raises the potential energy of a boosted configuration without bound. That is the statement that a boost costs energy in a massive theory, and it is the one place in the polar form where the boost's non-compactness is a physical effect rather than a coordinate choice.

### The action, assembled

$$
\boxed{\;
S=\int\mathrm{d}^{4}x\;\Bigl\{g_{ab}(p)\,\partial_{r'_t}p^{a}\partial_{r'_t}p^{b}-\sum_{\eta}g_{ab}(p)\,\partial_{r_\eta}p^{a}\partial_{r_\eta}p^{b}-r^{2}V(p)\Bigr\}\;}
$$

with $p^{a}=(r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}},\vec u_{\mathrm b},\vec u_{\mathrm r})$ and $g$ known on the slice of fixed axes, which is the boxed metric above. The functional is the element-form action in other coordinates: no term was added, no term was dropped, and the only object that changed is the measure of the parameter space.

**The central field is the case of one block.** With $\theta_{\mathrm{rpd}}=0$ and the axes frozen, $g_{rr}=1$, $g_{\theta\theta}=r^{2}$, and all other entries vanish, so

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl[(\partial_{r'_t}r)^{2}-\lvert\nabla r\rvert^{2}+r^{2}\bigl((\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\bigr)-k_m^{2}r^{2}\Bigr],
$$

which is Madelung's relativistic action for the pair $(r,S_{\tilde\Xi})$ with $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$. The signs are the Minkowski ones, so the amplitude equation of the next section carries the d'Alembertian and not the Laplacian.

## The Euler–Lagrange Equations

### The central field: the pair, and nothing else

The two variations of the central action give two equations, and they are the parent's exactly.

**Varying the phase.** $\partial S/\partial\theta_{\mathrm{pha}}=0$ gives, with $\rho_{\mathrm{num}}=r^{2}$,

$$
\partial_{r'_t}\bigl(r^{2}\partial_{r'_t}\theta_{\mathrm{pha}}\bigr)-\nabla\cdot\bigl(r^{2}\nabla\theta_{\mathrm{pha}}\bigr)=0
\qquad\Longleftrightarrow\qquad
\nabla\cdot\bigl(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi}\bigr)-\partial_{r'_t}\bigl(\rho_{\mathrm{num}}\partial_{r'_t}S_{\tilde\Xi}\bigr)=0,
$$

which is the parent's transport equation. The two forms differ by the overall sign and by the factor $\hbar$, and neither changes the solution set.

**Varying the amplitude.** $\partial S/\partial r=0$ gives

$$
\Box_\Phi r+r\bigl((\partial\theta_{\mathrm{pha}})^{2}-k_m^{2}\bigr)=0
\qquad\Longleftrightarrow\qquad
\Bigl(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\Bigr)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r},
$$

which is the parent's amplitude equation, that is, the mass shell with the quantum potential $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ on the right. The equivalence uses $\hbar k_m=mc$ and multiplies by $\hbar^{2}$.

**The check is an identity.** Varying $r$ in the central action and integrating by parts gives $2r$ times the bracket of the first display up to the overall factor $-\hbar^{2}$, and varying $\theta_{\mathrm{pha}}$ gives $2r^{2}$ times the bracket of the second, with no boundary term for fields that vanish at the boundary. The two brackets are the two displays, so the Euler–Lagrange equations of the polar action are the parent's pair by construction, and the only input is $\hbar k_m=mc$.

**Nothing else.** The variation of $\varepsilon$ is not an equation: the sign is a branch of the modulus and not a coordinate, as the parent's §*The half turn, and the modulus* states. The central field therefore has two equations for two functions, and they are the parent's.

### The general element

For the eight parameters the statement is one line and it is exact.

**The pull-back.** The word $p\mapsto\tilde\Xi$ is a bijection from the parameter domain onto the $N$-regular set, with a smooth inverse and a Jacobian of full rank everywhere on that set. Hence $\delta S/\delta p^{a}=0$ for all eight $a$ if and only if $\delta S/\delta\tilde\Xi=0$, and the second is the Klein–Gordon equation. The eight parameter equations are the eight real components of the equation in the parameter basis, and the change between the two bases is the Jacobian.

**There is no constraint, and no multiplier.** This deserves stating, because the first-order case invites the opposite guess. The polar action is second order in every parameter, and its temporal block $g_{ab}$ restricted to $(\ln r,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}})$ is the pull-back of $\mathrm{Sc}((\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi)$ by an injective map, hence positive definite with the unit-determinant block of §*The Parameter Form*. So the conjugate momenta are $p_{a}=2g_{ab}\partial_{r'_t}p^{b}$ with $g$ invertible, no momentum vanishes identically, and the Legendre transform is a diffeomorphism. There are no primary constraints to analyse. In the first-order case four momenta vanish identically and the system is degenerate in that sense; here none does, and the degeneracy of the first-order case is a property of the first-order action, not of the word.

**No Lagrange multipliers for the unit conditions.** The four factors of the word are a boost of unit Hermitian norm, a rotor of unit quaternionic norm, a positive scale and an angle, so the unit conditions are solved by the parameterisation instead of being imposed. This is the contrast with Takabayasi's tensor formulation, whose spin vector and velocity are constrained unit vectors and whose variational principle therefore carries three multipliers. The parameters carry no multiplier because the parameters are coordinates on the constraint surface and not coordinates in the ambient space.

**What the equations do not say.** They do not say that $r$ and $\theta_{\mathrm{rpd}}$ are constant, or that the rotor precesses at a fixed rate; those are properties of particular solutions, not of the equations. The equations are the Klein–Gordon equation, and the parent's flow is what that equation does for a constant coefficient in the polar coordinates. The variational derivation reproduces the equation and therefore the flow, and it reproduces nothing else.

**Per mode, the constant-coefficient case is closed.** On a fixed four-wavevector the field is a constant biquaternion times a plane wave, and the element-form companion's §*A Vector Coefficient* gives the closed-form block for the two coefficients of that mode. The polar action is that same statement read on the amplitude and the phase of the mode, so it adds a reading and not a propagator. What has no closed form is the field, and this functional does not supply one.

### What the domain costs

The equivalence holds on the $N$-regular set, and only there. At $r=0$ the word has no value, the parameters are not coordinates, and the parameter equations are not defined; the Klein–Gordon equation itself is defined and regular there, and its solutions cross the nodal set without incident. So the polar action is a description of the field off its nodal set, and the element-form action of the companion is the description of the field everywhere. The two agree wherever both are defined. This is the same boundary the parent records, and the variational principle inherits it unchanged: a parametrisation cannot extend a functional past the points where the parametrisation stops.

## The Currents in Polar Variables

The Noether currents of the companion are one computation in the element form and one line each in these variables. That is the clearest thing the polar action adds.

### The charge is the phase rate times the density

On a central field the phase current of the companion is

$$
j_{r'_t}=2\,\mathrm{Re}\,\mathrm{Sc}\big[i(\partial_{r'_t}\tilde\Xi)^{*}\tilde\Xi\big]
=2r^{2}\,\partial_{r'_t}\theta_{\mathrm{pha}}=\frac{2r^{2}}{\hbar}\,\partial_{r'_t}S_{\tilde\Xi},
\qquad
j_\eta=-2r^{2}\,\partial_{r_\eta}\theta_{\mathrm{pha}},
$$

because $\mathcal{A}_\mu=\partial_\mu\ln r+i\partial_\mu\theta_{\mathrm{pha}}$, so that $i\mathcal{A}_\mu^{*}$ has scalar part $\partial_\mu\theta_{\mathrm{pha}}$. The charge density is therefore the density times the phase rate, and the phase rate is minus the energy over $\hbar c$,

$$
j_{r'_t}=2\rho_{\mathrm{num}}\frac{\partial_{r'_t}S_{\tilde\Xi}}{\hbar}
=-\frac{2\rho_{\mathrm{num}}E}{\hbar c}
=-2k_m\frac{\rho_{\mathrm{num}}E}{mc^{2}}
=-2k_m\,\rho_{\mathrm{chg}},
\qquad
\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}E}{mc^{2}},
\qquad
E=-c\,\frac{\partial S_{\tilde\Xi}}{\partial r'_t},
$$

which is the companion's $-2k_m\rho_{\mathrm{chg}}$ with the parent's $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$ and $E$ the sheet's energy. The sign of the charge is the sign of $\partial_{r'_t}\theta_{\mathrm{pha}}$ and nothing else: the amplitude is positive and carries no sign, and the factor $2\rho_{\mathrm{num}}$ is positive.

**Conservation is one of the two Euler–Lagrange equations.** Taking the divergence,

$$
\partial_{r'_t}j_{r'_t}+\sum_{\eta}\partial_{r_\eta}j_\eta
=2\Bigl[\partial_{r'_t}\bigl(r^{2}\partial_{r'_t}\theta_{\mathrm{pha}}\bigr)-\nabla\cdot\bigl(r^{2}\nabla\theta_{\mathrm{pha}}\bigr)\Bigr],
$$

whose bracket is the transport equation. So the conservation of the charge is the Euler–Lagrange equation of the phase, exactly, and not merely a consequence of it. In the element form the same statement needs the equation and its conjugate; here it needs one variation.

### The energy is a sum of squares

The energy density of the companion is

$$
T^{00}=(\partial_{r'_t}r)^{2}+\lvert\nabla r\rvert^{2}+r^{2}\bigl((\partial_{r'_t}\theta_{\mathrm{pha}})^{2}+\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\bigr)+r^{2}V,
$$

which is four squares and a positive potential for $V>0$, hence non-negative for every field on both frequency branches. The contrast with the charge is now visible in one display each: the charge is linear in the phase rate and the energy is quadratic in it, so the charge changes sign when the phase runs backwards and the energy does not. Nothing about the amplitude distinguishes the branches, and $r$ is the same on both.

**The two defects in one line.** The parent's §*The two defects, and one mechanism* reaches this conclusion by reading the current as $\rho_{\mathrm{num}}\tilde P_\Phi/m$. The variational principle reaches it from the other side: the charge is the Noether charge of a symmetry generated by the central $i$, the energy is the Noether charge of time translation, and the first is indefinite, the second is not, because the first is linear in a velocity that can run either way and the second is quadratic in it.

### The amplitude equation is the other Euler–Lagrange equation

The second equation of the pair is the variation of $r$, and in the polar variables it reads as the mass shell shifted by the curvature of the amplitude. So the two Euler–Lagrange equations of the polar action are the two statements of the parent's §*The Equation in Polar Variables*, and the variational principle adds to them the statement that they are two variations of one functional. The action that produces both is the one of §*The Action in Polar Variables*, and no second functional is needed.

## The Four Brackets and the Parameter Basis

### Two bases of one tangent space

At a point of the $N$-regular set the tangent space of the field values is eight-dimensional, and it has two natural bases.

**The bracket basis** is the decomposition of $\mathcal{A}_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$ into its four algebraic types: a real scalar, a central imaginary, a Hermitian element along the boost axis, and a real vector along the rotor's axis. Each type carries one physical role, and each is one object and not one number.

**The parameter basis** is the set of eight derivatives $\partial\tilde\Xi/\partial p^{a}$. These are eight elements of $\mathbb{B}$, not eight numbers, and they are the Jacobian columns of the word.

The two are related by $\mathcal{A}_\mu=\sum_a\mathcal{A}_a\,\partial_\mu p^{a}$ with $\mathcal{A}_a=\tilde\Xi^{-1}\partial\tilde\Xi/\partial p^{a}$, so the bracket basis is the parameter basis multiplied by one more factor of $\tilde\Xi^{-1}$. The metric of the polar action is the same in both readings,

$$
g_{ab}=\mathrm{Sc}\big[\mathcal{A}_a^{*}\,\tilde\Xi^{*}\tilde\Xi\,\mathcal{A}_b\big],
$$

which is the parameter form, and $\mathrm{Sc}(\mathcal{A}^{*}\tilde\Xi^{*}\tilde\Xi\,\mathcal{A})$ with $\mathcal{A}=\mathcal{A}_a\partial_\mu p^{a}$, which is the bracket form. The two differ by where the sum over the parameters is taken.

### The central field's Jacobian, worked

On the central field only $r$ and $\theta_{\mathrm{pha}}$ survive, and the Jacobian is computed in one line. With $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$,

$$
\frac{\partial\tilde\Xi}{\partial r}=e^{i\theta_{\mathrm{pha}}}\varepsilon e_t,
\qquad
\frac{\partial\tilde\Xi}{\partial\theta_{\mathrm{pha}}}=i\tilde\Xi,
\qquad
g_{rr}=\mathrm{Sc}\big[(\partial_r\tilde\Xi)^{*}\partial_r\tilde\Xi\big]=1,
\qquad
g_{\theta\theta}=\mathrm{Sc}\big[(\partial_\theta\tilde\Xi)^{*}\partial_\theta\tilde\Xi\big]=r^{2},
\qquad
g_{r\theta}=0,
$$

so the Jacobian is diagonal and the metric is $(1,r^{2})$. The two parameter equations are then the two brackets: the $r$ equation is the real-scalar bracket's content, that is the amplitude equation, and the $\theta_{\mathrm{pha}}$ equation is the central-imaginary bracket's content, that is the transport equation.

**The correspondence is triangular here.** Each parameter touches one bracket and one only, so the two parameter equations are the two brackets and the map between them is the identity. In the general element this ceases to hold: the derivatives of the amplitude carry a piece of the rapidity because of the $\sinh$ cross term, and the derivative of the phase carries a piece of the rotor's rate whenever $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}\neq0$. That is what a nonlinear parameterisation does, and it is why the parameter equations mix the brackets.

### Which is the natural form

**The bracket form is the natural one.** The Lagrangian is one quadratic form in one object, the bracket $\mathcal{A}_\mu$, weighted by one density factor; the bracket is four objects of four types, and the four types are the four things an element of the algebra can be. The equation is the vanishing of eight residuals, and the four brackets are the four types those residuals fall into.

**The parameter form is the Jacobian image of it.** It is the form in which the variational principle is stated over eight real functions with no auxiliary object, and it is the form in which the count is right: eight functions, eight equations, no constraint. But it is not simpler, and the parameter equations are not four equations plus four conditions; they are eight equations whose content is the brackets'.

**The equivalence is exact.** The Jacobian is invertible on the $N$-regular set, so the two systems have the same solutions there. Neither is weaker: a solution of the brackets is a solution of the parameters and conversely, and the passage is the chain rule.

## What the Polar Variational Principle Adds and What It Does Not

**Adds.** A variational derivation of the parent's pair, with the two equations as two variations of one functional. The exact metric of the parameter space, with the cosh on the squares, the two sinh cross terms and the unit determinant of the amplitude–rapidity block. The potential as $r^{2}V$ with the same $V$ as the Schrödinger companion, so that the two articles' potentials are one function. The statement that the charge conservation is the phase equation and the mass shell is the amplitude equation. The statement that the unit conditions cost no multiplier, because the word is a parameterisation of the constraint surface. And the statement that the second-order polar action has no primary constraint, in contrast with the first-order case.

**Does not add.** No new prediction and no new solution: the equation is the parent's and the flow is the parent's. No simplification of the four brackets, which remain the natural form. No extension past the nodal set, where the word stops and the equation does not. And no claim that the parameter equations are a weaker or a stronger system than the brackets: they are the same system in another basis.

**The distinction that matters.** The element-form variational principle is standard and its Noether currents are the classical ones. The polar-form one is the same functional in the coordinates of the algebra's polar decomposition, and what it delivers that the element form does not is the metric, the density weighting, and the one-line reading of the two currents. What it costs is the domain: the polar action is defined off the nodal set only.

## Open Questions

1. **The metric with moving axes.** The boxed metric is computed on the slice of fixed axes, where four of the eight parameters vary. With the axes moving there are further terms, and whether the eight-parameter metric factors into a product of the four bracket blocks, or keeps irreducible cross terms between them, is not settled here. The central-field case suggests a product structure; the $\sinh$ cross terms already show that the product is not the naive one.

2. **The nodal set and the functional.** The polar action is defined where the word is, and the word stops at $r=0$. The element-form action of the companion is defined everywhere and its solutions cross the nodal set. Whether a functional of the eight parameters can be continued across a node, and what the continuation means for the circulation of the phase around it, is a question for *The Nodal Set and Quantized Circulation* and is not answered by the variational principle.

3. **The operator case in these variables.** With a coefficient that varies in space and time the polar action keeps its form and $V$ becomes a function of position as well as of the parameters. Whether the quantum potential keeps its density-only form when $V$ varies, and whether the metric story survives a coefficient that is not central, is not attempted here. The non-relativistic limit of the parent suggests that the density-only form survives, and a suggestion is not a derivation.

## Summary

The polar action is the element-form action in the coordinates of the word,

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{g_{ab}(p)\,\partial_{r'_t}p^{a}\partial_{r'_t}p^{b}-\sum_{\eta}g_{ab}(p)\,\partial_{r_\eta}p^{a}\partial_{r_\eta}p^{b}-r^{2}V(p)\Bigr\},
$$

with the kinetic Lagrangian of one direction

$$
\mathrm{Sc}\big[(\partial\tilde\Xi)^{*}\partial\tilde\Xi\big]
=r^{2}\Bigl\{\cosh\theta_{\mathrm{rpd}}\Bigl[(\partial\ln r)^{2}+(\partial\theta_{\mathrm{pha}})^{2}+\frac{(\partial\theta_{\mathrm{rpd}})^{2}}{4}+\frac{(\partial\theta_{\mathrm{axr}})^{2}}{4}\Bigr]+\sinh\theta_{\mathrm{rpd}}\Bigl[(\partial\ln r)(\partial\theta_{\mathrm{rpd}})-(\partial\theta_{\mathrm{pha}})(\partial\theta_{\mathrm{axr}})\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}\Bigr]\Bigr\}
$$

for fixed axes, whose metric $g_{ab}$ is read off by replacing each $\partial p^{a}$ with the parameter derivative, and with the potential $V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_{\mathrm b})$ for a Hermitian coefficient $h_t e_t+i\vec h_\Psi$. The kinetic Lagrangian is $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi\,\mathcal{A}_\mu\mathcal{A}^{\mu*})$ with $\mathcal{A}_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$: the frame density times the square of the bracket. The density factor is $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=r^{2}\cosh\theta_{\mathrm{rpd}}$, and it is the coefficient of every square.

The rapidity enters in two ways and both are needed. It multiplies all four squares through $\cosh\theta_{\mathrm{rpd}}$, and it multiplies two cross terms through $\sinh\theta_{\mathrm{rpd}}$: one between the amplitude gradient and the rapidity gradient, one between the phase gradient and the rotor's angular rate, and the second carries the cosine between the two axes. The amplitude–rapidity block has determinant $\tfrac14$, the identity $\cosh^{2}-\sinh^{2}=1$ appearing as a unit-determinant mixing. The first-order Schrödinger action has the same cosh multiplying a single velocity, because its kinetic term is one bracket; the second-order action has two brackets and the same factor becomes a metric entry.

For the central field the metric collapses to $(1,r^{2})$ and the action is Madelung's, with the two Euler–Lagrange equations being the parent's transport equation and the parent's quantum Hamilton–Jacobi equation. The charge density is $j_{r'_t}=2\rho_{\mathrm{num}}\partial_{r'_t}\theta_{\mathrm{pha}}=-2k_m\rho_{\mathrm{chg}}$, linear in the phase rate and therefore of either sign; the energy density is a sum of four squares plus $r^{2}V$, quadratic in the phase rate and therefore non-negative. The conservation of the charge is the phase equation, and the amplitude equation is the mass shell with the quantum potential.

For the general element the equivalence with the Klein–Gordon equation is exact, because the word is a bijection with a smooth inverse and the Jacobian is invertible on the $N$-regular set. There is no constraint and no multiplier: the action is second order in every parameter, the temporal block of the metric is positive definite, and the Legendre transform is regular. The unit conditions cost no multiplier because the parameterisation solves them. The four brackets remain the natural form, and the parameter equations are their Jacobian image, exact and triangular on the central field and mixed on the general element. The domain is the $N$-regular set, and the variational principle stops where the word stops.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_{C},\ \mathbb{B}_{\Psi},\ \mathbb{B}_{\Phi}$ | Centre, Hermitian subspace, anti-Hermitian subspace |
| $^{*},\ ^{\natural}$ | Hermitian conjugation, quaternion conjugation |
| $\mathrm{Sc},\ \mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part and trace |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r'^{2}_{t}$ | d'Alembertian; $r'_t=c\,t'$ |
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word |
| $r>0$ | Scale and amplitude; $\rho_{\mathrm{num}}=r^{2}$ |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Phase angle; $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ |
| $\theta_{\mathrm{rpd}}\ge0$ | Rapidity of the boost $\tilde U_{\Psi,\mathrm b}$ |
| $\theta_{\mathrm{axr}}\in[0,2\pi)$ | Angle of the rotor $\tilde u_{\mathrm r}$ |
| $\vec u_{\mathrm b},\ \vec u_{\mathrm r}$ | Real unit axes of the boost and the rotor |
| $\vec u_{\mathrm b}'=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ | Boost axis in the rotor's frame |
| $\mathcal{A}_\mu=\tilde\Xi^{-1}\partial_\mu\tilde\Xi$ | The bracket; four algebraic types |
| $\tilde\Xi^{*}\tilde\Xi=r^{2}(\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}')$ | Frame density |
| $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=r^{2}\cosh\theta_{\mathrm{rpd}}$ | The density ratio that weights every square |
| $\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2r^{2}\cosh\theta_{\mathrm{rpd}}$ | The parent's density |
| $g_{ab}(p)$ | Induced metric on the parameters |
| $p^{a}$ | The eight parameters as coordinates |
| $k_m=mc/\hbar$ | Mass wave number |
| $V$ | $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)/r^{2}$, real, a function of rapidity and axis |
| $j_{r'_t},\ j_\eta$ | Charge current; $j_{r'_t}=2\rho_{\mathrm{num}}\partial_{r'_t}\theta_{\mathrm{pha}}$ |
| $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$ | Charge density; $j_{r'_t}=-2k_m\rho_{\mathrm{chg}}$ |
| $T^{00}$ | Energy density; four squares plus $r^{2}V$ |
| $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ | Quantum potential of the amplitude equation |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the non-relativistic pair and its action.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, and "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin-$0$ and spin-$\tfrac12$ cases; the multiplier-free formulation of this article is what the parameterisation buys against the tensor version of the second.
- Louis de Broglie, *La mécanique ondulatoire* (Gauthier-Villars, 1930), for the phase as the action.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Belfer Graduate School, 1964), for primary and secondary constraints; the second-order polar action has none, and the contrast with the first-order case is the point of §*The General Element*.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the relativistic quantum potential and the difficulty with the speed of light.
- The companion articles: [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Form](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-form.html), for the element-form action, its pairing and its currents; [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the pair, the current and the two defects in these variables; [The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the first-order case, where the cosh multiplies a velocity; [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its domain; [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the cone; [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), for the tensor built from these two functions; [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the phase around a node; [The Non-Quantum Limit of the Free Schrödinger Equation](the-non-quantum-limit-of-the-free-schrodinger-equation.html), for the non-relativistic pair and its quantum potential.
