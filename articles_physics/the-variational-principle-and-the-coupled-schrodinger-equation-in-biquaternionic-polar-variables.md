# __The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables__

## Introduction

*The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables* computes the free polar Lagrangian exactly,

$$
L=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}
+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})
-r^{2}V,
\qquad
V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b}),
$$

with $\vec\Omega$ the rotor's angular velocity, $\partial_{t'}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{-1}=\frac12\vec\Omega$. It shows that four of the eight momenta vanish identically, that the Euler–Lagrange equations are exactly the eight components of the field equation in the parameter basis, and that their solutions are the parent's flow.

This article puts the electromagnetic connection into that Lagrangian and asks what the chart does with it. The answer has one sentence — **the connection enters the potential and not the kinetic term, in the constant setting** — and that sentence has consequences worth four sections: the phase coefficient $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}$ is untouched, so the momenta and the constraint structure are untouched; the potential $V$ becomes the shifted potential $V_{\mathrm{gco}}$; the flow is the free flow read with the kinetic eigenvalues; and the chart acquires a gauge direction which the free chart does not have.

**Three findings.**

*First, in the constant setting the coupling is a shift of the potential and nothing else.* The kinetic term is built from the field's own velocities — $\dot\theta_{\mathrm{pha}}$ and $\vec\Omega$ — and the connection contributes no velocity, because its coefficients are constants and its only slot in a first-order action is the energy. So

$$
V_{\mathrm{gco}}=(h_t-ϙ\varphi)\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,\big((\vec h_\Psi+ϙ\vec A)\cdot\vec u_{\mathrm b}\big),
$$

and every other term of the Lagrangian is the free one, letter for letter. The four vanishing momenta stay vanishing, the cross term $\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}(\vec\Omega\cdot\vec u_{\mathrm b})$ stays, and the phase momentum stays $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}$ (§*The Coupled Polar Lagrangian*, §*The Euler–Lagrange Equations*).

*Second, the shift is the whole of minimal coupling in a setting with no derivatives, and it is a shift of two numbers.* The unshifted pair $(h_t,\vec h_\Psi)$ is the canonical pair; the shifted one is the kinetic pair; the flow's two rates are built from the shifted one. So the coupled flow is the free flow with $h_t\to h_t-ϙ\varphi$ and $\vec h_\Psi\to\vec h_\Psi+ϙ\vec A$, and no structural statement changes (§*The Euler–Lagrange Equations*).

*Third, the chart acquires a gauge direction, and the direction is $\theta_{\mathrm{pha}}$.* The gauge group translates the phase and leaves the other seven parameters alone, so the coupled chart has a direction along which the field and the connection together are unchanged. The free chart has no such direction: all eight parameters are physical. The consequence is the sharp statement of the coupled chart — the momentum conjugate to the gauge direction is $-\hbar N$, and $N$ is the charge that the connection sources (§*The Gauge Direction of the Chart*).

**What is not claimed.** No new prediction and no new solution. The polar Lagrangian is a substitution, not a new principle; the free article's closure argument — that the parameter equations are the equation's components and the Jacobian is invertible — is repeated with covariant letters and not replaced. The genuinely new statements are the four above: that the kinetic term is untouched, that the constraint structure is therefore untouched, that the potential shift is a two-number shift, and that the gauge direction of the chart is the phase.

**Conventions.** The algebra, the word, the parameter ranges, the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$ and the letters are the free polar variational article's. The connection is $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ with $\varphi=c\,a'_t$, the coupling is $ϙ$, and the covariant derivative is $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$. The charge $ϙ$ is minus the electric charge of the older convention, so the mechanical momentum is $\vec\pi=\vec p+ϙ\vec A$ and the potential energy enters as $-ϙ\varphi$. Time is $t'$ throughout, and the article never writes $r'_t$.

## The Coupled Polar Lagrangian

**The substitution.** The element-form companion's action is Article 3's,

$$
S=\int dt'\,d^{3}x\;\mathrm{Sc}\Big[\frac{i\hbar}{2}\big(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\big)
-\frac{\hbar^{2}}{2m}\sum_\eta\big(D_\eta\tilde\Xi\big)^{*}\big(D_\eta\tilde\Xi\big)
+ϙ\varphi\,\tilde\Xi^{*}\tilde\Xi\Big],
$$

