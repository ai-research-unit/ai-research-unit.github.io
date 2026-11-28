# __The Generating Functional and the Exact Gaussian: The Quadratic Part Inverted into the Propagator__

## Introduction

**The claim.** The second stage of the method computes nothing and answers the question of what could be computed. The theory is the generating functional $Z[J]$; every correlator is a derivative of it with respect to the source; and the reason the functional is computable at all is that its quadratic part is a Gaussian. The Gaussian is integrated exactly, and its inverse is the propagator. Stages $1$ and $2$ are one article because they are one sentence: *here is the integral, and here is the one part of it that closes.*

**What the stage produces.** Three objects, and each is used by everything after it.

| object | what it is | where it goes |
|---|---|---|
| $Z[J]$ | the generating functional, with the source | every correlator, by differentiation |
| $\Delta=W^{-1}$ | the inverse of the quadratic operator | the propagator, and every internal line |
| $(\det W)^{-1/2}$ | the Gaussian's leftover | the vacuum bubbles, and the one-loop determinant |

**The strongest objection.** *The functional integral is not a definition; nothing infinite-dimensional is exact.* The objection is half right, and the article states which half. The Gaussian is exact per mode: the operator is inverted exactly, and the algebra of the inversion is finite at every momentum. What is not exact is the measure, and the measure is not the algebra's. The exactness claimed here is exactness of the inversion, which is the whole of what the propagator needs.

**Position.** Stage $1$ and stage $2$ of the chain in [the hub](the-lagrangian-method-from-the-collected-lagrangian-to-the-feynman-diagram.html), and the article that turns the collection of [stage $0$](the-collection-of-lagrangian-components-the-full-action-as-the-input-to-perturbation-theory.html) into the vertices and lines of [stage $3$](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html).

## The Generating Functional

**One functional carries the theory.** With the source $J$ coupled to the field,

$$
Z[J]=\int\mathcal D\phi\;\exp\Bigl(i\theta_{\mathrm{act}}+i\theta_{\mathrm{src}}\Bigr),\qquad
\theta_{\mathrm{act}}=\frac{2\pi}{h}\mathrm{Re}\,S[\phi],\qquad
\theta_{\mathrm{src}}=\frac{2\pi}{h}\int J\phi,
$$

and the correlators are its derivatives,

$$
\bigl\langle\phi(r_{1})\cdots\phi(r_{n})\bigr\rangle
=\frac{1}{Z[0]}\Bigl(\frac{h}{2\pi i}\Bigr)^{n}
\frac{\delta^{n}Z[J]}{\delta J(r_{1})\cdots\delta J(r_{n})}\Biggr|_{J=0}.
$$

**The whole of the method is a statement about this one line.** "What does the theory predict?" becomes "can this integral be computed?" The theory is not silent about the answer; it says that the answer is a derivative of an integral whose non-Gaussian part is a polynomial. That is the fact the next stage exploits.

**The exponent's two parts are the corpus's own, and they must not be conflated.** The real part of the action gives the phase $\theta_{\mathrm{act}}$, which is what oscillates and what makes the integral a stationary-phase problem. The imaginary part gives $\kappa_{\mathrm{act}}$, the damping that decides which configurations dominate. [The Functional Integral in Biquaternionic Form](the-functional-integral-in-biquaternionic-form.html) states both, and states what the algebra supplies to each: the central imaginary supplies the phase, and the Wick rotation supplies the Euclidean weight. Neither is chosen by the algebra.

## The Split and the Shift

**Two lines turn a non-Gaussian integral into a Gaussian one times an operator.** Write $S=S_{2}+S_{\mathrm{int}}$, shift the integration variable by the classical response to the source, and note that a functional derivative in $J$ is a multiplication by $\phi$ inside the integral. Then

$$
Z[J]=\exp\Bigl(iS_{\mathrm{int}}\bigl[\tfrac{\delta}{i\delta J}\bigr]\Bigr)\,Z_{0}[J],
\qquad
Z_{0}[J]=\int\mathcal D\phi\;\exp\Bigl(i\theta_{2}+i\int J\phi\Bigr).
$$

**The identity is exact and it is the whole content of "perturbation theory".** No approximation has been made. The non-Gaussian part has been moved out of the integral and into an operator acting on the Gaussian's value. Everything after this line is either the evaluation of $Z_{0}$ or the expansion of that operator.

