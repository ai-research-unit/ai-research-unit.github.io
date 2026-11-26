# __Rank Five From Three: The Weak Factors as a Condensate Index, and Two Theorems Against the Composite Route__

## Introduction

**The layer.** The transition is a breaking of $\mathrm{SU}(4)$ on a formal copy of the carrier, and everything this article proves is either linear algebra on $\mathfrak{su}(4)$ or a count on the endpoint. **The one postulate in it is a choice of representation, and the article names that choice in the section where it is spent.**

**The question.** Can the weak force be *created* by the transition that breaks the primordial force — not carried into the transition as a fragment, not assembled from the debris, but born with it? And if it can, what exactly plays the role of creator?

**The answer.**

$$
\boxed{\;
\text{the primordial force breaks; the object that breaks it carries a doublet index;}
\;}
$$

$$
\boxed{\;
\text{the doublet index is the weak force: it arrives with the breaking, not out of it.}
\;}
$$

**Three statements carry the construction, and they have three different statuses.**

| statement | status | where it is proved |
| --- | --- | --- |
| a subalgebra never has larger rank than its algebra | **theorem** | §*The Lemma* |
| the sextet cannot make the weak pair | **theorem**, twice over | [The Charge Theorem](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html); §*The Other Route, Closed Elsewhere* |
| the transition's scalar carries a doublet index | **postulate** | §*The Price* |

**What this article establishes.** That rank five is unreachable from rank three inside $\mathfrak{su}(4)$, hence that the weak factors must arrive beside the primordial force rather than emerge from it; that the object doing the breaking carries an index, and that an index is exactly the kind of object that can arrive beside; that the resulting ledger is $3+1+1=5$ with one sense of rank and no composite spectrum; and that the weak bosons' masses come from later vacua, so no mass hierarchy problem is created.

**Not established.** Why the condensate carries a doublet index at all. **That is a postulate, and it is the only one.** Why the index splits into two chiral factors rather than a single one. **That is a second assumption, inherited from the corpus rather than invented here.** And the dynamics of the condensation itself, which the corpus does not derive for any sector.

**What this article is not.** It is not a derivation of the weak force from $\mathrm{SU}(4)$. **It is a proof that the weak force cannot come from inside $\mathrm{SU}(4)$, together with a construction in which it comes from the outside at the transition.** The difference between those two sentences is the whole content of the migration.

**Where the rest is.** The breaking that this article interprets is [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The sextet whose closures are proved here is [Six Leptoquarks Above $M_C$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html) and [The Charge Theorem](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html). The grammar of *survives*, *breaks* and *arrives* is [The Centraliser, the Complement, and the Index](the-centraliser-the-complement-and-the-index-dimension-and-rank.html). The scales are [The Matching at $M_C$](matching-at-m-c.html). The internal working note with the full arithmetic is [Rank Five From Three](../articles_internal/structures/structure-weak-force-as-side-effect.html).

## What a Transition Must Deliver

**Three things, and they are separate deliverables with separate status.**

| deliverable | status | where it comes from |
| --- | --- | --- |
| $\mathrm{SU}(4)\to\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}$ | **theorem, already in the corpus** | the adjoint mass matrix |
| the sextet is exactly what is eaten | **theorem, already in the corpus** | $\operatorname{ad}(iD)$ on the fifteen |
| $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ appears | **postulate, new** — one postulate, the doublet index | not derivable inside $\mathrm{SU}(4)$, and it does not have to be |

**The first two are free.** The corpus's mass matrix article already states them: $M^{2}=2v^{2}[D,[D,\cdot\,]]$ is diagonal in the plane basis with $32v^{2}$ on the six planes through the lepton line and $0$ on the nine that avoid it. Equivalently, on the vacuum $\operatorname{diag}(-3,1,1,1)$,

$$
\operatorname{ad}(iD):\quad 0^{9}\ \oplus\ (-4i)^{3}\ \oplus\ (+4i)^{3},
$$

