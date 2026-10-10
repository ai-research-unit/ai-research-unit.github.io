# __The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra__

## Introduction

For a bilinear antisymmetrisation the structural theory is short: the diagonal vanishes, the operation is alternating, and the only question is whether the Jacobi identity holds. For the operation of the block none of the three statements survives in its bilinear form, and this article develops what replaces them. The diagonal of $\diamond$ is the **vector part of the square** of the row, $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$; it is a quadratic map of the space into the purely imaginary vectors, its vanishing is a genuine condition and not an identity, and the set on which it vanishes is a quadric cone of real dimension five. The Jacobi identity fails, with the tabulated cyclic sum $e_3$ at $(e_0,e_1,e_2)$, and the failure is not an associator defect: it is the obstruction of a sesquilinear antisymmetrisation, the one recorded in *Lie Algebras of Sesqualgebras*.

Three comparisons organise the article. The block is the **other** antisymmetrisation of the same product, the one that keeps the class, and its relation to the bare sesquilinear commutator of *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions* is an identity off the real part and a defect on it; the identity and the defect are computed in §*The Identity with the Sesquilinear Bracket and its Defect*. The block has two siblings among the failing brackets of the row table, $\mathrm{AQA}$ and $\mathrm{AQS}$, and the three failures have three different reasons; the comparison is in §*The Comparison with the Two Siblings*. And on the real part of the space the block collapses to a cross product, which is developed in §*The Reading on the Real Part*.

The setting, the notation and the definition of the block are those of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the product that is split is *Introduction to the General Plain Sesqualgebra of Biquaternions*; the general construction of the two parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, and its long development is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*; the row table, the three Jacobi failures and the identity $\overline{\tilde Q\tilde P^{*}}=(\tilde P\tilde Q^{*})^{\natural}$ are *The 12 Products of the Biquaternion Complex Space*; the form $H$ and the zero divisors are *Biquaternion Norm and Invertibility*; the sesquilinear commutator and the plain symmetrisation are *The Sesquilinear Commutator* and *The Sesquilinear Symmetrised Product*; and the remarkable subspaces are *Introduction to the Remarkable Subspaces*. The purity list of the pass is respected: no word of distance, limit or continuity occurs, the norm that is used is the algebraic form $H$ and the multiplicative element $\tilde Q\tilde Q^{*}$, and never a length.

## The Diagonal and its Formula

**Theorem (the diagonal is the vector part of the square).** For every biquaternion,

$$
\tilde Q\diamond\tilde Q=\mathrm{Vect}\bigl(\tilde Q\tilde Q^{*}\bigr),
$$

the vector part of the square of the general plain sesquilinear product.

*Proof.* Put $\tilde P=\tilde Q$ in the definition: $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$, and $\overline{\tilde Q\tilde Q^{*}}=\tilde Q\tilde Q^{*}$ because $\tilde Q\tilde Q^{*}$ is Hermitian. So the two terms of the half-difference are equal and the half-difference is the value itself. $\square$

**Corollary (the real form).** Write the element in real coordinates, $Q_0=a+ib$ and $\mathbf{Q}=\mathbf{u}+i\mathbf{v}$, with $a,b\in\mathbb{R}$ and $\mathbf{u},\mathbf{v}$ real vectors. Then

$$
\tilde Q\diamond\tilde Q=2i\bigl(a\,\mathbf{v}-b\,\mathbf{u}+\mathbf{u}\times\mathbf{v}\bigr),
$$

a purely imaginary vector. In particular the diagonal takes its values in the three-dimensional real space $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ of the purely imaginary vectors, and it is a **quadratic** map, $\tilde Q\diamond\tilde Q$ being homogeneous of degree two in the real coordinates.

