# __Least Squares and Total Least Squares over the Reduced Biquaternions__

## Introduction

The approximation of an inconsistent linear system by a solvable one is the least squares problem, and its two refinements are the total least squares problem, in which the data matrix as well as the right-hand side is allowed to be wrong, and the mixed problem, in which only some of the columns of the data matrix are wrong. This article reads the three problems over the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, where the system is

$$
AX\approx B,\qquad A\in\mathbb{B}_{\mathrm{r}}^{m\times n},\quad B\in\mathbb{B}_{\mathrm{r}}^{m\times d},\quad m\ge n+d,
$$

and where the residual and the perturbations are measured by the positive definite norm $\langle\cdot\rangle_{\mathrm{ts}*}$ of the four products. The least squares problem minimises the size of the residual $AX-B$; the total least squares problem perturbs both $A$ and $B$ by the smallest amount that makes the system consistent; the mixed problem perturbs $B$ and a prescribed block of the columns of $A$ while leaving the rest exact.

The reason the commutative algebra makes these problems tractable is the idempotent decomposition. The algebra is the direct product $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$, every matrix over it is a pair of complex matrices, the multiplication is componentwise, and the norm $\langle\cdot\rangle_{\mathrm{ts}*}$ is the sum of the two squared complex Frobenius norms, up to the factor $\tfrac12$. The consequence is that each of the three problems splits into two problems over the complex field, solved independently and in parallel. The reduced biquaternion least squares solution is the pair of the two complex least squares solutions; the reduced biquaternion total least squares solution is the pair of the two complex total least squares solutions; and the same holds for the mixed problem. No coupling term survives.

The coupling appears only through the unknown. If $X$ is an arbitrary reduced biquaternion matrix, the two complex problems are independent; if $X$ is a complex matrix, the same complex unknown must serve in both; if $X$ is a real matrix, the same real unknown must serve in both. The three cases are nested, and the third is the one treated in the source of this article, Ahmad and Bhadala, whose real representation is the price paid for excluding complex and reduced biquaternion unknowns. The article states the three problems, proves the reduction, identifies the metric that makes the reduction a Hilbert-space statement, records the adjoint and the Moore–Penrose inverse it produces, presents the real representation and the algorithm of the source as the real case, and collects the conditions for existence and uniqueness. A final remark observes a phenomenon absent from the division-algebra layers: the least squares solution can be a zero divisor.

**Boundaries.** The algebra, its idempotents and the coordinates are *Reduced Biquaternion Space* and *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*. The form $\langle\cdot\rangle_{\mathrm{ts}*}$ and the algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms*; the involution and the adjoint are *The Two Involutions and the Group of Involutions*. The array representation $M_{m\times n}(\mathbb{B}_{\mathrm{r}})\cong M_{m\times n}(\mathbb{C})\times M_{m\times n}(\mathbb{C})$ is *Reduced Biquaternion Other Algebraic Element Representations*; the objects and their matrices are *Reduced Biquaternion Objects and their Matrix Correspondences*. The spectrum and the singular values are *Reduced Biquaternion Spectral Theory*; the singular values as a general tool are *Compact Operators*. The least squares problem in the non-commutative quaternion statistics is *Quaternion Augmented Statistics*; the non-commutative companion of the matrix dictionary is *Biquaternion Objects and Their Matrix Correspondences*.

**Conventions.** The element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, and the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so that $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$. The conjugations are the bar $\bar{\cdot}$, the tessarine sign ${}_{\mathrm{ts}}$ and the star ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$, and the form and the norm of the tessarine sesquilinear product are

$$
\langle\breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\mathrm{Sc}\bigl(\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}\bigr)=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},\qquad \langle\breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}=\tfrac12\bigl(|Q_{+}|^{2}+|Q_{-}|^{2}\bigr).
$$

For matrices the form is read entrywise, $K_{\mathrm F}(M,N)=\sum_{r,s}\langle M_{rs},N_{rs}\rangle_{\mathrm{ts}*}$, and $K_{\mathrm F}(M)=K_{\mathrm F}(M,M)$; it is the square of the Frobenius norm the source writes $\lVert M\rVert_{F}$. The two **idempotent components** of a matrix are the pair $(M^{+},M^{-})$ of *Reduced Biquaternion Other Algebraic Element Representations*, read entrywise, $(M^{\pm})_{rs}=\lambda_{\pm}(M_{rs})$ with $\lambda_{+}(\breve Q)=Q_{+}$ and $\lambda_{-}(\breve Q)=Q_{-}$ the two characters; the component $M^{+}$ is the one attached to $\Pi_+$ and $M^{-}$ the one attached to $\Pi_-$. The $\langle\cdot\rangle_{\mathrm{ts}*}$-**adjoint** of a matrix is written $M^{\dagger}$, in agreement with the dagger of the operator conventions, and the **Moore–Penrose inverse** is written $M_{\mathrm{MP}}$, the dagger marking the adjoint and the sign marking a component, so neither is read for the other.

## The Three Approximation Problems

### The Definitions

**Definition (the least squares problem).** Given $A$ and $B$, the **reduced biquaternion least squares problem** is

$$
\min_{X\in\mathbb{B}_{\mathrm{r}}^{n\times d}}K_{\mathrm F}(AX-B),
$$

and any minimiser $X$ is a **least squares solution**. The minimum measures the residual that no $X$ can remove.

**Definition (the total least squares problem).** Given $A$ and $B$, the **reduced biquaternion total least squares problem** is

$$
\min_{X,E,G}K_{\mathrm F}\bigl([E,G]\bigr)\quad\text{subject to}\quad (A+E)X=B+G,
$$

where $E\in\mathbb{B}_{\mathrm{r}}^{m\times n}$ and $G\in\mathbb{B}_{\mathrm{r}}^{m\times d}$, and $[E,G]$ is the horizontal concatenation. Any $X$ of a minimising triple is a **total least squares solution**. The minimum is the smallest perturbation of the pair $(A,B)$ that makes the system consistent.

**Definition (the mixed problem).** Partition $A=[A_{a},A_{b}]$ into its first $n_{1}$ columns $A_{a}$ and its last $n_{2}$ columns $A_{b}$, with $n_{1}+n_{2}=n$, and partition $X$ by rows accordingly, $X=\begin{pmatrix}X_{a}\\ X_{b}\end{pmatrix}$. The **reduced biquaternion mixed least squares and total least squares problem** is

