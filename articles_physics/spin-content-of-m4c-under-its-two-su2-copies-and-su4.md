# __Spin Content of $M_4(\mathbb{C})$ Under Its Two $\mathrm{SU}(2)$ Copies and $\mathrm{SU}(4)$: Label $2$ Names a Composite, Label $\tfrac32$ Names a Module__

## Introduction

**The question.** The mathematical corpus reads the algebra of order four and reports spins $0,1,2,3$ on it and a module of spin $\tfrac32$. The algebra $\mathfrak{su}(4)$ is a subalgebra of that same matrix algebra, and $\mathrm{SU}(4)$ is the gauge group of this block. **Do those numbers name a spin that a field of this corpus can carry?**

**The answer.** No, and it rests on two sentences. **A spin is read from a pair, a group and a space, and the space whose carriers are meant is $\mathbb{B}$, not $M_4(\mathbb{C})$.** And the group must be one of **the two actions the unit quaternions already exert on the algebra itself** — left multiplication and conjugation; any further copy is a construction on a chosen carrier space, not an action the algebra supplies. On those two actions the carriers of $\mathbb{B}$ are the line, the plane and the vector part, of spins $0$, $\tfrac12$ and $1$. **No force extends that roster; a group may act on a product of two carriers, and that is a statement about composites, not about the roster.**

**Why the question is answered and not dismissed.** The mathematical corpus's $M_4(\mathbb{C})$ and this corpus's ambient operator algebra are one algebra, and this corpus says so itself: *Matrix Representations Conventions* writes the ambient as $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$. So the shared name is a shared object. Transferring its spin labels to physics is a claim that needs a test, not a slip that needs a correction.

**What the article separates, in order.** The three objects and the word *spin*, with the carrier and its closure kept apart because their dimensions are counted differently; the two $\mathrm{SU}(2)$ copies and the group, which give three different lists; the one module that carries two different spins; the branching of the quartet and the fifteen; why no carrier of spin $\tfrac32$ exists; the two numbers above one; and the numeral four, which occurs in four unrelated places in this block.

**Boundaries.** The decomposition is the mathematical corpus's, in *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$*, and it is quoted and recomputed here, not re-proved. The Rarita–Schwinger field is named and its carrier count checked; its quantisation is *Canonical Quantization of the Rarita–Schwinger Field from the Vector Carrier and the Dirac Field*. Nothing below uses the restructuring at $M_C$, so the article is a statement about the unbroken phase. **One convention is load-bearing and is fixed in the next section: a carrier's dimension is real and a closure's is complex, and $2s+1$ is the same number in either column** (*The Carrier Roster* states the identity on the carrier column, and only there).

## Three Objects, and the Word Spin

**The algebra of fields.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ is the algebra of fields: four complex dimensions, eight real. Its carriers are the state spaces of the three spins, of **real** dimensions $1$, $2$ and $3$: the line $\mathbb{R}e_t$, spin $0$, trivial action; the plane $\Sigma(\vec u)=\mathbb{C}\tilde\Pi_{\mathrm{id},+}(\vec u)$, spin $\tfrac12$, left multiplication about its own axis; and the vector part $\mathfrak{k}$, spin $1$, conjugation. **The identity $2s+1=\dim_{\mathbb{R}}$ holds on the carrier column, and only there.**

**A carrier is not its closure, and the two are counted differently.** The smallest invariant subspace containing a carrier is a *closure*, of **complex** dimension $2s+1$ and real dimension $2(2s+1)$: the centre $\mathbb{C}e_t$ closes the line, the spinor space $S_\pm=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ closes the plane, and the anti-Hermitian space $\mathbb{B}_\Phi$ closes the vector part. **So $2s+1$ is one number read twice — the real dimension of the carrier and the complex dimension of its closure — and every count below says which column it is counting.** *The Carrier Roster* states the distinction and its one-sentence reason: "a statement about a carrier and a statement about its closure are different statements".

**The ambient operator algebra.** $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ has sixteen complex dimensions and holds the operators on $\mathbb{B}$: the regular representation, the sixteen two-sided products, the Clifford reading. It carries no biquaternion name and no carrier. **It is never the algebra of a field.** Its own spin content is the subject of this article, and it is a statement about operators.

**The gauge group.** $\mathrm{SU}(4)$ is the group of unitary four-by-four matrices of determinant one, of real dimension $15$, and it is the gauge group of this block: the adjoint is the fifteen directions of the one connection. **A gauge transformation acts on the ambient algebra by conjugation, and that action is the one the whole block uses.**

