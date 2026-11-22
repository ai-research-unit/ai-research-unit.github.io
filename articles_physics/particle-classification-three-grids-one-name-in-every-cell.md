# __Particle Classification: Three Grids, One Name in Every Cell__

## Introduction

**The model.** This article classifies the particles of one model and no other: **the fourth-colour left–right model**, the model the corpus adopts, set out in [The Fourth-Colour Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-fourth-colour-left-right-model.html). The name is stated first because every name below belongs to that model and to nothing else. It is not the Standard Model's particle list, and it is not a general classification of everything the algebra could describe: it is the spectrum of this frame, under this group, with this one declaration.

**The structure.** The frame is one group with three factors,

$$
G_{4LR}=\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R ,
\qquad
15+3+3=21
$$

acting on a formal copy of the quartet. $\mathrm{SU}(4)$ acts on the four dimensions of the carrier; the two $\mathrm{SU}(2)$'s act on a two-dimensional index each.

**What the model declares and what it derives, in one paragraph, because the names depend on the difference.** The carrier supplies the group, the canonical split $\mathbf 4=\mathbf 1\oplus\mathbf 3$, the two-sided action and the traceless diagonal. What it does **not** supply is which of the four dimensions is the lepton; that is the model's one load-bearing declaration, (A), and every charge in this article is computed after it. The chiral assignment is declared too. Everything else below is arithmetic on those two declarations.

**The answer, and it is a picture.** Three grids of cells, one grid per factor: a $4\times4$ for $\mathrm{SU}(4)$ over the labels $t,x,y,z$, and a $2\times2$ for each $\mathrm{SU}(2)$ over the labels $\uparrow,\downarrow$. Each is drawn as a matrix, with the symbol of the boson and the name of the particle inside the cell. A cell is a direction, not a generator — a cell and its mirror image are the two halves of one plane, and the plane's two particles are their combinations. That single fact is what makes the grids readable and is stated once in §2.

**The count, in one line.**

$$
\underbrace{16}_{4\times4}+\underbrace{4}_{2\times2}+\underbrace{4}_{2\times2}=24\ \text{cells},
\qquad
\underbrace{15+3+3}_{21\ \text{generators}}+\underbrace{1+1+1}_{3\ \text{traces}}=24 ,
$$

so **twenty-four cells, twenty-one generators, three trace directions.** The three cells that hold no generator are the three traces, one per factor, and that is why the group is $21$ and not $24$.

**What this article is.** A nomenclature built on that structure. Every name in every cell is a name already in the corpus; the grid is the frame's own decomposition, drawn. §8 lists the spectrum the grids produce, and §9 and §10 give the fermions and the scalars that sit on the same cells.

**What this article is not, stated at the top because it governs every entry.** It is not a coupling sector. The model carries three gauge couplings as symbols multiplying their generators and fixes none of their values; it fixes no scalar multiplet; and it predicts no mass relation. Everything below is content and charge — what exists, in which cell, with which name and which $Q$ — and none of it depends on a coupling. Where a number in this family cannot be written without a scale, it is the literature's and it is flagged as such.

## 1. What Each Factor Acts On

**Three factors, three carriers, and the index each one uses.**

| factor | acts on | the index | how many values | the cells |
|---|---|---|---|---|
| $\mathrm{SU}(4)$ | the quartet | $i=\nu,r,g,b$ | $4$ | $4\times4$ |
| $\mathrm{SU}(2)_L$ | a left doublet | $\uparrow,\downarrow$ | $2$ | $2\times2$ |
| $\mathrm{SU}(2)_R$ | a right doublet | $\uparrow,\downarrow$ | $2$ | $2\times2$ |

**The quartet's four values, and the declaration behind them.** The carrier's canonical basis is $(e_t,e_x,e_y,e_z)$, and its canonical split is $\mathbb C e_t\oplus B_V$. The declaration is that the line is the lepton and the three-space is colour:

$$
\nu\equiv e_t,\qquad r\equiv e_x,\qquad g\equiv e_y,\qquad b\equiv e_z .
$$

This is the one declaration of the frame. Without it the group still has its $4\times4$ grid; what it does not know is which row is the lepton. With it, the $(e_t,e_x,e_y,e_z)$ in the algebra articles and the $(\nu,r,g,b)$ in this one are the same four labels.

**The two doublets are not the same doublet.** The left index pairs left-handed fields, the right index pairs right-handed fields, and they are two different $\mathrm{SU}(2)$'s acting on two different copies of a two-dimensional space:

$$
(\nu_L,e_L),\ (u_L,d_L)\ \text{under }\mathrm{SU}(2)_L ;
\qquad
(\nu_R,e_R),\ (u_R,d_R)\ \text{under }\mathrm{SU}(2)_R .
$$

The quark doublet is the same doublet in three colour copies, so a generation has two doublets per chirality if the colour copies are counted as one orbit.

**The model has exactly three numbers, and they are the table's third column: $4$, $2$, $2$.** Each factor contributes one number, and that number is the dimension of the representation its index labels — how many values the index takes. $\mathrm{SU}(4)$ acts on a quartet, so its index takes four values. Each $\mathrm{SU}(2)$ acts on a doublet, so each takes two. **Everything countable in this article is built from those three numbers, and it is built by two different operations: a sum of squares for the bosons, a product for the fermions.**

**The bosons are a sum of squares, one square per factor.** A gauge boson is a direction inside one factor's algebra, and a factor of dimension $d$ has $d^2$ entries in its defining matrix, one of which is the trace. So the factors contribute $4^2+2^2+2^2=16+4+4=24$ cells, and the three traces are removed: $24-3=21$. **No factor multiplies another**, because a gauge boson lives in one factor and is a singlet of the other two. That is why the grids are three separate rectangles and not one box.