**The shift is where the source's meaning is fixed, and where the factor of $\frac{h}{2\pi}$ enters.** Completing the square in $Z_{0}$ gives the exponent $-\frac{1}{2}\int J\Delta J$ with

$$
\Delta=\frac{h}{2\pi}\,i\,W^{-1},
$$

so the source couples to the field through the propagator, and the two-point function at zeroth order in the interaction is $\Delta$ itself. The $\frac{h}{2\pi}$ is what the correlator formula's $\bigl(\frac{h}{2\pi i}\bigr)^{n}$ demands: each derivative brings $\frac{2\pi}{h}$ of field, and the two factors must cancel in a two-point function. In the units $\frac{2\pi}{h}=1$, which the rest of the section uses, $\Delta=iW^{-1}$ and the exponent is $-\frac12\int J\Delta J$ with no visible $h$. That is the sentence the diagrams call *the internal line is the propagator*.

**The operator's argument is a derivative, and the derivative is with respect to the source.** Writing $S_{\mathrm{int}}[\delta/i\delta J]$ means: replace every field in the interaction by $\delta/i\delta J$, then act on $Z_{0}$. Each derivative brings down one factor of $\Delta J$ or one $\Delta$ from the exponent, which is why the expansion produces exactly the two objects the diagrams draw: lines and vertices.

## The Gaussian, Exact

**The finite-dimensional identity is elementary, and the field case is the same identity per mode.**

$$
\int\mathrm{d}^{n}x\;\exp\Bigl(-\tfrac12x^{T}Ax+J^{T}x\Bigr)
=\bigl(\det A\bigr)^{-1/2}\exp\Bigl(\tfrac12J^{T}A^{-1}J\Bigr).
$$

**The identity was checked by exact quadrature, not by trusting the formula.** For one hundred random positive-definite $2\times2$ matrices and one hundred random sources, and again in dimension four, the integral was computed in the eigenbasis of $A$, where it factorises into one-dimensional quadratures, and compared with the closed form: the largest relative deviation over the hundred samples was $8.3\times10^{-15}$ at $2\times2$ and $1.4\times10^{-14}$ at $4\times4$, which is the quadrature's own error and not the identity's. The check is small and it fixes the sign of the exponent, which is the one thing a reader is entitled to doubt.

**The corpus's version differs by the measure and by the pairing.** With $\langle\cdot,\cdot\rangle_{\mathbb R}$ the real part of the scalar pairing and $W$ the quadratic operator,

$$
\int\mathcal D\tilde\Xi\;\exp\Bigl(-\tfrac12\bigl\langle\tilde\Xi,W\tilde\Xi\bigr\rangle_{\mathbb R}
+\bigl\langle J,\tilde\Xi\bigr\rangle_{\mathbb R}\Bigr)
=\bigl(\det W\bigr)^{-1/2}\exp\Bigl(\tfrac12\bigl\langle J,W^{-1}J\bigr\rangle_{\mathbb R}\Bigr),
$$

and the $i$ that the Minkowski weight carries is the central imaginary, which turns the exponent into the phase $\theta_{\mathrm{act}}$. [The Functional Integral in Biquaternionic Form](the-functional-integral-in-biquaternionic-form.html) states the rotation and what it costs.

**The determinant is what is left over, and it is not zero.** $(\det W)^{-1/2}$ is the vacuum's own factor, and its logarithm is the one-loop effective action of [The Functional Determinant](the-functional-determinant-in-biquaternionic-form.html). A computation that wants correlators divides it out; a computation that wants the vacuum energy keeps it. The article below treats it as the closed loop it is.

## The Inverse Is the Propagator

**The quadratic operator is inverted exactly, and its inverse is called the propagator.** In the corpus's chart the scalar's operator is

$$
W=\Box_{\Phi}-4\pi^{2}\nu_{m}^{2},\qquad \nu_{m}=\frac{mc}{h},
$$

and its momentum-space symbol is $-\mathcal M(\tilde Q_{\Phi})$, with $\mathcal M$ the mass-shell operator $N(\tilde Q_{\Phi})+m^{2}c^{2}$. The propagator is therefore

