# __$M_2(\mathbb{H})$ Diagonal Representation__

## Introduction

**The split-biquaternion algebra is a product of two quaternion algebras, so its faithful model is the diagonal subalgebra of $M_{2}(\mathbb{H})$, and the absence of off-diagonal entries is the whole content of the category.**

**The algebra.** The split biquaternion algebra is
$$
\mathbb{B}^{\mathrm{spl}}=\mathbb{C}^{\mathrm{spl}}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{H}\oplus\mathbb{H},
$$
with $\mathbb{C}^{\mathrm{spl}}=\mathbb{R}[j]/(j^{2}-1)$ the split-complex algebra, $j$ central, of real dimension eight. Its two idempotents are
$$
\tilde\Pi_{1}=\tfrac12(1+j),\qquad \tilde\Pi_{2}=\tfrac12(1-j),
$$
and every element splits as
$$
\tilde Q=\tilde Q_{+}\tilde\Pi_{1}+\tilde Q_{-}\tilde\Pi_{2},\qquad \tilde Q_{\pm}\in\mathbb{H},
$$
with two ordinary quaternions as coordinates. The algebra is semisimple and **not simple**, and its two simple summands are division rings.

**The model.** Left multiplication on the free module of rank two over $\mathbb{H}$ with basis $(1,j)$ is the diagonal matrix
$$
\mathsf M(\tilde Q)=\begin{pmatrix}\tilde Q_{+}&0\\ 0&\tilde Q_{-}\end{pmatrix}\in M_{2}(\mathbb{H}),
$$
a faithful image of real dimension eight inside the sixteen of $M_{2}(\mathbb{H})$. The matrix is diagonal because $j$ is a unit of the algebra and not a nilpotent and not a distinct conjugate: multiplying by $j$ permutes nothing, it only flips the sign of the second coordinate, so the two off-diagonal blocks of the multiplication table vanish identically.

**What the model shows.** The block diagonal form is the semisimplicity made visible: the algebra is a product, the module is a direct sum, and every computation separates into two independent quaternionic computations. The determinant is the product of the two reduced norms, $N(\tilde Q_{+})N(\tilde Q_{-})$, a nonnegative real, and it vanishes exactly on the zero divisors, which are the elements with one vanishing block. The trace is a **quaternion** and not a real, it is not central, and only its scalar part is an invariant. The spectrum is a pair of quaternions and not a family of scalars, and the block diagonalisation is the spectral theorem. And the four fixed subspaces of the conjugations are **block conditions**: equal blocks, conjugate blocks, and their negatives.

**Why there is no matrix algebra.** The algebra is not isomorphic to any full matrix algebra, because a full matrix algebra is simple and this one is not. The best possible model is the diagonal subalgebra, and it is genuinely smaller than the ambient: the off-diagonal corners are empty, the system of matrix units is degenerate, and the element that would fill them does not exist. That absence is the one thing this category has that no other category of the block has, and the article is organised around it.

**The boundaries.** The algebra, its conjugations and its four fixed subspaces are *Split-Biquaternion Algebra*; the norms and the invertibility criterion are *Split-Biquaternion Norm and Invertibility*; the zero divisors are *Split-Biquaternion Zero Divisors*; the ideals and the Peirce decomposition are *Split-Biquaternion Ideals and Peirce Decomposition*; the involution lattice is *Split-Biquaternion Involution Lattice*; the four-vector is *Split-Biquaternion Four-Vector Element Representation*; the linear representations are *Split-Biquaternion Linear Representations*; the operators are *$M_{2}(\mathbb{H})$ Diagonal Representation : Operators*. The section on the absence of a matrix representation of *Split-Biquaternion Algebraic Element Representations* is absorbed here as the frame section, and that article is retired.

## The Frame

**Eight real coefficients, one split unit, two idempotents, two blocks and a degenerate system of matrix units.**

**The basis.** The algebra has the real basis
$$
e_{t}=1,\quad \vec e_{x},\quad \vec e_{y},\quad \vec e_{z},\qquad je_{t},\ j\vec e_{x},\ j\vec e_{y},\ j\vec e_{z},
$$
of eight elements, and an element is
$$
\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_{\mu}e_{\mu},\qquad Q_{\mu}=q_{\mu}+jq'_{\mu},\quad q_{\mu},q'_{\mu}\in\mathbb{R}.
$$
The quaternion units satisfy $\vec e_{x}^{2}=\vec e_{y}^{2}=\vec e_{z}^{2}=-1$ and $\vec e_{x}\vec e_{y}=\vec e_{z}$ cyclically, and the split unit satisfies $j^{2}=+1$ and commutes with all four.

**The idempotents.** The two elements $\tilde\Pi_{1}=\tfrac12(1+j)$ and $\tilde\Pi_{2}=\tfrac12(1-j)$ satisfy
$$
\tilde\Pi_{1}^{2}=\tilde\Pi_{1},\qquad \tilde\Pi_{2}^{2}=\tilde\Pi_{2},\qquad \tilde\Pi_{1}\tilde\Pi_{2}=0,\qquad \tilde\Pi_{1}+\tilde\Pi_{2}=1,
$$
and they are central because $j$ is. Their matrices are the two diagonal matrix units,
$$
\mathsf M(\tilde\Pi_{1})=\begin{pmatrix}1&0\\ 0&0\end{pmatrix}=\tilde E_{11},\qquad \mathsf M(\tilde\Pi_{2})=\begin{pmatrix}0&0\\ 0&1\end{pmatrix}=\tilde E_{22}.
$$

