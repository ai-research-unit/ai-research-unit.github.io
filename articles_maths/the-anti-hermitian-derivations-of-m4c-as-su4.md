# __The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$__

## Introduction

**Two conditions pick out the generators: anti-Hermitian and traceless. They hold exactly for fifteen matrices, which form $\mathfrak{su}(4)$ of real dimension fifteen, and the fifteen split as six real antisymmetric and nine purely imaginary, $6+9$. Each generator $K$ gives the derivation $[K,\cdot]$, whose array is the Kronecker difference $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$, and whose exponential is the conjugation by the rotor $U=e^{K}\in\mathrm{SU}(4)$.**

The article writes the fifteen generators out in full, and it builds them the way the corpus builds every array: from the axis-free matrices $L_{\mathrm{axf}}$ and $R_{\mathrm{axf}}$ of *Matrix Representations and Conventions*, not from a frame chosen for the occasion. The six real generators are the left and right matrices of the three vector units; the nine imaginary ones are $i$ times their nine products. Each of the fifteen is an involution up to the factor $i$, so each has the eigenvalues $i,i,-i,-i$ and each rotor is a closed form in $\cos\theta$ and $\sin\theta$. The article then prints a second basis of the same fifteen, the plane basis, in which every off-diagonal array is a single plane, and sets the properties of the two bases side by side.

The article also states the bracket table of the six and the nine, the split of the fifteen as $6+9$, the position of the three inner derivations of the biquaternion algebra inside the six, the spectrum of the derivation as the differences of the eigenvalues of its generator, and the orbit dimensions of the conjugation.

The article assumes the Lie group results of *The Exponential and the Lie Group of $M_4(\mathbb{C})$*, the determinant formula $\det e^{F}=e^{\operatorname{tr}F}$, and the reading of the adjoint representation of $\mathrm{SU}(4)$.

## The Two Conditions on the Generator

### The Fifteen Parameters

**Proposition (the generators).** The matrices $K\in M_4(\mathbb{C})$ with $K^{*}=-K$ and $\operatorname{tr}K=0$ form a real vector space of dimension fifteen, closed under the bracket, isomorphic to $\mathfrak{su}(4)$.

**Proof.** An anti-Hermitian matrix of order four has sixteen real parameters: four imaginary diagonal entries and six complex off-diagonal pairs. The trace is imaginary, so the traceless condition is one real equation and fifteen remain. The bracket of two anti-Hermitian matrices is anti-Hermitian, and the trace of a bracket vanishes.

### The Split as Six and Nine

**Proposition (the real form inside).** Every anti-Hermitian traceless $K$ splits uniquely as

$$
K=\underbrace{\tfrac12(K-\bar K)}_{\text{real antisymmetric}}+\;i\underbrace{\tfrac{1}{2i}(K+\bar K)}_{\text{real symmetric, traceless}} ,
$$

and the two summands have dimensions six and nine, so $15=6+9$ with intersection zero.

**Proof.** $\tfrac12(K-\bar K)$ is real and satisfies $S^{\mathsf T}=-S$; it has $\tfrac12\cdot4\cdot3=6$ parameters. $\tfrac{1}{2i}(K+\bar K)$ is real symmetric; a real symmetric matrix of order four has ten parameters, and the traceless condition removes one, leaving nine. The two summands are of different symmetry types, so they meet only in zero.

**Corollary (one summand is closed, the other is not).** The real antisymmetric matrices form the subalgebra $\mathfrak{so}(4)$ of $\mathfrak{su}(4)$. The set $i\cdot\operatorname{Sym}_0(4,\mathbb{R})$ is not a subalgebra.

**Proof.** The bracket of two real antisymmetric matrices is real antisymmetric, so the six close. The bracket of two elements of $i\operatorname{Sym}_0$ is $-[\cdot,\cdot]$ of two real symmetric matrices, which is real antisymmetric, so it lands in the other summand and the nine do not close.

**Remark (the split is not conjugation invariant).** The split is taken with respect to the standard real structure of $\mathbb{C}^4$, and a conjugation by a unitary matrix with complex entries moves the six. The split therefore records the position of the generator relative to the standard basis. The eigenvalue spectrum is invariant under conjugation; the split into real and imaginary parts is not, and it is the split that decides which planes turn in which sense, so it is what decides the shape of the rotor. Two generators with the same eigenvalues are conjugate to each other and so have the same derivation spectrum, and they are still different rotors: $\ell_x$ turns both coordinate planes by $\theta$, $r_x$ turns one plane by $\theta$ and the other by $-\theta$, and $iN_{xx}$ multiplies two coordinates by $e^{i\theta}$ and two by $e^{-i\theta}$. All three have the eigenvalues $i,i,-i,-i$ and the derivation spectrum $0^{8},(\pm2i)^{4}$.

## The Fifteen Generators, Written Out

**The notation.** The generators are not chosen from a list. They are the arrays the corpus already prints, the axis-free left and right matrices of the three vector units in *Matrix Representations and Conventions*, together with their nine products:

$$
\ell_k:=L_{\mathrm{axf},\vec e_k},\qquad r_k:=R_{\mathrm{axf},\vec e_k},\qquad N_{jk}:=\ell_jr_k,\qquad j,k\in\{x,y,z\}.
$$

The fifteen are $\ell_x,\ell_y,\ell_z$, $r_x,r_y,r_z$ and the nine $iN_{jk}$.

**The fifteen are fifteen words.** A product of one left matrix with one right one is a **word** $W_{\mu\nu}=L_{\mathrm{axf}}(e_\mu)R_{\mathrm{axf}}(e_\nu)$, and the sixteen words are a basis of $M_4(\mathbb{R})$ with $\operatorname{tr}(W_{\mu\nu}^{\mathsf T}W_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$. Only $W_{tt}=\mathrm I_4$ has a nonzero trace, so the traceless part is the grid of pairs without the corner, and the fifteen of this article are those fifteen words made anti-Hermitian: the six antisymmetric words $\ell_k,r_k$ are already anti-Hermitian, and the nine symmetric words $N_{jk}$ become anti-Hermitian on multiplication by $i$. The split $15=6+9$ of §*The Split as Six and Nine* is therefore the split of the words by the number of $t$ indices they carry. The table of names is §*The Sixteen Words, and Their Names* of [$M_4(\mathbb{C})$ Axis-Free Representation: Operators](m4c-axis-free-representation-operators.html).

**The fifteen, one to a display.** They are numbered $G_{1}$ to $G_{15}$ once, so that every later section can point at one of them. The first six are real antisymmetric, the last nine imaginary symmetric.

$$
G_{1}=\ell_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}
$$

$$
G_{2}=\ell_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
G_{3}=\ell_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}
$$

$$
G_{4}=r_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

$$
G_{5}=r_y=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix}
$$

$$
G_{6}=r_z=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}
$$

$$
G_{7}=iN_{xx}=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}
$$

$$
G_{8}=iN_{xy}=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&-i&0&0\\i&0&0&0\end{pmatrix}
$$

$$
G_{9}=iN_{xz}=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix}
$$

$$
G_{10}=iN_{yx}=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&-i&0&0\\-i&0&0&0\end{pmatrix}
$$

$$
G_{11}=iN_{yy}=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}
$$

$$
G_{12}=iN_{yz}=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix}
$$

$$
G_{13}=iN_{zx}=\begin{pmatrix}0&0&i&0\\0&0&0&-i\\i&0&0&0\\0&-i&0&0\end{pmatrix}
$$

$$
G_{14}=iN_{zy}=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix}
$$

$$
G_{15}=iN_{zz}=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&i&0\\0&0&0&-i\end{pmatrix}
$$

**The count.** Fifteen, and the table says which is which.

