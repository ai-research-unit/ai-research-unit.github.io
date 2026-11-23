# __Charge Quantisation from the Fourth Colour: One Trace, One Third, and Where the Twenty-One Generators Go__

## Introduction

**The question.** Why is the proton's charge exactly minus the electron's? The Standard Model assigns hypercharges and then checks that the anomalies cancel. It does not explain the equality; it imposes it. Does this frame do better?

**The answer, in one line.**

$$
\boxed{\;
\operatorname{tr}_{\mathbf4}(B-L)=3\Bigl(+\tfrac13\Bigr)+(-1)=0
\quad\Longrightarrow\quad
3q+\ell=0
\quad\Longrightarrow\quad
q=-\tfrac13\ell
\;}
$$

The trace vanishes because $B-L$ is a generator, and a generator of $\mathrm{SU}(4)$ is traceless. The quark's $B-L$ is minus a third of the lepton's because the lepton stands against three colours and the four entries must sum to zero. The advantage over the Standard Model is one of assumption, not of reach: the Standard Model reaches the same ratio from its field list, and the comparison section states the difference at its true size.

**The second question, which this article also answers.** Where does each of the twenty-one gauge generators go? A common summary says that the fifteen of $\mathrm{SU}(4)$ are the strong interaction and the six of the two $\mathrm{SU}(2)$'s are the weak one. Both halves of that summary are wrong, and the correction is arithmetic. Eight of the fifteen are the gluons; one is $B-L$; six are leptoquarks. Three of the six are the weak isospin the Standard Model keeps, and three belong to a factor it does not keep.

**The third question.** Does the abelian factor of the Standard Model come out of $\mathrm{SU}(4)$? Partly. The breaking supplies $\mathrm{U}(1)_{B-L}$. It does not supply $\mathrm{U}(1)_Y$. Hypercharge is a mixture of one direction from $\mathrm{SU}(4)$ and one from $\mathrm{SU}(2)_R$, and the mixture is why $B-L$ can be read as the link between the colour side and the electroweak side.

**What is claimed.** That $B-L$ is a traceless generator of $\mathrm{SU}(4)$, so its four eigenvalues on the quartet sum to zero; that this sum is exactly the quark–lepton charge relation; that the charge quantum is $e/(N-1)$, so that the third is the number of colours; that the corpus's own display $D=\operatorname{diag}(-3,1,1,1)$ is the same equation; that the trace which quantises the charge is also the row which cancels the mixed anomaly; and that the relation is a statement about a trace, not about a dynamics.

**What is not claimed.** That it explains why the electron's charge has the value it has — it does not, and no group-theoretic argument can. That it derives the charges from the algebra alone — the quartet is the declaration (A), and the trace is a property of $\mathrm{SU}(4)$, the carrier's group. That the Standard Model lacks the fact — given its field list it fixes the same ratio by anomaly cancellation, and the comparison section states what the frame's smaller assumption is worth. That the trace fixes a scale — it does not, and the section on the trace shows the invariance by scaling.

**The order.** What charge quantisation means; the trace and why it vanishes; the relation in four notations; the fate of the twenty-one generators, including the sort by what each does to the time line and the nine read as a real form; the question of the $\mathrm{U}(1)$; $B-L$ as a bridge and where the metaphor stops; the comparison with the Standard Model; what is explained and what is not; the same trace in the corpus's own language.

## What Charge Quantisation Means, Exactly

**Three statements are usually run together. This frame separates them.**

| statement | content | who gives it |
|---|---|---|
| **integrality** | every charge is an integer multiple of $e/3$ | the frame, through the relation: the denominator is the number of colours |
| **the quark–lepton relation** | $3q+\ell=0$ on the $B-L$ eigenvalues, hence $Q_p+Q_e=0$ | the frame: the trace of $B-L$ |
| **the absolute scale** | $e$ has the value it has | nobody: it is a measurement |

**Only the second is the frame's achievement, and the first follows from it.** The third is outside any group theory, and the closing ledger says so.

**Why the second is the interesting one.** A hydrogen atom's neutrality is a measured fact of extraordinary precision. In the Standard Model it is a consequence of the hypercharge assignments being what they are, and anomaly cancellation constrains those assignments without determining them. In the frame it is a consequence of one diagonal matrix being traceless, and that matrix is a generator of the group that was already there.

**Why the first is nearly free.** If $3q+\ell=0$ and $\ell$ is a multiple of $e$, then $q$ is a multiple of $e/3$. Integrality in thirds is not a separate mystery once the relation holds; it is bookkeeping.

**The quantum is set by the number of colours, and that is the content of "thirds".** For an $\mathrm{SU}(N)$ that puts one lepton beside $N-1$ colours in its fundamental, tracelessness reads

$$
(N-1)q+\ell=0\quad\Longrightarrow\quad q=-\frac{\ell}{N-1},
$$

so the quantum is $e/(N-1)$, and it is $e/3$ because there are three colours and not because of anything in a hypercharge table. Four colours would give quarters and two would give halves.

**The unit is attained, and the denominator is a count.** The four charges of one left-handed quartet are $\tfrac23$, $-\tfrac13$, $0$ and $-1$, and their differences generate exactly $\tfrac13\mathbb{Z}$ and not a sublattice of it. The denominator three is the number of entries that share the quark eigenvalue. A reader who wants to know why nature chose thirds is answered here: the lepton stands against three colours, and three is the number of dimensions the algebra supplies for them.

## The Trace, and Why It Vanishes

**The computation is one line.**

$$
\operatorname{tr}_{\mathbf4}(B-L)=\tfrac13+\tfrac13+\tfrac13-1=0 .
$$

The ordering is colour first and lepton last, so that $B-L=\operatorname{diag}\bigl(\tfrac13,\tfrac13,\tfrac13,-1\bigr)$. The same matrix in the order the corpus writes its Cartan, $(e_t,\vec e_x,\vec e_y,\vec e_z)$, is $\tfrac13 D$ with $D=\operatorname{diag}(-3,1,1,1)$, that is $(-1,\tfrac13,\tfrac13,\tfrac13)$: the lepton first and the three colours after. The two displays are one matrix read in two orders, and both are used below with the order named.

**Why it must vanish, stated three ways.**

