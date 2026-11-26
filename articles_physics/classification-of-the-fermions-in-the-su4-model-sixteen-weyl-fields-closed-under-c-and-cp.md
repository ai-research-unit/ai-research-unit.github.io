# __Classification of the Fermions in the $\mathrm{SU}(4)$ Model: One Generation, Sixteen Weyl Fields, Thirty-Two States, Closed Under $C$ and Under $CP$__

## Introduction

**The question.** The bosons fill the cells of the grid. Do the fermions fill them too, how many are there, and what happens to a fermion under charge conjugation?

**The answer.**

$$
2\cdot\underbrace{\mathbf4}_{\text{quartet}}+2\cdot\underbrace{\bar{\mathbf4}}_{\text{antiquartet}}=16\ \text{Weyl fields per generation},
\qquad
C:\ \mathbf4_{\imath}\mapsto\bar{\mathbf4}_{\imath},
$$

sixteen fields, thirty-two states, **closed under $C$ and, since $P$ maps the list to itself, under $CP$.** The two copies of each quartet are an index, not a gauge doublet: **the model makes one local group and this is its fermion content.**

**Why the count is a product and still a product.** A fermion carries one quartet value and one copy value, so the count is $4\times2$ per quartet type and $4\times2\times2$ with the conjugate type included. **The arithmetic is the old article's arithmetic and the meaning is not**: the second $2$ used to be a made local weak doublet, and here it is an index the group does not act on.

**What this article is.** The fermion side of the classification and its conjugation: the count, the two octets, the $B-L$ assignment read off the grid, the anomaly cancellation as a count, and the conjugation as a permutation of the field set.

**What this article is not.** It is not a flavour article and it says nothing about why there are three generations. Nor does it assign electric charge: **$Q$ needs the splitting of the copy index, which needs a weak factor and is therefore a statement about $M_C$**, and §*The Charge the Model Does Not Fix* says so explicitly.

## The Count Is a Product, Not a Sum of Squares

**The fermions are a product, because a fermion carries one value of every index.**

$$
\underbrace{4}_{\text{quartet}}\times\underbrace{2}_{\text{copy}}\times\underbrace{2}_{\text{quartet or antiquartet}}=16 .
$$

**The two quartets of the first type and the two of the second are two multiplets each**, and the product above distributes over them:

$$
2\cdot\mathbf4+2\cdot\bar{\mathbf4}=8+8=16 .
$$

**The sum of squares is the wrong operation and it is worth naming why.** $4^{2}+2^{2}+2^{2}=24$ counts the components of a tensor product of three spaces, which is the count of a boson's adjoint content. **A fermion is not a bilinear of the frame; it is a vector in one representation**, and the representation is fixed once the quartet index and the copy index are fixed. **The product is the count of vectors; the sum of squares is the count of operators.**

## The Fermions, on the Same Grid

**Sixteen per generation, and they sit on the quartet's four labels times two copies, on each side of the conjugate pair.** A fermion is one quartet index and one copy index; the $B-L$ of a row is the eigenvalue of that cell.

**The two quartets $\mathbf4_{\imath}$: the four labels, twice.**

| field | cell | $B-L$ | $Q$ in this model |
|---|---|---|---|
| $\nu_{\imath}$ | $t$ | $-1$ | not fixed |
| $e_{\imath}$ | $t$ | $-1$ | not fixed |
| $u^{\alpha}_{\imath}$ | $\alpha=r,g,b$ | $+\tfrac13$ | not fixed |
| $d^{\alpha}_{\imath}$ | $\alpha=r,g,b$ | $+\tfrac13$ | not fixed |

**The two antiquartets $\bar{\mathbf4}_{\jmath}$: the same, with every $B-L$ reversed.**

| field | cell | $B-L$ | $Q$ in this model |
|---|---|---|---|
| $\bar\nu_{\jmath}$ | $t$ | $+1$ | not fixed |
| $\bar e_{\jmath}$ | $t$ | $+1$ | not fixed |
| $\bar u^{\alpha}_{\jmath}$ | $\alpha=r,g,b$ | $-\tfrac13$ | not fixed |
| $\bar d^{\alpha}_{\jmath}$ | $\alpha=r,g,b$ | $-\tfrac13$ | not fixed |

**Three remarks about the pairing.**

