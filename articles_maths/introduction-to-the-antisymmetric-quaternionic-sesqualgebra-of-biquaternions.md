# __Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions__

## Introduction

The quaternionic sesquilinear product of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the operation $\tilde P^{\natural}\tilde Q^{*}$ of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, with one $\mathbb{C}$-linear slot and one conjugate-linear slot. Its exchange of the two arguments does not keep the class of the operation, so the splitting of the product into a symmetric and an antisymmetric part is read with the **class-preserving exchange**, the conjugate of the swapped value, and not with the bare interchange; the construction and its two admissible cases are *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. This article reads the **antisymmetric part** as a multiplication in its own right:

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)
=\mathbf{P}\times\overline{\mathbf{Q}},
$$

scalar part zero and vector part the cross product of the vector part of the first argument with the **conjugate** of the vector part of the second. The operation is the operation named $\mathrm{AQS}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; it is the only one of the twelve whose value is a single cross-product term with the second argument conjugated, with neither a scalar part nor a mixed term, and its second slot carries the Hermitian conjugation, as do the second slots of the five other sesquilinear operations of the two sesqualgebra rows.

The reading is one of the twelve operations of the corpus; the general construction of the parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, the product it splits is *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, the sesquilinear obstruction behind its failing law is *Lie Algebras of Sesqualgebras*, and the block that reads the symmetric half is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*. This article owns the block as a multiplication: the rule, the class, the conjugate-alternation, the pure-vector image, the absence of a unit, the sixteen products of the basis, the non-vanishing diagonal, the failure of the Jacobi identity, and the placement of the block among the twelve. The diagonal and the conjugate cross product are developed in *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*; the pairing with the Krein form is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*; the remarkable subspaces are *Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*; the operators are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*; and the two matrix models are *The Antisymmetric Quaternionic Sesqualgebra in the $2\times2$ and $4\times4$ Matrix Element Representations*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, central scalar imaginary $i$ and $e_1e_2=e_3$, so that $e_1^2=e_2^2=e_3^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. A generic element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$; $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ is the complex bilinear dot product, $\times$ the cross product of the vector parts, and $\overline{\mathbf{Q}}=\sum_k\overline{Q_k}e_k$ the coefficientwise conjugate of the vector part. The natural conjugation ${}^{\natural}$ negates $e_1,e_2,e_3$, the Hermitian conjugation is ${}^{*}={}^{\natural}\circ\bar{\cdot}$, and the Krein form is $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon=(1,-1,-1,-1)$, linear in the first argument and conjugate-linear in the second, as the scalar part of the product $\tilde P^{\natural}\tilde Q^{*}$. The operation of the block is written $\diamond$; the comment of the menu entry writes it $\wedge$, and this article prefers $\diamond$ because $\wedge$ names the plain outer product $\mathbf{P}\times\mathbf{Q}$ of *Introduction to the Antisymmetric Plain Algebra of Biquaternions*.

## The Split of the Quaternionic Sesquilinear Product

### The Rule

**Definition.** The **conjugate cross product** of two biquaternions is

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr).
$$

It is the **antisymmetric part** of the general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ under the class-preserving exchange, the operation named $\mathrm{AQS}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The space $\mathbb{B}$ with the product $\diamond$ is the **antisymmetric quaternionic sesqualgebra** of the block. The decomposition is the one of the general theory: the class-preserving exchange fixes the two halves, so no choice of notation enters the rule.

### The Scalar–Vector and Coordinate Forms

**Theorem (the value is a cross product).** For all biquaternions,

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}},
$$

so the scalar part of the value is zero and its vector part is $\mathbf{P}\times\overline{\mathbf{Q}}$.

*Proof.* The product $\tilde P^{\natural}\tilde Q^{*}$ of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* has the scalar–vector form

$$
\tilde P^{\natural}\tilde Q^{*}=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}} .
$$

