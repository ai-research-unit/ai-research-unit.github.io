# __The Fourier Transform and the Coupled Proca Equation in Biquaternionic Form__

## Introduction

**The Proca field is the first in the corpus whose carrier has to be widened before a connection can be written, and the widening is forced by the connection itself.** *The Coupled Proca Equation in Biquaternionic Form* states the reason in its §*The Carrier*: the minimal substitution replaces the gradient by $\tilde\nabla_\Phi+\frac{i\varkappa}{\hbar}\tilde A_\Phi$, the product of two material potentials is not material because of the $i$ in the time slot, and the field therefore has to be a general biquaternion. **The $i$ that breaks closure is the $i$ the mass term needs**, which is why the massless Proca field can be a real potential and the massive one cannot.

**The article's subject is what the transform says about that widening, and the answer is a two-term symbol.** In the coupled theory the operator's symbol is the free symbol at a shifted four-wave-number, plus one extra term that is the curvature:

$$
\sigma_{\mathrm{gco}}\bigl(\pi\bigr)=\underbrace{\bigl(-\pi^{2}\delta^\mu{}_\nu-\pi^\mu\pi_\nu\bigr)}_{\text{the free symbol at }\pi}
\;+\;\underbrace{\frac{i\varkappa}{\hbar}\,F^{(\Phi)\mu}{}_{\nu}}_{\text{the obstruction}} ,
\qquad
\pi_\mu=\hbar k_\mu+\varkappa A_\mu .
$$

The first bracket is the free Proca symbol with $\pi$ in place of $k$ — translation and rank-one projector together — and the second is the commutator of two covariant derivatives. **The first term is what the transform says and the second is what the transform cannot say**, and the article is the separation of the two.

**The translation is exact and it is the corpus's own identity.** The parent proves $\tilde\nabla^{\natural}_{\mathrm{gco}}\tilde\nabla_{\mathrm{gco}}=\sum_\mu\tilde\nabla^{2}_{\mathrm{gco},\mu}+\frac{i\varkappa}{\hbar}\tilde F^{(\Phi)}$, a decomposition of the covariant d'Alembertian into a symmetric sum of squares and a curvature. **In frequency space the first piece is $-\pi^{2}$ and the second is the curvature term**, so the identity is exactly the symbol's two terms and the article's first finding is that no third term exists.

**The second finding is that the same four-wave-number can give different symbols.** Two connections can agree in $\pi$ at a point and disagree in $F$ there, and the symbol's difference is $\frac{i\varkappa}{\hbar}$ times the difference of the curvatures: for two connections used below, $\lvert F_{21}\rvert$ is $0$ and $0.9$ while $\pi$ agrees at the point of evaluation. **So the symbol is not a function of the momentum alone**, and that is the exact statement of what a Fourier description of a gauge theory loses.

**The third finding is that the mass does not enter the obstruction.** The mass term is $-k_m^{2}\delta$ on the amplitude space, which is inert under the curvature; the curvature term carries no $k_m$. **So the obstruction and the mass are two independent additions to the Klein–Gordon symbol**, and §*The Mass Does Not Enter the Obstruction* states the check.

**The fourth finding is a floor on how much a coefficient can hide.** The companions' bench measures the mode occupancy of a multiplication, a derivative of a delta and a general function on a $256$-mode circle: one mode, first order, and all $256$. **Covariant differentiation is the derivative's floor**, so a connection moves the symbol away from the free one by an amount the occupancy does not see, and the article quotes the bench rather than rerunning it.

**The denial is stated plainly.** No sector is exchanged. The coupled field is an element of $\mathbb{B}$, its transform is $\mathbb{B}$-valued, and the symbol is a matrix of numbers only at a constant connection. **The article adds the decomposition and its two failures: the failure of the symbol to be a function of $\pi$, and the failure of the ladder to reach the floor.**

## Conventions

The algebra, the products, the two forms, the units and the sectors are those of *Algebra and Element Conventions*, *Product and Form Conventions*, *Norm and Pairing Conventions*, *Physics Units and Common Elements Conventions* and *Mirror Biquaternions and the Phy–Psy Switch*. The gradient and the covariant derivative are those of *Operator and Calculus Conventions* and *Gauge Fields and the Covariant Derivative*, and the transform is the one of *Derivatives, Fields and Transforms*, whose symbol rule for a gauge-covariant operator is quoted in derived form:

$$
\tilde\nabla_{\mathrm{gco},\mu}\longmapsto i\pi_\mu ,
\qquad
\pi_\mu=\hbar k_\mu+\varkappa A_\mu ,
\qquad
k_\mu=\bigl(k_t',\vec k_\Phi\bigr) ,
\qquad
k_t'=\frac{\omega}{c} ,
$$

with $\varkappa$ the coupling and $A_\mu$ the background potential. **The shift is a translation of the wave number and not a scaling**: the coupling enters as a length and the potential as its inverse.

**The minimal substitution and the field strength are the parent's.** The substitution is $\tilde\nabla_\Phi\mapsto\tilde\nabla_\Phi+\frac{i\varkappa}{\hbar}\tilde A_\Phi$, and the covariant field strength is

$$
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_{\mathrm{gco}})^{\natural}\tilde A\bigr)
=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A\bigr)
+\frac{i\varkappa}{\hbar}\,\mathrm{Vect}\bigl(\tilde A_\Phi^{\natural}\tilde A\bigr) ,
$$

whose second term is the parent's extra piece, measured between $0.7$ and $12$ over one hundred random draws. **That term is a product of two fields and not a derivative**, and §*The Field Strength's Extra Term* is about what the transform does with it.

**The square-splitting identity is the parent's and it is the article's spine.** For a connection with curvature $F^{(\Phi)}$,

$$
(\tilde\nabla_{\mathrm{gco}})^{\natural}\tilde\nabla_{\mathrm{gco}}
=\sum_\mu\tilde\nabla^{2}_{\mathrm{gco},\mu}+\frac{i\varkappa}{\hbar}\tilde F^{(\Phi)} ,
\qquad
\bigl[D_{\mathrm{gco},\mu},D_{\mathrm{gco},\nu}\bigr]=\frac{i\varkappa}{\hbar}F^{(\Phi)}_{\mu\nu} ,
$$

the commutator checked on a test function to $1.1\times10^{-5}$. **The first display is the symbol's decomposition before the transform is applied**, and the transform turns the two terms into $-\pi^{2}$ and $\frac{i\varkappa}{\hbar}F^{(\Phi)}$.

**The constant-connection licence.** The symbol below is the symbol of a differential operator with constant coefficients, which requires a constant background. **A linear background is not constant and its symbol is not defined**; §*The Obstruction: Same Momentum, Different Curvature* handles that case by evaluating at a point and saying so.

**The denial of the Legendre reading, once.** The transform's variable is not a canonical momentum, and the parent's $d_\Phi=-i\hbar c\tilde\partial_\Phi+i\varkappa c\tilde A_\Phi$ is a covariant derivative and not a conjugate momentum. **The corpus's second conjugacy is the canonical one, and it is not used here.**

## The Symbol in Two Terms

**The transform acts on the identity and gives the decomposition, term by term.** Applying the symbol rule to the square splitting, the symmetric sum of squares becomes $-\pi^{2}$ — the four-momentum's interval with a sign — and the curvature term becomes $\frac{i\varkappa}{\hbar}F^{(\Phi)}$. **There is no third term because the identity has two**, and the article's first claim is only that the identity survives the transform unchanged.

**The identity is the d'Alembertian's and the Proca symbol adds two pieces of its own.** The square splitting decomposes $\tilde\nabla^{\natural}_{\mathrm{gco}}\tilde\nabla_{\mathrm{gco}}$, which is the covariant d'Alembertian; the Proca operator is that d'Alembertian less the projector onto the Lorenz form and less $k_m^{2}$. So the symbol's three pieces are the interval, the projector and the curvature, and the first two together are the free symbol at $\pi$. **The curvature is the only piece the free article has no counterpart for**, and every statement below about the obstruction is a statement about that piece alone.

