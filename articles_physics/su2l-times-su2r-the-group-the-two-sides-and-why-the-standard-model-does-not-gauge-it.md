# __$\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$: The Group, the Two Sides, and Why the Standard Model Does Not Gauge It__

## Introduction

**The question.** The frame's gauge group carries two $\mathrm{SU}(2)$ factors, one on each side. Where does a doubled $\mathrm{SU}(2)$ come from in this algebra, and why does the Standard Model, which has the same algebra available, gauge only half of it?

**The answer in three lines.**

$$
\boxed{\;
L(\mathfrak{k})\oplus R(\mathfrak{k})=\mathfrak{so}(4),\quad \dim=3+3=6,
\qquad
Y=T_{3R}+\tfrac12(B-L),\quad Q=T_{3L}+Y .
\;}
$$

**The group is the algebra's own product, at the element level, for free**, as the two one-sided families of the vector part. **The Standard Model uses it twice as a global symmetry** — the chiral symmetry of the strong sector and the custodial symmetry of the scalar sector — **and uses its broken remnant as hypercharge.** What it does not do is gauge it unbroken. So the honest answer to the title's question is not that the Standard Model declines the group. It is that the Standard Model is the phase in which the right-handed factor is broken.

**What this article claims.** That the group is present in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ without an operator layer; that its two factors are the self-dual and anti-self-dual halves of $\mathfrak{so}(4)$, distinguished by the sign of one bracket; that the same group acts on two different modules, spacetime and internal, and that only the second is a gauge factor; that three of its four roles in physics are already realised; and that the fourth is excluded at low energy by the module and not by the algebra.

**What this article does not claim.** That the algebra supplies a chiral gauge theory. It does not: one-sided multiplication is vector-like, and the tie between an operator side and a spinor letter is not in the algebra. That failure is the *chiral wall*, stated in [Electroweak Theory in the Biquaternion Framework](electroweak-theory-in-the-biquaternion-framework-the-u2-reach-and-the-chiral-wall.html) and restated for the frame in [The Fourth-Colour Left–Right Model](the-fourth-colour-left-right-model.html); §3 and §5.5 quote it and do not re-derive it. **Nor does this article state any coupling value**; where the two factors' strengths would enter, it names the structure and stops.

**One word, five jobs.** *Left* and *right* name, in this corpus, the slot an operator acts on, the label of an element, the helicity of a field, the multiplication side in a product, and — in $\mathrm{SU}(2)_L$ — a gauge factor. **Five meanings of two words is how this subject goes wrong**, so this article says *side* for the multiplication, *letter* for the chirality slot, and *factor* for the gauge group.

**The order.** §1 fixes the group as an abstract object. §2 finds it in the algebra and separates its two halves. §3 separates the two modules the group can act on, which is the technical heart. §4 lists the four roles it plays in physics. §5 answers the question in the title. §6 is the cost. §7 is what would settle it.

## 1. The Group

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

**So the left–right group and the Lorentz group are not two unrelated structures.** They are the untied and the tied versions of one object, and §2 shows that the corpus builds exactly this tie, with the involution $*$ as the tie.

## 2. The Two Sides in the Algebra

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
| $L_{\tilde Q}R_{\tilde Q_2}$, free | two, modulo the rescaling $\tilde Q\to\lambda\tilde Q$, $\tilde Q_2\to\lambda^{-1}\tilde Q_2$ | $\mathrm{SU}(2)\times\mathrm{SU}(2)$ | $\mathrm{Spin}(4)$, Euclidean, untied |
| $\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$, tied | one | $\mathrm{SL}(2,\mathbb{C})$ on the unit slice | $\mathrm{SO}^{+}(1,3)$, Lorentz, tied |

**What the table says.** The corpus contains both groups and the difference between them is one involution. **Untie the two sides and the group is $\mathrm{SU}(2)\times\mathrm{SU}(2)$; tie them by Hermitian conjugation and it is the Lorentz group.** Physics uses the tied version for spacetime and the untied version for internal symmetry, and the arithmetic is the same arithmetic in both cases.

## 3. One Group, Two Modules

**The danger.** §2 shows that the group is native. It does not show that the group can be an *internal* gauge symmetry, and that difference is the whole question. **A group is not a physical symmetry until a module is named**, and this group acts here on two modules that are not the same physics.

**The first module: the carrier.** $\mathbb{B}$ itself, real dimension eight, with the vector part $\mathfrak{k}$ of dimension three carrying the adjoint action. Here the group is

$$
\mathrm{Spin}(4)_{E}=\mathrm{SU}(2)\times\mathrm{SU}(2)\ \text{acting on the four-dimensional real carrier},
$$

