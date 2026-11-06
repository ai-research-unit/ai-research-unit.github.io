# __The Neutron in Biquaternionic Form__

## Introduction

The neutron is the electrically neutral, spin-$\tfrac12$ baryon: in the Standard Model a bound colour-singlet composite of one up quark and two down quarks, with mass $m_n c^2 = 939.565$ MeV, magnetic moment $\mu_n = -1.9130427\,\mu_N$, mean lifetime about $880$ s, and baryon number one. All of these are measured facts, and standard physics accounts for them within the colour gauge theory and its bound states. This article asks a narrower question than *what is the neutron*: **which properties of the neutron does the biquaternion framework of this series reach, which does it merely represent, and which does it not reach at all?**

The answer is stated at the outset because the pull toward closure is strong. The framework supplies one field with two chiral parts and a Dirac equation on it, with a separate two-sided partner on the same algebra, so it can represent a neutral spin-$\tfrac12$ field; it gives each part its own charge, so it can state the neutron's neutrality as a constraint; and there it stops. The framework contains no colour group, no confinement mechanism, no three-dimensional internal space, no quark, and no bound-state construction. The neutron's **composite character is therefore not reached.** Its three-quark content, its colour singlet, its baryon number, its mass, its magnetic moment, and its lifetime are imported from standard physics, not derived here. That is a negative result, and it is the article's finding; it is written as such rather than padded.

A second honest point belongs here. The series takes the standing position that its predictions agree with standard physics because it is a **reformulation**, not a new theory. For the neutron that position is radical: nothing here distinguishes the framework's neutron from the Standard Model's, and the tree-level spin coupling it inherits gives a **zero** magnetic moment for a neutral structureless Dirac field, which is not the neutron. The neutron is exactly the object on which a colourless reformulation has nothing to say about structure, and the article records the boundary rather than crossing it.

## The Neutron as a Spin-$\tfrac12$ Biquaternion Field

The framework's carrier for any spin-$\tfrac12$ fermion is the algebra itself. The neutron field is an element

$$
\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}\in\mathbb{B},
$$

whose two parts carry the two values of the chirality, $\tilde{Ξ}_{\mathrm{sp},L}$ the value L and $\tilde{Ξ}_{\mathrm{sp},R}$ the value R, at the declared axis $\vec u$ (*Special Element Conventions*, §*The Chirality Convention*); every element of the algebra is such a field, and only the zero element has both parts zero. This article takes the axis $\vec u=\vec e_z$, the unit that the two-sided equation below multiplies the field by on the right. The free propagation of the field is the biquaternion Dirac equation. Two objects carry that name, and the companion article keeps them apart; the neutron uses the first. The **one-sided equation** is the chiral pair

$$
\begin{aligned}
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} &= m_n\,\tilde{Ξ}_{\mathrm{sp},L},\\[4pt]
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} &= m_n\,\tilde{Ξ}_{\mathrm{sp},R},
\end{aligned}
$$

with $m_n$ the neutron mass. The other, Kravchenko's **two-sided equation**, is a different operator, with the derivative and the mass on opposite sides; it is recorded in the subsection *The Two Dirac Equations, and Which One the Neutron Uses* below and is not used here. The norm-one elements of the algebra, $\langle\tilde U\rangle_{\natural}=e_t$, form $\mathrm{SL}(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group; the left multiplications act irreducibly on each part with weights $\pm\tfrac12$, and a rotation by $2\pi$ is the element $-e_t$. The representation-theoretic content of spin-$\tfrac12$ — half-integer weight, the double-valued rotation, Lorentz covariance — is inherited from the algebra, and in this sense the framework **represents** a spin-$\tfrac12$ field. Three qualifications are what the neutron actually tests, and the third of them has a partial answer.

**The representation is generic.** The algebra is simple, with one class of simple carrier, so every structureless spin-$\tfrac12$ field is an element of the same algebra with the same two values; the electron article records the same point, that the algebra contains no discriminator. The neutron is distinguished from the electron here only by the two numbers inserted into the equation, $m_n$ and the charge. Nothing in the algebra prefers these values, and nothing in it marks the field as the neutron rather than any other spin-$\tfrac12$ fermion of the same mass and charge.

**Spin-$\tfrac12$ is represented, not built.** In standard physics the neutron's spin-$\tfrac12$ is not fundamental: it is the total angular momentum of three spin-$\tfrac12$ constituents in a bound colour-singlet state, and the composite nature is what makes the spin assignment non-trivial (the naive three-quark spin coupling gives both $\tfrac12$ and $\tfrac32$; the observed ground state is $\tfrac12$). The algebra carries spin-$\tfrac12$ as a representation, but the framework contains no constituents and no composition rule, so it does **not** derive that the neutron's bound state has spin-$\tfrac12$. It represents the answer rather than producing it.

