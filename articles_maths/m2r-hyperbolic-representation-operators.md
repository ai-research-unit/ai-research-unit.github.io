# __$M_2(\mathbb{R})$ Hyperbolic Representation : Operators__

## Introduction

**The operator layer of a split algebra.** The carrier is $\mathbb{C}_{\mathrm{spl}}$, of real dimension two, and the ambient is

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{C}_{\mathrm{spl}})\cong M_2(\mathbb{R}),
$$

of dimension four. The one-sided family is the image of the model; the two-sided family is the set of maps $X\mapsto QXP$; and the two are related by the failure of the algebra to be central simple.

**The four objects, and what becomes of them here.**

| object | general case | here |
|---|---|---|
| the two one-sided families | two copies, meeting in the scalars | one copy, they coincide |
| the two-sided family | the whole ambient | the algebra again, of dimension two |
| the sandwich | the vector action, a nontrivial group | a scalar on the carrier, a double boost on the ambient |
| the length | a rank in $\{0,\dots,n\}$ | in $\{0,1\}$, and only inside the algebra |

Three of the four collapse as in the complex category, and the reason is the same: the algebra is commutative, so the map $A\otimes A_{\mathrm{opp}}\to\operatorname{End}_{\mathbb{R}}(A)$ factors through the multiplication. The fourth does not collapse but **inverts**: the sandwich, which was the interesting operator of the non-commutative categories, is here the least informative one, and the one-sided operator carries everything. This article is about that inversion, and about the one place where the sandwich recovers information.

**The place where it recovers information.** The sandwich is scalar on the carrier and is not scalar on the ambient. Its ambient form has eigenvalues $N$, $\lambda_+^{2}$, $\lambda_-^{2}$, $N$: it kills the boost on the two mixed directions and **doubles** it on the two pure ones. So the two-sided operator of this category is a map that acts as a scalar on the algebra and as a double boost on the endomorphisms, and the gap between the two behaviours is the subject of the section on the Kronecker display.

**The absence of spin, precisely located.** The biquaternion category has a half angle, a double cover and a spinor action. This category has a full angle and no cover, and the reason is not the commutativity alone but the fact that the eigenvalues of the one-sided operator are the *idempotent coordinates*, which are linear in $Q$. A half angle would need a square root: the operator of a square root would be a square root of the operator, and the spectrum of $M_Q$ is $\{\lambda_+,\lambda_-\}$, so a square root exists if and only if both coordinates are non-negative. So the half angle exists, but only on a cone, and it is a real square root and not a lift of a rotation. This is stated in the section on the pair.

**Boundaries.** The model, the frame, the trace, the determinant, the projectors, the adjugate, the norms and the subspaces are *$M_2(\mathbb{R})$ Hyperbolic Representation*. The polar decomposition of the algebra is *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*; the one-sided operators in the abstract setting are *One-Sided Operators on a Clifford Algebra* and *Two-Sided Operators on the Biquaternion Algebra*, and the commutative complex companion of this article is *Operators on the Reduced Biquaternions*.

**Conventions.** The carrier has the basis $(1,j)$; a column of two real numbers is read as $x+jx'$. The operator $M_Q$ is multiplication by $Q$, with matrix $\mathsf{M}_2(Q)=qI_2+q'J$, $J=\begin{pmatrix}0&1\\1&0\end{pmatrix}$; $M_Q=L_Q=R_Q$. The two-sided operator is $L_{Q}R_{P}(X)=QXP$ on the carrier and $K_{Q,P}$ on the ambient. The split form is $g=\operatorname{diag}(1,-1)$; the idempotents are $\Pi_\pm$; the coordinates are $\lambda_\pm=q\pm q'$.

## The One-Sided Operators

**The family.** The left multiplications are the hyperbolic Cayley matrices, and the right multiplications are the same set:

$$
L(\mathbb{C}_{\mathrm{spl}})=R(\mathbb{C}_{\mathrm{spl}})=\{\mathsf{M}_2(Q)\},\qquad \dim=2,\qquad L+R=L.
$$

**The representation.** $M:Q\mapsto M_Q$ is $\mathbb{R}$-linear, multiplicative and faithful, and its image is the algebra of matrices symmetric with equal diagonal. Faithfulness is evaluation at $1$: $M_Q(1)=Q$. So the one-sided layer is the algebra itself, read on its regular module, and there is nothing else in it.

**Kernel, image and rank.** For $Q\in\mathbb{C}_{\mathrm{spl}}$,

$$
\ker M_Q=\operatorname{Ann}(Q),\qquad \operatorname{im}M_Q=Q\mathbb{C}_{\mathrm{spl}},
$$