$$
\min_{X_{a},X_{b},E_{b},G}K_{\mathrm F}\bigl([E_{b},G]\bigr)\quad\text{subject to}\quad A_{a}X_{a}+(A_{b}+E_{b})X_{b}=B+G,
$$

with $E_{b}\in\mathbb{B}_{\mathrm{r}}^{m\times n_{2}}$; any $X$ of a minimising tuple is a **mixed solution**. The columns $A_{a}$ are held exact and only $A_{b}$ and $B$ are perturbed.

### The One Parameter

**Remark (the parameter interpolates).** The mixed problem contains the other two. For $n_{1}=0$ every column of $A$ is perturbed, $A_{a}$ is empty, and the problem is the total least squares problem; for $n_{1}=n$ no column of $A$ is perturbed, $A_{b}$ is empty, and the problem is the least squares problem.

The three problems are therefore the three values of one parameter, the number $n_{1}$ of exact columns.

| problem | perturbed | held exact | the parameter |
|---|---|---|---|
| least squares | $B$ | $A$ | $n_{1}=n$ |
| total least squares | $A,B$ | none | $n_{1}=0$ |
| mixed | $A_{b},B$ | $A_{a}$ | $0<n_{1}<n$ |

## The Idempotent Reduction

### The Two Coordinates of a Matrix

Each entry of a matrix over $\mathbb{B}_{\mathrm{r}}$ has two idempotent coordinates, and applying the coordinates entrywise splits the matrix.

**Definition.** Write $M=M_{0}+M_{1}i+M_{2}j+M_{3}ij$ with real matrices $M_{0},M_{1},M_{2},M_{3}$. The **idempotent components** of $M$ are the complex matrices

$$
M^{+}=M_{0}+M_{2}+i(M_{1}+M_{3}),\qquad M^{-}=M_{0}-M_{2}+i(M_{1}-M_{3}).
$$

**Proposition (the array isomorphism).** The map $M\mapsto(M^{+},M^{-})$ is an isomorphism of rings

$$
M_{m\times n}(\mathbb{B}_{\mathrm{r}})\longrightarrow M_{m\times n}(\mathbb{C})\times M_{m\times n}(\mathbb{C}),
$$

and $M=M^{+}\Pi_++M^{-}\Pi_-$ with the identity and the zero of the pair the identity and the zero matrices.

*Proof.* The idempotent coordinates of an entry are the two characters, and applying them entrywise is an algebra homomorphism on the matrices because the multiplication of the algebra is componentwise and the matrices multiply entrywise in the two components; the displayed decomposition is the entrywise form of $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$. The inverse reads the four real blocks from the real and imaginary parts, $M_{0}=\tfrac12\operatorname{Re}(M^{+}+M^{-})$, $M_{1}=\tfrac12\operatorname{Im}(M^{+}+M^{-})$, $M_{2}=\tfrac12\operatorname{Re}(M^{+}-M^{-})$ and $M_{3}=\tfrac12\operatorname{Im}(M^{+}-M^{-})$.

This is the array representation of *Reduced Biquaternion Other Algebraic Element Representations*, applied to a rectangular matrix and read column by column.

### The Multiplication Decouples

**Theorem (the multiplication is componentwise).** For $M\in\mathbb{B}_{\mathrm{r}}^{m\times p}$ and $N\in\mathbb{B}_{\mathrm{r}}^{p\times n}$,

$$
(MN)^{+}=M^{+}N^{+},\qquad (MN)^{-}=M^{-}N^{-}.
$$

*Proof.* Write $M=M^{+}\Pi_++M^{-}\Pi_-$ and $N=N^{+}\Pi_++N^{-}\Pi_-$; multiplying with $\Pi_+^{2}=\Pi_+$, $\Pi_-^{2}=\Pi_-$ and $\Pi_+\Pi_-=\Pi_-\Pi_+=0$ gives $MN=M^{+}N^{+}\Pi_++M^{-}N^{-}\Pi_-$, and the components are read off. Equivalently, the entrywise multiplication of the four real coefficient blocks is exactly the two complex matrix products of the components.

The theorem is the reason every linear-algebraic problem over $\mathbb{B}_{\mathrm{r}}$ decouples: it is a statement about the algebra, not about the problem.

### The Metric Splits

The form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is the one that makes the reduction a metric statement, because it is the sum of the two complex quadratic forms.

**Definition.** The **matrix form of $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$** is the entrywise sum

$$
K_{\mathrm F}(M,N)=\sum_{r=1}^{m}\sum_{s=1}^{n}\langle M_{rs},N_{rs}\rangle_{\mathrm{ts}*},
$$

with matrix norm $K_{\mathrm F}(M)=K_{\mathrm F}(M,M)$. Its real part is a real inner product on $\mathbb{B}_{\mathrm{r}}^{m\times n}$, read on the $4mn$ real coefficients.

**Theorem (the metric splits).** Let $M=M_{0}+M_{1}i+M_{2}j+M_{3}ij$. Then

$$
K_{\mathrm F}(M)=\sum_{t=0}^{3}\lVert M_{t}\rVert_{F}^{2}=\tfrac12\Bigl(\bigl\lVert M^{+}\bigr\rVert_{F}^{2}+\bigl\lVert M^{-}\bigr\rVert_{F}^{2}\Bigr),
$$

and likewise $K_{\mathrm F}(M,N)=\sum_{t}\langle M_{t},N_{t}\rangle_{F}=\tfrac12\bigl(\langle M^{+},N^{+}\rangle_{F}+\langle M^{-},N^{-}\rangle_{F}\bigr)$, the real inner product of the coefficients being the Euclidean one in each reading.

*Proof.* The norm $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}=q_{\blacktriangle}^{2}+q'^{2}_{\blacktriangle}+q_{\blacktriangledown}^{2}+q'^{2}_{\blacktriangledown}$ is the sum of the four squares of the real coordinates, whence the first equality on summing over the entries. For the second, $|Q_{+}|^{2}+|Q_{-}|^{2}=2(|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2})$ by the identity $|Q_{\blacktriangle}+Q_{\blacktriangledown}|^{2}+|Q_{\blacktriangle}-Q_{\blacktriangledown}|^{2}=2|Q_{\blacktriangle}|^{2}+2|Q_{\blacktriangledown}|^{2}$, and $K=\tfrac12(|Q_{+}|^{2}+|Q_{-}|^{2})$; summing the two coordinatewise Frobenius norms gives the result. The form case is the polarisation of the norm case.

