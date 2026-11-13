# __The Fourier Transform and the Schrödinger Equation in Biquaternionic Polar Variables__

## Introduction

**The transform has a phase, and the polar chart has a name for every factor of it.** The kernel of the transform is $e^{-i\theta_{\mathrm{pwp}}}$ with $\theta_{\mathrm{pwp}}=\omega t'-\vec k_\Phi\cdot\vec r$, so the kernel is a central unit times a sign. In the word of *The Schrödinger Equation in Biquaternionic Polar Variables* that kernel is the most degenerate element there is: scale one, no boost, rotor equal to a sign. **The transform is the operation that reads a field's phase and leaves everything else in place**, and the chart shows why.

**The second object is the word of the symbol.** The symbol of the companion article is an element of $\mathbb{B}$ at each frequency, so it has a word of its own: a scale, a phase, a boost and a rotor. Its quaternionic norm is $(\hbar\omega-h_t)^{2}-\lvert\vec h_\Psi\rvert^{2}$, and its determinant is that norm squared. **The word of the symbol fails exactly on the spectrum**, because the norm vanishes there and the element is a zero divisor. That is the polar reading of the pole set.

**The third finding is a count of types.** The four brackets of the logarithmic derivative are the four types of an element of $\mathbb{B}$: a real central number, an imaginary central number, a Hermitian traceless part and an anti-Hermitian traceless part, of dimensions one, one, three and three. In the constant setting the symbol occupies two of the four. **The other two are occupied only by a word that varies**, which is why the free equation's transform is exact.

**The fourth finding is that the phase is a character and the rotor is not.** The phase of the flow adds over intervals, exactly, for a constant Hamiltonian; the rotor multiplies. Composing a turn of $0.6$ about $\vec e_x$ with a turn of $0.9$ about $\vec e_y$ gives a turn of $1.070152$ and not of $1.5$. **The angle composes because it is a character of the time group; the rotor does not, because rotor space is a group under multiplication and not under addition.**

**The fifth finding is the conjugate pair.** The parent's kinetic Lagrangian is $-\hbar\,n\,\partial_{t'}\theta_{\mathrm{pha}}$ plus a rotor term, so the phase's conjugate momentum is $-\hbar$ times the density. The pair is $(\theta_{\mathrm{pha}},n)$, and $n=r^{2}$ makes the change of variable polynomial: $r\,\mathrm{d}r=\tfrac12\mathrm{d}n$, exact, with no weight. **The dual variable of this chart is flat**, and that is a property of a first-order equation.

**What this article is not.** It is not a second transform and not a second equation. It is the companion's symbol read in the word, and every number below is a number of the companion with a name attached.

## Conventions

The algebra, the units, the caret table and the two conjugations are those of *Algebra and Element Conventions*; the symbol rule is that of *Operator and Calculus Conventions*; the two forms are those of *Norm and Pairing Conventions*; the word, its domain and the two norms are those of *The Schrödinger Equation in Biquaternionic Polar Variables*.

**The word.** $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r}$, with $r>0$ the scale, $\theta_{\mathrm{pha}}$ the phase, $\tilde U_{\Psi,\mathrm b}$ the Hermitian boost of unit quaternionic norm, and $\tilde u_{\mathrm r}$ the real unit rotor. It is a bijection with the eight real components off the cone $\langle\tilde\Xi\rangle_\natural=0$.

**The two norms.** $\langle\tilde\Xi\rangle_\natural=r^{2}e^{2i\theta_{\mathrm{pha}}}$ reads the scale and the phase; $\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2r^{2}\cosh\theta_{\mathrm{rpd}}$ reads the scale and the rapidity. Neither reads the rotor, and neither reads an axis.

**The symbol.** $\sigma(\omega)=\hbar\omega\,e_t-\tilde H_\Psi$ with $h_t$ and $\vec h_\Psi$ real, and its two invariants $\operatorname{tr}\sigma=4(\hbar\omega-h_t)$ and $\det\sigma=\langle\sigma\rangle_\natural^{2}$.

## The Kernel of the Transform in the Word

**The kernel is a central unit times a sign.** The transform pairs a field with $e^{-i\theta_{\mathrm{pwp}}}$, and a central element of unit modulus has the word

