# __The Proton in Biquaternionic Form__

## Introduction

The proton is the stable charged baryon: spin-$\tfrac{1}{2}$, electric charge $+1$ in units of the elementary charge, mass $938.272$ MeV, and a composite of three quarks bound by the colour interaction. In the biquaternion framework of these articles it can be placed as a massive spin-$\tfrac{1}{2}$ Dirac field, and the purpose of this article is to separate, as the corpus's discipline requires, what the framework's own structure says about it from what is imported from standard physics.

The framework is a research programme, not a completed theory, and three of its existing results bear directly on any claim about the proton.

- **It has a non-abelian gauge construction inside the algebra** — a connection, a curvature containing the commutator term, the adjoint transformation law, the Bianchi identity and a gauge-invariant Yang–Mills density — built on the compact factor $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ of the material sector (*Non-Abelian Gauge Fields in Biquaternionic Form*).
- **It gives each value of the field its own charge**, $ϙ_L$ on the L part and $ϙ_R$ on the R part, with the mass selection rule $ϙ_L=ϙ_R$: a massive Dirac field in the framework is vector-like (*Chiral Fermions in the Biquaternion Framework*).
- **It has no colour group, no confinement mechanism, and no quark content.** The compact algebra available inside $\mathbb{B}$ is at most $\mathfrak{u}(2)$ of real dimension $4$; every carrier of $\mathbb{B}$ has even complex dimension, so no three-dimensional colour carrier exists within the present construction; and nothing in the series derives $SU(3)$ or a confinement mechanism (*Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*).

The consequence for the proton is stated at the outset, because the article depends on it.

- **Representable, and checked below.** The proton can be placed in the framework as a massive spin-$\tfrac{1}{2}$ Dirac field. Its spin-$\tfrac{1}{2}$ content comes from the algebra's single simple carrier; its electric charge is the value its charge element carries; and, being massive, the field is necessarily vector-like. The value $+1$ is a value the operator carries, and this is verified explicitly.
- **Not derived.** Nothing in the algebra selects $ϙ_p=+1$, relates it to the electron's charge $-1$, or makes it an integer. The free biquaternion Dirac equation contains no charge at all, so the proton and the neutron satisfy the *same* free equation and differ only in an inserted coupling. The charge value is a parameter, exactly as the electron's charge is a parameter.
- **Outside the framework.** The proton's compositeness — its quark content, its colour, its binding, its anomalous magnetic moment, and the fact that it is a bound state at all — is not in the framework. These are standard-physics imports, and the QCD agenda records that the framework has no route to them.

This is a deliberately modest accounting, and it is the honest one. The sharpest test the proton offers is its charge: the framework's charge operator must give $+1$ for the proton where the corresponding operator gives $0$ for the neutron. The operator carries both values, and that is a genuine, checkable statement about its spectrum; but the *selection* of $+1$ and $0$ is not a framework result. The negative half of that sentence is the more useful one, and it is stated plainly rather than smoothed over with a derivation the algebra does not supply.

## The Proton as a Spin-$\tfrac{1}{2}$ Biquaternion Dirac Field

The proton enters the framework the way any massive spin-$\tfrac12$ fermion does: as an element of the algebra,

$$
\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R\in\mathbb{B},
$$

whose two parts carry the two values of the chirality, $\tilde{Ξ}^{\mathrm{sp}}_L$ the value L and $\tilde{Ξ}^{\mathrm{sp}}_R$ the value R, at the declared axis $\vec u$ (*Special Element Conventions*, §*The Chirality Convention*); every element of the algebra is such a field, and only the zero element has both parts zero. This article declares the axis $\vec u=\vec e_z$, the unit at which the chirality cell is the volume cell of the material frame $\mathbb{M}_-$. The free propagation is the biquaternion Dirac equation

$$
\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R=m_p\,\tilde{Ξ}^{\mathrm{sp}}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m_p\,\tilde{Ξ}^{\mathrm{sp}}_R .
$$

In this section we record what is structural about placing it there and what is not.

### The One-Sided and the Two-Sided Equation

The article carries two Dirac equations, and they must not be read as one. They share the operator and the mass coefficient; they differ in how many times the operator is written.

**The one-sided equation** is the pair displayed above, and it is the corpus's definition. Every derivative acts by left multiplication, and the mass is the off-diagonal pairing of the two values rather than a term inside either. The two values are read from the chirality cell and from nothing else; the label is not an element of the algebra, because the element that suggests itself, $i\vec e_z$, has square $+e_t$ and the split it gives is the index of the decomposition and not the chirality (*Special Element Conventions*, §*The Chirality Convention*, the paragraph *What the word does not name*).

**The two-sided equation** writes the same pair once, on the same element. The pair operator of *Conventions of the Operators and the Calculus*, §*The Pair Operator and Its Symbol*, carries the L value by $\tilde{\nabla}^{\natural}$ and the R value by $\tilde{\nabla}$,

$$
\mathbb{D}\tilde{Ξ}^{\mathrm{sp}}=m_p\,\tilde{Ξ}^{\mathrm{sp}},
\qquad
\mathbb{D}^2=\Box
$$

on each value, so the pair reads

$$
\left(\mathbb{D}-m_p\right)\tilde{Ξ}^{\mathrm{sp}}=0 .
$$

The operator is a single object acting on the element: it is the pair written once, and it contains no matrix generator. What the one-operator reading adds is the charge and the bilinears, which are read on the element. The algebra carries the mass term and the mass shell, and the two readings are related by a change of the operator, not by a change of physics.