*Proof.* Substitute $Q_0=a+ib$, $\overline{Q_0}=a-ib$, $\mathbf{Q}=\mathbf{u}+i\mathbf{v}$, $\overline{\mathbf{Q}}=\mathbf{u}-i\mathbf{v}$ in the coordinate rule $\tilde Q\diamond\tilde Q=-Q_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{Q}-\mathbf{Q}\times\overline{\mathbf{Q}}$. The first two terms give $2i(a\mathbf{v}-b\mathbf{u})$ and the third gives $2i\,\mathbf{u}\times\mathbf{v}$, because $\mathbf{Q}\times\overline{\mathbf{Q}}=-2i\,\mathbf{u}\times\mathbf{v}$. $\square$

**Remark (why the values are purely imaginary).** The square $\tilde Q\tilde Q^{*}$ is a Hermitian element, $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$; the Hermitian subspace $\mathbb{M}_+$ is the fixed set of the involution, and on it the scalar part is real while the vector part is purely imaginary. The vector part of the square is therefore the diagonal itself, and no further computation is needed to see that the diagonal cannot be a real vector: the imaginary unit in the corollary is forced by the involution, exactly as it is for the diagonal of the Hermitian form.

**Remark (the diagonal is not the square of the operation).** The formula is the diagonal, not a square in a bilinear sense: the operation $\diamond$ is conjugate-linear in its second slot, so the polarisation identity of the bilinear theory, which recovers a symmetric product from its diagonal, is unavailable and its place is taken by the pair $(\mathrm{SPS}(\tilde Q,\tilde Q),\tilde Q\diamond\tilde Q)$ of the two adapted halves of the square. This is the general phenomenon of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, §*The Diagonal and the Square*, read on the biquaternion product.

## The Elements of Square Zero

**Theorem (the criterion).** For a biquaternion $\tilde Q$, the diagonal vanishes,

$$
\tilde Q\diamond\tilde Q=0,
$$

if and only if $\tilde Q=0$ or $\tilde Q\tilde Q^{*}$ is a scalar, $\tilde Q\tilde Q^{*}=H(\tilde Q,\tilde Q)e_0$. In the second case $\tilde Q=\rho\,\tilde u$ for a complex $\rho\neq0$ and an element $\tilde u$ with $\tilde u\tilde u^{*}=e_0$.

