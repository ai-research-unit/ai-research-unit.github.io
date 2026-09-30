# __The Particle Roster of the Complex Octonionic Chain Algebra__

## Introduction

The complex octonionic chain algebra $\overleftarrow{\mathbb{C}\otimes\mathbb{O}}$ is isomorphic to the Clifford algebra $\mathrm{Cl}(6)\cong M_8(\mathbb{C})$, and its minimal left ideals, built from Furey's ladder operators, carry sixteen states whose charges are exactly those of one generation of the Standard Model. This is the most concrete construction in the neighbourhood of the biquaternion corpus: it is associative, it carries an intrinsic $\mathrm{su}(3)$ with the dimensions and rank of colour, its charges are eigenvalues of a number operator and are therefore quantised, and the states of a single ideal fall into colour singlets and colour triplets of the right multiplicities. The construction is also not the biquaternion framework. The chain algebra is a sixty-four-dimensional complex matrix algebra, while $\mathbb{B}\cong M_2(\mathbb{C})$ is eight-dimensional and real; the algebra of this article cannot be reached from $\mathbb{B}$ by any of its own operations, and the inclusion of this article in the physics category is a statement about the size of the literature's answer to the colour and generation problems, not a claim that the framework contains it.

The article is placed here because the framework's own ledger names this construction. *The Standard Model under the Biquaternion Framework — A Research Agenda* records that the framework supplies $\mathrm{U}(2)$ and never $SU(3)$, and that the one candidate ever named for a larger internal factor was an enlargement of the carrier; *The Number of Generations and the Biquaternion Algebra* records the octonionic chain-algebra construction as one of the two nearby constructions that suggest a three, with its three coming from a reading of a decomposition of a larger carrier and not from a derivation inside $\mathbb{B}$; and *The Gluon: An Octet Outside the Biquaternion Algebra* establishes the octet on the same footing, outside the algebra. What none of those articles does is exhibit the sixteen states, their charges, and the exact point at which the reading either succeeds or fails. That is this article's task, and its main result is a statement of where the open end is: the assignment is a reading, the decisive tests are three finite commutator conditions, and none of them has been performed.

The conventions are those of *Complex Octonions and the Clifford Algebra Cl(6)* of the mathematics category, which establishes the algebra, the ladder operators, the maximal totally isotropic subspace, the $\mathrm{su}(3)$, and the charge spectrum of the minimal left ideal of the idempotent $P$. The Clifford-algebraic notion of a minimal left ideal is that of *Spinors as Minimal Left Ideals with Inner Conjugation*; the spinor representations and the $\mathrm{su}(4)$-and-$\mathrm{so}(6)$ correspondence used below are those of *Spin Representations of the Orthogonal Lie Algebra with Inner Conjugation* and *List of Clifford Algebras and Spin Groups*; the general theorem behind the intrinsic $\mathrm{su}(3)$ is that of *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*; and the electroweak and colour content against which the reading is compared is that of *The Standard Model under the Biquaternion Framework — A Research Agenda* and *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*. Nothing in this article is derived from the biquaternion algebra, and no result of this article feeds back into the framework's ledger.

## The Chain Algebra and Its Ladder Structure

The facts needed are collected here in the order in which the construction uses them. All of them are established in the mathematics article.

The six chains $e_1,\dots,e_6$ satisfy $\{e_i,e_j\} = -2\delta_{ij}I$, generate the algebra, and their product is the volume element $e_7 = e_1e_2\cdots e_6$ with $e_7^2 = -I$. The ladder operators

$$
\alpha_1 = \tfrac12(-e_5+ie_4), \qquad \alpha_2 = \tfrac12(-e_3+ie_1), \qquad \alpha_3 = \tfrac12(-e_6+ie_2),
$$

and their conjugates $\alpha_i^\dagger$ satisfy

$$
\{\alpha_i,\alpha_j\} = \{\alpha_i^\dagger,\alpha_j^\dagger\} = 0, \qquad \{\alpha_i,\alpha_j^\dagger\} = \delta_{ij}I ,
$$

so that the span of the $\alpha_i$ is a three-dimensional maximal totally isotropic subspace of the complexified six-space $\mathbb{C}^6 = \mathrm{span}\{e_1,\dots,e_6\}$, and the span of the $\alpha_i^\dagger$ is the conjugate isotropic subspace. The number operator

