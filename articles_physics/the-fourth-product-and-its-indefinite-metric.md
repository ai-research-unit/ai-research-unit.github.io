# __The Fourth Product and Its Indefinite Metric__

## Introduction

A quantum theory that insists on a local, covariant description of a gauge field pays for it with an **indefinite metric**. In the Gupta–Bleuler treatment of electromagnetism the four components of the potential are kept, the unphysical ones are given negative or zero squared length, and the physical states are cut out afterwards by a subsidiary condition; in the BRST treatment of a non-abelian gauge theory the same price is paid, and the physical state space is a cohomology rather than a subspace. Every such theory therefore needs a pairing that is Hermitian, non-degenerate and **not** positive. This article is about where that pairing comes from in the biquaternion framework, and the answer is one algebraic operation: the insertion of the **natural quaternion conjugation** ${}^{\natural}$ into the first slot of the probability (sesquilinear) product. The product that results is the fourth of the framework's four general products, and its scalar form is an indefinite Hermitian form of signature $(1,3)$ — **one positive direction and three negative ones**, the sign vector $\varepsilon=(1,-1,-1,-1)$.

The article has three objects. The first is the fourth product itself and the sense in which it is the gauge corner of the four. The second is its indefinite metric, the **Krein form** $K$, its signature, and the fact — the physics of the article — that on a material four-vector this form is the **Minkowski metric** with one positive time direction and three negative space directions, while on an informational element it is the same signature carried by the scalar direction. The third is the reading, offered as a **labelled hypothesis**, that the single positive direction is the classical (commuting, $c$-number) direction of the algebra and the three negative directions are its quantum ones.

The article keeps to its own product. It defers the classification of Hermitian forms by inertia and Sylvester's law to *Inertia and the Witt Invariant: What a Signature Allows a Spectrum to Carry*; the positivity of the probability form, which is what keeps the framework free of ghosts, to *Mass, Rank and the Positivity of the Dagger*; the states that the indefinite metric cannot normalise to *The States the Indefinite Metric Cannot Normalise*; the map of all four general products and their jobs to *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*; and the mathematics to the mathematics articles *The Krein Gram Matrix and the Restrictions of the Form*, *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* and *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*.

**Conventions.** As in the companion articles of this block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0=1$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with complex coefficients $Q_\mu=q_\mu+iq'_\mu$. The conjugations are the natural one $\tilde Q^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$, the coefficientwise one $\bar{\tilde Q}=\sum_\mu\bar Q_\mu e_\mu$, and the star $\tilde Q^{*}=\bar{\tilde Q}^{\natural}$. The scalar part is $\mathrm{Sc}(\tilde X)=X_0$ and the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$. The sectors are $\mathbb{M}_+=\{\tilde Q^{*}=\tilde Q\}$ (informational) and $\mathbb{M}_-=\{\tilde Q^{\flat}=\tilde Q\}$ (material), with $\flat=-{}^{*}$; the centre is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ and the vector subspace is $\mathrm{Vect}(\mathbb{B})=\{Q_0=0\}$. The sign vector is $\varepsilon=(1,-1,-1,-1)$. The $2\times2$ model is $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, with $\Phi(\tilde Q^{\natural})=\operatorname{adj}\Phi(\tilde Q)$ and $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$. All conventions are those of *Conventions in the Biquaternion Universe*.

## What a Gauge Theory Needs from Its Metric

The physical demand is worth stating before the algebra, because it is what the fourth product answers.

**A gauge field has more components than physical polarisations.** The four-potential $A_\mu$ of electromagnetism carries four real functions, but a massless vector particle has two polarisations; the two extra components are removed by a gauge choice, and the removal cannot be done locally and covariantly without cost. Gupta and Bleuler kept all four components, quantised them with the wrong-sign commutator for the timelike one, and recovered the physical theory by demanding that the physical states satisfy a subsidiary condition; the unphysical components then have **negative or zero squared length** in the inner product the theory carries. The same structure reappears in the BRST treatment of a non-abelian gauge theory: a gauge-fixing term with an indefinite metric, and a physical state space recovered as the cohomology of a nilpotent operator rather than as a positive subspace.