**The idempotent coordinates.** In the basis $(1,j)$,
$$
\tilde Q_{\pm}=\sum_{\mu}\bigl(q_{\mu}\pm q'_{\mu}\bigr)e_{\mu},
$$
so the split unit doubles and halves the coefficients and the two coordinates are two real quaternions. The passage matrix is the same one as in the reduced biquaternion category,
$$
P=\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},\qquad P^{2}=2\,\mathrm I_{2},\qquad P^{-1}=\tfrac12P,
$$
read over $\mathbb{H}$: it acts on the two blocks and does not touch the quaternions.

**The two blocks.** The algebra is the direct sum of the two ideals
$$
\mathbb{B}^{\mathrm{spl}}\,\tilde\Pi_{1}=\mathbb{H}\tilde\Pi_{1}\cong\mathbb{H},\qquad \mathbb{B}^{\mathrm{spl}}\,\tilde\Pi_{2}=\mathbb{H}\tilde\Pi_{2}\cong\mathbb{H},
$$
and there are no other proper ideals. Each is a division ring, so each is a minimal ideal, and the sum is direct: the algebra is a product of two division rings, which is the structure the model displays.

**The degenerate system of matrix units.** A system of matrix units in an algebra of dimension $n^{2}$ is a family $\{E_{ij}\}$ with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $\sum_{i}E_{ii}=1$. Here the only system is
$$
\tilde E_{11}=\tilde\Pi_{1},\qquad \tilde E_{22}=\tilde\Pi_{2},\qquad \tilde E_{12}=\tilde E_{21}=0,
$$
and the two off-diagonal units are **zero**. The reason is one line: an element $u$ with $\tilde\Pi_{1}u\tilde\Pi_{2}\neq0$ would lie in the ideal $\mathbb{H}\tilde\Pi_{1}$ and be annihilated on the left by $\tilde\Pi_{1}$, which is impossible in a division ring. So no element of the algebra connects the two blocks, and the model is diagonal because the algebra cannot be anything else.

**The image.** The image is
$$
\mathsf M(\mathbb{B}^{\mathrm{spl}})=\left\{\begin{pmatrix}u&0\\ 0&v\end{pmatrix}:u,v\in\mathbb{H}\right\},
$$
of real dimension eight inside the sixteen of $M_{2}(\mathbb{H})$, and the membership test is the vanishing of the two off-diagonal blocks, four real equations:
$$
b=0,\qquad c=0 .
$$
The test is **linear** and it is stricter than any determinantal condition: the model is a subspace of codimension eight, and there is no question of a rank condition because the image never leaves the diagonal. This is the only category of the block in which even the span of the family falls short of the ambient, and the reason is that the algebra is not simple.

**The centraliser.** The matrices of $M_{2}(\mathbb{H})$ commuting with every diagonal matrix are the diagonal matrices, because the blocks are division rings and a nonzero off-diagonal entry would have to annihilate a unit. So
$$
\mathsf M(\mathbb{B}^{\mathrm{spl}})'=\mathsf M(\mathbb{B}^{\mathrm{spl}}),\qquad \mathsf M(\mathbb{B}^{\mathrm{spl}})''=\mathsf M(\mathbb{B}^{\mathrm{spl}}),
$$
and the image is self-centralising, in the same position as the diagonal subalgebra of $M_{2}(\mathbb{C})$, but noncommutative. A maximal subalgebra is not the right word here, because the image is not commutative; the right word is self-centralising.

**The ambient is simple and the image is not.** This is the sentence to keep: $M_{2}(\mathbb{H})$ is simple and $\mathbb{B}^{\mathrm{spl}}$ is not, so no injective homomorphism can be surjective, and the deficiency is structural and not an accident of the choice of basis. The comparison table is short.

| | $\mathbb{B}^{\mathrm{spl}}$ | $M_{2}(\mathbb{H})$ |
|---|---|---|
| simple | no, a product of two | yes |
| real dimension | $8$ | $16$ |
| centre | $\mathbb{C}^{\mathrm{spl}}$, of real dimension two | $\mathbb{R}$ |
| matrix units | $\tilde E_{12}=\tilde E_{21}=0$ | all four nonzero |
| model | the diagonal subalgebra | the whole algebra |

## The Left and the Right Matrices

**Two commuting copies, one per block, and the regular module is a direct sum of two simple modules.**

**The operators.** Left multiplication and right multiplication are the blockwise operators
$$
L_{\tilde Q}=\begin{pmatrix}L_{\tilde Q_{+}}&0\\ 0&L_{\tilde Q_{-}}\end{pmatrix},\qquad R_{\tilde P}=\begin{pmatrix}R_{\tilde P_{+}}&0\\ 0&R_{\tilde P_{-}}\end{pmatrix},
$$
where $L_{u}$ and $R_{v}$ are the left and right multiplications of the quaternion algebra on itself. They **commute**, $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$, because the two act on different slots of the product, and every $L$ commutes with every $R$ blockwise.

**The module.** The regular module is the free module $\mathbb{H}^{2}$ over $\mathbb{H}$ with basis $(1,j)$, and as a module over the algebra it is
$$
\mathbb{B}^{\mathrm{spl}}=\mathbb{H}\tilde\Pi_{1}\oplus\mathbb{H}\tilde\Pi_{2},
$$
a direct sum of two simple modules, each of quaternionic dimension one, each annihilated by the other idempotent. The series splits and there is no extension: the module theory is trivial, and the whole content is the two blocks.

**The kernel and the image.** For the left multiplication by $\tilde Q$,