**so the kernel is the nine-dimensional $\mathfrak{u}(3)$ and the sextet is precisely the $\pm4i$ eigenspace.**

**The third is the invention, and the rest of this article is about what it costs and what it does not.**

## The Rank Ledger: Three Is All There Is

**The account, with nothing in it but the corpus's own numbers.**

$$
\dim\mathfrak{su}(4)=15,\qquad \operatorname{rank}\mathfrak{su}(4)=3 .
$$

**The endpoint costs more than the opening balance.**

| item | rank cost |
| --- | --- |
| the strong group $\mathrm{SU}(3)_c$ | $2$ |
| the abelian factor $\mathrm{U}(1)_{B-L}$ | $1$ |
| $\mathrm{SU}(2)_L$ | $1$ |
| $\mathrm{SU}(2)_R$ | $1$ |
| **endpoint** | $2+1+1+1=\mathbf 5$ |
| **opening balance** | $\mathbf 3$ |

**Two integers, and the second is smaller. That is the whole of the difficulty.**

**The two maximal-rank readings spend the same three, which is why they exist.** They are the two subgroup rows of the branching table:

| subgroup | structure | rank | branching of the $\mathbf{15}$ |
| --- | --- | --- | --- |
| $\mathrm{U}(3)$ | $\mathrm{SU}(3)\times\mathrm{U}(1)$ | $2+1=3$ | $\mathbf 8_0\oplus\mathbf 1_0\oplus\mathbf 3_{+4}\oplus\bar{\mathbf 3}_{-4}$ |
| $\mathrm{S}(\mathrm{U}(2)\times\mathrm{U}(2))$ | $\mathrm{SU}(2)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ | $1+1+1=3$ | $(\mathbf3,\mathbf1)_0\oplus(\mathbf1,\mathbf3)_0\oplus(\mathbf1,\mathbf1)_0\oplus(\mathbf2,\mathbf2)_{\pm2}$ |

**Row one buys the spatial block plus one abelian factor. Row two buys weak-times-weak plus one abelian factor. Neither buys the spatial block *and* weak**, because the block needs two ranks and weak needs two, and four exceeds three. **Two ways to spend three ranks, not two halves of five.**

**And the two rows cannot both be exact.** Their Lie bracket generates all fifteen generators of $\mathfrak{su}(4)$, which is simple, so a vacuum annihilated by both would break nothing. **The model must choose, and the corpus chooses the first row — that is what the transition is.**

**The endpoint is the group at $M_C$, and it is the same group below.** The vacuum that produces the two factors is the lepton line $\operatorname{diag}(-3,1,1,1)$, and it is exact at the transition. **The rank is three above and three below**, and the effective theory below is the same group with the sextet removed.

## The Lemma: A Subalgebra Never Outranks Its Algebra

**The statement is one line and it is why the whole article exists.**

> **Lemma.** If $\mathfrak h\subseteq\mathfrak g$ then $\operatorname{rank}\mathfrak h\le\operatorname{rank}\mathfrak g$.

**Proof.** A maximal torus of $\mathfrak h$ is an abelian subalgebra of $\mathfrak g$ consisting of semisimple elements, so it lies in a maximal torus of $\mathfrak g$. Its dimension is therefore at most the dimension of $\mathfrak g$'s maximal torus. 

**The consequence, applied to the model.**

$$
\operatorname{rank}\mathfrak{su}(4)=3
\quad\Longrightarrow\quad
\text{every subalgebra of }\mathfrak{su}(4)\text{ has rank at most }3 .
$$

**Rank is not a dynamical quantity.** It is the dimension of a torus, and a torus does not grow when a vacuum chooses a direction inside it. **So no chain of breakings, in any order, with any dynamics, at any temperature, reaches rank five from rank three.**

**And the block times weak needs five.** The endpoint's dimension is a sum of four positive ranks; the sum is five; the opening balance is three. **Therefore $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ is not a subgroup of $\mathrm{SU}(4)$, and no condensation will make it one.**