and the three cases are exhaustive:

| $Q$ | $\langle Q\rangle_{*}$ | rank $M_Q$ | kernel | image |
|---|---|---|---|---|
| $0$ | $0$ | $0$ | $\mathbb{C}_{\mathrm{spl}}$ | $0$ |
| $\lambda_+\Pi_+$, $\lambda_+\neq0$ | $0$ | $1$ | $S_-$ | $S_+$ |
| $\lambda_-\Pi_-$, $\lambda_-\neq0$ | $0$ | $1$ | $S_+$ | $S_-$ |
| unit | $\neq0$ | $2$ | $0$ | $\mathbb{C}_{\mathrm{spl}}$ |

**The reading.** The rank takes the three values $2,1,0$ and drops to one exactly on the two null lines. This is the first category of the block in which the one-sided operator has an intermediate rank, and it is the operator-level statement that the algebra has zero divisors.

**The adjoint, twice.** For the plain form, $\langle M_QX,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(QXY)=\operatorname{tr}(X\cdot QY)=\langle X,M_QY\rangle_{\operatorname{tr}}$, so the operator is self-adjoint: commutativity again. For the Frobenius form, the adjoint is $M_Q$ as well, because every matrix of the image is symmetric, $M_Q^{\mathsf T}=M_Q$. So both adjoints are the operator itself, and

$$
M_Q^{*}=M_Q
$$

for either form. In the complex case the Frobenius adjoint was the operator of the conjugate; here the conjugate is not the transpose, and the Frobenius adjoint does not see the conjugation at all. The involution of the algebra is therefore invisible to both adjoints, and it is carried instead by the congruence $gMg$.

**The conformal identity.** With $g=\operatorname{diag}(1,-1)$,

$$
M_Q^{\mathsf T}g\,M_Q=\langle Q\rangle_{*}\,g,
$$

so every nonzero member of the family is a conformal map of the Minkowski plane, of factor the norm. Normalising, $M_Q/\sqrt{\lvert\langle Q\rangle_{*}\rvert}$ lies in $O(1,1)$, and on the norm-one slice the family is exactly $O(1,1)$.

**The polar word.** Writing

$$
Q=r\,\epsilon\,\exp(\theta_{\mathrm{rpd}} j),\qquad r=\sqrt{\lvert\langle Q\rangle_{*}\rvert}>0,\quad \epsilon\in\{\pm1,\pm j\},\quad \theta_{\mathrm{rpd}}\in\mathbb{R},
$$

the operator inherits the word factor by factor:

$$
M_Q=r\,M_\epsilon\,\exp(\theta_{\mathrm{rpd}} M_j),\qquad M_j=J,\qquad \exp(\theta_{\mathrm{rpd}} J)=\cosh\theta_{\mathrm{rpd}}\,I_2+\sinh\theta_{\mathrm{rpd}}\,J .
$$

In the spectral frame, where $J=\operatorname{diag}(1,-1)$ and $M_\epsilon=\operatorname{diag}(\epsilon_+,\epsilon_-)$,

$$
M_Q=\operatorname{diag}\bigl(r\epsilon_+e^{\theta_{\mathrm{rpd}}},\,r\epsilon_-e^{-\theta_{\mathrm{rpd}}}\bigr)=\operatorname{diag}(\lambda_+,\lambda_-).
$$

**The three factors and their roles.** The scale acts as $r$ and not as $r^{2}$; the sign is a discrete diagonal sign; the boost acts as $e^{\pm\theta_{\mathrm{rpd}}}$ on the two Peirce lines, with opposite exponents. All three are visible to the one-sided operator, and this is the whole of the polar content of the category:

- the modulus is the geometric mean of the absolute values of the two eigenvalues;
- the sign is the pair $(\operatorname{sgn}\lambda_+,\operatorname{sgn}\lambda_-)$, which is the component label of the unit group;
- the boost is the half-difference of their logarithms, $\theta_{\mathrm{rpd}}=\tfrac12\ln\lvert\lambda_+/\lambda_-\rvert$.

**The exponent is the full angle.** The eigenvalues of the boost are $e^{\pm\theta_{\mathrm{rpd}}}$, not $e^{\pm\theta_{\mathrm{rpd}}/2}$, and the polar word writes $\theta_{\mathrm{rpd}}$ and not $\theta_{\mathrm{rpd}}/2$. The reason is that the two exponents are the two eigenvalue logarithms, and the eigenvalues are the idempotent coordinates $\lambda_\pm = r e^{\pm\theta_{\mathrm{rpd}}}$, which are *linear* in the polar data. A half angle would require $\lambda_\pm = r e^{\pm\theta_{\mathrm{rpd}}/2}$, that is $Q = r\exp(\tfrac{\theta_{\mathrm{rpd}}}{2}j)$, which is a different element. So the category has no half angle in its spectrum, and the geometric half angle that appeared in the model article was the axis of a Euclidean reflection, not a weight.