| $\tilde Q$ | $\ker L_{\tilde Q}$ | $\operatorname{im}L_{\tilde Q}$ | $\operatorname{rank}_{\mathbb{H}}$ |
|---|---|---|---|
| both blocks nonzero | $0$ | all | $2$ |
| $\tilde Q_{+}\neq0$, $\tilde Q_{-}=0$ | $\mathbb{H}\tilde\Pi_{2}$ | $\mathbb{H}\tilde\Pi_{1}$ | $1$ |
| $\tilde Q_{+}=0$, $\tilde Q_{-}\neq0$ | $\mathbb{H}\tilde\Pi_{1}$ | $\mathbb{H}\tilde\Pi_{2}$ | $1$ |
| $\tilde Q=0$ | all | $0$ | $0$ |

The kernel and the image of a zero divisor are the two different blocks, so they are complementary, and the complementary block is exactly the ideal that the element annihilates. In the quaternion category the analogue of this table had one row; here the two rows are independent and either can fail alone.

**The spectrum of the regular module.** The two simple modules are non-isomorphic, because an intertwiner between them would be a nonzero element of the missing off-diagonal corner. So the module has two non-isomorphic composition factors and, unlike the reduced biquaternion category where the two factors were the same field with different actions, the factors here are two non-isomorphic simple modules over the same division ring.

## The Product

**The product is blockwise, the algebra separates, and the model is faithful but not surjective.**

**Theorem (multiplicativity).** For all $\tilde Q,\tilde P$,
$$
\mathsf M(\tilde Q)\mathsf M(\tilde P)=\mathsf M(\tilde Q\tilde P)=\begin{pmatrix}\tilde Q_{+}\tilde P_{+}&0\\ 0&\tilde Q_{-}\tilde P_{-}\end{pmatrix}.
$$

*Proof.* The left multiplication is a homomorphism of the algebra into the endomorphisms of the module, and in the basis $(1,j)$ its matrix is diagonal with the two block multiplications on the diagonal. Injectivity holds because the two diagonal entries are the two idempotent coordinates.

**The algebra separates.** The consequence is that the algebra has no cross-block structure at all: sums, products, inverses, powers and polynomials act blockwise, and every question about $\mathbb{B}^{\mathrm{spl}}$ is two questions about $\mathbb{H}$. The Peirce decomposition is therefore not a convenience but an isomorphism,
$$
\mathbb{B}^{\mathrm{spl}}\cong\mathbb{H}\times\mathbb{H},\qquad \tilde Q\longmapsto(\tilde Q_{+},\tilde Q_{-}),
$$
and the matrix model is that isomorphism written as a diagonal matrix.

**The failure of surjectivity.** The model reaches only the diagonal, so the eight real dimensions of the off-diagonal corners are unreachable, and no product, sum or limit of models fills them. Concretely, a matrix with a nonzero upper-right corner is not the multiplication by any element, and there is no element whose multiplication would put a nonzero entry there: the missing entries are missing from the algebra and not from the model.

**Powers and the functional calculus.** Since the model is diagonal,
$$
\mathsf M(\tilde Q)^{n}=\operatorname{diag}\bigl(\tilde Q_{+}^{n},\tilde Q_{-}^{n}\bigr),\qquad f\bigl(\mathsf M(\tilde Q)\bigr)=\operatorname{diag}\bigl(f(\tilde Q_{+}),f(\tilde Q_{-})\bigr),
$$
where $f$ is a polynomial or a power series with real coefficients, and the two quaternionic values are computed by the quaternionic calculus. The two blocks are independent quaternions, so the two values are computed at two unrelated arguments. That is the one thing the block structure adds to the quaternion category: **two independent quaternionic variables** in the same matrix, which is what makes the algebra a product and not a field.

**The idempotents and the zero divisors.** The idempotents of the algebra are the four elements with each quaternionic coordinate $0$ or $1$,
$$
0,\qquad 1,\qquad \tilde\Pi_{1},\qquad \tilde\Pi_{2},
$$
the four diagonal matrices with entries in $\{0,1\}$, exactly as in the reduced biquaternion category. The zero divisors are the elements with **exactly one** vanishing block; they are not nilpotent, and there is no nilpotent but zero in the algebra, because a quaternion is invertible unless it is zero. So the algebra is reduced and the singular set is a union of two subspaces.

**The noncommutativity is inside the blocks.** The algebra is not commutative and it is not a product of fields: the two factors are division rings with real dimension four. That is the difference from the reduced biquaternion category, whose two factors are copies of $\mathbb{C}$, and it is the reason the trace, the adjugate and the norms of this article are quaternionic objects and not complex ones.

## The Trace

**The trace is a quaternion, it is not central, and only its scalar part is an invariant.**

**Theorem (the trace).** For every $\tilde Q$,
$$
\operatorname{tr}\mathsf M(\tilde Q)=\tilde Q_{+}+\tilde Q_{-}=2\sum_{\mu}q_{\mu}e_{\mu}=2\,\mathrm{Re}_{\mathbb{C}^{\mathrm{spl}}}\tilde Q,
$$
a quaternion, whose scalar part is $2q_{t}$. The realification has the trace $8q_{t}$.

*Proof.* The trace of a block diagonal matrix is the sum of the traces of the blocks, and the trace of $L_{u}$ as an endomorphism of the real four-space $\mathbb{H}$ is $4\,\mathrm{Sc}(u)$, so the realified trace is $4\,\mathrm{Sc}(\tilde Q_{+})+4\,\mathrm{Sc}(\tilde Q_{-})=4(q_{t}+q'_{t})+4(q_{t}-q'_{t})=8q_{t}$.

**Why the trace is not an invariant.** The trace of a product of quaternion matrices is invariant only up to a commutator: $\operatorname{tr}(AB)-\operatorname{tr}(BA)=[A,B]$, and the commutator subspace of $\mathbb{H}$ is its three-dimensional pure imaginary part. So the naive trace of the model is invariant modulo that subspace, and the only invariant part is the **reduced trace**
$$
\operatorname{Trd}\mathsf M(\tilde Q)=2q_{t}=\tfrac12\bigl(\operatorname{tr}\mathsf M(\tilde Q)+\operatorname{tr}\mathsf M(\tilde Q)^{\natural}\bigr),
$$
a real number. The correct statement of the category is therefore that the trace is not central and that the reduced trace is the invariant, and the determinant below is the object that carries the real information.