*Proof.* $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})$, so the diagonal vanishes exactly when the Hermitian element $\tilde Q\tilde Q^{*}$ is central; a Hermitian central element is a real multiple of $e_0$, and its scalar part is $H(\tilde Q,\tilde Q)$. For $\tilde Q\neq0$ the scalar part $H(\tilde Q,\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ is positive, and $\rho$ a complex square root of it gives $\tilde u=\rho^{-1}\tilde Q$ with $\tilde u\tilde u^{*}=e_0$. Conversely, if $\tilde Q=\rho\tilde u$ and $\tilde u\tilde u^{*}=e_0$, then $\tilde Q\tilde Q^{*}=\lvert\rho\rvert^{2}e_0$ is central and the diagonal vanishes. $\square$

**Examples.** The centre $\mathbb{C}_{\mathbb{B}}$ lies wholly in the vanishing set, since a central element has zero vector part. The real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ lie wholly in it too: at a real element $\mathbf{v}=0$ and $b=0$ in the real form, and at an imaginary element $a=0$ and $\mathbf{u}=0$, so $a\mathbf{v}-b\mathbf{u}+\mathbf{u}\times\mathbf{v}=0$ in both cases. The element $e_1+ie_2$, which is in none of the three, is not in the set, since $\mathbf{u}=e_1$, $\mathbf{v}=e_2$ and $a=b=0$ give $2i\,\mathbf{u}\times\mathbf{v}=2ie_3\neq0$. And the element $e_0+ie_1$ is not in the set either, since the same form gives $2i\,\mathbf{v}=2ie_1$. The vanishing set is therefore a proper subset of the space that contains three of the remarkable subspaces — the centre and the two quaternion subspaces — and misses the vector subspace, on which the diagonal is the cross product $-\mathbf{Q}\times\overline{\mathbf{Q}}$.

**Corollary (the vanishing set is a cone).** If $\tilde Q\diamond\tilde Q=0$ then $(\lambda\tilde Q)\diamond(\lambda\tilde Q)=\lvert\lambda\rvert^{2}(\tilde Q\diamond\tilde Q)=0$ for every complex $\lambda$, so the vanishing set is a **complex cone**. It is the union of $\{0\}$ and the complex cone over the elements $\tilde u$ with $\tilde u\tilde u^{*}=e_0$.

## The Cone Traced by the Diagonal

**Proposition (the image of the diagonal).** The image of the map $\tilde Q\mapsto\tilde Q\diamond\tilde Q$ is the whole real three-dimensional space $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ of the purely imaginary vectors.

*Proof.* A purely imaginary vector is the vector part of a Hermitian element, and every Hermitian element of the form $\rho e_0+\mathbf{V}$, with $\mathbf{V}\in i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ and $\rho$ real, is positive semi-definite for $\rho$ large enough; being positive semi-definite and Hermitian it is a value $\tilde Q\tilde Q^{*}$ — it is the square of its own Hermitian square root. Hence every $\mathbf{V}\in i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ is attained as $\mathrm{Vect}(\tilde Q\tilde Q^{*})=\tilde Q\diamond\tilde Q$. $\square$

**Remark (the quadric).** The vanishing set of the diagonal is a **quadric cone**, the common zero set of the three real quadratic forms $a v_k-b u_k+(\mathbf{u}\times\mathbf{v})_k$ of the real coordinates, and it is not a hypersurface: it has real dimension five. It is the complex cone over the real **four-dimensional** set of the elements $\tilde u$ with $\tilde u\tilde u^{*}=e_0$, the complex scale contributing one real dimension after its redundancy is removed, since a nonzero $\tilde Q$ determines that scale up to a circle. Its cells are the centre, the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, which lie in it, and its generating section is the set of the elements $\tilde u$ with $\tilde u\tilde u^{*}=e_0$; the element $e_1+ie_2$ of the introduction lies in none of the cells and is not a zero. The image, by contrast, is not a quadric at all but the whole purely imaginary vector space of the corollary: the diagonal is a surjection onto a linear subspace, and its vanishing set is the quadric it carries.

**Remark (the relation to the row).** The vanishing criterion is the condition that the square of the element be central, $\tilde Q\tilde Q^{*}\in\mathbb{C}_{\mathbb{B}}$, and nothing else. It is the same condition that makes the Hermitian form $H(\tilde Q,\cdot)$ degenerate in a direction of the element, by *Biquaternion Norm and Invertibility*, so the elements of square zero for the block are exactly the elements that the row form cannot separate from the central line they span. In the two-by-two model the condition reads that the matrix of the element is a complex multiple of a matrix whose matrix product with its own conjugate transpose is the identity, which is the matrix reading of *The Antisymmetric Plain Sesqualgebra in the $2\times2$ and $4\times4$ Matrix Element Representations*, §*The Image and its Invariants*, below in this block.

## The Identity with the Sesquilinear Bracket and its Defect

The corpus carries a second antisymmetrisation of the same product, the **sesquilinear commutator** of *The Sesquilinear Commutator*,

$$
[\tilde P,\tilde Q]_{\varsigma}=\tilde P\tilde Q^{*}-\tilde Q\tilde P^{*},
$$

which is the difference of the two orders of the bare interchange. It is $R^{\varsigma}$-bilinear and antisymmetric in the bilinear sense, it is **not** a product of the class, and it is not the block either: the block is the half-difference of the product and its **conjugate**, $2\,\tilde P\diamond\tilde Q=\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}$, while the commutator is the difference of the product and its **swap**. The two agree exactly when the swapped value is its own conjugate.

**Theorem (the exact relation).** For all biquaternions,

$$
[\tilde P,\tilde Q]_{\varsigma}=2\,\tilde P\diamond\tilde Q+\bigl(\overline{\tilde Q\tilde P^{*}}-\tilde Q\tilde P^{*}\bigr).
$$

