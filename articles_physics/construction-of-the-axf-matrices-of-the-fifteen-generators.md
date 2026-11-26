# __Construction of the AXF Matrices of the Fifteen Generators: Fifteen Arrays and Six $\mathfrak{so}(4)$ Halves__

## Introduction

**Everything on this page is built from six arrays.** The six are the axis-free arrays of left and right multiplication by the three vector units $\vec e_x,\vec e_y,\vec e_z$. With the two identities of the scalar unit they are eight arrays, and every one of the fifteen generators is one of three operations applied to them: **halve one array**, **multiply one array by $i$**, or **add and subtract two arrays** (two, once, for each diagonal). No array below is chosen, and no array below is a Pauli array or a gamma array. **The six halved arrays are printed here too, and they are not generators**: they are the six planes of $\mathfrak{so}(4)$, a real subalgebra of the fifteen, and §*Part I* states exactly what they are.

**The order of the article is the order of the construction.** §*Part I* prints the six arrays of $\mathfrak{so}(4)$, which are the raw arrays halved. §*Part II* builds the fifteen of $\mathfrak{su}(4)$ in three steps: the eight arrays, the sixteen words, the six pairs. §*Part III* reads the result back: one table of properties, one boson per array, and the mass each one gets.

**The counts, in one display.**
$$
\underbrace{16}_{4\times4}-\underbrace{1}_{\text{the trace}}=15,
\qquad
\underbrace{6}_{\text{pairs}}\times2+\underbrace{3}_{\text{diagonals}}=15 .
$$
**Six composites beside fifteen generators is not a contradiction**, and it is why the article prints the six half-arrays beside them: **the six are a second basis of a six-dimensional subspace, and §*The Fifteen, Counted* proves it with a rank.**

**The frame.** The axis-free frame of [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html). The array of an operator is read by columns, the $j$-th column being the product with the $j$-th unit:
$$
L_{\mathrm{axf}}(\tilde Q)_{\imath\jmath}=\bigl[\tilde Q\,e_{\jmath}\bigr]_{\imath},\qquad
R_{\mathrm{axf}}(\tilde Q)_{\imath\jmath}=\bigl[e_{\jmath}\,\tilde Q\bigr]_{\imath},
\qquad e_\mu\in\{e_t,\vec e_x,\vec e_y,\vec e_z\}.
$$
**The order is $(e_t,\vec e_x,\vec e_y,\vec e_z)$, the product is $\vec e_x\vec e_y=\vec e_z$ cyclically, and $E_{jk}$ is the matrix unit in that order.** The scalar unit $e_t$ is the identity of the algebra, so $e_t\vec X=\vec Xe_t=\vec X$: the temporal line is the lepton line of the model, and that is the whole of the identification.

**Two words that name a side and not a chirality.** $L$ and $R$ name the side of the multiplication in the algebra, left or right. **They do not name group factor of this model**: the six arrays they index are a real basis of $\mathfrak{so}(4)\subset\mathfrak{su}(4)$, and no fermion chirality is assigned to a side here. **The chirality assignment is a declaration made below $M_C$**, in the next section of the corpus.

## Part I. The Six Arrays of $\mathfrak{so}(4)$ from the Axis-Free Arrays

**The definition, and the only number in it.**
$$
T^{L}_{a}:=\tfrac12\,L_{\mathrm{axf}}(\vec e_a),\qquad
T^{R}_{a}:=\tfrac12\,R_{\mathrm{axf}}(\vec e_a),\qquad a=x,y,z .
$$
**These six are not generators of the model.** They are the six planes of $\mathfrak{so}(4)$, a real six-dimensional subalgebra of the fifteen with rank two, and they add no direction to it. **They are printed first because they are the input of Part II**: the raw arrays $\ell_a,r_a$ are twice them, and the pair resolution of §*Step 3* is written in terms of them. **What they are, and what they are not, is settled in §*The Fifteen, Counted*.**

**The three left arrays.** Each is a signed permutation, read by columns: the $j$-th column is $\vec e_a e_j$.

$$
\ell_x:=L_{\mathrm{axf}}(\vec e_x)=\begin{pmatrix}0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0\end{pmatrix}
$$

$$
\ell_y:=L_{\mathrm{axf}}(\vec e_y)=\begin{pmatrix}0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0\end{pmatrix}
$$

$$
\ell_z:=L_{\mathrm{axf}}(\vec e_z)=\begin{pmatrix}0 & 0 & 0 & -1 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0\end{pmatrix}
$$

**The three right arrays.** The same reading with the factors exchanged.

$$
r_x:=R_{\mathrm{axf}}(\vec e_x)=\begin{pmatrix}0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0\end{pmatrix}
$$

$$
r_y:=R_{\mathrm{axf}}(\vec e_y)=\begin{pmatrix}0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0\end{pmatrix}
$$

$$
r_z:=R_{\mathrm{axf}}(\vec e_z)=\begin{pmatrix}0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0\end{pmatrix}
$$

**The one structural fact about the six, and it is visible in the two arrays of the same direction.** $\ell_x$ and $r_x$ are the same signed permutation and differ only in the signs of the second plane. Both send $e_t\mapsto\vec e_x$ and $\vec e_x\mapsto-e_t$; both send the pair $\{\vec e_y,\vec e_z\}$ to itself; **the block $\{t,x\}$ is identical and the block $\{y,z\}$ is opposite**. The same holds for $y$ and $z$ with the complement cycled. **That single fact is the reason a sum can isolate a plane**, and Part II Step 3 is nothing but that fact used six times.

**The properties inherited from the algebra.**
$$
\ell_a^{2}=r_a^{2}=-\mathrm I_4,\qquad \ell_x\ell_y=\ell_z,\qquad r_xr_y=-r_z,\qquad \ell_a r_b=r_b\ell_a .
$$
**The first is $\vec e_a^2=-1$; the second says left multiplication is a homomorphism; the third says right multiplication is an anti-homomorphism**, $R_AR_B=R_{BA}$; **the fourth is associativity**, $(\vec e_a\tilde X)\vec e_b=\vec e_a(\tilde X\vec e_b)$, and it will be the reason the two triples commute.

**The model's six, at their own normalisation.** One direction printed left next to right, so that the two signs of the second plane stand in one picture.