and in the constant setting the spatial terms are absent: $\tilde H_\Psi$ is an element, not a differential operator, and the connection is constant. So the only two places the connection can enter are the potential term $ϙ\varphi\,\tilde\Xi^{*}\tilde\Xi$ and the Hamiltonian element itself, and both are central.

**Why the kinetic term cannot change.** The kinetic term is built from the field's velocities and from the field's algebraic type. The connection contributes (i) no velocity, since it is constant, and (ii) a central number in every slot, since its coefficients are scalars. A central number added to a bracket cannot create a Hermitian part or a real vector, so it cannot enter the cross term, which needs one of each; and it cannot change $\tilde U^{2}=\cosh\theta_{\mathrm{rpd}}+i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$, which is built from the field alone. The kinetic term of the coupled Lagrangian is therefore the free one,

$$
K=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b}),
$$

with no subscript and no correction. This is the article's first finding and the reason the rest of the article is short.

**The potential.** The potential term of the action is $+ϙ\varphi\,\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$, and the free article's computation of $\mathrm{Sc}(\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi)=r^{2}V$ goes through with $\tilde H_\Psi\to\tilde H^{\mathrm{gco}}_\Psi$, because the shift is by a central number and the central phase cancels between the two factors as before. Hence

$$
V_{\mathrm{gco}}=(h_t-ϙ\varphi)\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,\big((\vec h_\Psi+ϙ\vec A)\cdot\vec u_{\mathrm b}\big),
$$

and the coupled Lagrangian is

$$
\boxed{\;L=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}
+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})
-r^{2}V_{\mathrm{gco}}.\;}
$$

**What the shifted potential contains.** The first term is the shifted energy times the boost's weight; the second is the shifted momentum contracted with the boost axis. So a constant potential changes the weight of $\cosh\theta_{\mathrm{rpd}}$, a constant vector potential changes the weight of $\sinh\theta_{\mathrm{rpd}}$, and neither changes the coefficient of $\dot\theta_{\mathrm{pha}}$. The $\vec A$-dependence is the term that the free Lagrangian had with $\vec h_\Psi$ alone, and it is the polar form of the statement that the vector potential is a momentum shift.

**The action, written out.**

$$
S=\int dt'\Big[-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}
+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})
-r^{2}\Big((h_t-ϙ\varphi)\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi+ϙ\vec A)\cdot\vec u_{\mathrm b}\Big)\Big].
$$

It is a functional of the eight parameters and of the two connection numbers, it is first order in the parameters' velocities, and its only dependence on the connection is through $V_{\mathrm{gco}}$.

## The Euler–Lagrange Equations

**The momenta are the free ones.** Differentiating with respect to the velocities and using $\partial(\vec\Omega\cdot\vec u_{\mathrm b})/\partial\dot\theta_{\mathrm{rpd}}=0$ (the angular velocity is the rotor's own, not the boost's):

$$
p_{r}=0,
\qquad
p_{\theta_{\mathrm{rpd}}}=0,
\qquad
p_{\vec u_{\mathrm b}}=0,
\qquad
p_{\theta_{\mathrm{pha}}}=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}} .
$$

Four vanishing momenta and one nonzero, exactly as in the free article, and for the same reason: the Lagrangian is first order, so the velocities other than $\dot\theta_{\mathrm{pha}}$ enter only through $\vec\Omega$, which is not conjugated to any of them. **The coupling does not change the constraint structure**, and the reason is stated in §*The Coupled Polar Lagrangian*: it contributes no velocity, so it cannot create a momentum.

**The equations.** The Euler–Lagrange equations are the free ones with $V\to V_{\mathrm{gco}}$:

$$
\frac{d}{dt'}\big(r^{2}\cosh\theta_{\mathrm{rpd}}\big)=0,
$$

$$
-\hbar\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\frac{\hbar}{2}\sinh\theta_{\mathrm{rpd}}\,a=V_{\mathrm{gco}},
\qquad
-\hbar\sinh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}+\frac{\hbar}{2}\cosh\theta_{\mathrm{rpd}}\,a=\frac{\partial V_{\mathrm{gco}}}{\partial\theta_{\mathrm{rpd}}},
$$