**Generators are traceless.** Every generator of a compact semisimple group is traceless on every finite-dimensional unitary representation. $\mathrm{SU}(4)$ is semisimple, and $B-L$ is a linear combination of its Cartan generators. So the vanishing is not a numerical accident of the eigenvalue choice; it is forced by $B-L$ being a generator at all.

**Determinant one.** If $M$ generates $\mathrm{SU}(4)$, then $\exp(i\theta M)$ has determinant one for every $\theta$, and $\det\exp(i\theta M)=\exp\bigl(i\theta\operatorname{tr}M\bigr)$. So $\operatorname{tr}M=0$ follows from the determinant condition alone, with no appeal to semisimplicity. The vanishing trace is the linearisation of "determinant one", and that is the same statement in the group rather than in the algebra.

**The corpus's own display.** $D=\operatorname{diag}(-3,1,1,1)$ is traceless, $-3+1+1+1=0$, and it is the corpus's $\mathfrak{su}(4)$ Cartan element. The array "$-3$ and three ones" is "$-1$ and three thirds" multiplied by three, and the equality of the two readings is the trace.

**The step that is not automatic.** The trace vanishing says the sum of the four eigenvalues is zero. Reading it as $3q+\ell=0$ requires that the three equal entries be the quarks and the single entry be the lepton, and that is (A), the split $\mathbf4\to\mathbf3\oplus\mathbf1$ with the line identified as the lepton. The trace gives the arithmetic; the declaration gives the interpretation.

**So the claim has two halves, and neither is enough alone.** Given that the fourth direction is the lepton, the tracelessness of $B-L$ forces the quark charge to a third of it. Without the trace there is no relation; without (A) there is no quark–lepton assignment.

**What the trace does not fix, shown by scaling it.** The trace is a linear condition on the eigenvalues, so it survives $B-L\to c\,(B-L)$ for any $c$. Multiplying the array by three gives

$$
\operatorname{tr}_{\mathbf4}\bigl(3(B-L)\bigr)=1+1+1-3=0 ,
$$

with eigenvalues $(+1,+1,+1,-3)$: still traceless, still one lepton against three quarks, and with charges three times larger. So the trace fixes the ratio $q:\ell=1:-3$ and says nothing about the scale. A trace that survives rescaling is exactly the kind of statement a scale-free equation can make, and stating it here is what keeps the comparison with the Standard Model honest.

## The Relation in Four Notations

**The same equation four times, so that no reader is left with a different version.**

**In trace form.** $\operatorname{tr}_{\mathbf4}(B-L)=0$: the sum of the quartet's four $B-L$ eigenvalues vanishes.

**In eigenvalue form.** $3\cdot\tfrac13+(-1)=0$: three quarks at $+\tfrac13$ and one lepton at $-1$.

**In charge form.** The charge operator of the frame is

$$
Q=T_{3L}+T_{3R}+\tfrac12(B-L)=T_{3}+\tfrac12(B-L),
$$

with $T_{3}=T_{3L}+T_{3R}$ the total third component of weak isospin. The left-handed fields sit in the $(\mathbf4,\mathbf2,\mathbf1)$ and the right-handed in the $(\bar{\mathbf4},\mathbf1,\mathbf2)$, and the two columns below carry the physical charges of those fields, with the conjugate's sign already absorbed. Applied to the seven states of one generation, the formula gives the observed charges with nothing added.

| state | $T_{3L}$ | $T_{3R}$ | $B-L$ | $Q$ |
|---|---|---|---|---|
| ${\jmath}_L$ | $+\tfrac12$ | $0$ | $-1$ | $0$ |
| $e_L$ | $-\tfrac12$ | $0$ | $-1$ | $-1$ |
| $u_L$ | $+\tfrac12$ | $0$ | $+\tfrac13$ | $+\tfrac23$ |
| $d_L$ | $-\tfrac12$ | $0$ | $+\tfrac13$ | $-\tfrac13$ |
| $u_R$ | $0$ | $+\tfrac12$ | $+\tfrac13$ | $+\tfrac23$ |
| $d_R$ | $0$ | $-\tfrac12$ | $+\tfrac13$ | $-\tfrac13$ |
| $e_R$ | $0$ | $-\tfrac12$ | $-1$ | $-1$ |

**Computed on the proton and the electron directly.** Summing the same operator over the constituents, with each constituent contributing its own $T_3$ and its own $B-L$,

$$
Q_p=\underbrace{\tfrac12}_{T_3}+\tfrac12\underbrace{\Bigl(\tfrac13+\tfrac13+\tfrac13\Bigr)}_{B-L}=+\tfrac12+\tfrac12=+1 ,
$$

$$
Q_e=\underbrace{\Bigl(-\tfrac12\Bigr)}_{T_3}+\tfrac12\underbrace{\bigl(-1\bigr)}_{B-L}=-\tfrac12-\tfrac12=-1 ,
$$

so

$$
Q_p+Q_e=\bigl(\tfrac12-\tfrac12\bigr)+\tfrac12\bigl(1-1\bigr)=0 .
$$

**Two cancellations, and they are different cancellations.** The $T_3$ parts cancel because the proton's three quarks and the electron carry $\sum T_3=0$ between them; that is the tracelessness of $T_3$, which any $\mathrm{SU}(2)$ has. The $B-L$ parts cancel because the proton's constituents and the electron are one full quartet of $B-L$ eigenvalues, and a quartet sums to zero. The second cancellation is the trace, and it is the one the frame supplies.

**In the corpus's form.** $D=\operatorname{diag}(-3,1,1,1)$ is traceless; the eigenvalues are $-3,1,1,1$; and $-3+1+1+1=0$. Multiply by $\tfrac13$ and add the $\mathrm{SU}(2)$ piece and the Standard Model's charges appear.

**One warning about the symbols, because the equation is written twice in the literature and the two writings differ by a sign.** The relation $3q+\ell=0$ holds on the $B-L$ eigenvalues, with $q=+\tfrac13$ and $\ell=-1$. On electric charges it reads $3Q_d=Q_e$, not $3Q_d+Q_e=0$, and the passage between the two is one line: the down quark and the electron both carry $T_{3}=-\tfrac12$, so $Q=T_{3}+\tfrac12(B-L)$ gives $Q_d=-\tfrac12+\tfrac16=-\tfrac13$ and $Q_e=-\tfrac12-\tfrac12=-1$, whence $3Q_d-Q_e=0$. Both statements are true. A reader who transposes the additive form to electric charges gets $3\bigl(-\tfrac13\bigr)+(-1)=-2$ instead of $0$, and goes looking for an error in a table that has none.

