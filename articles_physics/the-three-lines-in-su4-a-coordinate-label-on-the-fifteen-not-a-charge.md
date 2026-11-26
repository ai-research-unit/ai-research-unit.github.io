# __The Three Lines in $\mathrm{SU}(4)$: A Coordinate Label on the Fifteen, Not a Charge__

## Introduction

**The question.** The corpus writes $r\bar g$, $r\bar b$ and $b\bar\ell$ on the fifteen connections, and it calls them line names. **Are they charges?**

**The answer.** No. **They are coordinates in a $4\times4$ table.** Above $M_C$ the group is one simple factor and no $\mathrm{SU}(3)$ is made local, so a line letter names a slot and nothing else. **It is not an eigenvalue, not a conserved number, and not an observable.**

**What this article establishes.** The fifteen flat labels, with no broken-phase word among them: twelve ordered pairs and three diagonal directions. Why the labels mix under a local transformation. Why nothing can measure them above $M_C$. And the four facts that are real — the group, its dimension, its rank, and the common mass.

**What it does not establish.** That the strong group exists anywhere. **The $\mathrm{SU}(3)$ content — eight, rank two, the singlet excluded — belongs to the phase below $M_C$**, and the companion article [The Three Lines in $\mathrm{SU}(3)$](the-three-lines-in-su3-a-coordinate-label-on-the-eight-not-a-charge.html) carries it. This article is the first half, and it stops at the transition.

**Why the flat list comes first.** A claim that "the labels are bookkeeping" is worth nothing until the bookkeeping is printed. **So the article prints all fifteen labels before it argues anything about them.**

## The Four Lines, and the Two Things the Renaming Does

**The carrier above $M_C$ is a four-dimensional complex space, and its basis is written $(t,x,y,z)$.** The line-letter notation writes the same four lines as $(\ell,r,g,b)$.

**Two separate acts sit inside that renaming, and only one of them carries content.**

| act | what it is | status |
| --- | --- | --- |
| writing $x,y,z$ as $r,g,b$ | a change of letter | notation, no content |
| writing $t$ as $\ell$ | the statement that the temporal line is the lepton line | declaration (A) |

**The first act is free.** Nothing in the model depends on calling the second line red rather than green, and a permutation of the three line letters changes no number. **The second act is the corpus's one declared input**, and its content is which line is which — not that a strong group exists.

**What neither act does is representative anything.** The group acting on the quartet is $\mathrm{SU}(4)$, one factor, and its fifteen generators act on the four lines. **There is no second factor, and no three-line subgroup that is a factor of the theory.** A reader who supplies one has added a premise the model does not contain.

**That is the whole of the pre-breaking situation.** Four lines, fifteen directions between them, one group. **The letters name the lines; the labels below name the directions.**

## The Fifteen, Flat

**Define the matrix unit $E_{ij}$: the direction that moves line $j$ into line $i$, with $i\ne j$.** Its cell label is $i\bar j$, read as *line $i$ on line anti-$j$*. **Columns are sources and rows are targets**, so cell $(i,j)$ of the corpus's grid is $E_{ij}$.

**The fifteen are twelve such pairs and three diagonal directions.** That is the complete list, and no word from the broken phase appears in it.

### The Twelve Ordered Pairs

**Four lines, three partners each, twelve ordered pairs.** Each pair is one direction, labelled by the two lines it connects.

| # | direction | label | what it moves |
| --- | --- | --- | --- |
| 1 | $E_{rg}$ | $r\bar g$ | $g\to r$ |
| 2 | $E_{rb}$ | $r\bar b$ | $b\to r$ |
| 3 | $E_{r\ell}$ | $r\bar\ell$ | $\ell\to r$ |
| 4 | $E_{gr}$ | $g\bar r$ | $r\to g$ |
| 5 | $E_{gb}$ | $g\bar b$ | $b\to g$ |
| 6 | $E_{g\ell}$ | $g\bar\ell$ | $\ell\to g$ |
| 7 | $E_{br}$ | $b\bar r$ | $r\to b$ |
| 8 | $E_{bg}$ | $b\bar g$ | $g\to b$ |
| 9 | $E_{b\ell}$ | $b\bar\ell$ | $\ell\to b$ |
| 10 | $E_{\ell r}$ | $\ell\bar r$ | $r\to\ell$ |
| 11 | $E_{\ell g}$ | $\ell\bar g$ | $g\to\ell$ |
| 12 | $E_{\ell b}$ | $\ell\bar b$ | $b\to\ell$ |