**The kernel of the trace.** The quaternionic trace vanishes exactly when $\sum_{\mu}q_{\mu}e_{\mu}=0$, that is when the four $\mathbb{C}^{\mathrm{spl}}$-real coefficients vanish: the kernel is the four-dimensional real subspace
$$
\ker\operatorname{tr}=j\mathbb{H},
$$
the purely split-imaginary part of the algebra. It is a subspace and not an ideal: the algebra has only two proper ideals, the two blocks, and neither is $j\mathbb{H}$. This is a difference from the reduced biquaternion category, where the kernel of the trace was the complex line $\mathbb{C}j$ and the complement was the scalar line.

**The trace form.** The bilinear form $(\tilde Q,\tilde P)\mapsto\operatorname{Sc}\operatorname{tr}(\mathsf M(\tilde Q)\mathsf M(\tilde P))$ is the reduced trace of the product,
$$
\operatorname{Sc}\operatorname{tr}\bigl(\mathsf M(\tilde Q)\mathsf M(\tilde P)\bigr)=\operatorname{Sc}\bigl(\tilde Q_{+}\tilde P_{+}\bigr)+\operatorname{Sc}\bigl(\tilde Q_{-}\tilde P_{-}\bigr),
$$
a real bilinear form of real signature $(4,4)$: four positive directions from the two real parts and four negative from the two imaginary parts. The form is **nondegenerate**, because the quaternion trace form is nondegenerate and the block sum of two copies is nondegenerate. So the trace form of the category is a form of signature $(4,4)$, and its radical is zero.

**The reading.** Four trace forms of the block: $\operatorname{diag}(2,-2)$ of signature $(1,1)$ for the complex numbers, $\operatorname{diag}(2,0)$ degenerate for the dual numbers, $2\,\mathrm I_{2}$ of signature $(2,2)$ for the reduced biquaternions, and the $(4,4)$ form here. The pattern is the real dimension: the form is the reduced trace of the product, and the signature is $(n/2,n/2)$ where $n$ is the real dimension of the algebra, for every semisimple algebra of the block.

## The Determinant

**The determinant is the product of the two reduced norms, a nonnegative real, and its zero set is the union of the two block hyperplanes.**

**Theorem (the determinant).** For every $\tilde Q$,
$$
\det\mathsf M(\tilde Q)=N(\tilde Q_{+})\,N(\tilde Q_{-}),\qquad N(u)=uu^{\natural}=|u|^{2}\in[0,\infty),
$$
the product of the two quaternion norms, and it is multiplicative. The realification has the determinant
$$
\det_{\mathbb{R}}\mathsf L_{\tilde Q}=N(\tilde Q_{+})^{2}N(\tilde Q_{-})^{2}.
$$

*Proof.* For a block diagonal quaternion matrix the Dieudonné determinant is the product of the determinants of the blocks, each of which is the reduced norm of a quaternion and hence a nonnegative real; the reduced norm multiplies, so the product is multiplicative. For the realification, the $4\times4$ real matrix of $L_{u}$ has determinant $N(u)^{2}$, and the two blocks multiply.

**The zero set.** The determinant vanishes exactly when one block vanishes,
$$
\det\mathsf M(\tilde Q)=0\iff \tilde Q_{+}=0\ \text{or}\ \tilde Q_{-}=0,
$$
which is the union of the two ideals, each of real dimension four, meeting only at the origin. So the singular locus is the union of two four-dimensional subspaces of the eight-dimensional algebra, and it is **not** the zero set of the split-biquaternion norm $\langle\tilde Q\rangle_{\natural}$, which is anisotropic and vanishes only at the origin. The two objects are different and the article keeps them apart: the determinant decides invertibility, the quaternionic norm does not.

**The two determinants.** The determinant of the model $M_{2}(\mathbb{H})$ is a **Study determinant** — the determinant of the realification of the block diagonal matrix, taken blockwise — and there are two conventions in the literature: the Study determinant of a quaternion matrix, which is real, and the Dieudonné determinant, which is valued in the abelianisation of the quaternion group and for a diagonal matrix is the same real. The real $8\times8$ determinant is the square of the Study determinant, exactly as the complex $2\times2$ determinant of a quaternion is the square of its norm,
$$
\det_{\mathbb{C}}\begin{pmatrix}a&b\\ -\bar b&\bar a\end{pmatrix}=N(a)+N(b),\qquad \det_{\mathbb{R}}(L_{u})=N(u)^{2},
$$
so the ladder is norm, Study determinant, and real determinant, with the exponents $1,1,2$ on the respective carriers. The article uses the Study determinant, calls it the determinant, and states the real one explicitly when the realification is in play.

**The rank ladder.** The rank over $\mathbb{H}$ is
$$
\operatorname{rank}_{\mathbb{H}}\mathsf M(\tilde Q)=\operatorname{rank}(\tilde Q_{+})+\operatorname{rank}(\tilde Q_{-})\in\{0,1,2\},
$$
each block contributing $0$ or $1$ because each block is a division ring, and the real rank is four times that value,
$$
\operatorname{rank}_{\mathbb{R}}\mathsf L_{\tilde Q}\in\{0,4,8\}.
$$
The three values are attained: $0$ at the zero element, $4$ on the union of the two punctured ideals, and $8$ on the units. This ladder of three separated values, with no intermediate rank, is the parametrisation of the singular set of the category: a quaternion is invertible unless it is zero, so a block is either full or empty.