| | One-sided equation | Two-sided equation |
|---|---|---|
| Equation | $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R=m_p\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m_p\tilde{Ξ}^{\mathrm{sp}}_R$ | $(\mathbb{D}-m_p)\tilde{Ξ}^{\mathrm{sp}}=0$ |
| Field | $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R\in\mathbb{B}$, two values | the same element, the same two values |
| Mass | the off-diagonal pairing of the two values | the same coefficient, off-diagonal in the two values |
| Operator | left multiplication by $\tilde{\nabla}$ and $\tilde{\nabla}^{\natural}$ | one operator, $\mathbb{D}^2=\Box$ on each value |
| Chirality | the value carried by each part | the same values |
| Use | the definition, the mass term, the mass shell | the charge, the charge value, the bilinears |

**The spin-$\tfrac12$ content follows from the algebra and not from the proton.** The elements of norm one, $\tilde U\tilde U^{\natural}=e_t$, form $\mathrm{SL}(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group; the left multiplications act on each value with weights $\pm\tfrac12$, and a rotation by $2\pi$ is the element $-e_t$. Left multiplication by $-e_t$ carries the field to $-\tilde{Ξ}^{\mathrm{sp}}$, while the conjugation action of the same element on the four-vectors of $\mathbb{M}_-$, $\tilde V\mapsto\tilde U\tilde V\tilde U^{-1}$, returns $+\tilde V$. The half-integral, double-valued character of the proton's spin is therefore a consequence of where the field lives, and *not* of anything proton-specific. What the framework does **not** derive is why this composite object has spin $\tfrac12$: that is angular-momentum addition among constituents in standard physics, and the framework has no constituent structure to add. The correct statement is the conditional one — *if* the proton is modelled as an element of $\mathbb{B}$, its spin is $\tfrac12$.

**The mass term is structural; the mass value is not.** The proton mass appears exactly once, as the coefficient $m_p$ of the linear term that couples the two values, $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R=m_p\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m_p\tilde{Ξ}^{\mathrm{sp}}_R$; it is the only mass term in the free equation. The algebra's real structure $\flat=-{}^{*}$ is a different object: for $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_++\tilde{Ξ}^{\mathrm{sp}}_-$ with $\tilde{Ξ}^{\mathrm{sp}}_\pm\in\mathbb{M}_\pm$ one has $\tilde{Ξ}^{\mathrm{sp}\flat}=-\tilde{Ξ}^{\mathrm{sp}}_++\tilde{Ξ}^{\mathrm{sp}}_-$, so $\flat$ acts as $+1$ on the material part and $-1$ on the informational part.

The value $m_p=938.272$ MeV, or $1.6726\times10^{-27}$ kg, is not a consequence of the algebra or of the equation. It is a parameter, and the framework is scale-free until it is supplied. Equivalently, the free field lies on the mass shell

$$
\tilde{P}\tilde{P}^{\natural}=-m_p^2c^2,
$$

in the corpus's four-momentum convention $\tilde{P}=iE/c\,e_t+\vec p$, where the product is $-E^2/c^2+|\vec p|^2$ and the relation is $E^2=|\vec p|^2c^2+m_p^2c^4$: the *form* of the mass shell is structural, the number in it is an import.

**The free equation contains no charge.** Neither the one-sided pair nor the two-sided equation $(\mathbb{D}-m_p)\tilde{Ξ}^{\mathrm{sp}}=0$ contains a coupling. The mass coefficient $m_p$ is the only parameter, and it is central.

Charge enters only when the field is coupled to a four-potential, through minimal substitution. Two immediate consequences follow and they are the theme of the next section. First, the proton and the neutron satisfy the same free equation with the same operator; whatever distinguishes them is an inserted coupling and not a structure of the equation. Second, the framework's ability to state the proton's charge is the ability of its charge element to *carry* the value $+1$, not an ability to produce it.

## The Charge Operator on the Field

The charge of the framework multiplies each value of the field by its own number,

$$
\tilde{Ξ}^{\mathrm{sp}}_L\mapsto ϙ_L\tilde{Ξ}^{\mathrm{sp}}_L,
\qquad
\tilde{Ξ}^{\mathrm{sp}}_R\mapsto ϙ_R\tilde{Ξ}^{\mathrm{sp}}_R,
$$

with independent couplings $ϙ_L,ϙ_R\in\mathbb{R}$ that the algebra does not fix (*Chiral Fermions in the Biquaternion Framework*).

**The two rules are one right multiplication.** The action is $\tilde{Ξ}^{\mathrm{sp}}\mapsto\tilde{Ξ}^{\mathrm{sp}}Ϙ$, by the element

$$
Ϙ=\tfrac{ϙ_L+ϙ_R}{2}\,e_t+\tfrac{i}{2}\left(ϙ_L-ϙ_R\right)\vec e_z\;\in\;\mathbb{M}_+ ,
$$

a derived form: $Ϙ=ϙ_L\tilde\Pi_+(\vec e_z)+ϙ_R\tilde\Pi_-(\vec e_z)$, the two chirality states at the axis of the previous section. The element $Ϙ$ is Hermitian, and it is central only in the vector-like case $ϙ_L=ϙ_R$, where the action is also a left multiplication. The covariant derivative carries it,

$$
D_\mu\tilde{Ξ}^{\mathrm{sp}}=\frac{\partial\tilde{Ξ}^{\mathrm{sp}}}{\partial Q_\mu}+\frac{i}{\hbar}A_\mu\,\tilde{Ξ}^{\mathrm{sp}}Ϙ .
$$

The framework's own abelian gauge structure — the one drawn from the central line $\mathbb{C}_{\mathbb{B}}$ — is the specialization $ϙ_L=ϙ_R$: a central phase multiplies the two values alike, so it is vector-like by construction, and an axial coupling would have to sit outside the centre.

Two structural facts about $Ϙ$ are inherited from the chiral-fermion article and are used here. First, $Ϙ$ is Hermitian and diagonal in the two values: it commutes with the chirality cell $\Gamma=-iR_{\vec e_z}$, and it acts on the L value by $ϙ_L$ and on the R value by $ϙ_R$. Second, the **mass selection rule**. The mass term is the only term of the free pair that links the two values, so it is the only place where the two charges meet. Under a gauge transformation the L value picks up the phase $\exp(iϙ_L\lambda/\hbar)$ and the R value the phase $\exp(iϙ_R\lambda/\hbar)$; the derivative terms are made covariant by the transformed potential, but the mass term $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R=m_p\tilde{Ξ}^{\mathrm{sp}}_L$ then carries one phase on each side, so it is invariant for every real gauge function $\lambda$ **if and only if** $ϙ_R=ϙ_L$. A framework fermion that carries a mass is thus *forced* to be vector-like, and its charge element collapses to the central element,

$$
\boxed{\;ϙ_L=ϙ_R=ϙ
\quad\Longrightarrow\quad
Ϙ=ϙ\,e_t\;}.
$$

This much is a derivation: the mass term of the framework and the charge element of the framework are not independent, and for the proton — which is massive — they force the vector-like form. It is the structural reason a colour interaction, which is vector-like, sits comfortably with massive baryons, just as the QCD agenda records. One qualification belongs to the step: the selection rule is a statement about the Dirac mass term, and the proton's mass term is precisely that term — the linear pair of the two values — so the vector-like forcing follows directly. The open real-form question of the chiral-fermion article concerns a separate conjugate pairing built on the algebra's real structure $\flat$, a neutral-fermion coupling that does not enter the charged proton's Dirac mass; it is carried into the open questions below.

**The check on the values $+1$ and $0$.** The proton's charge is $+1$ and the neutron's is $0$, in units of the elementary charge. Substituting the two assignments into the operator gives

$$
\boxed{\;Ϙ_p=Ϙ\big|_{ϙ=+1}=+e_t,
\qquad
Ϙ_n=Ϙ\big|_{ϙ=0}=0\;},
$$

two central elements, the first of which carries every element of the algebra to $+1$ times itself and the second to zero. Each is Hermitian, each is blind to the chirality label, each is compatible with the mass selection rule, and the two are distinct. The spectrum is that of the one-particle field; the antiproton's $-1$ is not a second value of $Ϙ$, but the charge of the conjugate field, an import from the second-quantized reading. This was recomputed exactly on a hundred generic elements: the two multiplications, the element $Ϙ$, its Hermiticity, its centrality in the vector-like case, and the covariance of the free pair on the vector-like branch $ϙ_L=ϙ_R$ against its failure on the axial branch $ϙ_R=-ϙ_L$. So the operator *carries* the proton's $+1$; the value is a number the framework's charge element has.

**The honest qualification.** Carrying a value is not selecting it. The value $ϙ$ is a free real parameter of the framework; nothing in $\mathbb{B}$, in the Dirac equation, or in the gauge principle fixes it to $+1$ for the proton, to $0$ for the neutron, or to any integer at all. The framework does not relate $ϙ_p$ to the electron's $ϙ_e$, so the equality of their magnitudes and the opposite signs — a striking and measured fact about the world — are not framework results; the electron article records the same absence for the electron. Nor does the framework explain why the proton's charge is an integer while a hypothetical fractionally charged constituent would not be; charge quantisation is not derived anywhere in the series. And the framework cannot *distinguish* the proton's field from the neutron's: the two are the same kind of element of the algebra, differing only in the value of an inserted coupling, exactly as the electron and muon are the same kind of element differing only in mass. In short, the sharpest test the proton offers is passed as a statement about the operator's value and failed as a derivation. That is the result, and it is a negative one about derivation.

## Which Generator Carries the Electric Charge

The charge operator must not be silently identified with a Lie-algebra generator without saying which; here the answer is definite, and it is itself a checkable structural result.

The framework's abelian gauge group is the $*$-unitary part of the centre,

$$
\mathrm{U}(1)\subset\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\},
\qquad
\mathrm{U}(1)=\{\exp(i\theta e_t):\ \theta\in\mathbb{R}\},
$$

