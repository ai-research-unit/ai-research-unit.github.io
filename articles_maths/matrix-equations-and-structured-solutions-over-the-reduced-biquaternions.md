# __Matrix Equations and Structured Solutions over the Reduced Biquaternions__

## Introduction

The linear matrix equation over the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ is

$$
\sum_{l=1}^{r}A_lX_lB_l=E,\qquad A_l\in\mathbb{B}_{\mathrm{r}}^{m\times n_l},\quad B_l\in\mathbb{B}_{\mathrm{r}}^{s_l\times t},\quad E\in\mathbb{B}_{\mathrm{r}}^{m\times t},
$$

and the version of it read in the source of this article constrains the unknowns. Each unknown is required to lie in a prescribed set $L_l(n_l,s_l)$ of matrices cut by a set of real-linear conditions on its entries; the source calls such a set an **L-structure**, the name Magnus gave to a finite matrix pattern defined by a linear condition on the vec. The four instances the source develops are the Toeplitz, the symmetric Toeplitz, the Hankel and the circulant matrices over the algebra. The problem is to find the solution of least squares size whose unknowns obey the constraints, of least norm among those, and when the equation is consistent, the constrained solution of least norm.

The algebra is commutative, and this is what makes the constrained problem linear. The classical vec identity $\mathrm{vec}(AXB)=(B^{\mathsf T}\otimes A)\mathrm{vec}(X)$ holds over $\mathbb{B}_{\mathrm{r}}$ unchanged, because the coefficients of the algebra commute, so a linear condition on the entries of an unknown is carried into the coefficient matrix by the Kronecker product: writing the structure as the linear map $\mathrm{vec}(X_l)=\mathsf E_{L_l}\xi_l$ from the list of independent entries to the vec, the equation becomes one linear system over the algebra, $\mathsf C\xi=\mathrm{vec}(E)$. The sibling article *Least Squares and Total Least Squares over the Reduced Biquaternions* solves every such system: by the idempotent decomposition it is a pair of complex systems with independent complex unknowns, the norm $\langle\cdot\rangle_{\natural*}$ is half the sum of the two squared complex Frobenius norms, and the least-norm least squares solution is the pair of the two complex Moore–Penrose solutions. This article takes that solution as the answer to the structured problem; its own content is the structure, what an L-structure is, how it is encoded, and which structures the four classical patterns produce, together with the two inverse problems the structure serves.

**The results.** An **L-structure** is the set of matrices whose coefficient stack lies in a prescribed real subspace, and a **basis matrix** $M_L$ of the subspace reads the structure as one linear map on the real reading. The four classical L-structures are **of entry type**: each is the $\mathbb{B}_{\mathrm{r}}$-span of a finite family of real zero-one matrices with pairwise disjoint supports, so the structure condition is $\mathrm{vec}(X)=\mathsf E_L\xi_L$ with $\mathsf E_L$ the real matrix whose columns are the vecs of the family, of full column rank. The structured equation becomes the single algebra-valued system $\mathsf C\xi=\mathrm{vec}(E)$, and by the sibling article's reduction the least-norm structured least squares solution is the pair of the two complex Moore–Penrose solutions. The applications are the structured matrix equation $AXB+CYD=E$ with both unknowns structured, and the two inverse problems, the **partial inverse eigenvalue problem** $M\Phi=\Phi\Lambda$, a structured matrix carrying a prescribed part of its spectrum, and its generalized companion $M\Phi=N\Phi\Lambda$, in which both factors are structured and the spectrum is that of the matrix pencil.