**An indefinite metric is therefore a standard object of gauge physics, not a pathology.** The point of the Gupta–Bleuler construction is that the covariant description is worth a metric with a negative part; positivity is recovered at the level of the physical subspace, not at the level of the covariant state space.

**A second, independent appearance.** A Lie algebra carries an invariant bilinear form, its Killing form. The Killing form of a **compact** group is negative definite, that of a non-compact group is indefinite; the compact directions and the non-compact directions are separated by the sign. The internal symmetry group of the framework is the compact $U(2)$, and the boosts form a non-compact family, so a sign split in an invariant form of the algebra is exactly the kind of object that distinguishes the compact from the non-compact part of a symmetry.

Both structures — the indefinite metric of a covariant gauge, and the sign split of an invariant form — are pairs of a Hermitian form with a signature. The framework's fourth product supplies one such form from its own data, and the rest of the article computes it.

## The Fourth Product

### The Four General Products and Their Two Slots

The four general products of the biquaternion space are the four ways of inserting a conjugation into each slot of the plain product: the identity or ${}^{\natural}$ in the first slot, the identity or ${}^{*}$ in the second. Written by their slots, they are the plain product $\tilde P\tilde Q$, the quaternionic product $\tilde P^{\natural}\tilde Q$, the sesquilinear product $\tilde P\tilde Q^{*}$, and the **general quaternionic sesquilinear product**

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*},
$$

the plain product with both conjugations inserted. Two rules govern the grid. The **second slot decides geometry against statistics**: a product without the star is $\mathbb{C}$-bilinear and its scalar form is a metric, a product with the star is conjugate-linear in that slot and its scalar form is a Hermitian pairing. The **first slot decides definite against signed**: inserting ${}^{\natural}$ into the first slot is the one operation that gives the scalar form a signature, in either row.

The fourth product is therefore the sesquilinear (probability) row read through ${}^{\natural}$, and the framework's grouping assigns it the fourth physical job: the plain product is **composition**, the quaternionic product is **causality** through the interval it squares to, the sesquilinear product is **probability** through its positive definite form, and the general quaternionic sesquilinear product is **gauge** through its indefinite form. The grouping is the framework's, and it is labelled as a reading; the map of the four is *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*, and it is cited here, not restated.

### The Rule and the Scalar Part

The product is additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, and its scalar part is the form the block is about:

$$
\mathrm{Sc}\bigl(\tilde P\star\tilde Q\bigr)
=\mathrm{Sc}\bigl(\tilde P^{\natural}\tilde Q^{*}\bigr)
=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu\overline{Q_\mu}
=K(\tilde P,\tilde Q).
$$

$K$ is Hermitian, $\overline{K(\tilde P,\tilde Q)}=K(\tilde Q,\tilde P)$, non-degenerate, and **indefinite**. This product is not the derived operation of the algebra with its involution — it has no unit on either side. The two one-sided actions of $e_0$ are the two conjugations themselves,

$$
e_0\star\tilde Q=\tilde Q^{*},\qquad \tilde Q\star e_0=\tilde Q^{\natural},
$$

and the star of a product reverses the order without exchanging the slots, $(\tilde P\star\tilde Q)^{*}=\tilde Q\overline{\tilde P}$. The absence of a unit and the non-associativity are the two properties the closing article of the block reads; here they are only recorded.

### The Metric and Its Signature

The form is diagonal in the coefficient basis with the signs of $\varepsilon$:

$$
K(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu\lvert Q_\mu\rvert^{2}
=\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2}.
$$

Read on the eight real basis elements $e_\mu$ and $ie_\mu$, the diagonal is

| basis element | $e_0$ | $ie_0$ | $e_1$ | $ie_1$ | $e_2$ | $ie_2$ | $e_3$ | $ie_3$ |
|---|---|---|---|---|---|---|---|---|
| $K$ | $+1$ | $+1$ | $-1$ | $-1$ | $-1$ | $-1$ | $-1$ | $-1$ |