and the infinitesimal generator of the gauge transformation is the central element $ie_t\in\mathbb{M}_-$, anti-Hermitian as a Lie-algebra generator must be. The corresponding Hermitian charge is the central $Ϙ=ϙe_t$, whose generator is $e_t$ itself, the unit of the algebra. The two differ by the factor $\pm i$, $e_t=-i(ie_t)$, and that factor is the convention which turns an anti-Hermitian algebra element into a Hermitian observable. The electric charge is therefore carried by the **abelian factor** of the algebra — the central line — and not by the non-abelian factor.

The non-abelian factor cannot be the electric charge, and this is checked, not asserted. The generators of the compact factor are $T_a=\tfrac12\vec e_a$; they are anti-Hermitian, and each squares to minus a quarter of the unit,

$$
\boxed{\;T_a^2=\tfrac14\vec e_a^2=-\tfrac14 e_t,
\qquad
\text{values } \pm\tfrac{i}{2}\ \ (\text{purely imaginary})\;}.
$$

A charge operator is an observable: it must be Hermitian with real values. The $T_a$ fail the first condition and have imaginary values, so no $\mathrm{SU}(2)$ generator in $\mathbb{M}_-$ can be the electric charge. Their Hermitian partners are the isospin-like generators $iT_a=\tfrac12i\vec e_a\in\mathbb{M}_+$, with

