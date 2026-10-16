# __Non-Negative Matrix Factorization over the Reduced Biquaternions__

## Introduction

Non-negative matrix factorization writes a non-negative matrix as a product of two non-negative matrices of lower rank and reads the result as a basis and a coefficient matrix. Over the reduced biquaternions the same construction is available, and it is constrained by the algebra in a way the real and the complex cases are not: the product of two non-negative reduced biquaternion matrices need not be non-negative, so the constraint must be placed on the **structure** of one of the two factors and not on its non-negativity alone. The model of the literature is
$$
X\approx WH,\qquad W\in\mathbb{B}_{\mathrm{r}}^{m\times l},\quad H\in\mathbb{B}_{\mathrm{r}}^{l\times n},\qquad X\succeq0,\quad W\succeq0,\quad H=H_0+H_2j\ \text{with}\ H_0,H_2\ \text{real non-negative},
$$
where $\succeq0$ means that the four coefficient matrices of the matrix are real non-negative matrices, which is the entrywise reading of the non-negative cone of the algebra, and where the coefficient matrix $H$ is restricted to the elements of the form $h_0+h_2j$ with $h_0,h_2\ge0$. The restriction is exactly what makes the product non-negative, and it is the reason the reduced biquaternion case is more than a doubling of the real one.

**The results.** The non-negative matrices form the cone $\mathcal{C}_{+}^{m\times n}$, four real non-negative coefficient matrices read together, and the structured matrices form the smaller cone $\mathcal{O}^{m\times n}$, the orthant of the split-complex subring $\mathbb{R}\{1,j\}$; both are closed convex cones. The **product formula** $WH=(W_0H_0+W_2H_2)+(W_1H_0+W_3H_2)i+(W_0H_2+W_2H_0)j+(W_1H_2+W_3H_0)ij$ shows the **closure**: if $W\succeq0$ and $H$ is structured then $WH\succeq0$, every component of the product being a sum of products of non-negative real matrices; and it shows that the constraint on $H$ cannot be weakened to non-negativity, since $i\cdot i=-1$. The **non-negative reduced biquaternion rank** of $X$, the least $l$ for which an exact factorization exists, is defined and is at most $\min(m,n)$; a factorization with a real basis matrix produces only structured data, so data outside $\mathcal{O}$ forces a basis matrix with a nonzero $i$- or $ij$-component. Under the isomorphism with $\mathbb{C}\oplus\mathbb{C}$ the product becomes the two products $X^{\pm}=W^{\pm}H^{\pm}$ and the objective becomes half the sum of the two complex Frobenius norms, so the reconstruction **decouples** into two complex factorizations; the constraints do **not** decouple, because the two factors descend from the four real matrices $W_0,\dots,W_3$ and the two real matrices $H_0,H_2$, and they read $H^{+}\ge|H^{-}|$ entrywise together with the four sum-and-difference inequalities of $W^{\pm}$. The **graph regularizer** of the graph-regularized model is the Dirichlet energy of the graph applied to the two real coefficient matrices, $R(H)=\operatorname{tr}(H_0LH_0^{\top})+\operatorname{tr}(H_2LH_2^{\top})$, and it splits into the two components and into the two real factorizations. The **alternating projected gradient method** gives a nonincreasing objective and, in the limit, a first-order stationary point.

**Boundaries.** The cone, the order and the cone-preserving elements are *The Non-Negative Cone and the Coordinatewise Order of the Reduced Biquaternions*; the four components and the product rule are *The Four Products, Their Forms and Their Algebraic Norms* and *Reduced Biquaternion Other Algebraic Element Representations*; the isomorphism with $\mathbb{C}\oplus\mathbb{C}$, the idempotent coordinates and the two-fold reduction are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$* and *Least Squares and Total Least Squares over the Reduced Biquaternions*, whose reduction of a matrix equation to two complex equations is the model of the reduction below. The Euclidean and the Frobenius norms are *The Euclidean Topology of the Reduced Biquaternion Algebra*; the graph, its Laplacian and the identity $\tfrac12\sum_{m,n}A_{mn}\lVert s_m-s_n\rVert^{2}=\operatorname{tr}(SLS^{\top})$ are *Graph Theory*, *The Hodge Laplacian* and *Dirichlet Forms and the Hermitian Dirichlet Principle*. The general theory of the cone and of the projection is *Ordered Vector Spaces and the Order Unit*, *The Cone of Positive Operators* and *Positive Operators on an Ordered Space*.

