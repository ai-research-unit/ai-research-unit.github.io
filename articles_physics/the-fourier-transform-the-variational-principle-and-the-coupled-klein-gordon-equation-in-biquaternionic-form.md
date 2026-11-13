# __The Fourier Transform, the Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Form__

## Introduction

**The variational parent records a mismatch and leaves it open, and the mismatch is not where it says it is.** *The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Form* writes, at §*The Variation in the Field*, that the action's pairing of the two factors in the temporal slot is $\partial^{2}_{R_t}-(ϙa_t'/\hbar)^{2}$ while the article's equation carries $(\partial_{R_t}-ϙa_t'/\hbar)^{2}$, and it calls the difference "one bookkeeping choice, stated rather than absorbed". The two displays differ by a cross term, and the parent is right that a cross term is at stake. It is wrong about which side of the mismatch each display belongs to.

**The transform settles the attribution in one measurement.** The action of the temporal slot is a modulus squared, and its Euler–Lagrange operator can be read off by differentiating the functional. Done on a grid of $256$ points the linear term of the variation reproduces $2\,\mathrm{Re}\langle(\partial_{R_t}+c_t)^{2}\Xi,\eta\rangle$ to two parts in $10^{11}$, and the action's density on a plane wave is $10.956100$ — which is the *squared* symbol and not the paired one, which is $8.903900$. **The action and the equation agree; the paired form is a third object, and it is what the parent's first display describes.**

**The finding is that a real action is a weaker condition than a real symbol.** A modulus squared is real for every complex coefficient, so the action cannot be the criterion for the reality of a symbol. What makes the symbol real is that the operator's coefficients are real in the slot basis, and by the parity lemma of the main article that is exactly the anti-Hermitian writing of the connection. The reality of the action is satisfied always; the reality of the symbol is satisfied exactly in the corpus's writing. **The gap between the two is the parity lemma, and the lemma is the content of the variational principle in this case.**

**The second finding is that the parent's two ambiguities are one.** The sign of the charge and the order of the two first-order factors are not two questions: the paired form *is* the product of the two charge-conjugate factors, so flipping the charge and reordering the factors are the same operation. The symbol records both in one place, the cross term $2c_t(c_t-k_t')$, which is $2.0522$ at the values used throughout and is real.

**The article is a clarification and it does not arbitrate.** It does not say that the action is the right starting point, that the paired form is wrong, or that either equation should be adopted. It says which functional produces which operator, and it says that the property which survives all the choices is the reality of the symbol — not the reality of the action, which was never in doubt.

**The register note.** This is the variational reading of the main article's symbols; the polar companion reads them in the word, and the main article states the class theorem they both use. The action, the two variations, the Noether currents and the source are the parent's, and they are cited rather than restated.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient and the d'Alembertian those of *Operator and Calculus Conventions*, the two forms those of *Norm and Pairing Conventions*, the units and the material time those of *Physics Units and Common Elements Conventions*. The action is the parent's $S_{\mathrm{c}}$, the slot-summed functional whose Euler–Lagrange equation the element companion calls E2, and the connection is the parent's anti-Hermitian writing $\tilde A_\Phi=i a_t'e_t+\vec A$ with $a_t'$ and $\vec A$ real. The symbol rule is quoted in its derived form and not re-derived:

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi,
\qquad
\Box_\Phi\longmapsto-\langle\tilde K_\Phi\rangle_\natural,
\qquad
\tilde K_\Phi=ik_t'e_t+\vec k_\Phi .
$$

**The bookkeeping is the main article's and is quoted once.** With $c_\mu=\frac{i\,ϙ}{\hbar}A_\mu$ the material connection gives $c_t=-\frac{ϙa_t'}{\hbar}$ real and $c_\eta=i\frac{ϙ}{\hbar}A_\eta$ imaginary, and the free slot symbols are $\sigma_t=-k_t'$ real and $\sigma_\eta=i\kappa_\eta$ imaginary. The temporal slot is the only one where the two readings of the covariant square differ, so the article states everything in that slot and adds the spatial slots only where they change a conclusion.