$$
N = \sum_{i=1}^{3}\alpha_i^\dagger\alpha_i
$$

has integer eigenvalues $0,1,2,3$ with multiplicities $1,3,3,1$ on the states buildable from a vacuum, and the **charge** is $Q = \tfrac13 N$.

The isotropic subspace carries an intrinsic $\mathrm{su}(3)$: the eight chains

$$
\Lambda_1 = -\alpha_2^\dagger\alpha_1-\alpha_1^\dagger\alpha_2,\quad
\Lambda_2 = i\alpha_2^\dagger\alpha_1-i\alpha_1^\dagger\alpha_2,\quad
\Lambda_3 = \alpha_2^\dagger\alpha_2-\alpha_1^\dagger\alpha_1,
$$

together with the five further chains obtained cyclically from them and

$$
\Lambda_8 = -\tfrac1{\sqrt3}\bigl(\alpha_1^\dagger\alpha_1+\alpha_2^\dagger\alpha_2-2\alpha_3^\dagger\alpha_3\bigr),
$$

satisfy $[\tfrac12\Lambda_a,\tfrac12\Lambda_b] = if^{abc}\tfrac12\Lambda_c$ with the standard structure constants, coincide with the octonionic automorphism generators fixing $e_7$, and commute with $N$ and with $e_7$. The algebra $\mathrm{su}(3)\oplus\mathrm{u}(1)$ so obtained acts on the complexified six-space $\mathbb{C}^6$, where the generators are the antisymmetric bilinears in the $\alpha$ and $\alpha^\dagger$, and the representation of $\mathrm{su}(3)\oplus\mathrm{u}(1)$ on that six-space will be needed below.

## The Minimal Left Ideal and the Charges of One Generation

The idempotent

$$
P = \alpha_1\alpha_2\alpha_3\,\alpha_3^\dagger\alpha_2^\dagger\alpha_1^\dagger
$$

is primitive: $P^2 = P$, $\alpha_iP = 0$, $\omega^\dagger\alpha_i^\dagger = 0$ with $\omega = \alpha_1\alpha_2\alpha_3$, and $P$ has rank one as an $8\times8$ matrix, so that the left ideal $S^u = \mathrm{Cl}(6)P$ is eight-dimensional with basis

$$
\Bigl\{\,P,\ \alpha_1^\dagger P,\ \alpha_2^\dagger P,\ \alpha_3^\dagger P,\
\alpha_3^\dagger\alpha_2^\dagger P,\ \alpha_1^\dagger\alpha_3^\dagger P,\ \alpha_2^\dagger\alpha_1^\dagger P,\
\alpha_3^\dagger\alpha_2^\dagger\alpha_1^\dagger P \,\Bigr\} .
$$

On this basis the number operator takes the values $0,1,1,1,2,2,2,3$, so the charge $Q = N/3$ takes the values

$$
0,\quad \tfrac13,\tfrac13,\tfrac13,\quad \tfrac23,\tfrac23,\tfrac23,\quad 1 ,
$$

which is the charge spectrum of one generation's worth of states in the four multiplet pattern $1 + 3 + 3 + 1$: a singlet of charge $0$, a triplet of charge $1/3$, a triplet of charge $2/3$, and a singlet of charge $1$. The charge is quantised because it is the eigenvalue of a number operator, and the denominator three is the dimension of the isotropic subspace; this is the mechanism the framework does not possess, where the abelian charge is a continuous central label.

The conjugate idempotent

$$
P^c = \alpha_1^\dagger\alpha_2^\dagger\alpha_3^\dagger\,\alpha_3\alpha_2\alpha_1
$$

is also primitive, is orthogonal to $P$, and generates a second eight-dimensional left ideal. The literature's reading takes its states to be the conjugates of the first ideal's states, with the charges negated, so that the sixteen states of the two ideals together are

$$
\underbrace{1(0)+3(\tfrac13)+3(\tfrac23)+1(1)}_{S^u} \ \oplus\ \underbrace{1(0)+3(-\tfrac13)+3(-\tfrac23)+1(-1)}_{S^{u,c}} ,
$$

and this is one generation: the neutrino, the three up-type and three down-type colour states and their conjugates, the electron and the positron, together with the two neutral states. The identification of the second ideal's spectrum with the negated spectrum of the first is the literature's bookkeeping rather than a computation reproduced in the corpus, and the mathematics article that establishes the first ideal records exactly this bookkeeping of the conjugate half as not reproduced. It is the first of two places in the construction where a reading is doing work.