**The translation term is a scalar and the curvature term is a matrix.** $-\pi^{2}$ is one number times the identity in the amplitude space; $\frac{i\varkappa}{\hbar}F^{(\Phi)}$ is a two-form's matrix, antisymmetric and traceless in the four-vector reading. **So the symbol is a scalar plus a traceless part**, and any statement about a trace is a statement about the translation alone.

**The curvature term's trace vanishes, which is the parent's Lorenz argument in frequency space.** The parent shows that taking the trace of the covariant equation removes the commutator, so the curvature does not enter the covariant Lorenz condition. **In the symbol's language: the trace of $\sigma_{\mathrm{gco}}$ is $-\pi^{2}\cdot4$ and has no curvature in it**, so the constraint's symbol is the free one at $\pi$. That single sentence is the whole of the parent's §*The Lorenz Condition in Covariant Form*, and the article states it as a trace.

**The curvature term is what makes the symbol non-scalar and it is what a gauge transformation cannot remove.** A gauge transformation shifts $A_\mu$ by a gradient, which shifts $\pi_\mu$ and leaves $F$ alone; so the symbol's translation moves and its obstruction does not. **That is the frequency-space form of gauge covariance: the symbol is not invariant, its two parts transform differently**, and the next section separates them.

## The Translation Is Exact

**For a constant connection the symbol is the free one at shifted momentum, and the shift is the only change.** With $F=0$ the second term vanishes identically, so

$$
\sigma_{\mathrm{gco}}\bigl(\pi\bigr)=-\pi^{2}\mathbb{1}
\qquad\text{when}\qquad
F^{(\Phi)}_{\mu\nu}=0 ,
$$

and the symbol's dependence on the coupling is entirely through $\pi_\mu=\hbar k_\mu+\varkappa A_\mu$. **The mass shell then reads $\pi^{2}=k_m^{2}$**, which is the parent's constant-background dispersion with the coupling in the momentum and nowhere else.

**The check is one line and it is exact.** A constant connection has $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu=0$ identically, so the commutator vanishes and the square splitting reduces to the symmetric sum of squares. **The symbol of that sum is $-\pi^{2}$**, and the identity is an identity and not an approximation.

**What the translation does to the spectrum is the parent's shift, read as a symbol.** The temporal component of $\pi$ is $\hbar\omega/c+\varkappa\varphi$, so the symbol's evenness is about $\omega=-\varkappa c\varphi/\hbar$ and not about zero. **A constant potential moves the axis of the symbol's parity**, which is the frequency-space form of "a constant potential shifts every energy by $\varkappa\varphi$".

**The spatial components shift the wave vector's origin, and that is the same statement.** $\vec\pi=\hbar\vec k_\Phi+\varkappa\vec A$ means the symbol's dependence on $\vec k_\Phi$ is a translation, so the dispersion's minimum sits at $\vec k_\Phi=-\varkappa\vec A/\hbar$. **A constant vector potential moves the dispersion's centre and not its shape**, and the symbol's translation is exactly that statement.

**The translation is therefore the entire content of "the coupling is a shift" and the obstruction is the entire content of "the coupling is not only a shift".** The article separates them because the corpus's literature separates them: the constant-background section of the parent is the translation, and its covariant field strength is the obstruction.

## The Obstruction: Same Momentum, Different Curvature

**Two connections can agree in $\pi$ at a point and disagree in $F$ there, and then the symbols differ.** That is the article's sharpest statement and it is a statement about what a Fourier description can and cannot represent. **Written as a display, at a point $r_0$:**

$$
\pi^{(1)}(r_0)=\pi^{(2)}(r_0)
\qquad\text{while}\qquad
F^{(1)}(r_0)\neq F^{(2)}(r_0)
\qquad\Longrightarrow\qquad
\sigma^{(1)}(r_0)\neq\sigma^{(2)}(r_0) ,
$$

the difference being $\frac{i\varkappa}{\hbar}(F^{(1)}-F^{(2)})$ and nothing else. **So the symbol at a point is not a function of the momentum at that point**, and a reading that computed the symbol from $\pi$ alone would be wrong by the curvature.

