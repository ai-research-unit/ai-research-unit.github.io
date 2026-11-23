# __The Lagrangian and the Klein–Gordon Equation in Momentum Space__

## Introduction

The variational parent states one sentence in passing and drops it. At its §*The Action on the Carrier and on the Algebra* it writes that for a constant $\tilde M$ the plane-wave problem becomes the eigenvalue problem $(\omega^{2}-c^{2}\,4\pi^{2}\nu_{\Phi}^{2})\tilde\Xi_0=\tilde M\tilde\Xi_0$, "whose four branches are the four eigenvalues". The sentence is stated, used as a remark about what a non-central coefficient would do, and not developed. This article develops it.

The finding is a count, and the count is not four. Under the transform the equation becomes $(\omega^{2}/c^{2}-4\pi^{2}\nu_{\Phi}^{2})\tilde\Xi_0=\tilde M\tilde\Xi_0$, an eigenvalue problem for one operator on $\mathbb{B}$. For a Hermitian $\tilde M=a\,e_t+i\vec v\cdot\vec e$ the spectrum of left multiplication is $a+\lvert\vec v\rvert$ and $a-\lvert\vec v\rvert$, each with multiplicity two. **There are two eigenvalues and four frequencies, and the doubling is not the sector pair.**

The governing thesis is one sentence. The free Klein–Gordon symbol is a central scalar; it commutes with everything, including the sector projectors; therefore the free scalar theory carries no sector content at all, and every sector statement at Klein–Gordon level is a statement about the potential. This is why the article is about $\tilde M$ and not about $\tilde\nabla_\Phi$. The Dirac family gets its sector selection from the Hermiticity of a first-order symbol; the scalar family gets it from the reality of the second-order action.

The selection rule has a direction. The potential term of the action is $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)$. That number is real when $\tilde M$ is Hermitian and purely imaginary when $\tilde M$ is anti-Hermitian. So the material sector $\mathbb{B}_\Phi$ is excluded from the Klein–Gordon Lagrangian by the reality of $S$, and not by taste. The formal consequence of admitting it — a purely imaginary spectrum and a complex dispersion — is stated after the exclusion and not before it.

The potential also sets a threshold. **The lower branch $a-\lvert\vec v\rvert$ is negative whenever the potential's vector part exceeds its scalar part**, and then the frequency is imaginary at small wave number. One inequality, one threshold, and a measured frequency of occurrence.

The companion asks a different question of the same equation. *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form* asks when the second-order symbol factors into first-order ones, and answers through the zero set rather than the spectrum. This article asks what the eigenvalues are. Neither answer depends on the other.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient, the d'Alembertian and the symbol rule those of *Operator and Calculus Conventions*, the two forms those of *Norm and Pairing Conventions*, the invertibles and the material time those of *Physics Units and Common Elements Conventions*. The kernel and its $i\epsilon$ prescription are those of *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*.

The bookkeeping is stated once. With $\tilde\Upsilon_\Phi=i\nu_t'e_t+\vec\nu_\Phi$, $2\pi\nu_t'=\omega/c$, $\nu_m=\frac{mc}{h}$ and $r_t'=ct'$,

$$
\langle\tilde\Upsilon_\Phi\rangle_\natural=-2\pi\nu_t'^{2}+4\pi^{2}\nu_{\Phi}^{2},
\qquad
\langle\tilde P_\Phi\rangle_\natural=N,
\qquad
\tilde\nabla_\Phi\longmapsto 2\pi i\tilde\Upsilon_\Phi,
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\longmapsto-\langle\tilde\Upsilon_\Phi\rangle_\natural .
$$

The phase carries the sign and the sign is quoted. A positive-frequency plane wave is $\tilde\Xi=\tilde\Xi_0\exp(-i\theta_{\mathrm{pwp}})$ with $\theta_{\mathrm{pwp}}=\omega r_t'-2\pi\vec\nu_\Phi\cdot\vec r$. On it $\partial/\partial r_t'\mapsto-i\omega$ and $\partial/\partial r_k\mapsto i\nu_{\Phi,k}$, so $\Box_\Phi\mapsto 2\pi\nu_t'^{2}-4\pi^{2}\nu_{\Phi}^{2}$, which is the parent's own computation and is used here without alteration.

