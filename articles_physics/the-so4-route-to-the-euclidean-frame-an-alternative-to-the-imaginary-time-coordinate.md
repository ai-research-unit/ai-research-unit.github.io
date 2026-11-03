# __The SO(4) Route to the Euclidean Frame: An Alternative to the Imaginary Time Coordinate__

## Introduction

The corpus sets its frame with a complex coordinate. In the $\mathbb{B}$ frame the four coefficients of an element are $Q_\mu\in\mathbb{C}$, the interval is

$$
\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural=Q_t^2+Q_x^2+Q_y^2+Q_z^2 ,
$$

with four $+1$ coefficients, and the Lorentzian sign is not in the form at all: it appears only when a sector is imposed, and on the material sector the one substitution $Q_t=ict'$ puts it in the coordinate. The Euclidean form is a consequence of a complex structure, and that complex structure is the central imaginary $i$ of the algebra.

A second route reaches the same form and never introduces an $i$. It takes the **real** four-dimensional rotation group as fundamental: the arena is $\mathbb{R}^4$ with the positive-definite metric, the symmetry is

$$
\mathrm{SO}(4)\cong\bigl(\mathrm{SU}(2)\times\mathrm{SU}(2)\bigr)/\mathbb{Z}_2 ,
$$

compact, and Minkowski signature is neither assumed nor derived — it is **selected**, by a field that singles out one direction and breaks the group.

This article records that route. It states what the real group buys, it records the one programme that develops the route into a unification of the Standard Model with gravity, it lists claim by claim what of the corpus depends on the complex coordinate, and it sets out the work that the route would impose. That work is a **translation**, and the last of the thematic sections states it as such: the route is not a rival algebra, and adopting it does not mean abandoning the corpus's null cone.

The article establishes four things and imports the rest.

- **Established, and recomputed below.** The material sector $\mathbb{M}_-=\mathfrak{u}(2)$ is exactly the commutant of a complex structure inside $\mathfrak{so}(4)$, so the corpus's gauge group is the group a choice of complex structure leaves unbroken; the space of such choices is the sphere $S^2$ of unit pure-imaginary quaternions, which is the fibre of the twistor fibration already recorded in the corpus; on two-forms the Hodge star squares to $+1$ in Euclidean signature and to $-1$ in Minkowski signature, so a real self-dual connection exists on one side and not on the other; and the external programme's generation of fermions is a sixteen-component object, which is the dimension count of one Standard-Model generation with a right-handed neutrino.
- **Imported, and left visible.** The unification programme itself, its field content, its action on projective twistor space, and its identification of the Higgs with the imaginary time direction. Nothing in it is derived by the framework, and no result of it feeds back into the framework's ledger.

## The Two Devices

The two routes are easiest to compare as a table, because they differ in every row and agree in the answer.

|  | complex-coordinate route | real-group route |
|---|---|---|
| arena | the $\mathbb{B}$ frame, $Q_\mu\in\mathbb{C}$ | $\mathbb{R}^4$, positive-definite |
| interval | $\sum_\mu Q_\mu^2$, complex-valued in general | $\sum_\mu x_\mu^2$, real and positive |
| where the minus sign comes from | $i^2=-1$ at $Q_t=ict'$ | nowhere: it is produced by breaking the group |
| group of the arena | $\mathrm{SO}(4)$ on real coefficients, $\mathrm{SO}(3,1)$ on $\mathbb{M}_-$ | $\mathrm{SO}(4)$, compact |
| status of Minkowski space | a **sector**, selected by a coordinate | a **slice**, selected by a field |
| status of the complex structure | the centre of the algebra; structural | absent, with an $S^2$ of them available at each point |
| cost | a convention to defend | a field to supply, and its potential |

**Neither device is a Wick rotation.** The distinction matters because the two are easily conflated, and the corpus states the difference twice. The Wick rotation is an analytic continuation used to compute: one continues $t'\to-i\tau$, calculates, and continues back; the $i$ is a device of the calculation and is removed at the end. The $ict'$ of the corpus is not that. It is a coordinate of the material sector, its $i$ is the central imaginary of the algebra rather than a symbol of convenience, and it is never removed — *The KMS Condition and the Biquaternion Framework* says the imaginary time is intrinsic and "not an analytic continuation", and *Hawking Radiation in Biquaternionic Form* records the same fact for the period of imaginary time. The real-group route differs from both: it removes nothing because there is nothing to remove, and it pays for Minkowski space in a currency the other two do not use at all.

**The contrast in one sentence each.** In the corpus the Euclidean form is bought with a **complex coordinate**; in the real-group route it is bought with a **real group**, and the Lorentzian form is bought back with a field.

## What the Real Group Buys

The real-group route is worth recording because four of the corpus's own open items are supplied by it structurally rather than by construction.

### Chirality comes from the product, not from the module

