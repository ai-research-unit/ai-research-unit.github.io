# __The Polar Form of the Coupled Dirac Equation in Biquaternionic Form__

## Introduction

The coupled Dirac equation of this corpus is one element of $\mathbb{B}$ acting on another by left multiplication, with the gradient replaced by the covariant derivative of *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*:

$$
\tilde\nabla_{\mathrm{gco}}\tilde\Xi_{R}=k_m\,\tilde\Xi_{L},
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_{L}=k_m\,\tilde\Xi_{R},
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi},
$$

with $\tilde A_{\Phi}$ the potential biquaternion and $ϙ$ the charge. *The Polar Form of the Dirac Equation in Biquaternionic Form* substitutes the polar word into the uncoupled pair. This article substitutes the same word into the coupled one, and reads what the connection does to it.

**The claim, stated first.** The covariant derivative enters the word at one place and at one place only: it is added to the phase gradient. The other seven parameters are untouched, by the coupling and by the gauge group alike. That is the whole of the article, and the rest is its warrant and its consequences.

The word is the one the polar article uses, in the exponential form of *Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion*:

$$
\tilde\Xi=r\,e^{i\alpha}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$ a real scale, $\alpha$ a central angle, $\tilde U_{\Psi,\mathrm b}$ a Hermitian positive boost and $\tilde u_{\mathrm r}$ a real rotor. The field is the element $\tilde\Xi_{\mathrm{sp}}$ of the minimal-coupling article; the present article writes $\tilde\Xi$ for it, as the polar article does, because the subscript would carry no information here. The label $\mathrm{sp}$ is the corpus's Dirac-field label, fixed in *Algebra and Element Conventions*, and it survives below in $\tilde S_{\Psi,\mathrm{sp}}$, which names the spin element of that field.

**The domain has two halves, and both are stated at the outset.** The first is the polar article's: the word is a parametrisation of the group of units, so it exists exactly where $N(\tilde\Xi)\neq0$, and it fails on every $N$-degenerate field. The second is new here: the connection must have **central** component coefficients. Central components are the abelian case, and the abelian case is electromagnetism; a $\mathbb{B}$-valued connection is the non-abelian extension, and it lies outside this article. The corpus states the restriction in *Operator and Calculus Conventions*, where $\tilde\nabla_{\mathrm{gco},\mu}$ is called a central scalar that commutes with every element, and the minimal-coupling article works in the same abelian case. Every theorem below is conditional on both halves. §*The Connection Is Central* says what the second costs, and Open Question 4 says what happens without it.

What the article establishes is short, and each item is one sentence:

- the covariant logarithmic derivative has the same four brackets as the free one, with the second shifted;
- the shift is the covariant wavevector $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_{\Phi}+\frac{ϙ}{\hbar}\tilde A_{\Phi}$, and the momentum-space system of the coupled pair is the free one with $\tilde K_{\Phi}$ replaced by it;
- the velocity and the mass factor are read from the covariant wavevector and not from the canonical one, so the word's frame is the kinetic frame;
- the mass shell is one hyperboloid of radius $k_m$: the covariant momentum lies on it and the canonical momentum lies on a displaced copy;
- the gauge orbit of the field is the circle of the word's second factor, so one of the eight parameters is gauge and seven are invariant;
- the density, the velocity and the spin direction read the seven invariant parameters, while the quaternionic norm shifts by the square of the gauge factor.

Two points of discipline carry over from the polar article unchanged, and both are ways of losing the alignment.

**The word is not a split of the field.** It is a re-coordinatisation of the element. Every factor is read from the element and the product is the element. Nothing is put into a slot, and the connection is not a fifth factor.

**The word brings nothing in behind it.** No module, no ideal, no projector, no column, no state space stands behind the four factors. The object the word parametrises is one element of $\mathbb{B}$, and the equation it is put into is one element acting on another.

## The Coupled Equation and the Word

### One Element and One Operator

The field is one element $\tilde\Xi=\tilde\Xi_{L}+\tilde\Xi_{R}$ of $\mathbb{B}$, carrying four complex coefficients, that is eight real numbers. The two subscripts name two parts of that one element and not two values; the polar article proves that a part of definite value is a zero divisor annihilated by $\vec e_z\pm ie_t$, so it lies outside the word's domain, and the letters cannot name the values.

The operator acts from the left, and its two members carry the two conjugations. Since $\natural$ fixes the coefficients and negates the three spatial units, the conjugate connection is the same potential with the vector part reversed, $\tilde A_{\Phi}^{\natural}=A_te_t-\sum_\eta A_\eta\vec e_\eta$. The second member of the pair therefore carries the conjugate of the entry and not its negative: for a purely electric potential the two entries coincide, for a purely magnetic one they are opposite, and for a general potential they are neither, because a general gauge function moves an electric potential out of the purely electric class. That is the parent's statement, repeated here because the polar reading of the second member uses it.

### The Word

The four factors and their types are those of the polar article, and this article repeats none of their theory.