The potential is a constant element. Throughout, $\tilde M$ is a constant element of $\mathbb{B}$: Hermitian, $\tilde M=a\,e_t+i\vec v\cdot\vec e$ with $a$ and $\vec v$ real, or anti-Hermitian, $\tilde M=i\,a\,e_t+\vec v\cdot\vec e$. Its left multiplication $L(\tilde M)$ is complex-linear on the four-dimensional complex space $\mathbb{B}$, because $i$ is central, so it is a $4\times4$ complex matrix in the basis $e_{\imath}$ and its eigenvalues are ordinary complex eigenvalues.

### The Constant-Coefficient Licence

Constant coefficients are the licence. The eigenvalue problem needs $\tilde M$ constant, because the symbol exists only there. A position-dependent Hermitian $\tilde M$ keeps the equation and loses the spectrum: the momentum-space operator becomes a convolution, its kernel is the transform of $\tilde M$, and there is no matrix and no eigenvalue. The parent's constant setting is therefore not a simplification of convenience but the only setting in which the four branches exist as branches.

The abelian component form matters for the same reason. The parent separates the covariant derivative into components because the coefficients are central scalars, and that is what makes $L(\tilde M)$ a single constant matrix rather than a connection. A non-abelian coefficient would add a commutator inside the potential term and the eigenvalue problem would become a matrix-valued one with no scalar spectrum.

The companion's question is the zero set, and it is not this article's. *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form* asks when the second-order symbol factors into first-order ones and answers through the reducibility of its quadric. A spectrum and a factorization are different properties of the same symbol: an operator can have a perfectly good spectrum and no square root, which is exactly the Klein–Gordon case, and the scalar Klein–Gordon operator has both a known spectrum and a known obstruction.

The third article of the family reads the polar word, and this one does not. *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Polar Variables* asks where the transform's phase comes from and what removes the symbol; its answer is about the amplitude, and it is not a restatement of anything here. Nothing in the article is a transform between sectors: every object above is an element of $\mathbb{B}$ or a coefficient of one, and the transform returns the same algebra.

## The Action in Momentum Space

### The Momentum-Space Equation Is an Eigenvalue Problem

Finding 1. Substituting $\tilde\Xi=\tilde\Xi_0\exp(-i\theta_{\mathrm{pwp}})$ into $(\Box_\Phi-\tilde M)\tilde\Xi=0$ and using the symbol rule gives, in one line,

$$
\left(\frac{\omega^{2}}{c^{2}}-4\pi^{2}\nu_{\Phi}^{2}\right)\tilde\Xi_0=\tilde M\,\tilde\Xi_0 .
$$

The right side is left multiplication, and that is the whole content. The parent's position-space equation has $\tilde M$ multiplying the field at each event; its transform is the same left multiplication at each wave number, because a constant element has no position dependence to transform. The equation is therefore an eigenvalue problem with $\tilde M$ as the operator and $\omega^{2}/c^{2}-\nu_{\Phi}^{2}$ as the eigenvalue.

The parent's display has a bookkeeping defect, and it is repaired here rather than copied. The parent prints $(\omega^{2}-c^{2}\,4\pi^{2}\nu_{\Phi}^{2})\tilde\Xi_0=\tilde M\tilde\Xi_0$. Take $\tilde M=4\pi^{2}\nu_m^{2}e_t$, which the parent's own §*The Two Settings* permits: the right side then has dimension $\mathrm{L}^{-2}$, because $\nu_m$ is an inverse length, while the left side has dimension $\mathrm{T}^{-2}$, because $\omega$ is an inverse time. The two differ by $c^{2}$. The parent's own §*The Equation and Its Operator* fixes $\nu_t'^{2}-\nu_{\Phi}^{2}=+\nu_m^{2}$ with $2\pi\nu_t'=\omega/c$, which is the corrected display. The parent's eigenvalue form is therefore its reading with the speed of light divided out, and the article uses the corrected form throughout.

The repair is measured, not asserted. On the case $c=2$, $2\pi\nu_m=1.4$, $2\pi\vec\nu_\Phi=(0.9,-0.5,0.3)$ and a Hermitian potential $\tilde M=4\pi^{2}\nu_m^{2}e_t+i(0.3,-0.2,0.5)\cdot\vec e$, the two eigenvalues of $\tilde M$ are $2.576441$ and $1.343559$. On the corresponding solutions the corrected left side returns those two numbers to all printed digits; the parent's expression $\omega^{2}-c^{2}\nu_{\Phi}^{2}$ returns $10.305766$ and $5.374234$, which are the same numbers multiplied by $c^{2}=4$. The residual of the corrected form is $0.0$ and the discrepancy of the uncorrected form is exactly the factor, so the defect is a bookkeeping slip and not a physical disagreement.