## The Colour Triples and Their Conjugation

The four multiplets of one ideal have a Lie-theoretic meaning which the reading uses, and which is standard. The complexified six-space $\mathbb{C}^6$ carries $\mathrm{so}(6,\mathbb{C})\cong\mathrm{sl}(4,\mathbb{C})$, whose rank is three, and the subalgebra $\mathrm{su}(3)\oplus\mathrm{u}(1)$ is a maximal reductive subalgebra. The six-dimensional representation branches as

$$
\mathbf 6 = \mathbf 3_{+\frac23}\oplus\bar{\mathbf 3}_{-\frac23} ,
$$

and the two spinor representations of $\mathrm{so}(6,\mathbb{C})$, of dimensions four each, branch as

$$
\mathbf 4 = \mathbf 3_{+\frac13}\oplus\mathbf 1_{-1}, \qquad
\bar{\mathbf 4} = \bar{\mathbf 3}_{-\frac13}\oplus\mathbf 1_{+1},
$$

in the normalisation in which the $\mathrm{u}(1)$ generator is traceless on the six-space. The eight states of one ideal, with charges $0,\tfrac13,\tfrac13,\tfrac13,\tfrac23,\tfrac23,\tfrac23,1$ as eigenvalues of $Q = N/3$, are counted by these multiplets as $1+3+3+1$: the two triplets are the colour triplet and antitriplet components of the two spinors, and the two singlets are the spinor singlets. The $\mathrm{su}(3)$ acts on the ideal, and its action on the triplet states is the defining three-dimensional representation with its conjugate on the antitriplet states; the triplet and the antitriplet are exchanged by the conjugation of the algebra, and this is why the two ideals are related by charge conjugation.

Two consequences follow, and both are used by the reading. First, the sixteen states of the two ideals are vector-like under the $\mathrm{su}(3)$: every colour multiplet in the first ideal is matched by its conjugate in the second, so the $\mathrm{su}(3)$ of the isotropic structure is a vector-like colour symmetry, and a chiral colour symmetry would need the two ideals to be treated differently. Second, the three-colour structure is not put in by hand and is not chosen: it is the rank-one case of the general fact, established in *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*, that a maximal totally isotropic subspace of a complexified Euclidean space carries a unitary symmetry whose representation theory reproduces the colour multiplets. This is the precise sense in which the literature's construction has an answer to the colour problem that the biquaternion framework does not: it is not that a group $SU(3)$ has been proposed and attached, but that the largest isotropic subspace available in the algebra carries an intrinsic $\mathrm{su}(3)$ together with a three-dimensional module.

## The Lorentz Structure and Chirality on the Two Ideals

The Lorentz group must also be found, since the Standard Model is chiral and the construction's states are spinors. Here the construction's structure is different from what the three-supercharge discussion may suggest, and the difference is worth stating plainly.

The algebra $\mathrm{so}(6,\mathbb{C})\cong\mathrm{sl}(4,\mathbb{C})$ acts on the six-space and on the ideals; the idempotent singles out the $\mathrm{su}(3)\oplus\mathrm{u}(1)$ of the isotropic structure, which is the Levi factor of the stabiliser of the isotropic splitting, and that is the internal symmetry the construction gives. The complexified Lorentz algebra is six-dimensional and simple-factorisable,

$$
\mathrm{so}(3,1)_{\mathbb{C}} \cong \mathrm{su}(2)_L\oplus\mathrm{su}(2)_R ,
$$

and the question that has to be answered is where it sits. The corpus's caution is that the answer is not automatic. If the Lorentz algebra is taken inside the internal algebra $\mathrm{so}(6,\mathbb{C})$, it must commute with the colour $\mathrm{su}(3)$ and with the abelian $\mathrm{u}(1)$ — otherwise the colour multiplet structure that the construction's success rests on is destroyed by the Lorentz action — and the algebra available to commute with $\mathrm{su}(3)\oplus\mathrm{u}(1)$ inside $\mathrm{so}(6,\mathbb{C})$ is the centraliser of that subalgebra, which is where the question becomes a finite computation. The corpus has not performed it. The alternative reading, which is the one the literature uses, keeps the Lorentz group outside the internal algebra altogether: the ideals supply the internal quantum numbers, and the Lorentz group acts on the four-dimensional spacetime spinor index that each internal state carries, so that the two are independent by construction and the colour structure is untouched. Under that reading the state of a fermion is a Weyl spinor times an internal state, and the question of how many internal states make one generation is answered separately from the question of chirality.