**The denials are the main article's, restated once.** The transform does not exchange sectors; a symbol exists only at constant coefficients; and a Legendre transform between a field and its conjugate momentum is not a Fourier transform, so the parent's four canonical momenta are not wave numbers and no display below reads them as one.

## Reality of the Action Is Weaker Than Reality of the Symbol

**The action is real for every connection, and that is an identity rather than a measurement.** The kinetic term is $\mathrm{Sc}\big[(\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi)^{*}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi\big]$, a modulus squared summed over four slots, and a modulus squared is real for any complex coefficient whatsoever. **No choice of connection can make the action complex**, so no argument from the reality of the action can select a connection, and the parent's care over the temporal slot is not about the reality of $S$.

**The symbol is real only in the corpus's writing, and the difference is the whole content.** Applying the parity lemma of the main article, the squared symbol $\sum_\mu(\sigma_\mu+c_\mu)^{2}$ is real in the temporal slot when $c_t$ is real — that is, when $A_t$ is imaginary — and real in a spatial slot when $c_\eta$ is imaginary — that is, when $A_\eta$ is real. Both conditions together are $\tilde A_\Phi^{*}=-\tilde A_\Phi$. **A modulus squared is real for every $c$; a symbol is real for the anti-Hermitian $c$ and for no other.**

**The gap between the two conditions is one slot deep.** Take a real $A_t$, which is what a four-potential written in ordinary coordinates suggests. Then $c_t$ is imaginary, the action is still real, and the symbol is $(\sigma_t+i\lvert c_t\rvert)^{2}=k_t'^{2}-2ik_t'\lvert c_t\rvert-\lvert c_t\rvert^{2}$: real part $k_t'^{2}-\lvert c_t\rvert^{2}$, imaginary part $-2k_t'\lvert c_t\rvert$. **The action reports nothing and the symbol reports a complex number**, and the complex number is exactly the shape of the one the path-integral companion measures for a wrong-parity coefficient.

**So the variational principle's role here is narrower than it looks.** It supplies the operator, and it does not supply the criterion. The criterion is the parity lemma, which is an observation about the square of a complex number and needs no action at all.

## The Action's Operator

**The action's Euler–Lagrange operator is the squared one, and the measurement is decisive.** For the temporal slot with a constant $c_t$ the functional is $S_t=\int\bigl\lvert(\partial_{R_t}+c_t)\Xi\bigr\rvert^{2}$, and its variation is computed twice: once by the analytic reading $\delta S_t/\delta\Xi^{*}=(\partial_{R_t}+c_t)^{2}\Xi$, and once by differencing the functional itself at $\Xi\pm h\eta$ with $h=10^{-5}$ and a two-mode probe $\eta$. The linear term of the difference is $96.374889164$ and the analytic prediction $2\,\mathrm{Re}\langle(\partial_{R_t}+c_t)^{2}\Xi,\eta\rangle$ is $96.374889162$: a ratio of $1.000000000020$.

**The action's density on a plane wave is the squared symbol and not the paired one.** With $k_t'=3$ and $c_t=-0.31$ the functional's density is $10.956100$, the squared symbol is $10.956100$, and the paired symbol is $8.903900$. The two candidates differ by $2.0522$ and the action is on the squared side by the whole of it. **The identification is exact, not approximate**, and it is what the box records:

$$
\boxed{\;
\frac{\delta S_{\mathrm{c}}}{\delta\tilde\Xi^{*}}
=-\Bigl(\Box_{\mathrm{gco}}-k_m^{2}\Bigr)\tilde\Xi
\;}
$$

