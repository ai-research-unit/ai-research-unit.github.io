# __The Non-Quantum Limit of the Free Proca Equation using the Variational Principle__

## Introduction

**The limit taken on the action, and what the action adds that the equation's route cannot.** The companion *The Non-Quantum Limit of the Free Proca Equation* reads the three groups of the exact identity and takes the limit by contraction. This article takes the same limit on the action of *The Variational Principle and the Proca Equation in Biquaternionic Polar Variables*, and the gain is of a specific kind: **the action's own term count is the criterion**, so no sensitivity argument is needed, and the two equations that survive are the two variations rather than the two parts of one identity.

**The obstruction is the same one, and it appears in the same place.** The parent's chart is the modulus and the frame, and the parent's action in that chart is a function of the modulus and its gradients. **A criterion written on those variables is of order one on the parent's own solutions**, by the argument the companion gives: the parent's plane wave has $r=r_0\lvert\cos\theta_{\mathrm{pwp}}\rvert$ and its criterion is $\lvert\tan\theta_{\mathrm{pwp}}\rvert$. This article therefore takes the action on a mode, as the companion does, and its first two sections are the statement of that necessity in the action's language rather than the equation's.

**What the article establishes, in five sentences.** On a mode the action splits into three groups of orders $\epsilon^{-2}$, $\epsilon^{-1}$ and $\epsilon^{0}$, and the truncation deletes exactly the third. The truncated action is **algebraic in the amplitude** and quadratic in the phase's gradient, so its variation with respect to the amplitude is the order-$\epsilon^{-2}$ group and its Hessian is minus the Proca symbol, whose determinant is $-k_m^{2}(k^{2}-k_m^{2})^{3}$ and whose rank on the shell is one. Its variation with respect to the phase is the transport equation, and it is the Noether charge of the amplitude–phase redundancy of the decomposition — **the transport equation is a Gauss law and not an extra equation**. The amplitude consequently stops being dynamical: four primary constraints, $p_a=0$, replacing the parent's rank-three Hessian, and the amplitude is reduced on shell to the three-dimensional Lorenz plane. The inversion is two-valued, because the truncated action is quadratic in $\omega$.

**Notation.** As in the companion: $\tilde A_\Phi=ie_t a'_t+\vec e\cdot\vec A$ real, the interval $v^{2}=v'^{2}_t-\lvert\vec v\rvert^{2}$, the sector norm its negative, $A_\mu=\mathrm{Re}(a_\mu e^{i\theta})$, $k_\mu=\partial_\mu\theta=(\omega/c,\vec k)$, $k_m=mc/\hbar$, and $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r'^{2}_{t}$ with $\partial/\partial R_t=-i\,\partial/\partial r'_t$.

## The Action in the Chart, and the Same Obstruction

**The parent's action, in the element form and in the chart.**

$$
S[\tilde A_\Phi]=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^{2}\langle\tilde A_\Phi\rangle_\natural\Bigr],
\qquad
\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^{2}\Bigr]-\tfrac12 S^{2},
$$

with $S=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)$ the divergence. **The parent's cleanest new statement is the mass term's sign**: in the chart the mass term is $+\tfrac12k_m^{2}r^{2}$ on the timelike branch and $-\tfrac12k_m^{2}r^{2}$ on the spacelike one, so the sign of the mass term **is** the branch, and the causal character of the four-vector is read as a sign in the action.

**The parent's structural numbers, which this article inherits.** The chart has four parameters and four equations, no Lagrange multiplier is needed for the normalisation of the frame because the word is exact, the Hessian has **rank three out of four**, and the single constraint is the standard one of a massive vector field. **The contrast the parent draws with the first-order companions is the one that matters here**: the Schrödinger polar action is first order, six of its eight momenta vanish identically, and its closure needs Dirac analysis; this action is second order and its Hessian is nearly regular.

