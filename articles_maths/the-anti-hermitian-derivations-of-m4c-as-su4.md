# __The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$__

## Introduction

**Two conditions pick out the generators: anti-Hermitian and traceless. They hold exactly for fifteen matrices, which form $\mathfrak{su}(4)$ of real dimension fifteen, and the fifteen split as six real antisymmetric and nine purely imaginary, $6+9$. Each generator $K$ gives the derivation $[K,\cdot]$, whose array is the Kronecker difference $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$, and whose exponential is the conjugation by the rotor $U=e^{K}\in\mathrm{SU}(4)$.**

The article writes the fifteen generators out in full, and it builds them the way the corpus builds every array: from the axis-free matrices $L_{\mathrm{axf}}$ and $R_{\mathrm{axf}}$ of *Matrix Representations and Conventions*, not from a frame chosen for the occasion. The six real generators are the left and right matrices of the three vector units; the nine imaginary ones are $i$ times their nine products. Each of the fifteen is an involution up to the factor $i$, so each has the eigenvalues $i,i,-i,-i$ and each rotor is a closed form in $\cos\theta$ and $\sin\theta$.

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

**Remark (the split is not conjugation invariant).** The split is taken with respect to the standard real structure of $\mathbb{C}^4$, and a conjugation by a unitary matrix with complex entries moves the six. The split therefore records the position of the generator relative to the standard basis, and that position is what decides the shape of the rotor. Two generators with the same eigenvalues are conjugate to each other and so have the same derivation spectrum, and they are still different rotors: $\ell_x$ turns both coordinate planes by $\theta$, $r_x$ turns one plane by $\theta$ and the other by $-\theta$, and $iN_{xx}$ multiplies two coordinates by $e^{i\theta}$ and two by $e^{-i\theta}$. All three have the eigenvalues $i,i,-i,-i$ and the derivation spectrum $0^{8},(\pm2i)^{4}$.

## The Fifteen Generators, Built from the Axis-Free Matrices

**The rule.** The generators are not written in a frame chosen for the occasion. They are built from the arrays the corpus already prints, the axis-free left and right matrices of the three vector units in *Matrix Representations and Conventions*. Nothing below introduces a frame of its own.

**Definition.** With the axis-free matrices of the units, put

$$
\ell_k:=L_{\mathrm{axf},\vec e_k},\qquad r_k:=R_{\mathrm{axf},\vec e_k},\qquad N_{jk}:=\ell_jr_k,\qquad j,k\in\{x,y,z\},
$$

and take the fifteen generators to be

$$
\ell_x,\;\ell_y,\;\ell_z,\qquad r_x,\;r_y,\;r_z,\qquad iN_{jk}\ \ (9\ \text{of them}).
$$

**Proposition (the count and the properties).** The fifteen are anti-Hermitian, traceless and linearly independent over $\mathbb{R}$, so they are a basis of $\mathfrak{su}(4)$.

**Proof.** The printed matrices $L_{\mathrm{axf},\vec e_k}$ and $R_{\mathrm{axf},\vec e_k}$ are signed permutations with entries in $\{0,1,-1\}$ and are antisymmetric, so each is anti-Hermitian and of trace zero. Each $N_{jk}$ is a product of two such and is a symmetric signed permutation, of trace zero, so $iN_{jk}$ is anti-Hermitian and traceless. For independence: the sixteen products $L_{\mathrm{axf},\mu}R_{\mathrm{axf},\nu}$ are a basis of $M_4(\mathbb{C})$, the fifteen above are fifteen of them, and the factor $i$ on the nine is invertible.

**Remark (why the products are sixteen and not fewer).** The sixteen products are the arrays of the sixteen operators $T_{a,b}:X\mapsto aXb$ in the axis-free frame, and those operators are a basis of $\operatorname{End}(\mathbb{B})$. Their arrays have rank sixteen. This is the same count as the operator frame of *The Anti-Hermitian Derivations of the Operators of the Biquaternion Algebra as $\mathfrak{su}(4)$*, where the carrier is written as the sixteen products.

### The Six Real Generators

The three left matrices, as the conventions article prints them:

$$
\ell_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
\ell_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
\ell_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

The three right matrices:

$$
r_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\quad
r_y=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
r_z=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**Remark (the six are the chiral pair).** The left matrices commute with the right ones, $\ell_a r_b=r_b\ell_a$, because a left and a right multiplication commute. Each triple closes on its own, $[\ell_x,\ell_y]=2\ell_z$ and $[r_x,r_y]=-2r_z$, so the six are $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, of real dimension six, which is $\mathfrak{so}(4)$. In the Peirce frame the same six are the chiral generators $K_a^{L}$ and $K_a^{R}$ of *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*; the axis-free frame writes them as the left and right matrices of the units.

**Corollary (the three inner derivations inside the six).** With

$$
D_k:=\tfrac12(\ell_k-r_k),\qquad S_k:=\tfrac12(\ell_k+r_k),
$$

the three $D_k$ are the derivations $\tfrac12\mathrm{ad}_{\vec e_k}$ of the biquaternion algebra in the axis-free frame, and they satisfy

