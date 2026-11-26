# __Particle Spins in the Biquaternion Algebra: Three Carriers, Their Meaning and Their Order__

## Introduction

**The claim.** The algebra has three carriers and they are not on the same footing. One of them costs nothing: the real vector part $\mathfrak{k}\subset\mathbb{B}_{V}$, on which the algebra acts by conjugation, is there before any frame is chosen and stays the same subspace in every frame. The second costs one idempotent: the minimal left ideal $\mathbb{B}\tilde\Pi$ exists only once an axis is chosen, and the axis is a frame and not a datum. The third is the answer to a question about the first two: the centre is what the conjugation cannot move, and it is therefore named without any choice at all. **The order in which the corpus can build its physics — the operator, then the state, then the invariant — is the order of what each carrier costs, and this article states the criterion, checks it on the three carriers, and reads the particle content in it.**

**What is established.** Five things. First, the non-commutativity of $\mathbb{B}$ is located exactly on $\mathfrak{k}$: the commutator of two vector elements is a vector element, while the product of two is not, and those two facts together are what makes $\mathfrak{k}$ a Lie algebra that is not a subalgebra. Second, the adjoint action of a rotor on $\mathfrak{k}$ is a rotation with weights $+1$, $0$, $-1$, so the carrier has three states, and the third polarization of a massive vector is one of its dimensions rather than an extra ingredient. Third, the ideal is not canonical: conjugation by a rotor sends it to a different ideal of the same dimension, and the intersection of the two is smaller than either. Fourth, the centre is the commutant of the whole algebra, two real dimensions, one complex, fixed pointwise by every unit element. Fifth, the three dimensions are $3$, $2$, $1$, which are $2s+1$ at $s=1$, $\tfrac12$, $0$, so the arithmetic of the carriers and the arithmetic of the spins are the same arithmetic.

**What this article does not claim.** It does not claim that the vector carrier is more important, or more numerous, or more fundamental in the sense of compositeness. The menu as it stands holds $67$ entries in the spin-one bands, $115$ in the spin-$\tfrac12$ bands and $110$ in the spin-zero bands. It does not claim that the adjoint carrier is a state: no amplitude lives on $\mathfrak{k}$, and a Hilbert space of vectors is not what the algebra offers. It does not claim that the algebra is built in time. **What is ordered is not the algebra but the number of choices a statement costs, and that number is a fact about the algebra.**

**Why it stands here and not in Relativity.** Relativity carries the three subspaces and gives each its own introduction; it names no particle, and this article names photons, quarks and scalars. **The particle content appears for the first time in the spin bands that open every force block below, and those bands belong to no single block — so the reading of them is stated once, here, between the last block that has no particles and the first block that has them.**

**Why it follows the survey.** The survey, in Relativity, fixes the catalogue: three carriers, no fourth, and the two repairs that the passage from a carrier to a subspace costs. What it does not do is rank them, and the ranking is what a reader needs before the first band, because each band writes its field on one of the three. **One half of the question is Relativity's, the other half belongs to no sector, and this is where the second half is stated.**

## The Three Carriers and the Criterion

**The catalogue, from the companion article on tensor products.** The three carriers are the centre, the ideals and the material sector's scalar-free part:

$$
\mathbb{B}_{C}=\mathbb{C}e_t, \qquad S_{\pm}=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}, \qquad \mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k} .
$$

| Carrier | Set | Action | Spin | Real dimension |
|---|---|---|---|---|
| centre | $\mathbb{C}e_t$ | conjugation; fixed | $0$ | $2$ |
| ideals | $\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ | left multiplication | $\tfrac12$ | $4$ |
| vector part | $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z\subset\mathbb{B}_{V}$ | conjugation | $1$ on $\mathfrak{k}$ | $3$ |

**The criterion.** Ask of each carrier how much must be chosen before it can be named.

- The vector part is named by the algebra alone. Conjugation preserves it, so a statement about it does not depend on which unit element performs the conjugation.
- The ideal is named by an idempotent. Change the idempotent and the ideal changes, so a statement about it carries the frame that produced it.
- The centre is named by a property with no free parameter: it is the set of elements that commute with everything. No choice can move it and no choice is needed to define it.