| # | generator | built from | kind |
|---|---|---|---|
| $1$ | $G_{1}=\ell_x$ | left multiplication by $\vec e_x$ | real antisymmetric |
| $2$ | $G_{2}=\ell_y$ | left multiplication by $\vec e_y$ | real antisymmetric |
| $3$ | $G_{3}=\ell_z$ | left multiplication by $\vec e_z$ | real antisymmetric |
| $4$ | $G_{4}=r_x$ | right multiplication by $\vec e_x$ | real antisymmetric |
| $5$ | $G_{5}=r_y$ | right multiplication by $\vec e_y$ | real antisymmetric |
| $6$ | $G_{6}=r_z$ | right multiplication by $\vec e_z$ | real antisymmetric |
| $7$ | $G_{7}=iN_{xx}$ | $\ell_xr_x$, times $i$ | imaginary symmetric |
| $8$ | $G_{8}=iN_{xy}$ | $\ell_xr_y$, times $i$ | imaginary symmetric |
| $9$ | $G_{9}=iN_{xz}$ | $\ell_xr_z$, times $i$ | imaginary symmetric |
| $10$ | $G_{10}=iN_{yx}$ | $\ell_yr_x$, times $i$ | imaginary symmetric |
| $11$ | $G_{11}=iN_{yy}$ | $\ell_yr_y$, times $i$ | imaginary symmetric |
| $12$ | $G_{12}=iN_{yz}$ | $\ell_yr_z$, times $i$ | imaginary symmetric |
| $13$ | $G_{13}=iN_{zx}$ | $\ell_zr_x$, times $i$ | imaginary symmetric |
| $14$ | $G_{14}=iN_{zy}$ | $\ell_zr_y$, times $i$ | imaginary symmetric |
| $15$ | $G_{15}=iN_{zz}$ | $\ell_zr_z$, times $i$ | imaginary symmetric |

**One product, worked.** The labels can be checked without redoing the whole multiplication, because each row of $\ell_x$ carries a single entry: each row of the product is $\pm$ one row of $r_y$,

$$
\ell_x:\ \text{rows } -e_x^{\mathsf T},\; e_t^{\mathsf T},\; -e_z^{\mathsf T},\; e_y^{\mathsf T}
\quad\Longrightarrow\quad
\ell_xr_y:\ \text{rows } -(r_y)_{x\cdot},\; (r_y)_{t\cdot},\; -(r_y)_{z\cdot},\; (r_y)_{y\cdot},
$$

$$
-(0,0,0,-1),\quad (0,0,-1,0),\quad -(0,1,0,0),\quad (1,0,0,0),
$$

which is the matrix printed at $G_8$ with the factor $i$ removed. The remaining eight products are read the same way, one row at a time.

**A second basis, printed below.** The fifteen-dimensional space has a second basis built from the same words, and §*Step 3: The Plane Basis* prints it: the half-sum and the half-difference of each of the six pairs, which is the only resolution of a pair that puts each array on a single plane. The two bases agree on the three diagonal words, differ on the twelve off-diagonal ones, and are carried into each other by $\ell_a=-A_{ta}-A_{bc}$ and $r_a=-A_{ta}+A_{bc}$. §*The Two Bases Compared* sets the properties of the two side by side.

**Proposition (they are the fifteen of $\mathfrak{su}(4)$).** The fifteen are anti-Hermitian, traceless and linearly independent over $\mathbb{R}$, so they are a basis of $\mathfrak{su}(4)$.

**Proof.** The printed matrices $L_{\mathrm{axf},\vec e_k}$ and $R_{\mathrm{axf},\vec e_k}$ are antisymmetric signed permutations with entries in $\{0,1,-1\}$, so each is anti-Hermitian and of trace zero. Each $N_{jk}$ is a product of two such and is a symmetric signed permutation, of trace zero, so $iN_{jk}$ is anti-Hermitian and traceless. For independence: the sixteen products $L_{\mathrm{axf},\mu}R_{\mathrm{axf},\nu}$ are a basis of $M_4(\mathbb{C})$, the fifteen above are fifteen of them, and the factor $i$ on the nine is invertible.

**Proposition (each squares to $-\mathrm{I}_4$).** Every one of the fifteen satisfies $K^{2}=-\mathrm{I}_4$, so each has the eigenvalues $i,i,-i,-i$ and each has trace zero.

**Proof.** $\ell_k^{2}=-\mathrm{I}_4$ because $\ell_k$ is a quarter-turn of the two coordinate planes it moves, and the square of a real quarter-turn is minus the identity; the same holds for $r_k$. For these factors $N_{jk}^{2}=\ell_j^{2}r_k^{2}=\mathrm{I}_4$, since $\ell_j$ and $r_k$ commute and each squares to $-\mathrm{I}_4$, so $(iN_{jk})^{2}=-\mathrm{I}_4$. This is a fact about the six printed matrices, not about symmetric signed permutations in general, which need not square to the identity. Four eigenvalues of modulus one and of square $-1$ are $\pm i$, and the trace is zero, so they are $i,i,-i,-i$.

**Remark (the eight axis-free matrices).** The axis-free frame names eight matrices, $\ell_t,\ell_x,\ell_y,\ell_z$ and $r_t,r_x,r_y,r_z$, and the two scalar ones are both the identity, $\ell_t=r_t=\mathrm{I}_4$. So the eight are seven distinct arrays, and the two identities are exactly the two the traceless condition excludes. The six that remain are $G_1$ to $G_6$.

**Remark (the Cartan is inside the nine).** The three diagonal generators are $G_7=iN_{xx}$, $G_{12}=iN_{yy}$ and $G_{15}=iN_{zz}$; they are imaginary diagonal and traceless, and they span the diagonal traceless subspace. The other six of the nine are off-diagonal, and $G_1$ to $G_6$ have no diagonal entry at all. So this basis puts the Cartan among the nine and puts none among the six.

**Remark (why the products are sixteen and not fewer).** The sixteen products are the arrays of the sixteen operators $T_{a,b}:X\mapsto aXb$ in the axis-free frame, and those operators are a basis of $\operatorname{End}(\mathbb{B})$. Their arrays have rank sixteen. This is the same count as the operator frame of *The Anti-Hermitian Derivations of the Operators of the Biquaternion Algebra as $\mathfrak{su}(4)$*, where the carrier is written as the sixteen products.

**Remark (the ordering of the corpus, not of a textbook).** A textbook basis would single out a Cartan first and then add the roots. This basis does the opposite: the six real generators come from the multiplication itself, and the Cartan appears among the nine as three products. That is what building the generators from the axis-free matrices does, and it is the reason the fifteen here are all of one shape rather than split into weights. The plane basis of §*Step 3* takes the textbook order: the three diagonals first, then the twelve planes. The article prints both orders, and §*The Two Bases Compared* says what each order is for.

## Step 3: The Plane Basis

**Steps 1 and 2 were forced and step 3 is not.** The eight arrays, the sixteen words, the deletion of $W_{tt}$ and the factor $i$ on the nine leave no freedom: they produce the fifteen $G_1,\dots,G_{15}$ of §*The Fifteen Generators, Written Out*, every one of them a single word, and twelve of them touching two planes. A second basis of the same fifteen is reached by one optional step, applied to the six pairs of words: replace each pair by its half-sum and its half-difference. Nothing is added and nothing is dropped, so the list is again fifteen, and the support falls from two planes to one.

**The step is a resolution of a pair and not a new construction.** The two words of a pair are the same signed permutation with the signs of one plane reversed, so the pair has two plane parts $X$ and $Y$ and the two words are $X+Y$ and $X-Y$. The half-sum and the half-difference are the two parts themselves. This section states that lemma, applies it six times, prints the fifteen arrays, and compares the two bases.

### The Pair Lemma

**The two words of a pair differ in one plane.** The two words of a pair are one signed permutation, so both are supported on the same two planes; call the two plane parts $X$ and $Y$. The signs of one of the two planes are reversed between them, so

$$
W_{\mu\nu}=X+Y,\qquad W_{\nu\mu}=X-Y .
$$

**The pair $\{t,x\}$, in full.** With $X=-A_{tx}$ and $Y=+A_{yz}$,

$$
W_{tx}=r_x=-A_{tx}+A_{yz}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\qquad
W_{xt}=\ell_x=-A_{tx}-A_{yz}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}.
$$