**And yet the chart cannot be expanded, for a reason that is in the action and not only in the equation.** The action's chart variables are $r$ and the frame, and the fast variation of a solution sits in $r$. **The parent's own dispersion, $k'^{2}_t=\lvert\vec k_\Phi\rvert^{2}+k_m^{2}$, is obtained from the scale equation $(\Box_\Phi-k_m^{2})r+r\sum_\mu\mathrm{Sc}(\Gamma_\mu^{2})=0$ with a constant frame and a cosine modulus**, which is the statement that the phase information is in the modulus. There is no term of that action which is small on a solution, so there is no group to delete, and a truncation written on the chart would delete the solution.

**The mode is therefore the action's variable and not an alternative to it.** Substituting $A_\mu=\mathrm{Re}(a_\mu e^{i\theta})$ into the parent's action is a change of variables on the carrier, exact, and the piecewise branch structure disappears with it: the branch was a property of a real four-vector's sign of norm, and a mode has no such sign to read.

## The Action on the Mode

**The substitution and the leading form.** With $\tilde F$ carrying $i(k_\mu a_\nu-k_\nu a_\mu)e^{i\theta}$ at leading order, the parent's action becomes

$$
S=\int d^{4}r\;\Bigl[\tfrac12\bigl(\lvert k\cdot a\rvert^{2}-k^{2}\lvert a\rvert^{2}\bigr)+\tfrac12\,k_m^{2}\lvert a\rvert^{2}\Bigr]+\text{(terms with one derivative of }a\text{)}+\text{(terms with two)},
$$

with $\lvert a\rvert^{2}=a_\nu\bar a^{\nu}$ and $k\cdot a=k_\mu a^{\mu}$. **The three groups of the action are the three groups of the identity**, and the correspondence is one-to-one because the identity is the variation of this action term by term.

**What the leading group says, and the indefiniteness it keeps.** The leading density $\tfrac12\bigl(\lvert k\cdot a\rvert^{2}-k^{2}\lvert a\rvert^{2}+k_m^{2}\lvert a\rvert^{2}\bigr)$ is quadratic in $a$, carries no derivative of $a$, and its mass term is $\tfrac12k_m^{2}\lvert a\rvert^{2}$ — **indefinite**, because $\lvert a\rvert^{2}$ is indefinite for a complex four-vector. The parent's "the sign of the mass term is the branch" survives the limit in this form and is not repaired by it: **the positivity of the energy is a property of the field's own bilinear and appears at the next order, not at this one.**

**The truncation, stated as a deletion of a group.** Dropping the two-derivative group leaves

$$
S_{\mathrm{trunc}}=\int d^{4}r\;\tfrac12\Bigl[\lvert k\cdot a\rvert^{2}-\bigl(k^{2}-k_m^{2}\bigr)\lvert a\rvert^{2}\Bigr],
$$

**algebraic in $a$ and first order in nothing**: it contains $a$ and $\partial\theta$, and no $\partial a$. That is the whole of the truncation, and the companion's second and third groups are its Euler–Lagrange shadow.

**Why this group is the one to drop, on the action's own terms.** Its size is $\lvert a\rvert^{2}/L^{2}$ against the leading $\lvert a\rvert^{2}k^{2}$, so the ratio is $\epsilon^{2}$; and it is a functional of $a$ alone, with no $\theta$ in it, so **dropping it cannot break any symmetry of the phase** — the argument the Klein–Gordon variational article makes, and it holds here for the same reason. A truncation that dropped the $\lvert k\cdot a\rvert^{2}$ term instead, keeping the derivatives, would break the redundancy the next section exhibits.

## The Truncated Action's Two Variations

**The amplitude's variation is the order-$\epsilon^{-2}$ group.**

$$
\frac{\delta S_{\mathrm{trunc}}}{\delta\bar a^{\nu}}=0
\qquad\Longleftrightarrow\qquad
(k^{2}-k_m^{2})a^{\nu}-k^{\nu}(k\cdot a)=0 .
$$

**And its Hessian is minus the Proca symbol.**