$$
(iT_a)^2=+\tfrac14 e_t,
\qquad
\text{values } \pm\tfrac12,
$$

which are Hermitian but have *half-integer* values; they cannot carry the proton's integer charge $+1$ either. All three $T_a$ and all three $iT_a$ were checked, from the square alone: an element whose square is $-\tfrac14e_t$ has the two values $\pm\tfrac{i}{2}$, and an element whose square is $+\tfrac14e_t$ has the two values $\pm\tfrac12$. The conclusion is sharp: the proton's electric charge lives on the central $\mathrm{U}(1)$, the $\mathrm{SU}(2)$ generators are a different set of quantum numbers, and identifying the two would be an error the framework's own spectrum forbids.

Three further distinctions belong here, because the framework has several conserved-looking quantities and they are easy to conflate.

- **Electric charge versus chirality.** The element $Ϙ$ is diagonal in the two values and commutes with the chirality cell for every $ϙ_L,ϙ_R$; the axial combination $ϙ_R=-ϙ_L$ makes $Ϙ=-ϙ_L\,\Gamma$, proportional to the chirality cell. But $\Gamma$ is the chirality cell, not an electric charge, and the axial assignment is precisely one that fails the mass selection rule. For the massive proton only the vector-like specialization survives, and it is blind to the chirality.
- **Electric charge versus the $\mathrm{SU}(2)$ generators.** As above, these have imaginary or half-integer values; they are isospin-like, not electric.
- **Electric charge versus baryon number.** The framework supplies no baryon-number current, no conserved fermion number beyond the central phase, and no composite quantum number at all. The central phase does pass through the linear pair, so the proton's electric charge is conserved by the massive free equation; but that is a statement about the $\mathrm{U}(1)$ of electromagnetism, not about baryon number, which is not constructed here.

## The Isospin Partner, and Why It Is Not in This Equation

The equation of this article carries one field, and the proton–neutron near-degeneracy is nowhere in it. There is a second way to place a spin-$\tfrac12$ fermion in the algebra, however, and there the pair *is* structural. In Lanczos's doubled system

$$
\tilde{\nabla}\tilde Q_1=m\tilde Q_2, \qquad \tilde{\nabla}\tilde Q_2=m\tilde Q_1,
$$

one takes the two superpositions of the companion articles. With $\sigma=\tfrac12(e_t+i\vec{\nu})$ the state along a unit direction $\vec{\nu}$, so that $\sigma^2=\sigma$ because $(i\vec{\nu})^2=i^2\vec{\nu}^2=(-e_t)(-e_t)=e_t$, with $\bar{\sigma}=e_t-\sigma=\tfrac12(e_t-i\vec{\nu})$ its complementary state, of zero product $\sigma\bar{\sigma}=0$, and with $\vec{\tau}$ any unit direction orthogonal to $\vec{\nu}$:

$$
\tilde{Ξ}^{\mathrm{sp}}_p=\tilde Q_1\sigma+\tilde Q_2^{*}\bar{\sigma}, \qquad \tilde{Ξ}^{\mathrm{sp}}_n=\left(\tilde Q_1\bar{\sigma}-\tilde Q_2^{*}\sigma\right)i\vec{\tau}.
$$

These are Gürsey's proton and neutron. Both descend from the one system with the one mass parameter $m$, so they have **equal mass by construction**; the relative sign and the factor $i\vec{\tau}$ place them in orthogonal isospin directions. The transformations that preserve both superpositions form a two-parameter group, found by Nishijima in a different context,

$$
G_N=\sigma\,\exp(i\alpha)+\bar{\sigma}\,\exp(i\beta),
$$

which acts by right multiplication, multiplies each state by its own phase and annihilates the other,

$$
\tilde{Ξ}^{\mathrm{sp}}_p\,G_N=e^{i\alpha}\tilde{Q}_1\sigma+e^{i\beta}\tilde{Q}_2^{*}\bar{\sigma}.
$$

The two superpositions therefore carry two independent abelian phases, and with them two independent charges, while the single mass parameter $m$ gives them equal mass. The source's interpretation is that Lanczos's "doubling" of the spin-$\tfrac12$ field was isospin in 1929, three decades early.

**The price of that reading.** The two phases are independent on the superpositions, but the common mass links the two Lanczos fields. Read on those fields, the re-phasing is $\tilde Q_1\mapsto e^{i\alpha}\tilde Q_1$ and $\tilde Q_2\mapsto e^{-i\beta}\tilde Q_2$, the minus sign coming from the conjugation in $\tilde{Ξ}^{\mathrm{sp}}_p$ and $\tilde{Ξ}^{\mathrm{sp}}_n$. The first Lanczos equation then becomes $\tilde{\nabla}\bigl(e^{i\alpha}\tilde Q_1\bigr)=m\,e^{-i\beta}\tilde Q_2$, which is the original equation only when $\alpha+\beta=0$. The doubled system with $m\neq0$ is therefore invariant on that one line of the $(\alpha,\beta)$ plane, and the orthogonal combination is a symmetry of the superpositions' *form* alone. Two independent phases and one common mass stand together only as a kinematic statement, which is the same phenomenon the charge section records: a mass term, being a link between the two values, breaks the relative phase.