**The inverse of the pair is the Hadamard matrix.** Solving the two equations,

$$
X=\tfrac12\bigl(W_{\mu\nu}+W_{\nu\mu}\bigr),\qquad Y=\tfrac12\bigl(W_{\mu\nu}-W_{\nu\mu}\bigr),\qquad
a\,W_{\mu\nu}+b\,W_{\nu\mu}=(a+b)\,X+(a-b)\,Y .
$$

**Proposition (a combination is one-plane exactly when the coefficients are equal or opposite).** The array $aW_{\mu\nu}+bW_{\nu\mu}$ is supported on $X$ alone when $a=b$, on $Y$ alone when $a=-b$, and on both planes otherwise.

**Proof.** The two coefficients are $a+b$ and $a-b$, and one of them vanishes exactly when $a=\pm b$. The solutions are the two eigenlines of $\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, whose inverse carries the two words to the two planes. **The halves are therefore the inverse of the Hadamard matrix and not a normalisation chosen at will.**

**Worked, with a coefficient that is not a half.**

$$
\tfrac12\bigl(W_{tx}+W_{xt}\bigr)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}=-A_{tx},\qquad
2\,W_{tx}+W_{xt}=-3A_{tx}+A_{yz}=\begin{pmatrix}0&-3&0&0\\3&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}.
$$

Two cells against four: the second array moves both planes at once, and no plane can be named for it.

**The scale.** The demand $\lvert a\rvert=\lvert b\rvert$ fixes the direction of the resolution in each pair and leaves a sign and a scale. The sign is fixed below by the ordering of the indices, and the scale $\tfrac12$ is the one that makes the two outputs matrices with entries in $\{0,\pm1\}$, that is, a pair of matrix units read in real form.

**What the demand alone does not do.** One plane is also reached by a single matrix unit, $iE_{jk}$, which is in neither basis; the uniqueness of the step is a uniqueness inside the six pairs. The demand is applied one pair at a time, and that restriction is its hypothesis.

### The Six Pairs and Their Twelve Outputs

**The table.** The pair is written in ascending index order, the complement likewise, and the sign of a half-difference is the sign of the permutation $(\mu,\nu,\mu',\nu')$ against $(t,x,y,z)$.

| pair | the two words | half-sum | half-difference |
|---|---|---|---|
| $\{t,x\}$ | $W_{tx}=r_x$, $W_{xt}=\ell_x$ | $-A_{tx}$ | $+A_{yz}$ |
| $\{t,y\}$ | $W_{ty}=r_y$, $W_{yt}=\ell_y$ | $-A_{ty}$ | $-A_{xz}$ |
| $\{t,z\}$ | $W_{tz}=r_z$, $W_{zt}=\ell_z$ | $-A_{tz}$ | $+A_{xy}$ |
| $\{x,y\}$ | $W_{xy}=N_{xy}$, $W_{yx}=N_{yx}$ | $-S_{xy}$ | $+S_{tz}$ |
| $\{x,z\}$ | $W_{xz}=N_{xz}$, $W_{zx}=N_{zx}$ | $-S_{xz}$ | $-S_{ty}$ |
| $\{y,z\}$ | $W_{yz}=N_{yz}$, $W_{zy}=N_{zy}$ | $-S_{yz}$ | $+S_{tx}$ |

**The table read as one sentence.** The half-sum is minus the array on the pair's own two indices, and the half-difference is the array on the complementary pair, with the sign of the ordering. Each pair therefore yields one array on a plane through the $t$ line and one on a plane that avoids it.

**Six of the twelve need the factor $i$.** On the three pairs $\{t,a\}$ both outputs are real antisymmetric, so both are anti-Hermitian as they stand. On the three pairs $\{b,c\}$ both outputs are real symmetric, $-S_{bc}$ and $\pm S_{ta}$, and they take the factor $i$ of the nine. After that multiplication the twelve are $\pm A_{jk}$ and $\pm iS_{jk}$, and the sign in each pair is fixed by the printing.

**The identity behind the table, in one line.** For $(a,b,c)$ a cyclic order of $(x,y,z)$,

$$
A_{ta}=-\tfrac12\bigl(W_{ta}+W_{at}\bigr),\qquad
A_{bc}=+\tfrac12\bigl(W_{ta}-W_{at}\bigr).
$$

### The Twelve Plane Arrays and the Three Diagonals

**The convention.** The rows and the columns are read in the order $t,x,y,z$, so that $t,x,y,z$ are $1,2,3,4$; $E_{jk}$ is the matrix unit; and for $j<k$ in that order,

$$
A_{jk}:=E_{jk}-E_{kj},\qquad iS_{jk}:=i\bigl(E_{jk}+E_{kj}\bigr).
$$

**The two indices are not the one index of §*The Commutators and the Grading*.** $iS_{jk}$ with two indices is the imaginary symmetric array of the plane $\{j,k\}$; $S_k=\tfrac12(\ell_k+r_k)$ with one index is the real antisymmetric combination of the words basis. The arity is the whole difference, and this section writes the one-index symbol only where the words basis is meant.

**The six real arrays.** They are the two outputs of the three pairs $\{t,a\}$, both of which are real antisymmetric: the half-sums give $A_{tx},A_{ty},A_{tz}$, the half-differences give $A_{yz},A_{xz},A_{xy}$.

$$
A_{tx}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{ty}=\begin{pmatrix}0&0&1&0\\0&0&0&0\\-1&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{tz}=\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\-1&0&0&0\end{pmatrix}
$$

$$
A_{xy}=\begin{pmatrix}0&0&0&0\\0&0&1&0\\0&-1&0&0\\0&0&0&0\end{pmatrix}
$$

$$
A_{xz}=\begin{pmatrix}0&0&0&0\\0&0&0&1\\0&0&0&0\\0&-1&0&0\end{pmatrix}
$$

$$
A_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}
$$

**The six imaginary arrays.** They are the two outputs of the three pairs $\{b,c\}$, both of which are real symmetric, each multiplied by $i$: the half-sums give the arrays on the planes $\{x,y\},\{x,z\},\{y,z\}$ and the half-differences the arrays on $\{t,z\},\{t,y\},\{t,x\}$. The sign of each output is the sign of the table, and the displays print the twelve with the plus sign.

$$
iS_{tx}=\begin{pmatrix}0&i&0&0\\i&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{ty}=\begin{pmatrix}0&0&i&0\\0&0&0&0\\i&0&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{tz}=\begin{pmatrix}0&0&0&i\\0&0&0&0\\0&0&0&0\\i&0&0&0\end{pmatrix}
$$

$$
iS_{xy}=\begin{pmatrix}0&0&0&0\\0&0&i&0\\0&i&0&0\\0&0&0&0\end{pmatrix}
$$

$$
iS_{xz}=\begin{pmatrix}0&0&0&0\\0&0&0&i\\0&0&0&0\\0&i&0&0\end{pmatrix}
$$

$$
iS_{yz}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&i\\0&0&i&0\end{pmatrix}
$$

**The three diagonals.** They are not paired: the three words $W_{xx},W_{yy},W_{zz}$ are diagonal, and they are taken whole, in one sum and two successive differences.

$$
iD=i\bigl(W_{xx}+W_{yy}+W_{zz}\bigr)=\begin{pmatrix}-3i&0&0&0\\0&i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}
$$

$$
d_2=\tfrac i2\bigl(W_{yy}-W_{xx}\bigr)=\begin{pmatrix}0&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&0\end{pmatrix}
$$

$$
d_3=\tfrac i2\bigl(W_{zz}-W_{yy}\bigr)=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&i&0\\0&0&0&-i\end{pmatrix}
$$

**The three diagonals are the three diagonal words, recombined.** $iD=G_7+G_{11}+G_{15}$, and the map from $(iN_{xx},iN_{yy},iN_{zz})$ to $(iD,d_2,d_3)$ is invertible, so the two bases agree on the three-dimensional diagonal space and differ only on the twelve off-diagonal arrays.

**Proposition (the fifteen are a second basis).** The fifteen arrays are anti-Hermitian, traceless and of rank fifteen over $\mathbb{R}$, so they are a basis of $\mathfrak{su}(4)$.