with $a=\vec\Omega\cdot\vec u_{\mathrm b}$, and the four equations for the two axes and the rotor's angle are the free ones with $\vec h_\Psi\to\vec h_\Psi+ϙ\vec A$ and $h_t\to h_t-ϙ\varphi$. Eliminating $a$ between the second and third gives the two rates,

$$
\dot\theta_{\mathrm{pha}}=-\frac{h_t-ϙ\varphi}{\hbar},
\qquad
\vec\Omega=\frac{2\big(\vec h_\Psi+ϙ\vec A\big)}{\hbar},
$$

which are the free flow's rates with the shifted numbers.

**Why the coupled system closes the way the free one does.** The free article's closure argument is that the eight residuals are exactly the eight real components of the field equation in the parameter basis, and that the word's Jacobian is invertible. Neither half of that argument uses the potential: the first is an identity between the residual $i\hbar\partial_{t'}\tilde\Xi-\tilde H_\Psi\tilde\Xi$ and its coordinates, and the second is a property of the word. In the coupled case the residual is $i\hbar D_t\tilde\Xi-\frac{1}{2m}(-i\hbar\vec D)^{2}\tilde\Xi$ in the operator setting, and in the constant setting it is $i\hbar\partial_{t'}\tilde\Xi-\tilde H^{\mathrm{gco}}_\Psi\tilde\Xi$ — the same element equation with a different letter. So the closure carries over unchanged, and the article states that rather than repeating the proof.

**The honest qualification.** The closure of the *free* polar variational principle is the free article's result and it is established there. The coupled statement is a corollary and not a new proof, which is why this section is short. What the coupling does not do is supply a second, independent derivation: the parameter equations are the equation's components, and they are not "the four brackets" — the relation between the two bases is the Jacobian's, and it is the free article's §*The Relation to the Four Brackets*.

**One difference in the residual's shape.** In the operator setting the residual is not a single element at a point but a differential operator, and the parameter equations then contain the gradient terms of §*The Central Field in the Operator Setting*. The constant setting is where the article's structural statements live, and the operator setting is where the physics of the potential and the current lives.

## The Central Field in the Operator Setting

**The word collapses.** With $\theta_{\mathrm{rpd}}=0$ and a rotor that is a sign, the two paragraphs of the free article apply: the boost and the rotor are trivial, $K=-\hbar r^{2}\dot\theta_{\mathrm{pha}}$, and the potential is $h_t r^{2}$. With the connection in place and the operator $\hat H^{\mathrm{gco}}=\tilde{\vec\pi}^{2}/2m-ϙ\varphi+\hat V_{\mathrm{op}}$, the action becomes

$$
S=\int dt'\,d^{3}x\Big[-\hbar\,r^{2}\,\dot\theta_{\mathrm{pha}}
-\frac{\hbar^{2}}{2m}\Big(|\nabla r|^{2}+r^{2}\Big|\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Big|^{2}\Big)
-r^{2}V_{\mathrm{op}}+ϙ\varphi\,r^{2}\Big],
$$

which is the free article's Madelung action with the two covariant replacements: the phase gradient becomes the kinetic momentum over $\hbar$, and the potential energy is added. Both replacements are the same rule as everywhere else, and neither is optional.

**The three coupling pieces.** Expanding the middle term separates the coupling into three parts,

$$
-\frac{\hbar^{2}}{2m}r^{2}\Big|\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Big|^{2}
=-\frac{\hbar^{2}}{2m}r^{2}|\nabla\theta_{\mathrm{pha}}|^{2}
-\frac{\hbar ϙ}{m}r^{2}\,\vec A\cdot\nabla\theta_{\mathrm{pha}}
-\frac{ϙ^{2}}{2m}r^{2}A^{2},
$$

which are the free kinetic term, the paramagnetic term linear in $\vec A$, and the diamagnetic term quadratic in $\vec A$. The three are one object read at three orders, and the sign of the third is what makes the energy bounded below: the quadratic term is positive for every $\vec A$, so the coupled action's kinetic part is bounded below by zero, and the diamagnetism is a variational statement before it is a physical one.

**The equations.** Varying $\theta_{\mathrm{pha}}$ gives the covariant continuity equation, varying $r$ the covariant Hamilton–Jacobi equation with the quantum potential, and varying the sign gives nothing because the sign is a branch. The two are the polar companion's pair,