The spinor module of $\mathrm{Spin}(4)=\mathrm{SU}(2)\times\mathrm{SU}(2)$ is the sum of the two half-spinor modules,

$$
\Delta=\bigl(\tfrac12,0\bigr)\oplus\bigl(0,\tfrac12\bigr),
\qquad
\dim_{\mathbb{C}}=2+2=4 ,
$$

and each factor of the group acts on one summand and not on the other. Chirality is therefore not a property imposed on a module that does not have it; it is what a product group does to its own spinor module. The corpus has the same two-sidedness in its cells, $L_aR_b$, left multiplication and right multiplication, and *The Gauge Group Ceiling* already notes that the norm-preserving rotors form $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R/\mathbb{Z}_2=\mathrm{SO}(4)$ with the diagonal as the gauge group and the axial combination as the chirality rotation. What the corpus does **not** do is put a connection on each factor separately, and that is the step the route takes.

### A chiral gauge coupling is available

Gauging one factor gives a connection that acts on one chirality and not on the other. This is precisely the object the electroweak agenda names as what would settle its central obstacle: "the object is a **chiral non-abelian matter representation**". The corpus's own non-abelian action is left multiplication, which is vector-like on the defining module, and *Anomalies and Anomaly Cancellation* records "a chiral gauge group, and the spectrum it would constrain" as not supplied. On the real-group route the chiral coupling is not an addition; it is a choice of which factor to gauge.

The same structure is what *Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions* records from the algebra side, at the price of enlarging the carrier to $\mathrm{Cl}(3)$ and $\mathrm{Cl}(7)$. The real-group route reaches the same pattern without enlarging anything, which is the whole of its advantage.

### Self-duality is a real condition

On two-forms the Hodge star satisfies $\star^2=+1$ in Euclidean signature, so $\Lambda^2$ splits into two real three-dimensional eigenspaces,

$$
\Lambda^2=\Lambda^2_+\oplus\Lambda^2_- ,
\qquad
\dim_{\mathbb{R}}\Lambda^2_\pm=3 ,
$$

and a real self-dual connection is an object that exists. In Minkowski signature $\star^2=-1$, the eigenvalues are $\pm i$, and there is no real self-dual two-form: the split is a split of the complexified space. Recomputed on the six-dimensional space of two-forms in both signatures, with the epsilon contraction and the metric inverse, the star has eigenvalues $\{+1,+1,+1,-1,-1,-1\}$ in Euclidean signature and $\{+i,+i,+i,-i,-i,-i\}$ in Minkowski signature. *The Self-Dual and Anti-Self-Dual Split* treats the complexified case, which is the one the corpus's complex field strength needs; a **chiral connection** needs the real case, and only the Euclidean signature has it.

This is why a chiral formulation of general relativity lives on the real-group side: the self-dual half of the connection is a real object there, and it carries one of the two $\mathrm{SU}(2)$ factors.

### Both factors are compact

The group is compact, so a gauge theory on it is the ordinary compact one: no reality condition to impose, no indefinite form on the field space, unitary finite-dimensional representations throughout. The corpus reaches the same conclusion by a different route — $\mathbb{M}_-$ is exactly the anti-Hermitian part of $\mathbb{B}$, and exponentiating it gives the $*$-unitary group — but it reaches it for one factor, not for two.

## The Sphere of Complex Structures

Here the two routes touch, and the point of contact is exact.

**The objects.** A complex structure on $\mathbb{R}^4$ compatible with the metric is an endomorphism $J$ with

$$
J^2=-I_4,\qquad J^{\mathsf T}J=I_4,\qquad \det J=+1 .
$$

For every unit pure-imaginary quaternion $\vec u$, the left multiplication $L_{\vec u}$ is such a $J$, and conversely every such $J$ on the quaternionic line is one of them. Recomputed on a hundred random unit $\vec u$: $J^{\mathsf T}J-I_4$, $J^2+I_4$ and $\det J-1$ all vanish to $6.7\times10^{-16}$, and distinct $\vec u$ give distinct $J$.

**The space of them is a sphere.** The unit pure-imaginary quaternions are

$$
S^2=\bigl\{\vec u\in\mathbb{H}_{\mathbb{B}} : \vec u^2=-e_t,\ |\vec u|=1\bigr\} ,
$$

which is the sphere of *The Hopf Fibration and the Biquaternion Gauge Bundle*, where it appears as the Bloch sphere and as the base of the Hopf map. So the set of complex structures on the algebra's own quaternionic line is a two-sphere, and it is the corpus's sphere, under another name.

**The commutant is the material sector.** The endomorphisms of $\mathbb{R}^4$ that are antisymmetric and commute with $J$ form a Lie algebra. Recomputed for $J$ the left multiplication by $ie_t$: the solution space of $[A,J]=0$ inside $\mathfrak{so}(4)$ has dimension $4$, and it is exactly the span of the four real matrices of $\mathbb{M}_-$, both inclusions checked. For twenty random complex structures $J=L_{\vec u}$ the dimension is $4$ in every case, so the statement is basis-free. Thus