**Proof.** Each is $i$ times a real matrix with two or four nonzero entries, so the conjugate transpose is minus itself, and each has zero trace. For independence: the twelve are supported on the twelve distinct off-diagonal planes, the three lie in the diagonal space, and the diagonal space meets the span of the twelve in zero.

**Proposition (one plane per array).** Each of the twelve off-diagonal arrays has exactly two nonzero entries, in the positions $(j,k)$ and $(k,j)$ of one plane $\{j,k\}$, and each of the three diagonals has its nonzero entries on the diagonal.

**Proof.** Read the displays. **This is the property the step was taken for**: one array, one plane, and no array that mixes two planes.

### The Change of Basis

**The six real generators of the words basis, in the plane basis.** For $(a,b,c)$ a cyclic order of $(x,y,z)$,

$$
\ell_a=-A_{ta}-A_{bc},\qquad r_a=-A_{ta}+A_{bc}.
$$

**Proof.** By the table, $W_{ta}=r_a=-A_{ta}+A_{bc}$ and $W_{at}=\ell_a=-A_{ta}-A_{bc}$, and the two displays hold for each of the three cyclic choices.

**The two triples are the two kinds of plane.** Adding and subtracting the two relations,

$$
\tfrac12\bigl(\ell_a+r_a\bigr)=-A_{ta},\qquad \tfrac12\bigl(\ell_a-r_a\bigr)=-A_{bc}.
$$

**So the plane basis displays the two triples.** The three planes through the $t$ line are the three diagonal combinations $\tfrac12(\ell_a+r_a)$, and the three planes that avoid it are the three inner derivations $D_a=\tfrac12(\ell_a-r_a)$. In the words basis those two triples are combinations; in the plane basis they are basis elements, and a sign is the only difference.

**The inverse, and the nine.** The relations invert to

$$
A_{ta}=-\tfrac12\bigl(\ell_a+r_a\bigr),\qquad A_{bc}=-D_a,
$$

and the nine words are read from the table, one pair at a time, for example

$$
N_{xy}=W_{xy}=-S_{xy}+S_{tz},\qquad N_{yx}=W_{yx}=-S_{xy}-S_{tz}.
$$

**One matrix unit from one plane.** The two arrays of a plane are the antisymmetric and the symmetric part of the two matrix units, so the plane pair carries the same information as the pair $E_{jk},E_{kj}$:

$$
S_{jk}+A_{jk}=2E_{jk},\qquad S_{jk}-A_{jk}=2E_{kj},\qquad S_{jk}=-i\,(iS_{jk}).
$$

### The Adjoint of $iD$

**Proposition (a quarter turn on six dimensions and zero on nine).** With $iD$ as above,

$$
[iD,A_{ta}]=-4\,iS_{ta},\qquad [iD,iS_{ta}]=4\,A_{ta},\qquad [iD,X]=0
$$

for $X$ among the other nine arrays. So the image of $\mathrm{ad}_{iD}$ is the six-dimensional span of $A_{ta},iS_{ta}$, the kernel is the nine-dimensional span of the rest, and on each of the three planes the array acts as four times a quarter turn.

**Proof.** The commutator with a diagonal matrix multiplies the entry $X_{pq}$ by $d_q-d_p$ with $d=(-3,1,1,1)$; on the plane $\{t,a\}$ the difference is $4$ in one direction and $-4$ in the other, and on the planes $\{b,c\}$ and on the diagonal it is zero.

**The quadratic form of the pair.** Define

$$
\beta(X,Y):=\operatorname{Re}\operatorname{tr}\bigl([X,iD]^{*}[Y,iD]\bigr).
$$

**Proposition ($\beta$ is diagonal in the plane basis and of rank one on a pair in the words basis).** $\beta$ is positive semidefinite, of kernel the nine-dimensional centraliser of $iD$ in $\mathfrak{su}(4)$, and it is $32$ on each of the six arrays $A_{ta},iS_{ta}$ and $0$ on the other nine. In the words basis the block of $\beta$ on the pair $(\ell_a,r_a)$ is

$$
32\begin{pmatrix}1&1\\1&1\end{pmatrix},
$$

of rank one, with eigenlines $\ell_a+r_a=-2A_{ta}$ and $\ell_a-r_a=-2A_{bc}$.

**Proof.** $\beta(X,X)=\lVert[X,iD]\rVert^{2}\ge0$, and $[A_{ta},iD]=-4iS_{ta}$ has square norm $16\cdot2=32$. In the words basis $\beta(\ell_a,\ell_a)=\beta(r_a,r_a)=\beta(\ell_a,r_a)=32$, because $\ell_a$ and $r_a$ have the same component along $A_{ta}$ and opposite components along $A_{bc}$, which $\beta$ annihilates.

**Remark (this is a second $6+9$, and it is not the symmetry split).** The fifteen split as six and nine twice: once as six real antisymmetric and nine imaginary symmetric, and once as the six-dimensional image and the nine-dimensional kernel of $\mathrm{ad}_{iD}$. The two sixes differ. Their intersection is the three-dimensional span of $A_{tx},A_{ty},A_{tz}$, because the image holds three antisymmetric and three symmetric arrays, and its antisymmetric half is exactly the three planes through $t$. A reader who writes $6+9$ must say which split is meant.

## The Two Bases Compared

**Two bases, one space, two demands.** The words basis is the unique basis in which every array is a single word. The plane basis is the unique resolution of the six pairs in which every off-diagonal array is supported on a single plane. Each is the solution of one demand, and neither demand implies the other.

| property | words basis, $G_1,\dots,G_{15}$ | plane basis |
|---|---|---|
| how it is reached | steps 1 and 2, forced | step 3, one optional choice |
| nonzero entries | four, on all fifteen | two on fourteen, four on $iD$ |
| planes touched | two on twelve, none on three | one on twelve, none on three |
| entries | $\{0,\pm1\}$ and $i\{0,\pm1\}$ | $\{0,\pm1\}$ and $i\{0,\pm1\}$, and $i\{-3,1,1,1\}$ on $iD$ |
| $\operatorname{tr}(G^{*}G)$ | $4$ on all fifteen | $2$ on fourteen, $12$ on $iD$ |
| the trace form | $\operatorname{tr}(G_a^{*}G_b)=4\delta_{ab}$ | not diagonal: $\operatorname{tr}(d_2^{*}d_3)=-1$ |
| spectrum | $i,i,-i,-i$ on all fifteen | $0,0,\pm i$ on fourteen, $-3i,i,i,i$ on $iD$ |
| $K^{2}$ | $-\mathrm{I}_4$ | $-(E_{jj}+E_{kk})$ on the twelve, $\operatorname{diag}(-9,-1,-1,-1)$ on $iD$ |
| the rotor | $\cos\theta\,\mathrm{I}_4+\sin\theta\,K$ | $\mathrm{I}_4+\sin\theta\,K+(1-\cos\theta)K^{2}$ |
| spectrum of $\mathrm{ad}_K$ | $0^{8},(\pm2i)^{4}$, the same for all fifteen | differs: $0^{6},(\pm i)^{4},\pm2i$ for a plane, $0^{10},(\pm4i)^{3}$ for $iD$ |
| structure constants | integers | integers, except the six brackets of a plane with its own partner, which carry thirds |
| $\ell_k$ and $r_k$ | basis elements | $-A_{ta}\mp A_{bc}$ |
| $D_k$ and $\tfrac12(\ell_k+r_k)$ | combinations of $\ell_k,r_k$ | $-A_{bc}$ and $-A_{ta}$, basis elements |
| the Cartan | three products $iN_{kk}$ | the three diagonals, first in the list |
| the six of $\mathfrak{so}(4)$ | two families of one shape | two triples, split by the plane's incidence with $t$ |
| the form $\beta$ | of rank one on each pair | diagonal |
| the demand it answers | every array one word | every off-diagonal array one plane |

**What the words basis buys.** Four things, and the article uses all four.