$$
T^{L}_{x}=\tfrac12\ell_x=\begin{pmatrix}0 & -\tfrac12 & 0 & 0 \\ \tfrac12 & 0 & 0 & 0 \\ 0 & 0 & 0 & -\tfrac12 \\ 0 & 0 & \tfrac12 & 0\end{pmatrix},\qquad
T^{R}_{x}=\tfrac12 r_x=\begin{pmatrix}0 & -\tfrac12 & 0 & 0 \\ \tfrac12 & 0 & 0 & 0 \\ 0 & 0 & 0 & \tfrac12 \\ 0 & 0 & -\tfrac12 & 0\end{pmatrix}
$$

**The same pattern, for the six, with the entries and not the displays.**

| array | $(t,a)$ | $(a,t)$ | $(b,c)$ | $(c,b)$ |
| --- | --- | --- | --- | --- |
| $T^{L}_{a}$ | $-\tfrac12$ | $+\tfrac12$ | $-\tfrac12$ | $+\tfrac12$ |
| $T^{R}_{a}$ | $-\tfrac12$ | $+\tfrac12$ | $+\tfrac12$ | $-\tfrac12$ |

**Read the table as row then column, and read the two blocks as two planes.** $T^{L}_{a}$ sends $e_t\mapsto\tfrac12 e_a$ and $e_a\mapsto-\tfrac12 e_t$, so it turns the plane $\{t,a\}$; and it sends $e_b\mapsto\tfrac12 e_c$ and $e_c\mapsto-\tfrac12 e_b$, so it turns the plane $\{b,c\}$. **Two planes, four cells, one array.** $T^{R}_{a}$ agrees on the first plane and reverses on the second. The entries are the same six numbers in both rows, and the difference is two signs.

**Why the half, in one line.** The raw arrays close with $2$ in the structure constants,
$$
[\ell_a,\ell_b]=2\epsilon_{abc}\,\ell_c ,
$$
so
$$
[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}\,T^{L}_{c}
$$
with no constant left over. **The half is the number that removes the $2$, and it is the only number in the definition of the six.**

**The three brackets, all exact.**
$$
[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}T^{L}_{c},\qquad
[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}T^{R}_{c},\qquad
[T^{L}_{a},T^{R}_{b}]=0 .
$$
**The minus in the second is the anti-homomorphism of the properties display above**, and it is a sign inside the triple, not a different algebra: $\{-T^{R}_{a}\}$ closes with $+\epsilon_{abc}$. **The third line is the one that matters for the model.** Two triples that commute span $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, a six-dimensional real subalgebra of $\mathfrak{su}(4)$. **It is not the model's weak pair.** The weak factors arrive with the doublet index at the transition, and no generator of them is among the fifteen.

**The six halves split $\mathfrak{so}(4)$ into its self-dual and anti-self-dual parts, and the star says which is which.** Read an array as the two-form $\omega=\tfrac12\omega_{jk}\,dx^j\wedge dx^k$ with $\omega_{jk}=M_{jk}$, and fix the star by
$$
\star(dt\wedge dx)=dy\wedge dz,\qquad \star(dt\wedge dy)=dz\wedge dx,\qquad \star(dt\wedge dz)=dx\wedge dy .
$$
**The star here is the star of $\mathbb{R}^4$ with the Euclidean metric, the four signs all plus**, which is the metric of the frame and the one the Rotors article uses; on two-forms it satisfies $\star^2=+1$, so its eigenvalues are $\pm1$ and the split below is a split into eigenspaces. **With the Minkowski star the same computation would give $\star^2=-1$ and eigenvalues $\pm i$, and the self-dual statement would be false as written** — the definiteness is what is being used.

Then, for every one of the six,
$$
\star\,\omega(T^{L}_{a})=+\omega(T^{L}_{a}),\qquad \star\,\omega(T^{R}_{a})=-\omega(T^{R}_{a}),
$$
six checks and six hits. **So the left triple spans the self-dual three-space of $\Lambda^{2}\mathbb{R}^{4}$, the right triple the anti-self-dual one, and $\mathfrak{so}(4)=\mathfrak{su}(2)_{+}\oplus\mathfrak{su}(2)_{-}$ is this display read as a statement about algebras.** For $a=x$ the coefficients are $\omega_{tx}=\omega_{yz}=-\tfrac12$ on the left and $\omega_{tx}=-\tfrac12$, $\omega_{yz}=+\tfrac12$ on the right: the same number on the plane $\{t,x\}$ and opposite numbers on $\{y,z\}$. **The same split is visible in the three brackets of §*Part I* with no star at all**: the left triple closes with $+\epsilon_{abc}$ and the right with $-\epsilon_{abc}$, and that sign is what distinguishes the two eigenspaces.

**The properties of the six, in one line each.** Anti-Hermitian, because they are real and antisymmetric. Traceless. $\operatorname{tr}(X^{\dagger}X)=1$. Spectrum $\pm\tfrac i2$, each twice. Four cells. **No array of the six is one cell wide**, and that is already the reason the fifteen are built in pairs.

**The doublet reading, three sentences, and then dropped.** The same abstract generator also acts on a two-row doublet, where it is $\tfrac i2$ times a $2\times2$ array of Pauli type. **That array belongs to the copy index of the sixteen and not to the quartet**, so it is a different carrier and a different array, and it is not printed here. What is printed here is the carrier's reading, which is the one the two-sided action supplies — **and it is the reading that shows the six sitting inside the fifteen rather than beside it.**

## Part II. The Fifteen of $\mathfrak{su}(4)$ in Three Steps

**The construction is the one of [Building the Two Bases of $\mathfrak{su}(4)$ from the Axis-Free Left and Right Matrices](../articles_internal/structures/structure-SU4-basis-construction.html), and it has three steps.** Step 1 names the raw material; Step 2 makes the sixteen words and deletes the trace; Step 3 sums and subtracts the six pairs. **Steps 1 and 2 are forced. Step 3 is one choice, and it is the choice that puts one plane in one array.** The choice is not arbitrary even so: §*The Unique Property of the Physics Base* of that article proves the pair resolution is the only basis of the fifteen that a diagonal adjoint $M^2$ admits, with "one plane", "eigenline of the pair" and "diagonal mass matrix" three names for one condition.

