# __The Commutation Table of the Twenty-One Generators: 441 Entries, 231 Independent, 164 Nonzero, and Six Rules That Produce Them All__

## Introduction

**The question.** The group block of the corpus quotes one bracket where it needs one bracket. That is enough to prove a point about a sector, and it is not enough to see the object every sector sits on: the bracket of every generator with every other generator.

**The answer, in numbers.** The twenty-one arrays give $21\times21=441$ ordered brackets. Antisymmetry leaves $231$ independent ones. Of those, $164$ are nonzero and $67$ vanish. Every right-hand side is a combination of the same fifteen algebra elements, so the table needs no symbol that the algebra does not already have.

**The answer, in structure.** Six rules produce all $164$ nonzero entries. Each is one line of matrix algebra. Together they are a presentation of the algebra in the twenty-one arrays.

**The method.** Every entry was computed from the $4\times4$ matrices in exact rational arithmetic, pair by pair. The six rules were then implemented a second time, without the matrices, and compared with the $441$ computed entries on all $210$ independent pairs: no disagreement. Nothing in this article is a fit, a sample or an estimate.

## The Twenty-One, and the Convention of the Table

**The frame.** The index order is $(t,x,y,z)$. The matrix unit is $E_{jk}$, the real plane is $A_{jk}=E_{jk}-E_{kj}$, the imaginary plane is $iS_{jk}=i(E_{jk}+E_{kj})$, and the bracket is the commutator of the matrices,
$$
[X,Y]=XY-YX .
$$
No other convention enters, and no generator is rescaled.

**The twenty-one, in six blocks.**

| block | number | the arrays |
| --- | --- | --- |
| real planes | $6$ | $A_{jk}$, one for each of the six pairs of indices |
| imaginary planes | $6$ | $iS_{jk}$, the same six pairs |
| the corner | $1$ | $iD=i\operatorname{diag}(-3,1,1,1)$ |
| colour diagonals | $2$ | $d_2=i\operatorname{diag}(0,1,-1,0)$, $d_3=i\operatorname{diag}(0,0,1,-1)$ |
| left triple | $3$ | $T^{L}_{a}=-\tfrac12\bigl(A_{ta}+A_{bc}\bigr)$ |
| right triple | $3$ | $T^{R}_{a}=-\tfrac12\bigl(A_{ta}-A_{bc}\bigr)$ |

**The last two rows use $(a,b,c)$ cyclic in $(x,y,z)$.** The three weak arrays of each triple are half sums of two planes, one leptoquark plane and one colour plane, and that single fact decides every bracket they take part in.

**The three diagonals are one family.** They are the diagonal generators of $\mathfrak{su}(4)$, and their eigenvalues are all that a bracket with a diagonal reads.

**Only one order is printed.** Since $[Y,X]=-[X,Y]$, the $441$ entries are $231$ entries and their negatives, and every table below lists a pair once, with the two arrays in the order of the block list above.

**The coefficients are few.** In the $441$ entries exactly fourteen signed values occur:
$$
\pm\tfrac13,\quad \pm\tfrac12,\quad \pm\tfrac23,\quad \pm1,\quad \pm\tfrac43,\quad \pm2,\quad \pm4 .
$$
**Seven magnitudes, each a rational with denominator $1$, $2$ or $3$**, and no other number appears anywhere in the table.

**Most entries are short.** Ninety of the $164$ nonzero brackets carry one term, sixty-five carry two and nine carry three. The nine with three terms are the three $\{t,k\}$ planes paired with their own imaginary partner, and the six brackets of an imaginary plane with the weak array of its own label.

## The Six Rules

**Six rules, and the table is finished.** In this section $j$, $k$, $l$ are distinct indices, $A_{kj}=-A_{jk}$ is understood throughout, and $iS_{kj}=+iS_{jk}$ is understood throughout.

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

**Rule 6, the two triples.**
$$
[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}T^{L}_{c},
\qquad
[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}T^{R}_{c},
\qquad
[T^{L}_{a},T^{R}_{b}]=0 .
$$
**A weak array is half a sum of two planes, so every other bracket with a weak array is the average of two plane brackets.** Rule 6 adds no coefficient that Rules 1 to 5 do not already contain, and Parts VI and VII are that statement spelled out.