$$
\mathbb{M}_-=\mathfrak{u}(2)=\bigl\{A\in\mathfrak{so}(4) : [A,J]=0\bigr\},
$$

with the central generator $ie_t$ realising $J$ itself and the three imaginary quaternions realising the traceless part $\mathfrak{su}(2)$.

**What this says.** The corpus's compact gauge group is the group that a **choice of complex structure leaves unbroken** in the rotation group of the frame. The corpus presents $\mathbb{M}_-=\mathrm{U}(2)$ as the algebra's intrinsic anti-Hermitian part, which it is; the same group is also the stabiliser of a complex structure, and the corpus does not say so.

That single identification is the whole difference between the routes, in the only place where they can be compared without ambiguity:

|  | what fixes $J$ | what follows |
|---|---|---|
| complex-coordinate route | the coordinate substitution $Q_t=ict'$, globally | $J$ is a convention; no dynamics; $U(2)$ is the algebra's own |
| real-group route, unbroken | nothing; the $S^2$ is unbroken | the group is $\mathrm{SO}(4)$, and every point of the $S^2$ is equivalent |
| real-group route, broken | a **field** taking values in the $S^2$, i.e. a direction | $U(2)$ survives as the stabiliser; the field is the Higgs |

The first row is the corpus's position: the substitution is global, so one $J$ is fixed everywhere at once and nothing depends on which one it is. The second row is the route without a breaking field, in which no $J$ is selected at all. The third is the external programme, and it is the only one of the three in which the choice of complex structure is a physical object with a potential.

## The External Construction: Euclidean Twistor Unification

The programme is N. J. Woit, "Euclidean Twistor Unification" (arXiv:2104.05099). It is recorded here as an external construction, in the manner of *Matter Makes Space*: nothing in it is derived by the framework, and nothing in the framework is evidence for it.

**The choice of signature.** Euclidean signature is taken as fundamental. The reason given is the state space: a Euclidean quantum field theory determines its Hilbert space only after an imaginary time direction is chosen, which is the direction used for the Osterwalder–Schrader reflection. If Euclidean signature is the physics, that direction is a degree of freedom of the theory and not a calculational choice.

**The two factors, gauged differently.** On $\mathbb{R}^4$ the rotation group is $\mathrm{Spin}(4)=\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$. The programme gauges them into two different things:

- the $\mathrm{SU}(2)_R$ connection is the **chiral spin connection**, with the vierbein as a $\mathbb{R}^4$-valued one-form, and Einstein's equations are written on that pair;
- the $\mathrm{SU}(2)_L$ connection is the **weak interaction**;
- the field that picks the imaginary time direction is one component of the vierbein, and it transforms under $\mathrm{SU}(2)_L$ and under a $U(1)$ exactly as the Higgs field does.

This is the division the corpus declines to make. The corpus writes the same two factors, with the diagonal as the gauge group and the axial combination as a chirality rotation; the programme writes the same two factors with each one gauged, one of them as gravity.

**Projective twistor space, and the internal groups.** Four-dimensional Euclidean space compactifies to $S^4=\mathbb{HP}^1$, and projective twistor space fibres over it,

$$
S^2=\mathbb{CP}^1\;\hookrightarrow\;\mathbb{PT}=\mathbb{CP}^3\;\longrightarrow\;S^4=\mathbb{HP}^1 ,
$$

with fibre the space of complex structures at the point — which is the sphere of the preceding section. A point of $\mathbb{PT}$ is a complex line $l\subset\mathbb{C}^4$, and because

$$
\mathbb{PT}=\frac{\mathrm{SU}(4)}{\mathrm{U}(1)\times\mathrm{SU}(3)} ,
$$

each point carries an internal $U(1)$, from the tautological line bundle, and an internal $\mathrm{SU}(3)$, from the quotient bundle $\mathbb{C}^4/l$. The $U(1)$ and the $\mathrm{SU}(2)_L$ act on the lifted imaginary time direction as the electroweak group acts on a Higgs doublet; the $\mathrm{SU}(3)$ acts on $l^\perp$ and is colour.

**The generation.** One generation of fermions is the space of linear maps

$$
\mathrm{Hom}\bigl(l\oplus l^\perp,\ S_R\oplus S_L\bigr)
=\bigl(l\oplus l^\perp\bigr)^{*}\otimes\bigl(S_L\oplus S_R\bigr) ,
$$

with $S_L=\mathbb{C}^2_0$ a doublet of $\mathrm{SU}(2)_L$ of weight $0$, and $S_R=\mathbb{C}_{-1}\oplus\mathbb{C}_{+1}$ the two singlets of $\mathrm{SU}(2)_L$ carrying the internal $U(1)$ weights shown. The point of the construction is that no large group is used: there is no $\mathrm{SU}(5)$, no $\mathrm{SO}(10)$, no $\mathrm{SU}(4)\times\mathrm{SU}(2)\times\mathrm{SU}(2)$; the internal groups are read off the geometry of a point of $\mathbb{PT}$.

