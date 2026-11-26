# __The Commutation Table of the Fifteen Generators: 225 Entries, 105 Independent, 80 Nonzero, and Five Rules That Produce Them All__

## Introduction

**The question.** The group block of the corpus quotes one bracket where it needs one bracket. That is enough to prove a point about a sector, and it is not enough to see the object every sector sits on: the bracket of every generator with every other generator.

**The answer, in numbers.** The fifteen arrays give $15\times15=225$ ordered brackets. The fifteen brackets of an array with itself vanish, and antisymmetry pairs the remaining $210$, leaving $105$ independent brackets. Of those, $80$ are nonzero and $25$ vanish. **Counting the fifteen self-brackets as well, $120$ entries are distinct up to sign and $40$ of the $225$ entries are zero.** **Every right-hand side is a combination of the same fifteen arrays**, so the table closes on itself and needs no symbol the algebra does not already have.

**The answer, in structure.** Five rules produce all $80$ nonzero entries. Each is one line of matrix algebra. Together they are a presentation of the algebra in the fifteen arrays.

**The method.** Every entry was computed from the $4\times4$ matrices in exact rational arithmetic, pair by pair. The five rules were then implemented a second time, without the matrices, and compared with the $225$ computed entries on all $105$ independent pairs: no disagreement. Nothing in this article is a fit, a sample or an estimate.

## The Six Composites, and the Convention of the Table

**The frame.** The index order is $(t,x,y,z)$. The matrix unit is $E_{jk}$, the real plane is $A_{jk}=E_{jk}-E_{kj}$, the imaginary plane is $iS_{jk}=i(E_{jk}+E_{kj})$, and the bracket is the commutator of the matrices,
$$
[X,Y]=XY-YX .
$$
No other convention enters, and no generator is rescaled.

**The fifteen, in four blocks.**

| block | number | the arrays |
| --- | --- | --- |
| real planes | $6$ | $A_{jk}$, one for each of the six pairs of indices |
| imaginary planes | $6$ | $iS_{jk}$, the same six pairs |
| the corner | $1$ | $iD=i\operatorname{diag}(-3,1,1,1)$ |
| colour diagonals | $2$ | $d_2=i\operatorname{diag}(0,1,-1,0)$, $d_3=i\operatorname{diag}(0,0,1,-1)$ |
**The four blocks hold twelve planes and three diagonals, and nothing else.** **The six arrays $T^{L}_{a}$, $T^{R}_{a}$ are not rows of this table.** Each is half a sum or difference of two planes, so its brackets are the brackets of Part I, and §*The Six Arrays Outside the Table* says why they are printed elsewhere.

**The three diagonals are one family.** They are the diagonal generators of $\mathfrak{su}(4)$, and their eigenvalues are all that a bracket with a diagonal reads.

**Only one order is printed.** Since $[Y,X]=-[X,Y]$, the $210$ off-diagonal brackets are $105$ brackets and their negatives, and every table below lists a pair once, with the two arrays in the order of the block list above. The fifteen self-brackets are not printed at all: they are zero by antisymmetry, and they are counted in §*The Forty Zeros*.

**The coefficients are few.** In the $225$ entries exactly ten signed values occur:
$$
\pm\tfrac23,\quad \pm1,\quad \pm\tfrac43,\quad \pm2,\quad \pm4 .
$$
**Five magnitudes, each a rational with denominator $1$ or $3$**, and no other number appears anywhere in the table. **The half and the third of the old table came from the six halves**, whose normalisation is the half and whose planes are the sums.

**Most entries are short, and shorter than they were.** Seventy-six of the $80$ nonzero brackets carry one term, one carries two, and three carry three. **The three are the $\{t,k\}$ planes paired with their own imaginary partner**, whose answer needs all three diagonal directions; **the single two-term entry is $[A_{xz},iS_{xz}]=2\,d_2+2\,d_3$**, the one diagonal that needs two of the three to be named.

## The Five Rules

**Five rules, and the table is finished.** In this section $j$, $k$, $l$ are distinct indices, $A_{kj}=-A_{jk}$ is understood throughout, and $iS_{kj}=+iS_{jk}$ is understood throughout.

**Rule 1, two real planes.**
$$
[A_{jk},A_{kl}]=A_{jl}.
$$
**Two real planes with no common index commute**, and that is the only zero of their block.

**Rule 2, two imaginary planes.**
$$
[iS_{jk},iS_{kl}]=-A_{jl}.
$$
**The minus sign is the $i^{2}$.** The two imaginary units multiply to $-1$, and the answer is a real plane.

