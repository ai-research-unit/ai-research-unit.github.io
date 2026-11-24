# __The AXF Matrices of the Twenty-One Generators: Fifteen for $\mathfrak{su}(4)$, Three for $\mathfrak{su}(2)_L$, Three for $\mathfrak{su}(2)_R$__

## Introduction

**The aim.** This article prints every generator of the Four Colours Left–Right Model as an axis-free matrix, all of them of the same size, and keeps the three algebras in three separate parts. **All twenty-one are four-row arrays.** The fifteen of $\mathfrak{su}(4)$ are the coordinate planes and the diagonals; the three of $\mathfrak{su}(2)_L$ are half the left multiplication by the three vector units; the three of $\mathfrak{su}(2)_R$ are half the right multiplication by the same units.

**The three parts.**

| part | algebra | generators | array |
| --- | --- | --- | --- |
| I | $\mathfrak{su}(4)$ | $15$ | $A_{jk}$, $iS_{jk}$, $iD$, $d_2$, $d_3$ |
| II | $\mathfrak{su}(2)_L$ | $3$ | $T^{L}_{a}=\tfrac12 L_{\vec e_a}$ |
| III | $\mathfrak{su}(2)_R$ | $3$ | $T^{R}_{a}=\tfrac12 R_{\vec e_a}$ |

**The left and right triples are different arrays, and the difference is visible.** $T^{L}_{x}$ and $T^{R}_{x}$ agree in the upper two rows and columns, the block that carries the line into the colour $x$, and they differ in sign in the lower block, the plane $\{y,z\}$. **Left multiplication turns both planes by the same quarter and right multiplication turns them by opposite quarters**, and that is exactly the difference between the arrays. §*Part III* prints the six side by side in a pattern table.

**$15+3+3=21$, and the sizes agree.** The quartet is four-dimensional and each of the three vector units is an element of it, so all three algebras act on the same four-row carrier and all twenty-one arrays are four-row. The count from the cells is
$$
16-1+4-1+4-1=15+3+3=21,
$$
with the three subtrahends the three identities $i\mathrm I_4$, $i\mathrm I_2$, $i\mathrm I_2$: the quartet's trace, and the trace of each doublet's endomorphism algebra.

**What the frame is.** The axis-free frame of [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html). In it the array of an operator is read by columns, the $j$-th column being the product with the $j$-th unit,
$$
L_{\mathrm{axf}}(\tilde Q)_{\imath\jmath}=\bigl[\tilde Q\,e_{\jmath}\bigr]_{\imath},
$$
and the arrays of the units' two one-sided actions are printed in [The Twenty-One Generators in the Axis-Free Frame](../articles_internal/the-twenty-one-generators-in-the-axis-free-frame.html) and [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html). **No array below is a Pauli array or a gamma array**, and no axis is chosen anywhere.

## Part I. The Fifteen Matrices of $\mathfrak{su}(4)$

**The frame and the indices.** The quartet is $\mathbb{C}^{4}$ with the base $(e_t,\vec e_x,\vec e_y,\vec e_z)$, $e_t$ the lepton line and the other three the colours, and $E_{jk}$ the matrix unit in that order. The fifteen come in three families.

| family | count | array | entries |
| --- | --- | --- | --- |
| real planes | $6$ | $A_{jk}=E_{jk}-E_{kj}$ | $0$, $\pm1$ |
| imaginary planes | $6$ | $iS_{jk}=i\,(E_{jk}+E_{kj})$ | $0$, $\pm i$ |
| diagonals | $3$ | $i\operatorname{diag}$, traceless | $0$, $\pm i$, one $-3i$ |

### The Six Real Planes

**The three mixed planes, which move the lepton line.**

$$
A_{tx}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{ty}=\begin{pmatrix}0&0&1&0\\0&0&0&0\\-1&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{tz}=\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\-1&0&0&0\end{pmatrix}
$$

**Their action.** $A_{ta}e_t=-e_a$ and $A_{ta}e_a=e_t$: the exponential turns the plane $\{t,a\}$ and fixes the two remaining colours. These three are the real halves of the leptoquark block.

**The three colour planes, which fix the lepton line.**

$$
A_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

$$
A_{zx}=\begin{pmatrix}0&0&0&0\\0&0&0&-1\\0&0&0&0\\0&1&0&0\end{pmatrix}
$$