**The two triples commute.** The nine zeros of $[T^{L}_{a},T^{R}_{b}]=0$ are the table's statement that $\mathfrak{su}(2)_L$ and $\mathfrak{su}(2)_R$ are independent factors and not one factor read twice.

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

**Among the fifteen of $\mathfrak{su}(4)$, six meet the corner: the three planes through $t$ and their three imaginary partners.** The three colour planes and both colour diagonals never do. The six weak arrays do meet it, and their brackets are Part VII.

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

## Part V. The Two Triples

**Left closes with $+\epsilon$ and right closes with $-\epsilon$.** The sign is the whole difference between the two triples at the level of the algebra, and it is the same sign that separates $T^{L}$ from $T^{R}$ entry by entry.

| $X$ | $Y$ | $[X,Y]$ |
| --- | --- | --- |
| $T^{L}_{x}$ | $T^{L}_{y}$ | $-\tfrac{1}{2}\,A_{tz} - \tfrac{1}{2}\,A_{xy}$ |
| $T^{L}_{x}$ | $T^{L}_{z}$ | $\tfrac{1}{2}\,A_{ty} - \tfrac{1}{2}\,A_{xz}$ |
| $T^{L}_{y}$ | $T^{L}_{z}$ | $-\tfrac{1}{2}\,A_{tx} - \tfrac{1}{2}\,A_{yz}$ |

| $X$ | $Y$ | $[X,Y]$ |
| --- | --- | --- |
| $T^{R}_{x}$ | $T^{R}_{y}$ | $\tfrac{1}{2}\,A_{tz} - \tfrac{1}{2}\,A_{xy}$ |
| $T^{R}_{x}$ | $T^{R}_{z}$ | $-\tfrac{1}{2}\,A_{ty} - \tfrac{1}{2}\,A_{xz}$ |
| $T^{R}_{y}$ | $T^{R}_{z}$ | $\tfrac{1}{2}\,A_{tx} - \tfrac{1}{2}\,A_{yz}$ |

**The nine cross brackets vanish, and they are the only block of the table that is entirely zero without being a diagonal.**

| $X$ | $Y$ | $[X,Y]$ |
| --- | --- | --- |


## Part VI. A Weak Array and a Plane

**A real plane either is one of the two planes of the weak array or it is not.** If it is, the bracket vanishes: six entries for each triple, twelve in all. If it is not, the bracket is half a sum of two planes of the same type.

| $X$ | $A$ | $[X,A]$ |
| --- | --- | --- |
| $A_{tx}$ | $T^{L}_{y}$ | $\tfrac{1}{2}\,A_{tz} + \tfrac{1}{2}\,A_{xy}$ |
| $A_{tx}$ | $T^{L}_{z}$ | $-\tfrac{1}{2}\,A_{ty} + \tfrac{1}{2}\,A_{xz}$ |
| $A_{ty}$ | $T^{L}_{x}$ | $-\tfrac{1}{2}\,A_{tz} - \tfrac{1}{2}\,A_{xy}$ |
| $A_{ty}$ | $T^{L}_{z}$ | $\tfrac{1}{2}\,A_{tx} + \tfrac{1}{2}\,A_{yz}$ |
| $A_{tz}$ | $T^{L}_{x}$ | $\tfrac{1}{2}\,A_{ty} - \tfrac{1}{2}\,A_{xz}$ |
| $A_{tz}$ | $T^{L}_{y}$ | $-\tfrac{1}{2}\,A_{tx} - \tfrac{1}{2}\,A_{yz}$ |
| $A_{xy}$ | $T^{L}_{x}$ | $\tfrac{1}{2}\,A_{ty} - \tfrac{1}{2}\,A_{xz}$ |
| $A_{xy}$ | $T^{L}_{y}$ | $-\tfrac{1}{2}\,A_{tx} - \tfrac{1}{2}\,A_{yz}$ |
| $A_{xz}$ | $T^{L}_{x}$ | $\tfrac{1}{2}\,A_{tz} + \tfrac{1}{2}\,A_{xy}$ |
| $A_{xz}$ | $T^{L}_{z}$ | $-\tfrac{1}{2}\,A_{tx} - \tfrac{1}{2}\,A_{yz}$ |
| $A_{yz}$ | $T^{L}_{y}$ | $\tfrac{1}{2}\,A_{tz} + \tfrac{1}{2}\,A_{xy}$ |
| $A_{yz}$ | $T^{L}_{z}$ | $-\tfrac{1}{2}\,A_{ty} + \tfrac{1}{2}\,A_{xz}$ |