**Rule 3, a real plane and an imaginary one.**
$$
[A_{jk},iS_{kl}]=iS_{jl}.
$$
**The free index moves and the type is kept.** The two shapes this rule does not cover are the pair with no common index, which gives zero, and the equal pair, which is Rule 4.

**Rule 4, a plane and its own partner.**
$$
[A_{jk},iS_{jk}]=2i\bigl(E_{jj}-E_{kk}\bigr).
$$
**This is the only bracket among the twelve planes whose answer is not a plane.** The six entries it produces are the entire source of the three diagonal directions in the table, and that is why the Cartan is not an independent fifth block but a consequence of the planes.

**Rule 5, a plane and a diagonal.** For a diagonal $i\Lambda$ with eigenvalues $\lambda_{j}$,
$$
[A_{jk},i\Lambda]=(\lambda_{k}-\lambda_{j})\,iS_{jk},
\qquad
[iS_{jk},i\Lambda]=-(\lambda_{k}-\lambda_{j})\,A_{jk}.
$$
**One rule, three diagonals, and the coefficients $4$, $2$ and $1$ are eigenvalue spacings.** The corner has spacing $4$ through $t$ and spacing $0$ inside colour, which is why it meets three planes and not six. The colour diagonals have spacings $1$ and $2$, and each meets five planes of the six.

**There is no sixth rule, and that is a result.** A bracket with one of the six $\mathfrak{so}(4)$ arrays is the average of two plane brackets, because each of them is half a sum or difference of two planes. **A sixth rule would be Rules 1 to 5 applied twice**, and §*The Six Arrays Outside the Table* does exactly that once, for the record.

**What the absence means.** A table that needs five rules is a table of one algebra. **A table that needed a sixth, with a sign of its own and a commutativity of its own, would be a table of a product** — and this model is not one.

## Part I. Two Real Planes

**Twelve nonzero entries, three zeros, and only $\pm1$.** The block is $\mathfrak{so}(4)$: the six real planes are closed, their brackets never leave them, and every structure constant is an integer.

| $X$ | $Y$ | $[X,Y]$ |
| --- | --- | --- |
| $A_{tx}$ | $A_{ty}$ | $-A_{xy}$ |
| $A_{tx}$ | $A_{tz}$ | $-A_{xz}$ |
| $A_{tx}$ | $A_{xy}$ | $A_{ty}$ |
| $A_{tx}$ | $A_{xz}$ | $A_{tz}$ |
| $A_{ty}$ | $A_{tz}$ | $-A_{yz}$ |
| $A_{ty}$ | $A_{xy}$ | $-A_{tx}$ |
| $A_{ty}$ | $A_{yz}$ | $A_{tz}$ |
| $A_{tz}$ | $A_{xz}$ | $-A_{tx}$ |
| $A_{tz}$ | $A_{yz}$ | $-A_{ty}$ |
| $A_{xy}$ | $A_{xz}$ | $-A_{yz}$ |
| $A_{xy}$ | $A_{yz}$ | $A_{xz}$ |
| $A_{xz}$ | $A_{yz}$ | $-A_{xy}$ |

**The three zeros are the three pairs of complementary planes**, $\{t,x\}$ with $\{y,z\}$, $\{t,y\}$ with $\{x,z\}$ and $\{t,z\}$ with $\{x,y\}$. **Planes with no common index act on disjoint entries and commute**, and no other pair of real planes does.

## Part II. Two Imaginary Planes

**The same twelve and the same three zeros, with the answer on the other side.** The imaginary block has exactly the support of the real one, and its image is the real planes.

| $X$ | $Y$ | $[X,Y]$ |
| --- | --- | --- |
| $iS_{tx}$ | $iS_{ty}$ | $-A_{xy}$ |
| $iS_{tx}$ | $iS_{tz}$ | $-A_{xz}$ |
| $iS_{tx}$ | $iS_{xy}$ | $-A_{ty}$ |
| $iS_{tx}$ | $iS_{xz}$ | $-A_{tz}$ |
| $iS_{ty}$ | $iS_{tz}$ | $-A_{yz}$ |
| $iS_{ty}$ | $iS_{xy}$ | $-A_{tx}$ |
| $iS_{ty}$ | $iS_{yz}$ | $-A_{tz}$ |
| $iS_{tz}$ | $iS_{xz}$ | $-A_{tx}$ |
| $iS_{tz}$ | $iS_{yz}$ | $-A_{ty}$ |
| $iS_{xy}$ | $iS_{xz}$ | $-A_{yz}$ |
| $iS_{xy}$ | $iS_{yz}$ | $-A_{xz}$ |
| $iS_{xz}$ | $iS_{yz}$ | $-A_{xy}$ |

