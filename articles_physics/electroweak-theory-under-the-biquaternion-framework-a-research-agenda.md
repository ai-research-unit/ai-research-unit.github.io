# __Electroweak Theory under the Biquaternion Framework — A Research Agenda__

## Introduction

**Electroweak theory** is the gauge theory of the weak and electromagnetic interactions: a gauge theory with group $SU(2)_L \times \mathrm{U}(1)_Y$, matter in **chiral** representations — left-handed quarks and leptons in $SU(2)_L$ doublets and their right-handed partners in singlets — a scalar doublet whose vacuum expectation value breaks the symmetry to the electromagnetic $\mathrm{U}(1)$, and massive $W^\pm$ and $Z$ bosons alongside the massless photon. Two features are structural rather than incidental. The gauge group acts *inequivalently* on the two chiralities, so no bare fermion mass is gauge invariant; and the fermion masses exist only because of the scalar sector, whose vacuum expectation value carries the charge the mass term lacks. This article is a research agenda for electroweak theory inside the biquaternion framework. Its subject is not a result; it is the boundary between what the framework has built and what electroweak theory requires.

The starting position is stated at the outset, because the whole agenda depends on it and because it is easy to overstate.

- **The framework has an abelian gauge principle.** It has a canonical central $\mathrm{U}(1)$, a connection, a transformation law, a covariant derivative, and a curvature, together with the statement that the framework cannot fix the gauge. This is established and is recalled in the next section.
- **The framework has a non-abelian gauge field construction, and the algebra it needs is present.** The material sector decomposes as a Lie algebra, $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, so the compact algebra available is $\mathrm{U}(1)\oplus\mathrm{SU}(2)=\mathrm{U}(2)$, of real dimension four. That is exactly the dimension count of the electroweak gauge group. It supplies the **algebra** of a non-abelian gauge theory. It does **not** supply a **chiral** gauge theory, and the two are different objects.
- **The framework has not constructed the electroweak sector.** Nothing derives weak hypercharge; no chiral non-abelian matter representation is built; there is no scalar sector, no symmetry breaking, and no Yukawa coupling; and the framework's inability to fix the gauge bounds the physical content of any orbit.

The word "electroweak" occurs in the corpus only where standard theory is being named or imported. *The Dirac Equation in Biquaternionic Form* states that the framework "does not by itself derive the mass term or the electroweak structure". *The CPT Theorem in Biquaternionic Form* records the electroweak relevance of the discrete operations $C$ and $P$ and says plainly that it "is imported". *The Neutrino and Majorana Fermions in Biquaternionic Form* names a dimension-five operator arising "after electroweak symmetry breaking" as something the framework does not represent. No article constructs $SU(2)_L\times \mathrm{U}(1)_Y$, derives a hypercharge assignment, a Higgs doublet, or a $W$ or $Z$ field.

The discipline this forces on the article is the one the genre requires: **an agenda that quietly assumes hypercharge or chirality has fabricated its own premise.** Both are therefore carried as **open items throughout**, never as working assumptions. Wherever a standard electroweak statement is written down — the group, the hypercharge values, the Weinberg angle, the Higgs doublet, the $W$ and $Z$ masses — it is flagged as standard input, not as a framework result.

**One notation, and the one operator that differentiates.** The algebra's own objects are written as elements — $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{A}_{\Phi}$, $\mathcal{A}_\mu$ — and an action is named by the element it uses and the side it uses it on, so that no glyph names a side: the left action is $\tilde{Ξ}_{\mathrm{sp}}\mapsto b\tilde{Ξ}_{\mathrm{sp}}$, the right action is $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} b$, and the side is read off the position of $b$. The only operator that differentiates is the biquaternionic gradient $\tilde\nabla_\Phi$ of *Operator and Calculus Conventions*, §*The Gradient*, used unchanged throughout, with the d'Alembertian $\Box$ of the same section for its two-derivative form; no other letter stands for a gradient, and none is introduced. Chirality is a side; the basis operator that shows it on the frame is the fifth basis operator, a pure right multiplier, and on an element it is the subscript of two values, $L$ and $R$ (*Special Element Conventions*, §*The Chirality Convention*); the mass bilinear and the axial current are read through single elements on the right, and every section that uses them writes the product out. The legacy frame display of *Matrix Representations Conventions* is a dictionary for the same algebra and is not used in this article. Every factor of $i$ in a product is spent with $i^2=-1$.

**The three-way classification.** The article sorts every item into one of three categories, and the distinction is the point of the agenda.

1. **Established.**
2. **Obstacle with a known route.** The object does not exist, but the route to it is identifiable, usually because standard field theory supplies the computation and the framework must reproduce it on its own carrier, or because the object can be built on a declared carrier at the cost of leaving the framework's own construction.
3. **Obstacle with no route yet.** No mechanism has been proposed, and naming an object is not the same as having a route to it. The hypercharge values and a gauge-fixing principle are in this class.

The four obstacles the agenda treats are the **chiral-fermion obstacle** (the framework's non-abelian construction is vector-like on the field), **weak hypercharge** (nothing derives it), the **scalar sector and symmetry breaking** (needed for masses, not available), and the **inability to fix the gauge** (which bounds the physical content of any orbit). They are not independent: the scalar sector needs the chiral action and the hypercharge assignments, and every physical statement about masses needs a gauge fixing. A closing ledger collects them, and a short synthesis names the upstream items.

## What the Framework Already Reaches

### The abelian gauge principle

The read-list article *The Gauge Principle in Biquaternionic Form* derives the abelian gauge structure from the centre of the algebra. Its results are established and are used here unchanged.

The centre is $\mathbb{B}_{C} = \mathrm{span}_\mathbb{R}\{e_t, ie_t\}$, and its $*$-unitary part is $\mathrm{U}(1) = \{\exp(i\theta)\}$. A constant central phase is a symmetry of the massless biquaternion field equation, because a central constant passes through the gradient. Localizing it, $\lambda(\tilde{Q}) = \exp(\frac{i\,ϙ\,\Gamma\,\tilde{Q}}{\hbar})$ with real $\Gamma$, forces a connection $\tilde{A}_{\Phi}$ with the transformation law

$$
\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde\nabla_\Phi\Gamma,
$$

under which the field equation is gauge covariant. Its covariant derivative is the $\tilde D$ of *Algebra and Element Conventions*, read with $\tilde A_{\Phi}$ for its connection, and it acts on the left as $\tilde\nabla_\Phi$ does, so the abelian structure is one-sided throughout and no side hides in its letters. Its component is $D_\mu$, the curvature is the abelian $F_{\mu\nu} = \partial/\partial R_\mu A_\nu - \partial/\partial R_\nu A_\mu$, with $[D_\mu,D_\nu] =\frac{i\,ϙ}{\hbar}F_{\mu\nu}$, and a real gauge function keeps $\tilde{A}_{\Phi}$ in the material sector $\mathbb{B}_{\Phi}$. The coupling $ϙ$ is a parameter: the algebra does not fix its value.

Two inherited facts bear directly on this agenda. First, the **gauge group is canonically attached**: it is the $*$-unitary part of the centre, and no choice is made in selecting it. Second, the **mass term is linear and passes the continuous central phase**: the framework's Dirac mass is the linear chiral pair $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $(\tilde\nabla^{\natural})_\Phi\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$, so the vector $\mathrm{U}(1)$ is conserved for the massive field and the broken symmetry is the axial one. The algebra's anti-linear object is the real structure $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$: because $\flat$ is anti-linear, $(\lambda\tilde{Ξ}_{\mathrm{sp}})^{\flat} = \lambda^{*}\tilde{Ξ}_{\mathrm{sp}}^{\flat}$, so a conjugate coupling built on it would survive the continuous central phase only for real $\lambda$, i.e. only $\lambda = \pm 1$ — a discrete $\mathbb{Z}_2$, not the continuous $\mathrm{U}(1)$. Whether the framework deploys such a coupling is the open Majorana interpretation. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

Finally, the same article and its parents record the negative fact that the framework **cannot fix the gauge**. That fact is treated here as an obstacle in its own right, because every statement about a massive vector spectrum is normally a statement in a fixed gauge.

### The non-abelian construction, and the algebra it runs on

The read-list article *Non-Abelian Gauge Fields in Biquaternionic Form* builds the general non-abelian gauge structure inside $\mathbb{B}$. Its results are established and are used here unchanged.

The vector part of the material sector closes under the commutator and is $\mathrm{SU}(2)$ in a non-standard normalization,

$$
[e_a,e_b] = 2\,\varepsilon_{abc}\,e_c, \qquad
T_a = \tfrac12 e_a,\quad [T_a,T_b] = \varepsilon_{abc}T_c,\quad \mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab},
$$