| $X$ | $A$ | $[X,A]$ |
| --- | --- | --- |
| $A_{tx}$ | $T^{R}_{y}$ | $-\tfrac{1}{2}\,A_{tz} + \tfrac{1}{2}\,A_{xy}$ |
| $A_{tx}$ | $T^{R}_{z}$ | $\tfrac{1}{2}\,A_{ty} + \tfrac{1}{2}\,A_{xz}$ |
| $A_{ty}$ | $T^{R}_{x}$ | $\tfrac{1}{2}\,A_{tz} - \tfrac{1}{2}\,A_{xy}$ |
| $A_{ty}$ | $T^{R}_{z}$ | $-\tfrac{1}{2}\,A_{tx} + \tfrac{1}{2}\,A_{yz}$ |
| $A_{tz}$ | $T^{R}_{x}$ | $-\tfrac{1}{2}\,A_{ty} - \tfrac{1}{2}\,A_{xz}$ |
| $A_{tz}$ | $T^{R}_{y}$ | $\tfrac{1}{2}\,A_{tx} - \tfrac{1}{2}\,A_{yz}$ |
| $A_{xy}$ | $T^{R}_{x}$ | $\tfrac{1}{2}\,A_{ty} + \tfrac{1}{2}\,A_{xz}$ |
| $A_{xy}$ | $T^{R}_{y}$ | $-\tfrac{1}{2}\,A_{tx} + \tfrac{1}{2}\,A_{yz}$ |
| $A_{xz}$ | $T^{R}_{x}$ | $\tfrac{1}{2}\,A_{tz} - \tfrac{1}{2}\,A_{xy}$ |
| $A_{xz}$ | $T^{R}_{z}$ | $-\tfrac{1}{2}\,A_{tx} + \tfrac{1}{2}\,A_{yz}$ |
| $A_{yz}$ | $T^{R}_{y}$ | $\tfrac{1}{2}\,A_{tz} - \tfrac{1}{2}\,A_{xy}$ |
| $A_{yz}$ | $T^{R}_{z}$ | $-\tfrac{1}{2}\,A_{ty} - \tfrac{1}{2}\,A_{xz}$ |

**With the imaginary planes there is no zero at all**: eighteen entries for each triple, and every one of them is a combination of imaginary planes.

| $X$ | $iS$ | $[X,iS]$ |
| --- | --- | --- |
| $iS_{tx}$ | $T^{L}_{x}$ | $-\tfrac{1}{3}\,iD - \tfrac{2}{3}\,d_{2} - \tfrac{1}{3}\,d_{3}$ |
| $iS_{tx}$ | $T^{L}_{y}$ | $\tfrac{1}{2}\,iS_{tz} - \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{tx}$ | $T^{L}_{z}$ | $-\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |
| $iS_{ty}$ | $T^{L}_{x}$ | $-\tfrac{1}{2}\,iS_{tz} - \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{ty}$ | $T^{L}_{y}$ | $-\tfrac{1}{3}\,iD + \tfrac{1}{3}\,d_{2} - \tfrac{1}{3}\,d_{3}$ |
| $iS_{ty}$ | $T^{L}_{z}$ | $\tfrac{1}{2}\,iS_{tx} - \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{tz}$ | $T^{L}_{x}$ | $\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |
| $iS_{tz}$ | $T^{L}_{y}$ | $-\tfrac{1}{2}\,iS_{tx} - \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{tz}$ | $T^{L}_{z}$ | $-\tfrac{1}{3}\,iD + \tfrac{1}{3}\,d_{2} + \tfrac{2}{3}\,d_{3}$ |
| $iS_{xy}$ | $T^{L}_{x}$ | $\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |
| $iS_{xy}$ | $T^{L}_{y}$ | $\tfrac{1}{2}\,iS_{tx} + \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{xy}$ | $T^{L}_{z}$ | $d_{2}$ |
| $iS_{xz}$ | $T^{L}_{x}$ | $\tfrac{1}{2}\,iS_{tz} + \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{xz}$ | $T^{L}_{y}$ | $-d_{2} - d_{3}$ |
| $iS_{xz}$ | $T^{L}_{z}$ | $\tfrac{1}{2}\,iS_{tx} - \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{yz}$ | $T^{L}_{x}$ | $d_{3}$ |
| $iS_{yz}$ | $T^{L}_{y}$ | $\tfrac{1}{2}\,iS_{tz} - \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{yz}$ | $T^{L}_{z}$ | $\tfrac{1}{2}\,iS_{ty} + \tfrac{1}{2}\,iS_{xz}$ |