The bracket, the block and the defect are all additive and $\mathbb{R}$-bilinear, and the defect is the **imaginary part** of the swapped value with respect to the coefficientwise conjugation.

*Proof.* Subtract $2\,\tilde P\diamond\tilde Q=\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}$ from the definition of the commutator: $[\tilde P,\tilde Q]_{\varsigma}-2\,\tilde P\diamond\tilde Q=\overline{\tilde Q\tilde P^{*}}-\tilde Q\tilde P^{*}$, which is the defect. $\square$

**Corollary (the agreement on the real part, and the failure off it).** On the real span of $e_0,e_1,e_2,e_3$ the coefficientwise conjugation acts trivially, the defect vanishes, and the block coincides with the sesquilinear bracket; off the real part it does not. The witness is the pair $(ie_0,e_1)$: the bracket is

$$
[ie_0,e_1]_{\varsigma}=ie_0(-e_1)-e_1(-ie_0)=-ie_1+ie_1=0,
$$

while the doubled block is $2\,(ie_0\diamond e_1)=-2ie_1$, the defect being the difference $2ie_1$.

**Remark (which antisymmetrisation keeps the class).** The commutator is $R^{\varsigma}$-bilinear and does not lie in the class of the product; the block is sesquilinear over $(\mathbb{C},\bar{\cdot})$ and does. That is the content of *The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*, and it is why the two must not be identified: they are the two readings of the antisymmetry of the same product, one under the bare interchange of the arguments and one under the interchange twisted by the conjugation, and only the second keeps the class and so can be called the antisymmetric part.

## The Failure of the Jacobi Identity

**Definition.** For an operation $b$, additive in each variable, the **cyclic sum** of $b$ at the triple $(\tilde X,\tilde Y,\tilde Z)$ is

$$
\mathrm{cyc}\,b(\tilde X,\tilde Y,\tilde Z)=b\bigl(b(\tilde X,\tilde Y),\tilde Z\bigr)+b\bigl(b(\tilde Y,\tilde Z),\tilde X\bigr)+b\bigl(b(\tilde Z,\tilde X),\tilde Y\bigr),
$$

the outer form of *The Symmetric and Antisymmetric Parts of an Algebra Product*, §*Lie-Admissible Algebras*. The operation $b$ satisfies the Jacobi identity exactly when its cyclic sum vanishes for all triples; the factor $\tfrac12$ of the block is carried by $b$, so a bracket written without it has its cyclic sum multiplied by four.

**Theorem (the failure, and its witness).** The cyclic sum of the block does not vanish. At the real triple $(e_0,e_1,e_2)$,

$$
\mathrm{cyc}\,\diamond\,(e_0,e_1,e_2)=e_3\neq0,
$$

and at the complex triple $(e_1,e_1,ie_2)$,

$$
\mathrm{cyc}\,\diamond\,(e_1,e_1,ie_2)=-2ie_2\neq0 .
$$

*Proof.* For the first, the basis table gives $e_0\diamond e_1=-e_1$, $e_1\diamond e_2=-e_3$, $e_2\diamond e_0=e_2$ and $e_2\diamond e_1=e_3$; hence the three terms are $\diamond(e_0\diamond e_1,e_2)=\diamond(-e_1,e_2)=e_3$, $\diamond(e_1\diamond e_2,e_0)=\diamond(-e_3,e_0)=-e_3$ and $\diamond(e_2\diamond e_0,e_1)=\diamond(e_2,e_1)=e_3$, so the sum is $e_3$. For the second, $e_1\diamond e_1=0$, $\diamond(e_1,ie_2)=\overline{i}\,(e_1\diamond e_2)=ie_3$, and the two remaining terms are each $\diamond(ie_3,e_1)=i\,(e_3\diamond e_1)=i(-e_2)=-ie_2$, so the sum is $-2ie_2$. $\square$