**The mass is a parameter, and the near-degeneracy with the proton is unexplained.** The free pair contains $m_n$ only as the common coefficient of the two mass terms, one per chirality; the framework is scale-free until that number is supplied, so the neutron mass is an input rather than a consequence. So is the fact that the neutron and proton masses agree to about $0.14\%$ ($m_n-m_p \approx 1.293$ MeV): in standard physics this near-degeneracy is the isospin symmetry of the strong interaction, an approximate flavour $SU(2)$ acting on the $(p,n)$ doublet. The framework does contain an $SU(2)$ — the span of $\vec e_x,\vec e_y,\vec e_z$ is $\mathfrak{su}(2)$ under the commutator, exponentiating to $\mathrm{SU}(2)$ — but that is the rotation/gauge algebra of the material sector, not flavour isospin, and identifying the two would be an import rather than a derivation. The framework supplies no second fermion with a nearly equal mass.

**Where the near-degeneracy does live, and its price.** The single-field equation of this article has no partner inside it. The doubled Lanczos system does. The companion article *The Proton in Biquaternionic Form* records Gürsey's construction in the section *The Isospin Partner, and Why It Is Not in This Equation*: from the Lanczos pair $\tilde\nabla\tilde Q_1=m\tilde Q_2$, $\tilde\nabla\tilde Q_2=m\tilde Q_1$, one forms the two superpositions

$$
\tilde{Ξ}_{\mathrm{sp},p}=\tilde Q_1\sigma+\tilde Q_2^{*}\bar{\sigma}, \qquad \tilde{Ξ}_{\mathrm{sp},n}=\left(\tilde Q_1\bar{\sigma}-\tilde Q_2^{*}\sigma\right)i\vec{\tau},
$$

with $\sigma=\tilde\Pi_+(\vec\nu)$ and $\bar\sigma=\tilde\Pi_-(\vec\nu)=e_t-\tilde\Pi_+(\vec\nu)$ the two complementary states along the unit direction $\vec\nu$, of zero product, $\sigma\bar\sigma=0$, and $\vec{\tau}$ a unit direction orthogonal to $\vec{\nu}$.

The group that preserves both forms is Nishijima's two-parameter group $G_N=\sigma\exp(i\alpha)+\bar\sigma\exp(i\beta)$, acting by right multiplication. Because the two states are complementary and of zero product, each term picks up its own phase and the other term dies,

$$
\tilde{Ξ}_{\mathrm{sp},p}\,G_N=e^{i\alpha}\tilde Q_1\sigma+e^{i\beta}\tilde Q_2^{*}\bar{\sigma},
\qquad
\tilde{Ξ}_{\mathrm{sp},n}\,G_N=e^{i\beta}\tilde Q_1\bar{\sigma}-e^{i\alpha}\tilde Q_2^{*}\sigma ,
$$

so the second superposition is preserved up to the same two phases before the trailing $i\vec{\tau}$ is applied. Equivalently, $\exp(-\vec{\nu}\alpha)\sigma=\sigma\exp(i\alpha)$ and $\exp(+\vec{\nu}\beta)\bar{\sigma}=\bar{\sigma}\exp(i\beta)$, since $\vec{\nu}^{2}=-e_t$ gives $\exp(\pm\vec{\nu}\theta)=\cos\theta\pm\vec{\nu}\sin\theta$. Each of the two states therefore carries its own abelian phase, and with it its own charge, while the form of both superpositions is unchanged.

A price is paid. The two parameters are independent on the superpositions, but the common mass links the two Lanczos fields. Read on those fields, the re-phasing is $\tilde Q_1\mapsto e^{i\alpha}\tilde Q_1$ and $\tilde Q_2\mapsto e^{-i\beta}\tilde Q_2$, the minus sign coming from the conjugation in $\tilde{Ξ}_{\mathrm{sp},p}$ and $\tilde{Ξ}_{\mathrm{sp},n}$. The first Lanczos equation then becomes $\tilde\nabla\bigl(e^{i\alpha}\tilde Q_1\bigr)=m\,e^{-i\beta}\tilde Q_2$, which is the original equation only when $\alpha+\beta=0$. So the doubled system with $m\neq0$ is invariant on that one line of the $(\alpha,\beta)$ plane, and the orthogonal combination is a symmetry of the superpositions' *form* alone. Two independent phases and one common mass therefore stand together only as a kinematic statement, which is the same phenomenon the charge section records below: a mass term, being a link between the two values, breaks the relative phase.

Two qualifications keep this from overturning the paragraph above. First, the isospin of that construction acts by **right** multiplication on $\tilde Q_1$, $\tilde Q_2$ of the doubled field, not by the left multiplication and commutator of the material sector's $\mathrm{SU}(2)$, so the two groups remain different objects. Second, the route doubles the field and still does not fix $m$. The precise statement is that the near-degeneracy is an **import in this equation** and a **structural feature of the doubled one**: this article uses the single-field equation, and that choice is why $m_n$ is a parameter here.

