# __The Electroweak Gauge Group and the Hypercharge Assignment__

## Introduction

**The claim.** The electroweak factor of the Standard Model is $SU(2)_L\times \mathrm{U}(1)_Y$, and the hypercharges of the fifteen fields of one generation are not chosen one by one. They are the solution of a system of four equations, and the system has exactly three solution rays. This article writes the group, writes the system, solves it, and shows that one of the three rays is the observed assignment and one is excluded.

**The standing.** The group and the assignment are standard theory. Nothing here is derived from the biquaternion algebra, and §*Why the Assignment Is Not Derivable Here* says why in the sharpest form the corpus allows. What the article supplies is the computation in full, in exact arithmetic, in the corpus's notation.

**Why the assignment deserves its own article.** Three statements circulate about hypercharge and all three are loose.

- **That the hypercharges are arbitrary.** They are not. Four anomaly conditions constrain five numbers, and the constraint is strong enough to leave three rays.
- **That they are fixed by anomaly cancellation alone.** They are not. Anomaly freedom leaves a continuous freedom, and the discrete choice among the rays is made by the electric charges, which are measured.
- **That the assignment follows from the gauge group.** It does not. The group is silent on which field is a doublet and which is a singlet, and silent on the charges.

The article makes all three statements precise.

**The strongest objection, named at the start.** A computation that reproduces a known table proves nothing about the framework, and this article does not claim otherwise. The computation's value is that it removes a false freedom: it shows how much the model really leaves open. That number — two continuous parameters and one discrete choice, not five independent numbers — is the input to the ledger of [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html).

**The order.** The group and its two couplings; the three labels and the charge; the anomaly system derived rather than quoted; its linear part solved; the cubic and the three rays; what the conditions leave free; the Witten condition; the scalar's hypercharge and the chain that follows from it; and the framework's position.

## The Group and Its Two Couplings

**The group.** The electroweak factor is the product

$$
SU(2)_L\times \mathrm{U}(1)_Y ,
$$

of a compact simple group and a compact abelian group. The two factors carry two independent couplings, $g$ and $g_{\mathrm Y}$, and the model supplies no relation between them. The ratio $g_{\mathrm Y}/g$ is the Weinberg angle, and it is measured rather than computed.

**Why the subscript $L$.** The $SU(2)$ factor acts on left-handed fields and not on right-handed ones. Every left-handed doublet has $T=\tfrac12$; every right-handed field is a singlet. This asymmetry is the whole reason a chiral gauge theory has anomalies at all, and it is why the conditions of §*The Anomaly System* are a system rather than a tautology.

**Why the abelian factor is chiral too.** The hypercharge of a left-handed field and the hypercharge of its right-handed partner are different numbers. For the electron, $Y_L=-\tfrac12$ and $Y_R=-1$. A vector-like abelian factor would assign the same charge to both, and the corpus's own central phase does exactly that, which is the substance of §*Why the Assignment Is Not Derivable Here*.

**The algebra of the group is $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$.** The Lie algebra is a direct sum, and the algebra alone therefore cannot distinguish $SU(2)\times\mathrm{U}(1)$ from $\mathrm{U}(2)$, whose algebra is the same. The two differ in global structure and in the charge assignment, and the difference is exactly what the anomaly conditions constrain.

**What the group does not say.** Three things are outside the group and inside the model.

| Question | Where the answer comes from |
|---|---|
| Which of the fifteen fields is a doublet, which a singlet | the representation content, an input |
| What $Y$ each field carries | the anomaly conditions and the measured charges |
| What the ratio $g_{\mathrm Y}/g$ is | measurement, the Weinberg angle |

**The covariant derivative carries both.** Its action on a field of hypercharge $Y$ in the representation $\tau$ of $SU(2)_L$ is

$$
D_\mu\psi=\frac{\partial\psi}{\partial R_\mu}+i\,g\sum_a\tau_aW^a_\mu\psi+i\,g_{\mathrm Y}Y B_\mu\psi ,
$$

and the product $g_{\mathrm Y}Y$ is what appears. That product is the reason the overall scale of $Y$ is not a physical quantity, as §*What the Conditions Do Not Fix* shows.