**Corollary (the square of the real Frobenius norm).** With $\lVert M\rVert_{F}:=\sqrt{K_{\mathrm F}(M)}$ the Frobenius norm of the source, $\lVert M\rVert_{F}=\tfrac12\lVert M^{R}\rVert_{F}$, where $M^{R}$ is the real representation of §*The Representations and the Coefficient Stack*, whose coefficient blocks each occur four times.

*Proof.* The real representation has each $M_{t}$ in four of its block rows, so $\lVert M^{R}\rVert_{F}^{2}=4\sum_{t}\lVert M_{t}\rVert_{F}^{2}=4K_{\mathrm F}(M)$ by the theorem, and the square root gives $\lVert M^{R}\rVert_{F}=2\lVert M\rVert_{F}$.

### The Least Squares Problem Factorises

**Theorem (least squares factorises).** Let $X$ be an arbitrary reduced biquaternion matrix, and let $X^{+}$ and $X^{-}$ range independently over the complex matrices. Then $X$ is a least squares solution of $AX\approx B$ if and only if $X^{+}$ is a least squares solution of $A^{+}X^{+}\approx B^{+}$ and $X^{-}$ is a least squares solution of $A^{-}X^{-}\approx B^{-}$. In that case

$$
\min_{X}K_{\mathrm F}(AX-B)=\tfrac12\Bigl(\min_{X^{+}}\bigl\lVert A^{+}X^{+}-B^{+}\bigr\rVert_{F}^{2}+\min_{X^{-}}\bigl\lVert A^{-}X^{-}-B^{-}\bigr\rVert_{F}^{2}\Bigr).
$$

*Proof.* By the decoupling theorem $AX-B$ has components $A^{+}X^{+}-B^{+}$ and $A^{-}X^{-}-B^{-}$, and by the metric theorem its norm is half the sum of the two squared Frobenius norms. The two components of $X$ are independent variables, so the minimum of the sum is the sum of the minima.

The theorem is the whole content of the reduction in the unconstrained case: two complex least squares problems, with no interaction.

### The Total Least Squares Problem Factorises

**Theorem (total least squares factorises).** Let $X$ be an arbitrary reduced biquaternion matrix, and let $X^{+},X^{-}$ range independently over the complex matrices. Then $X$ is a total least squares solution of $AX\approx B$ if and only if $X^{+}$ is a total least squares solution of $A^{+}X^{+}\approx B^{+}$ and $X^{-}$ is a total least squares solution of $A^{-}X^{-}\approx B^{-}$. In that case the minimum perturbation size is

$$
\min_{X,E,G}K_{\mathrm F}\bigl([E,G]\bigr)=\tfrac12\Bigl(\sum_{k=n+1}^{n+d}\bigl(s_{k}^{+}\bigr)^{2}+\sum_{k=n+1}^{n+d}\bigl(s_{k}^{-}\bigr)^{2}\Bigr),
$$

where $s_{k}^{+}:=s_{k}([A^{+},B^{+}])$ and $s_{k}^{-}:=s_{k}([A^{-},B^{-}])$, so that $s_{1}^{+}\ge\cdots\ge s_{n+d}^{+}$ are the singular values of the complex matrix $[A^{+},B^{+}]$, and likewise with the sign $-$ for the other component.

*Proof.* The constraint $(A+E)X=B+G$ is equivalent, by the decoupling theorem applied to it, to the two complex constraints $(A^{+}+E^{+})X^{+}=B^{+}+G^{+}$ and $(A^{-}+E^{-})X^{-}=B^{-}+G^{-}$, the perturbations $E^{+},G^{+}$ being arbitrary complex matrices when $E,G$ are arbitrary over the algebra; and the objective is half the sum of the two complex objective terms, by the metric theorem. The two complex problems are independent, and the complex total least squares minimum is the sum of the squares of the $d$ smallest singular values of the augmented matrix, the Eckart–Young–Mirsky statement recalled in §*Existence and Uniqueness*.

**Corollary (the mixed problem factorises).** The mixed problem factorises in the same way, into the complex mixed problems for $A_{a}^{+}X_{a}^{+}\approx B^{+}$ with the block $A_{b}^{+}$ perturbed, and for the other component; the minimum is half the sum of the two complex mixed minima.

The two theorems together are the statement that the reduced biquaternion approximation problems are pairs of complex approximation problems, and that nothing is lost and nothing is coupled.

## The Adjoint and the Moore–Penrose Inverse

The reduction is a statement about a form, and the form has an adjoint.

**Proposition (the adjoint is the bar-transpose).** Equip $\mathbb{B}_{\mathrm{r}}^{m\times n}$ with the real inner product $\mathrm{Re}\,K_{\mathrm F}$. Then the adjoint of the left multiplication $X\mapsto AX$, $A\in\mathbb{B}_{\mathrm{r}}^{m\times n}$, is the left multiplication by

$$
A^{\dagger}=\bar A^{\mathsf T},\qquad (A^{\dagger})_{rs}=\overline{A_{sr}},
$$

the bar-transpose; and $(AM)^{\dagger}=M^{\dagger}A^{\dagger}$. In components $(A^{\dagger})^{+}=(A^{+})^{*}$ and $(A^{\dagger})^{-}=(A^{-})^{*}$, the complex conjugate transposes.

*Proof.* The element identity is $\langle A\breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\langle\breve Q_{1},\bar A \breve Q_{2}\rangle_{\mathrm{ts}*}$ for all elements, which is the statement that left multiplication by $\bar A$ is adjoint to left multiplication by $A$; on matrices the two identities are summed over the entries, and the transpose of the index pair converts the left multiplication into the bar-transpose. For the components, the bar conjugates the coefficients, that is conjugates each complex component, and the transpose transposes each component; so the bar-transpose acts componentwise as the complex conjugate transpose.

**Theorem (the normal equations).** A matrix $X$ minimises $K_{\mathrm F}(AX-B)$ if and only if