**The unit group.** The determinant is nonzero exactly when both blocks are nonzero, so
$$
{\mathbb{B}^{\mathrm{spl}}}^{\times}\cong\mathbb{H}^{\times}\times\mathbb{H}^{\times}\cong\bigl(SU(2)\times\mathbb{R}_{>0}\bigr)^{2},
$$
of real dimension eight, and the retract is $SU(2)\times SU(2)=S^{3}\times S^{3}$. This is the object the operators article uses: the unit group is not connected, it has four components distinguished by the signs of the two real parts, and its compact retract is a product of two three-spheres and not a torus.

## The Spectral Projectors

**The two central idempotents are the spectrum, and the block diagonalisation is the primary spectral statement.**

**The theorem.** For every $\tilde Q$, the model is already diagonal, and the diagonalisation theorem of the category is the trivial one:
$$
\mathsf M(\tilde Q)=\tilde Q_{+}\,\tilde E_{11}+\tilde Q_{-}\,\tilde E_{22},\qquad \tilde E_{11}+\tilde E_{22}=1,\qquad \tilde E_{11}\tilde E_{22}=0 .
$$
So the two spectral projectors are the two central idempotents, they do not depend on the element, and the two "eigenvalues" are quaternions.

**What "spectrum" means here.** A quaternionic eigenvalue is not a single scalar, and the word must be used with care. The right eigenvalues of a quaternion $u$ are the complex numbers $\lambda$ with $ux=x\lambda$ for a nonzero $x\in\mathbb{H}$, and they form at most two conjugate pairs, because $ux=x\lambda$ is a complex-linear condition once $\lambda$ is fixed in $\mathbb{C}$. The real spectrum of $L_{u}$ as a $4\times4$ real matrix is one conjugate pair counted twice, or two distinct conjugate pairs, or the quadruple $\{u_{0},u_{0},u_{0},u_{0}\}$ when $u$ is real. In every case the correct invariant is the conjugate pair, and the model has
$$
\operatorname{spec}_{\mathbb{R}}\mathsf L_{\tilde Q}=\{\lambda_{+},\bar\lambda_{+}\}\cup\{\lambda_{-},\bar\lambda_{-}\},
$$
two independent conjugate pairs, one from each block. The comparison with the biquaternion category is the point: there the carrier was $M_{2}(\mathbb{C})$ and an element had two complex eigenvalues; here the element has two quaternions, each with a conjugate pair, and the total is four complex numbers or fewer when coincidences occur.

**The two spectra are independent.** A quaternion in the first block puts no constraint on the second, so the spectrum of an element of this category is the union of two free conjugate pairs, and the parameter space of the spectrum is the square of the quotient of $\mathbb{C}$ by the conjugation. In the biquaternion category the two eigenvalues were constrained by the reality of the trace and the norm; here there is no constraint, because the two blocks are independent division rings.

**Lagrange's formula and its degenerate locus.** The projector formula
$$
\tilde\Pi_{1}=\bigl(\tilde Q_{+}-\tilde Q_{-}\bigr)^{-1}\bigl(\tilde Q-\tilde Q_{-}\bigr),\qquad \tilde\Pi_{2}=\bigl(\tilde Q_{-}-\tilde Q_{+}\bigr)^{-1}\bigl(\tilde Q-\tilde Q_{+}\bigr)
$$
holds on the complement of $\tilde Q_{+}=\tilde Q_{-}$, because a nonzero quaternion is invertible and the inverse can be taken on the left. It degenerates exactly on the **quaternion subspace** $\tilde Q_{+}=\tilde Q_{-}$, of real dimension four, and there the two projectors still exist, being constants of the algebra. So the failure is of the formula and not of the object, as in the reduced biquaternion category, with the degenerate locus of real dimension four instead of two, and the reason for the larger locus is that the equation $\tilde Q_{+}=\tilde Q_{-}$ is four real equations and not two.

**The spectral mapping.** For a function $f$ analytic on a neighbourhood of the two conjugate pairs,
$$
\operatorname{spec}f(\tilde Q)=f\bigl(\operatorname{spec}\tilde Q\bigr),\qquad f(\tilde Q)=f(\tilde Q_{+})\tilde\Pi_{1}+f(\tilde Q_{-})\tilde\Pi_{2},
$$
so the calculus is the blockwise evaluation and fixes the two projectors. Since the two blocks are division rings, the calculus is defined for every function that is defined on the two spectra, and there is no nilpotent correction term: the algebra is reduced.

## The Adjugate and the Inverse

**The inverse is blockwise and stays in the algebra; the adjugate does not come from a conjugation, and that is the new phenomenon of this category.**

**Theorem (the inverse).** On the complement of the singular set,
$$
\mathsf M(\tilde Q)^{-1}=\begin{pmatrix}\tilde Q_{+}^{-1}&0\\ 0&\tilde Q_{-}^{-1}\end{pmatrix}=\begin{pmatrix}N(\tilde Q_{+})^{-1}\tilde Q_{+}^{\natural}&0\\ 0&N(\tilde Q_{-})^{-1}\tilde Q_{-}^{\natural}\end{pmatrix}=\mathsf M\bigl(\tilde Q^{-1}\bigr),
$$
with $\tilde Q^{-1}=\tilde Q_{+}^{-1}\tilde\Pi_{1}+\tilde Q_{-}^{-1}\tilde\Pi_{2}$, so the algebra is closed under inversion and the model is closed too.

