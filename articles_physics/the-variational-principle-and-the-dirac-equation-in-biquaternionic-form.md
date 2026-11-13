# __The Variational Principle and the Dirac Equation in Biquaternionic Form__

## Introduction

*The Dirac Equation in Biquaternionic Form* writes the equation as a pair,

$$
\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R,
\qquad
k_m=\frac{mc}{\hbar},
$$

with $\tilde\Xi=\tilde\Xi_L+\tilde\Xi_R$ one element of $\mathbb{B}$ and the two subscripts naming its two parts. This article asks the question the Schrödinger companion asks: what action has this pair as its Euler–Lagrange equations, and what do the action's symmetries give?

The answer is one action, the pair as its variation, the electric current and the energy-momentum tensor with their chiral partner, and one structural statement that the element form could not make on its own. The structural statement is that the two-part form is a factorization that the two operators force: $\tilde\nabla_\Phi$ acts on one part and $(\tilde\nabla_\Phi)^{\natural}$ on the other, a first-order functional gives each operator one slot, and the mass is the only term that can couple two slots. It is not that a one-element action is impossible; it is that a one-element action cannot be the pair's.

**This is the element-form variational principle.** The polar-form one is the companion article. The two differ more than the Schrödinger pair do, because the polar word carries a boost and a rotor and the polar action therefore carries the constraints that the element action does not.

**The equation is the parent's.** Nothing here is a new prediction and nothing here is a new solution. What is added is the action, the currents, and the reason the split is forced.

The formalism is that of *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, and the action principle is that of *The Action Principle and the Non-Quantum Limit in Biquaternionic Form*; this article applies the principle to the Dirac equation in its element form.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $e_t=1$, $\vec e_\mu^{2}=-e_t$, $i$ central. $\mathrm{Sc}$ is the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. The conjugations are $*$ (Hermitian, $\tilde X^{*}=\bar{\tilde X}^{\natural}$) and $\natural$ (quaternion). The gradient is $\tilde\nabla_\Phi=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ with $R_t=ir'_t$, so that $\partial/\partial R_t=-i\,\partial/\partial r'_t$, and $(\tilde\nabla_\Phi)^{\natural}$ is the same operator with the spatial part reversed. The four-position is $\tilde R_\Phi=ir'_te_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$. The material time is $r'_t=ct'$, a length, and the action below is integrated with $\mathrm{d}^4r=\mathrm{d}r'_t\,\mathrm{d}^3r$ so that the constant multiplying the derivative is $\hbar c$ and not $\hbar$.

Every symbol is defined where it first appears, and §*Summary of Notation* collects them.

**One convention, used throughout.** The two parts are written $\tilde\Xi_L$ and $\tilde\Xi_R$. They are not the parts of definite value. A part of definite value is an element of a right ideal of $\mathbb{B}$, and left multiplication by $\tilde\nabla_\Phi$ preserves the value, so the two sides of the first line would have different values and only the zero field would solve the pair. The parent states this; the action makes it visible, because a value-split action is identically zero (§*The Count of the Pair*).

## The Action in Element Form

The action is

$$
\boxed{\;
S=\frac{\hbar c}{2}\int\mathrm{d}^4r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\,\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\,\tilde\nabla_\Phi\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr]\;}
$$

Its two kinetic terms are diagonal in the parts and its mass term is off-diagonal. That arrangement is the two-component structure the equation itself has: each part carries its own derivative and the mass is what couples them.

**The two kinetic terms are one operator on the two parts.** The left part carries $\tilde\nabla_\Phi^{\natural}$ and the right part carries $\tilde\nabla_\Phi$, so the two differ only in the sign of the spatial derivative. In the homogeneous case both reduce to $-i\partial_{r'_t}$, and the kinetic sum collapses to $\mathrm{Im}\,\mathrm{Sc}[\tilde\Xi_L^{*}\dot{\tilde\Xi}_L+\tilde\Xi_R^{*}\dot{\tilde\Xi}_R]$. The polar companion computes that object for the word, and it is the reason the polar action has no momentum conjugate to the boost.

**The potential term is the mass, and it is the only term that couples the parts.** A kinetic term couples a part to itself; a mass term couples one part to the other. This is why the massless theory has two independent symmetries and the massive theory has one (§*The Massless Case and the Two Phases*).

**Reality, and the reason the real part is not a truncation.** Both gradients are self-adjoint for the Hermitian pairing. The temporal term is $e_t\partial_{R_t}=-i\partial_{r'_t}$; left multiplication by an imaginary unit is antisymmetric for $\mathrm{Sc}(\cdot^{*}\cdot)$, and $\partial_{r'_t}$ is antisymmetric under integration by parts, so the two signs cancel and the temporal term is self-adjoint. Each spatial term is a left multiplication by $\vec e_\eta$, which is antisymmetric, times the same antisymmetric derivative, and it is self-adjoint for the same reason. Hence

$$
\int\mathrm{d}^4r\;\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\nabla_\Phi\tilde\Xi\bigr]
=\int\mathrm{d}^4r\;\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi\bigr]\ \text{up to a boundary term},
$$