$$
A^{\dagger}AX=A^{\dagger}B,
$$

and in components the two complex normal equations $(A^{+})^{*}A^{+}X^{+}=(A^{+})^{*}B^{+}$ and $(A^{-})^{*}A^{-}X^{-}=(A^{-})^{*}B^{-}$ hold.

*Proof.* The objective is convex and smooth, so $X$ is a minimiser if and only if the derivative vanishes, that is if and only if $\mathrm{Re}\,K_{\mathrm F}(A\delta,AX-B)=0$ for every $\delta$. By the adjoint proposition this is $\mathrm{Re}\,K_{\mathrm F}(\delta,A^{\dagger}(AX-B))=0$ for every $\delta$, and a vector whose real pairing with every vector vanishes is zero. Reading the equation in components gives the two complex normal equations.

**Theorem (the Moore–Penrose inverse).** There is a unique matrix $A_{\mathrm{MP}}$ satisfying the four Penrose equations for the adjoint $A^{\dagger}$,

$$
AA_{\mathrm{MP}}A=A,\qquad A_{\mathrm{MP}}AA_{\mathrm{MP}}=A_{\mathrm{MP}},\qquad (AA_{\mathrm{MP}})^{\dagger}=AA_{\mathrm{MP}},\qquad (A_{\mathrm{MP}}A)^{\dagger}=A_{\mathrm{MP}}A,
$$

and it is the pair of the complex Moore–Penrose inverses,

$$
A_{\mathrm{MP}}=(A^{+})_{\mathrm{MP}}\Pi_++(A^{-})_{\mathrm{MP}}\Pi_-.
$$

The least-norm least squares solution is $X=A_{\mathrm{MP}}B$, and the general least squares solution is $X=A_{\mathrm{MP}}B+(I-A_{\mathrm{MP}}A)Y$ for an arbitrary $Y$.

*Proof.* Each Penrose equation is equivalent, by the decoupling theorem, to the same equation in each complex component, because the adjoint is componentwise and the algebra multiplication is componentwise; the four complex equations have the unique complex pseudoinverse as their solution, so the pair is the unique solution of the four reduced biquaternion equations. The least-norm statement is that the complex pseudoinverse gives the least-norm complex solution, and the norm is half the sum of the two complex norm squares, so the reduced biquaternion least-norm solution is the pair of the complex least-norm solutions; the affine statement is the complex one read in the two components.

The normal equations of the theorem are the classical ones the article started from, and the pseudoinverse is the pair of the two complex pseudoinverses; the algebra adds no new inverse.

## The Three Nested Unknowns

The reduction of the two theorems holds for an arbitrary reduced biquaternion unknown, in which the two components are free. Two smaller unknowns are obtained by imposing conditions, and they are the cases met in applications.

**Definition.** An unknown matrix is **reduced biquaternion** if it ranges over $\mathbb{B}_{\mathrm{r}}^{n\times d}$; **complex** if it is fixed by the tessarine sign, $X_{\mathrm{ts}}=X$, equivalently $X^{+}=X^{-}$ with the common value a complex matrix; and **real** if it is fixed by the tessarine sign and the bar, equivalently $X^{+}=X^{-}$ is a real matrix, equivalently the coefficient blocks $X_{1},X_{2},X_{3}$ vanish.

**Theorem (the nesting).** The complex unknown is the reduced biquaternion unknown with the two components constrained to be equal, and the real unknown is the complex unknown with the common component constrained to be real:

$$
\text{reduced biquaternion}\ \supset\ \text{complex}\ \supset\ \text{real}.
$$

For each of the three problems of §*The Three Approximation Problems* the minimum is nondecreasing along the chain.

*Proof.* If $X\in\mathbb{C}^{n\times d}$ then $X^{+}=X^{-}=X$ by the definition of the components and the vanishing of the coefficients of $j$ and $ij$; if $X\in\mathbb{R}^{n\times d}$ then the common component is real. The minimum over a larger set is no larger, since the objective is the same function restricted.

The effective problem in each case is a complex problem, and the three differ only in the unknown:

| unknown $X$ | constraint | the effective problem |
|---|---|---|
| reduced biquaternion | none | two independent complex problems |
| complex | $X^{+}=X^{-}=X$, complex | two complex problems sharing one complex unknown |
| real | $X^{+}=X^{-}=X$, real | two complex problems sharing one real unknown |

**Corollary (the complex unknown as a stacked problem).** For the complex unknown the objective is $\tfrac12\lVert \mathsf A X-\mathsf B\rVert_{F}^{2}$ with the stacked complex matrices $\mathsf A=\begin{pmatrix}A^{+}\\ A^{-}\end{pmatrix}$ and $\mathsf B=\begin{pmatrix}B^{+}\\ B^{-}\end{pmatrix}$, so the least squares solution is $X=\mathsf A_{\mathrm{MP}}\mathsf B$; the total least squares and mixed problems are the complex ones for this stack.

*Proof.* Setting $X^{+}=X^{-}=X$ in the factorised objective of §*The Idempotent Reduction* gives half the sum of the two complex residual squares, which is half the squared Frobenius norm of the stacked residual; the stacked complex least squares solution is the pseudoinverse one.

The source works with the third row of the table, the real unknown, and its real representation is the way it inverts the equality of the two complex unknowns into a single real problem.

## The Representations and the Coefficient Stack

### The Coefficient Stack

**Definition.** The **coefficient stack** of $M\in\mathbb{B}_{\mathrm{r}}^{m\times n}$ is the real matrix

$$
C_{M}=\begin{pmatrix}M_{0}\\ M_{1}\\ M_{2}\\ M_{3}\end{pmatrix}\in\mathbb{R}^{4m\times n},
$$

and the stack of $B$ is written $C_{B}$, of size $4m\times d$.

**Theorem (the stack carries the problem).** For a real unknown $X\in\mathbb{R}^{n\times d}$,

$$
K_{\mathrm F}(AX-B)=\bigl\lVert C_{A}X-C_{B}\bigr\rVert_{F}^{2}.
$$

*Proof.* The stack identity is the identity $\sum_{t}\lVert M_{t}\rVert_{F}^{2}=\lVert C_{M}\rVert_{F}^{2}$ of the metric theorem, applied to the three residuals, the residual of the stack being the stack of the residual coefficientwise.

