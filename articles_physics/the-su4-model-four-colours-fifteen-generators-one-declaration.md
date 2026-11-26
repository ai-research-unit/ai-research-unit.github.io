# __The $\mathrm{SU}(4)$ Model: One Group, Fifteen Generators, One Declaration__

## Introduction

**The model is one group.** Not a product, not a pair of weak factors beside a colour group: one simple group acting on one four-dimensional complex space.

$$
\boxed{\;
G=\mathrm{SU}(4),\qquad
\dim_{\mathbb R}\mathfrak g=15,\qquad
\operatorname{rank}\mathfrak g=3,\qquad
15=\underbrace{8}_{\mathfrak{su}(3)}\oplus\underbrace{1}_{\mathbb R\,iD}\oplus\underbrace{6}_{\mathfrak m}
\;}
$$

**One group, fifteen generators, one declaration.** The fifteen split, *below the transition*, as eight of colour, one abelian direction and six leptoquarks. **Above the transition there is no colour group and no colour label**: there are four lines of one quartet, and the only statement the algebra does not make is which of the four lines is the lepton. **The labels themselves are coordinates, and Gauge Fields: An Introduction to Quantum Theory prints all fifteen and shows why none of them is a charge.**

**Why the group is one and not three.** The fifteen contains a real $\mathfrak{so}(4)$, spanned by the six real antisymmetric planes, and those six directions look like two weak triples. **They are not.** A factor is a group; a subalgebra is a subspace of the algebra, and reading a subalgebra as a factor is what names three groups where the algebra has one. **The six arrays are $\mathfrak{so}(4)$ in a rotated basis.** §*The Real $\mathfrak{so}(4)$ Inside the Fifteen* computes which one this is, and the next section of the corpus says what the weak force actually is.

**The two layers, and the one that matters here.** Layer A is what the algebra does on its own carrier. Layer B is $\mathrm{SU}(4)$ acting on a formal copy of that carrier. **The distinction is load-bearing**: the algebra's commutant forces the copy, and §*The Carrier Is a Copy* proves it with a count.

**What this article establishes.** That the group is $\mathrm{SU}(4)$ and the count is fifteen; that the fifteen split as $8+1+6$; that the matter content is the sixteen and that it is vector-like under the group, so its anomaly cancels by counting; that one coupling multiplies all fifteen generators; that the fifteen already contains a real $\mathfrak{so}(4)$ of six dimensions and rank two; that the sixteen is closed under $C$ and, since $P$ maps it to itself as well, under $CP$, so the content is real under both while the Lagrangian's phases remain free; and that the ceiling on any group commuting with the Lorentz action is $\mathrm{SU}(2)$, which is why the carrier is a copy.

**What it does not establish.** That the algebra derives the group — it derives the group *given* the carrier. That the lepton line is the fourth colour — that is declaration (A). That the model is chiral where it gauges — **it is not, and §*The Chiral Wall* shows that this is now a theorem about the model rather than a caveat about a representation.**

**What is absent here.** No weak pair, no hypercharge, no photon, no $W$, no $Z$, no rank five. **Those arrive at $M_C$, where colour, one abelian factor and two weak factors describe what the vacuum leaves**, and that is the subject of the next section of the corpus. This article is the gauge content of the model above that scale, and it is complete as a statement of that content: **the scalar sector is $W$, and the fermion masses are $Z$, whose verdict is that the ratio $m_\ell=3m_q$ is falsified.**

