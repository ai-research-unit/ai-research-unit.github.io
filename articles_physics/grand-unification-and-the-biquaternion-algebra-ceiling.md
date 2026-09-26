# __Grand Unification and the Biquaternion Algebra Ceiling__

## Introduction

Grand unification is the programme of embedding the Standard-Model gauge group

$$
G_{\mathrm{SM}}=SU(3)_c\times SU(2)_L\times U(1)_Y
$$

into a single simple group $G_{\mathrm{GUT}}$, so that the three independent couplings become one at a high scale and the electric charge is quantised by the group's structure. The standard candidates are Georgi–Glashow $SU(5)$, Pati–Salam $SU(4)\times SU(2)_L\times SU(2)_R$, $SO(10)$ and $E_6$, with characteristic ranks and dimensions:


|  | $SU(3)\times SU(2)\times U(1)$ | $SU(5)$ | $SO(10)$ | $E_6$ |
|---|---|---|---|---|
| $\text{rank}$ | $2+1+1=4$ | $4$ | $5$ | $6$ |
| $\text{dimension}$ | $8+3+1=12$ | $24$ | $45$ | $78$ |


The preceding article of this group, *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, proved that the biquaternion algebra's intrinsic compact gauge structure is

$$
\mathbb M_-=\mathrm{span}_{\mathbb R}\{ie_0,e_1,e_2,e_3\}=\mathfrak u(2)=\mathfrak{su}(2)\oplus\mathfrak u(1),
\qquad
\text{rank}=2,
\qquad
\dim_{\mathbb R}=4 .
$$

This article draws the consequence for unification. The conclusion is a sharp structural statement: **the framework unifies the electroweak and abelian factors, because those are exactly the $U(2)$ that the algebra carries, and it cannot unify them with colour, because $SU(3)_c$ is not inside the algebra and no grand-unified group containing it has rank at most two.** Grand unification in the strict sense is outside the algebra's reach. It is reachable only by enlarging the carrier, and every enlargement pays in canonicity and in unwanted structure. As in the companion ceiling article, this is a result about the framework and not a failure of effort.

The article first sets the threshold that any unified group must clear, then locates the framework's reach below it, then shows what the enlargement to $M_n(\mathbb B)$ would cost, and finally states what the framework's unification actually is: electroweak, with the strong sector present only through its gauge-invariant composites.

**Conventions.** We use those of *Conventions in the Biquaternion Universe* and of the companion gauge articles. The algebra is $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H\cong M_2(\mathbb C)$, the compact sector is $\mathbb M_-=\mathfrak u(2)$ with generators $T_a=\tfrac12e_a$ and $T_0=\tfrac12ie_0$, and the defining module is $S\cong\mathbb C^2$. The Standard-Model group is written $SU(3)_c\times SU(2)_L\times U(1)_Y$ with $Y$ the weak hypercharge, and the electric charge is $Q=T_3+Y$ in the normalisation of the electroweak article. The enlargement carries $M_n(\mathbb B)\cong M_{2n}(\mathbb C)$ with compact part $\mathfrak u(2n)$. The trace is the matrix trace on the defining module, distinguished from the informational trace $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$.

- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, for the programme this article constrains.
- Companion article *Electroweak Theory under the Biquaternion Framework — A Research Agenda*, for the unification of the electroweak and abelian factors.
- Companion article *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*, for the colour-singlet programme.
- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, for the ceiling itself.
- Companion article *The Renormalization Group in Biquaternionic Form*, for the running of the couplings and the unification scale.

## The Threshold a Unified Group Must Clear

A unified group $G_{\mathrm{GUT}}$ must contain $G_{\mathrm{SM}}$ as a subgroup, and containment forces two inequalities. The **rank** of a group is the dimension of its maximal torus, and a subgroup's rank cannot exceed its parent's,

$$
\mathrm{rank}\,G_{\mathrm{SM}}=4\;\le\;\mathrm{rank}\,G_{\mathrm{GUT}} ,
$$