**The rule that the rest of the article applies.** A spin is not a property of a space. **It is a property of a pair, a group and a space, and the number is the highest weight of the representation.** The same space carries different spins under different groups, and a number quoted without its group is a number half read. The mathematical corpus states the rule for its own object in *Two Numbers and Two Readings*, and this article's work is to apply it here.

**One caution about the word label.** In this corpus a *label* is the upright name in a subscript. The mathematical corpus uses the same word for the highest weight of a module. **This article keeps the second sense only where it quotes the mathematics**, and writes *spin* for the physical quantity.

## The Subalgebras of $\mathfrak{su}(4)$ and the Group Itself

**Two three-dimensional subalgebras, and the whole group, act on the same sixteen complex dimensions, and each gives its own list of spins.** That is the whole of the difficulty. The list is not a property of the algebra; it is a property of the group that cuts it.

### The Principal Copy

**The definition.** The principal copy is the image of $\operatorname{Sym}^{3}$ of the defining two-dimensional module, so its matrices are the spin-$\tfrac32$ matrices on $\mathbb{C}^4$. In its weight basis the diagonal generator is $\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$, and the module is $\mathbb{C}^4=V_{3/2}$, of complex dimension $4=2\cdot\tfrac32+1$.

**What it gives on the operator algebra.** Acting by conjugation, $X\mapsto gXg^{-1}$, it cuts the sixteen dimensions into four pieces. The Casimir $\sum_i\mathrm{ad}_{J_i}^{2}$ has the spectrum $0$, $2$, $6$, $12$ with multiplicities $1$, $3$, $5$, $7$, that is $j(j+1)$ at $j=0,1,2,3$ in dimensions $2j+1$. **The decomposition is $7+5+3+1=16$, and the four summands are $V_3,V_2,V_1,V_0$.**

**It is a subalgebra of the gauge algebra.** The three generators $iJ_x,iJ_y,iJ_z$ are anti-Hermitian and traceless, so the principal copy lies inside $\mathfrak{su}(4)$. **This is why the question is sharp: the copy that produces the label $\tfrac32$ is not outside the gauge group, it is a three-dimensional subalgebra of it.**

### The Rotor Copy

**The definition.** Left multiplication by the unit elements of $\mathbb{B}$ generates a second copy. The algebra splits into its two minimal left ideals, $\mathbb{B}=S_+\oplus S_-$, each of two complex dimensions, and left multiplication preserves each. In a basis adapted to the two ideals the copy acts as $\operatorname{diag}(u,u)$ with $u\in\mathrm{SU}(2)$.

**The splitting is a frame and the module is not.** The minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$ form a projective line's worth, $\mathbb{CP}^1$, and the axis $\vec u$ selects one orthogonal pair $S_\pm=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u)$ out of it. **So the pair $S_+\oplus S_-=\mathbb{B}$ depends on the axis, while the module type $V_{1/2}\oplus V_{1/2}$ under left multiplication does not.** Everything below that speaks of *the* two ideals means that selected pair.

**What it gives on the module.** Each ideal is the defining two-dimensional module, so the four dimensions carry $V_{1/2}\oplus V_{1/2}$. **The Casimir has the eigenvalue $\tfrac34=j(j+1)$ at $j=\tfrac12$ on all four states, which is two copies of the spin-$\tfrac12$ module.** The two ideals are the closures of the plane, and the module of this copy is the union of two such closures.

**What it gives on the operator algebra.** Under conjugation it cuts the sixteen dimensions into $4V_1\oplus4V_0$: the Casimir has the eigenvalue $2$ on twelve states and $0$ on four. **Four triplets and four singlets, and no half-integer piece anywhere.**

**It is a subalgebra of the gauge algebra too.** The three generators $i\operatorname{diag}(\sigma_1,\sigma_1)/2$ and its two companions are anti-Hermitian and traceless, so this copy also lies inside $\mathfrak{su}(4)$.

### The Group Itself

**The definition.** $\mathrm{SU}(4)$ acting on the ambient algebra by conjugation is not a three-dimensional copy but the whole fifteen-dimensional group. The trace separates a singlet, and the traceless part is irreducible, so the decomposition is $\mathbb{C}\mathrm{I}\oplus\mathfrak{sl}_4$, of dimensions $1+15$.

**What it gives.** No spin at all. **A decomposition into a singlet and an irreducible fifteen carries no label of the kind this article is testing**, because the fifteen is irreducible for the group that defines it. The irreps of this reading are $\mathbf4$, $\overline{\mathbf4}$, $\mathbf{15}$, $\mathbf6$ and $\mathbf{10}$, and none of them is a spin.

### The Lists Side by Side