**Integrality.** Every array is a signed permutation before the factor $i$, so every one of the $225$ brackets is an integer combination of basis elements. The bracket table can be checked by hand or in exact arithmetic, and it carries no tolerance.

**Orthonormality.** $\operatorname{tr}(G_a^{*}G_b)=4\delta_{ab}$, so the Gram matrix is $4\mathrm{I}_{15}$ and the coordinate of a matrix is a trace divided by four. Each coefficient is one projection.

**One involution, one spectrum, one rotor.** Every member squares to $-\mathrm{I}_4$, so every member has the eigenvalues $i,i,-i,-i$, every derivation has the spectrum $0^{8},(\pm2i)^{4}$, and every rotor is $\cos\theta\,\mathrm{I}_4+\sin\theta\,K$. Three propositions of this article are propositions about this basis and about no other.

**The two $\mathfrak{su}(2)$'s of $\mathfrak{so}(4)$ as two families.** The six are $\ell_x,\ell_y,\ell_z$ and $r_x,r_y,r_z$, two copies of one shape, with $[\ell_a,\ell_b]=2\ell_c$ and $[r_a,r_b]=-2r_c$. The two copies appear as two lists, not as two blocks of a split.

**What the plane basis buys.** Four things, and none of them is available in the words basis.

**One array, one plane.** Each of the twelve off-diagonal generators is one plane, and the array names the plane it turns. A question about a plane, such as which generators move it and which fix it, becomes a question about one array.

**The Cartan displayed.** $iD,d_2,d_3$ are the three diagonals and are printed first, so the basis is a Cartan followed by the roots, in the order a textbook uses. The weights are read off the diagonal entries, and each pair $\{A_{jk},iS_{jk}\}$ spans over $\mathbb{C}$ the two matrix units $E_{jk},E_{kj}$.

**The two $\mathfrak{su}(2)$'s as two triples.** $\tfrac12(\ell_a+r_a)=-A_{ta}$ and $D_a=-A_{bc}$, so the two triples of $\mathfrak{so}(4)$ are the three planes through the $t$ line and the three planes that avoid it. The split is by incidence with one line, a statement the words basis cannot make without a combination.

**The adjoint of $iD$, and the form $\beta$.** The image of $\mathrm{ad}_{iD}$ is six-dimensional, its kernel nine-dimensional, and $\beta$ is diagonal with two values. In the words basis the same form has a rank-one block on each pair, which is the block that step 3 resolves.

**What the plane basis costs.** Four things, and they are the reason the article does not use it for the rotors.

**The spectrum is no longer uniform.** A plane array has the eigenvalues $0,0,i,-i$ and $iD$ has $-3i,i,i,i$, so no single closed form covers the fifteen and no single derivation spectrum either. Each family needs its own display.

**$K^{2}$ is no longer $-\mathrm{I}_4$.** A plane array squares to minus the sum of two matrix units, so the exponential is a polynomial of degree two and the compact form $\cos\theta\,\mathrm{I}_4+\sin\theta\,K$ is lost:

$$
e^{\theta A_{ta}}=\mathrm{I}_4+\sin\theta\,A_{ta}+(1-\cos\theta)\,A_{ta}^{2},\qquad
e^{\theta iD}=\operatorname{diag}\bigl(e^{-3i\theta},e^{i\theta},e^{i\theta},e^{i\theta}\bigr).
$$

**The trace form is not diagonal.** $\operatorname{tr}(d_2^{*}d_3)=-1$, so the coefficients of a matrix in this basis solve a small linear system and are not single projections, and the norms are $2$ and $12$ rather than $4$ on all.

**The brackets of a plane carry thirds.** The bracket of the two arrays of one plane lands in the Cartan, and its coefficients there are $\pm\tfrac23$ and $\pm\tfrac43$, because $iD$ is not a multiple of a projection. Six of the $225$ brackets are of that kind, the two orders for each of the three planes, and the other $219$ are integral.

**What neither basis buys.** No basis of the fifteen is at once of one norm and of one plane per array: the two demands are incompatible, and that incompatibility is the whole content of the choice. Nor does the trace form select a basis, since on $\mathfrak{su}(4)$ it is a negative multiple of the identity and names no direction. What is left is a demand on the support, and there are two such demands, so there are two bases.

**Which basis this article uses, and where.** The sections that follow §*The Derivation and Its Array* use $G_1,\dots,G_{15}$, because the closed forms, the common spectrum and the derivation theorem rest on $K^{2}=-\mathrm{I}_4$. The plane basis answers the questions in which a plane is the object: the change of basis of this section, the Cartan, the incidence split of the six, the image of $\mathrm{ad}_{iD}$, and the form $\beta$. The change of basis is two lines, so a reader can pass from one to the other at any point.

## The Derivation and Its Array

**Definition.** For $K$ in the algebra the derivation is $\mathrm{ad}_K(X)=[K,X]$.

**Proposition (it is a derivation and it is anti-Hermitian).** The Leibniz rule holds, and for the Hilbert–Schmidt form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ one has $(\mathrm{ad}_K)^{*}=\mathrm{ad}_{K^{*}}$, so $\mathrm{ad}_K$ is anti-Hermitian exactly when $K$ is. The kernel of $K\mapsto\mathrm{ad}_K$ is the scalars, so the map is injective on $\mathfrak{su}(4)$.

**Proof.** The Leibniz rule is associativity. For the adjoint, $\operatorname{tr}([K,X]^{*}Y)=\operatorname{tr}(X^{*}[K^{*},Y])$. The kernel is the centre, and a scalar multiple of $\mathrm{I}_4$ is traceless only when it is zero.

**Proposition (the Kronecker form).** Stack the rows of $X$ one after another. Then the array of $\mathrm{ad}_K$ is

$$
[K,\cdot]\longleftrightarrow K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}.
$$

**Proof.** Left multiplication by $K$ acts on the stacked vector by $K\otimes\mathrm{I}_4$; right multiplication by $K$ acts by $\mathrm{I}_4\otimes K^{\mathsf T}$. The commutator is the difference.

**Corollary (the spectrum).** The spectrum of the array is the multiset of the sixteen differences $\kappa_i-\kappa_j$ of the eigenvalues of $K$, the trace is zero, and the exponential is unitary of determinant one.

**Proof.** The eigenvalues of a Kronecker product are the products of the eigenvalues, $-\kappa_j$ from the second factor, so $\kappa_i-\kappa_j$ over all ordered pairs. The sum of the sixteen differences is four times the sum minus four times the same sum. The array is anti-Hermitian, and $\det e^{F}=e^{\operatorname{tr}F}=1$.

**Corollary (one spectrum for the whole basis).** All fifteen generators of the basis above have the eigenvalues $i,i,-i,-i$, so all fifteen derivations have the spectrum $0$ eight times, $2i$ four times and $-2i$ four times.

**Proof.** A generator $K$ of the basis is anti-Hermitian with $K^{2}=-\mathrm{I}_4$, hence normal with the four eigenvalues $i,i,-i,-i$; the spectrum of $\mathrm{ad}_K$ is the multiset of the sixteen differences and depends only on those eigenvalues. The differences of $i,i,-i,-i$ are zero on the eight ordered pairs of equal eigenvalue, $2i$ on the four pairs that run from $i$ to $-i$, and $-2i$ on the four that run back. A generic element of $\mathfrak{su}(4)$ has four distinct eigenvalues and the spectrum $0^{4}$, $\pm i^{6}$, $\pm2i^{2}$; the basis of this article is not generic in that sense, because every one of its members is an involution up to $i$.

## The Exponential of Each Generator

### The Two Kinds of Rotor

**Proposition (two closed forms).** For real $\theta$,

$$
e^{\theta\ell_k}=\cos\theta\,\mathrm{I}_4+\sin\theta\,\ell_k,\qquad
e^{\theta r_k}=\cos\theta\,\mathrm{I}_4+\sin\theta\,r_k,\qquad
e^{\theta iN_{jk}}=\cos\theta\,\mathrm{I}_4+i\sin\theta\,N_{jk}.
$$