### Step 1. Eight Arrays, Two of Them the Identity

**Both families are linear in the algebra element**, so the array of a general element is a combination of four arrays per side, and the eight
$$
L_{\mathrm{axf}}(e_\mu),\quad R_{\mathrm{axf}}(e_\nu),\qquad \mu,\nu\in\{t,x,y,z\},
$$
are the whole input. **Six are distinct and two coincide**, because the scalar unit acts the same on both sides:
$$
L_{\mathrm{axf}}(e_t)=R_{\mathrm{axf}}(e_t)=\mathrm I_4 .
$$
**The six distinct ones are $\ell_x,\ell_y,\ell_z,r_x,r_y,r_z$, printed in §*Part I*.** Each is a signed permutation, orthogonal, of determinant $+1$ and trace $4\delta_{\mu t}$. **$\mathrm I_4$ is the degenerate member of the same family**, one signed permutation with no transpositions; the count of eight is a count of signed permutations, and the six distinct ones are the ones worth printing.

**Nothing here is a frame chosen for the occasion.** The eight arrays are the multiplication table of the algebra read twice, once from each side. **A reader who wants to know where $\ell_x$ comes from is answered by four words: left multiplication by $\vec e_x$.**

### Step 2. The Sixteen Words, Minus One, Times $i$

**The definition of a word.** A product of one left array with one right array:
$$
W_{\mu\nu}:=L_{\mathrm{axf}}(e_\mu)\,R_{\mathrm{axf}}(e_\nu).
$$
**Proposition.** The sixteen $W_{\mu\nu}$ are a basis of $M_4(\mathbb{R})$, and they are orthogonal in the trace form,
$$
\operatorname{tr}\bigl(W_{\mu\nu}^{\mathsf T}W_{\mu'\nu'}\bigr)=4\,\delta_{\mu\mu'}\delta_{\nu\nu'} .
$$
**Both checks are recomputed here: $256$ pairs, $256$ hits.**

**The six with one scalar index are the raw arrays again**, $W_{ta}=r_a$ and $W_{at}=\ell_a$, and they are real antisymmetric, so they are anti-Hermitian as they stand. **The nine with both indices vector are real symmetric**, so they need the factor $i$ and nothing else:
$$
iN_{jk}:=i\,W_{jk}=i\,\ell_jr_k,\qquad j,k=x,y,z .
$$

**The nine, one to a display.**

$$
iN_{xx}=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & -i & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & i\end{pmatrix}
$$

$$
iN_{xy}=\begin{pmatrix}0 & 0 & 0 & i \\ 0 & 0 & -i & 0 \\ 0 & -i & 0 & 0 \\ i & 0 & 0 & 0\end{pmatrix}
$$

$$
iN_{xz}=\begin{pmatrix}0 & 0 & -i & 0 \\ 0 & 0 & 0 & -i \\ -i & 0 & 0 & 0 \\ 0 & -i & 0 & 0\end{pmatrix}
$$

$$
iN_{yx}=\begin{pmatrix}0 & 0 & 0 & -i \\ 0 & 0 & -i & 0 \\ 0 & -i & 0 & 0 \\ -i & 0 & 0 & 0\end{pmatrix}
$$

$$
iN_{yy}=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & -i & 0 \\ 0 & 0 & 0 & i\end{pmatrix}
$$

$$
iN_{yz}=\begin{pmatrix}0 & i & 0 & 0 \\ i & 0 & 0 & 0 \\ 0 & 0 & 0 & -i \\ 0 & 0 & -i & 0\end{pmatrix}
$$

$$
iN_{zx}=\begin{pmatrix}0 & 0 & i & 0 \\ 0 & 0 & 0 & -i \\ i & 0 & 0 & 0 \\ 0 & -i & 0 & 0\end{pmatrix}
$$

$$
iN_{zy}=\begin{pmatrix}0 & -i & 0 & 0 \\ -i & 0 & 0 & 0 \\ 0 & 0 & 0 & -i \\ 0 & 0 & -i & 0\end{pmatrix}
$$

$$
iN_{zz}=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & -i\end{pmatrix}
$$

**Why the factor $i$ is forced and not chosen.** Every generator of $\mathfrak{su}(4)$ is anti-Hermitian. A real antisymmetric array is anti-Hermitian already; a real symmetric one is Hermitian and must be multiplied by $i$. **The split $6+9$ is the count of scalar indices, and the $i$ is the sign of the nine.**

**Deleting the trace is deleting one word, and that is why the count is $15$.** Exactly one of the sixteen has a trace, namely $W_{tt}=\mathrm I_4$, the product of the two scalar units. **So "remove the trace" is not an operation on a sum: it is the deletion of a single word**, and $16-1=15$ is a count of index pairs. The same fifteen is the number of cells of the $4\times4$ grid with the corner dropped.

**The fifteen as they stand are a basis of the corpus, the maths base.** Nothing is added, halved or rescaled: six raw arrays and nine products times $i$. Its trace form is inherited from the words, $\operatorname{tr}(G^{\dagger}G)=4$ on each.

**What the maths base spends.** A word moves four cells, $\ell_x$ moves the pairs $(t,x)$ and $(y,z)$. **Taking the words whole therefore means that no generator of this basis is one cell wide**, and a reader looking for a single particle finds two planes in one array. That is the whole of the choice Step 3 makes.

### Step 3. The Six Pairs, Sum and Difference

**One operation, applied to pairs of words.** For each of the six unordered index pairs $\{\mu,\nu\}$ replace the two words of the pair by their half-sum and half-difference:
$$
P^{+}_{\mu\nu}:=\tfrac12\bigl(W_{\mu\nu}+W_{\nu\mu}\bigr),\qquad
P^{-}_{\mu\nu}:=\tfrac12\bigl(W_{\mu\nu}-W_{\nu\mu}\bigr).
$$
**Why it works is the structural fact of §*Part I*, used six times.** The two words of a pair are the same signed permutation and differ only in the signs of one of the two planes they move. **So the sum keeps the plane on which they agree, the difference keeps the plane on which they disagree, and both results are supported on a single plane.** Two four-cell words give two two-cell arrays.