The chirality of the construction, in the literature's reading, is then the statement that the single ideal and the conjugate ideal are distinguished by the two summands of the complexified Lorentz algebra — the transformations of one summand acting on one ideal only and those of the other summand on the conjugate ideal only — so that the Standard Model's requirement that left-handed and right-handed components transform inequivalently is met with no internal space and no compactification. The algebraic ingredient the statement needs is the separate action of the two ideals, which is exact; the identification of the summands with $\mathrm{su}(2)_L$ and $\mathrm{su}(2)_R$, and the choice of the commuting Lorentz algebra inside or outside the internal algebra, are the reading's steps, and neither is recomputed in the corpus. The framework's own chirality result is the contrast: *Chiral Fermions in the Biquaternion Framework* establishes the projectors, the chirality-odd mass bilinear and the selection rule $q_L = q_R$, but not a non-central compact action under which the two chiral halves transform inequivalently, which is the upstream chirality problem on the agenda's list. Whether the chain algebra's construction does better depends on the commuting-algebra computation just described.

The reading of one ideal plus its conjugate as one generation has a cost, and the cost is best stated in the language of representations. Under the internal algebra $\mathrm{su}(3)\oplus\mathrm{u}(1)$ the sixteen states are self-conjugate: every state of charge $q$ is accompanied by a state of charge $-q$ with the conjugate colour, with the two exceptions of the two neutral singlets, which are each their own conjugate. A self-conjugate representation content cannot be chiral, since chirality requires the content to be complex; chirality therefore has to come from a further factor, exactly as it comes from the weak $\mathrm{su}(2)$ in the Standard Model. The Standard Model's own fifteen states are also self-conjugate under colour and hypercharge, and their chirality is due to the weak factor, under which the doublets and the singlets sit in inequivalent representations. The minimal version of the construction has no such factor: its internal algebra is $\mathrm{su}(3)\oplus\mathrm{u}(1)$ alone. The chirality of the construction therefore has to come from the enlarged version, whose second non-abelian factor plays the role that $\mathrm{su}(2)_L$ plays in the Standard Model. The corpus's own statement of the framework's chirality problem — that a mass term for a chiral fermion requires a compensating scalar, and that the framework's module is a Dirac module $S\oplus\bar S$ — has its counterpart here, and in the construction the counterpart is met by enlarging the supercharge sector rather than by enlarging the algebra.

## The Hypercharge Reading and Its Decisive Tests

What remains, in the literature's reading, is the assignment of the states to the Standard Model's particles, and it is the step that deserves the closest scrutiny because it is where a construction of this kind can go wrong quietly.

The assignment of the sixteen states, in the literature's reading, is the following, with every state taken as a left-handed Weyl field in the Standard Model's own chiral convention so that the conjugate states of the second ideal stand for the right-handed particles. In the first ideal, the singlet of charge $0$ is the left-handed neutrino; the triplet of charge $1/3$ is the down-type antiquark $\bar d$; the triplet of charge $2/3$ is the up-type quark $u$; and the singlet of charge $1$ is the antielectron $e^+$. In the second ideal, the singlet of charge $0$ is the second neutral state; the triplet of charge $-1/3$ is the down-type quark $d$; the triplet of charge $-2/3$ is the up-type antiquark $\bar u$; and the singlet of charge $-1$ is the electron $e^-$. Every colour multiplet appears with the right multiplicity, and the charges are the observed electric charges in units in which the charge quantum is a third.

The fifteen states of one chiral Standard-Model generation, with the electric charges in the same units and again all written as left-handed Weyl fields, are

$$
1(0),\quad 3(\tfrac13),\quad 3(-\tfrac13),\quad 3(\tfrac23),\quad 3(-\tfrac23),\quad 1(1),\quad 1(-1),
$$

