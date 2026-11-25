# __Where the Fifteen Generators Go: One Ledger, Three Readings, and the One Abelian Factor__

## Introduction

**The question.** Fifteen generators, one group, one breaking. Which generator goes where, and what happens to each one?

**The answer has three parts, and the first is arithmetic.**

$$
15=\underbrace{8}_{\mathfrak{su}(3)}+\underbrace{1}_{\mathbb R\,iD}+\underbrace{6}_{\mathfrak m}.
$$

**That single equation is the frame, and it is also the reason the frame can break to the Standard Model**: of the fifteen, eight are the gluons, one is the $B-L$ boson and six are leptoquarks. **There is no second equation, because there is no second factor.**

**The names are the ones the boson articles use, and this article renames nothing.** **The six arrays $T^{L}_{a}$, $T^{R}_{a}$ appear once below, in a row that says what they are not.** The corner array is $iD=i\operatorname{diag}(-3,1,1,1)$ and its boson is $B'$; the six off-diagonal colour arrays are $A_{xy},iS_{xy}$ and their four relatives, printed as $g_{1},g_{2},g_{4},g_{5},g_{6},g_{7}$; the two colour diagonals are $d_{2},d_{3}$, printed as $T^{c}_{3},T^{c}_{8}$; the six mixed planes are $A_{ta},iS_{ta}$ for $a=x,y,z$, printed as $\bar X^{a},X^{a}$; the six weak arrays are $T^{L}_{a},T^{R}_{a}$, printed as the two $W$ triples. **The atoms are the same atoms, so the counts can be checked against the matrices entry by entry.**

**What this article does not do.** It computes no matrix, chooses no vacuum and derives no mass. The arrays are printed one at a time in [The Fifteen AXF Matrices of the Bosons in Detail](the-15-axf-matrices-of-the-bosons-in-detail.html) and built in [Construction of the AXF Matrices](construction-of-the-axf-matrices-of-the-fifteen-generators.html); the chain is in [The Breaking Chain](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html); the states are tabulated in [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). **This article reads one ledger, three ways, and then answers the one question the ledger raises and cannot settle: which abelian factor survives.**

**The three readings, named before they are used.** The first sorts the fifteen by what each does to the time line $\mathbb C e_t$ and finds $8+1+6$ — a sort that uses no structure beyond the split the matrix already has. The second grades the sextet by $D$ and finds two triples, which is the particle–antiparticle pairing of the six. The third reads the same nine as a maximal compact subalgebra, and there the leptoquark count becomes a compactness count. **Each reading is a different question asked of the same table**, and none of them introduces a new object.

## The Ledger, and Where It Is Printed

**The ledger is the summary of two articles that print more than a summary.** The detail article prints all twenty-one, one section per array, with the boson named before the array; the classification article names the cell of each in the three grids and lists the twenty-one states they become. **The table below is their join, and it exists because the two questions "which array is it" and "what does it become" are answered in different places.**

**The ledger.** Every generator of the frame, with the array it is, the factor it sits in, what it becomes, and the scale at which it does so.

| class | count | the arrays | sits in | after the chain | scale |
|---|---|---|---|---|---|
| gluons | $8$ | $A_{xy},iS_{xy},A_{xz},iS_{xz},A_{yz},iS_{yz},d_{2},d_{3}$ — the detail article's $g_{1},g_{2},g_{4},g_{5},g_{6},g_{7},T^{c}_{3},T^{c}_{8}$ | $\mathfrak{su}(3)$, the subalgebra that fixes the unit line | massless and unbroken at every scale | none |
| the $B-L$ boson, $B'$ | $1$ | $iD$, the corner | the Cartan direction of $\mathfrak{su}(4)$ that commutes with colour | one of the two ingredients of hypercharge | none of its own |
| leptoquarks | $6$ | $A_{ta}$ and $iS_{ta}$, $a=x,y,z$ — the detail article's $\bar X^{a},X^{a}$ | the off-diagonal block $\mathfrak m$, mixing $\mathbb C e_t$ with $B_V$ | massive, colour triplet, charge $\pm\tfrac23$ | $M_{C}$ |
| the six $\mathfrak{so}(4)$ arrays | not generators | $T^{L}_{a}$, $T^{R}_{a}$, $a=x,y,z$ | $\operatorname{span}\{A_{ab}\}$, rank $2$ of $3$ | **no particle**: half heavy, half massless | none |