| copy | dimension | module | operator algebra |
| --- | --- | --- | --- |
| principal $\operatorname{Sym}^{3}$ | $3$ | $V_{3/2}$, dim $4$ | $V_3\oplus V_2\oplus V_1\oplus V_0$, $7+5+3+1$ |
| rotor, left multiplication | $3$ | $V_{1/2}\oplus V_{1/2}$, dim $2+2$ | $4V_1\oplus4V_0$, $4\cdot3+4\cdot1$ |
| $\mathrm{SU}(4)$ | $15$ | $\mathbf4$ | $\mathbf1\oplus\mathbf{15}$, $1+15$ |

**The three rows are one algebra and three groups.** The list $7+5+3+1$ is the principal row's, and it is not the algebra's list. **The mathematical corpus makes the same point with four lists in *The Four Carrier Lists of One Algebra at $n=4$*; the rotor row above is a fifth, and it is the reading this corpus's own carriers come from.**

## One Module, Two Spin Contents

**The same four complex dimensions carry spin $\tfrac32$ in one row and spin $\tfrac12$ twice in another, and that is not a contradiction.** It is the rule of the previous section applied twice. The module is $\mathbb{C}^4$ in both cases, the group is different, and the highest weight follows the group.

**The check that separates the two rows.** The principal diagonal generator has the spectrum $\{\tfrac32,\tfrac12,-\tfrac12,-\tfrac32\}$, four distinct weights. Left multiplication by the Hermitian generator $\sigma_z/2$ has the spectrum $\{\tfrac12,\tfrac12,-\tfrac12,-\tfrac12\}$, two weights twice. **The two generators are traceless and Hermitian, and their spectra differ, so no unitary change of basis carries one to the other: the two copies are genuinely different subgroups and not one subgroup in two bases.**

**Which row the physics uses.** The second. The corpus's carriers are read from left multiplication by the rotors and from conjugation by them, and those are the rotor row's actions. **No article of this block gauges the principal copy or writes a field on it, and none carries $\tfrac32$ as a spin.** The number does occur in the block, twice, and neither occurrence is a spin: $-\tfrac32$ is the scheme constant of the one-loop potential and $\tfrac32\lambda_1\rho^{2}$ is a mass. **The one place it meets a representation is the branch record of §*The Branching of the Quartet and the Adjoint*.**

**Why this is worth a section of its own.** A reader meets the sentence that the module of $M_4(\mathbb{C})$ has spin $\tfrac32$ in the mathematical corpus, and then meets the quartet of $\mathbb{C}^4$ in this block, and holds two statements about one space with no rule for reconciling them. **The rule is that the sentence needs its group, and with the group named the two sentences are both true and about different things.**

## The Branching of the Quartet and the Adjoint

**The one true sense in which $\tfrac32$ touches this block.** Take the principal copy, a subalgebra of $\mathfrak{su}(4)$, and restrict the irreps of $\mathrm{SU}(4)$ to it. The branchings are

| $\mathrm{SU}(4)$ irrep | dimension | restriction to the principal copy |
| --- | --- | --- |
| $\mathbf4$ | $4$ | $V_{3/2}$ |
| $\mathbf{15}$ | $15$ | $V_3\oplus V_2\oplus V_1$, that is $7+5+3$ |
| $\mathbf1$ | $1$ | $V_0$ |

**The first row is the quartet, and it is the answer to the question.** The four lines $(t,x,y,z)$, which this block carries as one multiplet, are the spin-$\tfrac32$ module of the principal copy. **Nothing is postulated here: the quartet is irreducible for $\mathrm{SU}(4)$ and the principal copy is a subalgebra, so the restriction is the whole space and the label is $\tfrac32$ by the module's dimension, $2\cdot\tfrac32+1=4$.**

**The second row is why the adjoint contains no spin-zero direction.** The Casimir of the principal copy restricted to the traceless part has the spectrum $2,6,12$ with multiplicities $3,5,7$ and no zero, so no direction of the fifteen is a singlet under the copy. **This is consistent with the scalar of the block being a separate matrix field and not a component of the connection**, and the consistency is a check on the reading, not a derivation of the scalar.

**What the quartet is actually used as, and this is the whole of the physical content.** It is the index space of the scalar, $\Phi\in(\mathbf4,\mathbf1,\mathbf2)$, taken in this corpus as the whole matrix; and it is the index space of the fermion fundamental. **Its physical spin is zero in the first use and $\tfrac12$ in the second.** The label $\tfrac32$ is what the quartet carries for a subalgebra that no field of the block is written on.

**A branching is not a content, and the difference is the article's warning.** A statement of the form $15=7+5+3$ says that one irreducible multiplet is seen by a smaller group as three pieces. **It does not say the fifteen are three multiplets, and it does not say the block contains fields of spin $2$ and $3$.** The fifteen are fifteen connection components on the vector carrier, and their physical spin is one, fifteen times over. **The reader who takes the branch as a content reads three multiplets of three spins where the model has one multiplet of one spin.**