so the form is positive on exactly two real directions, those spanning the **centre**, and negative on the other six, those spanning the **vector subspace**. The algebra therefore splits into a positive part and a negative part, orthogonal for the form,

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B}),
\qquad
K\bigl(\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B})\bigr)=0,
$$

the **fundamental decomposition** that makes $(\mathbb{B},K)$ an indefinite inner product space: a Krein space, and since the negative part is finite-dimensional a Pontryagin space over $\mathbb{R}$. The inertia is

$$
(1,3)\ \text{over the complex coefficients},\qquad (2,6)\ \text{over the eight real parameters},
$$

with signature $p-q=-2$ in the complex counting. The isometry group of $K$ is $U(1,3)$, of real dimension sixteen; the isometry group of its realification is the larger real orthogonal group $O(2,6)$, of real dimension twenty-eight. The involution that relates $K$ to the positive definite form is the natural conjugation itself, $J={}^{\natural}$, with $J^{2}=\mathrm{id}$, the **fundamental symmetry** of the indefinite metric; in the matrix model it is the adjugation, $\Phi(\tilde Q^{\natural})=\operatorname{adj}\Phi(\tilde Q)$. The general theory of the fundamental decomposition, the negative index and the Pontryagin type is *Krein Spaces* and *Pontryagin Spaces*; the form, its inertia and its null set are proved in *The Krein Gram Matrix and the Restrictions of the Form*, and the isometry group and the adjugation in *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation*.

### The Metric Is Not the Interval, and Is Its Negative on Matter

The framework already carries an indefinite pairing of signature $(3,1)$ on the material sector — the interval — and it is worth separating the two, because they are read by different products and their signs differ.

Let $\tilde T=ict\,e_0+\mathbf x$ be a material four-vector, $\mathbf x=(x,y,z)$. The biquaternion norm, read by the quaternionic product, is the interval,

$$
N(\tilde T)=\mathrm{Sc}\bigl(\tilde T^{\natural}\tilde T\bigr)=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2}
=-c^{2}t^{2}+x^{2}+y^{2}+z^{2},
$$

of signature $(3,1)$ on the material sector, the one positive direction being the spatial block. The form of the present article is its **negative** on that sector:

$$
K(\tilde T,\tilde T)=c^{2}t^{2}-x^{2}-y^{2}-z^{2}=-N(\tilde T),\qquad \tilde T\in\mathbb{M}_-.
$$

On the informational sector the two agree, $K=+N$ on $\mathbb{M}_+$. The pair of identities

$$
K=\begin{cases}+N,& \tilde Q\in\mathbb{M}_+,\\[2pt] -N,& \tilde Q\in\mathbb{M}_-\end{cases}
$$

is the **Lagrange identity** of the block, and it is the algebraic statement that the fourth product's metric and the interval differ by the sign of the sector. The classification that makes the inertia the only invariant of a Hermitian form is *Inertia and the Witt Invariant: What a Signature Allows a Spectrum to Carry*; it is cited, not re-proved.

## The Physical Object: The Gauge Metric

The form $K$ is the invariant pairing of the fourth product, and its signature is what the block reads physically.

**The sign vector is the Minkowski sign vector.** On the material sector the identity $K=-N$ gives

$$
K(\tilde T,\tilde T)=c^{2}t^{2}-x^{2}-y^{2}-z^{2},
$$

which is the Minkowski metric in the convention with **one positive time direction and three negative space directions**. The indefinite metric of the fourth product, read on the four-vectors of the framework, is therefore not an exotic construction: it is the spacetime metric with the opposite overall sign to the interval, the familiar $(+,-,-,-)$ signature, and the sign vector $\varepsilon=(1,-1,-1,-1)$ is read as the sign of time against the sign of space.