| # | factor | range | type |
| --- | --- | --- | --- |
| 1 | $r$ | $r>0$ | real central scale |
| 2 | $e^{i\alpha}$ | $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | central phase |
| 3 | $\tilde U_{\Psi,\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | $\theta_{\mathrm{rpd}}\ge0$, $\vec u_{\mathrm b}$ a real unit vector | Hermitian positive, $N=1$ |
| 4 | $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\vec u_{\mathrm r}$ a real unit vector | real unit quaternion, $N=1$ |

The count closes at $1+1+3+3=8$ against four complex coefficients, and the word is a bijection on its domain. The boost is the square root of the four-vector factor, $\tilde U_{\Psi,\mathrm b}^{2}=\mathcal B_{\Psi}^{-1}$, so every factor of two in this article comes from that square and from nowhere else. Two factors are central and two have norm one, and that split is where the two norms come from.

### The Connection Is Central

Write the potential in components, $\tilde A_{\Phi}=\sum_\mu A_\mu e_\mu$ with $A_\mu$ central scalars. In the material sector its temporal coefficient is imaginary and its spatial coefficients are real, $\tilde A_{\Phi}=i\,a'_t\,e_t+\vec A$ with $a'_t$ and $\vec A$ real, so $\tilde A_{\Phi}^{*}=-\tilde A_{\Phi}$ and the potential is anti-Hermitian. The coupling coefficient is

$$
\frac{ϙ}{\hbar},
$$

the mass cancelling in the ratio. That cancellation is the physical point, and it is the companion's: the charge couples the same way whatever the mass, so the coefficient must not be read as one that grows with $m$. The component operators are

$$
\tilde\nabla_{\mathrm{gco},\mu}=\frac{\partial}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu,
\qquad
\frac{\partial}{\partial R_t}=-i\frac{\partial}{\partial h_t^{\prime}},
\qquad
\frac{\partial}{\partial R_\eta}=\frac{\partial}{\partial r_\eta}.
$$

*Proposition.* Each $\tilde\nabla_{\mathrm{gco},\mu}$ is a central scalar operator: it commutes with every element of $\mathbb{B}$ and with every unit.

*Proof.* The derivative acts on the coefficients only, and the $A_\mu$ are complex numbers. Both are central, and a sum of central scalars is central.

**What the proposition buys, in one line.** For any element $\tilde Q$ and any central scalar $\lambda$, $\lambda\tilde Q=\tilde Q\lambda$. Hence the interaction term passes through the field and can be written on either side of it. That one line is the whole of §*The Shifted Bracket*, and it is why the covariant derivative does not disturb the word's factorisation.

**The qualification is not decoration.** In a non-abelian extension the connection is $\mathbb{B}$-valued and no component is central. The interaction term then does not pass through the field, and the statement of the next section fails; what replaces it is written in Open Question 4. The corpus's conventions and the minimal-coupling article both work in the central case, and this article states its theorems for that case and no other.

## The Covariant Logarithmic Derivative

### The Shifted Bracket

*Proposition.* Let the connection have central component coefficients, and let $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$. Then

$$
\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi
=\tilde\Xi\left[\frac{1}{2}\frac{\partial_\mu\rho}{\rho}
+i\Bigl(\partial_\mu\alpha+\frac{ϙ}{\hbar}A_\mu\Bigr)
+\tilde u_{\mathrm r}^{-1}\Bigl(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}\Bigr)\tilde u_{\mathrm r}
+\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}\right],
$$

with $\rho=r^{2}$ and $\partial_\mu=\partial/\partial R_\mu$.

*Proof.* The free proposition of the polar article gives $\partial_\mu\tilde\Xi=\tilde\Xi B_\mu$ with the four brackets displayed there. The connection adds $\frac{i\,ϙ}{\hbar}A_\mu\tilde\Xi$, and $A_\mu$ is central, so the addition is $\tilde\Xi\,\frac{i\,ϙ}{\hbar}A_\mu$. It is central and imaginary, so it joins the central imaginary bracket and no other.

**The count of brackets does not change.** The interaction term is not a fifth bracket. It is an addition to the second, and the second is the only bracket it can join: the first is real central, the third is Hermitian and non-central, and the fourth is a real vector part. A central scalar cannot be turned into any of those three.

The four brackets, with the second now shifted, are the following.

| term | type | zero when |
| --- | --- | --- |
| $\tfrac12\partial_\mu\rho/\rho$ | real central scalar | the density is constant |
| $i\bigl(\partial_\mu\alpha+\frac{ϙ}{\hbar}A_\mu\bigr)$ | central imaginary | the covariant phase gradient vanishes |
| $\tilde u_{\mathrm r}^{-1}(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b})\tilde u_{\mathrm r}$ | Hermitian | the boost is constant |
| $\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}$ | real vector part | the rotor is constant |

**The second row is a gradient and the other three are parameters.** The third and fourth brackets vanish when a factor is constant, and the first when a factor is constant in scale. The second vanishes when the covariant phase gradient vanishes, which is not the same condition: a constant angle with $A_\mu\neq0$ gives $\partial_\mu\alpha+\frac{ϙ}{\hbar}A_\mu\neq0$, and a linear angle can make the sum vanish on a nonzero potential. The row records the condition that the coupled equation actually uses.

**The objection, and its answer.** A coupling is expected to add a term, and the display appears to have absorbed it. The absorption is exact, and it is the content: the phase bracket collects every central imaginary contribution there is, and the connection's component coefficient is one. A reader who looks for the interaction term as a separate summand is looking for it in the wrong decomposition. It sits in the second bracket, in the company of the gradient it corrects.

### The Covariant Wavevector

The second bracket is a four-vector, and with the connection it is the **covariant wavevector**:

$$
\tilde K_{\Phi,\mathrm{gco}}=\tilde\nabla\alpha+\frac{ϙ}{\hbar}\tilde A_{\Phi}=\tilde K_{\Phi}+\frac{ϙ}{\hbar}\tilde A_{\Phi}.
$$

*Proposition.* $\tilde K_{\Phi,\mathrm{gco}}$ lies in the material sector $\mathbb{B}_{\Phi}$, and for a plane wave, where the frame and the density are constant and the angle is linear,

$$
\tilde\nabla_{\mathrm{gco}}\tilde\Xi=i\,\tilde K_{\Phi,\mathrm{gco}}\,\tilde\Xi.
$$

*Proof.* The gradient of a real angle is a material four-vector, the potential is one by the previous section, and a real multiple of a sum of two is one. For the display, $\partial_\mu\tilde\Xi=iK_{\Phi,\mu}\tilde\Xi$, so $\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi=i\bigl(K_{\Phi,\mu}+\frac{ϙ}{\hbar}A_\mu\bigr)\tilde\Xi$; the coefficients are central, so they pass the unit $e_\mu$ and the sum is left multiplication by $i\tilde K_{\Phi,\mathrm{gco}}$.

**The slots, read one by one.** With $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$ and $\tilde A_{\Phi}=ia'_te_t+\vec A$, the four entries of the covariant wavevector are

$$
\bigl(\tilde K_{\Phi,\mathrm{gco}}\bigr)_t=\frac{i}{\hbar c}\bigl(E+ϙ\phi\bigr),
\qquad
\bigl(\tilde K_{\Phi,\mathrm{gco}}\bigr)_\eta=\frac{1}{\hbar}\bigl(p_\eta+ϙA_\eta\bigr),
$$

with $\phi=ca'_t$. No factor is inserted by hand: the temporal entry of the operator is $\frac{i}{\hbar c}$ times an energy and the spatial entries are $\frac{1}{\hbar}$ times momenta, because $h_t^{\prime}$ is a length and $\hbar$ is what turns a gradient into a momentum. The combination $E+ϙ\phi$ is the one the gauge law preserves, and the same holds for each spatial slot.