The corpus's own position is not overturned by this, and it becomes sharper. The isospin of the doubled system is **not** the material sector's $\mathrm{SU}(2)$: it acts by *right* multiplication on the two biquaternions $\tilde Q_1$, $\tilde Q_2$ of the doubled field, whereas the rotation and gauge $\mathrm{SU}(2)$ of the previous section acts on the algebra by left multiplication and commutator. The corpus's refusal to identify flavour isospin with that $\mathrm{SU}(2)$ therefore stands unchanged. What the doubled route shows is that the near-degeneracy need not be imported *if* the two particles are taken as the two superpositions of one Lanczos pair — at the price of doubling the field and of a mass parameter the algebra still does not fix. In the single-field equation used here, the pair must be inserted; that is the choice this article makes, and the doubling is the alternative.

## What the Framework Does Not Supply: Compositeness and Colour

The proton is not an elementary field in nature; it is a bound state. Nothing in the biquaternion framework represents that, and the omission is not a gap with a known route.

**No colour group.** The compact algebra available inside $\mathbb{B}$ is the maximal compact subalgebra of $\mathrm{GL}(2,\mathbb{C})$, namely $\mathfrak{u}(2)=\mathbb{R}(ie_t)\oplus\mathfrak{su}(2)$, of real dimension $4$; a $\mathrm{SU}(3)$ of dimension $8$ does not embed in it. The matter side has the matching ceiling: $\mathbb{B}$ is simple, so every carrier is a sum of copies of the unique simple one, of complex dimension two, and therefore every carrier has even complex dimension, so a three-dimensional colour carrier does not exist. (This was spot-checked on the elements: the three units close under the commutator, $[\vec e_a,\vec e_b]$ lying in their own span, and with $ie_t$ that is the whole compact part, of real dimension four.) The framework has no colour triplet and no gluon octet.

**No confinement.** There is no Wilson loop, no area law, no string tension, no mass gap, and no gauge-fixing principle in the series, and the QCD agenda classifies confinement as an obstacle with no route yet. The zero-divisor cone of $\mathbb{M}_-$ is not an area law.

**No quark content.** Nothing derives a quark, a flavour, or a fractional charge. The identification "proton $=uud$" is standard physics, and the framework can only transcribe the phrase. Since the framework cannot even host a three-dimensional internal carrier, it cannot host the triplet in which a quark would sit.

**No bound-state structure.** The framework has no two-body or many-body bound-state formalism on which a baryon could be built, and no action, measure or gauge-invariant regulator of the kind the QCD agenda names as prerequisites. The proton must therefore be represented as an *effective* elementary spin-$\tfrac12$ field, with all composite physics absorbed into imported parameters.

The consequence is that the proton's compositeness — the reason its mass is 938 MeV rather than a Lagrangian parameter, the reason its magnetic moment is not the Dirac value, and the reason its charge is an integer — is entirely outside the framework. The framework can describe the effective proton; it cannot explain why there is one.

## Spin, Statistics and the Magnetic Moment

**Spin.** The spin-$\tfrac12$ content is derived conditionally, as in the first section: it follows from the algebra, not from any proton-specific structure. The spin-statistics theorem is transcribed rather than derived (*The Spin–Statistics Theorem in Biquaternionic Form*), but the framework does identify the half-integer weights as native to the algebra, on which a rotation by $2\pi$ acts by left multiplication as $-e_t$, whereas the conjugation action on $\mathbb{M}_-$, the carrier of integer spin, returns $+e_t$. The proton, written as an element, is a fermion for exactly the same structural reason as the electron; the framework does not derive that this particular composite is a fermion.

**The magnetic moment.** Carrying the biquaternion Dirac equation to the non-relativistic regime produces the tree-level gyromagnetic factor $g=2$ for any structureless spin-$\tfrac12$ field with the inserted charge, exactly as for the electron (*The Electron in Biquaternionic Form*). Applied to the proton's effective field this gives a magnetic moment $\vec\mu_p=(e\,ϙ_p/m_p)\vec S$ with $ϙ_p=+1$, of one nuclear magneton $\mu_N=e\hbar/2m_p$ when $\vec S$ is aligned with the field. The measured proton moment is $2.7928\,\mu_N$, i.e. $g_p\approx5.586$. The deviation is *not* a small radiative correction of the kind the electron's $g-2$ is: it is a large strong-interaction and compositeness effect, produced by the quark and gluon dynamics of the bound state, and the framework supplies none of it. For the proton, therefore, even the tree-level value is not a prediction about the real object — it is the value the framework would assign to a fictitious elementary field of the same mass and charge.

## What Is Imported from Standard Physics

The table sorts the proton's properties by the status they have in the framework, in the manner of the electron article.

| Property of the proton | Status in the framework | Where it comes from |
|---|---|---|
| Spin-$\tfrac12$ content | Represented (forced once modelled) | the algebra's single simple carrier; the left multiplications act on each value with weights $\pm\tfrac12$ |
| Spin states, observables, Born rule | Derived | the states of $\mathbb{M}_+$; $\mathrm{Tr}(\tilde Q_1\tilde Q_2^{*})=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ |
| Mass term is off-diagonal in the two values; real structure acts $+1/-1$ on $\mathbb{M}_\mp$ | Derived | the linear pair of the two values; $\tilde{Ξ}^{\mathrm{sp}\flat}=-\tilde{Ξ}^{\mathrm{sp}}_++\tilde{Ξ}^{\mathrm{sp}}_-$ |
| Vector-like charge element $Ϙ=ϙ\,e_t$ for a massive field | Derived | mass selection rule $ϙ_L=ϙ_R$, from the covariance of the mass term |
| Conserved current, an element of $\mathbb{M}_-$ | Quoted (framework) | the sesquilinear commutator of *Product and Form Conventions*, §*The Twelve Products and Their Names*: $\tilde J=i[\tilde{Ξ}^{\mathrm{sp}*}(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}})-(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}*})\tilde{Ξ}^{\mathrm{sp}}]$ |
| Electric charge generator is the central $\mathrm{U}(1)$ | Derived | $\mathbb{C}_{\mathbb{B}}$ central; the $\mathrm{SU}(2)$ generators have imaginary or half-integer values |
| Charge value $ϙ_p=+1$ | Represented (parameter) | inserted coupling; not selected by the algebra |
| $\lvert ϙ_p\rvert=\lvert ϙ_e\rvert$, opposite signs | Outside | no framework structure; independent parameters |
| Charge quantisation (integrality) | Outside | not derived in the framework |
| Mass value $m_p$ | Represented (parameter) | inserted into the Dirac equation |
| Compositeness; quark content $uud$; colour; confinement | Outside | standard QCD; no route in the framework |
| Anomalous magnetic moment $g_p\approx5.586$ | Outside | strong-interaction / composite dynamics |
| Baryon number | Outside | not constructed |
| Conservation of the charge under the framework's own mass | Derived | the mass term is the linear pair of the two values, through which the continuous central phase passes; the real structure's separate pairing is the open interpretation |
| Empirical contact | Outside | no prediction distinguishing the framework from standard physics |