**The nine imaginary arrays are not a subalgebra**, because the bracket of two of them is real. **The six real planes are one**, because the bracket of two of them is real again. **The Cartan split of $\mathfrak{su}(4)$ is therefore lopsided**: one half closes, the other half falls back on the first.

## Part III. A Real Plane and an Imaginary Plane

**Thirty nonzero entries of thirty-six, and six of them are the whole story of the diagonals.** The six zeros are the complementary pairs of different type. The six exceptions to Rule 3 are the equal planes, and those six are the only entries of the twelve-plane block whose answer is not a plane.

| $X$ | $Y$ | $[X,Y]$ |
| --- | --- | --- |
| $A_{tx}$ | $iS_{tx}$ | $-\tfrac{2}{3}\,iD - \tfrac{4}{3}\,d_{2} - \tfrac{2}{3}\,d_{3}$ |
| $A_{tx}$ | $iS_{ty}$ | $-iS_{xy}$ |
| $A_{tx}$ | $iS_{tz}$ | $-iS_{xz}$ |
| $A_{tx}$ | $iS_{xy}$ | $iS_{ty}$ |
| $A_{tx}$ | $iS_{xz}$ | $iS_{tz}$ |
| $A_{ty}$ | $iS_{tx}$ | $-iS_{xy}$ |
| $A_{ty}$ | $iS_{ty}$ | $-\tfrac{2}{3}\,iD + \tfrac{2}{3}\,d_{2} - \tfrac{2}{3}\,d_{3}$ |
| $A_{ty}$ | $iS_{tz}$ | $-iS_{yz}$ |
| $A_{ty}$ | $iS_{xy}$ | $iS_{tx}$ |
| $A_{ty}$ | $iS_{yz}$ | $iS_{tz}$ |
| $A_{tz}$ | $iS_{tx}$ | $-iS_{xz}$ |
| $A_{tz}$ | $iS_{ty}$ | $-iS_{yz}$ |
| $A_{tz}$ | $iS_{tz}$ | $-\tfrac{2}{3}\,iD + \tfrac{2}{3}\,d_{2} + \tfrac{4}{3}\,d_{3}$ |
| $A_{tz}$ | $iS_{xz}$ | $iS_{tx}$ |
| $A_{tz}$ | $iS_{yz}$ | $iS_{ty}$ |
| $A_{xy}$ | $iS_{tx}$ | $-iS_{ty}$ |
| $A_{xy}$ | $iS_{ty}$ | $iS_{tx}$ |
| $A_{xy}$ | $iS_{xy}$ | $2\,d_{2}$ |
| $A_{xy}$ | $iS_{xz}$ | $-iS_{yz}$ |
| $A_{xy}$ | $iS_{yz}$ | $iS_{xz}$ |
| $A_{xz}$ | $iS_{tx}$ | $-iS_{tz}$ |
| $A_{xz}$ | $iS_{tz}$ | $iS_{tx}$ |
| $A_{xz}$ | $iS_{xy}$ | $-iS_{yz}$ |
| $A_{xz}$ | $iS_{xz}$ | $2\,d_{2} + 2\,d_{3}$ |
| $A_{xz}$ | $iS_{yz}$ | $iS_{xy}$ |
| $A_{yz}$ | $iS_{ty}$ | $-iS_{tz}$ |
| $A_{yz}$ | $iS_{tz}$ | $iS_{ty}$ |
| $A_{yz}$ | $iS_{xy}$ | $-iS_{xz}$ |
| $A_{yz}$ | $iS_{xz}$ | $iS_{xy}$ |
| $A_{yz}$ | $iS_{yz}$ | $2\,d_{3}$ |

**The six diagonal answers, written in the basis $iD$, $d_2$, $d_3$.** Rule 4 gives a difference of two matrix units, and the same difference reads:

| pair | $[A_{jk},iS_{jk}]$ |
| --- | --- |
| $\{t,x\}$ | $-\tfrac{2}{3}\,iD - \tfrac{4}{3}\,d_{2} - \tfrac{2}{3}\,d_{3}$ |
| $\{t,y\}$ | $-\tfrac{2}{3}\,iD + \tfrac{2}{3}\,d_{2} - \tfrac{2}{3}\,d_{3}$ |
| $\{t,z\}$ | $-\tfrac{2}{3}\,iD + \tfrac{2}{3}\,d_{2} + \tfrac{4}{3}\,d_{3}$ |
| $\{x,y\}$ | $2\,d_{2}$ |
| $\{x,z\}$ | $2\,d_{2} + 2\,d_{3}$ |
| $\{y,z\}$ | $2\,d_{3}$ |

**The corner enters the three $\{t,k\}$ pairs with one coefficient, $-\tfrac23$, and never a colour pair.** The reason is visible in Rule 5: the corner has a single distinguished eigenvalue, at $t$, so it separates $t$ from everything and separates nothing inside colour. **The colour pairs give pure colour diagonals, and their coefficients $2$ are the spacings of $d_2$ and $d_3$.**

## Part IV. A Plane and a Diagonal

### The Corner

**Six arrays meet the corner: the three planes through $t$ and their three imaginary partners.** The three colour planes and both colour diagonals never do. **The six $\mathfrak{so}(4)$ arrays meet it too, and each bracket is the average of two of the six rows below** — no new coefficient, which is why they need no table of their own.

| $X$ | $iD$ | $[X,iD]$ |
| --- | --- | --- |
| $A_{tx}$ | $iD$ | $4\,iS_{tx}$ |
| $A_{ty}$ | $iD$ | $4\,iS_{ty}$ |
| $A_{tz}$ | $iD$ | $4\,iS_{tz}$ |
| $iS_{tx}$ | $iD$ | $-4\,A_{tx}$ |
| $iS_{ty}$ | $iD$ | $-4\,A_{ty}$ |
| $iS_{tz}$ | $iD$ | $-4\,A_{tz}$ |

**The coefficient $4$ is the eigenvalue spacing from $-3$ to $1$.** No other bracket of the table has it, so the corner can be recognized in a bracket by its coefficient alone.

### The Two Colour Diagonals

**Each colour diagonal meets five planes of its type and misses one.** $d_2$ misses $A_{tz}$ and $iS_{tz}$, because $t$ and $z$ are its two fixed lines. $d_3$ misses $A_{tx}$ and $iS_{tx}$, for the same reason with $x$ in place of $z$.

| $X$ | $d_2$ | $[X,d_2]$ |
| --- | --- | --- |
| $A_{tx}$ | $d_{2}$ | $iS_{tx}$ |
| $A_{ty}$ | $d_{2}$ | $-iS_{ty}$ |
| $A_{xy}$ | $d_{2}$ | $-2\,iS_{xy}$ |
| $A_{xz}$ | $d_{2}$ | $-iS_{xz}$ |
| $A_{yz}$ | $d_{2}$ | $iS_{yz}$ |

| $X$ | $d_3$ | $[X,d_3]$ |
| --- | --- | --- |
| $A_{ty}$ | $d_{3}$ | $iS_{ty}$ |
| $A_{tz}$ | $d_{3}$ | $-iS_{tz}$ |
| $A_{xy}$ | $d_{3}$ | $iS_{xy}$ |
| $A_{xz}$ | $d_{3}$ | $-iS_{xz}$ |
| $A_{yz}$ | $d_{3}$ | $-2\,iS_{yz}$ |

| $X$ | $d_2$ | $[X,d_2]$ |
| --- | --- | --- |
| $iS_{tx}$ | $d_{2}$ | $-A_{tx}$ |
| $iS_{ty}$ | $d_{2}$ | $A_{ty}$ |
| $iS_{xy}$ | $d_{2}$ | $2\,A_{xy}$ |
| $iS_{xz}$ | $d_{2}$ | $A_{xz}$ |
| $iS_{yz}$ | $d_{2}$ | $-A_{yz}$ |

| $X$ | $d_3$ | $[X,d_3]$ |
| --- | --- | --- |
| $iS_{ty}$ | $d_{3}$ | $-A_{ty}$ |
| $iS_{tz}$ | $d_{3}$ | $A_{tz}$ |
| $iS_{xy}$ | $d_{3}$ | $-A_{xy}$ |
| $iS_{xz}$ | $d_{3}$ | $A_{xz}$ |
| $iS_{yz}$ | $d_{3}$ | $2\,A_{yz}$ |

**The coefficient $2$ marks the plane that leaves both fixed lines**, the coefficient $1$ marks a plane that leaves one of them, and $0$ marks the plane that lies inside a fixed line. **The three coefficients are the three possible spacings of a two-line plane against a two-line diagonal.**

