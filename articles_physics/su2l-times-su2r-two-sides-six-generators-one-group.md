# __$\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$: Two Sides, Six Generators, One Group__

## Introduction

**The question.** The frame's gauge group carries two $\mathrm{SU}(2)$ factors, one on each side. Where does a doubled $\mathrm{SU}(2)$ come from in this algebra, and what does it act on?

**The answer in three lines.**

$$
\boxed{\;
L(\mathfrak{k})\oplus R(\mathfrak{k})=\mathfrak{so}(4),\quad \dim=3+3=6,\quad \operatorname{rank}=2,
\qquad
\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R=\mathrm{Spin}(4)
\;}
$$

**The group is the algebra's own product, at the element level, for free**, as the two one-sided families of the vector part. **Its two factors are the self-dual and anti-self-dual halves of $\mathfrak{so}(4)$**, and the sign of one bracket is what distinguishes them. **And the same group acts on two different modules**, spacetime and internal, of which only the second is a gauge factor.

**What this article claims.** That the group is present in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ without an operator layer; that its two factors are the self-dual and anti-self-dual halves of $\mathfrak{so}(4)$, distinguished by the sign of one bracket; that the same group acts on two different modules, spacetime and internal, and that only the second is a gauge factor; that three of its four roles in physics are already realised; and that whether the fourth is realised is a question about the module and not about the algebra.

**What this article does not claim.** That the algebra supplies a chiral gauge theory. It does not: one-sided multiplication is vector-like, and the tie between an operator side and a spinor letter is not in the algebra. That failure is the *chiral wall*, stated in [Electroweak Theory in the Biquaternion Framework](electroweak-theory-in-the-biquaternion-framework-the-u2-reach-and-the-chiral-wall.html) and restated for the frame in [The Four Colours Left–Right Model](the-four-colours-left-right-model.html); *One Group, Two Modules* and *What Would Settle It* quote it and do not re-derive it. **Nor does this article state any coupling value**; where the two factors' strengths would enter, it names the structure and stops.

**Where the other question is answered.** Why the low-energy gauge group has one weak factor and not two is a question about hypercharge, about the multiplet assignment and about a breaking, and it is the Standard Model's chapter: [The Standard Model as the Low-Energy Phase](the-standard-model-as-the-low-energy-phase.html), §*Why the Standard Model Gauges One Side and Not Two*. **This article keeps the group; that section keeps the comparison.**

**One word, five jobs.** *Left* and *right* name, in this corpus, the slot an operator acts on, the label of an element, the helicity of a field, the multiplication side in a product, and — in $\mathrm{SU}(2)_L$ — a gauge factor. **Five meanings of two words is how this subject goes wrong**, so this article says *side* for the multiplication, *letter* for the chirality slot, and *factor* for the gauge group.

**The order.** *The Group* fixes the group as an abstract object. *The Two Sides in the Algebra* finds it in the algebra and separates its two halves. *One Group, Two Modules* separates the two modules the group can act on, which is the technical heart. *Four Roles in Physics* lists the four roles it plays in physics. *What the Group Costs* is the cost, *What Would Settle It* is what would settle it, *The Checks* is the checks and *Distinctions That Are Easy to Lose* the distinctions.

## The Group

**The algebra.** Complexified, the Lie algebra is two simple ideals that commute:

$$
\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C}),\qquad \dim_{\mathbb{C}}=6,\qquad \operatorname{rank}=2 .
$$

**It is not simple, and that is its defining property here.** A semisimple group with a two-dimensional Cartan subalgebra, split into two halves that cannot reach each other through the bracket.

**The compact form.** The compact real form is $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, of real dimension six, whose group is the double cover of $\mathrm{SO}(4)$:

$$
1\longrightarrow\mathbb{Z}_2\longrightarrow \mathrm{SU}(2)\times\mathrm{SU}(2)\xrightarrow{\ \rho\ }\mathrm{SO}(4)\longrightarrow 1 .
$$

**The display.** In this corpus $\rho$ is not an abstraction but a construction from a pair of rotors acting on two sides,

$$
\rho:\mathrm{Spin}(3)\times\mathrm{Spin}(3)\longrightarrow \mathrm{SO}(4),\qquad \ker\rho=\{\pm(\mathrm{I}_4,\mathrm{I}_4)\},
$$