## Why No Carrier of Spin Three Halves

**The test, in the corpus's own dimensions.** A carrier of spin $\tfrac32$ would have $2s+1=4$ states, so its closure would be an invariant subspace of $\mathbb{B}$ of **complex** dimension $4$ that is irreducible under the actions that define carriers. **The test is a count of the irreducible pieces of $\mathbb{B}$, and it is arithmetic, not preference.**

### The Two Actions, and Their Irreducible Pieces

**Left multiplication** gives the invariant subspaces of $\mathbb{B}$ of complex dimension $0$, $2$ and $4$: a minimal left ideal (any one from the $\mathbb{CP}^1$ family, of which $S_\pm$ is the pair selected by the axis), and the whole algebra. **The dimension $4$ occurs once, is $\mathbb{B}$ itself, and is reducible as $S_+\oplus S_-$.**

**Conjugation** gives complex dimensions $0$, $1$, $3$ and $4$: the centre $\mathbb{C}e_t$, the traceless part $\ker\operatorname{tr}$, the two together, and the whole. **The dimension $4$ is again the whole algebra, reducible as $Z\oplus V$.**

**Consequence.** Under either of the two product actions, no invariant subspace of $\mathbb{B}$ of complex dimension $4$ is irreducible. **This is the corpus's own count: the three carriers would need $1+2+3=6$ dimensions inside one structure, but $\dim_{\mathbb{C}}\mathbb{B}=4$** (*The Determination of the Possible Spins in Biquaternionic Form*).

### The One Irreducible Four, and Why It Names No Carrier

**The principal copy does make $\mathbb{B}$ irreducible of complex dimension $4$.** Acting by left multiplication it carries $\mathbb{B}\cong V_{3/2}$ and no proper invariant subspace, so under *that* group there is an irreducible four-dimensional object, and the label $\tfrac32$ is real — it is the branch record computed above. **A careless statement of the no-go would therefore be false, and this section states it the careful way.**

**It is not a carrier, and the reason is where the two embeddings come from, not whether one exists.** In the determination article's words, the two structures are "the two actions the product supplies without a choice: left multiplication and conjugation", while "other actions require extra data, such as a form or a grading, and are not carried by the product alone". **That phrasing is looser than the fact it reports, and the fact is worth stating exactly, because it is the whole of the argument.**

**The rotor copy and conjugation are actions of the unit quaternions on the algebra itself, and they come from the $\mathbb{H}$ factor of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$.** Left multiplication is the $\mathbb{H}$-module action of $\mathbb{B}$ on itself; conjugation is the adjoint action of the unit group; both are read off the product and the real structure with nothing added.

**The principal copy is not an action of the unit quaternions on $\mathbb{B}$; it is a representation-theoretic construction on a chosen carrier space.** It is the image of $\operatorname{Sym}^{3}$ of a two-dimensional module, and to write it as matrices on $\mathbb{B}$ one must first identify $\mathbb{B}$ with $\operatorname{Sym}^{3}$ of that module — a choice of spinor structure that the product does not supply. **Different identifications give conjugate copies, so the subgroup is canonical only up to conjugacy, while the rotor and conjugation copies are pinned outright.**

**Both are embeddings of $\mathrm{SU}(2)$ into $\mathrm{SU}(4)$, and the rotor copy is one too** ($\operatorname{diag}(u,u)$ above). **So the distinction is not the existence of an embedding but its provenance**: one is the real structure of the algebra acting on itself, the other is a construction that presupposes a carrier space. A carrier is a subspace of $\mathbb{B}$ together with an action of the unit elements, so it is defined by an embedding of the first kind. The corpus neither gauges the principal copy nor writes a field on it. **So $\mathbb{B}$ carries the label $\tfrac32$ for a group this block does not use, and no carrier of that label for the groups that define carriers.**

**The boundary is the corpus's and not the algebra's.** Nothing forbids a different theory from gauging the principal copy and writing a spin-$\tfrac32$ field on $\mathbb{B}$; that theory would be a different one, and *The Rarita–Schwinger Equation* is the corpus's note on the field such a theory would need.

### Why the Half-Integer at Order Two Misleads

**At order two the module is itself a minimal left ideal, and this is the single fact behind the confusion.** There the algebra is $M_2(\mathbb{C})=\mathbb{B}$, of complex dimension $4$, and its minimal left ideal is the module $\mathbb{C}^2=V_{1/2}$, of complex dimension $2$. **The half-integer looks like a subspace label at that size because the module coincides with a subspace of the algebra — the closure $S_\pm$ — and its complex dimension $2$ is also the real dimension of the plane.**