**The adjugate.** Multiplying the inverse by the determinant,
$$
\operatorname{adj}\mathsf M(\tilde Q)=\begin{pmatrix}N(\tilde Q_{-})\,\tilde Q_{+}^{\natural}&0\\ 0&N(\tilde Q_{+})\,\tilde Q_{-}^{\natural}\end{pmatrix},
$$
and the two entries are **crossed**: the first block carries the norm of the second. So the adjugate is not the model of any element obtained from $\tilde Q$ by one of the conjugations of the algebra:
$$
\operatorname{adj}\mathsf M(\tilde Q)\neq\mathsf M(\tilde Q^{\natural}),\qquad \operatorname{adj}\mathsf M(\tilde Q)\neq\mathsf M(\tilde Q^{*}),
$$
because the first would be $\mathrm{diag}(\tilde Q_{+}^{\natural},\tilde Q_{-}^{\natural})$ and the second $\mathrm{diag}(\tilde Q_{-}^{\natural},\tilde Q_{+}^{\natural})$: the second has the right blocks but no norms and the first has the right norms but no swap. The adjugate is the star-conjugate times the crossed norms, an element of the algebra and not the image of a conjugation.

**Why the adjugate was a conjugation in the other categories.** In the complex, split-complex, dual-number and reduced biquaternion categories the determinant of the multiplication was a single element and the adjugate was its conjugate; the formula $\operatorname{adj}M=\det(M)M^{-1}$ then produced a conjugate because the inverse of a multiplication by a scalar is the multiplication by the inverse of that scalar in the same slot. Here the determinant is a **product of two norms living in the two slots**, so the cofactor of the first block must carry the norm of the second, and the crossing is forced. This is the sharpest difference between this category and the reduced biquaternion category, and it is a difference of content and not of notation.

**The three operations.** The transpose and the conjugate transpose of a quaternion matrix are distinct operations, and the model responds to both:
$$
\mathsf M(\tilde Q)^{\mathsf T}=\mathsf M(\tilde Q),\qquad \mathsf M(\tilde Q)^{\dagger}=\mathsf M(\tilde Q^{\natural}),
$$
the first because the matrix is diagonal, the second because the conjugate transpose of a block diagonal matrix is the block diagonal matrix of the conjugate transposes and the conjugate transpose of $L_{u}$ is $L_{u^{\natural}}$. So the model is a **$*$-representation** for the quaternion conjugation, and the transpose is trivial on the image, exactly as in the reduced biquaternion category. The split-complex conjugation is the only one that is not read entrywise, and it is the block swap
$$
\mathsf M(\bar{\tilde Q})=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}\mathsf M(\tilde Q)\begin{pmatrix}0&1\\ 1&0\end{pmatrix},
$$
a conjugation by an element **outside** the image. So the element that the algebra lacks — the off-diagonal matrix unit — is exactly the element that implements the split-complex conjugation in the ambient, and that is the structural punchline of the category.

**The four conjugations in the model.** The table is short and complete.

| conjugation | action on $(\tilde Q_{+},\tilde Q_{-})$ | action on the model | inside the image |
|---|---|---|---|
| quaternion ${}^{\natural}$ | $(\tilde Q_{+}^{\natural},\tilde Q_{-}^{\natural})$ | conjugate transpose | yes |
| split-complex ${}^{-}$ | $(\tilde Q_{-},\tilde Q_{+})$ | conjugation by the swap | no, outer |
| Hermitian ${}^{*}$ | $(\tilde Q_{-}^{\natural},\tilde Q_{+}^{\natural})$ | swap conjugate transpose swap | no, outer |
| anti-Hermitian ${}^{\flat}$ | $(-\tilde Q_{-}^{\natural},-\tilde Q_{+}^{\natural})$ | minus the previous | no, outer |

**The four fixed spaces as block conditions.** The table of the previous section settles the subspaces, and they are the content of the subspaces section: equal blocks, conjugate blocks, and their negatives.

## The Norms

**Two norms, the anisotropic quaternionic one and the singular determinant, both read from the same pair of nonnegative reals.**

**The quaternionic norm.** The split-biquaternion norm is
$$
\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_{\mu}Q_{\mu}^{2}=N(\tilde Q_{+})\tilde\Pi_{1}+N(\tilde Q_{-})\tilde\Pi_{2},
$$
a split-complex number whose two idempotent coordinates are the two quaternion norms. It is **anisotropic**: it vanishes only at $\tilde Q=0$, because each coordinate is a sum of squares. It is not the determinant, and it does not detect the zero divisors.

**The determinant is the product of the two coordinates.** From the same pair,
$$
\det\mathsf M(\tilde Q)=N(\tilde Q_{+})N(\tilde Q_{-}),
$$
so the relation between the two norms is a **product**: the quaternionic norm gives the pair $(N(\tilde Q_{+}),N(\tilde Q_{-}))$ and the determinant gives their product. The pair vanishes only at zero; the product vanishes whenever one factor vanishes. That is the whole of the difference between the anisotropic norm and the singular determinant, and it is why the split biquaternion algebra is the category where the two words "norm" and "determinant" must be used with care.

**The four forms.** With $\mathrm{Sc}$ the scalar part taken in the quaternion and in the split-complex slot alike, the four forms of the layer are
$$
\langle\tilde Q,\tilde P\rangle_{\sigma_{1}\sigma_{2}}=\mathrm{Sc}\bigl(\tilde Q^{\sigma_{1}}\tilde P^{\sigma_{2}}\bigr),
$$
with each $\sigma$ the identity, the quaternion conjugation ${}^{\natural}$ or the star ${}^{*}$, and the model reads each one as a scalar part of a product of two models, that is as a reduced trace. The four slots at equal arguments behave as follows.

