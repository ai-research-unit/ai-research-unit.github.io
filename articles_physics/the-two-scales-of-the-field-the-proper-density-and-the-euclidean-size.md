# __The Two Scales of the Field: the Proper Density and the Euclidean Size__

## Introduction

**The fluid block calls one number the density and never asks what the field's size is.** The polar word writes $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, and every article of the block reads the scale $r$ as the density, $\rho_{\mathrm{num}}=r^{2}$. The element also has a second number, the Euclidean size $\langle\tilde\Xi\rangle_{*}=\sum_\mu\lvert\Xi_\mu\rvert^{2}$, which the algebra supplies without a chart and which no article of the block uses.

**The two numbers are not equal, and their ratio is the boost.** Off the null cone,

$$
\frac{\langle\tilde\Xi\rangle_{*}}{\lvert N(\tilde\Xi)\rvert}=\cosh\theta_{\mathrm{rpd}},
\qquad
\rho_{\mathrm{num}}=\lvert N(\tilde\Xi)\rvert=r^{2},
$$

so the proper density is the Euclidean size divided by the fluid's own Lorentz factor. The ratio is exact and not an approximation, and it is the same rapidity the velocity is built from.

**Three consequences, and they are the article.** First, the Euclidean size is not a second and looser notion of density: at the spinor rung it is the time component of the block's own number current over $c$, up to the algebra's $i$, so the two numbers are the invariant length and the time component of one four-vector. Second, at the scalar rungs the ratio is identically one, because a central element has no second real dimension to be non-parallel to; that is why the block could be written below the spinor rung and exhibit none of this. Third, on the null cone the ratio has no value and diverges along every approach to it, while the Euclidean size stays at the field's full size: the chart's density vanishes where the field does not.

**What is new here, stated plainly.** The identity $\langle\tilde Q\rangle_{*}^{2}=\lvert N(\tilde Q)\rvert^{2}+4A^{2}$ is Lagrange's identity in $\mathbb{R}^{4}$, applied to the real and imaginary four-vectors of the coefficients; it is classical, and no algebraic theorem is claimed. The contribution is interpretive and organizational: the corpus has one number under two names, $r^{2}$ and $r^{2}\cosh\theta_{\mathrm{rpd}}$, and two articles spell it differently without a stated relation. **This article supplies the relation, identifies which name belongs to which quantity, and records what each name does at the cone.** Two further statements are proved here and are not quotations: the transformation law of §*Transformation Properties*, which shows that the Euclidean size is the time component and the modulus the invariant length, and the factor of two between the spinor and vector carriers of §*The Factor of Two, and the Two Carriers*.

**Status.** The identities are proved in §*Appendix: The Algebra* from the eight real coordinates. The numerical values quoted throughout were computed independently of the word's parameters, from the eight real coordinates, and their residuals are collected in §*Appendix: The Algebra*, §*The Numerical Checks*; they confirm the algebra and are not a substitute for it. The polar word, its four factors and the density $\rho_{\mathrm{num}}=r^{2}$ are [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html); the current and its reading are [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html); the ratio of the two invariants as a rapidity is [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html) for the vector case, and this article supplies the spinor case and the factor of two between them; the cone is [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) and [The Meaning of N-Regularity and Degeneracy](the-meaning-of-n-regularity-and-degeneracy.html); the degenerate factorisation is [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html).

## Conventions and Notation

**The element.** $\tilde Q=Q_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_\mu\in\mathbb{C}$, the product fixed by $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^{2}=-e_t$, the scalar $i$ central. The symbol $e_t$ is the algebra's unit, not a time coordinate; $E$ and $t$ are reserved for energy and coordinate time, so no confusion arises.

**The two norms.** $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ is the **quaternionic norm**: complex-valued, multiplicative, vanishing on the zero-divisor cone $\mathcal N$. $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ is the **Euclidean size**, also called the Hermitian norm $H$: real, non-negative, definite. $\mathrm{Sc}\,\tilde Q=Q_t$ is the scalar part and $\vec Q$ the vector part, so $\tilde Q=Q_t+\vec Q$.

**The two cases.** An element is **$N$-regular** when $N(\tilde Q)\neq0$, which is exactly when it is invertible; it is **$N$-degenerate** when $N(\tilde Q)=0$ with $\tilde Q\neq0$, which is a zero divisor [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html). The degenerate set is the **null cone** $\mathcal N$, one complex equation and therefore two real equations, of real codimension two.

**The polar word.** On the regular elements, and only there, $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ the central phase, $\tilde U_{\Psi,\mathrm b}$ the **boost factor**, $\tilde u_{\mathrm r}$ the rotor [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html). With $\vec u_{\mathrm b}$ a real unit pure quaternion, $\vec u_{\mathrm b}^{2}=-e_t$, the boost factor is

$$
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b},
$$

with $\theta_{\mathrm{rpd}}\ge0$ the **rapidity**. The half-angle in the exponent is the subject of §*The Factor of Two, and the Two Carriers*.

**The two names for the density.** The block's fluid articles write $\rho_{\mathrm{num}}=r^{2}$ and call it the **proper density**. The polar-variable articles write $n=r^{2}\cosh\theta_{\mathrm{rpd}}$ and call it the **density** [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html). This article shows that the first is the invariant length of the current over $c$ and the second its time component over $c$, and proposes no change of letters: **the two names stay, and the relation between them is the subject.**

**Units.** The field $\tilde\Xi$ carries the amplitude's units, $r$ and $\langle\tilde\Xi\rangle_{*}$ their square, $\rho_{\mathrm{num}}$ and $n$ the units of a number density, and $j^{0}$ density times velocity. No numerical value in this article depends on the units, all statements being ratios or identities between quantities of the same dimension.

## The Two Numbers

**One element, two numbers, and they differ by the boost.**

$$
N(\tilde\Xi)=r^{2}e^{2i\theta_{\mathrm{pha}}},
\qquad\text{so}\qquad
\lvert N(\tilde\Xi)\rvert=r^{2}=\rho_{\mathrm{num}},
$$

whereas

$$
\langle\tilde\Xi\rangle_{*}=r^{2}\cosh\theta_{\mathrm{rpd}}=n .
$$