$$
A_{xy}=\begin{pmatrix}0&0&0&0\\0&0&1&0\\0&-1&0&0\\0&0&0&0\end{pmatrix}
$$

**Their action.** $A_{bc}e_t=0$: the exponential fixes the lepton line point by point and turns the colour triple. These three are the real part of the eight colour generators, and they are minus the inner derivations, $\tfrac12\operatorname{ad}_{\vec e_a}=-A_{bc}$.

**What the six share.** Real antisymmetric signed permutations with four nonzero entries, of spectrum $i,-i,0,0$, of trace of square $-2$. **The minus sign in that trace is what makes them rotations**: the boost of the same plane has $+2$.

### The Six Imaginary Planes

**The colour three.**

$$
iS_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&i\\0&0&i&0\end{pmatrix}
$$

$$
iS_{zx}=\begin{pmatrix}0&0&0&0\\0&0&0&i\\0&0&0&0\\0&i&0&0\end{pmatrix}
$$

$$
iS_{xy}=\begin{pmatrix}0&0&0&0\\0&0&i&0\\0&i&0&0\\0&0&0&0\end{pmatrix}
$$

**The mixed three.**

$$
iS_{tx}=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{ty}=\begin{pmatrix}0&0&i&0\\0&0&0&0\\i&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{tz}=\begin{pmatrix}0&0&0&i\\0&0&0&0\\0&0&0&0\\i&0&0&0\end{pmatrix}
$$

**Why the factor $i$.** Without it, $S_{jk}=E_{jk}+E_{kj}$ is real and symmetric, its exponential is not unitary, and it generates no compact group. The product by $i$ makes it anti-Hermitian and traceless and puts it in $\mathfrak{su}(4)$. **The pair $(A_{jk},iS_{jk})$ is the two real amplitudes of one plane**, and each is one generator.

**What the six share.** $i$ times a symmetric signed permutation, four nonzero entries, spectrum $i,-i,0,0$, trace of square $-2$, fixing the two lines they do not touch. None is real, so no exponential of one of them is a real array.

### The Three Diagonals

**The corner.**

$$
iD=\begin{pmatrix}-3i&0&0&0\\0&i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix},\qquad D=\operatorname{diag}(-3,1,1,1).
$$

**It is not a fourth diagonal.** With $N_{jk}=\ell_jr_k$ the operator frame's products, $iN_{xx}+iN_{yy}+iN_{zz}=iD$: the corner is minus the sum of the three diagonal products, and that identity is why the quartet carries three diagonal generators and not four. **The same $D$ carries $B-L$**, with $B-L=\tfrac13D$ on $\mathbf4$.

**The two colour diagonals.**

$$
d_{2}=\begin{pmatrix}0&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&0\end{pmatrix},\qquad d_{3}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&i&0\\0&0&0&-i\end{pmatrix}.
$$

**They fix the lepton line and differ on two colours.** Spectrum $i,-i,0,0$, trace of square $-2$ each, and together with the six colour planes they make the eight colour generators, $3+3+2=8$. **Their trace form couples them**, $\operatorname{tr}(d_id_j)=\begin{pmatrix}-2&1\\1&-2\end{pmatrix}$, which is the array form of the statement that a colour basis is a choice and the algebra is not.

## Part II. The Three Matrices of $\mathfrak{su}(2)_L$

**The frame.** The generators are half the left multiplication by the three vector units, read in the same four-row axis-free frame:
$$
T^{L}_{a}:=\tfrac12\,L_{\vec e_a},\qquad a=x,y,z .
$$
**The half removes a factor two.** The arrays of the units satisfy $[L_{\vec e_a},L_{\vec e_b}]=2\epsilon_{abc}L_{\vec e_c}$, because $[\vec e_x,\vec e_y]=2\vec e_z$ at the element level; halving makes the structure constants $\epsilon_{abc}$ with no constant. **Nothing else is chosen**: each array is a signed permutation and the half is a number.

**The three, one to a display.**

$$
T^{L}_{x}=\tfrac12 L_{\vec e_x}=\begin{pmatrix}0&-\tfrac12&0&0\\\tfrac12&0&0&0\\0&0&0&-\tfrac12\\0&0&\tfrac12&0\end{pmatrix}
$$

