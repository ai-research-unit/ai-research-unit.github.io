# __Hermitian Solutions of the Pair Matrix Equation over the Reduced Biquaternions__

## Introduction

The pair equation over the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ is

$$
(AXB,CXD)=(E,F),\qquad A,C\in\mathbb{B}_{\mathrm{r}}^{m\times n},\quad B,D\in\mathbb{B}_{\mathrm{r}}^{n\times s},\quad E,F\in\mathbb{B}_{\mathrm{r}}^{m\times s},
$$

with one unknown $X\in\mathbb{B}_{\mathrm{r}}^{n\times n}$ carrying two equations at once. The two residuals are measured together by

$$
\bigl\|(AXB-E,CXD-F)\bigr\|_{\mathrm F}^{2}=\|AXB-E\|_{\mathrm F}^{2}+\|CXD-F\|_{\mathrm F}^{2},
$$

the square of the Frobenius norm of *Least Squares and Total Least Squares over the Reduced Biquaternions*. The problem is to minimise that residual over $X\in H(n)$, and then, among the minimisers, to take the one of least $\|X\|_{\mathrm F}$. The article reads the least squares solutions of the pair in the Hermitian set of the source, the set $H(n)$ of §*The Pair Equation and the Hermitian Set*, and the inverse eigenvalue problem that is its application.

**Hermitian is taken in the source's sense, and the corpus's sense is a different condition.** The corpus calls Hermitian an element fixed by the star, the plane $\mathbb{R}\{1,ij\}$ of *The Group of Units of the Algebra of the Reduced Biquaternions*. The source's set is fixed by the transpose composed with the conjugation negating the three imaginary units, which is not the star, not the bar, not the natural sign and not the flat; it is not multiplicative, since it sends $i$ and $j$ to $-i$ and $-j$, whose product is $ij$, while it sends $ij$ to $-ij$. The name is kept because the construction is the source's, and the set is written in blocks throughout, so no glyph is attached to that conjugation.

**The sibling reduction does not apply.** The set $H(n)$ has real dimension $2n^{2}-n$, and it is not closed under multiplication by $i$ or by $j$: $iX$ is Hermitian only when $X_{0}=X_{1}=X_{3}=0$, and $jX$ only when $X_{0}=X_{2}=0$. The set is therefore not a module over the algebra and not an L-structure of entry type in the sense of *Matrix Equations and Structured Solutions over the Reduced Biquaternions*. The idempotent decomposition does not split the problem into two independent complex problems, the two idempotent coordinates are coupled, and the reduction to two independent complex Moore–Penrose solutions is unavailable.

**The two devices that replace the reduction are the real representation and the half-vectorisation.** The real representation $M^{R}$ of *Least Squares and Total Least Squares over the Reduced Biquaternions* turns the pair into one real linear system, and the vectorisations $\mathrm{vec}_{S}$ and $\mathrm{vec}_{A}$ of the symmetric and the antisymmetric parts turn the Hermitian constraint into a linear parametrisation with $2n^{2}-n$ coordinates. The source's matrix $J$ passes from the row form of the real representation to its full form, and the matrices $Q$ and $R$ carry the compressed coordinates to the row form and to the four real blocks.

**The results.** The residual identity $\|(AXB-E,CXD-F)\|_{\mathrm F}^{2}=\|PJQz-t\|^{2}$ holds for every Hermitian $X$, with $z$ the half-vectorisation and $P$, $J$, $Q$, $t$ of §*The Reduction to One Real System*; the least squares set is the set of Hermitian matrices whose four vecs are $R$ applied to the affine set of least squares solutions of $PJQz=t$, and its least-norm element in the compressed coordinates has the column $R(PJQ)_{\mathrm{MP}}t$ as its four vecs. The pair has a Hermitian solution exactly when the residual of $t$ against the projector of $PJQ$ vanishes, and the solution is unique exactly when $\operatorname{rank}(PJQ)=2n^{2}-n$. The complex field is the degenerate case $X_{2}=X_{3}=0$, with $n^{2}$ unknowns instead of $2n^{2}-n$, and the Hermitian partial inverse eigenvalue problem $M\Phi=\Phi\Lambda$ is the case $A=I_{n}$, $C=D=0$, $B=\Phi$, $E=\Phi\Lambda$, $F=0$ of the complex problem.

**Boundaries.** The real representation, the Frobenius norm, the coefficient stack and the idempotent reduction are *Least Squares and Total Least Squares over the Reduced Biquaternions*, which owns them; the L-structure and the structures of entry type are *Matrix Equations and Structured Solutions over the Reduced Biquaternions*. The algebra and the idempotents are *Reduced Biquaternion Space* and *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the four involutions are *The Two Involutions and the Group of Involutions of the Reduced Biquaternions*; the algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms*; the complex Hermitian and skew-symmetric matrices are the classical objects of Horn and Johnson. The pair equation and its Hermitian reduction, the vectorisations, the encodings and the inverse eigenvalue problem are the source's, Ahmad and Bhadala.

