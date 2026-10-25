# __The Moore–Penrose Inverse of a Matrix__

## Introduction

For a square invertible matrix the inverse is the matrix that undoes the multiplication. For a singular or rectangular matrix there is no inverse, but there is a canonical replacement: the **Moore–Penrose inverse** $A^{+}\in M_{n\times m}(\mathbb{C})$, the unique matrix satisfying the four Penrose equations

$$
AA^{+}A=A,\qquad A^{+}AA^{+}=A^{+},\qquad (AA^{+})^{*}=AA^{+},\qquad (A^{+}A)^{*}=A^{+}A .
$$

It exists for every matrix, and it inverts $A$ between the row space and the column space, with zero on the two orthogonal complements. This article gives the closed forms, the four subspaces it determines, its least-squares reading, the limit formula that produces it as a regularised inverse, and the discontinuity at the matrices where the rank drops.

The general theory is *The Moore–Penrose Inverse in an Involutive Algebra*: the four equations, their uniqueness, the characterisation by the two ideals and the algebraic identities are proved there for an arbitrary algebra with involution, and they are cited here rather than repeated. The matrix case adds three things: the rank factorisation, which gives the inverse in closed form; the singular value form, which gives it entry by entry in a unitary basis; and the numerical analysis, the least-squares reading and the limit formula. The tensor case is *The Moore-Penrose Inverse of a Reduced Biquaternion Tensor*; the biquaternion case, where the inverse of a Hermitian factor drives the polar decomposition, is *The Polar Decomposition of a Biquaternion*.

Throughout, $A\in M_{m\times n}(\mathbb{C})$, $A^{*}=\overline{A}^{\mathsf T}$ is the conjugate transpose, and $I=I_{m}$ or $I_{n}$ according to the side. The rank is $\operatorname{rk}A$. A **projection** is a matrix $\Pi$ with $\Pi^{2}=\Pi=\Pi^{*}$, that is the orthogonal projection onto its range. The **operator norm** is $\lVert A\rVert_{2}=\max_{\lVert x\rVert=1}\lVert Ax\rVert$ and the **Frobenius norm** is $\lVert A\rVert_{F}^{2}=\operatorname{Tr}(A^{*}A)$. On square matrices the conjugate transpose is the involution of the algebra $M_{n}(\mathbb{C})$, and it is the only involution used; on rectangular matrices it maps $M_{m\times n}(\mathbb{C})$ to $M_{n\times m}(\mathbb{C})$ and is read with it.

## The Four Conditions

**Definition.** A **Moore–Penrose inverse** of $A$ is a matrix $A^{+}\in M_{n\times m}(\mathbb{C})$ satisfying the four Penrose equations above.

**Theorem (existence and uniqueness).** Every matrix has exactly one Moore–Penrose inverse.

*Proof.* Uniqueness is the theorem of *The Moore–Penrose Inverse in an Involutive Algebra*, §*Uniqueness*; existence is proved by the rank factorisation of the next section. $\square$

**Theorem (the four subspaces).** The two products are the orthogonal projections onto the column and the row space, and their complements are the projections onto the two null spaces:

$$
AA^{+}=\Pi_{\operatorname{col}A},\qquad
A^{+}A=\Pi_{\operatorname{row}A},\qquad
I_{m}-AA^{+}=\Pi_{\ker A^{*}},\qquad
I_{n}-A^{+}A=\Pi_{\ker A}.
$$

*Proof.* By the lemma of *The Moore–Penrose Inverse in an Involutive Algebra*, §*The Four Conditions*, the product $AA^{+}$ is a projection whose range is the column space of $A$, and $A^{+}A$ is a projection whose range is the row space. A projection in the sense of the definition is self-adjoint, so it is the orthogonal projection onto its range. The complements follow from $\operatorname{col}A\oplus\ker A^{*}=\mathbb{C}^{m}$ and $\operatorname{row}A\oplus\ker A=\mathbb{C}^{n}$. $\square$

**Corollary (the rank).** The four matrices $A$, $A^{+}$, $AA^{+}$ and $A^{+}A$ have the same rank,