**The canonical normalisation.** A theory is normally written with the kinetic terms $-\tfrac14\sum W^aW^a$ and $-\tfrac14\sum BB$ both of unit coefficient. That fixes the normalisation of the two gauge fields and hence splits the product $g_{\mathrm Y}Y$ into a coupling and a charge. The split is a convention: the covariant derivative carries the product $g_{\mathrm Y}Y$ and not the two factors separately, so the rescaling $Y\mapsto\lambda Y$ with $g_{\mathrm Y}\mapsto g_{\mathrm Y}/\lambda$ moves a number between the coupling and the charge and changes nothing else. $B_\mu$ is not rescaled in that operation, which is why the field strength $B_{\mu\nu}$ and the kinetic term $-\tfrac14\sum BB$ come through untouched. Rescaling $B_\mu$ as well would rescale the kinetic term by $\lambda^{-2}$ and would have to be undone by changing its coefficient, which is exactly the freedom the canonical normalisation removes.

## The Three Labels and the Charge

**The labels.** A field is placed by its colour representation, its weak representation and its hypercharge. The first two are discrete; the third is a real number. The electric charge is not a fourth label: it is the combination

$$
Ϙ=Y+T_3
$$

in units of the elementary charge, with $T_3=\pm\tfrac12$ in a doublet and $T_3=0$ in a singlet.

**The table.** The content of one generation, with the charge computed from the two labels and the hypercharge doubled in the last column for comparison with the reference checklist, which writes $Y_W=2Y$.

| Field | $SU(3)_c$ | $SU(2)_L$ | $T_3$ | $Y$ | $Ϙ$ | $Y_W=2Y$ |
|---|---|---|---|---|---|---|
| $u_L$ | $3$ | $2$ | $+1/2$ | $1/6$ | $2/3$ | $1/3$ |
| $d_L$ | $3$ | $2$ | $-1/2$ | $1/6$ | $-1/3$ | $1/3$ |
| $u_R$ | $3$ | $1$ | $0$ | $2/3$ | $2/3$ | $4/3$ |
| $d_R$ | $3$ | $1$ | $0$ | $-1/3$ | $-1/3$ | $-2/3$ |
| $\nu_L$ | $1$ | $2$ | $+1/2$ | $-1/2$ | $0$ | $-1$ |
| $e_L$ | $1$ | $2$ | $-1/2$ | $-1/2$ | $-1$ | $-1$ |
| $e_R$ | $1$ | $1$ | $0$ | $-1$ | $-1$ | $-2$ |

**Five independent numbers, not fifteen.** The seven rows carry five distinct hypercharges, since the two members of a doublet share one. Those five are the five unknowns of the next section. The charges are then seven numbers computed from five, and the two relations among them are the reason a chiral theory can exist at all.

**The unit is one sixth.** Every hypercharge in the table is an integer multiple of $\tfrac16$, and $\tfrac16$ is the smallest multiple that occurs. That is not a coincidence of the fractions chosen. It is what an embedding into a simple group would supply: inside a simple group the hypercharge is one generator among the others, its eigenvalues are fixed by tracelessness within a representation, and they therefore sit on a rational lattice with a common denominator. $SU(5)$ gives exactly the sixths, with $g_1=\sqrt{5/3}\,g_{\mathrm Y}$. [Grand Unification and the Biquaternion Algebra Ceiling](grand-unification-and-the-biquaternion-algebra-ceiling.html) carries the argument and states the negative half of it, which §*What the Conditions Do Not Fix* repeats: the framework's own abelian factor is central and continuous, so it does not quantise anything, and the sixths are inherited with the model rather than forced by any condition used here.

**The two conventions, and the one that is not a convention.** Writing $Q$ for $Y+T_3$ and writing $Y=Q-T_3$ are the same statement; the first is used here because it makes the hypercharge the unknown. The comparison with the GUT-normalised coupling, $g_1=\sqrt{5/3}\,g_{\mathrm Y}$, is a convention about the relative normalisation of the three couplings and not a physical statement. The corpus writes $g_{\mathrm Y}$ and never $g_1$ outside the context of unification.