| $X$ | $iS$ | $[X,iS]$ |
| --- | --- | --- |
| $iS_{tx}$ | $T^{R}_{x}$ | $-\tfrac{1}{3}\,iD - \tfrac{2}{3}\,d_{2} - \tfrac{1}{3}\,d_{3}$ |
| $iS_{tx}$ | $T^{R}_{y}$ | $-\tfrac{1}{2}\,iS_{tz} - \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{tx}$ | $T^{R}_{z}$ | $\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |
| $iS_{ty}$ | $T^{R}_{x}$ | $\tfrac{1}{2}\,iS_{tz} - \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{ty}$ | $T^{R}_{y}$ | $-\tfrac{1}{3}\,iD + \tfrac{1}{3}\,d_{2} - \tfrac{1}{3}\,d_{3}$ |
| $iS_{ty}$ | $T^{R}_{z}$ | $-\tfrac{1}{2}\,iS_{tx} - \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{tz}$ | $T^{R}_{x}$ | $-\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |
| $iS_{tz}$ | $T^{R}_{y}$ | $\tfrac{1}{2}\,iS_{tx} - \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{tz}$ | $T^{R}_{z}$ | $-\tfrac{1}{3}\,iD + \tfrac{1}{3}\,d_{2} + \tfrac{2}{3}\,d_{3}$ |
| $iS_{xy}$ | $T^{R}_{x}$ | $\tfrac{1}{2}\,iS_{ty} + \tfrac{1}{2}\,iS_{xz}$ |
| $iS_{xy}$ | $T^{R}_{y}$ | $\tfrac{1}{2}\,iS_{tx} - \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{xy}$ | $T^{R}_{z}$ | $-d_{2}$ |
| $iS_{xz}$ | $T^{R}_{x}$ | $\tfrac{1}{2}\,iS_{tz} - \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{xz}$ | $T^{R}_{y}$ | $d_{2} + d_{3}$ |
| $iS_{xz}$ | $T^{R}_{z}$ | $\tfrac{1}{2}\,iS_{tx} + \tfrac{1}{2}\,iS_{yz}$ |
| $iS_{yz}$ | $T^{R}_{x}$ | $-d_{3}$ |
| $iS_{yz}$ | $T^{R}_{y}$ | $\tfrac{1}{2}\,iS_{tz} + \tfrac{1}{2}\,iS_{xy}$ |
| $iS_{yz}$ | $T^{R}_{z}$ | $\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |

**The coefficients $\tfrac12$ are the $\tfrac12$ of the definition of $T^{L}$ and $T^{R}$ and nothing else.** An entry with a single half multiplying one plane is a pair where the two planes of the weak array contribute with one sign each.

## Part VII. A Weak Array and a Diagonal

**The corner halves what it does to a plane.** $[T^{L}_{a},iD]=-2\,iS_{ta}$ and $[T^{R}_{a},iD]=-2\,iS_{ta}$: the coefficient $-2$ is half of the $-4$ of Rule 5, because only the $\{t,a\}$ plane of the two the weak array carries meets the corner, and the weak array holds half of that plane.

| $X$ | $iD$ | $[X,iD]$ |
| --- | --- | --- |
| $T^{L}_{x}$ | $iD$ | $-2\,iS_{tx}$ |
| $T^{L}_{y}$ | $iD$ | $-2\,iS_{ty}$ |
| $T^{L}_{z}$ | $iD$ | $-2\,iS_{tz}$ |

| $X$ | $iD$ | $[X,iD]$ |
| --- | --- | --- |
| $T^{R}_{x}$ | $iD$ | $-2\,iS_{tx}$ |
| $T^{R}_{y}$ | $iD$ | $-2\,iS_{ty}$ |
| $T^{R}_{z}$ | $iD$ | $-2\,iS_{tz}$ |