## Open Questions

1. **Is the charge value derivable at all?** The framework's charge operator carries $+1$ for the proton and $0$ for the neutron, but no principle of the algebra selects those values. Is there a framework-internal quantisation condition — an anomaly, a topological constraint, or a compactness condition on the central $\mathrm{U}(1)$ — that would fix $ϙ$ to integers, or to the specific integer $+1$ for the proton? None is known, and none is proposed here.

2. **Is there any relation between $ϙ_p$ and $ϙ_e$?** The measured equality $|ϙ_p|=|ϙ_e|$ and the opposite signs are not explained. In the framework the proton and electron are independent elements of the same algebra, with independent couplings; nothing ties them.

3. **Which generator, in the end?** This article shows that the electric charge must be the central $\mathrm{U}(1)$ generator, because the $\mathrm{SU}(2)$ generators and their Hermitian partners have imaginary and half-integer spectra. Is that identification forced, or could an enlarged carrier host a different Hermitian generator with integer spectrum that also plays the role of electric charge? The ceiling result of the QCD agenda suggests not within $\mathbb{B}$, but the enlarged-carrier question is open.

4. **Can the framework host a bound state?** The proton's compositeness is entirely imported because the framework has no bound-state formalism and no colour. A biquaternionic bound-state construction — if one could be built on the carrier the QCD agenda says is missing — is the only route by which compositeness could enter. No route yet.

5. **Does the framework's own mass violate the charge it relies on?** No: the framework's mass term is the linear chiral pair, through which the continuous central phase passes, so the massive free equation conserves the proton's charge. The interpretation the chiral-fermion article leaves open concerns a separate conjugate pairing on the algebra's real structure $\flat$, a neutral-fermion coupling that does not enter the charged proton's mass. The live question is therefore whether that separate pairing exists physically, not whether the proton's charge survives its own mass.

6. **Baryon number.** Nothing in the framework distinguishes the proton's conserved fermion number from the electron's. Is there any framework object that could carry baryon number, given that the algebra's abelian charge is the electromagnetic-type $\mathrm{U}(1)$ and no composite quantum number is constructed? **One external claim bears on this**, and it is recorded here because it is the only one the corpus knows: Gsponer and Hurni (*Lanczos's Equation to Replace Dirac's Equation?*, Lanczos centenary, 1994; arXiv:hep-ph/0112317) report that the Einstein–Mayer generalized-mass system classifies its solutions into two families — quarks and leptons — carrying the correct fractional and integral electric charges **and baryonic charge**, with the neutrino and the u-quark masses zero by eigenvalue equations. Three things should be said about it. It is a four-page conference abstract with no derivation exhibited, so it is a claim and not a result, and the present article's "not constructed" status stands. It **does** give baryon number an abelian current of its own, which is more than a place in a classification: the Einstein–Mayer Lagrangian carries the **barycharge current** $S = AEA^{+} + BEB^{+}$, conserved and invariant exactly under those abelian gauge transformations that commute with the generalized mass $E$ — the abelian part of the Nishijima group, "which contains the electric and baryonic gauge groups" — alongside the probability current $C = AA^{+} + BB^{+}$, which is invariant under any non-abelian unitary gauge of $A$ or $B$. And it does not settle whether the assignment is forced: the *Note added in 1996* attached to the arXiv version states that the Nishijima-group restriction used to fix the charges is "not sufficient to set the correct fractional or integral electric and baryonic charges of the quarks and leptons". The source is therefore a pointer with its own retraction attached, and the corpus records the current, the claim, and the retraction together.

7. **Empirical contact.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard physics. The construction above is a reformulation, and a reformulation that must import the proton's mass, charge and compositeness has no prospect of doing so.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

No gamma appears in the sections above, and this section is where it does. Its purpose is to give the same cells their standard names, for a reader who wants the Dirac notation, and to state once the identities that notation carries. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Each gamma is a single cell $L_aR_b$, the operator $\tilde{Ξ}^{\mathrm{sp}}\mapsto a\tilde{Ξ}^{\mathrm{sp}} b$. The frame is

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

Because $L_{e_t}^{\mathrm{pau}}$ is the identity of the module, the first and the last simplify: $\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}$ and $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$. In this frame $\gamma_0$ and $\gamma_5$ are Hermitian and $\gamma_1,\gamma_2,\gamma_3$ are anti-Hermitian — the standard Dirac pattern for $\varepsilon=(1,-1,-1,-1)$ — and that is why the Dirac adjoint of the charge section is built with $G_t=\gamma_0$ alone. Each gamma is one cell and not a sum of cells, which the coefficient matrix $c(\gamma)$ records by having rank one; a general element is a sum of such products, they form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and the least number of products summing to $M$ is $\operatorname{rank}c(M)$, at most four.