so a unified group has rank at least four. The **dimension** of a subgroup cannot exceed that of its parent,

$$
\dim G_{\mathrm{SM}}=12\;\le\;\dim G_{\mathrm{GUT}} ,
$$

so a unified group has at least twelve generators. The standard candidates clear both: $SU(5)$ has rank $4$ and dimension $24$, $SO(10)$ has rank $5$ and dimension $45$, $E_6$ has rank $6$ and dimension $78$. The threshold is the pair $(\text{rank}\ge4,\ \dim\ge12)$.

Two further requirements are structural rather than numerical. First, the unified group must contain $SU(3)_c$ as a subgroup, because colour is a subgroup of $G_{\mathrm{SM}}$ and containment is transitive. Second, the fermions of a generation must fit into representations of $G_{\mathrm{GUT}}$ that reduce correctly under $G_{\mathrm{SM}}$ — the $\bar{\mathbf 5}\oplus\mathbf{10}$ of $SU(5)$, the $\mathbf{16}$ of $SO(10)$, the $\mathbf{27}$ of $E_6$ — so the unified group must have the right representation content, not merely the right size. These two requirements are the substantive ones: a group of rank $4$ and dimension $12$ that failed to contain $SU(3)$ would still not unify the Standard Model.

**The framework against the threshold.** The algebra's intrinsic group is $U(2)$, with

$$
\mathrm{rank}\,U(2)=2<4,
\qquad
\dim_{\mathbb R}U(2)=4<12 .
$$

It fails both numerical conditions, and it fails the structural one: $U(2)$ does not contain $SU(3)_c$, by the dimension argument of *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, since $\dim\mathfrak{su}(3)=8>4=\dim\mathfrak u(2)$. The framework is therefore below the grand-unification threshold on every count. No group of rank two and dimension four can contain the Standard-Model group, and the algebra supplies no larger intrinsic group.

## The Framework's Own Unification: Electroweak and Abelian

The failure to reach grand unification is not a failure to unify. The algebra does unify its two gauge factors, and the unification is the electroweak one.

The compact sector is

$$
\mathbb M_-=\mathfrak u(2)=\mathfrak{su}(2)\oplus\mathfrak u(1),
$$

and the two summands are the algebra's non-abelian and abelian gauge algebras. A gauge field valued in $\mathbb M_-$ is, in components,

$$
\mathcal A_\mu=\mathcal A_\mu^aT_a+\mathcal A_\mu^0T_0 ,
\qquad
T_a=\tfrac12e_a,\quad T_0=\tfrac12ie_0 ,
$$

so the field content is automatically that of an $SU(2)\times U(1)$ gauge theory: a triplet and a singlet, the $W$ fields and the $B$ field of the electroweak sector. This is the content of the companion research agenda *Electroweak Theory under the Biquaternion Framework — A Research Agenda*, and it is the framework's unification: the two factors that the Standard Model keeps separate are the two summands of the single compact algebra $\mathfrak u(2)$, both generated by the algebra's own elements.

The sense in which this is a unification is precise and limited. It is a unification in the sense that the two gauge potentials are coefficients of one algebra-valued field, and that the generators close in one Lie algebra,

$$
[T_a,T_b]=\varepsilon_{abc}T_c,
\qquad
[T_a,T_0]=0 ,
$$

with $T_0$ central. It is **not** a unification in the sense that the two couplings become one: a central generator can carry its own independent coupling, and the algebra does not identify the $\mathfrak{su}(2)$ and $\mathfrak u(1)$ couplings. The two couplings remain separate parameters of the framework, exactly as the algebra's centre is a separate summand. Unification in the strong sense — one coupling, one simple group — is what grand unification adds, and it is what the ceiling forbids.