**The example is two connections that differ by a term linear in the coordinate, and the numbers are the parent's.** Take $A^{(1)}=0$ and $A^{(2)}$ with $A_2=0$ and $A_1=b\,r_2'$; the second is the parent's linear connection, whose curvature has $\lvert F_{21}\rvert=b=0.9$ and whose other components vanish. **At the point $r_0=(0,0,0,0)$ the two connections agree in every component**, because a linear connection vanishes at its own origin, and their curvatures differ there by a matrix with one independent component of size $0.9$.

**The consequence for a Fourier description is a limit and not a defect.** The transform diagonalises a constant-coefficient operator and does nothing for a variable one. **A background with curvature has no symbol**, and the closest a symbol can come is the constant-connection symbol at the background's value at a point. **The article's statement is that this approximation is exact in $\pi$ and wrong in $F$**, which is the sharpest form the limitation takes.

**What the parent's covariant field strength does with the same fact is the position-space version.** The extra term $\frac{i\varkappa}{\hbar}\mathrm{Vect}(\tilde A_\Phi^{\natural}\tilde A)$, measured between $0.7$ and $12$, is the same curvature's appearance in the field strength rather than in the operator. **Two registers, one object:** the symbol's obstruction and the field strength's extra term are both the commutator, and the article's §*The Field Strength's Extra Term* is the second register.

**The obstruction's rank is the curvature's rank and its trace is zero.** A two-form in four dimensions has rank four unless its invariants vanish, so the obstruction is a full-rank traceless addition in general; the trace's vanishing is what leaves the constraint untouched. **So the obstruction moves every eigenvalue of the symbol's transverse part and moves the constraint not at all**, and that asymmetry is why the covariant Lorenz condition is the free one in $\pi$.

## The Mass Does Not Enter the Obstruction

**The mass term is a multiple of the identity and the obstruction is traceless, so the two additions are independent.** The coupled equation's symbol in the four-component reading is

$$
\sigma_{\mathrm{gco}}=\bigl(-\pi^{2}-k_m^{2}\bigr)\delta^\mu{}_\nu+\frac{i\varkappa}{\hbar}F^{(\Phi)\mu}{}_{\nu}
-\pi^\mu\pi_\nu ,
$$

so the mass appears in one diagonal entry of the decomposition and the curvature in a different one. **Neither can be written in terms of the other**, and the check is that the obstruction's trace is zero at every $k_m$ and the mass's is $-4k_m^{2}$ at every $F$.

**The consequence is that the count cannot be changed by the coupling.** The mass's effect on the symbol's rank is the linear factor $-k_m^{2}$, which is the same at every curvature; the curvature's effect is traceless, so it cannot create or destroy the mass's factor. **The degrees-of-freedom count is therefore a property of the mass and of the constraint's structure, not of the background**, and the form companion's rank table survives the coupling with $\pi$ in place of $k$.

**The independence is visible in the eigenvalues at a constant connection.** With $F=0$ the eigenvalues are the free ones at $\pi$, and the two multiplicities $\{\pi^{2}-k_m^{2},\pi^{2}-k_m^{2},\pi^{2}-k_m^{2},-k_m^{2}\}$ are unchanged in *structure*; what changes is the value of $\pi^{2}$. **The coupling moves the numbers and not the multiplicities**, which is the same sentence as the mass's independence read forwards.

**What the independence does not say is that the coupling is spectroscopically invisible.** It says the coupling's effect on the *count* is nil. Its effect on the values is the whole of the constant-background dispersion, and its effect on the eigenvectors is the curvature's. **The article states three things and not one**, because the three are cheap and the confusion between them is not.

## The Field Strength's Extra Term

**The covariant field strength has a term the free one does not, and the transform makes it a product.** The parent's display

$$
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A\bigr)+\frac{i\varkappa}{\hbar}\mathrm{Vect}\bigl(\tilde A_\Phi^{\natural}\tilde A\bigr)
$$

has two terms of different kinds: a derivative of the field and a product of two fields. **The first has a symbol and the second does not**, because a product is a convolution in frequency space and a convolution is not a multiplier.

**The parent's measurement of the second term is the reason it cannot be dropped.** Over one hundred random draws at unit amplitude the term ranges from $0.7$ to $12$ in the units of the display, so it is not a small correction to the derivative term; it is comparable to it and sometimes larger. **A frequency-space account that kept only the derivative term would be wrong by an $O(1)$ amount**, and the article records the range rather than a mean.

