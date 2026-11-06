# __$M_2(\mathbb{H})$ Diagonal Representation : Operators__

## Introduction

**The split biquaternion algebra has one operator family and not two: the left and the right multiplications are two commuting copies of the same diagonal pattern, and the two-sided operators form the product of two quaternionic cones inside the block diagonal part of the ambient.**

**The count.** The algebra has real dimension eight. Its left multiplications form an eight-dimensional subspace of the endomorphisms of an eight-dimensional real space, because the algebra is faithful and not a matrix algebra. The left and the right multiplications together span a fourteen-dimensional space, and they commute, so they give two copies of the same algebra inside the 64-dimensional ambient, meeting in the two-dimensional centre. The two-sided operators $L_{\tilde Q}R_{\tilde Q_2}(\tilde X)=\tilde Q\tilde X\tilde Q_2$ have sixteen parameters and reach a fourteen-dimensional family, because a central rescaling of $\tilde Q$ against the inverse rescaling of $\tilde Q_2$ changes nothing. And every operator of the family is block diagonal, because the algebra is.

**The two copies.** The left multiplications and the right multiplications are not the same in this category, unlike the reduced biquaternion category where the algebra is commutative and $L=R$. They are independent, they commute, and their sum generates the whole of $\mathrm{End}(\mathbb{B}_{\mathrm{spl}})$ as a vector space of dimension sixteen. So the category has a genuine bimodule structure, and the structure is the double of the quaternionic one.

**The cone.** The family of two-sided operators is a **product of two cones**, one per block, each the seven-dimensional cone of a product of a left and a right quaternion multiplication inside a sixteen-dimensional ambience. The reach is fourteen-dimensional, the span is the thirty-two-dimensional block diagonal part of the ambient, and the deficit of sixteen real dimensions is one hundred percent of the off-diagonal corners: every off-diagonal entry is unreachable, and every diagonal entry is reachable only from the cone.

**Why the article exists.** The general article established the model, the trace, the determinant, the adjugate and the block conditions. This article establishes what the operators do with them: the one-sided copies, the two-sided family, the Kronecker display, the ranks, the semigroup of pairs, the cone and the coefficient array, the length, and the two rank ladders of the category.

## The Carrier, the Ambient and the Ladder

**The carrier is $\mathbb{B}_{\mathrm{spl}}$, of real dimension eight and of quaternionic dimension two; the ambient is its endomorphism algebra, of real dimension sixty-four; the ladder between them has three rungs.**

**The carrier.** The algebra acts on itself by left and right multiplications, and the two modules are the same module of rank two over $\mathbb{H}$,
$$
\mathbb{B}_{\mathrm{spl}}=\mathbb{H}\tilde\Pi_{1}\oplus\mathbb{H}\tilde\Pi_{2}\cong\mathbb{H}^{2},
$$
with basis $(1,j)$ over $\mathbb{H}$. The real dimension is eight and the quaternionic dimension is two.

**The ambient.** The endomorphisms of the carrier as a real space form $M_{8}(\mathbb{R})$, of dimension sixty-four. The endomorphisms as a module over $\mathbb{H}$ form $M_{2}(\mathbb{H})$, of real dimension sixteen. The two-sided operators of the block of algebras live in the first, and the left and the right multiplications live in the second.

**The ladder.**

| rung | object | real dimension |
|---|---|---|
| the family | the two-sided operators $L_{\tilde Q}R_{\tilde Q_2}$ | reaches $14$ |
| the left and the right copies together | $L$ and $R$ | $14$ |
| the diagonal subalgebra of the ambient | $\mathsf M(\mathbb{B}_{\mathrm{spl}})$ | $8$ |
| the carrier | $\mathbb{B}_{\mathrm{spl}}$ | $8$ |
| the ambient | $\mathrm{End}_{\mathbb{R}}(\mathbb{B}_{\mathrm{spl}})$ | $64$ |

**The two ranks.** The carrier is two-dimensional over $\mathbb{H}$, so the natural rank of an operator is its rank as an $\mathbb{H}$-linear map, in $\{0,1,2\}$, and the real rank is four times that, in $\{0,4,8\}$. The article uses the real rank when it compares with the ambient and the $\mathbb{H}$-rank when it compares with the quaternions, and the table of the last section fixes the passage.

**The block diagonal part.** The left multiplications, the right multiplications and the two-sided operators are all block diagonal, so they lie in
$$
\mathrm{End}_{\mathbb{R}}\bigl(\mathbb{H}\tilde\Pi_{1}\bigr)\oplus\mathrm{End}_{\mathbb{R}}\bigl(\mathbb{H}\tilde\Pi_{2}\bigr)\subset M_{8}(\mathbb{R}),
$$
of dimension thirty-two, which is the ambient of the category and not the whole of $M_{8}(\mathbb{R})$. The off-diagonal corner is not merely unreachable from the family: it is unreachable from the span.