**Conventions.** A matrix over $\mathbb{B}_{\mathrm{r}}$ is written $M=M_0+M_1 i+M_2 j+M_3 ij$ with the four **component matrices** $M_\ell$ real, and the source's symbol $k$ is this $ij$. The matrix is **non-negative**, written $M\succeq0$, when the four component matrices are entrywise non-negative; the non-negative matrices form the cone $\mathcal{C}_{+}^{m\times n}$. The matrix is **structured**, written $M\in\mathcal{O}^{m\times n}$, when $M_1=M_3=0$ and $M_0,M_2\ge0$ entrywise, that is when $M=M_0+M_2j$ with both real component matrices non-negative; the structured matrices form the cone $\mathcal{O}^{m\times n}$, the source's $\mathrm{RB}_{+j}^{l\times N}$. The **reduced biquaternion Frobenius norm** is $\lVert M\rVert_{\mathrm F}^{2}=\operatorname{Re}\langle M,M\rangle=\sum_{m,n}K(m_{mn})$, and the reconstruction error is $\tfrac12\lVert X-WH\rVert_{\mathrm F}^{2}$. The idempotent components of a matrix are $M^{\pm}=M_0\pm M_2+i(M_1\pm M_3)$, the projections of the isomorphism $\varphi$, and $\varphi_\pm(M)=M^{\pm}$; the source's factorisation rank is $l$, the number of columns of $W$, and its $\succeq$ on matrices is the same symbol as the elementwise cone.

## The Non-Negative Matrices and Their Product

**The non-negative matrices and the structured matrices are two cones, the second inside the first, and the product of a non-negative matrix with a structured one is non-negative.**

### The Two Cones of Matrices

**Definition.** A matrix $M\in\mathbb{B}_{\mathrm{r}}^{m\times n}$ is **non-negative** when its four component matrices are entrywise non-negative, $M_\ell\ge0$ for $\ell=0,1,2,3$; the set of them is $\mathcal{C}_{+}^{m\times n}$, the product of the cones $\mathcal{C}_{+}$ over the $mn$ entries. The matrix is **structured** when $M=M_0+M_2j$ with $M_0\ge0$ and $M_2\ge0$ entrywise; the set of them is $\mathcal{O}^{m\times n}$, the product of the orthants $\mathcal{O}$ over the entries.

**Theorem (the two cones).** Both $\mathcal{C}_{+}^{m\times n}$ and $\mathcal{O}^{m\times n}$ are closed convex pointed cones of the real vector space of the matrices, with nonempty interior and with the entrywise order, and
$$
\mathcal{O}^{m\times n}\subsetneq\mathcal{C}_{+}^{m\times n}
$$
unless $mn=0$. The larger cone $\mathcal{C}_{+}^{m\times n}$ is self-dual for the entrywise Euclidean inner product $\operatorname{Re}K$; the smaller cone $\mathcal{O}^{m\times n}$ is self-dual for $\operatorname{Re}K$ **within the split-complex subspace** $\mathbb{R}\{1,j\}^{m\times n}$ it generates, and it is not self-dual in the ambient space.

*Proof.* Each is a finite product of the cones $\mathcal{C}_{+}$ and $\mathcal{O}$ of *The Non-Negative Cone and the Coordinatewise Order of the Reduced Biquaternions*, with the product entry and the product inner product. The product of closed convex pointed cones is closed, convex and pointed, and the interior is the product of the interiors. The inclusion is entrywise, and it is proper because the matrix $iI$ is non-negative and not structured. The self-duality of $\mathcal{C}_{+}$ for $\operatorname{Re}K$ is entrywise; for $\mathcal{O}$ the ambient dual is the larger cone $\{W:W_0\ge0,\ W_2\ge0\}$, of dimension $4mn$, so the self-duality holds only in the subspace $\{W_1=W_3=0\}$, where the coordinates $(h_0,h_2)$ repeat the one-element computation.

### The Product Formula

**Theorem (the product formula).** For $W=W_0+W_1 i+W_2 j+W_3 ij$ and $H=H_0+H_2 j$, the product has the four components
$$
WH=(W_0H_0+W_2H_2)+(W_1H_0+W_3H_2)\,i+(W_0H_2+W_2H_0)\,j+(W_1H_2+W_3H_0)\,ij .
$$

*Proof.* Multiply the two sums termwise using the table $i^{2}=-1$, $j^{2}=+1$, $ji=ij$ and the commutativity of the algebra. The sixteen products reduce, since $H_1=H_3=0$, to the eight displayed, and the component matrices commute with the scalars $i$ and $j$ because they are real.