**Conventions.** The element is $Q_\pm=Q_++jQ_-$ with $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$, the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, and the idempotent coordinates are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$. A matrix over $\mathbb{B}_{\mathrm{r}}$ is written $M=M_{0}+M_{1}i+M_{2}j+M_{3}ij$ with the four coefficient matrices real, and its idempotent components are the complex matrices $M^{+}$ and $M^{-}$ of *Least Squares and Total Least Squares over the Reduced Biquaternions*. The **coefficient stack** $C_{M}$ is the four coefficient matrices one above the other, of the same article; its column reading $\mathrm{vec}(C_{M})$ interleaves the four blocks, and the source's displays, followed here, put the four vecs $\mathrm{vec}(M_{0}),\dots,\mathrm{vec}(M_{3})$ one above the other instead. The form is $\langle\cdot,\cdot\rangle_{\natural*}$, read entrywise as $K_{\mathrm F}$ with $\|M\|_{\mathrm F}^{2}=K_{\mathrm F}(M)$; the transpose is written $^{\mathsf T}$, the $K$-adjoint $M^{\dagger}=\bar M^{\mathsf T}$, and the Moore–Penrose inverse $M_{\mathrm{MP}}$. The dagger is never used for the source's conjugation, which is written in blocks. The **row form** $M^{R}_{r}$ is the first block row of the real representation, $M^{R}_{r}=[M_{0},-M_{1},M_{2},-M_{3}]$, as in the source. The identity is $I_{n}$.

## The Pair Equation and the Hermitian Set

### The Pair Equation

**The pair imposes two linear equations on one unknown, and the least squares problem measures the two residuals together.**

**Definition (the pair equation).** Given $A,C\in\mathbb{B}_{\mathrm{r}}^{m\times n}$, $B,D\in\mathbb{B}_{\mathrm{r}}^{n\times s}$ and $E,F\in\mathbb{B}_{\mathrm{r}}^{m\times s}$, the **pair equation** is

$$
AXB=E,\qquad CXD=F,
$$

and its **residual** at $X$ is the pair $(AXB-E,CXD-F)$, of squared size

$$
\|(AXB-E,CXD-F)\|_{\mathrm F}^{2}=\|AXB-E\|_{\mathrm F}^{2}+\|CXD-F\|_{\mathrm F}^{2}.
$$

The two equations share the unknown, which is what distinguishes the pair from the equation $\sum_{l}A_{l}X_{l}B_{l}=E$ of *Matrix Equations and Structured Solutions over the Reduced Biquaternions*: there each unknown carries one coefficient pair, here one unknown carries two.

### The Conjugation of the Source

**The source's Hermitian condition is the fixed set of the transpose followed by the conjugation that negates the three imaginary units.**

**Definition.** The **conjugation of the source** is the real-linear map

$$
a_{0}+a_{1}i+a_{2}j+a_{3}ij\longmapsto a_{0}-a_{1}i-a_{2}j-a_{3}ij .
$$

**Proposition (it is an involution and it is not multiplicative).** The conjugation of the source is an involution of the real vector space and it fixes the scalar block; it is not multiplicative.

*Proof.* Applying it twice returns the element, and it fixes $1$. On the units, $i\mapsto-i$ and $j\mapsto-j$, so the product $ij$ maps to $(-i)(-j)=ij$, while the conjugation sends $ij$ to $-ij$; the two images differ, and the map is not multiplicative.

The failure is the reason the map is not one of the four involutions of *The Two Involutions and the Group of Involutions of the Reduced Biquaternions*: the bar, the natural sign and the star are multiplicative because the algebra is commutative, and this map is outside their Klein group. Its fixed set on elements is the scalar line, not the Hermitian plane $\mathbb{R}\{1,ij\}$ of the corpus, and the map is an involution of the real space and not an automorphism of the algebra.

### The Hermitian Set

**The Hermitian set is the set of matrices fixed by the transpose composed with the conjugation of the source, and it is a real subspace of dimension $2n^{2}-n$.**

**Definition.** The **Hermitian set** is

$$
H(n)=\bigl\{X\in\mathbb{B}_{\mathrm{r}}^{n\times n}:\ X_{0}^{\mathsf T}=X_{0},\ X_{1}^{\mathsf T}=-X_{1},\ X_{2}^{\mathsf T}=-X_{2},\ X_{3}^{\mathsf T}=-X_{3}\bigr\},
$$

where $X=X_{0}+X_{1}i+X_{2}j+X_{3}ij$ with real $X_{t}$.

**Proposition (it is a real subspace).** $H(n)$ is a real subspace of $\mathbb{B}_{\mathrm{r}}^{n\times n}$ of real dimension $2n^{2}-n$.

*Proof.* Each condition is a real-linear condition on the coefficient matrices, so the set is a real subspace. The symmetric block $X_{0}$ has $n(n+1)/2$ independent entries, and each of the three antisymmetric blocks has $n(n-1)/2$, so the dimension is $n(n+1)/2+3n(n-1)/2=2n^{2}-n$.

The set is the source's $\mathbb{H}\mathbb{Q}^{n\times n}_{R}$. Its name is the source's and does not agree with the corpus's use of Hermitian for elements, which is the star; §*The Two Complex Blocks* records the exact difference.

### The Two Complex Blocks

**In the two complex blocks of the algebra the Hermitian set is the product of the Hermitian and the skew-symmetric complex matrices.**

Write $U=X_{0}+iX_{1}$ and $V=X_{2}+iX_{3}$, so that $X=U+Vj$. The conditions of the definition read

$$
U^{\mathsf T}=\bar U,\qquad V^{\mathsf T}=-V,
$$