$$
r=1,
\qquad
\theta_{\mathrm{pha}}=\theta_{\mathrm{pwp}},
\qquad
\tilde U_{\Psi,\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\pm e_t .
$$

**So the kernel carries one parameter and a sign.** The scale is one, the rapidity is zero, and the rotor is the branch $\pm e_t$ that the phase's half-angle forces at $\theta_{\mathrm{pha}}=\pi$. That is the same degeneration as the free propagator's word, computed in the polar parent, and the reason is the same: a central unit of modulus one can carry nothing else.

**The transform therefore moves one coordinate and touches no other.** Applied to a field of word $(r,\theta_{\mathrm{pha}},\tilde U_{\Psi,\mathrm b},\tilde u_{\mathrm r})$, the transform shifts the phase by the kernel's phase and multiplies the coefficients; the scale, the rapidity and the rotor are what the amplitudes carry, and the amplitudes are the transform of the field's non-central part. **The chart's reading of the transform is: the phase is the transform's variable and the other seven parameters are its data.**

**A caution about the sign.** The rotor $\pm e_t$ is not a second degree of freedom. It is the branch of the square root, and the polar parent fixes it as the sign of the modulus. A kernel's word with a negative rotor is the same kernel read on the other branch, and no physical statement distinguishes them.

**What the kernel cannot do.** It cannot change a scale or a rapidity, because it has neither. So the transform of a field has the same density profile in the frequency variable as the field has in time, up to the phase; the density is moved and not rescaled. **That is the exact content of "the transform is unitary" in the chart's letters.**

## The Word of the Symbol, and Where It Fails

**The symbol has a word because it is an element.** At each real $\omega$ the symbol $\sigma(\omega)=\hbar\omega\,e_t-\tilde H_\Psi$ is an element of $\mathbb{B}$, so it has a scale, a phase, a boost and a rotor whenever it is off the cone.

**Its quaternionic norm is the elementary determinant.** With $\sigma=c_t\,e_t+\sum c_\mu\vec e_\mu$ the norm is $c_t^{2}+c_x^{2}+c_y^{2}+c_z^{2}$, and here $c_t=\hbar\omega-h_t$ and $c_\mu=-ih_\mu$, so

$$
\langle\sigma(\omega)\rangle_\natural=\big(\hbar\omega-h_t\big)^{2}-\lvert\vec h_\Psi\rvert^{2},
\qquad
\det\sigma(\omega)=\langle\sigma(\omega)\rangle_\natural^{2},
$$

verified over one hundred draws to $2.1\times10^{-14}$. **The determinant of the companion is the square of a quaternionic norm**, and that identity is the whole of this section.

**The zeros of the determinant are the cone.** The word of a symbol exists exactly off the cone $\langle\cdot\rangle_\natural=0$, by the polar parent's domain proposition. So the frequencies at which the symbol has no word are exactly the spectrum. **The pole set is the cone**, and the statement is exact rather than asymptotic.

**The numbers, read as norms.** With $h_t=0.4$ and $\lvert\vec h_\Psi\rvert=0.616$, the norm is $-0.2200$ at $\omega=0$, $0.2600$ at $\omega=1.2$ and $2.1800$ at $\omega=-1.2$. The first is negative, so the symbol at zero frequency has a boost and a rotor but no scale in the quaternionic sense; the norm's sign is not a positivity statement and the chart does not read it as one.

**What the negative norm means in the chart.** A negative quaternionic norm makes $\langle\sigma\rangle_\natural$ a negative real, whose square root is $\pm i\lvert\cdot\rvert^{1/2}$: the phase of the symbol's word is $\pi/2$ and its scale is the fourth root of the modulus. **The symbol's phase is therefore not the dynamical phase**, and confusing the two is the error this paragraph exists to prevent.

**Why the cone and not a nodal set.** A zero divisor is not a vanishing element. The symbol at a zero of the determinant has a nonzero array whose rank drops to two, and only the quaternionic norm vanishes. The chart's failure at the cone is a failure of the parametrisation and not of the object, exactly as the polar parent says of the field.

## The Four Brackets Are the Four Types

**The decomposition of the algebra.** Every element of $\mathbb{B}$ is a sum of four pieces of distinct types:

| Type | Form | Real dimension | Name in the chart |
| --- | --- | --- | --- |
| real central | $a\,e_t$, $a\in\mathbb{R}$ | $1$ | the scale rate |
| imaginary central | $ib\,e_t$, $b\in\mathbb{R}$ | $1$ | the phase rate |
| Hermitian traceless | $i\vec g$, $\vec g\in\mathbb{R}^{3}$ | $3$ | the boost connection |
| anti-Hermitian traceless | $\vec v$, $\vec v\in\mathbb{R}^{3}$ | $3$ | the rotor connection |

The four add to eight, which is the algebra's real dimension, and the decomposition is direct because the types are distinguished by the two conjugations.

**The four brackets are these four pieces.** The polar parent's logarithmic derivative is

$$
\partial_{t'}\tilde\Xi=\tilde\Xi\Big[\tfrac12\partial_{t'}\ln r^{2}+i\partial_{t'}\theta_{\mathrm{pha}}+\tilde u_{\mathrm r}^{-1}\big(\tilde U_{\Psi,\mathrm b}^{-1}\partial_{t'}\tilde U_{\Psi,\mathrm b}\big)\tilde u_{\mathrm r}+\tilde u_{\mathrm r}^{-1}\partial_{t'}\tilde u_{\mathrm r}\Big],
$$

and the four terms are, in order, a real central number, an imaginary central number, a Hermitian traceless element and an anti-Hermitian traceless element. **The bracket is not four equations; it is one element read in its four types.**

**The symbol occupies two of the four.** In the constant setting the symbol is $\hbar\omega\,e_t-\tilde H_\Psi$, whose imaginary central part vanishes and whose anti-Hermitian traceless part vanishes. What remains is the real central part $\hbar\omega-h_t$ and the Hermitian traceless part $i\vec h_\Psi$. **The phase type and the rotor type are empty in frequency space**, and the emptiness is the statement that a plane wave has a constant phase rate and a constant rotor.

**The empty types are filled by a varying word.** A field whose phase rate varies with $t'$, or whose rotor turns, has a logarithmic derivative with all four types present. Its transform is then not supported at one frequency: the effective number of modes of a chirped unit is $5.64$ at a chirp rate of $1$ and $26.20$ at a rate of $4$ on a grid of sixty-four points, against $1.00$ for an integer tone. **The symbol is a model of the bracket, and the model is faithful exactly when the bracket is constant.**

**The two populated types are the two rates.** The real central part is the mean $(\hbar\omega-h_t)$ and the Hermitian traceless part is the gap $\lvert\vec h_\Psi\rvert$. The polar parent's two rates are the mean of the eigenvalues for the phase and the gap for every carried direction, so the symbol's two occupied types carry exactly the two rates.

## Which Parameters the Transform Moves

**One of eight.** The kernel's word has $\theta_{\mathrm{pha}}$ and nothing else, so the transform moves the phase and no other parameter. The scale, the rapidity, the boost axis and the rotor's angle and axis are carried by the amplitudes and are not translated by the transform.

**The density is invariant, and it is the modulus squared.** $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ is built from the amplitudes, so a transform that only shifts the phase leaves the total density unchanged. Parseval is the discrete form of that statement: on a grid of $4096$ points a superposition of three integer modes has $\sum_j\lvert c_j\rvert^{2}=1.562500000000$ and a grid norm equal to the same number to the last digit.

**A constant phase multiplies the modes and changes no modulus.** Multiplying the field by $e^{i\alpha}$ multiplies every coefficient $c_j$ by $e^{i\alpha}$, and $\lvert c_j\rvert$ is unchanged to $1.1\times10^{-16}$. **So the phase is the transform's invisible coordinate**: it enters the kernel and not the spectrum.

**That is why the phase is the gauge direction in the coupled chart.** The coupled polar companion records that the gauge group translates $\theta_{\mathrm{pha}}$ and nothing else. Here the same fact appears before any connection is introduced: the phase is the one coordinate a central unit of modulus one can shift.

**What the transform does move is the frequency.** The symbol's argument is the frequency, and the frequency is the time derivative of the phase for a single mode. **The transform's variable and the chart's phase rate are the same object read once as a label and once as a derivative.**

## The Eigenvalue Pair Is the Pole Set

**Two numbers, each twice.** The array $L_{\mathrm{axf}}(\tilde H_\Psi)$ has the eigenvalues $h_t+\lvert\vec h_\Psi\rvert$ and $h_t-\lvert\vec h_\Psi\rvert$, each with multiplicity two, and verified over one hundred draws to $1.8\times10^{-15}$ against the closed form. **The spectrum is a mean and a half-gap**, and the chart names the two numbers as the phase's rate and the rotor's rate.

**The pair is the pole set, and the poles are simple in the resolvent.** The determinant's zero is double because each eigenvalue is doubly degenerate; the resolvent $\sigma^{-1}$ has simple poles at the same two frequencies, with residues the two spectral projectors of rank two. The ranks were computed: the symbol has rank four off the zeros, rank two at a zero, and rank zero at the single zero of a scalar Hamiltonian.

**The pair is transmitted to the flow without change.** The parent's propagator is $e^{i\theta_{\mathrm{pha},Q}}\tilde u_Q$ with $\theta_{\mathrm{pha},Q}=-h_tt'/\hbar$ and $\theta_{\mathrm{axr},Q}=2\lvert\vec h_\Psi\rvert t'/\hbar$. So the phase runs at the mean and the rotor's angle at the gap, and the two rates are the two eigenvalues combined as a sum and a difference. **The map from the symbol's pair to the flow's two rates is the identity on the mean and the gap**, which is the sharpest statement of this section.

**The half-gap appears once and the gap twice.** The rotor's angle runs at the gap, and its half-angle at half the gap. That factor is the word's and not the parent's, as the polar companion says, and it is why the gap has to be read twice.

**What the pair does not fix.** The pair does not fix the rotor's axis. Every Hamiltonian with the same $\lvert\vec h_\Psi\rvert$ and a different direction has the same two frequencies and a different axis, so the axis is frame data and not spectrum. **A frequency pair is not a state**, and the chart is the place where that becomes visible.

**The degenerate case.** For a scalar Hamiltonian the pair collapses to one number of multiplicity four, the rotor's angle does not run, and the flow is a pure phase. The chart's four types then reduce to one, and the rank of the symbol at the zero is zero.

## The Angle Is a Character

**The additivity.** For a constant Hamiltonian the phase of the flow is linear in the interval, so

$$
\theta_{\mathrm{pha}}(t'_1+t'_2)=\theta_{\mathrm{pha}}(t'_1)+\theta_{\mathrm{pha}}(t'_2),
\qquad
\theta_{\mathrm{pha}}(t')=-\frac{h_t}{\hbar}t' .
$$

That is a homomorphism from the additive group of times to the circle, and it is exact. **A character of the time group is what a Fourier kernel's exponent is**, and the parent's additivity is the statement that the phase is one.

**The rotor is not a character.** The rotor obeys $\tilde u_Q(t'_1+t'_2)=\tilde u_Q(t'_1)\tilde u_Q(t'_2)$ with $\tilde u_Q=\cos\theta+\sin\theta\,\vec u_\Psi$, and its angles do not add when the axes differ. Composing a turn of $0.6$ about $\vec e_x$ with a turn of $0.9$ about $\vec e_y$ gives a turn of $1.070152$, not $1.5$. **The rotor composes by multiplication and its angle is not a homomorphism**, and the failure is first order in the angle between the axes.

**The same axis is the exception.** Two turns about one axis compose to the sum, exactly: $0.6$ and $0.9$ about $\vec e_x$ gave $1.500000000$. A one-parameter subgroup is a character in its own angle, and that is why the parent can speak of a rotor angle at all.

**The scale is not a character either.** Scale multiplies rather than adds, so the scale of a product is the product of the scales. On the central field the scale is a modulus and its evolution is frozen, so the question does not arise there; on a general field the scale is frozen too, and the reason is the same unitarity that fixes the rapidity.

**The density is not a character.** A superposition's density is not the sum of the densities: the interference terms are exactly what the cross terms of the squared modulus supply. **So of the four factors, only the phase composes additively**, and the article states that as the chart's rendering of the companion's affine dependence on $\omega$.

**What composes is what the transform sees.** The phase is the transform's variable, and it is the one factor that adds. The scale, the rotor and the density do not add, and none of them is the transform's argument. **The correspondence is exact and it is not a coincidence**: a transform is a homomorphism on the group whose character the exponent is.

## The Angle and the Density Are Conjugate

**The parent's kinetic Lagrangian.** The polar variational parent computes

$$
K=-\hbar\,r^{2}\cosh\theta_{\mathrm{rpd}}\;\partial_{t'}\theta_{\mathrm{pha}}+\frac{\hbar}{2}r^{2}\sinh\theta_{\mathrm{rpd}}\,\big(\vec\Omega\cdot\vec u_{\mathrm b}\big),
$$

with $n=r^{2}\cosh\theta_{\mathrm{rpd}}=\rho/2$. So the coefficient of the phase's rate is $-\hbar n$, and the conjugate momentum of the phase is

$$
p_\theta=\frac{\partial K}{\partial(\partial_{t'}\theta_{\mathrm{pha}})}=-\hbar\,n .
$$

**The density is the conjugate momentum of the phase.** The statement is the parent's and it is one line here. **It is also the reason the phase is the transform's variable**: a pair $(q,p)$ with $p$ the density is exactly what a transform in $q$ acts on.

**The pair is invariant in the coupled chart.** The coupled polar parent records $p_\theta=-\hbar N$ and its invariance under the gauge transformation, and the invariance is the statement that the pair survives the coupling. **The transform's variable is therefore gauge invariant as a variable**, even though the phase itself is translated.

**The pair is not a pair of independent data.** On a central field $n=r^{2}$ and the two functions are the two unknowns of Madelung's pair; on a general field the rapidity enters $n$ and the density is a function of two parameters. **The conjugacy is between the phase and the density, not between the phase and the scale**, and the distinction matters as soon as the field is not central.

**A check on the sign.** The sign of $p_\theta$ is fixed by the sign of the kinetic term, which is the parent's, and it is negative. A positive sign would reverse the sense of the phase's evolution; the article keeps the parent's sign and does not re-derive the Lagrangian.

## The Dual Variable Is Flat

**The change of variable.** $n=r^{2}$, so

$$
\mathrm{d}n=2r\,\mathrm{d}r,
\qquad
r\,\mathrm{d}r=\tfrac12\,\mathrm{d}n .
$$

The Jacobian is $2r$, polynomial in the chart's own variable, and it vanishes only at $r=0$, which is the cone. **The dual variable is flat**: no weight beyond the flat one is needed to integrate over $n$, and the equation's own variable $r$ is its square root.

**Why this is a property of the first order.** The polar parent states the contrast in one sentence: here the density is a norm and not the temporal slot of a current, so it has no sign to lose. A norm is a square, and a square is a polynomial change of variable. **A second-order equation's density is the temporal slot of a current, its sign is the sign of the energy, and no polynomial square of the chart's amplitude produces it**; that is why the second-order chart has no flat dual.

**The flat dual is not a measure statement about the algebra.** It is a statement about the pair $(\theta_{\mathrm{pha}},n)$ and its two coordinates. The algebra's own measure is not at issue, and the article does not construct one.

**What the flat dual buys.** The transform in $\theta_{\mathrm{pha}}$ has $n$ as its dual variable, and the change of variable from $r$ to $n$ is exact, so the transform's normalisation is the standard one. **No weight is inserted and none is dropped**, and the check is the Jacobian line above.

## What the Polar Reading Adds

**The type statement.** The symbol's two occupied types are the two rates, and the two empty types are the two things a constant word cannot vary. **This is the chart's sharpest addition**: it says which of the eight parameters the frequency can address.

**The domain statement.** The spectrum is the cone. The word of the symbol fails exactly where the symbol is singular, and the failure is a failure of the parametrisation. The polar parent's domain proposition and this article's pole set are one statement.

**The composition statement.** The phase composes because it is a character; the rotor, the scale and the density do not. That is the chart's rendering of the fact that the transform's exponent is affine in the frequency.

**What it does not add.** No new prediction, no new solution, no closure of the operator setting. The chart is a lens, and the lens is exact.

## Limits

**Constant coefficients.** The symbol's word exists where the field's word exists, and both need a constant Hamiltonian. Where the Hamiltonian varies, the symbol is a convolution and has no word to read.

**The cone is not a physical boundary.** The symbol has no word on the cone and a field has none there either. The two failures coincide because they are one failure, and the article claims nothing more than that coincidence.

**One time.** The chart is the time chart and the transform is in one variable. A four-dimensional transform would need the spatial chart as well, which the Dirac and Klein–Gordon polar companions supply for their own equations.

## Open Questions

**The first question is the varying word.** A field whose phase rate varies has no symbol, and its transform is broad. Whether the chart supplies a substitute — a local frequency, a Wigner-type reading — that plays the symbol's role for such a field is not settled here.

**The second is the sign of the symbol's norm.** A negative quaternionic norm makes the symbol's own phase $\pi/2$ and its scale a fourth root. Whether that phase has a dynamical meaning, or is an artefact of reading a symbol as a field, is not decided.

**The third is the coupled chart's pair.** The pair $(\theta_{\mathrm{pha}},n)$ is invariant under the gauge transformation, and the connection enters the phase's rate. Which variable replaces $n$ when the connection is time dependent is the coupled companion's question, and it is open there too.

**The fourth is the operator setting.** With $\tilde H_\Psi=\hat H\,e_t$ the symbol becomes a convolution, and the chart's two rates become functions of position. Whether the chart survives as a local reading, with the quantum potential as the residue, is the polar parent's open question and it is not answered here.

## Summary

The transform's kernel is a central unit of modulus one, so its word has scale one, no boost, a phase and a sign. **The transform moves the phase and nothing else**, and the phase is the one coordinate a central unit can shift.

The symbol's word fails exactly on the spectrum, because the determinant is the square of the quaternionic norm, $\det\sigma=\langle\sigma\rangle_\natural^{2}$ to $2.1\times10^{-14}$, and the norm vanishes on the cone. The four brackets of the logarithmic derivative are the four types of the algebra, of dimensions one, one, three and three; in the constant setting the symbol occupies the real central and the Hermitian traceless types, which are the mean and the gap, and the other two are empty.

The phase is a character and the rotor is not: $0.6$ and $0.9$ about different axes compose to $1.070152$ and not to $1.5$, while the same axis gives $1.500000000$ exactly. The phase's conjugate momentum is $-\hbar n$, and $n=r^{2}$ gives $r\,\mathrm{d}r=\tfrac12\mathrm{d}n$: **the dual variable of this chart is flat**, and the flatness is a property of a first-order equation.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\theta_{\mathrm{pwp}}=\omega t'-\vec k_\Phi\cdot\vec r$ | The plane wave's phase; the transform's exponent |
| $r=1$, $\tilde U_{\Psi,\mathrm b}=e_t$, $\tilde u_{\mathrm r}=\pm e_t$ | The word of the transform's kernel |
| $\langle\sigma\rangle_\natural=(\hbar\omega-h_t)^{2}-\lvert\vec h_\Psi\rvert^{2}$ | The symbol's quaternionic norm; the elementary determinant |
| $\det\sigma=\langle\sigma\rangle_\natural^{2}$ | The determinant; its zeros are the cone, hence the spectrum |
| $h_t\pm\lvert\vec h_\Psi\rvert$ | The two eigenvalues; the mean and the gap; the two rates |
| $1+1+3+3=8$ | The four types of the bracket, and their dimensions |
| $p_\theta=-\hbar n$ | The phase's conjugate momentum; the density |
| $n=r^{2}\cosh\theta_{\mathrm{rpd}}=\rho/2$ | The density; the dual coordinate |
| $r\,\mathrm{d}r=\tfrac12\mathrm{d}n$ | The flat dual; the Jacobian $2r$ |
| $\theta_{\mathrm{axr},Q}=2\lvert\vec h_\Psi\rvert t'/\hbar$ | The rotor's angle; the gap, read twice |

## Further Reading

- *The Schrödinger Equation in Biquaternionic Polar Variables*, for the word, its domain, the four brackets and the two rates this article reads in frequency space.
- *The Fourier Transform and the Schrödinger Equation in Biquaternionic Form*, for the symbol, its determinant and the counts of poles.
- *The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables*, for the kinetic Lagrangian, the factor $\cosh\theta_{\mathrm{rpd}}$ and the conjugate momentum $-\hbar n$.
- *The Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the gauge direction of the chart and the invariance of the pair.
- *The Fourier Transform, the Variational Principle and the Schrödinger Equation in Biquaternionic Form*, for the action's quadratic form at fixed frequency.
- *Algebra and Element Conventions*, for the four types and the two conjugations that separate them.