and the companion computation gives the spins a pair of operators can carry: each factor carries $s=\tfrac12$, and the addition rule gives $0$ and $1$ and nothing else. **So the group of this article is the spin group of four-dimensional space, built as the corpus builds every pair.**

**The invariants.**

| object | $\dim_{\mathbb{R}}$ | rank | centre | simple? |
|---|---|---|---|---|
| $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ | $6$ | $2$ | trivial | no, two ideals |
| $\mathfrak{so}(4)$ | $6$ | $2$ | trivial | no, two ideals |
| group $\mathrm{Spin}(4)$ | — | $2$ | $\mathbb{Z}_2$ (diagonal) | no |
| $\mathfrak{su}(2)$ alone | $3$ | $1$ | trivial | yes |

**The diagonal is the Lorentz group, and this is the article's most useful sentence.** The doubled complex algebra contains its diagonal, $X\mapsto(X,X)$, and that diagonal is $\mathfrak{sl}(2,\mathbb{C})$, whose group covers the proper orthochronous Lorentz group:

$$
\mathrm{SU}(2)\times\mathrm{SU}(2)=\text{compact form of the doubled algebra},
\qquad
\mathrm{SL}(2,\mathbb{C})=\text{its diagonal}.
$$

**So the left–right group and the Lorentz group are not two unrelated structures.** They are the untied and the tied versions of one object, and *The Two Sides in the Algebra* shows that the corpus builds exactly this tie, with the involution $*$ as the tie.

## The Two Sides in the Algebra

**Three addresses.** With $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}(\vec e_x,\vec e_y,\vec e_z)$, the algebra's rotor group enters the endomorphisms of $\mathbb{B}$ at three places:

$$
L(\mathfrak{k})=\operatorname{span}\{L_{\vec e_x},L_{\vec e_y},L_{\vec e_z}\},\quad
R(\mathfrak{k})=\operatorname{span}\{R_{\vec e_x},R_{\vec e_y},R_{\vec e_z}\},\quad
\mathrm{ad}(\mathfrak{k})=\operatorname{span}\{L_{\vec e_k}-R_{\vec e_k}\},
$$

$$
L(\mathfrak{k})\oplus R(\mathfrak{k})=\mathfrak{so}(4),\qquad
\mathrm{ad}(\mathfrak{k})=\mathfrak{su}(3)\cap\mathfrak{so}(4).
$$

**The group of this article is the first two addresses together**, at the element level, inside $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$:

$$
\boxed{\ \mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\ =\ \exp\bigl(L(\mathfrak{k})\bigr)\times\exp\bigl(R(\mathfrak{k})\bigr)\ =\ \mathrm{Spin}(4)\ }
$$

**No operator layer, no Clifford algebra, no imported object. The two factors are the two ends of one multiplication**, which is the whole of the corpus's claim about this group.

**Why they commute, and why commuting is the point.** $L_a$ and $R_b$ commute for every $a$ and $b$, because they act on the two ends of the argument. **So the two factors are independent, and the group is a product and not a quotient.** A group that is a product of two commuting factors is exactly what a left–right symmetric theory needs, and the algebra supplies it with no work.

**The self-dual split, which names the sides.** On the six-dimensional space of two-forms,

$$
\mathfrak{so}(4)=\Lambda^{2}_{+}\oplus\Lambda^{2}_{-},\qquad \star^{2}=\mathrm{id},
$$

and the corpus proves which side is which:

$$
L(\vec e_x)=-\omega_1,\quad L(\vec e_y)=-\omega_2,\quad L(\vec e_z)=-\omega_3\ \in\Lambda^{2}_{+},
\qquad
R(\vec e_x)=-\tau_1,\quad R(\vec e_y)=-\tau_2,\quad R(\vec e_z)=-\tau_3\ \in\Lambda^{2}_{-},
$$

with the brackets

$$
[L(\vec e_x),L(\vec e_y)]=2L(\vec e_z),\qquad [R(\vec e_x),R(\vec e_y)]=-2R(\vec e_z).
$$