because $X_{0}^{\mathsf T}=X_{0}$ and $X_{1}^{\mathsf T}=-X_{1}$ are the two conditions $U^{\mathsf T}=\bar U$, and $X_{2}^{\mathsf T}=-X_{2}$ and $X_{3}^{\mathsf T}=-X_{3}$ are $V^{\mathsf T}=-V$.

| block | condition | the classical object | real dimension |
|---|---|---|---|
| $U=X_{0}+iX_{1}$ | $U^{\mathsf T}=\bar U$ | complex Hermitian matrices | $n^{2}$ |
| $V=X_{2}+iX_{3}$ | $V^{\mathsf T}=-V$ | complex skew-symmetric matrices | $n(n-1)$ |
| $X=U+Vj$ | both | the product of the two | $2n^{2}-n$ |

The two conditions are not those of the star applied entrywise and transposed: the star fixes $1$ and $ij$ and negates $i$ and $j$, so it would keep the sign of the $ij$-block and ask $X_{3}$ to be symmetric, while the source's conjugation negates all three imaginary units and asks $X_{3}$ to be skew. The difference is exactly the sign with which the $ij$-block enters the conjugation. The corpus's matrix adjoint, the bar-transpose of the Conventions, gives a third set, which differs in the $j$-block instead.

## The Half-Vectorisation

### The Symmetric and the Antisymmetric Vectorisations

**A symmetric matrix is read by its lower triangle and an antisymmetric one by its strict lower triangle, and the two readings are linear with full column rank.**

**Definition.** For $X=(x_{ij})\in\mathbb{R}^{n\times n}$ the **symmetric vectorisation** is

$$
\mathrm{vec}_{S}(X)=\bigl(x_{11},x_{21},\dots,x_{n1},x_{22},x_{32},\dots,x_{n2},\dots,x_{nn}\bigr)^{\mathsf T}\in\mathbb{R}^{n(n+1)/2},
$$

the entries on and below the diagonal, column by column, and the **antisymmetric vectorisation** is

$$
\mathrm{vec}_{A}(X)=\bigl(x_{21},x_{31},\dots,x_{n1},x_{32},\dots,x_{n2},\dots,x_{n,n-1}\bigr)^{\mathsf T}\in\mathbb{R}^{n(n-1)/2},
$$

the entries strictly below the diagonal, column by column.

**Proposition (the two readings are faithful).** For $X$ symmetric, $\mathrm{vec}(X)=K_{S}\mathrm{vec}_{S}(X)$; for $X$ antisymmetric, $\mathrm{vec}(X)=K_{A}\mathrm{vec}_{A}(X)$. The matrices $K_{S}\in\mathbb{R}^{n^{2}\times n(n+1)/2}$ and $K_{A}\in\mathbb{R}^{n^{2}\times n(n-1)/2}$ have full column rank.

*Proof.* The column of $K_{S}$ attached to $x_{ij}$ with $i\ge j$ has the unit at the position of $(i,j)$ in the vec and, when $i>j$, the unit at the position of $(j,i)$, since $x_{ji}=x_{ij}$. The column of $K_{A}$ attached to $x_{ij}$ with $i>j$ has the unit at $(i,j)$ and the negative unit at $(j,i)$, since $x_{ji}=-x_{ij}$. Distinct columns have distinct supports in the strict lower triangle, so the ranks are full.

The two encodings are the source's $K_{S}$ and $K_{A}$. They are not isometries: the column of $K_{S}$ attached to an off-diagonal entry has two units, so $K_{S}^{\mathsf T}K_{S}$ has the weight $2$ on the off-diagonal coordinates and the weight $1$ on the diagonal ones, while $K_{A}^{\mathsf T}K_{A}=2I_{n(n-1)/2}$, since every column of $K_{A}$ has one unit and one negative unit.

### The Block Diagonal

**The four blocks of a Hermitian matrix are carried by one block diagonal matrix into the row form of the real representation.**

**Definition.** The matrices

$$
Q=\operatorname{diag}\bigl(K_{S},-K_{A},K_{A},-K_{A}\bigr),\qquad R=\operatorname{diag}\bigl(K_{S},K_{A},K_{A},K_{A}\bigr)
$$

act on the **half-vectorisation**

$$
z=\bigl(\mathrm{vec}_{S}(X_{0}),\mathrm{vec}_{A}(X_{1}),\mathrm{vec}_{A}(X_{2}),\mathrm{vec}_{A}(X_{3})\bigr)^{\mathsf T}\in\mathbb{R}^{2n^{2}-n}.
$$

**Proposition (the two identities).** For $X\in H(n)$,

$$
\mathrm{vec}\bigl(X^{R}_{r}\bigr)=Qz,\qquad
\begin{pmatrix}\mathrm{vec}(X_{0})\\ \mathrm{vec}(X_{1})\\ \mathrm{vec}(X_{2})\\ \mathrm{vec}(X_{3})\end{pmatrix}=Rz .
$$

*Proof.* The row form is $X^{R}_{r}=[X_{0},-X_{1},X_{2},-X_{3}]$, and its vec is the column of the four vecs with the signs of the row form, which is $Qz$; the four vecs with positive signs are the column $Rz$.

The map $z\mapsto X$ is a linear bijection from $\mathbb{R}^{2n^{2}-n}$ onto $H(n)$, since $R$ has full column rank; this is the parametrisation that replaces the idempotent coordinates.

## The Reduction to One Real System

### The Real Representation and Its Row Form

**The real representation carries the product to the product, and the row form is the first block row.**