$$
T^{L}_{y}=\tfrac12 L_{\vec e_y}=\begin{pmatrix}0&0&-\tfrac12&0\\0&0&0&\tfrac12\\\tfrac12&0&0&0\\0&-\tfrac12&0&0\end{pmatrix}
$$

$$
T^{L}_{z}=\tfrac12 L_{\vec e_z}=\begin{pmatrix}0&0&0&-\tfrac12\\0&0&-\tfrac12&0\\0&\tfrac12&0&0\\\tfrac12&0&0&0\end{pmatrix}
$$

**The action, read off the columns.** $T^{L}_{a}$ sends $e_t\mapsto\tfrac12 e_a$ and $e_a\mapsto-\tfrac12 e_t$, so it turns the plane $\{t,a\}$; and it sends $e_b\mapsto\tfrac12 e_c$ and $e_c\mapsto-\tfrac12 e_b$, so it turns the plane $\{b,c\}$ **by the same quarter turn**. **The two planes are turned with one orientation**, and the four nonzero entries are the four moves.

**The properties.** Anti-Hermitian, traceless, of trace of square $-1$, of spectrum $\pm\tfrac i2$ each twice, and closing as
$$
[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}\,T^{L}_{c},
$$
so the three are a basis of $\mathfrak{su}(2)_L$ with the alternating symbol as structure constants.

## Part III. The Three Matrices of $\mathfrak{su}(2)_R$

**The frame.** Half the right multiplication by the same three units, in the same frame:
$$
T^{R}_{a}:=\tfrac12\,R_{\vec e_a},\qquad a=x,y,z .
$$
**The three, one to a display.**

$$
T^{R}_{x}=\tfrac12 R_{\vec e_x}=\begin{pmatrix}0&-\tfrac12&0&0\\\tfrac12&0&0&0\\0&0&0&\tfrac12\\0&0&-\tfrac12&0\end{pmatrix}
$$

$$
T^{R}_{y}=\tfrac12 R_{\vec e_y}=\begin{pmatrix}0&0&-\tfrac12&0\\0&0&0&-\tfrac12\\\tfrac12&0&0&0\\0&\tfrac12&0&0\end{pmatrix}
$$

$$
T^{R}_{z}=\tfrac12 R_{\vec e_z}=\begin{pmatrix}0&0&0&-\tfrac12\\0&0&\tfrac12&0\\0&-\tfrac12&0&0\\\tfrac12&0&0&0\end{pmatrix}
$$

**The action, and the difference from the left.** $T^{R}_{a}$ sends $e_t\mapsto\tfrac12 e_a$ and $e_a\mapsto-\tfrac12 e_t$, the same as the left array; and it sends $e_b\mapsto-\tfrac12 e_c$ and $e_c\mapsto\tfrac12 e_b$, **the opposite quarter turn**. So the right array turns the plane $\{t,a\}$ one way and the plane $\{b,c\}$ the other way, and the two arrays differ in sign on exactly those two entries.

**The six, in one pattern table.**

| array | entries $(t,a)$ | entries $(a,t)$ | entries $(b,c)$ | entries $(c,b)$ |
| --- | --- | --- | --- | --- |
| $T^{L}_{x}$ | $-\tfrac12$ | $\tfrac12$ | $-\tfrac12$ | $\tfrac12$ |
| $T^{L}_{y}$ | $-\tfrac12$ | $\tfrac12$ | $-\tfrac12$ | $\tfrac12$ |
| $T^{L}_{z}$ | $-\tfrac12$ | $\tfrac12$ | $-\tfrac12$ | $\tfrac12$ |
| $T^{R}_{x}$ | $-\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $-\tfrac12$ |
| $T^{R}_{y}$ | $-\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $-\tfrac12$ |
| $T^{R}_{z}$ | $-\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $-\tfrac12$ |

**Read the table as row then column.** The action written above is a column, so $e_t\mapsto\tfrac12 e_a$ is the entry $(a,t)$ and the entry $(t,a)$ is the one that sends $e_a\mapsto-\tfrac12 e_t$.

**The last two columns are the whole difference.** Same entries, opposite signs on the colour plane, and the two signs are the two orderings of the product: $\vec e_a\vec e_b=+\vec e_c$ but $\vec e_b\vec e_a=-\vec e_c$.

