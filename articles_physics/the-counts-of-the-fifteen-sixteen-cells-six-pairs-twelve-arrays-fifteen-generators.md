# __The Counts of the Fifteen: Sixteen Cells, Six Pairs, Twelve Arrays, Fifteen Generators__

## Introduction

**Four different objects are called "the fifteen" in this block of the corpus, and each has its own count.** The counts are $16$ cells, $6$ geometric pairs, $12$ plane arrays, and $15$ generators. **Each is arithmetically right and none is the others**, and most of the slips in the boson articles are a slide from one to the next.

**The slides are easy because every count is correct in its own register.** The grid has sixteen cells. A four-index object has six unordered pairs, and each pair carries two arrays. The algebra has fifteen generators. **A sentence that mixes two registers is wrong even when both numbers are right.**

**This article fixes the four words**, defines each, states the maps between them, and names the article where each is the operative one. **It is a vocabulary article: it proves counts and identities and adds no physics.**

**What is not here.** The old version of this article carried five counts and two of them were $24$ cells and $21$ arrays — the grids of three factors and the names on a declared copy. **With one group there is one grid and one copy of the fifteen**, so those two counts are gone and the article is shorter. **The subtraction is the model's:** it lost two factors and gained a shorter ledger.

**The articles it leans on** are [The $\mathrm{SU}(4)$ Model](the-su4-model-four-colours-fifteen-generators-one-declaration.html) for the group and the declaration, [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html) for the arrays, [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html) for the grid, and [The Death of the Primordial Force](the-death-of-the-primordial-force-the-id-condensate-and-the-six-carriers-it-eats.html) for the count the mass spectrum uses.

## The Cell: Sixteen Positions

**A cell is a position in the $4\times4$ grid.** The quartet is four-dimensional, so the grid is

$$
4^{2}=16 .
$$

**A cell is a position and not a generator.** The cell $(i,j)$ is the matrix unit $E_{ij}$; it is not an element of the algebra. **The algebra is the traceless anti-Hermitian part**, so a generator is a combination of cells: an off-diagonal generator occupies two cells, $A_{jk}=E_{jk}-E_{kj}$ or $iS_{jk}=i(E_{jk}+E_{kj})$, and a diagonal generator is a combination of diagonal cells. With $N_{xx},N_{yy},N_{zz}$ the colour diagonal cells and $E_{tt}$ the corner,

$$
iD=i\bigl(N_{xx}+N_{yy}+N_{zz}\bigr)-3iE_{tt}.
$$

**The four diagonal cells against the three diagonal generators.** The grid has four diagonal cells and the algebra has three diagonal generators, because the trace is removed. **Four cells span a four-dimensional space, its traceless part is three-dimensional**, and that is the arithmetic behind "remove the trace": one cell, one dimension, no coincidence.

**The grid in blocks.** It splits by what a cell touches:

| block | cells | what it is |
| --- | --- | --- |
| corner | $1$ | $(t,t)$, the single cell that carries $B'$ |
| mixed band | $6$ | the $t$ row and the $t$ column, off the corner |
| colour block | $9$ | the $3\times3$ grid on $x,y,z$ |

$1+6+9=16$. **The generator count of the same three blocks is $1+6+8=15$**, because the colour block has nine cells and eight traceless generators.

**Why the cells are counted at all.** The cell count says how many amplitudes a generator moves: two for an off-diagonal array, none for a diagonal one. **The mass articles say "one entry per plane" and the classification says "one name in every cell"**, and both are statements about cells.

**The identity of this register.** $16=1+15$: sixteen cells, one trace, fifteen generators. **That single line replaces the old $24=16+4+4$**, and the four that is missing twice is the two weak factors that are not in the model.

## The Pair and the Plane: Six Geometric Pairs, Twelve Arrays

**A plane is an unordered pair of the four indices.** There are

$$
\binom{4}{2}=6
$$

of them: **three mixed**, $\{t,x\}$, $\{t,y\}$, $\{t,z\}$, and **three colour**, $\{x,y\}$, $\{y,z\}$, $\{z,x\}$.

**Each plane carries two arrays.** The real array $A_{jk}=E_{jk}-E_{kj}$ and the imaginary one $iS_{jk}=i(E_{jk}+E_{kj})$ are independent, both lie in the algebra, and both are supported on the same two indices. **So six planes carry twelve arrays, and $12+3=15$ counts the fifteen once the three diagonals are added.**

**The word "plane" is used for the array in the mass articles, and that is the one slide to know.** "The six leptoquark planes" and "$32v^{2}$ on six planes" count arrays: three geometric pairs, each contributing a real and an imaginary array. "The three colour planes" counts geometric pairs, because the colour block is discussed as a block. **Both usages are arithmetically consistent; a sentence that mixes them is not.** The safe form names the object: *the six mixed arrays, on three geometric planes*.