**Theorem (the closure of the product).** If $W\succeq0$ and $H\in\mathcal{O}$, then $WH\succeq0$. More precisely, the four component matrices of the product are
$$
(WH)_0=W_0H_0+W_2H_2,\quad (WH)_1=W_1H_0+W_3H_2,\quad (WH)_2=W_0H_2+W_2H_0,\quad (WH)_3=W_1H_2+W_3H_0,
$$
and each is a sum of products of entrywise non-negative real matrices, hence entrywise non-negative.

*Proof.* The formula is the theorem above; the sum of products of non-negative matrices is non-negative, since the entries of a product of non-negative matrices are sums of products of non-negative numbers. This is the reason the source imposes the structured constraint on $H$ and no more.

**Proposition (the constraint cannot be weakened).** If the coefficient constraint is relaxed from the structured cone to the non-negative cone, then the product of two non-negative matrices need not be non-negative: the matrices $W=iI$ and $H=iI$ are both non-negative and
$$
(iI)(iI)=i^{2}I=-I,
$$
which is not non-negative.

*Proof.* The reduced biquaternion unit $i$ has square $-1$, so the diagonal matrix $iI$, all of whose four component matrices are the non-negative matrices $I,0,0,0$, has non-negative factors and a negative product. The structured cone removes the $i$- and the $ij$-components of $H$, which is exactly what makes the product non-negative; the constraint is indispensable and not cosmetic.

**Remark (why the two cones are the two correct ones).** The cone of the elements whose left multiplication carries $\mathcal{C}_{+}$ into itself is $\mathcal{O}$, and it is a proper subcone of $\mathcal{C}_{+}$ (*The Non-Negative Cone and the Coordinatewise Order of the Reduced Biquaternions*). The closure theorem is the entrywise form of that statement over the entries common to the two matrices, and the negative result is the entrywise form of the failure at a single entry.

## The Factorization Problem and the Non-Negative Rank

**The factorization problem is the minimization of the reconstruction error over the two cones, and the rank is the least inner dimension for which it is exact.**

**Definition.** For a non-negative matrix $X\in\mathcal{C}_{+}^{m\times n}$ and an integer $l\le\min(m,n)$, the **non-negative reduced biquaternion factorization problem** is
$$
\min_{W,H}\ \tfrac12\lVert X-WH\rVert_{\mathrm F}^{2}\qquad\text{subject to}\quad W\in\mathcal{C}_{+}^{m\times l},\quad H\in\mathcal{O}^{l\times n}.
$$
The **non-negative reduced biquaternion rank** of $X$ is the least $l$ for which the minimum is $0$, that is for which $X=WH$ with $W\succeq0$ and $H\in\mathcal{O}^{l\times n}$; it is written $\operatorname{rank}_{+}(X)$.

**Theorem (the rank is defined and bounded).** Every non-negative matrix has a non-negative reduced biquaternion rank, and
$$
\operatorname{rank}_{+}(X)\le\min(m,n).
$$

*Proof.* If $m\le n$, take $W=[\,X\ \ 0\,]\in\mathbb{B}_{\mathrm{r}}^{m\times n}$, the matrix $X$ followed by $n-m$ zero columns, and $H=[\,I_m\ \ 0\,]^{\top}\in\mathcal{O}^{n\times m}$, the identity on top of $n-m$ zero rows; then $WH=X$, both factors are in their cones, and $l=m$. If $n\le m$, take $W=X\in\mathcal{C}_{+}^{m\times n}$ and $H=I_n\in\mathcal{O}^{n\times n}$; then $WH=X$ and $l=n$. In both cases an exact factorization with $l=\min(m,n)$ is exhibited, so the set over which the minimum is taken is nonempty and the rank is at most $\min(m,n)$.

**Proposition (a real basis forces structured data).** If the basis matrix is real non-negative, $W=W_0\ge0$ with $W_1=W_2=W_3=0$, and $H\in\mathcal{O}$, then $X=WH$ is structured,
$$
X=W_0H_0+W_0H_2j\in\mathcal{O}^{m\times n}.
$$
Consequently, if $X\notin\mathcal{O}$ then every exact factorization has a basis matrix that is not real, that is with $W_1\neq0$ or $W_3\neq0$.

*Proof.* With $W_2=W_3=0$ the product formula gives $(WH)_0=W_0H_0$, $(WH)_1=W_1H_0+W_3H_2=0$, $(WH)_2=W_0H_2$ and $(WH)_3=W_1H_2+W_3H_0=0$; so $WH=W_0H_0+W_0H_2j$ with both components non-negative. The contrapositive is the second statement.