**One relabelling, stated once.** With the inherited sign of $ϙ$ the spatial entry is $\vec p+ϙ\vec A$. The companion *Relativistic Mechanics from the Dirac Wave* writes the same coupling with $ϙ$ replaced by $-ϙ$, so that its kinetic momentum is $\vec p-ϙ\vec A$; the two writings are one coupling with the sign of the charge carried differently. This article keeps the inherited sign and does not flip it.

### Canonical and Covariant

Two elements now carry the name of momentum, and they differ by the potential's share.

| element | definition | gauge | what it is |
| --- | --- | --- | --- |
| $\tilde K_{\Phi}$ | $\tilde\nabla\alpha$ | shifts by $+\frac{ϙ}{\hbar}\tilde\nabla\Gamma$ | the gradient of the word's angle; the canonical wavevector |
| $\tilde K_{\Phi,\mathrm{gco}}$ | $\tilde K_{\Phi}+\frac{ϙ}{\hbar}\tilde A_{\Phi}$ | invariant | the wavevector of the coupled pair; the kinetic one |

The free article's sentence is therefore amended, and not weakened: *the momentum is the gradient of the angle* becomes *the kinetic momentum is the gradient of the angle plus the potential's share*. The two coincide when the potential vanishes, which is why the free sentence was right in its own case.

**The momentum of the word.** Multiplying by $\hbar$ and using $\hbar k_m=mc$,

$$
\tilde P_{\Phi}=\hbar\tilde K_{\Phi}=m\tilde V_{\Phi}-ϙ\,\tilde A_{\Phi},
$$

since $\hbar\,\frac{ϙ}{\hbar}=ϙ$. The canonical momentum is the kinetic one less the potential's share, which is the standard content of minimal coupling written as an identity of elements. The velocity $\tilde V_{\Phi}$ is the next section's, and it is read from the covariant wavevector.

### The Objection of Triviality

The strongest objection is that this section has said nothing: writing $D=\partial+i\frac{ϙ}{\hbar}A$ and calling the result a shifted gradient is the definition of the covariant derivative. The section must separate what the definition gives from what it does not, and the separation is the following.

**The trivial part, granted in full.** That $D$ is a shifted derivative is the definition. No new element appears, no new bracket, no new parameter, and no solution is produced. In this respect the article transcribes the companion.

**The non-trivial part, in one sentence.** The shift lands in one bracket and the factorisation survives, and both halves of that sentence need the centrality of $A_\mu$. The first half is the type argument: a central imaginary scalar joins the central imaginary bracket because nothing else in the display is of that type. The second half is the one that could fail, and it is the assertion that the derivative of the word is again the word times a bracket. It holds because the interaction term can be moved from the left of the field to the right of it. Without centrality the term stays on the left, the display is not of the form element times bracket, and no reading of the eight parameters follows from it.

**The consequence, stated as a test.** A reader who doubts the distinction can drop centrality and recompute. The display then fails, the leftover is the object of Open Question 4, and the failure is what makes the success informative. The following sections draw the readings that the surviving factorisation supplies: the velocity from the covariant wavevector and not the canonical one, a mass shell displaced and not resized, and a gauge orbit one parameter wide.

## The Word Under a Gauge Transformation

### Only the Angle Moves

The gauge transformation of the coupled pair is

$$
\tilde\Xi_2=\lambda\,\tilde\Xi,
\qquad
\lambda=\exp\Bigl(\frac{i\,ϙ\,\Gamma}{\hbar}\Bigr),
\qquad
\tilde A_{\Phi,2}=\tilde A_{\Phi}-\tilde\nabla\Gamma,
\qquad \Gamma\ \text{real},
$$

with $\lambda$ central and of unit modulus.

*Proposition.* Let $\tilde\Xi_2=\lambda\tilde\Xi$ with $\lambda=e^{i\beta}$, $\beta$ real. Then the word's scale, rapidity, boost axis, rotor angle and rotor axis are unchanged, and its angle becomes $\alpha+\beta$.

*Proof.* A central unimodular factor multiplies the element and passes through every factor. The element $\tilde Q'=\tilde\Xi/(re^{i\alpha})$ is therefore unchanged, and $\tilde Q'$ is what the polar decomposition reads for the boost and the rotor. The quaternionic norm multiplies by $\lambda^{2}$, so its modulus is unchanged and its argument gains $2\beta$; the scale is the square root of the modulus and the angle is half the argument.

**The eight parameters split one and seven.** The gauge group moves exactly the factor it is built from, and it leaves the frame, the density and the spin direction alone. That is the sharpest statement the chart makes about minimal coupling, and it is a statement of count.

| parameter | under $\tilde\Xi\mapsto e^{i\beta}\tilde\Xi$ | status |
| --- | --- | --- |
| $\alpha$ | $\alpha+\beta$ | the gauge parameter's seat |
| $r$, $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$, $\theta$, $\vec u_{\mathrm r}$ | unchanged | invariant, seven in number |

**The half-turn, and the rotor's sign.** The angle's declared range is half a turn, so a shift of the angle is a shift modulo $\pi$. Take a representative with $\alpha$ shifted by an odd multiple of $\pi$. The factor $e^{i\alpha}$ changes sign, so the element is recovered only if another factor changes sign with it, and the only candidate is the rotor: $\tilde u_{\mathrm r}\mapsto-\tilde u_{\mathrm r}$, that is, $\theta\mapsto\theta+2\pi$ on the same axis. That is the double cover and nothing else, and it is invisible to the spin direction $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, because the sign cancels between the rotor and its conjugate. No observable of this article feels the reduction.

### The Density Is the Gauge-Invariant Part of the Norm

The two norms of the polar article separate further under the gauge group.

$$
\langle\tilde\Xi_2\rangle_{\natural}=\rho\,e^{2i(\alpha+\beta)}=\lambda^{2}\langle\tilde\Xi\rangle_{\natural},
\qquad
\langle\tilde\Xi_2\rangle_{*}=\gamma\rho=\langle\tilde\Xi\rangle_{*},
$$

with $\rho=r^{2}$ and $\gamma=\cosh\theta_{\mathrm{rpd}}$.

**The quaternionic norm is not gauge invariant, and its modulus is.** The whole of the invariance sits in $\rho$; the argument $2\alpha$ is shifted by twice the gauge function. That is the polar article's observation that no bilinear reads the angle, sharpened: the reason is now visible, since the shift doubles because the norm is built from two factors of the field, each carrying $e^{i\alpha}$.

**The density, the velocity and the spin are the invariant readings.** The polar article's table of what each bilinear reads keeps its rows and gains a column.