and the material sector decomposes as a direct sum of Lie algebras,

$$
\boxed{\;\mathbb{B}_{\Phi} \;=\; \mathbb{R}(ie_t) \;\oplus\; \mathrm{SU}(2),
\qquad\text{so the compact algebra available is}\qquad
\mathrm{U}(2) = \mathrm{U}(1)\oplus\mathrm{SU}(2),\quad \dim_\mathbb{R} = 4\;}.
$$

This is the read-list article's central algebraic result, and it is the reason the electroweak question can be posed at all: the compact algebra of dimension four that electroweak theory uses is *already present in the material sector*, not adjoined. What is not present is the way electroweak theory uses it. The gauge group of the construction is the unit real quaternions, $SU(2) = \{\tilde U \in \mathbb{B}_{H} : \tilde U\bar{\tilde U} = e_t\}$, acting on a matter field **by left multiplication**. The connection transforms as

$$
\mathcal{A}_{2,\mu} = \tilde U\,\mathcal{A}_\mu\,\tilde U^{-1} + \frac{i}{\kappa}\,(\partial/\partial R_\mu \tilde U)\,\tilde U^{-1}.
$$

The curvature is

$$
F_{\mu\nu} = \partial/\partial R_\mu\,\mathcal{A}_\nu - \partial/\partial R_\nu\,\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu].
$$

It transforms in the adjoint, $F_{2,\mu\nu} = \tilde UF_{\mu\nu}\tilde U^{-1}$, satisfies the Bianchi identity, and admits the gauge-invariant density $-\tfrac12\mathrm{Tr}\bigl(\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}\bigr)$, a plain sum: the metric is carried by the index positions and by the reality classes of the components, so an explicit $\varepsilon_\mu\varepsilon_\nu$ would apply it a second time.

Two gaps of this construction are inherited and matter here. The first is the **matter representation**: the covariant derivative acts by left multiplication, the representation carried by the matter field is not specified, and the non-abelian version of the chiral charge operator is not constructed (the read-list article's open question 3). The second is the **reality class of the connection**: no single Hermitian-conjugation eigenspace is gauge invariant across all four components, because the $i r'_t$ derivative $\partial/\partial R_t = -i\partial/\partial r'_t$ flips the conjugation behaviour of the Maurer–Cartan form in the time direction. A consistent mixed assignment exists — $\mathcal{A}_0$ anti-Hermitian traceless in $\mathrm{SU}(2)\subset\mathbb{B}_{\Phi}$, $\mathcal{A}_k$ Hermitian traceless in $i\,\mathrm{SU}(2)\subset\mathbb{B}_{\Psi}$ — but whether it is the intended physical assignment is not settled.

For the purposes of this agenda, the construction is the **general machinery of a non-abelian gauge theory on $\mathrm{U}(2)$**. The dimension of that algebra matches the dimension of the electroweak gauge algebra, and the match is a coincidence of counting, not an identification. The identification fails in two ways that the rest of the article makes precise: the $\mathrm{SU}(2)$ here acts on matter by left multiplication, which is vector-like; and the $\mathrm{U}(1)$ here is the centre, whose action is scalar, which is also vector-like. Weak isospin and weak hypercharge are both chiral.

### The chiral structure: two values on one element

The read-list article *Chiral Fermions in the Biquaternion Framework* establishes the following, and this agenda inherits it without change.

The field is one element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$, and its chirality is a side: $\mathsf{V}_{\mathrm{vol}}=-iR_{\vec e_z}$ is a pure right multiplier, so it is an example of the right slot and the side is what the label records (*Special Element Conventions*, §*The Chirality Convention*). On the element the basis operator does one thing: it gives the subscript its two values, $L$ for the minus value and $R$ for the plus value, so that the field is the sum of its two parts,

$$
\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R},
$$

and only the zero element is both. That is the whole of the chirality. Everything else in this section is read off from it by two laws of the subscript — **a product takes the letter of its right factor, and left multiplication keeps the letter** (*Matrix Representations Conventions*, §*The Legacy Pauli Gamma Formulation*) — together with one law of the units: right multiplication by $\vec e_t$ or by $\vec e_z$ keeps the letter, and right multiplication by $\vec e_x$ or by $\vec e_y$ exchanges the two.

**The letters are constants of the equation.** The Lorentz action on the field multiplies on the left, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde U_{\mathrm{lor}}\tilde{Ξ}_{\mathrm{sp}}$, and a left multiplication keeps the letter. The chirality multiplies on the right, and right multiplications commute with left multiplications; so the basis operator commutes with every left multiplier, the gradient among them, and the two values are conserved by the free equation.

**The mass bilinear is mixed.** The Dirac mass bilinear is the scalar part of an element product built on the time-like unit,

$$
B=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}i\tilde{Ξ}_{\mathrm{sp}}\vec e_x\bigr),
$$

and both of its properties follow from the letter law. Right multiplication by $\vec e_x$ exchanges the two letters, so $B$ pairs each part with the other and not a part with itself: it vanishes on an element of one letter, $B(\tilde{Ξ}_{\mathrm{sp},L})=B(\tilde{Ξ}_{\mathrm{sp},R})=0$. The chirality keeps the letter instead, and its element $\vec e_z$ does not commute with $\vec e_x$, $\vec e_z\vec e_x=-\vec e_x\vec e_z$; so the chirality reverses the bilinear, $B(-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z)=-B(\tilde{Ξ}_{\mathrm{sp}})$. A bare mass term is available for a mixed element and not for a part of definite letter.