and each side is real up to a boundary term. The $i$ inside the material time is the whole of the mechanism: it is the one factor that makes the temporal term self-adjoint without disturbing the spatial ones, so all four directions agree.

**Consequence.** Each kinetic term is real up to a divergence and the mass terms are Hermitian, so the imaginary part of the bracket is a total divergence. Its integral vanishes on a closed surface, the real part carries the whole content, and nothing is lost by writing $\mathrm{Re}$ in front. This is an identity of the pairing, not a property observed on a lattice.

**The constant $\hbar c$.** It multiplies the whole action and cancels in the variation, so the residuals do not carry it while the currents carry one power of it. It is written so that the two terms have the dimension of an action and so that the derivative term is $\hbar c\,\tilde\nabla_\Phi$ and not $\tilde\nabla_\Phi$.

## Why the Pairing Is the Hermitian One

The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$, the Hermitian form, the same form the two Schrödinger articles use. The quaternion pairing $\mathrm{Sc}(\cdot^{\natural}\cdot)$ does not work, and the reason is worth stating because the symbol $\natural$ appears everywhere in the Dirac equation and the temptation to pair with it is strong.

**The quaternion pairing makes every kinetic density a total derivative.** The form $\mathrm{Sc}(X^{\natural}Y)$ is complex-bilinear and symmetric, $\mathrm{Sc}(X^{\natural}Y)=\mathrm{Sc}(Y^{\natural}X)$, and it conjugates no coefficient: $\natural$ reverses the units and leaves the central $i$ alone. So the identity

$$
\mathrm{Sc}\bigl(\tilde\Xi^{\natural}\partial_\mu\tilde\Xi\bigr)=\tfrac12\partial_\mu\mathrm{Sc}\bigl(\tilde\Xi^{\natural}\tilde\Xi\bigr)
$$

holds exactly, and multiplying by a central constant changes nothing, because the constant passes through the product and through the derivative:

$$
\mathrm{Sc}\bigl(\tilde\Xi^{\natural}i\hbar c\,\partial_\mu\tilde\Xi\bigr)=\tfrac{i\hbar c}{2}\partial_\mu\mathrm{Sc}\bigl(\tilde\Xi^{\natural}\tilde\Xi\bigr).
$$

A kinetic density that is a total derivative on every field carries no equation of motion. This is the whole defect of the $\natural$ pairing, and it is why the same symbol, used to conjugate the gradient, does not also serve to pair the action.

**The Hermitian pairing is the one the equation's own structure uses.** The two lines of the pair carry $\tilde\nabla_\Phi$ and $(\tilde\nabla_\Phi)^{\natural}$. Under $*$ these are two different operators, related by $(\tilde\nabla_\Phi)^{*}=(\tilde\nabla_\Phi)^{\natural}$, and the pairing is antilinear in its first slot, so the two slots are not interchangeable. Under $\natural$ the two are related by a conjugation of the units alone, the $i$ of the material time is untouched, and the bilinear is symmetric, which is why it cannot produce a density that is not exact. The pair's asymmetry is the $*$-pairing's asymmetry.

**Which one-sided functional is empty, and which is not.** Two candidates look alike and behave differently.

Without the $i$ the candidate is not empty. $\mathrm{Re}\,\mathrm{Sc}[\tilde\Xi^{*}\hbar c\,\tilde\nabla_\Phi\tilde\Xi]$ is real, because the gradient is self-adjoint for the pairing, and its variation is twice the residual $\tilde\nabla_\Phi\tilde\Xi$; the factor two is the absence of a $\tfrac12$ in front. So one element does carry a real first-order action, and the equation it gives is $\tilde\nabla_\Phi\tilde\Xi=0$, which is the massless member the parent writes $R$.

