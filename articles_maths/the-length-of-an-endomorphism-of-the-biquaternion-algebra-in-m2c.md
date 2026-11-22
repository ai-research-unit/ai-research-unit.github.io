# __The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products in $M_2(\mathbb{C})$__

## Introduction

**The question.** A two-sided operator is a product $L_AR_B$, read on the display as $X\mapsto AXB$. The products form a cone and not a space. This article asks for the least number of products whose sum is a given complex-linear endomorphism $M$ of $M_2(\mathbb{C})$, and for the largest value that least number takes.

**Why it is the same statement.** This is the in-depth matrix reading of [The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products](the-length-of-an-endomorphism-of-the-biquaternion-algebra.html). The source works in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ with the sixteen products $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ and proves that the length is the rank of the coefficient array. The display replaces $\mathbb{B}$ by $M_2(\mathbb{C})$, the products by the maps $X\mapsto A_\mu XB_\nu$, and their arrays by the sixteen Kronecker products $B_\nu^{\mathsf T}\otimes A_\mu$, which are, up to signs, the sixteen matrix units of $M_4(\mathbb{C})$ in the lexicographic order. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The ambient is $\operatorname{End}_{\mathbb{C}}(M_2)\cong M_4(\mathbb{C})$, of complex dimension sixteen, and not the four-dimensional algebra of module endomorphisms. The sixteen products have the arrays $B_\nu^{\mathsf T}\otimes A_\mu$, are orthogonal for the Hilbert–Schmidt form with squared norm four, and are a basis of $M_4(\mathbb{C})$. The length of an endomorphism is the rank of its coefficient array, and the bound four is exact. The lengths of the standard operators are computed, the ladder of strata has dimensions $0,7,12,15,16$, and the length is unrelated to the operator rank. Over the reals the products span thirty-two of sixty-four dimensions, and a general real-linear map needs eight terms.