### The Two Dirac Equations, and Which One the Neutron Uses

The companion article separates two objects that both carry the name *Dirac equation*, and they must not be read as one. The neutron needs the separation stated once, because the two differ in which side of the field the derivative and the mass act.

**The one-sided equation** is the chiral pair displayed at the head of this section: the definition. The gradient acts by left multiplication on the element $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$, and the mass is the off-diagonal pair: each equation of the pair carries one value into the other. Chirality is the subscript, with the two values fixed above.

**The two-sided equation** is Kravchenko's dictionary form, a single equation on the element $F\in\mathbb{B}$, in the corpus's units $c=1$,

$$
\Bigl(i\frac{\partial}{\partial r'_t}+\nabla\Bigr)F-m_n\,i\,\bar{F}\,\vec e_z=0,
$$

with $\nabla$ the spatial gradient and the bar the coefficientwise complex conjugation, to be read apart from the Dirac adjoint. The time derivative and the gradient act on the left, the mass term on the right, through $\vec e_z$, and it carries the conjugation. On the material sector the left side is $-\tilde\nabla^{\natural}$, so the equation is $\tilde\nabla^{\natural}F=-m_n i\,\bar F\,\vec e_z$, which is the second member of the one-sided pair under $\tilde{Ξ}_{\mathrm{sp},L}=F$ and $\tilde{Ξ}_{\mathrm{sp},R}=-i\bar F\vec e_z$; that element carries the value R when $F$ carries L, checked on a hundred elements. That reading is not a change of basis: it is **antilinear**, because of the bar. The two operators are therefore distinct — one mass pairs the two values of one element, the other conjugates the element and multiplies it on the right — and they agree only on the solutions, through that antilinear reading.

| | One-sided equation | Two-sided equation |
|---|---|---|
| Equation | $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m_n\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m_n\tilde{Ξ}_{\mathrm{sp},R}$ | $\tilde\nabla^{\natural}F=-m_n i\,\bar F\,\vec e_z$ |
| Field | $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$, two values | $F\in\mathbb{B}$ |
| Derivative | left, by $\tilde\nabla$ and $\tilde\nabla^{\natural}$ | left, by $i\partial/\partial r'_t$ and $\nabla$ |
| Mass | the off-diagonal pair of the two values | right multiplication by $\vec e_z$, with $\bar F$ |
| Chirality | the value carried by each part | the unit $\vec e_z$ of the mass term |
| Status here | the definition, used throughout | quoted; not used |

The article uses the one-sided pair, because the spin content, the mass-shell relation and the charge of the next section are all read on the element. The two-sided form is quoted for one point that does matter here: its mass term multiplies on the right by $\vec e_z$, and the axis at which the two values of the chirality are read is that same $\vec e_z$. The mass acts on the right, the derivative on the left. Neither equation contains a second fermion, and neither fixes $m_n$.

## Neutrality and the Charge Operator

The neutron's charge is zero. Of the neutron's properties, neutrality looks like the one the framework might own, because the framework does have a charge. The chiral-fermion article gives each value its own charge: the L part is multiplied by $ϙ_L$ and the R part by $ϙ_R$,

$$
\tilde{Ξ}_{\mathrm{sp},L}\mapsto ϙ_L\tilde{Ξ}_{\mathrm{sp},L},\qquad \tilde{Ξ}_{\mathrm{sp},R}\mapsto ϙ_R\tilde{Ξ}_{\mathrm{sp},R},
$$

with independent chirality charges $ϙ_L,ϙ_R$ that the algebra does not fix: they are parameters, and the bare Dirac mass is gauge invariant if and only if $ϙ_L=ϙ_R$.

**The two rules are one right multiplication.** The action is $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} b$, by the element

$$
b \;=\; \tfrac{ϙ_L+ϙ_R}{2}\,e_t+\tfrac{i}{2}\left(ϙ_L-ϙ_R\right)\vec e_z \;\in\; \mathbb{B}_{\Psi} ,
$$

a derived form: $b=ϙ_L\tilde\Pi_+(\vec e_z)+ϙ_R\tilde\Pi_-(\vec e_z)$, the two chirality states at the axis of the previous section. The element $b$ is Hermitian; it is central only in the vector-like case $ϙ_L=ϙ_R$, where the action is also a left multiplication. That is why the parent's left-multiplied connection arises exactly for a vector-like fermion. The covariant derivative and its curvature carry the same element,

$$
D_\mu\tilde{Ξ}_{\mathrm{sp}}=\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial R_\mu}+\frac{i}{\hbar}A_\mu\,\tilde{Ξ}_{\mathrm{sp}} b,
\qquad
[D_\mu,D_\nu]\tilde{Ξ}_{\mathrm{sp}}=\frac{i}{\hbar}F_{\mu\nu}\,\tilde{Ξ}_{\mathrm{sp}} b
$$