The generator rows sum to $8+1+6=15$, and the array column lists each of the fifteen exactly once: **an entry in the table and a subsection of the detail article are the same object.** **The fourth row is not a fourth class of generator.** It is the six arrays the corpus prints in a redundant basis, and its entry in the last-but-one column is the reason it is not a row of the spectrum.

**The classes are disjoint as generators, and the fourth row is not one of them.** Each row is a class of generators and not of states — the three of $\mathrm{SU}(2)_R$ yield two massive states and one direction that is not a state at all but an ingredient. But $L_{\vec e_a}$ and $R_{\vec e_a}$ are traceless and skew-adjoint for $\operatorname{tr}(X^\dagger Y)$, hence elements of $\mathfrak{su}(4)$, and they are independent, so the six weak generators lie *inside* the fifteen. The carrier therefore supplies

$$
\dim_{\mathbb R}\mathfrak u(4)=16=15+1 ,
$$

and the twenty-one exists only on the formal copy the group acts on — which is why the copy is declared rather than found. Said as arithmetic: $15+6=21$ double counts, and $15+6-6=15$ is the algebra. [The Counts of the Fifteen](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html) takes that distinction as its subject and counts the same objects five ways.

**And the overlap is not marginal.** Projecting a weak generator onto the block $8+1$ and onto the coset $\mathfrak m$, in the same norm, gives $\sqrt2$ and $\sqrt2$ against a total of $2$: **each weak generator is an equal superposition of a colour direction and a leptoquark direction.** So neither block equals a weak generator, and a reader who takes the six of $\mathfrak m$ for the six of the two $\mathrm{SU}(2)$'s has conflated two different sixes that are not even orthogonal.

**The common summary, and its two errors.** It is often said that the fifteen of $\mathrm{SU}(4)$ are the strong interaction and the six of the two $\mathrm{SU}(2)$'s are the weak one. Both halves are wrong, and the errors are of different kinds.

**The first error is a count.** Of the fifteen, eight are the gluons, one is the $B-L$ boson $B'$, the array $iD$, and six are leptoquarks. Seven of the fifteen are therefore not the strong interaction, and the sentence "the fifteen are the strong interaction" overstates by seven generators. The correct sentence is exact: *eight of the fifteen are the gluons; one is the $B-L$ boson, the corner array $iD$; six are leptoquarks.*

**The second error is that the six are not one object.** The six are three plus three, and the two triples are not the same object. The three of $\mathrm{SU}(2)_L$ are the weak isospin the Standard Model keeps: two of them become $W^{\pm}$ and one mixes into the photon and the $Z$. The three of $\mathrm{SU}(2)_R$ belong to a factor the Standard Model does not keep: two become $W_R^{\pm}$, and the third is not a Standard Model generator at all — it is the raw material of hypercharge, and it is paired with a direction from $\mathrm{SU}(4)$ rather than used on its own. The correct sentence is exact: *three of the six are the weak isospin; three are the right-handed weak group, of which one direction becomes part of hypercharge and two become the $W_R$.*

**What "comes from" means, and the two senses it has.** A generator can descend from a subgroup, or it can be a mixture of directions from different factors. The eight gluons descend: $\mathrm{SU}(3)$ is a subgroup of $\mathrm{SU}(4)$, unbroken at every scale. Hypercharge does not descend: it is a mixture, and the section on the abelian factor is about it. Keeping the two senses apart is what makes the ledger readable, because the first is a containment statement and the second is a statement about a linear combination.

**The dimension budget is the arithmetic check, and it lives with the chain.** The chain is $21\to15\to12\to9$ in dimensions and $5\to5\to4\to3$ in rank, and the number of massless gauge bosons equals the dimension of the unbroken group at every stage — a theorem, because the Higgs mechanism eats one Goldstone per broken generator. **What the budget does not say is which generator goes where.** That is the ledger, and the ledger is the content. [The Breaking Chain](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html) writes the budget and the spectrum; this article writes only the address of each generator and reads that address three times.

## Reading One: the Fifteen Sorted by What They Do to the Time Line

**The split the matrix already has.** The canonical split of the carrier is $\mathbb C e_t\oplus B_V$, and $e_t$ is the time unit of the algebra — the Krein norm is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$, signature $(1,3)$. So the split that identification (A) names lepton against colour is, in the algebra's own form, the **signature split**: the line is the time-like direction and $B_V$ is the space-like part. Sorting the fifteen by what they do to that line therefore sorts them by a property the corpus did not have to introduce.