$$
\operatorname{rk}A^{+}=\operatorname{rk}A=\operatorname{rk}AA^{+}=\operatorname{rk}A^{+}A=\operatorname{Tr}(AA^{+}),
$$

and $\operatorname{rk}A^{+}$ is the number of nonzero singular values of $A$.

*Proof.* The projection $AA^{+}$ has rank equal to the dimension of its range, the column space, and its trace is its rank; the same for $A^{+}A$. The matrix $A^{+}$ maps the column space isomorphically onto the row space, so its rank is the same. $\square$

The four equations therefore carry the whole subspace geometry of $A$: the column space, the row space and the two null spaces are read from the inverse and from the products.

## The Rank Factorisation

**Theorem (the factorisation).** Let $A$ have rank $r>0$. Then $A=CR$ with $C\in M_{m\times r}$ of full column rank and $R\in M_{r\times n}$ of full row rank, and

$$
\boxed{\;A^{+}=R^{*}\bigl(RR^{*}\bigr)^{-1}\bigl(C^{*}C\bigr)^{-1}C^{*}\;}
$$

with $A^{+}=0$ when $A=0$.

*Proof.* Choose $r$ linearly independent columns of $A$ and let $C$ be the matrix they form; every column of $A$ is a linear combination of them, and the coefficients form the columns of $R$. Then $C$ has full column rank and $R$ has full row rank, so $C^{*}C$ and $RR^{*}$ are invertible. Put $B=R^{*}(RR^{*})^{-1}(C^{*}C)^{-1}C^{*}$. Then

$$
ABA=C\bigl(RR^{*}\bigr)\bigl(RR^{*}\bigr)^{-1}\bigl(C^{*}C\bigr)^{-1}\bigl(C^{*}C\bigr)R=CR=A,
$$

$$
BAB=R^{*}\bigl(RR^{*}\bigr)^{-1}\bigl(C^{*}C\bigr)^{-1}\bigl(C^{*}C\bigr)\bigl(RR^{*}\bigr)\bigl(RR^{*}\bigr)^{-1}\bigl(C^{*}C\bigr)^{-1}C^{*}=B,
$$

and

$$
AB=C\bigl(C^{*}C\bigr)^{-1}C^{*},\qquad BA=R^{*}\bigl(RR^{*}\bigr)^{-1}R,
$$

which are the orthogonal projections onto the column space of $C$ and the row space of $R$, hence self-adjoint. The four equations hold, and uniqueness gives $B=A^{+}$. $\square$

**Corollary (full column rank).** If $A$ has full column rank, $r=n$, then $A^{+}=(A^{*}A)^{-1}A^{*}$.

**Corollary (full row rank).** If $A$ has full row rank, $r=m$, then $A^{+}=A^{*}(AA^{*})^{-1}$.

*Proof.* If $r=n$, then $R$ is invertible and $R^{*}(RR^{*})^{-1}=R^{-1}$, so the formula reads $A^{+}=R^{-1}(C^{*}C)^{-1}C^{*}=(A^{*}A)^{-1}A^{*}$, since $A=CR$. If $r=m$, then $C$ is invertible and $(C^{*}C)^{-1}C^{*}=C^{-1}$, so the formula reads $A^{+}=R^{*}(RR^{*})^{-1}C^{-1}=A^{*}(AA^{*})^{-1}$. $\square$

**Corollary (rank one).** For nonzero $u\in\mathbb{C}^{m}$ and $v\in\mathbb{C}^{n}$,

$$
\bigl(uv^{*}\bigr)^{+}=\frac{vu^{*}}{\lVert u\rVert^{2}\lVert v\rVert^{2}} .
$$

*Proof.* Take $C=u$ and $R=v^{*}$: $C^{*}C=\lVert u\rVert^{2}$ and $RR^{*}=\lVert v\rVert^{2}$. $\square$

**Example.** For

$$
A=\begin{pmatrix}1&1\\0&0\end{pmatrix}
$$