**Three answers: no choice, one choice, and the invariant of all choices.** That is the order, and the rest of the article is the verification.

## The Vector Part Is Where the Algebra Fails to Commute

**Two vector units do not commute.** In the framework's basis the product is $\vec e_x\vec e_y=\vec e_z$ and $\vec e_y\vec e_x=-\vec e_z$, so

$$
[\vec e_x,\vec e_y]=2\vec e_z .
$$

**The commutator closes on $\mathfrak{k}$ and the product does not.** The bracket of any two elements of $\mathfrak{k}$ is again an element of $\mathfrak{k}$; this holds for all nine ordered pairs and is the statement that $\mathfrak{k}$ is a Lie algebra under the commutator. The product fails for exactly the three squares, $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$, which land on the Hermitian scalar and not on the vector part; the other six products stay inside. **So $\mathfrak{k}$ is a Lie algebra that is not an associative subalgebra, and the three failures are the three squares.**

**This is where the algebra's non-commutativity lives, and nowhere else.** The centre commutes with everything, so $[Q_t e_t,\tilde Q]=[i q'_t e_t,\tilde Q]=0$ for every element $\tilde Q$; no failure of commutativity is located there. An algebra with no vector part is the centre, $\mathbb{C}$, commutative by definition and with nothing to rotate. **The vector part is not a piece of the algebra that happens to be three-dimensional; it is the piece that makes the algebra non-commutative, and the non-commutativity is what the whole framework reads as a connection.**

## The Adjoint Action Rotates the Vector Part Without Choosing Anything

**The transformation law.** A unit rotor $\tilde u=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u$ acts on the material sector by conjugation,

$$
\tilde R_\Phi\;\longmapsto\;\tilde u\,\tilde R_\Phi\,\tilde u^{*},
$$

and on the vector part this is a rotation. Three numbers fix that statement, and all three were verified on the matrix of the map in the basis $(\vec e_x,\vec e_y,\vec e_z)$: the trace is $1+2\cos\theta$, the determinant is $1$, and the axis $\vec u$ is fixed. **The spectrum is therefore $1$, $e^{i\theta}$, $e^{-i\theta}$ — weights $+1$, $0$, $-1$ — and the carrier is spin one with its three states.**

**The generators are the same three units.** The inner derivation $\mathrm{ad}_{\vec e_z}(v)=[\vec e_z,v]$ acts on the complexified vector part with eigenvalues $-2i$ on $\vec e_x+i\vec e_y$, $+2i$ on $\vec e_x-i\vec e_y$ and $0$ on $\vec e_z$, so the one-parameter group it generates is the rotation above. **The algebra does not need an imported representation of $SU(2)$: it contains three elements whose brackets are the rotation algebra, and the factor of two in that bracket is exactly the half angle carried by the rotor.**

**Nothing is chosen.** No idempotent, no axis, no basis and no frame enters the definition of $\mathfrak{k}$. Every rotor produces another rotation of the same subspace, and the subspace is the same subspace in each. **That is the precise sense in which the vector part is canonical: it is $\mathfrak{k}$ in every frame, and a statement about it is a statement about the algebra.**

**Why three matters.** The dimension is $2\cdot 1+1$. A massive vector has three independent polarization directions, and the corpus does not add the third by hand: it is the number of dimensions the carrier has. The companion article on the third polarization reads the same fact from the field strength, where the longitudinal mode is the one the self-dual split cannot reach. **The third state is a dimension of the carrier, and a carrier that had two dimensions could not have it.**

## The Ideal Costs One Idempotent, and an Idempotent Is a Frame

**The construction.** Let

$$
\tilde\Pi=\tfrac12\left(e_t+i\vec u\right),\qquad \vec u\cdot\vec u=1 ,
$$

with the axis taken along $\vec e_z$ for the check. It is idempotent, $\tilde\Pi^{2}=\tilde\Pi$, and the left ideal $\mathbb{B}\tilde\Pi$ is four real dimensions, two complex. **Left multiplication acts on it irreducibly**: the operators of left multiplication by the eight basis elements, written on a basis of the ideal, have a commutant of one complex dimension and no invariant subspace. That is the whole content of the spin-$\tfrac12$ carrier.