## The One-Sided Operators

**Two commuting faithful copies, block diagonal, with the rank of the sum equal to the sum of the ranks.**

**Theorem (the one-sided operators).** For $\tilde Q,\tilde Q_2$,
$$
L_{\tilde Q}=\begin{pmatrix}L_{\tilde Q_{+}}&0\\ 0&L_{\tilde Q_{-}}\end{pmatrix},\qquad R_{\tilde Q_2}=\begin{pmatrix}R_{\tilde Q_{2+}}&0\\ 0&R_{\tilde Q_{2-}}\end{pmatrix},
$$
and $L_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q}$, so the pair $(L,R)$ is a representation of $\mathbb{B}_{\mathrm{spl}}\otimes{\mathbb{B}_{\mathrm{spl}}}_{\mathrm{opp}}$ that is faithful on each factor.

**The two copies are independent.** Unlike the commutative categories, $L_{\tilde Q}\neq R_{\tilde Q}$ in general, and the difference is exactly the commutator structure of the quaternion: $L_{u}x=ux$ and $R_{u}x=xu$ differ by $[u,x]$. Since the commutator of $\mathbb{H}$ is its three-dimensional pure imaginary part, the two copies agree exactly on the centre, and the "two-sided" instruction is a genuine instruction and not a decoration.

**The real dimensions.** The left copy is eight-dimensional, the right copy is eight-dimensional, and their span is fourteen-dimensional because the two copies intersect in the two-dimensional centre,
$$
\dim L=8,\qquad \dim R=8,\qquad \dim(L\cap R)=\dim\mathbb{C}_{\mathrm{spl}}=2,\qquad \dim\langle L,R\rangle=14 .
$$
Read inside $M_{2}(\mathbb{H})$, of real dimension sixteen, the span is the whole block diagonal part, so the two missing dimensions are exactly the two off-diagonal matrix units $\tilde E_{12}$ and $\tilde E_{21}$: the left and the right multiplications generate everything except the two elements that do not exist.

**The ranks.** The ranks are additive over the two blocks:
$$
\operatorname{rank}_{\mathbb{H}}L_{\tilde Q}=\operatorname{rank}(\tilde Q_{+})+\operatorname{rank}(\tilde Q_{-})\in\{0,1,2\},
$$
with each block contributing one when the quaternion is nonzero. The same formula holds for $R$, and the two blocks fail independently.

**The three adjoints.** The three adjoint operations of the layer are

| form | adjoint of $L_{\tilde Q}$ | adjoint of $R_{\tilde Q}$ | sides |
|---|---|---|---|
| plain $\langle\cdot,\cdot\rangle$ | $R_{\tilde Q}$ | $L_{\tilde Q}$ | exchanged |
| quaternionic $\langle\cdot,\cdot\rangle_{\natural}$ | $L_{\tilde Q^{\natural}}$ | $R_{\tilde Q^{\natural}}$ | kept |
| Hermitian $\langle\cdot,\cdot\rangle_{*}$ | $L_{\tilde Q^{*}}$ | $R_{\tilde Q^{*}}$ | kept |

The plain form is bilinear and symmetric, so it exchanges the two copies: $\langle L_{\tilde Q}X,Y\rangle=\mathrm{Sc}(\tilde QXY)=\mathrm{Sc}(XY\tilde Q)=\langle X,R_{\tilde Q}Y\rangle$ by the cyclicity of the scalar part. The quaternionic form is sesquilinear with the conjugation in the first slot, so it keeps the sides and conjugates the parameter: $\langle L_{\tilde Q}X,Y\rangle_{\natural}=\mathrm{Sc}(X^{\natural}\tilde Q^{\natural}Y)=\langle X,L_{\tilde Q^{\natural}}Y\rangle_{\natural}$. The Hermitian form is the same computation with the star. So **the plain form is the only one that exchanges the two copies**, and it is the only one for which the two-sided theory has a purely transpositional character.

**The pair of copies is the double.** The left and the right copies together with the two adjoints form the algebraic content of the category: the algebra acts faithfully on the left and on the right, the two actions commute, the quaternionic adjoint exchanges them, and the whole is the standard bimodule of a division algebra.

## The Two-Sided Operator

**The family over $\mathbb{B}_{\mathrm{spl}}\times\mathbb{B}_{\mathrm{spl}}$, blockwise, and the reach is the product of the two quaternionic cones.**