**What the programme does not do, in its own words.** No full theory on $\mathbb{PT}$ is constructed. The Higgs kinetic term and potential are the standard ones inserted by hand. The origin of the **number** of generations is not addressed — the construction gives one, and the three of the world are unexplained. The candidate extension that might supply them, a theory on $S^7$, is offered as speculation. And the state space construction, through cohomology on the upper half of $\mathbb{PT}$, is stated as a direction rather than a result.

**Which $U(1)$, and why it matters.** The programme is explicit that its $U(1)$ is the subgroup of $\mathrm{SU}(2)_R$ acting on right-handed spinors, and that it is **determined by the point** of $\mathbb{PT}$: the point is a choice of complex structure, and the $U(1)$ rotates the fibre of the tautological line over it. This is the arrangement *Custodial Symmetry and the Rho Parameter* already uses on the scalar side, where "the left action is the full $\mathrm{SU}(2)_L$ and the right action is an $\mathrm{SU}(2)_R$ whose $T_3^R$ is the hypercharge". The two agree, and the agreement is worth stating plainly, because it is the one place where the corpus has already written down the programme's electroweak assignment.

What differs is what the $U(1)$ is attached to. In the corpus the subgroup $T_3^R\subset\mathrm{SU}(2)_R$ is fixed once for all — the algebra does not choose which element of the right factor plays the part of hypercharge — while in the programme the $U(1)$ is a function of the point of $\mathbb{PT}$, so that choosing the hypercharge direction and choosing the complex structure and the imaginary time direction are one choice. The corpus's scalar sector uses the right arrangement with that choice already made; the programme makes the choice dynamical. That is the difference, and it is the difference the translation has to handle.

## The Generation, Recomputed

The dimension count is the part of the programme that can be checked without its dynamics, and it is the sharpest evidence that the geometric reading is not empty.

The two factors have complex dimensions $4$ and $4$, so

$$
\dim_{\mathbb{C}}\Bigl[\bigl(l\oplus l^\perp\bigr)^{*}\otimes\bigl(S_L\oplus S_R\bigr)\Bigr]=4\times 4=16 ,
$$

which is the number of Weyl components of one Standard-Model generation with a right-handed neutrino: $2$ for the lepton doublet, $1$ for the charged singlet, $1$ for the sterile singlet, $6$ for the quark doublet, and $3+3$ for the two quark singlets, totalling $16$. The programme's expansion reproduces exactly this list, with the multiplets read off the tensor product.

The $U(1)$ weights follow from the two line-bundle weights. With $\mathrm{U}(1)\subset\mathrm{S}(\mathrm{U}(1)\times\mathrm{U}(3))\subset\mathrm{U}(4)$, the weight on $l$ and the weight on $l^\perp$ are in the ratio $-3:1$; taking $l$ at weight $-1$ and $l^\perp$ at weight $+\tfrac13$, the six terms carry the weights below, and the electric charge follows from $Q=T_3+\tfrac12Y$ in the usual normalisation.

| term | multiplet | $Y$ | $Q$ | particle |
|---|---|---|---|---|
| $l^{*}\otimes S_L$ | $\mathbb{C}^2$ | $-1$ | $0,-1$ | $(\nu_e,e)_L$ |
| $l^{*}\otimes\mathbb{C}_{-1}$ | $\mathbb{C}$ | $-2$ | $-1$ | $e_R$ |
| $l^{*}\otimes\mathbb{C}_{+1}$ | $\mathbb{C}$ | $0$ | $0$ | $\nu_R$ |
| $(l^\perp)^{*}\otimes S_L$ | $\mathbb{C}^3\otimes\mathbb{C}^2$ | $\tfrac13$ | $\tfrac23,-\tfrac13$ | $(u,d)_L$ |
| $(l^\perp)^{*}\otimes\mathbb{C}_{-1}$ | $\mathbb{C}^3$ | $\tfrac43$ | $\tfrac23$ | $u_R$ |
| $(l^\perp)^{*}\otimes\mathbb{C}_{+1}$ | $\mathbb{C}^3$ | $-\tfrac23$ | $-\tfrac13$ | $d_R$ |

Recomputed: the six dimensions sum to $16$, and the eight charges above are exactly the eight of one generation. The overall sign of the displayed $U(1)$ weight is a convention, and it is fixed here by the lepton doublet, which carries $Y=-1$. The source prints the two triplet singlets with the weights $\tfrac23$ and $-\tfrac43$; with the lepton weights fixed as above they are $\tfrac43$ and $-\tfrac23$, and the assignment $Q=T_3+\tfrac12Y$ requires the latter — the content is unaffected, since both pairs are the two members of one $S_R$ doublet.