**The check that the four forms agree.** Each is a rewriting of $\sum_i\eta_i=0$ with $\{\eta_i\}=\{\tfrac13,\tfrac13,\tfrac13,-1\}$. Agreement is therefore not a matter of computation but of notation, and the corpus's value is that its own $\mathfrak{su}(4)$ display already is one of the four.

## Where the Twenty-One Generators Go

**Why the ledger is in this article.** The trace is a statement about where $B-L$ sits among the twenty-one generators, and a reader who cannot place $B-L$ cannot tell why the trace is one trace and not a coincidence. The ledger is the map the trace is drawn on, and it is also the answer to the two summaries that go wrong in opposite directions: one calls fifteen generators strong, the other calls six weak.

**The arithmetic closes twice.**

$$
21=\underbrace{15}_{\mathrm{SU}(4)}+\underbrace{3}_{\mathrm{SU}(2)_L}+\underbrace{3}_{\mathrm{SU}(2)_R},
\qquad
15=\underbrace{8}_{\mathfrak{su}(3)}+\underbrace{1}_{\mathbb R\,iD}+\underbrace{6}_{\mathfrak m}.
$$

The first equation is the frame. The second is the reason the frame can break to the Standard Model.

**The ledger.** Every generator of the frame, with the factor it sits in, what it becomes, and the scale at which it does so.

| class | count | sits in | after the breaking | scale |
|---|---|---|---|---|
| gluons | $8$ | the subalgebra $\mathfrak{su}(3)\subset\mathfrak{su}(4)$ that fixes the unit line | massless and unbroken at every scale | none |
| $B-L$ | $1$ | the Cartan direction $iD$ of $\mathfrak{su}(4)$ | one of the two ingredients of hypercharge | none of its own |
| leptoquarks | $6$ | the off-diagonal block $\mathfrak m$ of $\mathfrak{su}(4)$, mixing $\mathbb C e_t$ with $B_V$ | massive, colour triplet, charge $\pm\tfrac23$ | $M_C$ |
| weak isospin | $3$ | $\mathrm{SU}(2)_L$ | $W^{\pm}$ massive, $W^3_L$ mixed into the photon and the $Z$ | $M_W$ |
| right-handed weak | $3$ | $\mathrm{SU}(2)_R$ | $W_R^{\pm}$ and $Z_R$ massive, and the neutral direction supplies $T_{3R}$ to hypercharge | $M_R$ |

The rows sum to $8+1+6+3+3=21$. The classes are disjoint **as generators of the product group**, and each is a class of generators and not of states: the three of $\mathrm{SU}(2)_R$ yield two massive states and one direction that is not a state at all but an ingredient.

**They are not disjoint as operators on the carrier, and that is the one place this ledger needs a qualifier.** $L_{\vec e_a}$ and $R_{\vec e_a}$ are traceless and skew-adjoint for $\operatorname{tr}(X^\dagger Y)$, hence elements of $\mathfrak{su}(4)$, and they are independent, so the six weak generators lie *inside* the fifteen. The carrier therefore supplies

$$
\dim_{\mathbb R}\mathfrak u(4)=16=15+1 ,
$$

and the twenty-one exists only on the formal copy the group acts on — which is why the copy is declared rather than found. Said as arithmetic: $15+6=21$ double counts, and $15+6-6=15$ is the algebra.

**And the overlap is not marginal.** Projecting a weak generator onto the block $8+1$ and onto the coset $\mathfrak m$, in the same norm, gives $\sqrt2$ and $\sqrt2$ against a total of $2$: **each weak generator is an equal superposition of a colour direction and a leptoquark direction.** So neither block equals a weak generator, and a reader who takes the six of $\mathfrak m$ for the six of the two $\mathrm{SU}(2)$'s has conflated two different sixes that are not even orthogonal.

**The common summary, and its two errors.** It is often said that the fifteen of $\mathrm{SU}(4)$ are the strong interaction and the six of the two $\mathrm{SU}(2)$'s are the weak one. Both halves are wrong, and the errors are of different kinds.

**The first error is a count.** Of the fifteen, eight are the gluons, one is $B-L$, and six are leptoquarks. Seven of the fifteen are therefore not the strong interaction, and the sentence "the fifteen are the strong interaction" overstates by seven generators. The correct sentence is exact: *eight of the fifteen are the gluons; one is $B-L$; six are leptoquarks.*

**The second error is that the six are not one object.** The six are three plus three, and the two triples are not the same object. The three of $\mathrm{SU}(2)_L$ are the weak isospin the Standard Model keeps: two of them become $W^{\pm}$ and one mixes into the photon and the $Z$. The three of $\mathrm{SU}(2)_R$ belong to a factor the Standard Model does not keep: two become $W_R^{\pm}$, and the third is not a Standard Model generator at all — it is the raw material of hypercharge, and it is paired with a direction from $\mathrm{SU}(4)$ rather than used on its own. The correct sentence is exact: *three of the six are the weak isospin; three are the right-handed weak group, of which one direction becomes part of hypercharge and two become the $W_R$.*

**What "comes from" means, and the two senses it has.** A generator can descend from a subgroup, or it can be a mixture of directions from different factors. The eight gluons descend: $\mathrm{SU}(3)$ is a subgroup of $\mathrm{SU}(4)$, unbroken at every scale. Hypercharge does not descend: it is a mixture, and the next section is about it. Keeping the two senses apart is what makes the ledger readable, because the first is a containment statement and the second is a statement about a linear combination.

**The dimension budget, and what it does and does not say.** The chain is $21\to15\to12\to9$ in dimensions and $5\to5\to4\to3$ in rank. The first step loses six and no rank, because the six leptoquarks are off-diagonal and eat no Cartan direction. The second loses three and one, the third three and one. The count of massless gauge bosons equals the dimension of the unbroken group at every stage, which is a theorem and not a dynamics: the Higgs mechanism eats exactly one Goldstone per broken generator. What the budget does not say is *which* generator goes where. That is the ledger, and the ledger is the content; the budget is the arithmetic check on it. [The Breaking Chain and the Boson Spectrum](the-breaking-chain-and-the-boson-spectrum.html) writes the budget and the spectrum, and this section writes only the bookkeeping of where each generator sits.