**Boundaries.** The idempotent reduction, the form $\langle\cdot,\cdot\rangle_{\natural*}$ as the metric, the adjoint and the Moore–Penrose inverse, the coefficient stack and the real representation are *Least Squares and Total Least Squares over the Reduced Biquaternions*, which owns them; this article cites them rather than restating them. The algebra, the idempotents and the coordinates are *Reduced Biquaternion Space* and *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms*; the array representation $M_{m\times n}(\mathbb{B}_{\mathrm{r}})\cong M_{m\times n}(\mathbb{C})\times M_{m\times n}(\mathbb{C})$ and the repeated-block form are *Reduced Biquaternion Other Algebraic Element Representations*. The Kronecker calculus and the vec identity over a commutative ring are *The Hermitian Sylvester Equation*, where the Sylvester equation is inverted by it. The inverse eigenvalue problem, its partial form and its least squares treatment are the classical problem of Chu and Golub, and the spectrum of a matrix over the algebra is *Reduced Biquaternion Spectral Theory*. The Toeplitz **algebra** of operators of *Toeplitz Algebras* is a different object from the Toeplitz L-structure of finite matrices here, and the two are not identified.

**Conventions.** The element is $Q_\pm=Q_++jQ_-$ with $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$, the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, and the idempotent coordinates are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$; the involutions are the bar, the natural sign, the star and the flat of *Conventions in Mathematics*, and the $K$-adjoint is the bar-transpose. A matrix over $\mathbb{B}_{\mathrm{r}}$ is written $M=M_{0}+M_{1}i+M_{2}j+M_{3}ij$ with the four **coefficient matrices** real, and the **coefficient stack** is $C_{M}\in\mathbb{R}^{4m\times n}$ of the sibling article, the four coefficient matrices one above the other; its vec is the real reading of the vec of $M$. The **idempotent components** are the pair $(M^{+},M^{-})$ of complex matrices of the sibling article. The form is $\langle\cdot,\cdot\rangle_{\natural*}$, read entrywise as $K_{\mathrm F}$ with $\lVert M\rVert_{\mathrm F}^{2}=K_{\mathrm F}(M)$; the transpose is written $^{\mathsf T}$, the $K$-adjoint $M^{\dagger}$ and the Moore–Penrose inverse $M_{\mathrm{MP}}$, as in the sibling article. The **L-structure** is always named with its letter, to keep the finite matrix pattern distinct from the real and the complex structures of the algebra. The source writes $\Psi_M$ for the row form and $h(M)$ for the block form of the array representation, $\overrightarrow{\mathrm{vec}}(M)$ for the real reading of the vec, $M_L$ for the basis matrix of an L-structure and $K_T,K_{ST},K_H,K_C$ for the four pattern matrices; the pattern matrices are written $\mathsf E_T,\mathsf E_{ST},\mathsf E_H,\mathsf E_C$ here, because $\langle\cdot,\cdot\rangle_{\natural*}$ is the positive definite form of the corpus.

## The L-Structure

### The Definition

**An L-structure is a real-linear condition on the entries of a matrix over the algebra, read on the coefficient stack.**

**Definition (the reduced biquaternion L-structure).** Let $\Omega$ be a real subspace of $\mathbb{R}^{4ns}$. The **L-structure** cut by $\Omega$ is

$$
L(n,s)=\bigl\{X\in\mathbb{B}_{\mathrm{r}}^{n\times s}:\ \mathrm{vec}(C_X)\in\Omega\bigr\},
$$

where $C_X$ is the coefficient stack of $X$. A **basis matrix** of the L-structure is a real matrix $M_L$ whose columns are a basis of $\Omega$, so that the structure condition reads

$$
\mathrm{vec}(C_X)=M_L\,u_L,\qquad u_L\in\mathbb{R}^{D},\quad D=\dim_{\mathbb{R}}\Omega .
$$

The number $D$ is the **real dimension** of the structure and $u_L$ its real coordinate vector.

**Proposition (the structure is a real subspace).** $L(n,s)$ is a real subspace of $\mathbb{B}_{\mathrm{r}}^{n\times s}$ of real dimension $D$.

