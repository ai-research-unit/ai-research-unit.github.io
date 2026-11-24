# __The AXF Matrices of the Twenty-One Generators: Fifteen for $\mathfrak{su}(4)$, Three for $\mathfrak{su}(2)_L$, Three for $\mathfrak{su}(2)_R$__

## Introduction

**The aim.** This article prints every generator of the Four Colours Left–Right Model as a matrix, in the axis-free frame, and groups them by the algebra each belongs to. Three algebras are involved and they come in two sizes, so the article has three parts: the fifteen are printed in Part I, and the two weak triples in Parts II and III, and the parts do not share a display.

**The three parts.**

| part | algebra | generators | matrices | prints in |
| --- | --- | --- | --- | --- |
| I | $\mathfrak{su}(4)$, the colour-leptoquark algebra | $15$ | four-row | §*The Fifteen Matrices of* $\mathfrak{su}(4)$ |
| II | $\mathfrak{su}(2)_L$, weak isospin on the left doublet | $3$ | two-row | §*The Three Matrices of* $\mathfrak{su}(2)_L$ |
| III | $\mathfrak{su}(2)_R$, weak isospin on the right doublet | $3$ | two-row | §*The Three Matrices of* $\mathfrak{su}(2)_R$ |

**$15+3+3=21$, and the sizes differ for a reason.** The quartet has four dimensions, so its algebra has fifteen generators and its matrices have four rows. Each doublet has two dimensions, so each weak algebra has three generators and its matrices have two rows. **A four-row matrix cannot hold the weak generators and a two-row matrix cannot hold the colour ones**, and the two are therefore printed separately, in separate frames, with no array serving two algebras.

**The count from the cells, once.** A block of $d$ rows carries $d^{2}$ real directions in its anti-Hermitian slice and the trace removes exactly one, so a factor of $d$ rows yields $d^{2}-1$ generators. Hence
$$
16-1=15,\qquad 4-1=3,\qquad 4-1=3,\qquad 15+3+3=21 .
$$
The three removed directions are the three identities $i\mathrm I_4$, $i\mathrm I_2$, $i\mathrm I_2$, one per factor, and they are what makes each algebra traceless.

**What the frame is.** The axis-free frame of [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html). In it the matrices of the units are signed permutations with entries in $\{0,+1,-1\}$ and the columns are the products with the units,
$$
L_{\mathrm{axf}}(\tilde Q)_{\imath\jmath}=\bigl[\tilde Q\,e_{\jmath}\bigr]_{\imath} .
$$
Every array below is built from the arrays of the units by that rule, by transposition, or by multiplication by $i$. **No array below is a Pauli array or a gamma array**, and no axis is selected anywhere.

## Part I. The Fifteen Matrices of $\mathfrak{su}(4)$

**The frame and the indices.** The quartet is $\mathbb{C}^{4}$ with the base $(e_t,\vec e_x,\vec e_y,\vec e_z)$, where $e_t$ is the lepton line and the other three are the colours, and $E_{jk}$ is the matrix unit in that order. The fifteen are built from the three families of the table.

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
A_{xy}=\begin{pmatrix}0&0&0&0\\0&0&1&0\\0&-1&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

$$
A_{zx}=\begin{pmatrix}0&0&0&0\\0&0&0&-1\\0&0&0&0\\0&1&0&0\end{pmatrix}
$$

**Their action.** $A_{bc}e_t=0$: the exponential fixes the lepton line point by point and turns the colour triple. These three are the real part of the eight colour generators, and they are minus the inner derivations, $\tfrac12\operatorname{ad}_{\vec e_a}=-A_{bc}$.

**What the six share.** Real antisymmetric signed permutations with four nonzero entries, of square $-(E_{jj}+E_{kk})$ on their plane and zero elsewhere, of spectrum $i,-i,0,0$, of trace of square $-2$. **The minus sign in that trace is what makes them rotations**: the boost of the same plane has $+2$.

### The Six Imaginary Planes

**The colour three, the second generator of each colour plane.**

$$
iS_{xy}=\begin{pmatrix}0&0&0&0\\0&0&i&0\\0&i&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&i\\0&0&i&0\end{pmatrix}
$$

$$
iS_{zx}=\begin{pmatrix}0&0&0&0\\0&0&0&i\\0&0&0&0\\0&i&0&0\end{pmatrix}
$$

**The mixed three, the second generator of each leptoquark plane.**