$$
\Delta(\tilde Q_{\Phi})=\frac{i}{-\mathcal M(\tilde Q_{\Phi})+i\epsilon}
=\frac{i}{-\bigl(N(\tilde Q_{\Phi})+m^{2}c^{2}\bigr)+i\epsilon}.
$$

**The sign was checked, because the whole chain hangs on it.** With $N(\tilde Q_{\Phi})=-\frac{E^{2}}{c^{2}}+\vec p^{\,2}$ and $p_{0}=\frac{E}{c}$,

$$
-\mathcal M(\tilde Q_{\Phi})=-N(\tilde Q_{\Phi})-m^{2}c^{2}=p_{0}^{2}-\vec p^{\,2}-m^{2}c^{2},
$$

which is the standard $p^{2}-m^{2}$ in the $(+,-,-,-)$ convention. The sign is the one the corpus's [Feynman propagator article](the-feynman-propagator-in-biquaternionic-form.html) displays, and the displayed formula and the inversion agree. A reader who writes $i/[\mathcal M+i\epsilon]$ instead has the pole on the wrong side of the axis and the wrong sign in every loop.

**The free propagation is the whole content of the quadratic part.** Nothing else is claimed: $\mathcal L_{2}$ inverts to $\Delta$, and $\Delta$ is what a line means. The mass, the wave operator and the $i\epsilon$ all sit in the one operator, and the propagator is what remains when it is inverted.

**The fermion's inverse is the same inversion with a numerator.** For the Dirac field the operator's symbol is the action $\mathcal A_{p}$, whose inverse is $(\mathcal A_{p}+mc)/(-\mathcal M+i\epsilon)$; the numerator is the spin sum, and its rank is two. [The Feynman Propagator](the-feynman-propagator-in-biquaternionic-form.html) writes the element form, and [The LSZ Reduction Formula](the-lsz-reduction-formula-in-biquaternionic-form.html) shows that the residue is the spin sum and not a scalar.

| rung | the operator $W$ | the propagator | what the inverse is |
|---|---|---|---|
| central scalar | $\Box_{\Phi}-4\pi^{2}\nu_{m}^{2}$ | $i/[-\mathcal M+i\epsilon]$ | one scalar function |
| Dirac | the action $\mathcal A_{p}$ | $i(\mathcal A_{p}+mc)/[-\mathcal M+i\epsilon]$ | a rank-two spin sum |
| connection, unfixed | $p^{2}\delta_{\imath\jmath}-p_{\imath}p_{\jmath}$ | none: singular on $p$ | nothing, until the representative is fixed |
| connection, fixed | the $R_{\xi}$ kernel | the transverse part plus the $\zeta$ part | one matrix, invertible |

**The third row is the row that fails, and it fails before any loop is drawn.** The unfixed connection's kernel annihilates the momentum itself, $p^{2}p_{\imath}-p_{\imath}p^{2}=0$ identically, so its spectrum is $\{p^{2},p^{2},0\}$ for every momentum and $p$ is the zero eigenvector; the singularity is exact and not a small eigenvalue. The Proca kernel $K+M^{2}\delta$ has smallest eigenvalue $M^{2}$. The zero mode is the orbit of the local symmetry, and it is [stage $2$'s only structural failure](the-failure-modes-of-the-diagram-expansion-gauge-fixing-renormalisation-asymptotic-series-and-strong-coupling.html).

## The Determinant Is the Vacuum Bubble

**The leftover factor is a closed loop, and this is the first appearance of the count that organises the quantum corrections.** The Gaussian's $(\det W)^{-1/2}$ is the product over modes of $W$'s eigenvalues, and its logarithm is a trace,

$$
\Gamma_{1}=\tfrac12\,\mathrm{Tr}\log W ,
$$

which is the sum of the one-loop diagrams with no external legs. [The Functional Determinant](the-functional-determinant-in-biquaternionic-form.html) states what the algebra contributes to it — the pairing, the sector factorisation, the axis of the $i\epsilon$ — and what it does not: the regularisation, which is not a four-dimensional biquaternion construct.

**The determinant is why stage $2$ is called exact and stage $4$ is called approximate.** The inversion is exact and its leftover is exact; the series of which the leftover is the first term is not. The distinction is the subject of [the last article](the-failure-modes-of-the-diagram-expansion-gauge-fixing-renormalisation-asymptotic-series-and-strong-coupling.html).