*Proof.* The map $X\mapsto\mathrm{vec}(C_X)$ is a real isomorphism from $\mathbb{B}_{\mathrm{r}}^{n\times s}$ onto $\mathbb{R}^{4ns}$, and the preimage of a subspace is a subspace of the same dimension.

The definition is the source's, with the vec of the matrix read as the vec of its coefficient stack; the two readings differ by a fixed real permutation of the coordinates.

### The Four Classical L-Structures

**The four L-structures of the source are cut by equalities among the entries, and each is the span of a finite family of real zero-one matrices with coefficients in the algebra.**

For an index $d\in\{-n+1,\dots,n-1\}$ let $J_d$ be the real $n\times n$ matrix of the $d$-th diagonal, $(J_d)_{pq}=1$ if $q-p=d$ and $0$ otherwise; for $m\in\{0,\dots,2n-2\}$ let $R_m$ be the real matrix of the $m$-th reverse diagonal, $(R_m)_{pq}=1$ if $p+q=m$; and for $k\in\{0,\dots,n-1\}$ let $Z_k$ be the cyclic matrix, $(Z_k)_{pq}=1$ if $q-p\equiv k\ (\mathrm{mod}\ n)$. The four structures and their generating families are these.

| structure | the pattern | the generating family | the width $d$ |
|---|---|---|---|
| Toeplitz | $X_{pq}$ depends on $q-p$ | $J_{-n+1},\dots,J_{n-1}$ | $2n-1$ |
| symmetric Toeplitz | $X_{pq}=X_{qp}$ and Toeplitz | $J_0$ and $J_k+J_{-k}$, $k=1,\dots,n-1$ | $n$ |
| Hankel | $X_{pq}$ depends on $p+q$ | $R_0,\dots,R_{2n-2}$ | $2n-1$ |
| circulant | $X_{pq}$ depends on $q-p$ modulo $n$ | $Z_0,\dots,Z_{n-1}$ | $n$ |

The diagonal structure, with the family of matrix units $E_{pp}$, the triangular structures, with the units above or below the diagonal, and every sequence of equalities among the entries are of the same kind: a finite family of real zero-one matrices. The four families of the table are independent over $\mathbb{R}$, the matrices of each family having pairwise disjoint supports.

### The Structures of Entry Type

**A structure is of entry type when it is spanned by real zero-one matrices, and then it is a module over the algebra and its condition commutes with the idempotent decomposition.**

**Definition.** An L-structure $L(n,s)$ is **of entry type** when it is the $\mathbb{B}_{\mathrm{r}}$-span of a finite family $S_1,\dots,S_d$ of real zero-one matrices of shape $n\times s$,

$$
X=\sum_{\lambda=1}^{d}Q_{\pm,\lambda} S_\lambda,\qquad Q_{\pm,\lambda}\in\mathbb{B}_{\mathrm{r}} .
$$

The number $d$ is the **width** of the structure, so that the real dimension is $D=4d$.

**Proposition (the encoding matrix).** For a structure of entry type, the structure condition is

$$
\mathrm{vec}(X)=\mathsf E_L\,\xi_L,\qquad \mathsf E_L=\bigl[\mathrm{vec}(S_1),\dots,\mathrm{vec}(S_d)\bigr]\in\mathbb{R}^{ns\times d},\qquad \xi_L=\bigl(Q_{\pm,1},\dots,Q_{\pm,d}\bigr)^{\mathsf T}\in\mathbb{B}_{\mathrm{r}}^{d},
$$

and on the coefficient stack it is $\mathrm{vec}(C_X)=(I_4\otimes\mathsf E_L)\xi_L^{\mathbb{R}}$, where $\xi_L^{\mathbb{R}}$ is the stack of the four real readings of the $Q_{\pm,\lambda}$, so that the basis matrix is $M_L=I_4\otimes\mathsf E_L$ and the real coordinate vector is $u_L=\xi_L^{\mathbb{R}}$; the matrix $\mathsf E_L$ has full column rank when the supports of the $S_\lambda$ are distinct, in particular for the four families of the table.