**Hypercharge and electric charge.** A consequence that the ceiling fixes is the status of charge quantisation. In a grand-unified theory the hypercharge is a generator of the simple group, and its eigenvalues are therefore quantised by the group's representation theory; the electric charge of every particle is an integer multiple of a basic unit because $Q$ lies in a simple group. In the framework the abelian factor is the centre $\mathbb C_{\mathbb B}$, whose unitary part $U(1)$ has a **continuous** charge; the framework does not, by itself, quantise the hypercharge. Quantisation must be imposed from outside: either by the Dirac condition in the presence of a magnetic charge, as *The Magnetic Monopole in Biquaternionic Form* and *The 't Hooft–Polyakov Monopole in Biquaternionic Form* show, or by embedding the abelian factor into the non-abelian one, which the algebra permits but does not require. The framework therefore *accommodates* charge quantisation but does not *explain* it in the way a simple unified group does. This is a genuine structural difference, and it is the same fact as the non-simplicity of $\mathfrak u(2)$ read as a statement about charges.

## What a Biquaternionic Grand Unification Would Require

The ceiling can be passed by enlarging the carrier, and the cost can be stated exactly. Pass from $\mathbb B$ to the matrix algebra over it,

$$
M_n(\mathbb B)\cong M_{2n}(\mathbb C),
\qquad
\text{compact part}=\mathfrak u(2n),
\qquad
\dim_{\mathbb R}\mathfrak u(2n)=(2n)^2=4n^2,
\qquad
\mathrm{rank}=2n .
$$

The numerical threshold requires rank at least four and dimension at least twelve, and both are met for $n\ge2$: $\mathfrak u(4)$ has rank $4$ and dimension $16$. The numerical threshold is necessary but not sufficient, because the unified group must also contain the Standard-Model group as a subgroup, and containment is a statement about representations as well as dimensions. The carrier $\mathbb C^{2n}$ must contain a faithful representation of the group being embedded, so $2n$ must be at least the dimension of the smallest faithful representation. This gives a higher floor than the numerical one: $SU(3)$ alone fits in $U(4)$, since $\mathbf 3\oplus\mathbf 1=\mathbf 4$; the Standard-Model group fits in $U(6)$, since $\mathbf 3\otimes\mathbf 2=\mathbf 6$; and the standard unified groups fit for larger $n$,

$$
SU(5)\subset U(6)\ (n=3),
\qquad
SO(10)\subset U(10)\ (n=5),
\qquad
E_6\subset U(28)\ (n=14),
$$

where the embedding is the obvious one through the defining representation of the unified group and the identification $\mathbb C^{2n}$ as the carrier. Three costs are attached to every one of these.

- **The group is no longer the algebra's own.** The intrinsic group of $M_n(\mathbb B)$ is $U(2n)$, not $SU(5)$; the unified group appears only as a subgroup of the unitaries, so its selection is an extra input and not a consequence of the algebra. The framework supplies $\mathfrak u(2)$ canonically and $\mathfrak u(2n)$ after enlargement, but never a simple GUT group as its own.
- **Unwanted commuting factors.** $U(2n)$ is locally $SU(2n)\times U(1)$, the two meeting in a $\mathbb Z_{2n}$, and $SU(5)$ sits inside $SU(6)\subset U(6)$ with the commutant $U(1)\times U(1)$ of the split $\mathbb C^6=\mathbf 5\oplus\mathbf 1$, together with further broken generators; the determinant $U(1)$ of the enlarged unitaries is present as well. These must be removed by a mechanism outside the algebra, or they appear as extra gauge bosons. The enlargement therefore brings baggage that the algebra cannot discard.
- **The carrier doubles the module dimension.** The defining module of $M_n(\mathbb B)$ has complex dimension $2n$, which is even; a unified group with an odd-dimensional defining representation, such as $SU(5)$ with its $\mathbf 5$, cannot act irreducibly on it, so the fermions must be placed in reducible combinations. The cost is milder than the colour obstruction was: it is an extra singlet rather than an impossibility, since $\mathbf 5\oplus\mathbf 1=\mathbb C^6$ has even dimension and $SU(5)\subset U(6)$ with $n=3$, while the full generation $\bar{\mathbf 5}\oplus\mathbf{10}$ needs $\mathbb C^{15}$ and so fits only in $\mathbb C^{16}=2n$ with $n=8$, i.e. in $M_8(\mathbb B)$, and then with a further singlet. The module structure of the algebra therefore rules out the economical unified embeddings rather than the existence of an embedding at all.