the Euclidean rotation group, whose Lorentzian relative is the tied version of §2. **This is a spacetime group and its indices are spacetime indices.**

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

**And that is what a left–right model asks for.** One non-abelian factor per chirality requires the two-sided structure and the tie *side* $\leftrightarrow$ *letter*. **The corpus has the two sides and has the two letters and does not exhibit the map.** So the frame's chirality is put in by the assignment of multiplets — a declaration — and not by the algebra. §5.5 returns to this once.

## 4. Four Roles in Physics

**The same group, four statuses.** Keeping them apart is what makes §5 answerable.

| role | group | status in nature | broken by | what survives |
|---|---|---|---|---|
| spacetime rotations | $\mathrm{Spin}(4)_{E}$, or $\mathrm{SL}(2,\mathbb{C})$ when tied | exact, local | nothing | the Lorentz group |
| chiral symmetry of the strong sector | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | exact in the two-flavour chiral limit | quark masses and the condensate | $\mathrm{SU}(2)_V$, the pions as Goldstones |
| custodial symmetry of the scalar sector | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, global and accidental | approximate | the mass splittings | $\mathrm{SU}(2)_V$, hence $\rho=1$ |
| gauged electroweak left–right | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | **not observed** | its own breaking scale | $\mathrm{SU}(2)_L$ |

**Role one, spacetime.** The group is the rotation group of four dimensions and the Euclidean partner of the Lorentz group, related by the tie of §2. **The weak interaction's maximal parity violation is a statement about the internal factors and has nothing to do with this role**; a left–right model restores parity in the internal factor, not in spacetime.

**Role two, the strong sector.** With two light flavours the strong interaction has an approximate global symmetry of this shape, spontaneously broken to the diagonal, and the pions are the three Goldstones of the broken half. **The corpus carries it** as the nonlinear sigma field with the action $\tilde Q\mapsto g_L\tilde Qg_R^{*}$, its invariant metric, its currents and its decay constant; see [The Nonlinear Sigma Model and the Chiral Field](the-nonlinear-sigma-model-and-the-chiral-field-in-biquaternionic-form.html) and [The Chiral Theory, the Lagrangian, the Pion and the Decay Constant](the-chiral-theory-and-the-lagrangian-the-pion-and-the-decay-constant.html).

**Role three, the custodial symmetry.** The scalar sector has an accidental global symmetry of the same shape acting on the doublet, and the vacuum value $(0,v)$ is invariant under the diagonal. **That diagonal is what ties the two masses:**

$$
\rho=\frac{M_W^{2}}{M_Z^{2}\cos^{2}\theta_W}=1\quad\text{at tree level, to a part in a thousand.}
$$

The corpus recomputes it: the quaternion-valued scalar admits $\tilde Q\mapsto g_L\tilde Qg_R^{*}$, a central vacuum is diagonal-invariant, and the two mass matrices come out proportional. The detail is in [Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter-in-biquaternionic-form.html).

**Role four, the gauge symmetry.** The only role not realised: the two sides promoted to local symmetries with their own gauge fields. **Nothing in the data requires it, and nothing excludes it above its breaking scale.**

**The lesson of the table.** "The Standard Model does not use this group" is false as stated. **It uses it as an exact global symmetry of the strong sector, as an approximate global symmetry of the scalar sector, and as the source of hypercharge.** What it does not do is gauge it unbroken.

## 5. Why the Standard Model Does Not Gauge It

**Five reasons, and the last one is structural.**

**5.1 The charged current is purely $V-A$.** Reinstating parity would require a right-handed charged current of the same size as the observed one, and it is not there. **The measured parity violation is maximal and not partial**, so the two factors cannot be approximately symmetric at the electroweak scale.

**5.2 The right-handed neutrino.** For the right-handed electron to be a doublet it needs a partner, and the only candidate is a right-handed neutrino. **That state is not required by the Standard Model and has never been seen as a gauge state**; it is allowed, and its mass is bounded from above only by cosmology. So the group costs a particle the model does not need.

**5.3 The group forces the sixteen.** This is the sharpest reason, and it is a chain rather than a choice. Charge in the frame is

$$
Q=T_{3L}+T_{3R}+\tfrac12(B-L),
$$

so $B-L$ must itself be a gauge symmetry, because $Q$ is a combination of gauge generators. **And the abelian factor is anomaly-free exactly when the right-handed neutrino is included**, since the two conditions

$$
\textstyle\sum(B-L)=0,\qquad \sum(B-L)^{3}=0
$$

hold on the sixteen and fail on the fifteen. So