**The explicit matrices.**

$$
Q=r\epsilon\,e^{\theta_{\mathrm{rpd}} j}:\quad M_Q=r\epsilon\begin{pmatrix}\cosh\theta_{\mathrm{rpd}}&\sinh\theta_{\mathrm{rpd}}\\ \sinh\theta_{\mathrm{rpd}}&\cosh\theta_{\mathrm{rpd}}\end{pmatrix},
\qquad
Q=r\epsilon\,j\,e^{\theta_{\mathrm{rpd}} j}:\quad M_Q=r\epsilon\begin{pmatrix}\sinh\theta_{\mathrm{rpd}}&\cosh\theta_{\mathrm{rpd}}\\ \cosh\theta_{\mathrm{rpd}}&\sinh\theta_{\mathrm{rpd}}\end{pmatrix}.
$$

The first is the boost, the second the boost composed with the reflection $J$; the two families are the two components of $O(1,1)$ with positive and negative determinant, and the sign $\epsilon=\pm1$ multiplies both.

**The one-parameter subgroup.** $t\mapsto M_{\exp(tj)}$ is a homomorphism $\mathbb{R}\to SO^{+}(1,1)$, injective, and its image is the identity component of the units. So the exponential of the algebra is the exponential of the operator, and the polar word is a statement about a one-parameter subgroup of the ambient's conformal group.

## The Two-Sided Operator

**Definition and collapse.** For a pair $(Q,P)$,

$$
L_{Q}R_{P}(X)=QXP,\qquad L_{Q}R_{P}=M_{QP}=L_QR_P .
$$

**The reading.** The two slots are not independent: the operator depends on the pair only through the product, and since the algebra is commutative the map $(Q,P)\mapsto QP$ is the multiplication of the algebra. So the two-sided family is the one-sided family,

$$
\{L_{Q}R_{P}\}=\{M_{QP}\}=M(\mathbb{C}_{\mathrm{spl}}),
$$

of dimension two, and the pair is a redundant parametrisation of the algebra.

**The redundancy.** For $\lambda\neq0$, $L_{\lambda Q}R_{P/\lambda}=L_{Q}R_{P}$; so the four real parameters of the pair fall to the two of the product, and the map from the pair to the operator has two-dimensional fibres.

**The sandwich.** The sandwich is the case $P=\bar Q$:

$$
\mathrm{Sd}_Q(X)=QX\bar Q=\langle Q\rangle_{*}\,X .
$$

**Proof.** $Q\bar Q=\langle Q\rangle_{*}$ is central, so it commutes past $X$.

**The reading, and the inversion.** $\mathrm{Sd}_Q$ is a **scalar operator**, equal to the norm. It is multiplicative, $\mathrm{Sd}_Q\circ\mathrm{Sd}_P=\mathrm{Sd}_{QP}$, and it is not faithful: it depends on $Q$ only through the norm, so its fibres are the level sets of $\langle\cdot\rangle_{*}$, which are the hyperbola branches. On the units the image is the group of nonzero scalar operators, of dimension one, and the kernel is the hyperbola $\{\langle Q\rangle_{*}=1\}$.

**Why it collapses.** $\mathrm{Sd}_Q=\langle Q\rangle_{*}\operatorname{Ad}_Q$, where $\operatorname{Ad}_Q$ is the inner automorphism of the algebra; and the inner automorphism group of a commutative algebra is trivial. So the sandwich is the norm times the identity, and the whole of its non-triviality is the scalar. In the biquaternion category the same formula produced a Lorentz transformation, because the algebra was not commutative and the inner automorphisms were a three-dimensional group. Here there is nothing to conjugate.

**What the sandwich forgets.** The boost. Two elements on the same hyperbola have the same sandwich; in particular $Q$ and $Q^{-1}$ have the same norm $1$ and the same sandwich, the identity, while their one-sided operators are inverse boosts. So the sandwich is strictly less informative than the one-sided operator, which is the inversion announced in the introduction: in the non-commutative categories the sandwich carried the vector action and the one-sided operator the spinor one; here the one-sided operator carries everything and the sandwich carries one number.