With the $i$ it is empty. $\mathrm{Re}\,\mathrm{Sc}[\tilde\Xi^{*}i\hbar c\,\tilde\nabla_\Phi\tilde\Xi]$ vanishes identically, because $i\hbar c\tilde\nabla_\Phi$ is anti-self-adjoint: $\langle\tilde\Xi,i\hbar c\tilde\nabla_\Phi\tilde\Xi\rangle$ is purely imaginary up to a boundary term, so its real part is zero for every field. The identity that states this correctly carries the real part on the left,

$$
\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde\Xi^{*}\partial_\mu\tilde\Xi\bigr)=\tfrac12\partial_\mu\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr),
$$

and without the real part it is false: the imaginary part of $\mathrm{Sc}(\tilde\Xi^{*}\partial_\mu\tilde\Xi)$ is a current and not a derivative. The distinction is worth keeping, because it says exactly how much has been shown. The real part of the $i$-inserted functional is a boundary term; its imaginary part is not.

**What the emptiness does and does not prove.** It does not prove that no real first-order action on one element exists. The standard Dirac action is a one-field action and is not empty, because its bilinear carries one element more than the candidate above: the Dirac adjoint's $\gamma^{0}$, which in this algebra is a right multiplication by $i\vec e_\eta$. The same repair is available here — a Hermitian right multiplier inside the bilinear makes the operator self-adjoint and the functional non-empty — and it gives the one-element equation $\tilde\nabla_\Phi\tilde\Xi=k_m\tilde\Xi$, which is one equation on one element and is not the pair.

**Therefore the split is a factorization, and the operator count is its reason.** The pair is not one operator applied once. The gradient acts on the part written $R$, the conjugated gradient acts on the part written $L$, and $k_m$ relates them. A first-order functional hosts one operator per slot, so the pair needs two slots, and the mass is the only term that can couple them, which is why it is off-diagonal. That is the variational reading of the parent's remark that the field is one element and the letters name two parts of it: the parts are what the action needs, they are not values, and the mass is what makes the two of them necessary.

## The Variation and the Pair

Vary both parts, $\tilde\Xi_p\mapsto\tilde\Xi_p+\delta\tilde\Xi_p$, and take the real part. The result is

$$
\delta S=\hbar c\,\mathrm{Re}\int\mathrm{d}^4r\;\Bigl[\mathrm{Sc}\bigl(\delta\tilde\Xi_L^{*}\,r_L\bigr)+\mathrm{Sc}\bigl(\delta\tilde\Xi_R^{*}\,r_R\bigr)\Bigr],
$$

with the two residuals