**What this does to the parent's recorded mismatch.** The parent's second display, $(\partial_{R_t}-ϙa_t'/\hbar)^{2}$, is the action's slot with $c_t=-ϙa_t'/\hbar$, so the parent's *equation* side is the action's operator and the two agree. The parent's first display, $\partial^{2}_{R_t}-(ϙa_t'/\hbar)^{2}$, is $\partial^{2}-c_t^{2}$: the paired form, which no functional in the parent produces. **The mismatch is real but it is not between the action and the equation**; it is between the action and a third object the parent wrote down as though it were the action's.

**The correction is an attribution and not an equation.** Nothing in the parent's displays is wrong as a display. $\partial^{2}_{R_t}-(ϙa_t'/\hbar)^{2}$ is a perfectly good operator and the article of §*The Ordering Ambiguity Is the Cross Term* identifies its symbol. What is wrong is the sentence that attaches it to the action. **The corpus's action and the corpus's equation are one operator**, and the third object is the subject of the next section.

## The Ordering Ambiguity Is the Cross Term

**The paired form is the product of the two charge-conjugate first-order operators.** Writing the two factors as $(\partial_{R_t}-\bar c_t)$ and $(\partial_{R_t}+c_t)$, their product is $\partial^{2}_{R_t}+\partial_{R_t}(c_t-\bar c_t)-\lvert c_t\rvert^{2}$, and for a real $c_t$ the middle term vanishes and the product is $\partial^{2}-c_t^{2}$. **The squared form is the product of one factor with itself**, $(\partial_{R_t}+c_t)^{2}=\partial^{2}+2c_t\partial+c_t^{2}$, and the two differ by

$$
\bigl(\partial+c_t\bigr)^{2}-\Bigl(\partial^{2}-c_t^{2}\Bigr)=2c_t\bigl(\partial+c_t\bigr),
$$

which is the corpus's own identity at the temporal slot and which is first order in the derivative and in the potential.

**In momentum space the difference is one number per wave number.** The identity's symbol is $2c_t(\sigma_t+c_t)$, and with $\sigma_t=-k_t'$ it is $2c_t(c_t-k_t')$: real, of magnitude $2.0522$ at $k_t'=3$ and $c_t=-0.31$. **The ordering ambiguity decides whether the cross term survives**, and its survival is the difference between a linear and a quadratic response to the potential.

**The paired form is the two-charge reading and the squared form is the one-charge reading.** The factor $(\partial_{R_t}+c_t)$ carries the charge $+ϙ$ and the factor $(\partial_{R_t}-\bar c_t)$ carries $-ϙ$; the squared form uses $+ϙ$ twice and the paired form uses $+ϙ$ and $-ϙ$ once each. **A second-order operator is therefore ambiguous between "the same charge twice" and "the two opposite charges once each"**, and that is the ordering ambiguity in one sentence.

**Nothing in the parity lemma distinguishes the two readings.** Both are real in the corpus's writing, because both are built from real coefficients there. The lemma decides reality; the ordering decides the power of the response. **The article keeps them apart because they are decided by different arguments.**

## The Charge Ambiguity Translates the Pair

**Flipping the charge translates the roots and leaves their separation.** The squared shell is $(k_t'-c_t)^{2}=\lvert\vec\kappa\rvert^{2}+k_m^{2}$; at $k_m=0.7$ and $\lvert\vec\kappa\rvert=3$ its roots with $c_t=-0.31$ are $+2.770584$ and $-3.390584$, and with $c_t=+0.31$ they are $+3.390584$ and $-2.770584$. **The separation is $6.161169$ in both cases and the pair translates by $-2c_t=0.62$**; the symbol at a fixed wave number moves from $10.956100$ to $7.236100$.

**So the sign of the charge is the sign of the linear response.** A charge-conjugated field in the same potential shifts the other way, and the shift is the whole of the effect at first order. **The charge ambiguity is visible in momentum space as a translation of the root pair** and it is not visible as a change of the separation, which is why a mass measurement cannot see it.

**And it is the same operation as the reordering.** The two factors of the paired form differ in exactly the charge they carry, so exchanging them is charging one of them oppositely; flipping the sign of $c_t$ in the squared form is charging both. **The sign ambiguity and the order ambiguity are the same functional read twice**, and the parent's two sentences about the temporal slot are two descriptions of one object.

**What this means for the parent's question.** The parent asks whether the temporal slot's cross term belongs to the energy or to the derivative. In momentum space the answer is that the cross term belongs to neither on its own: it is the difference between the one-charge and the two-charge readings, and the energy-versus-derivative question is the same question asked in position space, where the two readings are two operators related by an integration by parts.

## They Are One Question

**The one criterion that survives all the choices is the reality of the symbol.** Both readings, both signs of the charge, and both orderings give real symbols in the corpus's anti-Hermitian writing, and none of them does in a writing with a real temporal potential. **So the invariant is the parity condition**, and the variational principle's contribution is to say that it is the condition under which the operator the action produces is real-coefficient.

**The three statements of the invariant agree.** The parity lemma states it slot by slot; the anti-Hermiticity of $\tilde A_\Phi$ states it once; the requirement that the operator's coefficients be real in the $R$-slot basis states it in the language of the functional. **They are one condition written three ways**, and the article states all three because a reader arriving from any of the three directions should meet the same sentence.

**What the invariant does not do is choose between the readings.** A reader who wants the variational principle to select E2 over E1 will not get it from the reality of the symbol, because both are real. **The selection, where there is one, is the action's**, and the action's operator is the squared one — that is the previous section, and it is a different kind of statement.

## The Source's Symbol

**The connection's equation is algebraic only in the constant setting, and there its symbol is the current's transform.** Varying the matter action with respect to $A_\mu$ gives $\delta S_{\mathrm{c}}/\delta A_\mu=-\frac{ϙ}{\hbar}J_\mu$, and the transform of that equation replaces the derivative by $i\tilde K_\Phi$; the current is a bilinear, so its transform is a convolution and the connection's equation is algebraic only where the current is a single mode. **The source's symbol is therefore the transform of the current, and it is a convolution in every other case.**

**The constant setting is the one the article uses and the one the parent uses.** There the current's transform is a coefficient at one wave number, the connection's equation is algebraic, and the fork of §*The Ordering Ambiguity Is the Cross Term* is the fork between two polynomials in the same variable. **Nothing in the source's structure decides which polynomial is the operator's**, and the article states this rather than reading a decision into the variation.

## Limits

**The constant-coefficient licence bounds the article.** The Euler–Lagrange operator of §*The Action's Operator* is read at constant $c_t$; a varying potential makes the functional's variation a differential operator of higher order in the coefficient and the identification with a symbol fails there, as the main article's ladder records.

**The temporal slot is the only one where the two readings differ.** In a spatial slot $\bar c_\eta=-c_\eta$, the cross term vanishes identically, and the action, the squared form and the paired form are one operator. **A vector potential therefore gives no ordering ambiguity**, and the article does not manufacture one.

**The self-adjointness argument is not used.** Both readings are self-adjoint in the corpus's writing, so the standard criterion that a real action's operator be self-adjoint does not separate them. The article derives the separation from the cross term instead, and says so because the weaker argument is tempting.

## Open Questions

**The paired form's functional is not identified.** Both operators are self-adjoint at constant coefficients, so both are the Euler–Lagrange operators of some real quadratic functional, and the article exhibits the difference between the two functionals as the cross term without exhibiting the paired functional itself. Whether it is the cross bilinear $\int\bigl[(\partial_{R_t}-\bar c_t)\Xi\bigr]^{*}\bigl[(\partial_{R_t}+c_t)\Xi\bigr]$ and whether that object has a name in the standard literature is open. **The question is well posed because the operator is self-adjoint**, and nothing in the article answers it.

**Whether the corpus wants the first-order response is the parent's question and it is not answered here.** The action's operator shifts the energy linearly and the paired form shifts the mass squared; the difference is $2c_t(c_t-k_t')$ and it is first order in the potential. Which of the two the physics follows is a question about the corpus's choice of equation, and the article records the two responses without ranking them.

## Summary

The action of the coupled scalar theory is a modulus squared, so it is real for every connection, and the reality of the action is therefore not the criterion for the reality of the symbol. The criterion is the parity lemma of the main article: the symbol is real in a slot exactly when the connection's coefficient has the reality of that slot's gradient symbol, and in the corpus's slots that is the anti-Hermitian writing $\tilde A_\Phi^{*}=-\tilde A_\Phi$.

The action's Euler–Lagrange operator is the squared one. Its variation reproduces $2\,\mathrm{Re}\langle(\partial_{R_t}+c_t)^{2}\Xi,\eta\rangle$ to two parts in $10^{11}$, and its density on a plane wave is $10.956100$, which is the squared symbol against the paired symbol's $8.903900$. **The parent's recorded mismatch between its action and its equation therefore does not exist**: the two agree, and the parent's first display, $\partial^{2}_{R_t}-(ϙa_t'/\hbar)^{2}$, is the paired form, a third object.

The two ambiguities are one. The paired form is the product of the two charge-conjugate first-order operators and the squared form is one factor with itself, so flipping the charge and reordering the factors are the same operation. The symbol records both in the cross term $2c_t(\partial_{R_t}+c_t)$, whose value is $2c_t(c_t-k_t')=2.0522$. The charge flip translates the root pair by $-2c_t=0.62$ and leaves the separation at $6.161169$; the ordering decides whether the cross term survives at all.

Both readings are real in the corpus's writing, so the reality of the symbol cannot choose between them; what it does is mark the writing in which either can be real. The residual is that the paired form's own functional is not identified, and that which response the physics follows is the parent's question, restated as a question about a power.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $S_{\mathrm{c}}$ | The parent's slot-summed matter action |
| $\delta S_{\mathrm{c}}/\delta\tilde\Xi^{*}$ | The Euler–Lagrange operator; $-\bigl(\Box_{\mathrm{gco}}-k_m^{2}\bigr)\tilde\Xi$ |
| $c_\mu=\frac{iϙ}{\hbar}A_\mu$ | The per-slot connection coefficient; $c_t=-ϙa_t'/\hbar$ real, $c_\eta$ imaginary |
| $\sigma_\mu$ | The free slot symbol; $\sigma_t=-k_t'$ real, $\sigma_\eta=i\kappa_\eta$ imaginary |
| $(\partial_{R_t}+c_t)^{2}$ | The squared reading; one charge twice |
| $(\partial_{R_t}-\bar c_t)(\partial_{R_t}+c_t)$ | The paired reading; the two opposite charges once each |
| $2c_t(\partial_{R_t}+c_t)$ | Their difference as operators; symbol $2c_t(c_t-k_t')=2.0522$ |
| $10.956100$, $8.903900$ | The action's density and the squared symbol, against the paired symbol |
| $-2c_t$ | The translation of the root pair under a flip of the charge |

## Further Reading

- *The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Form*, for the action, the two variations, the Noether currents and the recorded mismatch this article attributes.
- *The Fourier Transform and the Coupled Klein–Gordon Equation in Biquaternionic Form*, for the parity lemma, the two symbols and the corrected shells.
- *The Fourier Transform and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables*, for the same ordering term read in the word.
- *The Coupled Klein–Gordon Equation in Biquaternionic Form*, for the two equations, the covariant square and the prohibition.
- *Derivatives, Fields and Transforms*, for the symbol rule and the transform of a product.
- *Norm and Pairing Conventions*, for the Hermitian form and the modulus squared.
- *The Gauge Principle in Biquaternionic Form*, for the localization of the central phase and the sign of the coupling.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 2, for the minimal substitution and the constant-potential shift.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 4th ed., 1975), §17, for the coupling prescription in the standard language.