**This is a different statement from the usual "the algebra is too small", and it is stronger.** The usual objection says there is not enough *dimension*; but dimension is not the obstacle — $15\ge 8+1+3+3=15$ exactly, so dimension is in fact sufficient. **What is insufficient is rank, and rank is conserved downwards.** That is why the obstruction survives every clever rearrangement of the breaking.

## Two Readings of One Barrier, and Which One the Corpus Uses

**The barrier has two readings, and the migration takes the second.**

| reading | sentence | status |
| --- | --- | --- |
| the wall | the weak force is not inside $\mathrm{SU}(4)$ | true, and it is a dead end |
| the door | therefore the weak force must arrive from beside $\mathrm{SU}(4)$ | true, and it is a construction |

**Read as a wall, the lemma refutes one sentence.** Read as a door, it *proves that any successful story must have the weak force arriving at the transition*, because arriving is the only thing left. **The word for a factor that arrives beside rather than emerging from within is "arrival", and it is the right word.**

**This inversion changes the direction of the argument and it is worth stating slowly.**

**A defensive article says:** the algebra forbids the naive reading, so we retreat to a postulate.
**The correct article says:** the algebra forbids the naive reading, therefore the weak force must be born at the transition, and here is the object that bears it.

**The second is not rhetoric.** The first sentence of the second version is a theorem, and it constrains the construction: whatever bears the weak force must be an object that can arrive, which is to say **not a subalgebra and not a subset of the fifteen.** Among the objects a transition possesses — a vacuum, a condensate, a scalar multiplet, a set of couplings — only the scalar multiplet has indices, and **only an index can bring in a factor.** That is why the mechanism is the index and not the debris.

## The Mechanism: The Condensate That Carries a Doublet

**The object that does the breaking, and the corpus already has it.**

$$
Ξ\in(\mathbf 4,\mathbf 1,\mathbf 2),\qquad 4\cdot1\cdot2=8\ \text{complex},\qquad 16\ \text{real components}.
$$

**It has two kinds of index, and each does one job.**

**The $\mathrm{SU}(4)$ index breaks.** A vacuum along the lepton line, $Ξ\propto(1,0,0,0)$, breaks

$$
\mathrm{SU}(4)\ \longrightarrow\ \mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L},\qquad 15\to9,
$$

**and the six generators that leave are eaten.** They are the sextet, and the corpus proves it twice over: the adjoint mass matrix puts $32v^{2}$ on the six planes through the lepton line and $0$ on the nine that avoid it, and $\operatorname{ad}(iD)$ has the sextet as its $\pm4i$ eigenspace.

**The copy index births.** A scalar that must be a doublet to do its job is a scalar whose condensation simultaneously announces a two-dimensional internal space. **That space is the weak factor**: it is not a fragment of the primordial force, it is a property of the object that killed it.

**The whole story in one table.**

| what happens | where it lives | rank |
| --- | --- | --- |
| $\mathrm{SU}(4)$ condenses along the lepton line | the $\mathrm{SU}(4)$ index of $Ξ$ | $3$ |
| six leptoquarks eaten, the strong group and $B-L$ survive | the stabiliser of that line | $2+1$ |
| a two-dimensional internal space appears | the $\mathbf 2$ index of $Ξ$ | $1$ |
| its chiral half is the second weak factor | the copy structure of the condensate | $1$ |
| **endpoint** | $\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $\mathbf{3+1+1=5}$ |

**Note what the table does not say.** It does not say the sextet becomes anything. **The sextet is eaten and its mass goes up, not down** — the charge theorem and the confinement-scale theorem below are two independent reasons nothing else was possible.

**Note also the ordering of the two events.** The breaking is done by the $\mathrm{SU}(4)$ index, which is a dynamical statement; the birth is done by the copy index, which is a representational one. **The breaking and the birth are one event with two aspects, and the aspects are ranked**: the breaking is the physics, the birth is the bookkeeping of a representation that the physics required.