**Proposition.** For matrices of matching shapes over $\mathbb{B}_{\mathrm{r}}$,

$$
(MN)^{R}=M^{R}N^{R},\qquad (MN)^{R}_{r}=M^{R}_{r}N^{R},\qquad \|M\|_{\mathrm F}=\tfrac12\|M^{R}\|_{\mathrm F}=\|M^{R}_{r}\|_{\mathrm F}.
$$

*Proof.* The real representation is the left multiplication on the four real coordinates, so it is multiplicative; the row form is its first block row, and the first block row of a product is the first block row of the left factor times the right factor. Each coefficient of $M$ occurs in four blocks of $M^{R}$ and once in $M^{R}_{r}$, whence the two norm identities.

The propositions are the source's Lemma 2.1 and its identity (4); the real representation is that of *Least Squares and Total Least Squares over the Reduced Biquaternions*.

### The Signed Selection

**The full real representation and its row form carry the same information, and the passage between them is a signed selection.**

**Proposition.** There is a matrix $J$ with entries in $\{0,\pm1\}$, depending on $n$ and on nothing else, with exactly one nonzero in each row and four in each column, such that

$$
\mathrm{vec}\bigl(X^{R}\bigr)=J\,\mathrm{vec}\bigl(X^{R}_{r}\bigr).
$$

*Proof.* Each entry of $X^{R}$ is one entry of one of the four blocks of $X$ with a sign, and that entry occurs in the row form, at one position and with a sign; every entry of $X^{R}$ therefore reads one coordinate of the row form, and every coordinate of the row form occurs in four entries of $X^{R}$, so the map is linear with one nonzero in each row and four in each column.

The matrix is the source's $J$ of its equation (6). It is a selection and not a permutation: each coordinate of the row form occurs in four entries of $X^{R}$, so $J$ has one nonzero in each row and four in each column.

### The Stacked Residual

**The two residuals become one real system in the half-vectorisation.**

**Definition.** Put

$$
P=\begin{pmatrix}(B^{R})^{\mathsf T}\otimes A^{R}_{r}\\[2pt](D^{R})^{\mathsf T}\otimes C^{R}_{r}\end{pmatrix}\in\mathbb{R}^{8ms\times 16n^{2}},\qquad t=\begin{pmatrix}\mathrm{vec}\bigl(E^{R}_{r}\bigr)\\[2pt]\mathrm{vec}\bigl(F^{R}_{r}\bigr)\end{pmatrix}\in\mathbb{R}^{8ms}.
$$

**Theorem (the residual identity).** For every $X\in H(n)$, with $z$ its half-vectorisation,

$$
\|(AXB-E,CXD-F)\|_{\mathrm F}^{2}=\|PJQz-t\|^{2}.
$$

*Proof.* By the norm identity and the multiplicativity of the row form,

$$
\|AXB-E\|_{\mathrm F}^{2}=\bigl\|A^{R}_{r}X^{R}B^{R}-E^{R}_{r}\bigr\|_{\mathrm F}^{2}=\bigl\|P_{1}\mathrm{vec}(X^{R})-\mathrm{vec}(E^{R}_{r})\bigr\|^{2}
$$

with $P_{1}=(B^{R})^{\mathsf T}\otimes A^{R}_{r}$, and likewise for the second residual with $P_{2}=(D^{R})^{\mathsf T}\otimes C^{R}_{r}$. Stacking the two gives $P\mathrm{vec}(X^{R})-t$, and $\mathrm{vec}(X^{R})=JQz$ for $X\in H(n)$ by the two propositions above.

The identity is the source's reduction: the constrained problem in $X$ is the unconstrained least squares problem in $z$.

### The Least-Norm Solution

**The least squares set is the set whose four vecs are $R$ applied to the affine set of least squares solutions of $PJQz=t$, and the least-norm element in the coordinates is the pseudoinverse solution.**

**Theorem (the least squares set).** The set $H_{LE}$ of least squares solutions of the pair in $H(n)$ is the set of $X\in H(n)$ for which

$$
\begin{pmatrix}\mathrm{vec}(X_{0})\\ \mathrm{vec}(X_{1})\\ \mathrm{vec}(X_{2})\\ \mathrm{vec}(X_{3})\end{pmatrix}
=R\Bigl((PJQ)_{\mathrm{MP}}\,t+\bigl(I_{2n^{2}-n}-(PJQ)_{\mathrm{MP}}(PJQ)\bigr)y\Bigr)
$$

for some $y\in\mathbb{R}^{2n^{2}-n}$.

The element whose four vecs are the column $R(PJQ)_{\mathrm{MP}}t$ is the one of least coordinate norm $\|z\|$.

*Proof.* The least squares solutions of $Mz=t$ over the real vector space are $M_{\mathrm{MP}}t+(I-M_{\mathrm{MP}}M)y$ with $y$ arbitrary, by the classical lemma of the source, and $M_{\mathrm{MP}}t$ is the one of least $\|z\|$. The map $z\mapsto X$ defined by the four vecs $Rz$ is a linear bijection onto $H(n)$, so the image is the stated set.

The theorem is the source's Theorem 3.1. The selection of the least-norm element is in the coordinates $z$, and §*The Norm of the Coordinates* records what that means for the Frobenius norm of $X$.

### Consistency

**The pair has a Hermitian solution exactly when the right-hand side lies in the range of $PJQ$.**

**Theorem (the consistency criterion).** The pair equation has a solution in $H(n)$ if and only if