**Remark (rank against dimension).** The rank is the inner dimension of the cone factorization, and the constraint set is a product of cones and not a linear space, so the rank is not the algebraic rank and is not additive; it is the reduced biquaternion analogue of the non-negative rank of the real theory, and the same three faces appear — the trivial bound, the structured case, and the combinatorial character of the exactness. The reduced biquaternion algebraic rank, by contrast, is the pair of complex ranks of the two idempotent components, since the algebra is the direct product $\mathbb{C}\oplus\mathbb{C}$.

## The Coefficient Reduction

**Under the isomorphism with $\mathbb{C}\oplus\mathbb{C}$ the objective becomes half the sum of two complex Frobenius norms, but the constraints remain coupled through the four real component matrices.**

**Theorem (the product in the two idempotent components).** Let $W^{\pm}=W_0\pm W_2+i(W_1\pm W_3)$ and let $H^{\pm}=H_0\pm H_2$, so that $W^{\pm}$ are the two complex matrices $\varphi_\pm(W)$ and $H^{\pm}$ are the two real matrices $\varphi_\pm(H)$. Then
$$
(WH)^{\pm}=W^{\pm}H^{\pm},
$$
and the objective satisfies
$$
\tfrac12\lVert X-WH\rVert_{\mathrm F}^{2}=\tfrac14\lVert X^{+}-W^{+}H^{+}\rVert_{\mathrm F}^{2}+\tfrac14\lVert X^{-}-W^{-}H^{-}\rVert_{\mathrm F}^{2}.
$$

*Proof.* The map $\varphi$ is an isomorphism of algebras onto $\mathbb{C}\oplus\mathbb{C}$, so $\varphi(WH)=\varphi(W)\varphi(H)$ and the two components multiply separately; that is the first identity. For the second, the Frobenius norm of a matrix satisfies $\lVert M\rVert_{\mathrm F}^{2}=\sum_{p,q}K(m_{pq})$, and $K=\tfrac12(K^{+}+K^{-})$ with $K^{\pm}(z)=|z|^{2}$ on the two complex components, $K^{+}(z)=|z_1|^{2}$ and $K^{-}(z)=|z_2|^{2}$ for $z=(z_1,z_2)$; summing gives the displayed decomposition. The reduction of a matrix equation to two complex equations is that of *Least Squares and Total Least Squares over the Reduced Biquaternions*.

**Theorem (the constraints in the two components).** The structured cone reads, in the two components,
$$
H\in\mathcal{O}^{l\times n}\iff H^{+}\ \text{and}\ H^{-}\ \text{are real and}\ H_{pq}^{+}\ge|H_{pq}^{-}|\ \text{for every}\ p,q,
$$
and the non-negative cone of the basis reads
$$
W\succeq0\iff \operatorname{Re}(W^{+}+W^{-})\ge0,\quad \operatorname{Im}(W^{+}+W^{-})\ge0,\quad \operatorname{Re}(W^{+}-W^{-})\ge0,\quad \operatorname{Im}(W^{+}-W^{-})\ge0
$$
entrywise.

*Proof.* The component matrices are recovered by $H_0=\tfrac12(H^{+}+H^{-})$, $H_2=\tfrac12(H^{+}-H^{-})$, $W_0=\tfrac12\operatorname{Re}(W^{+}+W^{-})$, $W_1=\tfrac12\operatorname{Im}(W^{+}+W^{-})$, $W_2=\tfrac12\operatorname{Re}(W^{+}-W^{-})$ and $W_3=\tfrac12\operatorname{Im}(W^{+}-W^{-})$. The requirements $H_0\ge0$ and $H_2\ge0$ are $H^{+}+H^{-}\ge0$ and $H^{+}-H^{-}\ge0$, which for real entries reduce to $H^{+}_{pq}\ge|H^{-}_{pq}|$; the requirements $W_0,W_1,W_2,W_3\ge0$ are the four displayed inequalities.

**Corollary (the reduction is not a decoupling).** The two complex factorizations $X^{+}=W^{+}H^{+}$ and $X^{-}=W^{-}H^{-}$ have objective terms that add, but they are not independent: the pair $(W^{+},W^{-})$ ranges over the four inequalities above and the pair $(H^{+},H^{-})$ over the entrywise band $H^{+}\ge|H^{-}|$. In particular, if the basis is required to be real then $W^{+}=W^{-}=W_0$ and the two complex factorizations share the basis, and if the data are structured then $H^{-}$ is arbitrary within the band of $H^{+}$.