and the sixteen states of the two ideals supply exactly this multiset and one further neutral state: the two neutrals, which is what a construction built on two ideals rather than on one gives. The matching is not a coincidence of multiplicities only. It is worth recording, however, that the partition of the sixteen into the two ideals is **not** the partition of the fifteen into the Standard Model's unified multiplets. The ideals split the states by the sign of the number-operator charge — eight states of non-negative charge in the first, eight of non-positive charge in the second — whereas the fifteen states of a chiral generation group into a $\bar{\mathbf 5}$ and a $\mathbf{10}$ of $SU(5)$, each of which mixes the two signs: the $\bar{\mathbf 5}$ carries the $1/3$ triplet with the neutral and the $-1$ singlet, and the $\mathbf{10}$ carries the $2/3$ triplet, the $-1/3$ triplet, the $-2/3$ triplet and the $+1$ singlet. Both groupings contain the same sixteen (or fifteen) charge values, so the charge table fixes the multiplicities and not the grouping; the assignment of individual states to particles is a choice of grouping, and it is the literature's choice, not a consequence of the algebra. This is the second place in the construction where a reading is doing work, and it is more consequential than the first, because the grouping determines which states are the $SU(2)$ doublets of the enlarged construction.

Anomaly cancellation, which in the Standard Model fixes the relative hypercharges and is a nontrivial consistency condition, is automatic for the assignment, since the assignment is the Standard Model's own charge table: the conditions $\sum Y = 0$, $\sum Y^3 = 0$ and $\sum YT_3^2 = 0$ hold for the observed multiplets, and the construction reproduces the observed multiplets. The construction's success on the charge front is therefore real, and it is the reason the literature's claim is worth the corpus's attention.

The decisive tests are not the charge table, which any abelian choice can match, but whether the abelian direction that the charge defines is compatible with the $\mathrm{su}(3)$ and with the Lorentz structure in the way a gauge charge must be. Three conditions have to hold, and they are independent.

- **The charge must be a combination of the algebra's own generators, with the weak isospin present.** The assignment above takes the charge to be $Q = N/3$ and identifies it directly with the Standard Model's electric charge. The electric charge of a state is a combination of the weak isospin and the hypercharge, $Q = T_3+Y$, and the electric charges of the right-handed components carry no $T_3$ while those of the left-handed doublets do. A single abelian eigenvalue of a number operator is not a combination of $T_3$ and $Y$ unless $T_3$ is separately present and the alignment is specified. Whether the algebra's abelian generator is to be identified with $Y$, with $Q$, or with the combination $T_3+Y$ is a choice, and the choice must be justified by the algebra and not by the desired answer. The minimal version of the construction has no second non-abelian factor to supply $T_3$; the enlarged version does.
- **The charge must be isotropic in the colour directions.** A gauge charge that commutes with $\mathrm{su}(3)$ acts as a scalar on each colour multiplet, so that all states in one multiplet have the same charge — which is why the Standard Model's hypercharge and electric charge are colour-blind. If the abelian generator of the construction is a combination $Q = N/3 + \sum_a c_a H_a$ of the number operator and a colour Cartan generator $H_a$, then the construction does not have a colour-blind charge: the states within one colour multiplet are split by the $H_a$ contribution. The requirement is that the coefficient vector $c$ vanish for the abelian generator that acts on the physical spectrum, once the theory's full gauge embedding is taken into account. This is a finite computation: the generator in question is a specific element of the algebra, its components on the $\mathrm{su}(3)$ Cartan subalgebra are determined by the requirement that it commute with the full unbroken symmetry, and its projection on the colour Cartan is a definite vector. If that projection vanishes, the construction has a colour-blind charge and the reading stands; if it does not, the states inside each colour triplet have unequal charges and the assignment to colour multiplets is inconsistent as stated.
- **The charge must commute with the Lorentz action.** The charge of a state must be a Lorentz-invariant label. In the construction the number operator commutes with $e_7$ and with the $\mathrm{su}(3)$; whether it commutes with the Lorentz algebra identified by the reading — which, as the previous section records, is either a subalgebra of the internal algebra commuting with the colour or an external factor acting on spacetime indices — is again a finite check of commutators, and it decides which combination of the generators is a candidate charge at all.

The three conditions are commutator conditions, and each is finite: the centraliser of $\mathrm{su}(3)\oplus\mathrm{u}(1)$ inside $\mathrm{so}(6,\mathbb{C})$, the projection of the physical abelian generator on the colour Cartan subalgebra, and the commutator of that generator with the Lorentz algebra. The corpus has performed none of them, and the literature's claim that the construction reproduces the Standard Model's electric charges requires all three to hold. Stated as a single question: does the complex octonionic chain algebra's enlarged construction contain a commuting Lorentz algebra, and does its abelian generator reduce to a colour-blind, Lorentz-invariant element on the physical spectrum? The claim requires an affirmative answer; a computation would settle it in either direction; and this is the exact sense in which the construction is a candidate and not a result. It is also the reason this article belongs to the physics category rather than to the mathematics one: the mathematics of the ideals is settled, and what remains is the physics bookkeeping.