**The charge audit.** Recomputing the seven charges from the two labels in exact rational arithmetic gives the column above. The audit is short and it is a tautology once the hypercharges are given; what is not a tautology is the next section.

## The Anomaly System

**Why a chiral theory needs conditions.** A gauge symmetry whose left- and right-handed couplings differ can be broken by the quantum measure. The failure is the triangle diagram with three gauge currents, and its coefficient is a sum over the left-handed Weyl fields minus the same sum over the right-handed ones. [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) derives the coefficient, proves the three lemmas below and verifies the conditions on the observed assignment. This article organises the same material as a system to be solved, which that article does not do.

**The coefficient.** For generators $T_a$ acting on a left-handed Weyl field in the representation $R$,

$$
A_{abc}(R)=\mathrm{Tr}_R\big[T_a\{T_b,T_c\}\big] ,
\qquad
\sum_{\text{left}}A_{abc}(R)-\sum_{\text{right}}A_{abc}(R)=0 .
$$

A right-handed field in $R$ contributes as a left-handed field in the conjugate $\bar R$, which is why the second sum can be folded into the first by reversing each right-handed hypercharge. Both writings are used below, and the difference between them is the commonest source of sign errors in this computation.

**Three lemmas, each one line.**

- **$SU(2)$ has no cubic invariant.** For any representation, $\{T_b,T_c\}=\tfrac12\delta_{bc}\mathrm I$ in the fundamental, so $T_a\{T_b,T_c\}=\tfrac12\delta_{bc}T_a$, whose trace vanishes because every $SU(2)$ generator is traceless. Since every $SU(2)$ representation is real or pseudoreal, the same holds for all of them. Hence $SU(2)_L^3$ vanishes identically, whatever the fermion content.
- **A single trace vanishes whenever at most one non-abelian generator is present.** A condition with one non-abelian generator and two abelian ones is $Y^2\mathrm{Tr}\,[T_a]$, and one with one colour, one weak and one abelian generator is $Y\,\mathrm{Tr}\,[T_a^c]\,\mathrm{Tr}\,[T_b^L]$. Both single traces vanish, so both families do. The conditions that survive are the ones with a *pair* of generators of the same factor, where $\mathrm{Tr}\,[T_aT_b]\propto\delta_{ab}$ does not vanish and the content enters through one power of $Y$: those are the $SU(3)_c^2$ and $SU(2)_L^2$ rows below. This split is the reason the list is four and not two.
- **The colour cubic cancels because the colour content is vector-like.** With $A(3)=1$ and $A(\bar3)=-1$, the quark doublet supplies $2A(3)$ from its two components and the two right-handed quarks supply $-A(3)$ each, so $2A(3)-A(3)-A(3)=0$.

**The four surviving conditions.** Three are linear in the hypercharges and one is cubic. Written in the hypercharges of the table, so that $Y_u$, $Y_d$ and $Y_e$ are the values the singlets carry,

$$
\underbrace{2Y_Q-Y_u-Y_d=0}_{SU(3)_c^2\,\mathrm{U}(1)_Y},
\qquad
\underbrace{3Y_Q+Y_L=0}_{SU(2)_L^2\,\mathrm{U}(1)_Y},
$$

$$
\underbrace{6Y_Q-3Y_u-3Y_d+2Y_L-Y_e=0}_{\text{gravitational}},
\qquad
\underbrace{6Y_Q^3-3Y_u^3-3Y_d^3+2Y_L^3-Y_e^3=0}_{\mathrm{U}(1)_Y^3}.
$$

The coefficients are the multiplicities: the quark doublet is six states, each quark singlet three, the lepton doublet two and the charged-lepton singlet one.