Two limits belong beside the table. The construction gives **one** generation and has no mechanism for three: the count is a dimension of a tensor product, and no integer in the geometry selects $3$. And it gives no mass and no mixing angle, because the masses come from Yukawa couplings, which the construction does not contain. What it does give is the **pattern** — that the fermions of one generation are the linear maps between two bundles at a point — and the pattern is exact.

## What the Route Cannot Carry

A route is defined as much by what it cannot carry as by what it can, and here the loss is precise.

**There are no null directions.** On $\mathbb{R}^4$ with the positive-definite metric, $\sum_\mu x_\mu^2=0$ has the single solution $x=0$. The real quaternions multiply with multiplicative norm, recomputed on a hundred random pairs to $1.4\times10^{-14}$, so they are a division algebra and have no zero divisors. Every null object of the corpus lives in the complexification: the element

$$
\tilde Q=i e_t+\vec e_x ,
\qquad
\langle\tilde Q\rangle_\natural=i^2+1=0 ,
$$

has vanishing norm, and its conjugates are the zero divisors on which the light cone, the celestial sphere, the complex eikonal, the shear-free congruences and the whole algebrodynamical programme are built.

**The consequence.** The real-group route covers the **gauge and gravity half** of the corpus — the part that concerns connections, chirality, self-duality and compact groups — and it cannot carry the **null half** — the part that concerns the cone, the zero divisors, the caustics and the particles as singular loci. It is a lens on part of the framework, not a rival universe, and any adoption of it has to be an adoption of that part.

This is the reason the corpus's complex coordinate is not mere convention, and it is the strongest argument the corpus has against replacing it. The reply available to the real-group route is that the null structure of the complexified algebra survives untouched, because complexification is a separate operation from the choice of real slice; that reply is correct, and it is also the reason the translation of the next section is possible at all.

## The Ledger

The corpus's claims fall into four classes with respect to the route. The classification is this article's, and it is the part most likely to be revised by later work.

| class | content | consequence if the route were adopted |
|---|---|---|
| **inherited unchanged** | module theory, Peirce decomposition, the two sectors, the trace form and the Born rule, the spectral theory, the operator calculus, the tensor obstructions, the whole mathematics category | nothing moves: none of these sees the signature |
| **rephrased** | the Lorentz group as the norm automorphisms of $\mathbb{B}$; the gauge ceiling $\mathbb{M}_-=\mathrm{U}(2)$; the celestial sphere as the projective null cone | true in a different order: the norm automorphisms are $\mathrm{SU}(2)\times\mathrm{SU}(2)$, of which $\mathrm{SL}(2,\mathbb{C})$ is a real form; $U(2)$ becomes a stabiliser, as in the preceding section |
| **exposed** | the intrinsic imaginary time: the KMS strip, black-hole thermodynamics and the period of imaginary time, Hawking radiation, the statement that the Matsubara formalism needs no Wick rotation | "intrinsic" would have to become "selected": the imaginary direction becomes a choice of slice, and the period becomes the period of a chosen circle |
| **out of reach** | the light cone as the zero-divisor cone, the complex eikonal, the shear-free congruences, the caustic as particle, charge quantisation | none of it is expressible on $\mathbb{R}^4$; it survives only in the complexification |

The third row is the one that matters for the corpus's own programme, because those are the articles that make the sharpest claims. *The KMS Condition and the Biquaternion Framework*, *Black-Hole Thermodynamics in Biquaternionic Form* and *Hawking Radiation in Biquaternionic Form* all rest on the same sentence — that the imaginary time is intrinsic — and that sentence is exactly what the route denies. This is not an error in those articles: they are written inside the complex-coordinate route, and inside it the sentence is a theorem. It is a dependency, and it should be visible as one.

One article already stands on the boundary. *Interpretation of the Wick Rotation in the Biquaternion Universe* reads the rotation as an identification of the material sector with the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and tabulates the two symmetry groups as $\mathrm{SO}(4)$ compact against $\mathrm{SO}(3,1)$ non-compact. That is the real-group route stated as an interpretation of a computational procedure, and it is the corpus's nearest existing approach to the alternative. It is recorded there as one reading of a trick, and it is more than that.

## The Translation, Which Is the Work

If the route is useful, then what it establishes has to be carried back into the framework, and that carrying is a definite task with a definite criterion. Two rules make it a translation rather than a borrowing.

**Rule one: every translated statement must be written with elements of $\mathbb{B}$ alone.** A statement that needs a bundle over a base space, or a section of one, is not translated — it is imported, and it must be labelled as imported. This is the rule the corpus already applies when it records an external construction.

**Rule two: no translation may introduce a preferred direction into the frame.** The corpus's frame singles out no direction; that is what "the four coefficients are $+1$" means. A translated statement that needs a direction has not been translated: it has been transferred, with its cost.

The dictionary that the two routes suggest is this.

