# __The Five Counts of the Twenty-One: Twenty-Four Cells, Six Planes, Twenty-One Arrays, Fifteen Directions__

## Introduction

**Five different objects are called "the twenty-one" in this block of the corpus, and each has its own count.** The counts are $24$ cells, $6$ geometric planes, $21$ arrays, $21$ generator names on the declared copy against $15$ on the carrier, and $15$ directions. None of them is the others, and most of the slips in the boson articles are a slide from one to the next.

The slides are easy to make because every count is arithmetically right. The grid has $16$ cells and the three grids have $24$. A four-index object has six unordered pairs. The boson ledger has $21$ entries. The algebra $\mathfrak{su}(4)$ has dimension $15$. Each number answers a different question, and a sentence that mixes two of them is wrong even when both numbers are right.

This article fixes the five words, gives each one a definition, states the map from one to another, and names the article where each count is the operative one. It is a vocabulary article: it proves counts and identities and adds no physics. Where a count has a home elsewhere, the home is cited and the count is restated only as far as the map needs it.

The articles it leans on are [The Four Colours Left–Right Model](the-four-colours-left-right-model.html) for the declaration of the group, [Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html) for the arrays, [Classification of the Bosons](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html) for the grid, and [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html) for the count that the mass spectrum uses.

## The Cell: Twenty-Four Positions

**A cell is a position in one of the three grids.** The model declares three unitary factors, of ranks $4$, $2$ and $2$, and each factor has a grid: the $4\times4$ grid of the quartet carrier, and a $2\times2$ grid for each weak doublet. The count is the sum of squares,

$$
4^{2}+2^{2}+2^{2}=16+4+4=24 .
$$

**A cell is a position and not a generator.** The cell $(i,j)$ is the matrix unit $E_{ij}$; it is not an element of the algebra. The algebra is the traceless anti-Hermitian part, so a generator is a combination of cells: an off-diagonal generator occupies two cells, $A_{jk}=E_{jk}-E_{kj}$ or $iS_{jk}=i(E_{jk}+E_{kj})$, and a diagonal generator is a combination of diagonal cells, $iD$ being $i$ times the three colour diagonal cells minus three times the corner cell, $iD=i(N_{xx}+N_{yy}+N_{zz})-3iE_{tt}$.

**The four diagonal cells against the three diagonal directions.** The quartet grid has four diagonal cells and the algebra has three diagonal directions, because the trace is removed: the four cells span a four-dimensional space and the traceless part of it is three-dimensional. That is the arithmetic behind "remove the trace", and it is one cell and one dimension, not a coincidence.

**The $4\times4$ grid in blocks.** The grid splits by what a cell touches:

| block | cells | what it is |
|---|---|---|
| corner | $1$ | $(t,t)$, the single cell that carries $B'$ |
| mixed band | $6$ | the $t$ row and the $t$ column off the corner |
| colour block | $9$ | the $3\times3$ grid on $x,y,z$ |

$1+6+9=16$. The generator count of the same three blocks is $1+6+8=15$, because the colour block has nine cells and eight traceless directions.

**Why the cells are counted at all.** The cell count is the one that says how many amplitudes a generator moves: two for an off-diagonal array, none for a diagonal one. The mass articles use "one entry per plane" and the classification uses "one name in every cell", and both are statements about cells. The generator ledger never uses $24$.

## The Plane: Six Geometric Pairs, Twelve Arrays

**A plane is an unordered pair of the four indices.** There are

$$
\binom{4}{2}=6
$$

of them: three mixed, $\{t,x\}$, $\{t,y\}$, $\{t,z\}$, and three colour, $\{x,y\}$, $\{y,z\}$, $\{z,x\}$.

**Each plane carries two arrays.** The real array $A_{jk}=E_{jk}-E_{kj}$ and the imaginary one $iS_{jk}=i(E_{jk}+E_{kj})$ are independent, both lie in the algebra, and both are supported on the same two indices. So six planes carry twelve arrays, and $12+3=15$ counts the fifteen once the three diagonal directions are added.

**The word "plane" is used for the array in the mass articles, and that is the one slide to know.** "The six leptoquark planes" and "$32v^{2}$ on six planes" count arrays: three geometric pairs, each contributing a real and an imaginary plane. "The three colour planes" counts geometric pairs, because the colour block is discussed as a block. Both usages are arithmetically consistent; a sentence that mixes them is not. The safe form is to name the object: *the six mixed arrays, on three geometric planes*.

**A plane is not a particle.** The three mixed planes carry six leptoquark states, because each plane carries two amplitudes, $X^{\alpha}$ and $\bar X^{\alpha}$. The three colour planes carry eight gluons, because the colour block is $\mathfrak{su}(3)$ and not three directions. So "one plane, one particle" holds for the mixed band and fails for colour. [Classification of the Bosons](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html) states both fates; the count of particles is neither six nor three.

## The Array: Twenty-One Matrices, Fifteen Dimensions