## The Ranks Add Because the Factors Are Independent

**This is the positive content of the construction, and it is the sentence the article should be remembered by.**

**Ranks add across independent factors and never across a subgroup relation.**

$$
\operatorname{rank}\bigl(\mathrm{SU}(3)\times\mathrm{U}(1)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R\bigr)=2+1+1+1=5 ,
$$

**whereas for any $\mathfrak h\subseteq\mathfrak{su}(4)$ the same sum is capped at three by the lemma.**

**So the arithmetic $3+1+1=5$ is a certificate and not a loophole.** If the weak factors were pieces of the primordial force, five would be unreachable. **That the endpoint reaches five is therefore evidence that the weak factors sit beside — that they are separate factors, born with the transition.**

**"Arrives with the index" and "rank five from rank three" are the same statement in two vocabularies.** The first says where the group comes from; the second says what its rank must be; and the lemma says the two are only compatible if the group is not a subalgebra. **No construction satisfies the second without the first**, which is why the arrival reading is forced rather than chosen.

**One check that the endpoint is a group and not a list.** The four factors are pairwise commuting and each is closed under brackets, so the product is a group of dimension $8+1+3+3=15$ and rank $5$. **Its dimension equals $\mathfrak{su}(4)$'s dimension and its rank exceeds $\mathfrak{su}(4)$'s rank.** Equal dimension with greater rank is possible exactly because the two are not related by inclusion — **which is the whole point in one arithmetic comparison.**

## The Price: One Postulate, in the Corpus's Own Currency

**What is postulated.** That the transition's condensate is a $(\mathbf 4,\mathbf 1,\mathbf 2)$. Nothing in the fifteen forces that representation.

**Why it is cheap in this corpus specifically.** The scalar sector article says it without hedging: *the corpus cannot derive the scalar content: the scalar sector is the one place in the frame with no algebraic guidance at all.* **So the postulate spends a currency the corpus already spends.** The transition does not open a new debt; it names an existing one as the birth certificate of the weak force.

**What is not postulated, and this list is the reason the construction is worth having.**

| object | needed? | why not |
| --- | --- | --- |
| a new symmetry group | **no** | the endpoint is $\mathrm{SU}(3)\times\mathrm{U}(1)\times\mathrm{SU}(2)\times\mathrm{SU}(2)$ |
| a new scale $\Lambda$ | **no** | the scales are $M_C$ and $v$, both of them the corpus's |
| a new confining dynamics | **no** | no bound state is built |
| a matching rule for $W^{3}_L,W^{3}_R$ | **no** | they are the Cartans of factors that exist from the transition on |
| a new vacuum | **no** | $iD=\operatorname{diag}(-3i,i,i,i)$ is the corpus's |

**So the construction adds one line to the ledger and removes a question the corpus could not answer**: why the weak force exists at all.

**The honest size of the postulate.** It is a choice of representation in a sector where the corpus has no guidance. **It is not a small choice** — a $(\mathbf 4,\mathbf 1,\mathbf 1)$ would break $\mathrm{SU}(4)$ and produce no index at all — **but it is the smallest choice available**, and it is the only one that both breaks the primordial force and carries a two-dimensional internal space.

## The Mass Ledger: Where the Weak Masses Actually Come From

**This section exists because the natural objection to a "born" group is that it has no scale.** It has one, and the corpus supplies it.

**The weak bosons get their masses from the two indices of one field, and the two are given at different scales.**

$$
M_X\sim g_4\,v_C,\qquad m_{W}\sim g\,v,\qquad v=246\ \mathrm{GeV},
$$

**with $v_C$ the condensate that does the transition and $v$ the electroweak value.** The chain therefore reads

$$
M_C\ >\ v .
$$

| scale | what happens | who gets mass |
| --- | --- | --- |
| $M_C\gtrsim250\ \mathrm{TeV}$ | $\mathrm{SU}(4)$ breaks, sextet eaten, the strong group and $B-L$ survive | the six leptoquarks |
| $v=246\ \mathrm{GeV}$ | electroweak breaking | $W$, $Z$ |