**The same signature, carried by the scalar direction.** On the informational sector the identity $K=+N$ gives the same signature $(1,3)$, the positive direction being now the real scalar direction $e_0$ and the negative directions the three $ie_k$ of the vector part. The two sectors therefore carry the same indefinite signature on different carriers: on the material sector the metric is the spacetime metric, on the informational one it is the metric of the operator space, and the two agree in inertia.

**The reading of the one positive direction.** The single positive direction of $K$ is the centre — the commuting, scalar, $c$-number direction of the algebra, which is the central phase $e^{i\theta}$ and the real scalar; the three negative directions are the vector part, where the multiplication does not commute. The physical reading, offered as a **labelled hypothesis**, is that this sign split is a split between one **classical** direction and three **quantum** ones: the classical direction is the commuting one, which carries no internal quantum number, and the three negative directions are the non-commuting ones that do. The passage from the positive definite form $H$ of the probability block to the indefinite form $K$ is then read as the passage from a signless pairing to a pairing with a classical–quantum split, which is what a metric on an internal space does. The reading is a hypothesis: the sign of a form is not by itself a statement about classicality, and the article says so in its ledger.

**The background–quantum division.** The split can be named more sharply than by the words classical and quantum, and the sharper name is the one the corpus uses elsewhere. The two positive directions are the two **$c$-number** directions of the algebra, the real scalar direction $e_0$ and the central imaginary $ie_0$, which together carry the complex amplitude of the centre, the central imaginary being the generator of the global phase. The six negative directions are the **$q$-number** part, the vector subspace, where the multiplication does not commute and where the internal quantum numbers live. The passage from the positive definite form $H$ to the indefinite form $K$ is then read as the passage from an all-numeric pairing to the pairing of a **background-field** description, in which a classical amplitude and phase have been separated from a quantum rest — the shape of a semiclassical expansion, the centre playing the background and the vector part the fluctuation. The reading sharpens the classical–quantum hypothesis above and shares its label: the sign of the form is not derived from the separation, and the article does not claim that the centre is classical **because** $K$ is positive there.

**Why the same object can be read as gauge.** The Killing form of a symmetry algebra separates its compact from its non-compact directions by sign. The fourth product's metric does exactly that on the algebra: the positive part is the centre (the abelian, commuting direction) and the negative part is the vector subspace. Read with the internal group of the framework, the positive complex direction is the abelian $U(1)$ direction of the central phase and the three negative ones are the three non-abelian directions. The pairing that a covariant gauge theory needs is thus supplied by the fourth product, and its sign structure is read as the compact/non-compact split of the internal symmetry. The group itself is *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*.

**The internal ruler of the frame.** The form $K$ is the ruler of the internal frame, and two groups are read on it that must be kept apart. The **isometry group** of the form, in the standard linear sense, is $U(1,3)$, of real dimension sixteen — the full group of linear maps that leave $K$ alone. The **acting group** of the framework is much smaller: it is the group of **inner** isometries, the conjugations $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ by a unitary element, and because the central phase acts trivially the acting group is $PU(2)\cong SO(3)$, of real dimension three. The compact part of the ruler rotates the internal frame and the non-compact part boosts it, and only the compact inner part acts on the framework's fields. The distinction is *Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem*, and the intrinsic compact group of the algebra is *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*. The article records the reading and does not identify a gauge group with the full isometry group $U(1,3)$.

## A Worked Case: One Four-Vector in Four Forms

One element settles the arithmetic, and it is worth writing out because the four signs are easy to confuse. Take the material four-vector with $ct=3$ and $\mathbf x=e_1$, that is $\tilde T=3i\,e_0+e_1$.

| form | read by | value at $\tilde T$ |
|---|---|---|
| $N(\tilde T,\tilde T)$, the interval | the quaternionic product | $-9+1=-8$ |
| $K(\tilde T,\tilde T)$, the gauge metric | the fourth product | $+9-1=+8$ |
| $B(\tilde T,\tilde T)$, the plain scalar product | the plain product | $-9-1=-10$ |
| $H(\tilde T,\tilde T)$, the probability form | the sesquilinear product | $+9+1=+10$ |