**At order four the module is an object of the operator algebra, not of the carrier space.** There the module is $\mathbb{C}^4=V_{3/2}$, of complex dimension $4$, and it is a minimal left ideal of $M_4(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of the same dimension. **$M_4P$ is a left-module summand of $M_4$, since $M_4=M_4P\oplus M_4(\mathrm I-P)$, and it is not a two-sided algebra summand; but it is a subspace of the operator algebra and not of the carrier space $\mathbb{B}$.** The carrier space does not grow when the order of the operator algebra grows: it is $\mathbb{B}$ throughout, and its carriers are the three of the roster.

**The lesson is the one the roster states.** Importing the order-two picture is the error: at $n=2$ the module label $\tfrac12$ and the carrier dimensions $1,2,3$ sit in one algebra and look like one list, and they are a module label and carrier dimensions belonging to two different objects.

### The Field of That Shape Is Imported

**One object of the right shape exists in the corpus, and it is a product, not a carrier.** The Rarita–Schwinger field is the module tensored with a vector index, $S\otimes V$, of complex dimension $2\cdot3=6$, and the Clebsch–Gordan rule gives

$$
S\otimes V=\left(\tfrac32\right)\oplus\left(\tfrac12\right),\qquad 6=4+2 .
$$

**The check is the Casimir.** On the six states it takes the values $\tfrac{15}{4}$ on four and $\tfrac34$ on two, that is one $V_{3/2}$ and one $V_{1/2}$. **A constraint removes the spin-$\tfrac12$ piece**, and the remaining four states are the spin-$\tfrac32$ field. **Its equation is imported and its carrier is a product**, which is the same statement as before: the algebra supplies the factors and not the field. *Particle Spins in the Biquaternion Algebra* states the consequence, and the roster states it as a boundary of the object rather than a gap in the method.

**Three objections, and their answers.**

- *The module of $M_4(\mathbb{C})$ has complex dimension four, so there is a carrier of dimension four.* **Its complex dimension four is the closure dimension a $\tfrac32$ carrier would need, and the only invariant space of that dimension is $\mathbb{B}$ itself, which is reducible under both product actions.** The module $V_{3/2}$ is $\mathbb{B}$ under the principal copy, the action of the previous subsection but one.
- *$\mathrm{SU}(4)$ is a subalgebra of the ambient algebra, so its representations inherit the ambient spin labels.* **A branching is not an inheritance.** The label is relative to the group; the $\mathbf4$ is irreducible for $\mathrm{SU}(4)$ and carries $\tfrac32$ only for the principal copy.
- *The algebra has a spin-two carrier $V_2$ of complex dimension five, so the graviton is already there.* **The number matches and the object does not**; it is answered in the next section.

## The Two Numbers Above One

### Spin Two Is Two Different Objects

**The principal copy's $V_2$ has complex dimension $5$, and so does the graviton's carrier.** The graviton's is the symmetric trace-free square of the material vector, $(V\odot V)_{\mathrm{sym}}=0\oplus2$ with $6=1+5$; the principal one is the alternating square of the module with its singlet removed, $\Lambda^{2}V_{3/2}=V_2\oplus V_0$ with $6=5+1$. **Both counts split a six as $5+1$, and they split different sixes.**

**The difference is where each object lives.** $V_2$ is a summand of $M_4(\mathbb{C})$ under the principal copy, that is, a space of operators. The graviton's carrier is built from $\mathfrak{k}$ inside $\mathbb{B}$ by a tensor product and a trace removal. **One is a subspace of the operator algebra and the other is a product of the field algebra, and no map between them is asserted anywhere in the corpus.** The equality of dimension is arithmetic: the alternating square of four dimensions and the symmetric square of three both give six, and the two sixes are built from different spaces.

**What the corpus does assert, and it is the honest limit.** The graviton is spin two as a composite: its carrier is a product of two vector carriers, and a product is not a carrier. **So spin two is above the roster without contradicting it**, and the corpus's phrase *no fourth* is a statement about fundamental carriers.

### Spin Three Has No Counterpart

**The principal copy's $V_3$ has complex dimension $7$.** No object of this corpus has spin $3$: not a carrier, not a composite, not an imported field. **The number occurs in the reconstruction of the mathematical corpus and nowhere in the physics of this block**, and the honest statement is that it has no physical interpretation at all rather than a small one.

## The Numeral Four in Four Places

**The numeral four is used four times in this block, for four unrelated dimensions, and the overlap is the source of the mistaken transfer.**

| the four | what it counts | dimension of what |
| --- | --- | --- |
| $\mathbf4$ of $\mathrm{SU}(4)$ | the fundamental, the quartet of lines | $4$ complex |
| $V_{3/2}$ of the principal copy | the module, label $\tfrac32$ | $4$ complex |
| the carrier basis $e_t,\vec e_x,\vec e_y,\vec e_z$ | the centre and the traceless part | $4$ complex, $1+3$ |
| the count $4=4$ of the Goldstone bookkeeping | the vector's gain against the scalar's loss | four degrees of freedom |

**The first two are one space read under two groups**, which is §*One Module, Two Spin Contents*. **The third is the algebra's own basis over $\mathbb{C}$**, and its four is $1+3$: one complex dimension closing the spin-$0$ carrier and three closing the spin-$1$ carrier. **The fourth is a count of degrees of freedom across the restructuring** and is not a dimension of a space at all.

**Why the table is worth printing.** The first three rows are dimensions of spaces and the fourth is a count of degrees of freedom, and a reader who merges any two of them can produce a false sentence: *the quartet is the module, so the scalar is a spin-$\tfrac32$ field* merges the first two; *the quartet has four real components, so it holds a spin-$\tfrac32$ state* merges the second and the third. **Each false sentence is refuted by naming the group or the reality of the four, and both refutations are one line.**

## What This Block Uses From the Operator Algebra

**The ambient algebra is used, and heavily; its spin content is not.** The regular representation $\rho_L$ and $\rho_R$, the sixteen two-sided products as a basis, the Clifford reading $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$, the fifteen arrays of the generators, and the derivation $[K,\cdot]$ with its array $K\otimes\mathrm{I}-\mathrm{I}\otimes K^{\mathsf{T}}$ are all statements about the ambient algebra. **They are statements about operators, and the block uses them as such.**

**The principal copy's list is never used.** No article of the block meets $7+5+3+1$; no field is written on $V_1$, $V_2$ or $V_3$; and no mass, coupling or vertex of the block refers to them. **The one place the list could enter is a branch record, and the block's branch records are records of the fifteen seen under $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$, at the restructuring, and not under the principal copy.**

**The fifteen are fifteen fields of one spin.** Each of the fifteen is a component of the connection on the vector carrier, so each is a spin-one field, and the fifteen is an internal index. **A reader who took the branch $7+5+3$ as a content would count seven spin-three, five spin-two and three spin-one fields in a model that has fifteen spin-one ones**, and would then look for the missing states in the spectrum.

**Where the answer would change, stated so that the boundary is visible.** The answer would change if this corpus gauged the principal copy and wrote a field on it; that field would be the spin-$\tfrac32$ one, and §*The One Irreducible Four, and Why It Names No Carrier* says why the corpus does not. **The absence is therefore a boundary of the corpus and not a gap in the writing: the algebra has the object, and the corpus declines the gauge group that would make it a carrier.**

## The Checks

| check | computation | result |
| --- | --- | --- |
| module Casimir of the principal copy | $j(j+1)$ at $j=\tfrac32$, four states | $\tfrac{15}{4}$ |
| principal Casimir on the ambient algebra | $0,2,6,12$ with multiplicities $1,3,5,7$ | $7+5+3+1=16$ |
| principal Casimir on the traceless part | $2,6,12$ with multiplicities $3,5,7$, no zero | $7+5+3=15$ |
| dimension of $\mathfrak{su}(4)$ | $16$ real parameters of an anti-Hermitian matrix, less the trace | $15$ |
| principal generators inside the gauge algebra | $iJ_x,iJ_y,iJ_z$ anti-Hermitian and traceless | in $\mathfrak{su}(4)$ |
| rotor copy on the module | $j(j+1)=\tfrac34$ on four states | $V_{1/2}\oplus V_{1/2}$ |
| rotor copy on the ambient algebra | Casimir $2$ on $12$, $0$ on $4$ | $4V_1\oplus4V_0$ |
| the two copies are different subgroups | spectra $\{\pm\tfrac12,\pm\tfrac32\}$ against $\{\pm\tfrac12,\pm\tfrac12\}$ | not conjugate |
| $\mathrm{SU}(4)$ on the ambient algebra | trace plus traceless | $1+15$ |
| carrier against closure | plane real $2$, module $V_{1/2}$ complex $2$ | $2s+1=2$ in both columns |
| $\mathbb{B}$ under the principal copy | left multiplication, no proper invariant subspace | irreducible $V_{3/2}$, complex $4$ |
| invariant dimensions of $\mathbb{B}$ | $0,2,4$ (left) and $0,1,3,4$ (conjugation), complex | the dimension $4$ is $\mathbb{B}$, reducible in both |
| the corpus's own bound | $1+2+3$ against $\dim_{\mathbb{C}}\mathbb{B}$ | $6>4$ |
| Rarita–Schwinger carrier count | $2\otimes3$, Casimir $\tfrac{15}{4}$ on $4$ and $\tfrac34$ on $2$ | $6=4+2$ |
| the carrier closures | $Z$, $S_\pm$, $\ker\operatorname{tr}$ | complex $1,2,3$ |

## Summary

**Three physical spins, and the numbers of $M_4(\mathbb{C})$ do not add a fourth.** The carriers of $\mathbb{B}$ are the line, the plane and the vector part, of real dimensions $1$, $2$ and $3$, and their closures are the centre, the two Peirce ideals and the traceless part, of complex dimensions $1$, $2$ and $3$; their spins are $0$, $\tfrac12$ and $1$, and the roster is fixed by the algebra before a group is named. **A spin is a pair, a group and a space, and the carriers are carried by $\mathbb{B}$ under the two actions of the unit quaternions on $\mathbb{B}$ itself.**

**The labels $0,1,2,3$ and the module label $\tfrac32$ belong to the principal copy, and this corpus does not gauge it.** Two three-dimensional subalgebras of $\mathfrak{su}(4)$, and the group itself, give three different lists on the same sixteen dimensions: the principal copy gives $7+5+3+1$ and the module $V_{3/2}$; the rotor copy gives $\tfrac12\oplus\tfrac12$ on the same module and $4V_1\oplus4V_0$ on the operators; the group gives $1+15$. **The module is one space and its spin depends on which copy reads it, and the corpus's carriers come from the rotor row.**

**The one true sense of $\tfrac32$ is a branch record.** The quartet $\mathbf4$ restricts to $V_{3/2}$, the adjoint $\mathbf{15}$ to $7+5+3$ with no singlet, and the singlet to $V_0$. **The quartet is a scalar and a fermion fundamental in this block, at spin $0$ and spin $\tfrac12$, and never a spin-$\tfrac32$ field.**

**No carrier of spin $\tfrac32$ exists, and the reason is a count of the product's own two actions.** A $\tfrac32$ carrier would need a closure of complex dimension $4$; under left multiplication the invariant dimensions are $0,2,4$ and under conjugation $0,1,3,4$, and in both the dimension $4$ is $\mathbb{B}$ itself and reducible. **Under the principal copy $\mathbb{B}$ is irreducible $V_{3/2}$, and that is why the label is real — but the principal copy is a construction on a chosen carrier space rather than an action of the unit quaternions on the algebra, and it is neither gauged nor written upon.** The field of the right shape is the imported $S\otimes V=4\oplus2$ with its constraint.

**Spin two is a composite and spin three does not occur.** The principal $V_2$ and the graviton's symmetric traceless square both count five and are different objects, one a summand of the operator algebra and the other a product of the field algebra; spin three is a number of the mathematical reconstruction with no counterpart here.

**The numeral four is four unrelated things**, and the two false sentences that merge them are both refuted in one line by naming the group or the reality of the four. **The absence of a spin-$\tfrac32$ carrier is a boundary of the corpus, since the principal copy is not an action of the unit quaternions on the algebra itself, and not a gap in the writing.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}$ | the biquaternion algebra, $\cong M_2(\mathbb{C})$, four complex dimensions; the algebra of fields |
| $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ | the ambient operator algebra, sixteen complex dimensions; carries no biquaternion name and no carrier |
| $\mathrm{SU}(4)$ | the gauge group of the block, fifteen real dimensions |
| $\mathfrak{su}(4)$ | its Lie algebra, the anti-Hermitian traceless matrices |
| the principal copy | the image of $\operatorname{Sym}^{3}$ of the defining two-dimensional module; a three-dimensional subalgebra of $\mathfrak{su}(4)$ |
| the rotor copy | the three-dimensional subalgebra generated by left multiplication of the unit elements, $\operatorname{diag}(u,u)$ with $u\in\mathrm{SU}(2)$ |
| $V_j$ | the mathematical corpus's carrier of spin $j$, complex dimension $2j+1$; quoted only where the mathematics is quoted |
| $s$, $s_z$ | the physical spin and its projection |
| carrier | the state space of a spin, of **real** dimension $2s+1$: $\mathbb{R}e_t$, $\Sigma(\vec u)$, $\mathfrak{k}$ |
| closure | the smallest invariant subspace containing a carrier, of **complex** dimension $2s+1$: $\mathbb{C}e_t$, $S_\pm$, $\ker\operatorname{tr}$ |
| $\tilde\Pi_{\mathrm{id},\pm}$ | the two Peirce idempotents, $\tfrac12(e_t\pm i\vec u)$ for a unit $\vec u\in\mathfrak{k}$, with $i$ the complex unit commuting with $\mathbb{H}$; $\tilde\Pi_++\tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=0$ |
| $Z=\mathbb{C}e_t$, $\ker\operatorname{tr}$ | the centre and the traceless part, the two pieces of the conjugation action, complex dimensions $1$ and $3$ |
| $V_{3/2}$ | the module of the principal copy, $\mathbb{C}^4$, complex dimension $4$ |
| $S_\pm=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}(\vec u)$ | the two minimal left ideals of $\mathbb{B}$ closing the plane, each of complex dimension $2$; the pair is selected by the axis $\vec u$ |
| $M_4P$ | a minimal left ideal of the operator algebra, complex dimension $4$; a subspace of $M_4$, not of $\mathbb{B}$ |
| $\mathfrak{k}$ | the vector part, the spin-one carrier, real dimension $3$ |
| $\mathbf4,\mathbf{15},\mathbf1$ | the fundamental, the adjoint and the singlet of $\mathrm{SU}(4)$ |
| $S\otimes V$ | the Rarita–Schwinger carrier, $6=4+2$ before the constraint |
| $\Phi\in(\mathbf4,\mathbf1,\mathbf2)$ | the scalar of the block, read here as the whole matrix |