**Definition.** The two-sided operator of the pair $(\tilde Q,\tilde Q_2)$ is
$$
L_{\tilde Q}R_{\tilde Q_2}(\tilde X)=\tilde Q\tilde X\tilde Q_2=\begin{pmatrix}L_{\tilde Q_{+}}R_{\tilde Q_{2+}}(\tilde X_{+})&0\\ 0&L_{\tilde Q_{-}}R_{\tilde Q_{2-}}(\tilde X_{-})\end{pmatrix},
$$
so the family is the product of the two quaternionic families.

**The composition.**
$$
L_{\tilde Q_{1}}R_{\tilde Q_{2,1}}\circ L_{\tilde Q_{2}}R_{\tilde Q_{2,2}}=L_{\tilde Q_{1}\tilde Q_{2}}R_{\tilde Q_{2,2}\tilde Q_{2,1}},
$$
the order reverses in the second slot, and the pair of pairs is a semigroup under the product $(\tilde Q,\tilde Q_2)(\tilde Q_3,\tilde Q_4)=(\tilde Q\tilde Q_3,\tilde Q_4\tilde Q_2)$, with unit $(1,1)$.

**The fibre.** Two pairs give the same operator exactly when they differ by a central rescaling in opposite directions,
$$
L_{\tilde Q\lambda}R_{\lambda^{-1}\tilde Q_2}=L_{\tilde Q}R_{\tilde Q_2}\qquad \text{for every }\lambda\in{\mathbb{C}_{\mathrm{spl}}}^{\times},
$$
with ${\mathbb{C}_{\mathrm{spl}}}^{\times}=\mathbb{R}^{\times}\times\mathbb{R}^{\times}$ blockwise, so the fibre over a nonzero operator is two-dimensional and the reach has real dimension $16-2=14$, which agrees with the block count $7+7$.

**The reach.** The reach
$$
\mathcal C_{R}=\bigl\{L_{\tilde Q}R_{\tilde Q_2}\bigr\}\subset\mathrm{End}_{\mathbb{R}}(\mathbb{B}_{\mathrm{spl}})
$$
is the product of the two quaternionic cones, each of real dimension seven inside the sixteen of $\mathrm{End}_{\mathbb{R}}(\mathbb{H})$. It is **not** a subspace: a sum of two elements of a block need not be in the block, because the quaternionic cone is not closed under addition. It is not convex either, for the same reason. It is a genuine semialgebraic cone with two independent irreducible components, and it is the object that the coefficient array of the next sections tests.

**The zero operator.** $L_{\tilde Q}R_{\tilde Q_2}=0$ exactly when each block has a vanishing factor, that is when
$$
\tilde Q_{+}=0\ \text{or}\ \tilde Q_{2+}=0,\qquad\text{and}\qquad \tilde Q_{-}=0\ \text{or}\ \tilde Q_{2-}=0,
$$
so the zero operator is attained by nonzero pairs — $\tilde Q=\tilde\Pi_{1}$ and $\tilde Q_2=\tilde\Pi_{2}$, for example — and the three other combinations of the two idempotents. The zero set of the map $(\tilde Q,\tilde Q_2)\mapsto L_{\tilde Q}R_{\tilde Q_2}$ is therefore a union of four products, of real dimension $4+8=12$ each, and the pairs that achieve the zero operator are the ones that the length discussion below must count.

**The units.** The operators of the family that are invertible are those with both blocks nonzero, that is
$$
L_{\tilde Q}R_{\tilde Q_2}\in GL(\mathbb{B}_{\mathrm{spl}})\iff \tilde Q_{\pm}\neq0,\ \tilde Q_{2\pm}\neq0 ,
$$
and the map from the pairs to the invertible operators is a surjection with two-dimensional fibres. The stabiliser of the identity is
$$
\{(t,t^{-1}):t\in{\mathbb{C}_{\mathrm{spl}}}^{\times}\}=\mathbb{R}^{\times}\times\mathbb{R}^{\times},
$$
the centre, and the group of pairs modulo the stabiliser is the product of the two projective quaternion groups.

## The Sandwich

**Four words, four operators, and here the sandwich does not collapse.**

**The four words.** With the four slots of the corpus,
$$
T^{\sigma_{1}\sigma_{2}}_{\tilde Q}(\tilde X)=\tilde Q^{\sigma_{1}}\tilde X\tilde Q^{\sigma_{2}},
$$
the plain ($\sigma_{1}=\sigma_{2}=1$), quaternionic ($\sigma_{1}=\sigma_{2}=\natural$), Hermitian ($\sigma_{1}=1$, $\sigma_{2}=*$) and Krein ($\sigma_{1}=\natural$, $\sigma_{2}=*$) sandwiches. The four are the four operators the corpus uses, and the model reads them blockwise with the corresponding quaternion operations.