The swapped product $\tilde Q^{\natural}\tilde P^{*}$ has the same form with $\tilde P$ and $\tilde Q$ exchanged, and its conjugate is $\overline{\tilde Q^{\natural}\tilde P^{*}}=\tilde Q^{*}\tilde P^{\natural}$, the second term of the rule. Subtracting the conjugate of the swapped form from the form and halving: the scalar parts cancel because $P_0\overline{Q_0}-\overline{Q_0}P_0=0$ and $(P,\overline{\mathbf{Q}})-(\overline{\mathbf{Q}},\mathbf{P})=0$, the two arguments of the dot product being equal; the two mixed terms are equal and cancel in the subtraction, since the mixed term of the exchanged form is $-\bigl(Q_0\overline{\mathbf{P}}+\overline{P_0}\mathbf{Q}\bigr)$ and its conjugate is $-\bigl(P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}\bigr)$, the mixed term of the form; and the two cross terms add, $\mathbf{P}\times\overline{\mathbf{Q}}+\overline{\mathbf{Q}\times\overline{\mathbf{P}}}=2\,\mathbf{P}\times\overline{\mathbf{Q}}$, since $\overline{\mathbf{Q}\times\overline{\mathbf{P}}}=\overline{\mathbf{Q}}\times\mathbf{P}=-\mathbf{P}\times\overline{\mathbf{Q}}$. The half is therefore $\mathbf{P}\times\overline{\mathbf{Q}}$, of scalar part zero. Verified on general elements.

**Proposition (coordinate rule).** In the coordinates of the two arguments,

$$
\tilde P\diamond\tilde Q=\bigl(P_2\overline{Q_3}-P_3\overline{Q_2}\bigr)e_1+\bigl(P_3\overline{Q_1}-P_1\overline{Q_3}\bigr)e_2+\bigl(P_1\overline{Q_2}-P_2\overline{Q_1}\bigr)e_3.
$$

*Proof.* The displayed cross product of the vector parts, in the quaternion basis with $e_1e_2=e_3$. Verified on the coordinate rule.

### The Class

**Proposition.** The conjugate cross product is **sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$**: it is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second,

$$
(A\tilde P)\diamond\tilde Q=A(\tilde P\diamond\tilde Q),\qquad
\tilde P\diamond(A\tilde Q)=\overline{A}\,(\tilde P\diamond\tilde Q)\qquad(A\in\mathbb{C}).
$$

*Proof.* The cross product $\mathbf{P}\times\overline{\mathbf{Q}}$ is $\mathbb{C}$-linear in $\mathbf{P}$ and conjugate-linear in $\overline{\mathbf{Q}}$; equivalently the coordinate rule above is homogeneous of degree one in each coordinate of $\tilde P$ and of degree one in each conjugate coordinate of $\tilde Q$. Verified on the coordinate rule.

**Remark (the class is the whole difficulty of the block).** The operation is conjugate-linear in the second argument; that slot is shared with the five other sesquilinear operations of *The 12 Products of the Biquaternion Complex Space*, and what singles the block out among the twelve is that its value is the conjugate cross product alone, with no scalar part and no mixed term. Every later statement of the block is a consequence of the conjugate-linear slot: the ordinary operator calculus is unavailable for the left multiplications, the value is not conjugate-symmetric but conjugate-alternating, and the coincidence with the plain cross product holds only on the real elements.

### Conjugate-Alternation

**Proposition.** The conjugate cross product is **conjugate-alternating**:

$$
\tilde P\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde P}.
$$

*Proof.* The rule gives $\tilde Q\diamond\tilde P=\mathbf{Q}\times\overline{\mathbf{P}}$, and $\overline{\mathbf{Q}\times\overline{\mathbf{P}}}=\overline{\mathbf{Q}}\times\mathbf{P}=-\mathbf{P}\times\overline{\mathbf{Q}}$, which is the negative of the value of the block. Verified on the coordinate rule.

The symmetry is the antisymmetry of the block read through the conjugate of the value, in the sense of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*: the bare interchange of a sesquilinear product returns the conjugate of the value, and the antisymmetric part is conjugate-alternating rather than alternating.

### The Pure-Vector Image and the Absence of a Unit

**Proposition.** The values of the block are **pure vector**, so its image is contained in $\mathrm{Vect}(\mathbb{B})$, and it is $\mathrm{Vect}(\mathbb{B})$ itself.

*Proof.* The rule has no scalar term, so every value has scalar part zero. Conversely every vector $\mathbf{V}$ is attained, since for a real $\mathbf{P}$ the map $\mathbf{Q}\mapsto\mathbf{P}\times\overline{\mathbf{Q}}$ is the cross product with a fixed nonzero real vector, whose values fill the two-dimensional subspace orthogonal to $\mathbf{P}$; taking $\mathbf{P}$ over two independent real directions fills $\mathrm{Vect}(\mathbb{B})$. Verified on the basis, where the values of the block are exactly the six signed vector units.