### The same fifteen, sorted by what they do to the time line

**A second reading of the same ledger, which the table above already implies but does not state.** The canonical split of the carrier is $\mathbb C e_t\oplus B_V$, and $e_t$ is the time unit of the algebra — the Krein norm is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$, signature $(1,3)$. So the split that identification (A) names lepton against colour is, in the algebra's own form, the **signature split**: the line is the time-like direction and $B_V$ is the space-like part. Sorting the fifteen by what they do to that line therefore sorts them by a property the corpus did not have to introduce.

| what it does to $\mathbb C e_t$ | count | which | class |
|---|---|---|---|
| annihilates it, $X e_t=0$ | $8$ | $\mathfrak{su}(3)$ | gluons |
| acts on it as a phase | $1$ | $iD$ | $B-L$ |
| moves it out of itself | $6$ | $\mathfrak m$ | leptoquarks |

$8+1+6=15$. The $8+1=9$ is the stabiliser of the line, and it is a subgroup; the $6$ is not. **Seven see the line and one of them does not move it.**

**The six split three and three, and the split is by $B-L$.** With $D=\operatorname{diag}(3i,-i,-i,-i)$,

$$
[D,E_{0i}]=4i\,E_{0i},\qquad [D,E_{i0}]=-4i\,E_{i0},
$$

so three of the six raise the line into a colour direction and three lower it back. In the normalisation where $B-L$ has eigenvalues $(-1,\tfrac13,\tfrac13,\tfrac13)$ on the quartet, the raising triple carries $B-L=+\tfrac43$ and the lowering triple $-\tfrac43$ — the leptoquark charge of $\pm\tfrac23$ once the $\mathrm{SU}(2)_R$ half is added, which is the $\pm\tfrac23$ in the table. **The $3+3$ is therefore not a relabelling: it is the particle–antiparticle pairing of the six, in the $B-L$ grading.**

**And the six leave a fingerprint on the weak pair.** Projecting $L_{\vec e_a}$ onto $\mathfrak m$ gives a norm of $\sqrt2$ out of $2$, and the projection of $R_{\vec e_a}$ onto $\mathfrak m$ is *the same vector*. Two consequences follow, and the second is the one worth keeping. First, $L_{\vec e_a}-R_{\vec e_a}$ has no leptoquark part at all — it is pure colour. Second, the six weak generators reach only a three-dimensional subspace of the six-dimensional $\mathfrak m$, so three leptoquark directions are not the leptoquark half of any weak generator.

> **What this does and does not mean.** Leptoquarks and Lorentz boosts are both "directions that mix the time line with a space line", and that is a statement about the *shape* of the generators in the same matrix algebra. It is not a statement that the leptoquarks are boosts. A boost is a spacetime transformation and the six are internal gauge directions; the coincidence is that $\mathrm{SU}(4)$ acts on four coordinates which the algebra also reads as time and space, and the physics identification of those four coordinates with colour is (A), not a theorem. The count is a bookkeeping fact about one carrier used twice.

### The nine as a real form, and the leptoquark count as a compactness count

**The same $8+1+6$ is a Cartan decomposition of one algebra in two real forms.** $\mathfrak{su}(4)$ and $\mathfrak{su}(1,3)$ — the second preserving $G=\operatorname{diag}(1,-1,-1,-1)$ — are both real forms of $\mathfrak{sl}(4,\mathbb C)$, and the split is the same on both sides:

| | preserves $\operatorname{tr}(X^\dagger Y)$ | preserves $G$ |
|---|---|---|
| $8$ gluons | yes | yes |
| $1$ $B-L$ | yes | yes |
| $6$ leptoquarks | **yes** | **no, but $i$ times them does** |

The nine are the **maximal compact subalgebra** of both, of dimension $9$; and $i\,\mathfrak m$ is the non-compact part of $\mathfrak{su}(1,3)$. The two real forms have the same dimension, $15$, the same rank, $3$, and the same maximal compact, and they differ on exactly one thing: **whether the six are compact.**

**That is the cleanest statement of the leptoquark count the corpus has, and it needs no new axiom.** The leptoquarks are the six directions that are compact in $\mathfrak{su}(4)$ and non-compact in the pseudo-unitary form. Any structure that fixes a signature on the carrier — a Krein form, a pseudo-Riemannian structure in the sense of the non-commutative-geometry literature — selects the second real form, and selecting it *is* the statement that the six are not gauged. In the language of that literature this is the object called $\beta$, and the result quoted there is that the full Pati–Salam algebra admits no such $\beta$ unless it is reduced, which removes both the six and the off-diagonal Yukawa block. **The corpus is not in a position to adopt that result**, because its finite triple fails the first-order condition and it has no unitaries to quotient; what it can state, and what this paragraph states, is the algebraic core that does not depend on any of that.

**One consequence worth naming, because it cuts both ways.** The six weak generators are in $\mathfrak{su}(4)$ but not in $\mathfrak{su}(1,3)$, and no scalar multiple of one is either: each is half block and half coset, and the $i$-rotation that maps $\mathfrak m$ into the pseudo-unitary form cannot map a mixture of the two. So a signature-fixing condition on the carrier would not spare the weak pair — which is why, in the literature where this is done, the weak generators are placed on the *other* index of a rectangular array rather than on the same four coordinates. On one $M_4(\mathbb C)$ the colour and weak actions overlap; that overlap is the price of the corpus's carrier, and the formal copy is what pays it.

## Does the $\mathrm{U}(1)$ Come From $\mathrm{SU}(4)$?

**The question is asked because the answer is "partly", and both halves of that matter.**

**What $\mathrm{SU}(4)$ supplies.** Breaking $\mathrm{SU}(4)$ to $\mathrm{SU}(3)\times\mathrm{U}(1)$ leaves one abelian factor, generated by the diagonal direction that commutes with $\mathfrak{su}(3)$ and is traceless. That direction is one-dimensional: the centraliser of $\mathfrak{su}(3)$ in $\mathfrak{su}(4)$ is spanned by $iD$ alone. So the $\mathrm{U}(1)_{B-L}$ of the intermediate stage does come out of $\mathrm{SU}(4)$, and it comes out uniquely, once the split is declared.

**What $\mathrm{SU}(4)$ does not supply.** The Standard Model's hypercharge is not that factor. It is the combination