*Proof.* The vec of the sum is the sum of the vecs, and $\mathrm{vec}(Q_{\pm,\lambda} S_\lambda)=Q_{\pm,\lambda}\mathrm{vec}(S_\lambda)$ because $S_\lambda$ has real entries; collecting the coefficients of the $Q_{\pm,\lambda}$ gives the display. The coefficient-stack reading repeats the same pattern in each of the four blocks, the four coefficient matrices of $X$ being the four coefficients of each $Q_{\pm,\lambda}$ in the same real span. The columns of $\mathsf E_L$ are the vecs of matrices with pairwise disjoint supports, distinct coordinate vectors, and distinct coordinate vectors are independent.

**Proposition (the widths).** The four encodings of the table have the shapes $\mathsf E_T,\mathsf E_H\in\mathbb{R}^{n^{2}\times(2n-1)}$ and $\mathsf E_{ST},\mathsf E_C\in\mathbb{R}^{n^{2}\times n}$, each of full column rank, and the four structures have real dimensions $4(2n-1)$, $4n$, $4(2n-1)$ and $4n$.

*Proof.* The width is the number of matrices in the generating family, and the real dimension is four times the width by the definition; the ranks are the proposition above.

**Remark (the general L-structure mixes the coefficients).** A general real subspace $\Omega$ need not be spanned by the vecs of real matrices, and the corresponding L-structure then need not be a module over the algebra: the condition may couple the four coefficient matrices of $X$ to one another, and through them the two idempotent components. For a structure of entry type the four coefficient matrices are constrained to the same real pattern, each with its own independent coefficients, so the condition is $\mathbb{B}_{\mathrm{r}}$-linear and commutes with the idempotent decomposition. The four classical structures and the structures of the applications are of entry type, and the source states its results for the general L-structure, its reduction reaching the real system in either case.

## The Structured Equation

### The Algebra-Valued System

**The structure enters the vec identity through the encoding matrix, and the equation in several structured unknowns becomes one linear system over the algebra.**

**Theorem (the structured system).** Let $A_l\in\mathbb{B}_{\mathrm{r}}^{m\times n_l}$ and $B_l\in\mathbb{B}_{\mathrm{r}}^{s_l\times t}$ for $l=1,\dots,r$, let $E\in\mathbb{B}_{\mathrm{r}}^{m\times t}$, and let each unknown lie in a structure $L_l(n_l,s_l)$ of entry type with encoding matrix $\mathsf E_{L_l}$ and coordinates $\xi_{L_l}$. Then the equation $\sum_lA_lX_lB_l=E$ is equivalent to the algebra-valued linear system

$$
\mathsf C\,\xi=\mathrm{vec}(E),\qquad \mathsf C=\bigl[(B_1^{\mathsf T}\otimes A_1)\mathsf E_{L_1},\dots,(B_r^{\mathsf T}\otimes A_r)\mathsf E_{L_r}\bigr],\qquad \xi=\bigl(\xi_{L_1},\dots,\xi_{L_r}\bigr)^{\mathsf T},
$$

of size $mt\times\sum_ld_l$ over $\mathbb{B}_{\mathrm{r}}$, and the coefficient matrix $\mathsf C$ does not depend on the unknown.

*Proof.* The vec identity applied to each term gives $\mathrm{vec}(A_lX_lB_l)=(B_l^{\mathsf T}\otimes A_l)\mathrm{vec}(X_l)=(B_l^{\mathsf T}\otimes A_l)\mathsf E_{L_l}\xi_{L_l}$, and the sum of the vecs is the vec of the sum.