**The dimension is $2\cdot\tfrac12+1$, and it is the reason there is no spin-one module.** Every finite-dimensional module of $\mathbb{B}\cong M_2(\mathbb{C})$ is a direct sum of copies of the defining module, so its complex dimension is even. A three-dimensional module would need a unital algebra map $M_2(\mathbb{C})\to M_3(\mathbb{C})$; its image would be a unital simple subalgebra of $M_3(\mathbb{C})$, and the only one is $M_3(\mathbb{C})$ itself, of complex dimension nine. **The counting argument the companion article gives — $1+2+3>4$ — is the same obstruction stated on the weights.**

**But conjugation does not preserve the ideal.** Taking a rotor and conjugating the whole ideal gives another ideal of the same dimension, and the two are different subspaces: the span of the two has dimension eight, the whole algebra. **So the ideal is not a property of the algebra; it is a property of the algebra together with a chosen axis.** This is the proof of the sentence the corpus uses in its discussion of the state: the axis is a frame and not a datum.

**Therefore the ideal is a carrier of states and not of operators.** An operator statement is a statement about $\mathfrak{k}$ or about the algebra, and it can be made without choosing anything. A state statement needs the ideal, because an amplitude is a component, and a component is a coefficient in a basis of an ideal. **The cost of a state is one idempotent, and it is paid once per frame.**

## The Centre Is What No Frame Can Move

**The centre is the commutant, and its dimension was checked.** Solving $[\tilde Q,\tilde X]=0$ for all eight basis elements $\tilde X$ leaves exactly two real dimensions, spanned by $e_t$ and $ie_t$. The corpus calls the centre the fixed line of the adjoint action; the computation says the same thing and adds the dimension, which is two over $\mathbb{R}$ and one over $\mathbb{C}$.

**It is fixed pointwise by every unit element.** Conjugation by a rotor or by a central phase leaves $e_t$ and $ie_t$ unchanged, element by element and not up to a rotation. **So the centre is not a subspace that a frame rotates into itself, like $\mathfrak{k}$; it is a subspace that no frame touches at all.** The distinction is the whole difference between spin one and spin zero in this framework.

**The dimension is $2\cdot 0+1$, one complex.** A single state, no multiplet, no axis and no polarization: a scalar has one component in every frame, and that is what the count says.

**What the physics does with it.** The vacuum value of the corpus's scalar sector is central, $\langle\tilde\Xi\rangle=\langle\xi\rangle e_t$, and the local redundancy that produces the connection is a localization of the central phase. **A scalar has one thing to say — a phase and a magnitude — and the centre is exactly the carrier that can say it and nothing else.**

## The Order Is a Dependency, Stated in One Place

**The ideal presupposes an element, and an element presupposes the decomposition.** $\tilde\Pi$ is an element of $\mathbb{B}$; naming it requires the algebra, and the algebra is understood through the conjugacy decomposition into centre and vector part. **An axis is a direction in $\mathfrak{k}$, so the choice that produces the ideal is a choice made on the spin-one carrier.**

**The centre presupposes the action.** It is defined as the commutant, that is, as the set of elements the adjoint action leaves alone. Its definition quotes the action of the first carrier.

**So the two later carriers are functions of the first: one is an orbit of a chosen point under it, the other is its fixed set.** That is the dependency, and it is the reason the order is not a matter of taste.

**The limit of the statement.** The three carriers are co-defined; the algebra is not assembled in time, and nothing here says that $\mathfrak{k}$ is logically prior to the centre in every possible presentation. **What is ordered is the cost of a statement, and the cost is $0$, $1$, $0$-but-only-as-an-invariant. A presentation that begins with the scalar must first choose a frame in order to say that the scalar does not depend on it.**

## The Physics in the Same Order

### The operator: the bosons of the connection