**The quaternionic sandwich is conformal.** The main one is
$$
\Phi_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{\natural},
$$
and it is blockwise the quaternionic sandwich $x\mapsto uxu^{\natural}$. Since $u^{\natural}u=N(u)$ is a real scalar,
$$
N\bigl(uxu^{\natural}\bigr)=N(u)\,N(x)\,N(u^{\natural})=N(u)^{2}N(x),
$$
so the operator is a **conformal** map of the quaternionic norm, with factor $N(u)^{2}$ in each block. This is the analogue of the modulus sandwich of the reduced biquaternion category, and it is strictly richer: there the sandwich was a scalar on each block, whereas here it is a full quaternionic conjugation followed by a scaling, so it rotates as well as scales.

**The invariant cone.** On the Hermitian subspace $\mathbb{B}_{\Psi}$ the Hermitian sandwich
$$
\Phi_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*},\qquad \tilde X^{*}=\tilde X,
$$
is again Hermitian, because $(\tilde Q\tilde X\tilde Q^{*})^{*}=\tilde Q\tilde X^{*}\tilde Q^{*}$, and positive definite when $\tilde Q$ is a unit, because each block is a positive quaternionic operator. So the group of units acts on the open cone of positive Hermitian elements, and this action is the conformal action of the category on the Minkowski space of signature $(1,3)$ of the norms section of the general article.

**The kernel.** The units giving the identity operator are those that centralise every element and square to one,
$$
\{\tilde Q:\tilde Q\tilde X\tilde Q^{*}=\tilde X\ \forall\tilde X\}=\{\pm1,\pm j\},
$$
a four-group, because the centraliser is $\mathbb{C}_{\mathrm{spl}}$ and the units of $\mathbb{C}_{\mathrm{spl}}$ are the split-complex units $\{\pm e^{\phi j}\}$, cut down by the condition $Q^{2}=1$ to the four elements. So the kernel of the sandwich map is a four-group and not a torus, and the difference from the reduced biquaternion category, where the kernel was the whole torus $T^{2}$, is that the quaternion blocks have no commuting phases: the phases are noncommutative and the sandwich sees them.

**The plain sandwich.** $x\mapsto \tilde Q\tilde X\tilde Q$ is not conformal in the same sense, since $u^{2}$ is not real, and it is the operator of the plain product and of the functional calculus: its powers give $\tilde Q^{n}\tilde X\tilde Q^{n}$, and its kernel over the family is again the four-group.

**The two involution sandwiches.** The bar and the star sandwiches,
$$
\tilde X\longmapsto\tilde Q\tilde X\bar{\tilde Q},\qquad \tilde X\longmapsto\tilde Q\tilde X\tilde Q^{\flat},
$$
are the two-sided operators with the second parameter a conjugation. In the model the bar is the swap, so the first is $L_{\tilde Q}R_{\bar{\tilde Q}}$ and the second is $L_{\tilde Q}R_{-\tilde Q^{*}}$: the two are the sandwich with the swapped blocks up to a sign, so the four words reduce to two in this category, one with the conjugations inside the blocks and one with the swap.

## The Kronecker Display and the Coefficient Matrix

**The display is block diagonal, one Kronecker product per block, and the coefficient array is tested blockwise.**

**The display.** The operator $L_{\tilde Q}R_{\tilde Q_2}$ acts on $\mathbb{B}_{\mathrm{spl}}$ and its realification acts on $\mathbb{R}^{8}=\mathbb{R}^{4}\oplus\mathbb{R}^{4}$, so its matrix is block diagonal with two blocks of $4\times4$ real entries. Each block is a Kronecker product,
$$
\mathsf K_{\pm}=L(\tilde Q_{2\pm})^{\mathsf T}\otimes L(\tilde Q_{\pm})\in M_{16}(\mathbb{R}),
$$
where $L(u)$ is the $4\times4$ real matrix of the left multiplication by the quaternion $u$; the display of the pair is the direct sum
$$
\mathsf K=\mathsf K_{+}\oplus\mathsf K_{-}\in M_{32}(\mathbb{R}).
$$

**The invariants.** The trace and the determinant multiply and add over the two blocks:
$$
\operatorname{tr}\mathsf K=16\bigl(\mathrm{Sc}\tilde Q_{+}\,\mathrm{Sc}\tilde Q_{2+}+\mathrm{Sc}\tilde Q_{-}\,\mathrm{Sc}\tilde Q_{2-}\bigr),\qquad \det\mathsf K=\bigl(N(\tilde Q_{+})N(\tilde Q_{2+})\bigr)^{4}\bigl(N(\tilde Q_{-})N(\tilde Q_{2-})\bigr)^{4},
$$
and the rank is
$$
\operatorname{rank}\mathsf K=16\bigl(\operatorname{rank}(\tilde Q_{+})\operatorname{rank}(\tilde Q_{2+})+\operatorname{rank}(\tilde Q_{-})\operatorname{rank}(\tilde Q_{2-})\bigr)\in\{0,16,32\},
$$
because each block contributes sixteen exactly when both its quaternions are nonzero.