| observable | reads | under the gauge group |
| --- | --- | --- |
| $\rho$ | $r$ | invariant |
| $\tilde J_{\Phi}=\rho\tilde V_{\Phi}$ | $r$, $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ | invariant |
| $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ | $r$, $\theta$, $\vec u_{\mathrm r}$ | invariant |
| $\langle\tilde\Xi\rangle_{\natural}$ | $\rho$, $2\alpha$ | shifts by $\lambda^{2}$ |

### Why the Common Phase Is the Gauged One

The minimal-coupling article establishes that the mass keeps the common phase of the two parts and breaks the relative one, and that the two-sided form has no continuous central phase at all. The chart gives that statement a second warrant, and the warrant is a count.

**The word has one central factor.** A local symmetry that acts by multiplication by a central scalar moves that factor and nothing else, as the proposition above shows. The relative phase of the two parts is not of that form: it multiplies $\tilde\Xi_{R}$ by $\varsigma$ and $\tilde\Xi_{L}$ by $\varsigma^{-1}$, which is not the multiplication of the element by one central scalar. The word has no parameter for it, and it cannot: the eight parameters describe one element, and the relative phase describes a relation between two parts.

**The objection, and its answer.** The objection is that this is a statement about a chart and not about the theory. The answer is that it is exactly what was asked. The question is where the localization can sit, and the answer is: in the one central factor the field's parametrisation contains, which is the angle. The eight-parameter count forces the choice, and the mass's breaking of the relative phase is then a statement about a transformation the chart never names.

### The Loop and the Angle

One gauge-invariant number survives the shift. It is the loop integral, and it is what an interference experiment reads.

**The loop integral of the covariant wavevector is invariant.** Since $\tilde K_{\Phi,\mathrm{gco}}$ is gauge invariant, so is $\oint\sum_\mu\bigl(\tilde K_{\Phi,\mathrm{gco}}\bigr)_\mu\,dR_\mu$ around any closed path on which the field is $N$-regular. The same integral splits into the angle's winding and the potential's circulation:

$$
\oint\sum_\mu\bigl(\tilde K_{\Phi,\mathrm{gco}}\bigr)_\mu\,dR_\mu
=\Delta\alpha+\frac{ϙ}{\hbar}\oint\sum_\mu A_\mu\,dR_\mu .
$$

**The winding is quantised by single-valuedness.** The field returns to itself around the loop, so the word returns to itself. The scale and the boost are single-valued, and the rotor is single-valued up to sign, so the only factor that can return with an offset is the central phase: $e^{i\Delta\alpha}=1$, and $\Delta\alpha$ is a multiple of $2\pi$ for a closed path on which the rotor also returns, and a multiple of $\pi$ when it returns with the opposite sign. That parity is the rotor's sign, recorded in the preceding section. The potential's circulation is then the gauge-invariant integral less a multiple of $\pi$, which is the Aharonov–Bohm phase in the chart's language: a flux, read as the mismatch between a loop integral and a winding.

## The Equation in Polar Variables

### The Momentum-Space System

The pair in momentum space is the free one with the canonical wavevector replaced.

*Proposition.* Let $\tilde\Xi=\tilde\Xi_0\exp(i\alpha)$ with $\alpha$ linear in $\tilde R_\Phi$ and $\tilde\Xi_0$ constant. Then the coupled pair is equivalent to

$$
i\tilde K_{\Phi,\mathrm{gco}}\tilde\Xi_0^{R}=k_m\tilde\Xi_0^{L},
\qquad
i\tilde K_{\Phi,\mathrm{gco}}^{\natural}\tilde\Xi_0^{L}=k_m\tilde\Xi_0^{R},
\qquad
\tilde K_{\Phi,\mathrm{gco}}\tilde K_{\Phi,\mathrm{gco}}^{\natural}=-k_m^{2}.
$$

*Proof.* The derivative is left multiplication by $i\tilde K_{\Phi,\mathrm{gco}}$ by §*The Covariant Wavevector*, and the pair is the parent's with that operator in place of $\tilde\nabla$. The third relation follows from the first two as in the free case: eliminate $\tilde\Xi_0^{L}$ between them.

**What the display says.** The connection has not changed the form of the system. It has changed the element that appears in it, from the gradient of the angle to the covariant wavevector. A reader who knows the free polar system knows the coupled one, provided he reads the momentum as the kinetic momentum.

### The Boost Is the Kinetic Velocity

The velocity is the boost, and the boost is now read from the covariant wavevector.

*Proposition.* Let $\tilde K_{\Phi,\mathrm{gco}}=i\kappa_te_t+\vec\kappa$ with $\kappa_t>0$ and $\kappa_t^{2}-|\vec\kappa|^{2}=k_m^{2}$. Then

$$
\tilde K_{\Phi,\mathrm{gco}}=ik_m\,\tilde U_{\Psi,\mathrm b}^{-2}=ik_m\,\mathcal B_{\Psi},
\qquad
\tilde V_{\Phi}=ic\,\tilde U_{\Psi,\mathrm b}^{-2}=\frac{\hbar}{m}\tilde K_{\Phi,\mathrm{gco}},
\qquad
\tilde P_{\Phi,\mathrm{gco}}=m\,\tilde V_{\Phi},
\qquad
\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2},
$$

with $\cosh\theta_{\mathrm{rpd}}=\kappa_t/k_m$ and $\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}=-\vec\kappa/k_m$.

*Proof.* Divide by $ik_m$. The quotient is $\frac{\kappa_t}{k_m}e_t-i\frac{\vec\kappa}{k_m}$, a Hermitian unit whose scalar part exceeds one, so it has the form $\cosh\theta_{\mathrm{rpd}}e_t+i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$ with the rapidity and the axis just stated, and they are unique. That element is $\tilde U_{\Psi,\mathrm b}^{-2}$ by the square computed in §*The Word*. The remaining displays follow by multiplying, and the last is the free article's line, unchanged, because a unit inverts under $\natural$.

**Momentum is mass times velocity, and the momentum is the kinetic one.** The identity $\tilde P_{\Phi,\mathrm{gco}}=m\tilde V_{\Phi}$ is the standard relation with the standard content: the frame factor carries the kinetic momentum. The canonical momentum is the same expression less $ϙ\tilde A_{\Phi}$, by §*Canonical and Covariant*. A reader who takes the canonical momentum for the velocity finds the potential added to a mass times a velocity, which is the classical statement and not an error.