What the transform buys is a diagonal basis for the coupling. The parent says that a non-central $\tilde M$ turns the four independent coefficients into four coupled channels. In momentum space the coupling is one $4\times4$ matrix acting on one four-component amplitude, and the channels are its eigenvectors. The transform does not remove the coupling; it exhibits the basis in which the coupling is diagonal, and that basis is available because $\tilde M$ is constant.

The eigenvalue is a frequency squared, so the count doubles again. Each eigenvalue $\lambda$ of $\tilde M$ gives $\omega^{2}=c^{2}(4\pi^{2}\nu_{\Phi}^{2}+\lambda)$ and therefore two frequencies $\pm c\sqrt{\nu_{\Phi}^{2}+\lambda}$, one per sign of $\omega$. The eigenvalue problem fixes the dispersion relation; it does not fix the sign of the frequency, and no choice of $\vec\nu_\Phi$ removes the negative root.

The licence travels with the finding: everything in this section needs $\tilde M$ constant, because the symbol exists only there, and a position-dependent $\tilde M$ replaces the matrix by a convolution with no eigenvalue problem at all.

### The Spectrum of Left Multiplication

Finding 2. For a Hermitian potential $\tilde M=a\,e_t+i\vec v\cdot\vec e$ with $a$ and $\vec v$ real, the spectrum of $L(\tilde M)$ is

$$
\operatorname{eig}L(\tilde M)=\bigl\{a+\lvert\vec v\rvert,\;a+\lvert\vec v\rvert,\;a-\lvert\vec v\rvert,\;a-\lvert\vec v\rvert\bigr\}.
$$

The proof is one algebraic identity. Put $q=\vec v\cdot\vec e$, the pure vector part. Then $q^{2}=-\lvert\vec v\rvert^{2}e_t$, so $L(q)^{2}=-\lvert\vec v\rvert^{2}I$, so $L(q)$ has the two eigenvalues $\pm i\lvert\vec v\rvert$, each twice. Since $i$ is central, $L(iq)=iL(q)$, and the two eigenvalues become $\mp\lvert\vec v\rvert$. Adding the central $a$ gives $a\pm\lvert\vec v\rvert$. The minimal polynomial of $L(\tilde M)$ is $(L-a)^{2}-\lvert\vec v\rvert^{2}$, of degree two, on a four-dimensional space, so each root has algebraic multiplicity exactly two.

The count is measured. Over three hundred random draws of $(a,\vec v)$ the sorted computed spectrum matched the sorted display to $3.1\times10^{-15}$, and the characteristic polynomial of the computed spectrum matched the polynomial $(x-a)^{2}-\lvert\vec v\rvert^{2}$ squared, coefficient by coefficient, to $1.6\times10^{-13}$. The doubling is therefore not a numerical accident of the examples.

Two eigenvalues, four frequencies, and the parent's "four branches" is a count of the second kind. The parent counts four eigenvalues. Two of them are distinct and each is doubled. If one counts the frequencies $\pm c\sqrt{\nu_{\Phi}^{2}+\lambda}$ instead, one gets four values, each carrying the multiplicity of its $\lambda$. Both counts reach four; neither is a count of four independent branches, and the phrase "four branches" hides which count is meant. The article writes "two eigenvalues, each doubled" and "four frequencies, each doubled" and uses no other count.

The doubling is the central complex structure, and the sectors sit inside each branch. Because $i$ is central, $L(\tilde M)(i\tilde\Xi)=iL(\tilde M)\tilde\Xi$, so every eigenspace is closed under multiplication by $i$. Because left multiplication commutes with right multiplication, the eigenspace of $\lambda$ is the right ideal $\mathbb{B}w$ generated by any one eigenvector $w$. That ideal contains $ww^{*}$, which is Hermitian, and $i\,ww^{*}$, which is anti-Hermitian. **So each branch carries both sectors, and the sector split does not separate the branches.** An eigenspace cannot lie inside one sector, because it is closed under multiplication by $i$ and $i$ exchanges the sectors. The smallest Hermiticity defect attainable inside an eigenspace was $0.000$ over forty branches, reached by $ww^{*}$ itself, and no eigenspace is a sector.