The numbers carry four statements. The **interval** is negative, so the four-vector is timelike and massive, with $m^{2}c^{2}=8$ in these units; the interval is the quantity the mass shell is the level set of. The **gauge metric** is its negative, $K=-N$, and is therefore the Minkowski form with the time direction positive. The **plain scalar product** is the negative Euclidean square, $-(c^{2}t^{2}+\mathbf x^{2})$, of signature $(0,4)$ on the material sector — it has no cone and so cannot be a metric. And the **probability form** is the Euclidean square, positive definite, which is why the states live with it and not with $K$. The same four-vector, in other words, is measured by four pairings with four different meanings, and only the fourth product's gives the spacetime sign convention.

**One more value, the informational one.** Take $\tilde H=2e_0+i(e_1+e_2+e_3)$ in the informational sector. Then $N(\tilde H)=4-3=1$ and $K(\tilde H)=4-3=1$, the Lagrange identity $K=+N$ on $\mathbb{M}_+$; the signature is again $(1,3)$, the positive direction the scalar one, and the element is of norm one, so it is a unit of the algebra rather than a zero divisor. The metre that reads a material four-vector and the metre that reads an informational element are the same metric read on the two sectors, and the sign of the sector is the whole difference.

## The Reading: An Indefinite Metric for the Gauge Corner

The four general products are assigned four jobs, and the fourth job is gauge. The reading of this article is that the assignment is carried by the metric: the fourth product is the corner of the grid whose scalar form has a **signature** rather than a sign, and a signature is what a gauge structure needs — an invariant pairing with a compact and a non-compact part, a definite form for the states and an indefinite one for the transformations.

Two facts fix the reading's limits. The first is that the framework's **state space is not carried by $K$**. The positivity of the probability form $H$ is proved in *Mass, Rank and the Positivity of the Dagger*, and it is what excludes ghosts; the indefinite metric is the gauge-side pairing, and the framework does not quantise with it. The second is that the sign split and the sector split are **different decompositions of the same algebra**: $K$'s fundamental decomposition cuts by the coefficient index into the centre and the vector subspace, while the material–informational split cuts by the involution ${}^{*}$ into two four-dimensional halves. The two cross, each sector taking one coefficient direction from the centre and three from the vector subspace, and the sign of $K$ is a statement about the first decomposition and not directly about the second. Whether the positive centre of $K$, the sector split and the centre-as-classical reading are one structure or three is not settled by the algebra, and it is recorded as open.

### Named Readings of the Metric

Six further readings of the same metric are recorded here, each under a name of its own, so that a reading can be cited without being confused with a theorem. Each is labelled a reading rather than a theorem; where a name rests on an identity of the body, the identity is the body's and the name adds only the reading. Several of them read the same signs as the classical–quantum hypothesis of the Ledger: they are distinct names for distinct questions — what the directions of $K$ are *ordered* by, what the fundamental symmetry *is*, what the two forms *compare* — and whether those readings are one structure or several is the open item the article already records.