**Remark (the tabulated value).** The value $e_3$ at $(e_0,e_1,e_2)$ is the one recorded for $\mathrm{APS}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Twelve Structures, One by One*, and it is reproduced here by the cyclic sum as that article declares it: the factor $\tfrac12$ is in the operation, so the bracket of the table is the operation itself and not twice it. The second witness is the one recorded for $\mathrm{AQS}$ in the same table, and the two share it; §*The Comparison with the Two Siblings* draws the consequence.

**Remark (the failure is not an associator).** The two displays show that the cyclic sum is a quadratic function of the elements that does not vanish; the failure is therefore not the associator defect of a bilinear product, of the kind that $\mathrm{AQA}$ exhibits, but the obstruction carried by the two conjugations of the operation. The plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ is genuinely **sesquilinear**, its two slots have opposite parity, and its antisymmetrisation is $R^{\varsigma}$-bilinear only, as *The Sesquilinear Product*, §*The Transposed Product*, records; the next section states which obstruction that is.

## The Obstruction of Lie Algebras of Sesqualgebras

**Proposition (a genuine sesquilinear antisymmetrisation is not a Lie bracket).** Let $A$ be a unital faithful sesqualgebra over $(R,\varsigma)$ with a $\varsigma$-sesquilinear product $\star$, and let $[x,y]_{\varsigma}=x\star y-y\star x$ be its antisymmetrisation. Then $[\,,\,]_{\varsigma}$ is antisymmetric and $R^{\varsigma}$-bilinear, and it satisfies the Jacobi identity exactly when the two involutions collapse, $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$, that is exactly when the product is bilinear and the sesqualgebra is an algebra. For a genuine sesqualgebra of full type at least one involution is nontrivial and the Jacobi identity fails.

*Proof.* The antisymmetry and the $R^{\varsigma}$-bilinearity are the two scalar rules read in the exchanged slots, as in *The Sesquilinear Product*, §*The Transposed Product*: the transposed product has the opposite parity, so the two halves of the bare split are only $R^{\varsigma}$-bilinear, and the two classes coincide exactly when $\bigl(\varsigma(\lambda)-\lambda\bigr)(y\star x)=0$ for all $\lambda,x,y$, which for a unital faithful algebra forces $\varsigma=\mathrm{id}$ and $*=\mathrm{id}$. For the Jacobi identity the computation is *Lie Algebras of Sesqualgebras*, §*The Failure of the Jacobi Identity*, where the failure is identified with the gap between the same two classes; the identity holds only in the collapse case, which is the bilinear and associative theory. $\square$

**Corollary (the reason for the block).** The block is the antisymmetric part of the plain sesquilinear product, so its failure is the failure of the proposition, and the obstruction is the one of *Lie Algebras of Sesqualgebras*. It is not the associator defect of $\mathrm{AQA}$, which lives in the bilinear row and comes from the non-associativity of the quaternionic product, and it is not a defect of a ternary product. The reason the block fails is that a genuine sesqualgebra over $(\mathbb{C},\bar{\cdot})$ carries two slots of opposite parity, and no $R^{\varsigma}$-bilinear bracket that is built out of the product alone can satisfy the identity that a bilinear bracket satisfies.

**Remark (which failure is invisible on the real basis).** The failure at the real triple $(e_0,e_1,e_2)$ is visible on the real span already, since the triple and the value $e_3$ are real: there the block is the $\mathrm{AQA}$-like operation $-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$, and it fails exactly as $\mathrm{AQA}$ does, with the opposite value. The **conjugated** failure is the invisible one: its witness $(e_1,e_1,ie_2)$ needs the non-real coefficient in the second slot, and the real span sees nothing of it. The two failures are of two kinds, and only the first is shared with the bilinear sibling.

## The Comparison with the Two Siblings

**The three failing brackets.** Of the twelve operations of *The 12 Products of the Biquaternion Complex Space*, exactly three fail the Jacobi identity, and the table of the failures, with the block entered at both of its witnesses, reads