| what it does to $\mathbb C e_t$ | count | which | class |
|---|---|---|---|
| annihilates it, $X e_t=0$ | $8$ | $\mathfrak{su}(3)$ | gluons |
| acts on it as a phase | $1$ | $iD$ | the $B-L$ boson, $B'$ |
| moves it out of itself | $6$ | $\mathfrak m$ | leptoquarks |

$8+1+6=15$. The $8+1=9$ is the stabiliser of the line, and it is a subgroup; the $6$ is not. **Seven see the line and one of them does not move it.** The nine, in this reading, are exactly the generators that survive the first breaking, and the six are exactly the ones that do not: [The Unbroken Subgroup](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html) proves the general statement, that the kernel of the mass matrix is the stabiliser, and this table is that kernel computed on the corner.

> **What this does and does not mean.** Leptoquarks and Lorentz boosts are both "directions that mix the time line with a space line", and that is a statement about the *shape* of the generators in the same matrix algebra. It is not a statement that the leptoquarks are boosts. A boost is a spacetime transformation and the six are internal gauge directions; the coincidence is that $\mathrm{SU}(4)$ acts on four coordinates which the algebra also reads as time and space, and the physics identification of those four coordinates with colour is (A), not a theorem. The count is a bookkeeping fact about one carrier used twice.

## Reading Two: the Sextet as Two Triples, Graded by $D$

**The sextet splits three and three, and the split is the corner's own.** With $iD=i\operatorname{diag}(-3,1,1,1)$ and $E_{jk}$ the matrix unit in the order $(t,x,y,z)$,

$$
[iD,E_{ti}]=-4i\,E_{ti},\qquad [iD,E_{it}]=+4i\,E_{it},
$$

so three of the six raise the line into a colour direction and carry $D=+4$, and three lower it back and carry $D=-4$. **This is not the $3+3$ of the $\mathfrak{so}(4)$ arrays.** Both sixes split three and three — the sextet by the corner's grading, the real planes by self-duality — and the two splits are of different sixes: the ledger's third row here, its fourth row there. **The coincidence of the number is a coincidence of dimension and nothing more.** Divided by three that is $B-L=\pm\tfrac43$ — the leptoquark charge of $\pm\tfrac23$ once the $\mathrm{SU}(2)_R$ half is added, which is the $\pm\tfrac23$ of the ledger.

**So the $3+3$ is not a relabelling of the sextet: it is the particle–antiparticle pairing, written in the corner's grading.** The detail article names the two halves $\bar X^{a}$ and $X^{a}$, assigns the real array $A_{ta}$ to the first and the imaginary array $iS_{ta}$ to the second, and states that the choice of which is the particle is a convention of the $i$ — [The Leptoquarks of the Four Colours Left–Right Model](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html) owns the sector. **What is not a convention is the grading**: the two halves carry opposite $D$, so the corner distinguishes them whether or not anyone names them.

**And the six composites leave a fingerprint on the sextet.** Projecting $L_{\vec e_a}$ onto $\mathfrak m$ gives a norm of $\sqrt2$ out of $2$, and the projection of $R_{\vec e_a}$ onto $\mathfrak m$ is *the same vector*. Two consequences follow. First, $L_{\vec e_a}-R_{\vec e_a}$ has no leptoquark part at all — it is pure colour. Second, **the two composites share their leptoquark half, which is exactly why they cannot be independent generators of the model**: the sextet is one six, and a redundant basis reads it twice. The six composites reach only a three-dimensional subspace of the six-dimensional $\mathfrak m$, so three leptoquark directions are not the leptoquark half of any weak generator. **That is why the ledger's last two rows cannot be read off the sextet.**

## Reading Three: the Same Nine as a Maximal Compact

**The same $8+1+6$ is a Cartan decomposition of one algebra in two real forms.** $\mathfrak{su}(4)$ and $\mathfrak{su}(1,3)$ — the second preserving $G=\operatorname{diag}(1,-1,-1,-1)$ — are both real forms of $\mathfrak{sl}(4,\mathbb C)$, and the split is the same on both sides:

| | preserves $\operatorname{tr}(X^\dagger Y)$ | preserves $G$ |
|---|---|---|
| $8$ gluons | yes | yes |
| $1$ $B-L$ boson, $iD$ | yes | yes |
| $6$ leptoquarks | **yes** | **no, but $i$ times them does** |