- **The two copies carry the same $B-L$ and the same colour.** That is the definition of an index: $\imath=1,2$ is a label the group does not see, so it cannot change an eigenvalue. **The splitting of the two copies happens below $M_C$**, and it is where the up/down and the neutrino/electron distinction is made.
- **A massive fermion needs both halves.** $\mathbf4$ and $\bar{\mathbf4}$ are one Dirac field read twice; the electron is the pair, not either row alone. **So a count of fields is sixteen and a count of particles is fewer.**
- **Three generations multiply the table by three**: forty-eight Weyl fields and ninety-six states. **The number of generations is not fixed by the grid.**

## The Charge the Model Does Not Fix

**One statement, made once, because the model's tables cannot carry it.**

**The model fixes $B-L$ and it does not fix $Q$.** $B-L$ is a generator of the algebra, so every entry of every quartet has a definite value of it. **$Q$ is not a generator of $\mathrm{SU}(4)$, and no combination of the fifteen is the electric charge of a fermion**, because the two copies of a quartet carry the same $B-L$ and the same colour and differ in nothing the group acts on.

**What supplies the difference.** A weak factor: a made local $\mathrm{SU}(2)$ acting on the copy index, with $T_3=\pm\tfrac12$, gives

$$
Q=T_3+\tfrac12\bigl(B-L\bigr),
$$

and the familiar charges come back — $0$ and $-1$ on the lepton line, $+\tfrac23$ and $-\tfrac13$ on each colour line. **That equation belongs below $M_C$ and not here**: it is written where the weak factor is born as a side effect, and it is not used in this article's tables.

**Why the distinction is worth a section.** A table of $Q$ values in an $\mathrm{SU}(4)$-only article would be a table of charges that this model does not carry. **The honest column is the one above, and its fourth entry reads "not fixed".**

## The Conjugate Grid

### The Operation

**Charge conjugation reverses the quartet and keeps the copy.**

$$
C:\ \mathbf4_{\imath}\longmapsto\bar{\mathbf4}_{\imath},\qquad
C^{2}=\mathbb 1 .
$$

**On the algebra it sends a generator to the corresponding generator of the conjugate group**, which is the same fifteen read oppositely, and the boson articles already use it: the antiparticle of a boson is the same array with the opposite $i$. **For the fermions the statement is shorter**: $C$ acts on the representation label and it is a permutation of the sixteen fields, because for every $\mathbf4_{\imath}$ the list contains a $\bar{\mathbf4}_{\imath}$.

**A chiral content would fail here, and the contrast is the point.** Content of the form $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$ would send $(\mathbf4,\mathbf2,\mathbf1)$ under $C$ to a representation **not** in the list: such a model is closed under $CP$ and not under $C$. **This content is vector-like and closed under both**, and the reason is a count: two copies on each side.

### The Antiparticle $B-L$

**Reversal of the quartet reverses the eigenvalue.**

$$
B-L\bigl(\bar{\mathbf4}\bigr)=-\bigl(B-L\bigr)(\mathbf4):\qquad
(-1,\,\tfrac13,\,\tfrac13,\,\tfrac13)\longmapsto(+1,\,-\tfrac13,\,-\tfrac13,\,-\tfrac13).
$$

**The trace of the conjugate is minus the trace of the original**, and both vanish: $(-\tfrac33+\tfrac13+\tfrac13+\tfrac13)=0$ and its negative. **So conjugation preserves the tracelessness of the algebra and reverses the charge of every state** — which is what "antiparticle" means, stated as a statement about a diagonal.

### The Count

**Sixteen fields, thirty-two states, and no missing multiplet.**

| what | count | why |
|---|---|---|
| Weyl fields per generation | $16$ | $2\cdot4+2\cdot\bar4$ |
| states per generation | $32$ | each Weyl field has two helicities |
| fields with $B-L=-1$ | $4$ | $\nu_{1},\nu_{2},e_{1},e_{2}$ |
| fields with $B-L=+1$ | $4$ | the four conjugates |
| fields with $B-L=+\tfrac13$ | $6$ | $u,d$ in three colours, two copies |
| fields with $B-L=-\tfrac13$ | $6$ | their conjugates |
| the sum of $B-L$ over the sixteen | $4(-1)+4(+1)+6(\tfrac13)+6(-\tfrac13)$ | $0$ |

**The last row is the anomaly check in one line, and it is a count.** The $\mathrm{SU}(4)^{3}$ anomaly coefficient is $+1$ on $\mathbf4$ and $-1$ on $\bar{\mathbf4}$, so

$$
2(+1)+2(-1)=0 .
$$

