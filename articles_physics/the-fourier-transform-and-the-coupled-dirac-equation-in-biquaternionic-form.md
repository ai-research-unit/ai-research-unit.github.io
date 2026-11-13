# __The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Form__

## Introduction

**The coupled equation adds one term to the Dirac operator, and this article asks what the transform does to that term.** *The Coupled Dirac Equation in Biquaternionic Form* replaces the gradient with $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi$. The first summand is a derivative and the second is a multiplication, and the transform treats the two differently. Everything below is the reading of that difference.

**The finding is a classification of one term by its order.** The coupling acts as a multiplier in momentum space exactly when $\tilde A_\Phi$ is constant. A linear $\tilde A_\Phi$ gives a first-order differential operator. A general $\tilde A_\Phi$ gives a convolution, which is an integral operator of no finite order. The three cases are one ladder, and the ladder is the article.

**The ladder has a gauge-invariant floor.** A gauge in which $\tilde A_\Phi$ is constant exists exactly when the field strength vanishes, because a constant connection is a gradient and a connection is a gradient exactly when its field strength vanishes. So the multiplier case is the zero-curvature case, and the first case that no gauge can remove is the linear one. **That is why the linear bench is the interesting one**: it is the first coupling that is genuinely an operator rather than a multiplier.

**The shift of the wave number is a translation and not an addition.** At constant $\tilde A_\Phi$ the covariant wave number element is $\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi$, and its quaternionic norm is $\langle i\tilde K_{\Phi,\mathrm{gco}}\rangle_\natural=p'^{2}/\hbar^{2}$ with $p'$ the kinetic four-momentum. A translation of a variable cannot change the quadratic form's shape, only its origin, and the numerical check confirms that the naive sum of the two norms misses the cross terms by an amount of order one.

**The sector statement is inherited and not re-derived.** The connection is written anti-Hermitially in the parent, $\tilde A_\Phi^{*}=-\tilde A_\Phi$ on $\mathbb{B}_\Phi$, and the factor $i$ in $\frac{i\,ϙ}{\hbar}\tilde A_\Phi$ carries it into the Hermitian sector. The coupling element of this article is that same element. It is not a new object and it is not written loosely.

**The companion reads the same transform in the word.** *The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables* asks which bracket of the word the coupling lands in and counts what the operator does to the mode basis. This article asks what order the operator has. The two questions are different and neither answer depends on the other.

**The denial is stated once.** The transform carries $\mathbb{B}$-valued functions to $\mathbb{B}$-valued functions. It does not carry a material-sector field to an informational-sector field, and no display below claims that a coefficient's sector is a function's sector. The sector statements are statements about one element that multiplies, at one wave number or at one event.

**There is no new prediction and no new solution.** The equation, its gauge law, its constant-potential solutions and its Larmor rate are the parent's. What the transform adds is the order of the coupling in the momentum-space reading and the reason that order is a gauge-invariant notion at its floor.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient and the d'Alembertian those of *Operator and Calculus Conventions*, the four products those of *Product and Form Conventions*, the two forms those of *Norm and Pairing Conventions*, the units and the material time those of *Physics Units and Common Elements Conventions*, and the sector bookkeeping those of *Mirror Biquaternions and the Phy–Psy Switch*. The transform is the one of *Derivatives, Fields and Transforms*, whose symbol rule is quoted in its derived form and not re-derived:

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi ,
\qquad
(\tilde\nabla_\Phi)^{\natural}\longmapsto i\tilde K_\Phi^{\natural},
\qquad
\tilde K_\Phi=ik_t'e_t+\vec k_\Phi ,
\qquad
k_t'=\frac{\omega}{c}.
$$

**The temporal slot carries the sign, and the sign is not a convention of this article.** The coordinate is $R_t=ir_t'$, so the temporal derivative is $\partial/\partial R_t=-i\,\partial/\partial r_t'$, and the temporal slot of the symbol is $+ik_t'$ because the plane wave's phase carries $-k_t'r_t'$. On the plane wave $\tilde\Xi=\tilde\Xi_0\exp(i\theta_{\mathrm{pha}})$ with $\theta_{\mathrm{pha}}=\vec k_\Phi\cdot\vec r-k_t'r_t'$ the two identities used below are