$$
iS_{tx}=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{ty}=\begin{pmatrix}0&0&i&0\\0&0&0&0\\i&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{tz}=\begin{pmatrix}0&0&0&i\\0&0&0&0\\0&0&0&0\\i&0&0&0\end{pmatrix}
$$

**Why the factor $i$.** Without it, $S_{jk}=E_{jk}+E_{kj}$ is real and symmetric, its exponential is not unitary and it generates no compact group. The product by $i$ makes it anti-Hermitian and traceless and puts it in $\mathfrak{su}(4)$. **The pair $(A_{jk},iS_{jk})$ is one cell pair's two real amplitudes**, the two generators of one plane.

**What the six share.** $i$ times a symmetric signed permutation, four nonzero entries, spectrum $i,-i,0,0$, trace of square $-2$, fixing the two lines they do not touch. None is real, so no exponential of one of them is a real matrix.

### The Three Diagonals

**The corner.**

$$
iD=\begin{pmatrix}-3i&0&0&0\\0&i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix},\qquad D=\operatorname{diag}(-3,1,1,1)
$$

**It is not a fourth diagonal.** With $N_{jk}=\ell_jr_k$ the operator frame's products, $iN_{xx}+iN_{yy}+iN_{zz}=iD$: the corner is minus the sum of the colour diagonals, and that identity is why the quartet carries three diagonal generators and not four. **The same $D$ carries $B-L$**, since $B-L=\tfrac13D$ on $\mathbf4$ and $\tfrac12(B-L)=\tfrac16D$.

**The two colour diagonals.**

$$
d_{2}=\begin{pmatrix}0&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&0\end{pmatrix}
$$

$$
d_{3}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&i&0\\0&0&0&-i\end{pmatrix}
$$

**They fix the lepton line and differ on two colours.** Spectrum $i,-i,0,0$, trace of square $-2$ each, and together with the six colour planes they make the eight colour generators, $3+3+2=8$. **The trace form couples them**, $\operatorname{tr}(d_id_j)=\begin{pmatrix}-2&1\\1&-2\end{pmatrix}$, which is the array form of the statement that a colour basis is a choice and the algebra is not.

## Part II. The Three Matrices of $\mathfrak{su}(2)_L$

**The frame.** A different frame and a different size: the left doublet is $\mathbb{C}^{2}$, and its generators are half the axis-free matrices of the three units of the two-row frame,
$$
T^{L}_{a}:=\tfrac12\,\mathsf M_2(\vec e_a),\qquad a=x,y,z ,
$$
with $\mathsf M_2$ the axis-free two-row representation. The half removes the factor two that $[\vec e_x,\vec e_y]=2\vec e_z$ carries, so that the structure constants come out as $\epsilon_{abc}$ with no constant.

**The three, one to a display.**

$$
T^{L}_{x}=\tfrac12\mathsf M_2(\vec e_x)=\begin{pmatrix}0&-\tfrac{i}{2}\\-\tfrac{i}{2}&0\end{pmatrix}
$$

$$
T^{L}_{y}=\tfrac12\mathsf M_2(\vec e_y)=\begin{pmatrix}0&-\tfrac12\\\tfrac12&0\end{pmatrix}
$$

$$
T^{L}_{z}=\tfrac12\mathsf M_2(\vec e_z)=\begin{pmatrix}-\tfrac{i}{2}&0\\0&\tfrac{i}{2}\end{pmatrix}
$$

**The shape, read off the entries.** $T^{L}_{x}$ is $i$ times a real symmetric array, $T^{L}_{y}$ is real antisymmetric, $T^{L}_{z}$ is $i$ times a real diagonal. **The three symmetry types are the three generators**, and no sign was chosen by hand: each is $\tfrac12$ times an array of the units.

**The properties.** Anti-Hermitian, traceless, of square $-\tfrac14\mathrm I_2$, of spectrum $\pm\tfrac i2$, and closing as
$$
[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}\,T^{L}_{c} ,
$$
so they are a basis of $\mathfrak{su}(2)_L$ and the structure constants are the alternating symbol.

## Part III. The Three Matrices of $\mathfrak{su}(2)_R$

**The frame.** The right doublet is a second, independent $\mathbb{C}^{2}$, and its generators are the same three arrays in that frame's units:
$$
T^{R}_{a}:=\tfrac12\,\mathsf M_2(\vec e_a),\qquad a=x,y,z .
$$
**The three, one to a display.**