**The six pairs and their twelve outputs.** The sign of a half-difference is the orientation sign of the four indices $(\mu,\nu,\mu',\nu')$ against $(t,x,y,z)$, with $\{\mu',\nu'\}$ the complementary pair written in ascending order.

| pair | the two words | half-sum | half-difference |
| --- | --- | --- | --- |
| $\{t,x\}$ | $W_{tx}=r_x$, $W_{xt}=\ell_x$ | $-A_{tx}$ | $+A_{yz}$ |
| $\{t,y\}$ | $W_{ty}=r_y$, $W_{yt}=\ell_y$ | $-A_{ty}$ | $-A_{xz}$ |
| $\{t,z\}$ | $W_{tz}=r_z$, $W_{zt}=\ell_z$ | $-A_{tz}$ | $+A_{xy}$ |
| $\{x,y\}$ | $W_{xy}=N_{xy}$, $W_{yx}=N_{yx}$ | $-S_{xy}$ | $+S_{tz}$ |
| $\{x,z\}$ | $W_{xz}=N_{xz}$, $W_{zx}=N_{zx}$ | $-S_{xz}$ | $-S_{ty}$ |
| $\{y,z\}$ | $W_{yz}=N_{yz}$, $W_{zy}=N_{zy}$ | $-S_{yz}$ | $+S_{tx}$ |

**Read the third column as one sentence.** The half-sum is always **minus** the array on the pair's own two indices; the half-difference is **plus or minus** the array on the complementary pair. **Take the pair $\{t,a\}$: the agreement is the plane $\{t,a\}$, which is a leptoquark plane, and the disagreement is the plane $\{b,c\}$, which is a spatial plane.** Take the pair $\{b,c\}$: the agreement is the real spatial array $-S_{bc}$ and the disagreement is the real leptoquark array $\pm S_{ta}$.

**Six of the twelve outputs are generators as they stand and six are not.** The three outputs on a pair $\{t,a\}$ are real antisymmetric, $A_{ta}$ and $A_{bc}$, which is $\mathfrak{su}(4)$ already; the three outputs on a pair $\{b,c\}$ are real symmetric, $S_{bc}$ and $S_{ta}$, and they take the factor $i$ of Step 2 like the other symmetric words. **That is why the displays below write $iS_{jk}$ and not $S_{jk}$, and it is the same rule as before, not a second one.**

**The identity behind the table, in one line.** For $\{a,b,c\}=\{x,y,z\}$ cyclic, with $A_{bc}$ written on the complement in that same cyclic order,
$$
A_{ta}=-\tfrac12\bigl(W_{ta}+W_{at}\bigr),\qquad
A_{bc}=+\tfrac12\bigl(W_{ta}-W_{at}\bigr),
$$
**and this is the sentence the model is built on**: the leptoquark plane is where left and right multiplication agree, and the spatial plane is where they disagree. **The half is what makes these two lines integral.**

**The six mixed planes, three displays.** $A_{jk}=E_{jk}-E_{kj}$ and $iS_{jk}=i(E_{jk}+E_{kj})$.

$$
A_{tx}=\begin{pmatrix}0 & 1 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix},\qquad iS_{tx}=\begin{pmatrix}0 & i & 0 & 0 \\ i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

$$
A_{ty}=\begin{pmatrix}0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix},\qquad iS_{ty}=\begin{pmatrix}0 & 0 & i & 0 \\ 0 & 0 & 0 & 0 \\ i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

$$
A_{tz}=\begin{pmatrix}0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ -1 & 0 & 0 & 0\end{pmatrix},\qquad iS_{tz}=\begin{pmatrix}0 & 0 & 0 & i \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ i & 0 & 0 & 0\end{pmatrix}
$$

**The six spatial arrays, three displays.**

$$
A_{xy}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix},\qquad iS_{xy}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}
$$

$$
A_{xz}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0\end{pmatrix},\qquad iS_{xz}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i \\ 0 & 0 & 0 & 0 \\ 0 & i & 0 & 0\end{pmatrix}
$$

$$
A_{yz}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0\end{pmatrix},\qquad iS_{yz}=\begin{pmatrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i \\ 0 & 0 & i & 0\end{pmatrix}
$$

**And the three diagonals, which the same rule produces.** The diagonal takes the two words of the pair $\{t,j\}$ and their half difference, in the three words $W_{tt}$, $W_{jj}$, and **all three carry the factor $i$ of the nine**:
$$
M_j=\tfrac12\bigl(W_{tt}-W_{jj}\bigr),\qquad G_j=iM_j,\qquad j=x,y,z .
$$
$$
iM_x=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix},\qquad iM_y=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & 0\end{pmatrix},\qquad iM_z=\begin{pmatrix}-i & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & i\end{pmatrix}
$$

**The three are the frame, and the trace direction is their sum and not a fourth member.**
$$
iM_x+iM_y+iM_z=iD=\begin{pmatrix}-3i & 0 & 0 & 0 \\ 0 & i & 0 & 0 \\ 0 & 0 & i & 0 \\ 0 & 0 & 0 & i\end{pmatrix}
$$
**The permutation of $x,y,z$ permutes the three of them**, because $W_{tt}$ is common to all three and each carries only its own $W_{jj}$; the sum, being fixed, is the direction the breaking singles out. [The Symmetric Diagonal Frame](the-symmetric-diagonal-frame-of-the-fifteen.html) takes this apart, including why $\mathfrak{su}(3)$ cannot do the same.

**The factor $i$ on the diagonals is the factor the nine planes carry, and a construction that drops it produces a real Hermitian array that is not in $\mathfrak{su}(4)$.** Written without the $i$, $M_j=E_{jj}-E_{tt}$ is a real diagonal with entries $\pm1$ and $0$, and $D=\sum_jM_j$ is the real diagonal $\operatorname{diag}(-3,1,1,1)$; **the generators are $iM_j$, the generator of the trace direction is $iD$, and $D$ is the array that carries $B-L$**, with $B-L=\tfrac13D$ on $\mathbf4$.