**The second is not a function of the four factors one at a time, and it is not multiplicative.** $e_t+i\vec e_x$ and $e_t-i\vec e_x$ each have Euclidean size $2$ and their product is $0$, so $\langle\cdot\rangle_{*}$ is not a homomorphism; the modulus $N$ is. What the size does have is invariance: the phase and the rotor act on the four complex coefficients by unitary transformations and leave the size fixed, while the boost acts hyperbolically and moves it. **The invariant is the modulus and the frame-dependent number is the size**, which §*Transformation Properties* makes precise.

**The two numbers on five elements.**

| element | $N$ | $\lvert N\rvert$ | $\langle\cdot\rangle_{*}$ | ratio |
| --- | --- | --- | --- | --- |
| $e_t+\vec e_x$ | $2$ | $2$ | $2$ | $1$ |
| $2e_t+i\vec e_z$ | $3$ | $3$ | $5$ | $5/3=1.6667$ |
| $e_t+(1+i)\vec e_x$ | $1+2i$ | $\sqrt5=2.2361$ | $3$ | $1.3416$ |
| $e_t+i\vec e_z$ | $0$ | $0$ | $2$ | no value |
| $\vec e_x+i\vec e_y$ | $0$ | $0$ | $2$ | no value |

**The first row is a real element, its rapidity is zero, and the two numbers agree.** The second is a pure boost with $r=\sqrt3$ and $\cosh\theta_{\mathrm{rpd}}=5/3$. The third carries a central phase, which the ratio does not see. The last two are on the cone: there the ratio has no value and the Euclidean size is still two — not small, not zero, and not tending to zero.

## The Inequality, and What Equality Means

**The quaternionic norm never exceeds the Euclidean size in modulus.**

$$
\lvert N(\tilde Q)\rvert\le\langle\tilde Q\rangle_{*},
$$

with equality exactly when the four coefficients have a common argument modulo $\pi$, that is when $\tilde Q=\varkappa\tilde R$ with $\varkappa$ a complex unit and $\tilde R$ real.

*Proof.* $\lvert\sum_\mu Q_\mu^{2}\rvert\le\sum_\mu\lvert Q_\mu\rvert^{2}$ is the triangle inequality, since $\lvert Q_\mu^{2}\rvert=\lvert Q_\mu\rvert^{2}$. Equality in the triangle inequality needs the summands to be non-negative real multiples of one another, $Q_\mu^{2}=\varkappa^{2}r_\mu^{2}$ with $\varkappa$ a fixed unit and $r_\mu\ge0$; then $Q_\mu=\varkappa\,\epsilon_\mu r_\mu$ with $\epsilon_\mu=\pm1$, and the signs are absorbed into real coefficients. **The full derivation, including the sign bookkeeping, is §*Appendix: The Algebra*, §*The Triangle Inequality*.**

**So the inequality is the statement that a boost costs Euclidean size at fixed modulus.** The word's scale is a modulus and its velocity a direction, and the Euclidean size charges for the direction. **That is why the ratio can be read as a kinematic quantity at all**: it is not an arbitrary function of eight real numbers, it is the price of the velocity, and §*Transformation Properties* shows that the price transforms as a time component.

## The Gap Is the Boost

**Write the element as two real four-vectors.** Put $Q_\mu=a_\mu+ib_\mu$ with $a,b\in\mathbb{R}^{4}$. Then

$$
N(\tilde Q)=\bigl(\lvert a\rvert^{2}-\lvert b\rvert^{2}\bigr)+2i\,a\cdot b,
\qquad
\langle\tilde Q\rangle_{*}=\lvert a\rvert^{2}+\lvert b\rvert^{2},
$$

a difference of squares and a sum of squares of the same two lengths: a Lorentzian pair. The missing piece is the angle between them, and it enters through the Lagrange identity in $\mathbb{R}^{4}$:

$$
\langle\tilde Q\rangle_{*}^{2}=\lvert N(\tilde Q)\rvert^{2}+4A^{2},
\qquad
A^{2}=\sum_{j\lt k}\bigl(a_jb_k-a_kb_j\bigr)^{2}=\lvert a\rvert^{2}\lvert b\rvert^{2}-(a\cdot b)^{2},
$$

with $A$ the area of the parallelogram spanned by $a$ and $b$, the sum running over the six coordinate planes of $\mathbb{R}^{4}$. **The two forms of $A^{2}$ are quoted together because the first displays the geometry and the second is what makes the identity algebraic.** The symbol $A$ is the area; the Proca potential $\tilde A_\Phi$ carries a tilde and a label and is a different object.

*Proof.* $\lvert N\rvert^{2}=(\lvert a\rvert^{2}-\lvert b\rvert^{2})^{2}+4(a\cdot b)^{2}$ and $\langle\cdot\rangle_{*}^{2}=(\lvert a\rvert^{2}+\lvert b\rvert^{2})^{2}$, so the difference is $4(\lvert a\rvert^{2}\lvert b\rvert^{2}-(a\cdot b)^{2})$, and Lagrange's identity turns the bracket into the sum over pairs. **Every step is in §*Appendix: The Algebra*, §*The Lagrange Identity*.**

**Divide by $\lvert N\rvert^{2}$ and the square is a hyperbolic identity.**

$$
\Bigl(\frac{\langle\tilde Q\rangle_{*}}{\lvert N\rvert}\Bigr)^{2}-\Bigl(\frac{2A}{\lvert N\rvert}\Bigr)^{2}=1,
\qquad\text{hence}\qquad
\cosh\theta_{\mathrm{rpd}}=\frac{\langle\tilde Q\rangle_{*}}{\lvert N\rvert},\quad
\tanh\theta_{\mathrm{rpd}}=\frac{2A}{\langle\tilde Q\rangle_{*}} ,
$$

for an element off the cone and $N$-regular.

**What the second display says and does not say.** It says that the parametrisation is hyperbolic: the pair $(\langle\cdot\rangle_{*},2A)$ lies on a hyperbola of radius $\lvert N\rvert$, and $\tanh\theta\le1$ is a property of that hyperbola. **It does not derive physical causality.** A velocity bound follows only after the identification of $\vec v/c$ with a tangent of this angle, which is the fluid reading's input and not the algebra's output. Within the reading the bound is automatic; as a statement about Nature it is a statement about the reading.