for commuting potentials.

A single-particle state is an element of $\mathbb{B}$, and it is **neutral** when the charge gives it zero, $\tilde{Ξ}_{\mathrm{sp}} b=0$. The kernel is elementary and was recomputed exactly:

- If **both** $ϙ_L$ and $ϙ_R$ are nonzero, then $\tilde{Ξ}_{\mathrm{sp}} b=0$ only for $\tilde{Ξ}_{\mathrm{sp}}=0$: there is no nonzero neutral element.
- If $ϙ_L=0$ and $ϙ_R\neq0$, the neutral elements are those whose R part vanishes, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}$.
- If $ϙ_R=0$ and $ϙ_L\neq0$, the neutral elements are those whose L part vanishes, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},R}$.
- If $ϙ_L=ϙ_R=0$ every element is neutral (the trivially uncoupled case).

Neutrality is therefore not a generic property: it requires one of the two values to be uncoupled from the abelian charge. And, apart from the trivially uncoupled case $ϙ_L=ϙ_R=0$, the neutral element carries one value alone. On such an element the massive pair collapses: for $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}$ the first equation reads $0=m_n\tilde{Ξ}_{\mathrm{sp},L}$, so no nonzero neutral element solves it. The neutral single-particle state of the algebra therefore carries no Dirac mass in the pair. Whether it can carry a mass at all then rests on a Majorana-type coupling built on the algebra's real structure $\flat$, which pairs the field with its conjugate rather than with an opposite value, and whether the framework's real structure carries such a physical coupling is the open question inherited from the chiral-fermion article.

The framework therefore does not cleanly supply a **massive neutral spin-$\tfrac12$ single particle**: in the algebra, neutrality and the massive Dirac interpretation pull in opposite directions.

**Can a neutral composite be expressed?** The neutron is not a single element; it is a bound state of three fermions. The framework does have a many-particle construction: the Fock-space article builds the antisymmetric tensor algebra of the one-particle space, with creation and annihilation operators, so a three-fermion **state** is expressible in principle. But the three things the neutron needs are absent. First, **colour**: there is no three-dimensional internal space, and the carrier ceiling forbids a colour triplet, so any three constituents would be three excitations of one colourless species rather than three coloured quarks. Second, **binding**: the framework has no confinement mechanism and no bound-state construction, so nothing makes a three-particle state a neutron rather than a free scattering state, and there is no mass gap to hold it below threshold. Third, a **selection rule** fixing the constituent number three, the baryon number, and the spin-$\tfrac12$ of the bound state: none is supplied. The charge is defined on one element; a total charge on the Fock space would be its additive second-quantized sum, but the corpus does not construct it, and even granting it, the resulting neutrality condition would fix a relation among unfixed charges rather than a value. If one imposes the additive condition on three constituents, neutrality reads

$$
\boxed{\;n_L\,ϙ_L + n_R\,ϙ_R = 0, \qquad n_L+n_R = 3\;},
$$

which has solutions for special charge ratios (for instance $(n_L,n_R)=(1,2)$ requires $ϙ_R=-\tfrac12 ϙ_L$), but nothing in the framework fixes $ϙ_L$ or $ϙ_R$, and the standard quark charges are not framework objects. Reading the quark charges $\tfrac23,-\tfrac13,-\tfrac13$ into the three constituents would be exactly the manufacture of the neutrality from an imported quark model, and this article does not do it.

**Verdict.** The framework's charge operator can *state* the neutron's neutrality as the constraint $\tilde{Ξ}_{\mathrm{sp}} b=0$, and it classifies the single-particle solutions of that constraint; a neutral many-particle **state** is not ruled out in principle once a Fock space and an additive total charge are granted. But the neutron as a **bound colour-singlet composite** is not expressible: colour, confinement, and the selection rule that fixes three constituents are all absent. And the neutrality is not *derived*, because the framework contains no constituents whose charges could sum to zero. The honest sentence is: **neutrality is expressible as a constraint on unfixed charges, a neutral bound composite is not expressible, and the neutrality itself is imported from standard physics.** That is a negative result, and it is reported as one.

## Composite Character: No Colour, No Confinement, No Constituents

The reason the bound composite is unavailable is structural, and the QCD research agenda of this series states it precisely. Three of its established findings carry over unchanged.

**No colour group.** The compact algebra available inside $\mathbb{B}$ under the commutator is at most $\mathrm{U}(2)=\mathrm{U}(1)\oplus\mathrm{SU}(2)$, of real dimension four: $\mathbb{B}_{\Phi}$ decomposes as a Lie algebra into $\mathbb{R}(ie_t)\oplus\mathrm{su}(2)$. No $\mathrm{SU}(3)$ subalgebra is available, and the three quaternion units $\vec e_x,\vec e_y,\vec e_z$ span the *adjoint* of $\mathrm{SU}(2)$, not a complex triplet. Counting three basis vectors is not constructing colour.