| norm | value on $\tilde Q$ | reading in the model | character |
|---|---|---|---|
| plain $\langle\tilde Q\rangle$ | $\mathrm{Sc}\bigl(\tilde Q^{2}\bigr)$ | $\tfrac12\mathrm{Trd}\bigl(\mathsf M(\tilde Q)^{2}\bigr)$ | indefinite |
| quaternionic $\langle\tilde Q\rangle_{\natural}$ | $N(\tilde Q_{+})\tilde\Pi_{1}+N(\tilde Q_{-})\tilde\Pi_{2}$ | the two norms on the diagonal | anisotropic, split-complex valued |
| Hermitian $\langle\tilde Q\rangle_{*}$ | $\mathrm{Sc}\bigl(\tilde Q^{*}\tilde Q\bigr)$ | $\tfrac12\mathrm{Trd}\bigl(\mathsf M^{\dagger}\mathsf M\bigr)$ | indefinite of signature $(4,4)$ |
| Krein $\langle\tilde Q\rangle_{\natural*}$ | $\mathrm{Sc}\bigl(\tilde Q^{\natural*}\tilde Q\bigr)$ | the same with the two slots exchanged | indefinite |

The quaternionic norm is the only one of the four that is a *sum of squares* in each block, and it is the only one that is anisotropic; the other three carry negative directions, and their signatures are read from the real parts of the two blocks.

**The four subspace norms.** On the four fixed subspaces the four forms restrict to forms of definite signature or of Minkowski type, and the two that matter are the following. On the **quaternion subspace**, $\tilde Q=q_{t}+\vec q$, the quaternionic norm is $q_{t}^{2}+|\vec q|^{2}$ and is positive definite, while the Hermitian form is the Minkowski form
$$
\mathrm{Sc}\bigl(\tilde Q^{2}\bigr)=q_{t}^{2}-|\vec q|^{2},\qquad \text{signature }(1,3),
$$
whose null cone is the light cone. On the **Hermitian subspace** $\tilde Q=q_{t}+j\vec q$, the same two formulas hold with the roles exchanged: the Hermitian form is the Minkowski form of signature $(1,3)$ and the quaternionic norm is $q_{t}^{2}+|\vec q|^{2}$. So the two subspaces carry the same pair of forms with the two slots exchanged, and the light cone appears in both. On the **split-complex subspace** the forms are the split-complex forms of signature $(1,1)$; on the **anti-Hermitian subspace** the quaternionic norm is positive definite again.

**The reading.** The category has an anisotropic norm and a singular determinant, and the two are the pair and the product of the same two nonnegative numbers. That is the cleanest statement of the difference from the reduced biquaternion category, where the determinant was the product of two *complex* coordinates and the positive definite norm was their sum of squares: here the coordinates are two *real* nonnegative numbers, so their sum and their product are two different real functions and both are multiplicative-ish in their own way — the product is multiplicative, the sum is not.

## The Subspaces

**The four fixed subspaces are block conditions, and the model reads them as equal, conjugate and negated blocks.**

| subspace | algebra condition | block condition | model | real dim |
|---|---|---|---|---|
| split-complex $\mathbb{C}^{\mathrm{spl}}$ | $\tilde Q^{\natural}=\tilde Q$, vector part zero | $\tilde Q_{+}=\tilde Q_{-}=Q_{t}\in\mathbb{C}^{\mathrm{spl}}$ | $\mathrm{diag}(Q_{t},Q_{t})$ | $2$ |
| quaternion $\mathbb{H}$ | $\bar{\tilde Q}=\tilde Q$, coefficients real | $\tilde Q_{+}=\tilde Q_{-}=q\in\mathbb{H}$ | $\mathrm{diag}(q,q)$ | $4$ |
| Hermitian $\mathbb{M}_{+}$ | $\tilde Q^{*}=\tilde Q$ | $\tilde Q_{-}=\tilde Q_{+}^{\natural}$ | $\mathrm{diag}(u,u^{\natural})$ | $4$ |
| anti-Hermitian $\mathbb{M}_{-}$ | $\tilde Q^{\flat}=\tilde Q$ | $\tilde Q_{-}=-\tilde Q_{+}^{\natural}$ | $\mathrm{diag}(u,-u^{\natural})$ | $4$ |
| the centre | $[\tilde Q,\cdot]=0$ | both blocks central, $\tilde Q_{\pm}\in\mathbb{R}$ | $\mathrm{diag}(a,b)$, $a,b\in\mathbb{R}$ | $2$ |
| the zero divisors | one block zero | $\tilde Q_{+}=0$ or $\tilde Q_{-}=0$ | rank $4$ | $4$, two components |
| the units | both blocks nonzero | $\tilde Q_{\pm}\neq0$ | rank $8$ | open, dense |
| the idempotents | each block in $\{0,1\}$ | four combinations | $0$, $1$, $\tilde E_{11}$, $\tilde E_{22}$ | four points |
| the nilpotents | none but zero | both blocks zero | $0$ | one point |

**The three decompositions.** The algebra splits in three canonical ways, and the model sees two of them as the same decomposition:
$$
\mathbb{B}^{\mathrm{spl}}=\mathbb{H}\oplus j\mathbb{H}=\mathbb{H}\tilde\Pi_{1}\oplus\mathbb{H}\tilde\Pi_{2}=\mathbb{M}_{+}\oplus\mathbb{M}_{-},
$$
the first into the quaternion subspace and its translate, the second into the two ideals, the third into the Hermitian and the anti-Hermitian subspaces. The first and the third are decompositions into two subspaces with no algebra structure preserved, the second is a decomposition into two ideals and is the only one that is an isomorphism of algebras. The model diagonalises with respect to the second and reads the first and the third as the equal-blocks and conjugate-blocks conditions.