**Measured on three boosted elements with $r=1.3$, $\theta_{\mathrm{pha}}=0.4$.** The second column is computed from the eight real coordinates alone, the third from the word's parameter:

| $\theta_{\mathrm{rpd}}$ | $\langle\cdot\rangle_{*}/\lvert N\rvert$ | $\cosh\theta_{\mathrm{rpd}}$ | $2A/\langle\cdot\rangle_{*}$ | $\tanh\theta_{\mathrm{rpd}}$ |
| --- | --- | --- | --- | --- |
| $0.5493$ | $1.1547005$ | $1.1547005$ | $0.5000000$ | $0.5000000$ |
| $1.0986$ | $1.6666667$ | $1.6666667$ | $0.8000000$ | $0.8000000$ |
| $3.0000$ | $10.0676620$ | $10.0676620$ | $0.9950548$ | $0.9950548$ |

**Both columns agree to the seven decimals printed, a residual below $5\times10^{-8}$, and that agreement is a check of the identity and not its proof.**

## Transformation Properties

**The distinction the words "size" and "density" carry is a distinction under boosts, so the two numbers must be followed through one.** Take an $N$-regular element $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}(c_h+is_h\vec u_{\mathrm b})$ with $c_h=\cosh\frac{\theta_{\mathrm{rpd}}}{2}$, $s_h=\sinh\frac{\theta_{\mathrm{rpd}}}{2}$, and act on the left by a boost factor of rapidity $\phi$ about the real unit axis $\vec u_{\phi}$,

$$
\tilde U_{\mathrm b}(\phi,\vec u_{\phi})=\cosh\frac{\phi}{2}+i\sinh\frac{\phi}{2}\vec u_{\phi} .
$$

**The modulus does not move.** $N(\tilde U_{\mathrm b}\tilde\Xi)=N(\tilde U_{\mathrm b})N(\tilde\Xi)$ and $N(\tilde U_{\mathrm b})=\cosh^{2}\frac\phi2-\sinh^{2}\frac\phi2=1$, so

$$
\lvert N(\tilde\Xi')\rvert=\lvert N(\tilde\Xi)\rvert=r^{2}:\quad\text{the invariant length is invariant.}
$$

**The Euclidean size moves as a time component.** With $\chi$ the angle between $\vec u_{\mathrm b}$ and $\vec u_{\phi}$,

$$
\langle\tilde\Xi'\rangle_{*}=r^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\cosh\phi+\sinh\theta_{\mathrm{rpd}}\sinh\phi\cos\chi\Bigr),
$$

which is $\gamma_\phi\bigl(u^{0}+\beta_\phi\,\vec u_{\phi}\cdot\vec u\bigr)$ for the four-velocity $u^{\mu}=(\cosh\theta_{\mathrm{rpd}},\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b})$, scaled by $r^{2}$. **The two special cases are the memorable ones**: for a boost along the flow, $\langle\tilde\Xi'\rangle_{*}=r^{2}\cosh(\theta_{\mathrm{rpd}}+\phi)$, the rapidity adding; for a boost perpendicular to it, $\langle\tilde\Xi'\rangle_{*}=r^{2}\cosh\theta_{\mathrm{rpd}}\cosh\phi$, the two Lorentz factors multiplying. *Proof and residuals: §*Appendix: The Algebra*, §*The Boost Composition*.*

**So the ratio is the flow's Lorentz factor and transforms as one.** $\langle\tilde\Xi\rangle_{*}/\lvert N\rvert=\cosh\theta_{\mathrm{rpd}}$ is the time component of the four-velocity, and the sentence "the Euclidean size is the coordinate density" is the statement that a coordinate density is a time component. **$\lvert N\rvert$ is a scalar of the theory; $\langle\cdot\rangle_{*}$ is not**, and the phrase "the field's size" is therefore misleading wherever it appears in the block: the field has no Lorentz-invariant **Euclidean** size, it has an invariant modulus and a frame-dependent time component.

**Verified on five angles and three boosts.** With $r=1$, $\theta_{\mathrm{rpd}}=1.0986$, $\phi=0.7$, the measured $\langle\tilde\Xi'\rangle_{*}$ and the displayed law agree to $1.3\times10^{-15}$ at $\chi=0^{\circ},30^{\circ},60^{\circ},90^{\circ},180^{\circ}$, and $\lvert N\rvert$ stays at $1$ to $2\times10^{-16}$ throughout.

## The Element's Size Is the Current's Time Component

**At the spinor rung the Euclidean size is already in the block, under another name.** The current is $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi$ with $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), where

$$
\tilde U_{\Psi,\mathrm b}^{-2}=\cosh\theta_{\mathrm{rpd}}-i\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
\qquad
\tilde J_\Phi=ic\gamma\rho_{\mathrm{num}}\,e_t+\rho_{\mathrm{num}}\gamma\vec v .
$$

**The scalar part carries the $i$, and the $i$ is the corpus's, not a slip.** The time component of the corpus's four-vectors is written with an imaginary coefficient, $\tilde P_\Phi=i\frac{E}{c}e_t+\vec p$ [The Material Sector](the-material-sector-four-vectors-interval-and-lorentz-action.html), so the coefficient of $e_t$ in a current is $i$ times the physical time component. Hence

$$
\mathrm{Sc}(\tilde J_\Phi)=ic\,\gamma\rho_{\mathrm{num}}=ic\,\langle\tilde\Xi\rangle_{*},
\qquad\text{so}\qquad
\langle\tilde\Xi\rangle_{*}=\frac{\mathrm{Sc}(\tilde J_\Phi)}{ic}=\frac{j^{0}}{c},
$$

with $j^{0}=\gamma\rho_{\mathrm{num}}c=\mathrm{Im}\,\mathrm{Sc}(\tilde J_\Phi)$ the real time component. **The first display is the form to quote; the bare $\mathrm{Sc}(\tilde J_\Phi)/c$ is wrong by a factor $i$ and would give an imaginary density.**