**Remark (the identity is the classical one).** The identity $\mathrm{vec}(AXB)=(B^{\mathsf T}\otimes A)\mathrm{vec}(X)$ is the classical one over a commutative ring, and the algebra, being commutative, carries it with the entries of the Kronecker product read in the algebra; this is the reason no commutation term appears and the reason the structure is a linear condition after the reduction. The source states the same identity on the row form $\Psi_M$ and the block form $h(M)$ of the array representation, where the Kronecker product is written blockwise over the two complex summands; the two forms are the sibling article's array representation, and the source's version is this identity read there.

### The Least-Norm Structured Least Squares Solution

**The system is a linear system over the algebra, and the sibling article's reduction solves it: the structured least squares solution is the pair of the two complex Moore–Penrose solutions.**

**Theorem (the structured solution).** The squared norm of the residual of the structured equation is half the sum of the two squared complex norms of the two components,

$$
K_{\mathrm F}\Bigl(\sum_{l}A_lX_lB_l-E\Bigr)=\tfrac12\Bigl(\bigl\lVert\mathsf C^{+}\xi^{+}-\mathrm{vec}(E)^{+}\bigr\rVert_{\mathrm F}^{2}+\bigl\lVert\mathsf C^{-}\xi^{-}-\mathrm{vec}(E)^{-}\bigr\rVert_{\mathrm F}^{2}\Bigr),
$$

and the least-norm least squares structured solution is

$$
\xi^{\pm}=\bigl(\mathsf C^{\pm}\bigr)_{\mathrm{MP}}\mathrm{vec}(E)^{\pm},\qquad X_l=\sum_{\lambda=1}^{d_l}\bigl(\xi_{L_l}\bigr)_{\lambda}S_\lambda,
$$

the Moore–Penrose inverses being taken in the complex field; the minimum is half the sum of the two independent complex minima, attained separately.

*Proof.* The structured system is a linear system $\mathsf C\xi=\mathrm{vec}(E)$ over $\mathbb{B}_{\mathrm{r}}$ with the unknown $\xi$ ranging over the algebra, and the objective is the entrywise norm $K_{\mathrm F}$; the sibling article's least squares theorem applies to it verbatim, its hypotheses being only the algebra and the norm. The two components of $\xi$ are independent because $\xi$ ranges over the whole algebra, and the encoding matrices have real entries, so the structure is invisible to the idempotent decomposition and the two complex problems are the reductions of the same structured system.

**Corollary (consistency and uniqueness).** The structured equation has an exact solution if and only if $\mathsf C^{\pm}_{\mathrm{MP}}\mathrm{vec}(E)^{\pm}=\mathrm{vec}(E)^{\pm}$ for both signs, and the least squares residual is zero exactly then; the structured solution is unique if and only if both complex matrices $\mathsf C^{+}$ and $\mathsf C^{-}$ have full column rank, equivalently if and only if the coefficient stack of $\mathsf C$ has full real column rank.

*Proof.* The three statements are the sibling article's existence and uniqueness criteria, read on the structured system; the equivalence of the full-rank conditions is its rank proposition.

**Remark (the real reading and the partition formula).** The source writes the same solution in the real reading, as the stacked system $\begin{pmatrix}Q_1\\Q_2\end{pmatrix}x=e$ of the real and the imaginary parts of the two components, and gives the least-norm solution by the partitioned pseudoinverse of the stacked matrix. This is the sibling article's stack of the two components with the classical partition formula of Cline, and it is the numerical form of the solution above rather than a second reduction.

**Remark (the structured solution as a pair, and the zero divisors).** The two complex systems are the two factors of the algebra, and a structured solution is a pair of complex solutions rather than one complex solution; either member of the pair may vanish while the other does not, and the corresponding structured matrix is then a zero divisor. This is the phenomenon the sibling article records for the unstructured problem: the algebra has no division, and a structure of entry type does not remove the phenomenon, because the constraint is imposed on each component alike and neither component is forced to be nonzero.

## The Applications

### The Structured Matrix Equation