The nine are the $+1$ eigenspace of the same involution $X\mapsto GXG$ in both algebras, and that eigenspace is a subalgebra of dimension $9$: in $\mathfrak{su}(1,3)$ it is the **maximal compact**, and in $\mathfrak{su}(4)$ it is a $\mathfrak u(3)$, the fixed algebra of an inner automorphism. **The two real forms have the same dimension, $15$, the same rank, $3$, and the same nine, and they differ on exactly one thing: whether the six are compact.** In $\mathfrak{su}(4)$ the six lie in the compact form; in $\mathfrak{su}(1,3)$ they lie in the $-1$ eigenspace, which is the non-compact part, and $i\,\mathfrak m$ is what returns them to $\mathfrak{su}(1,3)$.

**That is the cleanest statement of the leptoquark count the corpus has, and it needs no new axiom.** The leptoquarks are the six directions that are compact in $\mathfrak{su}(4)$ and non-compact in the pseudo-unitary form. Any structure that fixes a signature on the carrier — a Krein form, a pseudo-Riemannian structure in the sense of the non-commutative-geometry literature — selects the second real form, and selecting it *is* the statement that the six are not gauged. In the language of that literature this is the object called $\beta$, and the result quoted there is that the full Pati–Salam algebra admits no such $\beta$ unless it is reduced, which removes both the six and the off-diagonal Yukawa block. **The corpus is not in a position to adopt that result**, because its finite triple fails the first-order condition and it has no unitaries to quotient; what it can state, and what this paragraph states, is the algebraic core that does not depend on any of that.

**One consequence worth naming, because it cuts both ways.** The six weak arrays are in $\mathfrak{su}(4)$ and not in $\mathfrak{su}(1,3)$: $T^{L}_{x}=-\tfrac12(A_{tx}+A_{yz})$ is built from one mixed plane and one colour plane, the involution turns it into $-T^{R}_{x}$, and no real multiple of it is fixed: the involution reverses the sign of $A_{tx}$ and keeps $A_{yz}$, so a fixed multiple would have to be zero. So a signature-fixing condition on the carrier would not spare the weak pair — which is why, in the literature where this is done, the weak generators are placed on the *other* index of a rectangular array rather than on the same four coordinates. On one $M_4(\mathbb C)$ the colour and weak actions overlap; that overlap is the price of the corpus's carrier, and the formal copy is what pays it.

## Does the $\mathrm{U}(1)$ Come From $\mathrm{SU}(4)$?

**The question is asked because the answer is "partly", and both halves of that matter.** It is the one question the ledger leaves open: the $B-L$ row says "one of the two ingredients of hypercharge", and that sentence is a claim about a linear combination, not a containment.

**What $\mathrm{SU}(4)$ supplies.** Breaking $\mathrm{SU}(4)$ to $\mathrm{SU}(3)\times\mathrm{U}(1)$ leaves one abelian factor, generated by the diagonal direction that commutes with $\mathfrak{su}(3)$ and is traceless. That direction is one-dimensional: the centraliser of $\mathfrak{su}(3)$ in $\mathfrak{su}(4)$ is spanned by $iD$ alone. So the $\mathrm{U}(1)_{B-L}$ of the intermediate stage does come out of $\mathrm{SU}(4)$, and it comes out uniquely, once the split is declared. **This is the ledger's second row, read as a theorem.**

**What $\mathrm{SU}(4)$ does not supply.** The Standard Model's hypercharge is not that factor. It is the combination

$$
Y=T_{3R}+\tfrac16D=T_{3R}+\tfrac12(B-L),
$$

one direction from $\mathrm{SU}(2)_R$ and one from $\mathrm{SU}(4)$, with a fixed relative weight: $\tfrac16$ on the corpus's array, which is $\tfrac12$ on the charge, since $\tfrac16D=\tfrac12(B-L)$. **The weight is not a new number and it is not a second parameter**; it is the one number $\tfrac12$ written on two normalisations of one direction. So $\mathrm{U}(1)_Y$ is contained in $\mathrm{SU}(4)\times\mathrm{SU}(2)_R$ and in neither factor alone.

**The precise form of "contained".** $\mathrm{U}(1)_Y$ is a diagonal subgroup of the product $\mathrm{U}(1)_{B-L}\times\mathrm{U}(1)_{3R}$: the one-parameter subgroup along which both phases turn together, with the parameter of the first at half the rate of the second. A diagonal subgroup is not a subgroup of either factor, which is why "hypercharge comes from $\mathrm{SU}(4)$" and "hypercharge does not come from $\mathrm{SU}(4)$" are both false as stated.