$$
r_L=(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L-k_m\tilde\Xi_R,
\qquad
r_R=\tilde\nabla_\Phi\tilde\Xi_R-k_m\tilde\Xi_L .
$$

**The coefficient, once.** Take the $\tilde\Xi_L$ kinetic term alone. Varying $\tilde\Xi_L^{*}$ gives $\tfrac{\hbar c}{2}\mathrm{Re}\int\mathrm{Sc}[\delta\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L]$; varying $\tilde\Xi_L$ gives $\tfrac{\hbar c}{2}\mathrm{Re}\int\mathrm{Sc}[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\delta\tilde\Xi_L]$, and moving the operator onto the other slot by its self-adjointness gives exactly the same expression again. The two halves add, the $\tfrac12$ cancels, and the coefficient is $\hbar c$ with the residual as the bracket. The $\tfrac12$ in the action is put there exactly so that the coefficient comes out $\hbar c$ and not $2\hbar c$, and the factor that a naive count of the two halves suggests is the one it removes.

**Why this gives eight equations and not sixteen.** The two residuals are elements of $\mathbb{B}$, and each has eight real components, so the pair is sixteen real equations on sixteen real unknowns. That is the count the parent's pair has. It is not an overdetermination, because the two lines are not independent on solutions: applying $(\tilde\nabla_\Phi)^{\natural}$ to the first and using the second gives the Klein–Gordon equation, $(\Box_\Phi-k_m^{2})\tilde\Xi_R=0$, which is the compatibility condition rather than a further equation.

**Stationarity is the pair.** The pairing $\mathrm{Re}\,\mathrm{Sc}(\delta\tilde\Xi^{*}\,\cdot)$ is non-degenerate on the eight real directions of $\mathbb{B}$, so the vanishing of $\delta S$ for every variation is exactly $r_L=r_R=0$. No boundary term appears when the variation has compact support, and none appears when the fields are periodic in the spatial directions.

**The massless limit is two independent equations.** At $k_m=0$ the residuals decouple, $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=0$ and $\tilde\nabla_\Phi\tilde\Xi_R=0$, and the action is a sum of two independent functionals. Each is a one-sided functional on its own part, and each is not empty. The contrast with the candidate rejected in §*Why the Pairing Is the Hermitian One* is exactly the $i$: without it the one-sided functional is real and its variation is the residual, and it is only the extra $i\hbar c$ that makes the operator anti-self-adjoint and the functional empty.

## The Count of the Pair

Three counts must be kept apart, and the action keeps them apart.

**One element has four complex coefficients**, that is eight real numbers, which is the count of the four-component column. This is the field's count and the parent's count.

**The pair at fixed momentum has four complex solutions.** Write a plane wave $\tilde\Xi_{L,R}=\tilde\Xi^{L,R}_0e^{i\theta}$; the pair becomes $i\tilde K_\Phi\tilde\Xi^{R}_0=k_m\tilde\Xi^{L}_0$ and $i\tilde K_\Phi^{\natural}\tilde\Xi^{L}_0=k_m\tilde\Xi^{R}_0$. Substituting the first into the second gives $N(\tilde K_\Phi)=-k_m^{2}$ and leaves $\tilde\Xi^{R}_0$ free. So the solution space is four complex dimensional: the first line reads $\tilde\Xi^{L}_0=k_m^{-1}i\tilde K_\Phi\tilde\Xi^{R}_0$, and the second is then satisfied by the mass shell alone.

**The action's two parts are not twice the field.** The count is the same four complex, because the first line determines $\tilde\Xi_L$ from $\tilde\Xi_R$. The action is a functional of two elements, but its stationary points are parametrised by one element's worth of data. The split is a device of the action, not an enlargement of the carrier.

**What the value-split would do.** If the parts were taken as $\tilde\Xi\Pi_\pm$ with $\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ the frame's idempotents, the mass term would vanish identically: $\mathrm{Sc}[\Pi_+\tilde\Xi^{*}\tilde\Xi\Pi_-]=0$ because $\Pi_-\Pi_+=0$ and $\mathrm{Sc}$ is cyclic. The vanishing is the identity $\mathrm{Sc}[\tilde\Pi_+\tilde X^{*}\tilde X\tilde\Pi_-]=0$, since the product $\tilde\Pi_-\tilde\Pi_+$ is zero and $\mathrm{Sc}$ is cyclic. The kinetic terms survive such a split, the mass does not. The parent's display with the fixed direction $i\vec v$ in the mass term is the repair, and the polar companion uses it.

## The Massless Case and the Two Phases

At $k_m=0$ the action has two independent phase symmetries,

$$
\tilde\Xi_L\mapsto e^{i\alpha}\tilde\Xi_L,
\qquad
\tilde\Xi_R\mapsto e^{i\beta}\tilde\Xi_R,
$$

with $\alpha$ and $\beta$ independent central angles. The sum $\alpha=\beta$ is the electric phase; the difference is the chiral phase. For $k_m\ne0$ the mass term carries $\tilde\Xi_L^{*}\tilde\Xi_R$ and its conjugate, both invariant under the sum and neither invariant under the difference, so the chiral symmetry is broken by the mass and by nothing else.

**The chiral current is the difference of the two part-currents**, and it is conserved exactly when $k_m=0$. The article does not derive it: it is the same Noether computation as the electric one with the two signs opposite, and its conservation is the statement that the mass term is the only obstruction.

**One caution.** The chiral symmetry of this action is a symmetry of the two-part functional. Whether it is a symmetry of the parent's equation read as a single equation is the same question as whether the split is canonical, and the answer is not needed here.

## The Noether Currents

Three symmetries are available, and two of them are standard.

**The electric current.** Under $\tilde\Xi_{L,R}\mapsto e^{i\alpha}\tilde\Xi_{L,R}$ with $\alpha$ constant, the Lagrangian is invariant: the phase cancels inside each kinetic term and inside the mass term. The Noether current is

$$
J^{t}=\mathrm{Re}\,\mathrm{Sc}\bigl[\tilde\Xi_L^{*}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\Xi_R\bigr],
\qquad
J^{\eta}=\mathrm{Re}\,\mathrm{Sc}\bigl[i\bigl(\tilde\Xi_R^{*}\vec e_\eta\tilde\Xi_R-\tilde\Xi_L^{*}\vec e_\eta\tilde\Xi_L\bigr)\bigr],
$$

with conservation $\partial_\mu J^{\mu}=0$ on solutions, by the standard argument: the variation of the action under a local angle is $-\int(\partial_\mu\alpha)J^{\mu}$ plus the equations of motion.

**The two components have different structures and both are right.** The time component is a sum over the parts; the spatial component is a difference. The difference is not an error: the two parts carry conjugate spatial derivatives, $-\vec e_\eta\partial_\eta$ on the left and $+\vec e_\eta\partial_\eta$ on the right, and the current inherits that relative sign. In the two-component language this is the statement that one part uses $\bar\sigma$ and the other $\sigma$.

**The polar reading of the same numbers.** Take the parent's polar field $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and evaluate the same two components with the two-part combinations replaced by their one-element counterparts: the sum $\tilde\Xi_L^{*}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\Xi_R$ by $\tilde\Xi^{*}\tilde\Xi$, and the difference $\tilde\Xi_R^{*}\vec e_\eta\tilde\Xi_R-\tilde\Xi_L^{*}\vec e_\eta\tilde\Xi_L$ by $\tilde\Xi^{*}\vec e_\eta\tilde\Xi$. The result is

$$
J^{t}=\rho\cosh\theta_{\mathrm{rpd}}=\rho\gamma,
\qquad
J^{\eta}=\rho\sinh\theta_{\mathrm{rpd}}\,u_{\mathrm b,\eta}=\rho\gamma\,\frac{v_\eta}{c},
$$

which is the polar parent's current $\tilde J_\Phi=\rho\tilde V_\Phi$ divided by $ic$. The time component is an identity of the word: $\tilde U_{\Psi,\mathrm b}^{\natural}\tilde U_{\Psi,\mathrm b}=\cosh^{2}\tfrac{\theta_{\mathrm{rpd}}}{2}+\sinh^{2}\tfrac{\theta_{\mathrm{rpd}}}{2}=\cosh\theta_{\mathrm{rpd}}$, so $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=r^{2}\cosh\theta_{\mathrm{rpd}}=\rho\gamma$, and the same line gives the spatial component once the boost axis is identified with the direction of $\tilde V_\Phi$, which is the polar article's own identification.

**The two readings agree in the time component and differ in the spatial one, and that is a limitation of this derivation.** The action's own Noether current is the two-part display above, and it is conserved on solutions whatever the reading. What the action does not do is decide which object of the algebra the physical current is. The two-part display and the one-element reading differ in the spatial component by the relative sign of the chiral split, and nothing in the variational derivation chooses between them. A derivation that fixed the answer would have to state what the two parts are as functionals of one field; no such statement is made here, and none is available to the author. So the current of this article is conserved and, in its spatial component, one of two objects: the action fixes its conservation and not its identification. That is weaker than a variational derivation usually delivers, and it should be read as the limit of what this action can settle.

**Energy and momentum.** The Lagrangian does not depend on the coordinates explicitly, so translation in $r'_t$ and in the three $r_\eta$ gives four conserved charges. The canonical expressions are

$$
T^{\mu}{}_{\nu}=\sum_{p}\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_p^{*}\,s_\mu e_\mu\,\partial_\nu\tilde\Xi_p\Bigr]-\delta^{\mu}_{\nu}\,\mathcal{L},
\qquad
E=T^{t}{}_{t},
$$