$$
Y=T_{3R}+\tfrac12(B-L),
$$

one direction from $\mathrm{SU}(2)_R$ and one from $\mathrm{SU}(4)$, with fixed relative weight $\tfrac12$ in this normalisation. So $\mathrm{U}(1)_Y$ is contained in $\mathrm{SU}(4)\times\mathrm{SU}(2)_R$ and in neither factor alone.

**The precise form of "contained".** $\mathrm{U}(1)_Y$ is a diagonal subgroup of the product $\mathrm{U}(1)_{B-L}\times\mathrm{U}(1)_{3R}$: the one-parameter subgroup along which both phases turn together, with the parameter of the first at half the rate of the second. A diagonal subgroup is not a subgroup of either factor, which is why "hypercharge comes from $\mathrm{SU}(4)$" and "hypercharge does not come from $\mathrm{SU}(4)$" are both false as stated.

**The counting, which is the sharp form of the same statement.** Write the four generators the Standard Model keeps and ask where each one comes from.

| Standard Model generator | count | drawn from |
|---|---|---|
| $W^1_L,W^2_L,W^3_L$ | $3$ | $\mathrm{SU}(2)_L$, as a factor |
| $Y$ | $1$ | one direction of $\mathrm{SU}(2)_R$ and one of $\mathrm{SU}(4)$, mixed |

So four surviving generators draw on five frame directions: three from $\mathrm{SU}(2)_L$, one from $\mathrm{SU}(2)_R$, one from $\mathrm{SU}(4)$. The surplus direction is not an error in the count. The two neutral raw directions span a plane; $Y$ is one direction in it; the orthogonal direction in the same plane is a physical state, the $Z_R$, which becomes massive at $M_R$. The step $5\to4$ is therefore the step in which one gauge boson acquires a mass, and it happens entirely inside that plane.

**The next step is the same construction once more.** At the electroweak scale the two directions $W^3_L$ and $Y$ span a second plane; the photon is one direction in it and the $Z$ is the other. So the neutral sector is three fields in and three states out, of rank two, with one null direction. That count is a property of a sum of two rank-one matrices and holds for any couplings; [The Breaking Chain and the Boson Spectrum](the-breaking-chain-and-the-boson-spectrum.html) derives the null vector and the two masses.

**Why the distinction has to be kept.** "The $\mathrm{U}(1)$ of $\mathrm{SU}(4)$" and "the $\mathrm{U}(1)$ of the Standard Model" name two different generators. The first is $B-L$, whose boson is the fifteenth Cartan field. The second is $Y$, whose boson is a mixture. A reader who conflates them will expect the photon to be the $\mathrm{SU}(4)$ boson, and it is not: the photon is a mixture of all three neutral fields, and its coefficient on the $B-L$ direction is nonzero.

## $B-L$ as a Bridge, and Where the Metaphor Stops

**The sentence the metaphor is meant to carry.** $B-L$ is a generator that sits inside $\mathrm{SU}(4)$ beside the colour structure, and after the breaking it becomes one of the two ingredients of hypercharge, which then mixes with the weak isospin to produce the photon and the $Z$. In that sense it carries information from the colour side to the electroweak side.

**Why the metaphor is apt.** Three facts support it, and each is a statement already made above.

- Before the breaking, $B-L$ is one of the fifteen that sit with the eight gluons in one group; it is the direction that distinguishes the lepton line from the three colour lines.
- After the breaking, it is not discarded. It is paired with $T_{3R}$ to form hypercharge, and the pairing is exact, with a fixed relative weight.
- After the second breaking it is still present, as a component of the photon and of the $Z$. The $B-L$ direction enters all three neutral fields and leaves none of them.

**What the metaphor must not be taken to mean.** It is a bridge between *symmetries*, not between *forces*, and no boson sits halfway between a gluon and a $W$.

- There is no particle that mediates a "colour–electroweak" interaction. The $B-L$ boson is a real field with its own mixing, and after the breaking it is not a separate force: its direction is one ingredient of the photon, and the orthogonal combination of its plane is the $Z_R$.
- The bridge is a statement about a generator's address in a product of groups, not a statement about a fifth force. At every energy below $M_R$ the number of gauge groups is three, and none of them is called $B-L$.
- The bridge does not imply that the two sides have equal status. Colour is unbroken at every scale; the $B-L$ direction is broken as an independent factor at $M_R$.

**The precision that makes the metaphor more than a picture.** $B-L$ is sensitive to both sides, and it is the one generator that is. Quarks carry $B-L=+\tfrac13$ and leptons carry $-1$, so $B-L$ measures quark content minus lepton content. That is exactly what a bridge has to do: carry a quantity defined on both banks. And the quantity it carries is a third on one bank and a unit on the other, which is the trace again — $+\tfrac13$ three times and $-1$ once is zero, so the bridge's two ends are calibrated against each other by the same sum that quantises the charge.

**The one-sentence form, if a single sentence is wanted.** *$B-L$ is the direction the $\mathrm{SU}(4)$ breaking leaves behind, and hypercharge is that direction combined with the neutral direction of $\mathrm{SU}(2)_R$; the combination is a symmetry statement, and it is not a force of its own.*

## What the Standard Model Assumes, and What the Frame Assumes

**The section is named after the comparison it makes, and the naming is itself a correction.** An earlier form of it was called "Why the Standard Model Cannot Do This". That title was false, and the paragraph inside the section already showed it false while the title went on asserting it. The Standard Model can produce the ratio. What differs is what each theory has to be given in order to produce it, and that is the comparison this section makes.

**Two retractions, because both were one overclaim.** The earlier argument said the Standard Model's conditions are homogeneous and the trace is not. The trace is homogeneous: the array scales to $(+1,+1,+1,-3)$ and still sums to zero. And the earlier title said the Standard Model cannot get thirds. It can, as the computation below shows. What does the work in the frame is not a difference in homogeneity but that the trace's coefficients *are* the counts, three colours against one lepton, so $(N-1)q+\ell=0$ has the integer solution $q:\ell=1:-(N-1)$. A claim that rests on the wrong reason is a claim the first careful reader breaks, and losing a slogan is cheaper than losing the argument.