$$
\frac{\partial^{2}S_{\mathrm{trunc}}}{\partial\bar a^{\mu}\,\partial a^{\nu}}=k_{\mu}k_{\nu}-\bigl(k^{2}-k_m^{2}\bigr)\eta_{\mu\nu}=-\sigma_{\mu\nu},
\qquad
\det\bigl(-\sigma\bigr)=-k_m^{2}\bigl(k^{2}-k_m^{2}\bigr)^{3}.
$$

**So the Fourier article's symbol is the truncated action's Hessian**, and every number that article computes is a property of this Hessian: the eigenvalues $\{k^{2}-k_m^{2},k^{2}-k_m^{2},k^{2}-k_m^{2},-k_m^{2}\}$, measured at $k=(1.30,0.50,-0.30,0.20)$ with $k_m^{2}=0.49$ as $-0.49$ and $0.82$ three times; the determinant $-0.27017032$ against the formula's $-0.27017032$; and on the shell the rank one that makes the kernel three-dimensional. **The variational route does not need the Fourier article to obtain the count, and it obtains the same count**: it differentiates its own truncated action.

**The phase's variation is the transport equation, and it is a Noether charge.**

$$
\frac{\delta S_{\mathrm{trunc}}}{\delta\theta}=0
\qquad\Longleftrightarrow\qquad
\partial_\mu\bigl(\lvert a\rvert^{2}k^{\mu}\bigr)=0 .
$$

**The reason is the decomposition's redundancy, and it is exact at every order.** Shifting $\theta$ by a constant and rotating $a$ by $e^{-i\alpha}$ leaves the field $A_\mu$ unchanged, so the identity $\theta\to\theta+\alpha$ with $a$ fixed is a symmetry of the full action in the mode's variables; the truncated action depends on $\theta$ only through $k=\partial\theta$, so the symmetry is retained exactly; and its Noether charge is $\lvert a\rvert^{2}k^{\mu}$, which is the companion's transport current. **The transport equation is therefore a Gauss law of the decomposition and not an additional dynamical equation**, which is why it survives a truncation that deletes all the amplitude's derivatives: it never needed them.

**Read the two variations together and the structure is the same as the Klein–Gordon pair's.** One variation gives the Hamilton–Jacobi-type equation; the other gives the conservation of a current that the first-order structure supplies for free. **What is new here is only that the amplitude is a vector**, so the first variation is a four-component algebraic system with a kernel instead of a single scalar condition.

## The Amplitude Stops Being Dynamical

**The truncation is singular, and the singularity is the family's largest statement.** Because $S_{\mathrm{trunc}}$ contains no derivative of $a$, all four momenta conjugate to the amplitude vanish,