$$
\partial_{t'}r^{2}+\nabla\cdot\Big(r^{2}\,\frac{\nabla S+ϙ\vec A}{m}\Big)=0,
\qquad
\partial_{t'}S+\frac{|\nabla S+ϙ\vec A|^{2}}{2m}-ϙ\varphi+Q=0,
$$

with $S=\hbar\theta_{\mathrm{pha}}$ and $Q=-\hbar^{2}\Delta r/2mr$, and the article does not re-derive them: they are the Euler–Lagrange equations of the action above, and the derivation is the free article's with two substitutions.

**The current as the action's derivative.** The vector potential's conjugate is the current:

$$
-\frac{\partial L}{\partial\vec A}
=\frac{\hbar^{2}}{2m}r^{2}\cdot 2\Big(\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A\Big)\frac{ϙ}{\hbar}
=ϙ\,\frac{r^{2}\big(\hbar\nabla\theta_{\mathrm{pha}}+ϙ\vec A\big)}{m}
=ϙ\,\vec j,
$$

which is the element-form companion's identity in the chart and is one line here because the action's only $\vec A$-dependence is the modulus. The polar form of the identity is worth having because it displays the current's three pieces at once: a gradient piece, a term linear in $\vec A$ from the paramagnetic term, and a term quadratic in $\vec A$ from the diamagnetic one — and only the sum is gauge invariant.

**The vorticity, unchanged in form.** The velocity is $\vec\pi/m$ and its curl is $ϙ\vec B/m$; the parameterization does not change that, because the curl of a gradient vanishes and the parameterization only names the gradient. So the free article's irrotationality statement becomes: the canonical flow is irrotational, the kinetic flow is rotational exactly where the field is, and the chart exhibits the difference as the difference between $\nabla S$ and $\vec\pi$.

**What the operator setting does not have.** It has no vanishing momenta. The action is second order in the spatial derivatives and first order in time, so the momenta conjugate to $r$ and to the phase are both nontrivial, and the constraint structure of the constant setting has no analogue here. The two settings' variational principles are different objects, and the article keeps them apart as the parents do.

## The Gauge Direction of the Chart

**The action of the gauge group on the parameters.** Under $\tilde\Xi\mapsto e^{iϙ\Gamma/\hbar}\tilde\Xi$,

$$
r\longmapsto r,
\qquad
\theta_{\mathrm{pha}}\longmapsto\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Gamma,
\qquad
\theta_{\mathrm{rpd}}\longmapsto\theta_{\mathrm{rpd}},
\qquad
\vec u_{\mathrm b}\longmapsto\vec u_{\mathrm b},
\qquad
\theta_{\mathrm{axr}}\longmapsto\theta_{\mathrm{axr}},
\qquad
\vec u_{\mathrm r}\longmapsto\vec u_{\mathrm r},
$$

because the factor is central and commutes with every unit. Seven parameters are inert and one is translated by a function.

**The Lagrangian's response.** The kinetic term gains $-ϙ\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\partial_{t'}\Gamma$ and the potential term gains $+ϙ\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\partial_{t'}\Gamma$, since $\varphi\mapsto\varphi+\partial_{t'}\Gamma$ enters $V_{\mathrm{gco}}$ with one minus. The gains cancel, and the action of the field and the connection together is invariant — the element-form companion's statement, in the chart's letters, and here it is visibly the statement that $\theta_{\mathrm{pha}}$'s coefficient and $\varphi$'s coefficient are the same function of the rapidity.

**What happens when the connection is held fixed.** With $\varphi$ fixed, the two gains do not cancel and the action changes by a boundary term for a time-dependent $\Gamma$. So the local transformation is not a symmetry of the fixed-background action; only its constant part is. The distinction is worth stating because it is exactly the distinction between the global symmetry that gives the charge and the local one that gives the redundancy: **the gauge direction of the chart is a direction of the coupled system's action and not of the field's action in a fixed background.**

**The momentum along the gauge direction.** $p_{\theta_{\mathrm{pha}}}=-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}=-\hbar N$, and $N$ is invariant, so the momentum is invariant: the translation of $\theta_{\mathrm{pha}}$ moves the coordinate and not the momentum. That is the chart's version of the statement that the charge is gauge invariant and the phase is not, and it is also the reason the conservation of $N$ survives the coupling: it is the Euler–Lagrange equation of $\theta_{\mathrm{pha}}$, and the gauge direction does not disturb it, because the equation is $\dot p_{\theta}=0$ and a constant translation cannot change a derivative.

