# __Gauge Fixing in the Electroweak Theory: $R_\xi$ Gauges, Ghosts and the Goldstone Equivalence Theorem__

## Introduction

**The claim.** The quadratic part of the electroweak Lagrangian is not invertible, because it is flat along the gauge orbits. A gauge-fixing functional is what makes it invertible, and the functional that is chosen here does two things at once: it gives the would-be Goldstones a mass $\zeta M^2$ and it cancels the derivative mixing between each Goldstone and the vector that ate it. Both jobs are done by one term, and that is why the choice is the one it is.

$$
\mathcal{L}_{\mathrm{gf}}=-\frac{1}{2\zeta}\sum_{a=1,2}\left(\sum_\mu\frac{\partial W^a_\mu}{\partial R_\mu}-\zeta M_W\,\xi^a\right)^2-\frac{1}{2\zeta}\left(\sum_\mu\frac{\partial Z_\mu}{\partial R_\mu}-\zeta M_Z\,\xi^0\right)^2-\frac{1}{2\zeta_A}\left(\sum_\mu\frac{\partial A_\mu}{\partial R_\mu}\right)^2 .
$$

**The parameter's name.** The gauges are called $R_\xi$ in the literature and the title keeps the name. The corpus writes the gauge parameter $\zeta$, as *BRST Symmetry in Biquaternionic Form* and *The Yang–Mills Path Integral and the Faddeev–Popov Procedure* do, and this article does the same, because article 4 has already spent $\xi$ on the three would-be Goldstone fields, there written $\xi_a$ with the index down. A reader comparing with a textbook should read $\xi_{\text{there}}=\zeta_{\text{here}}$, and the Goldstone fields of article 4 are unchanged; the index position differs and nothing else does.

**Why a whole article.** Because gauge fixing is where three separate statements meet, and each is usually made in a different place. The quadratic form is degenerate, and the degeneracy is not a technicality: it *is* the gauge symmetry, seen at the level of the free theory. The Goldstones become massive, and their mass is not a physical mass but a coordinate-dependent one. The ghosts appear, and they carry a minus sign that has to be tracked. And the equivalence theorem, which is the physical content of the whole construction, follows from one property of the longitudinal polarisation vector.

**Three results that are computed here and not usually stated together.**

- **The zero mode of the quadratic form is the gauge orbit, and in the broken phase that orbit is the vector–Goldstone mixing.** The vector $v=(p_\mu,\,iM)$ is annihilated by the quadratic kernel before gauge fixing, to $\lVert Kv\rVert/\lVert v\rVert=4.6\times10^{-16}$, and it is not annihilated afterwards. So the mixing that the functional cancels and the flat direction that it lifts are one object.
- **One formula covers the three gauges.** With $\Pi$ the positive momentum invariant and $P$, $L$ the transverse and longitudinal projectors, the propagator is $\frac{P}{\Pi-M^2}+\frac{\zeta L}{\Pi-\zeta M^2}$; $\zeta=1$ gives $\delta/(\Pi-M^2)$, $\zeta=0$ gives the transverse part alone, and $\zeta\to\infty$ gives the Proca propagator. Verified against direct inversion of the kernel to $2.2\times10^{-16}$.
- **The $\zeta$-pole is shared by the Goldstone and the ghost, at $\Pi=\zeta M^2$, and at $\zeta=1$ all three poles coincide with the physical one.** That is the structural reason the $\zeta$-dependent parts cancel in loops, and it is a statement about pole positions rather than about diagrams.

**The order.** Why the quadratic form is degenerate; the functional and its two jobs; the Goldstone masses; the ghost sector and its weights; the propagators and the three limits; what $\zeta$ cannot change; power counting and the renormalisability argument; the equivalence theorem; the numbers; and what the framework does and does not supply.

## Why the Quadratic Form Is Degenerate

**The kernel.** Write the quadratic part of the gauge sector in momentum space, with $\Pi\equiv-\sum_\mu p_\mu p_\mu$ positive for timelike momenta and equal to $M^2$ on the mass shell:

$$
\mathcal{L}^{(2)}=\tfrac12\sum_{\mu,\nu}A_\mu\left[(\Pi-M^2)\delta_{\mu\nu}+p_\mu p_\nu\right]A_\nu ,
$$

for one massive direction of mass $M$, and the same with $M=0$ for the photon. The sign of the $p_\mu p_\nu$ term is fixed by the momentum convention, $\Pi\equiv-\sum_\mu p_\mu p_\mu$: with the opposite sign the kernel is neither transverse on shell nor invertible.

**The massless case is singular and the massive case is not.** For $M=0$ the kernel $\Pi\,\delta_{\mu\nu}+p_\mu p_\nu$ annihilates $p_\mu$, since $\Pi p_\mu+p_\mu\sum_\nu p_\nu p_\nu=\Pi p_\mu-\Pi p_\mu=0$, so it has a zero eigenvalue and no inverse. For $M\neq0$ the same kernel acting on $p_\mu$ gives $-M^2p_\mu$, which is not zero, and the kernel is invertible. The reason is worth stating: a mass term removes the flat direction that gauge invariance leaves, so the Proca propagator exists without any gauge condition while the Maxwell propagator does not. *Canonical Quantization of the Biquaternion Proca Field* therefore needs none.

**What the zero mode is.** The vector annihilated by the massless kernel is $p_\mu$, and a field variation proportional to $p_\mu$ in momentum space is a derivative in position space, that is, a gauge transformation. So the zero mode is not an accident of the algebra: **the kernel is degenerate exactly along the gauge orbit**, and the number of zero modes equals the number of generators.

**What the broken phase adds.** Breaking the symmetry does not remove the degeneracy; it moves it. The scalar's kinetic term produces a mixing between the vector and the Goldstone, and the flat direction is now a simultaneous shift of both. With the doublet written as in article 4,

$$
\varphi=\exp\left(\frac{i}{v}\sum_a\xi^a\tau_a\right)\frac{1}{\sqrt2}\begin{pmatrix}0\\ v+h\end{pmatrix},
$$