**Checked on three words**, with $r=1.3$, $\theta_{\mathrm{pha}}=0.4$ and $\theta_{\mathrm{rpd}}\in\{0,1.0986\}$, and with $r=0.7$, $\theta_{\mathrm{pha}}=-2$, $\theta_{\mathrm{rpd}}=2.5$: the two sides of the second display agree to $4\times10^{-16}$, and $\mathrm{Re}\,\mathrm{Sc}(\tilde J_\Phi)$ vanishes to $0$.

**Write the current's components plainly.** The element $\tilde J_\Phi$ is the corpus's biquaternion current, whose scalar coefficient is $i$ times the physical time component. Put $j^{0}=\gamma\rho_{\mathrm{num}}c$ for the number density times $c$ and $\vec j=\gamma\rho_{\mathrm{num}}\vec v$ for the flux, so that $\tilde J_\Phi=ij^{0}e_t+\vec j$. **Then $\mathrm{Sc}(\tilde J_\Phi)=ij^{0}$ and $\langle\tilde\Xi\rangle_{*}=j^{0}/c$**, the second display of this section.

**So the pair of numbers is one four-vector's invariant length and time component.** The proper density is the invariant length over $c$; the Euclidean size is the time component over $c$; the ratio is the Lorentz factor of the flow that carries it. **The spatial components of the current are not discussed here** and are not implied by any statement above: what is claimed is the pair $(j^{0},\lvert j\rvert)$ against the two numbers, and only through the standard relation $j^{0}=\gamma\rho c$ which the corpus's $\tilde V_\Phi$ already states.

**Two names, and one letter twice.** A reader who takes $\rho_{\mathrm{num}}=r^{2}$ for the field's size is reading $j^{0}/\gamma$; a reader who takes $n$ for the proper density is reading $j^{0}/c$ unnormalised. **Neither name is wrong and the pair is the standard one; the error is to use one where the other is meant**, and it costs exactly the factor $\cosh\theta_{\mathrm{rpd}}$ — one at rest, and unbounded near the cone, which is precisely the regime where the two are confused.

## The Scalar Rungs Show Nothing

**A central element has $a$ and $b$ collinear, so the parallelogram is degenerate and the two numbers coincide.**

$$
\tilde\Xi=\Xi_t e_t,\quad a=(\mathrm{Re}\,\Xi_t,0,0,0),\quad b=(\mathrm{Im}\,\Xi_t,0,0,0)
\quad\Longrightarrow\quad A=0,\quad \langle\tilde\Xi\rangle_{*}=\lvert N(\tilde\Xi)\rvert .
$$

**The reason is dimensional and not dynamical.** A central element's eight real coordinates occupy a two-dimensional real subspace, and the real and imaginary parts lie on the same real line through the origin, so the parallelogram they span has no area. No boost exists in one complex dimension, so $\cosh\theta_{\mathrm{rpd}}=1$ identically and the Schrödinger and Klein–Gordon rungs have one scale and not two.

**That is why the block could be written for the scalar rungs and say nothing about this.** Every statement about the two scales is invisible below the spinor rung, and the three quantities that separate them — the boost, the velocity and the $\gamma$ — are exactly the ones the first-order rung does not have. **The two scales appear when the element stops being central and not before**, which is the same threshold at which the block's fluid equations acquire the spin terms that keep them from closing. *Why they do not close is [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), §on the non-closure of the three bilinears, and is not re-derived here.*

## On the Cone the Ratio Has No Value

**The polar word exists exactly on the $N$-regular set**, so on the cone the ratio $\langle\tilde\Xi\rangle_{*}/\lvert N(\tilde\Xi)\rvert$ is not merely large: it has no value. **It diverges along every approach to a nonzero point of the cone**, that is along every path on which the limiting Euclidean size is nonzero; a path whose amplitude also goes to zero can give any ratio at all, and carries no information, because it leaves the field's own value as well as the chart. The two numbers behave in opposite ways at fixed field size:

$$
\rho_{\mathrm{num}}=\lvert N\rvert\longrightarrow0,
\qquad
\langle\tilde\Xi\rangle_{*}=r^{2}\cosh\theta_{\mathrm{rpd}}\longrightarrow\langle\tilde\Xi\rangle_{*}\neq0 .
$$

**The gap is unbounded and the field is not small.** A chiral field with $\tilde\Xi\vec e_z=-i\tilde\Xi$ is the clean case: $N=0$ and $\langle\tilde\Xi\rangle_{*}=2$ for $\tilde\Xi=e_t+i\vec e_z$, with no word to read.

**The cone is reached at infinite rapidity with a vanishing scale.** The massless path is

$$
r\longrightarrow0,\qquad
\theta_{\mathrm{rpd}}\longrightarrow\infty,\qquad
r\cosh\frac{\theta_{\mathrm{rpd}}}{2},\ r\sinh\frac{\theta_{\mathrm{rpd}}}{2}\ \text{finite},
$$

which sends $\rho_{\mathrm{num}}\to0$ and $\langle\tilde\Xi\rangle_{*}\to$ twice the square of the surviving half-amplitude. For the chiral element the two halves are $1$ and $1$, so the Euclidean size is $2$ in the limit and $j^{0}/c$ is $2$.

**So the cone is where the ratio is undefined and the pair is not.** $\cosh\theta_{\mathrm{rpd}}$ diverges and $r^{2}$ vanishes separately while $\langle\tilde\Xi\rangle_{*}$ is continuous: **a limit taken on the ratio is meaningless and a limit taken on the pair $(\rho_{\mathrm{num}},\langle\tilde\Xi\rangle_{*})$ is not.** That is the boundary-value statement of [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html), read as a statement about two numbers instead of about the word.

## What Each Variable Becomes

**The chart's variables and the algebra's numbers on the two regions.**