**The counting, which is the sharp form of the same statement.** Write the four generators the Standard Model keeps and ask where each one comes from.

| Standard Model generator | count | drawn from |
|---|---|---|
| $W^1_L,W^2_L,W^3_L$ | $3$ | $\mathrm{SU}(2)_L$, as a factor |
| $Y$ | $1$ | one direction of $\mathrm{SU}(2)_R$ and one of $\mathrm{SU}(4)$, mixed |

So four surviving generators draw on five frame directions: three from $\mathrm{SU}(2)_L$, one from $\mathrm{SU}(2)_R$, one from $\mathrm{SU}(4)$. The surplus direction is not an error in the count. The two neutral raw directions span a plane; $Y$ is one direction in it; the orthogonal direction in the same plane is a physical state, the $Z_R$, which becomes massive at $M_R$. The step $5\to4$ is therefore the step in which one gauge boson acquires a mass, and it happens entirely inside that plane.

**The next step is the same construction once more.** At the electroweak scale the two directions $W^3_L$ and $Y$ span a second plane; the photon is one direction in it and the $Z$ is the other. So the neutral sector is three fields in and three states out, of rank two, with one null direction. That count is a property of a sum of two rank-one matrices and holds for any couplings; [The Neutral Sector](the-neutral-sector-of-the-four-colours-left-right-model-three-ingredients-rank-two-one-null-direction.html) derives the null vector and the two masses, and [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html) states the same rank-two fact in the grid's language.

**Why the distinction has to be kept.** "The $\mathrm{U}(1)$ of $\mathrm{SU}(4)$" and "the $\mathrm{U}(1)$ of the Standard Model" name two different generators. The first is $B-L$, whose boson is the corner field $B'$. The second is $Y$, whose boson is a mixture. A reader who conflates them will expect the photon to be the $\mathrm{SU}(4)$ boson, and it is not: the photon is a mixture of all three neutral fields, and its coefficient on the $B-L$ direction is nonzero.

## $B-L$ as a Bridge, and Where the Metaphor Stops

**The sentence the metaphor is meant to carry.** $B-L$ is a generator that sits inside $\mathrm{SU}(4)$ beside the colour structure, and after the breaking it becomes one of the two ingredients of hypercharge, which then mixes with the weak isospin to produce the photon and the $Z$. In that sense it carries information from the colour side to the electroweak side.

**Why the metaphor is apt.** Three facts support it, and each is a row of the ledger read in order.

- Before the breaking, $B-L$ is one of the fifteen that sit with the eight gluons in one group; it is the direction that distinguishes the lepton line from the three colour lines.
- After the breaking, it is not discarded. It is paired with $T_{3R}$ to form hypercharge, and the pairing is exact, with a fixed relative weight.
- After the second breaking it is still present, as a component of the photon and of the $Z$. The $B-L$ direction enters all three neutral fields and leaves none of them.

**What the metaphor must not be taken to mean.** It is a bridge between *symmetries*, not between *forces*, and no boson sits halfway between a gluon and a $W$.

- There is no particle that mediates a "colour–electroweak" interaction. The $B-L$ boson is a real field with its own mixing, and after the breaking it is not a separate force: its direction is one ingredient of the photon, and the orthogonal combination of its plane is the $Z_R$.
- The bridge is a statement about a generator's address in a product of groups, not a statement about a fifth force. At every energy below $M_R$ the number of gauge groups is three, and none of them is called $B-L$.
- The bridge does not imply that the two sides have equal status. Colour is unbroken at every scale; the $B-L$ direction is broken as an independent factor at $M_R$.

**The precision that makes the metaphor more than a picture.** $B-L$ is sensitive to both sides, and it is the one generator that is. Quarks carry $B-L=+\tfrac13$ and leptons carry $-1$, so $B-L$ measures quark content minus lepton content. That is exactly what a bridge has to do: carry a quantity defined on both banks. And the quantity it carries is a third on one bank and a unit on the other, which is the trace again — $+\tfrac13$ three times and $-1$ once is zero, so the bridge's two ends are calibrated against each other by the same sum that quantises the charge: [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html).