*Proof.* The identities of the two theorems give the objective and the constraints, and the recovery formulas show that the two components are the reading of the same four real matrices; the last two sentences are the specialisations $W_1=W_3=0$, giving $W^{+}=W^{-}=W_0$, and $X_1=X_3=0$, giving $H$ structured and the band $|H^{-}|\le H^{+}$ with $H^{-}$ otherwise free.

**Remark (the reduction of the rank).** The algebraic rank of a reduced biquaternion matrix is the pair of complex ranks of the two idempotent components, since the algebra is $\mathbb{C}\oplus\mathbb{C}$; the non-negative rank is not, because the cone constraints prevent the two complex factorizations from being chosen independently. The two share the basis when it is real, which is the structured case of the proposition above, and they are otherwise coupled through the four inequalities.

## The Graph Regularizer

**The graph regularizer is the Dirichlet energy of the graph applied to the two real coefficient matrices, and it splits into them.**

**Definition.** A graph on the $n$ samples is a symmetric affinity matrix $A=[A_{mn}]$ with non-negative entries, its **degree matrix** is diagonal with $D_{mm}=\sum_n A_{mn}$, and its **graph Laplacian** is $L=D-A$, a symmetric positive semidefinite matrix. The squared distance between the samples is the reduced biquaternion Frobenius one, $d_{mn}^{2}=\lVert x_m-x_n\rVert_{\mathrm F}^{2}$, and the affinity is the symmetric $0$–$1$ $p$-nearest-neighbour weight, $A_{mn}=1$ when $m\in\mathcal{N}_p(n)$ or $n\in\mathcal{N}_p(m)$.

**Theorem (the graph identity).** For a real matrix $S=[s_1,\dots,s_n]\in\mathbb{R}^{l\times n}$ and a symmetric affinity matrix,
$$
\tfrac12\sum_{m,n}A_{mn}\lVert s_m-s_n\rVert_2^{2}=\operatorname{tr}(SLS^{\top}),
$$
and the quantity is non-negative, vanishing exactly for the constant coefficient rows on each connected component of the graph.

*Proof.* Expand $\lVert s_m-s_n\rVert^{2}=\lVert s_m\rVert^{2}-2\langle s_m,s_n\rangle+\lVert s_n\rVert^{2}$ and collect the terms with the degree and the affinity, which is the displayed identity by the symmetry of $A$; the non-negativity is that $L$ is positive semidefinite, the quadratic form being a sum of squares, and the kernel of $L$ is the space of the rows constant on each component. The identity is that of *Graph Theory*, *The Hodge Laplacian* and *Dirichlet Forms and the Hermitian Dirichlet Principle*.

**Theorem (the regularizer of the reduced biquaternion coefficient matrix).** For a structured coefficient matrix $H=H_0+H_2j$ with columns $h_m=h_{0,m}+h_{2,m}j$, the energy
$$
R(H)=\tfrac12\sum_{m,n}A_{mn}\lVert h_m-h_n\rVert_{\mathrm F}^{2}
$$
satisfies
$$
\lVert h_m-h_n\rVert_{\mathrm F}^{2}=\lVert h_{0,m}-h_{0,n}\rVert_2^{2}+\lVert h_{2,m}-h_{2,n}\rVert_2^{2},
\qquad
R(H)=\operatorname{tr}(H_0LH_0^{\top})+\operatorname{tr}(H_2LH_2^{\top}).
$$
Consequently the regularizer is a sum of two Dirichlet energies, one for each real component matrix of the coefficient, and it is non-negative.

*Proof.* For the difference $h_m-h_n=(h_{0,m}-h_{0,n})+(h_{2,m}-h_{2,n})j$ the four components are $(h_{0,m}-h_{0,n},0,h_{2,m}-h_{2,n},0)$, so the reduced biquaternion Frobenius norm is the sum of the two real norms; applying the graph identity to $H_0$ and to $H_2$ separately gives the second displayed identity, and both terms are non-negative. The source obtains the same expression and observes that the regularizer meets the two nonzero components of $H$.

**Remark (the objective).** The graph-regularized model is
$$
\min_{W,H}\ \tfrac12\lVert X-WH\rVert_{\mathrm F}^{2}+\tfrac{\lambda}{2}\bigl[\operatorname{tr}(H_0LH_0^{\top})+\operatorname{tr}(H_2LH_2^{\top})\bigr]\qquad\text{subject to}\quad W\in\mathcal{C}_{+}^{m\times l},\ H\in\mathcal{O}^{l\times n},
$$
with $\lambda\ge0$ the regularization parameter; at $\lambda=0$ it is the non-negative factorization above. Because $L$ is positive semidefinite and the reconstruction error is non-negative, the objective is bounded below by $0$ on the feasible set.