**The sign difference is the mirror.** The two triples obey the same table with opposite sign, so the two factors are mirror images, and that is the exact sense in which they differ — not a relabelling. **The left factor rotates the self-dual planes, the right factor the anti-self-dual planes, and the Hodge star exchanges them.** The derivation is in [The Lie Algebra $\mathfrak{so}(4)$](../articles_maths/the-lie-algebra-skew-4-and-so-4.html).

**So the group means this in the algebra.** $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ is the rotation group of the four-dimensional carrier, split into the half that acts on the self-dual planes and the half that acts on the anti-self-dual ones. **It is the two angles of a four-dimensional rotation made into two groups.**

**The sandwich, and the tie.** On an element the two sides act by

$$
\tilde Q\longmapsto g_L\,\tilde Q\,g_R^{*},\qquad g_L,g_R\in\mathbb{H}^{1},
$$

and a central value is invariant under the diagonal $g_L=g_R$. **Setting $g_R=g_L^{*}$ instead is the tie**, and the corpus's Hermitian pair is what makes it:

$$
\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}},\qquad
\text{unit-norm slice:}\ \ \mathrm{SL}(2,\mathbb{C})\longrightarrow \mathrm{SO}^{+}(1,3)\ \text{twofold}.
$$

**The two cases, side by side, and this is the article's central table.**

| two-sided action | parameters | compact part | what it is |
|---|---|---|---|
| $L_{\tilde Q}R_{\tilde Q_2}$, free | two, modulo the rescaling $\tilde Q\to\digamma_{\mathrm{cfm}}\tilde Q$, $\tilde Q_2\to\digamma_{\mathrm{cfm}}^{-1}\tilde Q_2$ | $\mathrm{SU}(2)\times\mathrm{SU}(2)$ | $\mathrm{Spin}(4)$, Euclidean, untied |
| $\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$, tied | one | $\mathrm{SL}(2,\mathbb{C})$ on the unit slice | $\mathrm{SO}^{+}(1,3)$, Lorentz, tied |

**What the table says.** The corpus contains both groups and the difference between them is one involution. **Untie the two sides and the group is $\mathrm{SU}(2)\times\mathrm{SU}(2)$; tie them by Hermitian conjugation and it is the Lorentz group.** Physics uses the tied version for spacetime and the untied version for internal symmetry, and the arithmetic is the same arithmetic in both cases.

## One Group, Two Modules

**The danger.** *The Two Sides in the Algebra* shows that the group is native. It does not show that the group can be an *internal* gauge symmetry, and that difference is the whole question. **A group is not a physical symmetry until a module is named**, and this group acts here on two modules that are not the same physics.

**The first module: the carrier.** $\mathbb{B}$ itself, real dimension eight, with the vector part $\mathfrak{k}$ of dimension three carrying the adjoint action. Here the group is

$$
\mathrm{Spin}(4)_{E}=\mathrm{SU}(2)\times\mathrm{SU}(2)\ \text{acting on the four-dimensional real carrier},
$$

the Euclidean rotation group, whose Lorentzian relative is the tied version of *The Two Sides in the Algebra*. **This is a spacetime group and its indices are spacetime indices.**

**The second module: the operator algebra.** $\mathcal{E}_{\mathbb{C}}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$, of complex dimension sixteen, where the two tensor factors are the two sides:

$$
\mathbb{B}_L=\{\mathrm{I}_2\otimes A\},\qquad \mathbb{B}_R=\{B^{\mathsf T}\otimes\mathrm{I}_2\},\qquad \mathbb{B}_L\cap\mathbb{B}_R=\mathbb{C}\,\mathrm{I}_4 .
$$

**Here an $\mathrm{SU}(2)$ on the first factor and an $\mathrm{SU}(2)$ on the second are internal factors**: they act on a sixteen-dimensional multiplet of states, not on a coordinate. This is the module the frame uses.

**The naming rule decides the question.** The group's name stays and the sentence after the name says what the group is *in the algebra*:

| module | the group is | status |
|---|---|---|
| $\mathbb{B}$, vector part | $\mathrm{Spin}(4)_{E}$, the rotation group of the carrier | spacetime, built |
| $\mathbb{B}\otimes\mathbb{B}$, tensor factors | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, internal factors | internal, built as a module |
| $\mathbb{B}$, one-sided action on matter | $L(\mathfrak{k})$ alone, vector-like | internal, built, **not chiral** |