**In frequency space the product is a convolution and it is the obstruction's second appearance.** The first appearance is the symbol's $\frac{i\varkappa}{\hbar}F$, which is a multiplier because a constant curvature is a constant; the second is the product term, which is not a multiplier because the potential is a function. **The two are one object seen at two levels of resolution**, and the article says so once and does not claim they are numerically equal.

**What the transform can say about the product is its support, and the companions' bench gives the numbers.** On a $256$-mode circle, a delta is a multiplier and occupies one mode; a derivative of a delta is first order and occupies a small window; a general function occupies all $256$. **A product with a general potential therefore occupies every mode**, which is the frequency-space statement of "the covariant field strength is not a local operator in the free field".

## The Ladder and Its Floor

**The companions' bench measures how far a multiplication can be from a diagonal action, and the floor is the derivative.** The three numbers are the three rungs: a delta is a multiplier and occupies one mode of $256$; a derivative of a delta is first order; a function is a convolution and occupies all $256$. **Covariant differentiation is the derivative's rung**, so it is first order and never diagonal.

**The article's use of the bench is a floor and not a measurement.** A connection's curvature term is a multiplier at constant curvature, so it sits on the delta's rung there; but the covariant derivative that produced it sits on the derivative's rung, and the product term sits on the function's. **The three rungs are occupied simultaneously in one expression**, which is why the coupled theory has a symbol in one limit and not in general.

**The floor is the reason the free theory's exactness is not misleading.** The free Proca symbol is exact because the coefficients are constant; the coupled one is exact only where the connection is, and the bench says how much of the structure the exactness buys: **everything at constant curvature, the translation term at every curvature, and nothing else.**

**The rungs are the companions' and the article does not rerun them.** *The Fourier Transform and the Coupled Klein–Gordon Equation in Biquaternionic Form* and *The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Form* establish the occupancy counts, and the article quotes them because the Proca case adds no rung. **The Proca case's addition is the second matrix index**: the field strength has two, so its product term is a matrix product and its convolution is a convolution of matrices, and the occupancy count is the same.

## Limits

**The constant-connection licence bounds the symbol and nothing else.** The translation term is exact for a constant connection; the obstruction is a multiplier only where the curvature is constant. **Every statement about the symbol above carries that condition**, and the article repeats it because the condition is easy to lose in a display.

**The Abelian case is the one treated.** The commutator's value is the curvature and there is no second term from the algebra's non-commutativity, because the coupling is Abelian. **A non-Abelian coupling would add a term to the field strength and the symbol would acquire a second obstruction**, and the article does not treat that case.

**The mass's independence is a statement about the symbol's structure and not about the spectrum's values.** The values move with the coupling through $\pi$; the multiplicities do not. **A reader who took "independent" for "invisible" would be reading the wrong half of the sentence.**

**The denial, once more.** No sector is exchanged. The coupled field is one element with eight real parameters, its transform is $\mathbb{B}$-valued, and the symbol is a matrix only at a constant connection. **None of the three is a statement about $\mathbb{B}_\Phi$ and $\mathbb{B}_\Psi$.**

## Open Questions

**Whether a frequency-space account of the obstruction exists at all is open.** The symbol's curvature term is exact at constant curvature, and the product term is a convolution; whether a transform-like object exists that diagonalises the second is not known to the article, and the companions raise the same question for their own fields.

**Whether the extra term's range $[0.7,12]$ has a bound is open.** The parent measures the range over random draws at unit amplitude and does not bound it. **A bound in terms of the amplitude's norm and the coupling would turn the range into an inequality**, and nothing above supplies one.

**Whether the mass's independence survives a non-Abelian coupling is open.** An obstruction of a different kind would have a different trace, and the trace's vanishing is what the constraint's survival rests on. **The article's independence argument uses the trace and would need redoing.**

**The covariant Lorenz condition's exactness is the parent's and it is quoted, not proved here.** The article's §*The Symbol in Two Terms* reads it as a trace; whether the trace argument and the parent's divergence argument are the same argument is a question about the two orders of differentiation, and it is not answered here.