one may take $C=\binom{1}{0}$ and $R=(1\ \ 1)$, so $C^{*}C=1$ and $RR^{*}=2$, and

$$
A^{+}=R^{*}\bigl(RR^{*}\bigr)^{-1}\bigl(C^{*}C\bigr)^{-1}C^{*}
=\frac12\binom{1}{1}\bigl(1\ \ 0\bigr)
=\frac12\begin{pmatrix}1&0\\1&0\end{pmatrix}.
$$

The product $AA^{+}$ is the projection onto the line of $\binom{1}{0}$, which is $\begin{pmatrix}1&0\\0&0\end{pmatrix}$, and $A^{+}A$ is the projection onto the line of $(1\ \ 1)$, which is $\tfrac12 J$. The two differ, so $AA^{+}\neq A^{+}A$.

## The Singular Value Form

**Definition.** A **singular value decomposition** of $A$ is a factorisation

$$
A=U D V^{*},
$$

with $U\in M_{m}(\mathbb{C})$ and $V\in M_{n}(\mathbb{C})$ unitary, and $D\in M_{m\times n}(\mathbb{C})$ diagonal with entries $\mu_{1}\ge\dots\ge\mu_{r}>0$ and all further entries zero. The numbers $\mu_{1},\dots,\mu_{r}$ are the **singular values** of $A$.

Every matrix has such a factorisation: it is the diagonalisation of the self-adjoint positive semidefinite matrix $A^{*}A$ in an orthonormal basis, the finite-dimensional spectral theorem, which belongs to the spectral theory of Part III and is used here without proof.

**Proposition (the inverse in the unitary basis).** If $A=UDV^{*}$, then

$$
\boxed{\;A^{+}=V D^{+} U^{*}\;}
$$

with $D^{+}\in M_{n\times m}(\mathbb{C})$ the diagonal matrix with entries $1/\mu_{1},\dots,1/\mu_{r}$ and zeros elsewhere.

*Proof.* The diagonal matrix $D^{+}$ satisfies $DD^{+}D=D$, $D^{+}DD^{+}=D^{+}$, and the two products $DD^{+}$ and $D^{+}D$ are real diagonal projections; the four equations for $A$ and $VD^{+}U^{*}$ follow by inserting $UU^{*}=I_{m}$ and $VV^{*}=I_{n}$. Uniqueness gives the formula. $\square$

**Corollary (diagonal matrices).** For a diagonal matrix $\Lambda=\operatorname{diag}(\lambda_{1},\dots,\lambda_{n})$,

$$
\Lambda^{+}=\operatorname{diag}\bigl(\lambda_{1}^{+},\dots,\lambda_{n}^{+}\bigr),\qquad
\lambda_{i}^{+}=\begin{cases}1/\lambda_{i}, & \lambda_{i}\neq0,\\ 0, & \lambda_{i}=0.\end{cases}
$$

**Corollary (the rank and the norms).** The rank of $A$ is the number of nonzero singular values $r$. For $r\ge1$,

$$
\bigl\lVert A^{+}\bigr\rVert_{2}=\frac{1}{\mu_{r}},\qquad
\bigl\lVert A^{+}\bigr\rVert_{F}^{2}=\sum_{i=1}^{r}\frac{1}{\mu_{i}^{2}},
$$

with $\mu_{r}$ the smallest nonzero singular value; for $A=0$ both norms vanish.

*Proof.* The nonzero singular values of $A^{+}$ are the reciprocals of those of $A$, and the norms are read on the diagonal. $\square$

**Corollary (unitary invariance).** For unitary $U$ and $V$,

$$
\bigl(UAV^{*}\bigr)^{+}=VA^{+}U^{*}.
$$

*Proof.* Insert the decomposition, or apply the unitary-factor proposition of *The Moore–Penrose Inverse in an Involutive Algebra*, §*The Algebra of the Inverse*, twice. $\square$

**Example.** For $A=\operatorname{diag}(3,0)$ one has $A^{+}=\operatorname{diag}(1/3,0)$, and for $A=\operatorname{diag}(3,2)$ one has $A^{+}=\operatorname{diag}(1/3,1/2)$.