$$
\bigl(I_{8ms}-(PJQ)(PJQ)_{\mathrm{MP}}\bigr)t=0,
$$

and then the residual is zero and the solution set is that of the preceding theorem.

*Proof.* The system $Mz=t$ is solvable exactly when $MM_{\mathrm{MP}}t=t$, and the projection $MM_{\mathrm{MP}}$ is the orthogonal projector onto the range of $M$; the residual is zero exactly then, and the Hermitian solutions are the preimages under $R$ of the solutions.

### Uniqueness

**The Hermitian solution is unique exactly when the reduced system has full column rank.**

**Theorem (the uniqueness criterion).** When the consistency criterion holds, the pair has exactly one solution in $H(n)$ if and only if

$$
\operatorname{rank}(PJQ)=2n^{2}-n,
$$

and then it is the matrix whose four vecs are the column $R(PJQ)_{\mathrm{MP}}t$.

*Proof.* The affine set of solutions of $Mz=t$ is a single point exactly when $M$ has full column rank, and the number of columns is $2n^{2}-n$; $R$ is injective, so the preimage is a single point exactly then.

The two theorems are the source's Theorem 3.2, with the Moore–Penrose inverse written $M_{\mathrm{MP}}$ in the corpus's glyph and the dagger kept for the adjoint.

### The Norm of the Coordinates

**The pseudoinverse minimises the norm of $z$, and the Frobenius norm of $X$ is a weighted norm of $z$, so the two selections need not coincide when the least squares set is not a point.**

**Proposition.** $R^{\mathsf T}R=\operatorname{diag}(w)$ with $w=1$ on the diagonal coordinates of $\mathrm{vec}_{S}$ and $w=2$ on every other coordinate; consequently $\|X\|_{\mathrm F}^{2}=z^{\mathsf T}R^{\mathsf T}Rz$, and for $n\ge2$ this is not $\|z\|^{2}$.

*Proof.* The column of $K_{S}$ attached to an off-diagonal entry has two units and the other columns have one, so $K_{S}^{\mathsf T}K_{S}$ has the diagonal $1$ and $2$ as stated; $K_{A}^{\mathsf T}K_{A}=2I$, every column of $K_{A}$ having one unit and one negative unit; the blocks of $R$ are $K_{S}$ and three copies of $K_{A}$, whence the diagonal of $R^{\mathsf T}R$. Then $\|X\|_{\mathrm F}^{2}=\|Rz\|^{2}=z^{\mathsf T}R^{\mathsf T}Rz$.

**Remark (what the source selects).** The point whose four vecs are $R(PJQ)_{\mathrm{MP}}t$ minimises $z^{\mathsf T}z$ over the least squares set, while the minimiser of $\|X\|_{\mathrm F}$ over the same set minimises $z^{\mathsf T}R^{\mathsf T}Rz$; the two coincide exactly when $R^{\mathsf T}Rz_{0}$ is orthogonal to the kernel of $PJQ$, and in particular when that kernel is supported on the diagonal coordinates of $X_{0}$. The consistency and uniqueness criteria are unaffected, and when the solution is unique the two points coincide. The source's Problem 3.1 asks for the minimum of $\|X\|_{\mathrm F}$, so its Theorem 3.1 returns the requested element exactly when the two points coincide. The verification records a rank-deficient instance of the pair on which the two differ.

## The Idempotent Coordinates

### The Coupled Equations

**In the idempotent coordinates the Hermitian condition is two equations coupling the two coordinates, not one condition on each.**

**Proposition.** With $q_{1}=U+V$ and $q_{2}=U-V$ the complex idempotent coordinates of $X=U+Vj$, the condition $X\in H(n)$ is equivalent to

$$
q_{1}^{\mathsf T}+q_{1}=q_{2}^{\mathsf T}+q_{2},\qquad q_{1}^{\mathsf T}+q_{2}^{\mathsf T}=\bar q_{1}+\bar q_{2}.
$$

*Proof.* The first equation is $2V^{\mathsf T}=-2V$ and the second is $2U^{\mathsf T}=2\bar U$, by $U=(q_{1}+q_{2})/2$ and $V=(q_{1}-q_{2})/2$ and the two block conditions. The first equates the symmetric parts of the two coordinates, and the second ties their transposes to their conjugates; neither constrains $q_{1}$ alone, so the two coordinates are coupled.

### The Structure Is Not of Entry Type

**The Hermitian set is not a module over the algebra, so the idempotent reduction and the theorem for structures of entry type do not apply to it.**

**Proposition.** $iH(n)\cap H(n)$ is the set of matrices $X=X_{2}j$ with $X_{2}$ antisymmetric, and $jH(n)\cap H(n)$ is the set of matrices $X=X_{1}i+X_{3}ij$ with $X_{1}$ and $X_{3}$ antisymmetric; in particular $iH(n)\not\subset H(n)$ and $jH(n)\not\subset H(n)$.

*Proof.* Multiplying $X=X_{0}+X_{1}i+X_{2}j+X_{3}ij$ by $i$ gives $iX=-X_{1}+X_{0}i-X_{3}j+X_{2}ij$. Its blocks must satisfy the conditions of $H(n)$: $-X_{1}$ symmetric forces $X_{1}=0$, because $X_{1}$ is antisymmetric; $X_{0}$ antisymmetric forces $X_{0}=0$, because $X_{0}$ is symmetric; $-X_{3}$ symmetric forces $X_{3}=0$; and $X_{2}$ antisymmetric holds automatically. Multiplying by $j$ gives $jX=X_{2}+X_{3}i+X_{0}j+X_{1}ij$, and the conditions force $X_{2}=0$ and $X_{0}=0$, the conditions on $X_{1}$ and $X_{3}$ holding automatically.