## The Alternating Projected Gradient Method

**The two blocks are minimised in turn by a projected gradient step with a backtracking step size, and the objective is nonincreasing with limit points that are stationary.**

**Definition.** The **projection** onto a cone is the nearest point map $P_{\mathcal{C}}(z)=\operatorname{argmin}\{\lVert z-y\rVert:y\in\mathcal{C}\}$. For the two cones of the problem the projection is the entrywise operation: on the non-negative cone it replaces every real coordinate of every entry by its positive part, and on the structured cone it replaces every entry of the two real component matrices $H_0$ and $H_2$ by its positive part and leaves the other two matrices at zero.

**Theorem (the projection lemma).** For a closed convex cone $\mathcal{C}$, a point $z\in\mathcal{C}$, a gradient $g$ and a step $\tau>0$, the projected point $z^{+}=P_{\mathcal{C}}(z-\tau g)$ satisfies
$$
\langle g,z^{+}-z\rangle\le-\tfrac1\tau\lVert z^{+}-z\rVert^{2}\le0 .
$$

*Proof.* The optimality of the projection gives $\langle z^{+}-(z-\tau g),y-z^{+}\rangle\ge0$ for $y\in\mathcal{C}$; taking $y=z$ and rearranging gives the inequality.

**Theorem (the algorithm).** Start from feasible $W^{0}$ and $H^{0}$, and at each step set
$$
W^{t+1}=P_{\mathcal{C}_{+}}\bigl(W^{t}-\alpha_t\nabla_{W}F(W^{t},H^{t})\bigr),\qquad H^{t+1}=P_{\mathcal{O}}\bigl(H^{t}-\beta_t\nabla_{H}F(W^{t},H^{t})\bigr),
$$
where the step sizes are the first of $1,\mu,\mu^{2},\dots$ with $\mu\in(0,1)$ satisfying the Armijo condition
$$
F\bigl(W^{t+1},H^{t}\bigr)\le F\bigl(W^{t},H^{t}\bigr)+\sigma\,\operatorname{Re}\bigl\langle \nabla_{W}F(W^{t},H^{t}),\,W^{t+1}-W^{t}\bigr\rangle
$$
and its analogue for $H$, with $\sigma\in(0,1)$. Then each line search terminates after finitely many reductions, the objective is nonincreasing, it converges to a finite value, and the successive differences tend to zero, $\lVert W^{t+1}-W^{t}\rVert_{\mathrm F}\to0$ and $\lVert H^{t+1}-H^{t}\rVert_{\mathrm F}\to0$. If the sequence converges, its limit is a first-order stationary point, characterised by the complementarity of each variable with the corresponding gradient component.

*Proof.* The line search terminates because the block gradients are Lipschitz on the sublevel sets, with the moduli built from the spectral norms of the component matrices and of $L$; the sufficient decrease of the projection lemma and the descent lemma give the Armijo condition for all small enough steps, and the backtracking sequence reaches such a step after finitely many halvings. The objective is nonincreasing and bounded below, hence convergent, and the decrease at each step is controlled by the squared step, which forces the step to tend to zero. The stationarity of a limit point is the complementarity of the gradient with the active components at that point, read in the real component representation. The statements are those of the source, and they are carried out there in the real coordinates $\Phi$ and $\Phi_j$.

**Remark (the two-block structure).** The problem is nonconvex, since the feasible set is a product of cones and the objective is quadratic in the product $WH$; the alternating scheme is a block coordinate method on a product of convex sets with a smooth objective, and the two blocks are the two factors. The stationarity is first-order and the convergence is to a stationary point of the two blocks and not to a global minimum, as in the real theory of non-negative matrix factorization.

## Worked Examples

**The product of a non-negative factor and a structured factor.** For $W=iI$ and $H=jI$ the product is $ij\,I$, with components $0,0,0,I$, non-negative: the $j$ of the coefficient and the $i$ of the basis meet in the $ij$-component, and the closure theorem covers it.

**The product that leaves the cone.** For $W=iI$ and $H=iI$, both non-negative, the product is $-I$, whose first component is $-I$ and whose remaining components vanish; the product is not non-negative, which is the failure the structured constraint avoids.

**A factorization of a structured matrix.** For $X=X_0+X_2j$ with $X_0,X_2\ge0$, the choice $W=X$ and $H=I$ gives $WH=X$ with $W$ non-negative and $H$ structured of rank $n$; the basis is the data itself and the two components of the product are $X_0$ and $X_2$. The proposition above says the converse: if such an $X$ is factorised with a real basis, the product is again structured.

