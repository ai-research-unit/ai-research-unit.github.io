# __$M_2(\mathbb{R})$ Cayley Representation : Operators__

## Introduction

**The same operator layer, at its smallest.** The carrier is $\mathbb{C}$, of real dimension two, and the ambient is

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{C})\cong M_2(\mathbb{R}),
$$

of dimension four. Every operator of the series is a real-linear map of $\mathbb{C}$; the two-sided layer is built from the two one-sided families, and here both families are the same family. So the ambient is four-dimensional, the family of two-sided operators is a two-dimensional subspace of it, and the general theory has nothing left to stratify.

**The four objects of the general theory, and what becomes of them.**

| object | general case | here |
|---|---|---|
| the two one-sided families | two copies, meeting in the scalars | one copy, they coincide |
| the cone of products | a cone of dimension $4n-1$ | a linear subspace of dimension two |
| the length | a rank in $\{0,\dots,n\}$ | in $\{0,1\}$, and only inside the span |
| the two ranks | operator rank against coefficient rank | $2$ against $1$, diverging at every nonzero member |

Three of the four collapse and the fourth survives in a form that shows the phenomenon without any of the machinery. This article is therefore the place where the definitions of the operator layer are seen to be necessary: what disappears here is not the theory but the room it needs.

**The one non-trivial feature.** The pair $(\tilde q,\tilde p)$ of the other categories collapses to the single product $QP$, because the algebra is commutative. But the *formula* $X\mapsto QXP$ defines two different operators depending on which space it acts on: on the carrier it is the multiplication by $QP$, of rank two, while on the space of all matrices it is the Kronecker product, of rank four. The gap between the two is the only place in this category where the operator layer says something the model article does not, and it is the subject of the section on the Kronecker display.

**Boundaries.** The model, the Cayley display, the trace, the determinant, the adjugate and the subspaces are *$M_2(\mathbb{R})$ Cayley Representation*. The abstract one-sided operators of the algebra are *The One-Sided Operators* of the complex algebra, and the two-sided ones are *Two-Sided Operators on the Complex Algebra*; this article does not replace them. The same operator layer for the other algebra of the block is *The Matrix Element Representations of the Complexoid*.

**Conventions.** The carrier has the basis $(1,i)$; a column of two real numbers is read as $x+iy$. The operator $L_Q$ is multiplication by $Q$, with matrix $\mathsf{M}_2(Q)=qI_2+q'J$; $R_Q$ is the same. The two-sided operator is $L_{Q}R_{P}(X)=QXP$. The coefficient array of an operator is its array of coordinates in the basis $\{T_1,T_i\}=\{I_2,J\}$ of the family. The Frobenius form is $\langle X,Y\rangle_F=\operatorname{tr}(X^{\mathsf T}Y)$ and the plain form is $\langle X,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(XY)$.

## The One-Sided Operators

**The family.** The left multiplications are the Cayley matrices, and the family is the image of the model:

$$
L(\mathbb{C})=\{\mathsf{M}_2(Q):Q\in\mathbb{C}\},\qquad \dim_{\mathbb{R}}L(\mathbb{C})=2 .
$$

The right multiplications are the same set, and the intersection and the sum are the family itself:

$$
L(\mathbb{C})=R(\mathbb{C}),\qquad L(\mathbb{C})+R(\mathbb{C})=L(\mathbb{C}),\qquad \dim=2 .
$$

**The kernel and the image.** For $Q\neq0$ the operator $L_Q$ is a bijection: it is injective because $QX=0$ forces $X=0$ in a field, and it is surjective because $X=Q^{-1}Y$ solves $QX=Y$. So

$$
\ker L_Q=\{0\},\qquad \operatorname{im}L_Q=\mathbb{C},\qquad \operatorname{rank}L_Q=2,
$$

and the kernel is never a line, never a hyperplane, and never depends on $Q$. The rank is constant on the punctured algebra: there is no rank drop anywhere in the family, which is the operator-level statement that $\mathbb{C}$ has no zero divisor.