**No three-dimensional carrier.** The algebra $\mathbb{B}$ is simple, so every carrier is a sum of copies of the unique simple one, of complex dimension two: every carrier has complex dimension $2k$. A colour triplet — a three-complex-dimensional internal space for a quark — is not a carrier of $\mathbb{B}$. The ceiling is a statement about the carrier, not about the arithmetic.

**No confinement.** The framework has no non-perturbative formulation, no Wilson loop, no gauge-invariant regulator, no gauge-fixing principle, and no mass gap; the agenda records confinement as an obstacle with **no mechanism proposed**, not merely an unproven one.

Consequently the neutron's defining structural facts — baryon number one, three constituent quarks, a colour singlet, a bound state with a mass gap above it — lie outside the framework. The framework cannot say what the neutron is made of, and it cannot explain why a colourless composite of charged constituents exists at all. Its own closest apparatus is the zero-divisor cone of $\mathbb{B}_{\Phi}$ and the non-abelian curvature it does contain, neither of which is a confinement mechanism. On the fermion-number question the framework is also not equipped: the parent's linear mass conserves the vector $\mathrm{U}(1)$, while the separate Majorana-type coupling built on the real structure $\flat$ reduces a continuous fermion-number phase to a sign on that interpretation; neither supplies the quark model's baryon number as a conserved $\mathrm{U}(1)$.

The composite character is thus not a gap of the article; it is the framework's boundary. What is left, for the neutron, is a representation of a structureless spin-$\tfrac12$ field with two inserted parameters and a neutrality constraint — and, as the next section shows, even the most basic measured consequence of compositeness falls outside it.

## The Magnetic Moment: A Neutral Field with a Nonzero Moment

The electron article derives, from the $1/2m$ coefficient produced by the Dirac equation under minimal coupling, the tree-level gyromagnetic relation $\vec\mu = (g ϙ/2m)\vec S$ with $g=2$. Applied to a **neutral** structureless Dirac fermion the same treatment gives

$$
\boxed{\;\vec\mu \;=\; \frac{g\,ϙ}{2m}\,\vec S \;=\; 0 \qquad (ϙ=0)\;},
$$

for any $g$: a neutral point Dirac fermion has no magnetic moment. The measured neutron moment is

$$
\mu_n \;=\; -1.9130427\,\mu_N \;\neq\; 0,
$$

and its sign is negative. The nonzero value is direct evidence that the neutron is not structureless; in standard physics it arises from the charged quarks and their spin and orbital motion inside the colour-singlet bound state. The framework has neither the charged constituents nor the binding, so it cannot supply the moment, and its tree-level spin prediction is not merely incomplete on the neutron — read as a neutral point Dirac field it is **zero, against a measured number of order one in nuclear magnetons**. This is the sharpest place in the article where a framework statement meets a neutron measurement and does not match, and it matches the composite conclusion of the preceding section rather than contradicting it: the neutron is precisely the object for which the framework's structureless Dirac description is quantitatively wrong.

The same boundary shows in the neutron's decay. The free neutron beta-decays with a mean lifetime of about $880$ s; the decay is a weak-interaction process, and the framework contains no weak chiral gauge structure — its centre is vector-like, and the chiral-fermion article records that a chiral gauge group is not derived. The lifetime is therefore outside the framework, as is the isospin near-degeneracy with the proton noted above. The mechanism by which a coupling becomes a lifetime — the complex energy pole of an unstable state and its width — is treated in *The Unstable State and the Complex Energy Pole in Biquaternionic Form*; what the framework lacks is the weak coupling itself, not the mechanism.

## Accounting: Derived, Represented, Outside

The article's finding is best stated as a ledger, in the manner of the electron article. Each row is a property of the neutron, its status in the framework, and where the content actually comes from.