**The third row decides everything.** One-sided multiplication acts on both letters alike, because $L_{\tilde Q}$ carries no information about which letter of its argument it multiplies. **The general statement is the chiral wall**: among one-sided multiplications, those that respect a chirality split commute with the chirality operator, and that centraliser is abelian. **Abelian and chiral is available, at the centre; non-abelian and vector-like is available, at $L(\mathfrak{k})$ and $R(\mathfrak{k})$; non-abelian and chiral is not available** without a two-sided structure whose sides are tied to the letters.

**And that is what a left–right model asks for.** One non-abelian factor per chirality requires the two-sided structure and the tie *side* $\leftrightarrow$ *letter*. **The corpus has the two sides and has the two letters and does not exhibit the map.** So the frame's chirality is put in by the assignment of multiplets — a declaration — and not by the algebra. *What Would Settle It* returns to this once.

## Four Roles in Physics

**The same group, four statuses.** Keeping them apart is what makes the fourth row answerable.

| role | group | status in nature | broken by | what survives |
|---|---|---|---|---|
| spacetime rotations | $\mathrm{Spin}(4)_{E}$, or $\mathrm{SL}(2,\mathbb{C})$ when tied | exact, local | nothing | the Lorentz group |
| chiral symmetry of the strong sector | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | exact in the two-flavour chiral limit | quark masses and the condensate | $\mathrm{SU}(2)_V$, the pions as Goldstones |
| custodial symmetry of the scalar sector | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, global and accidental | approximate | the mass splittings | $\mathrm{SU}(2)_V$, hence $\rho=1$ |
| gauged electroweak left–right | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | **not observed** | its own breaking scale | $\mathrm{SU}(2)_L$ |

**Role one, spacetime.** The group is the rotation group of four dimensions and the Euclidean partner of the Lorentz group, related by the tie of *The Two Sides in the Algebra*. **The weak interaction's maximal parity violation is a statement about the internal factors and has nothing to do with this role**; a left–right model restores parity in the internal factor, not in spacetime.

**Role two, the strong sector.** With two light flavours the strong interaction has an approximate global symmetry of this shape, spontaneously broken to the diagonal, and the pions are the three Goldstones of the broken half. **The corpus carries it** as the nonlinear sigma field with the action $\tilde Q\mapsto g_L\tilde Qg_R^{*}$, its invariant metric, its currents and its decay constant; see [The Nonlinear Sigma Model and the Chiral Field](the-nonlinear-sigma-model-and-the-chiral-field-in-biquaternionic-form.html) and [The Chiral Theory, the Lagrangian, the Pion and the Decay Constant](the-chiral-theory-and-the-lagrangian-the-pion-and-the-decay-constant.html).

**Role three, the custodial symmetry.** The scalar sector has an accidental global symmetry of the same shape acting on the doublet, and the vacuum value $(0,v)$ is invariant under the diagonal. **That diagonal is what ties the two masses:**

$$
\rho=\frac{M_W^{2}}{M_Z^{2}\cos^{2}\theta_W}=1\quad\text{at tree level, to a part in a thousand.}
$$

The corpus recomputes it: the quaternion-valued scalar admits $\tilde Q\mapsto g_L\tilde Qg_R^{*}$, a central vacuum is diagonal-invariant, and the two mass matrices come out proportional. The detail is in [Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter.html).

**Role four, the gauge symmetry.** The only role not realised: the two sides promoted to local symmetries with their own gauge fields. **Nothing in the data requires it, and nothing excludes it above its breaking scale.** Why the observed theory stops at one factor is a question about hypercharge and the multiplet assignment, and it is answered in [The Standard Model as the Low-Energy Phase](the-standard-model-as-the-low-energy-phase.html), §*Why the Standard Model Gauges One Side and Not Two*.

**The lesson of the table.** The group is not an unused object. **Three of the four roles are realised: an exact global symmetry of the strong sector, an approximate one in the scalar sector, and the rotation group of the carrier.** The fourth is the only one nature does not exhibit at low energy, and the reason belongs to the Standard Model's chapter rather than to this one. **What the table settles here is narrower and enough: the group is native, and only its use is a choice.**