**Twelve, and the count is arithmetic: $4\times3=12$.** Each unordered pair of lines carries two directions, the move and its reverse, so the same twelve are $\binom42=6$ pairs with two amplitudes each. **The corpus's other count — six planes, two arrays per plane — is this one**, printed in the anti-Hermitian basis as $A_{ij}$ and $iS_{ij}$.

**Which of the two amplitudes is called the boson and which the antiparticle is a convention**, and the corpus states it as one: the real and the imaginary halves of a plane are the two components of one complex field, separated by a factor of $i$. **The count is not a convention; the naming of the halves is.**

### The Three Diagonal, and the Slot That Is Not in the Algebra

**The diagonal cells do not move a line. They weight it.** Four cells, $r\bar r$, $g\bar g$, $b\bar b$ and $\ell\bar\ell$, each a direction in which a line keeps its identity and changes its phase.

**Four cells, three directions, and the missing one is the definition of the group.** The sum of the four is the identity,

$$
\sum_{i}i\bar i=\mathbb 1 ,
$$

**and $\mathfrak{su}(4)$ is traceless, so the identity direction is not a generator.** The trace-free combinations that remain are three. **That is the whole content of "one fewer on the diagonal": the count is $4^{2}-1$, and the removed direction is the one the $S$ in $\mathrm{SU}$ removes.**

**The corpus's three are $iM_x$, $iM_y$ and $iM_z$**, with $M_j=E_{jj}-E_{tt}$, and the trace direction $D=\operatorname{diag}(-3,1,1,1)$ is their sum up to normalisation. **That basis is a choice; the dimension three is not.** **This one is chosen because it is symmetric in $x,y,z$: the permutation of the three vector labels permutes the three of them and fixes no member**, and the fourth line is what makes the choice possible at all, as [The Symmetric Diagonal Frame](the-symmetric-diagonal-frame-of-the-fifteen.html) proves. A reader who prefers $i\bigl(W_{xx}+W_{yy}+W_{zz}\bigr)$, $\tfrac i2\bigl(W_{yy}-W_{xx}\bigr)$ and $\tfrac i2\bigl(W_{zz}-W_{yy}\bigr)$ has the same three-dimensional space in another basis, and every number computed from it is unchanged.

**The diagonal directions carry no root.** A Cartan generator has weight zero: it measures the shift a root produces and produces none itself. **"The label of a diagonal boson" is therefore the zero label**, which is another way of saying that the three are the measuring rods and the twelve are the moves.

**And the analogous arithmetic one size down names the same object.** Triplet–antitriplet slots number $N^{2}$; the algebra keeps $N^{2}-1$; the removed one is the trace. **At $N=4$ that is $16\to15$; at $N=3$ it is $9\to8$.** The arithmetic is identical and so is its status: **a count, not a convention.**

## Why the Label Is Not a Charge

**Two arguments, and either one is enough.**

### It Is Not Invariant

**The connection is $A_\mu=\sum_{a}A_\mu^{a}t_{a}$, and the index $a$ is the label.** Under a local transformation,

$$
A_\mu\ \longmapsto\ U A_\mu U^{\dagger}+\tfrac{i}{g_4}U\partial_\mu U^{\dagger},
$$

**so the components rotate among themselves**, $A_\mu^{a}\mapsto R^{ab}A_\mu^{b}$ plus the inhomogeneous term, with $R$ the adjoint rotation built from $U$. **A field carrying $r\bar g$ in one representative carries a combination of all fifteen in another.** The only basis-independent numbers are the Casimirs, and the quadratic Casimir of the adjoint takes the same value on all fifteen.