**Vector bosons are the carrier read as a field.** The photon, $W^{+}$, $W^{-}$ and $Z$ are components of connections in $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$: the central slot carries the temporal component, $\mathfrak{k}$ the three spatial ones, and the transformation law is the conjugation above. In the $\mathrm{SU}(4)$ model the connection has fifteen directions, nine massless above $M_C$ and six heavy; the six are the leptoquarks, and the article that classifies them reads each of the fifteen as a cell of one grid. **The gluons enter as a residual reading of the same fifteen, and the colours are a coordinate label on the fifteen rather than a charge.**

**The mass of a vector is not a vector statement.** The Proca mass is an input, written $k_m$ and put in by hand; above $M_C$ the $\mathrm{SU}(4)$ mass form is the commutator double bracket $2v^{2}[D,[D,\cdot\,]]$, which vanishes when the condensate does. **The carrier supplies the three states and not their splitting, which is why the third polarization exists at every mass and why its energy depends on the mass.**

**The graviton does not escape the order.** Its carrier is the symmetric trace-free square of the material vector,

$$
\left(V\odot V\right)_{\mathrm{sym}}=0\oplus 2,\qquad 6=1+5 ,
$$

so spin two is built from the spin-one carrier by a symmetric square and a removal of the trace. **The vector part is prior even to the spin that lies above it.**

### The state: the fermions

**Fermions are the ideal read as a field.** Sixteen Weyl fields in the $\mathrm{SU}(4)$ model, the quarks and the leptons, the electron and the neutrinos. **Chirality is a property of the carrier and not of the algebra: left multiplication carries the chiral spinor $(\tfrac12,0)$, and its conjugate $(0,\tfrac12)$ is the conjugate module, with a conjugate-linear action, and not a complex module of $\mathbb{B}$ at all. The framework therefore has one chiral spinor carrier and reaches the other chirality by conjugation.**

**The statistics sign is a property of the carrier as well.** The exchange sign is $(-1)^{2s}$, and the algebra separates the two cases by the action of $-e_t$: it acts as $-1$ on the ideal and trivially on the centre and on $\mathfrak{k}$. **The module and the adjoint sector track the two integrality classes, so the sign is read off the carrier and the spin–statistics theorem is not needed to see which side a field is on.**

**The cost of a fermion mass is one more choice.** The Yukawa sector is a single matrix and its diagonalisation, and the matrix is an input. **A state can be written for free once a frame is fixed; a mass needs a second structure on the same frame, and that is where the framework's fermion sector stops.**

**The electroweak block has no fermion action, and the reason is the order.** The algebra owns the connection outright and the chiral matter by transcription; the action on doublets and singlets is one of the imported rows. **A sector can be complete on the carrier it owns and incomplete on the one it borrows, and the electroweak block is exactly that.**

### The invariant: the scalars

**Three scalars, three different relations to the centre.** The Higgs doublet is imported with its representation, and its role in the corpus's own bookkeeping is the sharpest statement of the order: the connection gains a longitudinal mode and the scalar loses one, so the count balances at $4=4$. **The scalar's degree of freedom becomes a state of the vector, which is the order of the carriers performed on a single field.**

**The pion is a rotor.** The chiral field is a unit quaternion and the chiral Lagrangian is built from its derivatives; the diagonal case $g_L=g_R=g_V$ is the adjoint action, so the pion's own action on the vector part is the conjugation that defines spin one. **The strong sector's scalar is a group element acting on $\mathfrak{k}$, not an element of the centre, and the framework's one natively constructed scalar is therefore written on the spin-one carrier.**

**The axion and the sigma belong to the same two families**: a phase of the centre and a radial mode of the rotor. **No scalar in the corpus is a fourth kind of object; each is either an invariant or a rotation.**

### Above: spin $\tfrac32$ and spin two

**The Rarita–Schwinger field is a module tensored with a vector index**, with a constraint that removes the lower spin, and its equation is imported. **Spin two is the symmetric square of the vector.** Both live outside the base algebra for the same reason: a tensor product is not a subcarrier, and the closure of the three carriers is a statement about $\mathbb{B}$ alone.

## What the Order Does Not Say