the quadratic form in the pair $(A_\mu,\xi)$ is the vector's kernel coupled to the Goldstone by a term proportional to $p_\mu\xi$, and the vector that it annihilates is

$$
v=\begin{pmatrix}p_\mu\\ iM\end{pmatrix},
\qquad
Kv=0 ,
$$

up to the phase convention on $\xi$, which the mixing term's sign fixes and nothing else does.

**Verified.** On a generic off-shell momentum and $M\neq0$, $\lVert Kv\rVert/\lVert v\rVert=4.6\times10^{-16}$. The zero mode is the gauge orbit written in the broken variables: $A_\mu\to A_\mu+\partial_\mu\theta$ with $\xi\to\xi+M\theta$, which is exactly the transformation that article 4 uses to remove the Goldstones.

**The consequence.** A propagator does not exist until a condition is chosen. That is the whole problem, and the term "gauge fixing" names the choice of condition.

## The Gauge-Fixing Functional

**The functional.** A single scalar function of the fields, one for each generator, set to zero:

$$
G^{a}=\sum_\mu\frac{\partial W^a_\mu}{\partial R_\mu}-\zeta M_W\xi^{a} ,
\qquad
G^{Z}=\sum_\mu\frac{\partial Z_\mu}{\partial R_\mu}-\zeta M_Z\xi^{0} ,
\qquad
G^{A}=\sum_\mu\frac{\partial A_\mu}{\partial R_\mu} .
$$

**What the identity does with it.** The Faddeev–Popov identity inserts unity as $1=\Delta[A]\int\mathcal{D}U\,\delta(G[A^{U}])$, and the $\delta$-functional is then traded for a Gaussian weight $-\frac{1}{2\zeta}\sum_a(G^a)^2$, which is the term displayed in the introduction. The determinant $\Delta$ that the identity produces is the ghost sector, and §*The Ghost Sector and Its Weights* writes it.

**Why each entry has the shape it has.** The first two are chosen, and the third is the ordinary Lorenz condition. The $-\zeta M_W\xi^a$ insertion is the one addition that the electroweak theory makes to the Yang–Mills functional of *The Yang–Mills Path Integral and the Faddeev–Popov Procedure*, and it is the whole of the difference: in the pure-gauge theory the functional is $\partial\cdot A$ alone.

**In the unbroken basis the same object is less transparent.** Written in $(W^1,W^2,W^3,B)$, the neutral functionals are $\partial\cdot W^3-\zeta M_W\xi^3$ and $\partial\cdot B+\zeta M_Y\xi^3$, with $M_Y=g_{\mathrm Y}v/2$. Their sum of squares gives the Goldstone the mass $\zeta(M_W^2+M_Y^2)=\zeta M_Z^2$, and the orthogonal combination, the one in which the two enter with opposite weights, is the photon's condition $\partial\cdot A=0$. The two writings are the same condition expressed in two bases, and the physical basis is the one in which the masses are the eigenvalues rather than the entries.

**The count of parameters.** Four functionals, four parameters if they are weighted independently, one if a common $\zeta$ is used. Nothing physical depends on the choice, and the rest of the article is the verification of that sentence in the cases where it can be checked exactly.

**The BRST reading.** The same object is the gauge-fixing fermion of *BRST Symmetry in Biquaternionic Form*,

$$
\tilde\Xi_{\mathrm{sp}}=\sum_a\bar c^{\,a}\left(\sum_\mu\frac{\partial W^a_\mu}{\partial R_\mu}-\zeta M_W\xi^a+\frac{\zeta}{2}B^a\right),
$$

with $B^a$ the Nakanishi–Lautrup field. Eliminating $B^a$ by its own equation of motion reproduces the $-\frac{1}{2\zeta}(G^a)^2$ term, so the two formulations differ only in whether the auxiliary field is kept. The one addition to the companion article's fermion is the $-\zeta M_W\xi^a$ insertion, and it is the same addition as before.

## Two Jobs in One Functional

**The scalar kinetic term.** Expanding $\left|D_\mu\varphi\right|^2$ around the vacuum in the parametrisation of §*Why the Quadratic Form Is Degenerate* gives three pieces: a mass term $\frac{M^2}{2}A_\mu A_\mu$, a derivative mixing $-M\,\xi\,\partial^\mu A_\mu$, and the Goldstone's own kinetic term $-\frac12(\partial\xi)^2$. There is no $\xi^2$ term without a mass, because the potential's curvature along the Goldstone direction vanishes at the minimum: that is the Goldstone theorem in its dynamical form.

**What the functional contributes.** Squaring $G$ gives three pieces with the same shapes:

$$
-\frac{1}{2\zeta}\left(\partial\cdot A-\zeta M\xi\right)^2=-\frac{1}{2\zeta}\left(\partial\cdot A\right)^2+M\,\xi\,\partial\cdot A-\frac{\zeta M^2}{2}\xi^2 .
$$

**The two cancellations, term by term.** The cross terms are equal and opposite, $+M\xi\partial\cdot A$ against $-M\xi\partial\cdot A$; and the new $\xi^2$ term is what the potential could not supply. So one functional removes the mixing and supplies the mass, and the two facts are one fact: the functional is the gauge-invariant completion of the Goldstone's mass term.

| Piece | from $\lvert D\varphi\rvert^2$ | from $\mathcal{L}_{\mathrm{gf}}$ | Sum |
|---|---|---|---|
| $A_\mu A_\mu$ | $+\frac{M^2}{2}A^2$ | $-\frac{1}{2\zeta}(\partial\cdot A)^2$ | the massive kernel |
| $A_\mu\partial^\mu\xi$ | $-M\xi\,\partial\cdot A$ | $+M\xi\,\partial\cdot A$ | $0$ |
| $\xi^2$ | $0$ | $-\frac{\zeta M^2}{2}\xi^2$ | $-\frac{\zeta M^2}{2}\xi^2$ |