**The fermions are a product, because a fermion carries one value of every index.** One quartet value, one doublet slot, and one chirality. The count is therefore

$$
\underbrace{4}_{\text{quartet}}\times\underbrace{2}_{\text{doublet slot}}\times\underbrace{2}_{\text{chirality block}}=16 ,
$$

and **$16$ is literally the product of the model's three numbers.** That is the answer to "why sixteen": it is $4\times2\times2$, and each factor contributes the size of its own index.

**The product is taken block by block, and that is where the count has to be done carefully.** The sixteen is not one block of $4\times2\times2$ components; it is two blocks, and in each block one factor is a singlet:

$$
(\mathbf4,\mathbf2,\mathbf1):\ 4\times2\times1=8
\qquad
(\bar{\mathbf4},\mathbf1,\mathbf2):\ 4\times1\times2=8
\qquad
8+8=16 .
$$

The sum of the two blocks equals the full product because $1+1=2$:

$$
4\times2\times1+4\times1\times2=4\times2\times(1+1)=4\times2\times2=16 .
$$

**So the identity $16=4\times2\times2$ holds, and it holds by distributing over the two blocks, not by any single representation having sixteen components in the shape $4\otimes2\otimes2$.** The difference is not pedantry: in $(\mathbf4,\mathbf2,\mathbf2)$ both weak factors act on the same field, while in the actual spectrum a left-handed field is a doublet of $\mathrm{SU}(2)_L$ and a **singlet** of $\mathrm{SU}(2)_R$.

| the job | the operation on $4,2,2$ | the arithmetic | the result |
|---|---|---|---|
| the boson cells | sum of squares | $4^2+2^2+2^2$ | $24$ |
| the boson generators | each square minus one | $15+3+3$ | $21$ |
| the fermions, left block | product with the third factor trivial | $4\times2\times1$ | $8$ |
| the fermions, right block | product with the second factor trivial | $4\times1\times2$ | $8$ |
| the fermions, both blocks | the two added | $8+8$ | $16$ |
| the full product | distributing $1+1=2$ | $4\times2\times2$ | $16$ |

**The three numbers also have a meaning each, and the meanings are different kinds of thing.** $4$ counts the threads: one lepton line and three colours. The first $2$ counts the slots of a doublet: up-type and down-type. The second $2$ counts the chirality blocks: which $\mathrm{SU}(2)$ acts. **Two of the three numbers are $2$, they are not the same $2$, and they never multiply inside one field**, since no fermion is a doublet of both weak groups at once.

**One number that is *not* used, named so it is not mistaken for one of the three.** The ranks are $3+1+1=5$: three diagonal generators in $\mathrm{SU}(4)$, one in each $\mathrm{SU}(2)$. The rank is not the quartet's size and it is not used in any count here. **The index takes four values, not three**, which is the whole reason the fourth colour exists and the reason the fermion count is $16$ and not $9$. A sentence that reaches for the rank where the dimension belongs gets $3\times2\times2=12$ and loses the lepton line.

**The one genuine coincidence, stated as one.** The number $16$ is also the dimension of the bifundamental $(\mathbf4,\mathbf2,\mathbf2)$, because $4\times2\times2$ does not care which factor is which. **The fermion content of this model is not that representation**; the equality is arithmetic, and the block table above is what distinguishes the two objects.

## 2. The $\mathrm{SU}(4)$ Grid, $4\times4$, with a Name in Every Cell

**How to read a cell.** Cell $(i,j)$ is the direction that moves index $j$ into index $i$. A cell alone is not a generator: it is one of the two amplitudes of the plane $\{i,j\}$, and the plane's two directions are the amplitude and its reverse. **The two particles of a plane are the two real combinations of its two amplitudes**, which is why each cell can carry a particle name and why the pair of mirrored cells carries a pair of particles.

**And one honest convention about the names in the cells.** Since each particle is a real combination of a cell and its mirror, which name goes in which cell is a choice: the two names of a mirrored pair could be exchanged without changing a single number. What is *not* a choice is the count — one plane, two amplitudes, two particles — and that is the only thing the grid is used for below. The cells are a register of names and not a basis of the Lie algebra.

**The grid.** Rows are *from*, columns are *to*; cell $(i,j)$ moves index $j$ into index $i$. Each cell carries the symbol of its boson and, beneath it, the name of the particle.

$$
\begin{array}{ccccc}
 & \substack{t\\ \text{lepton}} & \substack{x\\ \text{red}} & \substack{y\\ \text{green}} & \substack{z\\ \text{blue}}\\[10pt]