**What the Standard Model has, with its content assumed.** Take one family: a quark doublet in three colours at hypercharge $Y_q$, a lepton doublet at $Y_l$, the singlets $Y_u,Y_d,Y_e$, and one scalar doublet at $Y_H$, with the Yukawa couplings tying the singlets to it, $Y_u=Y_q+Y_H$, $Y_d=Y_q-Y_H$ and $Y_e=Y_l-Y_H$. The condition $\operatorname{tr}(T_{3L}^2Y)=0$ reads $\tfrac32Y_q+\tfrac12Y_l=0$ and gives $Y_l=-3Y_q$. The condition $\operatorname{tr}Y=0$ then reads $6Y_q+2Y_l-3Y_u-3Y_d-Y_e=0$, which on substituting the tie gives $Y_H=3Y_q$. And with those two the cubic condition $\operatorname{tr}Y^3=0$ is satisfied identically, for every $Y_q$. So the whole table follows from one number, and that number is fixed by the measured $e$.

**What that shows, and what the earlier count got wrong.** It shows that the Standard Model fixes the ratio: $Y_l=-3Y_q$ is $3q+\ell=0$ written in hypercharges. The earlier framing, "six unknowns against three conditions", counted the wrong way — it is not the number of equations that reduces the unknown count, it is the content. It also shows how much the content has to include: the multiplet structure of five fermion fields, the scalar's being a doublet, and the Yukawa structure that ties the singlets to it. Remove any of the three and the system has to be solved again on different assumptions.

**What the frame assumes to reach the same ratio.** One declaration, (A), which says that the fourth line of the quartet is the lepton. Nothing else. The trace then holds for every field that comes as a whole quartet, and it holds with no reference to the scalar sector: no scalar enters the argument, and no Yukawa structure does either.

**The gain, in one word and then in one sentence.** The word is parsimony. The sentence is: the frame assumes one declaration and reads one trace, the Standard Model assumes a field list and solves a small system, and both reach the same ratio. The frame does not explain more; it assumes less.

**The three places the difference is real, each stated at its true size.**

- **Robustness of the content.** In the frame, any content built from whole quartets inherits the ratio, and a new quartet can be added without disturbing the old ones, because each quartet contributes zero to the trace. In the Standard Model a new chiral field with an unknown hypercharge is a new unknown in the same system, and the solution moves.
- **Linearity, which is a gain in length and not in reach.** The frame's condition is linear with integer coefficients, so the integral solution is read off. The Standard Model's information sits partly in a cubic condition, although on this content the cubic turns out to be automatic once the linear ones are imposed. The gain is a shorter derivation, not a different prediction.
- **The unit.** Neither theory fixes $e$. The frame's advantage is that its unit is tied to the coupling of the group that contains colour, through the same embedding, and that relation is a scale-bearing statement kept in [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html). Tied to is not explained.

**What the frame still does not explain.** $\operatorname{tr}_{\mathbf4}(B-L)=0$ says the four eigenvalues sum to zero. It does not say that the lepton's is $-1$ rather than $-2$ with the quarks' $-\tfrac23$. The scale of $B-L$ is a normalisation, and the pair — the array and the weight with which it enters $Y$ — carries one physical product. The trace is blind to how that product is split. So the frame explains the ratio exactly and the scale not at all.

**The comparison in one sentence each.** *Standard Model: one scale is free, and the whole table, ratio included, is fixed once the content and the single-doublet Yukawa structure are assumed. Frame: the ratio is fixed by the trace, with nothing assumed beyond the declaration, and the scale is a split of one product.* Both sentences are about what is assumed, and neither is about explanatory reach.

## What Is Explained and What Is Not

**A four-row ledger, so that the claim cannot be inflated.**

| question | answered by | answer |
|---|---|---|
| why is $Q_p=-Q_e$? | the tracelessness of $B-L$ | because $3q+\ell=0$ |
| why is every charge a multiple of $e/3$? | the same, plus the integrality of $\ell$ | bookkeeping |
| why is the electron's charge $-1$? | the normalisation of $B-L$ | a stated convention, not a measurement |
| why is $e$ the value it is? | nothing | it is measured |

**The first row is the frame's genuine answer.** Proton–electron neutrality is a theorem in the frame and a coincidence in the Standard Model. It is the strongest claim this article makes about electromagnetic physics, and it is strong because it is small and exact.

**The third row is a convention, and which convention has to be named.** Saying "the electron has charge $-1$" is not a measurement, but it is not arbitrary either. Only the product of the array with its weight in $Y$ is physical, and the pair — the scale of $B-L$ and the coefficient in $Y=T_{3R}+c\,(B-L)$ — can be split more than one way without changing the product. The array $(\tfrac13,\tfrac13,\tfrac13,-1)$ with $c=\tfrac12$ prints one set of numbers; the array $(+1,+1,+1,-3)$ with $c=\tfrac16$ prints the same set, because the product is the same. Two different conventions, one physics. What the trace fixes is the ratio inside the array, and that is why the second row is the one with content: "the electron's charge is three times the down quark's" is printed identically by both conventions, and "$-1$" is not.

**And the scaling of the earlier section is the other case, which is why the two must not be run together.** There the weight was held and only the array was rescaled, and the charges did change. That is exactly what shows the trace is blind to the scale: it survives a change that the physics does not survive. So the trace fixes a ratio and nothing else, and the scale is fixed by the convention $c$ and by the measured $e$.

**The fourth row is outside any group theory.** $e$ is a coupling; it runs; its value at a scale is a measured input. No trace fixes it, and the frame relates it to another coupling rather than explaining it.

**What would refute the claim, so that it is a claim and not a slogan.** Three ways, and naming them is part of the argument.

- **If the fourth colour were not gauged.** The trace would still hold as algebra and would say nothing about nature. The whole content is conditional on (A), and (A) is a declaration.
- **If a fourth-colour-like resonance had the wrong $B-L$.** A state coupled to $q\bar q$ rather than to $q\ell$, or one whose $B-L$ is not proportional to $D$, would break the identification of the diagonal with $B-L$, and with it the reading of the three entries as quarks.
- **If a charge outside $\tfrac13\mathbb{Z}$ were found in the visible sector.** A state charged under a new $\mathrm{U}(1)$ that mixes kinetically with hypercharge carries a charge irrational in units of $e$, and no current measurement excludes it. That would make "every charge lies in $\tfrac13\mathbb{Z}$" false as a universal statement, and the trace a statement about one lattice rather than about all charges.