**The properties.** Anti-Hermitian, traceless, of trace of square $-1$, of spectrum $\pm\tfrac i2$ each twice, the same as the left triple. **The bracket carries a minus sign**:
$$
[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}\,T^{R}_{c} .
$$
**Why, in one line.** Right multiplication reverses the order of a product, $R_A R_B=R_{BA}$, so the map $\vec e_a\mapsto R_{\vec e_a}$ is an anti-homomorphism while $\vec e_a\mapsto L_{\vec e_a}$ is a homomorphism. **The span is the same Lie algebra either way**, and $\{-T^{R}_{a}\}$ closes with $+\epsilon_{abc}$; the sign is a choice of labelling inside the triple and not a choice of group.

**The two triples commute.**
$$
[T^{L}_{a},T^{R}_{b}]=0,\qquad a,b=x,y,z,
$$
because $(\vec e_a\tilde X)\vec e_b=\vec e_a(\tilde X\vec e_b)$ by associativity. **That single identity is what makes $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ a subgroup of $\mathrm{SU}(4)$**, and it is why the two triples can be printed side by side without one disturbing the other.

## How the Six Sit Inside the Fifteen

**The six are sums and differences of the fifteen, and the coefficients are integers after the halving.**
$$
A_{ta}=-(T^{L}_{a}+T^{R}_{a}),\qquad A_{bc}=-(T^{L}_{a}-T^{R}_{a}),\qquad \{a,b,c\}=\{x,y,z\}.
$$
**Check one, in four cells.** The two weak arrays agree on the $\{t,a\}$ block, so their sum keeps it doubled and its half is the leptoquark plane; they differ on the $\{b,c\}$ block, so their difference keeps it doubled and its half is the colour plane. **The half in the definition of $T$ is exactly what makes these two lines integral.**

**Twenty-one arrays, fifteen directions.** The six relations above are independent, so the rank of the twenty-one columns is fifteen. **Both statements are needed and neither is a defect**: twenty-one distinct arrays, one per generator, and fifteen directions, because six of the arrays are two-term sums of the other fifteen.

**The normalisation, said once.** The fifteen are integer arrays with trace of square $-2$; the six are half-integer arrays with trace of square $-1$. The two normalisations differ by the factor that removes the $2$ from $[\vec e_a,\vec e_b]=2\vec e_c$, and no display mixes them: every array above is printed at its own normalisation and the relations above hold with the halves as written.

**The doublet reading, in three sentences, and then dropped.** The same abstract weak generator also acts on a two-row doublet, where it is $\tfrac i2$ times a $2\times2$ array of Pauli type; that array belongs to the doublet factor of $(\mathbf4,\mathbf2,\mathbf1)\oplus(\bar{\mathbf4},\mathbf1,\mathbf2)$ and not to the quartet. **It is a different carrier and therefore a different array**, and it is not printed here. What is printed here is the carrier's reading, which is the one the two-sided action supplies and the one that makes $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ a subgroup of $\mathrm{SU}(4)$.

## The Checks

Twenty recomputations, the quartet ordered $(t,x,y,z)$ and the product fixed by $\vec e_x\vec e_y=\vec e_z$.

| check | result |
| --- | --- |
| arrays displayed | $21$, all four-row |
| anti-Hermitian, traceless | $21/21$, $21/21$ |
| distinct arrays | $21$ |
| rank of the twenty-one / of the fifteen | $15$ / $15$ |
| $T^{L}_{a}$ differs from $T^{R}_{a}$, each $a$ | $3/3$, by $1$ on two entries |
| left and right agree on the $\{t,a\}$ block | $3/3$ |
| entries of the weak six | $0$, $\pm\tfrac12$ |
| $[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}T^{L}_{c}$ | $3/3$ exact |
| $[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}T^{R}_{c}$ | $3/3$ exact |
| $\{-T^{R}_{a}\}$ closes with $+\epsilon_{abc}$ | $3/3$ exact |
| $[T^{L}_{a},T^{R}_{b}]=0$ | $9/9$ exact |
| $[L_{\vec e_a},L_{\vec e_b}]=2\epsilon_{abc}L_{\vec e_c}$ | $3/3$ exact |
| $\operatorname{tr}(T^{L})^{2}=\operatorname{tr}(T^{R})^{2}$ | $-1$, $-1$ |
| spectrum of each weak array | $\pm\tfrac i2$, twice |
| $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$ | $3/3$ exact |
| $A_{bc}=-(T^{L}_{a}-T^{R}_{a})$ | $3/3$ exact |
| $iN_{xx}+iN_{yy}+iN_{zz}=iD$ | exact |
| $\operatorname{tr}X^{2}$ of the fifteen | $-2$ on the twelve planes, $-12$ on $iD$ |
| eight colour generators fix $e_t$ / six mixed move it | $8/8$ / $6/6$ |
| $\det\exp(0.7X)=1$ and unitary | $21/21$ |