## Sixteen States and the Doubling to Thirty-Two

There is a second, independent reason to think that the minimal version is not the whole construction, and the corpus records it because it bears on the same chirality problem as the previous section: the minimal version's supercharge count is not the one the literature's optimal version uses.

The minimal version described here has three pairs of ladder operators, and their algebra generates, on a single ideal, eight states; the three ladder operators are the ones built from three of the six Clifford generators, with the seventh unit of the octonions playing the role of the volume element and of the abelian factor. The literature's analyses of the optimal supercharge count settle on a version with a larger supercharge sector in which the generation content, the unbroken symmetries and the chirality assignment are organised differently, and whose state count is thirty-two rather than sixteen. The corpus records the outcome and not the derivation: what matters here is that the successful version is larger than the minimal one, that the additional structure is exactly the weak isospin and the chirality assignment that the minimal version leaves to a reading, and that the extra structure is obtained from the same algebra by a different choice of the supercharge sector rather than by leaving the algebra.

The point for the corpus is not the arithmetic of the doubling but the shape of the argument. The construction's successes — quantised charge, three colours, the observed charge multiplicities — are not independent of its supercharge count, and the count is a choice. A minimal version is easier to exhibit and harder to justify; the version the literature settles on is larger, and its extra structure is the electroweak and chirality structure. The corpus records the construction, and this article in particular, because the shape of that argument is the same shape as the one the framework's own ledger enforces: the objects that the framework lacks are supplied, outside the framework's algebra, by a construction whose successful version is larger than its minimal version, at the price of a carrier that the framework's ceiling does not contain.

## What the Construction Establishes, Reads, and Leaves Open

The construction is best summarised by sorting its steps, as the framework's own agendas sort theirs.

| Step | Status |
|---|---|
| $\overleftarrow{\mathbb{C}\otimes\mathbb{O}}\cong\mathrm{Cl}(6)\cong M_8(\mathbb{C})$; ladder operators; maximal isotropic subspace and its conjugate | Established in the mathematics article, recomputed |
| Primitive idempotent $P$; eight-dimensional minimal left ideal; charge spectrum $0,\tfrac13,\tfrac13,\tfrac13,\tfrac23,\tfrac23,\tfrac23,1$ as eigenvalues of $Q=N/3$ | Established in the mathematics article, recomputed |
| Intrinsic $\mathrm{su}(3)$ on the isotropic subspace, agreeing with the octonionic automorphism generators and commuting with $N$ and $e_7$ | Established in the mathematics article, recomputed |
| Second ideal from the conjugate idempotent, with the conjugate charge spectrum | Reading; the corpus establishes the first ideal and records the conjugate bookkeeping as not reproduced |
| Branchings $\mathbf 6 = \mathbf 3_{2/3}\oplus\bar{\mathbf 3}_{-2/3}$ and $\mathbf 4 = \mathbf 3_{1/3}\oplus\mathbf 1_{-1}$ | Standard; the Lie theory of the complexified orthogonal algebra |
| The sixteen states as one generation, with the four multiplets assigned to the Standard Model's particles | Reading; the charge multiset matches, and both the assignment of individual states and the partition of the sixteen into the two ideals are choices, not consequences |
| The partition of the sixteen by the number operator coincides with the Standard Model's $\bar{\mathbf 5}+\mathbf{10}$ grouping | **No**; the ideals split by the sign of the charge, and the unified multiplets mix signs |
| Chirality of the construction: the two ideals distinguished by the two summands of the complexified Lorentz algebra | Reading; the separate action of the two ideals is exact, the identification of the summands is not recomputed |
| Self-conjugacy of the sixteen states under the internal $\mathrm{su}(3)\oplus\mathrm{u}(1)$ | Established by the charge multiset; chirality therefore requires the weak factor of the enlarged version |
| Colour-blindness, Lorentz invariance and $\mathrm{su}(3)$-commutativity of the abelian charge on the physical spectrum | **Open**; the three finite commutator computations described in the hypercharge section have not been performed |
| Existence of a Lorentz algebra commuting with the colour inside the internal algebra | **Open**; a centraliser computation in $\mathrm{so}(6,\mathbb{C})$ |
| Full supercharge sector with one generation and no spurious doubling; the thirty-two-state version | Literature's analysis; the state count is recorded, the derivation is not recomputed |
| Agreement with the Standard Model's anomaly conditions | Automatic for the charge table as observed; not an independent check |