**The coefficient matrix.** Choose the real basis of the algebra
$$
e_{\epsilon\mu}=e_{\epsilon}e_{\mu},\qquad \epsilon\in\{1,j\},\ \mu\in\{t,x,y,z\},
$$
of eight elements, and expand a two-sided operator in the basis of the products:
$$
L_{\tilde Q}R_{\tilde Q_2}=\sum_{\epsilon,\mu,\eta,\nu}c^{(\epsilon\mu)(\eta\nu)}\,L_{e_{\epsilon\mu}}R_{e_{\eta\nu}} .
$$
The coefficients form an $8\times8$ real array $c$. Because the algebra is a product, the array is block diagonal in the indices $\epsilon$ and $\eta$: the coefficients with $\epsilon\neq\eta$ vanish, since a product with one factor in each block is zero. So the array is the direct sum of two $4\times4$ real arrays, one per block, and each of the two is the coefficient array of a quaternion two-sided operator.

**The criterion.** By the quaternionic criterion, a block array is realisable exactly when it has rank at most one,
$$
c^{(++)}\ \text{realisable}\iff\operatorname{rank}c^{(++)}\le1,\qquad c^{(--)}\ \text{realisable}\iff\operatorname{rank}c^{(--)}\le1,
$$
so the test of the category is **blockwise linear** and the reach is the product of the two cones. This is the point of the section: the rank-one test of the quaternions applies twice, independently, and the two applications do not interact.

**The dimension count.** The parameter space is sixteen, the stabiliser is two-dimensional, and the reach is fourteen: $7+7$. The two blocks are independent and the count is additive, unlike the count of the reduced biquaternion category where the two blocks were tied by one complex parameter.

## The Rank and the Invariants

**The rank ladder has three values, the trace is not an invariant, and the determinant is the product of the two Study determinants.**

**The rank.** For every element,
$$
\operatorname{rank}_{\mathbb{H}}\mathsf M(\tilde Q)\in\{0,1,2\},\qquad \operatorname{rank}_{\mathbb{R}}\mathsf L_{\tilde Q}\in\{0,4,8\},
$$
with the strata of the general article: the zero element, the union of the two punctured ideals, and the units.

**The two-sided rank.** For a pair,
$$
\operatorname{rank}_{\mathbb{H}}L_{\tilde Q}R_{\tilde Q_2}=\operatorname{rank}(\tilde Q_{+})\operatorname{rank}(\tilde Q_{2+})+\operatorname{rank}(\tilde Q_{-})\operatorname{rank}(\tilde Q_{2-})\in\{0,1,2\},
$$
with the same three strata, and the operator fails exactly when one of the two blocks has a vanishing factor.

**The invariants.** The determinant and the trace of the model are the objects of the general article; for the operator the relevant pair is the Study determinant and the reduced trace of the two-sided operator,
$$
\det L_{\tilde Q}R_{\tilde Q_2}=N(\tilde Q_{+})N(\tilde Q_{2+})\,N(\tilde Q_{-})N(\tilde Q_{2-}),\qquad \operatorname{Trd}L_{\tilde Q}R_{\tilde Q_2}=4\bigl(\mathrm{Sc}\tilde Q_{+}\mathrm{Sc}\tilde Q_{2+}+\mathrm{Sc}\tilde Q_{-}\mathrm{Sc}\tilde Q_{2-}\bigr),
$$
and the reduced trace is additive over sums of operators while the determinant is multiplicative over composition.

**The failure of the trace as a functional.** The naive trace of the two-sided operator is the quaternion $\tilde Q_{+}\tilde Q_{2+}+\tilde Q_{-}\tilde Q_{2-}$, which is not central and not invariant under the change of basis; only its scalar part is. So the operator theory of this category has one invariant functional, the reduced trace, and one multiplicative functional, the determinant, and no third.

## The Pair as a Semigroup

**Composition, the unit, the stabiliser, the isometries and the multiplicative pairs.**

**The semigroup.** The pairs form the semigroup $\mathbb{B}_{\mathrm{spl}}\times\mathbb{B}_{\mathrm{spl}}$ under $(\tilde Q,\tilde Q_2)(\tilde Q_3,\tilde Q_4)=(\tilde Q\tilde Q_3,\tilde Q_4\tilde Q_2)$, with the two-sided operators as a quotient by the central stabiliser, and the map is a homomorphism of semigroups. The units of the semigroup are the pairs with both entries in the group of units, and they act on the algebra by the two-sided operators.