## Summary

The coupled Proca operator's symbol is two terms. The first is the free symbol at the shifted four-momentum $\pi_\mu=\hbar k_\mu+\varkappa A_\mu$, which is the translation; the second is $\frac{i\varkappa}{\hbar}F^{(\Phi)}$, which is the commutator of two covariant derivatives and is the obstruction. **The decomposition is the parent's square-splitting identity, transformed term by term**, and there is no third term because the identity has two.

At a constant connection the obstruction vanishes identically and the symbol is $-\pi^{2}$ times the identity: **the translation is exact**, the dispersion is $\pi^{2}=k_m^{2}$, and a constant potential moves the axis of the symbol's parity to $\omega=-\varkappa c\varphi/\hbar$.

At a varying connection the obstruction is not removable. Two connections can agree in $\pi$ at a point and differ in $F$ there — the example is $A^{(1)}=0$ against $A^{(2)}$ with $A_1=b\,r_2'$, whose $\lvert F_{21}\rvert=0.9$ while both connections vanish at the origin. **So the symbol at a point is not a function of the momentum at that point**, and a Fourier description is wrong by exactly the curvature.

The mass does not enter the obstruction: the mass term is $-k_m^{2}\delta$, whose trace is $-4k_m^{2}$, and the obstruction is traceless at every $k_m$. **The coupling therefore cannot change the count**, only the values and the eigenvectors, and the form companion's rank table survives with $\pi$ in place of $k$. The field strength's extra term, the parent's product of two fields ranging from $0.7$ to $12$, is the same object in the other register, and in frequency space it is a convolution: the bench's ladder reads one mode for a delta, first order for its derivative, and all $256$ for a general function.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\varkappa$ | The coupling; a length whose inverse multiplies the potential |
| $A_\mu$ | The background potential |
| $\pi_\mu=\hbar k_\mu+\varkappa A_\mu$ | The shifted four-momentum; the symbol's argument |
| $k_t'=\omega/c$, $k^{2}=k_t'^{2}-\vec k_\Phi^{2}$ | The free four-wave-number and its interval |
| $k_m=mc/\hbar$ | The mass wave number |
| $\sigma_{\mathrm{gco}}=-\pi^{2}+\frac{i\varkappa}{\hbar}F^{(\Phi)}$ | The coupled symbol; translation plus obstruction |
| $F^{(\Phi)}_{\mu\nu}$ | The curvature; $\lvert F_{21}\rvert=0.9$ in the example |
| $\frac{i\varkappa}{\hbar}\mathrm{Vect}(\tilde A_\Phi^{\natural}\tilde A)$ | The field strength's extra term; $0.7$ to $12$ over $100$ draws |
| $-\pi^{2}$ | The trace part; the constraint's symbol |
| $256$ | The mode count of the companions' bench; one, a few, all |

## Further Reading

- *The Coupled Proca Equation in Biquaternionic Form*, for the carrier argument, the minimal substitution, the covariant field strength and the constant background.
- *The Coupled Proca Equation in Biquaternionic Polar Variables*, for the same theory read in the chart, and for the gauge transformation as a phase translation.
- *Gauge Fields and the Covariant Derivative*, for the commutator, the curvature and the square-splitting identity.
- *The Fourier Transform and the Proca Equation in Biquaternionic Form*, for the free symbol's determinant, rank and kernel.
- *The Fourier Transform and the Coupled Klein–Gordon Equation in Biquaternionic Form*, for the occupancy bench and the ladder's rungs.
- *The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Form*, for the same ladder with a first-order operator.
- *The Fourier Transform and the Coupled Proca Equation in Biquaternionic Polar Variables*, for the chart reading of this symbol.
- *Derivatives, Fields and Transforms*, for the symbol rule.
- M. Nakahara, *Geometry, Topology and Physics* (Adam Hilger, 1990), Chapter 10, for the curvature as a commutator and the square splitting.
- L. H. Ryder, *Quantum Field Theory* (Cambridge University Press, 2nd ed., 1996), Chapter 3, for the covariant derivative's symbol and the constant-background dispersion.