**The broken-phase names are combinations of the frame, and the two relations are the whole change of label.**
$$
d_2=\tfrac i2\bigl(M_x-M_y\bigr),\qquad d_3=\tfrac i2\bigl(M_y-M_z\bigr),
$$
so the two spatial diagonals $T^{c}_{3}$, $T^{c}_{8}$ are the two differences and $B'$ is the sum, exactly as before; what changes is that the frame does not put $iD$ in the list.

**One array worked from end to end, because the mechanism is worth seeing once.**
$$
\tfrac12\bigl(W_{tx}+W_{xt}\bigr)=\tfrac12\left[\begin{pmatrix}0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0\end{pmatrix}+\begin{pmatrix}0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0\end{pmatrix}\right]=\begin{pmatrix}0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{pmatrix}=-A_{tx}
$$
**The two words of the pair agree on the plane $\{t,x\}$ and disagree on $\{y,z\}$; the sum kills the disagreement; the survivor is one leptoquark plane.** The first display of the strong group does the same on the imaginary side: $iS_{tz}=i\tfrac12(W_{xy}-W_{yx})$ keeps $\{t,z\}$.

**The count.** Six pairs give twelve arrays, the three diagonal words give three, $12+3=15$. **The arithmetic of the construction is the arithmetic of the grid**: twelve off-diagonal planes and three diagonal arrays.

### The Fifteen, Counted

**The six halves are sums and differences of the fifteen, and the coefficients are integers after the halving.**
$$
A_{ta}=-\bigl(T^{L}_{a}+T^{R}_{a}\bigr),\qquad
A_{bc}=-\epsilon_{abc}\bigl(T^{L}_{a}-T^{R}_{a}\bigr),
$$
**and inverted,**
$$
T^{L}_{a}=-\tfrac12\bigl(A_{ta}+\epsilon_{abc}A_{bc}\bigr),\qquad
T^{R}_{a}=-\tfrac12\bigl(A_{ta}-\epsilon_{abc}A_{bc}\bigr).
$$
**The $\epsilon$ is a convention and not a sign of the algebra.** $A_{bc}$ is written with $b<c$ throughout, and $\epsilon_{abc}=+1$ when $(a,b,c)$ is a cyclic order of $(x,y,z)$. For $a=x$ and $a=z$ the cyclic pair is already ascending, so the second line reads with a minus; for $a=y$ the cyclic pair is $(z,x)$ and the ascending one is $(x,z)$, so the same array carries the opposite sign. **Write the pairs in cyclic order and $\epsilon=+1$ everywhere; write them with $b<c$ and $\epsilon$ is the price.**

**Check one, in four cells.** The two halves agree on the $\{t,a\}$ block, so their sum keeps it doubled and its half is the leptoquark plane; they differ on the $\{b,c\}$ block, so their difference keeps it doubled and its half is the spatial plane. **The half in the definition of $T$ is exactly what makes those two lines integral.**

**Fifteen generators, six halves.** The six relations are independent, so the six add no direction: the rank over $\mathbb{Q}(i)$ — equivalently over $\mathbb{R}$, the entries being Gaussian integers — is fifteen with them and fifteen without them, and each of the six is distinct from the fifteen. **Both statements are needed and neither is a defect**: one array per generator, and six arrays that are two-term sums of the other fifteen.

**The normalisation, said once.** The fifteen are Gaussian-integer arrays, every entry in $\{0,\pm1,\pm i\}$, with $\operatorname{tr}(X^{\dagger}X)=2$ on all fifteen. **The entry $-3$ survives only in the sum**, $D=M_x+M_y+M_z$, which is not a generator of the list, and its norm $|D|^{2}=12$ is the norm of that sum and not of any member. The six are real half-integer arrays, entries in $\{0,\pm\tfrac12\}$, with $1$. **No display mixes them**, and every relation above holds with the halves as written.

## Part III. The Properties of the Fifteen, and the Boson in Each

### One Table of Properties

**Six families, and every numeric entry in the table is recomputed in §*The Checks*.**

| family | arrays | entries | cells | $\operatorname{tr}(X^{\dagger}X)$ | spectrum | the exponential is |
| --- | --- | --- | --- | --- | --- | --- |
| real plane $\{j,k\}$ | $A_{jk}$, $6$ | $0,\pm1$ | $2$ | $2$ | $0,0,\pm i$ | a real rotation of the plane $\{j,k\}$ |
| imaginary plane $\{j,k\}$ | $iS_{jk}$, $6$ | $0,\pm i$ | $2$ | $2$ | $0,0,\pm i$ | complex, unitary, $\det=1$ |
| diagonal frame | $iM_x,iM_y,iM_z$, $3$ | $0,\pm i$ | $2$ | $2$ | $0,0,\pm i$ | two phases, two fixed lines |
| the sum of the frame | $iD=i\sum_jM_j$, not listed | $-3i$, $i$ | $4$ | — | $-3i,i,i,i$ | four phases |
| left triple | $T^{L}_{a}$, $3$ | $0,\pm\tfrac12$ | $4$ | $1$ | $\pm\tfrac i2$ twice | a real rotation by $\tfrac{\theta}{2}$ of two planes |
| right triple | $T^{R}_{a}$, $3$ | $0,\pm\tfrac12$ | $4$ | $1$ | $\pm\tfrac i2$ twice | the same, one plane reversed |

**The table has two behaviours, not six.** A real array has a real orthogonal exponential, so it turns planes and fixes the rest; an imaginary one has a complex exponential, so it does not preserve the real quartet. **That is the $6+9$ split read at the level of the group, and it is the reason the fifteen are not fifteen rotations of one kind.**

**One exponential, exactly.** For the real planes and the six arrays of $\mathfrak{so}(4)$ there is a closed form, and the two differ by the half:
$$
\exp\bigl(\theta A_{tx}\bigr)e_t=\cos\theta\,e_t-\sin\theta\,e_x,\qquad
\exp\bigl(\theta T^{L}_{x}\bigr)e_t=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,e_x .
$$
**At $\theta=0.4$ the first gives $(0.921061,\,-0.389418,\,0,\,0)$**, and $\exp(\theta A_{tx})$ fixes $e_y$ and $e_z$. **The half-angle in the second is the half in the definition of $T^{L}_{x}$ and nothing else.** $T^{L}_{x}$ turns both its planes by $\tfrac{\theta}{2}$ in the same sense; $T^{R}_{x}$ turns $\{t,x\}$ by $\tfrac{\theta}{2}$ and $\{y,z\}$ by $-\tfrac{\theta}{2}$.