**The one-sentence form, if a single sentence is wanted.** *$B-L$ is the direction the $\mathrm{SU}(4)$ breaking leaves behind, and hypercharge is that direction combined with the neutral direction of $\mathrm{SU}(2)_R$; the combination is a symmetry statement, and it is not a force of its own.*

## The Checks

Twelve recomputations, at $\operatorname{tr}$ in the fundamental, the quartet ordered $(t,x,y,z)$.

| claim | check | result |
|---|---|---|
| every generator in the ledger once | the three rows against the fifteen subsections | $15/15$, no repeat |
| the generator ledger | $8+1+6$ | $15$ |
| the composite row | the six arrays against the fifteen | $0$ new directions |
| the ledger on the carrier | $\dim\mathfrak u(4)$ against $16$ | $16$, so the fifteen is one short of the copy |
| the overlap of the two sixes | block part against coset part of $L_{\vec e_a}$ | $\sqrt2$ and $\sqrt2$ of $2$, not orthogonal |
| the shared leptoquark half | $L_{\vec e_a}$ against $R_{\vec e_a}$ on $\mathfrak m$ | the same vector; $L-R$ is pure colour |
| the time-line sort | $8+1+6$ by action on $\mathbb C e_t$ | $15$, and $8+1$ is the stabiliser |
| the $3+3$ of the sextet | $[iD,E_{it}]$ against $[iD,E_{ti}]$ | $+4i$ against $-4i$, so $B-L=\pm\tfrac43$ |
| the two real forms | $\mathfrak{su}(4)$ against $\mathfrak{su}(1,3)$ | $15=9+6$ both, the six compact in one only |
| the first misreading | $7$ of the $15$ against $8$ gluons | $7$ is not strong |
| the second misreading | $3+3$ from two commuting $\mathfrak{su}(2)$'s | a subspace of the fifteen, not a factor |
| the centraliser | $\mathfrak z_{\mathfrak{su}(3)}(\mathfrak{su}(4))$ | one-dimensional, spanned by $iD$ |
| the composite's fate | $m^{2}$ of $T^{L}_{a}$ | $8v^{2}$, not a generator |

## Summary

**The ledger.** $15=8+1+6$. Eight of the fifteen are gluons, one is the $B-L$ boson $B'$, the corner array $iD$, six are leptoquarks. **The six $\mathfrak{so}(4)$ arrays are a redundant basis of the six real planes and not a class of generator**, and their row in the ledger says so. **The classes are disjoint as generators**: there is no second factor for them to sit in, and the carrier's spectrum is the fifteenupplies $16=15+1$ and the twenty-one lives on the formal copy.

**The first reading.** Sorted by what it does to the time line $\mathbb C e_t$, the fifteen is $8$ (annihilate it) $+1$ (act on it as a phase) $+6$ (move it out). The nine are the stabiliser of the line; the seven that see the line are the six and the corner.

**The second reading.** The sextet is two triples graded by $D$: $+4$ on the three that carry the line into colour and $-4$ on the three that carry it back, which is the particle–antiparticle pairing and not a relabelling.

**The third reading.** The same nine are the maximal compact subalgebra of $\mathfrak{su}(1,3)$ as well as of $\mathfrak{su}(4)$; the six are compact in $\mathfrak{su}(4)$ and non-compact in the pseudo-unitary real form. The leptoquark count is a compactness count, and $\mathfrak{su}(4)$ and $\mathfrak{su}(1,3)$ differ on nothing else.

**The abelian factor.** The breaking supplies $\mathrm{U}(1)_{B-L}$ and not $\mathrm{U}(1)_Y$. **Hypercharge is a diagonal subgroup of $\mathrm{U}(1)_{B-L}\times\mathrm{U}(1)_{3R}$, and that product is not a product of this model's factors**: it is a product of the model's one abelian direction with a direction the transition creates. Four electroweak generators draw on five raw directions, and the fifth is the $Z_R$ — **all of it downstream of this ledger.**

**The bridge.** $B-L$ is the direction the $\mathrm{SU}(4)$ breaking leaves behind, and hypercharge is that direction combined with a neutral direction the transition supplies. It is a bridge between symmetries, not between forces, and it is calibrated at both ends by the same sum: $+\tfrac13$ three times and $-1$ once.

## Summary of Notation