| quantity | off the cone | on the cone | reason |
| --- | --- | --- | --- |
| $\rho_{\mathrm{num}}=r^{2}=\lvert N\rvert$ | $>0$ | $0$ | the norm vanishes |
| $\langle\tilde\Xi\rangle_{*}$ | $\ge\rho_{\mathrm{num}}$ | $>0$ | definite on the whole algebra |
| $n=r^{2}\cosh\theta_{\mathrm{rpd}}$ | $=\langle\tilde\Xi\rangle_{*}$ | $=\langle\tilde\Xi\rangle_{*}$ | the same number throughout |
| $\cosh\theta_{\mathrm{rpd}}$ | finite, $\ge1$ | no value | the word's factor does not exist |
| $\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$ | $\lvert\vec v\rvert=c\tanh\theta_{\mathrm{rpd}}\lt c$ | the word does not exist; $\lvert\vec v\rvert\to c$ along the limiting flow | the boost cannot be normalised |
| $r$ | $>0$ | $0$ | the modulus does not exist |
| $A$ | $\le\langle\tilde\Xi\rangle_{*}/2$ | $=\langle\tilde\Xi\rangle_{*}/2$ | equality is $\tanh\theta=1$ |

**The fourth and seventh rows are one statement.** A zero divisor has $\lvert N\rvert=0$ and $A=\langle\cdot\rangle_{*}/2$, so its pair $(a,b)$ spans a maximal parallelogram: **the real and imaginary parts of a zero divisor are as non-parallel as two vectors of fixed lengths can be**, and the flow that would carry it moves at $c$ in the limit.

## Rung by Rung

**The four rungs, with the angle at which the boost sits in the element.**

| rung | element | $\langle\cdot\rangle_{*}/\lvert N\rvert$ | the density in use |
| --- | --- | --- | --- |
| Schrödinger, Klein–Gordon | central | $1$ | $\rho_{\mathrm{num}}=r^{2}$ |
| spin, spinor | $\tilde\Xi$ | $\cosh\theta_{\mathrm{rpd}}$ | $\rho_{\mathrm{num}}=r^{2}$ and $n=r^{2}\cosh\theta_{\mathrm{rpd}}$ |
| Proca, spin one | $\tilde A_\Phi$ timelike | $\cosh2\theta_{\mathrm{rpd}}$ | $r=mc=\sqrt{-N(\tilde A_\Phi)}$ |

**The scalar rows have one number and the other two have two.** The vector row's ratio is the spinor's at doubled rapidity for a timelike potential boosted from rest by $\theta_{\mathrm{rpd}}$. There

$$
N(\tilde A_\Phi)=-m^{2}c^{2},\qquad r=mc=\sqrt{-N(\tilde A_\Phi)},\qquad \langle\tilde A_\Phi\rangle_{*}=m^{2}c^{2}\cosh2\theta_{\mathrm{rpd}},
$$

so the modulus is the mass and the density is the mass, $r^{2}=m^{2}c^{2}$, while the Euclidean size is the energy squared over $c^{2}$ at that rapidity. **The sign in $\sqrt{-N(\tilde A_\Phi)}$ is what makes $r$ real and positive on the timelike branch**, where the norm is negative [The Proca Fluid](the-proca-fluid.html); writing $\sqrt{-A^{2}}$ with the corpus's shorthand $A^{2}=A_\mu A^\mu$ invites a collision with the area and is not used here. **Each middle column is an exact identity for its carrier; the difference between the rows is the action of the boost on that carrier, and not a hierarchy of accuracy.**

### The Factor of Two, and the Two Carriers

**One boost, two angles, and the difference is how the carrier transforms.** A spinor transforms by left multiplication, $\xi\mapsto\tilde U\xi$, so a boost of rapidity $\theta_{\mathrm{rpd}}$ enters the element at half the rapidity. A four-vector transforms by congruence, $X\mapsto\tilde UX\tilde U^{*}$, so the same boost enters at the full rapidity. Hence

$$
\langle\tilde\Xi\rangle_{*}=r^{2}\cosh\theta_{\mathrm{rpd}}
\qquad\text{on a spinor,}
\qquad
\langle\tilde A_\Phi\rangle_{*}=\lvert N(\tilde A_\Phi)\rvert\cosh2\theta_{\mathrm{rpd}}
\qquad\text{on a four-vector,}
$$

both for an element boosted from rest by $\theta_{\mathrm{rpd}}$.

*Proof of the vector case.* Write $\tilde A_\Phi=mc\bigl(i\cosh\theta_{\mathrm{rpd}}e_t+\sinh\theta_{\mathrm{rpd}}\vec u\bigr)$, the corpus's four-vector shape with an imaginary time coefficient. Its coefficients are $imc\cosh\theta$ and $mc\sinh\theta\,u_k$, so

$$
N=(imc\cosh\theta)^{2}+(mc\sinh\theta)^{2}\sum_ku_k^{2}=-m^{2}c^{2}\bigl(\cosh^{2}-\sinh^{2}\bigr)=-m^{2}c^{2},
$$

using $\sum_ku_k^{2}=1$ and $(imc\cosh\theta)^{2}=-m^{2}c^{2}\cosh^{2}\theta$; and

$$
\langle\tilde A_\Phi\rangle_{*}=m^{2}c^{2}\bigl(\cosh^{2}+\sinh^{2}\bigr)=m^{2}c^{2}\cosh2\theta_{\mathrm{rpd}} .
$$

**So the ratio is $\cosh2\theta_{\mathrm{rpd}}$ and the modulus is mass-squared.** The factor of two is the carrier's: the same rapidity appears doubled because the four-vector carries the boost twice, once in each factor of the congruence. **This is the warning of [The Hamilton Pairing](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html), that its ratio is $\cosh\theta_{\mathrm{rpd},w}$ and not $\cosh\theta_{\mathrm{rpd}}$, explained by the half-angle and not by a convention.**

## Limits

**The identities are algebraic and need no dynamics.** All of them hold for one element at one event. Nothing here is an equation of motion, a conservation law, or a statement about a solution.

**The identification of $\langle\tilde\Xi\rangle_{*}$ with $j^{0}/c$ needs a rung.** It is exact at the spinor rung because the current there is $\rho_{\mathrm{num}}\tilde V_\Phi$; at the vector rung the current is the field strength's and the Euclidean size is not its time component. **The identity between the two numbers is a theorem; the reading of one of them as $j^{0}/c$ is rung-specific and is proved only where it is stated.**