**Corollary.** $H(n)$ is not a $\mathbb{B}_{\mathrm{r}}$-submodule of $\mathbb{B}_{\mathrm{r}}^{n\times n}$; in particular it is not of entry type, and the reduction to two independent complex problems is unavailable.

*Proof.* A structure of entry type is the $\mathbb{B}_{\mathrm{r}}$-span of real zero-one matrices, so it is a module, and a module is closed under multiplication by $i$ and by $j$. The set $H(n)$ is not, so it is not of entry type. Its real dimension is $2n^{2}-n$, which is a multiple of four exactly when $n\equiv0\pmod 4$; the dimension alone does not decide the question at $n=4$, where it is $28$, and the module argument decides it for every $n$.

The corollary is the reason the source needs the real representation and the half-vectorisation: the reduction through the idempotents is unavailable, and the constraint must be encoded on the real coordinates.

## The Complex Field

### The Degenerate Data

**The complex matrices are the reduced biquaternion matrices with vanishing $j$- and $ij$-blocks, and the complex pair is the degenerate case of the construction.**

**Proposition.** Let $A,C\in\mathbb{C}^{m\times n}$, $B,D\in\mathbb{C}^{n\times s}$ and $E,F\in\mathbb{C}^{m\times s}$, read in $\mathbb{B}_{\mathrm{r}}$ with the second and third blocks of all six matrices vanishing. Then the pair over $\mathbb{B}_{\mathrm{r}}$ has a Hermitian solution in the complex subspace if and only if the complex pair has a Hermitian solution, and the Hermitian unknown is $X=X_{0}+iX_{1}$ with $X_{0}$ symmetric and $X_{1}$ antisymmetric.

*Proof.* The blocks $2$ and $3$ of every coefficient and of every right-hand side vanish, so the blocks $2$ and $3$ of both residuals vanish for every $X$ with $X_{2}=X_{3}=0$; the two remaining block equations are the real and the imaginary parts of the complex pair. The Hermitian condition on $X$ is the two conditions on $X_{0}$ and $X_{1}$ of §*The Two Complex Blocks*.

### The Encodings and the Unknowns

**The complex case keeps two blocks instead of four, and the number of unknowns is $n^{2}$.**

**Proposition.** In the complex case the half-vectorisation is $z=(\mathrm{vec}_{S}(X_{0}),\mathrm{vec}_{A}(X_{1}))^{\mathsf T}$, of length $n^{2}$, and the reduction is that of §*The Reduction to One Real System* with

$$
\tilde Q=\operatorname{diag}\bigl(K_{S},-K_{A}\bigr),\qquad \tilde R=\operatorname{diag}\bigl(K_{S},K_{A}\bigr),
$$

the matrices $\tilde P$ and $\tilde J$ built from the two-block real representation $\tilde M^{R}=\begin{pmatrix}M_{0}&-M_{1}\\ M_{1}&M_{0}\end{pmatrix}$ and the row form $\tilde M^{R}_{r}=[M_{0},-M_{1}]$.

*Proof.* The unknown has two real blocks, $X_{0}$ symmetric and $X_{1}$ antisymmetric, so the half-vectorisation has $n(n+1)/2+n(n-1)/2=n^{2}$ coordinates. The row form of the two-block representation is $[X_{0},-X_{1}]$, and the rest of the construction is the same with two blocks in place of four.

The complex theorems are the source's Theorems 4.1 and 4.2, with the consistency criterion and the uniqueness criterion $\operatorname{rank}(\tilde P\tilde J\tilde Q)=n^{2}$.

## The Hermitian Partial Inverse Eigenvalue Problem

### The Problem

**The partial inverse eigenvalue problem prescribes part of the spectrum and asks for a Hermitian matrix carrying it.**

**Problem.** Given $\Lambda=\operatorname{diag}(\lambda_{1},\dots,\lambda_{k})\in\mathbb{R}^{k\times k}$ and $\Phi=[u_{1},\dots,u_{k}]\in\mathbb{C}^{n\times k}$ with $k\le n$, find a Hermitian $M\in\mathbb{C}^{n\times n}$ with

$$
M\Phi=\Phi\Lambda .
$$

The columns of $\Phi$ are the prescribed eigenvectors and the diagonal entries of $\Lambda$ the prescribed eigenvalues.

### The Criterion

**The problem is the complex pair with $A=I_{n}$ and one equation, and its solvability is the range condition of the reduced system.**

**Proposition.** The problem is the case $A=I_{n}$, $C=D=0$, $B=\Phi$, $E=\Phi\Lambda$, $F=0$ of the complex problem, and it is solvable exactly when

$$
\operatorname{rank}(N)=\operatorname{rank}\bigl([N,t]\bigr),
$$

where $\tilde S=(\tilde\Phi^{R})^{\mathsf T}\otimes[I_{n},0]$ is the coefficient matrix of the single equation, $[I_{n},0]$ being the row form of $\tilde I_{n}$, $N=\tilde S\tilde J\tilde Q$ and $t=\mathrm{vec}(\tilde E^{R}_{r})$ with $\tilde E=\Phi\Lambda$.