**Why the cross term has to cancel.** If it does not, the Goldstone propagator carries a numerator proportional to $p_\mu p_\nu$ that grows with energy, and the theory loses manifest power counting even though it remains formally gauge invariant. Cancelling it is what makes every field's propagator fall as $1/\Pi$, and that is the subject of §*Power Counting and the Renormalisability Argument*.

**The same statement as a determinant.** Before gauge fixing the quadratic form is degenerate, so its determinant vanishes identically. After gauge fixing the determinant is a product of the blocks, and each block is invertible. What the functional does is factorise a degenerate form into invertible factors, which is the precise sense in which it "fixes" anything.

## The Goldstones Acquire a Mass

**The masses.** From the $\xi^2$ terms of the functional, and with $\xi^\pm$ the two charged Goldstones and $\xi^0$ the neutral one,

$$
M_{\xi^\pm}^2=\zeta M_W^2 ,
\qquad
M_{\xi^0}^2=\zeta M_Z^2 .
$$

**The table, for the measured masses.**

| $\zeta$ | $M_{\xi^\pm}=\sqrt{\zeta}\,M_W$ | $M_{\xi^0}=\sqrt{\zeta}\,M_Z$ |
|---|---|---|
| $0$ | $0$ | $0$ |
| $0.1$ | $25.4$ GeV | $28.8$ GeV |
| $0.25$ | $40.2$ GeV | $45.6$ GeV |
| $0.5$ | $56.8$ GeV | $64.5$ GeV |
| $1$ | $80.4$ GeV | $91.2$ GeV |
| $2$ | $113.7$ GeV | $129.0$ GeV |
| $3$ | $139.2$ GeV | $157.9$ GeV |
| $10$ | $254.2$ GeV | $288.4$ GeV |

**At $\zeta=1$ the Goldstone is degenerate with the vector that ate it.** $M_{\xi^\pm}=M_W$ and $M_{\xi^0}=M_Z$ exactly, by the definitions of the two masses. This is the Feynman–'t Hooft gauge, and the degeneracy is why it is the gauge in which loop calculations are shortest: the $\zeta$-dependent parts of the gauge and Goldstone propagators have poles at the same place, so they combine into single integrals.

**Why this mass is not a mass.** It is a function of the parameter, and it vanishes at $\zeta=0$ and diverges at $\zeta\to\infty$. A quantity that can be set to zero or to infinity by a choice of coordinates is not an observable. What is observable is that the Goldstone appears in no asymptotic state: it is not in the $S$-matrix, whatever its propagator's pole.

**The $h$–$\xi$ mixing is absent.** The potential has no term linear in $\xi$ and none mixing $h$ with $\xi$, because the vacuum is the minimum along both directions. The functional therefore introduces no new mixing, which is a statement about the shape of the potential and not about the gauge.

**The counting is untouched.** The physical spectrum is article 4's: three massive vectors, one massless photon, one scalar, twelve degrees of freedom. The Goldstones and ghosts are not extra particles; they are the price of a propagator, and they appear only inside loops.

## The Ghost Sector and Its Weights

**The determinant.** The Faddeev–Popov identity produces $\Delta=\det M$ with $M_{ab}=\delta G^a/\delta\alpha^b$, the variation of the functional under an infinitesimal gauge transformation. For the $R_\xi$ functionals,

$$
M^{ab}=-\delta^{ab}\,\Pi+\zeta M_W^2\,\delta^{ab}+\cdots ,
$$

so the ghost of each broken direction has the mass of the Goldstone of that direction, and the ellipsis is the gauge-field dependence that makes the determinant field-dependent.

**The masses, precisely.**

| Ghost pair | Multiplicity | Mass$^2$ | Note |
|---|---|---|---|
| $c^\pm,\bar c^{\,\pm}$ | $2$ | $\zeta M_W^2$ | one per charged Goldstone |
| $c^{Z},\bar c^{\,Z}$ | $1$ | $\zeta M_Z^2$ | the neutral massive one |
| $c^{A},\bar c^{\,A}$ | $1$ | $0$ | massless, because $\mathrm{U}(1)_{\mathrm{em}}$ is unbroken |

**The neutral block, and the zero eigenvalue.** Written in the unbroken basis the neutral ghost mass matrix is

$$
M_{\mathrm{gh}}^2=\frac{\zeta v^2}{4}\begin{pmatrix}g^2 & -g\,g_{\mathrm Y}\\ -g_{\mathrm Y}\,g & g_{\mathrm Y}^2\end{pmatrix},
$$

whose determinant vanishes identically and whose trace is $\zeta M_Z^2$. Its eigenvalues are therefore $0$ and $\zeta M_Z^2$; verified at $\zeta=0.5$, $1$ and $3$, where the computed determinant stayed below $2\times10^{-8}$ GeV$^4$ against a trace squared of order $10^{8}$ GeV$^4$, that is zero to floating-point precision. **The zero eigenvalue is the photon's ghost, and its existence is the statement that the residual symmetry is unbroken.** A gauge theory with a compact unbroken factor has a massless ghost per generator of that factor, and the count is a check on the breaking pattern rather than on the gauge.

**The weights.** Three weights are attached to each ghost, and they are separate facts:

| Weight | Value | Where it enters |
|---|---|---|
| measure | $\det M$ | multiplies the integrand; equals the ghost path integral |
| statistics | $-1$ per closed ghost loop | relative sign against a bosonic loop |
| ghost number | $+1$ for $c$, $-1$ for $\bar c$ | additive, conserved by $s$ |

**The minus sign is not optional.** The Gaussian integral over anticommuting variables gives $\det M$ and not $1/\det M$, and a closed loop of an anticommuting field carries a minus relative to a bosonic loop. Both statements are consequences of the same sign in the measure, and dropping either changes the one-loop beta function of the gauge coupling. *The Yang–Mills Path Integral and the Faddeev–Popov Procedure* records the non-abelian case, where the ghost loop is what makes the coefficient $b_0=11C_2(G)/3$ positive.