**The same conditions in the left-handed writing.** A right-handed field replaced by its conjugate reverses its hypercharge, so with $Y^{\mathrm c}_u=-Y_{u_R}$, $Y^{\mathrm c}_d=-Y_{d_R}$ and $Y^{\mathrm c}_e=-Y_{e_R}$ every right-handed minus sign becomes a plus sign: $2Y_Q+Y^{\mathrm c}_u+Y^{\mathrm c}_d=0$, $3Y_Q+Y_L=0$, $6Y_Q+3Y^{\mathrm c}_u+3Y^{\mathrm c}_d+2Y_L+Y^{\mathrm c}_e=0$ and $6Y_Q^3+3(Y^{\mathrm c}_u)^3+3(Y^{\mathrm c}_d)^3+2Y_L^3+(Y^{\mathrm c}_e)^3=0$. Both writings hold on the observed assignment and neither holds on a mixture of the two. The mixture is the trap: the minus-sign form applied to a conjugate hypercharge, or the plus-sign form applied to a table hypercharge, gives $2Y_Q+Y_{u_R}+Y_{d_R}=\tfrac23$ instead of $0$, which is the arithmetic every reader of this section makes once.

**The matrix.** With $y=(Y_Q,Y_u,Y_d,Y_L,Y_e)^{\mathsf T}$ the linear part is $M\,y=0$ with

$$
M=\begin{pmatrix}
2 & -1 & -1 & 0 & 0\\
3 & 0 & 0 & 1 & 0\\
6 & -3 & -3 & 2 & -1
\end{pmatrix} .
$$

The rows are independent, so the rank is three and the solution space is two-dimensional. That number is the whole reason a continuous freedom survives.

**Why the gravitational condition is not a consequence of the other two.** A reader may suspect redundancy, since row three resembles a combination of rows one and two. It does not: rows one and two fix $Y_u+Y_d$ and $Y_L$, and row three then fixes $Y_e$ independently. Removing it would leave $Y_e$ free, and a free $Y_e$ is not what the model has.

## The Solution of the Linear System

**The two parameters.** The null space is spanned by two vectors, written here in the basis $(Y_Q,Y_u,Y_d,Y_L,Y_e)$:

$$
\mathbf p=(1,1,1,-3,-6),
\qquad
\mathbf q=(0,1,-1,0,0).
$$

The general solution is $y=p\,\mathbf p+q\,\mathbf q$, that is

$$
Y_Q=p ,
\qquad
Y_u=p+q ,
\qquad
Y_d=p-q ,
\qquad
Y_L=-3p ,
\qquad
Y_e=-6p .
$$

**The meaning of the two parameters.** $p$ sets the scale of the doublet hypercharges and of everything tied to them; $q$ splits the two quark singlets and nothing else. The lepton sector has no $q$: the lepton doublet hypercharge is fixed by the weak condition and the charged-lepton hypercharge by the gravitational one, both in terms of $p$ alone.

**The check.** Substituting the parametrisation into the three linear conditions gives zero identically, in exact arithmetic, for every rational $p$ and $q$. Substituting the observed assignment, $p=\tfrac16$ and $q=\tfrac12$, gives $(\tfrac16,\tfrac23,-\tfrac13,-\tfrac12,-1)$, which is the table of §*The Three Labels and the Charge*.

**The shape of the freedom.** The two-parameter family is not a small residual: it is the freedom to rescale all hypercharges and to tilt the quark singlets against each other. The cubic removes both, and it removes them in a way that can be written in closed form.

## The Cubic and the Three Rays

**The substitution.** On the solution space the cubic becomes a function of $p$ and $q$ alone. Substituting $Y_Q=p$, $Y_u=p+q$, $Y_d=p-q$, $Y_L=-3p$ and $Y_e=-6p$ and expanding,

$$
6Y_Q^3-3Y_u^3-3Y_d^3+2Y_L^3-Y_e^3
=18\,p\,\bigl(9p^2-q^2\bigr).
$$

**The proof is the expansion, and the check is exact.** The identity holds for every $p$ and $q$, and it was verified in exact rational arithmetic on a grid of values with denominator six, with no discrepancy. The five terms expand to $6p^3$, $-3(p^3+3p^2q+3pq^2+q^3)$, $-3(p^3-3p^2q+3pq^2-q^3)$, $2(-3p)^3=-54p^3$ and $-(-6p)^3=+216p^3$; the mixed terms cancel between $Y_u^3$ and $Y_d^3$, and the remainder is $6p^3-6p^3-18pq^2-54p^3+216p^3=162p^3-18pq^2=18p(9p^2-q^2)$.