*Proof.* Substituting these matrices into the complex pair leaves the single equation $M\Phi=\Phi\Lambda$; the reduction of §*The Encodings and the Unknowns* applies, and a linear system is solvable exactly when the rank of its matrix equals the rank of the matrix augmented by the right-hand side.

The criterion is the source's Corollary 4.3.

### Non-Uniqueness

**The prescribed data need not determine the matrix, and the general solution carries an arbitrary vector.**

**Proposition.** When the criterion holds, the general solution is

$$
\begin{pmatrix}\mathrm{vec}(M_{0})\\ \mathrm{vec}(M_{1})\end{pmatrix}=\tilde R\Bigl((N)_{\mathrm{MP}}\,t+\bigl(I_{n^{2}}-(N)_{\mathrm{MP}}N\bigr)y\Bigr),
$$

with $y\in\mathbb{R}^{n^{2}}$ arbitrary, and $M$ is unique exactly when $\operatorname{rank}(N)=n^{2}$.

*Proof.* The general solution of a consistent linear system is the sum of a particular solution and an arbitrary element of the kernel, and the parametrisation by $\tilde R$ is injective. The source's Remark 4.4 records the non-uniqueness in the same terms.

## Verification

The following identities were checked by exact recomputation with rational arithmetic on matrices of at most three rows and columns, and on one hundred random instances where an instance count is stated.

- The real representation is multiplicative, $(MN)^{R}=M^{R}N^{R}$ and $(MN)^{R}_{r}=M^{R}_{r}N^{R}$, and $\|M\|_{\mathrm F}=\tfrac12\|M^{R}\|_{\mathrm F}=\|M^{R}_{r}\|_{\mathrm F}$.
- The signed selection: $\mathrm{vec}(X^{R})=J\,\mathrm{vec}(X^{R}_{r})$ for $n=2,3$, with $J$ built from the basis, independent of $X$, and with one nonzero in each row and four in each column.
- The residual identity $\|(AXB-E,CXD-F)\|_{\mathrm F}^{2}=\|PJQz-t\|^{2}$ for $n=2,3$ and several shapes of $A,B$.
- The parametrisation $\mathrm{vec}(X^{R}_{r})=Qz$ and the four vecs $\mathrm{vec}(X_{0}),\mathrm{vec}(X_{1}),\mathrm{vec}(X_{2}),\mathrm{vec}(X_{3})$ equal to $Rz$, on one hundred random Hermitian matrices for $n=2,3$.
- The recovery: on sixty consistent instances with $\operatorname{rank}(PJQ)=2n^{2}-n=6$, the solution of the reduced system reproduces the prescribed Hermitian $X$ exactly.
- The weights $R^{\mathsf T}R$: the diagonal is $1$ on the diagonal coordinates of $\mathrm{vec}_{S}$ and $2$ on every other coordinate.
- The non-closure: on one hundred random Hermitian matrices for $n=2,3$, $iX$ and $jX$ are Hermitian in none of the instances, and the exact intersections $X_{0}=X_{1}=X_{3}=0$ for $i$ and $X_{0}=X_{2}=0$ for $j$ hold in every instance.
- The coupled idempotent equations hold on one hundred random Hermitian matrices.
- The norm selection: on a consistent rank-deficient instance of the pair with $A=C$, $B=D$, $E=F$ and $\operatorname{rank}(PJQ)=4$, the two free directions separate the selections, the source's point having $\|X\|_{\mathrm F}^{2}=486/25$ against $58/3$ for the Frobenius minimiser.

Two statements are the source's and were not recomputed here: the efficiency comparison of the real and the complex representations, and the numerical examples of the source's §5 that report it.

## Summary