**The ambient form is not scalar.** The formula $X\mapsto QX\bar Q$ defines an operator on the ambient as well, and there it is **not** a scalar: its matrix is the Kronecker display of the next section, of eigenvalues $\lambda_+^{2}$, $N$, $N$, $\lambda_-^{2}$. So the collapse to a scalar is a statement about the carrier, not about the formula. The carrier is the algebra, the algebra is the image of the model, and the sandwich never leaves the image; on the endomorphisms it does leave, and there it acts by a double boost. This is the one place in the category where the two-sided operator says something the one-sided operator does not.

## The Kronecker Display

**The identity.** Vectorising by columns, $\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}(X)$, so the ambient form of the two-sided operator is

$$
K_{Q,P}=\mathsf{M}_2(P)^{\mathsf T}\otimes\mathsf{M}_2(Q)=\mathsf{M}_2(P)\otimes\mathsf{M}_2(Q),
$$

the second equality because every matrix of the image is symmetric. The display is again a symmetric matrix, of size four, and it is the tensor product of the two factors.

**The spectrum of the display.** In the spectral frame both factors are diagonal, so the display is diagonal with entries the four products:

$$
\operatorname{spec}K_{Q,P}=\{\lambda_+(Q)\lambda_+(P),\ \lambda_+(Q)\lambda_-(P),\ \lambda_-(Q)\lambda_+(P),\ \lambda_-(Q)\lambda_-(P)\}.
$$

For the sandwich $P=\bar Q$, where $\lambda_\pm(\bar Q)=\lambda_\mp(Q)$:

$$
\operatorname{spec}K_{Q,\bar Q}=\{\lambda_+^{2},\ N,\ N,\ \lambda_-^{2}\}.
$$

**The reading, in the polar word.** With $\lambda_\pm=r\epsilon_\pm e^{\pm\theta_{\mathrm{rpd}}}$ and $N=r^{2}\epsilon_+\epsilon_-$:

- on the two **pure** directions the eigenvalue is $\lambda_\pm^{2}=r^{2}e^{\pm2\theta_{\mathrm{rpd}}}$: the scale is squared and the boost is **doubled**, the rapidity $2\theta_{\mathrm{rpd}}$ in place of $\theta_{\mathrm{rpd}}$;
- on the two **mixed** directions the eigenvalue is $N=r^{2}\epsilon_+\epsilon_-$: the scale is squared and the boost **cancels**, exactly as it cancels on the carrier.

So the ambient sandwich acts as a double boost on the diagonal corners of the tensor square and as a pure dilation on the off-diagonal corners. It is the exact analogue of the $2\theta$ of the complex category, in the hyperbolic parameter, and it is the only doubling of an angle in the whole block.

**The invariants of the display.**

$$
\operatorname{tr}K_{Q,P}=4qp,\qquad
\det K_{Q,P}=\langle P\rangle_{*}^{2}\langle Q\rangle_{*}^{2},\qquad
\operatorname{rank}K_{Q,P}=\operatorname{rank}M_Q\cdot\operatorname{rank}M_P .
$$

**Proof.** The trace of a Kronecker product is the product of the traces, and each trace is $2q$; the determinant is $(\det B)^{2}(\det A)^{2}$ for a $4\times4$ product of $2\times2$ factors; the rank is the product of the ranks.

**The reading.** The trace of the display is $4qp$, that is four times the product of the two scalar parts, so it is the *product* of the two factors' traces over four: the display sees the pair and not only the product. The determinant is a fourth power of norms, and the rank is the product of the ranks, which is the second rank of the series.

**The sign lost.** $K_{Q,P}=K_{-Q,-P}$, so the display is faithful on the pair only up to the simultaneous sign. It is not faithful on $Q$ alone: $K_{Q,\bar Q}$ determines $\lambda_\pm^{2}$ and $N$, hence $\lambda_\pm$ up to a common sign, hence $Q$ up to sign. So the ambient sandwich is faithful up to $\pm1$, and the carrier sandwich is faithful up to the hyperbola. The ladder of faithfulness is therefore

$$
\mathrm{J}:\ \text{norm}\ \succ\ K:\ \pm Q\ \succ\ M:\ Q,
$$

with the one-sided operator the faithful end, which is the inverted order of the non-commutative categories.

## The Rank and the Invariants

**The table.** One formula, two carriers.

| quantity | on the carrier, $T=M_{QP}$ | on the ambient, $K=M_P\otimes M_Q$ |
|---|---|---|
| size | $2\times2$ | $4\times4$ |
| rank | $2$ on units, $1$ on the null lines, $0$ at the origin | $4$, $2$, $1$ or $0$, the product of the two carrier ranks |
| trace | $2\operatorname{Re}(QP)$ | $4qp$ |
| determinant | $\langle QP\rangle_{*}$ | $\langle Q\rangle_{*}^{2}\langle P\rangle_{*}^{2}$ |
| eigenvalues | $\lambda_\pm(QP)$ | the four products $\lambda_i(Q)\lambda_j(P)$ |
| conformal for $g\otimes g$? | yes | yes |