## Summary

The twenty-one generators are twenty-one four-row axis-free arrays, printed one to a display and kept in three parts. **Part I prints the fifteen of $\mathfrak{su}(4)$**: six real planes, six imaginary planes and three diagonals. **Part II prints the three of $\mathfrak{su}(2)_L$** as half the left multiplication by the vector units, and **Part III the three of $\mathfrak{su}(2)_R$** as half the right multiplication.

**The left and right triples are different arrays**: they agree on the plane $\{t,a\}$ and differ in sign on the plane $\{b,c\}$, because left multiplication turns both planes together and right multiplication turns them apart. The difference is one sign on two entries per array, and it is the difference between the two factors of the model.

The two triples commute, so $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ sits inside $\mathrm{SU}(4)$; the right triple's bracket carries a minus sign because right multiplication reverses products; and the six weak arrays are the sums and differences of the fifteen, $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$ and $A_{bc}=-(T^{L}_{a}-T^{R}_{a})$, so twenty-one arrays span fifteen directions.

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the base of the carrier, $\vec e_x\vec e_y=\vec e_z$ cyclically |
| $L_{\mathrm{axf}}(\tilde Q)$ | the array of left multiplication, columns equal to products |
| $E_{jk}$ | the matrix unit of the quartet in the order $(t,x,y,z)$ |
| $A_{jk}=E_{jk}-E_{kj}$ | the real generator of the plane $\{j,k\}$ |
| $iS_{jk}=i(E_{jk}+E_{kj})$ | the imaginary generator of the same plane |
| $D=\operatorname{diag}(-3,1,1,1)$ | the corner, with $B-L=\tfrac13D$ |
| $d_2,d_3$ | the two traceless colour diagonals |
| $L_{\vec e_a},R_{\vec e_a}$ | left and right multiplication by the vector units |
| $T^{L}_{a}=\tfrac12 L_{\vec e_a}$ | the three generators of $\mathfrak{su}(2)_L$ |
| $T^{R}_{a}=\tfrac12 R_{\vec e_a}$ | the three generators of $\mathfrak{su}(2)_R$ |

## Further Reading

- [The Twenty-One Generators in the Axis-Free Frame](../articles_internal/the-twenty-one-generators-in-the-axis-free-frame.html). The arrays of $L_{\vec e_a}$ and $R_{\vec e_a}$, their word support and the six relations.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html). The frame, the signed permutations and the ten properties.
- [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html) and [$M_2(\mathbb{C})$ Defining Representation](../articles_maths/m2c-defining-representation.html). The four-row and two-row frames.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](../articles_maths/the-anti-hermitian-derivations-of-m4c-as-su4.html). The fifteen in the operator basis, numbered $G_1$ to $G_{15}$.
- [Two Bases of $\mathfrak{su}(4)$](../articles_internal/structures/structure-SU4-basis-comparison.html). The change of basis between this fifteen and the operator fifteen, in both directions.
- [The Rotors of the Twenty-One Generators](the-rotors-of-the-twenty-one-generators-three-turn-space-three-turn-the-quartet-and-no-boost.html). What each of these arrays does when exponentiated.
- [The Four Colours Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-four-colours-left-right-model.html). The declaration, and why $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R=\exp L(\mathfrak k)\times\exp R(\mathfrak k)$.
- [Classification of the Bosons: Twenty-Four Cells, Twenty-One Generators](classification-of-the-bosons-twenty-four-cells-twenty-one-generators-one-name-in-every-cell.html). The cells and the ledger.
- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer, 1991 — one-sided actions, the anti-homomorphism of the right action, and why the two commute.