$$
\tilde\nabla_\Phi e^{i\theta_{\mathrm{pha}}}=i\tilde K_\Phi\,e^{i\theta_{\mathrm{pha}}},
\qquad
(\tilde\nabla_\Phi)^{\natural}e^{i\theta_{\mathrm{pha}}}=i\tilde K_\Phi^{\natural}\,e^{i\theta_{\mathrm{pha}}},
$$

and both are the polar parent's, quoted at the temporal slot so that no sign is left to the reader.

**The parent's covariant derivative is quoted once.** It is

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi ,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_\Phi^{\natural},
$$

with $ϙ$ the charge, $k_m=mc/\hbar$ the mass wave number, and $\tilde A_\Phi$ the connection of the gauge principle. In the abelian component form the parent uses, $\tilde A_\Phi=\sum_\mu A_\mu e_\mu$ with complex scalar coefficients, and each component of the covariant derivative is a central scalar operator. That sentence is the parent's and its consequences are the polar companion's; this article uses only that the coefficients are central.

**The four sector statements.** $\tilde K_\Phi\in\mathbb{B}_\Phi$ and anti-Hermitian; $i\tilde K_\Phi\in\mathbb{B}_\Psi$ and Hermitian; $\tilde A_\Phi\in\mathbb{B}_\Phi$ and anti-Hermitian, which is the parent's own writing; $\frac{i\,ϙ}{\hbar}\tilde A_\Phi\in\mathbb{B}_\Psi$ and Hermitian. The last is a consequence of the third and of the centrality of $i$, and nothing else in the article turns on a sector question.

## The Symbol of the Coupled Operator

### The Two Summands

**In momentum space the coupled operator is the sum of a multiplier and the transform of a multiplication.** On a plane wave the derivative contributes $i\tilde K_\Phi$ and the connection contributes $\frac{i\,ϙ}{\hbar}\tilde A_\Phi$ at the same wave number, so the symbol of the first member is

$$
i\tilde K_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi
=i\Bigl(\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi\Bigr)
=i\tilde K_{\Phi,\mathrm{gco}} .
$$

**The first summand is a multiplier in every setting, and the second is a multiplier in one.** The derivative is a multiplier because the transform turns it into one; that is the symbol rule and it needs no hypothesis about the coefficients. The connection is a multiplier only where its transform is supported at one point, and that is the constant case. This section states the licence under which the second statement is used, and §*When the Coupling Is a Multiplier* states what replaces it when the licence fails.

**The constant-$\tilde A_\Phi$ licence, stated here and used here.** Throughout this section $\tilde A_\Phi$ is constant, so its transform is a central multiple of the delta at one wave number and the multiplication becomes a multiplier at every wave number. Every display in this section is a statement under that licence. The licence is dropped at §*When the Coupling Is a Multiplier*, and no result of that section assumes it.

**Under the licence the symbol is Hermitian in every entry, and the reason is a sum of two Hermitian elements.** The check used one hundred random connections $\tilde A_\Phi$ in the material sector and one hundred random wave numbers, with $ϙ=\hbar=1$: the element $\frac{i\,ϙ}{\hbar}\tilde A_\Phi$ satisfied $\lvert X^{*}-X\rvert=0.0$ at every draw, and the symbol $i\tilde K_{\Phi,\mathrm{gco}}$ satisfied the same with residual $0.0$. **The statement is structural**: a real linear combination of two Hermitian elements is Hermitian, and both summands are Hermitian by the sector list of the conventions.

### The Off-Diagonal Entries Cease to Be Conjugates

**The free symbol is $\natural$-symmetric and the coupled one is not.** The free pair has the two entries $i\tilde K_\Phi$ and $i\tilde K_\Phi^{\natural}$, which are each other's natural conjugates. With a connection the entries become $i\tilde K_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi$ and $i\tilde K_\Phi^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_\Phi^{\natural}$, and the second is the natural conjugate of the first only if $\tilde A_\Phi^{\natural}=\tilde A_\Phi$.