**The isometries.** The pairs whose two-sided operator preserves a form:

| form | condition | group per block | compact retract |
|---|---|---|---|
| quaternionic | $N(\tilde Q)N(\tilde Q_2)=1$ | $\mathbb{R}\times SU(2)\times SU(2)$, modulo the sign | $S^{3}\times S^{3}$ |
| plain | $\mathrm{Sc}(\tilde QX\tilde Q_2)=\mathrm{Sc}(X)$ for all $X$ | the same, with the two factors transposed | $S^{3}\times S^{3}$ |
| Hermitian | the same condition on the Hermitian subspace | $SU(2)\times SU(2)$ per block | $S^{3}\times S^{3}$ |

so the compact retract of the isometry group of the category is a product of four three-spheres, in contrast with the torus $T^{2}$ of the reduced biquaternion category and with the single three-sphere of the complex category. The reason is that the quaternionic blocks admit the noncommutative phases, and the phases are the three-spheres.

**The multiplicative pairs.** The pairs $(\tilde Q,\tilde Q^{\natural})$ are those whose operator is a conformal map, by the computation of the sandwich section, and the pairs $(\tilde Q,\tilde Q^{-1})$ are those whose plain operator is the identity composed with the inner automorphism: since the algebra is a product of division rings, the inner automorphism group is $(SU(2)\times SU(2))/\{\pm1\}$ per block, and it is the gauge of the category.

**The gauge.** The inner automorphisms of $\mathbb{B}_{\mathrm{spl}}$ are the conjugations by the units, and they act blockwise by the inner automorphisms of $\mathbb{H}$. The quotient by the inner automorphisms is the two-block outer group, and the model realises the inner ones as the pairs $(\tilde Q,\tilde Q^{-1})$. Since $\mathbb{H}$ is a division ring, the inner automorphism group is the whole of the automorphism group, so the outer group is trivial and the gauge is the whole of $SU(2)\times SU(2)$ per block modulo the sign. The difference from the reduced biquaternion category is large: there the algebra is commutative, the inner automorphism group was trivial, and the whole operator family was the multiplicative gauge.

## The Cone and the Coefficient Matrix

**The parameter space is sixteen-dimensional, the fibre is two-dimensional, the reach is fourteen, and the span is thirty-two.**

**The map.** The bilinear map of the pair,
$$
\beta:\mathbb{B}_{\mathrm{spl}}\times\mathbb{B}_{\mathrm{spl}}\longrightarrow\mathrm{End}_{\mathbb{R}}(\mathbb{B}_{\mathrm{spl}}),\qquad \beta(\tilde Q,\tilde Q_2)=L_{\tilde Q}R_{\tilde Q_2},
$$
is blockwise the quaternionic map, and its image is the product of the two cones.

**The count.** The parameter space has real dimension sixteen. The fibre over a nonzero operator is the two-dimensional centre acting by inverse scaling, so the reach is fourteen-dimensional. The span is the whole block diagonal part of the ambient, of dimension thirty-two, so the deficit of the span over the reach is eighteen. The honest count is blockwise: in each block the cone has dimension seven and its span has dimension sixteen, so each block misses nine, and the two blocks miss eighteen. The off-diagonal corners of the ambient contribute to neither number, because they lie outside the span from the start: they are excluded by the linear condition and not by the cone condition.

**The membership test.** A real operator $M$ of the ambient is in the reach exactly when

1. it preserves the two blocks, that is $M=\mathrm{diag}(M_{+},M_{-})$ with $M_{\pm}\in\mathrm{End}_{\mathbb{R}}(\mathbb{H})$;
2. each block is in the quaternionic cone, that is $\operatorname{rank}c(M_{\pm})\le1$ in the coefficient array of that block.

The first condition is linear and of codimension thirty-two; the second is the rank-one condition of a quaternion and it is **not** linear; so the reach is semialgebraic, of dimension fourteen, and not a subspace. This is the structural difference from the reduced biquaternion category, where both conditions were linear.

**The comparison with the quaternion and the biquaternion categories.** The three tables are the same table read at three ranks: the complex category has a line, the reduced biquaternion category a subspace of codimension two, the split biquaternion category a product of two cones, and the biquaternion category a single cone of codimension nine. The split biquaternion category is the only one in which the family is a **product** of two genuinely non-linear pieces.

## The Length

**The length is at most four and not at most eight, and the values are the five integers from zero to four.**

**Definition.** The length of a real operator $M$ in the span is the least $r$ such that
$$
M=\sum_{i=1}^{r}L_{\tilde Q_{i}}R_{\tilde Q_{2i}} .
$$