**A charge is a number that an invariant operator can read off.** The label $r\bar g$ is an index of a basis in which the group mixes components. **Those are different kinds of object**, and calling the second a charge is the error this article exists to prevent.

**The weights do not rescue it.** The weights of a representation are labels relative to a chosen Cartan basis, and the normalisation of a Cartan generator is itself a choice. **The root system is invariant; the numbers attached to a root are not.**

### Nothing Measures It: the Fifteen Are Degenerate

**Above $M_C$ the scalar has no vacuum value, so the adjoint mass matrix vanishes identically.** With the mass form

$$
M^{2}_{XY}=\operatorname{tr}\bigl([X,\Xi_0]^{\dagger}[Y,\Xi_0]\bigr),
$$

**and $\Xi_0=0$, every entry is zero for every pair.**

**So all fifteen are massless, with one coupling, in one degenerate multiplet.** A mass would be the one invariant label that could separate a direction from its neighbours, and there is none. **No cross-section, no decay rate and no spectrum can tell $E_{b\ell}$ from $E_{br}$**: every basis rotation is a symmetry of the numbers, and a label a symmetry can rotate away is not a property of anything.

**This is the sharpest form of the claim.** Below $M_C$ the degeneracy lifts — six of the fifteen take $32v^{2}$ and nine stay at zero — and that split is observable. **Above $M_C$ there is nothing to lift, and therefore nothing for a name to attach to.**

**The strongest objection, named before it is answered.** *QCD's triplet labels are basis labels too, and its eight gluons are physical.* **True, and it is the point.** Even below $M_C$, $r\bar g$ is a coordinate on the adjoint of $\mathrm{SU}(3)$; what is physical there is the group, the dimension eight, the rank two, the exclusion of the singlet, and the invariant rates computed from them. **The letters are never physics at either scale.** What changes between the scales is not that the letters become real. **It is that below $M_C$ there is a group for the coordinates to be coordinates of, and above it there is not.**

## What Is Real, and What Is Chosen

**Four facts survive every change of basis.**

$$
\boxed{\;
G=\mathrm{SU}(4),\qquad
\dim_{\mathbb R}\mathfrak g=15,\qquad
\operatorname{rank}\mathfrak g=3,\qquad
m^{2}=0\ \text{for all fifteen above }M_C
\;}
$$

**None of the four mentions a line, a letter or a cell**, and each is checkable without choosing a basis: the group is declared, the dimension is $4^{2}-1$, the rank is the number of independent diagonal directions, and the vanishing mass follows from $\Xi_0=0$.

**The split into twelve and three is a fifth, and it is invariant for the same reason.** Every basis of $\mathfrak{su}(4)$ exhibits twelve root directions and a Cartan of dimension three, because the algebra has twelve roots and rank three. **Which cell carries which root is a basis statement; that there are twelve and three is not.**

**What is chosen is everything else.**

| object | status |
| --- | --- |
| the letters $r,g,b,\ell$ | notation |
| which line is called $\ell$ | declaration (A) |
| the label $i\bar j$ of a given cell | a coordinate |
| the three combinations $iM_x$, $iM_y$, $iM_z$ | one basis of the Cartan, the symmetric one |
| the partition $15=8+1+6$ | a degeneration of the frame at $v_t=0$, and it needs the declaration |
| the words gluon, leptoquark, $B-L$ boson | names of cells, relative to that declaration |

**The last two rows are the ones that mislead, and the reason is the same in each.** They look like facts about the fifteen and they are facts about the fifteen *plus a declared line*. **Change the declaration and the partition changes and the names change, while no number computed from the spectrum moves.** That is exactly what a bookkeeping device does, and it is the test this article's title claims the labels pass.

## One Statement That Must Not Be Carried Upward

**The phrase that reads the labels as four group members is to be avoided.** It reads as a group with four lines, and above $M_C$ there is no strong group — there are four lines of one multiplet. **The correct pre-breaking sentence is: fifteen directions of one simple group, of which twelve move a line and three weight the lines.**