The generator cells $G_\mu$ of the charge section are exactly these gammas, $G_\mu=\gamma_\mu$: $G_t=\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}$ and $G_k=\gamma_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$. The anticommutator of the notation table is therefore the Clifford relation below.

**Chirality, three objects and one representative.** $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ *is* the chirality cell $\Gamma$ of the charge section, so the fifth cell and the fifth gamma are one object in two readings. The central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object: it is central, it belongs to the double $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}_\mathbb{R}$, and it is not an element of $\mathbb{B}$. The chain is $\xi$ in the double, $\Gamma=\mathrm{diag}(-I_2,I_2)$ its representative on the Dirac module, and $\gamma_5$ that representative written as a cell.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the body and the notation table cite.** Here $\mathrm{tr}$ is the $4\times4$ matrix trace, $I_4$ the identity of $M_4(\mathbb{C})$, $\varepsilon=(1,-1,-1,-1)$ and $\epsilon_{0123}=+1$.

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

**The contraction sums depend on the frame, because a cell's square does.** In $\mathbb{M}_-$, with the plain weight $\varepsilon=(1,-1,-1,-1)$,

$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$

$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\varepsilon_\alpha\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\rho\gamma_\mu=+2\gamma_\alpha\gamma_\beta\gamma_\rho .
$$

With the summed index raised the weights become signs, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, and the same four sums read $-4I_4$, $+2\gamma_\alpha$, $-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $-2\gamma_\alpha\gamma_\beta\gamma_\rho$. Without weights the sum is $\sum_\mu\gamma_\mu\gamma_\mu=(1-1-1-1)I_4=-2I_4$: the metric has left the cells and entered the sum.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The proton can be placed in the biquaternion framework as a massive spin-$\tfrac12$ Dirac field, written in the algebra as the one-sided pair $\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R=m_p\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=m_p\tilde{Ξ}^{\mathrm{sp}}_R$ and as the single equation $(\mathbb{D}-m_p)\tilde{Ξ}^{\mathrm{sp}}=0$ with $\mathbb{D}^2=\Box$. The framework makes three structural statements about it. The spin-$\tfrac12$ content follows from the algebra's single class of simple carrier, on which the left multiplications act with weights $\pm\tfrac12$; the mass term is the linear pair of the two values of the field; and, being massive, the proton is forced by the mass selection rule $ϙ_L=ϙ_R$ to be vector-like, so the general charge element, which multiplies the L value by $ϙ_L$ and the R value by $ϙ_R$, collapses to the central element,

$$
\boxed{\;Ϙ=ϙ_p\,e_t\;},
$$

the coupling sitting on the central element $ie_t\in\mathbb{M}_-$ and not on the compact $\mathrm{SU}(2)$.

On the sharpest available test, the framework's charge gives $+1$ for the proton and $0$ for the neutron as exact values: $Ϙ_p=+e_t$ and $Ϙ_n=0$, both central elements, both blind to the chirality, both compatible with the mass selection rule. This was verified on a hundred generic elements, together with the covariance of the free pair on the vector-like branch and its failure on the axial one. But the *selection* of the values is not a framework result: $ϙ$ is a free parameter, nothing fixes it to $+1$ or to an integer, nothing relates $ϙ_p$ to the electron's charge, and the free equation contains no charge at all. The test is therefore passed as a statement about the operator's value and failed as a derivation — a negative result, stated plainly.

It was also shown that the electric charge cannot be carried by the non-abelian factor: the $\mathrm{SU}(2)$ generators $T_a=\tfrac12\vec e_a$ have square $-\tfrac14e_t$ and purely imaginary values $\pm\tfrac i2$, and their Hermitian partners $iT_a$ have square $+\tfrac14e_t$ and half-integer values $\pm\tfrac12$, so neither can be the proton's integer electric charge. The charge lives on the central line $\mathbb{C}_{\mathbb{B}}$. This settles the "which generator" question within the present construction.