**The adjoint, twice.** The two pairings of the ambient give two different adjoints, and the difference is the whole of the involution theory of the category.

- For the plain form, $\langle L_QX,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(QXY)=\operatorname{tr}(X\cdot YQ)=\langle X,R_QY\rangle_{\operatorname{tr}}$, so the adjoint is $R_Q=L_Q$: the operator is self-adjoint, and this is commutativity.
- For the Frobenius form, $\langle L_QX,Y\rangle_F=\operatorname{tr}\bigl((QX)^{\mathsf T}Y\bigr)=\operatorname{tr}\bigl(X^{\mathsf T}Q^{\mathsf T}Y\bigr)=\langle X,L_{Q^{\mathsf T}}Y\rangle_F$, and $Q^{\mathsf T}=\bar Q$, so the adjoint is $L_{\bar Q}$: the operator's adjoint is the operator of the conjugate.

**The reading.** The pair of statements is the model's form of the pair of adjoints of the whole series. The plain adjoint is the identity because the algebra is commutative; the Frobenius adjoint is the conjugation, which in this model is the transpose. So $L$ is a **$*$-representation** of the involutive algebra $(\mathbb{C},\text{conjugation})$ on the Hilbert space $(\mathbb{C},\langle\cdot,\cdot\rangle_F)$, faithfully and irreducibly, and it is the smallest such representation in the series.

**The two copies, counted.** Since the copies coincide, there is no seven-dimensional sum, no mutual centraliser theorem to state, and no signed transpose to relate the two. The double centraliser holds in the form $C(L(\mathbb{C}))=L(\mathbb{C})$ of the model article, and the operator layer inherits the degeneracy.

## The Two-Sided Operator

**Definition and collapse.** For a pair $(Q,P)$,

$$
L_{Q}R_{P}(X)=QXP,\qquad L_{Q}R_{P}=\mathsf{M}_2(QP)=L_{QP}.
$$

**The reading.** The two-sided operator depends on the pair only through the product, so the parametrisation by two complex numbers has a two-real-dimensional redundancy: $L_{Q}R_{P}=L_{Q'}R_{P'}$ exactly when $QP=Q'P'$. The pair is not a pair, and the notation $L_{Q}R_{P}$ is kept only because the general formula has two slots.

**The scaling.** For $\lambda\neq0$,

$$
L_{\lambda Q}R_{P/\lambda}=L_{Q}R_{P},
$$

so the kernel of the parametrisation contains the one-dimensional group of rescalings, and the four real parameters of the pair fall to the two of the product. The picture of the general theory — a parameter count $2\dim$ falling to $2\dim-1$ — is here a count of four falling to two, because the two slots are not independent.

**The invariants.**

$$
\operatorname{rank}L_{Q}R_{P}=\begin{cases}2,&QP\neq0\\0,&QP=0,\end{cases}\qquad
\operatorname{tr}L_{Q}R_{P}=2\operatorname{Re}(QP),\qquad
\det L_{Q}R_{P}=N(QP),\qquad
\langle L_{Q}R_{P}\rangle_*=2N(QP).
$$

**Proof.** $L_{Q}R_{P}$ is the matrix $\mathsf{M}_2(QP)$, so the four quantities are the trace, the determinant and the Frobenius norm of a Cayley matrix, read from the model article.

**The trace, and what it is not.** The trace of the operator is $2\operatorname{Re}(QP)$ and not $(2\operatorname{Re}Q)(2\operatorname{Re}P)$: the trace of a product is not the product of the traces. The distinction becomes visible in the Kronecker display, whose trace is $4\operatorname{Re}Q\operatorname{Re}P$, and the two numbers are different operators' traces, not two computations of one.

**The inner automorphisms.** The operator $L_{Q}R_{Q^{-1}}$ is $X\mapsto QXQ^{-1}$, the conjugation by $Q$. On the carrier it is the identity, because the algebra is commutative:

$$
L_{Q}R_{Q^{-1}}=\mathsf{M}_2(QQ^{-1})=\mathsf{M}_2(1)=I_2 .
$$