**The Gram, and the three entries that are not orthogonal.** The fifteen are pairwise orthogonal in the trace form except the three of the frame,
$$
\operatorname{tr}\bigl(M_jM_k\bigr)=2\delta_{jk}+\bigl(1-\delta_{jk}\bigr),\qquad \operatorname{tr}\bigl(t_jt_k\bigr)=\tfrac12\delta_{jk}+\tfrac14\bigl(1-\delta_{jk}\bigr),
$$
**which is the array form of the statement that a basis on the spatial block is a choice and the algebra is not, and the price of choosing the symmetric one.** The orthogonal frame is the same three directions rotated by an integer matrix,
$$
A_j=W_{jj}=\sum_kM_k-2M_j,\qquad \operatorname{tr}\bigl(A_jA_k\bigr)=4\delta_{jk},\qquad \operatorname{tr}\bigl(-\tfrac{A_j}{\sqrt8}\,,\,-\tfrac{A_k}{\sqrt8}\bigr)=\tfrac12\delta_{jk},
$$
**so the trace form is diagonal on $A$ and sheared on $M$, and the passage from one to the other is $J-2\mathbb 1$, which is invertible.** The six halves are not orthogonal to the fifteen, and cannot be: they are sums of them. Their overlap is exactly the two planes they are made of,
$$
\operatorname{tr}\bigl(T^{L}_{a}A_{ta}\bigr)=1,\qquad \operatorname{tr}\bigl(T^{L}_{a}A_{bc}\bigr)=\epsilon_{abc},
$$
with $\operatorname{tr}(T^{L}_{a}T^{L}_{b})=-\delta_{ab}$ and $\operatorname{tr}(T^{L}_{a}T^{R}_{b})=0$. **The $\epsilon$ in the second is the same $\epsilon$ as above, and it is the orientation of the pair $(b,c)$ and not a sign of the algebra.**

### The Grid, and the Boson in Each Cell

**The grid is $4\times4$, rows from and columns to, cell $(i,j)$ moving index $j$ into index $i$.** Each cell carries a name; the pair of mirrored cells holds the two amplitudes of one plane, and therefore two particles.

| | $t$ lepton | $x$ red | $y$ green | $z$ blue |
| --- | --- | --- | --- | --- |
| **$t$ lepton** | $B'$ | $\bar X^{r}$ | $\bar X^{g}$ | $\bar X^{b}$ |
| **$x$ red** | $X^{r}$ | $T^{c}_{3}$ | $g_{1}$ | $g_{4}$ |
| **$y$ green** | $X^{g}$ | $g_{2}$ | $T^{c}_{8}$ | $g_{6}$ |
| **$z$ blue** | $X^{b}$ | $g_{5}$ | $g_{7}$ | trace, not a generator |

**The blocks, and the count of each.**

| block | cells | arrays | bosons |
| --- | --- | --- | --- |
| the $t$ row and column, off the corner | $6$ | $A_{ta}$, $iS_{ta}$ | the leptoquark sextet $X^{a}$, $\bar X^{a}$ |
| the $3\times3$ spatial block, off the diagonal | $6$ | $A_{bc}$, $iS_{bc}$ | six spatial–spatial arrays: the off-diagonal gluons below $M_C$ |
| the diagonal frame | $4$ cells, $3$ generators | $iM_j$ | the frame; below $M_C$ the two differences $T^{c}_{3}$, $T^{c}_{8}$ and the sum $B'$ |
| the corner cell | $1$ | none: the trace | not a generator, and $iD$ is the sum of the frame |
| not on the grid | — | $T^{L}_{a}$ | no particle: half heavy, half massless |
| not on the grid | — | $T^{R}_{a}$ | no particle: half heavy, half massless |

**The two counts of the frame's decomposition.**
$$
\underbrace{6}_{\text{leptoquarks}}+\underbrace{8}_{\text{gluons}}+\underbrace{1}_{B-L}=15,
\qquad
\underbrace{6}_{\text{mixed cells}}+\underbrace{9}_{3\times3}+\underbrace{1}_{(t,t)}=16 .
$$

**One array per generator, one boson per array.** The identification, with the cells each array moves and the mass each boson gets at tree level. **The names *gluon* and *leptoquark* in the last column are the broken phase's**, and [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html)'s §*The Names, and Which Phase They Belong To* says exactly what each is on deposit for: above $M_C$ no $\mathrm{SU}(3)$ is made local, and the eight are named by the lines they connect.

| array | the cells it moves | the boson | mass |
| --- | --- | --- | --- |
| $A_{tx}$, $iS_{tx}$ | $(t,x)$ and $(x,t)$ | $X^{r}$ and $\bar X^{r}$, one per amplitude | $32v^{2}$ |
| $A_{ty}$, $iS_{ty}$ | $(t,y)$ and $(y,t)$ | $X^{g}$ and $\bar X^{g}$ | $32v^{2}$ |
| $A_{tz}$, $iS_{tz}$ | $(t,z)$ and $(z,t)$ | $X^{b}$ and $\bar X^{b}$ | $32v^{2}$ |
| $A_{xy}$, $iS_{xy}$ | $(x,y)$ and $(y,x)$ | the gluon pair $g_{1}$, $g_{2}$ | $0$ |
| $A_{xz}$, $iS_{xz}$ | $(x,z)$ and $(z,x)$ | the gluon pair $g_{4}$, $g_{5}$ | $0$ |
| $A_{yz}$, $iS_{yz}$ | $(y,z)$ and $(z,y)$ | the gluon pair $g_{6}$, $g_{7}$ | $0$ |
| $iM_j$, $j=x,y,z$ | the diagonal, four cells | the frame: above $M_C$ three symmetric directions | $0$ |
| $d_2=\tfrac i2(M_x-M_y)$, $d_3=\tfrac i2(M_y-M_z)$ | combinations of the frame | $T^{c}_{3}$, $T^{c}_{8}$ | $0$ |
| $iD=i\sum_jM_j$ | the sum of the frame | $B'$ | $0$ at the first breaking; an ingredient of $\gamma$, $Z$, $Z_R$ |
| $T^{L}_{a}$, $T^{R}_{a}$ | four cells each: one mixed plane and one spatial plane | **no boson** | $32v^{2}$ on one half, $0$ on the other |