$$
[D_x,D_y]=D_z,\qquad [D_y,D_z]=D_x,\qquad [D_z,D_x]=D_y .
$$

**Proof.** The array of $\mathrm{ad}_{\vec e_k}$ is $\ell_k-r_k$, the difference of the left and the right matrix, so $D_k$ is $\tfrac12$ of it, which is the normalization of *Automorphisms and Derivations of Algebras*. The brackets are computed from the two triples: $[\ell_x-r_x,\ell_y-r_y]=2\ell_z+2r_z$, since the cross brackets vanish, and half of that is $\ell_z+r_z=2D_z$; so $[D_x,D_y]=D_z$.

### The Nine Imaginary Generators

The nine products $N_{jk}=\ell_jr_k$ are the symmetric signed permutations

$$
N_{xx}=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\;
N_{yy}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&1\end{pmatrix},\;
N_{zz}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix},
$$

$$
N_{xy}=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\;
N_{xz}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\;
N_{yx}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$

$$
N_{yz}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix},\;
N_{zx}=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\;
N_{zy}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix}.
$$

**Proposition (all fifteen are involutions up to $i$).** Each of the fifteen satisfies $K^{2}=-\mathrm{I}_4$, so each has the eigenvalues $i,i,-i,-i$ and each is of trace zero.

**Proof.** $\ell_k^{2}=-\mathrm{I}_4$ because $\ell_k$ turns the two coordinate planes $\{t,k\}$ and the remaining pair, each by a quarter turn of the array, and the square of a real quarter turn is minus the identity. The same holds for $r_k$. Each $N_{jk}$ is a symmetric signed permutation with $N_{jk}^{2}=\mathrm{I}_4$, so $(iN_{jk})^{2}=-\mathrm{I}_4$. Four eigenvalues, each of modulus one and of square $-1$, are $\pm i$; the trace is zero, so they are $i,i,-i,-i$.

**Remark (the Cartan is inside the nine).** The three diagonal generators of the basis are $iN_{xx}$, $iN_{yy}$, $iN_{zz}$: they are imaginary diagonal, traceless, and they span the diagonal traceless subspace. The other six of the nine are off-diagonal, and the six real generators have no diagonal entry at all. So the basis of this article puts the Cartan among the nine and puts no Cartan among the six.

**Remark (the ordering of the corpus, not of a textbook).** A textbook basis would single out a Cartan first and then add the roots. This basis does the opposite: the six real generators come from the multiplication itself, and the Cartan appears among the nine as three products. That is what building the generators from the axis-free matrices does, and it is the reason the fifteen here are all of one shape rather than split into weights.

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

with $D_k=\tfrac12(\ell_k-r_k)$ and $S_k=\tfrac12(\ell_k+r_k)$.

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
| the open summand | $i$ times real symmetric traceless | $9$ |
| $\operatorname{End}(M_4)\cong M_{16}(\mathbb{C})$ | none | $512$ |
| the anti-Hermitian operators | $F^{*}=-F$ | $256$ |
| the derivations | Leibniz rule | $30$ |
| the anti-Hermitian derivations | both | $15$ |

**Remark (three ladders at once).** At the element level $32\to30\to16\to15$. At the operator level $512\to256\to30\to15$. Inside the fifteen, $15=6+9$ and $6+9=6+6+3$. The number fifteen appears twice for two different reasons: the generators have fifteen parameters because the trace removes one of the sixteen, and the derivations have real dimension fifteen because the algebra is a full matrix algebra and the inner derivations are the algebra modulo the centre. The map $K\mapsto\mathrm{ad}_K$ is the isomorphism between them, and it is why the two fifteens agree.

**Remark (the operator level is five hundred and twelve).** $\operatorname{End}(M_4)$ has complex dimension $16\cdot16=256$, so real dimension five hundred and twelve. The anti-Hermitian half is two hundred and fifty-six, the derivation condition cuts to thirty, and the anti-Hermitian condition cuts to fifteen. The two conditions are not independent: the derivation condition alone loses four hundred and eighty-two, and it is the strong one.

## The Orbits

**Proposition (the orbit of a matrix).** The conjugation by $\mathrm{SU}(4)$ sends a matrix with four distinct eigenvalues to the matrices with the same spectrum, and the orbit has real dimension $12$.

**Proof.** The stabiliser of $X$ in the group is the set of unitaries commuting with $X$; for distinct eigenvalues these are the diagonal unitaries in the eigenbasis, of real dimension three. The orbit-stabiliser identity gives $15-3=12$. The same number is read on the array: $\operatorname{rank}\mathrm{ad}_X=16-4=12$, because the kernel of $\mathrm{ad}_X$ is the commutant, of complex dimension four.

**Proposition (the five patterns).** A generator has imaginary eigenvalues of sum zero, so the patterns of multiplicities are $1+1+1+1$, $2+1+1$, $2+2$, $3+1$ and $4$. The commutant of the generator in $M_4$ and the orbit of the generator have the following dimensions.