**A plane is not a particle.** The three mixed geometric pairs carry six leptoquark states, because each pair carries two amplitudes, $X^{\alpha}$ and $\bar X^{\alpha}$. The three colour pairs carry eight gluons, because the colour block is $\mathfrak{su}(3)$ and not three generators. **So "one plane, one particle" holds for the mixed band and fails for colour**, and the count of particles is neither six nor three.

## The Array: Fifteen Matrices

**An array is a $4\times4$ matrix in the algebra, and the corpus prints fifteen of them.**

| array | count | trace norm $\operatorname{tr}(G^{\dagger}G)$ | spectrum |
| --- | --- | --- | --- |
| $A_{jk}$ | $6$ | $2$ | $0,0,\pm i$ |
| $iS_{jk}$ | $6$ | $2$ | $0,0,\pm i$ |
| $d_2$, $d_3$ | $2$ | $2$ | $0,0,\pm i$ |
| $iD$ | $1$ | $12$ | $-3i$ and $i$ three times |

**Fifteen arrays, fifteen generators, and here the two counts agree** — because the fifteen arrays are a basis. **That agreement is the point of using this basis**, and it is the one register in which the count of printed names and the dimension are the same number.

**The entry twelve is arithmetic about the corner.** $\operatorname{tr}(D^{2})=9+1+1+1=12$: nine from the lepton line and one from each colour line. **It is the only array with a norm above two, and the excess is the fourth colour's weight squared.**

**A normalisation that will matter later.** Every plane array has norm two and every diagonal except $iD$ has norm two; $iD$ has norm twelve. **A mass quoted per generator is basis-independent; a mass quoted per array carries the array's normalisation.** The adjoint mass matrix is written per generator for that reason.

## The Six $\mathfrak{so}(4)$ Arrays Are Not Six More Directions

**This is the slide that the old version of this article called "twenty-one names against fifteen".**

**The object.** The algebra's two-sided action gives $\mathfrak k_L\oplus\mathfrak k_R$, six real dimensions, and the six arrays

$$
T^{L}_{x}=-\tfrac12\bigl(A_{tx}+A_{yz}\bigr),\qquad
T^{R}_{x}=-\tfrac12\bigl(A_{tx}-A_{yz}\bigr),
$$

and cyclic in $(x,y,z)$. **These are six printed matrices and they span six dimensions — but not six new ones.**

**The rank, computed and not asserted.**

$$
\operatorname{rank}\bigl\{A_{jk},\,iS_{jk},\,d_2,\,d_3\bigr\}=15,
\qquad
\operatorname{rank}\bigl\{A_{jk},\,iS_{jk},\,d_2,\,d_3,\,T^{L}_{a},\,T^{R}_{a}\bigr\}=15 .
$$

**Adding the six arrays adds no dimension**, because each is a real combination of two of the plane arrays:

$$
A_{ta}=-\bigl(T^{L}_{a}+T^{R}_{a}\bigr),\qquad
A_{bc}=-\bigl(T^{L}_{a}-T^{R}_{a}\bigr),
$$

with $(a,b,c)$ cyclic in $(x,y,z)$. **Six names, no new generator, and the bracket of the six closes on the six.**

**So the sentence to avoid.** "The model has twenty-one generators" is false twice: **it has fifteen generators, and the six extra names are a rotated basis of a six-dimensional subspace of those fifteen.** The correct sentence names what the six are — *the six planes of $\mathfrak{so}(4)$* — and points to the section of the corpus where they are given a physical reading.

**What the six are for.** They are the object the successor model will name. **They are not a factor, they do not commute with the colour block, and three of them are heavy after the transition** — so they are not even a well-defined set of particles. That is the whole content of [The Weak Force Born as a Side Effect](the-weak-force-born-as-a-side-effect-a-condensate-index-five-ranks-from-three.html), and it is why the count of *names* must never be read as a count of *generators*.

## The Direction: Fifteen, and Two Bases

**A generator is an element of the fifteen-dimensional real space $\mathfrak{su}(4)$.** A basis is a choice of fifteen arrays that span it, and the corpus uses two.

**The maths basis** is the words: the sixteen products $W_{\mu\nu}=L(e_{\mu})R(e_{\nu})$ are a basis of $M_4(\mathbb R)$; **delete the one that is the identity, $W_{tt}=\mathrm I_4$, and multiply the other fifteen by $i$.** Each of the fifteen has $\operatorname{tr}(G^{\dagger}G)=4$ and moves four cells, because a word is a product of two signed permutations and has one non-zero entry in every row.

**The physics basis** is the six pairs summed and differenced, plus the three diagonals. **Its arrays have norm two on the planes and each one moves two cells.** The change of basis is the pair resolution, and [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html) constructs it in three steps.

**One generator, two arrays.** $A_{tx}$ in the physics basis is $-\tfrac12(W_{tx}+W_{xt})$ in the maths basis. **Both are the same generator, both are printed in the corpus, and the norms differ by the factor two that the halving introduces.**