**An array is a $4\times4$ matrix, and the corpus prints twenty-one of them.** Fifteen are the arrays of $\mathfrak{su}(4)$ — six real planes, six imaginary planes, three diagonals — and six are the weak generators $T^{L}_{a}=\tfrac12L_{e_a}$ and $T^{R}_{a}=\tfrac12R_{e_a}$.

**The twenty-one arrays span fifteen dimensions, not twenty-one.** The rank is a computation, not a convention:

$$
\operatorname{rank}\{A_{jk},iS_{jk},iD,d_2,d_3,T^{L}_{a},T^{R}_{a}\}=15 .
$$

The reason is that each weak array is a sum or a difference of two of the fifteen: $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$ and $A_{bc}=-(T^{L}_{a}-T^{R}_{a})$ with $(a,b,c)$ cyclic. Six names, no new direction. **This is why "twenty-one arrays" and "twenty-one generators" are different sentences**: the first is a count of printed matrices, the second is a count of named generators on the declared copy, and neither is a dimension.

**The trace form separates the three kinds of array.** With $G^{\dagger}G$ read in the fundamental,

| array | $\operatorname{tr}(G^{\dagger}G)$ | spectrum of $G$ |
|---|---|---|
| $A_{jk}$, $iS_{jk}$ | $2$ | $0,0,\pm i$ |
| $iD$ | $12$ | $-3i$ and $i$ three times |
| $d_2$, $d_3$ | $2$ | $0,0,\pm i$ |
| $T^{L}_{a}$, $T^{R}_{a}$ | $1$ | $\pm\tfrac i2$ twice |

The entry $12$ is arithmetic about the corner: $\operatorname{tr}(D^{2})=9+1+1+1=12$, nine from the lepton line and one from each colour line. The weak arrays carry $1$, which is the half in $T^{L}_{a}$ appearing twice — the factor that a recomputation of a weak mass on the carrier gets wrong.

## The Generator: Twenty-One Names on the Copy, Fifteen on the Carrier

**The model's gauge group is declared on a copy of the carrier, and the twenty-one is a count on that copy.** [The Rotors of the Twenty-One Generators](the-rotors-of-the-twenty-one-generators-in-the-four-colours-left-right-model-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) proves the copy theorem: the physical quartet of the model is a formal copy of the algebra's four-dimensional carrier, and the copy does not inherit the Lorentz action of the carrier. On the copy the group is $\mathrm{SU}(4)\times\mathrm{SU}(2)_{L}\times\mathrm{SU}(2)_{R}$, of dimension $15+3+3=21$.

**On the carrier the six weak generators are not independent.** They sit inside the fifteen, as the recombination identities above show. So a statement of the form "the twenty-one generators act on the carrier" is shorthand for "the twenty-one names, each read as an array of the fifteen". The two readings give different matrices for the same name, and that is the second slide to know.

**Two cuts of the same fifteen.** The fifteen is cut twice, and both cuts are used:

| cut | parts | where it is used |
|---|---|---|
| by grid block | $8+1+6$ | the classification's picture of the quartet grid |
| by residual algebra | $8+1+3+3$ | the breaking chain and the gauge algebras |

The first is colour, corner, mixed. The second is colour, $B-L$, the two weak triples. They agree in the colour block and differ in how the six mixed arrays are grouped: as six leptoquarks, or as two triples that become the $W$'s and $Z$'s. [The Gauge Algebras of the Two Sectors](the-gauge-algebras-of-the-two-sectors-colour-on-three-dimensions-weak-isospin-on-two-the-photon-on-one.html) owns the second cut and proves the chain $8+1+3+3=15\to12\to9$.

## The Direction: Fifteen, and Two Bases

**A direction is an element of the fifteen-dimensional real space $\mathfrak{su}(4)$.** A basis is a choice of fifteen arrays that span it, and the corpus uses two.

**The maths basis** is the words: the sixteen products $W_{\mu\nu}=L(e_{\mu})R(e_{\nu})$ are a basis of $M_4(\mathbb R)$; delete the one that is the identity, $W_{tt}=\mathrm I_4$, and multiply the other fifteen by $i$. Each of the fifteen has $\operatorname{tr}(G^{\dagger}G)=4$ and each moves four cells, because a word is a product of two signed permutations and has one non-zero entry in every row.

**The physics basis** is the six pairs summed and differenced, plus the three diagonals. Its arrays have $\operatorname{tr}(G^{\dagger}G)=2$ on the planes and each one moves two cells. The change of basis is the pair resolution, and [Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html) constructs it in three steps.

**One direction, two arrays.** $A_{tx}$ in the physics basis is $-\tfrac12(W_{tx}+W_{xt})$ in the maths basis. Both are the same direction, both are printed in the corpus, and the trace norms differ by the factor two that the halving introduces. A mass quoted "per direction" is basis-independent; a mass quoted "per array" carries the normalisation of the array.

## The Map Between the Counts