**Proof.** Every generator of the basis satisfies $K^{2}=-\mathrm{I}_4$, so the exponential series splits into the even terms, which sum to $\cos\theta\,\mathrm{I}_4$, and the odd terms, which sum to $\sin\theta\,K$.

| generator | $e^{\theta K}$ | on the four coordinates | on the entries of a matrix |
|---|---|---|---|
| $\ell_k$ | real orthogonal, in $\mathrm{SO}(4)$ | turns the plane $\{t,k\}$ by $\theta$ and the complementary plane by $\theta$ in the same sense | the rows of $X$ and the columns of $X$ turn, in the same sense |
| $r_k$ | real orthogonal, in $\mathrm{SO}(4)$ | turns the plane $\{t,k\}$ by $\theta$, as $\ell_k$ does, and the complementary plane by $-\theta$ | the rows turn one way and the columns the other |
| $iN_{kk}$ | imaginary diagonal | multiplies two coordinates by $e^{i\theta}$ and two by $e^{-i\theta}$ | $X_{pq}\mapsto e^{i\theta(d_p-d_q)}X_{pq}$ with $d$ two plus signs and two minus |
| $iN_{jk}$, $j\ne k$ | complex, off-diagonal | mixes two pairs with the factor $i$ | the corresponding rows and columns mix with the factor $i$ |

**Proof.** For $\ell_k$: the array turns $e_t$ to $e_k$ and $e_k$ to $-e_t$, and it turns the two remaining coordinates into each other with the same sign, so both planes turn by $\theta$. For $r_k$: $r_k e_t=e_k$ as well, while on the complementary plane the sign is reversed, $r_x e_y=+e_z$ against $\ell_x e_y=-e_z$, so the two planes turn in opposite senses. For $iN_{kk}$: $N_{xx}=-\operatorname{diag}(1,1,-1,-1)$, and the exponential of an imaginary diagonal is the diagonal of the exponentials of the entries. For $iN_{jk}$ with $j\ne k$: $N_{jk}$ is a symmetric signed permutation with $N_{jk}^{2}=\mathrm{I}_4$ and the eigenvalues $1,1,-1,-1$, so $e^{i\theta N_{jk}}=\cos\theta\,\mathrm{I}_4+i\sin\theta\,N_{jk}$, which is the identity on the diagonal and $\pm i\sin\theta$ on the four entries that $N_{jk}$ moves.

**Corollary (what each family preserves).** The three rotors $e^{\theta\ell_k}$ preserve the real structure and the two planes; the three $e^{\theta r_k}$ preserve the real structure and swap the senses; the nine $e^{\theta iN_{jk}}$ preserve the splitting into two coordinate pairs of the diagonal ones and mix pairs for the others. All fifteen preserve the trace, the determinant, the spectrum and the Hermitian cone.

**Proof.** Each rotor is unitary, and the conjugation by a unitary matrix preserves every similarity invariant and carries $X^{*}$ to $(UXU^{*})^{*}$.

### What Each Generator Does to the Sixteen Entries

**Proposition (rows and columns).** In the conjugation $X\mapsto UXU^{*}$ the rotor acts on the row index on the left and on the column index on the right, so the entry $X_{pq}$ sees two phases or two turns, one from each index.

**Proof.** The array of the derivation is $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$, the first term on the row index and the second on the column index; the exponential is the pair of factors $U\otimes\mathrm{I}_4$ and $\mathrm{I}_4\otimes\bar U$.

| generator | the entry $X_{pq}$ | in words |
|---|---|---|
| $\ell_k$ | $\cos^{2}\theta\,X_{pq}+\cos\theta\sin\theta(\ldots)+\sin^{2}\theta\,X_{p'q'}$ | the row and the column turn in the same sense, so a pair of indices on the turned plane keeps its angle relation |
| $r_k$ | the same with one sense reversed | the row and the column turn in opposite senses |
| $iN_{kk}$ | $e^{i\theta(d_p-d_q)}X_{pq}$ | an entry keeps its modulus, and its phase is the difference of the two signs |
| $iN_{jk}$, $j\ne k$ | a pair of entries exchanges with the factor $i$ | the block on the two pairs turns by $\theta$ with the factor $i$ |

**Remark (the trace and the scalars).** The trace is the sum of the diagonal entries, and it is fixed by all fifteen because every generator is traceless. The scalars $\mathbb{C}\mathrm{I}_4$ are fixed by all fifteen because $\mathrm{I}_4$ commutes with every matrix.

### The Closed Form

**Theorem (the exponential is the conjugation).** With $U=e^{K}$,

$$
e^{\mathrm{ad}_K}=\mathrm{Ad}_U,\qquad \mathrm{Ad}_U(X)=UXU^{*},
$$

and the array of that operator is $U\otimes\bar U$ in the row stacking.

**Proof.** The exponential of $[K,\cdot]$ is the conjugation by $e^{K}$. On the array the two factors exponentiate to $U\otimes\mathrm{I}$ and $\mathrm{I}\otimes\bar U$, which commute.

**Corollary (the invariants).** The array lies in $\mathrm{SU}(16)$, its spectrum is the set of the products $\lambda_i\bar\lambda_j$ of the eigenvalues of $U$, and its fixed space is the commutant of $K$.

**Proof.** A Kronecker product of two unitaries is unitary, and the determinant is $(\det U)^{4}\overline{(\det U)}^{4}=1$. The eigenvalues are $\lambda_i\bar\lambda_j$, of modulus one. The fixed matrices are those commuting with $K$.

## The Commutators and the Grading

**The definitions the table uses.** The six real generators regroup as two triples,

$$
D_k:=\tfrac12(\ell_k-r_k),\qquad S_k:=\tfrac12(\ell_k+r_k),
$$

so that $\ell_k=D_k+S_k$ and $r_k=D_k-S_k$. The three $D_k$ are the inner derivations of the biquaternion algebra, in the normalization $D_k=\tfrac12\mathrm{ad}_{\vec e_k}$.

**Proposition (the bracket table).** With $a,b,c$ cyclic in $x,y,z$,

| bracket | value | where the value sits |
|---|---|---|
| $[\ell_a,\ell_b]$ | $2\ell_c$ | the six |
| $[r_a,r_b]$ | $-2r_c$ | the six |
| $[\ell_a,r_b]$ | $0$ | the six |
| $[D_a,D_b]$ | $D_c$ | the six, normalized |
| $[S_a,S_b]$ | $D_c$ | the six, normalized |
| $[D_a,S_b]$, $[S_a,D_b]$ | $S_c$ | the six, normalized |
| $[\ell_a,iN_{jk}]$ | $2\sum_c\epsilon_{ajc}\,iN_{ck}$ | the nine |
| $[r_a,iN_{jk}]$ | $-2\sum_c\epsilon_{akc}\,iN_{jc}$ | the nine |
| $[iN_{xx},iN_{xy}]$ | $-2r_z$ | the six |
| $[iN_{xy},iN_{yx}]$ | $0$ | the six |

Here $\epsilon_{ajc}$ is the Levi-Civita symbol, $+1$ when $a,j,c$ is a cyclic order of $x,y,z$ and $-1$ in the reverse order. With $a$ and $j$ fixed the sum over $c$ has a single nonzero term, so each of the two mixed rows is one term and not three.

**Proof.** Each identity is a computation with the multiplication of the units: $\ell_a\ell_b=\ell_c$ and $\ell_b\ell_a=-\ell_c$ for $a,b,c$ cyclic, $r_ar_b=-r_c$ because the law of the right matrices is reversed, and left and right matrices commute. The last two follow from $\ell_jr_k\ell_lr_m=\ell_{jl}r_{mk}$ together with the rules for $\ell_a\ell_b$ and $r_ar_b$.

**Corollary (the three counts).** The six close, the nine do not, and the brackets of the nine land in the six.

**Proof.** Rows one to five stay inside the six. Rows six and seven land in the nine. Rows eight and nine land in the six.

**Theorem (the gradings).** The bracket satisfies