That last sentence is the momentum-space form of the parent's own verdict. The parent's §*Does the Second-Order Structure Fit $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$?* concludes that the split of a Klein–Gordon field into $\mathbb{B}_\Psi$ and $\mathbb{B}_\Phi$ is the real-imaginary decomposition of a complex field, two $i$-related copies of one equation. Here the same fact appears as a property of an eigenspace: the space is $i$-invariant, so it carries both sectors and is identical with neither.

The anti-Hermitian case has the same shape with $i$ in front. For $\tilde M=i\,a\,e_t+\vec v\cdot\vec e$ the same identity gives $\operatorname{eig}L(\tilde M)=i(a\pm\lvert\vec v\rvert)$, each twice. Over three hundred draws the real part of every eigenvalue was below $8.9\times10^{-16}$ and the sorted spectrum matched $i(a\pm\lvert\vec v\rvert)$ to $3.6\times10^{-15}$. The spectrum is purely imaginary, and that is exactly what disqualifies the case in the next section.

The pairing. Settled once and inherited. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$; the quaternionic alternative and its two defects are the reality part of §*The Action* of *The Lagrangian and the Klein–Gordon Equation*, and the density here is that pairing applied to the symbol's action.

The type of the coefficient. Settled once and inherited. The kinetic coefficient is the central $i$, anti-Hermitian by inspection, so every kinetic density at a mode is real for every field. That is the element article's computation and it is not repeated.

The selection rule. Finding 3. The potential term of the action is $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)$, and its reality is equivalent to $\tilde M$ being Hermitian. The parent's kinetic term is already real for every field, so the potential term is the only place where a sector question can arise, and this is what it decides.

The proof is the Hermiticity of the pairing. The form $\langle A,B\rangle=\mathrm{Sc}(A^{*}B)$ is a positive-definite Hermitian form on the complex vector space $\mathbb{B}$. For a Hermitian $\tilde M$ one has $\langle\tilde\Xi,\tilde M\tilde\Xi\rangle=\langle\tilde M\tilde\Xi,\tilde\Xi\rangle$, so the number is real. For an anti-Hermitian $\tilde M$ the same computation gives $\langle\tilde\Xi,\tilde M\tilde\Xi\rangle=-\langle\tilde M\tilde\Xi,\tilde\Xi\rangle$, so the number is purely imaginary. There is no third case: the generic element splits uniquely into a Hermitian part and an anti-Hermitian part, $\tilde Q=\tilde Q_\Psi+\tilde Q_\Phi$ with $\tilde Q_\Psi=\tfrac12(\tilde Q+\tilde Q^{*})$ and $\tilde Q_\Phi=\tfrac12(\tilde Q-\tilde Q^{*})$, and the quadratic form splits with it into a real and an imaginary piece. The potential's own glyph is not doubled to say the same thing: it is Hermitian or anti-Hermitian as it stands, and when it is neither, the two parts are written $\tfrac12(\tilde M+\tilde M^{*})$ and $\tfrac12(\tilde M-\tilde M^{*})$.

The count confirms both halves. Over three hundred random pairs of a field and a Hermitian potential, the quantity $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)$ had an imaginary part below $3.6\times10^{-15}$. Over three hundred random pairs with an anti-Hermitian potential, its real part was below $7.1\times10^{-15}$. The two numbers are the two halves of the selection rule, and they are structural rather than numerical: no field can defeat them.

So the material sector is excluded, and the exclusion is a selection rule. A Klein–Gordon Lagrangian whose potential is anti-Hermitian, $\tilde M=\tfrac12(\tilde M-\tilde M^{*})\in\mathbb{B}_\Phi$, has an action whose imaginary part is $\int\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)$, which is not a boundary term and does not vanish. A complex action is not a variational principle with real stationary points; it is a saddle-point problem, and its stationarity conditions are not the equation the parent derives. The exclusion is therefore not a restriction of convenience. It is the condition under which the action of §*The Action in Element Form* exists at all.

The formal consequence, stated after the exclusion and not before. If one keeps the anti-Hermitian potential anyway, the equation still has plane-wave solutions, because the algebra does not care about the reality of an integral. Their eigenvalues are purely imaginary, by §*The Action in Momentum Space: The Spectrum of Left Multiplication*, so