**That condition is the parent's electric-magnetic split, read as a symmetry of the symbol.** For a purely electric connection $\tilde A_\Phi^{\natural}=+\tilde A_\Phi$ and the two entries are conjugates; for a purely magnetic one $\tilde A_\Phi^{\natural}=-\tilde A_\Phi$ and the two entries are conjugates up to a sign; for a general connection neither holds. The parent says that purity is a property of a gauge and not of the entry, and the same sentence applies here: the $\natural$-symmetry of the symbol is a property of a gauge, not of the operator.

$$
\mathcal{D}(\tilde K_\Phi)=
\begin{pmatrix}
-k_m & i\tilde K_\Phi^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_\Phi^{\natural}\\[2pt]
i\tilde K_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi & -k_m
\end{pmatrix}.
$$

**The diagonal entries do not move.** They are $-k_m$ in both slots, a real central number that the connection cannot touch, because the mass coefficient in the parent's pair is a scalar multiplying the field and the connection is inserted in the derivative. **This is the structural statement that matters for the companion**: the mass is diagonal in momentum and off-diagonal in the part label, in every setting, and the coupling changes neither of those facts.

## When the Coupling Is a Multiplier

### The Criterion

**The transform of a product is a convolution, and that theorem is the whole mechanism.** It is *Biquaternion Continuous Harmonic Analysis*'s: for two fields $f$ and $g$, $\mathcal{F}[fg]=\mathcal{F}[f]*\mathcal{F}[g]$. It is cited here and not restated. A multiplication in position space therefore becomes, in momentum space, an integral operator whose kernel is the transform of the multiplier, and the operator collapses to a multiplier exactly when that kernel is a delta.

**Finding 1.** The coupling acts as a multiplier if and only if its transform is a delta, and that holds if and only if $\tilde A_\Phi$ is constant. A constant field's transform is supported at the single wave number zero, so the convolution degenerates into a multiplication at every wave number. A non-constant field's transform is not a single delta, so the convolution genuinely integrates.

**The delta test, with a count and a residual.** On a grid of $64$ samples a constant multiplier's transform carried the fraction $1.0000000000000000$ of its weight in one bin and $0.00\times10^{0}$ in every other bin. A field supported on three wave numbers, multiplied by a constant, came back supported on the same three: three in, three out of sixty-four, with off-support residual $1.17\times10^{-16}$ of the peak.

### The Ladder of Orders

**A profile of degree $d$ in the position gives an operator of order $d$ in the wave number.** This is the structural form of the ladder: multiplication by a polynomial of degree $d$ is, after the transform, the $d$-th derivative with a coefficient. The constant case is $d=0$, the multiplier; the linear case is $d=1$, the first-order differential operator; the quadratic case is $d=2$. The ladder continues without bound, and a profile that is not a polynomial gives an operator of no finite order.

**The linear bench.** With a linear profile $A(x)=ax$ the transform of the product was reproduced by the first-order operator $ia\frac{L}{2\pi}\frac{\mathrm{d}}{\mathrm{d}m}$ acting on the transform, with residual $1.38\times10^{-16}$ of the peak over the whole grid, and the best zeroth-order approximation to the same output left a residual of $4.13\times10^{-1}$. The output occupied all $64$ of $64$ modes. **The order is therefore measured rather than assumed**: the correct order fits to round-off and the neighbouring order fails by forty per cent.

**The quadratic bench, as the control.** With a quadratic profile on the same sixty-four samples the second-order operator fitted with residual $2.35\times10^{-16}$ while the best first-order operator left $1.99\times10^{-1}$, so the fit is discriminating in both directions: order one is not enough for a quadratic profile, and order zero is not enough for a linear one.

**The middle bench is the one that matters, and the reason is gauge invariance.** A constant connection is a gradient on flat space, so the multiplier case is the zero-curvature case. A linear connection with a constant field strength is not a gradient: with $\tilde A_t=i\,b\,x$ and $\tilde A_x=0$ the integrability condition $\partial_x\tilde A_t=\partial_t\tilde A_x$ fails, and the curvature component is $\lvert F_{tx}\rvert=0.9$ for $b=0.9$ against $0.0\times10^{0}$ for a constant $\tilde A_t$. **So the linear bench is the first coupling that no gauge can turn into a multiplier.**