None of the three has happened, and the third is the one a future experiment could deliver.

## The Same Trace in the Corpus's Own Language

**The corpus's $\mathfrak{su}(4)$.** Its Cartan subalgebra is generated by three diagonal traceless matrices. $D=\operatorname{diag}(-3,1,1,1)$ is one of them, and its tracelessness is not a choice but the definition of $\mathfrak{su}(4)$ as a subalgebra of $\mathfrak{u}(4)$.

**What this article adds to that.** That $D$'s eigenvalue array, read as $B-L$ up to normalisation, is the one that distinguishes the fourth direction from the three, and that this reading is (A). So nothing in the algebra changes; what changes is the statement of which diagonal direction the physical $B-L$ is, and what follows from it.

**The diagonal was forced, given the split.** The centraliser of $\mathfrak{su}(3)$ in $\mathfrak{su}(4)$ is one-dimensional and is spanned by $iD$, so $D$ is the only traceless diagonal that commutes with colour: one value on the colour three-space and a different one on the lepton line. So there was no choice of which diagonal to call $B-L$, conditional on the split. The split is (A); the diagonal is forced.

**The trace that quantises the charge is the trace that cancels the anomaly.** $\operatorname{tr}_{\mathbf4}(B-L)=0$ is also the mixed row of the anomaly ledger. On the left-handed multiplet $(\mathbf4,\mathbf2,\mathbf1)$ the right-handed isospin vanishes, so $Y=\tfrac12(B-L)$; the two components of the doublet carry $T_{3L}^2=\tfrac14$ each, so their sum is $\tfrac12$; and the row is

$$
\operatorname{tr}\bigl(T_{3L}^2Y\bigr)=\tfrac12\cdot\tfrac12\operatorname{tr}_{\mathbf4}(B-L)=\tfrac14\operatorname{tr}_{\mathbf4}(B-L)=0 ,
$$

while the $(\bar{\mathbf4},\mathbf1,\mathbf2)$ contributes nothing because $T_{3L}=0$ there and no right-handed field enters this row. So the number that quantises the charge and the number that cancels the row are one number, and the row is a fixed multiple of it: the factor $\tfrac14$ is the doublet half times the weight half, and neither depends on the charges. The coincidence is not a coincidence: an anomaly coefficient is defined as a trace of the charge over the fermions in the multiplet, so a frame in which charge is quantised by a trace is a frame in which this particular row vanishes by construction. The two results are one equation read twice. [Anomalies and Anomaly Cancellation](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) computes the four rows and records that all four now hold identically.

## The Checks

| claim | check | result |
|---|---|---|
| the trace | $\tfrac13+\tfrac13+\tfrac13-1$ | $0$ |
| the relation | $3q+\ell$ at $q=\tfrac13$, $\ell=-1$ | $0$ |
| the quantum | $(N-1)q+\ell=0$ at $N=4$ | $e/3$, and the down quark attains it |
| the corpus's display | $-3+1+1+1$ | $0$ |
| the two orderings | $\tfrac13D$ against $\operatorname{diag}(\tfrac13,\tfrac13,\tfrac13,-1)$ | the same matrix, lepton first against lepton last |
| the scaling | $3\times\tfrac13$ and $3\times(-1)$ | $+1,+1,+1,-3$, still traceless |
| the centraliser | $\mathfrak z_{\mathfrak{su}(3)}(\mathfrak{su}(4))$ | one-dimensional, spanned by $iD$ |
| the generator ledger | $8+1+6+3+3$ | $21$ |
| the ledger on the carrier | $\dim\mathfrak u(4)$ against $15+1$ | $16$, so the $21$ is on the copy |
| the overlap of the two sixes | block part against coset part of $L_{\vec e_a}$ | $\sqrt2$ and $\sqrt2$ of $2$, not orthogonal |
| the shared leptoquark half | $L_{\vec e_a}$ against $R_{\vec e_a}$ on $\mathfrak m$ | the same vector; $L-R$ is pure colour |
| the time-line sort | $8+1+6$ by action on $\mathbb C e_t$ | $15$, and $8+1$ is the stabiliser |
| the $3+3$ of the six | $[D,E_{0i}]$ against $[D,E_{i0}]$ | $+4i$ against $-4i$, so $B-L=\pm\tfrac43$ |
| the two real forms | $\mathfrak{su}(4)$ against $\mathfrak{su}(1,3)$ | $15=9+6$ both, the six compact in one only |
| the first misreading | $7$ of the $15$ against $8$ gluons | $7$ is not strong |
| the second misreading | $3+3$ from the two $\mathrm{SU}(2)$'s | two different factors |
| the electroweak count | $3$ from $\mathrm{SU}(2)_L$ plus $1$ mixed | $4$ from $5$ raw directions |
| the mixed anomaly row | $\operatorname{tr}(T_{3L}^2Y)$ on $(\mathbf4,\mathbf2,\mathbf1)$ | $\tfrac14\operatorname{tr}_{\mathbf4}(B-L)=0$ |
| the electric form | $3Q_d-Q_e$ at $Q_d=-\tfrac13$, $Q_e=-1$ | $0$, both at $T_3=-\tfrac12$ |
| the bridge calibration | $+\tfrac13$ three times and $-1$ once | the trace |
| the Standard Model's system | content assumed, $\operatorname{tr}(T_{3L}^2Y)=\operatorname{tr}Y=0$ | one scale free, $Y_H=3Y_q$, cubic automatic |
| the frame's freedom | one array, trace fixed | the ratio, not the scale |

## Summary

**The relation.** $\operatorname{tr}_{\mathbf4}(B-L)=0$, so $3q+\ell=0$, so the quark's $B-L$ is minus a third of the lepton's, hence the down quark's charge is a third of the electron's, hence the proton and the electron cancel exactly.

**Why it holds.** Because $B-L$ is a generator of $\mathrm{SU}(4)$ and generators are traceless — not because the charges were chosen well.

**What it needs.** (A), to say that the single eigenvalue $-1$ is the lepton and the three $+\tfrac13$ are the quarks. The trace gives the arithmetic, the declaration gives the interpretation.

**The quantum.** The charge quantum is $e/(N-1)$, and it is $e/3$ because there are three colours; four colours would give quarters. The unit is attained, because the four charges of a quartet are $\tfrac23$, $-\tfrac13$, $0$ and $-1$, and they generate exactly $\tfrac13\mathbb{Z}$.