**What the chart's degeneracy means for the equations.** The eight parameter equations are the eight components of the field equation, and the gauge direction is not one of them: the field equation is invariant, so a family of parameters related by the gauge direction gives one equation. The counting is therefore unchanged — eight equations for eight parameters, with the gauge direction a redundancy of the description and not a new degree of freedom. The free chart's counting is the same, with the redundancy absent.

**The free article's "no gauge freedom" and the coupled statement.** The free polar variational article records that the free equation fixes the phase's rate and that there is no gauge freedom to fix. The coupled statement is compatible with it and sharper: the rate is still fixed, and it is the gauge-invariant combination $\mathcal E=-\hbar\dot\theta_{\mathrm{pha}}+ϙ\varphi$ that is fixed; the phase itself is free. So the coupling converts a physical coordinate into a coordinate with a gauge direction, and the direction is the one whose conjugate momentum is the density.

## What It Adds and What It Does Not

**Adds.** The coupled Lagrangian in the chart, and with it the two-number statement of minimal coupling: $h_t\mapsto h_t-ϙ\varphi$, $\vec h_\Psi\mapsto\vec h_\Psi+ϙ\vec A$ in the potential, and nothing else. The statement that the kinetic term is untouched, with the algebraic reason — the connection is central and carries no velocity — and the corollary that the four vanishing momenta and the cross term are untouched. The covariant Madelung action with its three coupling pieces, its two Euler–Lagrange equations, and the current as $-\partial L/\partial\vec A$. And the gauge direction of the chart, with the invariant momentum $-\hbar N$ along it.

**Does not add.** No new solution and no new prediction. No new closure proof: the closure is the free article's, transported. No decoupling of the four brackets from the parameter equations: the Jacobian is the free one's, because the word is the free one's. No constraint analysis: the constant-setting system's closure is the free article's open question and the coupling does not decide it — it neither creates a constraint nor removes one.

**The distinction that matters, stated once.** In the constant setting the coupling is a shift of the potential, so it touches the flow's numbers and not the flow's structure. In the operator setting the coupling is a covariant gradient, so it touches the kinetic term and not the potential's shape. The two settings' statements are different, and the polar chart is the only place where both are visible in one symbol — the phase bracket — because that is where the covariant derivative and the potential both live.

## Open Questions

**1. The coupled closure of the constrained system.** The free article leaves open whether the Dirac constraint analysis of the four vanishing momenta closes and reproduces the flow directly. The coupling does not change the constraints, so it does not change the question; but it does add one thing to check, namely that the Dirac bracket of the shifted potential's constraints reproduces the shifted flow and not the free one. The check is short and is not performed here.

**2. The operator setting for the general element.** The article's operator statements are the central field's. A boost that varies from point to point puts a gradient into the Hermitian bracket, and the connection's central-imaginary addition then sits alongside a Hermitian gradient term; how the three coupling pieces of §*The Central Field in the Operator Setting* generalize to the four-bracket decomposition is not examined here.

**3. The coupling's own variation in the chart.** Varying the connection in the polar action gives the Maxwell equation with the current of §*The Central Field in the Operator Setting* as source, and varying $\varphi$ gives the Gauss law with the density as its source. The chart has a sharper form of the second statement: the source is the momentum conjugate to the phase, $-\hbar N$, so the charge and the phase's momentum are one object. Whether that identification survives the constraint analysis of the constant-setting system is not examined here.

## Summary

The coupled polar Lagrangian is the free one with the potential shifted,

$$
L=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}
+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})
-r^{2}V_{\mathrm{gco}},
$$

$$
V_{\mathrm{gco}}=(h_t-ϙ\varphi)\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,\big((\vec h_\Psi+ϙ\vec A)\cdot\vec u_{\mathrm b}\big).
$$