| $X$ | $d_2$ | $[X,d_2]$ |
| --- | --- | --- |
| $T^{L}_{x}$ | $d_{2}$ | $-\tfrac{1}{2}\,iS_{tx} - \tfrac{1}{2}\,iS_{yz}$ |
| $T^{L}_{y}$ | $d_{2}$ | $\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |
| $T^{L}_{z}$ | $d_{2}$ | $iS_{xy}$ |

| $X$ | $d_3$ | $[X,d_3]$ |
| --- | --- | --- |
| $T^{L}_{x}$ | $d_{3}$ | $iS_{yz}$ |
| $T^{L}_{y}$ | $d_{3}$ | $-\tfrac{1}{2}\,iS_{ty} - \tfrac{1}{2}\,iS_{xz}$ |
| $T^{L}_{z}$ | $d_{3}$ | $\tfrac{1}{2}\,iS_{tz} - \tfrac{1}{2}\,iS_{xy}$ |

| $X$ | $d_2$ | $[X,d_2]$ |
| --- | --- | --- |
| $T^{R}_{x}$ | $d_{2}$ | $-\tfrac{1}{2}\,iS_{tx} + \tfrac{1}{2}\,iS_{yz}$ |
| $T^{R}_{y}$ | $d_{2}$ | $\tfrac{1}{2}\,iS_{ty} + \tfrac{1}{2}\,iS_{xz}$ |
| $T^{R}_{z}$ | $d_{2}$ | $-iS_{xy}$ |

| $X$ | $d_3$ | $[X,d_3]$ |
| --- | --- | --- |
| $T^{R}_{x}$ | $d_{3}$ | $-iS_{yz}$ |
| $T^{R}_{y}$ | $d_{3}$ | $-\tfrac{1}{2}\,iS_{ty} + \tfrac{1}{2}\,iS_{xz}$ |
| $T^{R}_{z}$ | $d_{3}$ | $\tfrac{1}{2}\,iS_{tz} + \tfrac{1}{2}\,iS_{xy}$ |

**The colour diagonals see the weak arrays through both of their planes at once**, which is why every entry here is a sum or a difference of two imaginary planes with equal halves rather than a single plane.

## The Sixty-Seven Zeros

**The zeros are as structured as the numbers.** Sixty-seven independent brackets vanish, and every one of them is one of eight statements.

| family | count | the reason |
| --- | --- | --- |
| an array with itself | $21$ | antisymmetry |
| two real planes with no common index | $3$ | disjoint entries, Rule 1 |
| two imaginary planes with no common index | $3$ | disjoint entries, Rule 2 |
| a real and an imaginary plane with no common index | $6$ | disjoint entries, Rule 3 |
| a real plane that is one of the two planes of a weak array | $12$ | the weak array is the average of the two, Rule 6 |
| a plane inside a fixed line of a colour diagonal | $4$ | the spacing is $0$, Rule 5 |
| a colour plane with the corner | $6$ | the corner has no spacing inside colour, Rule 5 |
| the three diagonals with each other | $3$ | the Cartan is abelian |
| the two triples with each other | $9$ | independent factors, Rule 6 |

**No zero is an accident, and the list has eight lines and one row that says why.** A reader who knows the eigenvalues of the three diagonals and the two planes of each weak array predicts all forty-six off-diagonal zeros without computing a single matrix.

## What the Table Says That No Single Bracket Says

**The real planes are a subalgebra and the imaginary ones are not.** Six generators close on themselves; nine do not, and their product falls back on the six. **The compact form of $\mathfrak{su}(4)$ is not symmetric across the Cartan split**, and this block is where that asymmetry is visible.

**The twelve plane arrays are closed except on six pairs, and the six are exactly the pairs that generate the Cartan.** Any reading in which the diagonal directions are extra data is contradicted here: they are produced by $[A_{jk},iS_{jk}]$ and by nothing else among the planes.

**The corner meets twelve brackets as a factor and appears in nine as an answer.** It meets the three $\{t,k\}$ planes, their three imaginary partners and the six weak arrays; it comes back from the three equal-plane brackets through $t$ and from the six brackets of a weak array with an imaginary plane. **The three colour planes and the two colour diagonals never see it at all**, which is the algebraic content of the phrase that the corner is the lepton-line direction.

**The two triples are independent factors.** Nine zeros and a direct product $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ inside the group. Any mixing of the two would have to come from the scalar sector and not from the algebra.