On the ambient it is not the identity. Writing $Q=\lvert Q\rvert e^{i\theta}$, the scalar cancels and the operator is $X\mapsto R_\theta XR_\theta^{-1}$, whose module structure on $M_2(\mathbb{R})$ is

$$
M_2(\mathbb{R})=\underbrace{\mathbb{R}I_2\oplus\mathbb{R}J}_{\text{fixed}}\oplus\underbrace{\{\text{symmetric traceless}\}}_{\text{rotated by }2\theta},
$$

so the scalars and the imaginary line are fixed and the two-dimensional space of traceless symmetric matrices is rotated by twice the angle. The map $\theta\mapsto\mathrm{Ad}_{R_\theta}$ is therefore $2$ to $1$ onto the rotations about $J$: the smallest instance of the double cover $\mathrm{SU}(2)\to SO(3)$ of the quaternion category, and the reason a rotation acts on the plane as a half-turn of the tensor square.

**The reading.** The inner automorphisms therefore separate two questions that the general theory asks at once: the group of automorphisms of the algebra, which is $\{\mathrm{id},\text{conj}\}$ and has nothing to do with the carrier's multiplications, and the group of inner automorphisms of the ambient, which is a circle acting non-trivially on the matrices and trivially on the algebra. In the quaternion category the two coincided, because the algebra was not commutative and its automorphisms were inner.

## The Kronecker Display

**The identity.** Vectorising a matrix by columns, $\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}(X)$; hence the operator $X\mapsto QXP$ on the four-dimensional space of matrices has the matrix

$$
K_{Q,P}=\mathsf{M}_2(P)^{\mathsf T}\otimes\mathsf{M}_2(Q),
$$

of size $4\times4$. This is the **Kronecker display** of the two-sided operator, and it is the only display in the category.

**The invariants of the display.** Since $A=\mathsf{M}_2(Q)$ and $B=\mathsf{M}_2(P)$ are conformal,

$$
K_{Q,P}^{\mathsf T}K_{Q,P}=N(Q)N(P)\,I_4,\qquad
\det K_{Q,P}=N(Q)^{2}N(P)^{2},\qquad
\operatorname{tr}K_{Q,P}=4\operatorname{Re}Q\operatorname{Re}P,\qquad
\operatorname{rank}K_{Q,P}=4 .
$$

**Proof.** $(B^{\mathsf T}\otimes A)^{\mathsf T}(B^{\mathsf T}\otimes A)=BB^{\mathsf T}\otimes A^{\mathsf T}A$, and each factor is a scalar matrix; the determinant of a Kronecker product is $\det(B^{\mathsf T})^{2}\det(A)^{2}$; the trace is the product of the traces; the rank is the product of the ranks, and both factors are invertible for non-zero parameters.

**The reading.** The display is a conformal matrix of $M_4(\mathbb{R})$, of the same shape as its factors but twice as large, and its determinant is the square of the product of the two norms. So the display's four numbers are the *second rank* of the series, the one the split-quaternion category tabulated as $\operatorname{rank}A\cdot\operatorname{rank}B$: it is the product of two ranks, and here the two factors are never singular, so the ladder is the two-point set $\{0,4\}$.

**The two operators.** The distinction that the category inverts is this: the same formula defines an operator of rank two on the carrier and an operator of rank four on the space of matrices. Neither is the other; the second is the first acting on the tensor square. In the quaternion category the display and the carrier had the same dimension, so the distinction was invisible; here it is the entire content of the section.

**The coefficient array.** The pair itself is described by the $2\times2$ array of products of coordinates,

$$
c(Q,P)=\begin{pmatrix}qp&qp'\\ q'p&q'p'\end{pmatrix},\qquad \operatorname{rank}c(Q,P)=1\ \text{for all non-zero pairs},
$$

the array of the bilinear map $(x,y)\mapsto Qx\cdot Py$, which is the coefficient array of the tensor $Q\otimes P\in\mathbb{C}\otimes\mathbb{C}$. Its rank is one and it is the array of the *pair*, not of the operator.