The theorem is the reason the real unknown is a classical real problem, and its minimiser is the real least squares solution of $C_{A}X\approx C_{B}$.

### The Real Representation

**Definition.** The **real representation** of $M=M_{0}+M_{1}i+M_{2}j+M_{3}ij$ is the real matrix

$$
M^{R}=\begin{pmatrix}M_{0}&-M_{1}&M_{2}&-M_{3}\\ M_{1}&M_{0}&M_{3}&M_{2}\\ M_{2}&-M_{3}&M_{0}&-M_{1}\\ M_{3}&M_{2}&M_{1}&M_{0}\end{pmatrix}\in\mathbb{R}^{4m\times 4n}.
$$

**Theorem (the real representation is a homomorphism).** $(MN)^{R}=M^{R}N^{R}$, and the first block column of $M^{R}$ is the coefficient stack $C_{M}$.

*Proof.* The four blocks of the product are the four coefficient blocks of $MN$, computed from the multiplication of the algebra on the coefficient blocks; the same rule reproduces the four block rows of $M^{R}N^{R}$. The first block column of $M^{R}$ is the column of the four blocks $M_{0},M_{1},M_{2},M_{3}$.

**Proposition (the rank of the stack).** The matrix $A\in\mathbb{B}_{\mathrm{r}}^{m\times n}$ has full column rank — the map $X\mapsto AX$ is injective on $\mathbb{B}_{\mathrm{r}}^{n\times d}$ — if and only if the coefficient stack $C_{A}$ has full real column rank $n$, equivalently if and only if both complex components $A^{+}$ and $A^{-}$ have full complex column rank.

*Proof.* Injectivity of $X\mapsto AX$ is injectivity in both components, so it holds if and only if the two complex matrices have full column rank. The real and imaginary parts of $A^{+}$ and of $A^{-}$ stack, after an invertible real row operation, into the four coefficient blocks $A_{0},A_{1},A_{2},A_{3}$; an invertible row operation preserves the column rank, so the compound of the two complex stacks has rank $n$ exactly when $C_{A}$ does.

The rank proposition is the source's rank lemma, and the stack theorem is its norm identity read in the corpus's form.

### The Complex Representation

The real representation has a complex counterpart, and the two carry the same multiplication.

**Definition.** The **homogeneous components** of $M=M_{0}+M_{1}i+M_{2}j+M_{3}ij$ are the complex matrices

$$
M^{(0)}=M_{0}+iM_{1},\qquad M^{(1)}=M_{2}+iM_{3},
$$

so that $M=M^{(0)}+jM^{(1)}$ and $M^{\pm}=M^{(0)}\pm M^{(1)}$, the superscript being the exponent of the hyperbolic unit $j$. The **complex representation** of $M$ is the $2m\times 2n$ complex matrix

$$
M^{C}=\begin{pmatrix}M^{(0)}&M^{(1)}\\ M^{(1)}&M^{(0)}\end{pmatrix}.
$$

It is the repeated-block form of *Reduced Biquaternion Other Algebraic Element Representations* read on a rectangular matrix, and its diagonalisation is the pair $(M^{+},M^{-})$ through the change of basis of *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*.

**Theorem (the complex representation is a homomorphism).** $(MN)^{C}=M^{C}N^{C}$.

*Proof.* Writing $M=M^{(0)}+jM^{(1)}$ and $N=N^{(0)}+jN^{(1)}$, the centrality of $j$ and $j^{2}=1$ give $MN=(M^{(0)}N^{(0)}+M^{(1)}N^{(1)})+j(M^{(0)}N^{(1)}+M^{(1)}N^{(0)})$, so the diagonal blocks of $M^{C}N^{C}$ are $M^{(0)}N^{(0)}+M^{(1)}N^{(1)}$ and the off-diagonal blocks are $M^{(0)}N^{(1)}+M^{(1)}N^{(0)}$, which are the blocks of $(MN)^{C}$. Equivalently these are $(MN)^{\pm}=M^{\pm}N^{\pm}$ read on the two signs.

**Corollary (the complex norm).**

$$
\lVert M\rVert_{F}=\tfrac{1}{\sqrt2}\bigl\lVert M^{C}\bigr\rVert_{F},\qquad \bigl\lVert M^{C}\bigr\rVert_{F}^{2}=\bigl\lVert M^{+}\bigr\rVert_{F}^{2}+\bigl\lVert M^{-}\bigr\rVert_{F}^{2}.
$$

*Proof.* Each homogeneous component occurs in two blocks of $M^{C}$, so $\lVert M^{C}\rVert_{F}^{2}=2(\lVert M^{(0)}\rVert_{F}^{2}+\lVert M^{(1)}\rVert_{F}^{2})$. The four real coefficient matrices split into these two complex pairs, so $\lVert M^{(0)}\rVert_{F}^{2}+\lVert M^{(1)}\rVert_{F}^{2}=\sum_{t}\lVert M_{t}\rVert_{F}^{2}=K_{\mathrm F}(M)=\lVert M\rVert_{F}^{2}$ by §*The Metric Splits*, and $\lVert M^{+}\rVert_{F}^{2}+\lVert M^{-}\rVert_{F}^{2}=2(\lVert M^{(0)}\rVert_{F}^{2}+\lVert M^{(1)}\rVert_{F}^{2})$ by the parallelogram identity for the entrywise squared modulus. The two displays follow.

### The Equivalence