Three statements deserve emphasis.

- **What the construction genuinely supplies that the framework does not.** A quantised charge, from a number operator rather than from a continuous central label; an intrinsic three-colour structure with a three-dimensional module, from a maximal isotropic subspace rather than from a proposed enlargement; and a sharp sense in which the charge multiplet structure of one generation is present in a finite algebra, with the observed multiplicities and the observed charges in units of a third. These are not transcriptions: they are properties of a finite algebra.
- **What it does not supply, and the shape of the gap.** The identification of the abelian generator with a Standard Model charge, the alignment of the weak isospin, the partition of the sixteen states into the Standard Model's multiplets, and the choice of the supercharge sector are all readings or choices rather than consequences; the successful version of the construction in the literature is larger than the minimal one, and the extra structure supplies the electroweak and chirality content. The construction's claim to a generation is a claim about a carrier and a decomposition, which is exactly the structure that *The Number of Generations and the Biquaternion Algebra* identifies as the source of every outside three.
- **What would settle it.** The three computations of the hypercharge section — the centraliser of $\mathrm{su}(3)\oplus\mathrm{u}(1)$ inside $\mathrm{so}(6,\mathbb{C})$, the projection of the physical abelian generator on the colour Cartan subalgebra, and its commutator with the Lorentz algebra — together with the reproduction of the enlarged supercharge sector. Each is finite and each is a computation in the complex octonionic chain algebra, not in the biquaternion framework. If the abelian projection vanishes and the Lorentz algebra exists, the reading is consistent and reduces to a check; if not, the assignment as stated fails and a different abelian generator must be chosen.

## Summary