## The Rank and the Invariants

**The table.** Two operators, one formula.

| quantity | on the carrier, $T=\mathsf{M}_2(QP)$ | on the matrices, $K=\mathsf{M}_2(P)^{\mathsf T}\otimes\mathsf{M}_2(Q)$ |
|---|---|---|
| size | $2\times2$ | $4\times4$ |
| rank | $2$ if $QP\neq0$, else $0$ | $4$ if $QP\neq0$, else $0$ |
| trace | $2\operatorname{Re}(QP)$ | $4\operatorname{Re}Q\operatorname{Re}P$ |
| determinant | $N(QP)$ | $N(Q)^{2}N(P)^{2}$ |
| Frobenius norm$^{2}$ | $2N(QP)$ | $4N(Q)N(P)$ |
| conformal? | yes | yes |

**The reading.** Both operators are conformal, both are invertible exactly when $QP\neq0$, and both have a positive determinant. The rank ladder of the general theory — the pairs of ranks of the two factors giving a stratum — is here a two-point set, because a conformal matrix of the plane has rank two or zero and nothing else. So the second rank measures nothing that the first does not, and the split-quaternion stratification has no analogue.

**The one difference that matters.** The trace. On the carrier it is $2\operatorname{Re}(QP)$; on the matrices it is $4\operatorname{Re}Q\operatorname{Re}P$. The first depends on the product, the second on the two factors separately. So the only numerical invariant that sees the pair and not merely the product is the trace of the display, and even that one sees only the two real parts.

**The coefficient rank.** It is one, for every non-zero pair, and it is the rank of the array of the pair. Its constancy is the reason there is no length theory: see the section on the length.

## The Pair as a Semigroup

**Composition.** $L_{Q}R_{P}L_{Q'}R_{P'}=L_{QQ'}R_{P'P}$ because the algebra is commutative. So the composition is the multiplication of the products, and the map $(Q,P)\mapsto L_{Q}R_{P}$ is a homomorphism of the monoid $\mathbb{C}\times\mathbb{C}$ onto the monoid $(\mathbb{C},\cdot)$ whose kernel is the rescaling.

**The units.** The invertible members are those with $QP\neq0$, of group

$$
\mathbb{C}^{\times}\cong\mathbb{R}_{>0}\times\mathrm{U}(1),
$$

of dimension two, and the isomorphism is the polar decomposition of the model article. The group of the two-sided operators is therefore the multiplicative group of the field, and not the seven-dimensional product of two copies that the quaternion category produced.

**The automorphisms.** The automorphism group of the algebra is $\{\mathrm{id},\overline{\phantom{Q}}\}$, of order two, and it is the Galois group of $\mathbb{C}$ over $\mathbb{R}$. The conjugation is not an inner automorphism: the algebra is commutative, so every map $Q\mapsto UQU^{-1}$ is the identity, and the Galois twist is outer. In the matrix model it is realised not by a product but by a **transpose**,

$$
\overline{Q}\longleftrightarrow\mathsf{M}_2(Q)^{\mathsf T},
$$

which is an operator of the ambient that is not of the form $X\mapsto AXB$. This is the one operator the model contains that the two-sided family cannot produce, and it is the external twist of the category.

**Proof that the transpose is not a product.** Suppose $AXB=X^{\mathsf T}$ for all $X$. Taking $X=I_2$ gives $AB=I_2$. Taking $X=E_{11}$ and $X=E_{22}$ gives $AE_{11}A^{-1}=E_{11}$ and $AE_{22}A^{-1}=E_{22}$, so $A$ is diagonal; taking $X=E_{12}$ then gives $(a/d)E_{12}=E_{21}$, which is impossible.

**The reading.** In the quaternion category every automorphism was inner, and the operator layer was closed: the two-sided products produced the conjugations. Here half of the automorphism group is outer, and the operator that produces it is the transpose, which lies outside the family. So the operator layer of $\mathbb{C}$ is the family plus one involution, and the involution is exactly the part of the structure that the two-sided formula cannot reach.