$$
[\mathfrak{so},\mathfrak{so}]\subset\mathfrak{so},\qquad [\mathfrak{so},\mathfrak{p}]\subset\mathfrak{p},\qquad [\mathfrak{p},\mathfrak{p}]\subset\mathfrak{so},
$$

with $\mathfrak{so}$ the span of the six and $\mathfrak{p}$ the span of the nine. So the split $6+9$ is a $\mathbb{Z}_2$-grading, the pair is a symmetric pair, and $\mathrm{SU}(4)/\mathrm{SO}(4)$ is the symmetric space it integrates to.

**Proof.** The three inclusions are read off the table: the rows of two of the six stay in the six, the mixed rows stay in the nine, and the bracket of two of the nine lands in the six. A grading whose odd part squares into the even part is the infinitesimal form of a symmetric space.

**Remark (the three inner derivations are half the six).** The three $D_k=\tfrac12(\ell_k-r_k)$ are the anti-diagonal combinations of the two $\mathfrak{su}(2)$'s, and the three $S_k=\tfrac12(\ell_k+r_k)$ the diagonal ones. The $D_k$ are the derivations of the biquaternion algebra; the twelve directions the algebra does not supply are the three $S_k$ together with the nine. That is the content of the count $3+12=15$.

**Proof.** $\ell_k=D_k+S_k$ and $r_k=D_k-S_k$ by definition, so the six span the same space as the two triples. The brackets are $[D_a,D_b]=D_c$, $[D_a,S_b]=[S_a,D_b]=S_c$ and $[S_a,S_b]=D_c$ for $a,b,c$ cyclic, so the six is $\mathfrak{so}(4)$ in the mixed basis $D,S$; in the basis $\tfrac12\ell,\tfrac12 r$ the same six reads as two commuting $\mathfrak{su}(2)$'s, $[\ell_a,\ell_b]=2\ell_c$ and $[r_a,r_b]=-2r_c$.

## The Dimension Ladder

| set | defining condition | real dimension |
|---|---|---|
| $M_4(\mathbb{C})$ | none | $32$ |
| the traceless matrices | $\operatorname{tr}X=0$ | $30$ |
| the anti-Hermitian matrices | $K^{*}=-K$ | $16$ |
| $\mathfrak{su}(4)$ | both | $15$ |
| $\mathfrak{so}(4)$ inside | real antisymmetric | $6$ |
| the $\mathfrak{p}$ summand | $i$ times real symmetric traceless, the non-compact part | $9$ |
| $\operatorname{End}(M_4)\cong M_{16}(\mathbb{C})$ | none | $512$ |
| the anti-Hermitian operators | $F^{*}=-F$ | $256$ |
| the derivations | Leibniz rule | $30$ |
| the anti-Hermitian derivations | both | $15$ |

**Remark (three ladders at once).** At the element level $32\to30\to16\to15$. At the operator level $512\to256\to30\to15$. Inside the fifteen, $15=6+9$ and $6+9=6+6+3$, the second being six symmetric arrays and three diagonal ones. The number fifteen appears twice for two different reasons: the generators have fifteen parameters because the trace removes one of the sixteen, and the derivations have real dimension fifteen because the algebra is a full matrix algebra and the inner derivations are the algebra modulo the centre. The map $K\mapsto\mathrm{ad}_K$ is the isomorphism between them, and it is why the two fifteens agree.

**Remark (the operator level is five hundred and twelve).** $\operatorname{End}(M_4)$ has complex dimension $16\cdot16=256$, so real dimension five hundred and twelve. The anti-Hermitian half is two hundred and fifty-six, the derivation condition cuts to thirty, and the anti-Hermitian condition cuts to fifteen. The derivation condition is the strong one: it removes four hundred and eighty-two of the five hundred and twelve real dimensions, against the two hundred and fifty-six that the anti-Hermitian condition removes, and the two together leave fifteen. Neither condition implies the other. The derivation $\mathrm{ad}_K$ with $K=\operatorname{diag}(1,0,0,0)$ is not anti-Hermitian, since $(\mathrm{ad}_K)^{*}=\mathrm{ad}_{K^{*}}=\mathrm{ad}_K$ makes it Hermitian and it is not zero; and of the two hundred and fifty-six real dimensions of anti-Hermitian operators only fifteen are derivations.

## The Orbits

**Proposition (the orbit of a matrix).** The conjugation by $\mathrm{SU}(4)$ sends a matrix with four distinct eigenvalues to the matrices with the same spectrum and the same multiplicities — with four distinct eigenvalues that is the whole isospectral set — and the orbit has real dimension $12$.

**Proof.** The stabiliser of $X$ in the group is the set of unitaries commuting with $X$; for distinct eigenvalues these are the diagonal unitaries in the eigenbasis, of real dimension three. The orbit-stabiliser identity gives $15-3=12$. The same number is read on the array: $\operatorname{rank}\mathrm{ad}_X=16-4=12$, because the kernel of $\mathrm{ad}_X$ is the commutant, of complex dimension four.

**Proposition (the five patterns).** A generator has imaginary eigenvalues of sum zero, so the patterns of multiplicities are $1+1+1+1$, $2+1+1$, $2+2$, $3+1$ and $4$. The commutant of the generator in $M_4$ and the orbit of the generator have the following dimensions.

| pattern | example | commutant, complex dimension | orbit, real dimension |
|---|---|---|---|
| $1+1+1+1$ | $i\operatorname{diag}(1,2,-1,-2)$ | $1+1+1+1=4$ | $12$ |
| $2+1+1$ | $i\operatorname{diag}(1,1,-2,0)$ | $4+1+1=6$ | $10$ |
| $2+2$ | $i\operatorname{diag}(1,1,-1,-1)$ | $4+4=8$ | $8$ |
| $3+1$ | $i\operatorname{diag}(1,1,1,-3)$ | $9+1=10$ | $6$ |
| $4$ | $0$ | $16$ | $0$ |

**Proof.** The commutant of a matrix with multiplicities $m_1,\dots,m_r$ is the block diagonal subalgebra of block sizes $m_l$, of complex dimension $\sum_l m_l^{2}$. The orbit has real dimension $16-\sum_l m_l^{2}$, which is the rank of $\mathrm{ad}_K$ and also $15$ minus the real dimension of the stabiliser. The pattern $4$ forces all four eigenvalues equal and the sum zero, so all are zero and the generator is the zero matrix, whose orbit is the single point and which is listed to close the classification; the pattern $3+1$ is realized by $i\operatorname{diag}(1,1,1,-3)$, whose entries are real and of sum zero.

## The Worked Example

**Proposition (two double eigenvalues).** Let $K=i\operatorname{diag}(1,1,-1,-1)$. Then the spectrum of the array is $0$ eight times and $\pm2i$ four times each, the commutant of $K$ is eight complex dimensional, and at $\theta=\pi/2$ the rotor is the identity on the commutant and minus the identity on the other eight dimensions.

**Proof.** The eigenvalues are $i,i,-i,-i$, so the differences are $0$ on the pairs of equal eigenvalue, which are eight ordered pairs, $2i$ on the four pairs of the first kind and $-2i$ on the four of the second. The commutant of a matrix with two eigenvalues of multiplicity two is the block diagonal subalgebra, of complex dimension $4+4=8$. The rotor at $\theta=\pi/2$ is $\operatorname{diag}(i,i,-i,-i)$, and the conjugation multiplies $X_{ij}$ by $e^{i\theta(\epsilon_i-\epsilon_j)}$ with $\epsilon=(1,1,-1,-1)$.

**Remark (why the example matters).** A generic generator fixes four complex dimensions, the span of $\mathrm{I}_4,K,K^{2},K^{3}$, and not only the scalars. This one fixes eight, which is the largest value for a generator with two distinct eigenvalues. The fixed space of the rotor is the commutant of the generator, so its dimension is $\sum_l m_l^{2}$ over the multiplicities, and the five patterns give the five values $4,6,8,10,16$ of the table above.

## The Two Frames