**The reading.** Both operators are conformal, for $g$ on the carrier and for $g\otimes g$ on the ambient; both have determinants that are squares; and both have a rank ladder. The ladder of the display is $\{0,1,2,4\}$ and the value $3$ is missing — a rank-three product of two rank-$\le2$ factors is impossible.

**The zero-divisor case in full.** Let $Q$ be null and nonzero, $Q=\lambda_+\Pi_+$, and let $P$ be a unit. Then

$$
M_Q=\lambda_+\rho_+,\qquad \operatorname{rank}=1,\qquad M_{QP}=\lambda_+\lambda_+(P)\,\rho_+,
$$

so the carrier operator stays of rank one and is the same projector scaled; and

$$
K_{Q,P}=\lambda_+\lambda_+(P)\,\Pi_{++}+\lambda_+\lambda_-(P)\,\Pi_{-+},\qquad \Pi_{ab}=(u_a\otimes u_+)(u_a\otimes u_+)^{\mathsf T},
$$

a sum of two orthogonal rank-one projectors on the two ambient directions $u_+\otimes u_+$ and $u_-\otimes u_+$, of rank two. So a null factor halves the ambient rank and does not change the *type* of the carrier operator, which remains a single scaled projector. If both factors are null the display has rank one whichever Peirce lines they lie on, because the rank is the product of the two carrier ranks; whether the two lines agree is invisible to the rank, and it only decides which single ambient direction survives.

**The explicit shape.** In the spectral frame the display is diagonal, so every rank statement is a statement about the number of non-zero products $\lambda_i(Q)\lambda_j(P)$. That is the whole of the stratification of this category: the strata are indexed by the pair of subsets of $\{+,-\}$ on which the two factors vanish, and there are four such strata, against the continuum of a matrix algebra.

## The Pair as a Semigroup

**Composition.** $L_{Q}R_{P}L_{Q'}R_{P'}=L_{QQ'}R_{P'P}$: the composition is the multiplication of the four factors in any order. So the map $(Q,P)\mapsto L_{Q}R_{P}$ is a homomorphism of the monoid $\mathbb{C}_{\mathrm{spl}}\times\mathbb{C}_{\mathrm{spl}}$ onto the monoid $(\mathbb{C}_{\mathrm{spl}},\cdot)$, with kernel the rescaling.

**The units.** The invertible members are those with $QP$ a unit, and the group is

$$
{\mathbb{C}_{\mathrm{spl}}}^{\times}\cong(\mathbb{Z}/2\mathbb{Z})^{2}\times\mathbb{R}^{2},
$$

of dimension two and four components. The group of two-sided operators is therefore the unit group of the algebra, and not the seven-dimensional product of the two one-sided groups of the quaternion category.

**The automorphisms of the algebra.** The only automorphisms are the identity and the conjugation $j\mapsto-j$: as an $\mathbb{R}$-algebra, $\mathbb{C}_{\mathrm{spl}}\cong\mathbb{R}\times\mathbb{R}$ and an automorphism is a permutation of the two idempotents. The group is $\mathbb{Z}/2\mathbb{Z}$, and its non-trivial element swaps the two Peirce lines and the two null lines.

**The conjugation is outer in the algebra and inner in the ambient.** The conjugation is not inner in $\mathbb{C}_{\mathrm{spl}}$, since the algebra is commutative and its unit group is abelian. But on the model it *is* implemented by an ambient inner automorphism,

$$
\mathsf{M}_2(\bar Q)=g\,\mathsf{M}_2(Q)\,g^{-1},\qquad g=\operatorname{diag}(1,-1),\quad g^{2}=I_2,
$$

with $g$ a reflection of the plane, of determinant $-1$ and not in the image. So the Galois twist of the algebra is the conjugation by a matrix outside the algebra: the twist is outer where it lives and inner where it is represented. This is a sharper statement than the complex case, where the implementer was the transpose and not a conjugation at all.

**The reading.** The three groups — the automorphisms of the algebra, the inner automorphisms of the ambient, the conformal group of the form — are here three different objects of orders $2$, $4$ and infinite, and the model displays all three. In the quaternion category the first two coincided, which is why that category had a single operator layer.