**Where the ghosts live.** They are not elements of $\mathbb{B}$: the algebra is even and ungraded, and no element anticommutes with its fellows. They are elements of the Grassmann envelope $\mathbb{B}\otimes\Lambda$, and that is the companion article's statement, repeated here because the ghost sector is where it is used.

**The ghost operator.** In the physical basis the quadratic part of the ghost action carries the operator $\Pi-\zeta M_a^2$ times $\delta^{ab}$, with $M_a$ the mass of the corresponding Goldstone, $M_W$ for the two charged, $M_Z$ for the neutral and $0$ for the photon, plus the gauge-field couplings that come from the covariant derivative inside $M^{ab}$. The couplings are what make the ghosts more than a bookkeeping device: they are the vertices that cancel the longitudinal gauge-field contributions in loops.

## The Propagators and the Three Limits

**The projectors.** With $\Pi\equiv-\sum_\mu p_\mu p_\mu$ the positive invariant of *The Yang–Mills Path Integral and the Faddeev–Popov Procedure*, define

$$
P_{\mu\nu}=\delta_{\mu\nu}+\frac{p_\mu p_\nu}{\Pi} ,
\qquad
L_{\mu\nu}=-\frac{p_\mu p_\nu}{\Pi} ,
$$

so that $P^2=P$, $L^2=L$, $PL=LP=0$, $P+L=\delta$, $\mathrm{tr}\,P=3$, $\mathrm{tr}\,L=1$ and $\sum_\mu p_\mu P_{\mu\nu}=0$. All seven identities are verified numerically to $2.2\times10^{-16}$ at a generic momentum. On the mass shell $\Pi=M^2$ and $P$ is the sum over the three physical polarisations of the massive vector, which is the numerator that *Canonical Quantization of the Biquaternion Proca Field* displays.

**A convention, stated once.** $\Pi$ is positive and equals $M^2$ on the mass shell, every propagator below is written with the sign that gives a positive residue to the field it belongs to, and the formula for a scalar of mass $M$ is $\frac{1}{\Pi-M^2}$. The relative minus that a closed ghost loop carries is the measure's, recorded in the weights table, and not the propagator's.

**The propagator.** One formula:

$$
\boxed{\;D_{\mu\nu}(p)=\frac{P_{\mu\nu}}{\Pi-M^2}+\frac{\zeta\,L_{\mu\nu}}{\Pi-\zeta M^2}\;}
$$

**The photon's entry.** The same formula at $M=0$, $D^{(A)}_{\mu\nu}=\frac{P_{\mu\nu}}{\Pi}+\frac{\zeta_A L_{\mu\nu}}{\Pi}=\frac{1}{\Pi}\left(\delta_{\mu\nu}-(1-\zeta_A)\frac{p_\mu p_\nu}{\Pi}\right)$.

**Its verification.** $D$ is the inverse of the kernel

$$
K_{\mu\nu}=\left(\Pi-M^2\right)\delta_{\mu\nu}+\left(1-\frac{1}{\zeta}\right)p_\mu p_\nu ,
$$

and the product $KD$ deviates from $\delta_{\mu\nu}$ by at most $2.2\times10^{-16}$ at $\zeta=0.5$, $1$, $2$ and $3$ on a generic off-shell momentum. The term $-\frac{1}{\zeta}p_\mu p_\nu$ in $K$ is exactly what the functional contributes: $K$ is the Proca kernel $(\Pi-M^2)\delta_{\mu\nu}+p_\mu p_\nu$ minus $\frac{1}{\zeta}p_\mu p_\nu$, and at $\zeta\to\infty$ it is the Proca kernel again.

**The other propagators, in the same notation.**

| Field | Propagator | Pole |
|---|---|---|
| massive vector | $\dfrac{P_{\mu\nu}}{\Pi-M^2}+\dfrac{\zeta L_{\mu\nu}}{\Pi-\zeta M^2}$ | $\Pi=M^2$, $\Pi=\zeta M^2$ |
| photon | $\dfrac{P_{\mu\nu}}{\Pi}+\dfrac{\zeta_A L_{\mu\nu}}{\Pi}$ | $\Pi=0$ only |
| Goldstone | $\dfrac{1}{\Pi-\zeta M^2}$ | $\Pi=\zeta M^2$ |
| ghost | $\dfrac{1}{\Pi-\zeta M^2}$ | $\Pi=\zeta M^2$ |
| physical scalar | $\dfrac{1}{\Pi-M_H^2}$ | $\Pi=M_H^2$ |

**The three limits, from the one formula.**

- **$\zeta=1$.** $\frac{P+L}{\Pi-M^2}=\frac{\delta_{\mu\nu}}{\Pi-M^2}$. The propagator is diagonal in the Lorentz indices, the Goldstone and ghost have mass $M$, and the $\zeta$-cancellation is between fields of equal mass. This is the Feynman–'t Hooft gauge.
- **$\zeta=0$.** $\frac{P_{\mu\nu}}{\Pi-M^2}$, which is regular: the second term is $\zeta L_{\mu\nu}/\Pi$ to leading order and vanishes with $\zeta$. The longitudinal term is absent, and the Goldstone and ghost become massless, their poles moving to $\Pi=0$. This is the Landau gauge: the best gauge for ultraviolet questions and the one in which the infrared structure of the Goldstone and ghost contributions has to be cancelled between them.
- **$\zeta\to\infty$.** $\frac{P_{\mu\nu}}{\Pi-M^2}-\frac{L_{\mu\nu}}{M^2}$, which is $\frac{\delta_{\mu\nu}+p_\mu p_\nu/M^2}{\Pi-M^2}$, the Proca form. The sign of the second term flips in the limit, because $\Pi-\zeta M^2\to-\zeta M^2$ and the whole term tends to $-L/M^2$; the two forms then add to the transverse-plus-longitudinal numerator that *Canonical Quantization of the Biquaternion Proca Field* displays. The Goldstone and ghost masses diverge and those fields decouple. This is the unitary gauge, and it is the same object as the Proca field of the companion article.