**The involution lattice.** The four conjugations form the lattice of *Split-Biquaternion Involution Lattice*, and in the model the lattice is generated by three operations: the conjugate transpose, the swap, and the minus sign. The quaternion conjugation is the conjugate transpose, the split-complex conjugation is the swap, the Hermitian conjugation is their composite, and the anti-Hermitian is minus the composite. So the group is generated by the conjugate transpose and the swap, and the conjugate transpose is the only entrywise one: the swap is the conjugation by the missing off-diagonal matrix unit, and it is the one generator that acts outside the image.

**The two implications for the operator theory.** Two facts of this section are used by the operators article. First, the model is a $*$-representation for the quaternion conjugation, so the family of operators is closed under the adjoint. Second, the split-complex conjugation is outer and is implemented by the swap, so the family is **not** invariant under the second adjoint of the ambient, and the two adjoint operations of the operator theory are of different kinds.

## Summary

1. The algebra is $\mathbb{B}^{\mathrm{spl}}=\mathbb{C}^{\mathrm{spl}}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{H}\oplus\mathbb{H}$, semisimple and not simple, of real dimension eight, with the two central idempotents $\tilde\Pi_{1},\tilde\Pi_{2}$ and the two quaternionic coordinates $\tilde Q_{\pm}$.
2. The model is the diagonal subalgebra of $M_{2}(\mathbb{H})$, of real dimension eight inside sixteen; the membership test is the vanishing of the two off-diagonal blocks, a linear test of codimension eight.
3. The matrix units of the algebra are degenerate, $\tilde E_{12}=\tilde E_{21}=0$, and the reason is that each block is a division ring, so no element connects the two blocks.
4. The product is blockwise and the algebra separates as $\mathbb{H}\times\mathbb{H}$; the model is faithful and not surjective, and no sum or product of models fills the off-diagonal corners.
5. The trace is the quaternion $\tilde Q_{+}+\tilde Q_{-}=2\,\mathrm{Re}_{\mathbb{C}^{\mathrm{spl}}}\tilde Q$, not central, with reduced trace $2q_{t}$, realified trace $8q_{t}$, and kernel the subspace $j\mathbb{H}$; the reduced trace form has signature $(4,4)$ and is nondegenerate.
6. The determinant is $N(\tilde Q_{+})N(\tilde Q_{-})$, a nonnegative real, multiplicative, vanishing exactly on the union of the two ideals; the realified determinant is its square, and the rank ladder is $\{0,4,8\}$.
7. The two central idempotents are the spectral projectors, the spectrum is two independent conjugate pairs, Lagrange's formula degenerates on the quaternion subspace of real dimension four, and the projectors exist there nonetheless.
8. The inverse is blockwise and stays in the algebra; the adjugate is $\mathrm{diag}(N(\tilde Q_{-})\tilde Q_{+}^{\natural},N(\tilde Q_{+})\tilde Q_{-}^{\natural})$ and is **not** the model of a conjugation, because the determinant is a product of the two norms and the cofactors cross.
9. The quaternionic norm is anisotropic with the two norms as coordinates, the determinant is their product, the four forms are the four reduced traces, and on the quaternion and Hermitian subspaces the Hermitian form is the Minkowski form of signature $(1,3)$.
10. The four fixed subspaces are the block conditions of equal, conjugate and negated blocks; the split-complex conjugation is the swap, an outer conjugation of the ambient by the missing off-diagonal unit, and the quaternion conjugation is the conjugate transpose, entrywise and inner.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{B}^{\mathrm{spl}}=\mathbb{C}^{\mathrm{spl}}\otimes_{\mathbb{R}}\mathbb{H}$ | the split biquaternion algebra, real dimension eight | *Split-Biquaternion Algebra* |
| $\tilde Q=\tilde Q_{+}\tilde\Pi_{1}+\tilde Q_{-}\tilde\Pi_{2}$ | the idempotent decomposition, two quaternionic coordinates | *Split-Biquaternion Algebra* |
| $\tilde\Pi_{1},\tilde\Pi_{2}$ | the two central idempotents $\tfrac12(1\pm j)$ | *Split-Biquaternion Idempotents and Projections* |
| $\mathsf M(\tilde Q)$ | the diagonal model in $M_{2}(\mathbb{H})$ | this article |
| $\mathsf L_{\tilde Q}$ | the $8\times8$ real matrix of the same operator | this article |
| $\tilde E_{11},\tilde E_{22}$ | the two diagonal matrix units, the only nonzero ones | this article |
| $N(u)=uu^{\natural}$ | the quaternion norm, a nonnegative real | this article |
| $\langle\tilde Q\rangle_{\natural}$ | the split-biquaternion norm, anisotropic, split-complex valued | *Split-Biquaternion Norm and Invertibility* |
| ${}^{\natural},{}^{-},{}^{*},{}^{\flat}$ | the quaternion, split-complex, Hermitian and anti-Hermitian conjugations | *Split-Biquaternion Involution Lattice* |
| $\mathbb{M}_{+},\mathbb{M}_{-}$ | the Hermitian and the anti-Hermitian subspaces | *Split-Biquaternion Algebra* |
| $P$ | the passage matrix $\begin{pmatrix}1&1\\ 1&-1\end{pmatrix}$, $P^{2}=2\,\mathrm I_{2}$ | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition, the matrix units of a product of division rings, and the absence of the off-diagonal units.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the structure of a semisimple algebra that is not simple, its two-sided ideals, and the module theory of the regular representation.
- F. Zhang, *Quaternions and Matrices of Quaternions* (Linear Algebra and its Applications 251, 1997), for the Study and Dieudonné determinants, the reduced trace and the reduced norm of a quaternion matrix.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the Kronecker product, block diagonal matrices and the rank of a block matrix.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the split biquaternion algebra as $\mathrm{Cl}_{0,3}$, its idempotents and its two quaternionic blocks.