**Where the rest is.** The counts and the arrays are [The Counts of the Fifteen](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html) and [The Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The transition is [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). What the weak force is, and why it is not a piece of the fifteen, is [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). The couplings are [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html).

## One Group, and the Count of Fifteen

**Where the group comes from.** The algebra $\mathbb B\cong M_2(\mathbb C)$ acts on its own carrier, a four-dimensional complex space. **The unitary group of that carrier is $\mathrm{SU}(4)$**: the matrices with $M^{\dagger}M=\mathrm I$ and $\det M=1$. It is not an element of the algebra and not a corner of its endomorphisms; **it is the whole group of the space the algebra acts on.**

**The count, from the arrays.** Take the four indices $(t,x,y,z)$ and the matrices that act on them.

| building block | count | what it is |
| --- | --- | --- |
| real antisymmetric planes $A_{jk}$ | $6$ | one per unordered pair |
| imaginary symmetric planes $iS_{jk}$ | $6$ | one per unordered pair |
| trace-free diagonals | $3$ | $iD$ and two colour diagonals |
| **total** | $\mathbf{15}$ | $\mathfrak{su}(4)$ |

**Six pairs, two arrays per pair, three diagonals: $12+3=15$.** The count is not a choice. There are $\binom42=6$ pairs of four indices; each pair carries a real and an imaginary array; and a trace-free diagonal has three dimensions.

**The same count from the cells.** A $4\times4$ grid has sixteen cells. The four diagonal cells span four directions and one combination of them is the trace, which $\mathfrak{su}(4)$ excludes; **three trace-free diagonals remain, and with the twelve off-diagonal cells they are the fifteen generators.**

$$
16=1+15 .
$$

**One grid, sixteen cells.** A product of factors would need one grid per factor, and a trace to remove from each; **one group needs one grid, and one trace removed from its sixteen cells gives the fifteen generators.**

**The split that the declaration fixes.** Under $\mathrm{SU}(3)_c$ acting on the three colours,

$$
\mathbf{15}=\mathbf 8_{0}\oplus\mathbf 1_{0}\oplus\mathbf 3_{+4/3}\oplus\bar{\mathbf3}_{-4/3},
$$

that is

$$
15=8+1+6 .
$$

**The eight is colour. The one is the abelian direction $iD$. The six is the leptoquark sextet**, carrying one colour and one lepton index at once, with $B-L=\pm\tfrac43$ and $Q=\pm\tfrac23$ once charge is defined.

**Read the split as a fate list.** The eight survive every breaking of the model as gluons. The one survives as the $B-L$ vector and later mixes. **The six are the only coloured massive vectors in the theory — massive below $M_C$, and massless above it, like every other vector of the fifteen**, and they are what a leptoquark search looks for.

**The rank.** A maximal torus of $\mathfrak{su}(4)$ has dimension three. It is spanned by $iD=\operatorname{diag}(-3i,i,i,i)$ and the two trace-free colour diagonals. **Rank three, and no breaking of this group reaches rank five** — not because of dynamics, but because a subalgebra never outranks its algebra. **That single line is why two weak factors cannot be pieces of this one.**

## The Sixteen, and the Copy Index

**The matter content, in one line.**

$$
\mathbf{16}=\mathbf 4\otimes\mathbf 2\ \oplus\ \bar{\mathbf4}\otimes\mathbf 2,
\qquad
4\cdot2+4\cdot2=16 .
$$

**Read the two factors of each term.** The first is the colour index: a quartet, lepton plus three colours. The second is a **copy index**, two-dimensional. Nothing else.

**The copy index is a label here, not a group factor.** It does not multiply a generator in the covariant derivative, it has no coupling, and no field in this model transforms under it. **It records that the matter comes in two copies**, and that is all it does in this article.

**What the two copies are.** They are the two chiralities of the sixteen, each a doublon of the quartet:

$$
\mathbf{16}=\underbrace{\mathbf 4\otimes\mathbf 2}_{\text{two copies of the quartet}}\oplus\underbrace{\bar{\mathbf4}\otimes\mathbf 2}_{\text{two copies of its conjugate}} .
$$

**The neutrino is not added.** The lepton line of the conjugate quartet, at $B-L=+1$, is the right-handed neutrino's slot. **The moment the lepton is a colour, the fourth component of the $\bar{\mathbf4}$ is forced, and it is a neutrino.** That is forced by the colours alone.

**The anomaly, by counting.** Under $\mathrm{SU}(4)$ alone the content is

$$
2\cdot\mathbf 4\ \oplus\ 2\cdot\bar{\mathbf4},
$$

**two quartets and two antiquartets.** The cubic index is $+1$ on the $\mathbf4$ and $-1$ on the $\bar{\mathbf4}$, so the $\mathrm{SU}(4)^3$ triangle coefficient is

$$
2(+1)+2(-1)=0 .
$$

**Zero by pairing, not by a numerical accident.** The spectrum is vector-like in pairs, so the anomaly cancels identically — and so does every mixed coefficient, because there is only one factor and nothing to mix with.

**The cancellation here costs no trace computation**, because the spectrum is vector-like in pairs. **The three hypercharge traces are conditions elsewhere**: hypercharge and the weak factors enter at $M_C$, and $\operatorname{tr}Y=0$, $\operatorname{tr}Y^{3}=0$ and the even doublet count become conditions on the spectrum below that scale.

**One remark, kept because it is a real computation.** The left-handed quartet gave $\operatorname{tr}Y^{3}=-\tfrac29$, computed as

$$
6\cdot\Bigl(\tfrac16\Bigr)^{3}+2\cdot\Bigl(-\tfrac12\Bigr)^{3}=\tfrac{1}{36}-\tfrac14=-\tfrac29 ,
$$

and its conjugate gave $+\tfrac29$ with the signs reversed, so the sum vanished. **The cancellation was between a representation and its own conjugate** — which is exactly the pairing that now makes the $\mathrm{SU}(4)$ anomaly vanish by counting. **The same structural fact, read on a smaller group.**

## One Covariant Derivative

**The whole gauge content is one line, and it is shorter than it used to be.**

$$
D_{\imath}=\partial_{\imath}-ig_4\sum_{a=1}^{15}A_{a,\imath}t_{a} .
$$

**One sum, fifteen fields, one coupling.** Three factors would bring three sums and three couplings; here there is one of each, and no ratio to fix. **The $t_{a}$ are Hermitian and normalised by $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$**, the same fifteen the Lagrangian uses; the anti-Hermitian printed arrays $G_{a}$ differ from them by a factor $i$ and a rescaling, and [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) fixes that once in §*The Normalisation*.

**Every index is low**, because the colour index's metric is $\delta_{\imath\jmath}=(1,1,1,1)$: a raised index names the same index. **The label $a$ is a name and not a frame slot**; it counts the fifteen generators. **The spacetime index is the exception and the two never mix**: a Dirac operator contracts it with the Minkowski weight $\varepsilon_{\imath}=(1,-1,-1,-1)$, as [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) states, while every index of this article's $4\times4$ matrices is colour and carries no weight.

**What the fifteen fields are.**

| block | count | $\mathrm{SU}(3)_c$ below $M_C$ | fate: above $M_C$ | fate: below $M_C$ |
| --- | --- | --- | --- | --- |
| $a$ in the $\mathfrak{su}(3)$ corner | $8$ | $\mathbf 8$ | **the eight colour directions, massless** | the gluon octet, massless |
| $A_{15}$ | $1$ | $\mathbf 1$ | the $B-L$ vector, massless | massless until it mixes downstream |
| $a$ in $\mathfrak m$ | $6$ | $\mathbf 3+\bar{\mathbf3}$ | **the sextet, massless** | **heavy at $M_C$** |

**Below $M_C$ there are nine massless and six massive, and that is the whole connection spectrum at that scale.** Above $M_C$ all fifteen are massless, no vacuum having formed — **and that includes the six leptoquarks, whose mass exists only once the condensate does.** The two columns are the point: **the sextet's column changes and the other two do not**, and a reader who reads "heavy" in the third row without the column heading has read the broken phase into the unbroken one.

**And the middle column says *eight*, not *the gluons*, on purpose.** Above $M_C$ the group is one factor and **no $\mathrm{SU}(3)$ is gauged**, so *gluon* is a name the broken phase supplies: the eight are the six colour–colour off-diagonals plus the two colour diagonals, defined by the lines they move and not by a subgroup. **The $\mathrm{SU}(3)_c$ column is therefore a branching and not a pre-breaking content**, and §*The Names, and Which Phase They Belong To* of [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html) states what changes at the transition and what does not — **the count $6+2=8$ never changes; only which group the two diagonals belong to does.**

**No $W$, no $Z$ and no photon in this list**: those need the weak factors, which arrive at $M_C$ in the same condensation that gives the right-handed pair its mass, and they become massive at $M_W$. **The scalar sector is not in this table**: it is sixteen real components in *The Scalar Content*, six of them eaten by these six vectors.

**What the model does not tie.** One connection coupling above $M_C$, so there is no ratio between connection couplings to fix. **That is not the absence of a matching problem; it turns the matching into a prediction**: the three couplings below $M_C$, and the four decades between the strong and the electroweak scales, are what one $g_4$ runs into, and they are treated in [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html). **The scalar and Yukawa couplings are separate parameters and this article fixes none of them.**

## The Real $\mathfrak{so}(4)$ Inside the Fifteen

**The six planes are the one place the algebra looks like a weak sector, and it is worth doing properly.**

**The object.** The algebra multiplies on two sides, so left and right multiplication by the imaginary units give two commuting triples:

$$
\mathfrak k_L=\{L_{\vec e_a}\},\qquad \mathfrak k_R=\{R_{\vec e_a}\},\qquad [L_{\vec e_a},R_{\vec e_b}]=0 .
$$

**Each triple is three real dimensions, they commute, and together they span six.** That six is exactly the span of the six real antisymmetric plane arrays:

$$
\mathfrak k_L\oplus\mathfrak k_R=\operatorname{span}\{A_{ab}\ :\ a<b\},\qquad \dim_{\mathbb R}=6 .
$$

**Both statements are computations, not identifications.** The six $A_{ab}$ number six, they are closed under brackets, and each $L_{\vec e_a}$ and $R_{\vec e_a}$ is a real combination of them — in the corpus's basis,

$$
T^{L}_{x}=-\tfrac12\bigl(A_{tx}+A_{yz}\bigr),\qquad
T^{R}_{x}=-\tfrac12\bigl(A_{tx}-A_{yz}\bigr),
$$

and cyclic in $(x,y,z)$. **Those six combinations span the same six dimensions as the six $A_{ab}$**, which is why the two descriptions are one subspace written twice.

**What it is, and what it is not.** It is a **real subalgebra of the fifteen**, with $\dim_{\mathbb R}=6$ and rank $2$. It is **not** a second factor: a factor is a group multiplying the algebra's fields, and this is a subspace of the algebra itself. **The difference is not bookkeeping** — it is the difference between rank three and rank five.

**What the condensate does to it.** The transition's vacuum is $iD=\operatorname{diag}(-3i,i,i,i)$, that is $D=\operatorname{diag}(-3,1,1,1)$ multiplied by $i$, and the mass matrix of the fifteen is

$$
M^{2}=2v^{2}\bigl[D,[D,\cdot\,]\bigr],
$$

**which is diagonal on the plane arrays with one number per plane:**

| planes | $m^{2}$ |
| --- | --- |
| $A_{ta},A_{ty},A_{tz}$ | $32v^{2}$ |
| $A_{xy},A_{xz},A_{yz}$ | $0$ |
| $iS_{ta},iS_{ty},iS_{tz}$ | $32v^{2}$ |
| $iS_{xy},iS_{xz},iS_{yz}$ | $0$ |
| the three diagonals | $0$ |

**So the real $\mathfrak{so}(4)$ straddles the transition**: three of its six planes are heavy and three are massless. **A half, being half of one plane and half of the other, is a sum of a heavy and a massless vector** — a coherence, not a particle. That single fact is why the six arrays could never be the weak bosons, and [The Charge Theorem](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html) makes it a theorem.

**Why the reading is tempting, and where the three sixes differ.** Six real planes, six leptoquark arrays and six weak generators are **three different sixes, and only the first two are even inside the fifteen**. The six planes are $\operatorname{span}\{A_{ab}\}$ and they close; the six leptoquarks are $\{A_{tk},iS_{tk}\}$ and they do **not** close, since $[A_{tx},A_{ty}]=-A_{xy}$ lies outside them; and the six weak generators close by assumption, not by arithmetic. **The match is a match of number and nothing else**: the planes are closed but are not the leptoquarks, the leptoquarks are not closed, and neither set is the weak pair.

**The honest sentence for this article.** **The fifteen contains a six-dimensional real subalgebra that looks like a weak sector and behaves like one under every operation except the three that matter** — it does not close on the sextet, its charges are thirds rather than integral, and its directions are half heavy. **A subalgebra is not a factor, and the three failures are why.**

## What Is Derived and What Is Declared

**Three different strengths, and the difference has to be stated or the article overclaims.**

| item | where it comes from | status |
| --- | --- | --- |
| $\mathrm{SU}(4)$ | the unitary group of the carrier | derived, given the carrier |
| the split $\mathbf 4=\mathbf 1\oplus\mathbf 3$ | $\mathbb C e_t\oplus B_V$ | derived, and the only canonical one |
| the identification with the quark–lepton quartet | — | **declared, (A)** |
| the sixteen | two copies of $\mathbf4$ and of $\bar{\mathbf4}$ | declared content, vector-like by construction |
| the copy index | — | declared, and ungauged here |
| chirality | the copy index | declared |
| any equality of couplings | — | not applicable: one coupling |

**The criterion of legitimacy, restated.** The corpus once carried an implicit test: a symmetry group is legitimate only if its generators are elements of the algebra, $X\in\mathbb B$. **That test is wrong and it has to go**, because $\mathfrak{su}(3)$ and $\mathfrak{su}(4)$ live in the endomorphisms of $\mathbb B$ and never in $\mathbb B$.

**The replacement is an address, not a filter.** A generator is an element of $\operatorname{End}_{\mathbb C}(\mathbb B)$, and the sixteen words $e_{\imath}[\,]e_{\jmath}=L_{e_{\imath}}R_{e_{\jmath}}$ are a basis of it. **The length of a generator is the rank of its coefficient array, and Conway's bound is four**:

$$
M=\sum_{\imath,\jmath}c_{\imath\jmath}\,L_{e_{\imath}}R_{e_{\jmath}},\qquad
\ell(M)=\operatorname{rank}\bigl(c_{\imath\jmath}\bigr)\le4 .
$$

**The ladder, for the generators this model names.**

| object | in $\mathbb B$? | length | the words |
| --- | --- | --- | --- |
| central $\mathrm{U}(1)$ | yes, $\mathbb R(ie_t)$ | $1$ | $L_{e_t}R_{e_t}$ |
| the six sides $\mathfrak k_L\oplus\mathfrak k_R$ | no | $1$ | $L_{\vec e_a}R_{e_t}$, $L_{e_t}R_{\vec e_a}$ |
| $\mathrm{SU}(3)_c$ | no | $2$ on seven, $3$ on $\operatorname{diag}(0,1,1,-2)$ | off-diagonal pairs of $B_V$, and the Cartan |
| $\mathrm{SU}(4)$ | no | $1$ on the six unscaled words, $2$ or $3$ on the other named generators, $4$ generic | all fifteen |
| $B-L$ | no | $3$ | $i\sum_a L_{\vec e_a}R_{\vec e_a}$ |

**Only the central phase is in the algebra.** Everything else is an endomorphism, at length one, two, three or four. **The table records addresses, and it is not a hierarchy**: $\mathfrak{su}(4)$ has a basis of fifteen elements of length one, so "the group $\mathrm{SU}(4)$ has length three" is not a statement.

**What selects the group is the module, and it selects it up to one choice.** The algebra supplies one four-dimensional complex module, and the largest compact simple group acting faithfully on it is $\mathrm{SU}(4)$; $\mathrm{SU}(5)$ needs five dimensions and $\mathrm{SO}(10)$ sixteen, and the algebra supplies neither. **Maximality is not a principle of physics, so what this fixes is the menu and not the choice**: the group is the maximal one of the module, which is what the table of §*What Is Derived* means by *derived, given the carrier*.

## Why This Group and Not a Larger One

**Two refusals, and one non-competitor.**

**$\mathrm{SU}(5)$.** Rank four, and its $\mathbf{10}+\bar{\mathbf5}$ has no right-handed neutrino and puts quarks and leptons in one multiplet in a way the algebra's split does not suggest. **The corpus's $\mathfrak{su}(4)$ is the carrier's group; $\mathfrak{su}(5)$ would be a group with no carrier in the algebra.**

**$\mathrm{SO}(10)$.** Rank five, and it contains $\mathrm{SU}(4)$ — **but its spinor is a $\mathbf{16}$ obtained by a Clifford algebra the corpus does not otherwise use**, and containment is not a derivation. It is recorded and refused.

**The four-factor group is the group at $M_C$.** Colour, one abelian factor and the two weak factors are what the vacuum of the primordial force leaves, and the weak factors arrive at that scale. **It is a step of the transition, not a rival candidate**: an alternative would be a group chosen instead, and this one is arrived at.

**The one-line reason the group is $\mathrm{SU}(4)$.** The full group of a four-dimensional complex carrier is $\mathrm{SU}(4)$, and the subgroup that fixes one line in it is $\mathrm{SU}(3)\times\mathrm{U}(1)$ modulo a discrete factor. **The stabiliser is a subgroup of $\mathrm{SU}(4)$, not an alternative to it** — it is what acts once the fourth direction is frozen out, and which of the two describes the world is a question about physics. **Whether the fourth direction is made local is that question, and this model answers that it is.**

## The Uniqueness Result, Demoted

**A theorem that used to be quoted in support, now recorded and set aside.**

**The result.** Boyle and Farnsworth ask which finite algebra carries the Standard-Model group as its inner automorphisms, in an $8\times8$ Hermitian block-diagonal representation commuting with the chirality. **The answer is unique**, and it is a sum of three simple Jordan algebras:

$$
\mathcal A_F=J_2^{L}(\mathbb C)\oplus J_2^{R}(\mathbb C)\oplus J_4(\mathbb C),
$$

of real dimension $4+4+16=24$, in blocks of size $2,2,4$. **Its automorphism group has Lie algebra $\mathfrak{su}(2)\oplus\mathfrak{su}(2)\oplus\mathfrak{su}(4)$, of dimension $3+3+15=21$** — three factors in all, and still not one group.

**Why it is demoted, in one paragraph.** The theorem forces a **product group** in a representation the corpus does not use. **The model here is one simple group**, so a theorem that forces a product is a theorem about a different object. **It is neither evidence against the $\mathrm{SU}(4)$ model nor evidence for it**, and it is recorded so that the citation is not mistaken for support.

**What survives from it, and is independent.** The Hermitian part of the corpus's operator layer is the single Jordan algebra $J_4(\mathbb C)$ of dimension sixteen, **whose derivation algebra is $\mathfrak{su}(4)$ of dimension fifteen.** That computation does not depend on the theorem: it is one Jordan algebra against four, and it is the corpus's own.

**And the one thing the theorem genuinely settled.** That the labelling of the quartet's directions is a choice — the source recovers observed charges only after adjoining an outer abelian factor. **Declaration (A) remains a declaration under any theorem**, which is why the corpus states it as one.

## The Carrier Is a Copy, and Here Is the Theorem

**The objection.** If $\mathrm{SU}(4)$ acts on the same four dimensions as the Lorentz action, the two must commute — and then colour would have to sit in the commutant of the Lorentz algebra, where there is no room for it.

**The computation, and it is the load-bearing one.**

$$
\mathfrak{su}(4)\cap\bigl\{X:[X,L_{\vec e_a}]=0\ \text{for }a=x,y,z\bigr\}
=\operatorname{span}\{R_{\vec e_x},R_{\vec e_y},R_{\vec e_z}\}\cong\mathfrak{su}(2),
\qquad
\dim_{\mathbb R}=3 .
$$

**The proof, in three counts.**

**First, the commutant.** As a module for $L(\mathbb B)\cong M_2(\mathbb C)$ the carrier is $\mathbb C^2\otimes\mathbb C^2$, with $L(\mathbb B)$ acting on the first factor. **By Schur's lemma the commutant is $\operatorname{End}_{\mathbb C}(\mathbb C^2)$, real dimension eight, and that commutant is exactly $R(\mathbb B)$.**

**Second, the anti-Hermitian part.** Of those eight real dimensions, four are anti-Hermitian: $R_{\vec e_a}$ together with $R_i=i\,\mathrm I_4$.

**Third, the trace.** $\operatorname{tr}R_i=4i\ne0$, so $R_i$ is excluded by the tracelessness of $\mathfrak{su}(4)$ read on the array in the coefficient basis. **What remains is $\{R_{\vec e_x},R_{\vec e_y},R_{\vec e_z}\}$: three real dimensions, and that is $\mathfrak{su}(2)$.**

**So the ceiling is $\mathrm{SU}(2)$, and it is attained by $\mathfrak k_R$.** This is exactly the $\mathfrak k_R$ of the earlier section — **the commutant theorem and the real $\mathfrak{so}(4)$ are the same structure seen from two sides.** A ceiling of dimension three forces the tensor product:

$$
(\text{internal }\mathbf 4)\otimes(\text{spinor}),
\qquad
\mathbf 4_{\text{int}}\cong\mathbb C e_t\oplus B_V .
$$

**The internal quartet is a formal copy of the carrier**: it inherits the split, because the split is canonical, and it does not inherit the Lorentz action, because it must not. **$M_4(\mathbb C)$ cannot host two large commuting compact groups**, and that is a fact about dimension, not about this model.

**One consequence worth stating, and it is negative.** The commutant result also says the fifteen contains a distinguished $\mathfrak{su}(2)$ — the one inside the commutant — **of rank one inside rank three.** **The vacuum does not preserve it.** On $D=\operatorname{diag}(-3,1,1,1)$,

$$
\bigl[D,T^{R}_{x}\bigr]=2\bigl(E_{tx}+E_{xt}\bigr)\ne0 ,
$$

**so $\mathfrak{k}_R$ is broken at $M_C$, and its three directions are not mass eigenstates either** — they are the half-sum of a $32v^{2}$ direction and a $0$ direction, exactly as the plane arrays are. **So the commutant supplies a distinguished $\mathfrak{su}(2)$ and not a weak factor**, which is [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html)'s point: the weak factors arrive beside the group and not inside it.

## The Chiral Wall, Which Is Now a Theorem

**Under one group the statement gets simpler and stronger.**

**What a chiral connection theory needs.** A connection action that distinguishes left from right at the level of the *coupling* — an action of the group on one copy of the matter and not on its conjugate.

**What this model has.** One copy index, ungauged, and one coupling multiplying the fifteen. **The made local content is $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$, vector-like in pairs.** A vector-like made local sector has no chiral connection coupling at all, and therefore:

> **The model is not chiral where it fixing conditions. This is not a caveat about a representation; it is a property of the model, proved by the same count that makes its anomaly vanish.**

**Where the chirality is.** Nowhere in this article, and the article says so. The copy index is a label the group does not see. **A single $\mathrm{SU}(2)$ acting on it would not change that**, because $\mathbf2\simeq\bar{\mathbf2}$ and $(\mathbf4,\mathbf2)\oplus(\bar{\mathbf4},\mathbf2)$ is its own conjugate — the count $2\cdot4\oplus2\cdot\bar4$ is vector-like under any group that acts on the copy index the same way in both terms. **A chiral content needs the two copies acted on by two different factors**, $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$, and **that split is a postulate of the transition rather than a consequence of this article** — [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html) carries it as exactly one postulate and names it.

**What would count as the algebra supplying chirality.** A one-sided action of the algebra on a chiral spinor module. **That remains the corpus's open problem, unchanged, and it is not solved here.** What has changed is that the model no longer pretends to have the answer in a representation: **it declares the copy index, and the declaration is honest because the index is visible.**

**What is refused.** Writing the sixteen as a single multiplet of a larger group and calling the chirality derived, when the multiplet is real. **A real multiplet cannot be chiral**, and the sixteen becomes chiral only when the copy index splits into two separately made local factors.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the dimension | arrays: $6$ pairs $\times\,2+3$ diagonals | $15$ |
| the cells | $4\times4$ minus the trace | $1+15$ |
| the split | branching of the $\mathbf{15}$ under $\mathrm{SU}(3)_c$ | $8+1+6$ |
| the sextet's $B-L$ | $(-1)-\bigl(+\tfrac13\bigr)$ | $\pm\tfrac43$ |
| the sextet's charge | $\tfrac12(B-L)$ with no isospin | $\pm\tfrac23$ |
| the rank | maximal torus of $\mathfrak{su}(4)$ | $3$ |
| the matter content | $(4\otimes2)\oplus(\bar4\otimes2)$ | $8+8=16$ |
| the $\mathrm{SU}(4)$ content | two quartets, two antiquartets | vector-like |
| the $\mathrm{SU}(4)^3$ index | $2(+1)+2(-1)$ | $0$ |
| the classical trace check | $\operatorname{tr}Y^{3}$ left, right | $-\tfrac29,+\tfrac29$, sum $0$ |
| the mixed anomaly | one factor, nothing to mix with | absent |
| the commutant | $8\to4\to3$ | $\mathfrak{su}(2)$ |
| $\mathfrak{so}(4)$ inside the fifteen | $\operatorname{span}\{A_{ab}\}$ | $\dim6$, rank $2$, closed |
| $[\mathfrak k_L,\mathfrak k_R]$ | all nine pairs | $0$ |
| the condensate on $\mathfrak{so}(4)$ | $2(1-(-3))^{2}$ on $A_{ta}$, $0$ on $A_{jk}$ | $32v^{2}$ and $0$ |
| the trace norms | $\operatorname{tr}(A^{2})$, $\operatorname{tr}(iD)^{2}$ | $-2$, $-12$ |

## Distinctions That Are Easy to Lose

A subalgebra is not a factor. $\mathfrak{so}(4)$ is six real dimensions inside the fifteen; a factor would be a group multiplying the fields. **Rank three against rank five is the difference** (*The Real $\mathfrak{so}(4)$*).

The copy index is not a group factor. It labels two copies of the quartet and carries no coupling; it becomes a factor only at the transition, and **the split of that factor into two weak factors is the transition's postulate and not this article's** (*The Sixteen*, *The Chiral Wall*).

Vector-like is not a defect. It is why the anomaly vanishes by counting, and it is why the model has no chiral connection coupling — the second being what the transition to $M_C$ exists to fix (*The Chiral Wall*).

One coupling is not a simplification of three. It is the absence of the two factors that carried the other two, and it turns the three low-energy couplings into a prediction: the matching at $M_C$ becomes a computation rather than a fit (*One Covariant Derivative*).

A theorem about another group is not evidence about this one. The Boyle–Farnsworth result forces a product group in a representation this frame does not use (*The Uniqueness Result, Demoted*).

## Summary

**One group.** $\mathrm{SU}(4)$, fifteen real dimensions, rank three, one connection coupling. **No product, no second factor, and no rank five anywhere above $M_C$** — the four factors and the rank five are what the vacuum leaves at that scale, and they are not a piece of this group.

**The count is fifteen, twice over.** Twelve plane arrays and three diagonals; or sixteen cells minus the trace. **The split is $8+1+6$**: colour, the abelian direction, and the six leptoquark planes.

**The sixteen is $2\cdot\mathbf4\oplus2\cdot\bar{\mathbf4}$** — two copies of the quartet and two of its conjugate, with the copy index as a label. **Vector-like in pairs, so the anomaly cancels by counting rather than by three traces**, and the model is not chiral where it fixing conditions.

**The fifteen already contains a real $\mathfrak{so}(4)$ of six dimensions and rank two**, spanned by the six antisymmetric planes and equal to $\mathfrak k_L\oplus\mathfrak k_R$. **It is the subalgebra that looks like two weak factors and is not.** It is a subalgebra, not a factor, and the condensate puts $32v^{2}$ on three of its planes and $0$ on the other three — **which is why the six arrays are not the weak bosons.**

**The ceiling on a commuting group is $\mathrm{SU}(2)$**, by the commutant count $8\to4\to3$, and that is why the carrier is a formal copy. **That $\mathfrak{su}(2)$ is not a weak factor**: the condensate breaks it, $[D,T^{R}_{x}]\ne0$, so its directions are coherent sums and not mass eigenstates. **The weak factors arrive beside the group; nothing in the fifteen supplies them.**

**Nothing numerical moved.** The spectrum of $\operatorname{ad}(iD)$, the masses, the sextet's charges and the nine massless directions are exactly as the first-breaking section states them. **The frame changed; no eigenvalue did.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $G=\mathrm{SU}(4)$ | the group, acting on the four-dimensional complex carrier |
| $\mathfrak m$ | the leptoquark sextet, $\mathbf3_{+4/3}\oplus\bar{\mathbf3}_{-4/3}$ |
| $iD$ | $\operatorname{diag}(-3i,i,i,i)$, the abelian direction and the transition's vacuum |
| $\mathbf{16}$ | the matter content, $\mathbf4\otimes\mathbf2\oplus\bar{\mathbf4}\otimes\mathbf2$ |
| the copy index | the two-dimensional label on the quartet; ungauged here |
| $\mathfrak k_L,\mathfrak k_R$ | the two commuting triples from the two-sided action |
| $\mathfrak{so}(4)$ | $\mathfrak k_L\oplus\mathfrak k_R=\operatorname{span}\{A_{ab}\}$, six real dimensions inside the fifteen |
| $A_{ab},iS_{ab}$ | the real antisymmetric and imaginary symmetric plane arrays |
| $g_4$ | the one coupling |
| (A) | the declaration that the line $e_t$ is the lepton |

## Further Reading

- [The Counts of the Fifteen: Sixteen Cells, Six Pairs, Twelve Arrays](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html). The arithmetic of this article, counted five ways.
- [The Classification of the Bosons: Nine Massless and Six Massive](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). One name in every cell of the $4\times4$ grid.
- [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html). Every generator printed, and the six $\mathfrak{so}(4)$ planes beside them.
- [Charge Quantisation From the Fourth Colour: One Trace, One Third](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). Why the corner is forced and the charges are in thirds.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). What the transition does to the fifteen.
- [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). Why the six arrays are not a factor, and what is.