**The two components of the objective.** For $W^{\pm}=W_0\pm W_2+i(W_1\pm W_3)$ and $H^{\pm}=H_0\pm H_2$ the identity $(WH)^{\pm}=W^{\pm}H^{\pm}$ gives the two complex products $(W_0H_0+W_2H_2)\pm(W_0H_2+W_2H_0)+i\bigl((W_1H_0+W_3H_2)\pm(W_1H_2+W_3H_0)\bigr)$, which are the two idempotent components of the product formula; the objective is half the sum of the two squared complex errors.

**The regularizer on a two-sample graph.** For $n=2$ with $A_{12}=A_{21}=1$ the Laplacian is $L=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, and for a coefficient matrix $H$ with columns $h_1,h_2$ the energy is $R(H)=\operatorname{tr}(H_0LH_0^{\top})+\operatorname{tr}(H_2LH_2^{\top})=\tfrac12\lVert h_1-h_2\rVert_{\mathrm F}^{2}$; the regularizer pulls the two coefficient columns together in both real components and none in the two vanishing ones.

## Verification

The following identities were checked by recomputation on random non-negative matrices and random graphs of at most a few dozen entries, the deviations found at the level of the floating-point noise.

- The product formula reproduces $WH$ from the four component matrices of $W$ and the two of $H$, and for $W\succeq0$ and $H$ structured all four components of $WH$ are entrywise non-negative.
- The product of the two non-negative matrices $i$ and $i$ is $-1$, outside the cone; the structured constraint is necessary.
- The graph identity $\tfrac12\sum_{m,n}A_{mn}\lVert s_m-s_n\rVert^{2}=\operatorname{tr}(SLS^{\top})$ holds for the symmetric $0$–$1$ affinity and $L=D-A$, and the regularizer splits as $\operatorname{tr}(H_0LH_0^{\top})+\operatorname{tr}(H_2LH_2^{\top})$.
- A projected gradient step on $H$ with a small step size does not increase the graph-regularized objective, in agreement with the descent lemma and the projection lemma.
- The component matrices are recovered from the pair $H^{\pm}$ by $H_0=\tfrac12(H^{+}+H^{-})$ and $H_2=\tfrac12(H^{+}-H^{-})$, and the structured constraint is the entrywise band $H^{+}\ge|H^{-}|$.

## Summary

Over the reduced biquaternions the non-negative matrices are the cone $\mathcal{C}_{+}^{m\times n}$ of the four real non-negative component matrices, the structured matrices are the cone $\mathcal{O}^{m\times n}$ of those of the form $M_0+M_2j$ with $M_0,M_2\ge0$, and $\mathcal{O}^{m\times n}$ is a proper subcone of $\mathcal{C}_{+}^{m\times n}$. The **product formula** $WH=(W_0H_0+W_2H_2)+(W_1H_0+W_3H_2)i+(W_0H_2+W_2H_0)j+(W_1H_2+W_3H_0)ij$ gives the **closure**: a non-negative basis times a structured coefficient is non-negative, and the constraint on the coefficient cannot be weakened to non-negativity, since $i^{2}=-1$ leaves the cone. The **non-negative reduced biquaternion rank** is the least inner dimension of an exact factorization; it is at most $\min(m,n)$, and a real basis matrix produces only structured data, so a general data matrix forces a basis with a nonzero $i$- or $ij$-component.