| statement | operator frame of the algebra | matrix frame |
|---|---|---|
| carrier | $\operatorname{End}(\mathbb{B})\cong M_4(\mathbb{C})$ | $M_4(\mathbb{C})$ |
| generator | an operator $K$ on the algebra | a matrix $K$ |
| basis of the carrier | the sixteen products $T_{a,b}$ | the sixteen matrix units |
| the fifteen generators | the fifteen operators in the operator basis | the six $\ell_k,r_k$ and the nine $iN_{jk}$ |
| array | sixteen by sixteen in that basis | $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$ |
| exponential | $\mathrm{Ad}_U$ | $U\otimes\bar U$ |
| image of the rotor map | $\mathrm{PSU}(4)$, kernel $\mathbb{Z}_4$ | the same |

**Remark (the checks).** On two hundred random generators of $\mathfrak{su}(4)$: the array is anti-Hermitian exactly, the Leibniz residual is at most $2.6\times10^{-14}$, the Kronecker form $F(X)=KX-XK$ holds to $7.1\times10^{-15}$, the power sums of the spectrum agree with the sums of the differences of the eigenvalues to a relative $1.2\times10^{-12}$, the exponential equals $U\otimes\bar U$ to $5.1\times10^{-15}$, and it is unitary to $4.7\times10^{-15}$ with determinant one to $7.3\times10^{-15}$. The fifteen generators of the basis are anti-Hermitian and traceless exactly, of rank fifteen, each of them squares to $-\mathrm{I}_4$ with the eigenvalues $i,i,-i,-i$. The closed forms agree to $3.6\times10^{-16}$. The bracket rows are exact identities over $\mathbb{Q}(i)$, and the residuals quoted for them are floating-point confirmations of exact identities rather than tolerances: $[\ell_x,\ell_y]=2\ell_z$, $[r_x,r_y]=-2r_z$, $[\ell_a,r_b]=0$, $[D_x,D_y]=D_z$, $[S_x,S_y]=D_z$, $[\ell_x,iN_{yz}]=2iN_{zz}$, $[iN_{xx},iN_{xy}]=-2r_z$, $[iN_{xy},iN_{yx}]=0$. The grading is checked on all $36+108+81$ pairs, with residual at most $8.9\times10^{-16}$: two of the six bracket into the six, one of the six with one of the nine into the nine, and two of the nine into the six.

## Summary

The anti-Hermitian traceless matrices of order four are $\mathfrak{su}(4)$, of real dimension fifteen, split as six real antisymmetric and nine purely imaginary, $6+9$. The fifteen are printed one to a display and numbered $G_{1}$ to $G_{15}$. The six are the left and right matrices of the three vector units in the axis-free frame, they are $\mathfrak{su}(2)\oplus\mathfrak{su}(2)=\mathfrak{so}(4)$, and the nine are $i$ times their nine products.

Every generator of the words basis satisfies $K^{2}=-\mathrm{I}_4$, so every rotor is a closed form in $\cos\theta$ and $\sin\theta$, and every generator has the eigenvalues $i,i,-i,-i$. The three inner derivations of the biquaternion algebra are the anti-diagonal combinations $\tfrac12(\ell_k-r_k)$, which satisfy $[D_x,D_y]=D_z$; the twelve remaining directions are the diagonal combinations $\tfrac12(\ell_k+r_k)$ and the nine.

The bracket respects the grading: the six is a subalgebra, the mixed brackets stay in the nine, and the brackets of two of the nine land in the six. So $\mathrm{SU}(4)/\mathrm{SO}(4)$ is a symmetric space, and the fifteen of this article are its tangent data together with the isotropy algebra.

The article prints two bases of the fifteen. The first is forced: eight arrays, sixteen words, the deletion of $W_{tt}$, the factor $i$ on the nine. It is orthogonal with $\operatorname{tr}(G_a^{*}G_b)=4\delta_{ab}$, every structure constant in it is an integer, every member squares to $-\mathrm{I}_4$, and every rotor is $\cos\theta\,\mathrm{I}_4+\sin\theta\,K$. The second is one optional step further, the half-sum and half-difference of the six pairs, and it puts each off-diagonal generator on a single plane. It pays for that where the two demands conflict: norms $2$ and $12$ instead of $4$, a spectrum that varies from array to array, a rotor of degree two in $K$, and thirds in the brackets of a plane with its own partner. The first basis is the one the rotors and the derivation spectrum are computed in; the second is the one in which a plane is one array.

Each generator gives the derivation $[K,\cdot]$, of array $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$, of spectrum the differences of the eigenvalues of $K$, of trace zero and of exponential $U\otimes\bar U\in\mathrm{SU}(16)$. The dimension ladder is $32\to30\to16\to15$ at the element level and $512\to256\to30\to15$ at the operator level, and the map $K\mapsto\mathrm{ad}_K$ makes the two fifteens the same fifteen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\mathrm{axf},\vec e_k}$ | the axis-free left matrix of the vector unit $\vec e_k$ |
| $R_{\mathrm{axf},\vec e_k}$ | the axis-free right matrix of the vector unit $\vec e_k$ |
| $\ell_k$, $r_k$ | the short names for the two above |
| $G_{1},\dots,G_{15}$ | the fifteen generators, numbered once in the section that prints them |
| $N_{jk}$ | the product $\ell_jr_k$, a symmetric signed permutation; the generator is $iN_{jk}$ |
| $A_{jk}$, $iS_{jk}$ | the plane arrays $E_{jk}-E_{kj}$ and $i(E_{jk}+E_{kj})$, for $j<k$ |
| $iD$, $d_2$, $d_3$ | the three diagonal arrays of the plane basis, $i(W_{xx}+W_{yy}+W_{zz})$ and two differences |
| $\beta$ | the form $\operatorname{Re}\operatorname{tr}([X,iD]^{*}[Y,iD])$ |
| $\ell_t$, $r_t$ | the two scalar matrices of the axis-free frame, both $\mathrm{I}_4$ |
| $D_k$ | $\tfrac12(\ell_k-r_k)$, the derivation $\tfrac12\mathrm{ad}_{\vec e_k}$ |
| $S_k$ | $\tfrac12(\ell_k+r_k)$, the symmetric combination |
| $\mathfrak{so}$, $\mathfrak{p}$ | the span of the six and the span of the nine |
| $\mathrm{ad}_K$ | the derivation $[K,\cdot]$ |
| $\langle X,Y\rangle$ | the Hilbert–Schmidt form $\operatorname{tr}(X^{*}Y)$ |
| $U$ | the rotor $e^{K}\in\mathrm{SU}(4)$ |
| $\mathrm{Ad}_U$ | the conjugation $X\mapsto UXU^{*}$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $\mathfrak{su}(n)$, the Cartan and the adjoint representation.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Kronecker product, its eigenvalues and the commutator equation.
- [Matrix Representations and Conventions](matrix-representations-conventions.md), for the axis-free matrices the generators are built from, and *Why AXF Matrices instead of Pauli and Gamma Matrices* for the rule the article follows.
- [Automorphisms and Derivations of Algebras](automorphisms-and-derivations-of-algebras.md), for the normalization $D_k=\tfrac12\mathrm{ad}_{\vec e_k}$ and the bracket $[D_1,D_2]=D_3$.
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the same six in the Peirce frame.
- [The Anti-Hermitian Derivations of $M_2(\mathbb{C})$ as $\mathfrak{su}(2)$](the-anti-hermitian-derivations-of-m2c-as-su2.html), for the same construction at order two, with three generators.
- [The Anti-Hermitian Derivations of the Operators of the Biquaternion Algebra as $\mathfrak{su}(4)$](the-anti-hermitian-derivations-of-the-operators-of-the-biquaternion-algebra-as-su4.html), for the same fifteen generators in the operator basis of the algebra.
- [The Exponential and the Lie Group of $M_4(\mathbb{C})$](the-exponential-and-the-lie-group-of-m4c.html), for the group behind the rotors.
- [The AXF Matrices of the Twenty-One Generators](../articles_physics/the-axf-matrices-of-the-twenty-one-generators.html), for the plane basis of the same fifteen, printed there beside the twenty-one generators.