## What the Group Costs

**The claim, in one line.** The algebra's alphabet is $\mathrm{SU}(2)$ and a circle, and a factor that is a copy of the alphabet costs nothing.

**The ledger.**

| group | $\dim$ | rank | where the algebra carries it | cost |
|---|---|---|---|---|
| $\mathrm{SU}(2)\times\mathrm{SU}(2)$ | $6$ | $2$ | $L(\mathfrak{k})\oplus R(\mathfrak{k})=\mathfrak{so}(4)$, element level | **free** |
| $\mathrm{SU}(2)^2\times\mathrm{U}(1)$ | $7$ | $3$ | the above, plus the central circle | **free** |
| $\mathrm{SU}(4)$ | $15$ | $3$ | the traceless part of the operator algebra, one layer up | one layer |
| $\mathrm{SU}(3)$ | $8$ | $2$ | inside $\mathfrak{su}(4)$, operator level only | one layer, and only inside |
| $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ | $12$ | $4$ | $A_2\oplus A_1$ does not sit in $A_3$ | **over budget** |
| $\mathrm{SO}(10)$ | $45$ | $5$ | exceeds $\mathfrak{u}(4)\oplus\mathfrak{u}(4)$, of dimension $32$ | **not available** |

**The reading, in three steps.** The element layer's compact sector is $\mathfrak{u}(2)=\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, of dimension four: one $\mathrm{SU}(2)$ and one circle. **Two sides give two $\mathrm{SU}(2)$'s**, because the second is the other family and costs nothing extra, and that doubling is the whole reason the group is free. **Colour costs a layer**, because $\mathfrak{su}(3)$ needs dimension eight against the four available at the element level, and it then comes only as a subgroup of $\mathfrak{su}(4)$. **Above dimension fifteen the budget is exhausted.** This ledger is the frame article's §*Why This Group and Not a Larger One* seen as an account statement; the ceiling that makes the second $\mathrm{SU}(2)$ free is the same computation that forces the frame to be a tensor product.

**Why the doubling is not an accident of naming.** The two factors are not two copies chosen for convenience. **One is the self-dual half of a four-dimensional rotation and the other is the anti-self-dual half**, and the carrier's dimension is four, so the split is canonical. A reader who wants one structural fact from this article should take that one.

## What Would Settle It

**The observations, in order of directness.** A resonance of the right-handed charged boson decaying to a lepton and a heavy neutral, which is the cleanest. **A right-handed charged current at low energy**, which would appear as a $V+A$ admixture in beta decay and in muon decay. **Neutrinoless double beta decay**, which needs the heavy Majorana neutral the group supplies. **And a measured departure from $\rho=1$**, which would break the custodial diagonal that role three relies on.

**The corpus's missing object, and it is one object.** A **chiral carrier**: a map that ties the operator side to the spinor letter, so that one side acts on one letter and the other side on the other. **With it, the multiplet assignment becomes a construction instead of a declaration**, and the wall of *One Group, Two Modules* comes down. Without it the frame's chirality is put in by hand and is honest about it.

**What the group does not need.** It needs no new algebra, no new layer, no exceptional structure and no octonion. **The group is present, of dimension six, at the element level, split into self-dual and anti-self-dual halves by an explicit computation, with the two factors commuting and each a copy of the algebra's own rotor group.** Everything else in this article is a consequence of that sentence or a refusal to go beyond it.

## The Checks