**The complement of the family.** The ambient splits by the involution $M\mapsto JMJ$:

$$
M_2(\mathbb{R})=\underbrace{\{M:JMJ=-M\}}_{\text{the family, dim }2}\oplus\underbrace{\{M:JMJ=M\}}_{\text{anti-complex-linear, dim }2},
$$

the first summand being the conformal matrices and the second the matrices with zero diagonal, spanned by $E_{12}$ and $E_{21}$. The two-sided products fill the first summand and nothing else; the second is inhabited by the reflections, of determinant $-1$, and by the maps that exchange the two axes. So the complement of the family is the space of the maps that reverse the complex structure, and it is unreachable by multiplication.

## The Cone and the Coefficient Matrix

**The image of the parametrisation.** The map

$$
\beta:\mathbb{C}\times\mathbb{C}\to\operatorname{End}_{\mathbb{R}}(\mathbb{C}),\qquad \beta(Q,P)=L_{QP},
$$

has image exactly the family $L(\mathbb{C})$, a linear subspace of dimension two and not a cone. In the general theory the image is the cone of rank-one coefficient arrays, of dimension $2\dim-1$; here it is a subspace, and the reason is the factorisation of $\beta$ through the product.

**The fibres.** The fibre over $L_c$ is

$$
\beta^{-1}(L_c)=\{(Q,P):QP=c\},
$$

of real dimension two for $c\neq0$: a free pair of parameters minus one rescaling. Over $c=0$ the fibre is the pair of axes $\{0\}\times\mathbb{C}\cup\mathbb{C}\times\{0\}$, again of dimension two but with a singularity at the origin. So the parametrisation is a map from four dimensions to two with two-dimensional fibres, everywhere.

**The membership test.** An operator of the ambient is a two-sided product exactly when it is conformal, and the test is the pair of linear equations

$$
s=-n,\qquad p=t,\qquad\text{for }M=\begin{pmatrix}p&n\\ s&t\end{pmatrix},
$$

equivalently $MJ=JM$. In the non-commutative categories the corresponding test was determinantal — a rank-one condition on a coefficient array — and it was nonlinear. Here the test is linear, the image is a subspace, and the "variety" of products is a linear space. This is the sharpest single contrast of the article.

**The basis and the coordinate.** The family has the basis

$$
T_1=I_2,\qquad T_i=J,
$$

and the coefficient array of a member is its pair of coordinates in that basis, that is the single complex number

$$
c(T_Q)=Q .
$$

So the "coefficient matrix" of the general theory, an array of size $n\times n$, is here a scalar: the operator is one complex number, and the array of the pair is a $2\times2$ rank-one array of the two coordinates. This is the smallest possible instance of the coefficient picture, and it is degenerate in the strongest sense.

## The Length

**The statement.** For a member of the span,

$$
\ell(L_{Q}R_{P})\in\{0,1\},
$$

with $\ell=0$ only for the zero operator; the value $2$ does not occur, and no member needs a sum. The span and the family coincide:

$$
\operatorname{span}\{L_{Q}R_{P}\}=L(\mathbb{C})\cup\{0\}=\{L_c:c\in\mathbb{C}\}.
$$

**Proof.** The span of a linear subspace that contains the zero operator is the subspace itself, and $L(\mathbb{C})$ is a linear subspace of the ambient containing $0$.

**The degenerate case of the length theorem.** The general theorem says that every operator of the ambient is a sum of at most $n$ products, where $n$ is the dimension of the carrier, and that the length is the rank of the coefficient array. Here $n=2$, so the theorem would allow $2$; but the coefficient array has size $2\times2$ and its rank can only be $0$ or $1$, because the array of a product is an outer product and the span is closed. The bound $2$ is not attained, and the theorem is not so much true as vacuous: the length is defined only inside a span that is already closed.

**Why the span is closed.** The reason is structural, and it is worth stating in full because it explains every other degeneration of the category. The two-sided products are the compositions

$$
L_Q\circ R_P=L_{QP},
$$