| Neutron property | Status | Object or reason |
|---|---|---|
| Spin-$\tfrac12$ representation content (generic) | Derived (framework), not neutron-specific | the element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$; the left multiplications act on each part with weights $\pm\tfrac12$ |
| Free Dirac kinematics, mass-shell relation | Derived (framework) | biquaternion Dirac equation, one-sided chiral pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=m_n\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m_n\tilde{Ξ}_{\mathrm{sp},R}$ |
| Neutrality constraint $\tilde{Ξ}_{\mathrm{sp}} b=0$ and its kernel | Derived (framework) | the charge $b=ϙ_L\tilde\Pi_+(\vec e_z)+ϙ_R\tilde\Pi_-(\vec e_z)$; no nonzero neutral element unless one charge vanishes |
| Mass value $m_n$ | Represented | parameter of the equation; not derived |
| Charge value $0$ | Represented | a constraint/parameter; not derived from quark charges |
| The identification "*this* field is the neutron" | Represented | the inserted mass and charge |
| Composite character: three quarks, colour singlet | **Outside** | no colour group, no three-dimensional carrier, no constituents |
| Confinement and the bound-state mass gap | **Outside** | no mechanism, no non-perturbative apparatus |
| Baryon number | **Outside** | not a framework quantum number |
| Magnetic moment $\mu_n\neq0$ | **Outside** | measured; the framework's neutral Dirac value is $0$ |
| Lifetime / beta decay | **Outside** | no weak chiral gauge structure |
| Isospin; $p$–$n$ near-degeneracy | **Outside** | approximate flavour $SU(2)$ not derived; the framework's $SU(2)$ is the sector's rotation algebra |
| Any discriminator from another spin-$\tfrac12$ field | **Outside** | the algebra contains none |

The table separates two kinds of statement that are easily run together. The framework *does* derive a spin-$\tfrac12$ representation and a charge; the neutron *does* carry that representation and *does* satisfy the neutrality constraint for a suitable, unfixed charge assignment. But none of that is specific to the neutron, and none of it reaches the properties that make the neutron a neutron. The derived rows are generic fermion structure; the neutron-specific rows are either inserted or outside.

## The Gaps, Named

Three gaps are structural and cannot be closed by better notation. First, **colour**: nothing in the series derives $SU(3)$ or any three-valued internal structure, and the carrier ceiling makes a colour triplet impossible within the present carrier. Second, **confinement**: no mechanism has been proposed, so the existence of the neutron as a bound colour singlet is not accounted for. Third, **the composite**: the framework has no multi-fermion bound-state construction, so even granting colour it could not assemble the neutron. These are the framework's boundary, and the QCD agenda's three-way classification places them there.

Two further gaps are the article's own, and they are narrower. The **neutrality is a constraint, not a derivation**: the charge operator can be set to zero, but the framework supplies neither the charge values nor the constituents whose charges must cancel, and the standard quark charges are an input the framework does not contain. And the **magnetic moment is a counterexample, not a confirmation**: a neutral structureless Dirac field has zero moment, while the neutron's is nonzero, so the framework's one quantitative spin statement does not describe the neutron at all.

Finally, the standing **empirical-contact** gap applies with full force. Nothing here distinguishes the framework's neutron from the Standard Model's, because the framework reaches only the generic fermion structure they share; the neutron-specific content is imported. The article therefore makes no prediction, claims no prediction, and leaves the neutron's structure exactly where standard physics found it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are the frame cells of the body written as letters, and this section is the only place in the article where they appear: every section above is written in cells.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

**Every $i$ in that display is the central scalar, $i^{2}=-1$, and it is what fixes the signs.** Since $L_{\mathrm{pau},e_t}$ is the identity, two of the five collapse to a one-sided multiplier, $\gamma_0=iR_{\mathrm{pau},\vec e_x}$ and $\gamma_5=-iR_{\mathrm{pau},\vec e_z}$. A gamma is one product, and each of its multipliers squares to the minus of $\vec e^{2}=-e_t$, so

$$
\gamma_0^{2}=i^{2}(R_{\mathrm{pau},\vec e_x})^{2}=(-1)(-I_4)=I_4,
\qquad
\gamma_k^{2}=i^{2}(L_{\mathrm{pau},\vec e_k})^{2}(R_{\mathrm{pau},\vec e_y})^{2}=(-1)(-I_4)(-I_4)=-I_4\quad(k=1,2,3).
$$

In the axis-free display:

$$
\gamma_0^{2}=i^{2}(R_{\mathrm{axf},\vec e_x})^{2}=(-1)(-I_4)=I_4,
\qquad
\gamma_k^{2}=i^{2}(L_{\mathrm{axf},\vec e_k})^{2}(R_{\mathrm{axf},\vec e_y})^{2}=(-1)(-I_4)(-I_4)=-I_4\quad(k=1,2,3).
$$

The time gamma has one multiplier, and its minus cancels $i^{2}=-1$; the spatial gammas have two, whose two minus signs multiply to $+I_4$ and leave $i^{2}=-1$ standing. The products of distinct gammas anticommute, so the frame obeys $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$ with $\varepsilon=(1,-1,-1,-1)$.

The fifth gamma is not a fifth frame vector but their product. The four defining $i$'s contribute $i^{4}=1$ and the cells contribute $\gamma_0\gamma_1\gamma_2\gamma_3=-R_{\mathrm{pau},\vec e_z}$, so

$$
i\,\gamma_0\gamma_1\gamma_2\gamma_3 \;=\; -iR_{\mathrm{pau},\vec e_z} \;=\; \gamma_5 ,
$$