**The four-velocity's norm is untouched.** It is $-c^{2}$ for every field, at every potential, because the boost is a unit by construction and the density is a separate factor. What the potential changes is which boost the field carries at a given canonical momentum, and that is all.

### The Mass Term Is Still the Four-Vector Factor

Substituting $\tilde K_{\Phi,\mathrm{gco}}=ik_m\mathcal B_{\Psi}$ into the first line of the momentum-space system gives

$$
\tilde\Xi_0^{L}=-\mathcal B_{\Psi}\,\tilde\Xi_0^{R},
\qquad
\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}=\frac{\tilde K_{\Phi,\mathrm{gco}}}{ik_m},
$$

and the second line is then satisfied identically.

**The relation is free of $k_m$ and of the potential.** The scalar cancels against the momentum it multiplies, and the potential cancels with it, because both sit in the same covariant wavevector. What remains is the frame factor. In this chart the mass term is an operator on the parts, and the operator is the four-vector factor that the velocity also carries.

**At rest the factor is the identity.** With $\theta_{\mathrm{rpd}}=0$ the boost is $e_t$ and the relation is the plain sign. The whole of the mass term's structure is the sign, and the whole of its motion dependence is the boost.

**The mass term is the frame factor; the mass is its scale.** The two statements must not be run together. What the relation says is that the operator carrying the mass in this chart is the boost, with coefficient $k_m$. What it does not say is that the mass depends on the frame: the scale sits outside the boost, no boost moves it, and the radius of §*The Mass Shell Is a Translated Hyperboloid* is $k_m$ in every frame and at every potential.

**What the coupling adds to the reading, and what it does not.** It adds the location of the potential: the potential is in the wavevector, not in the mass factor, so a potential cannot turn into a mass and a mass cannot turn into a potential. It does not change the sentence that the mass term is the frame factor and the mass its coefficient; the norm of $\mathcal B_{\Psi}$ is one and the scale is $k_m$, which no boost and no gauge touches.

### The Mass Shell Is a Translated Hyperboloid

The third relation is the dispersion relation, and in the word it is the frame's unitarity.

*Proposition.* Let $\tilde K_{\Phi,\mathrm{gco}}=i\kappa_te_t+\vec\kappa$ with $\kappa_t$ real and $\vec\kappa$ real. Then $\tilde K_{\Phi,\mathrm{gco}}\tilde K_{\Phi,\mathrm{gco}}^{\natural}=-k_m^{2}$ is equivalent to

$$
\kappa_t^{2}-|\vec\kappa|^{2}=k_m^{2},
$$

and with $\tilde K_{\Phi}=i\pi_te_t+\vec\pi$ and $\tilde A_{\Phi}=ia'_te_t+\vec A$ the canonical pair satisfies

$$
\Bigl(\pi_t+\frac{ϙ}{\hbar}a'_t\Bigr)^{2}-\Bigl|\vec\pi+\frac{ϙ}{\hbar}\vec A\Bigr|^{2}=k_m^{2}.
$$

*Proof.* Multiply out the product $\tilde K_{\Phi,\mathrm{gco}}\tilde K_{\Phi,\mathrm{gco}}^{\natural}$, using $e_t$ central and $\vec e_\eta^{2}=-e_t$; the cross terms cancel and the two signs leave the difference of squares. The second display is the first with the components of the covariant wavevector written in terms of the canonical ones.

**The hyperboloid is the same and its centre has moved.** The radius is $k_m$ in both displays. The potential displaces the surface, and the displacement carries the potential's four components; the mass, which is the radius, is untouched. That is the polar reading of the minimal-coupling article's sentence that a constant potential *translates and does not resize* the mass shell, and the chart says why in one line: the mass is a norm, and a norm is not changed by adding a covector.

**The objection, and its answer.** The objection is that the second display is a change of variables: the canonical entries are defined as the covariant ones less the potential's share, and a definition cannot fail. The answer is that the display fixes what a measurement of the canonical entries returns. A wavelength measured at a fixed potential is read against the displaced surface, and the displacement's four components are the potential's.

**What the display adds, and what it forbids.** It adds the displacement, which the free proposition does not contain. It forbids a gap: the potential enters only as the translation, with no coefficient of its own, so its powers are the ones the shift produces and the radius condition fixes them. A gap would need a term with a scale of its own, and the algebra has one scalar here, the mass coefficient.

## The Current and the Spin

### The Current Is the Covariant Momentum Density

The current of the field is the density times the four-velocity of the word,

$$
\tilde J_{\Phi}=\rho\,\tilde V_{\Phi}=\frac{\hbar}{m}\,\rho\,\tilde K_{\Phi,\mathrm{gco}},
$$

and the display contains four of the eight parameters: the density, the rapidity and the two components of the boost axis. The density multiplies and the boost supplies the rapidity and the direction. The angle is absent, and the rotor's angle and axis are absent as well.

**The current is gauge invariant by construction.** Both factors are invariant, so the product is. The potential's share is absent from it, and that is not an oversight: the current is built on the kinetic momentum, which is the invariant one. A current built on the canonical momentum would not be gauge invariant, and the chart shows the difference as one term, $ϙ\tilde A_{\Phi}$.

**The temporal slot is the charge density and the spatial part the current density.** Nothing here is new relative to the free article except the reading of which momentum the velocity carries. The current is not an independent object: the word carries the velocity, and the current is the density times it.

### The Bilinear That Is Not the Current

The algebra's own bilinear is unchanged by the coupling, and the polar article's line still explains it. By the norm proposition $\tilde\Xi\tilde\Xi^{*}=\rho\tilde U_{\Psi,\mathrm b}^{2}$, so

$$
i\tilde\Xi\tilde\Xi^{*}=\rho\bigl(i\cosh\theta_{\mathrm{rpd}}\,e_t-\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}\bigr),
$$

the temporal slot agreeing with the current and the spatial part reversed. The star conjugation fixes the boost and cancels the rotor, so the product carries the velocity twice and the spin not at all, and the outer $i$ reverses the spatial part. The current needs the velocity once and a fixed timelike direction once, and the fixed direction is the odd element the even algebra does not contain.

**Where the negative result lives.** The minimal-coupling article exhibits the non-conservation of this bilinear on an exact solution,

$$
\tilde\Xi_{R}=\tfrac12\,\xi\left(-e_t-i\vec e_x+\vec e_y+i\vec e_z\right),
\qquad
\xi=\exp\bigl(iQ_x-Q_t\bigr),
$$