## The Map Between the Counts

| word | count | what it counts | the article where it is operative |
| --- | --- | --- | --- |
| cell | $16$ | positions in the one grid | the classification's grid |
| pair | $6$ | unordered pairs of the four indices | the block picture |
| array | $15$ | printed $4\times4$ matrices | the AXF article |
| generator | $15$ | $\dim_{\mathbb R}\mathfrak{su}(4)$ | the adjoint mass matrix, the rotations |

**The two identities that connect the columns.**

$$
16=1+15,\qquad 6\ \text{pairs}\times2+3\ \text{diagonals}=12+3=15 .
$$

**The three slides that the table prevents.**

1. **Sixteen cells are not fifteen generators**: the cells include the four diagonal positions and both halves of every off-diagonal one, and the trace is removed.
2. **Six pairs are twelve arrays, not six generators**: each geometric pair carries a real and an imaginary array.
3. **Six more names are not six more generators**: the six $\mathfrak{so}(4)$ arrays are combinations of the twelve plane arrays, and the rank stays fifteen.

## The Checks

Recomputations, on the quartet ordered $(t,x,y,z)$ and the products fixed by $\vec e_x\vec e_y=\vec e_z$.

| check | computation | result |
| --- | --- | --- |
| the cell count | $4^{2}$ | $16$ |
| the pair count | $\binom42$, mixed plus colour | $6=3+3$ |
| the arrays on the pairs and the diagonals | $12+3$ | $15$ |
| the rank of the fifteen arrays | real rank of the $15\times32$ matrix | $15$ |
| the rank after adding the six $\mathfrak{so}(4)$ arrays | the $21\times32$ matrix | $15$ |
| the recombination identities | $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$, $A_{bc}=-(T^{L}_{a}-T^{R}_{a})$, $(a,b,c)$ cyclic | $6/6$ |
| the six $\mathfrak{so}(4)$ arrays close on themselves | brackets of all fifteen pairs | closed, $\dim6$ |
| the grid in blocks | $1+6+9$ | $16$ |
| the generators in the same blocks | $1+6+8$ | $15$ |
| the trace norms | $\operatorname{tr}(G^{\dagger}G)$ for $A_{jk}$, $iD$, $iS_{jk}$ | $2$, $12$, $2$ |
| the corner | $16-1$ cells minus the trace | $15$ |
| the rank of $\mathfrak{su}(4)$ | maximal torus | $3$ |

## Summary

**Four counts, four objects.** Sixteen cells are positions in the one grid. Six pairs are unordered index pairs, carrying twelve arrays. Fifteen arrays are printed matrices. Fifteen generators span $\mathfrak{su}(4)$.

**The map is two identities.** $16=1+15$; and six pairs times two plus three diagonals is fifteen.

**The three slides.** Cells are not generators; pairs are twice as many arrays; and six extra names are not six extra generators.

**Why it matters.** Every count in the boson block is right in its own register, and every error in that block is a sentence that changes register without saying so. **The cure is to name the object: a cell, a pair, an array, or a generator.**

**And what the shorter ledger bought.** The old ledger needed two more counts to describe two factors. **The model needs one grid, one basis and one dimension**, and the arithmetic that vanished with the factors was never about the algebra.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $E_{ij}$ | the matrix unit, one cell |
| $A_{jk}=E_{jk}-E_{kj}$ | the real array of the plane $\{j,k\}$ |
| $iS_{jk}=i(E_{jk}+E_{kj})$ | the imaginary array of the same plane |
| $D=\operatorname{diag}(-3,1,1,1)$ | the vacuum direction, traceless, $B-L=\tfrac13D$ |
| $iD$, $d_2$, $d_3$ | the three diagonal generators |
| $W_{\mu\nu}=L(e_\mu)R(e_\nu)$ | a word, one of the sixteen products |
| $T^{L}_{a},T^{R}_{a}$ | the six arrays of $\mathfrak{so}(4)$, combinations of the plane arrays |
| cell, pair, array, generator | the four counts, in the sense of this article |

## Further Reading

- [Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html). The fifteen arrays printed one to a display, and the three-step construction of the physics basis from the words.
- [Classification of the Bosons: Sixteen Cells, Fifteen Generators, Nine Massless and Six Massive](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The grid, the block picture and the ledger of the spectrum.
- [The Death of the Primordial Force](the-death-of-the-primordial-force-the-id-condensate-and-the-six-carriers-it-eats.html). The count of generators read as a mass spectrum.
- [The Real $\mathfrak{so}(4)$ Inside the Fifteen](the-su4-model-four-colours-fifteen-generators-one-declaration.html). The section that gives the six arrays their reading.
- [The Weak Force Born as a Side Effect](the-weak-force-born-as-a-side-effect-a-condensate-index-five-ranks-from-three.html). Why six names are not six generators, and what the weak force actually is.