with $\mathcal{L}$ the integrand of the action. Its conservation on solutions is the statement that the generator does not depend on the coordinate, and it is the Noether statement of the constant setting. The symmetric improvement of this tensor, and its agreement with the stress tensor computed from the operator, are the *Quantum Stress Tensor* article's subject and are not derived here.

**What is deliberately absent.** There is no spin current in this section. The spin of this field is the rotor's (§*the polar companion*), it is not a Noether current of the element action, and a "spin current" derived here would be a second derivation of something the polar form already states exactly. The Dirac spin current as a Noether current belongs to the polar article, where the rotor is a variable.

## The Two-Sided Form Has No Action of Its Own

The parent writes a second display of the same equation, in which the mass acts on the right,

$$
\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L i\vec v,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R i\vec v,
$$

with $\vec v$ a fixed unit spatial direction. That display has no action of its own, and the reason is structural rather than technical.

**The two displays are one equation.** Right multiplication by a constant unit is invertible and commutes with $\tilde\nabla_\Phi$, so the second display is the first composed with a fixed element on the right of each part: $\tilde\Xi\mapsto\tilde\Xi i\vec v$ carries the boxed pair into the display above. Two displays related by an invertible constant change of the field's right frame are one equation, and one equation has one action.

**The range of that argument, stated exactly.** It applies to a change of variable that is complex-linear, and $i\vec v$ is central and constant, so it applies here. It does not apply to the dictionary of the parent's §*An Explicit Dictionary with Conjugation in the Mass Term*, whose mass term carries a coefficient conjugation: that change of variable is a right multiplication composed with an antilinear map, and an antilinear map does not commute with $\tilde\nabla_\Phi$ in the same way. The conjugated display is still not a second equation, but the reason is different: it is the same functional read through a conjugation, and the reality of the action is what makes the two readings agree. The claim of this section is made for the display with $i\vec v$ and for that display only.