**The equation $AXB+CYD=E$ with two structured unknowns is the case $r=2$ of the system, and the source works it for the Hankel and the symmetric Toeplitz structures.**

The unknowns $X\in L_1(n,s)$ and $Y\in L_2(n,s)$ obey the equation with the four coefficients $A,C\in\mathbb{B}_{\mathrm{r}}^{m\times n}$ and $B,D\in\mathbb{B}_{\mathrm{r}}^{s\times t}$, and the system is that of the theorem with $r=2$, $\mathsf C=[(B^{\mathsf T}\otimes A)\mathsf E_{L_1},(D^{\mathsf T}\otimes C)\mathsf E_{L_2}]$. The source's two instances take the unknowns **complex** Hankel and **real** symmetric Toeplitz; a complex or a real unknown is the sibling article's nested unknown, and its constraint, that the two idempotent components coincide, and in the real case are real, is imposed in addition to the structure. The two reductions compose, the structure being invisible to the idempotent decomposition and the nesting being invisible to the structure.

### The Partial Inverse Eigenvalue Problem

**The partial inverse eigenvalue problem prescribes a part of the spectrum and asks for a structured matrix, and it is the structured equation with $A=I_n$ and the right-hand side $\Phi\Lambda$.**

**Problem (the PDIEP).** Given $\Lambda=\mathrm{diag}(\lambda_1,\dots,\lambda_k)$ and $\Phi=[v_1,\dots,v_k]$ with $k\le n$, and a structure $L(n,n)$, find $M\in L(n,n)$ with $M\Phi=\Phi\Lambda$; the columns of $\Phi$ are the prescribed eigenvectors and the entries of $\Lambda$ the prescribed eigenvalues.

**Remark (the problem is the structured equation).** With $A=I_n$, $X=M$, $B=\Phi$ and $E=\Phi\Lambda$ the PDIEP is the structured equation $AXB=E$ for $X\in L(n,n)$, and the theorem above returns the least-norm structured least squares solution when the prescribed part of the spectrum is not attainable exactly, and the exact structured solution when it is. The source works the problem for the symmetric Toeplitz and the Hankel structures; the theorem is blind to which structure of entry type is used.

### The Generalized Partial Inverse Eigenvalue Problem

**The generalized problem prescribes the same partial data for a pencil, and it is the structured equation $AXB+CYD=0$ with $A=I_n$ and $C=-I_n$.**

**Problem (the generalized PDIEP).** Given $\Lambda$ and $\Phi$ as above and a structure $L(n,n)$, find $M,N\in L(n,n)$ with $M\Phi=N\Phi\Lambda$, so that the columns of $\Phi$ are the prescribed eigenvectors and the entries of $\Lambda$ the prescribed eigenvalues of the pencil $M-\lambda N$.

**Remark (the problem is the two-unknown structured equation).** With $A=I_n$, $B=\Phi$, $C=-I_n$, $D=\Phi\Lambda$ and $E=0$ the generalized problem is the case $r=2$ of the structured system with both unknowns in the same structure, and the theorem returns the pair of structured matrices of least norm; as in the single problem, the exact pencil is recovered when the data are attainable and the least squares pencil otherwise. When $\Lambda$ carries the full spectrum of a structured matrix and $\Phi$ a full set of its eigenvectors, the data determine the matrix inside the structure, and the framework recovers it; this is the check of the last section.

## Verification

The following identities were checked by recomputation on random matrices of at most a few dozen entries, the deviations found at the level of the floating-point noise.