| pattern | example | commutant, complex dimension | orbit, real dimension |
|---|---|---|---|
| $1+1+1+1$ | $i\operatorname{diag}(1,2,-1,-2)$ | $1+1+1+1=4$ | $12$ |
| $2+1+1$ | $i\operatorname{diag}(1,1,-2,0)$ | $4+1+1=6$ | $10$ |
| $2+2$ | $i\operatorname{diag}(1,1,-1,-1)$ | $4+4=8$ | $8$ |
| $3+1$ | $i\operatorname{diag}(1,1,1,-3)$ | $9+1=10$ | $6$ |
| $4$ | $0$ | $16$ | $0$ |

**Proof.** The commutant of a matrix with multiplicities $m_1,\dots,m_r$ is the block diagonal subalgebra of block sizes $m_l$, of complex dimension $\sum_l m_l^{2}$. The orbit has real dimension $16-\sum_l m_l^{2}$, which is the rank of $\mathrm{ad}_K$ and also $15$ minus the real dimension of the stabiliser. The pattern $4$ forces all four eigenvalues equal and the sum zero, so all are zero and the generator vanishes; the pattern $3+1$ is the pattern of $H_3$, whose entries $1,1,1,-3$ are real and admissible.

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

**Remark (the checks).** On two hundred random generators of $\mathfrak{su}(4)$: the array is anti-Hermitian exactly, the Leibniz residual is at most $2.6\times10^{-14}$, the Kronecker form $F(X)=KX-XK$ holds to $7.1\times10^{-15}$, the power sums of the spectrum agree with the sums of the differences of the eigenvalues to a relative $1.2\times10^{-12}$, the exponential equals $U\otimes\bar U$ to $5.1\times10^{-15}$, and it is unitary to $4.7\times10^{-15}$ with determinant one to $7.3\times10^{-15}$. The fifteen generators of the basis are anti-Hermitian and traceless exactly, of rank fifteen, each of them squares to $-\mathrm{I}_4$ with the eigenvalues $i,i,-i,-i$. The closed forms agree to $3.6\times10^{-16}$. The bracket rows hold exactly: $[\ell_x,\ell_y]=2\ell_z$, $[r_x,r_y]=-2r_z$, $[\ell_a,r_b]=0$, $[D_x,D_y]=D_z$, $[S_x,S_y]=D_z$, $[\ell_x,iN_{yz}]=2iN_{zz}$, $[iN_{xx},iN_{xy}]=-2r_z$, $[iN_{xy},iN_{yx}]=0$. The grading is checked on all $36+108+81$ pairs, with residual at most $8.9\times10^{-16}$: two of the six bracket into the six, one of the six with one of the nine into the nine, and two of the nine into the six.

## Summary

The anti-Hermitian traceless matrices of order four are $\mathfrak{su}(4)$, of real dimension fifteen, split as six real antisymmetric and nine purely imaginary, $6+9$. The six are the left and right matrices of the three vector units in the axis-free frame, they are $\mathfrak{su}(2)\oplus\mathfrak{su}(2)=\mathfrak{so}(4)$, and the nine are $i$ times their nine products.

Every generator of the basis satisfies $K^{2}=-\mathrm{I}_4$, so every rotor is a closed form in $\cos\theta$ and $\sin\theta$, and every generator has the eigenvalues $i,i,-i,-i$. The three inner derivations of the biquaternion algebra are the anti-diagonal combinations $\tfrac12(\ell_k-r_k)$, which satisfy $[D_x,D_y]=D_z$; the twelve remaining directions are the diagonal combinations $\tfrac12(\ell_k+r_k)$ and the nine.

The bracket respects the grading: the six is a subalgebra, the mixed brackets stay in the nine, and the brackets of two of the nine land in the six. So $\mathrm{SU}(4)/\mathrm{SO}(4)$ is a symmetric space, and the fifteen of this article are its tangent data together with the isotropy algebra.

Each generator gives the derivation $[K,\cdot]$, of array $K\otimes\mathrm{I}_4-\mathrm{I}_4\otimes K^{\mathsf T}$, of spectrum the differences of the eigenvalues of $K$, of trace zero and of exponential $U\otimes\bar U\in\mathrm{SU}(16)$. The dimension ladder is $32\to30\to16\to15$ at the element level and $512\to256\to30\to15$ at the operator level, and the map $K\mapsto\mathrm{ad}_K$ makes the two fifteens the same fifteen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\mathrm{axf},\vec e_k}$ | the axis-free left matrix of the vector unit $\vec e_k$ |
| $R_{\mathrm{axf},\vec e_k}$ | the axis-free right matrix of the vector unit $\vec e_k$ |
| $\ell_k$, $r_k$ | the short names for the two above |
| $N_{jk}$ | the product $\ell_jr_k$, a symmetric signed permutation |
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
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the subalgebras of the fifteen.
- [The Exponential and the Lie Group of $M_4(\mathbb{C})$](the-exponential-and-the-lie-group-of-m4c.html), for the group behind the rotors.