and one line places that field in the chart: the element in brackets is annihilated by $(-e_t+i\vec e_x)$, a nonzero element, so it is a zero divisor and has $N=0$. The field is one-sided, the word does not exist on it, and the article that exhibits the failure is exhibiting it at the boundary of the chart.

**What that placement does and does not do.** It does not repair the current; the article claims no repair. It does say that the two statements are not in conflict: the chart is silent on that solution, and a conservation statement read from the chart is a statement about the $N$-regular set, which that solution is not. A reader who wants the two results compared must first ask whether the comparison is defined, and here it is not.

### The Spin Is Untouched by the Connection

The spin is carried by the rotor, as in the free article,

$$
\tilde S_{\Psi,\mathrm{sp}}=\rho\,\frac{\hbar}{2}\,i\,\hat s,
\qquad
\hat s=\tilde u_{\mathrm r}\,\vec e_z\,\tilde u_{\mathrm r}^{\natural},
\qquad
\hat s^{2}=-e_t,
$$

and it is gauge invariant, since neither $\rho$ nor the rotor moves under the gauge group.

**The connection cannot act on the rotor.** The interaction term is central in each component, and a central element cannot rotate a non-central factor; it multiplies the whole word. So the minimal coupling adds nothing to the spin's bracket, and the spin's magnitude and direction are the rotor's business alone. The $g=2$ statement of *The Classical Origin of $g=2$ in Biquaternionic Form* sits in the same frame factor that carries the velocity, not in the gradient, and the chart displays that separation.

**What this locates and what it does not derive.** It locates the magnetic coupling: the frame factor that carries the velocity also carries the magnetic moment, so a minimal substitution cannot give the two different coefficients. It does not derive the value, which requires the next order of the expansion, as *Relativistic Mechanics from the Dirac Wave* records when it places the spin term at order one. The chart's contribution is that the term it places is not the connection's.

**The spin is a direction and not a plane.** The element is a multiple of one real unit vector, and what the word carries is which direction in the plane is the field's. The connection does not change it, and that is one more reason the spin cannot enter at the order where the eikonal is central.

## The Second-Order Equation and the Curvature

Squaring the first member with the second gives a wave equation, and the square is where the field strength appears.

*Proposition.* On a solution of the coupled pair,

$$
\left(\sum_{\mu\in\{t,x,y,z\}}\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{i\,ϙ}{\hbar}\tilde F-k_m^{2}\right)\tilde\Xi_{R}=0,
$$

with $\tilde F$ the field-strength biquaternion and $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{ iϙ}{\hbar}\tilde F$.

*Proof.* Apply $\tilde\nabla_{\mathrm{gco}}^{\natural}$ to the first member and use the second; the operator identity is the corpus's, from *The Covariant Derivative and Gauge Connection in Biquaternionic Form*.

**The curvature is what the shift cannot remove.** The phase gradient can absorb the potential, because a gradient of a function is a gradient. It cannot absorb the field strength, because a field strength is not a gradient of anything when the circulation is nonzero. So the chart's account of the second-order equation is one sentence: the connection moves into the angle where it is a gradient, and what is left over is the curvature, which multiplies the field as an element.

**A constant potential leaves no curvature.** With $\tilde A_{\Phi}$ constant the field strength vanishes identically, the second-order operator is the free one with every component of the wavevector shifted at once, and the hyperboloid of §*The Mass Shell Is a Translated Hyperboloid* is the whole of the content. No constant potential opens a gap, and the chart says why without a computation: a shift of a variable does not change a radius.

## The Non-Relativistic Limit

### The Rest Phase

A slow state is one whose boost is small and whose angle is dominated by the rest phase. Write

$$
\alpha=-k_m h_t^{\prime}+\sigma,
\qquad
k_m h_t^{\prime}=\frac{mc^{2}}{\hbar}\,t,
$$

so that the field's own phase advances at $mc^{2}/\hbar$ and the norm's angle at twice that. The doubling is the polar article's factor of two, the one behind zitterbewegung, and it is why the norm's angle is not the field's phase: the norm reads the element twice, so it reads a turn where the element reads half a turn.

**With a potential the rest phase carries it.** The temporal entry of the covariant wavevector is $\frac{i}{\hbar c}(E+ϙ\phi)$. At rest, that is at $\vec\kappa=0$, the mass shell reads $\kappa_t=k_m$, so $E+ϙ\phi=mc^{2}$ and the canonical rest energy is $mc^{2}-ϙ\phi$. The chart's sentence is therefore about the combination and not about $E$: the potential enters the phase as an energy enters a phase, and the gauge-invariant rest energy is the mass.

### The Frame Loses Its Boost

At small rapidity the boost departs from the identity at first order, and the word becomes a scale, a phase and a rotor. The velocity's first correction is second order, the temporal slot departing from $ic$ at order $\theta_{\mathrm{rpd}}^{2}/2$, which is the kinetic energy over $mc^{2}$.

**The potential does not change that ordering.** It sits in the covariant wavevector with the momentum, so it shifts the rapidity at fixed canonical momentum and does not shift the order at which the boost appears. In the non-relativistic limit the whole of the coupling is the substitution $\vec p\mapsto\vec p+ϙ\vec A$ and $E\mapsto E+ϙ\phi$, which is the minimal substitution as it is usually written, with the inherited sign of $ϙ$.

**The rotor is untouched at every speed.** It is the factor the boost leaves alone and the factor the connection leaves alone, so the spin's dynamics in the limit is the free one, with the magnetic field entering through the curvature and not through the connection. The polar article's ordering survives the coupling: the current is the scale and the boost, the spin is the scale and the rotor, and the eikonal is the phase, which is central.

## What the Polar Form Does and Does Not Add

The objection has to be stated before it is answered. The decomposition is not new: it is the Yvon–Takabayasi–Hestenes decomposition of a field of this type, and the covariant derivative in those variables is standard in the polar literature of the Dirac theory. No solution is added and no number changes.

Four things are nevertheless not a relabelling.

**The connection's place in the word is fixed and it is one.** Of the eight parameters, exactly one moves under the gauge group and exactly one is shifted by the connection. The other seven are invariant under both. That is a statement the definition of the covariant derivative does not contain.

**The velocity is read from the kinetic momentum.** The word's frame is the kinetic frame, and the canonical momentum is the frame's momentum less the potential's share. The free article's identity *the velocity is the boost* becomes an identity about the covariant wavevector, and the free case is recovered at $\tilde A_{\Phi}=0$.