**The absence of a cover.** Two facts have to be separated, because it is easy to conflate them. The inner automorphisms of the *ambient* do act on the family, but by moving it: $U\mathsf{M}_2(\mathbb{C}_{\mathrm{spl}})U^{-1}=\mathbb{R}[UJU^{-1}]$ is a conjugate copy of the algebra, and the stabiliser of the model is the unit group of the algebra, of dimension two and four components. The inner automorphisms of the *algebra*, which is the group that the operator layer is about, are trivial, because the algebra is commutative. So there is no circle and no line acting on the algebra, no double cover inside the model, and no spin representation. The identity component of the conformal group is the boost line, which is simply connected; the abstract double cover $\mathrm{Spin}(1,1)\to SO^{+}(1,1)$ exists, but it is not realised by matrices of the image, because that would need a half-angle action and the spectrum has none.

## The Cone and the Coefficient Matrix

**The parametrisation.**

$$
\beta:\mathbb{C}_{\mathrm{spl}}\times\mathbb{C}_{\mathrm{spl}}\to\operatorname{End}_{\mathbb{R}}(\mathbb{C}_{\mathrm{spl}}),\qquad \beta(Q,P)=L_{QP},
$$

whose image is the algebra $M_2(\mathbb{C}_{\mathrm{spl}})$, a linear subspace of dimension two and not a cone.

**The fibres.** $\beta^{-1}(L_c)=\{(Q,P):QP=c\}$, of real dimension two for $c\neq0$; over $c=0$ it is the union of the two axis pairs, again of dimension two but singular at the origin. So the map is four dimensions to two with two-dimensional fibres, everywhere.

**The membership test.** An ambient matrix $C=\begin{pmatrix}p&n\\ s&t\end{pmatrix}$ is a two-sided product exactly when

$$
n=s\quad\text{and}\quad p=t,
$$

that is, when it is symmetric with equal diagonal entries, equivalently $CJ=JC$. The test is **linear**.

**The reading, and the contrast.** In the split-quaternion category the test was determinantal — the vanishing of a $2\times2$ minor of a coefficient array — and the image was a genuine cone. Here the test is two linear equations and the image is a subspace. The difference is the same one as in the complex category, and its cause is the same: the algebra is commutative, so the two-sided products are closed under addition. The image being a subspace, the word *cone* has no content in this category, and the article records the degeneration rather than the object.

**The coefficient matrix.** The pair is described by the array of products of coordinates,

$$
c(Q,P)=\begin{pmatrix}qp&qp'\\ q'p&q'p'\end{pmatrix},
$$

of rank one for every non-zero pair. The operator is described by the coefficient array of the product in the basis $(T_1,T_j)=(I_2,J)$, which is the single entry $QP$: an array of size one. So the two arrays of the general theory, of sizes $2\times2$ and $n\times n$, are here an array of rank one describing the pair and a scalar describing the operator.

## The Length

**The statement.**

$$
\ell(L_{Q}R_{P})\in\{0,1\},\qquad \operatorname{span}\{L_{Q}R_{P}\}=M(\mathbb{C}_{\mathrm{spl}})\cup\{0\},
$$

the value $0$ only for the zero operator, and the span equal to the algebra because the algebra is a subspace closed under products.

**The degenerate case of the length theorem.** The general theorem allows at most $n=2$ products and identifies the length with the rank of the coefficient array. Here the coefficient array has rank one for a single product and the span is closed, so no sum is ever needed and the bound is not attained. The null elements do not form an exception: a zero divisor is still a single product $L_Q$, of rank one, and its length is one and not two. This is the precise sense in which the length theory of this category is vacuous, and it is worth stating because the tempting error is to read the rank drop as a failure of the length: it is not, since the length counts products and not ranks.

**Why the span is closed.** The products are the compositions $L_Q\circ R_P=L_{QP}$, so the multiplication map sends $L(\mathbb{C}_{\mathrm{spl}})\times R(\mathbb{C}_{\mathrm{spl}})$ into $L(\mathbb{C}_{\mathrm{spl}})$; the image is the algebra and it is a subspace. In the quaternion category the same map is an isomorphism $A\otimes A_{\mathrm{opp}}\to\operatorname{End}_{\mathbb{R}}(A)$ and fills a sixteen-dimensional ambient; the difference is central simplicity. $\mathbb{R}\times\mathbb{R}$ is commutative and therefore not central simple, and the map collapses to the multiplication of the algebra.