$$
T^{R}_{x}=\tfrac12\mathsf M_2(\vec e_x)=\begin{pmatrix}0&-\tfrac{i}{2}\\-\tfrac{i}{2}&0\end{pmatrix}
$$

$$
T^{R}_{y}=\tfrac12\mathsf M_2(\vec e_y)=\begin{pmatrix}0&-\tfrac12\\\tfrac12&0\end{pmatrix}
$$

$$
T^{R}_{z}=\tfrac12\mathsf M_2(\vec e_z)=\begin{pmatrix}-\tfrac{i}{2}&0\\0&\tfrac{i}{2}\end{pmatrix}
$$

**Same entries as the left three, and that is the point.** The two triples are equal as arrays and different as operators, because each acts on its own doublet. **Nothing in the array distinguishes them; the block they occupy does**, and that is why a display must say which doublet it is for.

**The properties, identical.** Anti-Hermitian, traceless, of square $-\tfrac14\mathrm I_2$, spectrum $\pm\tfrac i2$, and $[T^{R}_{a},T^{R}_{b}]=\epsilon_{abc}T^{R}_{c}$.

## The Two Parts Side by Side

**Where each sits.** The three factors are separate spaces and the twenty-one occupy them one block apiece:

| block | rows | algebra | generators |
| --- | --- | --- | --- |
| the quartet | $1$–$4$ | $\mathfrak{su}(4)$ | the fifteen |
| the left doublet | $5$–$6$ | $\mathfrak{su}(2)_L$ | $T^{L}_{x},T^{L}_{y},T^{L}_{z}$ |
| the right doublet | $7$–$8$ | $\mathfrak{su}(2)_R$ | $T^{R}_{x},T^{R}_{y},T^{R}_{z}$ |

**The two parts commute.** Written in the three blocks, the twenty-one arrays are block diagonal with one nonzero block each, so every colour generator commutes with every weak generator,
$$
[X,Y]=0,\qquad X\in\mathfrak{su}(4),\quad Y\in\mathfrak{su}(2)_L\ \text{or}\ \mathfrak{su}(2)_R ,
$$
all ninety brackets zero, and the twenty-one are independent. **That is the whole content of the direct sum**: the model's group is $\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ and the matrices display the product as blocks and not as sums.

## Why the Sizes Differ

**One paragraph, because the point is easy to lose.** The fifteen are four-row because the space they act on is four-dimensional, and the six are two-row because each doublet is two-dimensional. **Neither size is a choice of convenience**: a two-row matrix cannot act on a quartet and a four-row matrix cannot be faithful on a doublet.

**And the same abstract weak generator also has a four-row reading.** On the carrier, left and right multiplication by the units are four-row arrays $\ell_a$ and $r_a$ with eigenvalues $\pm i$, twice those of $T^{L}_{a}$. They are the same operators under the identification that looks at the quartet rather than at the doublet, and the arithmetic that shows it is
$$
\ell_a=-A_{ta}-A_{bc},\qquad r_a=-A_{ta}+A_{bc},\qquad \{a,b,c\}=\{x,y,z\},
$$
so the four-row reading of the weak generators is a sum of two colour-leptoquark generators and adds no direction to the fifteen. **It is stated here for orientation and used nowhere else**: in this article the weak generators are the two-row arrays of Parts II and III, and the fifteen of Part I are complete without them.

## The Checks

Eighteen recomputations, the coefficient frame with the quartet ordered $(t,x,y,z)$ and the product fixed by $\vec e_x\vec e_y=\vec e_z$.

| check | result |
| --- | --- |
| Part I: arrays printed | $15$ |
| Part I: distinct, anti-Hermitian, traceless | $15$, $15/15$, $15/15$ |
| Part I: rank | $15$ |
| Part I: entries | $0$, $\pm1$, $\pm i$, one $-3i$ |
| Part I: $iN_{xx}+iN_{yy}+iN_{zz}=iD$ | exact |
| Part I: eight colour generators fix $e_t$ / six mixed move it | $8/8$ / $6/6$ |
| Part I: $\operatorname{tr}X^{2}$ | $-2$ on the twelve planes, $-12$ on $iD$ |
| Part II and III: arrays printed | $3$ and $3$ |
| Part II and III: anti-Hermitian, traceless | $6/6$, $6/6$ |
| Part II and III: $[T_a,T_b]=\epsilon_{abc}T_c$ | $6/6$ exact |
| Part II and III: square $-\tfrac14\mathrm I_2$, spectrum $\pm\tfrac i2$, $\operatorname{tr}T^{2}=-\tfrac12$ | yes, yes, yes |
| the three blocks independent at eight rows | rank $21$ |
| colour against weak brackets | $90/90$ zero |
| $\det\exp(0.7X)=1$ and unitary | $21/21$ |
| cell arithmetic $16-1+4-1+4-1=21$ | exact |