**Proton decay and the scale.** A unified theory predicts baryon-number violation and proton decay, at a rate set by the unification scale $M_X$ and the unified coupling. The framework, having no simple group and no unified coupling of its own, cannot predict $M_X$; the running of the three couplings and their meeting point are standard quantum field theory, governed by the renormalisation group of the companion article *The Renormalization Group in Biquaternionic Form*, and the framework's role is limited to supplying the gauge fields between which the couplings run. The grand-unification scale is therefore an import, and the framework cannot use proton decay to constrain itself.

## The Representation Content and the Even-Dimension Obstruction

The rank and dimension thresholds are the crude obstructions. The representation content gives a finer one, and it is the obstruction that actually blocks the economical unified embeddings inside an enlarged carrier.

A single generation of the Standard Model in $SU(5)$ sits in

$$
\bar{\mathbf 5}\oplus\mathbf{10} ,
\qquad
\dim_{\mathbb C}=5+10=15 ,
$$

which branches under $SU(3)_c\times SU(2)_L\times U(1)_Y$ as

$$
\bar{\mathbf 5}=(\bar{\mathbf 3},\mathbf 1)_{+1/3}\oplus(\mathbf 1,\mathbf 2)_{-1/2},
\qquad
\mathbf{10}=(\mathbf 3,\mathbf 2)_{+1/6}\oplus(\bar{\mathbf 3},\mathbf 1)_{-2/3}\oplus(\mathbf 1,\mathbf 1)_{+1} ,
$$

the second and third pieces being the up-type antiquark and the positron. In $SO(10)$ the whole generation plus a right-handed neutrino sits in the sixteen-dimensional spinor,

$$
\mathbf{16}=\bar{\mathbf 5}\oplus\mathbf{10}\oplus\mathbf 1 ,
\qquad
\dim_{\mathbb C}=16 .
$$

The hypercharge of the $SU(5)$ embedding is one of the generators of the group, its eigenvalues fixed by the tracelessness of the generator within the five-dimensional representation; the electric charges come out in the observed integer ratios because $Q$ lies in the simple group. This is the sense in which $SU(5)$ *explains* charge quantisation, and it is exactly what the framework cannot reproduce, because its abelian generator is central and its eigenvalue is a continuous label.

Now place a generation in the enlarged carrier $\mathbb C^{2n}$ of $M_n(\mathbb B)$. The representation must be a direct sum of modules of $SU(5)$ plus singlets, and its total complex dimension must be even because $2n$ is even. The generation has dimension $15$, which is odd, so at least one singlet must be added, giving the $\bar{\mathbf 5}\oplus\mathbf{10}\oplus\mathbf 1$ of dimension $16$; the smallest even carrier into which a generation fits is therefore $\mathbb C^{16}$, which is $2n=16$, i.e. $n=8$ and the carrier $M_8(\mathbb B)\cong M_{16}(\mathbb C)$ with intrinsic group $U(16)$. The $\mathbf{16}$ of $SO(10)$ fits the same way, and the $E_6$ $\mathbf{27}$ needs $\mathbb C^{28}$ and $n=14$. The even-dimension property of $\mathbb B$-modules therefore doubles the minimal carrier for the odd-dimensional unified representations and adds a spurious singlet: the framework cannot house a generation economically even after enlargement.

**Alternative unifications and the rank ladder.** The non-simple alternatives do no better. The Pati–Salam group