## Least Squares

**Theorem (the least-squares reading).** For $b\in\mathbb{C}^{m}$, the minimisers of $\lVert Ax-b\rVert_{2}$ are exactly the vectors

$$
x=A^{+}b+\bigl(I_{n}-A^{+}A\bigr)y,\qquad y\in\mathbb{C}^{n},
$$

and among them $A^{+}b$ is the unique vector of least norm.

*Proof.* Decompose $b=b_{1}+b_{2}$ with $b_{1}=AA^{+}b\in\operatorname{col}A$ and $b_{2}=(I_{m}-AA^{+})b\in\ker A^{*}=(\operatorname{col}A)^{\perp}$. For every $x$,

$$
\lVert Ax-b\rVert^{2}=\lVert Ax-b_{1}\rVert^{2}+\lVert b_{2}\rVert^{2},
$$

because $Ax-b_{1}\in\operatorname{col}A$ is orthogonal to $b_{2}$. The minimum is therefore attained exactly when $Ax=b_{1}$, and $x=A^{+}b$ is one such vector. Every solution is $A^{+}b+z$ with $Az=0$, that is with $z\in\ker A$, and $\ker A=(I_{n}-A^{+}A)\mathbb{C}^{n}$ by the theorem of §*The Four Conditions*; this gives the stated family. Finally $A^{+}b=A^{+}AA^{+}b$ lies in the range of $A^{+}A$, the row space, which is orthogonal to $\ker A$; hence $A^{+}b$ is orthogonal to every $z\in\ker A$ and is the minimiser of least norm. $\square$

**Corollary (the normal equations).** The least-squares minimisers are the solutions of

$$
A^{*}Ax=A^{*}b,
$$

and $A^{+}b$ is the solution of least norm.

*Proof.* $Ax-b_{1}$ is orthogonal to the column space exactly when $A^{*}(Ax-b)=0$. $\square$

**Corollary (consistent systems).** The system $Ax=b$ is solvable exactly when $AA^{+}b=b$, and then its solutions are $A^{+}b+(I_{n}-A^{+}A)y$, with $A^{+}b$ the solution of least norm.

*Proof.* The system is solvable exactly when $b=b_{1}$, that is when $AA^{+}b=b$; the rest is the theorem. $\square$

## The Limit Formula

**Theorem (the regularised inverse).** For every matrix,

$$
\boxed{\;A^{+}=\lim_{\epsilon\to0^{+}}\bigl(A^{*}A+\epsilon I_{n}\bigr)^{-1}A^{*}
=\lim_{\epsilon\to0^{+}}A^{*}\bigl(AA^{*}+\epsilon I_{m}\bigr)^{-1}\;}
$$

*Proof.* For $\epsilon>0$ the matrix $A^{*}A+\epsilon I_{n}$ is invertible, because

$$
x^{*}\bigl(A^{*}A+\epsilon I_{n}\bigr)x=\lVert Ax\rVert^{2}+\epsilon\lVert x\rVert^{2}\ge\epsilon\lVert x\rVert^{2}.
$$

Insert $A=UDV^{*}$. Then

$$
\bigl(A^{*}A+\epsilon I_{n}\bigr)^{-1}A^{*}
=V\bigl(D^{*}D+\epsilon I_{n}\bigr)^{-1}D^{*}U^{*}
=V\operatorname{diag}\Bigl(\frac{\mu_{i}}{\mu_{i}^{2}+\epsilon}\Bigr)U^{*},
$$

with zeros in the remaining diagonal entries, and each fraction tends to $1/\mu_{i}$ when $\mu_{i}>0$ and to $0$ when $\mu_{i}=0$. The limit is $VD^{+}U^{*}=A^{+}$. The second identity is the first applied to $A^{*}$, with $(A^{*})^{+}=(A^{+})^{*}$. $\square$