**The same statement in the other parametrisation.** Article 1 of this series solves the same system in the variables $a=Y_u$ and $b=Y_d$, where the three linear conditions give $Y_Q=\tfrac12(a+b)$, $Y_L=-\tfrac32(a+b)$ and $Y_e=-3(a+b)$, and the cubic becomes $a^3+b^3=7(a+b)^3$. The two forms are the same equation: with $a=p+q$ and $b=p-q$ the left side is $2p(p^2+3q^2)$ and the right side is $56p^3$, whose difference is $-6p(9p^2-q^2)$, that is $-\tfrac13$ times $18p(9p^2-q^2)$. The two routes share the linear solution and the three rays; they differ in which variable makes the factorisation visible. The form below is preferred here because the three factors correspond one to one with the three rays.

**The factorisation.** The cubic therefore factors completely,

$$
18\,p\,(3p-q)\,(3p+q)=0 ,
$$

and the solution set is the union of three lines through the origin. Each line is one ray, so the system has exactly three solutions up to scale:

| Ray | Condition | $(Y_Q,Y_u,Y_d,Y_L,Y_e)$ at $p=\tfrac16$ | Status |
|---|---|---|---|
| first | $q=3p$ | $(\tfrac16,\tfrac23,-\tfrac13,-\tfrac12,-1)$ | the observed assignment |
| second | $q=-3p$ | $(\tfrac16,-\tfrac13,\tfrac23,-\tfrac12,-1)$ | the observed assignment with $u$ and $d$ interchanged |
| third | $p=0$ | $(0,q,-q,0,0)$ | excluded |

**Why the third ray is excluded.** On it $Y_Q=0$, so the quark doublet carries charge $Ϙ=T_3+0=\pm\tfrac12$, and the lepton doublet likewise, whatever $q$ is. The observed quark charges are $\tfrac23$ and $-\tfrac13$. The exclusion is by measurement and not by consistency: the third ray is anomaly-free and would give a consistent theory of the wrong charges.

**Why the second ray is not a separate solution.** It differs from the first by the interchange of $u$ and $d$, which is a relabelling of two fields. With the labels fixed by the measured charges, only the first ray applies.

**What has been established.** Four conditions on five unknowns leave three rays, and the observed charges select one. So the assignment is determined by the anomaly conditions together with the measured charges, up to the overall scale. That is the precise content of the statement that the hypercharges are not arbitrary.

**The three rays in one sentence.** Two are the observed assignment with the quarks labelled one way or the other, and the third is the assignment in which both doublets are half-integrally charged.

## What the Conditions Do Not Fix

**The overall scale.** The system is homogeneous, so it fixes rays and not points. On the first ray the assignment is $Y=p\,(1,4,-2,-3,-6)$, with $p=\tfrac16$ in the table.

**The scale is not physical.** Physics depends on $Y$ only through $g_{\mathrm Y}Y$, so the rescaling $Y\mapsto\lambda Y$, $g_{\mathrm Y}\mapsto g_{\mathrm Y}/\lambda$ is a field redefinition that changes nothing. The scale is fixed by a convention. The standard convention sets $Y=-\tfrac12$ for the lepton doublet, or equivalently $Y=-1$ for the right-handed electron, which is the choice that makes $Q=Y+T_3$ give integral charges for the observed leptons. *A different convention would change every number in the table and no observable.*

**What the scale is not.** It is tempting to say that the scale is fixed by the measured electron charge, and article 1 of this series says it in that form. The sharper statement is that the electron charge is measured and the convention is chosen so that the charge formula reproduces it; the physical content is the ratio of the two couplings and the fact that the charges are quantised as they are.

**The number of generations.** The conditions are satisfied generation by generation, since each generation is a complete copy. They therefore say nothing about how many copies there are. [The Number of Generations and the Biquaternion Algebra](the-number-of-generations-and-the-biquaternion-algebra.html) records that the three is accommodated and not derived.