The pair equation $(AXB,CXD)=(E,F)$ over the reduced biquaternions imposes two equations on one unknown, and the unknown is taken in the Hermitian set $H(n)$ of the source, the set of matrices fixed by the transpose composed with the conjugation negating the three imaginary units. That conjugation is an involution and is not multiplicative, and the set is not the corpus's Hermitian plane, which is the fixed set of the star; in the two complex blocks the set is the product of the Hermitian and the skew-symmetric complex matrices, $U^{\mathsf T}=\bar U$ and $V^{\mathsf T}=-V$, of real dimension $2n^{2}-n$. The set is not closed under multiplication by $i$ or by $j$, so it is not a module over the algebra and not a structure of entry type, and the idempotent reduction of the sibling articles does not apply; in the idempotent coordinates the condition is the two coupled equations $q_{1}^{\mathsf T}+q_{1}=q_{2}^{\mathsf T}+q_{2}$ and $q_{1}^{\mathsf T}+q_{2}^{\mathsf T}=\bar q_{1}+\bar q_{2}$. The replacement is the real representation, whose row form carries the product, together with the half-vectorisation of the symmetric and the antisymmetric blocks; the signed selection $J$ passes from the row form to the full real representation, and the block diagonals $Q$ and $R$ carry the compressed coordinates $z$ to the row form and to the four blocks. The residual is then $\|PJQz-t\|^{2}$, the least squares set is the set of Hermitian matrices whose four vecs are $R$ applied to the affine set of least squares solutions, the pair is solvable exactly when the residual of $t$ against the projector of $PJQ$ vanishes, and the solution is unique exactly when $\operatorname{rank}(PJQ)=2n^{2}-n$. The complex field is the degenerate case with two blocks and $n^{2}$ unknowns, and the Hermitian partial inverse eigenvalue problem is the complex case $A=I_{n}$, $C=D=0$, $B=\Phi$, $E=\Phi\Lambda$, $F=0$, solvable under the rank condition $\operatorname{rank}(N)=\operatorname{rank}([N,t])$ and not unique in general. The one correction the corpus records is the selection of the least-norm element: the pseudoinverse minimises the coordinate norm, and the Frobenius norm of $X$ is a weighted coordinate norm with the weight $2$ on every coordinate other than the diagonal of $X_{0}$, so the two selections need not coincide when the least squares set is not a point.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(AXB,CXD)=(E,F)$ | The pair equation, two equations on one unknown $X$ |
| $H(n)$ | The Hermitian set of the source, real dimension $2n^{2}-n$ |
| $U=X_{0}+iX_{1}$, $V=X_{2}+iX_{3}$ | The two complex blocks of $X=U+Vj$ |
| $\mathrm{vec}_{S}$, $\mathrm{vec}_{A}$ | The symmetric and the antisymmetric vectorisations |
| $K_{S}$, $K_{A}$ | The encodings of the two vectorisations, of full column rank |
| $z$ | The half-vectorisation $(\mathrm{vec}_{S}X_{0},\mathrm{vec}_{A}X_{1},\mathrm{vec}_{A}X_{2},\mathrm{vec}_{A}X_{3})^{\mathsf T}$ |
| $Q$ | $\operatorname{diag}(K_{S},-K_{A},K_{A},-K_{A})$, the map $z\mapsto\mathrm{vec}(X^{R}_{r})$ |
| $R$ | $\operatorname{diag}(K_{S},K_{A},K_{A},K_{A})$, the map $z\mapsto(\mathrm{vec}(X_{0}),\mathrm{vec}(X_{1}),\mathrm{vec}(X_{2}),\mathrm{vec}(X_{3}))^{\mathsf T}$ |
| $M^{R}$, $M^{R}_{r}$ | The real representation and its row form $[M_{0},-M_{1},M_{2},-M_{3}]$ |
| $J$ | The signed selection $\mathrm{vec}(X^{R})=J\,\mathrm{vec}(X^{R}_{r})$ |
| $P$ | $\begin{pmatrix}(B^{R})^{\mathsf T}\otimes A^{R}_{r}\\ (D^{R})^{\mathsf T}\otimes C^{R}_{r}\end{pmatrix}$, the stacked coefficient matrix |
| $t$ | $(\mathrm{vec}(E^{R}_{r}),\mathrm{vec}(F^{R}_{r}))^{\mathsf T}$ |
| $M_{\mathrm{MP}}$ | The Moore–Penrose inverse |
| $\operatorname{rank}$, $\operatorname{diag}$ | The rank, and the block diagonal matrix |
| $\tilde Q,\tilde R,\tilde P,\tilde S,\tilde J$ | The complex versions of the encodings, of the selection and of the coefficient matrices |
| $\Lambda$, $\Phi$ | The prescribed eigenvalues and eigenvectors |

## Further Reading

- Sk. Safique Ahmad and Neha Bhadala, "Special least squares solutions of the reduced biquaternion matrix equation with applications", arXiv:2311.06472 [math.NA] (2023), the source of this article, for the pair equation $(AXB,CXD)=(E,F)$, the Hermitian set, the real representation and the signed selection $J$, the vectorisations and the encodings $K_{S}$ and $K_{A}$, the least squares set, the consistency and uniqueness criteria, the complex case, the Hermitian partial inverse eigenvalue problem and the numerical examples.
- Sk. Safique Ahmad and Neha Bhadala, "Algebraic technique for mixed least squares and total least squares problem in the reduced biquaternion algebra", arXiv:2311.06464 [math.NA] (2023), for the real representation and its rank lemma over the reduced biquaternions.
- Sk. Safique Ahmad and Neha Bhadala, "L-structure least squares solutions of reduced biquaternion matrix equations with applications", arXiv:2311.06461 [math.NA] (2023), for the L-structures and the partial inverse eigenvalue problem over the reduced biquaternions.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd edition (Cambridge University Press, 2013), for the complex Hermitian and skew-symmetric matrices, the Moore–Penrose inverse and the orthogonal projectors.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013), for the Kronecker product, the vec identity, the singular value decomposition and the pseudoinverse.
- *Least Squares and Total Least Squares over the Reduced Biquaternions* (`articles_maths/least-squares-and-total-least-squares-over-the-reduced-biquaternions.md`), for the real representation, the Frobenius norm, the adjoint, the Moore–Penrose inverse and the idempotent reduction this article does not use.
- *Matrix Equations and Structured Solutions over the Reduced Biquaternions* (`articles_maths/matrix-equations-and-structured-solutions-over-the-reduced-biquaternions.md`), for the L-structure, the structures of entry type and the partial inverse eigenvalue problem in the general form.
- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), for the algebra, the idempotents and the coordinates.
- *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), for the bar, the natural sign, the star and the flat, and the Klein four-group the source's conjugation is outside of.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the form $\langle\cdot,\cdot\rangle_{\natural*}$ and the Frobenius norm.
- *The Group of Units of the Algebra of the Reduced Biquaternions* (`articles_maths/the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the Hermitian plane $\mathbb{R}\{1,ij\}$, which is the corpus's Hermitian plane and not the set $H(n)$.