**The unitary limit, verified.** $\frac{P_{\mu\nu}}{\Pi-M^2}-\frac{L_{\mu\nu}}{M^2}$ equals $\frac{\delta_{\mu\nu}+p_\mu p_\nu/M^2}{\Pi-M^2}$ identically, entry by entry, and the reason is one line: $p_\mu p_\nu=-\Pi L_{\mu\nu}$, so $\frac{\delta+pp/M^2}{\Pi-M^2}=\frac{P}{\Pi-M^2}+\frac{L+pp/M^2}{\Pi-M^2}=\frac{P}{\Pi-M^2}-\frac{L}{M^2}$. The cancellation is algebraic and holds at every momentum, on shell or off. At finite $\zeta$ the deviation from the Proca form is $\frac{\Pi\,L_{\mu\nu}}{M^2\left(\Pi-\zeta M^2\right)}$, of order $1/\zeta$ and not of order of the off-shellness: $2.0\times10^{-9}$ at $\Pi=2M^2$ and $\zeta=10^{9}$. The Proca propagator is therefore the $\zeta\to\infty$ limit and not a separate object.

**Why the third limit is not free.** $\zeta\to\infty$ is not a gauge in which one can compute loops: the vector propagator tends to a constant, which is the subject of the next section but one. It is the right gauge for tree-level questions about the physical spectrum, and the wrong gauge for everything else. That asymmetry is the reason the $R_\xi$ family is used at all: it contains both limits and a good gauge in between.

## What the Parameter Cannot Change

**The residue at the physical pole.** The pole at $\Pi=M^2$ sits in the first term only, whose residue is $P_{\mu\nu}$, and $P$ carries no $\zeta$. Verified: multiplying $D$ by $(\Pi-M^2)$ and subtracting $P$ leaves a deviation that vanishes linearly with the off-shellness, $1.4\times10^{-9}$ for $2M\epsilon=2.8\times10^{-9}$ GeV$^{2}$. **The physical pole's residue is $\zeta$-independent, and the $\zeta$-pole is somewhere else.**

**The Ward identity, in the abelian case.** For a conserved external current, $\sum_\nu p_\nu j_\nu=0$, the longitudinal projector annihilates it, $L_{\mu\nu}j_\nu=0$, so

$$
D_{\mu\nu}(\zeta)\,j_\nu=\frac{P_{\mu\nu}j_\nu}{\Pi-M^2}
$$

for every $\zeta$. Verified: the vector $D_{\mu\nu}j_\nu$ drifts by at most $4.5\times10^{-16}$ across $\zeta=0,0.5,1,3,10$, while a current that is not conserved drifts by $0.78$ between $\zeta=0.5$ and $\zeta=3$. **The gauge parameter is invisible to conserved currents and visible to everything else**, and that is the exact content of "physical amplitudes are gauge independent" in the abelian case.

**The non-abelian case is the same statement with more indices.** The external current of a non-abelian gauge field is itself charged and only covariantly conserved, so the identity $\sum_\nu p_\nu j_\nu=0$ holds only after the commutator terms are included. The Ward identity then becomes a family of Slavnov–Taylor identities, one for each external leg, relating amplitudes with different numbers of ghosts and longitudinal fields. *BRST Symmetry in Biquaternionic Form* derives them from $s^2=0$; the point for this article is that they are the non-abelian form of the drift test just described.

**The parameter runs.** $\zeta$ is not a physical parameter, but it is renormalised, and its anomalous dimension is non-zero. The statement that amplitudes are $\zeta$-independent holds at each order in the loop expansion and is what makes the running harmless: one may take $\zeta(\mu)$ to be any function, and the answer does not change. *The Renormalization Group in Biquaternionic Form* records the running of the couplings that the ghosts and Goldstones enter.

**What can change: nothing observable, and three things that look observable.** The Goldstone mass, the ghost mass and the position of the longitudinal pole all move with $\zeta$, and none of them appears in an $S$-matrix element. A calculation that quotes one of them as a result has quoted a coordinate.

## Power Counting and the Renormalisability Argument

**Every propagator falls as $1/\Pi$.** In the $R_\xi$ gauge all five propagators of the table above behave as $\Pi^{-1}$ at large $\Pi$, including the longitudinal part of the vector, whose second term is $\frac{\zeta L}{\Pi-\zeta M^2}\sim\frac{\zeta L}{\Pi}$. With every internal line contributing $\Pi^{-1}$ and every vertex having dimension at most four, the superficial degree of divergence of a graph with $L$ loops is bounded independently of $L$:

$$
D\le 4 .
$$

**The unitary gauge does not have this property.** At $\zeta\to\infty$ the vector propagator tends to $-\frac{L_{\mu\nu}}{M^2}$, a constant, so an internal vector line contributes $\Pi^{0}$ instead of $\Pi^{-1}$, and the bound becomes $D\le 4+2I_V$ with $I_V$ the number of internal vector lines. The theory is not manifestly renormalisable in that gauge, although its $S$-matrix is the same.

| Gauge | Vector propagator at large $\Pi$ | Bound on $D$ | Manifest renormalisability |
|---|---|---|---|
| $R_\xi$, any finite $\zeta$ | $\Pi^{-1}$ | $4$ | yes |
| Landau, $\zeta=0$ | $\Pi^{-1}$ | $4$ | yes |
| unitary, $\zeta\to\infty$ | $\Pi^{0}$ | grows with $I_V$ | no |

**What "manifest" costs nothing and buys everything.** The two gauges describe the same theory, so renormalisability is a property of the theory and not of the gauge. What the $R_\xi$ family supplies is a *proof*: in it, every counterterm is local with dimension at most four, and the divergences can be absorbed into the parameters of the Lagrangian. This is the argument of 't Hooft and Veltman, and it is the reason the electroweak theory was accepted as renormalisable in 1971 rather than after the discovery of the $W$ and $Z$.