so the multiplication map $L(\mathbb{C})\times R(\mathbb{C})\to\operatorname{End}_{\mathbb{R}}(\mathbb{C})$ factors through the product of the algebra. Its image is therefore the product of the family with itself, which is the family, of dimension two. In the quaternion category the corresponding map is injective on the tensor product $L(\mathbb{H})\otimes R(\mathbb{H})\to\operatorname{End}_{\mathbb{R}}(\mathbb{H})$, of dimension $4\cdot4=16$, and it fills the whole ambient. The difference is exactly the double centraliser theorem: the map $A\otimes A_{\mathrm{opp}}\to\operatorname{End}_{\mathbb{R}}(A)$, $(a,b)\mapsto L_aR_b$, is an isomorphism if and only if $A$ is **central simple**. The quaternion and split-quaternion algebras are central simple over $\mathbb{R}$; the field $\mathbb{C}$ is simple but not central, since its centre is $\mathbb{C}$ itself, and the map collapses to multiplication.

**What lies outside the span.** Every operator that is not conformal. The transpose is one, and the reflections are others. So the length theory of this category is a theory of a two-dimensional subspace, and the two remaining dimensions of the ambient are not sums of products at any length: they are simply not in the span.

## The Two Ranks

**The two numbers.** The **operator rank** is the rank of the operator on the carrier; the **coefficient rank** is the rank of its coefficient array. Here

$$
\operatorname{rank}L_{Q}R_{P}=2\ (QP\neq0),\qquad \operatorname{rank}c(L_{Q}R_{P})=1,
$$

so the two differ at every nonzero member.

**The table.**

| operator | operator rank | coefficient rank | comment |
|---|---|---|---|
| $0$ | $0$ | $0$ | the vertex of the family |
| $I_2=L_1$ | $2$ | $1$ | the identity, of length one |
| $J=L_i$ | $2$ | $1$ | the quarter turn, of length one |
| $L_Q$, $Q\neq0$ | $2$ | $1$ | every nonzero member |
| the transpose | $4$ | — | not in the span, no length |
| a reflection | $2$ | — | not in the span, no length |

**The reading.** The rank is two for every nonzero member and one for every coefficient array, and the reason is structural: $\mathbb{C}$ is a field, so every nonzero element acts invertibly, so the left action is by invertible matrices and the operator rank cannot drop. In the split-quaternion category the two ranks moved independently because the algebra had zero divisors and a matrix could be singular without being zero; here nothing can be singular without being zero.

**The rank of the transpose.** The transpose is a rank-four operator on the four-dimensional space of matrices, so it is as far from a single product as an operator can be, and it has no coefficient array, because it is not in the span. So the table has an entry that the columns of the general theory cannot express, and that entry is the clearest evidence that the operator layer of this category is not the general one in small dimensions but its degenerate limit.

## What the Pair Buys and Does Not

**What it buys.** Nothing beyond the regular representation. The two-sided operator is the multiplication by the product; the one-sided operator is the multiplication by the element; the Kronecker display is the tensor square of the multiplication; and the automorphism group of the algebra is reached only by the transpose, which is outside the family. So the operator layer adds no structure to the model article: it restates the multiplicativity of the Cayley map in three notations.

**What it does not buy: the second product.** The complexoid block has two products, the plain one and the plain-plus-conjugation one, and the second lives in the *conjugation*, not in the multiplication. The operator layer of this article is the layer of the first product only. The map $X\mapsto Q\bar X$ is not a multiplication: since $\bar X=EXE$ with $E=\operatorname{diag}(1,-1)$, it is the two-sided formula with left factor $\mathsf{M}_2(Q)E$ and right factor $E$, and that left factor is not conformal, of determinant $-N(Q)$. So the second product is the same two-sided formula read with one factor outside the family, and it is where the reflections live.

**What it does not buy: the Peirce frame, the two-component carrier, the cone.** The three absent structures of the model article are absent here in the same way and for the same reason: no system of matrix units, no zero divisor, no central simplicity. The Peirce frame would need an idempotent, the two-component carrier would need a minimal ideal, and the cone would need the tensor product $L\otimes R$ to be full. Each is a consequence of a property $\mathbb{C}$ does not have as an $\mathbb{R}$-algebra.