On the field, a chiral abelian gauge symmetry with independent charges is consistent. The charge is one right action, by the element

$$
b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z\in\mathbb{B}_{\Psi},
$$

and the three actions of the construction are

$$
\boxed{\;
\tilde{Ξ}_{\mathrm{sp}}\longmapsto\tilde{Ξ}_{\mathrm{sp}} b,
\qquad
D_\mu:\ \tilde{Ξ}_{\mathrm{sp}}\longmapsto\frac{\partial}{\partial R_\mu}\tilde{Ξ}_{\mathrm{sp}}+\frac{i}{\hbar}A_\mu\,(\tilde{Ξ}_{\mathrm{sp}} b),
\qquad
[D_\mu,D_\nu]:\ \frac{i\,\tilde{Ξ}_{\mathrm{sp}}\,\longmapsto}{\hbar}F_{\mu\nu}\,(\tilde{Ξ}_{\mathrm{sp}} b)
\;}
$$

The $D_\mu$ of this display is not the left action of the abelian section above: it is an action with one slot on each side, written as a map so that both slots show. The derivative so written is gauge covariant for **arbitrary** $ϙ_L$, $ϙ_R$, and the mass bilinear is gauge invariant **if and only if** $ϙ_L = ϙ_R$. Every slot is on the page: the derivative multiplies on the left, the connection component on the left, the charge element $b$ on the right. The connection component of an abelian construction is a scalar, so its left factor is central and commutes with $\tilde{Ξ}_{\mathrm{sp}} b$; the connection term is therefore the single right multiplication by $A_\mu b$, and the covariant derivative mixes the two sides, a left derivative against a right multiplier. A genuinely chiral fermion has no gauge-invariant bare mass.

Two structural facts of that article are the hinges of this agenda. The first is that the **canonically available gauge group is vector-like**: the framework's own abelian gauge group is the $*$-unitary part of the centre, which acts as a *scalar* on $M_2(\mathbb{C})$, so every component receives the same charge; and a left multiplication keeps the letter, so the two parts of the field receive it alike. Chirality requires a charge the two letters do not share.

The second is that the **chiral charge is not a left multiplier read off from an element**: it is one right multiplication, by $b$, and the derived form of the display above, read with the subscript, is that it multiplies $\tilde{Ξ}_{\mathrm{sp},L}$ by $ϙ_L$ and $\tilde{Ξ}_{\mathrm{sp},R}$ by $ϙ_R$,

$$
\tilde{Ξ}_{\mathrm{sp}}\longmapsto\tfrac{ϙ_L+ϙ_R}{2}\tilde{Ξ}_{\mathrm{sp}}-\tfrac{i}{2}(ϙ_R-ϙ_L)\tilde{Ξ}_{\mathrm{sp}}\vec e_z .
$$

That is one action and not a two-sided one, and it coincides with a left multiplication — and hence with the framework's $\mathbb{B}$-valued connection — only when $ϙ_L=ϙ_R$, where $b$ is central. The basis operator is not central, and it is a right multiplier rather than a member of the centre; the central form of the chirality — the sign $\xi$ of the double, which is central and lies in the complexification rather than in $\mathbb{B}$ — is a different object in a different space (*Special Element Conventions*, §*The Chirality Convention*). The chiral structure therefore does not fit the form of the covariant derivative $\tilde D$ of *Algebra and Element Conventions*, taken with a $\mathbb{B}$-valued connection: it is a connection valued in the two-sided actions, not in $\mathbb{B}$.

A qualification recorded in that article is carried here because it bears on hypercharge. The corpus does not settle how the element is read on the four-dimensional carrier of the Dirac equation. Read one way, both parts carry the defining action of the group, and a central phase multiplies both by $\exp(i\theta)$: the vector-like reading. Read the other way, the two parts carry conjugate actions, and the same phase multiplies the $L$ part by $\exp(i\theta)$ and the $R$ part by $\exp(-i\theta)$: an **axial**, not vector-like, action. Which reading is physical is the unresolved "two-$i$" question, the same one that fixes the embedding of the chirality in the carrier. It matters here because it decides whether the framework's abelian factor is vector-like or axial.

### The mass term and the real structure

**Two Dirac equations.** The massive Dirac equation of the framework is the **linear chiral mass pair**

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
(\tilde\nabla^{\natural})_\Phi\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R},
$$

with massless limit $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp}} = 0$. Both members act on the algebra by left multiplication, and the mass couples the two letters off-diagonally: this is the one-sided statement.

**The same pair, read with the letters.** What the letters add is the reading of the field into its two parts, and the reading is a right multiplication: it commutes with every left multiplication, hence with the gradient. The free equation stays first order in one field,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp}}=0,
$$

and the massive equation stays the pair above. The second-order consequence is the d'Alembertian $\Box$ of *Operator and Calculus Conventions*, §*The Gradient*.

The square of the gradient is not that operator. $e_t$ commutes with the three spatial units, so the mixed derivatives survive: on a plane wave, where the symbol of the gradient is $k_{t}^{\prime}e_t-i\vec k_\Phi$ with $\vec k_\Phi=\sum_\eta\vec e_\eta k_{\Phi\eta}$,

$$
(k_{t}^{\prime}e_t-i\vec k_\Phi)^{2}=(k_{t}^{\prime\,2}+\lvert\vec k_\Phi\rvert^{2})e_t-2ik_{t}^{\prime}\vec k_\Phi,
\qquad
(k_{t}^{\prime}e_t+i\vec k_\Phi)(k_{t}^{\prime}e_t-i\vec k_\Phi)=k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^{2},
$$

the first carrying the vector part $-2ik_{t}^{\prime}\vec k_\Phi$ — $(-4i,-6i,-8i)$ at $k_{t}^{\prime}=1$, $\vec k_\Phi=(2,3,4)$ — and the second scalar. A one-field first-order massive equation would need a first-order operator with scalar square; the gradient has none, and the mass is therefore the chiral pair and not $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp}}=k_m\tilde{Ξ}_{\mathrm{sp}}$. The chirality is a right multiplier and neither member of the pair contains one, so it has no image under the left multiplication: it is a basis operator of the frame and a value read by the test, not a term of the algebra's equation. The mass shell and the Klein–Gordon consequence are statements in the algebra, while chirality and the axial rotation are statements about the letters.

**The axial current.** The mass is complex-linear in the field, so the continuous central phase passes through it and the vector $\mathrm{U}(1)$ — fermion number — is conserved for the massive field. What the mass breaks is the axial symmetry. The axial current is