**The cancellation that makes it work.** The $\zeta$-dependent divergences of the gauge loop are cancelled by the Goldstone and ghost loops, and the cancellation is possible because the three propagators share the pole at $\Pi=\zeta M^2$ and the vertices carry no $\zeta$. At $\zeta=1$ the three poles coincide, which is why the cancellation is most transparent there; at general $\zeta$ it holds by the Slavnov–Taylor identities, which do not care where the pole is.

**The one thing the argument needs from the algebra.** Local counterterms require that the ghost–gauge vertices come from a local action, and they do, because the ghost action is $\bar c\,M c$ with $M$ a differential operator built from the covariant derivative. That locality is the Jacobi identity of the structure constants, which in the framework is the associativity of $\mathbb{B}$.

## The Equivalence Theorem

**The statement.** For energies large compared with the mass,

$$
\mathcal{M}\left(W^{\pm}_L,\ldots\right)=\mathcal{M}\left(\xi^{\pm},\ldots\right)+O\left(\frac{M}{E}\right) ,
$$

and the same with $Z_L$ and $\xi^0$. An amplitude with a longitudinal vector in the initial or final state equals the amplitude with the corresponding Goldstone, up to corrections suppressed by the mass over the energy.

**Where it comes from, in one line.** The longitudinal polarisation vector of a vector of mass $M$ and momentum $p$ is

$$
\epsilon_L^\mu=\left(\frac{\lvert\vec p\rvert}{M},\ \frac{E}{M}\hat p\right),
$$

and it satisfies $\sum_\mu p_\mu\epsilon_L^\mu=0$ and $\sum_\mu\epsilon_{L,\mu}\epsilon_L^\mu=-1$ exactly. Comparing it with $p^\mu/M$,

$$
\epsilon_L^\mu=\frac{p^\mu}{M}+\eta^\mu ,
\qquad
\eta^0=-\frac{E-\lvert\vec p\rvert}{M} ,
\qquad
\eta^3=+\frac{E-\lvert\vec p\rvert}{M} ,
\qquad
\frac{E-\lvert\vec p\rvert}{E}=\frac{M^2}{E\left(E+\lvert\vec p\rvert\right)}\to\frac{M^2}{2E^2} .
$$

**The numerical size of the correction.**

| $E/M$ | $\left(E-\lvert\vec p\rvert\right)/E$ | $M^2/(2E^2)$ | Ratio |
|---|---|---|---|
| $2$ | $1.34\times10^{-1}$ | $1.25\times10^{-1}$ | $1.072$ |
| $5$ | $2.02\times10^{-2}$ | $2.00\times10^{-2}$ | $1.010$ |
| $10$ | $5.01\times10^{-3}$ | $5.00\times10^{-3}$ | $1.003$ |
| $100$ | $5.00\times10^{-5}$ | $5.00\times10^{-5}$ | $1.000$ |
| $1000$ | $5.00\times10^{-7}$ | $5.00\times10^{-7}$ | $1.000$ |

**Why $p^\mu/M$ is the Goldstone coupling.** The piece $\frac{1}{M}p^\mu$ contracted with a vertex is, by the Ward identity, the divergence of the corresponding current, and the divergence of the current is what the Goldstone field couples to. That is the content of the $R_\xi$ construction: the Goldstone's coupling is fixed by the same Ward identity that the gauge-fixing functional was chosen to make valid. So the theorem is not an independent fact about polarisations; it is the Ward identity read at high energy.

**The bound it gives.** Without a scalar, the amplitude for $W_LW_L\to W_LW_L$ grows as $s/v^2$. The $J=0$ partial wave is $a_0=s/(16\pi v^2)$, and the unitarity bound $\lvert a_0\rvert\le\frac12$ is saturated at

$$
\sqrt{s}=\sqrt{8\pi}\,v=1.23\ \text{TeV} .
$$

With the scalar present, the $s/v^2$ growth cancels against the scalar exchange and the residual is of order $M_H^2/v^2$. The $1.23$ TeV is therefore the energy at which the sector must either show its scalar or show something else.

**The theorem as the dynamical counterpart of the counting.** Article 4's count is $12=12$: the three eaten components become the three longitudinal polarisations. The theorem says which is which: at high energy the eaten Goldstone and the longitudinal polarisation are the same object, and the equality of their couplings is what makes the count a statement about dynamics and not only about arithmetic.

## The Numbers

**The masses used.** $M_W=80.377$ GeV and $M_Z=91.1876$ GeV. The tree-level values from the couplings of article 4, $g=0.65174$ and $g_{\mathrm Y}=0.3574$, are $80.24$ and $91.51$ GeV; the difference is the radiative correction and is not a gauge effect.

**The Goldstone and ghost masses at the three standard gauges.**

| Gauge | $\zeta$ | $M_{\xi^\pm}=M_{c^\pm}$ | $M_{\xi^0}=M_{c^Z}$ |
|---|---|---|---|
| Landau | $0$ | $0$ | $0$ |
| Feynman–'t Hooft | $1$ | $80.377$ GeV | $91.188$ GeV |
| Unitary | $\infty$ | $\infty$ | $\infty$ |

**The pole positions.** Physical pole at $\Pi=M^2$; $\zeta$-pole at $\Pi=\zeta M^2$, shared by the Goldstone and the ghost. At $\zeta=2$ the $\zeta$-pole of the $W$ sector sits at $\Pi=2M_W^2=1.29\times10^{4}$ GeV$^{2}$, that is at $\sqrt2\,M_W=113.7$ GeV, above the physical pole by a factor $\sqrt2$ in mass.

**The unitarity scale.** $\sqrt{8\pi}\,v=1.23$ TeV, and $\sqrt{16\pi}\,v=1.75$ TeV for the bound $\lvert a_0\rvert\le1$. The two differ by $\sqrt2$, which is the difference between the two conventions for the partial-wave bound, and both are quoted in the literature.