**Anomaly freedom is necessary and not sufficient.** Adding a vector-like pair of fields — a doublet and its conjugate, with opposite hypercharges — preserves all four conditions and changes the content. The conditions therefore do not select the content; they constrain it. What selects the content is the measurement of which fields exist.

**The quantisation.** The conditions constrain the hypercharges but do not force them to be rational, let alone multiples of $\tfrac16$. The sixths are a consequence of the standard normalisation convention together with the measured charges; the anomaly system alone would admit irrational solutions on each ray, and no experiment distinguishes a rational assignment from an irrational one rescaled.

**The mixed $\mathrm{U}(1)$ question.** If the model contained a second abelian factor, its kinetic term could mix with $B_\mu$, and the anomaly system would have more unknowns. The Standard Model has one, and the absence of kinetic mixing is a property of the content rather than a derived fact.

## The Witten Condition

**A second kind of anomaly.** Besides the perturbative triangle anomaly there is a global obstruction: an $SU(2)$ gauge theory with an odd number of left-handed doublets is inconsistent, because the fermion determinant changes sign under a large gauge transformation. The condition is not a triangle coefficient and is not found by the computation above.

**The count.** Each generation supplies four weak doublets: three from the colour triplet of $Q_L$ and one from $L_L$. Four is even. With three generations the count is twelve, also even.

**The check is satisfied and is not automatic.** A model with one generation of a single coloured quark doublet and no lepton doublet would violate it. The Standard Model's content satisfies it because colour multiplies the quark doublet by three and the lepton doublet adds one, so the parity is that of $N_c+1$ per generation, which is even for $N_c=3$.

**Why it belongs in this article.** The Witten condition is a constraint on the same assignment that the triangle conditions constrain, and a reader who solves the triangle system and stops would miss it. It is the one place where the number of colours enters a consistency condition rather than a coupling.

## The Scalar's Hypercharge, and the Chain

**The scalar is not in the anomaly system.** The doublet $\varphi$ is a boson, so it contributes to no triangle coefficient. Its hypercharge is fixed by a different requirement: the Yukawa couplings must be gauge invariant.

**The requirement.** For the charged-lepton mass the invariant term is $\bar L_L\varphi\,e_R$. Its total hypercharge must vanish, and a barred field carries the negative of the hypercharge of the unbarred one, so

$$
-Y_{L_L}+Y_\varphi+Y_{e_R}=0 ,
\qquad
Y_\varphi=Y_{L_L}-Y_{e_R}=-\tfrac12-(-1)=+\tfrac12 .
$$

That is the value in the table, and it is the value the rest of the series uses. The conjugate $\tilde\varphi$ carries $-\tfrac12$; it is the object with the opposite hypercharge, not a second field.

**The up-type term needs the conjugate.** With $\varphi$ alone the up-type term would carry total hypercharge $-\tfrac16+\tfrac12+\tfrac23=+1$. The conjugate doublet $\tilde\varphi$ carries $-\tfrac12$ and repairs it. The scalar sector therefore contains one field and two objects, and the object with hypercharge $-\tfrac12$ is not a second field.

**The chain, stated once.** The whole assignment follows from four steps, and no step is a free choice beyond the two the model really has:

| Step | Input | Output |
|---|---|---|
| one | the group and the representation content | the five unknowns |
| two | the four anomaly conditions | three rays |
| three | the measured charges | the ray, and the scale by convention |
| four | the invariance of the Yukawa terms | $Y_\varphi=\tfrac12$, $Y_{\tilde\varphi}=-\tfrac12$ |

**What follows from the last step.** With $Y_\varphi=\tfrac12$ the scalar's neutral component has $T_3=-\tfrac12$ and $Ϙ=0$, so the vacuum expectation value can sit in the neutral component and leave the photon massless. The tree-level relation $\rho=1$ follows from the doublet being a doublet. Both are computed in [Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-gauge-boson-masses.html), and the point here is that they follow from the assignment and not from an extra postulate.

**The neutrino charge.** With $Y_L=-\tfrac12$ and $T_3=+\tfrac12$ the neutrino comes out neutral, and that is a consequence of the assignment rather than an input to it. A reader who takes the neutrality of the neutrino as the starting point will find that it is one equation short of the whole table.