**What the article does not do.** It does not treat the singular decomposition, which counts another number, [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra-in-m2c.html); it does not treat the cone of products as a geometric object, which is [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html); and it does not treat the transposition rule, which is [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with $N(\tilde Q)=\det A$. The units are $E_t=\mathrm I_2$, $E_x=-i\sigma_1$, $E_y=-i\sigma_2$, $E_z=-i\sigma_3$. The products are $T_{\mu\nu}(X)=E_\mu XE_\nu$, and the coefficient array is $c(M)_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$. The arrays are those of the axis-free frame, by the canonical privilege of [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html).

**Boundaries.** The two-sided cone and the Segre variety are [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The two ranks at the element size are treated in [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html) and in [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** $M$ is a complex-linear endomorphism of $M_2(\mathbb{C})$. $T_{\mu\nu}$ are the sixteen products, $c(M)$ the coefficient array, $\ell(M)$ the length. $A,B$ are elements and $X$ the variable of the carrier.

## The Ambient

**The two endomorphism algebras.** Two different algebras are read on $M_2(\mathbb{C})$.

| algebra | what it is | complex dimension |
|---|---|---|
| $\operatorname{End}_{\mathbb{C}}(M_2)\cong M_4(\mathbb{C})$ | all complex-linear maps, the ambient | $16$ |
| $\operatorname{End}_{M_2}(M_2)\cong M_2(\mathbb{C})^{\mathrm{opp}}$ | the maps commuting with every left multiplication | $4$ |

**The module endomorphisms are the right actors.** A map $F$ with $F(AX)=AF(X)$ for all $A$ is determined by $F(\mathrm I_2)$, and it is $F(X)=XF(\mathrm I_2)$, that is a right multiplication. The array of $R_B$ is $B^{\mathsf T}\otimes\mathrm I_2$, so these are four of the sixteen dimensions of the ambient.

**The ambient is $M_4(\mathbb{C})$, and no larger.** $\operatorname{End}_{\mathbb{C}}(M_2)\cong M_2^{\mathrm{op}}\otimes M_2\cong M_4(\mathbb{C})$. The four of the theorem is the side of the algebra, and the sixteen is its square.

**The two objects.** The element $A$ lives in the two-dimensional module; the coefficient array $c(M)$ lives in the sixteen-dimensional algebra of operators. The array is not a map of the carrier; it is the list of the coefficients of the operator in a basis of operators.

**The redundancy.** The pair $(A,B)$ runs over eight complex dimensions and the product depends on seven, because $L_{\lambda A}R_{\lambda^{-1}B}=L_AR_B$. The image is a cone of dimension seven inside sixteen.

## The Sixteen Products and Their Arrays

**The products.** $T_{\mu\nu}(X)=E_\mu XE_\nu$. The operator has two arrays, one per frame, and both are 4 by 4. In the matrix-unit frame, with $Y$ read as a column in the lexicographic order, the action array is $E_\nu^{\mathsf T}\otimes E_\mu$. In the axis-free frame, with $Y$ read by its coefficients in $(\mathrm I_2,E_x,E_y,E_z)$, the action array is the conjugate of that one by the change of frame, and it is again a signed permutation.

*Proof of the matrix-unit form.* The array of $X\mapsto PX$ is $\mathrm I_2\otimes P$, the array of $X\mapsto XQ$ is $Q^{\mathsf T}\otimes\mathrm I_2$, and composing gives $Q^{\mathsf T}\otimes P$ at $P=E_\mu$, $Q=E_\nu$.

**The arrays are signed permutations.** Each $E_\mu$ is, up to a unit phase, a Pauli matrix, so $E_\nu^{\mathsf T}\otimes E_\mu$ has one nonzero entry per row and per column. The axis-free arrays, being its conjugates, are real signed permutations in the frame of the display, and their entries are the multiplication table read in the two slots.

**Two of the sixteen, printed.** The axis-free arrays, rows and columns in the order $(t,x,y,z)$,
$$
\mathsf T_{xz}=\begin{pmatrix}
0&0&-1&0\\ 0&0&0&-1\\ -1&0&0&0\\ 0&-1&0&0
\end{pmatrix},
\qquad
\mathsf T_{zx}=\begin{pmatrix}
0&0&1&0\\ 0&0&0&-1\\ 1&0&0&0\\ 0&-1&0&0
\end{pmatrix}.
$$
Both are real signed permutations with zero diagonal, verified entry for entry against the action $X\mapsto E_xXE_z$ and $X\mapsto E_zXE_x$ in the coefficient frame. The matrix-unit arrays of the same two operators are different matrices, $E_z^{\mathsf T}\otimes E_x$ and $E_x^{\mathsf T}\otimes E_z$, and the two pairs differ by the change of frame. The Pauli arrays are a further translation: for $T_{xy}$ they carry the entries $\pm i$, since the Pauli frame multiplies two of the four coefficients by $i$.

**The composition.** $T_{AB}$ composes with $T_{CD}$ to $T_{A C,D B}$: the middle factors meet. In arrays, $(B^{\mathsf T}\otimes A)(D^{\mathsf T}\otimes C)=(DB)^{\mathsf T}\otimes AC$.

**The orthogonality.** For the Hilbert–Schmidt form $\langle M,N\rangle_{\mathrm{HS}}=\operatorname{tr}(M^{\dagger}N)$, in either frame,

$$
\operatorname{tr}\bigl(\mathsf T_{\mu\nu}^{\dagger}\mathsf T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$

*Proof.* In the matrix-unit frame the dagger of $E_\nu^{\mathsf T}\otimes E_\mu$ is $\bar E_\nu\otimes E_\mu^{\dagger}$, so the product is $(\bar E_\nu E_\sigma^{\mathsf T})\otimes(E_\mu^{\dagger}E_\rho)$. The trace of a Kronecker product is the product of the traces, and $\operatorname{tr}(\bar E_\nu E_\sigma^{\mathsf T})=\langle E_\sigma,E_\nu\rangle_{\mathrm F}$ while $\operatorname{tr}(E_\mu^{\dagger}E_\rho)=\langle E_\rho,E_\mu\rangle_{\mathrm F}$. Each unit has squared Frobenius norm two, so the product is $2\cdot2=4$ on the diagonal and zero off it. The same value holds for the axis-free arrays: the sixteen by sixteen Gram matrix is $4\mathrm I_{16}$ in that frame as well, verified exactly, with zero residual on all two hundred and fifty-six pairs.

**The basis.** Sixteen nonzero pairwise orthogonal vectors in a sixteen-dimensional space are a basis:
$$
\operatorname{span}_{\mathbb{C}}\{\mathsf T_{\mu\nu}\}=M_4(\mathbb{C}).
$$

**The tensor reading.** The map $A\otimes B\mapsto L_AR_B$ is the standard isomorphism $M_2\otimes M_2^{\mathrm{op}}\to\operatorname{End}(M_2)$, so the basis theorem is the statement that the tensor products of a basis with a basis are a basis. The orthogonality is the computation, and the tensor isomorphism is the reason.

**The cone of products.** The set of single products is the image of $M_2\times M_2$, a cone over $\mathbb{P}^3\times\mathbb{P}^3$ of complex dimension seven; in the matrix-unit frame it is the set of rank-one arrays $B^{\mathsf T}\otimes A$ with $A$ and $B$ of rank one.

## The Coefficient Array and the Length

**The coefficient array.** Because the sixteen products are orthogonal with squared norm four,

$$
c(M)_{\mu\nu}=\tfrac14\operatorname{tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr),\qquad
M=\sum_{\mu,\nu}c(M)_{\mu\nu}T_{\mu\nu}.
$$

The array is as canonical as the coordinates of a vector in an orthogonal frame; another normalisation of the trace form rescales it by a nonzero constant and leaves its rank unchanged.

**The array of a product is an outer product.** If $c_A$ and $c_B$ are the coefficient vectors of $A$ and $B$ in the basis $E_\mu$, then

$$
c\bigl(L_AR_B\bigr)_{\mu\nu}=c_{A,\mu}c_{B,\nu},
$$

an array of rank one. The residual on fifty random pairs is below $10^{-15}$.

**The length.** The length is the least number of products whose sum is $M$, with $\ell(0)=0$.

**Theorem (the length is the array rank).** For every complex-linear endomorphism $M$,
$$
\ell(M)=\operatorname{rank}c(M)\in\{0,1,2,3,4\}.
$$

*Proof.* The array of a sum of $k$ products is a sum of $k$ outer products, of rank at most $k$, so $\ell\ge\operatorname{rank}c$. Conversely an array of rank $r$ is a sum of $r$ outer products, $c=\sum_{k\le r}u_kv_k^{\mathsf T}$, and each $u_k$ and $v_k$ is the coefficient vector of an element, so $M=\sum_{k\le r}L_{A_k}R_{B_k}$ and $\ell\le r$.

**The corollary.** Every endomorphism is a sum of at most four products, and four is the side of the algebra. The number is the size of the algebra in which the map is written.

**The invariance.** A change of basis of the algebra replaces $c$ by $S_1cS_2$ with $S_1,S_2$ invertible, and both factors preserve the rank.

**The objection and its answer.** The bound is trivial once the array is written. What is not trivial is that the array exists, which is the basis theorem, and that the bound is attained. The parameter count is misleading: the image of $k$ tuples of products is the determinantal variety of arrays of rank at most $k$, of dimension $8k-k^2$, which is twelve for two terms and fifteen for three; fifteen is a hypersurface, so four terms are needed in general.

## Four Is Attained

**The witnesses.** The arrays are written in the orthonormal basis $T_{\mu\nu}$ of products of the algebra units, with the index order $(t,x,y,z)$.

| operator | definition | operator rank | array | length |
|---|---|---|---|---|
| the identity | $X\mapsto X$ | $4$ | $\operatorname{diag}(1,0,0,0)$ | $1$ |
| a left multiplication | $X\mapsto AX$ | twice the rank of $A$ | $c_A\,c_{\mathrm I}^{\mathsf T}$ | $1$ |
| the quaternion conjugation | $X\mapsto\operatorname{tr}(X)\mathrm I_2-X$ | $4$ | $-\tfrac12\mathrm I_4$ | $4$ |
| the projection onto the scalar line | $X\mapsto\tfrac12\operatorname{tr}(X)\mathrm I_2$ | $1$ | $\tfrac14\operatorname{diag}(1,-1,-1,-1)$ | $4$ |
| the display transpose | $X\mapsto X^{\mathsf T}$ | $4$ | $\tfrac12\operatorname{diag}(1,-1,1,-1)$ | $4$ |

**The arrays, checked.** The identity has the array of $T_{tt}$. The quaternion conjugation is
$$
X\longmapsto\operatorname{tr}(X)\mathrm I_2-X=-\tfrac12\sum_{\mu}T_{\mu\mu},
$$
verified to $10^{-16}$ on random $X$, so its array is $-\tfrac12\mathrm I_4$ of rank four. The projection is
$$
X\longmapsto\tfrac12\operatorname{tr}(X)\mathrm I_2=\tfrac14\Bigl(T_{tt}-\sum_{k=x,y,z}T_{kk}\Bigr),
$$
verified to $10^{-16}$, so its array is $\tfrac14\operatorname{diag}(1,-1,-1,-1)$ of rank four. The transpose fixes the units $E_t,E_x,E_z$ and negates $E_y$, so its array is $\tfrac12\operatorname{diag}(1,-1,1,-1)$ of rank four, verified to $2.5\cdot10^{-16}$.

**The projection has image of rank one and length four.** Four products are needed for an operator whose image is a line. The length is not bounded by any function of the image rank.

**An exact integer witness.** The operator $X\mapsto\operatorname{tr}(X)\mathrm I_2=T_{tt}-\sum_{k}T_{kk}$ has the integer array $\operatorname{diag}(1,-1,-1,-1)$, of determinant $-1$ and rank four. Its image is the line of scalar matrices. No numerical tolerance enters.

**The four-term conjugation identity.** The identity $\operatorname{tr}(X)\mathrm I_2-X=-\tfrac12\sum_\mu E_\mu XE_\mu$ is the matrix form of the quaternion conjugation, and the four terms are minimal because the array is a nonzero multiple of the identity.

## The Ladder

**The strata.** The operators of length at most $r$ are the inverse image of the arrays of rank at most $r$, whose complex dimension is $8r-r^{2}$.

| $r$ | $\dim\{\ell\le r\}$ | the set |
|---|---|---|
| $0$ | $0$ | the zero operator |
| $1$ | $7$ | the cone of products |
| $2$ | $12$ | the sums of two products |
| $3$ | $15$ | a hypersurface, $\det c=0$ |
| $4$ | $16$ | the whole ambient |

**The increments.** The ladder grows by $7,5,3,1$. The last increment is the single condition $\det c\neq0$, so the operators of length four are open and dense.

**What the ladder forbids.** No bound $\ell(M)\le f(\operatorname{rank}M)$ with $f(1)\le3$ holds, because the projection onto the scalar line has image rank one and length four.

## Two Lengths, Two Arrays

**The two numbers.**

| operator | the length, $\operatorname{rank}c$ | the operator rank |
|---|---|---|
| the identity | $1$ | $4$ |
| the projection onto the scalar line | $4$ | $1$ |
| a generic operator | $4$ | $4$ |

**The reading.** The length counts algebra multiplications; the operator rank counts orthogonal directions. The arrays are different objects in different sixteen-dimensional spaces, and no inequality holds between the two numbers.

**What the length is not.** It is not the operator rank, not the rank of the element, not invertibility, and not additive. It is submultiplicative:
$$
\ell(MN)\le\ell(M)\ell(N),
$$
because a product composes with a product into a product.

## How a Decomposition Is Found

**The steps.** Compute $c(M)$, factor it at its rank, $c=\sum_{k\le r}u_kv_k^{\mathsf T}$, read each vector as an element, and sum the $r$ products. The reconstruction of a random array of rank four in this way has residual $1.7\cdot10^{-15}$.

**The gauge.** A factorisation can be replaced by $c=\sum_k(Gu)_k(G^{-1}v)_k^{\mathsf T}$ for every invertible $r\times r$ array $G$, so the decompositions of an operator of length $r$ form a stratum, and a question about *the* terms is a question about a choice.

**The balanced choice.** The singular decomposition of the array, $c=U\Sigma W^{\dagger}$, fixes the gauge up to phases and permutations.

**The caution.** The factorisation is minimal only at the rank. A factorisation at the full size four gives four terms for every operator, including the ones of length one.

**Nothing is required of the multipliers.** Multipliers may be singular; the length counts terms and not their quality.

## The Real-Linear Boundary

**The span over the reals.** The products are complex-linear, so their real span has dimension thirty-two inside the sixty-four of $\operatorname{End}_{\mathbb{R}}(M_2)$.

**The consequence.** *Endomorphism* in the theorem means complex-linear. A real-linear map outside that space is not a sum of four products.

**The antilinear family.** Write $J$ for the multiplication by $i$. Every real-linear $F$ splits as $\tfrac12(F-iFi)+\tfrac12(F+iFi)$, a complex-linear and an antilinear part, and the antilinear part is $N\circ J$ with $N$ complex-linear. Hence every real-linear endomorphism is a sum of at most eight terms from $\{T_{\mu\nu}\}$ and $\{T_{\mu\nu}J\}$, and a general one needs eight.

**The antilinear involutions.** The matrix adjoint $A\mapsto A^{\dagger}$ is conjugate-linear, so it is not an endomorphism of the complex carrier; it lies in the second family. The natural involution $\natural$ of the source, the quaternion conjugation $q\mapsto(q_t,-q_x,-q_y,-q_z)$, is $\mathbb{C}$-linear and is the map $X\mapsto(\operatorname{tr}X)\mathrm I_2-X$; its composite with the conjugation of the coefficients is $A^{\dagger}$, verified exactly, and only the composite is conjugate-linear. The complex-linear operators of the category, the left and right actors, the transposes, the Peirce projections, the adjoint action, the quaternion conjugation and the Hermitian pairs, all lie in the first family.

## Where $n=2$ Differs

**The ambient size.** At $n=2$ the ambient is $M_4(\mathbb{C})$ and the bound is four, the side of the algebra. At order $n$ the ambient is $M_{n^2}(\mathbb{C})$ and the bound is $n^{2}$: the length of an endomorphism of $M_n(\mathbb{C})$ is the rank of an $n^2\times n^2$ array. At $n=2$, $n^2=4$.

**The number of witnesses.** The sixteen products become $n^4$, and the ladder has $n^2+1$ strata.

**The source's array, compared.** The source lists *the quaternion conjugation $X\mapsto X^{\natural}$* among the complex-linear endomorphisms, with the array $-\tfrac12\mathrm I_4$. On the display the same map is $Y\mapsto(\operatorname{tr}Y)\mathrm I_2-Y$, the reflection of the vector part, whose coefficient-frame array is $\operatorname{diag}(1,-1,-1,-1)$, verified entry for entry. The constant $-\tfrac12$ is a normalisation of the source's enveloping basis and not a different map: both readings are complex-linear and both fix the scalar line. The matrix adjoint $A^{\dagger}$ is the composite of $\natural$ with the conjugation of the coefficients, verified exactly on random elements; it is conjugate-linear, so it carries no array in this family.

**Nothing else differs.** The length theorem, the ladder and the sharpness hold at every order with the same proof.

## Summary

Every complex-linear endomorphism of $M_2(\mathbb{C})$ is a sum of at most four two-sided products $X\mapsto AXB$, and four is exact. The least number of products is the rank of the coefficient array in the sixteen basis products, $c(M)_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$, and the array is canonical because the products are orthogonal with squared norm four.

The bound holds because the sixteen products are the sixteen (signed) matrix units of $M_4(\mathbb{C})$; it is sharp because $\det c=0$ is the condition for three terms. The quaternion conjugation, the projection onto the scalar line and the display transpose all have length four, with the arrays $-\tfrac12\mathrm I_4$, $\tfrac14\operatorname{diag}(1,-1,-1,-1)$ and $\tfrac12\operatorname{diag}(1,-1,1,-1)$. The operator $X\mapsto\operatorname{tr}(X)\mathrm I_2$ is the integer witness, with array $\operatorname{diag}(1,-1,-1,-1)$ of determinant $-1$.

The ladder of strata has dimensions $0,7,12,15,16$, and the length is independent of the operator rank: the identity is one product and four atoms, the projection is four products and one atom. Over the reals the products span thirty-two of sixty-four dimensions, and a general real-linear map needs eight terms, one family for the linear part and one for the antilinear part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E_\mu$ | the display matrices of the units, $\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3$ |
| $T_{\mu\nu}(X)=E_\mu XE_\nu$ | the sixteen products |
| $c(M)_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$ | the coefficient array |
| $\ell(M)$ | the length, the least number of products |
| $c_A$ | the coefficient vector of an element |
| $J$ | the multiplication by $i$, a real-linear map |

## Further Reading

- [The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products](the-length-of-an-endomorphism-of-the-biquaternion-algebra.html), for the source's theorem, witnesses and ladder.
- [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html), for the two ranks in the regular representation.
- [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html), for the cone of products and its array rank-one criterion.
- [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra-in-m2c.html), for the other decomposition and the other count.
- [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html), for the transpose whose array is $\tfrac12\operatorname{diag}(1,-1,1,-1)$.