**What lies outside the span.** Two dimensions: the traceless diagonal line $\mathbb{R}g$ and the skew line $\mathfrak{so}(2)$. The matrices of $\mathbb{R}g$ are the ones that change the sign of the determinant, and the skew line is the rotation. Neither is a product at any length, and neither is a sum of products: they are simply not in the span. So the operator layer of the split category covers half of the ambient and not more, exactly as in the complex category, and the missing half is again the part of $M_2(\mathbb{R})$ that does not commute with $J$.

## The Two Ranks

**The two numbers.** The **operator rank** is the rank of $M_Q$ on the carrier; the **coefficient rank** is the rank of the coefficient array of the element. Here

$$
\operatorname{rank}M_Q\in\{0,1,2\},\qquad \operatorname{rank}c(M_Q)=1\quad(M_Q\neq0).
$$

The two ranks differ exactly on the units, where the first is two and the second one, and they coincide exactly on the null lines, where the first has dropped to one. That is the opposite of the complex category, where the operator rank never dropped and the two ranks differed at every non-zero element.

**The table.**

| operator | operator rank | coefficient rank | comment |
|---|---|---|---|
| $0$ | $0$ | $0$ | the vertex |
| unit | $2$ | $1$ | bijective |
| null, nonzero | $1$ | $1$ | a scaled projector |
| $K_{Q,P}$, both units | $4$ | $1$ | the display, second rank four |
| $K_{Q,P}$, one null | $2$ | $1$ | second rank two |
| $K_{Q,P}$, both null | $1$ | $1$ | second rank one |

**The reading.** The first rank measures invertibility, the second measures the tensor product, and the coefficient rank is one throughout. So the rank ladder of this category is a ladder of the *second* rank, the one the split-quaternion category tabulated as $\operatorname{rank}A\cdot\operatorname{rank}B$; here the ladder is $\{0,1,2,4\}$ and it is complete, because the two carrier ranks are independent.

**The singular operators are single products.** This is the structural point that separates this category from the matrix algebras. A rank-one operator of $M_2(\mathbb{R})$ is $X\mapsto u\,v^{\mathsf T}X$, a two-sided product with $A=uv^{\mathsf T}$ and $B=I$; but $A$ is generally not in the algebra, so the operator is generally not in the span and has no length. The rank-one operators that *are* in the span are exactly the scalings of $\rho_+$ and $\rho_-$, and those are the ones the null elements produce. So the singular part of the family is one-dimensional inside each null line, and the rest of the singular operators of the ambient are outside.

## What the Pair Buys and Does Not

**What it buys.** Three things.

- **The conformal structure.** $M_Q^{\mathsf T}gM_Q=\langle Q\rangle_{*}g$, so the family is the conformal group of the Minkowski plane intersected with the symmetric matrices. The pair adds nothing to this, but the display $K_{Q,P}$ extends it to $g\otimes g$ on the ambient, which is where the double boost lives.
- **The doubling.** The ambient sandwich doubles the rapidity on the two pure corners and kills it on the two mixed ones, and this is the only place in the block where a hyperbolic angle is doubled. It is the analogue of the $2\theta$ of the complex category, and it is the trace of the two-sided formula that the non-commutative categories make into a group action.
- **The faithfulness ladder.** $\Theta$ sees the norm, $K$ sees the pair up to the simultaneous sign, $M$ sees the element; so the model separates three levels of information that the quaternion models cannot separate, because there all three are the same group.

**What it does not buy: a group action.** In the biquaternion category the sandwich is the vector action and its image is $CO^{+}(1,3)$, a six-dimensional group acting on a four-dimensional space. Here the image on the units is the ray of the identity, of dimension one, and it acts trivially on the algebra. So the two-sided family carries no action of a group on the carrier; what it carries is a scalar, and the action of the unit group on the algebra is the multiplication, which is the one-sided layer.

**What it does not buy: the half angle and the cover.** The biquaternion has a half angle in the one-sided spectrum, hence a double cover and a spinor action. Here the spectrum is $\{\lambda_+,\lambda_-\}=\{r e^{\pm\theta_{\mathrm{rpd}}}\}$, the exponent is the full angle, and no cover appears. A square root of the operator exists exactly on the cone where both coordinates are non-negative, and it is a real square root and not a lift: so the half angle exists on a cone of the algebra and is not a representation-theoretic object.

**What it does not buy: nilpotents.** There is no nilpotent in the algebra, so there is no Jordan block, no maximal ideal of the form $(X^{2})$, and no unipotent one-parameter subgroup. The whole nilpotent apparatus of the reduced biquaternion category — the Jordan decomposition, the non-semisimple sector, the $\Sigma_{00}$ stratum — is empty here, and it is empty for the reason $x^{2}-1$ has distinct roots.