**Two conventions live in that table, and both are named.** **Which of a plane's two amplitudes carries which of the pair's two names is a choice** — the two names of a mirrored pair could be exchanged without changing a number. **And the real and imaginary amplitudes of one plane are the two components of one complex field**, so calling $A_{tx}$ the particle and $iS_{tx}$ the antiparticle is the $i$ convention and not a physical distinction. **What is not a choice is the count**: fifteen arrays, two amplitudes per plane, one boson per amplitude — **and the six $\mathfrak{so}(4)$ arrays outside the count, which are coherences of a heavy and a massless direction and therefore not bosons at all.**

**Nine massless and six massive is this model's whole spectrum.** The nine are the gluon octet and $B'$; the six are the leptoquarks. **There is no $W$, no $Z$ and no photon here, and their absence is not a gap**: they need the weak factors, the three neutral directions and the second vacuum, and all three arrive at the transition. [Classification of the Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html) has the ledger; [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html) has where the rest come from.

### The Mass, and the One Difference That Decides It

**The scalar that breaks $\mathrm{SU}(4)$ takes its value along the lepton line**, $Ξ_0=vD$ with $D=\operatorname{diag}(-3,1,1,1)$, and the adjoint mass matrix of the fifteen is
$$
M^{2}_{XY}=\operatorname{tr}\bigl([X,Ξ_0]^{\dagger}[Y,Ξ_0]\bigr).
$$
**In the physics basis it is diagonal, with one number per plane.**
$$
M^{2}=2v^{2}\bigl(\lambda_j-\lambda_k\bigr)^{2}\ \text{ on a plane }\{j,k\},\qquad \lambda=\operatorname{eig}(D),
$$
**which is one display.**
$$
M^{2}=\operatorname{diag}\bigl(\underbrace{32v^{2},\dots,32v^{2}}_{6},\underbrace{0,\dots,0}_{9}\bigr).
$$

**Read $32$ off the eigenvalues.** $32=2\times4^{2}$, and $4=1-(-3)$ is a diagonal entry minus the lepton eigenvalue. **The strong group is unbroken because $D$ is a multiple of the identity on the three spatial lines**, and every diagonal direction is untouched because $[iM_j,D]=0$ for all three, so the corner is too; the nine zeros are those two facts and nothing else.

**The matrix has its own article.** [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html) derives the matrix from the double commutator, states the commutator lemma that produces it, names the nine-dimensional kernel as $\mathfrak{su}(3)\oplus\mathfrak{u}(1)_{B-L}$, and gives the spectrum at a general vacuum.

### Three Things the Arrays Do Not Do

**They do not boost.** No exponential of the fifteen is a Lorentz boost. The generator of the boost in a plane is the Hermitian $-i$ times the cell, and it is not in the algebra; [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators.html) proves it three ways.

**They do not identify the carrier with spacetime.** The quartet is a formal copy of the carrier, and a rotor of its three-space is a rotor of that three-space. The theorem and its consequence are in [The $\mathrm{SU}(4)$ Model](the-su4-model-four-lines-fifteen-generators-one-declaration.html), §*The Carrier Is a Copy*.

**They do not fix a coupling.** The model's one coupling is symbolic, so the numbers in the mass column are coefficients of $v^{2}$ and not predictions in kilograms. [The One Coupling That Returns the Standard Model](the-one-coupling-that-returns-the-standard-model.html) records what the model does and does not supply.

## The Checks

Twenty-nine recomputations, at $\operatorname{tr}$ in the fundamental, quartet ordered $(t,x,y,z)$ and the product fixed by $\vec e_x\vec e_y=\vec e_z$.