## What the Algebra Supplies Here

**The stage is the clearest case of the section's ledger, because the algebra supplies exactly one thing and it is decisive.**

| what the stage needs | where it comes from |
|---|---|
| the pairing that makes the integral a scalar | the algebra, [The Invariant Density](the-invariant-density-which-pairing-the-action-can-integrate.html) |
| the two sectors' factorisation | the algebra, the central $i$ exchanges $\mathbb B_{\Psi}$ and $\mathbb B_{\Phi}$ |
| the operator whose inverse is the propagator | the algebra, the mass-shell operator $\mathcal M$ |
| the axis of the $i\epsilon$ deformation | the algebra names it: the $ir'_{t}$ direction; it does not choose the orientation |
| the measure | not the algebra; an analytic construction outside the finite-dimensional space |
| the regularisation of the determinant | not the algebra; [the determinant article](the-functional-determinant-in-biquaternionic-form.html) says why |

**The honest reading is that the inverse is the algebra's and the integral is not.** The mass-shell operator is a real function of four real numbers, its inverse exists off the shell, and the residue at its zero is the wave-function renormalisation. All of that is algebra. The measure, the convergence and the regularisation are not, and the [functional integral article](the-functional-integral-in-biquaternionic-form.html) says so in its own words. A reader who wants a derivation of the path integral from $\mathbb B$ will not find one, and this stage says that rather than dressing the import.

## Summary

**Stage $1$ defines the object and stage $2$ computes its quadratic part.** The generating functional $Z[J]$ carries the theory, and every correlator is a derivative of it. Writing $S=S_{2}+S_{\mathrm{int}}$ factors the integral into an operator acting on a Gaussian, and the Gaussian is exact per mode: its inverse is the propagator, and its determinant is the vacuum's one-loop factor.

**The propagator is the inverse of the quadratic operator, and its sign is the one the corpus displays.** With $W=\Box_{\Phi}-4\pi^{2}\nu_{m}^{2}$ the symbol is $-\mathcal M$, so $\Delta=i/[-\mathcal M+i\epsilon]$ and $-\mathcal M=p_{0}^{2}-\vec p^{\,2}-m^{2}c^{2}$. The Gaussian identity was checked by exact quadrature to $8.3\times10^{-15}$ in dimension two.

**The stage's one failure is structural and it is stated here.** An unfixed connection's quadratic kernel annihilates the momentum, so it has no inverse and no propagator; the zero mode is the orbit, and fixing the representative is what removes it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Z[J]$, $Z_{0}[J]$ | the generating functional, and its Gaussian part |
| $\theta_{\mathrm{act}}$, $\kappa_{\mathrm{act}}$ | the action angle and the damping, from $\mathrm{Re}\,S$ and $\mathrm{Im}\,S$ |
| $W$, $\Delta=W^{-1}$ | the quadratic operator and the propagator |
| $\mathcal M(\tilde Q_{\Phi})=N(\tilde Q_{\Phi})+m^{2}c^{2}$ | the mass-shell operator |
| $p_{0}$, $\vec p$ | the wave biquaternion's components, $p_{0}=\frac{E}{c}$ |
| $\epsilon$ | the infinitesimal that fixes the pole's side |
| $\zeta$ | the gauge-fixing parameter of the $R_{\xi}$ family |

## Further Reading

- [The Functional Integral in Biquaternionic Form](the-functional-integral-in-biquaternionic-form.html), the measure, the phase and the rotation, and what each costs.
- [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html), the displayed propagator whose sign this article checks.
- [The Functional Determinant in Biquaternionic Form](the-functional-determinant-in-biquaternionic-form.html), the leftover factor and its regularisation.
- [The Mass Shell and the Scalar Part: What a Congruence Preserves](the-mass-shell-and-the-scalar-part.html), the level set that $N$ and $\mathcal M$ define, and what the congruence preserves on it.
- [The Lagrangian Method: From the Collected Lagrangian to the Feynman Diagram](the-lagrangian-method-from-the-collected-lagrangian-to-the-feynman-diagram.html), the chain this stage belongs to.
- [The Interaction Series and the Vertex: Wick Contraction from the Polynomial Part of the Action](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html), the stage that expands the operator this one factored out.