**The ledger.** $21=15+3+3$ and $15=8+1+6$. Eight of the fifteen are gluons, one is $B-L$, six are leptoquarks. Three of the six weak generators are the weak isospin, three are the right-handed weak group. The classes are disjoint as generators of the product, not as operators on the carrier: the six weak generators lie inside the fifteen, so the carrier supplies $16=15+1$ and the twenty-one lives on the formal copy.

**The two readings of the nine.** Sorted by what it does to the time line $\mathbb C e_t$, the fifteen is $8$ (annihilate it) $+1$ (act on it as a phase) $+6$ (move it out). The nine are the stabiliser of the line and the maximal compact subalgebra of $\mathfrak{su}(1,3)$; the six are compact in $\mathfrak{su}(4)$ and non-compact in the pseudo-unitary real form. The leptoquark count is a compactness count, and $\mathfrak{su}(4)$ and $\mathfrak{su}(1,3)$ differ on nothing else.

**The abelian factor.** The breaking supplies $\mathrm{U}(1)_{B-L}$ and not $\mathrm{U}(1)_Y$. Hypercharge is a diagonal subgroup of $\mathrm{U}(1)_{B-L}\times\mathrm{U}(1)_{3R}$, so four electroweak generators draw on five frame directions and the fifth is the $Z_R$.

**The bridge.** $B-L$ is the direction the $\mathrm{SU}(4)$ breaking leaves behind, and hypercharge is that direction combined with the neutral direction of $\mathrm{SU}(2)_R$. It is a bridge between symmetries, not between forces, and it is calibrated at both ends by the same sum: $+\tfrac13$ three times and $-1$ once.

**The comparison.** Both theories reach the ratio; the difference is the price. The Standard Model fixes the whole table, ratio included, from one scale once its field list and its single-doublet Yukawa structure are assumed. The frame fixes the ratio from one trace with nothing assumed beyond the declaration, and leaves the scale a split of one product. The gain is parsimony, not reach: neither theory fixes $e$, and neither explains the printed value of any charge.

**The limits.** The ratio is explained; the overall scale is set by a stated convention of normalisation; the value of $e$ is measured.

**The economy.** The trace that quantises the charge is the trace that cancels the mixed anomaly: the row is $\tfrac14\operatorname{tr}_{\mathbf4}(B-L)$, a fixed multiple of the same number, so one trace does two jobs.

**The corpus's form.** $D=\operatorname{diag}(-3,1,1,1)$ traceless, one-dimensional centraliser, so the diagonal was forced once the split was declared.

## Summary of Notation

| symbol | meaning |
|---|---|
| $B-L$ | baryon number minus lepton number, a Cartan generator of $\mathrm{SU}(4)$ |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the corpus's traceless diagonal, $\propto B-L$ |
| $T^{15}$ | the same Cartan normalised by $\operatorname{tr}(T^{15})^2=\tfrac12$, so $B-L=\sqrt{8/3}\,T^{15}$ |
| $q,\ell$ | the quark and lepton eigenvalues of $B-L$, $+\tfrac13$ and $-1$ |
| $N$ | the size of the fundamental, one lepton plus $N-1$ colours; $N=4$ here |
| $Y$ | $T_{3R}+\tfrac12(B-L)$, hypercharge as a combination of two factors |
| $Q$ | $T_{3L}+T_{3R}+\tfrac12(B-L)$, the electric charge |
| $\tfrac13\mathbb{Z}$ | the charge lattice, attained by the down quark's $-\tfrac13$ |
| $\mathfrak m$ | the six off-diagonal generators of $\mathfrak{su}(4)$, the leptoquark directions; equivalently the six that move $\mathbb C e_t$ out of itself |
| $\mathfrak z_{\mathfrak{su}(3)}(\mathfrak{su}(4))$ | the centraliser of the colour subalgebra, one-dimensional |

## Further Reading

- [The Four Colours Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-four-colours-left-right-model.html). The group, the sixteen, the declaration (A), and $15=8+1+6$ with $D=\operatorname{diag}(-3,1,1,1)$.
- [The Breaking Chain and the Boson Spectrum: One Flag, Three Scales, Twenty-One Bosons](the-breaking-chain-and-the-boson-spectrum.html). The budget $21\to15\to12\to9$, the rank budget, the neutral mass matrix and the photon as its null vector.
- [The Electroweak Gauge Group and the Hypercharge Assignment](the-electroweak-gauge-group-and-the-hypercharge-assignment.html). The anomaly system solved in full, the three rays, and the discrete choice among them.
- [Anomalies and Anomaly Cancellation in the Four Colours Left–Right Model](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html). The four hypercharge rows, all satisfied identically on the sixteen.
- [Quantum Chromodynamics as the Residual of $\mathrm{SU}(4)$](quantum-chromodynamics-in-the-biquaternion-framework-the-dimension-ceiling-and-the-colour-wall.html). Why the eight are unbroken at every scale.
- [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html). The mixture that survives the chain, before the two vacua are imposed.
- [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html). The matching relations and the scale-bearing statements this article does not print.

**The traps.** Do not say "charge quantisation is derived" without the two clauses: the ratio is, the scale is not. Do not drop (A): the trace alone gives no quark–lepton assignment. Do not read the third and fourth rows of the four-row ledger as failures of the frame; they are outside any group theory, and the Standard Model does not answer them either. Do not say the trace is "not homogeneous": it is homogeneous, and what does the work is that its coefficients are the integer counts and that the normalisation is fixed by the embedding. Do not say "the fifteen are the strong interaction": seven of the fifteen are not gluons. Do not say "the six are the weak interaction": they are two triples from two factors, and only one of the six triples is the weak isospin the Standard Model keeps. Do not say "hypercharge comes from $\mathrm{SU}(4)$": the breaking supplies $B-L$, and hypercharge is a mixture of that with one direction of $\mathrm{SU}(2)_R$. Do not say "the Standard Model cannot get thirds": it gets them from its field list, and this article's claim is that the frame gets them from less. Do not write $3Q_d+Q_e=0$ for electric charges: the additive form holds on the $B-L$ eigenvalues, and on electric charges the relation is $3Q_d=Q_e$. Do not call the electron's charge arbitrary: it is fixed by a normalisation convention, and a convention that is stated is not the same thing as no answer.