**It does not rank the carriers by quantity.** $69$ spin-one entries, $115$ spin-$\tfrac12$ entries, $110$ spin-zero entries and $14$ other-spin entries in the menu, counted band by band. **The thinnest band is the one the order puts last, and the first band is neither the thickest nor the thinnest.**

**It does not make the vector a module.** The adjoint is not a carrier of amplitudes, and a state written on $\mathfrak{k}$ is not a state the framework has. **The order is an order of construction, not a licence to move a state onto the vector part.**

**It does not say that every sector uses the carriers in equal measure.** The electromagnetic block carries one carrier and no matter: no article in it puts a spin-$\tfrac12$ or a spin-$0$ field in an electromagnetic role, and the Dirac title that appears there is the parabolic operator, which reformulates Maxwell and describes no fermion. The strong block reads the non-abelian factor as the rotation group of space, and receives a scalar that is a rotor rather than a centre element. **The order describes the carriers, and a sector may use one of them and not the others.**

**It does not derive the Standard Model.** The algebra lists three carriers; it does not say which particle occupies which, and the assignment of the fifteen and the sixteen is a declaration with a mass spectrum attached. **The order says which carrier a sector's field must be written on, not which fields exist.**

## Consequences for Reading the Corpus

**The menu runs $1$, $\tfrac12$, $0$, then other spins, and this article is the argument for that arrangement.** Every block that carries a spin band now opens on the vector, continues with the ideal, closes on the centre, and puts the tensor-product spins last, where they belong: they are not carriers of the algebra but products of it. **Reading in that order has one advantage: each band uses only what the band above it has already established.** The connection needs no idempotent, the state needs one, and the invariant needs the frame in order to be defined as what the frame cannot move.

**The other enumerations have their own criteria.** The tensor-product article's catalogue lists the centre first, the ideals second and the material sector third, because its subject is the isotypic decomposition of two actions and the enumeration follows the algebra's own order. The four object articles — those that list every article on one equation — mirror the menu band by band within each category, and they now run in the same order as the menu does. **The catalogue is an enumeration by the algebra's own order; the object lists are a projection of the menu. Neither is an ordering by cost, and the three are compatible once the criterion is named.**

**No article moves and no identity changes.** The order is a reading order: it reorders what is already written, and it leaves every field where the sector that owns it has put it.

## Open Questions

**Can the ideal be derived rather than chosen?** A state is a coefficient in a frame, and a frame is an idempotent. Whether the framework can produce a frame dynamically — whether the axis can be an output of the dynamics rather than an input to the notation — is not settled here. **A positive answer would move the cost of a state from one choice to zero, and the order would collapse to a single carrier.**

**Is the centre's priority visible in the action?** The vacuum is central and the mass form is built on it, so the centre does appear as a fixed point of the dynamics. **Whether the central value is selected or assumed is the question the symmetry-breaking block answers in the negative: it is assumed.**

**Why this triple and not another?** The dimensions $1$, $2$, $3$ are $2s+1$ at $s=0$, $\tfrac12$, $1$, and the sequence stops there because the algebra is $M_2(\mathbb{C})$. **A larger algebra would have a longer list and the order would still be by cost; whether the cost criterion extends to the tensor-product carriers is open.**

**Is the menu's asymmetry a fact about the physics or about the writing?** The scalar band is thinner than the fermion band by five entries and thicker than the vector band by forty-three. **A band's size measures the corpus's attention and not the carrier's rank, and the two have not been compared anywhere.**

## Summary

**Three carriers and one order: the vector part, then the ideal, then the centre.**

**The vector part is canonical.** It is the set on which the algebra's non-commutativity lives, the commutator closes on it while the product does not, and conjugation by any unit element rotates it without moving it. Its three dimensions are $2\cdot1+1$, and the third polarization of a massive vector is one of them.

**The ideal is a frame.** It costs one idempotent, it is irreducible, its dimension is $2\cdot\tfrac12+1$, and conjugation sends it to a different ideal of the same dimension, so no statement about it is free of the axis that produced it.

**The centre is the invariant of every frame.** It is the commutant, two real dimensions, fixed pointwise, $2\cdot0+1$, and it is where the vacuum, the phase and the classical limit live.