**The speed bound is the reading's, not the algebra's.** $\tanh\theta\le1$ is a property of the hyperbola $(\langle\cdot\rangle_{*},2A)$. Causality follows once $\vec v/c$ is identified with a tangent of the parametrisation, which is the fluid reading's input. **The algebra cannot be used to argue for causality and this article does not.**

**The factor of two belongs to the carrier.** A spinor transforms by left multiplication and a four-vector by congruence, so one and the same boost sits at half-rapidity in the first and at full rapidity in the second. **No normalisation is fixed here that another article could fix differently**; a reader who compares the two without the carrier's action finds the factor of two and no explanation, which is the difficulty the Hamilton article records.

**The cone is codimension two and the divergence is genuine.** $\lvert N\rvert\to0$ with $\langle\cdot\rangle_{*}$ bounded is not a limit of small fields: it is a limit along a path of fixed field size on which the phase degenerates. **No perturbation of the amplitude reaches it**, and [The Domain of the Fluid Reading](the-domain-of-the-fluid-reading.html) makes the same point by perturbing along all eight coordinates.

**No statement about measurement.** The two numbers are properties of the element. Whether a given configuration of a physical field puts an event on the cone is a question about the field's values, and is not settled here.

## Summary

**The field has two numbers and the block uses one.** The modulus of the quaternionic norm is the proper density, $\rho_{\mathrm{num}}=r^{2}$; the Euclidean size is $\langle\tilde\Xi\rangle_{*}=r^{2}\cosh\theta_{\mathrm{rpd}}$; their ratio is the flow's Lorentz factor.

**The identity is Lagrange's in four dimensions.** $\langle\tilde Q\rangle_{*}^{2}=\lvert N(\tilde Q)\rvert^{2}+4A^{2}$ with $A$ the area of the parallelogram of real and imaginary parts. **No new algebra is claimed**; what is supplied is the relation between two names the corpus already uses and the inventory of what each name does at the cone.

**The two numbers are one four-vector's length and time component.** $\lvert N\rvert$ is invariant under a boost and $\langle\cdot\rangle_{*}$ transforms as $u^{0}$, verified at five angles to $1.3\times10^{-15}$; and at the spinor rung $\mathrm{Sc}(\tilde J_\Phi)=ic\langle\tilde\Xi\rangle_{*}$, exact to $4\times10^{-16}$, the $i$ being the corpus's imaginary time coefficient.

**The scalar rungs cannot show it.** A central element has collinear real and imaginary parts, $A=0$, the ratio is one, and no boost exists in one complex dimension. **The two scales appear exactly where the element stops being central.**

**On the cone the ratio has no value and the pair does.** $\rho_{\mathrm{num}}\to0$, $\cosh\theta_{\mathrm{rpd}}$ diverges, $\langle\tilde\Xi\rangle_{*}$ stays at full size, and the reason is that a zero divisor's real and imaginary parts are maximally non-parallel. **A limit taken on the ratio is meaningless; a limit taken on the pair is the boundary value the massless article computes.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, $\sum_\mu Q_\mu^{2}$, complex, multiplicative |
| $\langle\tilde Q\rangle_{*}$ | the Euclidean size, $\sum_\mu\lvert Q_\mu\rvert^{2}$, the Hermitian norm |
| $\mathrm{Sc}\,\tilde Q$ | the scalar part $Q_t$ |
| $r$ | the word's scale, with $r^{2}=\lvert N(\tilde\Xi)\rvert$ |
| $\theta_{\mathrm{pha}}$ | the central phase of the word |
| $\theta_{\mathrm{rpd}}$ | the boost's rapidity, with $\gamma=\cosh\theta_{\mathrm{rpd}}$ |
| $\phi$, $\vec u_{\phi}$ | the rapidity of an applied boost and its real unit axis |
| $\chi$ | the angle between that axis and the flow's axis $\vec u_{\mathrm b}$ |
| $\rho_{\mathrm{num}}=r^{2}$ | the proper density, the invariant length of the current over $c$ |
| $n=r^{2}\cosh\theta_{\mathrm{rpd}}$ | the coordinate density, $j^{0}/c$ |
| $a$, $b$ | the real and imaginary four-vectors of the coefficients |
| $A$, $A^{2}$ | the area of the parallelogram of $a$ and $b$, with $A^{2}=\sum_{j\lt k}(a_jb_k-a_kb_j)^{2}$ |
| $\tilde A_\Phi$ | the Proca potential, a different object from $A$ |
| $j^{0}$, $\vec j$ | the current's time component and flux, with $\tilde J_\Phi=ij^{0}e_t+\vec j$ |

## Appendix: The Algebra

### The Triangle Inequality

**Claim.** $\lvert N(\tilde Q)\rvert\le\langle\tilde Q\rangle_{*}$ for every $\tilde Q$, with equality if and only if $\tilde Q=\varkappa\tilde R$, $\varkappa$ a complex unit and $\tilde R$ real.

*Proof.* With $Q_\mu=r_\mu e^{i\varphi_\mu}$ and $r_\mu\ge0$, $N=\sum_\mu r_\mu^{2}e^{2i\varphi_\mu}$ and $\langle\cdot\rangle_{*}=\sum_\mu r_\mu^{2}$. The modulus of a sum is at most the sum of the moduli, each modulus being $r_\mu^{2}$. Equality holds exactly when the summands $r_\mu^{2}e^{2i\varphi_\mu}$ are non-negative real multiples of one another, so that $2\varphi_\mu\equiv2\varkappa_0$ modulo $2\pi$ for a single angle $\varkappa_0$ and every $\mu$ with $r_\mu\neq0$. That is $\varphi_\mu\equiv\varkappa_0/2$ modulo $\pi$, so $Q_\mu=\varkappa\,\epsilon_\mu r_\mu$ with $\varkappa=e^{i\varkappa_0/2}$ and $\epsilon_\mu=\pm1$, and the signs are carried by the real coefficients of $\tilde R$. Conversely a real element has all $Q_\mu$ real, its summands $Q_\mu^{2}\ge0$ real non-negative, and equality. **The case of a real element is the case of a trivial boost**, since $\theta_{\mathrm{rpd}}=0$ exactly when $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde u_{\mathrm r}$ has real coefficients up to the central phase.

### The Lagrange Identity