The kinetic term is untouched, because the connection is central and carries no velocity. The four momenta $p_r$, $p_{\theta_{\mathrm{rpd}}}$, $p_{\vec u_{\mathrm b}}$ vanish identically and $p_{\theta_{\mathrm{pha}}}=-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}=-\hbar N$; the constraint structure is the free one's. The Euler–Lagrange equations are the free ones with $V\to V_{\mathrm{gco}}$, and their solution is the free flow with $\dot\theta_{\mathrm{pha}}=-(h_t-ϙ\varphi)/\hbar$ and $\vec\Omega=2(\vec h_\Psi+ϙ\vec A)/\hbar$: the coupling shifts the canonical pair to the kinetic pair and changes nothing else.

In the operator setting, for the central field, the action is the Madelung action with the kinetic momentum and the potential energy,

$$
S=\int dt'\,d^{3}x\Big[-\hbar r^{2}\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\Big(|\nabla r|^{2}+r^{2}\big|\nabla\theta_{\mathrm{pha}}+\tfrac{ϙ}{\hbar}\vec A\big|^{2}\Big)-r^{2}V_{\mathrm{op}}+ϙ\varphi r^{2}\Big],
$$

its equations are the covariant Madelung pair, and its $\vec A$-derivative is the charge current, $-\partial L/\partial\vec A=ϙ\vec j$. The three coupling pieces are the free kinetic term, the paramagnetic term and the positive diamagnetic term.

The gauge group translates $\theta_{\mathrm{pha}}$ and nothing else, so the coupled chart has one gauge direction and the free chart has none. Along it the momentum $-\hbar N$ is invariant, and the conservation of $N$ is the Euler–Lagrange equation of the phase, undisturbed by the translation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,b}u_r$ | The word of the field |
| $\tilde U_{\Psi,b}=\exp(i\theta_{\mathrm{rpd}}\vec u_b)$ | The Hermitian boost; $\vec u_b$ its axis |
| $\theta_{\mathrm{pha}}$, $r$ | The phase and the scale |
| $\theta_{\mathrm{rpd}}$, $\vec u_b$ | Rapidity and axis of the boost |
| $\theta_{\mathrm{axr}}$, $\vec u_r$ | Angle and axis of the rotor |
| $\vec\Omega$ | The rotor's angular velocity, $\partial_{t'}\tilde u_r\tilde u_r^{-1}=\frac12\vec\Omega$ |
| $a=\vec\Omega\cdot\vec u_b$ | The rotor's angular velocity along the boost axis |
| $h_t$, $\vec h_\Psi$ | The canonical energy and momentum of the free element |
| $h_t-ϙ\varphi$, $\vec h_\Psi+ϙ\vec A$ | The kinetic energy and momentum |
| $V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_b)$ | The free polar potential |
| $V_{\mathrm{gco}}$ | The coupled polar potential |
| $ϙ$ | The coupling; minus the electric charge of the older convention |
| $\varphi=c\,a'_t$, $\vec A$ | The electric and vector potentials |
| $N=r^{2}\cosh\theta_{\mathrm{rpd}}$ | The charge; $p_{\theta_{\mathrm{pha}}}=-\hbar N$ |
| $S=\hbar\theta_{\mathrm{pha}}$ | The action of the flow |
| $Q=-\hbar^{2}\Delta r/2mr$ | The quantum potential |
| $L$ | The Lagrangian; $K$ its kinetic term |
| $\Gamma$, $\lambda=e^{iϙ\Gamma/\hbar}$ | The gauge function and factor |

## Further Reading

- [The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), the free companion whose Lagrangian, momenta and closure argument this article extends.
- [The Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), for the chart's reading of the coupling without the action.
- [The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-schrodinger-equation-in-biquaternionic-form.html), for the element-form action and the current as the connection's derivative.
- [The Schrödinger Equation in Biquaternionic Polar Variables](the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the word, the four brackets and the free flow.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the word's bijection on which the closure rests.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator's two slots.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localisation that becomes the chart's gauge direction.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the same chart in the spinor case, where the connection reaches all four brackets.
- [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), for the hydrodynamical reading of the central-field action.
- [Landau Levels in Biquaternionic Form](landau-levels-in-biquaternionic-form.html), for the operator setting in a constant magnetic field, where the diamagnetic term is the whole spectrum.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40**, 322 (1927).
- T. Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8**, 143 (1952), for the hydrodynamical formulation and its constraint analysis.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the constraint analysis that §*Open Questions* invokes.