**What the direction does.** In the two-sided display the letters can be read as values, because right multiplication by $i\vec v$ with $\vec v\perp\vec e_z$ reverses the value and the two sides then agree in value. That reading is available in the display and it is not available in the boxed pair. The action above is written for the boxed pair, where the letters are parts and not values; the value-reading needs the direction, and the direction is what the two-sided display supplies.

**The price of the value-reading.** A fixed direction is an extra datum. The action of this article carries none, and it is therefore the version to use when the frame is not already declared. When the frame is declared — as it is in the polar form, where $\vec e_z$ is the direction of the value test — the direction costs nothing, and the polar companion takes the value-reading.

## What the Variational Principle Adds

The honest ledger, as in the Schrödinger companion.

**Adds.** A compact statement of the pair as one variation. The two currents of the electric symmetry and the four of translation, in one derivation. The reason the split is a factorization rather than a convenience: the pair carries two operators, a first-order functional gives each operator one slot, and the one-sided functional in the same pairing is empty. The proof is the self-adjointness of the gradient; it excludes the one-element reading of the pair without excluding one-element actions in general. The proof that the mass term is the only coupling, hence that the chiral symmetry is broken by the mass alone.

**Relabels.** No new prediction: the pair is the parent's. No new solution: the plane waves are the parent's, and the mass shell is the parent's. The action is the standard Dirac action written in the algebra, with the two-component structure that the algebra's derivative forces.

**What is genuinely different from the Schrödinger case.** There the action is one term on one element and the equation is second order in space and first in time. Here the action is four terms on two elements and the equation is first order in both. The difference is not a choice of notation: it is what makes the split mandatory and what makes the mass a coupling rather than a potential.

**One integral, one local.** The action is a functional on the whole field configuration and its Euler–Lagrange equations are local differential equations. The variational form is not opposed to the equation; it is equivalent to it, and it delivers the currents in the same step.

## Open Questions

1. **Which reading of the current is physical.** That the current's spatial component is ambiguous is recorded in §*The Noether Currents* as a limitation of this derivation. The question that remains is the physical one: which element of the algebra the measured current is. It is not a question about conservation, which holds in both readings. An answer would have to state the two parts as functionals of one field, and the author knows of no such statement.

2. **The operator setting.** The action is written for a constant Hamiltonian, where the propagator is a closed form. With an operator Hamiltonian the same functional exists, but whether the two parts stay in $\mathbb{B}$ under a non-central potential is the parent's closure question, and the action inherits it.

3. **The path integral.** The action is the extremum's object; the path integral is the sum over configurations. The two are different objects and the second is not attempted here.

## Summary

The Dirac equation of this corpus is a pair, $\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L$ and $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R$, with $k_m=mc/\hbar$. Its action is

$$
S=\frac{\hbar c}{2}\int\mathrm{d}^4r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_\Phi\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