**The residue.** What remains, and it is not nothing: the adjoint is the conjugation, so the model is a $*$-representation; the inner automorphisms are a circle acting on the matrices with the double cover; and the ambient splits into the conformal part, which is the family, and the anti-conformal part, which is the reflections. These three are the operators of the category, and the model article states them in the language of matrices.

## Summary

1. The carrier is $\mathbb{C}$ of dimension two and the ambient is $M_2(\mathbb{R})$ of dimension four: four entries for two parameters.
2. The one-sided families coincide, $L(\mathbb{C})=R(\mathbb{C})$, the sum is the family itself, and the two-sided operator depends on the pair only through the product, $L_{Q}R_{P}=L_{QP}$.
3. The operator is a bijection for every nonzero parameter: the kernel is trivial and the rank is two, with no rank drop anywhere.
4. The plain adjoint is the operator itself, by commutativity; the Frobenius adjoint is the operator of the conjugate; so the model is a faithful $*$-representation of the involutive algebra.
5. The parametrisation has a two-dimensional redundancy and a two-dimensional fibre, so four parameters fall to two, and the image is a linear subspace of the ambient.
6. The Kronecker display $K_{Q,P}=\mathsf{M}_2(P)^{\mathsf T}\otimes\mathsf{M}_2(Q)$ is conformal of $M_4(\mathbb{R})$, of rank four, trace $4\operatorname{Re}Q\operatorname{Re}P$ and determinant $N(Q)^{2}N(P)^{2}$.
7. The inner automorphisms are trivial on the carrier and act as a rotation by $2\theta$ on the traceless symmetric plane of the ambient: the smallest double cover $\mathrm{SO}(2)\to SO(3)$.
8. The membership test is linear, $MJ=JM$, against the determinantal test of the non-commutative categories; the family is a subspace and not a cone.
9. The length is in $\{0,1\}$ and is defined only inside the span, which is the family itself; the span is closed because the algebra is commutative, which is to say because it is not central simple.
10. The operator rank is two and the coefficient rank is one at every nonzero member, and the operators outside the span have no length at all.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $L_Q,R_Q$ | left and right multiplication, equal by commutativity | *$M_2(\mathbb{R})$ Cayley Representation* |
| $L_{Q}R_{P}$ | $X\mapsto QXP$, equal to $L_{QP}$ | this article |
| $K_{Q,P}$ | the Kronecker display $\mathsf{M}_2(P)^{\mathsf T}\otimes\mathsf{M}_2(Q)$ | this article |
| $c$ | the coefficient array, the pair $(Q,P)$ read as a rank-one array | this article |
| $\ell$ | the length, in $\{0,1\}$ inside the span | this article |
| $J$ | the complex structure, the generator of the family | *$M_2(\mathbb{R})$ Cayley Representation* |
| $E=\operatorname{diag}(1,-1)$ | the matrix of conjugation; the second product is $Q\bar X$ of matrix $\mathsf{M}_2(Q)E$ | this article |
| $\mathrm{Ad}_{R_\theta}$ | the inner automorphism $X\mapsto R_\theta XR_\theta^{-1}$ | this article |
| $JMJ$ | the involution splitting the ambient into the family and the anti-complex-linear part | this article |
| $E_{12},E_{21}$ | the matrix units spanning the complement of the family | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the map $A\otimes A_{\mathrm{opp}}\to\operatorname{End}(A)$ and the double centraliser theorem, whose failure for a non-central algebra is the collapse of this category.
- Frank B. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 1992), for the regular module over a division ring and the endomorphism ring of a simple module.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the vectorisation identity, the Kronecker product, its rank, trace and determinant.
- Joseph Landsberg, *Tensors: Geometry and Applications* (American Mathematical Society, 2012), for the tensor rank of the swap and the degeneracy of a tensor product over a non-central algebra.