**One number that is zero and must be.** The determinant of the neutral ghost mass matrix. It is zero for every $\zeta$, and it is zero because the photon is massless. A non-zero determinant would mean that $\mathrm{U}(1)_{\mathrm{em}}$ was broken by the gauge fixing, which cannot happen: a gauge condition cannot break a symmetry that the gauge condition respects.

## What the Framework Supplies

**The row the agenda calls a known route, and its status.** *The Standard Model under the Biquaternion Framework: A Research Agenda* classifies the gauge-fixing principle as *known route in standard field theory, no framework realisation*, with the settling computation named as "reproduce the Faddeev–Popov or BV procedure in the algebra, or prove a no-go". That computation is in the corpus: *The Yang–Mills Path Integral and the Faddeev–Popov Procedure* derives the determinant, the ghost action and the gauge-fixed propagator in the algebra, and *BRST Symmetry in Biquaternionic Form* constructs the nilpotent derivation and the gauge-fixing fermion. **The row is discharged at the level of the procedure**, and the agenda's table predates the two companion articles.

**Two agendas disagree about this row, and the disagreement is worth naming.** *Electroweak Theory under the Biquaternion Framework: A Research Agenda* carries the same item in its own ledger as **no route yet**, with the settling item "a biquaternionic gauge-fixing functional selecting a section, or a proof that physical content is orbit-invariant". Both labels were defensible when they were written and only one question separates them: the standard-model agenda asks whether a route exists, the electroweak one asks whether a section has been selected. After the two companion articles a route exists and a procedure is realised, so the first label is now stale; but no algebraic section has been produced, and this article supplies only the abelian half of the second — §*What the Parameter Cannot Change* shows the drift test, which is a statement about amplitudes and not a construction of a section. The honest reading is therefore three-part: the procedure is discharged, the label in the standard-model ledger is stale, and the label in the electroweak ledger still stands in the part that matters to that article. What this article adds is the electroweak completion of the procedure, and the completion's status is different.

**What the framework supplies here, item by item.**

| Item | Status |
|---|---|
| The gauge orbit as the zero mode of the quadratic kernel | Established; recomputed above |
| Faddeev–Popov determinant and ghost action in the algebra | Established (companion articles) |
| Ghosts in the Grassmann envelope $\mathbb{B}\otimes\Lambda$ | Established |
| The $R_\xi$ functional's $\zeta M\xi$ insertion | Transcribed |
| Goldstone masses, ghost masses, the three limits, the equivalence theorem | Transcribed, verified above |

**The one thing the framework cannot do, and why it does not matter here.** The parameter $\zeta$ is not derivable, and it should not be: it is a coordinate on the space of gauges, and a framework that derived a value for it would have derived a coordinate. The framework's contribution to this sector is the *procedure* — the determinant, the ghosts, the nilpotency — and not the parameter. A reader who asks why $\zeta=1$ should not expect an answer from the algebra, in the same way that a reader who asks why the $x$-axis points east should not.

**What the framework does not supply is the electroweak instantiation.** The $R_\xi$ functional above is written for $SU(2)_L\times\mathrm{U}(1)_{\mathrm{Y}}$ and a scalar doublet, and those are the agenda's *no route yet* items: there is no non-central compact action under which the two chiral values transform inequivalently, no derivation of the hypercharge assignments, and no scalar in the required representation. So the honest statement is a two-part one. **The gauge-fixing procedure is discharged in the algebra. Its electroweak instantiation is transcribed, because the group and the scalar it needs are not yet in the framework.**

**Why the article is still worth writing in the corpus's language.** Because the parts that are established are the parts that are usually stated without proof, and because the electroweak completion is exactly the kind of object the corpus's discipline asks to be labelled: the derivation of the $R_\xi$ structure from the mixing is linear algebra available to any framework, the pole structure is the same linear algebra, and the equivalence theorem is the Ward identity. What is imported is the group, the representation and the scalar. The three labels are different and they are kept apart.

## Summary

The quadratic part of the electroweak Lagrangian is degenerate along the gauge orbits. In the broken phase the flat direction is not a pure gauge transformation but the simultaneous shift $A_\mu\to A_\mu+\partial_\mu\theta$, $\xi\to\xi+M\theta$, and the corresponding zero mode of the quadratic kernel is $v=(p_\mu,\,iM)$, verified to $\lVert Kv\rVert/\lVert v\rVert=4.6\times10^{-16}$.

The $R_\xi$ functional $G^a=\partial\cdot W^a-\zeta M_W\xi^a$, with the analogous neutral and photonic conditions, does two jobs with one term: its cross term $+M\xi\partial\cdot A$ cancels the mixing $-M\xi\partial\cdot A$ from the scalar kinetic term, and its $\xi^2$ term supplies the mass $\zeta M^2$ that the potential cannot. The Goldstones therefore have $M_{\xi^\pm}^2=\zeta M_W^2$ and $M_{\xi^0}^2=\zeta M_Z^2$, degenerate with the vectors at $\zeta=1$.

The ghosts come from the Faddeev–Popov determinant, have the mass of the Goldstone of their direction, and carry three weights: $\det M$ in the measure, $-1$ per closed loop, and ghost number $\pm1$. The neutral ghost mass matrix has determinant zero for every $\zeta$, and the zero eigenvalue is the photon's ghost, which exists because $\mathrm{U}(1)_{\mathrm{em}}$ is unbroken.

One propagator formula covers the family, $D_{\mu\nu}=\frac{P_{\mu\nu}}{\Pi-M^2}+\frac{\zeta L_{\mu\nu}}{\Pi-\zeta M^2}$, verified against the kernel $K_{\mu\nu}=(\Pi-M^2)\delta_{\mu\nu}+(1-\frac{1}{\zeta})p_\mu p_\nu$ to $2.2\times10^{-16}$. It gives the Feynman–'t Hooft propagator at $\zeta=1$, the transverse-only propagator at $\zeta=0$, and the Proca propagator at $\zeta\to\infty$, the last to order $1/\zeta$ and algebraically exact in the limit.