**The residue.** What remains of the operator layer, and it is not nothing: the conformal identity, the boost group, the rank ladder $\{0,1,2\}$, the four strata of the display, and the faithfulness ladder. These are the operators of the category, and they are all one-sided or tensor-square statements. The two-sided formula, which was the engine of the non-commutative categories, is here a restatement.

## Summary

1. The carrier is $\mathbb{C}_{\mathrm{spl}}$ of dimension two, the ambient is $M_2(\mathbb{R})$ of dimension four, and the one-sided family is the two-dimensional algebra of hyperbolic matrices.
2. The one-sided operator is faithful, self-adjoint for both the trace and the Frobenius forms, and conformal for the split form with factor the norm; its rank is $2$ on the units, $1$ on the null lines and $0$ at the origin.
3. The polar word $Q=r\epsilon\exp(\theta_{\mathrm{rpd}} j)$ reads $M_Q=rM_\epsilon\exp(\theta_{\mathrm{rpd}} J)$, with eigenvalues $r\epsilon_\pm e^{\pm\theta_{\mathrm{rpd}}}$; the angle is full, the sign is a discrete label, and no cover appears.
4. The two-sided operator depends on the pair only through the product, $L_{Q}R_{P}=M_{QP}$, so the two-sided family is the algebra and the parametrisation has two-dimensional fibres.
5. The sandwich is a scalar on the carrier, $\mathrm{Sd}_Q=\langle Q\rangle_{*}\operatorname{id}$, because the inner automorphism group of a commutative algebra is trivial; it is faithful only up to the norm, and it forgets the boost entirely.
6. On the ambient the same formula is not scalar: $K_{Q,\bar Q}$ has eigenvalues $\lambda_+^{2}$, $N$, $N$, $\lambda_-^{2}$, doubling the rapidity on the two pure corners and killing it on the two mixed ones.
7. The display is symmetric, of trace $4qp$, of determinant $\langle Q\rangle_{*}^{2}\langle P\rangle_{*}^{2}$ and of rank $\operatorname{rank}M_Q\operatorname{rank}M_P$, so its ladder is $\{0,1,2,4\}$.
8. The Galois twist of the algebra is outer in the algebra and inner in the ambient, implemented by the reflection $g=\operatorname{diag}(1,-1)$, which is not in the image.
9. The membership test is linear — symmetric with equal diagonal — so the image is a subspace and not a cone, and the length is in $\{0,1\}$ inside a span that is already closed, because $\mathbb{R}\times\mathbb{R}$ is not central simple.
10. The operator rank is $2,1,0$ and the coefficient rank is $1$ throughout, so the rank theory of the category is the second rank of the display, and the singular operators in the span are exactly the scalings of the two projectors.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $M_Q$ | the multiplication operator $X\mapsto QX$, equal to $L_Q$ and $R_Q$ | *$M_2(\mathbb{R})$ Hyperbolic Representation* |
| $L_{Q}R_{P}$ | $X\mapsto QXP$, equal to $M_{QP}$ | this article |
| $\mathrm{Sd}_Q$ | the sandwich $QX\bar Q=\langle Q\rangle_{*}X$ | this article |
| $K_{Q,P}$ | the Kronecker display $\mathsf{M}_2(P)\otimes\mathsf{M}_2(Q)$ | this article |
| $g$ | the split form $\operatorname{diag}(1,-1)$, implementing the conjugation by congruence | *$M_2(\mathbb{R})$ Hyperbolic Representation* |
| $\lambda_\pm=q\pm q'$ | the eigenvalues, the idempotent coordinates | *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number* |
| $r,\epsilon,\theta_{\mathrm{rpd}}$ | modulus, component sign, hyperbolic angle | *Modulus–Unit Polar Decomposition of Split-Complex Numbers* |
| $\ell$ | the length, in $\{0,1\}$ inside the span | this article |
| $c(Q,P)$ | the coefficient array of the pair, of rank one | this article |
| $\operatorname{Ann}(Q)$ | the annihilator, the kernel of $M_Q$ | *Ideals and Peirce Decomposition of the Split-Complex Algebra* |
| $SO^{+}(1,1)$ | the boost group, the identity component of the units | *Exponential Polar Decomposition of Split-Complex Numbers* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the map $A\otimes A_{\mathrm{opp}}\to\operatorname{End}(A)$, the double centraliser theorem, and the Peirce carriers as minimal ideals.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for central simplicity, the centre of a split algebra, and the failure of the double centraliser isomorphism.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the Kronecker product, its spectrum, its rank, trace and determinant, and the vectorisation identity.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $SO^{+}(1,1)$, the exponential of the boost generator and the topology of the components.