**The mass shell's displacement is visible.** The canonical pair lies on a hyperboloid congruent to the free one and displaced by the potential; the radius is $k_m$ throughout. A translation of a surface is a different statement from a change of its size, and the chart separates them without an approximation.

**The negative result is located.** The non-conservation of $i\tilde\Xi\tilde\Xi^{*}$, exhibited in the minimal-coupling article, is exhibited there on a field of vanishing quaternionic norm, that is, outside the chart. The chart explains the failure and places the counterexample, and it does neither more nor less.

What the polar form does **not** add is the point of this article. It adjoins no object: no column, no array, no module, no ideal, no projector, no state space, no basis, and no second connection. The field was one element, the word is a parametrisation of it, and the equation is the minimal-coupling article's equation. The only thing the polar form adds is a qualification, and the qualification is two conditions: the field is $N$-regular and the connection is central.

## Open Questions

1. **The conserved current.** The current the word supplies is $\rho\tilde V_{\Phi}$, and it is gauge invariant by construction. Whether it is conserved on solutions of the coupled pair is not settled here: its divergence is the transport equation the chart leaves open, exactly as in the free article. The algebra's own bilinear is not the current, and the exact solution that shows it lies on the cone.

2. **The angle's status.** The free article asks whether the angle is observable through an interference of two branches. The coupled article settles half of it: under the local symmetry the angle is a gauge function, and only the covariant wavevector is physical. What remains is the holonomy of §*The Loop and the Angle*: whether the winding $\Delta\alpha$ has a gauge-invariant residue beyond the loop integral written there, and whether the half-turn range and the rotor's sign carry a topological reading.

3. **The connection terms.** The covariant logarithmic derivative carries a boost connection and a rotor connection, and the coupling has shifted the phase term and neither of the other two. Whether the pair of frame connections has a geometric reading — a connection on the frame bundle of the algebra, with the curvature term of the second-order equation as its field strength — is not attempted here.

4. **The non-central connection.** The whole of §*The Shifted Bracket* rests on the component coefficients being central. Without that, the interaction term does not pass through the field, and what remains after it is moved to the right is

$$
\frac{i\,ϙ}{\hbar}\,\tilde\Xi^{-1}\tilde A_{\Phi}\,\tilde\Xi,
$$

the potential read in the field's own frame. Whether that object has a reading — a connection transported by the word itself, with the frame factors acting on it as a rotation and a boost — is open. It is the chart's form of the minimal-coupling article's left-versus-right question.

5. **The two-sided form.** The parent carries a second form of the equation, with the mass acting on the right, and the minimal-coupling article shows that the prescription does not attach to it because its mass term is a conjugation and carries no continuous central phase. What the polar form is in that display is not written here. To the extent that its letters name the two values, the parts lie on the cone by the polar article's proposition, and the word is stated for the sum only.

6. **The general field.** The four brackets are constrained by the pair but not closed by it, and the coupling does not change that. The shift of the second bracket is exact; the transport of the other three is what a general solution supplies.

## Summary

The polar form of the coupled Dirac field of this corpus is the polar form of the free field with the canonical wavevector replaced by the covariant one. The word is $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, with $r>0$ the scale, $\alpha$ the central angle, $\tilde U_{\Psi,\mathrm b}$ a Hermitian positive boost and $\tilde u_{\mathrm r}$ a real rotor, and it exists exactly where $N(\tilde\Xi)\neq0$.

The covariant derivative enters at one place. The logarithmic derivative of the word has the free article's four brackets, with the second shifted:

$$
\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi=\tilde\Xi\left[\frac{1}{2}\frac{\partial_\mu\rho}{\rho}+i\Bigl(\partial_\mu\alpha+\frac{ϙ}{\hbar}A_\mu\Bigr)+\tilde u_{\mathrm r}^{-1}\bigl(\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}\bigr)\tilde u_{\mathrm r}+\tilde u_{\mathrm r}^{-1}\partial_\mu\tilde u_{\mathrm r}\right].
$$

There is no fifth bracket. The interaction is inside the second, and none of the other three can hold it, because each is of a type a central scalar is not.

The shift is the covariant wavevector $\tilde K_{\Phi,\mathrm{gco}}=\tilde\nabla\alpha+\frac{ϙ}{\hbar}\tilde A_{\Phi}$, an element of the material sector, and for a plane wave $\tilde\nabla_{\mathrm{gco}}\tilde\Xi=i\tilde K_{\Phi,\mathrm{gco}}\tilde\Xi$. The momentum-space system of the coupled pair is the free one with $\tilde K_{\Phi}$ replaced by $\tilde K_{\Phi,\mathrm{gco}}$, including the mass shell $\tilde K_{\Phi,\mathrm{gco}}\tilde K_{\Phi,\mathrm{gco}}^{\natural}=-k_m^{2}$.

The velocity is read from the covariant wavevector: $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}=\frac{\hbar}{m}\tilde K_{\Phi,\mathrm{gco}}$, so $\tilde P_{\Phi,\mathrm{gco}}=m\tilde V_{\Phi}$, and the canonical momentum is $\tilde P_{\Phi}=m\tilde V_{\Phi}-ϙ\tilde A_{\Phi}$. The mass term remains a frame factor, $\tilde\Xi_0^{L}=-\mathcal B_{\Psi}\tilde\Xi_0^{R}$ with $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}=\tilde K_{\Phi,\mathrm{gco}}/(ik_m)$, and the relation carries neither $k_m$ nor the potential.