$$
\frac{\omega^{2}}{c^{2}}=4\pi^{2}\nu_{\Phi}^{2}+i\,\lambda,
\qquad \lambda\in\mathbb{R},
$$

The result is not a wave. The frequency is complex for every wave number, and a complex frequency is growth or decay in time with no propagation threshold, so the mode is not a wave in any sense the parent's dispersion relation recognises. That is the formal content of the excluded case; it is recorded so that a reader who meets it elsewhere can identify it, not as a candidate theory.

The comparison with the Dirac family is exact and it is instructive. There the symbol is first order and the object that must be Hermitian is the symbol itself, because a first-order equation is a flow and a flow wants a unitary generator. Here the equation is second order, its action contains $\tilde M$ quadratically, and the object that must be real is the action's density. Same selection rule, different quantity selected. The scalar family selects on $S$ and the spinor family selects on $H$, and neither selection is available in the other family. The free case is the boundary of the rule: with $\tilde M=4\pi^{2}\nu_m^{2}e_t$ the potential is central and Hermitian at once, the anti-Hermitian part vanishes, and both sectors pass the test, which is why the free theory cannot tell them apart.

What reality does not buy. Not at issue here. The action of this article is real for every admissible field, and its claim is the opposite direction: that the *symbol* is real only for a Hermitian $\tilde M$. The gap between the two is not a weakness of the action here but the content of the exclusion, and the coupled article states it as one.

## The Variation

The variation is algebraic, and that is the whole difference from position space. The mode form $Q$ of the previous section is a quadratic form in the amplitude: it contains the amplitude and its conjugate and no derivative of either, because the transform has replaced every derivative by a multiplier. So the variation with respect to the conjugate amplitude is

$$
\delta Q=\mathrm{Sc}\bigl[\delta X^{*}\,\mathcal{S}(\omega,2\pi\vec\nu_{\Phi})X\bigr],
$$

with no integration by parts, no surface term and no boundary condition. A boundary term appears in a variational principle because a derivative is varied; here no derivative is varied, so none appears. That is not a convenience of the calculation, it is what the transform does to the principle.

Stationarity is the symbol equation. Vanishing for every $\delta X^{*}$ forces the bracket to vanish, by the same positivity argument as in the element article: choose $\delta X^{*}$ equal to the bracket and the scalar part becomes a sum of squared moduli. So

$$
\mathcal{S}(\omega,2\pi\vec\nu_{\Phi})\,X=0,
$$

the symbol equation the article solves. The passage from the action to the equation is one line and it is exact: the fixed-frequency action's stationarity and the symbol equation are the same statement.

What is lost, and it must be said. The variation at a mode cannot see a boundary condition, a topological charge or a spatially varying coefficient, because a mode is defined only where the coefficients are constant. Every statement in this section inherits the constant-coefficient licence that the section on limits makes explicit.

### The Tachyon Threshold

Finding 4. The lower branch $a-\lvert\vec v\rvert$ is the threshold, and the condition for a non-negative spectrum is one inequality:

$$
a\geq\lvert\vec v\rvert .
$$

The mechanism is one substitution. With $\lambda=a-\lvert\vec v\rvert$ the dispersion is $\omega^{2}=c^{2}(4\pi^{2}\nu_{\Phi}^{2}+a-\lvert\vec v\rvert)$. At small wave number the bracket is dominated by $a-\lvert\vec v\rvert$; when that is negative, $\omega^{2}$ is negative for every $\nu_{\Phi}$ below $\sqrt{\lvert\vec v\rvert-a}$, and $\omega$ is imaginary there. The mode is evanescent in time: it does not oscillate, it grows or decays.

The threshold itself is the massless case. At $a=\lvert\vec v\rvert$ the lower branch vanishes and its dispersion is $\omega^{2}=c^{2}\,4\pi^{2}\nu_{\Phi}^{2}$, the cone. The upper branch has $\lambda=2\lvert\vec v\rvert$ and its dispersion is the massive one with $4\pi^{2}\nu_m^{2}=2\lvert\vec v\rvert$. So the two branches are one massless and one massive cone, and the potential's two parts decide which is which.