## Why the Assignment Is Not Derivable Here

**Three facts about the framework, each established in a companion article.**

- **The framework's abelian factor is the central phase.** The gauge principle of [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) supplies the $*$-unitary part of the centre, which is $\mathrm{U}(1)$, and a charge parameter $ϙ$ that multiplies every coefficient of a state by the same phase.
- **That phase is vector-like.** Because the phase acts as a scalar, a state and its partner of the opposite chirality carry the same charge, so the cubic sum is $ϙ^3-ϙ^3=0$ identically, for every state and every charge. [Anomalies and Anomaly Cancellation](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) states this as the algebraic fact that the framework's abelian factor cannot be weak hypercharge.
- **The framework's compact factor is $SU(2)$ and not $SU(3)$.** [The Gauge Group Ceiling](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) proves that the algebra's intrinsic compact gauge algebra is $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, of real dimension four, and that no module of $\mathbb{B}$ carries a colour triplet.

**The consequence.** The framework reaches the *algebra* of the electroweak group, since $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$ is exactly the algebra of $SU(2)_L\times\mathrm{U}(1)_Y$. It does not reach the *assignment*, for two reasons that are worth separating.

- **It has one abelian charge, and the model needs two per field.** The chiral assignment requires $Y_L\neq Y_R$ for a single species. One central charge per state cannot supply two numbers for one species.
- **It has no representation content.** Even given the group, which field is a doublet is not an algebraic fact about $\mathbb{B}$. The content is an input of the model, and the framework inherits it with the group.

**What a derivation would need.** Not a larger algebra, and not a different group. What is needed is a structure that assigns different charges to the two sides of an element: an abelian generator whose left action and right action differ. The corpus's operator chirality is a slot, and a slot is precisely the kind of object that could carry two charges. [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) records the non-central case as the open question, and this article does not settle it.

**The sharpest form of the boundary.** The framework supplies the arena in which the electroweak group's algebra is written, and it supplies neither the content nor the charges. The assignment is therefore imported whole, and the computation of this article is a computation about the model that the framework inherits, not a computation about the framework.

**Why the computation is still worth doing here.** Because the ledger needs it. A boundary statement that says *hypercharge is imported* is weaker than one that says *hypercharge is imported, and it is two continuous parameters and one discrete choice, fixed by four conditions and three measured charges*. The second statement is what [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html) can use.

## Summary

The electroweak group is $SU(2)_L\times\mathrm{U}(1)_Y$, with two independent couplings $g$ and $g_{\mathrm Y}$ and the same Lie algebra as $\mathrm{U}(2)$. The electric charge is $Ϙ=Y+T_3$, so the seven charges of one generation follow from five hypercharges, and every hypercharge is an integer multiple of $\tfrac16$.

The five hypercharges are the solution of four anomaly conditions: the $SU(3)_c^2\,\mathrm{U}(1)_Y$, $SU(2)_L^2\,\mathrm{U}(1)_Y$ and gravitational conditions, which are linear, and the $\mathrm{U}(1)_Y^3$ condition, which is cubic. The $SU(2)_L^3$ condition and every condition with at most one non-abelian generator vanish identically — the first because $SU(2)$ has no cubic invariant and every $SU(2)$ generator is traceless, the rest because each factorises a single trace, $Y^2\mathrm{Tr}\,[T_a]$ or $Y\,\mathrm{Tr}\,[T_a^c]\,\mathrm{Tr}\,[T_b^L]$, and both single traces vanish. The two conditions with a pair of generators of one factor survive because $\mathrm{Tr}\,[T_aT_b]\propto\delta_{ab}$ does not, and the $SU(3)_c^3$ condition cancels because the colour content of the quarks is vector-like, $2A(3)-A(3)-A(3)=0$.

The linear system has rank three on five unknowns, so its solution space is two-dimensional, spanned by $(1,1,1,-3,-6)$ and $(0,1,-1,0,0)$. In the parameters $p$ and $q$ of that space the cubic becomes $18p(9p^2-q^2)$, which factors exactly as $18p(3p-q)(3p+q)$. The solution set is therefore three rays: $q=3p$, which is the observed assignment; $q=-3p$, which is the same assignment with up and down interchanged; and $p=0$, which is excluded because it makes both doublets half-integrally charged. The measured charges select the first, and the overall scale is a convention traded against the normalisation of $g_{\mathrm Y}$, not a physical quantity.