- The vec identity $\mathrm{vec}(AXB)=(B^{\mathsf T}\otimes A)\mathrm{vec}(X)$ over $\mathbb{B}_{\mathrm{r}}$, and the multiplicativity $h(MN)=h(M)h(N)$ of the block form.
- The four encodings $\mathsf E_T,\mathsf E_{ST},\mathsf E_H,\mathsf E_C$ reproduce their structures, the condition $\mathrm{vec}(X)=\mathsf E_L\xi_L$ holds, and each has full column rank, in each case for $n=3,4,5$.
- The constrained least squares equivalence: for the four classical structures the stacked real system $\begin{pmatrix}Q_1\\ Q_2\end{pmatrix}x=e$ and the direct constrained problem have the same minimiser.
- The structured solution: the solution of the theorem is minimal among random structured perturbations, and the normal equations $\mathsf C^{\dagger}(\mathsf C\xi-\mathrm{vec}(E))=0$ hold elementwise.
- The partition formula of Cline for the pseudoinverse of the stacked matrix, and the Penrose equations $APA=A$ and $PAP=P$.
- The PDIEP: with the full set of eigenpairs of a symmetric Toeplitz matrix the framework recovers the matrix.

## Summary

A linear matrix equation over the reduced biquaternions whose unknowns lie in prescribed matrix patterns is an unconstrained least squares problem after two linear reductions. **The L-structure** is the first: a set of matrices whose coefficient stack lies in a real subspace, written with a basis matrix $M_L$ as $\mathrm{vec}(C_X)=M_Lu_L$; the four classical structures, Toeplitz, symmetric Toeplitz, Hankel and circulant, are of **entry type**, each the span of a finite family of real zero-one matrices with disjoint supports and pairwise independent, and the structure condition is $\mathrm{vec}(X)=\mathsf E_L\xi_L$ with $\mathsf E_L$ the matrix whose columns are the vecs of the family, of full column rank. **The vec identity** is the second: the algebra is commutative, so $\mathrm{vec}(AXB)=(B^{\mathsf T}\otimes A)\mathrm{vec}(X)$ holds unchanged, and the equation in several structured unknowns becomes the single algebra-valued system $\mathsf C\xi=\mathrm{vec}(E)$ with $\mathsf C$ assembled from the Kronecker products and the encodings. The sibling article's reduction then applies: the system is a pair of complex systems with independent complex unknowns, the norm $\langle\cdot\rangle_{\natural*}$ is half the sum of the two squared complex Frobenius norms, and the least-norm structured least squares solution is the pair of the two complex Moore–Penrose solutions, of minimum half the sum of the two complex minima. The general L-structure of the source need not be spanned by real matrices, and then the condition may couple the four coefficient matrices; the structures of entry type do not, and the four classical patterns and both applications are of that kind. The applications are the structured equation $AXB+CYD=E$ with both unknowns structured, the partial inverse eigenvalue problem $M\Phi=\Phi\Lambda$ and the generalized problem $M\Phi=N\Phi\Lambda$, each an instance of the system with a particular choice of the coefficients and the right-hand side, and each solved by the same theorem. The one phenomenon the commutative algebra adds survives the structure: a structured solution is a pair of complex solutions, and either member may vanish, so the solution may be a zero divisor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L(n,s)$, $X\in L(n,s)$ | An L-structure of reduced biquaternion matrices, and a structured matrix |
| $\Omega$, $D$ | The real subspace cutting the structure, and its real dimension |
| $M_L$, $u_L$ | The basis matrix of the subspace, and its real coordinate vector, $\mathrm{vec}(C_X)=M_Lu_L$ |
| $S_1,\dots,S_d$, $d$ | The real zero-one generating family of a structure of entry type, and its width |
| $\mathsf E_L$, $\xi_L$ | The encoding matrix of a structure of entry type, and the algebra-valued coordinates, $\mathrm{vec}(X)=\mathsf E_L\xi_L$ |
| $\mathsf E_T,\mathsf E_{ST},\mathsf E_H,\mathsf E_C$ | The four classical encodings |
| $J_d$, $R_m$, $Z_k$ | The matrices of the $d$-th diagonal, the $m$-th reverse diagonal and the cyclic structure |
| $C_M$ | The coefficient stack, the four coefficient matrices one above the other |
| $M^{+},M^{-}$ | The idempotent components, $M^{\pm}=M_{0}\pm M_{2}+i(M_{1}\pm M_{3})$ |
| $\langle\cdot,\cdot\rangle_{\natural*}$, $K_{\mathrm F}$ | The positive definite form of the algebra, and its entrywise reading |
| $^{\mathsf T}$, $M^{\dagger}$, $M_{\mathrm{MP}}$ | The transpose, the $\langle\cdot,\cdot\rangle_{\natural*}$-adjoint and the Moore–Penrose inverse |
| $\otimes$, $\mathrm{vec}$ | The Kronecker product, and the vec column by column |
| $\mathsf C$, $\xi$ | The coefficient matrix $[(B_1^{\mathsf T}\otimes A_1)\mathsf E_{L_1},\dots]$, and the structure coordinates |
| $\Lambda$, $\Phi$ | The prescribed eigenvalues and eigenvectors of the inverse problems |