| symbol | meaning |
|---|---|
| $E_{jk}$ | the matrix unit in the order $(t,x,y,z)$, the time index first |
| $A_{jk}$, $iS_{jk}$ | $E_{jk}-E_{kj}$ and $i(E_{jk}+E_{kj})$, the real and imaginary arrays of the plane $\{j,k\}$ |
| $iD$ | $i(W_{xx}+W_{yy}+W_{zz})=i\operatorname{diag}(-3,1,1,1)$, the corner; norm $12$, spectrum $-3i,i,i,i$ |
| $d_{2}$, $d_{3}$ | the two colour diagonals, $\tfrac i2(W_{yy}-W_{xx})$ and $\tfrac i2(W_{zz}-W_{yy})$ |
| $B'$ | the boson of $iD$: the $B-L$ boson, and one of the three neutral ingredients |
| $g_{1}\dots g_{7}$, $T^{c}_{3}$, $T^{c}_{8}$ | the eight gluons as the detail article names them |
| $\bar X^{a}$, $X^{a}$ | the two leptoquark amplitudes of colour $a$, carried by $A_{ta}$ and $iS_{ta}$ |
| $T^{L}_{a}$, $T^{R}_{a}$ | $\tfrac12L_{\mathrm{axf}}(\vec e_a)$ and $\tfrac12R_{\mathrm{axf}}(\vec e_a)$, the six weak arrays |
| $\mathfrak m$ | the six off-diagonal generators of $\mathfrak{su}(4)$; equivalently the six that move $\mathbb C e_t$ out of itself |
| $\mathfrak z_{\mathfrak{su}(3)}(\mathfrak{su}(4))$ | the centraliser of the colour subalgebra, one-dimensional |
| $T^{15}$ | the corner normalised by $\operatorname{tr}(T^{15})^2=\tfrac12$, so $B-L=\sqrt{8/3}\,T^{15}$ |
| $M_{C}$, $M_{R}$, $M_{W}$ | the three scales: the colour one, the right one, the electroweak one |

## Further Reading

- [The Fifteen AXF Matrices of the Bosons in Detail: Every Matrix, Every Boson, Its Entries, Its Spectrum and Its Fate](the-15-axf-matrices-of-the-bosons-in-detail.html). The twenty-one one at a time; every row of the ledger here is a subsection there.
- [Classification of the Bosons in the $\mathrm{SU}(4)$ Model: Sixteen Cells, Fifteen Generators, Nine Massless and Six Heavy](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The three grids, the name in every cell, and the twenty-one states.
- [The Counts of the Fifteen](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html). Cell, plane, array, generator, direction, and the map between the counts.
- [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html). Where the three diagonal arrays are built from one sum and two differences.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-120-independent-80-nonzero-and-five-rules.html). Every bracket, which is how the classes here are proved closed.
- [The Breaking Chain of the Four Colours Left–Right Model: One Flag, Three Stabilisers, Three Scales](the-breaking-chain-of-the-four-colours-left-right-model-one-flag-three-stabilisers-three-scales.html). The budget $21\to15\to12\to9$, the rank budget, and the spectra.
- [The Unbroken Subgroup](the-unbroken-subgroup-of-the-four-colours-left-right-model-nine-massless-generators-twelve-that-acquire-mass.html). Why the kernel of the mass matrix is the stabiliser, which is the first reading in general form.
- [The Neutral Sector](the-neutral-sector-of-the-four-colours-left-right-model-three-ingredients-rank-two-one-null-direction.html). Three ingredients, rank two, one null direction.
- [The Leptoquarks of the Four Colours Left–Right Model](the-leptoquarks-of-the-four-colours-left-right-model-six-states-one-bound-and-why-proton-decay-does-not-bite.html). The sector the second reading is about.
- [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). The trace of the corner array, read as the quark–lepton relation: the sum the bridge is calibrated by.
- [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). The anomaly system solved in full, and the three discrete rays the diagonal-subgroup statement is the continuous form of.

**The traps.** Do not say "the fifteen are the strong interaction": seven of the fifteen are not gluons. Do not say "the six are the weak interaction": they are two triples from two factors, and only one of the six triples is the weak isospin the Standard Model keeps. Do not say "hypercharge comes from $\mathrm{SU}(4)$": the breaking supplies $B-L$, and hypercharge is a mixture of that with one direction of $\mathrm{SU}(2)_R$. Do not read the ledger and the carrier as the same list: $15+6=21$ double counts, and the twenty-one exists on the copy. Do not say the leptoquarks are boosts because they mix the time line with a space line: the shape is shared and the transformation is not.