\substack{t\\ \text{lepton}}
 & \substack{B'\\ \text{the }B\text{--}L\text{ boson}}
 & \substack{\bar X^{r}\\ \text{antileptoquark, red}}
 & \substack{\bar X^{g}\\ \text{antileptoquark, green}}
 & \substack{\bar X^{b}\\ \text{antileptoquark, blue}}\\[10pt]
\substack{x\\ \text{red}}
 & \substack{X^{r}\\ \text{leptoquark, red}}
 & \substack{T^{c}_{3}\\ \text{gluon, } r\bar r-g\bar g}
 & \substack{g_{1}\\ \text{gluon, } r\bar g}
 & \substack{g_{4}\\ \text{gluon, } r\bar b}\\[10pt]
\substack{y\\ \text{green}}
 & \substack{X^{g}\\ \text{leptoquark, green}}
 & \substack{g_{2}\\ \text{gluon, } g\bar r}
 & \substack{T^{c}_{8}\\ \text{gluon, colour-singlet diagonal}}
 & \substack{g_{6}\\ \text{gluon, } g\bar b}\\[10pt]
\substack{z\\ \text{blue}}
 & \substack{X^{b}\\ \text{leptoquark, blue}}
 & \substack{g_{5}\\ \text{gluon, } b\bar r}
 & \substack{g_{7}\\ \text{gluon, } b\bar g}
 & \substack{\text{trace}\\ \text{not a generator}}
\end{array}
$$

**The four diagonal cells hold four raw directions, and the names in them are a basis of the diagonal and not one cell each.** The cells are $iE_{tt},iE_{xx},iE_{yy},iE_{zz}$. Tracelessness removes one combination of the four and leaves three, and the three are what the names denote:

$$
B-L=\tfrac13\operatorname{diag}(-3,1,1,1),
\qquad
T^{c}_{3}=x\bar x-y\bar y,
\qquad
T^{c}_{8}=\tfrac{1}{\sqrt3}\bigl(x\bar x+y\bar y-2z\bar z\bigr).
$$

So $T^{c}_{3}$ spans $xx$ and $yy$, $T^{c}_{8}$ spans all three colour cells, and $B-L$ spans all four. The names are the conventional basis; the cells are the raw directions. What *is* one per cell is the count: four diagonal cells, one trace removed, three generators.

**The labels of that grid are the corpus's four algebra labels.** $t$ is $e_t$, the temporal unit, and $x,y,z$ are $e_x,e_y,e_z$; so the row written $t$ here is the row written $\nu$ elsewhere in the corpus, and the three written $x,y,z$ are $r,g,b$. The change of letter is (A) and nothing more: the lepton line is the temporal line.

**Read the four blocks of that grid, and the whole spectrum falls out.**

| block | cells | generators | names | what it is |
|---|---|---|---|---|
| the $\nu$ row and column, off the corner | $3+3=6$ | $6$ | $X^{r},X^{g},X^{b}$ and $\bar X^{r},\bar X^{g},\bar X^{b}$ | the leptoquark sextet |
| the $3\times3$ colour block | $9$ | $8$ | $g_{1}\dots g_{8}$ | the gluon octet |
| the $(\nu,\nu)$ corner | $1$ | $1$ | $B'$ | the $B-L$ boson |
| the diagonal of the colour block | $3$ | $2$ of them, plus the block's trace | $T^{c}_{3}$, $T^{c}_{8}$ | the Cartan of colour |

$$
\underbrace{6}_{\text{leptoquarks}}+\underbrace{8}_{\text{gluons}}+\underbrace{1}_{B-L}=15 ,
\qquad
\underbrace{6}_{\text{mixed cells}}+\underbrace{9}_{3\times3}+\underbrace{1}_{(\nu,\nu)}=16 .
$$

**That display is the whole of the frame's decomposition, and it is a picture of $15=8+1+6$.** The three colour planes $\{r,g\},\{r,b\},\{g,b\}$ hold the six off-diagonal gluons, two per plane. The three mixed planes $\{\nu,r\},\{\nu,g\},\{\nu,b\}$ hold the six leptoquarks, two per plane. The $3\times3$ colour block's diagonal holds the two Cartan directions of colour. And the $(\nu,\nu)$ corner holds the one generator that makes the total trace vanish.

**The corner is forced, and that is charge quantisation.** Read the diagonal cells as the four eigenvalues of the corner's generator, so that the grid's diagonal is

$$
B-L\ \longrightarrow\ \operatorname{diag}(-3,\,1,\,1,\,1)=D .
$$

The four entries must sum to zero, because a generator of $\mathrm{SU}(4)$ is traceless, so

$$
(\nu,\nu)=-\bigl(\text{the three colour entries}\bigr)=-(1+1+1)=-3 .
$$

Written as a generator,

$$
B-L=\tfrac13 D,\qquad \operatorname{tr}_{\mathbf 4}(B-L)=-\tfrac33+\tfrac13+\tfrac13+\tfrac13=0 ,
$$

and the vanishing of the trace is the same statement as the four diagonal entries summing to nothing. **The lepton cell is minus the colour trace**, which is the corpus's charge-quantisation result read off the grid in one line, and it is why the entry is $-3$ and not a free number.

**Four diagonal cells, three generators.** The diagonal of the $4\times4$ has four cells and the tracelessness condition leaves three independent combinations: $B-L$ in the corner and two in the colour block. The fourth combination — all four entries equal — is the trace direction $iI$, and it is not a generator of $\mathrm{SU}(4)$: it is the direction $\det=1$ removes. **That is the first of the three removed cells, and the other two are the diagonal cells of the next two grids.** So the $4\times4$ holds sixteen cells and fifteen generators, and the missing one is not a hole in the picture but the definition of $\mathrm{SU}(4)$.

## 3. The $\mathrm{SU}(2)_L$ Grid, $2\times2$

**Three generators, four cells, in a $2\times2$.** The index is the left doublet, and the grid names the left weak bosons.

**The grid.** The same drawing as §2, one factor smaller. Rows are *from*, columns are *to*.

$$
\begin{array}{ccc}
 & \substack{\uparrow\\ \text{up-type}} & \substack{\downarrow\\ \text{down-type}}\\[10pt]
\substack{\uparrow\\ \text{up-type}}
 & \substack{W^{3}_{L}\\ \text{the neutral left weak boson}}
 & \substack{W^{+}_{L}\\ \text{the positively charged left weak boson}}\\[10pt]
\substack{\downarrow\\ \text{down-type}}
 & \substack{W^{-}_{L}\\ \text{the negatively charged left weak boson}}
 & \substack{\text{trace}\\ \text{not a generator}}
\end{array}
$$

**The doublets it acts on, named.** The index is filled by whichever left-handed doublet is in play:

| doublet | up-type member | down-type member | colour copies |
|---|---|---|---|
| lepton | $\nu_{eL}$ | $e_{L}$ | $1$ |
| quark | $u_{L}$ | $d_{L}$ | $3$ |

So $\mathrm{SU}(2)_L$ acts on two doublets per generation: one leptonic and one quark, the latter in three colour copies. The $2\times2$ grid above is the same grid for both — what changes is which fermions sit in the two slots.

**The diagonal cell is one generator and the other is the trace.** The two diagonal cells of a $2\times2$ hold two real numbers and the constraint that their sum vanish leaves one, $W^3_L$. The other is the trace, the direction removed by $\det=1$ again. **So $\mathfrak u(2)_L=4=3+1$ and $\mathfrak{su}(2)_L=3$.**

## 4. The $\mathrm{SU}(2)_R$ Grid, $2\times2$

**The grid.** The same drawing, a different copy, and the names change because the particles do.

$$
\begin{array}{ccc}
 & \substack{\uparrow\\ \text{up-type}} & \substack{\downarrow\\ \text{down-type}}\\[10pt]
\substack{\uparrow\\ \text{up-type}}
 & \substack{W^{3}_{R}\\ \text{the neutral right weak boson}}
 & \substack{W^{+}_{R}\\ \text{the positively charged right weak boson}}\\[10pt]
\substack{\downarrow\\ \text{down-type}}
 & \substack{W^{-}_{R}\\ \text{the negatively charged right weak boson}}
 & \substack{\text{trace}\\ \text{not a generator}}
\end{array}
$$

**The doublets it acts on.**

| doublet | up-type member | down-type member | colour copies |
|---|---|---|---|
| lepton | $\nu_{eR}$ | $e_{R}$ | $1$ |
| quark | $u_{R}$ | $d_{R}$ | $3$ |

**The right neutrino is not an addition, and the grid says why.** $\nu_{eR}$ sits in the up-type slot of the right doublet because the right doublet is the doublet of the conjugate quartet $\bar{\mathbf 4}$, and the $\bar{\mathbf 4}$ has four components of which one is the lepton. A model that has to add $\nu_R$ by hand has no right doublet to put it in.

**The two $2\times2$ grids are not the same grid twice.** They are two factors acting on two copies, and on the carrier their generators lie *inside* the $4\times4$ grid rather than beside it: $L_{\vec e_a}$ and $R_{\vec e_a}$ are traceless and skew-adjoint, hence in $\mathfrak{su}(4)$, so the six weak generators form a six-dimensional subalgebra of the fifteen. That is why the frame's $21$ is the dimension of the product group on the declared copy and not the dimension of anything on the carrier. §5 states the arithmetic.

## 5. The Ledger of the Three Grids

**Twenty-four cells, twenty-one generators, three traces.**

| factor | grid | cells | generators | trace | the trace direction |
|---|---|---|---|---|---|
| $\mathrm{SU}(4)$ | $4\times4$ | $16$ | $15$ | $1$ | the diagonal combination $iI$, removed by $\det=1$ |
| $\mathrm{SU}(2)_L$ | $2\times2$ | $4$ | $3$ | $1$ | the diagonal combination $iI$, removed by $\det=1$ |
| $\mathrm{SU}(2)_R$ | $2\times2$ | $4$ | $3$ | $1$ | the diagonal combination $iI$, removed by $\det=1$ |
| **total** | | $\mathbf{24}$ | $\mathbf{21}$ | $\mathbf{3}$ | |

**So $21=24-3$, and the three removed cells are the same cell three times.** In each factor it is the trace direction, the one that $\det=1$ takes out: $\mathfrak u(N)=N^2$ and $\mathfrak{su}(N)=N^2-1$. That is why the frame's arithmetic read as grids is $16-1+4-1+4-1=15+3+3$.

**And the twenty-one survive as twenty-one states, but not one for one in the same order.** Three of them are ingredients: the two neutral components of the weak grids and the $(\nu,\nu)$ corner. §8 states that.

**The one place the three grids are not independent, stated because it is easy to get wrong.** On the formal copy the three factors are a product and the three grids are three independent sets of cells: $15+3+3=21$. On the carrier they are not, because the carrier supplies only $\mathfrak u(4)$:

$$
\dim_{\mathbb R}\mathfrak u(4)=16=15+1 ,
$$

and the six weak generators sit inside the fifteen. So $15+6=21$ is a double count on the carrier and $15+6-6=15$ is the algebra; the twenty-one exists only where the copy is declared, which is why the copy must be declared and cannot be found. The grids of §2, §3 and §4 are drawn on the copy, and that is the sense in which they are three grids and not one.

## 6. Where the Five Names of the Corner Come From

**One cell, five names, and this is the worst collision in the corpus.** The $(\nu,\nu)$ cell of the $4\times4$ grid is written, in the corpus and in the literature:

| name | where it appears | what it names |
|---|---|---|
| $B'_\mu$ | the spectrum, this article | the field |
| $C_\mu$ | proposed here as the unambiguous symbol | the field |
| $A_{15,\mu}$ | the covariant derivative, the fifteenth $\mathrm{SU}(4)$ field | the field |
| $X^0_\mu$ | the $X$-boson notation of the literature, with charge zero | the field |
| $iD$, or $D$ | the algebra articles, $\operatorname{diag}(-3,1,1,1)$ | the generator |
| "$B-L$ boson" | prose everywhere | the charge it carries |
| $B$ | the spectrum table | the field, and this is the collision |

**The collision is with hypercharge.** In the electroweak literature $B_\mu$ is the hypercharge field, a different object, mixed into the photon by a different coefficient. The frame's $B$ is the $(\nu,\nu)$ cell. They are not the same field and they do not even have the same charge: the frame's is $B-L$, the literature's is $Y$. **Write $B'$ or $C$ for the frame's field, and keep $B$ for hypercharge**; no number in any article changes.

## 7. The Sextet, Which Is the Six Cells of the Mixed Band

**Three planes, two cells each, two particles each.** The mixed band of the $4\times4$ grid is the $\nu$ row and the $\nu$ column, and its six off-corner cells are the leptoquarks.

| plane | the two cells | the two particles | $Q$ | $B-L$ | mass |
|---|---|---|---|---|---|
| $\{\nu,r\}$ | $(\nu,r)$ and $(r,\nu)$ | $\bar X^{r}$ and $X^{r}$ | $-\tfrac23$, $+\tfrac23$ | $-\tfrac43$, $+\tfrac43$ | $\sqrt2\,M_{W_R}$ |
| $\{\nu,g\}$ | $(\nu,g)$ and $(g,\nu)$ | $\bar X^{g}$ and $X^{g}$ | $-\tfrac23$, $+\tfrac23$ | $-\tfrac43$, $+\tfrac43$ | $\sqrt2\,M_{W_R}$ |
| $\{\nu,b\}$ | $(\nu,b)$ and $(b,\nu)$ | $\bar X^{b}$ and $X^{b}$ | $-\tfrac23$, $+\tfrac23$ | $-\tfrac43$, $+\tfrac43$ | $\sqrt2\,M_{W_R}$ |

**The charge follows from the two indices, and needs no separate rule.** Moving a lepton into a colour slot changes $B-L$ by $\tfrac13-(-1)=\tfrac43$, and with $T_{3R}=0$ that is $Q=\tfrac12\cdot\tfrac43=+\tfrac23$ for the out-direction and $-\tfrac23$ for the in-direction. **So the sextet's two charge classes are the two directions of its three planes**, and "$X$" without a bar is three particles of charge $+\tfrac23$ while "$\bar X$" is three of charge $-\tfrac23$.

**And $\bar X$ is not a different kind of object.** It is the reverse amplitude of the same plane, which is why its mass is the same and its charge is the opposite. A reader who takes $X$ and $\bar X$ for two species has read a factor of two into the sextet that is not there: there are six particles because there are three colour planes and two directions each.

## 8. The Spectrum: Twenty-One Generators, Twenty-One Particles

**Twenty-one cells hold generators; three of them are ingredients; the ingredients become particles. The two counts agree at the end of the chain and not at the beginning.**

| particle | full name | $Q$ | mass | from which cell |
|---|---|---|---|---|
| $g_{1}\dots g_{8}$ | the eight gluons | $0$ | $0$ | the six off-diagonal cells of the $3\times3$ block and two of its diagonal cells |
| $\gamma$ | the photon | $0$ | $0$ | a mixture of $W^3_L$, $W^3_R$, $B'$ |
| $Z$ | the neutral weak boson | $0$ | $91.2$ GeV | a mixture of $W^3_L$, $W^3_R$, $B'$ |
| $Z_R$ | the heavy right neutral boson | $0$ | $\propto g_R^2v_R^2$ | the third mixture |
| $W^{\pm}$ | the charged weak bosons | $\pm1$ | $80.4$ GeV | the off-diagonal cells of the $L$ grid |
| $W^{\pm}_{R}$ | the charged right bosons | $\pm1$ | $\propto g_R^2v_R^2$ | the off-diagonal cells of the $R$ grid |
| $X^{r},X^{g},X^{b}$ | the leptoquark gauge bosons | $+\tfrac23$ | $\sqrt2\,M_{W_R}$ | the $\nu$ column, below the corner |
| $\bar X^{r},\bar X^{g},\bar X^{b}$ | the antileptoquark gauge bosons | $-\tfrac23$ | $\sqrt2\,M_{W_R}$ | the $\nu$ row, right of the corner |

**The three ingredients and their one rotation.** The cells $(\nu,\nu)$, $(\uparrow,\uparrow)_L$ and $(\uparrow,\uparrow)_R$ are three directions, and no particle is any one of them. The three neutral particles are their combinations:

$$
\gamma=W^{3}_{L}+W^{3}_{R}+\sqrt{\tfrac23}\,B' ,
\qquad
Z,\ Z_R\ \text{the two directions orthogonal to it.}
$$

The coefficients are not free: $\gamma$ is the unique null direction of the $3\times3$ neutral mass matrix. **An ingredient is a cell that no particle occupies, because a particle is made of it** — and that is why $21$ cells and $21$ particles are not the same $21$.

## 9. The Fermions, on the Same Cells

**Sixteen per generation, and they occupy the cells of the $4\times4$ grid times the cells of the two $2\times2$ grids.** A fermion is one quartet index (four values) times one doublet index (two values per chirality), and $4\cdot2=8$ per chirality, so $16$ per generation. **That is the product rule of §1 read off the grids: the $4$ is the quartet's size, the $2$ is a doublet's size, and the second $2$ is the chirality block.** The tables below are the rule written out, one row per value of each index.

**The left octet: the $4\times4$ index times the $L$ grid's up/down.**

| fermion | quartet index | $L$ index | $Q$ | $B-L$ |
|---|---|---|---|---|
| $\nu_{eL}$ | $\nu$ | $\uparrow$ | $0$ | $-1$ |
| $e_{L}$ | $\nu$ | $\downarrow$ | $-1$ | $-1$ |
| $u^{r}_{L}$ | $r$ | $\uparrow$ | $+\tfrac23$ | $+\tfrac13$ |
| $d^{r}_{L}$ | $r$ | $\downarrow$ | $-\tfrac13$ | $+\tfrac13$ |
| $u^{g}_{L}$ | $g$ | $\uparrow$ | $+\tfrac23$ | $+\tfrac13$ |
| $d^{g}_{L}$ | $g$ | $\downarrow$ | $-\tfrac13$ | $+\tfrac13$ |
| $u^{b}_{L}$ | $b$ | $\uparrow$ | $+\tfrac23$ | $+\tfrac13$ |
| $d^{b}_{L}$ | $b$ | $\downarrow$ | $-\tfrac13$ | $+\tfrac13$ |

**The right octet: the same four indices times the $R$ grid.** $\nu_{eR}$, $e_R$, $u^{r}_{R}$, $d^{r}_{R}$, $u^{g}_{R}$, $d^{g}_{R}$, $u^{b}_{R}$, $d^{b}_{R}$, with $Q$ and $B-L$ identical to the left octet's rows. What differs is which $2\times2$ grid the doublet index belongs to.

**Three remarks about the pairing.**

- **The colour index is $\mathbf3$ on the left and $\bar{\mathbf3}$ on the right.** The four labels are the same four, but the right octet sits in the conjugate quartet, which is why the sixteen is anomaly-free by construction: the representation is complex and its conjugate appears in equal measure.
- **A massive fermion needs both octets.** $e_L$ and $e_R$ are two cells and one electron at low energy; the electron is the Dirac combination of the two. So a count of *cells* is sixteen and a count of *particles* is fewer.
- **Three generations multiply the table by three**, so forty-eight fermions. The number of generations is not fixed by the grid; that is the subject of a separate article and the grid says nothing about it.

## 10. The Scalars, Which Are Not on the Grids

**Twenty-four real components, twelve eaten, twelve surviving.** Scalars are bosons and are not gauge bosons, so they do not occupy a cell of any grid: a scalar is a field whose value is a vector in a representation, not a direction in the algebra.

**The Higgs is here, and it is $H$.** The name is stated once because the article would otherwise be unsearchable: the model's Higgs field is the bidoublet, and the observed $125$ GeV scalar is one of the two neutral survivors of its eight real components. Two differences from the Standard Model's Higgs are structural and not editorial, and both are counted below: **the field is a bidoublet $(\mathbf1,\mathbf2,\mathbf2)$, a $2\times2$ matrix of complex fields, and not a doublet**; and it is not alone in the sector, since $\Phi$ breaks the fourth colour and leaves survivors of its own.

| field | full name | representation | real components | role |
|---|---|---|---|---|
| $\Phi$ | the fourth-colour scalar | $(\mathbf4,\mathbf1,\mathbf2)$ | $16$ | breaks $\mathrm{SU}(4)$ and $\mathrm{SU}(2)_R$ |
| $H$ | the Higgs: the electroweak bidoublet | $(\mathbf1,\mathbf2,\mathbf2)$ | $8$ | breaks the electroweak pair |
| $\Sigma$ | the adjoint scalar | $(\mathbf{15},\mathbf2,\mathbf2)$ | $120$ | not minimal; splits the mass relations |

**The twelve that survive.**

| name | symbol | real components | $Q$ | status |
|---|---|---|---|---|
| the colour-triplet scalar, three colour states | $S^{\alpha}$ | $6$ | $+\tfrac23$ or $-\tfrac13$, whichever the vacuum leaves | unseen |
| the charged singlet, from $\Phi$ | $h$ | $2$ | $0$ or $-1$, one of the two | unseen |
| the charged Higgs, from $H$ | $H^{\pm}$ | $2$ | $\pm1$, one complex field | unseen |
| the lighter neutral Higgs, from $H$ | $h^{0}$ | $1$ | $0$ | the observed $125$ GeV candidate |
| the heavier neutral Higgs, from $H$ | $H^{0}$ | $1$ | $0$ | unseen |

$6+2+2+1+1=12$. The two neutral states mix, so $h^0$ and $H^0$ are interaction eigenstates and the mass eigenstates are their combinations.

**Read the four columns of that table as four different objects, because that is where the counting goes wrong.** $H^{\pm}$ is the charged Higgs, one complex field and two real components. $h^0$ and $H^0$ are the two neutral Higgses, one real component each, and the $125$ GeV boson is the lighter mass eigenstate of their mixture. $h$ is not a Higgs at all: it comes from $\Phi$'s lepton doublet, it is $\mathrm{SU}(2)_L$ neutral, and it is the model's own state with no Standard Model counterpart. **Four of the twelve survivors are Higgs and eight are not**, and a sentence that calls all twelve "the Higgs sector" is the commonest error in this family.

**The twelve that are eaten, and the names they do not get.** Six components of $\Phi$ become the longitudinal modes of the six leptoquarks, two become those of $W^{\pm}_R$, and four components of $H$ become those of $W^{\pm}$, $Z$ and $Z_R$. **An eaten component has no name of its own: it is the third polarisation of the boson that ate it.** So the count of named scalars is twelve, and the other twelve are not lost but transferred to the gauge grid.

**Two things the tables do not say, and one the corpus retracted.** Both belong here because this article lists sectors and a list invites the reading that each sector is settled.

- **The frame predicts no mass relation, because it fixes no scalar multiplet.** What is structural is a *count*: one bidoublet puts the down-type quarks and the charged leptons in one Yukawa term, so one matrix serves two sectors and the spectra come out **proportional**. That sentence has no scale in it and no coupling in it. The numerical equalities people write from it — $m_d=m_e$, $m_u=m_\nu$ — are the **Pati–Salam literature's published condition, not this model's prediction**, and the corpus quarantines them in [The Coupling Sector of the Fourth-Colour Left–Right Model: A Retired Working Record](../articles_internal/the-coupling-sector-of-the-fourth-colour-model.html), whose ledger note says so in its first line. Of the four per-generation ratios the literature then checks, two hold and two fail by orders of magnitude ($m_d/m_e=1$ against a measured $9.1$, $m_u/m_\nu=1$ against $\sim4\times10^{7}$). **A model that claims no number misses nothing and proves nothing**; that is the trade, and it is the corpus's own verdict on its own coupling sector.
- **Two neutral states is structural; their mixing angle is not.** The bidoublet's eight real components leave two neutral directions after the breaking, and that count is arithmetic. But the angle that rotates them into mass eigenstates is an entry of the potential, so it is scale-bearing and not fixed. **The $125$ GeV state is therefore a mixture of two directions, and *which* mixture is not something the frame decides.**

**The word to avoid is "the Higgs coupling".** This model leaves all three gauge couplings symbolic and predicts none of them; it fixes no scalar multiplet; and the observed state is a mass eigenstate of an unfixed mixing. **So the corpus does not have a coupling claim to patch — it has no coupling claims at all in this sector**, and an article that says "the minimal sector gives $m_d=m_e$" has imported the literature's claim into a model whose ledger refuses it.

**One caution on the letters.** The symbols $S$, $h$, $H^{\pm}$, $h^0$, $H^0$ are conventional and are introduced here so that the twelve can be listed; the corpus names them "a colour triplet, a charged singlet, $H^{\pm}$ and two neutral states". The multiplets, the counts and the fates are the corpus's; no claim depends on the choice of letter.

## 11. Names That Collide, and the One-Word Fix

| the collision | what it hides | the fix |
|---|---|---|
| "the six" | the sextet's six cells against the six weak cells; not even orthogonal | *the leptoquark sextet*, *the weak six* |
| "neutral" | three gauge directions against two scalar states; $3+2$ adds bosons to scalars | *gauge-neutral*, *scalar-neutral* |
| "colour" | the four labels, the lepton line, the three, and "colour triplet" | *the four*, *the fourth line*, *the three*, *colour triplet* |
| "mass" | the quaternionic norm, the finite mass $m$, an eigenvalue, and a scale | name which of the four |
| "$X$" | six particles in two charge classes | $X^{\alpha}$ and $\bar X^{\alpha}$ |
| "$B$" | the $(\nu,\nu)$ cell against the hypercharge field | $B'$ or $C$ for the cell, $B$ for hypercharge |
| "the Higgs" | the field $H$ against its $125$ GeV mass eigenstate against the whole scalar sector | *the field $H$*, *the $125$ GeV state*, *the scalar sector* |

**The mass collision is the worst.** The quaternionic norm $\mathcal N=-m^2c^2$ is a quartic invariant a boost preserves. The finite mass $m$ is a parameter of the finite Dirac operator. A mass eigenvalue is what a mass matrix returns. A mass scale $M_C$, $M_R$, $M_W$ is where a mass is generated. $M_X=\sqrt2\,M_{W_R}$ relates two of the fourth kind. **The equality $m_d=m_e$ is not of those four kinds at all: it is the Pati–Salam literature's per-generation condition, transcribed and flagged, and this model predicts no such relation because it fixes no scalar multiplet.** A sentence that says "the mass is $M_C$" mixes the fourth kind with the third.

## 12. The Seven Cells Touching the $\nu$ Index

**One arrangement fact, and it is the grid's own.** Seven generators have a nonzero entry in the $\nu$ row or the $\nu$ column. In the grid of §2 they are visible without any computation: everything in the $\nu$ row, everything in the $\nu$ column, and the corner.

| what it does with the $\nu$ line | cells | count | names |
|---|---|---|---|
| acts on it as a phase | $(\nu,\nu)$ | $1$ | $B'$ |
| carries it out into colour | the $\nu$ column below the corner | $3$ | $X^{r},X^{g},X^{b}$ |
| carries colour into it | the $\nu$ row right of the corner | $3$ | $\bar X^{r},\bar X^{g},\bar X^{b}$ |
| neither | the $3\times3$ colour block | $8$ | $g_{1}\dots g_{8}$ |

$1+3+3=7$, and the $3+3$ is the two directions of the three mixed planes. **So the sextet is exactly the set of gauge bosons that can change the lepton number, the corner measures it, and the eight gluons are the block that cannot.**

> **What this is not.** The $\nu$ index is the algebra's time unit, so "touching the $\nu$ index" is the algebra's own statement. It does not follow that these seven are spacetime objects: they are internal gauge directions that happen to touch the coordinate $e_t$, and the identification of the four coordinates with colour is the declaration of §1.

## The Checks

| claim | check | result |
|---|---|---|
| the cells of the $4\times4$ | $4$ diagonal $+\,6$ planes $\times2$ | $16$ |
| its diagonal cells | $4$ cells, one trace removed | $3$ generators |
| its generators | $16-1$ | $15$ |
| its four blocks | $6+9+1$ cells | $16$ |
| its generators by block | $6+8+1$ | $15$ |
| the cells of a $2\times2$ | $2$ diagonal $+\,1$ plane $\times2$ | $4$ |
| its generators | $4-1$ | $3$ |
| the three grids | $16+4+4$ | $24$ |
| the twenty-one | $15+3+3$ | $21$ |
| the traces | $24-21$ | $3$ |
| the corner | $(\nu,\nu)$ entry against the colour trace | $-3$ against $1+1+1$ |
| the trace over the quartet | $-3+1+1+1$ | $0$ |
| the sextet | $3$ planes $\times2$ directions | $6$ |
| the sextet's charge | $\tfrac12\bigl(\tfrac13-(-1)\bigr)$ | $+\tfrac23$ |
| the gluons | $6$ off-diagonal $+\,2$ Cartan | $8$ |
| the leptons per octet | $4$ quartet $\times$ $2$ doublet minus $6$ quarks | $2$ |
| the fermion count, as a product | $4\times2\times2$ | $16$ |
| the two fermion blocks | $4\times2\times1$ and $4\times1\times2$ | $8+8$ |
| the blocks against the product | $4\times2\times(1+1)$ | $16$ |
| the count with the rank in place of the dimension | $3\times2\times2$ | $12$, wrong |
| the fermions per generation | $8+8$ | $16$ |
| the surviving scalars | $6+2+2+1+1$ | $12$ |
| the eaten scalars | $6+2+4$ | $12$ |
| the cells touching $\nu$ | $1+3+3$ | $7$ |
| the block that does not | $8$ | $8$ |

## Summary

**The model.** The fourth-colour left–right model, $G_{4LR}=\mathrm{SU}(4)\times\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$, the frame the corpus adopts, with its one load-bearing declaration that the line $\mathbb C e_t$ is the lepton.

**The structure.** One group, three factors, $15+3+3=21$, acting on a quartet and two doublets.

**The three numbers.** The model's only numbers are the sizes of its three defining representations, $4$, $2$, $2$. **The bosons are their sum of squares**, $4^2+2^2+2^2=24$ cells minus three traces; **the fermions are their product**, $4\times2\times2=16$, taken block by block as $4\times2\times1$ plus $4\times1\times2$ because one factor is a singlet in each block.

**The picture.** A $4\times4$ grid and two $2\times2$ grids. A cell is half a plane's worth of generator; the plane's two particles are the two combinations of its two cells.

**The count.** Twenty-four cells, twenty-one generators, three traces. The three traces are the same direction three times, the one $\det=1$ removes. So $21=24-3$.

**The blocks of the $4\times4$.** The $3\times3$ colour block holds the eight gluons, the mixed band holds the six leptoquarks, and the $(\nu,\nu)$ corner holds $B-L$. Six plus nine plus one is sixteen cells; six plus eight plus one is fifteen generators.

**The corner is forced.** Its entry is minus the colour trace, so the quartet's diagonal sums to zero, and that is charge quantisation in one line.

**The spectrum.** Twenty-one cells, three of them ingredients, and the three ingredients rotate into three neutral particles. An ingredient is a cell no particle occupies, because a particle is made of it.

**The fermions.** Sixteen per generation, a quartet index times a doublet index, and the colour is $\mathbf3$ on the left and $\bar{\mathbf3}$ on the right.

**The scalars.** Not on the grids: twenty-four real components, twelve eaten into longitudinal modes, twelve named survivors. **The Higgs is among them and is $H$, the bidoublet $(\mathbf1,\mathbf2,\mathbf2)$**: its four surviving real components are the charged Higgs $H^{\pm}$ and the two neutral states $h^0$ and $H^0$, whose lighter mass eigenstate is the observed $125$ GeV boson. The other eight survivors come from $\Phi$ and are not Higgs.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\nu,r,g,b$ | the four labels of the quartet: the lepton line and three colours |
| $(i,j)$ | a cell of the $4\times4$ grid, the direction moving $j$ into $i$ |
| $B'_\mu$, also $C_\mu$ | the $(\nu,\nu)$ cell; $A^{15}_\mu$ in the covariant derivative, $iD$ as a generator |
| $X^{\alpha}$, $\bar X^{\alpha}$ | the $\nu$ column and the $\nu$ row, $\alpha=r,g,b$, $Q=\pm\tfrac23$ |
| $g_{1}\dots g_{8}$ | the $3\times3$ colour block |
| $T^{c}_{3}$, $T^{c}_{8}$ | the colour block's Cartan directions |
| $W^{\pm}_{L}$, $W^{3}_{L}$ | the three generators of the $L$ grid |
| $W^{\pm}_{R}$, $W^{3}_{R}$ | the three generators of the $R$ grid |
| ingredient | a cell no particle occupies, because a particle is made of it |

## Further Reading

- [The Fourth-Colour Left–Right Model: Four Colours, $21$ Generators, One Declaration](the-fourth-colour-left-right-model.html). The frame, the declaration, and the ledger $\dim\mathfrak u(4)=16=15+1$.
- [The Breaking Chain and the Boson Spectrum: One Flag, Three Scales, Twenty-One Bosons](the-breaking-chain-and-the-boson-spectrum.html). The fates and the scales.
- [Charge Quantisation from the Fourth Colour: One Trace, One Third, and Where the Twenty-One Generators Go](charge-quantisation-from-the-fourth-colour-one-trace-one-third.html). The trace, and the two misreadings of the ledger.
- [The Scalar Sector and the Leptoquark Bounds: Twenty-Four Real Components, Six Unseen States, Two Scales](the-scalar-sector-and-the-leptoquark-bounds.html). The scalars and the sextet's bounds.
- [The Yukawa Sector: Fermion Mass Matrices and Their Diagonalisation](the-yukawa-sector-fermion-mass-matrices-and-their-diagonalisation.html). Where the fermion masses come from.
- [The Temporal Dimension: Why the Temporal Unit Is the Identity](the-temporal-dimension-why-the-temporal-unit-is-the-identity.html). Why the lepton index is the time unit.