### The Three Diagonals with Each Other

**They commute.** $[iD,d_2]=[iD,d_3]=[d_2,d_3]=0$. The three are one Cartan subalgebra, no bracket of two of them produces the third, and this is the only block of the table whose every entry is zero with nothing to add.

## The Six Arrays Outside the Table

**One block is deliberately absent, and its absence is a statement about the model.**

**The six arrays.** The corpus still prints the six arrays

$$
T^{L}_{a}=-\tfrac12\bigl(A_{ta}+A_{bc}\bigr),\qquad
T^{R}_{a}=-\tfrac12\bigl(A_{ta}-A_{bc}\bigr),
$$

with $(a,b,c)$ cyclic in $(x,y,z)$. **They are not generators of this model.** They are a rotated basis of the six-dimensional real subspace $\operatorname{span}\{A_{ab}\}=\mathfrak{so}(4)\subset\mathfrak{su}(4)$, and they add no direction: the printed arrays span fifteen dimensions. **So a bracket of two of them is a bracket of two plane arrays, and every entry is already in Part I or Part II.**

**Their brackets, from the five rules and nothing more.** Because each is half a sum or difference of two planes,

$$
[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}T^{L}_{c},\qquad
[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}T^{R}_{c},\qquad
[T^{L}_{a},T^{R}_{b}]=0 .
$$

**The first two lines are Rules 1 and 2 read on the half-sum and half-difference**, and the third is the statement that a self-dual and an anti-self-dual two-form commute — **which is also the statement that $\mathfrak{k}_L$ and $\mathfrak{k}_R$ are independent factors of $\mathfrak{so}(4)$.**

**What that does not buy.** A direct product of two $\mathfrak{su}(2)$'s **inside** $\mathfrak{su}(4)$ is not a pair of group factor **beside** it. **The closure is real, the commutativity is real, and the factor reading is not available**: the rank of the algebra is three, the rank of the subspace is two, and no breaking of the fifteen produces five. **That is the whole reason this article has five rules and not six**, and the reason the six arrays are printed in [Construction of the AXF Matrices](construction-of-the-axf-matrices-of-the-fifteen-generators.html) as a remark rather than as a block of the table.

## The Forty Zeros

**The zeros are as structured as the numbers.** Forty independent brackets vanish, and every one of them is one of seven statements.

| family | count | the reason |
| --- | --- | --- |
| an array with itself | $15$ | antisymmetry |
| two real planes with no common index | $3$ | disjoint entries, Rule 1 |
| two imaginary planes with no common index | $3$ | disjoint entries, Rule 2 |
| a real and an imaginary plane with no common index | $6$ | disjoint entries, Rule 3 |
| a plane inside a fixed line of a colour diagonal | $4$ | the spacing is $0$, Rule 5 |
| a colour plane with the corner | $6$ | the corner has no spacing inside colour, Rule 5 |
| the three diagonals with each other | $3$ | the Cartan is abelian |

**No zero is an accident, and the list has seven lines and one row that says why.** $15+3+3+6+4+6+3=40$. **A reader who knows the eigenvalues of the three diagonals predicts all twenty-five off-diagonal zeros without computing a single matrix.**

## What the Table Says That No Single Bracket Says

**The real planes are a subalgebra and the imaginary ones are not.** Six generators close on themselves; nine do not, and their product falls back on the six. **The compact form of $\mathfrak{su}(4)$ is not symmetric across the Cartan split**, and this block is where that asymmetry is visible.

**The twelve plane arrays are closed except on six pairs, and the six are exactly the pairs that generate the Cartan.** Any reading in which the diagonal directions are extra data is contradicted here: they are produced by $[A_{jk},iS_{jk}]$ and by nothing else among the planes.

**The corner meets six brackets as a factor and appears in three as an answer.** It meets the three $\{t,k\}$ planes and their three imaginary partners, and it comes back from those three equal-plane brackets. **The three colour planes and the two colour diagonals never see it at all**, which is the algebraic content of the phrase that the corner is the lepton-line direction.

**The six real planes are a subalgebra of rank two, and it is not a factor.** $\operatorname{span}\{A_{ab}\}=\mathfrak{so}(4)$: six dimensions, closed, abelian when written as $\mathfrak{k}_L\oplus\mathfrak{k}_R$ — **and still a subspace of the fifteen.** That distinction is this article's one warning: **closure and commutativity are algebraic facts, and being a group factor is not.**