$$
SU(4)\times SU(2)_L\times SU(2)_R
$$

has rank $3+1+1=5$ and dimension $15+3+3=21$, and it contains the Standard-Model group with $B-L$ as the diagonal of $SU(4)$; the left–right group

$$
SU(3)_c\times SU(2)_L\times SU(2)_R\times U(1)_{B-L}
$$

has rank $2+1+1+1=5$ and dimension $8+3+3+1=15$. Both are above the framework's rank $2$. The rank ladder is

$$
\underbrace{2}_{U(2),\ \text{framework}}<
\underbrace{4}_{G_{\mathrm{SM}},\ SU(5)}<
\underbrace{5}_{SO(10),\ \text{Pati–Salam},\ \text{left–right}}<
\underbrace{6}_{E_6} ,
$$

and every rung above the first is inaccessible to the algebra's intrinsic structure. The framework sits strictly below the lowest unification threshold, and the gap is a property of the algebra and not of any particular model.

## What the Framework's Unification Means for Its Particle Content

The ceiling has a direct consequence for the particle programme, and it is worth stating plainly because it shapes the framework's existing articles.

The Standard-Model gauge group has three factors, and the framework reaches two of them intrinsically. The coloured sector is outside. Therefore a field valued in $\mathbb B$, or in a module of $\mathbb B$, cannot carry colour, and the quarks and gluons do not exist as algebra-valued fields. What does exist is the **colour-singlet content**: the hadrons, and more generally the operators invariant under the outside colour group. The framework's strong-interaction programme is accordingly a programme about the singlet sector, which is the content of the research agenda *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda* and of the ceiling article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*. This is why the framework's gauge articles treat the electroweak and abelian fields directly and the colour sector only through its composites, and why the informational reading of confinement in this corpus is a reading of information loss rather than a derivation of the colour group.

The general structural statement is the following. **The biquaternion algebra unifies the electroweak and abelian gauge interactions, because they are the two summands of its compact algebra $\mathfrak u(2)$; it does not unify them with the strong interaction, because the strong group has rank and dimension beyond any group the algebra carries, and because the algebra's modules have even complex dimension while colour is irreducibly three-dimensional.** Grand unification, in the strict sense of a single simple group and a single coupling, is outside the framework's reach; it is reachable by enlarging the carrier to matrices over the algebra, at the cost of losing the canonicity of the gauge group and of carrying unwanted factors. The framework's unification is electroweak, and this is a structural result about the algebra.

## Summary

Grand unification requires a group of rank at least four and dimension at least twelve containing $SU(3)_c$, with the correct representation content. The biquaternion algebra's intrinsic compact gauge structure is $\mathfrak u(2)=\mathfrak{su}(2)\oplus\mathfrak u(1)$, of rank two and dimension four, which fails both numerical thresholds and does not contain $SU(3)_c$:

$$
\mathrm{rank}\,U(2)=2<4=\mathrm{rank}\,G_{\mathrm{SM}},
\qquad
\dim_{\mathbb R}U(2)=4<12=\dim G_{\mathrm{SM}} .
$$

The framework does unify its two gauge factors, and the unification is electroweak: the $W$ triplet and the $B$ singlet are the coefficients of a single $\mathbb M_-$-valued field, and their generators close in one Lie algebra with $[T_a,T_b]=\varepsilon_{abc}T_c$ and $[T_a,T_0]=0$. But the two couplings remain separate, because the abelian factor is central and the algebra is not simple; and the framework does not quantise the hypercharge by itself, since the central $U(1)$ has continuous charge, so quantisation must be imposed through the Dirac condition or through embedding into the non-abelian factor.