## Further Reading

**The decomposition, from the mathematical corpus.**

- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](../articles_maths/the-clebsch-gordan-decomposition-of-m4c.html) — $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$, and the Casimir spectrum recomputed above.
- [The Four Carrier Lists of One Algebra at $n=4$](../articles_maths/the-four-carrier-lists-of-one-algebra-at-n-4.html) — the four lists, and why a label without a group is meaningless.
- [Two Numbers and Two Readings: $\tfrac32$ for the Module, $3$ for the Largest Carrier](../articles_maths/two-numbers-and-two-readings.html) — the element row against the operator row, which is the rule this article applies.
- [The Slot and the Summand: $\tfrac12$ in $\mathbb{B}$ and $\tfrac32$ in $M_4(\mathbb{C})$](../articles_maths/the-slot-and-the-summand.html) — the two rows side by side.
- [Integer Labels on the Algebra, a Half-Integer on the Module](../articles_maths/integer-labels-on-the-algebra-a-half-integer-on-the-module.html) and [No Half-Integer Summand at $n=4$](../articles_maths/no-half-integer-summand-at-n-4.html) — why the half-integer is a weight and not a label.
- [Introduction to the Spin-$\tfrac32$ Bispinor Spaces at $n=4$](../articles_maths/introduction-to-the-spin-three-halves-bispinor-spaces-at-n-4.html) — the module, the bispinors, and $V_{3/2}\otimes V_{3/2}^{*}\cong M_4(\mathbb{C})$, which is why the principal list is the bispinor decomposition.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](../articles_maths/the-anti-hermitian-derivations-of-m4c-as-su4.html) — the fifteen, and the derivation used above.