Beyond the triangle conditions stands the Witten condition, that the number of left-handed doublets be even. Each generation supplies $N_c+1=4$, so the content satisfies it, and the condition is the one place where the number of colours enters a consistency requirement rather than a coupling.

The scalar's hypercharge is not part of the anomaly system, since a boson contributes no triangle coefficient. It is fixed by the invariance of the Yukawa terms, $-Y_{L_L}+Y_\varphi+Y_{e_R}=0$ and so $Y_\varphi=Y_{L_L}-Y_{e_R}=+\tfrac12$, and with it the neutral component can carry the vacuum expectation value and leave the photon massless. The chain is: content, then four anomaly conditions, then the measured charges, then Yukawa invariance.

The framework reaches the algebra of the group and not the assignment. Its abelian factor is the central phase, which multiplies both chiralities by the same charge and is therefore vector-like, with the cubic sum vanishing identically; and its representation content is an input. A derivation would need an abelian generator whose left and right actions differ, which is the non-central case that [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) records as open. The assignment is imported, and what this article adds to that statement is its exact size: two continuous parameters and one discrete choice, constrained by four conditions and selected by three measured charges.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $SU(2)_L\times\mathrm{U}(1)_Y$ | The electroweak gauge group |
| $g$, $g_{\mathrm Y}$ | The weak and hypercharge couplings; $\tan\theta_W=g_{\mathrm Y}/g$ |
| $T_3$ | Third weak-isospin eigenvalue, $\pm\tfrac12$ in a doublet, $0$ in a singlet |
| $Y$ | Hypercharge; the reference checklist writes $Y_W=2Y$ |
| $Ϙ=Y+T_3$ | The electric charge in units of the elementary charge |
| $ϙ$ | The framework's central charge parameter |
| $Y_Q$, $Y_L$ | Hypercharges of the quark and lepton doublets, in the convention of the table |
| $Y_u$, $Y_d$, $Y_e$ | Hypercharges of the three singlets, reversed when a right-handed field is written as a conjugate |
| $A_{abc}(R)=\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ | The triangle coefficient |
| $A(3)$, $A(\bar3)$ | Cubic colour Casimirs, $+1$ and $-1$ |
| $M$ | The $3\times5$ matrix of the linear anomaly conditions |
| $p$, $q$ | The two parameters of the linear solution space |
| $Y_\varphi=\tfrac12$, $Y_{\tilde\varphi}=-\tfrac12$ | Hypercharges of the scalar doublet and its conjugate |
| $\mathbf p=(1,1,1,-3,-6)$, $\mathbf q=(0,1,-1,0,0)$ | Basis of the linear solution space |

## Further Reading

- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The content this assignment is written for, and the charge table the solution reproduces.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The derivation of the triangle coefficient, the three lemmas, and the verification of the conditions on the observed spectrum.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html). The central phase and the charge parameter $ϙ$.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The intrinsic compact algebra $\mathfrak{su}(2)\oplus\mathfrak{u}(1)$ and the colour ceiling.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html). Why a central charge cannot be chiral, and the non-central case as the open question.
- [The Standard Model Lagrangian Assembled: Four Sectors in One Expression](the-standard-model-lagrangian-assembled-four-sectors-in-one-expression.html). The covariant derivative and the Yukawa terms whose invariance fixes $Y_\varphi$.
- [The Standard Model under the Biquaternion Framework — A Research Agenda](the-standard-model-under-the-biquaternion-framework-a-research-agenda.html). The same boundary in agenda form.

The two companions this article leans on most — [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html), which consumes the count of two continuous parameters and one discrete choice, and [Grand Unification and the Biquaternion Algebra Ceiling](grand-unification-and-the-biquaternion-algebra-ceiling.html), which carries the quantisation argument of §*The Three Labels and the Charge* — are both in the corpus, and both are linked above at the point where they are used.