**The arrival brings in the group and the first vacuum kills the right half of it.** No object is built from parts a thousand times heavier than itself, and the left half waits for its own vacuum.

**The corpus states the same thing in the mass-matrix article, and it is worth repeating because it is the strongest textual support the construction has:** each of the six halves is one spatial plane plus or minus one leptoquark plane, so no one of them is a particle; and **the weak vectors arrive with the doublet index, taking their masses from the vacuum of that index and not from the spatial one.** **That is precisely the mass ledger of this section, written before the construction existed.**

## The Other Route, Closed Elsewhere

**The temptation, stated in its strongest form.** The sextet is six generators and the weak pair is six generators, so perhaps the six recompose into the pair. **Six for six. The dimension matches and nothing else does.**

**Both theorems that close it are proved in [The Charge Theorem](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html)**, with the mass table and the six bracket identities beside them, and repeating the proofs here would be repeating them for the third time in the corpus. In one line each:

- **Charge.** Every sextet member has $Q=\pm\tfrac23$, so two of them bind to $Q\in\{0,\pm\tfrac43\}$ and never to $\pm1$; the $\mathrm{SU}(4)$ singlet is neutral identically. **Six neutral vectors and no charged one, against the observed four charged and two neutral.**
- **Size.** A bound state weighs at least its confinement scale, and here that scale is $M_C\gtrsim250$ TeV, so an $80$ GeV composite is out by more than three orders of magnitude.

**Two theorems and not one, because they are independent.** A repair of the charge problem leaves the mass problem, and the other way round. **A route closed twice is closed in a way that a better calculation cannot reopen**, which is what makes this a closure rather than an objection — and the point that matters *here* is only that the route is closed before the arrival is spent on it.

## What This Does Not Say

**Four boundaries, each one line, because a construction that overstates itself is worth less than one that does not.**

**It does not derive the weak force.** It derives its *rank* — five, which is a theorem — and postulates its *birth* — the doublet index.

**It does not touch the electroweak couplings.** $g$ is the Standard Model's, and this model does not derive it.

**It does not explain chirality.** That the copy index splits into two factors rather than one is inherited from the corpus, which has the split as a fact and not as a derivation.

**It does not fix the order of the two events.** Whether the index appears *with* the condensation or is *required by* it is a phrasing the articles must choose once and keep; the two are different claims and mixing them is how a characterisation becomes a pretended derivation.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the opening rank | $\operatorname{rank}\mathfrak{su}(4)$ | $3$ |
| the endpoint rank | $2+1+1+1$ | $5$ |
| the lemma | a torus of $\mathfrak h$ lies in a torus of $\mathfrak g$ | $\operatorname{rank}\mathfrak h\le\operatorname{rank}\mathfrak g$ |
| the endpoint's dimension | $8+1+3+3$ | $15$, equal to $\mathfrak{su}(4)$'s |
| dimension versus rank | equal dimension, rank $5$ against $3$ | only possible without inclusion |
| the two maximal-rank rows | $\mathrm{U}(3)$ and $\mathrm{S}(\mathrm{U}(2)\times\mathrm{U}(2))$ | both rank $3$ |
| their joint closure | brackets generate all fifteen | simple, so both cannot be exact |
| the sextet's charges | $Q=\pm\frac23$ | sums give $\{0,\pm\frac43\}$, never $\pm1$ |
| the singlet channel | $\mathbf3\otimes\bar{\mathbf3}=\mathbf1_0\oplus\mathbf8_0$ | neutral identically |
| the confinement scale | $M_C\gtrsim250$ TeV | $\gg80$ GeV |
| the mass ledger | $m_W\sim gv$, $v=246$ GeV | from $v$, not from $M_C$ |

## Distinctions That Are Easy to Lose

Rank is not dimension. The endpoint has $\mathrm{SU}(4)$'s dimension and a larger rank; that combination is only possible without inclusion, and it is the proof, not a paradox (*The Lemma*).