| check | result |
| --- | --- |
| arrays displayed | the fifteen and the six halves of $\mathfrak{so}(4)$, all four-row |
| anti-Hermitian, traceless | $15/15$ and $6/6$ |
| distinct arrays | $15$ and $6$ |
| rank over $\mathbb{Q}(i)$ of the fifteen / of the fifteen with the six | $15$ / $15$ |
| $\ell_a^{2}=r_a^{2}=-\mathrm I_4$ | $6/6$ |
| $\ell_x\ell_y=\ell_z$ / $r_xr_y=-r_z$ | $3/3$ / $3/3$ |
| $[\ell_a,\ell_b]=2\epsilon_{abc}\ell_c$ | $3/3$ exact |
| $[T^{L}_{a},T^{L}_{b}]=\epsilon_{abc}T^{L}_{c}$ | $3/3$ exact |
| $[T^{R}_{a},T^{R}_{b}]=-\epsilon_{abc}T^{R}_{c}$ | $3/3$ exact |
| $[T^{L}_{a},T^{R}_{b}]=0$ | $9/9$ exact |
| $\operatorname{tr}(T^{L})^{2}=\operatorname{tr}(T^{R})^{2}=-1$ | $6/6$ |
| spectrum of each half | $\pm\tfrac i2$, twice |
| $T^{L}_{a}-T^{R}_{a}$ supported on $2$ cells | $3/3$ |
| star eigenvalue $+1$ (left) / $-1$ (right) | $3/3$ / $3/3$ |
| $\operatorname{tr}(W^{\mathsf T}W')=4\delta$ | $256/256$ |
| one scalar index $\Rightarrow$ antisymmetric / two $\Rightarrow$ symmetric | $6/6$ / $9/9$ |
| only $W_{tt}$ has a trace | $16/16$ |
| half-sum and half-difference one plane each | $6/6$ |
| the signs of the pair table | $6/6$ exact |
| $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$, $A_{bc}=-\epsilon_{abc}(T^{L}_{a}-T^{R}_{a})$ | $6/6$ exact |
| inversion of $T^{L}$, $T^{R}$ from $A_{ta}$, $A_{bc}$, with $\epsilon_{abc}$ | $6/6$ exact |
| $iN_{xx}+iN_{yy}+iN_{zz}=iD$ | exact |
| $\operatorname{tr}(X^{\dagger}X)$ of the fifteen | $2$ on all fifteen |
| $iM_x+iM_y+iM_z-iD$ | $0$, exact |
| Gram of the fifteen off-diagonal | one entry, $+1$ |
| eight eight generators fix $e_t$ / six mixed move it | $8/8$ / $6/6$ |
| eight eight generators closed under the bracket | $64/64$ |
| $M^{2}$ of the fifteen | $32v^{2}$ on the six mixed planes, $0$ on the nine, off-diagonals $0$ |
| $\exp(\theta A_{tx})$: rotation, $e_t\mapsto(\cos\theta,-\sin\theta,0,0)$ | exact; $0.4$ gives $(0.921061,-0.389418,0,0)$ |
| $\det\exp(0.7X)=1$ and unitary | $15/15$ and $6/6$ |

## Summary

**The fifteen generators are printed as fifteen four-row axis-free arrays, and the six halves follow them in the order they are made.** The six arrays of $\mathfrak{so}(4)$ are half the raw arrays $\ell_a$, $r_a$; the fifteen are the sixteen words minus the trace word, with $i$ on the nine symmetric ones, and then the six pairs replaced by half-sum and half-difference.

**The left and right triples differ by one sign on two entries per array**, they commute because the algebra is associative, and their brackets carry opposite signs because right multiplication is an anti-homomorphism. **As two-forms they are the self-dual and anti-self-dual halves of $\mathfrak{so}(4)$**, and the six real planes of $\mathfrak{su}(4)$ are their sums and differences: $A_{ta}=-(T^{L}_{a}+T^{R}_{a})$ and $A_{bc}=-\epsilon_{abc}(T^{L}_{a}-T^{R}_{a})$. Twenty-one arrays, fifteen generators.

**Every property in Part III is one number.** Two cells or four; $2$, $12$ or $1$ under $\operatorname{tr}(X^{\dagger}X)$; spectrum $0,0,\pm i$ or $\pm\tfrac i2$ twice; a real rotation or a complex one. **And every array of the fifteen is one boson**: six leptoquarks, eight gluons and $B'$. **The six $\mathfrak{so}(4)$ arrays are not bosons**: each is half heavy and half massless, and the four-factor phase is what names them. **The mass is $2v^{2}$ times the square of the difference of two eigenvalues of $D$**, which is $32v^{2}$ across the lepton line and zero across anything spatial, and that single difference is the whole of the nine-and-six split.

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the base of the carrier, $\vec e_x\vec e_y=\vec e_z$ cyclically |
| $L_{\mathrm{axf}},R_{\mathrm{axf}}$ | arrays of left and right multiplication, columns equal to products |
| $\ell_a,r_a$ | the six raw arrays $L_{\mathrm{axf}}(\vec e_a)$, $R_{\mathrm{axf}}(\vec e_a)$ |
| $E_{jk}$ | the matrix unit in the order $(t,x,y,z)$ |
| $A_{jk}=E_{jk}-E_{kj}$ | the real generator of the plane $\{j,k\}$, written $j<k$ |
| $iS_{jk}=i(E_{jk}+E_{kj})$ | the imaginary generator of the same plane |
| $W_{\mu\nu}=\ell_\mu r_\nu$ | a word, a signed permutation, $\operatorname{tr}(W^{\mathsf T}W')=4\delta$ |
| $N_{jk}=\ell_jr_k$ | the nine vector-vector words |
| $D=\operatorname{diag}(-3,1,1,1)$ | $M_x+M_y+M_z$, the direction that carries $B-L=\tfrac13D$ |
| $iM_j$, $j=x,y,z$ | the three diagonal generators, the symmetric frame |
| $iD$ | $i\sum_jM_j$, the trace direction, not one of the fifteen |
| $T^{L}_{a}=\tfrac12\ell_a$ | one of the three left halves, a plane of $\mathfrak{so}(4)$ |
| $T^{R}_{a}=\tfrac12r_a$ | one of the three right halves, a plane of $\mathfrak{so}(4)$ |
| $P^{\pm}_{\mu\nu}$ | half-sum and half-difference of a pair of words |

## Further Reading

- [Building the Two Bases of $\mathfrak{su}(4)$ from the Axis-Free Left and Right Matrices](../articles_internal/structures/structure-SU4-basis-construction.html). The three steps of Part II in full, with the word table and the theorem on why the physics base is the one a diagonal mass matrix forces.
- [Two Bases of $\mathfrak{su}(4)$](../articles_internal/structures/structure-SU4-basis-comparison.html). The change of basis between the maths fifteen and the physics fifteen, in both directions, with the composition checked to the identity.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The mass matrix of Part III: the operator, the commutator lemma, the nine-dimensional kernel and the general vacuum, both bases, and the $8v^{2}$ artefact of the coherent arrays — which is $16v^{2}$ once the array's norm is divided out.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html). The frame, the signed permutations and the ten properties.
- [The Axis-Free Arrays of the Fifteen and the Six Halves](../articles_internal/the-axis-free-arrays-fifteen-generators-six-halves-and-a-cartan.html). The arrays of $L_{\vec e_a}$ and $R_{\vec e_a}$, their word support and the six relations.
- [$M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html) and [$M_2(\mathbb{C})$ Defining Representation](../articles_maths/m2c-defining-representation.html). The four-row and two-row frames.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](../articles_maths/the-anti-hermitian-derivations-of-m4c-as-su4.html). The fifteen in the operator basis, numbered $G_1$ to $G_{15}$.
- [The Rotors of the Fifteen Generators](the-rotors-of-the-fifteen-generators.html). What each array does when exponentiated, and why no boost is in the group.
- [The Commutation Table of the Fifteen Generators](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). Every bracket of every array with every other, printed block by block, with the six rules that produce the table.
- [Classification of the Bosons: One Grid, Fifteen Generators](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html). The grid and the ledger of the spectrum.
- [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). Where the four absent particles come from.
- [The $\mathrm{SU}(4)$ Model: Four Lines, Fifteen Generators, One Declaration of Rank Three](the-su4-model-four-lines-fifteen-generators-one-declaration.html). The declaration, the carrier, and the real $\mathfrak{so}(4)$ inside the fifteen.
- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer, 1991 — one-sided actions, the anti-homomorphism of the right action, and why the two commute.