**Theorem (the length ladder).** For every operator in the span,
$$
\ell(M)\le4,
$$
and every value in $\{0,1,2,3,4\}$ is attained. The length is not additive over the two blocks:
$$
\ell\bigl(\mathrm{diag}(M_{+},M_{-})\bigr)=\max\bigl(\ell(M_{+}),\ell(M_{-})\bigr),
$$
because one index can serve both blocks, and this is why the bound is four and not eight.

*Proof.* Each block is a quaternion two-sided operator problem, whose ladder is the quaternionic one: every real endomorphism of the four-dimensional quaternionic space is a sum of at most four rank-one terms, so each block has length at most four. Padding the shorter block with zeros gives a common index set of size $\max$, and the two sums combine blockwise. The bound is attained by the operators that are not sums of three terms in either block.

**The zero operator.** The zero operator has length zero, and it is also attained by the nonzero pairs of the two-sided section. The pair attaining it is not the zero pair, so the semigroup has a nonzero kernel element and the length of the zero operator is a convention, as in the reduced biquaternion category.

**The identity.** The identity is $L_{1}R_{1}$, of length one, and the identity of the ambient — the swap $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ — is not in the span at all, so its length is undefined. This is the sharpest sign that the ambient of the category is the block diagonal part and not the whole of $M_{8}(\mathbb{R})$.

**The reading.** The ladder of the block is $1,4,7,16$ for the biquaternions, $1,4,7$ for the split biquaternions in each block and hence at most four for the pair, $1,2,3,4$ for the complex numbers, and $1,2,3,4$ for the dual numbers. The split biquaternion category is the only one where the ladder is a maximum over two independent blocks, and the maximum is the operation that keeps the bound at four.

## The Two Ranks

**The matrix rank and the coefficient rank of the category, and the passage between them.**

**The two columns.** For every element and every pair,

| object | $\mathbb{H}$-rank | real rank | coefficient rank |
|---|---|---|---|
| $\mathsf M(\tilde Q)$ | $\{0,1,2\}$ | $\{0,4,8\}$ | --- |
| $L_{\tilde Q}R_{\tilde Q_2}$ | $\{0,1,2\}$ | $\{0,4,8\}$ | per block $\{0,1\}$ |
| $\mathsf K$ | --- | $\{0,16,32\}$ | --- |

**The passage.** The passages are the four-times map for the realification and the blockwise rank-one test for the coefficient array. Unlike the quaternion family, where the coefficient rank and the matrix rank of an operator are related by a linear condition of rank one against the two-sided rank, here the relation holds **blockwise and independently**: the coefficient rank of a block is one exactly when the block's matrix is nonzero, so the two ranks agree in the only sense available — the block is in the cone or it is not.

**The table of the block.** The seven categories of the block have seven ladders of ranks, and the split biquaternion category is the one where the ladder has the fewest values because the divisions are the deepest: each block is a division ring, so each block's rank is zero or full and the total has three values.

## What the Pair Buys and Does Not

**It buys a genuine bimodule, a genuine cone and a genuine conformal sandwich, and it does not buy a simple algebra, a matrix model, a central trace, an adjugate that is a conjugation, or a length above four.**

| question | reduced biquaternion | split biquaternion | biquaternion |
|---|---|---|---|
| the model | a subspace of $M_{2}(\mathbb{C})$ | a subspace of $M_{2}(\mathbb{H})$ | the ambient |
| the algebra | a product of two fields | a product of two division rings | a matrix algebra |
| $L$ versus $R$ | equal | independent | independent |
| the two-sided family | a subspace | a product of two cones | a cone |
| the trace | central-ish, $2Q_{\blacktriangle}$ | a quaternion, non-central | a complex number |
| the determinant | $Q_{+}Q_{-}$ | $N(\tilde Q_{+})N(\tilde Q_{-})$ | a complex number |
| the adjugate | a conjugation | not a conjugation | a conjugation |
| the length | $\{0,1\}$ | $\{0,1,2,3,4\}$ | $1,4,7,16$ |
| the sandwich kernel | the torus $T^{2}$ | the four-group $\{\pm1,\pm j\}$ | a three-sphere |

**What it buys.** A bimodule: the two copies of the algebra are independent, the quaternionic adjoint exchanges them, and the operator theory has both sides. A cone: the two-sided family is not a subspace, so the length is a genuine invariant and the reach is semialgebraic. A conformal sandwich: the quaternionic sandwich is a conformal map with the factor $N(\tilde Q)^{2}$, which the reduced biquaternion sandwich was not. And a positive cone: the Hermitian sandwich preserves the open positive cone of the Hermitian subspace and acts on it as the conformal group of the Minkowski space of signature $(1,3)$.