**Proposition.** The block has **no unit**: there is no element $\tilde E$ with $\tilde E\diamond\tilde Q=\tilde Q$ for all $\tilde Q$, on either side.

*Proof.* A value of the block is pure vector, while a general $\tilde Q$ has a scalar part; for $\tilde Q=e_0$ every left value $\tilde E\diamond e_0$ is zero, so no $\tilde E$ can reproduce $e_0$. The same argument on the right. Verified on the basis.

The absence of a unit is shared with the other six parts of the twelve: of the twelve operations, only the general products and the symmetric plain product carry one.

### The Sixteen Products of the Basis

**Proposition.** The products of the basis elements are

| $\diamond$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $0$ | $e_3$ | $-e_2$ |
| $e_2$ | $0$ | $-e_3$ | $0$ | $e_1$ |
| $e_3$ | $0$ | $e_2$ | $-e_1$ | $0$ |

*Proof.* The basis elements are real, so $\overline{\mathbf{Q}}=\mathbf{Q}$ and the block is the ordinary cross product; the table is the cross-product table, with the first row and column zero because a scalar has zero vector part. Verified on the sixteen pairs.

**Remark (which entries vanish and why).** On the sixteen basis pairs the block vanishes exactly on the pairs one of whose arguments is central — the first row and the first column of the table — and on the four diagonal pairs, the diagonal one because a real vector is parallel to its own conjugate. The table is antisymmetric, with $e_\mu\diamond e_\nu=-e_\nu\diamond e_\mu$, as conjugate-alternation requires on the real basis. The diagonal of the block vanishes on the four real basis elements, and the block is nonetheless not alternating on the whole space, as the next section shows.

### The Diagonal and the Square

**Theorem (the diagonal does not vanish).** For every biquaternion,

$$
\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}},
$$

which is not zero in general; writing $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$ with $\mathbf{a},\mathbf{b}$ real vectors,

$$
\mathbf{Q}\times\overline{\mathbf{Q}}=-2i\,\mathbf{a}\times\mathbf{b},
$$

so that at $\tilde Q=e_1+ie_2$ the value is $-2ie_3$.

*Proof.* The rule with $\tilde P=\tilde Q$; and $\mathbf{Q}\times\overline{\mathbf{Q}}=(\mathbf{a}+i\mathbf{b})\times(\mathbf{a}-i\mathbf{b})=-i\,\mathbf{a}\times\mathbf{b}+i\,\mathbf{b}\times\mathbf{a}=-2i\,\mathbf{a}\times\mathbf{b}$, the two real cross products cancelling. At $\tilde Q=e_1+ie_2$ one has $\mathbf{a}=e_1$, $\mathbf{b}=e_2$ and $\mathbf{a}\times\mathbf{b}=e_3$. Verified on general elements and at the witness.

**Remark (the diagonal against the plain block).** The diagonal of $\mathrm{AQS}$ is the **vector part of the square** in the sense of the conjugate half-difference: $\tilde Q\diamond\tilde Q=\tfrac12\bigl(\tilde Q^{\natural}\tilde Q^{*}-\overline{\tilde Q^{\natural}\tilde Q^{*}}\,\bigr)$, the imaginary half of the square $\tilde Q^{\natural}\tilde Q^{*}$ of the general quaternionic sesquilinear product, whose theory is *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*. This is the bridge to the square article, and it is exact: the block is the conjugate half-difference of the two orders of the square, and it is not the vector part of the value $\tilde Q^{\natural}\tilde Q^{*}$ itself, which differs from the diagonal off the elements whose square has a real scalar part and a purely imaginary vector part.

**Proposition (the diagonal vanishes exactly on the cone of the diagonal).** The diagonal vanishes at $\tilde Q$ exactly when $\mathbf{Q}$ is a complex multiple of a real vector; the set of such $\tilde Q$ is the cone $\tilde Q\diamond\tilde Q=0$, of six real dimensions, the scalar coordinate being free and the vector part running over a cone of four real dimensions in the vector subspace, and the theory of that cone is *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*.

## The Failure of the Jacobi Identity

### The Witness

**Theorem.** The block fails the **Jacobi identity**. With the cyclic sum declared by the corpus,

$$
(\tilde P\diamond\tilde Q)\diamond\tilde R+(\tilde Q\diamond\tilde R)\diamond\tilde P+(\tilde R\diamond\tilde P)\diamond\tilde Q,
$$

the triple $(\tilde P,\tilde Q,\tilde R)=(e_1,e_1,ie_2)$ gives the value $-2ie_2$, which is not zero.