The complex octonionic chain algebra is $\mathrm{Cl}(6)\cong M_8(\mathbb{C})$; Furey's ladder operators build a three-dimensional maximal totally isotropic subspace and its conjugate, the isotropic subspace carries an intrinsic $\mathrm{su}(3)$ that commutes with the number operator $N$ and with the volume element, and the primitive idempotent $P = \alpha_1\alpha_2\alpha_3\alpha_3^\dagger\alpha_2^\dagger\alpha_1^\dagger$ generates an eight-dimensional minimal left ideal whose states carry the charges $0,\tfrac13,\tfrac13,\tfrac13,\tfrac23,\tfrac23,\tfrac23,1$ as eigenvalues of $Q = N/3$. The conjugate idempotent gives a second eight-dimensional ideal, whose states the literature reads as the conjugates of the first, so that the two ideals together carry sixteen states: exactly the charge multiset of one chiral Standard-Model generation plus one further neutral state, arranged as four multiplets of an intrinsic colour $\mathrm{su}(3)$ with a three-dimensional module. The charges are quantised because they are eigenvalues of a number operator, and the colour triplets arise because the maximal isotropic subspace of a complexified six-space carries $\mathrm{su}(3)$. What the construction does not supply without further input is the identification of its abelian generator with the Standard Model's electric charge or hypercharge, the weak isospin that makes the spectrum chiral, the partition of the sixteen states into the Standard Model's unified multiplets, and the supercharge count of the literature's larger version, whose state count is thirty-two; the decisive open computations are the centraliser of $\mathrm{su}(3)\oplus\mathrm{u}(1)$ in $\mathrm{so}(6,\mathbb{C})$, the projection of the physical abelian generator on the colour Cartan subalgebra, and its commutator with the Lorentz algebra. The construction is outside the biquaternion algebra — $\mathrm{Cl}(6)$ is sixty-four-dimensional and complex, $\mathbb{B}$ is eight-dimensional and real — and it is recorded here because it is the largest of the nearby constructions, and the one that comes closest to supplying in a single finite algebra the three properties that the framework's ledger records as missing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\overleftarrow{\mathbb{C}\otimes\mathbb{O}}\cong\mathrm{Cl}(6)\cong M_8(\mathbb{C})$ | Complex octonionic chain algebra, $\dim_{\mathbb{C}} = 64$ |
| $e_1,\dots,e_6$ | Clifford generators, $\{e_i,e_j\} = -2\delta_{ij}I$ |
| $e_7 = e_1e_2\cdots e_6$ | Volume element, $e_7^2 = -I$; commutes with $N$ |
| $\alpha_i$, $\alpha_i^\dagger$ | Ladder operators; square-zero, $\{\alpha_i,\alpha_j^\dagger\} = \delta_{ij}I$ |
| $W = \mathrm{span}\{\alpha_1,\alpha_2,\alpha_3\}$ | Maximal totally isotropic subspace; conjugate $\bar W = \mathrm{span}\{\alpha_i^\dagger\}$ |
| $N = \sum_i\alpha_i^\dagger\alpha_i$ | Number operator; eigenvalues $0,1,2,3$ with multiplicities $1,3,3,1$ |
| $Q = \tfrac13 N$ | Charge; values $0,\tfrac13,\tfrac23,1$ on one ideal |
| $\Lambda_1,\dots,\Lambda_8$ | Generators of the intrinsic $\mathrm{su}(3)$ |
| $P = \alpha_1\alpha_2\alpha_3\alpha_3^\dagger\alpha_2^\dagger\alpha_1^\dagger$ | Primitive idempotent; rank one |
| $S^u = \mathrm{Cl}(6)P$, $S^{u,c} = \mathrm{Cl}(6)P^c$ | The two eight-dimensional minimal left ideals |
| $\mathbf 6 = \mathbf 3_{2/3}\oplus\bar{\mathbf 3}_{-2/3}$ | Branching of the six-space under $\mathrm{su}(3)\oplus\mathrm{u}(1)$ |
| $\mathbf 4 = \mathbf 3_{1/3}\oplus\mathbf 1_{-1}$, $\bar{\mathbf 4} = \bar{\mathbf 3}_{-1/3}\oplus\mathbf 1_{1}$ | Branching of the two spinors of $\mathrm{so}(6,\mathbb{C})$ |
| $\mathrm{so}(3,1)_{\mathbb C} \cong \mathrm{su}(2)_L\oplus\mathrm{su}(2)_R \subset \mathrm{so}(6,\mathbb{C})$ | Complexified Lorentz algebra, inside or outside the internal algebra as the reading chooses |
| $16 = 8+8$ | States of the two ideals; one generation in the literature's reading |
| $32$ | States of the higher-supercharge version, one generation without doubling |

## Further Reading

- C. Furey, "Standard model physics from an algebra?" (2016), arXiv:1611.09182, for the complex octonionic chain algebra, the ladder operators, the maximal totally isotropic subspace, the minimal left ideal, and the reading of its states as one generation; the source of the construction.
- C. Furey, "Unified theory of ideals", *Physical Review D* **86** (2012) 025024, for the earlier form of the construction and the role of the ideals.
- C. Furey, "Three generations, two unbroken gauge symmetries, and one eight-dimensional algebra", *Physics Letters B* **785** (2018) 84–89, for the version in which the supercharge sector is enlarged and the generation content, the unbroken symmetries and the chirality assignment are organised differently; the literature's answer to the doubling treated in the text.
- The literature on the minimal supercharge count, among which A. Dittmann and T. Schücker's analyses of fermion generations from division-algebraic constructions, for the thirty-two-state version carrying one generation with the smallest number of supercharges; recorded as the literature's argument for the larger construction described in the text.
- J. C. Baez, "The octonions", *Bulletin of the American Mathematical Society* **39** (2002) 145–205, for the normed division algebras, $\mathrm{Aut}(\mathbb{O}) = G_2$, and the octonionic origin of the $\mathrm{su}(3)$.
- *Complex Octonions and the Clifford Algebra Cl(6)*, *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*, and *Spinors as Minimal Left Ideals with Inner Conjugation* — the mathematics category's articles on which the algebraic statements of this article rest.
- *The Gluon: An Octet Outside the Biquaternion Algebra* and *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)* — the colour sector of the framework and the reasons it lies outside the algebra.
- *The Number of Generations and the Biquaternion Algebra* — the count of generations, and the chain-algebra construction recorded there as one of the two nearby constructions that suggest a three.
- *The Standard Model under the Biquaternion Framework — A Research Agenda* — the ledger of the framework's gauge, matter, scalar and generation gaps, against which the construction of this article is the outside comparison.