The same identities in the axis-free display:

$$
i\,\gamma_0\gamma_1\gamma_2\gamma_3 \;=\; -iR_{\mathrm{axf},\vec e_z} \;=\; \gamma_5 ,
$$

the chirality cell of the neutrality section.

**The charge operator in gammas.** With $\gamma_5=P_R-P_L$ the two projectors read $P_L=\tfrac12(I_4-\gamma_5)$ and $P_R=\tfrac12(I_4+\gamma_5)$, so $Ϙ=ϙ_LP_L+ϙ_RP_R$ is diagonal in the gamma grading and the neutrality constraint $Ϙ\tilde{Ξ}_{\mathrm{sp}}=0$ is the statement that the neutral state lies in one chirality eigenspace of $\gamma_5$.

Two objects must not be confused here. $\gamma_5$ is the reference-frame cell of the chirality $\Gamma=-iR_{\mathrm{pau},\vec e_z}$. The central grading is $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, with $\tilde{Ζ}_{\mathrm{ad}}$ the central root of $-e_t$, so that $\xi^{2}=i^{2}\tilde{Ζ}_{\mathrm{ad}}^{2}=(-1)(-e_t)=e_t$; $\xi$ is also the difference $e_+-e_-$ of the two central idempotents. It is a different object, central and not an element of $\mathbb{B}$, and $\gamma_5$ is only its representative on the Dirac module.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The neutron is an electrically neutral spin-$\tfrac12$ baryon, and in the biquaternion framework of this series it is represented as an element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$ satisfying the linear chiral mass pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m_n\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m_n\tilde{Ξ}_{\mathrm{sp},R}$. That pair is the one-sided form, the definition; Kravchenko's two-sided equation writes the derivative on the left and the mass on the right through $\vec e_z$, and it is a different operator, quoted here but not used.

That representation is generic: the algebra carries any structureless spin-$\tfrac12$ field by the same two values, and the spin-$\tfrac12$ it supplies is a representation, not a construction from constituents.

The charge multiplies the two values by $ϙ_L$ and $ϙ_R$; the two rules are one right multiplication by the element $b=ϙ_L\tilde\Pi_+(\vec e_z)+ϙ_R\tilde\Pi_-(\vec e_z)\in\mathbb{B}_{\Psi}$. The neutrality constraint $\tilde{Ξ}_{\mathrm{sp}} b=0$ has a nonzero solution only if one value is uncoupled ($ϙ_L=0$ or $ϙ_R=0$), and, apart from the trivially uncoupled case $ϙ_L=ϙ_R=0$, the neutral element carries one value alone; the massive pair then forces it to vanish, so it is massless in the Dirac pair, and whether it can carry a mass depends on a Majorana-type coupling on the algebra's real structure $\flat$, whose interpretation is open.

The framework does have a Fock space, so a neutral many-particle **state** is not ruled out in principle. But no neutral **bound composite** is expressible: there is no colour, no confinement, no binding, and no selection rule fixing three constituents. The neutrality is therefore stateable as a constraint on unfixed charges but not derived, and manufacturing it from the standard quark charges would be an import.