*Proof.* The catalogue *The 12 Products of the Biquaternion Complex Space* declares the cyclic sum as the sum of the three reassociations displayed, and records the witness and the value; both are recomputed here on the cross-product table. The three inner values are $e_1\diamond e_1=0$, $e_1\diamond ie_2=\mathbf{e_1}\times\overline{ie_2}=e_1\times(-ie_2)=-ie_3$ and $ie_2\diamond e_1=(ie_2)\times e_1=i(e_2\times e_1)=-ie_3$. Hence the three reassociations are $(e_1\diamond e_1)\diamond ie_2=0$, $(e_1\diamond ie_2)\diamond e_1=(-ie_3)\diamond e_1=(-ie_3)\times e_1=-ie_2$ and $(ie_2\diamond e_1)\diamond e_1=(-ie_3)\diamond e_1=-ie_2$, whose sum is $-2ie_2$. Verified on the witness.

**Remark (the declaration of the cyclic sum).** The corpus declares the cyclic sum as the sum of the three reassociations, and the recomputation above uses that declaration. The older order of the inner brackets, $[[\tilde P,\tilde Q],\tilde R]+\cdots$ with $[\tilde P,\tilde Q]=2(\tilde P\diamond\tilde Q)$, and the sum of the reassociations do not have the same display; the value $-2ie_2$ recorded here is the value of the declared sum, and it is the one tabulated in the catalogue.

**Remark (the smallest witness needs a complex element).** The witness uses the complex element $ie_2$ and no triple of the real basis: on real elements the block is the ordinary cross product of *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, whose Jacobi identity is the classical one and holds, so a real witness cannot exist. The failure is therefore a genuine feature of the complex structure and of the conjugate-linear slot, and, of the six identity failures the corpus declares (the three Jacobi failures of the antisymmetric parts and the three Jordan failures of the symmetric parts), it is the only one whose witness needs an element off the real basis. It is not the only failure of the complex space: the two sesquilinear antisymmetric parts fail the Jordan identity as soon as a complex element enters, though the corpus does not ask it of them.

### The Coincidence with the Plain Block on the Real Part

**Theorem.** On the real elements the block coincides with the antisymmetric part of the plain product, the map $\tilde P\tilde Q\mapsto\mathbf{P}\times\mathbf{Q}$ of *Introduction to the Antisymmetric Plain Algebra of Biquaternions*:

$$
\tilde P\diamond\tilde Q=\mathbf{P}\times\mathbf{Q}=\mathrm{APA}(\tilde P,\tilde Q)
\qquad(\tilde P,\tilde Q\ \text{real}).
$$

*Proof.* A real vector is its own conjugate, so the rule reduces to $\mathbf{P}\times\mathbf{Q}$. Verified on the sixteen real basis pairs.

**Remark (the failure is invisible on the real forms).** The coincidence is the whole reason the failure of the Jacobi identity cannot be witnessed on real elements: there the block is the Lie product $\mathrm{APA}$, whose Jacobi identity holds, and the failure appears only once the conjugate of the second argument differs from the argument. The distinction between $\mathrm{APA}$ and $\mathrm{AQS}$ is the conjugate on the second slot, and it is exactly the distinction that the twelve collapse on the real part, where $\mathrm{APA}=\mathrm{AQS}$.

### The Consequence

The failure of the Jacobi identity is the obstruction of *Lie Algebras of Sesqualgebras* read on the block: the antisymmetrisation of a sesquilinear product is a Lie bracket only after the collapse of the two involutions, which a genuine sesqualgebra forbids, and the block is one of the three failing antisymmetrisations of the corpus. The consequence is stated without proof here and developed with the other two failing brackets in *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*: the block is not a Lie algebra over any ring of scalars of the complex space.

**Remark (the count and the closure).** On the eight-element basis the declared cyclic sum is nonzero on $72$ of the $512$ triples, the sparsest of the three failing brackets of the catalogue. And the failure is not a failure of a span: the real span of the values of the block over $100$ random complex triples is the **whole** six-dimensional vector subspace, so the block is not too small to close — it is a vector space of directions that is not an algebra. The closure one can form from the block is therefore a span and not a Lie algebra, which is the negative reading in its sharpest form. The count is a count on a basis and not an invariant; both are recomputed.

## The Reconstruction and the Twelve

### The Reconstruction $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$