**The physics, from this corpus.**

- [The Carrier Roster: Three Spins and No Fourth, Fixed Before Any Group Acts](the-carrier-roster-three-spins-and-no-fourth.html) — the three carriers, the completion, and the difference between a carrier and a composite.
- [What a Group Can Accept: A Carrier Must Transform in a Representation](what-a-group-can-accept-a-carrier-must-transform-in-a-representation.html) — the second filter, and the sector table.
- [Particle Spins in the Biquaternion Algebra: Three Carriers, Their Meaning and Their Order](particle-spins-in-the-biquaternion-algebra-three-carriers-their-meaning-and-their-order.html) — the order of the carriers and the paragraph above spin one.
- [The Determination of the Possible Spins in Biquaternionic Form](the-determination-of-the-possible-spins-in-biquaternionic-form.html) — the count of invariant subspaces quoted in §*Why No Carrier of Spin Three Halves*.
- [The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration of Rank Three](the-su4-model-four-lines-fifteen-generators-one-declaration.html) and [The Three Lines in $\mathrm{SU}(4)$: A Coordinate Label on the Fifteen, Not a Charge](the-three-lines-in-su4-a-coordinate-label-on-the-fifteen-not-a-charge.html) — the group, the quartet and the fifteen.
- [Matrix Representations Conventions](matrix-representations-conventions.html) — the ambient $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, the regular representation and the sixteen basis operators.
- [The Rarita–Schwinger Equation: Spin Three-Halves from the Vector Carrier and the Dirac Field](../articles_internal/archives/the-rarita-schwinger-equation-spin-three-halves-from-the-vector-carrier-and-the-dirac-field.html) and [its canonical quantisation](../articles_internal/archives/canonical-quantization-of-the-rarita-schwinger-field-from-the-vector-carrier-and-the-dirac-field.html) — the imported field of that shape.