two diagonal kinetic terms and one off-diagonal mass. Its variation is the pair, with residuals $r_L=(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L-k_m\tilde\Xi_R$ and $r_R=\tilde\nabla_\Phi\tilde\Xi_R-k_m\tilde\Xi_L$ and coefficient $\hbar c$, the $\tfrac12$ of the action cancelling against the two halves of each kinetic term. Its imaginary part is a total divergence, because both gradients are self-adjoint for the pairing, so the real part carries the whole content.

The pairing is the Hermitian one, $\mathrm{Sc}(\cdot^{*}\cdot)$, and the self-adjointness is the reason: the $i$ in the material time is what makes the temporal term Hermitian and lets the four directions agree. The quaternion pairing is bilinear and symmetric, so every kinetic density built from it is a total derivative and the functional is empty. The one-sided functional with $i\hbar c$ in the same pairing is empty for the same reason in another form, $i\hbar c\tilde\nabla_\Phi$ being anti-self-adjoint; without the $i$ it is real and non-empty and gives the massless member. The split into two parts is therefore a factorization forced by the two operators of the pair, one per slot, with the mass the only coupling between them.

The mass term is the only coupling of the parts, so the massless action has two independent phases and the mass breaks the difference. The electric current is a sum in its time component and a difference in its spatial one, because the two parts carry conjugate spatial derivatives; in the one-element reading its time component is exactly $\rho\gamma$, which is the polar parent's $\rho\tilde V_\Phi$ divided by $ic$; its spatial component agrees with the polar current once the boost axis is identified with the velocity, and the two readings differ there by the relative sign of the chiral split, which the action does not settle.

The two-sided display is the same equation in a different right frame — a constant right multiplication by $i\vec v$ — and has no action of its own. The argument covers that display and not the dictionary whose mass term carries a conjugation, which is the same functional read through an antilinear map. Its direction is what makes the value-reading of the letters available, and the price of that reading is the direction.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $*$ | Hermitian conjugation, $\tilde X^{*}=\bar{\tilde X}^{\natural}$ |
| $\natural$ | Quaternion conjugation; $\tilde U^{\natural}=\tilde U^{-1}$ for a unit |
| $\mathrm{Sc}$, $\mathrm{Tr}=2\,\mathrm{Sc}$ | Scalar part; trace |
| $\tilde\nabla_\Phi=e_t\partial_{R_t}+\vec e_\eta\partial_\eta$ | Biquaternionic gradient, $R_t=ir'_t$ |
| $(\tilde\nabla_\Phi)^{\natural}$ | The same gradient with the spatial part reversed |
| $\Box_\Phi=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi$ | D'Alembertian |
| $r'_t=ct'$ | Material time, a length |
| $\tilde\Xi=\tilde\Xi_L+\tilde\Xi_R$ | The field, one element of $\mathbb{B}$; the letters name two parts, not two values |
| $k_m=mc/\hbar$ | Mass wave number |
| $S$ | The action; $\mathcal{L}$ its integrand |
| $r_L,r_R$ | The two residuals, whose vanishing is the pair |
| $J^{\mu}$ | Electric Noether current |
| $T^{\mu}{}_{\nu}$ | Canonical energy-momentum |
| $\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | Frame idempotents; $\Pi_\pm^{*}=\Pi_\pm$, $\Pi_\pm^{\natural}=\Pi_\mp$, $\Pi_+\Pi_-=0$ |
| $\vec v$ | The fixed unit direction of the two-sided display |

## Further Reading

- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the pair, the two-sided display, and the operator $\mathcal{N}$ whose square is the wave operator.
- [The Dirac Equation in Biquaternionic Polar Variables](the-dirac-equation-in-biquaternionic-polar-variables.html), for the polar word, the four brackets, the current and the spin.
- [The Variational Principle and the Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-dirac-equation-in-biquaternionic-polar-variables.html), the companion, for the same action substituted with the word.
- [The Variational Principle and the Schrödinger Equation in Biquaternionic Form](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-form.html), for the second-order case, where the split is not forced.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), for the symmetric improvement of $T^{\mu}{}_{\nu}$ and its conservation.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, §8, for the tensor formulation of the same variational principle, whose unit-vector constraints need Lagrange multipliers.
- Julian Schwinger, "The theory of quantized fields I," *Physical Review* **82** (1951) 914, for the action principle in the fermionic case.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the standard action and its symmetries.