- **Gauge calibration.** $K$ is the calibration form of the internal frame: it fixes the comparison of the eight internal directions, their relative signs and their relative phase, and an isometry of $K$ leaves the calibration unchanged, exactly as a change of gauge leaves the physical content of a frame unchanged. The name separates the *calibration* role of the form from its *ruler* role, which the Ledger records: the ruler measures; the calibration fixes the comparison. The boundary is that no field, no coupling and no measured calibration stand behind the name.
- **Internal signature clock.** The **two** positive directions of $K$ — the centre, of real dimension two — are read as an **internal time** and the six negative directions of the vector subspace as **internal space**, so that the inertia $(2,6)$ over the real parameters fixes a time-versus-space character inside the frame. The reading is the internal counterpart of the sign-of-time reading of the interval on the material sector, and it is offered as such; the caution is that the internal time has no external clock and no ordering, and the sign is a fact about one form.
- **Adjugative parity.** The fundamental symmetry $J={}^{\natural}$ is the adjugation in the matrix model, and the adjugation is an involution of the algebra; read physically, $J$ is a **generalised internal parity** that splits the frame into its $J$-even and $J$-odd parts and pairs an element with its natural conjugate. The boundary is the corpus's: $J$ is an algebraic involution, and the identification with a spacetime parity is *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form* and not this article.
- **Relational origin.** The product has no unit on either side, $e_0\star\tilde Q=\tilde Q^{*}$ and $\tilde Q\star e_0=\tilde Q^{\natural}$, so no element of the frame plays the part of a neutral origin and the group-like structure is a structure of **differences**. Read as a physics statement, what the calibration of the frame fixes is the relation between two elements and not the absolute position of either; the origin is not a point of the algebra but a choice of frame. The name belongs to this article, and the positive companion statement is the composition of the one-sided actions, the sandwich of *Why the Fourth Product Is a Gauge Structure and Not a State Space*.
- **Adjugation passage.** The passage from the definite form $H$ to the indefinite form $K$ is the insertion of the natural conjugation in the first slot, $K(\tilde P,\tilde Q)=H(\tilde P^{\natural},\tilde Q)$, so the generator of the passage is the **adjugation** ${}^{\natural}$ and not the central imaginary. Multiplying an element by $i$ leaves the general quaternionic sesquilinear form unchanged, $K(i\tilde P,i\tilde Q)=K(\tilde P,\tilde Q)$, and so cannot rotate the sign vector $\varepsilon$; the name is given for the passage that the Ledger's dial records. **Caution, and a word avoided:** this passage is *not* the **Wick rotation** of *The Wick Rotation in the Biquaternion Universe*, which is the substitution $t\mapsto-i\tau$ and the identification $\mathbb{M}_-\leftrightarrow\mathbb{H}_{\mathbb{B}}$ between the Lorentzian and the Euclidean descriptions; the two are different constructions on the same algebra, and the capitalised word is not used here for the definite-to-indefinite passage.
- **Gupta–Bleuler pattern.** Every pure state is **null** for $K$, so the indefinite form cannot normalise a state; the fundamental symmetry $J={}^{\natural}$ is then the **metric/ghost-parity operator** of an indefinite-metric theory, with $J^{2}=1$ and $J^{*}=J$ (*Inertia and the Witt Invariant*), splitting the frame into a positive and a negative part. Read physically, this is the **Gupta–Bleuler** pattern: the physical subspace is selected by the **gauge condition** and is only **semi-definite**, containing the null states the condition allows, not the positive-definite part alone, while the negative part is the gauge redundancy. The name is labelled, and its boundary is the article's own: the algebra supplies the indefinite form and the fundamental symmetry, and it does not supply the gauge condition that fixes the physical subspace, nor does the framework quantise with $K$ — the no-ghost statement runs through $H$.

## The Limits

- The indefinite metric is not the state-space inner product of the framework; the state space is the positive cone carried by the sesquilinear product and by $H$, and the no-ghost statement is *Mass, Rank and the Positivity of the Dagger*.
- The sign split of $K$ is a fact about one form. The reading of the positive direction as the classical one and the negative directions as the quantum ones is a **labelled hypothesis**, not a theorem, and it is not derived from the metric sign.
- That $K$ is a Krein form, that a Krein space is the setting of an indefinite-metric quantum theory, and the inertia $(1,3)/(2,6)$ are standard and cited to *The Krein Gram Matrix and the Restrictions of the Form*; they are not proved here.
- The assignment of the fourth job to the fourth product is the framework's grouping, labelled as a reading in *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*; the article does not claim that a gauge theory is derived.
- The passage from the definite form to the indefinite one is the insertion of the natural conjugation, $K(\tilde P,\tilde Q)=H(\tilde P^{\natural},\tilde Q)$, named the **adjugation passage**; it is *not* the **Wick rotation** of *The Wick Rotation in the Biquaternion Universe*, and the word is not used here for it.

## The Ledger