**Remark (what the limit says).** The formula is the Tikhonov regularisation of the least-squares problem: the minimiser of $\lVert Ax-b\rVert^{2}+\epsilon\lVert x\rVert^{2}$ is $(A^{*}A+\epsilon I)^{-1}A^{*}b$, and the Moore–Penrose solution is its limit as the regularisation is removed. **The inverse of a singular matrix is the limit of the inverses of its regularisations**, and the limit is taken after the solutions, not before.

## Continuity

**Theorem (where the inverse is continuous).** The map $A\mapsto A^{+}$ is continuous at every matrix of full rank $r=\min(m,n)$, and discontinuous at every matrix of rank $r<\min(m,n)$.

*Proof.* At full rank the formulas of §*The Rank Factorisation* apply, $A^{+}=(A^{*}A)^{-1}A^{*}$ or $A^{+}=A^{*}(AA^{*})^{-1}$, and the Gram matrix is invertible in a neighbourhood; the inverse is a rational function of the entries.

For the discontinuity, let $r<\min(m,n)$ and choose $u\notin\operatorname{col}A$ and $v\notin\operatorname{row}A$. For $k\ge1$ put $A_{k}=A+\frac1k uv^{*}$. Then $\operatorname{col}A_{k}$ strictly contains $\operatorname{col}A$, so $\operatorname{rk}A_{k}=r+1$, and $A_{k}\to A$. The singular values depend continuously on the entries, being the square roots of the eigenvalues of the continuous family $A_{k}^{*}A_{k}$, so $\mu_{r+1}(A_{k})\to\mu_{r+1}(A)=0$. By the norm formula of §*The Singular Value Form*,

$$
\bigl\lVert A_{k}^{+}\bigr\rVert_{2}=\frac{1}{\mu_{r+1}(A_{k})}\longrightarrow\infty,
$$

while $\lVert A^{+}\rVert_{2}$ is finite. Hence $A_{k}^{+}$ does not converge to $A^{+}$, and the map is discontinuous at $A$. $\square$

**Example.** The family

$$
A_{\epsilon}=\begin{pmatrix}1&0\\0&\epsilon\end{pmatrix}\longrightarrow A=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
A_{\epsilon}^{+}=\begin{pmatrix}1&0\\0&1/\epsilon\end{pmatrix},
$$

shows the blow-up at the rank drop: the limit of the inverses does not exist, and the value at the limit is $\operatorname{diag}(1,0)$.

**Remark (the two discontinuities).** The discontinuity here is an unbounded one: the inverse leaves every norm ball as the rank drops. It is not the discontinuity of the polar factor of *The Polar Decomposition of a Biquaternion*, where the isometry factor jumps between two bounded values at the null cone. **The Moore–Penrose inverse is a continuous function of the matrix exactly on the full-rank stratum**, and its values on the lower strata are limits only in the regularised sense of §*The Limit Formula*.

## The Algebra of the Inverse

The identities are those of *The Moore–Penrose Inverse in an Involutive Algebra*, §*The Algebra of the Inverse*, read in matrices:

| identity | matrix form |
|---|---|
| involution | $(A^{+})^{+}=A$ |
| adjoint | $(A^{*})^{+}=(A^{+})^{*}$ |
| product with the adjoint | $(AA^{*})^{+}=(A^{+})^{*}A^{+}$, $(A^{*}A)^{+}=A^{+}(A^{+})^{*}$ |
| factorisation | $A^{+}=(A^{*}A)^{+}A^{*}=A^{*}(AA^{*})^{+}$ |
| unitary factors | $(UA)^{+}=A^{+}U^{*}$, $(AV)^{+}=V^{*}A^{+}$ |
| rank | $\operatorname{rk}A^{+}=\operatorname{rk}A$ |

**Remark (the product rule fails).** The identity $(AB)^{+}=B^{+}A^{+}$ does not hold in general. With

$$
A=\begin{pmatrix}1&1\end{pmatrix},\qquad B=\begin{pmatrix}1\\0\end{pmatrix},
$$