The occurrence is common, and the count says so. Over three hundred draws with $a$ standard normal and $\vec v$ standard normal in three dimensions, the lower branch was negative in $276$ of them. The vector part of a random Hermitian potential has three components and its length is typically larger than one component, so a positive scalar part does not by itself keep the spectrum non-negative. **A potential whose scalar part is not larger than the length of its vector part has a tachyon branch**, and that is the generic case for unconstrained coefficients. What the threshold is not: it is not a bound on the energy of a state, and it is not a statement about the sign of the charge. It is a statement about the sign of one eigenvalue of one operator, and its only consequence is the sign of $\omega^{2}$ at small $\nu_{\Phi}$. The parent's two defects — indefinite charge and negative energies — are separate, and neither is decided by this inequality.

### Why the Free Case Says Nothing

Finding 5. With $\tilde M=4\pi^{2}\nu_m^{2}e_t$ the four eigenvalues coincide at $\nu_m^{2}$, the symbol commutes with every element of $\mathbb{B}$, and no sector statement can be made. The eigenvalue problem degenerates from a matrix problem to a multiple of the identity. The count is exact and it is the point: the computed spectrum was $\nu_m^{2}$ four times with a residual below $10^{-15}$, and the commutator of the symbol with fifty random elements of $\mathbb{B}$ was $0.0$ in every component. A central symbol commutes with the sector projectors, so $\Box_\Phi-4\pi^{2}\nu_m^{2}$ acts identically on $\mathbb{B}_\Psi$ and on $\mathbb{B}_\Phi$. The equation cannot tell the sectors apart because its operator does not contain them.

This is the parent's conclusion reached in one line. The parent's §*Does the Second-Order Structure Fit $\mathbb{B}_{\Phi}/\mathbb{B}_{\Psi}$?* argues in position space that the sector split gives two $i$-related copies of the same equation and is therefore not the doubling the equation needs. In momentum space the same statement is a property of a scalar multiple of the identity: an operator proportional to $I$ has one eigenspace, which is the whole space, and the whole space is where the sectors live.

The thesis of the article is this finding read backwards. Because the free symbol is central and carries no sector content, every sector statement at Klein–Gordon level must come from the potential. The article's four other findings are the four ways in which it does: the spectrum, the multiplicity, the reality, and the threshold. Remove the potential and all four collapse to one number.

### The Legendre Transform

Quadratic in the frequency, so two-valued. The mode action is quadratic in $\omega$, so its derivative with respect to $\omega$ is linear and the transform inverts. The inverse image of the energy is two frequencies, and the two are the reading's two branches: the same form, read at $+\omega$ and at $-\omega$, with densities of opposite sign.

The two branches meet at one wave number. The quadratic's discriminant vanishes where $\vec\nu^{2}+\nu_m^{2}=0$, and there the two roots coincide. That is the article's tachyon threshold, and in the transform's language it is the place where the two branches become one and the density's sign stops being able to distinguish them. Below it there are two branches; above it there is none.

Why the threshold is a property of the form. It is the discriminant of the symbol's frequency dependence, and the symbol is the form's kernel. The threshold is therefore not a statement about a particle's mass but a statement about when the form's two roots are real, which is why the article's section on it precedes the section on what the free case does and does not say.

What the transform adds. The slope: the derivative of the action with respect to $\omega$ is the density per mode, so the transform maps the form's argument to its density. The slope's sign is the branch's sign, and the two branches therefore have opposite slopes at the same energy — the statement that makes the particle and the antiparticle distinguishable in this reading.

What the free case says, in the transform's language. Nothing about the coupling, and the article says so. The free transform is the coupled transform at zero connection, so every free statement is a special case and no free statement tests the shift. That is why the coupled article's transform section is short and its zero-pole section is long.

One caution the article keeps. The transform is taken at fixed wave number and fixed amplitude, before the equation is imposed. On shell the form vanishes and the transform of zero is zero, so the order matters and the article states it once.

## The Constraints the Action Imposes: The Constraint Is the Mass Shell

The action's equation is an eigenvalue problem, and that is where the constraint sits. In this chart the field equation reads $\bigl(\omega^{2}/c^{2}-4\pi^{2}\nu_{\Phi}^{2}\bigr)\tilde\Xi_0=\tilde M\tilde\Xi_0$, so the operator's symbol acts on the amplitude and the condition for a nonzero amplitude is that the symbol be singular at that momentum. Nothing is imposed on the amplitude itself.