## Further Reading

- Sk. Safique Ahmad and Neha Bhadala, "L-structure least squares solutions of reduced biquaternion matrix equations with applications", arXiv:2311.06461 [math.NA] (2023), the source of this article, for the L-structure of reduced biquaternion matrices, the four classical structures and their pattern matrices, the reduction of the equation in several structured unknowns, the partitioned pseudoinverse, the complex and the real matrix equation, the PDIEP and the generalized PDIEP, and the numerical examples.
- J. R. Magnus, "L-structured matrices and linear matrix equations", *Linear and Multilinear Algebra* **14** (1983) 67–88, for the L-structure as a linear condition on the vec of a matrix and its use in linear matrix equations.
- R. E. Cline, "Representations for the generalized inverse of a partitioned matrix", *Journal of the Society for Industrial and Applied Mathematics* **12** (1964) 588–600, for the partitioned form of the pseudoinverse of a stacked matrix.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013), for the Kronecker product, the vec identity, the Moore–Penrose inverse and the singular value decomposition.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd edition (Cambridge University Press, 2013), for the transpose and the partitioned inverses.
- Moody T. Chu and Gene H. Golub, *Inverse Eigenvalue Problems: Theory, Algorithms, and Applications* (Oxford University Press, 2005), for the inverse eigenvalue problem, its partial form and its least squares treatment.
- *Least Squares and Total Least Squares over the Reduced Biquaternions* (`articles_maths/least-squares-and-total-least-squares-over-the-reduced-biquaternions.md`), for the idempotent reduction, the form $\langle\cdot,\cdot\rangle_{\natural*}$ as the metric, the adjoint and the Moore–Penrose inverse, the three nested unknowns, the coefficient stack and the real representation, existence and uniqueness, the reduction this article cites rather than restates.
- *Reduced Biquaternion Other Algebraic Element Representations* (`articles_maths/reduced-biquaternion-other-algebraic-element-representations.md`), for the array representation $M\mapsto(M^{+},M^{-})$, the idempotent components and the repeated-block form.
- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), for the algebra, the idempotents and the coordinates.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the form $\langle\cdot,\cdot\rangle_{\natural*}$, its entrywise form $K_{\mathrm F}$ and the Frobenius norm.
- *The Hermitian Sylvester Equation* (`articles_maths/the-hermitian-sylvester-equation.md`), for the Kronecker inverse and the vec identity over a commutative ring, the Sylvester equation being the model.
- *Toeplitz Algebras* (`articles_maths/toeplitz-algebras.md`), for the Toeplitz algebra of operators, which is a different object from the Toeplitz L-structure of finite matrices here.
- *Hermitian Solutions of the Pair Matrix Equation over the Reduced Biquaternions* (`articles_maths/hermitian-solutions-of-the-pair-matrix-equation-over-the-reduced-biquaternions.md`), for the pair equation in the source's Hermitian set, which is not a structure of entry type, and for the real reduction that replaces the L-structure reduction.