| real-group object | biquaternion counterpart | status |
|---|---|---|
| the complex structure $J$ | the central imaginary $ie_t$, or a non-central root of $-1$ | established: the anti-Hermitian sector is the commutant of $J$ |
| the $S^2$ of complex structures | the sphere of unit pure-imaginary quaternions, $\vec u^2=-e_t$ | established: the same $S^2$, as the Bloch sphere of *The Hopf Fibration* |
| the fibre $\mathbb{CP}^1$ of $\mathbb{CP}^3\to S^4$ | the complex projectivisation of the quaternionic line | established in *The ADHM Construction and Biquaternion Instanton Data* |
| $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | left and right multiplication, the cells $L_aR_b$ | established as a decomposition; the gauging of each factor is not |
| the vierbein as a $\mathbb{R}^4$-valued one-form | the frame coefficients $Q_\mu$ of an element | carried, not generated: *Curved Spacetime and the Biquaternion Framework* |
| the chiral spin connection | a connection valued in one factor of $L_aR_b$ | **not translated**: no article gauges one side |
| the Higgs as the imaginary time direction | no counterpart | **not translated**: the corpus's scalar is the central singlet, and a direction is exactly what it may not introduce |
| the internal $\mathrm{SU}(3)$ on $\mathbb{PT}$ | none: $\mathbb{B}$ has no three-dimensional module | **not translated**, and not translatable inside $\mathbb{B}$: colour needs an enlarged carrier, as the ceiling article shows |

The table says where the work is. Four rows are done, one is carried, and three are open. The open ones are the interesting ones, and each has the same shape: the real-group route supplies an object whose biquaternion counterpart would have to be a **non-central** element, and every non-central element carries a direction.

**The proposal, labelled as a proposal.** The corpus need not choose between the routes. The two devices are compatible if the product group is imported as an **internal** structure while the frame keeps its complex coordinate: the four coefficients stay complex, $Q_t=ict'$ stays, the null cone stays where it is, and the cells $L_aR_b$ — which the corpus already has, and which already separate a left action from a right one — are gauged separately as an internal symmetry. Chirality would then come from the internal factor rather than from the frame's group, and the corpus would gain the chiral coupling without losing the zero divisors.

Whether that works is not settled here, and the corpus has a reason to be careful: the ceiling article's result is that a gauge group drawn from the algebra acts by left multiplication and is therefore vector-like on the defining module. An internal product group acting as $L_aR_b$ is not left multiplication alone, so the obstruction does not apply to it as stated — but the anomaly conditions, the mass selection rule and the charge operator would all have to be redone for it, and none of that is done here. The proposal is recorded because it is the natural form of the translation, not because its outcome is known.

## What Would Decide Between the Routes

Three tests, in increasing order of difficulty.

1. **A null structure in the real-group frame.** If the corpus's particle programme can be restated without the zero-divisor cone — if the caustic, the charge and the congruence have a description in terms of a direction field on $\mathbb{R}^4$ — then the null half is not lost and the routes are closer than the ledger says. No such description exists in the corpus or in the literature.
2. **A chiral coupling from the cells.** If the left and right factors can be gauged separately inside $\mathbb{B}$ while the frame keeps $ict'$, the corpus gains the electroweak object without paying the null cone. This is the proposal above, and the test is a computation: the covariant derivative, the curvature, the anomaly coefficient and the charge operator for a field transforming as $L_aR_b$. It is a finite computation and it has not been done.
3. **A prediction that separates them.** The routes agree on every kinematic statement, because they describe the same signature. They could differ dynamically, in the weight of a vacuum-energy contribution or in the spectrum of a thermal theory, since one has a preferred direction built in and the other does not. No such computation exists in either programme.

Until one of the three is settled, the routes are two descriptions of one frame with different books, and the corpus's own book is the one with the null cone in it.

## Summary

The Euclidean form of the biquaternion frame can be obtained in two ways that share no object: with a complex coordinate, $Q_t=ict'$, where the $i$ is the algebra's centre and the Lorentzian sign is $i^2$; or with a real group, $\mathrm{SO}(4)$, where no $i$ appears and the Lorentzian sign is produced by breaking the group with a field. Neither is a Wick rotation, and the corpus says so about its own device in two articles.

The real-group route buys four things structurally: chirality from the product $\mathrm{Spin}(4)=\mathrm{SU}(2)\times\mathrm{SU}(2)$, a chiral gauge coupling from gauging one factor, a real self-dual two-form because $\star^2=+1$ in Euclidean signature, and compactness of both factors. It pays for Minkowski space with a field and its potential.

The two routes touch at one exact point. The corpus's material sector is the commutant of a complex structure in the rotation algebra,

$$
\mathbb{M}_-=\mathfrak{u}(2)=\bigl\{A\in\mathfrak{so}(4):[A,J]=0\bigr\},
\qquad
\dim_{\mathbb{R}}=4 ,
$$