| bracket | the identity | the witness | the cyclic sum |
|---|---|---|---|
| $\mathrm{AQA}$ | Jacobi | $(e_0,e_1,e_2)$ | $-e_3$ |
| $\mathrm{APS}$ | Jacobi | $(e_0,e_1,e_2)$ | $e_3$ |
| $\mathrm{APS}$ | Jacobi | $(e_1,e_1,ie_2)$ | $-2ie_2$ |
| $\mathrm{AQS}$ | Jacobi | $(e_1,e_1,ie_2)$ | $-2ie_2$ |

with the block in the two rows that concern it: the real witness, where it meets $\mathrm{AQA}$, and the conjugated witness, where it meets $\mathrm{AQS}$. The three failures have three different reasons.

**$\mathrm{AQA}$, the associator defect.** The quaternionic antisymmetrisation $\tilde P\diamond_{\mathrm{AQA}}\tilde Q=P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ is $\mathbb{C}$-bilinear, alternating, and its cyclic sum is the associator defect of the quaternionic product: it fails because the product it antisymmetrises is not associative, and the defect is a ternary object of that product. Its witness is the real triple $(e_0,e_1,e_2)$ with the value $-e_3$.

**$\mathrm{AQS}$, the conjugate-linear slot.** The quaternionic sesquilinear antisymmetrisation $\tilde P\diamond_{\mathrm{AQS}}\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$ is pure vector and conjugate-alternating, and it fails at $(e_1,e_1,ie_2)$ with the value $-2ie_2$. Its failure is the obstruction of the proposition above: the product $\tilde P^{\natural}\tilde Q^{*}$ is genuinely sesquilinear, and the antisymmetrisation of a genuine sesquilinear product is not a Lie bracket.

**The block, between the two.** The block is the plain-sesqualgebra sibling: pure vector, conjugate-alternating, with the same conjugated witness as $\mathrm{AQS}$ and with the real triple of $\mathrm{AQA}$, where its cyclic sum is the negative of the one of $\mathrm{AQA}$. On the real basis the two operations share the cross term and differ in the sign of the mixed term, $P_0\mathbf{Q}-Q_0\mathbf{P}$ against $-P_0\mathbf{Q}+Q_0\mathbf{P}$, and that sign is the sign of the two cyclic sums; off the real basis the block picks up the conjugation in the second slot and meets $\mathrm{AQS}$ instead. The two identities that relate the four operations of the row are the ones of §*The Exchange Behind the Names* of *The 12 Products of the Biquaternion Complex Space*.

## The Reading on the Real Part

**Proposition (the block on the real elements).** Let $\tilde P,\tilde Q$ have real coefficients. Then

$$
\tilde P\diamond\tilde Q=-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q},
$$

and if in addition both are pure vectors, $\tilde P\diamond\tilde Q=-\mathbf{P}\times\mathbf{Q}$, the negative of the cross product.

*Proof.* At real coefficients the coefficientwise conjugation is the identity on the coefficients, so the coordinate rule becomes the display; at $P_0=Q_0=0$ the first two terms drop and the cross term remains. $\square$

**Corollary (the diagonal on the real part).** On the real span the diagonal vanishes, $\tilde Q\diamond\tilde Q=0$, as it does for every cross product; on the real vectors alone the block is the cross product up to the sign, and it is alternating there. So the block is alternating on the real span, as a cross product is, but it is a Lie bracket there no more than on the complex space: the real span already fails at $(e_0,e_1,e_2)$, and the complex space adds the conjugated failure, which is the whole content of §*The Failure of the Jacobi Identity*.

**Remark (the ten operations of the real part).** The twelve operations fall to ten on the real span, where $\mathrm{APA}=\mathrm{AQS}$ and $\mathrm{SQA}=\mathrm{SPS}$, by *The 12 Products of the Biquaternion Complex Space*. The block is not one of the two coincidences: its real reading is $-P_0\mathbf{Q}+Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$, which is the real reading of $\mathrm{AQA}$ with the sign of the mixed term reversed, so the block remains distinct there. What it shares with $\mathrm{APA}$ is only the diagonal and the alternation on the real vectors, and what it shares with neither is the sign of the mixed term and the conjugation in the second slot.