| claim | check | result |
|---|---|---|
| the dimension | $\dim\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ | $3+3=6$ |
| the rank | two Cartans, one per ideal | $2$ |
| the two ideals | $[L(\mathfrak{k}),R(\mathfrak{k})]=0$ | the bracket vanishes |
| the identity | $L(\mathfrak{k})\oplus R(\mathfrak{k})$ | $\mathfrak{so}(4)$ |
| the cover | $\ker\rho$ | $\{\pm(\mathrm{I}_4,\mathrm{I}_4)\}$, so two-to-one |
| the spins | $\tfrac12\otimes\tfrac12$ | $0\oplus1$ |
| the self-dual side | $L(\vec e_\imath)$ against $\omega_\imath$ | $-\omega_\imath\in\Lambda^2_+$ |
| the anti-self-dual side | $R(\vec e_\imath)$ against $\tau_\imath$ | $-\tau_\imath\in\Lambda^2_-$ |
| the mirror | the brackets | $+2$ against $-2$ |
| the tie | $g_R=g_L^{*}$ instead of $g_R=g_L$ | $\mathrm{SL}(2,\mathbb{C})$, hence the Lorentz group |
| the modules | carrier against tensor factors | $8$ real against $16$ complex |
| the chirality of one side | $L_{\tilde Q}$ on the two letters | the same action, so vector-like |
| the cost | $\mathfrak{su}(3)$ against $\mathfrak{u}(2)$ | $8$ against $4$, so one layer |
| the ceiling | $\mathfrak{so}(10)$ against $\mathfrak{u}(4)\oplus\mathfrak{u}(4)$ | $45$ against $32$ |

**The two rows that carry the article.** The identity $L\oplus R=\mathfrak{so}(4)$ is what makes the group free. The sign of the bracket is what makes the two factors mirror images rather than copies. **The remaining rows are checks on those two**: the mirror and the cover follow from the same computation, and the cost row is the dimension count.

## Distinctions That Are Easy to Lose

The group is not the pair's group. $\mathrm{SU}(2)\times\mathrm{SU}(2)$ is a product of two factors; the electroweak pair of the Standard Model, $\mathrm{SU}(2)\times\mathrm{U}(1)$, is a different group with a different quotient structure, and [The Electroweak Pair](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html) is where that difference is computed.

Native is not gauged. The group's presence at the element level is a fact about the algebra; a gauge symmetry is a fact about a module (*One Group, Two Modules*).

Spacetime is not internal. The same group is $\mathrm{Spin}(4)_{E}$ on the carrier and an internal factor on the tensor factors, and the left–right model needs the second (*One Group, Two Modules*).

Parity is broken by the module and not by the charges. The multiplet assignment is what breaks it; a charge bookkeeping symmetric under $L\leftrightarrow R$ is compatible with either choice, which is the point [The Standard Model as the Low-Energy Phase](the-standard-model-as-the-low-energy-phase.html) makes about the observed spectrum.

Broken is not absent. A factor that is no longer gauged below a scale has not left the algebra; the breaking chain is the Standard Model's chapter, and it is where the survivor is identified.

The chiral wall is a statement about the module. The group is licensed twice over; what is missing is the tie between an operator side and a spinor letter (*One Group, Two Modules*, *What Would Settle It*).

Not observed is not excluded. The fourth role is bounded from below only, and that is why it is a hypothesis rather than a refutation (*Four Roles in Physics*).

## Summary

**The group.** $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ is the compact form of $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$, of dimension six and rank two, the double cover of $\mathrm{SO}(4)$, and the spin group of four-dimensional space: each factor carries $s=\tfrac12$ and the pair carries $0$ and $1$.

**What it is in the algebra.** The two one-sided families of the vector part, $L(\mathfrak{k})\oplus R(\mathfrak{k})=\mathfrak{so}(4)$, at the element level, with the left factor the self-dual half and the right the anti-self-dual half, and the sign of the bracket as the mirror between them.

**The two modules.** On the carrier the group is $\mathrm{Spin}(4)_{E}$, spacetime. On the tensor factors of $\mathbb{B}\otimes\mathbb{B}$ it is internal. The frame needs the second, and the algebra builds it as a module.

**The four roles.** Spacetime rotations, exact; the chiral symmetry of the strong sector, approximate and spontaneously broken; the custodial symmetry of the scalar sector, approximate and giving $\rho=1$; the gauged left–right symmetry, not observed.

**Where the fourth role is decided.** Not here. Whether nature gauges the group, and why the low-energy theory gauges one factor of it, are questions about hypercharge, about the multiplet assignment and about a breaking; [The Standard Model as the Low-Energy Phase](the-standard-model-as-the-low-energy-phase.html) takes them up, and this article stops at the group the algebra supplies.

**The cost.** Two $\mathrm{SU}(2)$'s and a circle are free, because the alphabet is $\mathrm{SU}(2)$; colour costs a layer; a group needing a separate $\mathrm{SU}(3)$ with a commuting $\mathrm{SU}(2)$ is over budget.