**Claim.** $\langle\tilde Q\rangle_{*}^{2}=\lvert N(\tilde Q)\rvert^{2}+4A^{2}$ with $Q_\mu=a_\mu+ib_\mu$ and

$$
A^{2}=\sum_{j\lt k}\bigl(a_jb_k-a_kb_j\bigr)^{2}=\lvert a\rvert^{2}\lvert b\rvert^{2}-(a\cdot b)^{2},
$$

the sum over the six pairs $1\le j\lt k\le 4$.

*Proof.* From $Q_\mu^{2}=a_\mu^{2}-b_\mu^{2}+2ia_\mu b_\mu$,

$$
N=\bigl(\lvert a\rvert^{2}-\lvert b\rvert^{2}\bigr)+2i\,(a\cdot b),
\qquad
\lvert N\rvert^{2}=\bigl(\lvert a\rvert^{2}-\lvert b\rvert^{2}\bigr)^{2}+4(a\cdot b)^{2},
$$

and $\langle\cdot\rangle_{*}^{2}=(\lvert a\rvert^{2}+\lvert b\rvert^{2})^{2}$. Subtracting,

$$
\langle\cdot\rangle_{*}^{2}-\lvert N\rvert^{2}=4\bigl(\lvert a\rvert^{2}\lvert b\rvert^{2}-(a\cdot b)^{2}\bigr).
$$

Lagrange's identity in $\mathbb{R}^{4}$ reads

$$
\lvert a\rvert^{2}\lvert b\rvert^{2}-(a\cdot b)^{2}=\sum_{j\lt k}\bigl(a_jb_k-a_kb_j\bigr)^{2},
$$

the sum over the six coordinate planes. Substituting gives the claim. **The bracket is non-negative, so $\langle\cdot\rangle_{*}\ge\lvert N\rvert$ follows a second time, independently of the triangle inequality.**

### The Polar Ratio

**Claim.** $\langle\tilde\Xi\rangle_{*}=r^{2}\cosh\theta_{\mathrm{rpd}}$ and $\lvert N(\tilde\Xi)\rvert=r^{2}$ for an $N$-regular element.

*Proof.* The Euclidean size is **not** multiplicative in general — $e_t+i\vec e_x$ and $e_t-i\vec e_x$ each have size $2$ and their product is $0$ — so the factors are handled one at a time. Multiplication by the central phase multiplies every coefficient by a unit complex number and leaves $\sum_\mu\lvert Q_\mu\rvert^{2}$ fixed. Right multiplication by the real unit $\tilde u_{\mathrm r}$ acts on the four complex coefficients by the same real orthogonal $4\times4$ matrix that it induces on $\mathbb{R}^{4}$, and an orthogonal real matrix preserves $\sum_\mu\lvert Q_\mu\rvert^{2}$; the same holds for left multiplication, since the real unit quaternions act orthogonally on both sides. **What remains is the boost factor alone**, whose two coefficients are $\cosh\frac{\theta_{\mathrm{rpd}}}{2}$ and $i\sinh\frac{\theta_{\mathrm{rpd}}}{2}u_k$, so

$$
\langle\tilde U_{\Psi,\mathrm b}\rangle_{*}=\cosh^{2}\frac{\theta_{\mathrm{rpd}}}{2}+\sinh^{2}\frac{\theta_{\mathrm{rpd}}}{2}\sum_ku_k^{2}=\cosh^{2}+\sinh^{2}=\cosh\theta_{\mathrm{rpd}} .
$$

For the modulus, $N$ **is** multiplicative, by the theorem of [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), and $N$ of a central phase is that phase squared, $N$ of a real unit is $1$, and $N(\tilde U_{\Psi,\mathrm b})=\cosh^{2}-\sinh^{2}=1$; hence $N(\tilde\Xi)=r^{2}e^{2i\theta_{\mathrm{pha}}}$. **The contrast is the article in one line: the modulus is multiplicative and the size is not, which is why the modulus is the invariant and the size is a frame-dependent quantity.** **The half-angle in the exponent becomes a full angle in the ratio**, which is the origin of every factor of two in this article.

### The Boost Composition

**Claim.** For $\tilde\Xi$ with rapidity $\theta_{\mathrm{rpd}}$ about the real unit axis $\vec u_{\mathrm b}$ and a boost of rapidity $\phi$ about the real unit axis $\vec u_{\phi}$, with $\cos\chi=\vec u_{\mathrm b}\cdot\vec u_{\phi}$,

$$
\langle\tilde U_{\mathrm b}(\phi,\vec u_{\phi})\tilde\Xi\rangle_{*}=r^{2}\bigl(\cosh\theta_{\mathrm{rpd}}\cosh\phi+\sinh\theta_{\mathrm{rpd}}\sinh\phi\cos\chi\bigr),
\qquad
\lvert N(\tilde U_{\mathrm b}(\phi,\vec u_{\phi})\tilde\Xi)\rvert=r^{2}.
$$

*Proof.* The modulus is multiplicative and $N(\tilde U_{\mathrm b})=\cosh^{2}\frac\phi2-\sinh^{2}\frac\phi2=1$. For the size, write $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}(c_h+is_h\vec u_{\mathrm b})$ and $\tilde U_{\mathrm b}=c_\phi+is_\phi\vec u_{\phi}$. The product is

$$
e^{i\theta_{\mathrm{pha}}}\Bigl[\bigl(c_hc_\phi-s_hs_\phi\,\vec u_{\mathrm b}\vec u_{\phi}\bigr)+i\bigl(c_hs_\phi\vec u_{\phi}+s_hc_\phi\vec u_{\mathrm b}\bigr)\Bigr].
$$

Since $\vec u_{\mathrm b}\vec u_{\phi}=-\cos\chi+\vec u_{\mathrm b}\times\vec u_{\phi}$, with the cross product orthogonal to both axes, the product splits into three pieces:

$$
\underbrace{\bigl(c_hc_\phi+s_hs_\phi\cos\chi\bigr)}_{\text{real scalar}}-s_hs_\phi\,\vec u_{\mathrm b}\times\vec u_{\phi}+i\underbrace{\bigl(c_hs_\phi\vec u_{\phi}+s_hc_\phi\vec u_{\mathrm b}\bigr)}_{\text{real vector}} .
$$