The mass shell is one hyperboloid shape with one radius and two centres: $\kappa_t^{2}-|\vec\kappa|^{2}=k_m^{2}$ for the covariant components, and $(\pi_t+\frac{ϙ}{\hbar}a'_t)^{2}-|\vec\pi+\frac{ϙ}{\hbar}\vec A|^{2}=k_m^{2}$ for the canonical ones. The covariant surface is the one the algebra draws. The canonical surface is its translate, congruent to it and displaced by $-ϙ\tilde A_{\Phi}$. A constant potential translates the surface and leaves the radius, which is why no potential opens a gap.

The gauge group moves one parameter of the eight. With $\lambda=\exp(\frac{ iϙ\Gamma}{\hbar})=e^{i\beta}$ the scale, the rapidity, the boost axis, the rotor angle and the rotor axis are unchanged, the angle becomes $\alpha+\beta$, and the quaternionic norm becomes $\lambda^{2}\langle\tilde\Xi\rangle_{\natural}$; the density, the current, the velocity and the spin direction are invariant. The relative phase of the two parts is not a multiplication by a central scalar, so the chart has no parameter for it, and the common phase is the only one that can be localized.

The current is $\tilde J_{\Phi}=\rho\tilde V_{\Phi}$, the density times the kinetic four-velocity, and it is gauge invariant because both factors are. The bilinear $i\tilde\Xi\tilde\Xi^{*}$ remains the mirror of the current and not the current, and the exact solution on which the minimal-coupling article exhibits its failure is a zero divisor: the chart is silent there. The spin is $\tilde S_{\Psi,\mathrm{sp}}=\rho\frac{\hbar}{2}i\hat s$ with $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, and the connection cannot touch it, being central in each component.

The second-order equation carries the curvature, $\bigl(\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{ iϙ}{\hbar}\tilde F-k_m^{2}\bigr)\tilde\Xi_{R}=0$, and the curvature is the part of the connection a gradient cannot absorb. The word's domain is unchanged by the gauge group, because a central unit multiplies the element and a unit cannot move $N$ to or from zero.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$; $\vec e_z$ is the frame's third direction |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\tilde\Xi=\tilde\Xi_{L}+\tilde\Xi_{R}$ | The field, one element of $\mathbb{B}$; the letters name the two parts |
| $\mathrm{sp}$ | The Dirac-field label of *Algebra and Element Conventions*; kept in $\tilde S_{\Psi,\mathrm{sp}}$ |
| $\tilde\nabla,\ \tilde\nabla^{\natural}$ | Biquaternionic gradient and its quaternion conjugate, $\tilde\nabla^{\natural}\tilde\nabla=\Box$ |
| $\tilde R_\Phi=i h_t^{\prime}e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$ | Four-position; $\partial/\partial R_t=-i\partial/\partial h_t^{\prime}$ |
| $k_m=mc/\hbar$ | Mass wave number; the reciprocal reduced Compton length |
| $\tilde A_{\Phi}=A_te_t+\sum_\eta A_\eta\vec e_\eta=i a'_te_t+\vec A$ | Potential biquaternion, an element of $\mathbb{B}_{\Phi}$; $A_t=ia'_t$, $a'_t=\phi/c$ |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$ | Covariant derivative, left action |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial/\partial R_\mu+\frac{i\,ϙ}{\hbar}A_\mu$ | Its components; central scalars |
| $\tilde\nabla_{\mathrm{gco}}^{\natural}=\tilde\nabla^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}^{\natural}$ | Its $\natural$-image; the operator of the second member |
| $ϙ$ | Charge; the algebra fixes neither its value nor its sign |
| $\frac{ϙ}{\hbar}$ | The coupling coefficient; the mass does not enter |
| $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word |
| $r>0$, $\rho=r^{2}$ | Scale and density; real, central, gauge invariant |
| $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | The word's angle; the gauge parameter's seat; the norm's argument is $2\alpha$ |
| $\tilde U_{\Psi,\mathrm b}=\exp(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ | Boost; Hermitian positive, $N=1$; $\tilde U_{\Psi,\mathrm b}^{2}=\mathcal B_{\Psi}^{-1}$ |
| $\tilde u_{\mathrm r}$ | Rotor; real unit quaternion, $N=1$ |
| $\mathcal B_{\Psi}=\tilde U_{\Psi,\mathrm b}^{-2}$ | Four-vector factor; $\cosh\theta_{\mathrm{rpd}}e_t-i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$ |
| $\tilde K_{\Phi}=\tilde\nabla\alpha$ | Canonical wavevector; shifts under the gauge group |
| $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_{\Phi}+\frac{ϙ}{\hbar}\tilde A_{\Phi}$ | Covariant wavevector; gauge invariant; in $\mathbb{B}_{\Phi}$ |
| $\tilde K_{\Phi,\mathrm{gco}}\tilde K_{\Phi,\mathrm{gco}}^{\natural}=-k_m^{2}$ | The mass shell, as the frame's unitarity |
| $\tilde P_{\Phi}=\hbar\tilde K_{\Phi}$ | Canonical momentum; $\tilde P_{\Phi}=m\tilde V_{\Phi}-ϙ\tilde A_{\Phi}$ |
| $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | Four-velocity of the word; $\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}$; $\tilde P_{\Phi,\mathrm{gco}}=m\tilde V_{\Phi}$ |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$, $\vec v=c\tanh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$ | Lorentz factor and velocity of the frame |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; on the field $\rho e^{2i\alpha}$ |
| $\langle\tilde Q\rangle_{*}=\operatorname{Sc}(\tilde Q\tilde Q^{*})$ | Hermitian norm; on the field $\gamma\rho$ |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, $\hat s^{2}=-e_t$ | Spin direction |
| $\tilde J_{\Phi}=\rho\tilde V_{\Phi}=\frac{\hbar}{m}\rho\tilde K_{\Phi,\mathrm{gco}}$ | Current |
| $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ | Spin element |
| $i\tilde\Xi\tilde\Xi^{*}=\rho(i\cosh\theta_{\mathrm{rpd}}e_t-\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b})$ | The bilinear that is the mirror of the current |
| $\tilde F$ | Field-strength biquaternion; $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{ iϙ}{\hbar}\tilde F$ |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | Norm; zero exactly on the zero divisors |
| $\lambda=\exp(\frac{i\,ϙ\,\Gamma}{\hbar})=e^{i\beta}$ | Local central phase; $\Gamma$ real; $\beta=\frac{ϙ\Gamma}{\hbar}$ |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the eight-parameter polar variables of the spin-$\tfrac12$ field and for the transport equations the coupling leaves open.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966; second edition Birkhäuser, 2015), for the decomposition of the field into density, angle and rotor and for the reading of the covariant derivative in that decomposition.
- Jacques Yvon, "Équations matricielles du champ spinoriel," *Journal de Physique et le Radium* **1** (1940) 18–26, for the bilinears whose argument is the angle this article writes $2\alpha$.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the relativistic polar variables and for the covariant derivative written in them.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Dirac equation, its minimal coupling and the standard conserved current.
- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the origin of the local phase that the coupling localizes.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for minimal coupling, gauge invariance and the non-relativistic limit.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the fermion-number symmetry and the relative phase of the two chiral parts.
- Companion articles: [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html); [The Polar Form of the Dirac Equation in Biquaternionic Form](the-polar-form-of-the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html); [Relativistic Mechanics from the Dirac Wave](relativistic-mechanics-from-the-dirac-wave.html); [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html); [Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html); [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html).