**Proved, and recomputed.** The fourth product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$, additive, $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, with scalar part $\mathrm{Sc}(\tilde P\star\tilde Q)=K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, Hermitian, non-degenerate and indefinite. The diagonal $K(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2}$; the eight real signs $+1,+1,-1,-1,-1,-1,-1,-1$; the positive part is the centre (real dimension two), the negative part the vector subspace (real dimension six), and the two are orthogonal; the inertia $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$; the isometry group $U(1,3)$ of real dimension sixteen, with the realified form isometric under the larger $O(2,6)$ of real dimension twenty-eight; the fundamental symmetry $J={}^{\natural}$ as the adjugation. The two one-sided actions $e_0\star\tilde Q=\tilde Q^{*}$ and $\tilde Q\star e_0=\tilde Q^{\natural}$, so no unit on either side; the star of a product $(\tilde P\star\tilde Q)^{*}=\tilde Q\overline{\tilde P}$. The Lagrange identities $K=+N$ on $\mathbb{M}_+$ and $K=-N$ on $\mathbb{M}_-$, and the single four-vector $\tilde T=3i\,e_0+e_1$ with $N=-8$, $K=+8$, $B=-10$ and $H=+10$. Recomputed in a companion note and reproduced from *The Krein Gram Matrix and the Restrictions of the Form*, *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* and *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*.

**Standard identification.** That $K$ is a Krein form, that the fundamental decomposition makes the space a Pontryagin space of type $\Pi_6$ over $\mathbb{R}$, and that an indefinite-metric theory is the standard setting of a covariant gauge.

**Reading, labelled.** That the fourth product is the gauge corner of the four, its metric the invariant indefinite pairing, and the sign vector the sign of time against the sign of space on the material sector; and that $K$ is the ruler of the internal frame, whose full isometry group $U(1,3)$ is to be kept apart from the acting inner group $PU(2)\cong SO(3)$. Five further readings, each named in §*Named Readings of the Metric* and each labelled: **gauge calibration** (the form fixes the relative scale and phase of the frame), **internal signature clock** (two internal time directions, six internal space directions), **adjugative parity** (the fundamental symmetry $J={}^{\natural}$ read as a generalised internal parity), **relational origin** (no unit, so only differences are calibrated), and **adjugation passage** (the definite-to-indefinite passage $K(\tilde P,\tilde Q)=H(\tilde P^{\natural},\tilde Q)$, generated by ${}^{\natural}$ and *not* the Wick rotation).

**Hypothesis, labelled.** That the single positive direction of $K$ is the classical direction of the algebra and the three negative ones the quantum directions, so that the passage $H\to K$ installs a classical–quantum split in the metric; and, in the sharper form of the same hypothesis, that the two positive directions are the $c$-number amplitude and phase, the six negative ones the $q$-number rest, and the passage $H\to K$ the pairing of a background-field description.

**Not claimed.** That the metric sign derives a classical–quantum divide; that the sign split is the material–informational split; that the framework quantises with $K$; that the inertia classification is proved here.

**Open.** Whether the positive centre of $K$, the sector split and the centre-as-classical reading are one structure or three; what the physical carrier of the classical direction is.

## Summary