verified for twenty random complex structures; the set of those structures is the sphere $S^2$ of unit pure-imaginary quaternions, which is the corpus's own Bloch sphere and the fibre of its twistor fibration. So the corpus's gauge group is the group that a choice of complex structure leaves unbroken, and the two routes differ only in whether that choice is a convention or a field.

The external programme that develops the route — Euclidean signature as fundamental, $\mathrm{SU}(2)_R$ gauged as a chiral spin connection, $\mathrm{SU}(2)_L$ as weak isospin, the imaginary time direction as the Higgs, and the internal $\mathrm{U}(1)\times\mathrm{SU}(3)$ of projective twistor space as hypercharge and colour — reproduces one generation of fermions as a sixteen-component object, recomputed here, and gives no number of generations and no masses. It carries the gauge and gravity half of the corpus and cannot carry the null half: on $\mathbb{R}^4$ the norm is positive definite and there are no zero divisors, while in $\mathbb{B}$ the element $ie_t+\vec e_x$ has vanishing norm and every null object of the corpus is built on its conjugates.

The work the route imposes is a **translation**, under two rules: every translated statement must be written with elements of $\mathbb{B}$ alone, and no translation may introduce a preferred direction into the frame. Four rows of the dictionary are already established in the corpus, one is carried, and three are open — the chiral spin connection, the Higgs as a direction, and the internal colour. The natural form of the translation is to import the product group as an internal structure on the cells $L_aR_b$, keeping the complex coordinate and the null cone; that is recorded here as a proposal, with its anomaly, mass and charge computations named as undone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_\mu$ | Coefficients of an element in the $\mathbb{B}$ frame, $Q_\mu\in\mathbb{C}$ |
| $\langle\tilde Q\rangle_\natural=\sum_\mu Q_\mu^2$ | Biquaternion norm; four $+1$ coefficients, complex-valued in general |
| $Q_t=ict'$ | The material-sector substitution; the Lorentzian sign as $i^2$ |
| $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ | Anti-Hermitian sector, material sector, the algebra's compact part |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, fixed points of complex conjugation |
| $\mathrm{SO}(4)\cong(\mathrm{SU}(2)\times\mathrm{SU}(2))/\mathbb{Z}_2$ | Rotation group of the Euclidean frame; the real-group route's group |
| $\mathrm{Spin}(4)=\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | Its double cover; the two factors of the product |
| $J$ | Complex structure: $J^2=-I_4$, $J^{\mathsf T}J=I_4$, $\det J=+1$ |
| $S^2=\{\vec u\in\mathbb{H}_{\mathbb{B}}:\vec u^2=-e_t,\ \lvert\vec u\rvert=1\}$ | Sphere of unit pure-imaginary quaternions; also the space of complex structures, and the Bloch sphere |
| $[A,J]=0$ | Commutant condition; its solutions inside $\mathfrak{so}(4)$ are $\mathbb{M}_-$ |
| $\star$ | Hodge star; $\star^2=+1$ on two-forms in Euclidean signature, $-1$ in Minkowski |
| $\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-$ | Real self-dual and anti-self-dual two-forms, three-dimensional each in Euclidean signature |
| $L_aR_b$ | The cell $Q\mapsto aQb$; left and right multiplication, the corpus's two-sided action |
| $\mathbb{PT}=\mathbb{CP}^3$ | Projective twistor space, $\mathrm{SU}(4)/(\mathrm{U}(1)\times\mathrm{SU}(3))$ |
| $l\subset\mathbb{C}^4$, $l^\perp=\mathbb{C}^4/l$ | Tautological line at a point of $\mathbb{PT}$ and the quotient bundle (colour) |
| $S_L=\mathbb{C}^2_0$, $S_R=\mathbb{C}_{-1}\oplus\mathbb{C}_{+1}$ | The two half-spinor modules with their internal $U(1)$ weights |
| $\mathrm{Hom}(l\oplus l^\perp,S_R\oplus S_L)$ | One fermion generation, sixteen Weyl components |
| $Y$, $Q=T_3+\tfrac12Y$ | Hypercharge and electric charge in the normalisation of the generation table |
| $\mathbb{C}^2_{-1},\ \mathbb{C}_{-2},\ \mathbb{C}_0,\ (\mathbb{C}^3\otimes\mathbb{C}^2)_{1/3},\ \mathbb{C}^3_{4/3},\ \mathbb{C}^3_{-2/3}$ | The six multiplets of one generation, with their $U(1)$ weights |
| $i e_t+\vec e_x$ | A null biquaternion: norm $i^2+1=0$; no counterpart on $\mathbb{R}^4$ |

## Further Reading