A biquaternionic grand unification would require enlarging the carrier to $M_n(\mathbb B)\cong M_{2n}(\mathbb C)$, whose intrinsic group $\mathfrak u(2n)$ has rank $2n$ and dimension $4n^2$ and contains $SU(3)\times SU(2)\times U(1)$ for $n\ge3$ and $SU(5),SO(10),E_6$ from the defining representations of dimensions $5,10,27$, that is for $n=3,5,14$. The costs are that the gauge group ceases to be the algebra's own, that unwanted commuting factors appear, and that the even-dimensional modules obstruct the odd-dimensional unified representations. The proton-decay scale is therefore an import, and the framework's particle programme is a programme about colour singlets. The framework's unification is electroweak and not grand, and this is a structural result about the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H\cong M_2(\mathbb C)$ | Biquaternion algebra |
| $\mathbb M_-=\mathrm{span}_{\mathbb R}\{ie_0,e_1,e_2,e_3\}=\mathfrak u(2)$ | Compact sector; intrinsic gauge algebra |
| $\mathfrak{su}(2)\oplus\mathfrak u(1)$ | Decomposition; electroweak and abelian factors |
| $T_a=\tfrac12e_a$, $T_0=\tfrac12ie_0$ | Generators; $[T_a,T_b]=\varepsilon_{abc}T_c$, $[T_a,T_0]=0$ |
| $S\cong\mathbb C^2$ | Defining module; $\dim_{\mathbb C}=2r$ for any module |
| $G_{\mathrm{SM}}=SU(3)_c\times SU(2)_L\times U(1)_Y$ | Standard-Model gauge group |
| $Y$, $T_3$, $Q=T_3+Y$ | Hypercharge, weak isospin, electric charge |
| $SU(5)$, $SO(10)$, $E_6$ | Grand-unified candidates; ranks $4,5,6$; dimensions $24,45,78$ |
| $M_n(\mathbb B)\cong M_{2n}(\mathbb C)$ | Enlarged carrier; compact part $\mathfrak u(2n)$ |
| $2n$, $(2n)^2$ | Rank and dimension of $\mathfrak u(2n)$ |
| $\bar{\mathbf 5}\oplus\mathbf{10}$, $\mathbf{16}$, $\mathbf{27}$ | Unified fermion representations |
| $M_X$ | Grand-unification scale; imported |

## Further Reading

- Howard Georgi and Sheldon L. Glashow, "Unity of all elementary-particle forces", *Physical Review Letters* 32 (1974) 438–441, for the $SU(5)$ grand-unified theory and the fermion representations.
- Harald Fritzsch and Peter Minkowski, "Unified interactions of leptons and hadrons", *Annals of Physics* 93 (1975) 193–266, for the $SO(10)$ unification and the $\mathbf{16}$ spinor.
- Jogesh C. Pati and Abdus Salam, "Lepton number as the fourth colour", *Physical Review D* 10 (1974) 275–289, for the $SU(4)\times SU(2)\times SU(2)$ unification.
- F. Gürsey, Pierre Ramond and P. Sikivie, "A universal gauge theory model based on $E_6$", *Physics Letters B* 60 (1976) 177–180, for the $E_6$ unification.
- Howard Georgi, *Lie Algebras in Particle Physics* (Westview, 2nd ed. 1999), for the rank and dimension counting of the unified groups and their representations.
- R. Slansky, "Group theory for unified model building", *Physics Reports* 79 (1981) 1–128, for the branching rules and representation content of the unified models.
- Andrzej J. Buras, "Weak Hamiltonian, CP violation and rare decays", in *Probing the Standard Model of Particle Physics* (Cambridge University Press, 1998), for the running of the couplings and the unification scale.
- Steven Weinberg, "The quantum theory of fields", Vol. II (Cambridge University Press, 1996), for the renormalisation-group analysis of gauge couplings and the grand-unification threshold.
- Frank Wilczek and Anthony Zee, "Operator analysis of nucleon decay", *Physical Review Letters* 43 (1979) 1571–1573, for proton decay and the baryon-number-violating operators.
- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* 39 (2002) 145–205, for the division-algebraic routes to the unified groups and the role of the exceptional algebras.