**What is missing, and it is one thing.** The tie between the operator side and the spinor letter. With it the two factors become the two chiralities, and the group becomes a chiral gauge group in the algebra's own terms.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathfrak{k}$ | the vector part, $\operatorname{span}_{\mathbb{R}}(\vec e_x,\vec e_y,\vec e_z)$, dimension $3$ |
| $L(\mathfrak{k})$, $R(\mathfrak{k})$ | the two one-sided families of the vector part, each of dimension $3$ |
| $\mathrm{ad}(\mathfrak{k})$ | the diagonal family $L_{\vec e_k}-R_{\vec e_k}$, the derivation |
| $\Lambda^{2}_{\pm}$ | the self-dual and anti-self-dual two-forms, the two ideals of $\mathfrak{so}(4)$ |
| $\star$ | the Hodge star on two-forms, $\star^{2}=\mathrm{id}$, exchanging the ideals |
| $\rho$ | here the display $\mathrm{Spin}(3)\times\mathrm{Spin}(3)\to\mathrm{SO}(4)$; also the mass ratio of *Four Roles in Physics* |
| $\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | the tied two-sided action; the tie is what gives the Lorentz group |
| $\mathbb{B}_L$, $\mathbb{B}_R$ | the two tensor factors, $\{\mathrm{I}_2\otimes A\}$ and $\{B^{\mathsf T}\otimes\mathrm{I}_2\}$ |

## Further Reading

- [The Standard Model as the Low-Energy Phase: The $\mathrm{U}(2)$ Ceiling and the Four Unbuilt Sectors](the-standard-model-as-the-low-energy-phase.html). Why the low-energy theory gauges one side and not two, and hypercharge as the broken factor's remnant.
- [The Four Colours Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-four-colours-left-right-model.html). The frame that uses this group, where each factor comes from, and the ceiling that forces the tensor product.
- [The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html). $\mathrm{SU}(2)\times\mathrm{U}(1)$ against the algebra's $\mathrm{U}(2)$, and the selection rule the quotient imposes.
- [Electroweak Theory in the Biquaternion Framework: The $\mathrm{U}(2)$ Reach and the Chiral Wall](electroweak-theory-in-the-biquaternion-framework-the-u2-reach-and-the-chiral-wall.html). The wall of *One Group, Two Modules* at its four levels, and the ledger of what each level would need.
- [The Lie Algebra $\mathfrak{so}(4)$](../articles_maths/the-lie-algebra-skew-4-and-so-4.html). $\mathfrak{so}(4)=\Lambda^{2}_{+}\oplus\Lambda^{2}_{-}$, the self-dual basis, and the identification of $L(\vec e_\imath)$ with $-\omega_\imath$ and $R(\vec e_\imath)$ with $-\tau_\imath$.
- [The Spin Group via $4\times4$ Real Matrices](../articles_maths/the-spin-group-via-4x4-real-matrices.html). The display $\rho$ computed, and the warning that the group is a three-sphere and not a set of matrices.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](../articles_maths/the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html). $s=\tfrac12$ per factor and $0\oplus1$ for the pair.
- [The Hermitian Pair of Operators Acting on Two Sides](../articles_maths/the-hermitian-pair-of-operators-acting-on-two-sides.html). The tie $R_{\tilde Q^{*}}$ and the twofold cover of the Lorentz group.
- [The Transposition of the Two Sides](../articles_maths/the-transposition-of-the-two-sides.html). The conversion between the two factors, and the difference between a side and a letter.
- [The Pauli Representation Operators](../articles_maths/m4c-pauli-representation-operators.html). $\mathbb{B}_L=\{\mathrm{I}_2\otimes A\}$ and $\mathbb{B}_R=\{B^{\mathsf T}\otimes\mathrm{I}_2\}$, the internal tensor factors of *One Group, Two Modules*.
- [Custodial Symmetry and the $\rho$ Parameter in Biquaternionic Form](custodial-symmetry-and-the-rho-parameter.html). The third role, computed.
- [The Nonlinear Sigma Model and the Chiral Field in Biquaternionic Form](the-nonlinear-sigma-model-and-the-chiral-field-in-biquaternionic-form.html). The second role, and the left–right action on the pion field.