The singular set is the mass shell. The eigenvalue $\tilde M$ contributes $\nu_m^{2}$ on the central part and nothing on the spatial ones, so the singular set is $\omega^{2}/c^{2}-4\pi^{2}\nu_{\Phi}^{2}=4\pi^{2}\nu_m^{2}$ on the branch the amplitude occupies: the cone at $\nu_m=0$ and a two-sheeted surface at finite mass, the two sheets being the two signs of the frequency.

The mass is the only thing that separates the sheets. A constant connection translates the frequency and rotates the wave vector and leaves the separation at $2\nu_m$, which is why the dispersion relation of this article and the polar article's agree after the substitution that takes one chart to the other. The constraint is therefore one scalar equation on four numbers, and everything else the action says is about the amplitude.

What is absent. No Gauss law, because the connection is fixed at a mode; no boundary condition, because a variation at one momentum cannot see one; no restriction on the amplitude at a singular momentum. The constraint content is one determinant, and the structural consequence's denial is a statement about what that determinant leaves free.

## The Structural Consequence: The Denial That Survives

**The informational sector is not the Fourier dual of the material sector.** Every transform in this article acts on a $\mathbb{B}$-valued function and returns a $\mathbb{B}$-valued function. No step carries a field out of its sector, and no display above identifies a coefficient's sector with a function's sector. The sector statements are statements about one constant element that multiplies, at one wave number or at one event.

A second denial belongs here because the eigenvalue problem invites the error: the eigenvalues of $L(\tilde M)$ are complex numbers, and their real or imaginary character is a statement about $\tilde M$'s sector and not about the field's. A field in $\mathbb{B}_\Psi$ and a field in $\mathbb{B}_\Phi$ feel the same matrix, because the matrix is left multiplication on the whole algebra; what differs is only which sector their values occupy, and that is not an eigenvalue.

## The Noether Currents: The Charge Per Mode

The charge at a mode. The Noether charge is the spatial integral of the temporal component of the current, and by Parseval it becomes a sum over modes. At one mode the summand is the bilinear of the amplitude,

$$
\mathcal{Q}(\vec\nu_{\Phi})=\frac{h}{2\pi}\,\mathrm{Sc}\bigl[X^{*}(\vec\nu_{\Phi})X(\vec\nu_{\Phi})\bigr],
$$

up to the normalisation the element article fixes, so that the total charge is the integral of this density over the wave numbers. The step from the position-space charge to this display is Parseval's identity and nothing else; the companion article *The Lagrangian and the Schrödinger Equation in Momentum Space* proves it in that case and the proof transfers, because it uses only the transform and the Hermitian pairing.

The energy. The energy is the symbol evaluated at zero frequency, $E=\mathcal{S}(0,2\pi\vec\nu_{\Phi})$, which is the statement that the Hamiltonian is the generator of the frequency. On the shell the two agree with the dispersion relation, and off the shell the symbol is the energy the mode would have if it were on it.

What the mass term does to the two. The mass term shifts neither the charge nor the reality of the bilinear: it enters the symbol and leaves the pairing alone. What it does is remove the zero-frequency mode from the spectrum, and that removal is the count of degrees of freedom the article's structural section states.

## What the Principle Adds and What It Relabels: In Momentum Space

What the transform adds. One identity: the action at a fixed frequency is the quadratic form whose kernel is the symbol. That identity is worth having, because it turns the variational principle into linear algebra and the equation into a null space, and because it makes the reality of the action and the Hermiticity of the symbol one statement seen twice.

What it relabels. The variational principle itself: nothing is added to the physics, no new current appears, and no equation is solved that the parent did not already solve. The word *action* at a mode is a density in the frequency and the wave number, not an integral over a region, and calling it an action is a shorthand that this section keeps because the shorthand is the point.

What it cannot reach. The boundary term, the varying coefficient and the operator ordering. The first two need position space; the third is invisible at a constant symbol, where left and right multiplication agree. Each of those is named where the article meets it, and none is repaired by the transform.

## Open Questions

Is there an anti-Hermitian potential whose density is a total derivative? The exclusion in the reality part of §*The Action* is the exclusion of an anti-Hermitian part, because that part makes the action's density imaginary. An anti-Hermitian part that is a total derivative — one whose contribution to the action is a boundary term — would make the action real up to a surface term, and the variation would be unaffected. Whether such a potential exists in this algebra, whether it can be written as $\tilde\nabla_\Phi\tilde\Gamma$ for some $\tilde\Gamma$, and whether its spectrum is then admissible, is not decided. No claim is made in either direction.