The parameter changes nothing observable: the residue at the physical pole is $P_{\mu\nu}$ and carries no $\zeta$, and a conserved current is blind to the parameter, drifting by $4.5\times10^{-16}$ across five gauges while a non-conserved current drifts by $0.78$. Every $R_\xi$ propagator falls as $1/\Pi$, so the superficial degree of divergence is bounded by four independently of the number of loops; the unitary gauge loses that property, which is why renormalisability is proved in the family and not at its endpoint.

The equivalence theorem follows from $\epsilon_L^\mu=p^\mu/M+O(M^2/E^2)$, since $p^\mu/M$ contracts to the divergence of the current and the Goldstone couples to that divergence by the Ward identity. Without the scalar the $W_LW_L$ amplitude grows as $s/v^2$ and the $J=0$ partial wave saturates unitarity at $\sqrt{8\pi}\,v=1.23$ TeV.

The framework discharges the gauge-fixing row of the standard-model agenda at the level of the procedure — and not the electroweak agenda's stronger item, which asks for a section rather than a route — and transcribes the electroweak instantiation, which needs the group, the representation and the scalar that both agendas classify as unreached. The parameter $\zeta$ is a coordinate and is not derivable in principle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\zeta$ | The gauge parameter; $\xi$ of the literature |
| $\zeta_A$ | The gauge parameter of the photon's functional |
| $\xi^a$, $\xi^\pm$, $\xi^0$ | The would-be Goldstone fields of article 4, which writes the index down |
| $W^a_\mu$, $Z_\mu$, $A_\mu$ | The gauge fields in the broken basis: the charged pair, the neutral massive one and the photon |
| $\varphi$, $h$ | The scalar doublet and the physical scalar left after the Goldstones are eaten |
| $v$ | $246.22$ GeV, the vacuum expectation value, entering $M_W=gv/2$ |
| $g$, $g_{\mathrm Y}$ | The $SU(2)_L$ and $\mathrm U(1)_{\mathrm Y}$ couplings |
| $M_W$, $M_Z$, $M_H$ | $80.377$, $91.1876$ and $125.09$ GeV, the measured boson masses |
| $M_Y$ | $g_{\mathrm Y}v/2$, the hypercharge partner in the unbroken-basis functional |
| $G^a$, $G^Z$, $G^A$ | The gauge-fixing functionals |
| $B^a$ | The Nakanishi–Lautrup auxiliary field |
| $\tilde\Xi_{\mathrm{sp}}$ | The gauge-fixing fermion, $s$-exact |
| $\Pi$ | $-\sum_\mu p_\mu p_\mu$, positive, equal to $M^2$ on shell |
| $P_{\mu\nu}$, $L_{\mu\nu}$ | Transverse and longitudinal projectors, traces $3$ and $1$ |
| $D_{\mu\nu}(p)$ | The gauge-field propagator |
| $K_{\mu\nu}$ | Its kernel, $(\Pi-M^2)\delta_{\mu\nu}+(1-\tfrac1\zeta)p_\mu p_\nu$ |
| $M_{\xi}$ | $\sqrt{\zeta}\,M$, the Goldstone mass |
| $M_{\mathrm{gh}}$ | The ghost mass, equal to $M_\xi$ |
| $M_a$ | The Goldstone mass of direction $a$, entering the ghost operator |
| $\Delta[A]$, $\det M$ | The Faddeev–Popov determinant |
| $c^a$, $\bar c^{\,a}$ | Ghost and antighost, ghost numbers $+1$ and $-1$ |
| $\Lambda$ | The Grassmann envelope's odd part |
| $s$ | The nilpotent odd derivation, $s^2=0$ |
| $\epsilon_L^\mu$ | The longitudinal polarisation vector |
| $a_0$ | The $J=0$ partial wave, $s/(16\pi v^2)$ |

## Further Reading

- [The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form](the-yang-mills-path-integral-and-the-faddeev-popov-procedure-in-biquaternionic-form.html). The determinant, the ghost action and the gauge-fixed propagator in the algebra, for the pure-gauge theory this article extends.
- [BRST Symmetry in Biquaternionic Form](brst-symmetry-in-biquaternionic-form.html). The nilpotent derivation, the gauge-fixing fermion and the cohomology that makes "physical" a well-defined word.
- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html). The Goldstones, the counting $12=12$ and the unitary gauge whose limit this article writes.
- [The Weinberg Angle, the Neutral Current and the $Z$ Coupling](the-weinberg-angle-the-neutral-current-and-the-z-coupling.html). The couplings and the masses that enter the $\zeta$-pole positions.
- [Canonical Quantization of the Biquaternion Proca Field](canonical-quantization-of-the-biquaternion-proca-field.html). The massive vector's propagator and polarisation sum, which is the $\zeta\to\infty$ limit here.
- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html). The running of the couplings that the ghosts and Goldstones enter, and the running of $\zeta$ itself.
- [The Standard Model Lagrangian Assembled: Four Sectors in One Expression](the-standard-model-lagrangian-assembled-four-sectors-in-one-expression.html). The gauge-fixed action as the sum this article separates.
- [The Standard Model under the Biquaternion Framework: A Research Agenda](the-standard-model-under-the-biquaternion-framework-a-research-agenda.html). The three-way classification the last section uses, and the gauge-fixing row it discharges.

- [Electroweak Precision Observables: the Oblique Parameters $S$, $T$, $U$](electroweak-precision-observables-the-oblique-parameters-s-t-u.html). The two-point functions built from the projectors of §*The Propagators and the Three Limits*, and the gauge invariance that fixes their transverse structure.
- [The QCD Lagrangian: Colour, the Triplet, the Octet and the Feynman Rules](the-qcd-lagrangian-colour-the-triplet-the-octet-and-the-feynman-rules.html). The same functional in the unbroken non-abelian case, where the coupling is in the derivative and the ghost sector is the whole of the difference between the classical and the quantum action.