one has $AB=1$, hence $(AB)^{+}=1$, while $B^{+}A^{+}=\tfrac12$. **The product rule fails by the factor two**, and the failure is not repaired by the rank: both factors have full rank. The rule holds when one factor is unitary, by the table above.

## Summary

The Moore–Penrose inverse of a matrix is the unique solution of the four Penrose equations, and it is the inverse of the matrix read between the row space and the column space.

| item | result |
|---|---|
| definition | $AA^{+}A=A$, $A^{+}AA^{+}=A^{+}$, $(AA^{+})^{*}=AA^{+}$, $(A^{+}A)^{*}=A^{+}A$ |
| domain | every $A\in M_{m\times n}(\mathbb{C})$ |
| range | $A^{+}\in M_{n\times m}(\mathbb{C})$ |
| rank factorisation | $A=CR$, $A^{+}=R^{*}(RR^{*})^{-1}(C^{*}C)^{-1}C^{*}$ |
| full column rank | $A^{+}=(A^{*}A)^{-1}A^{*}$ |
| full row rank | $A^{+}=A^{*}(AA^{*})^{-1}$ |
| singular values | $A=UDV^{*}$, $A^{+}=VD^{+}U^{*}$ |
| rank one | $(uv^{*})^{+}=vu^{*}/(\lVert u\rVert^{2}\lVert v\rVert^{2})$ |
| projections | $AA^{+}=\Pi_{\operatorname{col}A}$, $A^{+}A=\Pi_{\operatorname{row}A}$ |
| least squares | $A^{+}b$ is the minimum-norm least-squares solution of $Ax=b$ |
| limit | $A^{+}=\lim_{\epsilon\to0}(A^{*}A+\epsilon I)^{-1}A^{*}$ |
| continuity | continuous on the full-rank stratum, discontinuous at every rank drop |

The three statements to carry away are these. The inverse exists for every matrix and is computed by the rank factorisation or by the singular value decomposition. The four subspaces of the matrix are read from the two products, and the inverse is the inverse of $A$ between the row space and the column space, with zero on the complements. The inverse solves the least-squares problem in the minimum-norm sense, is the limit of the regularised inverses, and is continuous exactly where the rank does not drop.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A$ | a matrix in $M_{m\times n}(\mathbb{C})$ |
| $A^{*}$ | the conjugate transpose |
| $A^{+}$ | the Moore–Penrose inverse |
| $\Pi_{V}$ | the orthogonal projection onto the subspace $V$ |
| $\operatorname{col}A$, $\operatorname{row}A$ | the column space and the row space |
| $\ker A$, $\ker A^{*}$ | the null space and the left null space |
| $\operatorname{rk}A$ | the rank |
| $\mu_{1},\dots,\mu_{r}$ | the nonzero singular values |
| $D^{+}$ | the diagonal matrix of reciprocal nonzero entries |
| $\lVert\cdot\rVert_{2}$, $\lVert\cdot\rVert_{F}$ | the operator norm and the Frobenius norm |

## Further Reading

- Roger Penrose, "A generalized inverse for matrices", *Proceedings of the Cambridge Philosophical Society* **51** (1955) 406–413. The four equations, their uniqueness, and the first systematic treatment of the singular case.
- Eliakim H. Moore, "On the reciprocal of the general algebraic matrix", *Bulletin of the American Mathematical Society* **26** (1920) 394–395. The earliest formulation of the reciprocal of a singular matrix.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013). The singular value decomposition, the rank factorisation, the pseudo-inverse and the numerical algorithms.
- Adi Ben-Israel and Thomas N. E. Greville, *Generalized Inverses: Theory and Applications*, 2nd edition (Springer, 2003). The algebraic and the least-squares theory of the inverse.
- Åke Björck, *Numerical Methods for Least Squares Problems* (SIAM, 1996). The minimum-norm least-squares solution, the normal equations and the regularised limit.
- Charles L. Lawson and Richard J. Hanson, *Solving Least Squares Problems* (Prentice-Hall, 1974; SIAM, 1995). The computational treatment of the pseudo-inverse and the rank-deficient problem.