**Every coefficient is $\pm\tfrac23$, $\pm1$, $\pm\tfrac43$, $\pm2$ or $\pm4$.** A table whose coefficients are five rationals is a table that can be checked by hand, and this one can.

## The Checks

| what | result |
| --- | --- |
| the $225$ ordered brackets, from the matrices | every one inside the span of the fifteen |
| the five rules, against the $225$ entries | $105$ independent pairs, $0$ disagreements |
| antisymmetry | holds on all $225$ |
| the Jacobi identity | holds identically: the bracket is a commutator of matrices |
| nonzero entries | $80$ of the $105$ independent brackets |
| zero entries | $25$ off-diagonal, plus the $15$ self-brackets: $40$ of the $225$ entries, in the seven families above |
| coefficient set | ten signed values, five magnitudes |
| term count | $76$ one-term, $1$ two-term, $3$ three-term |
| nonzero per block | $12+12+30+3+5+5+3+5+5+0+0+0=80$ |
| the six $\mathfrak{so}(4)$ arrays in the fifteen | $0$ entries outside the span |

**The count by block is the check on the tables themselves.** Parts I to IV contribute $12+12+30+3+5+5+3+5+5+0+0+0=80$. **The tables print exactly that many rows.**

**No pass exceeded thirty entries.** Each block was recomputed and compared in its own pass, and the largest single pass is the thirty-entry real-imaginary block.

## Summary

**Fifteen arrays, $225$ ordered brackets, $105$ independent, $80$ nonzero, $25$ of the zeros off the diagonal and $40$ in all.** Five rules produce all of them:
$$
[A_{jk},A_{kl}]=A_{jl},
\qquad
[iS_{jk},iS_{kl}]=-A_{jl},
\qquad
[A_{jk},iS_{kl}]=iS_{jl},
$$
$$
[A_{jk},iS_{jk}]=2i(E_{jj}-E_{kk}),
\qquad
[A_{jk},i\Lambda]=(\lambda_{k}-\lambda_{j})\,iS_{jk},
\qquad
[iS_{jk},i\Lambda]=-(\lambda_{k}-\lambda_{j})\,A_{jk}.
$$

**The real planes close, the imaginary ones do not, the corner is produced by the planes rather than added to them, and the six $\mathfrak{so}(4)$ arrays are a basis of the real planes and nothing more.** Those four sentences are the table.

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $E_{jk}$ | the matrix unit of $M_4(\mathbb{C})$, indices in the order $(t,x,y,z)$ |
| $A_{jk}=E_{jk}-E_{kj}$ | the real antisymmetric array of the plane $\{j,k\}$ |
| $S_{jk}=E_{jk}+E_{kj}$ | the real symmetric partner; $iS_{jk}$ is the algebra element |
| $iD$ | the corner, $i\operatorname{diag}(-3,1,1,1)$ |
| $d_2$, $d_3$ | the colour diagonals, $i\operatorname{diag}(0,1,-1,0)$ and $i\operatorname{diag}(0,0,1,-1)$ |
| $T^{L}_{a}$, $T^{R}_{a}$ | the six $\mathfrak{so}(4)$ arrays, $-\tfrac12(A_{ta}\pm A_{bc})$, $(a,b,c)$ cyclic; not generators |
| $[X,Y]$ | $XY-YX$, the commutator of the matrices |
| $\lambda_{j}$ | the eigenvalue of the diagonal $i\Lambda$ at the index $j$ |
| $\epsilon_{abc}$ | the Levi-Civita symbol of the three colour labels |
| complementary planes | two planes of $\{t,x,y,z\}$ with no common index |

## Further Reading

- J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972 — structure constants, the Chevalley basis, and a table of brackets read as a presentation of the algebra.
- H. Georgi, *Lie Algebras in Particle Physics*, Benjamin Cummings, 1982 — the physicists' conventions, the $\tfrac12$ of a weak generator, and the sign of $\epsilon_{abc}$.
- R. Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications*, Wiley, 1974 — compact real forms, the splitting $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, and the inertia that separates the two halves.
- The corpus: [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) for the exponential of each generator; [The Construction of the AXF Matrices of the Fifteen Generators](construction-of-the-axf-matrices-of-the-fifteen-generators.html) for the arrays themselves; [The Fifteen AXF Matrices of the Bosons in Detail](the-15-axf-matrices-of-the-bosons-in-detail.html) for one subsection per generator; [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html) for the cell each array occupies; [The Counts of the Fifteen](the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.html) for the count that ends at fifteen.