An arrival is not a metaphor. It is the name for a factor that enters beside the algebra rather than inside it, and entering beside is the only option once the lemma is granted (*Two Readings of One Barrier*).

The index is not the debris. The weak force is born from a representation the condensate carries, not from what the condensate ate (*The Mechanism*).

Postulating an index is not postulating a sector. The corpus already declares its scalar content underivable; the construction spends that same debt and no other (*The Price*).

The weak masses are not all at $M_C$. The right half is at $M_C$ and the left at $v$; the corpus already says so, and the construction only has to not contradict it (*The Mass Ledger*).

Two theorems are not one theorem twice. Charge closes the composite by quantum numbers, the confinement scale closes it by size; both are proved in *The Charge Theorem*, and this article only spends the conclusion (*The Other Route*).

## Summary

**The weak force can be born at the transition, and the birth certificate is the doublet index of the object that breaks the primordial force.**

**The rank lemma is why it must be so.** $\operatorname{rank}\mathfrak{su}(4)=3$, the endpoint costs $5$, and a subalgebra never outranks its algebra. **So the weak factors are not pieces of $\mathrm{SU}(4)$; they arrive beside it — which is what "arrival" means here, and what $3+1+1=5$ certifies.**

**The mechanism is one object with three indices.** $Ξ\in(\mathbf{15}\oplus\mathbf1)$: the pair of indices breaks $\mathrm{SU}(4)$ and eats the sextet, the $\mathbf 2$ index is the weak force. **The breaking and the birth are one event with two aspects.**

**The sextet cannot do it, twice over.** Charge: $Q=\pm\tfrac23$ sums to $\{0,\pm\tfrac43\}$ and never to $\pm1$, and the singlet is neutral identically. Mass: a bound state weighs at least its confinement scale, and that scale is $250$ TeV. Both proofs are [The Charge Theorem](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html)'s. **Neither closure can be repaired by dynamics.**

**The price is one postulate, paid in a currency the corpus already spends**, and the mass ledger stays the corpus's: $M_C>v$, with the sextet at $M_C$ and $W$ at $v$.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathfrak{su}(4)$ | the primordial force, dimension $15$, rank $3$ |
| $\mathfrak m$ | the leptoquark sextet, $\mathbf3_{+4/3}\oplus\bar{\mathbf3}_{-4/3}$, $Q=\pm\frac23$ |
| $iD$ | the condensate $\operatorname{diag}(-3,1,1,1)$; $\operatorname{ad}(iD)$ has spectrum $0^{9},(\pm4i)^{3}$ |
| $Ξ$ | the transition's scalar, $(\mathbf{15}\oplus\mathbf1)$, $16$ real components |
| $M_C$ | the first breaking scale, $\gtrsim250$ TeV from $K_L\to\mu e$ |
| $v_C,v$ | the transition and electroweak vacuum values, $v=246$ GeV |
| $\Lambda_{\text{confine}}$ | the scale a bound state weighs at least, $=M_C$ here |

## Further Reading

- [The Breaking of the Primordial Force: $\mathrm{SU}(4)\to\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}$ and the Mass of the Six Leptoquarks](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The theorem half of the transition.
- [Six Leptoquarks Above $M_C$: Quantum Numbers, the Mass Ratio, and the Bound From $K_L\to\mu e$](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html). The six states, their mass, and the bound that fixes $M_C$.
- [The Charge Theorem: The Sextet Cannot Be Recomposed Into the Weak Pair](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html). The identities, the mass table, and the two closures in full.
- [The Centraliser, the Complement, and the Index: Dimension Falls at a Breaking, Rank Rises at an Arrival](the-centraliser-the-complement-and-the-index-dimension-and-rank.html). The grammar this article uses.
- [The Matching at $M_C$](matching-at-m-c.html). The scale ledger and the interface with the left–right corpus.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The multiplet, and the sentence about the corpus having no algebraic guidance for it.