The neutron's composite character is not reached. The framework has no colour group (the compact algebra is at most $\mathrm{U}(2)$, of dimension four), no three-dimensional carrier (every carrier of $\mathbb{B}$ has even complex dimension), no confinement mechanism, and no bound-state construction; its baryon number, mass, lifetime, and isospin are not derived here. Its magnetic moment is the sharp quantitative case: a neutral structureless Dirac field has $\mu=0$, while $\mu_n=-1.9130427\,\mu_N$, so the framework's tree-level spin statement does not describe the neutron. The honest summary is that the framework reaches the neutron's neutrality as a constraint and its spin as a generic representation, and reaches nothing of what makes it a composite baryon.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, simple, of complex dimension four |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors; $\mathbb{B}=\mathbb{B}_{\Phi}\oplus\mathbb{B}_{\Psi}$ |
| $\tilde{\nabla}$ | Biquaternionic gradient, the Dirac operator, acting on the left |
| $\nabla$, $Q_t=i c r'_t$ | Spatial gradient; imaginary time of the material sector |
| $\Box$ | d'Alembertian, the quaternionic norm of the gradient |
| $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ | The field, an element of $\mathbb{B}$; $\tilde{Ξ}_{\mathrm{sp},L}$ the value L, $\tilde{Ξ}_{\mathrm{sp},R}$ the value R, at the axis $\vec e_z$ |
| $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$ | The algebra's real structure |
| $\tilde\Pi_\pm(\vec e_z)$ | The two states at the axis; $\tilde\Pi_+$ the L state, $\tilde\Pi_-$ the R state |
| $b=ϙ_L\tilde\Pi_++ϙ_R\tilde\Pi_-=\tfrac{ϙ_L+ϙ_R}{2}e_t+\tfrac{i}{2}(ϙ_L-ϙ_R)\vec e_z$ | The charge element, in $\mathbb{B}_{\Psi}$; the charge is the right multiplication by $b$ |
| $D_\mu\tilde{Ξ}_{\mathrm{sp}}=\partial\tilde{Ξ}_{\mathrm{sp}}/\partial R_\mu+\tfrac{i}{\hbar}A_\mu\tilde{Ξ}_{\mathrm{sp}} b$ | Covariant derivative of the chiral charge; the curvature is $\tfrac{i}{\hbar}F_{\mu\nu}\tilde{Ξ}_{\mathrm{sp}} b$ |
| $\tilde{Ξ}_{\mathrm{sp}} b=0$ | Neutrality constraint; no nonzero solution unless $ϙ_L=0$ or $ϙ_R=0$ |
| $(i\partial/\partial r'_t+\nabla)F-m_n i\,\bar F\,\vec e_z=0$ | Kravchenko's two-sided equation, $F\in\mathbb{B}$; the bar is the coefficientwise conjugation |
| $\gamma_\mu[\mathbb{B}_{\Phi}]$, $\gamma_5$ | The gamma frame of the legacy section; used only in §*The Legacy Pauli Gamma Formulation* |
| $G_N = \sigma\exp(i\alpha)+\bar{\sigma}\exp(i\beta)$, $\sigma=\tilde\Pi_+(\vec\nu)$ | Nishijima's two-parameter group of the doubled Lanczos system |
| $\mathrm{U}(2)=\mathrm{U}(1)\oplus\mathrm{SU}(2)$ | Maximal compact algebra in $\mathbb{B}$; dimension $4$ |
| $m_n$, $\mu_n = -1.9130427\,\mu_N$ | Neutron mass (input) and measured magnetic moment (outside) |
| $SU(3)$, quark | Standard-model notation, not framework objects |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html) — the sibling accounting for a fundamental spin-$\tfrac12$ fermion, and the source of the tree-level $g=2$ relation used here to show that a neutral structureless Dirac field has zero magnetic moment.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the biquaternion Dirac equation, its mass term, plane-wave solutions, and the mass-shell relation used throughout.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the two chiral parts, the charge on each part, the mass selection rule, and the real structure whose interpretation is left open here.
- [The Proton in Biquaternionic Form](the-proton-in-biquaternionic-form.html) — the charged partner, the isospin section from which the Gürsey construction above is quoted, and the single-field equation this article shares.
- [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html) — the many-particle space (the antisymmetric tensor algebra of the one-particle space) and its operators, the construction that lets a three-fermion *state* be written while supplying no binding.
- [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) — the established ceiling on the colour group, the absent confinement mechanism, and the three-way classification the composite section inherits.
- [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) — the compact gauge algebra inside $\mathbb{B}_{\Phi}$ and the non-abelian machinery that stops short of colour.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) — the sector decomposition, the four-vectors, and the $i c r'_t$ convention.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the Hermitian sector, the rotor action, and the trace formula.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html) — the algebra, the two sectors, the frame constants, and the open many-particle extension on which a composite construction would depend.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) — the Lorentz action on the field and the representation on which the spin-$\tfrac12$ content rests.
- *Spin-$\tfrac12$ Quantum Physics in Biquaternionic Form* — the qubit/operator dictionary and the trace formula applied to spin states.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html) — the spin observables and their algebra, used here only as the generic spin structure the neutron inherits.
- [The Spin–Statistics Theorem in Biquaternionic Form](the-spin-statistics-theorem-in-biquaternionic-form.html) — why the neutron, as a spin-$\tfrac12$ fermion, obeys Fermi–Dirac statistics, another generic rather than neutron-specific consequence.
- [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html) — the equal-time anticommutators, the mode expansion, and the field's quantization, the fermionic setting in which the neutron would have to be a state.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, for the two-sided biquaternionic Dirac equation with the conjugation in the mass term, the form quoted in *The Two Dirac Equations, and Which One the Neutron Uses*.
- F. Gürsey, "Relation of charge independence and baryon conservation to Pauli's transformation," *Nuovo Cimento* **7** (1958) 411–415, and K. Nishijima, "On the theory of leptons," *Nuovo Cimento* **5** (1957) 1349–1354, for the neutron as the second superposition of Lanczos's doubled system, and for the two-parameter group $G_N=\sigma \exp(i\alpha)+\bar{\sigma}\exp(i\beta)$ under which the proton and neutron superpositions keep their form while the two states take independent phases.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §8, for the relation of the doubled Lanczos system to isospin and for the neutron construction $\tilde{Ξ}_{\mathrm{sp},n}=(\tilde Q_1\bar{\sigma}-\tilde Q_2^{*}\sigma)i\vec{\tau}$, written $N$ there.