## Summary

The twenty-one generators are printed as twenty-one matrices, and the article keeps them in the two algebras they belong to. **Part I prints the fifteen of $\mathfrak{su}(4)$ as four-row axis-free arrays**: six real planes, six imaginary planes and three diagonals. **Parts II and III print the three of $\mathfrak{su}(2)_L$ and the three of $\mathfrak{su}(2)_R$ as two-row axis-free arrays**, each triple $\tfrac12$ times the matrices of the units and closing at $\epsilon_{abc}$.

The sizes differ because the spaces differ: four dimensions for the quartet, two for each doublet, and $16-1+4-1+4-1=15+3+3=21$ is the count from the cells with the three identities removed. The two parts commute and are independent, which is the statement that the model's group is a product.

The one place the two parts meet is a single remark: on the carrier the weak generators also read as $\ell_a=-A_{ta}-A_{bc}$ and $r_a=-A_{ta}+A_{bc}$, four-row sums of colour-leptoquark generators. That reading adds no generator to the fifteen, and this article does not use it.

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the base of the carrier, with $\vec e_x\vec e_y=\vec e_z$ cyclically |
| $L_{\mathrm{axf}}(\tilde Q)$ | the matrix of left multiplication in the coefficient basis |
| $\mathsf M_2(\vec e_a)$ | the axis-free two-row matrix of the unit $\vec e_a$ |
| $E_{jk}$ | the matrix unit of the quartet in the order $(t,x,y,z)$ |
| $A_{jk}=E_{jk}-E_{kj}$ | the real generator of the plane $\{j,k\}$ |
| $iS_{jk}=i(E_{jk}+E_{kj})$ | the imaginary generator of the same plane |
| $D=\operatorname{diag}(-3,1,1,1)$ | the corner, with $B-L=\tfrac13D$ |
| $d_2,d_3$ | the two traceless colour diagonals |
| $T^{L}_{a}=\tfrac12\mathsf M_2(\vec e_a)$ | the three generators of $\mathfrak{su}(2)_L$ |
| $T^{R}_{a}=\tfrac12\mathsf M_2(\vec e_a)$ | the three generators of $\mathfrak{su}(2)_R$ |
| $\ell_a,r_a$ | the four-row reading of the weak generators on the carrier, used once |

## Further Reading

- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html). The frame, the signed permutations and the ten properties.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](../articles_maths/the-anti-hermitian-derivations-of-m4c-as-su4.html). The fifteen in the operator basis, printed one to a display.
- [The Anti-Hermitian Derivations of $M_2(\mathbb{C})$ as $\mathfrak{su}(2)$](../articles_maths/the-anti-hermitian-derivations-of-m2c-as-su2.html). The three two-row generators and the half that removes the factor two.
- [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html) and [$M_2(\mathbb{C})$ Defining Representation](../articles_maths/m2c-defining-representation.html). The four-row and two-row frames the two parts are built in.
- [Matrix Representations Conventions](matrix-representations-conventions.html). The displays, the operator that owns the array, and the ban on tildes on arrays.
- [The Rotors of the Twenty-One Generators](the-rotors-of-the-twenty-one-generators-three-turn-space-three-turn-the-quartet-and-no-boost.html). What each of these arrays does when exponentiated.
- [Classification of the Bosons: Twenty-Four Cells, Twenty-One Generators, Nine Massless and Twelve Massive](classification-of-the-bosons-twenty-four-cells-twenty-one-generators-one-name-in-every-cell.html). The cells and the ledger.
- [Charge Quantisation from the Fourth Colour](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). $B-L$, the trace of $D$ and the charge table.
- [The Four Colours Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-four-colours-left-right-model.html). The declaration and the ladder.
- H. Georgi, *Lie Algebras in Particle Physics*, Benjamin Cummings, 1982 — the embeddings of $\mathfrak{su}(2)\times\mathfrak{su}(2)$ in $\mathfrak{su}(4)$ and the weak normalisations.
- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer, 1991 — direct sums, blocks, and why a product of groups is displayed as a block array.