**Theorem (the source's equivalence).** For a real unknown $X$, the mixed problem over the algebra and the real mixed problem for the stack $(C_{A},C_{B})$ have the same solutions. The reduced biquaternion mixed solution is the real mixed solution of the stack.

*Proof.* An arbitrary perturbation $E_{b}$ of $A_{b}$ over the algebra has arbitrary coefficient blocks, so its stack $C_{E_{b}}$ is an arbitrary real matrix, and conversely; the same holds for $G$ and $B$. For a real $X$ the stack commutes with the product, $C_{MX}=C_{M}X$, because the coefficient blocks of $MX$ are the products $M_{t}X$ of the coefficient blocks with the real matrix $X$; so the residual stack is $(C_{A}+C_{E})X-(C_{B}+C_{G})$ and the constraint is the real one. The objective is $\lVert[C_{E_{b}},C_{G}]\rVert_{F}^{2}$ by the stack theorem applied to the concatenation, which is the real objective. The two problems therefore have the same feasible tuples and the same objective, whence the same minimisers.

The equivalence is the reason the algorithm of the next section, which is a real algorithm, solves the reduced biquaternion problem with a real unknown.

## The Algorithm

### The Real Unknown

For the real unknown the source's algorithm is the classical mixed algorithm on the stack, and it proceeds by eliminating the exact block by a QR factorisation and then solving a reduced total least squares problem by a singular value decomposition. The Householder transformation is the standard one and is not repeated here.

Let $C=[C_{A_{a}},C_{A_{b}}]$ be the stack of $A$ split after $n_{1}$ columns, and $D=C_{B}$. Perform $n_{1}$ Householder transformations $Q$ of the stack so that

$$
Q^{\mathsf T}[C,D]=\begin{pmatrix}R_{11}&R_{12}&R_{1d}\\ 0&R_{22}&R_{2d}\end{pmatrix},
$$

and let $[R_{22},R_{2d}]=U\operatorname{diag}(s_{1},\dots,s_{n_{2}+d})V^{\mathsf T}$ be the singular value decomposition of the reduced block, with $V$ partitioned as $\begin{pmatrix}V_{11}&V_{12}\\ V_{21}&V_{22}\end{pmatrix}$ against the split $n_{2}+d$.

| step | operation | output |
|---|---|---|
| 1 | form the stack $C=[C_{A_{a}},C_{A_{b}}]$ and $D=C_{B}$ | the real data |
| 2 | Householder QR of the first $n_{1}$ columns | $R_{11},R_{12},R_{1d},R_{22},R_{2d}$ |
| 3 | singular value decomposition of $[R_{22},R_{2d}]$ | $U$, the singular values, $V$, split $V$ |
| 4 | reduced total least squares | $X_{b}=-V_{12}V_{22}^{-1}$ |
| 5 | back-substitution through the exact block | $X_{a}=R_{11}^{-1}(R_{1d}-R_{12}X_{b})$ |

**Proposition (the algorithm gives the mixed solution).** If $R_{11}$ is nonsingular and the reduced block has a unique total least squares solution, the algorithm outputs the mixed solution of the stack, hence the reduced biquaternion mixed solution of the source's real case.

*Proof.* The Householder transformation is orthogonal, so it preserves the Frobenius norm and therefore the perturbation objective; the exact block becomes triangular with nonsingular $R_{11}$, and the reduced problem is the total least squares problem of the block $[R_{22},R_{2d}]$, whose solution is $X_{b}=-V_{12}V_{22}^{-1}$ when it is unique; the back-substitution solves the triangular exact block, which is the $X_{a}$ obtained by projecting off the column space of $C_{A_{a}}$. The equivalence of the stack and the algebra is the theorem of the preceding section.

### The Arbitrary Unknown

For the arbitrary reduced biquaternion unknown the algorithm is two complex ones in parallel, with no Householder reduction needed to remove a coupling, because there is no coupling. The two complex mixed problems are solved by the classical complex mixed algorithm on the four data blocks $A_{a}^{+},A_{b}^{+},B^{+}$ and $A_{a}^{-},A_{b}^{-},B^{-}$, and the two solutions are the two components of the answer. The real algorithm above is the special case in which the two complex unknowns are constrained to be equal and real, which is exactly the equality that forces the two complex QR reductions to be performed on the same stack.

## Existence and Uniqueness

### The Complex Criterion

**Definition.** For a complex matrix $[A,B]\in\mathbb{C}^{m\times(n+d)}$ with singular values $s_{1}\ge\cdots\ge s_{n+d}$, its **best rank-$n$ approximation** is the truncation of its singular value decomposition after $n$ terms, and it is unique exactly when $s_{n}>s_{n+1}$ (Eckart–Young–Mirsky).

**Theorem (existence and uniqueness, complex case).** With the singular value decomposition $[A,B]=U\operatorname{diag}(s_{1},\dots,s_{n+d})V^{*}$, and $V=\begin{pmatrix}V_{11}&V_{12}\\ V_{21}&V_{22}\end{pmatrix}$ against the split $n+d$, if $s_{n}>s_{n+1}$ and $V_{22}$ is nonsingular then the complex total least squares solution exists and is unique, and it is $X=-V_{12}V_{22}^{-1}$; the perturbation of $[A,B]$ is the best rank-$n$ approximation $U_{1}\operatorname{diag}(s_{1},\dots,s_{n})V_{1}^{*}$.

*Proof.* The total least squares problem asks for the smallest perturbation of $[A,B]$ with a right kernel containing the vector $\begin{pmatrix}X\\ -I_{d}\end{pmatrix}$, and the smallest perturbation of rank at most $n$ is the best rank-$n$ approximation; the gap makes it unique, and its kernel is spanned by the columns of $\begin{pmatrix}V_{12}\\ V_{22}\end{pmatrix}$. The vector $\begin{pmatrix}X\\ -I_{d}\end{pmatrix}$ then equals $\begin{pmatrix}V_{12}\\ V_{22}\end{pmatrix}T$ for a nonsingular $T$, and the lower block gives $T=-V_{22}^{-1}$ and hence $X=V_{12}T=-V_{12}V_{22}^{-1}$.

### The Reduced Biquaternion Criterion

**Theorem (existence and uniqueness, algebra case).** For the arbitrary reduced biquaternion unknown the total least squares solution exists and is unique if and only if each complex component has a unique total least squares solution, that is, if and only if in each component $s_{n}>s_{n+1}$ and the block $V_{22}$ is nonsingular. The solution is then the pair $X=X^{+}\Pi_++X^{-}\Pi_-$ of the two complex solutions.

*Proof.* The problem is the pair of the two complex problems by the factorisation theorem, and a product of two problems has a unique solution exactly when each factor does; the complex criterion is the preceding theorem.

**Theorem (existence and uniqueness, mixed case).** For the mixed problem the two criteria are applied to the reduced blocks $[R_{22},R_{2d}]$ of the two components, with the gap $s_{n_{2}}>s_{n_{2}+1}$ and the nonsingularity of the block $V_{22}$ of the reduced right singular vectors; this is the source's criterion for the real case, read in the two components.

*Proof.* The mixed problem is the two complex reduced problems of §*The Algorithm*, and the complex criterion applies to each; the real case is the two components constrained to be equal and real, and the uniqueness of the constrained solution is the uniqueness of the reduced real problem, which is the common form of the two reduced complex ones.

**Remark (the failure modes).** When the gap fails, two or more singular values tie and the best rank-$n$ approximation is not unique, so the total least squares solution is a set; when $V_{22}$ is singular, the reduced total least squares problem has no solution in the classical sense and the perturbation must be enlarged. Both are the classical complex failure modes and they occur independently in the two components, so one component may be well posed while the other is not, in which case the arbitrary-unknown problem has the failure of that component.

## Special Cases and the Complex Field

### One Right-Hand Side

**Remark (the scalar case).** For $d=1$ the right-hand side is a column and the reduced total least squares solution is $X_{b}=-V_{12}V_{22}^{-1}$ with $V_{22}$ a scalar, so the criterion is the single condition that $V_{22}$ be nonzero; the three problems of the article all specialise to this case, which is the one the source's numerical example uses.

### The End Values of the Parameter

**Remark (the two ends).** For $n_{1}=n$ the exact block is the whole of $A$, the reduced block is empty of columns and the algorithm returns the least squares solution $X=A_{\mathrm{MP}}B$, in agreement with the corollary of the pseudoinverse; for $n_{1}=0$ the exact block is empty and the algorithm returns the total least squares solution. The mixed problem interpolates between them.

### The Complex Field

**Corollary (the complex problems are the special case).** The complex weighted and total least squares problems are the reduced biquaternion ones for an unknown in the fixed space of the tessarine sign and data whose absent coordinates vanish, since the complex field is the subalgebra $\mathbb{C}$ of $\mathbb{B}_{\mathrm{r}}$ and the two components of such data coincide. The developed methods therefore solve the complex least squares, total least squares and mixed problems as the degenerate case.

*Proof.* For data with $A^{+}=A^{-}=A$ and $B^{+}=B^{-}=B$ the two complex factor problems coincide, and their common solution is the complex solution; the unknown in the fixed space of the tessarine sign is the complex unknown.

### The Ordering of the Three Methods

**Remark (which method to use).** The three methods are distinguished by the noise they model, and each is the appropriate one when its model matches the data: the least squares method when only $B$ is contaminated, since it perturbs nothing else and is the optimal estimator under that hypothesis; the total least squares method when all of $A$ is contaminated, since it perturbs every column; and the mixed method when only $B$ and a prescribed block of the columns of $A$ are contaminated, since it perturbs exactly those. The source reports the numerical ordering of the three errors on a randomised example, one row of the ordering for each of the three contamination patterns, and the recovery of the pattern-matched method is what the reduction predicts: the method whose perturbed set is the contaminated set has the smallest error.

## The Solution as a Zero Divisor

The source restricts to a real unknown, and the reduced biquaternion case adds a phenomenon the division-algebra layers cannot show.

**Proposition (invertibility is componentwise).** A square matrix $X\in M_{n}(\mathbb{B}_{\mathrm{r}})$ is invertible if and only if both components $X^{+}$ and $X^{-}$ are nonsingular complex matrices, and then $X^{-1}=(X^{+})^{-1}\Pi_++(X^{-})^{-1}\Pi_-$; otherwise $X$ is a zero divisor of the algebra of matrices. In particular the least squares or total least squares solution of a square unknown can be a zero divisor.

*Proof.* The array isomorphism carries invertibility to invertibility in each factor, and an element of a direct product of rings is a unit exactly when both its entries are; a non-unit in the finite-dimensional algebra of matrices annihilates a nonzero matrix, so it is a zero divisor. For the example, take $B$ with vanishing $B^{-}$, so that $B=B_{0}(1+j)$ and $B^{-}=0$; then the least squares solution has $X^{-}=(A^{-})_{\mathrm{MP}}B^{-}=0$, so $X=X^{+}\Pi_+$ is annihilated by $\Pi_-$ on either side and is a zero divisor, although the problem is well posed and its residual is finite. For the single element unknown, $n=d=1$, the same example gives a nonzero $X$ with reduced norm $\langle X\rangle_{\mathrm{ts}}=\langle X^{+}\Pi_+\rangle_{\mathrm{ts}}=0$, a nonzero zero divisor of the algebra.

**Remark (the contrast).** For a scalar unknown over the division algebras $\mathbb{C}$ and $\mathbb{H}$ the solution is either zero or a unit, the null set being a single point; the reduced biquaternion solution can be a nonzero zero divisor on the null cone $\langle X\rangle_{\mathrm{ts}}=0$ while the approximation is solvable. For a square matrix unknown, non-invertible solutions occur over the complex field too, a singular matrix being a zero divisor of the matrix ring; what is specific to the reduced biquaternion case is the pair of independently vanishing components, one of which may be zero while the other is not, so that the solution is a zero divisor even when the complex companion problem has a solution of full rank.

## Verification

The following identities were checked by recomputation on random matrices of at most a few dozen entries, the deviations found at the level of the floating-point noise.

- The multiplication decoupling $(MN)^{+}=M^{+}N^{+}$ and $(MN)^{-}=M^{-}N^{-}$, and the norm identity $K_{\mathrm F}(M)=\sum_{t}\lVert M_{t}\rVert_{F}^{2}=\tfrac12(\lVert M^{+}\rVert_{F}^{2}+\lVert M^{-}\rVert_{F}^{2})$.
- The adjoint identity $K_{\mathrm F}(AM,N)=K_{\mathrm F}(M,A^{\dagger}N)$ with $A^{\dagger}=\bar A^{\mathsf T}$, and the normal equations $A^{\dagger}(AX-B)=0$ for the least squares solution.
- The rank lemma: the coefficient stack has full column rank if and only if both complex components have.
- The real representation homomorphism $(MN)^{R}=M^{R}N^{R}$ and that its first block column is the coefficient stack.
- The stack identity $K_{\mathrm F}(AX-B)=\lVert C_{A}X-C_{B}\rVert_{F}^{2}$ for a real $X$, and the nesting of the minima along the reduced biquaternion, the complex and the real unknown.
- The factorisation minima: the reduced biquaternion total least squares minimum is half the sum of the two complex minima, and the real-unknown value is no smaller than the arbitrary-unknown value.
- The zero-divisor example: with $B^{-}=0$ the least squares solution has $X^{-}=0$ and the value is the minimum over random probes.

The numerical ordering of the three methods was recomputed on random instances; the recovery of the pattern-matched method was reproduced, while the ordering of the other two depended on the instance at the level of a fraction of a percent, and is therefore reported as the source's observation rather than as a separate claim.

## Summary

The three approximation problems over the reduced biquaternion algebra — least squares, total least squares and the mixed problem interpolating between them — all reduce, through the idempotent decomposition $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$, to two complex problems, because the multiplication is componentwise and the norm $K$ splits as half the sum of the two squared complex Frobenius norms. For an arbitrary reduced biquaternion unknown the two complex problems are independent, for a complex unknown they share one complex unknown, and for a real unknown they share one real unknown; the minimum is nondecreasing along that chain. The form $K$ is a real inner product whose adjoint is the bar-transpose, so the normal equations decouple, and the Moore–Penrose inverse is the pair of the two complex pseudoinverses. The real unknown is the source's case: it is a classical real problem on the coefficient stack, whose algorithm is a Householder reduction of the exact block followed by a singular value decomposition of the reduced block, and whose existence and uniqueness hold exactly when the two spectral gaps separate and the block $V_{22}$ is nonsingular in each component. The coefficient stack and the real representation are the real readings of the matrix, and the complex representation $M^{C}$ is the complex one, with the two homogeneous components of $M$ in the hyperbolic unit as its blocks and the pair $(M^{+},M^{-})$ as its diagonalisation, the norm ladder being $\lVert M\rVert_{F}=\tfrac12\lVert M^{R}\rVert_{F}=\tfrac{1}{\sqrt2}\lVert M^{C}\rVert_{F}$. The complex field is the degenerate case of the construction, one right-hand side removes the matrix structure of the unknown, and the solution, unlike its counterparts in the division-algebra layers, may be a zero divisor of the algebra of matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle \breve Q\rangle_{\mathrm{ts}*}$ | The positive-definite norm, the topological one, $\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}=\tfrac12(\lvert Q_{+}\rvert^{2}+\lvert Q_{-}\rvert^{2})$ |
| $K_{\mathrm F}(M)$ | The entrywise matrix form, $\sum_{r,s}\langle M_{rs}\rangle_{\mathrm{ts}*}$, the square of the Frobenius norm |
| $M^{+},M^{-}$ | The two complex idempotent components, the pair of the array representation |
| $n_{1},n_{2}$ | The numbers of exact and of perturbed columns of $A$, $n_{1}+n_{2}=n$ |
| $A^{\dagger}=\bar A^{\mathsf T}$ | The $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$-adjoint of left multiplication |
| $A_{\mathrm{MP}}$ | The Moore–Penrose inverse for the adjoint $A^{\dagger}$ |
| $C_{M}$ | The coefficient stack $(M_{0},M_{1},M_{2},M_{3})^{\mathsf T}$ |
| $M^{R}$ | The $4m\times 4n$ real representation |
| $M^{(0)},M^{(1)}$ | The two complex homogeneous components of $M$ in $j$, $M_{0}+iM_{1}$ and $M_{2}+iM_{3}$ |
| $M^{C}$ | The $2m\times 2n$ complex representation, the blocks $M^{(0)}$ and $M^{(1)}$ |
| $s_{k}$ | A singular value of a component of $[A,B]$ or of the reduced block |
| $V_{12},V_{22}$ | The blocks of the right singular vectors of the augmented matrix |

## Further Reading

- Sk. Safique Ahmad and Neha Bhadala, "Algebraic technique for mixed least squares and total least squares problem in the reduced biquaternion algebra", arXiv:2311.06464 [math.NA] (2023), for the mixed problem over the reduced biquaternions, the four-block real representation and its rank lemma, the existence and uniqueness conditions, and the numerical example.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013), for the Householder QR factorisation, the singular value decomposition, the least squares problem and the Moore–Penrose inverse.
- Gene H. Golub and Charles F. Van Loan, "An analysis of the total least squares problem", *SIAM Journal on Numerical Analysis* **17** (1980) 883–893, for the total least squares problem and its solution by the singular value decomposition.
- Sabine Van Huffel and Joos Vandewalle, *The Total Least Squares Problem: Computational Aspects and Analysis* (SIAM, 1991), for the mixed least squares and total least squares problem and its reduced algorithm.
- Carl Eckart and Gale Young, "The approximation of one matrix by another of lower rank", *Psychometrika* **1** (1936) 211–218, for the best rank-$n$ approximation and its uniqueness under the spectral gap.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd edition (Cambridge University Press, 2013), for the adjoint, the normal equations and the polar decomposition.
- [Reduced Biquaternion Space](reduced-biquaternion-space.html), for the algebra, the idempotents and the coordinates.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the decomposition along the two idempotents.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the form $\langle\cdot\rangle_{\mathrm{ts}*}$ and the topological norm.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), for the bar, the tessarine sign and the star.
- [Reduced Biquaternion Other Algebraic Element Representations](reduced-biquaternion-other-algebraic-element-representations.html), for the array representation and the pair $(M^{+},M^{-})$.
- [Hermitian Solutions of the Pair Matrix Equation over the Reduced Biquaternions](hermitian-solutions-of-the-pair-matrix-equation-over-the-reduced-biquaternions.html), for the pair equation $(AXB,CXD)=(E,F)$ in the source's Hermitian set, the real representation and the signed selection used there, the half-vectorisation, and the least squares, consistency and uniqueness criteria.
- [Reduced Biquaternion Objects and their Matrix Correspondences](reduced-biquaternion-objects-and-their-matrix-correspondences.html), for the objects of the algebra and their matrix invariants.
- [Reduced Biquaternion Spectral Theory](reduced-biquaternion-spectral-theory.html), for the spectrum and the singular values of the algebra.
- [Compact Operators](compact-operators.html), for the singular values and the Schatten classes.
- [Quaternion Augmented Statistics](quaternion-augmented-statistics.html), for the least squares problem in the non-commutative quaternion statistics.
- [Biquaternion Objects and Their Matrix Correspondences](biquaternion-objects-and-their-matrix-correspondences.html), for the non-commutative companion of the matrix dictionary.