$$
\text{gauge }\mathrm{SU}(2)_R\ \Longrightarrow\ \text{gauge }B-L\ \Longrightarrow\ \nu_R\ \text{required}\ \Longrightarrow\ \text{matter is sixteen}.
$$

**The group demands the even multiplet.** A theory with half the group is free to be odd, and the Standard Model is odd. The arithmetic is in [Anomalies and Anomaly Cancellation](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html).

**5.4 It is broken, not absent, and hypercharge is the remnant.** The neutral generator of the broken factor survives as a global circle, and it mixes with $B-L$:

$$
Y=T_{3R}+\tfrac12(B-L).
$$

**The check is exact**, and it is the reason hypercharge is not an independent invention:

| field | $T_{3L}$ | $T_{3R}$ | $B-L$ | $Y=T_{3R}+\tfrac12(B-L)$ | $Q=T_{3L}+Y$ |
|---|---|---|---|---|---|
| $\nu_L$ | $+\tfrac12$ | $0$ | $-1$ | $-\tfrac12$ | $0$ |
| $e_L$ | $-\tfrac12$ | $0$ | $-1$ | $-\tfrac12$ | $-1$ |
| $\nu_R$ | $0$ | $+\tfrac12$ | $-1$ | $0$ | $0$ |
| $e_R$ | $0$ | $-\tfrac12$ | $-1$ | $-1$ | $-1$ |
| $u_L$ | $+\tfrac12$ | $0$ | $+\tfrac13$ | $+\tfrac16$ | $+\tfrac23$ |
| $d_L$ | $-\tfrac12$ | $0$ | $+\tfrac13$ | $+\tfrac16$ | $-\tfrac13$ |
| $u_R$ | $0$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ | $+\tfrac23$ |
| $d_R$ | $0$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ | $-\tfrac13$ |

**Two readings of that table, and the second is the interesting one.** The first is bookkeeping: the hypercharges come out right, so the relation is true. **The second is structural: the charge formula is parity-symmetric.** The two Cartans enter $Q$ on the same footing, and $Y$ is by definition the piece beyond $T_{3L}$, so substituting $T_{3R}$ for $T_{3L}$ throughout returns the same formula with the same charges. **So the Standard Model does not violate parity by its charges; it violates it by its multiplet assignment** — a doublet here, a singlet there, and the right-handed neutrino omitted. **Parity is broken by the choice of module and not by the choice of numbers**, which is the precise sense in which the frame "restores" it: the module changes and the arithmetic does not.

**5.5 The chiral wall.** From §3: chiral non-abelian one-sided multiplication does not exist. **The Standard Model's $\mathrm{SU}(2)_L$ couples only to left-handed fields, so it is chiral non-abelian, so the algebra cannot supply it as a one-sided action.** The corpus's $L(\mathfrak{k})$ is vector-like and therefore is not weak isospin; weak isospin is the corpus's $\mathrm{SU}(2)$ plus a chirality projection, and the projection is the missing object. **Note what this does not say.** It does not say $\mathrm{SU}(2)_L$ is illegitimate because its generators are absent — the group $\mathrm{SU}(2)$ is licensed twice over, as $L(\mathfrak{k})$ and as $R(\mathfrak{k})$. **The failure is on the module and not on the group**, which is the distinction the wall exists to make.

**The chain, written once.**

$$
\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\times\mathrm{U}(1)_{B-L}
\ \xrightarrow{\ \langle\Delta_R\rangle\ }\
\mathrm{SU}(3)_c\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_{Y}
\ \xrightarrow{\ \langle\Phi\rangle\ }\
\mathrm{SU}(3)_c\times\mathrm{U}(1)_{\mathrm{em}} .
$$

**The middle term is the Standard Model.** It is not a theory that declined the group; it is the low-energy description of a theory that broke one factor of it, and hypercharge is the left-over. **The scale of that breaking is bounded from below only**, so nothing forbids the group and nothing requires it — which is exactly why the fourth role is a hypothesis and not a fact.

## 6. What the Group Costs

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

## 7. What Would Settle It

**The observations, in order of directness.** A resonance of the right-handed charged boson decaying to a lepton and a heavy neutral, which is the cleanest. **A right-handed charged current at low energy**, which would appear as a $V+A$ admixture in beta decay and in muon decay. **Neutrinoless double beta decay**, which needs the heavy Majorana neutral the group supplies. **And a measured departure from $\rho=1$**, which would break the custodial diagonal that role three relies on.

**The corpus's missing object, and it is one object.** A **chiral carrier**: a map that ties the operator side to the spinor letter, so that one side acts on one letter and the other side on the other. **With it, the multiplet assignment becomes a construction instead of a declaration**, and the wall of §5.5 comes down. Without it the frame's chirality is put in by hand and is honest about it.