**"The fourth line" is a different phrase with a different status**, and the difference is worth keeping. It is shorthand for declaration (A), the statement that $e_t$ is the lepton line, and the corpus states it as one declaration rather than as a result. **A reader may keep the phrase provided the word *declaration* stays beside it.** Its content is which line is which; no measurement inside this article's scope decides that, and the algebra does not either.

**The test is mechanical.** Take any sentence carrying a line name in it and ask whether it survives a relabelling of the four lines. **What survives is physics. What does not is a coordinate, and coordinates belong to the table, not to nature.**

## The Checks

| check | arithmetic | result |
| --- | --- | --- |
| cells of the grid | $4\times4$ | $16$ |
| minus the trace | one direction removed | $15$ |
| ordered pairs | $4\times3$ | $12$ |
| pairs with two amplitudes each | $2\binom42=2\cdot6$ | $12$ |
| diagonal cells | $4$ | $4$ |
| minus the singlet | $-1$ | $3$ |
| roots and Cartan | $12+3$ | $15=\dim\mathfrak{su}(4)$ |
| rank | independent diagonal directions | $3$ |
| mass of every direction above $M_C$ | $\Xi_0=0$ | $0$ |
| the two branchings of the same arithmetic | $4^{2}-1$, $3^{2}-1$ | $15$, $8$ |
| the partition with the declaration | $8+1+6$, at the degenerate value of the frame | $15$ |
| the partition without it | $12+3$ | $15$ |

## Summary

**The fifteen labels are twelve ordered pairs and three diagonal directions, and none of them is a charge.** A pair names the two lines a direction connects; a diagonal names the weighting of a line. **The table is a chart of sixteen slots with the trace removed, and that is the whole of what the label means above $M_C$.**

**The labels are unobservable for two independent reasons.** They mix under a local transformation, so no invariant operator carries one; and the fifteen are exactly degenerate, so no rate or mass distinguishes one label from another. **A label a symmetry can rotate away is notation.**

**Four things are real: the group, the dimension, the rank, and the masslessness.** They survive every basis and are checkable without naming a line. **The twelve-and-three split is a fifth**, invariant for the same reason.

**Every statement that uses a line letter is downstream of a declared line.** The partition $8+1+6$, the words gluon and leptoquark, the phrase "the fourth line" — each requires declaration (A), and the first requires a second thing besides: a vacuum, because $8+1+6$ is the degenerate value of the diagonal frame and not a decomposition of the fifteen. **That is the test of bookkeeping, and the fifteen pass it.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $(t,x,y,z)$ | the carrier basis above $M_C$ |
| $(\ell,r,g,b)$ | the same four lines in line letters |
| $E_{ij}$ | the direction moving line $j$ into line $i$, with $i\ne j$ |
| $i\bar j$ | the cell label of $E_{ij}$ |
| $iM_j$, $j=x,y,z$ | the three trace-free diagonal directions, the symmetric frame |
| $iD$ | $i\sum_jM_j$, the trace direction, not one of the fifteen |
| $D$ | $\operatorname{diag}(-3,1,1,1)$ up to normalisation, the direction the vacuum takes below $M_C$ |
| $\Xi_0$ | the scalar's vacuum value, zero above $M_C$ |
| $M_C$ | the scale of the transition |
| declaration (A) | the statement that $e_t$ is the lepton line |

## Further Reading

- [The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration of Rank Three](the-su4-model-four-lines-fifteen-generators-one-declaration.html), for the group, the count of fifteen and the place of declaration (A).
- [The Counts of the Fifteen: Sixteen Cells, Six Pairs, Twelve Arrays, Fifteen Generators](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html), for the cell, plane and array vocabulary used above.
- [Classification of the Bosons in the $\mathrm{SU}(4)$ Model](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html), for the same grid read with names in every cell, and for what changes at the transition.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html), for the covariant derivative, the one coupling and the local transformation quoted above.