$$
j_{5\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,i\,e_\mu\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_z\vec e_{\tau(\mu)}\,\vec e_x ,
\qquad
\tau(r_t)=r_x,\quad \tau(k)=r_y,\quad e_\mu=e_t,\vec e_x,\vec e_y,\vec e_z ,
$$

three slots and no glyph: the element $i e_\mu$ multiplies the field on the left, the field sits in the middle, and the three elements $\vec e_z$, $\vec e_{\tau(\mu)}$, $\vec e_x$ multiply on the right, the last of them being the time-like element the adjoint carries, $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}i\,\cdot\,\vec e_x$. The right factors are written in the order in which they multiply, and that order is part of the formula, because they do not commute: $\vec e_z\vec e_{\tau(\mu)}=-\vec e_{\tau(\mu)}\vec e_z$. One imaginary unit survives, the adjoint's, since the $i$ of the generator and the $-i$ of the chirality are spent as $i(-i)=+1$. Its divergence is the classical identity

$$
\sum_\mu\frac{\partial}{\partial x_\mu}j_{5\mu}
=2im\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}}\,\vec e_z\vec e_x ,
$$

a plain sum, with the derivative taken in $x_\mu=(r'_t,r_x,r_y,r_z)$; in the $i r'_t$ coordinate $Q_t$ the time slot of the current carries the factor $ic$ that the coordinate requires, so the sum is the same divergence. The metric is already spent inside the units, $e_t^{2}=+e_t$ against $\vec e_\eta^{2}=-\vec e_t$, so an extra signature sign $\pm1$ would apply it a second time. The right-hand side vanishes only at $m=0$.

**The real structure.** The algebra's anti-linear object is the **real structure** $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$, order-reversing with a sign, fixing the anti-Hermitian sector $\mathbb{B}_{\Phi}$ and negating the Hermitian one $\mathbb{B}_{\Psi}$; a coupling built on it pairs the field with its conjugate. Whether the framework intends such a **Majorana-type** conjugate pairing, or whether its real structure only supplies the real-form expression of an ordinary **Dirac** mass, is not settled in the read list, and for that separate coupling the two readings differ on whether a conserved fermion number exists at all. This is inherited as an open item, and it is the pivot on which the scalar-sector question turns: a Majorana-type coupling needs no scalar doublet, whereas the linear Dirac mass for a chiral fermion needs a compensating field carrying the charge difference $ϙ_L-ϙ_R$ (the negative of the phase $\exp(\frac{i\,(ϙ_R-ϙ_L)\,\Gamma}{\hbar})$ the mass bilinear acquires).

## The Chiral-Fermion Obstacle: an Algebra Is Not a Chiral Gauge Theory

Electroweak theory is chiral, and this is not a detail of its matter content but the reason its masses need a scalar. The left-handed quarks and leptons sit in $SU(2)_L$ doublets; the right-handed ones are $SU(2)_L$ singlets. The framework's position is stated most sharply as a contrast between what it has and what this requires.

**What it has.** The algebra $\mathrm{SU}(2)$ is present in the material sector, by the decomposition $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$; the non-abelian connection, curvature, adjoint law, Bianchi identity, and invariant density are constructed on it; and a chiral abelian structure with two independent charges is constructed on the field. So both a non-abelian algebra and a chiral charge operator exist in the series — but not in the same construction.

**Why they do not meet.** The framework's non-abelian construction couples the gauge group to matter by **left multiplication** with a $\mathbb{B}$-valued connection, and a left multiplication keeps the letter. The two parts of the field therefore receive the *same* element $\tilde U$, and no choice of $\tilde U$ charges them differently. Under that action the two parts carry the defining action and its conjugate, and for $\mathrm{SU}(2)$ the conjugate of the doublet is **equivalent** to the doublet: the group is pseudoreal, $2\cong\bar{2}$. A gauge transformation manufactured from an element of $\mathbb{B}$ therefore cannot make the $R$ part a singlet or give the two parts inequivalent actions: it multiplies both, and it multiplies them by one element. **A $\mathbb{B}$-valued connection is vector-like on the field.** The pseudoreality was checked on a generic $\mathrm{SU}(2)$ element, not merely on a single generator.

There is a second, representation-theoretic way to say the same thing. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and Artinian, so every $\mathbb{B}$-module is a direct sum of copies of its unique simple module $\mathbb{C}^2$ and has complex dimension $2k$. A one-dimensional $\mathbb{B}$-module would therefore be a trivial module, and $\mathbb{B}$ has no nontrivial one-dimensional module; a fortiori the left action of $\mathrm{SU}(2)\subset\mathbb{B}$ is nonzero on every sub-object of any carrier, since every nonzero $\mathbb{B}$-submodule is a sum of copies of the simple module $\mathbb{C}^2$, on which $\mathrm{SU}(2)$ acts nontrivially. A right-handed $SU(2)_L$ singlet is not a structure the left-multiplication construction can express: there is no sub-object on which that action is trivial. This is a statement about the carrier, not about arithmetic: the electroweak assignment is perfectly writable, but it is not the one $\mathbb{B}$'s left action supplies.

**What a chiral non-abelian structure would require.** It would replace the $\mathbb{B}$-valued connection by one whose generators act on one letter only — schematically the action $\tilde{Ξ}_{\mathrm{sp}}\mapsto T_a\,\tilde{Ξ}_{\mathrm{sp},L}$, with $T_a$ the $\mathrm{SU}(2)$ generators of the read list multiplying on the left and the subscript selecting the part, so that the generator has two slots. The covariance computation is the abelian case of the chiral-fermion article with the single right multiplication promoted to a sum of such two-slot generators, and it is identifiable once every slot is named: with $\Lambda=\exp(\frac{i}{\hbar}\sum_a\Gamma_aT_a)$ multiplying on the left, with the field transforming as $\tilde{Ξ}_{\mathrm{sp}}\mapsto\Lambda\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$, and with the connection transforming in the adjoint with the Maurer–Cartan term, $\mathcal{A}'_\mu=\Lambda\mathcal{A}_\mu\Lambda^{-1}+\frac{i\,\hbar\,(\partial_\mu\Lambda)}{\Lambda}$, the identity $D'_\mu(\tilde{Ξ}_{\mathrm{sp}}')=\Lambda(D_\mu\tilde{Ξ}_{\mathrm{sp}})_L+(D_\mu\tilde{Ξ}_{\mathrm{sp}})_R$ holds. The $R$ part is untouched by the connection, which is what makes it a singlet, and the abelian law $\mathcal{A}'_\mu=\mathcal{A}_\mu-\partial_\mu\Gamma$ is the commuting-generator special case. The cost is explicit: such a connection is **not** $\mathbb{B}$-valued and does not act by left multiplication, so it is not the framework's own non-abelian construction; it is that construction's chiral analogue, valued in a larger algebra. Whether the framework may adjoin it, or must derive it, is the open question.

**The remaining pieces of the obstacle, named.** The matter representation is unbuilt (the read-list parent's open question 3): what representation the matter field carries under the non-abelian group is not specified. The reality class of the connection is unsettled: the mixed assignment $\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_k$ Hermitian is the consistent one, but whether it is intended is open, and it bears on how the physical vector fields are identified with connection components. And a chiral gauge theory must satisfy anomaly-cancellation conditions on its spectrum. The series does formulate the anomaly — the boxed trace, the axial anomaly density as a multiple of $\vec E\cdot\vec B$, and the Standard Model's four cancellation conditions recomputed exactly, in *Anomalies and Anomaly Cancellation in Biquaternionic Form* — and it records that the framework's own gauge factors are anomaly-free identically, the centre being vector-like and $\mathrm{SU}(2)$ having no cubic Casimir. What is absent is a chiral spectrum generated by the framework for those conditions to constrain: the anomaly computation exists, the spectrum it would test does not.

**What would settle it.** The object is a **chiral non-abelian matter representation**: a declared carrier with an $\mathrm{SU}(2)$-module structure in which the $L$ part transforms in the doublet and the $R$ part in the singlet, a connection valued in that structure's two-sided actions, and a verification of gauge covariance and of the resulting mass selection rule. The computation is not mysterious — it is the standard one — but naming the carrier is a decision the framework has not made, and the pseudoreality argument shows it cannot be the framework's own left action. A second settling object is the **anomaly conditions imposed on a framework-generated chiral spectrum** — the machinery exists in the series, the spectrum to feed it does not; a third is a **decision on the real-structure identification** ("two-$i$"), since it fixes whether the framework's abelian factor is vector-like or axial. Classification: **known route, outside the framework's own construction** — the object is identifiable, but it is not reached by the $\mathbb{B}$-valued connection, and the route's endpoint is a modelling choice rather than a derivation.

## Weak Hypercharge: Nothing Derives It

Electroweak theory needs a second gauge factor. With $SU(2)_L$ it forms $SU(2)_L\times \mathrm{U}(1)_Y$, and its charge, weak hypercharge $Y$, is what distinguishes the right-handed partners and what the scalar doublet carries into the masses. The framework's position on $Y$ is simple and should be stated without softening: **nothing in this series derives weak hypercharge, its values, or even its character.** No article assigns hypercharges of its own; where values of $Y$ are written down — in the cancellation conditions of *Anomalies and Anomaly Cancellation in Biquaternionic Form*, for instance — they are transcribed from the standard spectrum. This is an open item, not an assumption.

Three separate facts make the gap precise.

**First, the framework's own abelian factor is vector-like.** The abelian gauge group the algebra supplies canonically is the $*$-unitary part of the centre $\mathbb{B}_{C}$, and a central element acts as a *scalar* on $M_2(\mathbb{C})$, giving every component the same charge. Weak hypercharge is chiral: it acts differently on the two chiralities, since $Y(\tilde{Ξ}_{\mathrm{sp},L})\neq Y(\tilde{Ξ}_{\mathrm{sp},R})$ for the electron, for example. So $\mathrm{U}(1)_Y$ is not the framework's $\mathrm{U}(1)$; it is a different kind of abelian factor, one whose action is non-central. The mismatch is not a missing number, it is a missing *character*.

**Second, the chiral abelian structure that does exist leaves its charges free.** The chiral-fermion article constructs the charge as the one right multiplication $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} b$, with $b$ built from $ϙ_L$ and $ϙ_R$, and shows the mass selection rule $ϙ_L = ϙ_R$. That is exactly the right room for a chiral abelian factor — two independent charges — but $ϙ_L$ and $ϙ_R$ are parameters, exactly as $ϙ$ is in the gauge principle, and nothing fixes them. The structure shows *how* a chiral $\mathrm{U}(1)$ would act; it does not say *which* $\mathrm{U}(1)$ acts. Weak hypercharge would be a particular assignment of these charges to the fermion multiplets, and no such assignment is derived.

**Third, even the character of the framework's abelian factor is undecided.** As the chiral-fermion article's qualification records, under the Lorentz-conjugate interpretation a central phase acts axially rather than vector-like. So the framework does not yet say whether its own $\mathrm{U}(1)$ is vector-like or axial; a fortiori it does not say whether it can play the role of hypercharge.

A fourth, related gap is the **relative normalization of the two couplings**. In the standard theory the two gauge couplings $g$ (for $SU(2)_L$) and $g_{\mathrm Y}$ (for $\mathrm{U}(1)_Y$) fix the Weinberg angle, and the electric charge is a fixed linear combination of the two neutral generators,

$$
\tan\theta_W=\frac{g_{\mathrm Y}}{g},
\qquad
e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W,
\qquad
Q_{\mathrm{em}}=T_3+Y,
$$

in the normalization of $Y$ in which the scalar doublet carries $Y=\tfrac12$. The framework supplies two couplings $\kappa$ (non-abelian) and $ϙ$ (abelian) as free parameters, and no embedding; so neither the mixing angle nor the electric-charge relation is derived.

**What would settle it.** The standard route to hypercharge values is not an assumption but a computation: the requirement that the chiral spectrum be anomaly-free, together with the observed electric-charge spectrum, fixes the hypercharge assignments up to normalization. The settling object is therefore a **biquaternion anomaly computation on the framework's spectrum**, which would either reproduce the standard conditions — in which case $Y$ becomes a framework output for the spectrum the framework supplies — or fail to reproduce them. A second settling object is a **no-go**: a demonstration that the framework's abelian factor cannot carry independent left and right charges, forcing $Y$ to be adjoined as an independent factor. A third is a **positive construction**: a derivation of a chiral abelian generator from the algebra's own structure, rather than from the subscript. Classification: the values are **no route yet**; the anomaly conditions are computed in the series, but they can fix $Y$ only once the framework supplies the chiral spectrum they are imposed on.

## The Scalar Sector and Symmetry Breaking

The scalar sector is where electroweak theory gets its masses, and it is the obstacle that depends most visibly on the two before it.

The need is established on the framework's own terms. The chiral-fermion article's mass selection rule says that a bare Dirac mass is gauge invariant if and only if $ϙ_L = ϙ_R$: a genuinely chiral fermion has no gauge-invariant mass. Its mass must wait for a field whose charge cancels the phase, i.e. one carrying $ϙ_L - ϙ_R$, which is what the Standard Model's Higgs field supplies. So the framework itself identifies the quantum numbers a compensating scalar must carry; what it does not supply is the scalar.

What the framework has is a scalar *field type* but not a scalar *sector*. The gauge-principle article treats a complex scalar biquaternion field $\tilde{Ξ} = \xi_{\mathrm{scl}}\,e_t$ obeying a massive Klein–Gordon equation, and notes that its mass term is linear, so the central phase survives the mass. That is a scalar carrying the central $\mathrm{U}(1)$ — and it is exactly the vector-like abelian factor that hypercharge is not. In the read list there is no scalar *doublet*, no gauge-invariant potential with a non-trivial minimum, no vacuum expectation value, no kinetic term whose expansion gives the vector masses, and no Yukawa coupling. The Dirac article states the framework's relation to the mechanism plainly: it "does not derive the Higgs mechanism; it simply provides a compact notation for the mass term once the mechanism is assumed". The concurrent Higgs-mechanism article is not read here and nothing in this agenda depends on it; the mechanism is carried as an open item.

Three dependencies make this obstacle structural rather than technical.

- **It needs the chiral action.** A scalar that compensates a chiral fermion must carry the same non-abelian representation structure that the chiral-fermion obstacle leaves unbuilt. Without a chiral $SU(2)_L$, there is no doublet for the scalar to be.
- **It needs hypercharge.** The scalar's quantum numbers are exactly the assignments that nothing derives. The Standard Model's scalar is an $SU(2)_L$ doublet of hypercharge $\tfrac12$; both the doublet and the $\tfrac12$ are missing objects here.
- **It is contingent on the mass interpretation.** If the framework deploys a Majorana-type coupling on the real structure $\flat$, the field that carries it must be neutral (or in a real representation) and the Higgs story is replaced by a different one. The scalar program is therefore conditional on the unresolved Majorana-versus-Dirac question.

**What would settle it.** The object is a **gauge-charged scalar on the framework's carrier** with a declared $SU(2)_L\times \mathrm{U}(1)_Y$ representation, a gauge-invariant potential with a non-trivial minimum, a covariant kinetic term whose expansion about that minimum produces the vector-boson masses, and a Yukawa coupling whose charge reproduces the selection rule. The computation is standard; what is not standard is the carrier and the quantum numbers, which are precisely the outputs of the two preceding obstacles. Classification: **known route, blocked** — on the chiral matter representation and on hypercharge, with a contingent branch if the mass interpretation is Majorana-type.

## Gauge Fixing and the Physical Content of an Orbit

The fourth obstacle is not an object the electroweak sector needs but a condition on what may be said about it. The framework **cannot fix the gauge**: the canonical-quantization article records it, the gauge-principle article lists a gauge-fixing principle among the things the algebra does not supply, and the non-abelian article adds the Gribov-type question of whether a gauge orbit intersects a gauge-fixing surface more than once. Nothing in the read list addresses it.

Why this bounds the electroweak sector specifically. In a gauge theory the physical content is the **orbit**, not the connection: a statement about a component $\mathcal{A}_\mu$ is not a statement about the world unless it is gauge invariant or a gauge has been fixed. The vector-boson masses are the sharp case. The standard account exhibits them in unitary gauge, where the Goldstone modes are removed and the massive $W$ and $Z$ appear directly; if no gauge can be fixed, that account is unavailable, and one must instead identify the physical masses as poles of gauge-invariant correlators. The framework has neither a gauge-fixing function nor an invariant spectral analysis, so it can neither exhibit the massive vector spectrum by choice of gauge nor certify it invariantly.

Two inherited facts sharpen the bound. The first is the **mixed reality class** of the non-abelian connection: because $\partial/\partial R_t = -i\partial/\partial r'_t$ flips the conjugation behaviour of the Maurer–Cartan form, the time component and the space components of $\mathcal{A}_\mu$ lie in opposite Hermitian-conjugation eigenspaces, and while the mixed assignment is internally consistent, whether it is the intended physical one is unsettled. Until it is settled, even the identification of the physical vector fields with components of the connection is provisional. The second is that the **gauge function and the connection are material-sector objects** only for real $\Gamma$; the electroweak rotation that mixes the two factors is not of this abelian form, so the abelian gauge-fixing analysis does not extend to it.

**What would settle it.** The object is a **gauge-fixing principle internal to the algebra** — an algebraic condition selecting a preferred representative of each orbit, generalizing the abelian Lorenz condition $\sum_\mu\partial/\partial R_\mu\,A_\mu = 0$ that the parent already has, together with a demonstration that it selects a section (the Gribov question) — or, alternatively, a proof that the framework's physical content is determined entirely by gauge-invariant objects, with the massive spectrum read off from invariants such as the curvature and $\mathrm{Tr}\bigl(\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}\bigr)$ and their correlators. Either would convert "the framework cannot fix the gauge" from a bound on what can be said into a statement about how physics is to be expressed. Classification: **no route yet** for a fixing principle; the invariant formulation is a conceivable route but is not constructed.

## The Ledger

The table collects the items of the agenda and sorts each into the three-way classification. "Established" means recomputed in the series and inherited here; "known route" means the object does not exist but the computation that would produce it is identifiable; "no route yet" means no mechanism has been proposed.

| Item | Status | Object or computation that would settle it |
|---|---|---|
| Abelian gauge principle: central $\mathrm{U}(1)$, connection $\tilde{A}_{\Phi,2}=\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$, covariant derivative, abelian curvature | Established | — |
| Non-abelian construction on $\mathrm{SU}(2)$: connection, adjoint curvature with $[\mathcal{A},\mathcal{A}]$, Bianchi identity, gauge-invariant density | Established | — |
| Available compact algebra $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, i.e. $\mathrm{U}(2)$, real dimension $4$ | Established | — |
| Mixed reality class of the connection ($\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_k$ Hermitian; no single eigenspace) | Established gap (read list) | A declaration of the intended assignment, or a reformulation removing the mismatch |
| Chiral structure: the two letters $L$ and $R$, the charge $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} b$ with values $ϙ_L$ and $ϙ_R$, selection rule $ϙ_L=ϙ_R$, vector-like centre | Established | — |
| $\mathrm{SU}(2)$ as the algebra of weak isospin | Established as an **algebra** only | — |
| Chiral non-abelian gauge action ($SU(2)_L$ doublets and singlets) | Known route, **outside the $\mathbb{B}$-valued construction** | A declared carrier with $\mathrm{SU}(2)$-module structure ($L$ part doublet, $R$ part singlet), a two-slot connection, and verified gauge covariance; pseudoreality shows it cannot be the left action of $\mathbb{B}$ |
| Non-abelian matter representation (read-list open question 3) | Open, known route | Construct the $\mathrm{SU}(2)$ charge as a two-slot action, $\tilde{Ξ}_{\mathrm{sp}}\mapsto T_a\tilde{Ξ}_{\mathrm{sp},L}$, and verify covariance |
| Weak hypercharge: values $Y$ | **No route yet** | A derivation fixing $Y$, e.g. anomaly cancellation on the framework's spectrum; or a no-go forcing $Y$ to be adjoined |
| Character of the abelian factor (vector-like or axial) | Open, inherited | Decide the real-structure ("two-$i$") reading of the field on its carrier |
| Weinberg angle, electric-charge relation $Q_{\mathrm{em}}=T_3+Y$ | **No route yet** | Fix both couplings and the embedding of $\mathrm{U}(1)$ in $\mathrm{U}(2)$; requires hypercharge |
| Scalar sector: doublet, potential, vacuum expectation value, kinetic term | Known route, blocked | A gauge-charged scalar with a declared representation, a non-trivial invariant minimum, and a covariant kinetic term for the vector masses |
| Yukawa coupling and fermion masses | Known route, blocked | A coupling whose charge reproduces $ϙ_L-ϙ_R$; contingent on the mass interpretation |
| Mass interpretation: Majorana-type or real-form Dirac | Open, inherited | Decide the pairing on the real structure |
| Gauge fixing | **No route yet** | A biquaternionic gauge-fixing functional selecting a section, or a proof that physical content is orbit-invariant |
| Gribov copies of any fixing | No route yet | Follows the fixing principle; not addressed anywhere |
| Anomaly cancellation | **Computed** in the series: boxed trace, axial density, the four Standard Model conditions recomputed exactly; the framework's own factors are anomaly-free identically | A framework-generated chiral spectrum for those conditions to constrain |
| $W^\pm$, $Z$ spectrum and masses | Blocked | The scalar kinetic term in a fixed gauge, or an invariant pole analysis |
| Empirical contact | Open | A prediction distinguishing the framework from standard electroweak theory |

## What Would Settle It

The obstacles are not independent, and the dependency chain is short. The scalar sector needs the chiral action and the hypercharge assignments; the chiral non-abelian action needs a declared carrier and a connection that is not the framework's own $\mathbb{B}$-valued one; hypercharge needs either a derivation or a no-go; and every physical statement about masses needs a gauge fixing. Two items are therefore upstream of everything else.

1. **A chiral matter representation, and a decision about its carrier.** Either the framework supplies an object on which $SU(2)_L$ acts with inequivalent left and right representations — which, by the pseudoreality argument, cannot be the left action of $\mathbb{B}$ and must be a two-slot or otherwise enlarged structure — or it is shown that the chiral sector must be adjoined as an independent representation. Either outcome converts the framework's relation to electroweak theory from "unknown" to "stated". The one thing that does not convert it is writing $SU(2)_L$ doublets and singlets down and proceeding; that is the fabricated premise the agenda exists to prevent.
2. **A weak hypercharge assignment, derived or refused.** Either hypercharge comes out of an internal principle — the anomaly-cancellation route is the standard candidate, and the series has the machinery without a framework spectrum to impose it on — or it is shown that the framework's abelian factor cannot carry two independent charges and that $Y$ must be adjoined. As with chirality, the honest alternatives are a derivation and a no-go; an assumption is neither.

A third item is a condition on all physical statements rather than an object of the theory: **a gauge-fixing principle, or an invariant formulation**. Without one, the framework can compute curvature components but cannot say what the massive spectrum is, because it cannot connect an orbit to an observation. This is upstream of the $W$ and $Z$ masses in the same way the colour group and the quark content are upstream of QCD's running coupling in the companion agenda: the computation is standard, and its inputs are the missing objects.

With those settled, the rest of the agenda becomes ordinary work: build the scalar doublet, expand its kinetic term, read off the vector masses, write the Yukawa coupling, and compute the anomaly. Without them, the honest summary of the framework's relation to electroweak theory is the one this article opened with: it has a canonical abelian gauge principle, it has a non-abelian construction on an algebra of exactly the right dimension, it has an exact chiral structure on the field, and it does not have an electroweak sector.

Finally, the genre's standing caution applies here in its strongest form. *The Empirical Status of the Biquaternion Framework* records that on every domain developed, the framework is so far empirically equivalent to the standard theory it reformulates. A biquaternionic electroweak sector, if one is ever constructed, would inherit that position unless it makes a prediction standard electroweak theory does not; and a sector whose gauge group, hypercharge assignments, scalar potential, and gauge fixing are all imported has no prospect of doing so. The agenda's most useful output may be to make that consequence visible early, rather than to produce a construction that appears to answer electroweak theory while assuming all of it.

## Summary

This article is a research agenda for electroweak theory inside the biquaternion framework. Its finding is that the framework reaches the general machinery of a non-abelian gauge theory on a compact algebra of the right dimension, together with an exact chiral structure on the field, and stops before any chiral gauge theory, any hypercharge assignment, or any scalar sector.

What is established is recalled: the abelian gauge principle, with a canonical central $\mathrm{U}(1)$, the connection $\tilde{A}_{\Phi,2}=\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$, the covariant derivative, the abelian curvature, and the linear chiral mass, one-sided in the algebra and read through a right multiplication, with its conserved vector $\mathrm{U}(1)$ and broken axial symmetry; the non-abelian construction, with a connection transforming inhomogeneously, a curvature transforming in the adjoint and containing the commutator term and satisfying the Bianchi identity, and a gauge-invariant density, built on the $\mathrm{SU}(2)$ factor of the material sector; the Lie-algebra decomposition $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, so that the compact algebra available is $\mathrm{U}(2)$, of real dimension four; the chiral structure on the field, with the two letters preserved by every left multiplication, a chirality-odd mass bilinear, and the selection rule $ϙ_L=ϙ_R$; and the vector-like character of the centre.

What is not established is everything electroweak-specific.

- **A chiral gauge theory.** The framework's non-abelian connection is $\mathbb{B}$-valued and acts by left multiplication, which is vector-like on the field because the $SU(2)$ doublet is pseudoreal and $\mathbb{B}$ has no one-dimensional module. The chiral abelian structure that does exist is valued in the two-sided actions, not $\mathbb{B}$. **Known route, outside the framework's own construction**, with the carrier named as the thing to be decided.
- **Weak hypercharge.** Nothing derives its values or its chiral character; the framework's canonical abelian factor is the scalar centre, which is vector-like. **No route yet** for the values; the anomaly conditions are computed in the series, but there is no framework chiral spectrum to impose them on.
- **The scalar sector and symmetry breaking.** The framework has a scalar field type with a linear mass but no doublet; in the read list there is no potential, no vacuum expectation value, and no Yukawa coupling, and the framework states that it does not derive the mechanism. **Known route, blocked** on the chiral action and on hypercharge, and contingent on the mass interpretation.
- **Gauge fixing.** The framework cannot fix the gauge, and the non-abelian case adds the Gribov question; without a fixing or an invariant formulation, the physical content of an orbit — including the vector masses — cannot be exhibited. **No route yet.**

The two upstream items are a chiral matter representation with a declared carrier and a weak hypercharge assignment that is either derived or refused. Everything else depends on them. The article commits throughout to the agenda's central discipline: no section assumes $SU(2)_L$ doublets, hypercharge, or a scalar doublet, and where standard electroweak numbers appear, they are marked as imports.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra; *Algebra and Element Conventions*, §*The Algebra and Its Basis* |
| $e_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$ | The four units; *Algebra and Element Conventions*, §*The Base and Its Units* |
| $i$ | The scalar imaginary, central |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material and informational sectors; *Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces* |
| $\mathbb{B}_{H}$ | The real-quaternion subspace; *Algebra and Element Conventions*, §*The Quaternion and Antiquaternion Subspaces* |
| $\mathbb{B}_{C}$ | The centre of the algebra, and the vector-like abelian factor; *Algebra and Element Conventions*, §*The Centre and the Vector Subspace* |
| $\tilde\nabla_\Phi$, $\Box$ | Biquaternionic gradient and d'Alembertian; *Operator and Calculus Conventions*, §*The Gradient* |
| $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$, $D$ | Abelian connection law and covariant derivative, acting on the left (read list); $D$ is the derivative of *Operator and Calculus Conventions* |
| $[e_a,e_b]=2\varepsilon_{abc}e_c$, $T_a=\tfrac12 e_a$ | Commutator and normalized generators of $\mathrm{SU}(2)\subset\mathbb{B}_{\Phi}$ |
| $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, $\mathrm{U}(2)=\mathrm{U}(1)\oplus\mathrm{SU}(2)$ | Available compact algebra (real dimension $4$) |
| $\tilde U \in SU(2)$ (unit real quaternions), $\mathcal{A}_\mu\in\mathrm{SU}(2)$, $\kappa=\frac{ϙ}{\hbar}$ | Gauge group, non-abelian connection, coupling (read list) |
| $\mathcal{A}_{2,\mu}=\tilde U\mathcal{A}_\mu \tilde U^{-1}+\tfrac{i}{\kappa}(\partial/\partial R_\mu \tilde U)\tilde U^{-1}$ | Non-abelian connection law |
| $F_{\mu\nu}=\partial/\partial R_\mu\,\mathcal{A}_\nu-\partial/\partial R_\nu\,\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $F_{2,\mu\nu}=\tilde UF_{\mu\nu}\tilde U^{-1}$ | Non-abelian curvature; adjoint law |
| $\mathsf{V}_{\mathrm{vol}}=-iR_{\vec e_z}$ | One basis operator that carries the split, a pure right multiplier and hence an example of the right slot; the subscript of an element takes its two values (*Special Element Conventions*, §*The Chirality Convention*) |
| $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ | The field as one element and its two values: $L$ is the minus value, $R$ the plus value, and only the zero element is both |
| $\tilde{Ξ}_{\mathrm{sp}}\mapsto b\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} b$ | Left and right actions of an element; the side is position, and no glyph names one |
| right multiplication by $\vec e_t$ or $\vec e_z$ keeps the letter; by $\vec e_x$ or $\vec e_y$ exchanges the two; left multiplication keeps it | The two laws of the subscript, and the law of the units |
| $j_{5\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}i e_\mu\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_{\tau(\mu)}\vec e_x$, $e_\mu=e_t,\vec e_x,\vec e_y,\vec e_z$, $\tau(t)=x$, $\tau(k)=y$ | Axial current; its divergence is the plain sum $2im\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}}\vec e_z\vec e_x$ |
| $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}i\,\cdot\,\vec e_x$ (the adjoint pairing), $B=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}i\tilde{Ξ}_{\mathrm{sp}}\vec e_x)$, the charge $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} b$, $b=\tfrac{ϙ_L+ϙ_R}{2}e_t-\tfrac{i}{2}(ϙ_R-ϙ_L)\vec e_z$, selection rule $ϙ_L=ϙ_R$ | Dirac adjoint, the chirality-odd mass bilinear, the chiral charge as a single right multiplication |
| $2$, $\bar{2}$ | The doublet and its conjugate, equivalent for $\mathrm{SU}(2)$ (pseudoreality) |
| two-sided actions, $Q\mapsto aQb$ | The home a chiral gauge connection would need; not the left multiplications of $\mathbb{B}$ |
| $a$ | $\mathrm{SU}(2)$ adjoint index, written low; a contraction over it is an explicit sum |
| $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},\ (\tilde\nabla^{\natural})_\Phi\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$; $\tilde{Ξ}_{\mathrm{sp}}^{\flat}=-\tilde{Ξ}_{\mathrm{sp}}^*$ | Linear chiral mass pair; algebra real structure $\flat$ (Majorana/Dirac reading of its pairing open) |
| $\mathrm{Tr}$ | The plain trace of *Product and Form Conventions*, used for the invariant density |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| **Standard electroweak notation, not framework objects** | |
| $SU(2)_L$, $\mathrm{U}(1)_Y$ | Electroweak gauge group — not derived |
| $Y$, $T_3$, $Q_{\mathrm{em}}=T_3+Y$ | Weak hypercharge, weak isospin, electric charge — no derivation of $Y$ |
| $\theta_W$, $g$, $g_{\mathrm Y}$ | Weinberg angle and couplings — not fixed |
| $H$, $v$, Yukawa couplings | Scalar doublet, vacuum expectation value, fermion masses — not constructed |
| $W^\pm$, $Z$, photon | Massive and massless vector bosons — not identified |