What the framework does not supply is everything that makes the proton a proton. There is no colour group — the compact algebra inside $\mathbb{B}$ is at most $\mathfrak{u}(2)$, of real dimension $4$, and every carrier of $\mathbb{B}$ has even complex dimension, so no colour triplet exists. There is no confinement mechanism, no colour carrier, no quark content, no bound-state formalism, and no baryon number. The proton's mass $938.272$ MeV, its charge $+1$, the equality of its charge magnitude with the electron's, the integrality of that charge, its quark content, and its anomalous magnetic moment $g_p\approx5.586$ are all imports from standard physics. The framework represents an effective elementary proton; it does not derive one, and it cannot explain why the effective object exists.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, simple, of complex dimension four |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_x\vec e_y = \vec e_z$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors; $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; abelian (electric-charge) factor |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_{k=x,y,z}\vec e_k\partial/\partial Q_k$ | Biquaternionic gradient (Dirac operator), acting on the left |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R$ | The field, an element of $\mathbb{B}$; $\tilde{Ξ}^{\mathrm{sp}}_L$ the value L, $\tilde{Ξ}^{\mathrm{sp}}_R$ the value R, at the axis $\vec e_z$ |
| $\tilde{Ξ}^{\mathrm{sp}\flat}=-\tilde{Ξ}^{\mathrm{sp}*}$ | The algebra's real structure |
| $\tilde\Pi_\pm(\vec e_z)$ | The two chirality states at the axis; $\tilde\Pi_+$ the L state, $\tilde\Pi_-$ the R state |
| $Ϙ=\tfrac{ϙ_L+ϙ_R}{2}e_t+\tfrac{i}{2}(ϙ_L-ϙ_R)\vec e_z=ϙ_L\tilde\Pi_+(\vec e_z)+ϙ_R\tilde\Pi_-(\vec e_z)$ | The charge element, in $\mathbb{M}_+$; the charge is the right multiplication by it |
| $D_\mu\tilde{Ξ}^{\mathrm{sp}}=\partial\tilde{Ξ}^{\mathrm{sp}}/\partial Q_\mu+\tfrac{i}{\hbar}A_\mu\tilde{Ξ}^{\mathrm{sp}}Ϙ$ | Covariant derivative of the chiral charge |
| $ϙ_L, ϙ_R$ | Chiral couplings (real parameters); a massive field forces $ϙ_L=ϙ_R$ |
| $Ϙ=ϙ\,e_t$, $ϙ_p=+1$ | Vector-like charge element; the proton's value (inserted, not derived) |
| $m_p$ | Proton mass (a parameter) |
| $\tilde{P}=iE/c\,e_t+\vec p$ | Four-momentum; the mass shell is $\tilde{P}\tilde{P}^{\natural}=-m_p^2c^2$, that is $E^2=\lvert\vec p\rvert^2c^2+m_p^2c^4$ |
| $\mathbb{D}$, $\mathbb{D}^2=\Box$ | The pair operator of the two-sided equation $(\mathbb{D}-m_p)\tilde{Ξ}^{\mathrm{sp}}=0$; it carries the L value by $\tilde\nabla^{\natural}$ and the R value by $\tilde\nabla$ |
| $\Gamma=-iR_{\vec e_z}$ | The chirality cell, the cell that reads the two values; the legacy section writes it $\gamma_5$ |
| $\tilde J=i[\tilde{Ξ}^{\mathrm{sp}*}(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}})-(\tilde\nabla\tilde{Ξ}^{\mathrm{sp}*})\tilde{Ξ}^{\mathrm{sp}}]$ | The sesquilinear current of the field, an element of $\mathbb{M}_-$ (*Product and Form Conventions*) |
| $T_a=\tfrac12 e_a$ | Generators of $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}\subset\mathbb{M}_-$; $T_a^2=-\tfrac14e_t$, values $\pm\tfrac i2$ |
| $iT_a=\tfrac12 i e_a\in\mathbb{M}_+$ | $(iT_a)^2=+\tfrac14e_t$, values $\pm\tfrac12$; neither is the electric charge |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2^{*})=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | Inherited informational trace reading |
| $G_N=\sigma\exp(i\alpha)+\bar\sigma\exp(i\beta)$, $\sigma=\tilde\Pi_+(\vec\nu)$ | Nishijima's two-parameter group of the doubled Lanczos system |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the charge on each value of the field, the mass selection rule $ϙ_L=ϙ_R$, and the real-structure question that the separate pairing poses.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the biquaternion Dirac equation in its linear chiral-pair form, the mass term, and the mass-shell relation used here.
- [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) — the $\mathrm{SU}(2)$ generators $T_a=\tfrac12e_a$, their spectra, and the compact factor of the material sector whose distinction from the charge generator this article checks.
- [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) — the ceiling on the compact gauge algebra, the absence of a colour triplet and of confinement, and the three-way classification of what the framework reaches and what it does not.
- [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html) — the sibling accounting, in which charge and mass are likewise parameters, and the statement that nothing in the algebra fixes $|ϙ_e|=|ϙ_p|$.
- [The Spin–Statistics Theorem in Biquaternionic Form](the-spin-statistics-theorem-in-biquaternionic-form.html) — half-integer weights as native to the algebra, and the sense in which the spin–statistics theorem is transcribed rather than derived.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) — the two values of the field and the Lorentz action that fixes the spin-$\tfrac12$ content.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) — the abelian gauge group as the $*$-unitary part of the centre, on which the electric-charge identification rests.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html) — the spin operators $\tilde{S}_\mu=\tfrac\hbar2 i\vec e_\mu$ and the state structure used implicitly here.
- [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) — the real structure and the Majorana-versus-Dirac interpretation that bears on charge conservation.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the two sectors, their bases and the normalised Hermitian form, with its trace reading, inherited unchanged.
- [Conventions of the Operators and the Calculus](operator-and-calculus-conventions.html) — the pair operator $\mathbb{D}$, the square $\mathbb{D}^2=\Box$, and the one-operator reading of the massive equation, taken over unchanged.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html) — the algebra, the conjugations and the sector split in which the whole construction is set.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473, 474–483, 484–493 (arXiv:physics/0508002, physics/0508012, physics/0508013), for the coupled biquaternion system whose doubling is the isospin of the section *The Isospin Partner, and Why It Is Not in This Equation*.
- F. Gürsey, "Applications of Quaternions to Field Equations," PhD thesis, University of London, 1950, and "Relation of charge independence and baryon conservation to Pauli's transformation," *Nuovo Cimento* **7** (1958) 411–415, for the proton and neutron as the two superpositions of Lanczos's doubled system.
- K. Nishijima, "On the theory of leptons," *Nuovo Cimento* **5** (1957) 1349–1354, for the two-parameter group $G_N=\sigma \exp(i\alpha)+\bar{\sigma}\exp(i\beta)$ that leaves the proton and neutron superpositions intact.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §8, for the interpretation of Lanczos's doubling as isospin and for the explicit neutron construction $N=(\tilde Q_1\bar{\sigma}-\tilde Q_2^{*}\sigma)i\vec{\tau}$.