**The physics reads in the same order.** Bosons are the vector carrier, fermions are the ideal, scalars are the centre or a rotor; the third polarization, the Goldstone bookkeeping at $4=4$ and the graviton's symmetric square are all statements about the first.

**The order is a cost and not a rank.** The thinnest band in the menu is the one that comes first.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{B}_{C}\oplus\mathbb{B}_{V}$ | the biquaternion algebra over $\mathbb{R}$, eight real dimensions; the centre two, the vector subspace six |
| $\mathbb{B}_{C}=\mathbb{C}e_t$ | the centre, two real dimensions |
| $\mathfrak{k}\subset\mathbb{B}_{V}$ | the real vector part, three real dimensions, the spin-one carrier |
| $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$ | the material sector, four real dimensions |
| $S_{\pm}=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ | the minimal left ideals, four real dimensions each |
| $\tilde\Pi$ | an idempotent, the frame the ideal is built on |
| $\tilde u$ | a unit rotor, $\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u$ |
| $\mathrm{ad}_{\vec e_{\imath}}$ | the inner derivation $[\vec e_{\imath},\cdot\,]$ |

## Further Reading

- [Rotor, Spin, Pair and Carrier: A Survey of the Closure Block](rotor-spin-pair-and-carrier-a-survey-of-the-closure-block.html), for the catalogue, the closures and the proof that a fourth carrier does not exist.
- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), [Introduction to the Spin-Half Bispinors Spaces](the-spin-half-bispinor-spaces.html) and [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the three carriers each read on its own.
- [Higher Spin from Tensor Products: The Three Carriers and the Absence of a Fourth](higher-spin-from-tensor-products-the-three-carriers-and-the-absence-of-a-fourth.html), for the isotypic decomposition behind the catalogue.
- [The Determination of the Possible Spins in Biquaternionic Form](the-determination-of-the-possible-spins-in-biquaternionic-form.html), for the same three values read as Casimir labels.
- [The Centre of the Biquaternion Algebra as the Classical Sector](the-centre-of-the-biquaternion-algebra-as-the-classical-sector.html), for the commutant and the superselection structure.
- [Spin Zero and the Centre: Why the Scalar Field Lies Outside the State Module](spin-zero-and-the-centre-why-the-scalar-field-lies-outside-the-state-module.html), for the spin-zero carrier's exclusion from the amplitude space.
- [Integer Spin Quantization and the Adjoint Action on the Material Sector](integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the quantization of the adjoint carrier.
- [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html), for the longitudinal mode and the two helicities.
- [Canonical Quantization of the Biquaternion Proca Field](canonical-quantization-of-the-biquaternion-proca-field.html), for the three polarizations as oscillators.
- [The Covariant Derivative and Connection in Biquaternionic Form](the-covariant-derivative-and-connection-in-biquaternionic-form.html), for the connection as the carrier's field.
- [The Chiral Theory and the Lagrangian: The Pion and the Decay Constant](the-chiral-theory-and-the-lagrangian-the-pion-and-the-decay-constant.html), for the pion as a unit quaternion and the diagonal adjoint case.
- [The Nonlinear Sigma Model in Biquaternionic Form](the-nonlinear-sigma-model-in-biquaternionic-form.html), for the group-valued scalar and its targets.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html), for the count $4=4$ that moves a scalar degree of freedom into a vector state.
- [Classification of the Bosons in the SU(4) Model](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html), for the fifteen directions, nine massless and six heavy.
- [Classification of the Fermions in the SU(4) Model](classification-of-the-fermions-in-the-su4-model-sixteen-weyl-fields-closed-under-c-and-cp.html), for the sixteen Weyl fields and their discrete symmetries.
- [Canonical Quantization of the Biquaternion Graviton Field](canonical-quantization-of-the-biquaternion-graviton-field.html), for the symmetric square $0\oplus 2$ and $6=1+5$.
- [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html), for the first carrier that is not a subcarrier of $\mathbb{B}$.
- [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html), for the trace that turns a carrier into a number.