$$
p_{a^\nu}=\frac{\partial\mathcal{L}_{\mathrm{trunc}}}{\partial(\partial_{t'}a^{\nu})}=0 ,
$$

and the amplitude is determined algebraically instead of dynamically. **This is the Klein–Gordon article's singularity written for a vector**: there one momentum vanished, $p_r=0$, and the consistency condition was the eikonal; here four vanish, and the consistency conditions are the four components of the amplitude's equation.

**What the four algebraic equations amount to, read through the rank.** Off the shell the Hessian $-\sigma$ has rank four, so the only solution is $a=0$: **there is no propagation off the shell at all**, and the eikonal is the condition for the algebraic system to have a non-trivial solution. On the shell the rank falls to one, three of the four equations are dependent, and the solution set is the three-dimensional Lorenz plane. **So the limit does not merely allow the three polarisations; it makes them the kernel of a matrix, which is what a polarisation is.**

**The phase is the only dynamical field that remains.** Its momentum is $p_\theta=\partial\mathcal{L}_{\mathrm{trunc}}/\partial(\partial_{t'}\theta)=\lvert a\rvert^{2}k_{t}$, the density times the frequency, and the eikonal is a first-order equation for it. **The limit demotes the amplitude to a polarisation and promotes the phase to the only degree of freedom**, and that division is the same one the Klein–Gordon, Schrödinger and Dirac pairs deliver with a scalar and a spinor in place of a vector.

## The Constraint Count and the Comparison Across Families

**Before and after the limit, the physical count is three, and the bookkeeping moves.**

| | parent | truncated |
| --- | --- | --- |
| Hessian | rank three of four | $-\sigma$; rank four off shell, one on shell |
| vanishing momenta | none | four, $p_{a}=0$ |
| amplitude's status | dynamical, second order | algebraic, polarisation only |
| count on shell | three | three |

**The parent's rank-three Hessian is the standard massive-vector constraint, and the truncation's four vanishing momenta are a stronger degeneracy of the same count.** The parent says, correctly, that its action is second order and that no momentum vanishes identically; the truncated action is the one in which none of the amplitude's momenta survives. **The two statements do not conflict, because they are statements about different actions**, and the article's contribution is to have exhibited the second.

**The comparison with the three other families, stated as their constraint behaviour.**

| family | the limit's action | what the limit does to the constraints |
| --- | --- | --- |
| Schrödinger | first order | completes a constraint already half-present |
| Klein–Gordon | second order in $r$ | creates one, $p_r=0$ |
| Dirac | first order, linear in the velocities | creates none; changes nothing |
| Proca | second order in $A$, algebraic after truncation | creates four, $p_a=0$, and keeps the count |

**The fourth row is the family's own**, and its distinguishing feature is that the number of constraints created equals the dimension of the amplitude: one for a scalar, four for a vector, and the physical count is untouched in both cases because the amplitude was never the dynamical field.

## The Inversion Is Two-Valued

**The truncated action is quadratic in $\omega$, so its Legendre transform is two-valued.** $S_{\mathrm{trunc}}$ contains $k^{2}$ with $k_{t}=\omega/c$, so solving the eikonal for the frequency gives

$$
\omega=\pm\,c\sqrt{\lvert\vec k\rvert^{2}+k_m^{2}} .
$$

**Both roots are kept, and neither is a defect**: they are the mode's two frequency branches, the same two sheets the companion's eikonal delivers, and the parent's evenness result, $\sigma(-\tilde K_\Phi)=\sigma(\tilde K_\Phi)$, is their frequency-space statement.

**The contrast with the first-order families is a matter of degree and not of interpretation.** A first-order theory's form is linear in $\omega$ and its inversion is single-valued; the Dirac variational companion's inversion is of that kind. **The Proca form is degree two, so its inversion is degree two**, and the article states the degree rather than the analogy.

**What the two-valuedness does not do is select a sheet.** The constraint $k_m^{2}(k\cdot a)=0$ is independent of $\omega$ at both roots, so it cannot choose between them, and neither can the transport equation, which is a conservation law on either sheet. **A selection would need an initial condition**, which is the statement that the limit delivers a family and not a solution.

## What the Variational Route Adds

**Adds.**

- The criterion as a comparison of the action's own terms, so that the sensitivity argument of the substitution route is not needed: the ratio of the dropped group to the kept one is $\epsilon^{2}$ and that is the whole of it.
- The identification of the truncated action's Hessian with the Proca symbol, and therefore of the count with a rank.
- The transport equation as the Noether charge of the decomposition's redundancy, hence as a Gauss law rather than an independent equation.
- The statement that the amplitude is non-dynamical after truncation, with the count of four vanishing momenta and the comparison across the four families.
- The two-valued inversion, with the reason being the action's degree in $\omega$.

**Does not add.**

- No new solution and no new prediction: the truncated action is the parent's action written on a mode and cut at a stated order.
- No handling of the field term's normalisation, which is the element-form companion's open question and which this article uses as given.
- No statement about the branch structure of the parent's real chart, which the mode's variables do not have.

**The distinction that matters.** The equation's route and the action's route deliver the same three objects; the action's route says **why** each survives. The eikonal is a variation, the transport is a Noether charge, and the remainder is a group whose deletion is legitimate because it carries no phase.

## Summary

The parent's action in the modulus-and-frame chart cannot be expanded, for the reason the companion gives: the fast variation of a solution is in the modulus, and the criterion on the parent's own plane wave is $\lvert\tan\theta_{\mathrm{pwp}}\rvert$. Taken on a mode, $A_\mu=\mathrm{Re}(a_\mu e^{i\theta})$, the action splits into groups of orders $\epsilon^{-2}$, $\epsilon^{-1}$ and $\epsilon^{0}$, and the truncation deletes the last, which is legitimate because that group is a functional of $a$ alone and carries no phase.

The truncated action, $\int\tfrac12[\lvert k\cdot a\rvert^{2}-(k^{2}-k_m^{2})\lvert a\rvert^{2}]$, is algebraic in the amplitude. Its amplitude variation is the order-$\epsilon^{-2}$ group and its Hessian is minus the Proca symbol, with eigenvalues $\{k^{2}-k_m^{2},k^{2}-k_m^{2},k^{2}-k_m^{2},-k_m^{2}\}$, determinant $-k_m^{2}(k^{2}-k_m^{2})^{3}$ and rank one on the shell. Its phase variation is $\partial_\mu(\lvert a\rvert^{2}k^{\mu})=0$, the Noether charge of the amplitude–phase redundancy of the decomposition, so the transport equation is a Gauss law. The truncation is singular — four primary constraints $p_a=0$ — and the amplitude is thereby demoted to a polarisation while the phase becomes the only dynamical field. The count is three before and three after, and the number of constraints created equals the dimension of the amplitude: one for a scalar, four for a vector. The inversion is two-valued because the action is quadratic in $\omega$, and both roots are kept.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $S[\tilde A_\Phi]=\int\bigl[\tfrac12\mathrm{Re\,Sc}(\tilde F\tilde F)-\tfrac12k_m^{2}\langle\tilde A_\Phi\rangle_\natural\bigr]$ | The parent's action |
| $+\tfrac12k_m^{2}r^{2}$ / $-\tfrac12k_m^{2}r^{2}$ | The mass term's sign as the branch: timelike / spacelike |
| $A_\mu=\mathrm{Re}(a_\mu e^{i\theta})$ | The mode; $a_\mu$ complex, $\theta$ fast |
| $\tfrac12\bigl(\lvert k\cdot a\rvert^{2}-k^{2}\lvert a\rvert^{2}+k_m^{2}\lvert a\rvert^{2}\bigr)$ | The order-$\epsilon^{-2}$ density |
| $S_{\mathrm{trunc}}=\int\tfrac12\bigl[\lvert k\cdot a\rvert^{2}-(k^{2}-k_m^{2})\lvert a\rvert^{2}\bigr]$ | The truncated action; algebraic in $a$ |
| $-\sigma_{\mu\nu}=k_\mu k_\nu-(k^{2}-k_m^{2})\eta_{\mu\nu}$ | The truncated action's Hessian |
| $\det(-\sigma)=-k_m^{2}(k^{2}-k_m^{2})^{3}$ | The Hessian's determinant; the count |
| $p_{a^\nu}=0$ | The four primary constraints the truncation creates |
| $p_\theta=\lvert a\rvert^{2}k_t$ | The phase's momentum; the only dynamical one |
| $\partial_\mu(\lvert a\rvert^{2}k^{\mu})=0$ | The transport equation as a Gauss law |
| $\omega=\pm c\sqrt{\lvert\vec k\rvert^{2}+k_m^{2}}$ | The two sheets; the two-valued inversion |
| $\epsilon=1/(k_\Phi L)$ | The criterion; the ratio of the dropped group to the kept one, squared |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the equation and its constraint.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the analysis of constrained systems whose momenta vanish identically.
- Ludwig D. Faddeev and Victor N. Popov, "Feynman diagrams for the Yang–Mills field," *Physics Letters B* **25** (1967) 29–30, for the treatment of a Gauss law as the conservation of a redundancy rather than as an equation of motion.
- G. B. Whitham, *Linear and Nonlinear Waves* (Wiley, 1974), chapter 11, for the averaged Lagrangian of a real wave and the algebraic amplitude it produces.
- Michael V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the relation between the truncated action's variations and the eikonal and transport equations.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), §3-2, for the massive vector field's constraint structure and the singular massless limit.