**That is the precise statement of the finding.** The coupling is a multiplier in some gauge if and only if the field strength vanishes, and in that gauge $\tilde A_\Phi$ is constant. When the curvature is nonzero no gauge removes the operator character, and the cheapest it can be is first order, which is the constant-field-strength case.

### What the Criterion Does Not Say

**It does not say that a non-constant coupling is a small correction, nor that the order is a property of the physics.** The order of the operator and the size of its effect are different things: a weak linear connection spreads a single mode over all sixty-four, and a strong constant one spreads nothing. The order is a property of the operator in a gauge: a pure-gradient connection with a quadratic gauge function is linear in that gauge and zero in another, so the rung changes while the curvature stays zero. **The gauge-invariant content of the ladder is its floor**, that is, whether the coupling can be brought to order zero at all.

**It does not extend to a position-dependent symbol.** With a general $\tilde A_\Phi$ the momentum-space operator is a convolution, its kernel is the transform of the connection, and the notion of a symbol at a wave number is gone. The convolution is still self-adjoint for the Hermitian pairing, because the position-space multiplier is Hermitian at each event: on sixteen modes with a real temporal multiplier the matrix satisfied $\lVert C^{\dagger}-C\rVert/\lVert C\rVert=7.8\times10^{-17}$, while a non-Hermitian multiplier of the same size gave $1.3\times10^{0}$. **Self-adjointness survives the loss of a symbol; locality does not.**

## The Gauge Law in Momentum Space

**The gauge phase is $\theta_{\mathrm{gau}}=\frac{ϙ\,\Gamma}{\hbar}$ and the field transforms by a central phase.** The parent's law is $\tilde\Xi_2=\lambda\tilde\Xi$ with $\lambda=\exp(i\theta_{\mathrm{gau}})$ and $\tilde A_{\Phi,2}=\tilde A_\Phi-\tilde\nabla_\Phi\Gamma$ for real $\Gamma$. The multiplier $\lambda$ is central and of unit modulus, so the transform sees it as one scalar function and nothing else.

**Finding 4.** Gauge invariance is a translation in momentum space when the gauge phase is linear, and a phase is linear in the position exactly when its gradient is constant. For a linear $\theta_{\mathrm{gau}}$ the multiplication is a translation of the support by $\nabla\theta_{\mathrm{gau}}$, and the mode count is preserved. For a non-linear $\theta_{\mathrm{gau}}$ the multiplication is a convolution, and the mode count is not preserved.

**The linear case, with a count and a residual.** One mode at index $11$ of $128$, multiplied by $\exp(i\theta_{\mathrm{gau}})$ with $\theta_{\mathrm{gau}}=\frac{ϙ}{\hbar}\Gamma$ and $\Gamma$ linear, came back as one mode at index $24$ for a gauge gradient of thirteen modes and at index $40$ for one of twenty-nine. The residuals against the exact translated spectrum were $4.3\times10^{-15}$ and $1.9\times10^{-15}$ of the peak, and the occupied count was one of one hundred and twenty-eight in both cases.

**The non-linear case, with the same discipline.** One mode multiplied by a quadratic gauge phase came back occupying $128$ of $128$ modes, with the largest single coefficient carrying $0.465$ of the total weight. No translation reproduces that spectrum, and the count is the check: a translation cannot change the number of occupied modes, and the number changed from one to all. **The qualification is therefore not decoration**: gauge invariance of the equation holds for every $\Gamma$, while the description of it as a translation holds only for a linear $\Gamma$.

**What the translation buys.** For a linear gauge phase the covariant wave number is the canonical one shifted by a constant, the support moves rigidly, and every statement about the spectrum that depends on shape is unchanged. That is why the constant-potential case of the parent is solvable in closed form: the gauge that removes the potential is a translation, and a translation acts on a plane wave by multiplication.

## The Shift Translates and Cannot Resize

**Finding 3.** At constant $\tilde A_\Phi$ the covariant wave number element is $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi$, and its quaternionic norm is the interval at the shifted argument:

$$
\langle i\tilde K_{\Phi,\mathrm{gco}}\rangle_\natural
=\Bigl(k_t'+\frac{ϙ}{\hbar}a_t\Bigr)^{2}-\Bigl\lvert\vec k_\Phi+\frac{ϙ}{\hbar}\vec a\Bigr\rvert^{2}
=\frac{p'^{2}}{\hbar^{2}},
$$

with $\tilde A_\Phi=i a_t e_t+\vec a$, $a_t$ and $\vec a$ real, and $p'=\hbar\tilde K_{\Phi,\mathrm{gco}}$ the kinetic four-momentum. **The $\hbar^{2}$ is where it belongs**: the norm of a wave-number element is an inverse length squared, and $p'^{2}$ is that quantity multiplied by $\hbar^{2}$, so the division restores the wave-number units.

**The reason is that a translation cannot change a shape.** The norm is one fixed quadratic form of four real numbers. Evaluating it at the translated numbers gives the same form at a new origin: the surface is congruent to the free one, and the congruence is a translation rather than a Lorentz transformation. **What follows for the spectrum is the parent's sentence**: a uniform scalar potential shifts every level by $ϙA_tc$ and changes no spacing, and no constant potential opens a gap, because a translated hyperboloid has the same radius.

**The guard, and why it is needed.** The temptation is to write the norm of the sum as the sum of the norms. The check rejects it: over fifty random pairs of momenta and connections the correct identity held with deviation $0.0$, while the additive form $\langle i\tilde K_\Phi\rangle_\natural+\langle\frac{i\,ϙ}{\hbar}\tilde A_\Phi\rangle_\natural$ deviated by up to $4.2$ in absolute value. **The cross terms are the whole of the difference**, and they are what makes the shift a translation instead of an addition.

**The same statement in the momentum variable.** With $\tilde P_{\Phi,\mathrm{gco}}=\hbar\tilde K_{\Phi,\mathrm{gco}}$ the identity reads $\langle i\tilde P_{\Phi,\mathrm{gco}}\rangle_\natural/\hbar^{2}=p'^{2}/\hbar^{2}$, and the check gave deviation $0.0$: the two writings are one identity and the units carry the factor.

**The clause that must travel with the finding.** All of this holds at constant $\tilde A_\Phi$, under the licence stated where the multiplier was first used. For a position-dependent connection there is no $\tilde K_{\Phi,\mathrm{gco}}$ at a point, no single shifted argument, and no norm to evaluate: the operator is a convolution and the statement is empty.

## Limits

**Constant coefficients.** The symbol exists where the connection is constant, and the ladder's floors are exact there. A position-dependent connection replaces the symbol by a convolution and the ladder by a smoothness classification, which is the companion's subject.

**The gauge dependence of the rung.** The order of the operator is not gauge invariant and the floor of the ladder is. A reader who takes the order for a physical quantity will find it changing under a gauge transformation with a quadratic $\Gamma$, and the article states the invariant version so that this cannot be mistaken for an error.

**The abelian component form.** The parent's coupling separates into components because the coefficients are central scalars, and the convolution theorem used here is the central-kernel form. A non-abelian connection would add a commutator term, the transform of the coupling would not be a convolution of the field with a kernel alone, and the ladder would need a different argument.

**The companion's question is different, and this article does not answer it.** *The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables* counts what the operator does to the mode basis and reads it in the word. A count of occupied modes is not an order and an order is not a count: a first-order operator can preserve a single mode if the profile is right, and a multiplier can spread one if the multiplier is a distribution. The two articles meet at the constant case, where both statements are trivial, and they separate everywhere else.

## Open Questions

**One question is left open, and it is about the operator setting.** Whether the ladder survives when the symbol is operator-valued — that is, whether a covariant derivative with a position-dependent connection has a notion of order invariant under the gauge group rather than under a chosen gauge — is not settled here. The floor of the ladder is invariant, and the question is whether anything above the floor is. **The question is well posed because the object it asks about exists**: the convolution of §*When the Coupling Is a Multiplier* is a bounded operator on the mode space for a bounded connection, its kernel is the transform of the connection, and the order of a convolution is the decay of that kernel. Whether the decay has a gauge-invariant meaning is a question about the kernel and not about the transform, and it is not answered here.

## Summary

In momentum space the coupled Dirac operator is the sum of a multiplier and the transform of a multiplication. The multiplier is always present, because the derivative is always a multiplier; the second summand is a multiplier exactly when the connection is constant, which is exactly when its transform is a delta. Under that licence the symbol is $i\tilde K_{\Phi,\mathrm{gco}}=i(\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi)$, Hermitian in every entry because both summands are Hermitian, with the temporal slot $+ik_t'$ fixed by $\partial/\partial R_t=-i\partial/\partial r_t'$.

The ladder of orders is the article's finding. A profile of degree $d$ gives an operator of order $d$: the linear bench fitted to $1.38\times10^{-16}$ with order one and failed by $4.13\times10^{-1}$ with order zero, the quadratic bench fitted to $2.35\times10^{-16}$ with order two and failed by $1.99\times10^{-1}$ with order one. The linear bench is the first rung that no gauge can remove, because a linear connection with a constant field strength is not a gradient, and its curvature was $0.9$ against $0.0$ for a constant connection.

The shift of the wave number is a translation. At constant $\tilde A_\Phi$ the norm is $\langle i\tilde K_{\Phi,\mathrm{gco}}\rangle_\natural=p'^{2}/\hbar^{2}$, exact over fifty draws, while the additive form of the same quantity deviated by up to $4.2$. Gauge invariance is a translation in momentum space when the gauge phase $\theta_{\mathrm{gau}}=\frac{ϙ\Gamma}{\hbar}$ is linear — one mode in, one mode out, residual $4.3\times10^{-15}$ — and a convolution when it is not, where one mode became one hundred and twenty-eight.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi$ | The parent's covariant derivative |
| $\tilde A_\Phi=i a_t e_t+\vec a$ | The connection in the material sector; $a_t$, $\vec a$ real |
| $i\tilde K_\Phi$, $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$ | The symbol of the gradient; temporal slot $+ik_t'$ |
| $i\tilde K_{\Phi,\mathrm{gco}}=i(\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi)$ | The symbol of the coupled derivative |
| $p'=\hbar\tilde K_{\Phi,\mathrm{gco}}$ | The kinetic four-momentum |
| $\langle i\tilde K_{\Phi,\mathrm{gco}}\rangle_\natural=p'^{2}/\hbar^{2}$ | The norm of the shifted symbol; the interval at the shifted argument |
| $d$ | The degree of the connection's profile; the order of its momentum-space operator |
| $\theta_{\mathrm{gau}}=\frac{ϙ\,\Gamma}{\hbar}$ | The gauge angle |
| $\mathcal{F}[fg]=\mathcal{F}[f]*\mathcal{F}[g]$ | The convolution theorem; cited from *Biquaternion Continuous Harmonic Analysis* |

## Further Reading

- *The Coupled Dirac Equation in Biquaternionic Form*, for the covariant derivative, the gauge law, the anti-Hermitian writing of the connection and the constant-potential solutions.
- *The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables*, for the same transform read in the word and for the count of mixed modes.
- *The Fourier Transform and the Dirac Equation in Biquaternionic Form*, for the free symbol, its Hermiticity and the light cone as the idempotent variety.
- *The Fourier Transform and the Variational Principle and the Dirac Equation in Biquaternionic Form*, for the action's momentum-space quadratic form and the zero-pole relation.
- *Derivatives, Fields and Transforms*, for the transform, its kernel and the symbol rule.
- *Biquaternion Continuous Harmonic Analysis*, for the convolution theorem and its central-kernel hypothesis.
- *The Gauge Principle in Biquaternionic Form*, for the localization of the central phase and the sign of the coupling.
- *Wave–Particle Duality and the Fourier Transform*, for the transform as a change of description.
- R. N. Bracewell, *The Fourier Transform and Its Applications* (McGraw-Hill, 3rd ed., 1999), for the convolution theorem, the derivative rule and the order of a convolution.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 2, for the minimal substitution and its momentum-space reading in the standard language.