| word | count | what it counts | the article where it is operative |
|---|---|---|---|
| cell | $24$ | positions in the three grids | the classification's grid |
| plane | $6$ | unordered pairs of the four indices | the classification's block picture |
| array | $21$ | printed $4\times4$ matrices | the AXF article |
| generator name | $21$ | names on the declared copy | the model article, the rotors |
| direction | $15$ | $\dim_{\mathbb R}\mathfrak{su}(4)$ | the adjoint mass matrix, the rotations |

**The three identities that connect the columns.**

$$
16+4+4=24,\qquad 12+3=15,\qquad 15+3+3=21,\qquad \operatorname{rank}(\text{21 arrays})=15 .
$$

**The three slides that the table prevents.**

1. Twenty-four cells are not twenty-one generators: the cells include the four diagonal positions and both halves of every off-diagonal one.
2. Six planes are twelve arrays, not six generators: each geometric pair carries a real and an imaginary array.
3. Twenty-one named generators are fifteen directions: the six weak names are combinations of the fifteen.

## The Checks

Twelve recomputations, on the quartet ordered $(t,x,y,z)$ and the products fixed by $\vec e_x\vec e_y=\vec e_z$.

| check | computation | result |
|---|---|---|
| the cell count | $4^{2}+2^{2}+2^{2}$ | $24$ |
| the plane count | $\binom{4}{2}$, mixed plus colour | $6=3+3$ |
| the arrays on the planes and the diagonals | $12+3$ | $15$ |
| the boson ledger | $15+3+3$ | $21$ |
| the rank of the twenty-one arrays | real rank of the $21\times32$ matrix | $15$ |
| the rank of the fifteen | same, fifteen arrays only | $15$ |
| the recombination identities | $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$, $A_{bc}=-(T^{L}_{a}-T^{R}_{a})$, $(a,b,c)$ cyclic | $6/6$ |
| the grid in blocks | $1+6+9$ | $16$ |
| the generator count in the same blocks | $1+6+8$ | $15$ |
| the trace norms | $\operatorname{tr}(G^{\dagger}G)$ for $A_{jk}$, $iD$, $T^{L}_{a}$ | $2$, $12$, $1$ |
| the two cuts of the fifteen | $8+1+6$ and $8+1+3+3$ | $15$, $15$ |
| the corner | $16-1$ cells minus the trace | $15$ |

## Summary

**Five counts, five objects.** Twenty-four cells are positions in three grids. Six planes are unordered index pairs, carrying twelve arrays. Twenty-one arrays are printed matrices. Twenty-one generator names live on the declared copy. Fifteen directions span $\mathfrak{su}(4)$.

**The map is four identities.** $16+4+4=24$; $12+3=15$; $15+3+3=21$; and the twenty-one arrays have rank fifteen because the six weak names are sums and differences of the fifteen.

**The three slides.** Cells are not generators; planes are twice as many arrays; named generators are not directions.

**Why it matters.** Every count in the boson block of the corpus is right in its own register, and every error in that block is a sentence that changes register without saying so. The cure is to name the object: a cell, a plane, an array, a name, or a direction.

## Summary of Notation

| symbol | meaning |
|---|---|
| $E_{ij}$ | the matrix unit, one cell |
| $A_{jk}=E_{jk}-E_{kj}$ | the real array of the plane $\{j,k\}$ |
| $iS_{jk}=i(E_{jk}+E_{kj})$ | the imaginary array of the same plane |
| $D=\operatorname{diag}(-3,1,1,1)$ | the vacuum direction, traceless, $B-L=\tfrac13D$ |
| $iD$, $d_2$, $d_3$ | the three diagonal directions |
| $W_{\mu\nu}=L(e_\mu)R(e_\nu)$ | a word, one of the sixteen products |
| $T^{L}_{a}=\tfrac12L_{e_a}$, $T^{R}_{a}=\tfrac12R_{e_a}$ | the six weak arrays |
| cell, plane, array, name, direction | the five counts, in the sense of this article |

## Further Reading

- [Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html). The twenty-one arrays printed one to a display, and the three-step construction of the physics basis from the words.
- [Classification of the Bosons in the Four Colours Left–Right Model: Twenty-Four Cells, Twenty-One Generators, Nine Massless and Twelve Massive](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html). The grid, the block picture and the ledger of the spectrum.
- [The Rotors of the Twenty-One Generators in the Four Colours Left–Right Model](the-rotors-of-the-twenty-one-generators-in-the-four-colours-left-right-model-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html). The copy theorem, and what each of the twenty-one exponentials turns.
- [The Adjoint Mass Matrix of the Fifteen: One Number per Plane, $32v^2$ on Six and Zero on Nine](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html). The count of directions read as a mass spectrum.
- [The Gauge Algebras of the Two Sectors](the-gauge-algebras-of-the-two-sectors-colour-on-three-dimensions-weak-isospin-on-two-the-photon-on-one.html). The second cut of the fifteen, $8+1+3+3$, and the chain to $9$.