## Further Reading

- [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) — the immediate parent; the connection, the adjoint curvature, the Bianchi identity, the gauge-invariant density, the Lie-algebra decomposition $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, and the open matter-representation question this agenda inherits.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) — the abelian origin of the connection, the central $\mathrm{U}(1)$, the linear mass and the real structure, and the gauge-fixing gap.

- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the chirality structure of the field, the vector-like centre, the mass selection rule, the chiral charge as a single right multiplication, and the real-structure qualification that bears on hypercharge.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) — the boxed trace, the axial anomaly and its density, the Standard Model's four cancellation conditions recomputed exactly, and the anomaly-freedom of the framework's own vector-like factors; the computation this agenda's hypercharge route would need applied to a chiral spectrum.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) — the abelian connection whose non-abelian extension is the parent's starting point.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the abelian potential, field strength, and gauge scalar that the electroweak factors would generalize.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the mass term, the chirality of the mass bilinear, and the corpus's explicit statement that the framework does not derive the electroweak structure.

- [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) — the real-structure question and the unrepresented dimension-five operator; the article in which the mass interpretation is pursued.
- [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) and [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) — the left/right matter-representation issue and the module structure on which the chiral analysis rests.
- [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html) — the physical interpretation of chirality and its separation from the sector split.
- [Modules over the Biquaternion Algebra](../articles_maths/the-category-of-modules.html) and [Lie Algebras: A General Introduction](../articles_maths/lie-algebras-a-general-introduction.html) — the module structure of $M_2(\mathbb{C})$, the pseudoreality of $\mathrm{SU}(2)$, and the compact-subalgebra facts behind the available gauge algebra.
- [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) — the representation theory on which the doublet and singlet bookkeeping would rest.
- [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html) — the framework's inability to fix the gauge, on which the physical-content obstacle turns. ([Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html), which does not treat the gauge, records the separate second-class constraint $\pi - i\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\approx 0$.)
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the abelian invariants and the biquaternion norm, whose non-abelian extension is open.
- [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html) — the discrete operations and the corpus's statement that their electroweak relevance is imported.
- [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html) — the standing empirical-equivalence result, the caution under which any biquaternionic electroweak sector would labour.
- [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) — the sibling agenda whose three-way classification and settling-object discipline this article follows.
- [The Einstein Field Equations under the Biquaternion Framework — A Research Agenda](the-einstein-field-equations-under-the-biquaternion-framework-a-research-agenda.html) — the companion agenda whose format and ledger this article follows.