**Vector-like content cancels by counting and needs no repair term.** That is the structural gain of the SU(4)-only frame: the cancellation is visible in the field list and does not rest on a coincidence between different multiplets.

### What Charge Conjugation Does Not Do

**It does not add a field.** The sixteen are closed, so $C$ permutes them; there is no second sixteen and no missing partner.

**It does not reverse the colour.** The quartet and the antiquartet both carry the three colour labels, with opposite $B-L$. The colour of $\bar u$ is $\bar{\mathbf3}$ as a representation, and its *label* is still one of the three. **A reader who expects $C$ to exchange $r$ with $\bar r$ has conflated the label with the representation.**

**It does not give the mass.** $C$ is a symmetry of the content and not a mass term: a mass needs a scalar that converts $\mathbf4$ into $\bar{\mathbf4}$, which exists — the fourth-colour scalar $Ξ$ — and whose vacuum is what breaks the group. **The Yukawa sector is $C$**, and it is downstream of this count.

## The Checks

| claim | check | result |
|---|---|---|
| the content | $2\cdot4+2\cdot\bar4$ | $16$ |
| the product form | $4\times2\times2$ | $16$ |
| states | $2\times16$ | $32$ |
| the sum of $B-L$ | $4(-1)+4(1)+6(\tfrac13)+6(-\tfrac13)$ | $0$ |
| the $\mathrm{SU}(4)^{3}$ anomaly | $2(+1)+2(-1)$ | $0$ |
| $C$ as a permutation | every $\mathbf4_{\imath}$ has a $\bar{\mathbf4}_{\imath}$ | $4$ of $4$ |
| $C^{2}$ | two reversals | $\mathbb 1$ |
| the conjugate trace | $-(-3+1+1+1)$ | $0$ |
| $CP$ | $C$ closed, $P$ a space operation | closed |
| the sum of squares, as a control | $4^{2}+2^{2}+2^{2}$ | $24$, wrong operation |
| $Q$ from the algebra alone | any combination of the fifteen | impossible: same $B-L$, same colour |

## Distinctions That Are Easy to Lose

An index is not a factor. The copy index $\imath=1,2$ is invisible to the group; a made local doublet is not.

A label is not a representation. The three colour labels are the same on both sides of the conjugate pair; the representation is $\mathbf3$ on one side and $\bar{\mathbf3}$ on the other.

$B-L$ is not $Q$. The model fixes the first, and the second needs the weak factor.

Closed under $C$ is not the same as closed under $CP$. **This model has both, because the content is vector-like; a chiral content would have only the second.**

## Summary

**Sixteen Weyl fields per generation, as two quartets and two antiquartets, and the count is a product over the quartet index and the copy index.** The sum of $B-L$ vanishes and the $\mathrm{SU}(4)^{3}$ anomaly cancels by counting: $2(+1)+2(-1)=0$.

**Charge conjugation is a permutation of the sixteen, not an enlargement of them**, and $C^{2}=\mathbb 1$. **The content is vector-like, so the model is closed under $C$ and under $CP$** — a chiral pair would be closed under $CP$ only.

**The model fixes $B-L$ and does not fix $Q$.** The Standard Model's charge table needs the splitting of the copy index, which the weak factor at $M_C$ supplies — and printing it here would be printing numbers this model does not carry.

**Three generations multiply the table by three, and the grid does not fix the number.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbf4$, $\bar{\mathbf4}$ | the quartet and its conjugate |
| $\imath,\jmath\in\{1,2\}$ | the copy index, invisible to the group |
| $B-L$ | $\tfrac13\operatorname{diag}(-3,1,1,1)$ on $\mathbf4$, negated on $\bar{\mathbf4}$ |
| $C$ | charge conjugation, $\mathbf4_{\imath}\mapsto\bar{\mathbf4}_{\imath}$ |
| $T_3$ | the half-integer of the copy index, **supplied downstream** |
| $Q$ | $T_3+\tfrac12(B-L)$, **not a generator of this model** |

## Further Reading

- [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The cell picture the fermion labels use.
- [The $\mathrm{SU}(4)$ Model](the-su4-model-four-colours-fifteen-generators-one-declaration.html). The declaration, the group, and the fermion content stated as a principle.
- [The Yukawa Sector](the-yukawa-sector-of-the-su4-model-one-matrix-and-its-diagonalisation.html). The masses of these states.
- [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). Where $T_3$ comes from.
- [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). Why the lepton line is minus the colour trace.