## Summary

The diagonal of the block is the vector part of the square, $\tilde Q\diamond\tilde Q=\mathrm{Vect}(\tilde Q\tilde Q^{*})=2i(a\mathbf{v}-b\mathbf{u}+\mathbf{u}\times\mathbf{v})$ in real coordinates; it is a quadratic map into the purely imaginary vectors, its image is the whole three-dimensional space $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$, and it vanishes exactly on the complex cone of the elements whose square is central, $\tilde Q\tilde Q^{*}=H(\tilde Q,\tilde Q)e_0$, a quadric cone of real dimension five that contains the quaternion subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ and misses $e_1+ie_2$. The block is the plain-sesqualgebra sibling of the sesquilinear commutator, with which it agrees on the real span and from which it differs by the defect $\overline{\tilde Q\tilde P^{*}}-\tilde Q\tilde P^{*}$, the witness being the pair $(ie_0,e_1)$. The Jacobi identity fails, at $(e_0,e_1,e_2)$ with the cyclic sum $e_3$ and at $(e_1,e_1,ie_2)$ with $-2ie_2$, and the reason is the obstruction of *Lie Algebras of Sesqualgebras*, not an associator: a genuine sesquilinear antisymmetrisation is a Lie bracket only after the collapse of the two involutions, which the complex conjugation forbids. Among the three failing brackets of the row table, the block is the one that shares the witness of $\mathrm{AQS}$ and the opposite value of $\mathrm{AQA}$ at the real triple, and on the real vectors alone it is a cross product up to sign.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | the operation of the block |
| $\tilde Q\diamond\tilde Q=2i(a\mathbf{v}-b\mathbf{u}+\mathbf{u}\times\mathbf{v})$ | the diagonal, $Q_0=a+ib$, $\mathbf{Q}=\mathbf{u}+i\mathbf{v}$ |
| $i\,\mathrm{Vect}_{\mathbb{R}}(\mathbb{B})$ | the purely imaginary vectors, the image of the diagonal |
| $\tilde Q\tilde Q^{*}=H(\tilde Q,\tilde Q)e_0$ | the criterion for the square-zero elements |
| $[\tilde P,\tilde Q]_{\varsigma}=\tilde P\tilde Q^{*}-\tilde Q\tilde P^{*}$ | the sesquilinear commutator, the bare antisymmetrisation |
| $\overline{\tilde Q\tilde P^{*}}-\tilde Q\tilde P^{*}$ | the defect between the bracket and twice the block |
| $\mathrm{cyc}\,b(\tilde X,\tilde Y,\tilde Z)$ | the cyclic sum, with the factor $\tfrac12$ carried by $b$ |
| $\mathrm{AQA},\mathrm{AQS}$ | the two sibling failing brackets, $\mathbf{P}\times$ and conjugate variants |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the block, its class and the basis values used here
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the adapted split, the diagonal of a sesqualgebra part and the class the bare split fails to keep
- *The Sesquilinear Commutator* (`articles_maths/the-sesquilinear-commutator.md`) and *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions* (`articles_maths/the-sesquilinear-commutator-and-the-symmetrised-product-on-the-biquaternions.md`), for the bare antisymmetrisation and its laws
- *Lie Algebras of Sesqualgebras* (`articles_maths/lie-algebras-of-sesqualgebras.md`), for the obstruction that forbids the antisymmetrisation of a genuine sesquilinear product
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the row table, the three failures, the real witnesses and the ten operations of the real part
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form $H$, the square and the zero divisors
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the remarkable subspaces and the Hermitian and anti-Hermitian halves
- *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the diagonal and the square-zero elements in the realization
- *The Antisymmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the diagonal and the square-zero elements in the regular model