Can the Peirce restriction be imposed inside one eigenspace? The eigenspace of a branch is a right ideal $\mathbb{B}w$, and its Hermitian representative is $ww^{*}$. Whether the physical restriction to a Peirce carrier — the question the parent's §*Open Questions* raises for a non-central coefficient — can be imposed inside one eigenspace without breaking the $i$-invariance that produces the doubling is open.

## Summary

The transform of the variational parent's coupled four-channel equation is one eigenvalue problem, $(\omega^{2}/c^{2}-4\pi^{2}\nu_{\Phi}^{2})\tilde\Xi_0=\tilde M\tilde\Xi_0$, with the parent's $c^{2}$ restored: the parent prints $\omega^{2}-c^{2}\nu_{\Phi}^{2}$, whose dimension is $\mathrm{T}^{-2}$ against the potential's $\mathrm{L}^{-2}$, and at $c=2$ the two forms differ by the factor $4$.

For a Hermitian $\tilde M=a\,e_t+i\vec v\cdot\vec e$ the spectrum is $a\pm\lvert\vec v\rvert$, each doubled, because $L(\vec v\cdot\vec e)^{2}=-\lvert\vec v\rvert^{2}I$ and the minimal polynomial is quadratic on a four-dimensional space. Measured at $3.1\times10^{-15}$ over three hundred draws. There are two eigenvalues and four frequencies, each doubled; "four branches" names the second count and hides the first.

The reality of the action selects the potential's sector and not its own: $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)$ is real for Hermitian $\tilde M$ and purely imaginary for anti-Hermitian, verified at $3.6\times10^{-15}$ and $7.1\times10^{-15}$. So the material sector is excluded by the reality of $S$, and the excluded case has a purely imaginary spectrum and a complex dispersion.

The lower branch is negative when $\lvert\vec v\rvert>a$, which happened in $276$ of $300$ random draws: the tachyon threshold is generic for unconstrained coefficients. The free case has all four eigenvalues at $\nu_m^{2}$ and a symbol that commutes with everything, so **the free scalar symbol carries no sector content and every sector statement belongs to the potential**.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Upsilon_\Phi=i\nu_t'e_t+\vec\nu_\Phi$ | The four-wavevector; $2\pi\nu_t'=\omega/c$ |
| $\langle\tilde\Upsilon_\Phi\rangle_\natural=-\nu_t'^{2}+\nu_{\Phi}^{2}$ | Its quaternionic norm |
| $\tilde M$ | The constant potential; Hermitian $a\,e_t+i\vec v\cdot\vec e$ or anti-Hermitian $i\,a\,e_t+\vec v\cdot\vec e$ |
| $L(\tilde M)$ | Left multiplication by $\tilde M$; complex-linear on $\mathbb{B}$ |
| $\operatorname{eig}L(\tilde M)=a\pm\lvert\vec v\rvert$ | The spectrum, each value twice |
| $\omega^{2}/c^{2}-\nu_{\Phi}^{2}$ | The eigenvalue of $\Box_\Phi$ in wave-number units |
| $\mathrm{Sc}(\tilde\Xi^{*}\tilde M\tilde\Xi)$ | The potential density; real iff $\tilde M$ Hermitian |
| $a\geq\lvert\vec v\rvert$ | The non-negativity condition; its failure is the tachyon threshold |
| $ww^{*}$ | The Hermitian representative of the eigenspace $\mathbb{B}w$ |

## Further Reading

- *The Lagrangian and the Klein–Gordon Equation*, for the action, the four scalar actions, the Hermitian pairing and the sentence this article completes.
- *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form*, for the same symbol read through its zero set and the factorization question.
- *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Polar Variables*, for the transform's phase as the action and the role of the amplitude.
- *The Klein–Gordon Equation in Biquaternionic Form*, for the plane waves, the dispersion relation and the verdict on the sector split.
- *Derivatives, Fields and Transforms*, for the transform, its kernel and the symbol rule.
- *Norm and Pairing Conventions*, for the Hermitian form and the centrality of the quaternionic norm.
- *The First-Order Root of the Biquaternion Klein–Gordon Operator*, for the spinor square root that the scalar operator does not have.