**What it does not buy.** A simple algebra: the algebra is a product, the model is a subspace, and the off-diagonal corners are structurally empty. A central trace: the trace is a quaternion and only the reduced trace is invariant. An adjugate that is a conjugation: the determinant is a product of two norms and the cofactors cross. A length above four: the two blocks share the index. And a matrix model: the algebra is not isomorphic to any full matrix algebra, and the diagonal model is the best there is.

**The reading of the category.** The split biquaternion category is the only one of the block in which the algebra is semisimple and not simple, the model is a proper subalgebra of a matrix algebra over a division ring, and the two-sided family is a product of two cones. It is the category of the two independent quaternionic variables: everything that is true of the biquaternion category is true twice, side by side, and everything that is not true is the absence of the off-diagonal.

## Summary

1. The carrier is $\mathbb{B}_{\mathrm{spl}}$ of real dimension eight and quaternionic dimension two; the ambient of the category is the block diagonal part of $M_{8}(\mathbb{R})$, of dimension thirty-two; the whole ambient is sixty-four.
2. The left and the right multiplications are two commuting faithful copies, independent because the algebra is noncommutative, meeting in the two-dimensional centre, block diagonal, and additive in rank over the two blocks.
3. The three adjoints: the plain form exchanges the two copies, $L_{\tilde Q}^{*}=R_{\tilde Q}$; the quaternionic and the Hermitian forms keep the sides and conjugate the parameter, $L_{\tilde Q}^{*}=L_{\tilde Q^{\natural}}$ and $L_{\tilde Q}^{*}=L_{\tilde Q^{*}}$.
4. The two-sided operators are blockwise, compose with the order reversed in the second slot, have a two-dimensional central stabiliser, and reach a fourteen-dimensional product of two quaternionic cones inside a thirty-two-dimensional span.
5. The zero operator is attained by nonzero pairs, and the pairs that attain it are the four combinations of the two idempotents with the two idempotents.
6. The sandwich is genuine here: the quaternionic sandwich is conformal with factor $N(\tilde Q)^{2}$, its kernel is the four-group $\{\pm1,\pm j\}$, and on the Hermitian subspace it acts on the positive cone as the conformal group of the Minkowski space of signature $(1,3)$.
7. The Kronecker display is the direct sum of two $16\times16$ real blocks, with rank in $\{0,16,32\}$, trace $16$ times the sum of the two block products of scalar parts, and determinant the fourth powers of the two products of norms.
8. The coefficient array is block diagonal in the split index, each block is a $4\times4$ real array, and the criterion is the blockwise rank-one test.
9. The length is at most four and the value is the maximum of the two block lengths, because one index serves both blocks; the identity of the ambient, the swap, is not in the span.
10. The two ranks are the $\mathbb{H}$-rank in $\{0,1,2\}$ and the real rank in $\{0,4,8\}$, and the coefficient rank is the blockwise indicator of nonvanishing.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $L_{\tilde Q}R_{\tilde Q_2}(\tilde X)=\tilde Q\tilde X\tilde Q_2$ | the two-sided operator | this article |
| $L_{\tilde Q},R_{\tilde Q}$ | the left and the right multiplications, block diagonal | this article |
| $\mathcal C_{R}$ | the reach, the product of the two quaternionic cones | this article |
| $\mathsf K=\mathsf K_{+}\oplus\mathsf K_{-}$ | the Kronecker display, two $16\times16$ real blocks | this article |
| $c$ | the coefficient array, block diagonal in the split index | this article |
| $\ell(M)$ | the length, at most four | this article |
| $\Phi_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{\natural}$ | the quaternionic sandwich, conformal | this article |
| $N(u)=uu^{\natural}$ | the quaternion norm | *$M_{2}(\mathbb{H})$ Diagonal Representation* |
| $\{\pm1,\pm j\}$ | the kernel of the sandwich | this article |
| $\mathbb{B}_{\Psi}$ | the Hermitian subspace, the Minkowski space of signature $(1,3)$ | *Split-Biquaternion Algebra* |

## Further Reading

- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the bimodule structure of a division algebra, the semigroup of pairs and the stabiliser of the identity.
- F. Zhang, *Quaternions and Matrices of Quaternions* (Linear Algebra and its Applications 251, 1997), for the quaternionic cone of rank-one maps, the coefficient array and the two-sided rank.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the Kronecker product, the rank of a sum of tensor products and the block diagonal arithmetic of trace and determinant.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the conformal action of the quaternion group of units on the Minkowski space of signature $(1,3)$.
- Igor Frenkel and Matvei Libine, *Quaternionic Analysis, Representation Theory and Physics* (Advances in Mathematics 218, 2008), for the conformal group of the quaternions and the four-dimensional representation of $SL_{2}(\mathbb{C})$ on the Hermitian subspace.