Each piece is a real scalar, a real vector, or $i$ times a real vector, and the three are mutually orthogonal in the eight real coordinates, so the Euclidean size is the sum of their squared lengths:

$$
\frac{\langle\tilde U_{\mathrm b}\tilde\Xi\rangle_{*}}{r^{2}}=(c_hc_\phi+s_hs_\phi\cos\chi)^{2}+s_h^{2}s_\phi^{2}\sin^{2}\chi+\bigl(c_h^{2}s_\phi^{2}+s_h^{2}c_\phi^{2}+2c_hs_hc_\phi s_\phi\cos\chi\bigr).
$$

Adding the $\cos^{2}\chi$ and $\sin^{2}\chi$ terms, the first and third pieces give $c_h^{2}(c_\phi^{2}+s_\phi^{2})+s_h^{2}(c_\phi^{2}+s_\phi^{2})=(c_h^{2}+s_h^{2})\cosh\phi$, and the two cross terms give $4c_hs_hc_\phi s_\phi\cos\chi$. With $c_h^{2}+s_h^{2}=\cosh\theta_{\mathrm{rpd}}$ and $2c_hs_h=\sinh\theta_{\mathrm{rpd}}$, $2c_\phi s_\phi=\sinh\phi$, the total is $\cosh\theta_{\mathrm{rpd}}\cosh\phi+\sinh\theta_{\mathrm{rpd}}\sinh\phi\cos\chi$. **That is the time component of $u^{\mu}=(\cosh\theta_{\mathrm{rpd}},\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b})$ under a boost of rapidity $\phi$ about $\vec u_{\phi}$**, multiplied by $r^{2}$.

### The Scalar Part of the Current

**Claim.** $\mathrm{Sc}(\tilde J_\Phi)=ic\,\gamma\rho_{\mathrm{num}}=ic\langle\tilde\Xi\rangle_{*}$.

*Proof.* $\tilde U_{\Psi,\mathrm b}^{-2}=\cosh\theta_{\mathrm{rpd}}-i\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$, so $ic\tilde U_{\Psi,\mathrm b}^{-2}=ic\cosh\theta_{\mathrm{rpd}}+c\sinh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$, whose scalar part is $ic\cosh\theta_{\mathrm{rpd}}$ and whose vector part is real. Multiplying by the central scalar $\rho_{\mathrm{num}}$ leaves the scalar part $ic\rho_{\mathrm{num}}\cosh\theta_{\mathrm{rpd}}$. By the polar ratio, $\rho_{\mathrm{num}}\cosh\theta_{\mathrm{rpd}}=\langle\tilde\Xi\rangle_{*}$. **The $i$ is the corpus's convention that the time coefficient of a four-vector is imaginary**, as at $\tilde P_\Phi=i\frac{E}{c}e_t+\vec p$; the real time component is therefore $j^{0}=\mathrm{Im}\,\mathrm{Sc}(\tilde J_\Phi)=c\langle\tilde\Xi\rangle_{*}$.

### The Numerical Checks

**All residuals are on the quantities named and were computed from the eight real coordinates, without using the word's parameters on both sides of the comparison.**

| check | statement | residual |
| --- | --- | --- |
| the Lagrange identity | $\langle\cdot\rangle_{*}^{2}-\lvert N\rvert^{2}-4A^{2}$ on $20000$ random elements | $5.7\times10^{-13}$ |
| the polar ratio | $\langle\cdot\rangle_{*}/\lvert N\rvert$ against $\cosh\theta_{\mathrm{rpd}}$, three elements | $\lt 5\times10^{-8}$ |
| the boost, collinear | $r^{2}\cosh(\theta+\phi)$, $\phi\in\{0,0.5493,1.2\}$ | $1.8\times10^{-15}$ |
| the boost, perpendicular | $r^{2}\cosh\theta\cosh\phi$, $\phi\in\{0.5493,1.2\}$ | $8.9\times10^{-16}$ |
| the boost, five angles | $\chi\in\{0,30,60,90,180\}^{\circ}$, $\phi=0.7$ | $1.3\times10^{-15}$ |
| the modulus under a boost | $\lvert N\rvert$ before and after | $2.2\times10^{-16}$ |
| the current | $\mathrm{Sc}(\tilde J_\Phi)/(ic)$ against $\langle\cdot\rangle_{*}$ | $4.4\times10^{-16}$ |

**The polar-ratio row's bound is looser than the others for a reason of method, not of accuracy.** Every other comparison holds two quantities of the same kind; that row compares a number computed from the eight real coordinates with a number computed from the word's parameters, so the discrepancy includes the error of the parameter extraction ($\theta_{\mathrm{rpd}}$ recovered from the coefficients, then $\cosh$ taken) as well as the arithmetic. **The identity itself is exact, and the exact statement is the appendix's; the row measures the transcription, and its bound is the extraction's.**

**These are checks, not proofs.** The proofs are the five claims above; the numbers confirm that the claims were transcribed correctly into the corpus's conventions, and nothing more.

## Further Reading

**The block this article clarifies.** [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html) fixes the word and the reading of $r$; [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) supplies the current and the non-closure of the bilinears; [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html) the correspondence the density serves; [The Domain of the Fluid Reading](the-domain-of-the-fluid-reading.html) and [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html) the two ends of the cone.

**The algebra.** [Norm and Pairing Conventions](norm-and-pairing-conventions.html) for the four norms and their names; [The Meaning of N-Regularity and Degeneracy](the-meaning-of-n-regularity-and-degeneracy.html) for the two cases and what each costs; [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html) for the ratio of the two invariants as a rapidity in the vector case; [The Material Sector](the-material-sector-four-vectors-interval-and-lorentz-action.html) for the imaginary time coefficient.

**Outside.** P. Langevin, "L'évolution de l'espace et du temps", *Scientia* **10** (1911), for proper and coordinate densities as one current's two readings. R. Penrose and W. Rindler, *Spinors and Space-Time*, vol. 1, Cambridge University Press (1984), for the spinor and vector carriers' different actions of one boost, which is the factor of two of §*The Factor of Two, and the Two Carriers*.