**What the group does not need.** It needs no new algebra, no new layer, no exceptional structure and no octonion. **The group is present, of dimension six, at the element level, split into self-dual and anti-self-dual halves by an explicit computation, with the two factors commuting and each a copy of the algebra's own rotor group.** Everything else in this article is a consequence of that sentence or a refusal to go beyond it.

## 8. The Checks

| claim | check | result |
|---|---|---|
| the dimension | $\dim\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ | $3+3=6$ |
| the rank | two Cartans, one per ideal | $2$ |
| the two ideals | $[L(\mathfrak{k}),R(\mathfrak{k})]=0$ | the bracket vanishes |
| the identity | $L(\mathfrak{k})\oplus R(\mathfrak{k})$ | $\mathfrak{so}(4)$ |
| the cover | $\ker\rho$ | $\{\pm(\mathrm{I}_4,\mathrm{I}_4)\}$, so two-to-one |
| the spins | $\tfrac12\otimes\tfrac12$ | $0\oplus1$ |
| the self-dual side | $L(\vec e_k)$ against $\omega_k$ | $-\omega_k\in\Lambda^2_+$ |
| the anti-self-dual side | $R(\vec e_k)$ against $\tau_k$ | $-\tau_k\in\Lambda^2_-$ |
| the mirror | the brackets | $+2$ against $-2$ |
| the tie | $g_R=g_L^{*}$ instead of $g_R=g_L$ | $\mathrm{SL}(2,\mathbb{C})$, hence the Lorentz group |
| the modules | carrier against tensor factors | $8$ real against $16$ complex |
| the chirality of one side | $L_{\tilde Q}$ on the two letters | the same action, so vector-like |
| hypercharge | the eight rows against $Y=T_{3R}+\tfrac12(B-L)$ | all eight exact |
| the parity reading | substitute $T_{3R}$ for $T_{3L}$ in $Q$ | the same formula, the same charges |
| the sixteen | the two $B-L$ anomaly sums | $0$ and $0$ on sixteen, not on fifteen |
| the cost | $\mathfrak{su}(3)$ against $\mathfrak{u}(2)$ | $8$ against $4$, so one layer |
| the ceiling | $\mathfrak{so}(10)$ against $\mathfrak{u}(4)\oplus\mathfrak{u}(4)$ | $45$ against $32$ |

**The rows that carry the article.** The identity $L\oplus R=\mathfrak{so}(4)$ is what makes the group free. The sign of the bracket is what makes the two factors mirror images rather than copies. The eight hypercharge rows are what make hypercharge a remnant rather than a postulate. **And the parity row is what separates the two readings of §5.4**: the numbers are symmetric and the multiplets are not.

## 9. Distinctions That Are Easy to Lose

The group is not the pair's group. $\mathrm{SU}(2)\times\mathrm{SU}(2)$ is a product of two factors; the electroweak pair of the Standard Model, $\mathrm{SU}(2)\times\mathrm{U}(1)$, is a different group with a different quotient structure, and [The Electroweak Pair](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html) is where that difference is computed.

Native is not gauged. The group's presence at the element level is a fact about the algebra; a gauge symmetry is a fact about a module (§3).

Spacetime is not internal. The same group is $\mathrm{Spin}(4)_{E}$ on the carrier and an internal factor on the tensor factors, and the left–right model needs the second (§3).

Parity is broken by the module and not by the charges. The charge formula is symmetric under $L\leftrightarrow R$; the multiplet assignment is not (§5.4).

Broken is not absent. The Standard Model is the middle term of a three-term chain, and hypercharge is the survivor (§5).

The chiral wall is a statement about the module. The group is licensed twice over; what is missing is the tie between an operator side and a spinor letter (§3, §5.5).

Not observed is not excluded. The fourth role is bounded from below only, and that is why it is a hypothesis rather than a refutation (§5).

## Summary

**The group.** $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ is the compact form of $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$, of dimension six and rank two, the double cover of $\mathrm{SO}(4)$, and the spin group of four-dimensional space: each factor carries $s=\tfrac12$ and the pair carries $0$ and $1$.

**What it is in the algebra.** The two one-sided families of the vector part, $L(\mathfrak{k})\oplus R(\mathfrak{k})=\mathfrak{so}(4)$, at the element level, with the left factor the self-dual half and the right the anti-self-dual half, and the sign of the bracket as the mirror between them.

**The two modules.** On the carrier the group is $\mathrm{Spin}(4)_{E}$, spacetime. On the tensor factors of $\mathbb{B}\otimes\mathbb{B}$ it is internal. The frame needs the second, and the algebra builds it as a module.