- [Frame Conventions](frame-conventions.html), for the $\mathbb{B}$ frame, its four $+1$ coefficients, the statement that its form is Euclidean, and the $\mathbb{M}_-$ frame as a sector condition rather than a second frame.
- [Why Complexify Spacetime?](why-complexify-spacetime.html), for the complex-coordinate route stated as a programme: the $ict'$ convention, the local complex structure, and the claim that what is a postulate in the real formalism is derived in the complexified one.
- [The Local Complex Structure and the Speed of Light](the-local-complex-structure-and-the-speed-of-light.html), for the step from a global to a local complex structure through $c=1/\sqrt{\epsilon\mu}$ — the corpus's own field-valued complex structure, and the point at which it can be compared with a direction field.
- [Interpretation of the Wick Rotation in the Biquaternion Universe](interpretation-of-the-wick-rotation-in-the-biquaternion-universe.html), for the reading of the rotation as an identification of $\mathbb{M}_-$ with $\mathbb{H}_{\mathbb{B}}$, and for the tabulation of $\mathrm{SO}(4)$ compact against $\mathrm{SO}(3,1)$ non-compact.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html), for $\mathbb{M}_-=\mathrm{U}(2)$, for the four constructions that give it, and for the norm-preserving rotors $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R/\mathbb{Z}_2$ with the diagonal as gauge and the axial combination as chirality.
- [The Hopf Fibration and the Biquaternion Gauge Bundle](the-hopf-fibration-and-the-biquaternion-gauge-bundle.html), for the sphere of unit pure-imaginary quaternions as the base of the Hopf map and as the Bloch sphere — the $S^2$ that is also the space of complex structures.
- [The ADHM Construction and Biquaternion Instanton Data](the-adhm-construction-and-biquaternion-instanton-data.html), for the fibration $\mathbb{CP}^1\to\mathbb{CP}^3\to S^4$ and the identification of its fibre as the space of complex structures compatible with the quaternionic structure.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the split of the complexified field strength, against which the real Euclidean split of this article should be read.
- [Custodial Symmetry and the Rho Parameter in Biquaternionic Form](custodial-symmetry-and-the-rho-parameter-in-biquaternionic-form.html), for the arrangement in which the left action is the full $\mathrm{SU}(2)_L$ and the right action an $\mathrm{SU}(2)_R$ whose $T_3^R$ is the hypercharge, and for the opposite statement about matter — that left multiplication is vector-like.
- [Electroweak Theory under the Biquaternion Framework — A Research Agenda](electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html), for the chiral non-abelian matter representation named as what would settle the central obstacle.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html), for "a chiral gauge group, and the spectrum it would constrain" recorded as not supplied.
- [Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions](left-right-symmetric-fermions-from-complex-split-biquaternions-and-bioctonions.html), for the same two-factor pattern reached by enlarging the carrier to $\mathrm{Cl}(3)$ and $\mathrm{Cl}(7)$, and for the volume element as a Higgs candidate.
- [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html), [Black-Hole Thermodynamics in Biquaternionic Form](black-hole-thermodynamics-in-biquaternionic-form.html) and [Hawking Radiation in Biquaternionic Form](hawking-radiation-in-biquaternionic-form.html), for the claims that rest on the imaginary time being intrinsic, and which the real-group route denies.
- [Matter Makes Space — An External Construction from Quaternionic Spinors](matter-makes-space-an-external-construction-from-quaternionic-spinors.html), for the form this article follows: an outside construction recorded, recomputed where it can be, and not endorsed.
- [Twistor Theory and Biquaternions](twistor-theory-and-biquaternions.html), for projective twistor space, the Hermitian form of signature $(2,2)$, and the rule that a shared module is not evidence for either programme.
- N. J. Woit, "Euclidean Twistor Unification", arXiv:2104.05099 [hep-th] (2021), the source of the external construction recorded here: Euclidean signature as fundamental, the two factors of $\mathrm{Spin}(4)$ gauged as gravity and weak isospin, the imaginary time direction as the Higgs, the internal $\mathrm{U}(1)\times\mathrm{SU}(3)$ of projective twistor space, the generation as $\mathrm{Hom}(l\oplus l^\perp,S_R\oplus S_L)$, and the open problems as the source states them.
- M. F. Atiyah, N. J. Hitchin and I. M. Singer, "Self-duality in four-dimensional Riemannian geometry", *Proceedings of the Royal Society A* **362** (1978) 425–461, for the self-dual connection, the twistor fibration over a four-manifold with anti-self-dual metric, and the space of complex structures as a complex manifold.
- A. Ashtekar, "New variables for classical and quantum gravity", *Physical Review Letters* **57** (1986) 2244–2247, for the chiral connection formulation of general relativity in which one factor of the rotation group is gauged alone — the gravitational instance of the step this article's ledger records as untranslated.
- V. Vaibhav and T. P. Singh, "Left-Right Symmetric Fermions and Sterile Neutrinos from Complex Split Biquaternions and Bioctonions", arXiv:2108.01858, for the division-algebra construction of the same two-factor pattern, which enlarges the carrier where the real-group route does not.