**Theorem.** The quaternionic sesquilinear product is the sum of its two parts:

$$
\tilde P^{\natural}\tilde Q^{*}=\tilde P\diamond_{\!+}\tilde Q+\tilde P\diamond\tilde Q,
$$

where $\tilde P\diamond_{\!+}\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\overline{\tilde Q^{\natural}\tilde P^{*}}\,\bigr)$ is the symmetric part $\mathrm{SQS}$ and $\tilde P\diamond\tilde Q$ is the block.

*Proof.* The half-sum and the half-difference of the value and the conjugate of the swapped value are the two parts of the general construction, and they add to the value; the second is the rule of this article. Verified on general elements.

The pair is the unique decomposition of the product into a conjugate-symmetric and a conjugate-alternating part, and either determines the other from the product; the symmetric half is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*.

### The Placement among the Twelve

The name $\mathrm{AQS}$ is read with the code of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*: the first letter $\mathrm A$ says that the operation is the antisymmetric part of the row; the second letter $\mathrm Q$ says that the row is the quaternionic product $\tilde P^{\natural}\tilde Q$; and the third letter $\mathrm S$ says that the class is that of the two sesqualgebras over $(\mathbb{C},\bar{\cdot})$, whose second slot is conjugate-linear.

| the row | general | symmetric | antisymmetric |
|---|---|---|---|
| the plain algebra | $\mathrm{GPA}$ | $\mathrm{SPA}$ | $\mathrm{APA}$ |
| the quaternionic algebra | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
| the plain sesqualgebra | $\mathrm{GPS}$ | $\mathrm{SPS}$ | $\mathrm{APS}$ |
| the quaternionic sesqualgebra | $\mathrm{GQS}$ | $\mathrm{SQS}$ | $\mathrm{AQS}$ |

**Remark (the place of the block).** The block is conjugate-linear in its second slot, pure-vector-valued, has no unit, and fails the Jacobi identity; its diagonal does not vanish and its image is the vector subspace. Of the twelve operations it is the only one whose value is the conjugate cross product alone, and on the real part it falls together with $\mathrm{APA}$. The names of the twelve are owned by *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and their laws by *The 12 Products of the Biquaternion Complex Space*, and the general construction of the parts by *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

## Summary

The antisymmetric part of the general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ is the operation

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}},
$$

the conjugate cross product, the only operation of the twelve whose value is a single cross-product term with the second argument conjugated. It is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, conjugate-alternating, pure-vector-valued with image $\mathrm{Vect}(\mathbb{B})$, and has no unit. Its diagonal does not vanish, $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}=-2i\,\mathbf{a}\times\mathbf{b}$ at $\mathbf{Q}=\mathbf{a}+i\mathbf{b}$, and it is $-2ie_3$ at $e_1+ie_2$. The Jacobi identity fails, with the witness $(e_1,e_1,ie_2)$ whose declared cyclic sum is $-2ie_2$; the witness needs a complex element, and on the real elements the block coincides with $\mathrm{APA}$, so the failure is invisible there. The product reconstructs as $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$, the half-sum and the half-difference of the two orders of the square of the quaternionic sesquilinear product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})$ | the conjugate cross product, the multiplication of the block |
| $\mathbb{B}^{\diamond}$ | the biquaternion space with the conjugate cross product |
| $\mathrm{AQS}$ | the name of the operation among the twelve |
| $\mathbf{P}\times\overline{\mathbf{Q}}$ | the scalar–vector rule of the block |
| $\tilde Q\diamond\tilde Q=\mathbf{Q}\times\overline{\mathbf{Q}}$ | the diagonal, non-vanishing in general |
| $(e_1,e_1,ie_2)\mapsto-2ie_2$ | the Jacobi witness |
| $\mathrm{APA}=\mathbf{P}\times\mathbf{Q}$ | the real coincidence of the block |
| $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$ | the reconstruction of the quaternionic sesquilinear product |
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form of the block's pairing |

## Further Reading

- *The 12 Products of the Biquaternion Complex Space*, for the names, the laws and the table of the twelve operations.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*, for the class-preserving exchange and the two halves.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, for the product the block splits.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, for the companion half.
- *Lie Algebras of Sesqualgebras*, for the obstruction behind the failing Jacobi identity.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*, *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, *Remarkable Subspaces under the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* and *The Antisymmetric Quaternionic Sesqualgebra in the $2\times2$ and $4\times4$ Matrix Element Representations*, for the remainder of the block.