**The four roles.** Spacetime rotations, exact; the chiral symmetry of the strong sector, approximate and spontaneously broken; the custodial symmetry of the scalar sector, approximate and giving $\rho=1$; the gauged left–right symmetry, not observed.

**Why the Standard Model does not gauge it.** Because it uses it: as a global symmetry twice, and as the source of hypercharge, $Y=T_{3R}+\tfrac12(B-L)$. The Standard Model is the phase in which the right-handed factor is broken, and hypercharge is the survivor. Its charges are parity-symmetric; its multiplets are not.

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
| $\rho$ | here the display $\mathrm{Spin}(3)\times\mathrm{Spin}(3)\to\mathrm{SO}(4)$; also the mass ratio of §4 |
| $\mathrm{Hp}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | the tied two-sided action; the tie is what gives the Lorentz group |
| $\mathbb{B}_L$, $\mathbb{B}_R$ | the two tensor factors, $\{\mathrm{I}_2\otimes A\}$ and $\{B^{\mathsf T}\otimes\mathrm{I}_2\}$ |
| $T_{3L}$, $T_{3R}$ | the two Cartan generators, one per factor |
| $B-L$ | baryon minus lepton number, the abelian generator |
| $Y=T_{3R}+\tfrac12(B-L)$ | hypercharge as the remnant of the broken right-handed factor |
| $\Delta_R$, $\Phi$ | the scalars that break the right-handed factor and then the electroweak pair |

## Further Reading

- [The Fourth-Colour Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-fourth-colour-left-right-model.html). The frame that uses this group, where each factor comes from, and the ceiling that forces the tensor product.
- [The Electroweak Pair in the Biquaternion Framework: The Quotient and the Parity Lock](the-electroweak-pair-in-the-biquaternion-framework-the-quotient-and-the-parity-lock.html). $\mathrm{SU}(2)\times\mathrm{U}(1)$ against the algebra's $\mathrm{U}(2)$, and the selection rule the quotient imposes.
- [Electroweak Theory in the Biquaternion Framework: The $\mathrm{U}(2)$ Reach and the Chiral Wall](electroweak-theory-in-the-biquaternion-framework-the-u2-reach-and-the-chiral-wall.html). The wall of §3 at its four levels, and the ledger of what each level would need.
- [The Lie Algebra $\mathfrak{so}(4)$](../articles_maths/the-lie-algebra-skew-4-and-so-4.html). $\mathfrak{so}(4)=\Lambda^{2}_{+}\oplus\Lambda^{2}_{-}$, the self-dual basis, and the identification of $L(\vec e_k)$ with $-\omega_k$ and $R(\vec e_k)$ with $-\tau_k$.
- [The Spin Group via $4\times4$ Real Matrices](../articles_maths/the-spin-group-via-4x4-real-matrices.html). The display $\rho$ computed, and the warning that the group is a three-sphere and not a set of matrices.
- [From the Spin of a Single Rotor to the Spin of a Pair](../articles_maths/from-the-spin-of-a-single-rotor-to-the-spin-of-a-pair.html). $s=\tfrac12$ per factor and $0\oplus1$ for the pair.
- [The Hermitian Pair of Operators Acting on Two Sides](../articles_maths/the-hermitian-pair-of-operators-acting-on-two-sides.html). The tie $R_{\tilde Q^{*}}$ and the twofold cover of the Lorentz group.
- [The Transposition of the Two Sides](../articles_maths/the-transposition-of-the-two-sides.html). The conversion between the two factors, and the difference between a side and a letter.
- [The Pauli Representation Operators](../articles_maths/m4c-pauli-representation-operators.html). $\mathbb{B}_L=\{\mathrm{I}_2\otimes A\}$ and $\mathbb{B}_R=\{B^{\mathsf T}\otimes\mathrm{I}_2\}$, the internal tensor factors of §3.
- [Charge Quantisation from the Fourth Colour: One Trace, One Third, and Where the Twenty-One Generators Go](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). The trace that fixes the $B-L$ eigenvalues used in the hypercharge table.
- [Anomalies and Anomaly Cancellation in the Fourth-Colour Left–Right Model](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The two $B-L$ conditions that force the sixteen.
- [Custodial Symmetry and the $\rho$ Parameter in Biquaternionic Form](custodial-symmetry-and-the-rho-parameter-in-biquaternionic-form.html). The third role, computed.
- [The Nonlinear Sigma Model and the Chiral Field in Biquaternionic Form](the-nonlinear-sigma-model-and-the-chiral-field-in-biquaternionic-form.html). The second role, and the left–right action on the pion field.