**Every coefficient is $\pm\tfrac13$, $\pm\tfrac12$, $\pm\tfrac23$, $\pm1$, $\pm\tfrac43$, $\pm2$ or $\pm4$.** A table whose coefficients are seven rationals is a table that can be checked by hand, and this one can.

## The Checks

| what | result |
| --- | --- |
| the $441$ ordered brackets, from the matrices | every one inside the span of the fifteen |
| the six rules, against the $441$ entries | $210$ independent pairs, $0$ disagreements |
| antisymmetry | holds on all $441$ |
| the Jacobi identity | holds identically: the bracket is a commutator of matrices |
| nonzero entries | $164$ of $231$ |
| zero entries | $67$, in the eight families above |
| coefficient set | fourteen signed values, denominators $1$, $2$, $3$ |
| nonzero per block | $12+12+30+3+5+5+3+5+5+0+0+0+3+3+0+12+12+18+18+3+3+3+3+3+3=164$ |

**The count by block is the check on the tables themselves.** Parts I to IV contribute $12+12+30+3+5+5+3+5+5+0+0+0=80$. Parts V to VII contribute $3+3+0+12+12+18+18+3+3+3+3+3+3=84$. **The sum is $164$, and the tables print exactly that many rows.**

**No pass exceeded one hundred entries.** Each block was recomputed and compared in its own pass, and the largest single pass is the thirty-entry real-imaginary block.

## Summary

**Twenty-one arrays, $441$ ordered brackets, $231$ independent, $164$ nonzero, $67$ zero.** Six rules produce all of them:
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
$$
$$
[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}T^{L}_{c},
\qquad
[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}T^{R}_{c},
\qquad
[T^{L}_{a},T^{R}_{b}]=0 .
$$

**The real planes close, the imaginary ones do not, the two triples commute, and the corner is produced by the planes rather than added to them.** Those four sentences are the table.

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $E_{jk}$ | the matrix unit of $M_4(\mathbb{C})$, indices in the order $(t,x,y,z)$ |
| $A_{jk}=E_{jk}-E_{kj}$ | the real antisymmetric array of the plane $\{j,k\}$ |
| $S_{jk}=E_{jk}+E_{kj}$ | the real symmetric partner; $iS_{jk}$ is the algebra element |
| $iD$ | the corner, $i\operatorname{diag}(-3,1,1,1)$ |
| $d_2$, $d_3$ | the colour diagonals, $i\operatorname{diag}(0,1,-1,0)$ and $i\operatorname{diag}(0,0,1,-1)$ |
| $T^{L}_{a}$, $T^{R}_{a}$ | the weak arrays, $-\tfrac12(A_{ta}\pm A_{bc})$, $(a,b,c)$ cyclic |
| $[X,Y]$ | $XY-YX$, the commutator of the matrices |
| $\lambda_{j}$ | the eigenvalue of the diagonal $i\Lambda$ at the index $j$ |
| $\epsilon_{abc}$ | the Levi-Civita symbol of the three colour labels |
| complementary planes | two planes of $\{t,x,y,z\}$ with no common index |

## Further Reading

- J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972 — structure constants, the Chevalley basis, and a table of brackets read as a presentation of the algebra.
- H. Georgi, *Lie Algebras in Particle Physics*, Benjamin Cummings, 1982 — the physicists' conventions, the $\tfrac12$ of a weak generator, and the sign of $\epsilon_{abc}$.
- R. Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications*, Wiley, 1974 — compact real forms, the splitting $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, and the inertia that separates the two halves.
- The corpus: [The Rotors of the Twenty-One Generators](the-rotors-of-the-twenty-one-generators-in-the-four-colours-left-right-model-three-turn-space-three-turn-the-quartet-and-no-boost-is-in-the-group.html) for the exponential of each generator; [The Construction of the AXF Matrices of the Twenty-One Generators](construction-of-the-axf-matrices-of-the-twenty-one-generators.html) for the arrays themselves; [The 21 AXF Matrices of the Bosons in Detail](the-21-axf-matrices-of-the-bosons-in-detail.html) for one subsection per generator; [Classification of the Bosons](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html) for the cell each array occupies; [The Five Counts of the Twenty-One](the-five-counts-of-the-twenty-one-twenty-four-cells-six-planes-twenty-one-arrays-fifteen-directions.html) for the count that ends at fifteen.