The fourth of the framework's four general products is the general quaternionic sesquilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$, the plain product with the natural conjugation in the first slot and the star in the second. It is the sesquilinear row of the grid of the four general products read through ${}^{\natural}$, and it is the corner whose scalar form is **indefinite**: the **Krein form** $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, Hermitian, non-degenerate, with sign vector $\varepsilon=(1,-1,-1,-1)$, diagonal $\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2}$ and inertia $(1,3)$ over the complex coefficients and $(2,6)$ over the real parameters. Its positive part is the centre, of real dimension two, its negative part the vector subspace, of real dimension six, and the two are orthogonal: the fundamental decomposition that makes the algebra a Krein space. The isometry group is $U(1,3)$ and the fundamental symmetry the natural conjugation ${}^\natural$, the adjugation in the matrix model. Physically the article reads this as the **gauge metric** of the fourth corner: on a material four-vector the identity $K=-N$ makes it the Minkowski metric $c^{2}t^{2}-x^{2}-y^{2}-z^{2}$ with one positive time direction and three negative space directions, on an informational element the identity $K=+N$ gives the same signature carried by the scalar direction, and the sign split of the form is read — as a **labelled hypothesis** — as a split between one classical, commuting direction and three quantum ones. Five further readings of the same metric are named and labelled in §*Named Readings of the Metric*: **gauge calibration**, **internal signature clock**, **adjugative parity**, **relational origin** and **adjugation passage**. The framework does not quantise with this metric: the state space remains the positive cone carried by the sesquilinear product and its form $H$, whose positivity is *Mass, Rank and the Positivity of the Dagger*. The classification of forms by inertia is *Inertia and the Witt Invariant*; the states the indefinite metric cannot normalise are *The States the Indefinite Metric Cannot Normalise*, which follows; the map of the four general products is *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*; and the mathematics is *The Krein Gram Matrix and the Restrictions of the Form*, *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* and *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ | the fourth product; the gauge corner |
| $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the indefinite (Krein) metric of the fourth product |
| $K(\tilde Q,\tilde Q)=\lvert Q_0\rvert^{2}-\lvert\mathbf Q\rvert^{2}$ | the diagonal of the metric; the Krein invariant |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector; the metric's signs |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | the centre; the positive part of the metric |
| $\mathrm{Vect}(\mathbb{B})=\{Q_0=0\}$ | the vector subspace; the negative part of the metric |
| $(1,3)$ over $\mathbb{C}$, $(2,6)$ over $\mathbb{R}$ | the inertia and the real signature |
| $U(1,3)$, $O(2,6)$ | the isometry group of $K$, and the larger isometry group of its realification |
| $J={}^{\natural}$ | the fundamental symmetry; the adjugation in the matrix model |
| $K=\pm N$ on $\mathbb{M}_\pm$ | the Lagrange identities ($+$ informational, $-$ material) |
| $N(\tilde Q)=\tilde Q^{\natural}\tilde Q$ | the biquaternion norm; the interval on $\mathbb{M}_-$ |
| $B, H$ | the plain scalar form and the positive definite (probability) form |
| $\mathbb{M}_+,\mathbb{M}_-$ | the informational and material sectors |

## Further Reading

- Mathematics article *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form, its fundamental decomposition, its inertia, its null set and the Lagrange identities.
- Mathematics article *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-representation.md`), for the inertia $(1,3)/(2,6)$, the fundamental symmetry as adjugation and the isometry group $U(1,3)$.
- Mathematics article *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its two one-sided actions and the absence of a unit.
- Mathematics articles *Krein Spaces* (`articles_maths/krein-spaces.md`) and *Pontryagin Spaces* (`articles_maths/pontryagin-spaces.md`), for the fundamental decomposition, the negative index and the completeness in a fundamental symmetry.
- Mathematics article *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the involution that turns the Krein form into the Hermitian one.
- Mathematics article *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the restriction of $K$ to the six distinguished subspaces.
- Companion article *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*, for the map of the four general products and the placement of this one.
- Companion article *Inertia and the Witt Invariant: What a Signature Allows a Spectrum to Carry*, for the classification of Hermitian forms by inertia, Sylvester's law and the Witt group.
- Companion article *Mass, Rank and the Positivity of the Dagger*, for the positivity of the probability form and the absence of ghosts.
- Companion article *The States the Indefinite Metric Cannot Normalise*, which reads the states on the null cone of this metric.
- Companion article *Why the Fourth Product Is a Gauge Structure and Not a State Space*, which closes the block with the failure of the state-space property.
- Companion article *The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)*, for the internal group whose compact and non-compact directions the sign split distinguishes.
- Companion article *The Wick Rotation in the Biquaternion Universe* (`articles_physics/the-wick-rotation-in-the-biquaternion-universe.md`), named only so that the **adjugation passage** is not read as a Wick rotation.
- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the standard theory of an indefinite inner product and its fundamental decomposition.