Under the isomorphism with $\mathbb{C}\oplus\mathbb{C}$ the product becomes $X^{\pm}=W^{\pm}H^{\pm}$ and the objective becomes half the sum of the two complex Frobenius norms, so the reconstruction decouples; the constraints do not, since the two complex factors descend from the four real matrices $W_0,\dots,W_3$ and the two real matrices $H_0,H_2$, and they read as the entrywise band $H^{+}\ge|H^{-}|$ and the four sum-and-difference inequalities of $W^{\pm}$. The graph regularizer is the Dirichlet energy of the graph on the two real coefficient matrices, $R(H)=\operatorname{tr}(H_0LH_0^{\top})+\operatorname{tr}(H_2LH_2^{\top})$, non-negative and split into the two components. The alternating projected gradient method minimises the two blocks in turn, with a backtracking step size and a nonincreasing objective, and any convergent sequence has a first-order stationary limit point.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=M_0+M_1 i+M_2 j+M_3 ij$ | A reduced biquaternion matrix with the four real component matrices |
| $M\succeq0$, $\mathcal{C}_{+}^{m\times n}$ | The non-negative matrices, all four component matrices entrywise non-negative |
| $M\in\mathcal{O}^{m\times n}$ | The structured matrices, $M=M_0+M_2j$ with $M_0,M_2\ge0$; the source's $\mathrm{RB}_{+j}$ |
| $WH$ | The product, of the components displayed in §*The Product Formula* |
| $M^{\pm}=M_0\pm M_2+i(M_1\pm M_3)$ | The two idempotent components of a matrix, $\varphi_\pm(M)$ |
| $\operatorname{rank}_{+}(X)$ | The non-negative reduced biquaternion rank, the least exact inner dimension |
| $A$, $D$, $L=D-A$ | The symmetric affinity matrix, the degree matrix and the graph Laplacian |
| $R(H)=\operatorname{tr}(H_0LH_0^{\top})+\operatorname{tr}(H_2LH_2^{\top})$ | The graph regularizer, the Dirichlet energy of the two real coefficient matrices |
| $\lambda\ge0$ | The graph regularization parameter |
| $W^{t+1}=P_{\mathcal{C}_{+}}(W^{t}-\alpha_t\nabla_{W}F)$ | The projected gradient update of the basis |
| $\sigma,\mu$ | The Armijo constant and the backtracking ratio of the line search |

## Further Reading

- *The Non-Negative Cone and the Coordinatewise Order of the Reduced Biquaternions* (`articles_maths/the-non-negative-cone-and-the-coordinatewise-order-of-the-reduced-biquaternions.md`), for the cone $\mathcal{C}_{+}$, the orthant $\mathcal{O}$, the multiplicative core and the entrywise criterion for a cone-preserving multiplication.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the forms, and *Reduced Biquaternion Other Algebraic Element Representations* (`articles_maths/reduced-biquaternion-other-algebraic-element-representations.md`), for the component matrices and the multiplication rule.
- *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$* (`articles_maths/reduced-biquaternions-as-a-vector-space-over-r-and-c.md`), for the two idempotent coordinates and the isomorphism with $\mathbb{C}\oplus\mathbb{C}$.
- *Least Squares and Total Least Squares over the Reduced Biquaternions* (`articles_maths/least-squares-and-total-least-squares-over-the-reduced-biquaternions.md`), for the reduction of a matrix equation to two complex equations, the Frobenius norm as the form $K$ and the coefficient stack, on which the coefficient reduction of the present article is modelled.
- *The Euclidean Topology of the Reduced Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-reduced-biquaternion-algebra.md`), for the Euclidean norm, the inner product $\operatorname{Re}\langle\cdot,\cdot\rangle$ and the Cauchy–Schwarz inequality used on the cones.
- *Graph Theory* (`articles_maths/graph-theory.md`), *The Hodge Laplacian* (`articles_maths/the-hodge-laplacian.md`) and *Dirichlet Forms and the Hermitian Dirichlet Principle* (`articles_maths/dirichlet-forms-and-the-hermitian-dirichlet-principle.md`), for the graph, its Laplacian, the positive semidefiniteness and the identity $\tfrac12\sum A_{mn}\lVert s_m-s_n\rVert^{2}=\operatorname{tr}(SLS^{\top})$.
- *Ordered Vector Spaces and the Order Unit* (`articles_maths/ordered-vector-spaces-and-the-order-unit.md`), *The Cone of Positive Operators* (`articles_maths/the-cone-of-positive-operators.md`) and *Positive Operators on an Ordered Space* (`articles_maths/positive-operators-on-an-ordered-space.md`), for the closed convex cone, the projection and the positivity-preserving operators.
- Hailang Wu, Yonghe Liu, Bingxuan Yu and Chaoqian Li, "Graph regularized non-negative reduced biquaternion matrix factorization for color image recognition", arXiv:2606.03654v2 (2026), for the graph-regularized model, the structured constraint and the projected gradient algorithm and its convergence.
- J. F. Miao, J. J. Pan and M. K. Ng, "Non-negative reduced biquaternion matrix factorization with applications in color face recognition", arXiv:2408.05582v2 (2025), for the non-negative reduced biquaternion factorization without the graph term, of which the model above is the regularized extension.
- Daniel D. Lee and H. Sebastian Seung, "Learning the parts of objects by non-negative matrix factorization", *Nature* **401** (1999) 788–791, and "Algorithms for non-negative matrix factorization", *Advances in Neural Information Processing Systems* **13** (2000) 556–562, for the classical non-negative matrix factorization and its alternating multiplicative updates.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022, for the reduced biquaternion algebra of the engineering literature.
