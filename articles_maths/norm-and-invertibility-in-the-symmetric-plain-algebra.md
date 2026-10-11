# __Norm and Invertibility in the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*, the multiplication named $\mathrm{SPA}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. This article determines the elements of the block that have an **inverse**, gives the inverse, and reads the functional that decides invertibility as the **generic norm** of a Jordan algebra of degree two.

The block is commutative and unital and every element satisfies a **quadratic identity**; the two coefficients of that identity are the **generic trace** $T(\tilde Q)=2Q_0$ and the **generic norm** $N(\tilde Q)=\sum_\mu Q_\mu^2=\tilde Q\tilde Q^{\natural}$. The norm is not new to the space — *Norm and Invertibility in the General Plain Algebra* studies it as the norm of the algebra — but the reading is the block's own: the quadratic identity is the **generic minimal polynomial**, its companion root is the inverse, and the criterion is the non-vanishing of the norm.

The block is non-associative, and the inverse must be handled with care. The single equation $\tilde Q\bullet\tilde{R}=e_0$ is degenerate: the element $e_1+ie_2$ has a two-dimensional affine family of solutions and satisfies $N(e_1+ie_2)=0$. The inverse is therefore the inverse of the Jordan theory, defined by a **second equation**, and it is with that definition that the criterion $N(\tilde Q)\neq0$ holds. The same non-associativity destroys the multiplicativity of the norm, which is replaced by the quadratic representation, and it destroys the group of units, which does not survive under the block product.

Invertibility names a product, and the definition is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*; throughout this article the product is $\bullet$ and, unqualified, **invertible** means invertible of $\bullet$. The norm, its multiplicativity for the plain product and the invertibility criterion of the algebra are *Norm and Invertibility in the General Plain Algebra*; the trace form the norm polarises is *The Trace Form and the Invariance of the Symmetric Plain Algebra*; the degree-two structure and the square are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*; and the elements the block fails to invert are *Zero Divisors of the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and $Q_\mu\in\mathbb{C}$. An element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$, and $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ is the complex bilinear dot product of the vector parts. The product $\tilde P\tilde Q$ without a mark is the general plain bilinear product; the product with the mark is $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$, and $\tilde Q^{\bullet2}=\tilde Q\bullet\tilde Q$. The natural conjugation is $\tilde Q^{\natural}=Q_0e_0-\mathbf{Q}$. The remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ are *Introduction to the Remarkable Subspaces*.

## The Inverse of a Product

### The General Definition

An element is invertible relative to a product, and the equation names it. Let $\star$ be a product on $\mathbb{B}$ with a two-sided unit $e$; then $\tilde{Q}$ is **invertible of $\star$** when there is a $\tilde{R}$ with

$$
\tilde{Q}\star\tilde{R}=\tilde{R}\star\tilde{Q}=e,
$$

and such an $\tilde{R}$ is an inverse of $\tilde{Q}$ of $\star$ (*Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*). In an associative unital product the inverse is unique and the invertible elements form a group (*Unital Algebras*).

Throughout this article the product is the symmetric plain product $\bullet$, whose two-sided unit is $e_0$ (*Introduction to the Symmetric Plain Algebra of Biquaternions*); *unqualified*, **invertible** means invertible of $\bullet$, and the equation to solve is

$$
\tilde{Q}\bullet\tilde{R}=\tilde{R}\bullet\tilde{Q}=e_0 .
$$

The product is commutative, so the two one-sided equations are one, and no distinction of left, right and two-sided arises: **in the block the three notions coincide**, which is the first and the easy collapse. The second collapse is not automatic, and it is the subject of the next subsection.

### The Naive Inverse Is Not Unique

**Proposition (the inverse equation is degenerate).** The element $\tilde\Upsilon=e_1+ie_2$ has $N(\tilde\Upsilon)=0$ and satisfies $\tilde\Upsilon\bullet\tilde{R}=e_0$ for a two-dimensional affine family of $\tilde{R}$.

*Proof.* The left multiplication $L^{\bullet}_{\tilde\Upsilon}$ has the kernel $\mathrm{span}\{e_3,-ie_1+e_2\}$: the products are $\tilde\Upsilon\bullet e_3=\tfrac12(e_1e_3+e_3e_1)=0$ and $\tilde\Upsilon\bullet(-ie_1+e_2)=-i\tilde\Upsilon\bullet e_1+\tilde\Upsilon\bullet e_2=-i(-e_0)+(-ie_0)=0$, and the kernel is two-dimensional because the image is $\mathrm{span}\{e_0,\tilde\Upsilon\}$. The element $\tilde{R}_0=-e_1$ is a solution, $\tilde\Upsilon\bullet(-e_1)=-(-e_0)=e_0$, and every $\tilde{R}_0+\tilde{K}$ with $\tilde{K}$ in the kernel is a solution.

The counter-example is decisive against the naive equation alone: **the equation $\tilde{Q}\bullet\tilde{R}=e_0$ can have a solution when $N(\tilde{Q})=0$, and then the solution is not unique.** The block is therefore treated with the inverse of the Jordan theory and not with the equation of an associative algebra.

### The Jordan Inverse

**Definition (the Jordan inverse).** Let the product have a unit $e$. The element $\tilde{Q}$ is **invertible** when there is a $\tilde{R}$ with

$$
\tilde{Q}\star\tilde{R}=e\qquad\text{and}\qquad\tilde{Q}^{\star2}\star\tilde{R}=\tilde{Q},
$$

and such a $\tilde{R}$ is the **inverse** $\tilde{Q}^{-1}$ of $\tilde{Q}$. The second equation is the one that removes the degeneracy of the naive equation.

The definition is the classical one of the Jordan theory: an element of a unital Jordan algebra is invertible exactly when the second equation holds beside the first, and then the inverse is unique and the quadratic representation $U_{\tilde Q}$ is an invertible operator (McCrimmon, *A Taste of Jordan Algebras*, for the definition and the equivalence). In the block the three objects agree: the elements with the two equations, the elements with $U_{\tilde Q}$ invertible, and the elements with $N(\tilde Q)\neq0$ are the same set, computed in §*The Criterion*.

**Remark (why the two equations are one in the algebra and two in the block).** For an associative product the second equation follows from the first: $\tilde Q^{\star2}\star\tilde R=\tilde Q\star(\tilde Q\star\tilde R)=\tilde Q\star e=\tilde Q$, and $\tilde Q\star(\tilde Q\star\tilde R)=(\tilde Q\star\tilde Q)\star\tilde R$ is associativity. In the block that step fails, and on the witness $\tilde\Upsilon$ the first equation holds while the second fails, $\tilde\Upsilon^{\bullet2}\bullet\tilde R=0\neq\tilde\Upsilon$ for every solution $\tilde R$.

## The Generic Trace and the Generic Norm

### The Square and the Quadratic Identity

The square of the block is the plain square, so the scalar–vector rule of *Introduction to the General Plain Algebra of Biquaternions* gives it in closed form.

**Proposition (the square).** For every $\tilde Q$,

$$
\tilde Q^{\bullet2}=\tilde Q^2=\bigl[Q_0^2-(\mathbf{Q},\mathbf{Q})\bigr]e_0+2Q_0\mathbf{Q}.
$$

*Proof.* $\tilde Q\bullet\tilde Q=\tfrac12(\tilde Q^2+\tilde Q^2)=\tilde Q^2$, and the plain square is the displayed form (*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*).

**Theorem (the quadratic identity).** Every element of the block satisfies

$$
\tilde Q^{\bullet2}-T(\tilde Q)\tilde Q+N(\tilde Q)e_0=0,
$$

with the **generic trace** and the **generic norm**

$$
T(\tilde Q)=2Q_0,\qquad N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2=Q_0^2+(\mathbf{Q},\mathbf{Q})=\tilde Q\tilde Q^{\natural}.
$$

*Proof.* On the square, $T(\tilde Q)\tilde Q=2Q_0(Q_0e_0+\mathbf{Q})=2Q_0^2e_0+2Q_0\mathbf{Q}$; subtracting it from the square leaves $\bigl[Q_0^2-(\mathbf{Q},\mathbf{Q})-2Q_0^2+N(\tilde Q)\bigr]e_0$, and the coefficient vanishes because $N(\tilde Q)=Q_0^2+(\mathbf{Q},\mathbf{Q})$.

**Definition.** The quadratic identity is the **generic minimal polynomial** of the block; $T$ is its **generic trace** and $N$ its **generic norm**, and the block is a **Jordan algebra of degree two**. The operator trace of the left multiplication is twice the generic trace, $\operatorname{Tr}(L^{\bullet}_{\tilde Q})=2T(\tilde Q)=4Q_0$, and the generic norm is the biquaternion norm of the algebra article, $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}$.

The identity also fixes the unital subalgebra generated by one element: by the theorem $\tilde Q^{\bullet2}=T(\tilde Q)\tilde Q-N(\tilde Q)e_0$, so the subalgebra generated by $\tilde Q$ and $e_0$ is $\mathbb{C}e_0+\mathbb{C}\tilde Q$, of $\mathbb{C}$-dimension two off the centre.

### The Discriminant

**Proposition.** The discriminant of the generic minimal polynomial is

$$
T(\tilde Q)^2-4N(\tilde Q)=-4(\mathbf{Q},\mathbf{Q}).
$$

*Proof.* $T^2-4N=4Q_0^2-4(Q_0^2+(\mathbf{Q},\mathbf{Q}))=-4(\mathbf{Q},\mathbf{Q})$.

The discriminant vanishes exactly on the elements with $(\mathbf{Q},\mathbf{Q})=0$, which include the whole centre $\mathbb{C}_{\mathbb{B}}$ but are strictly larger, the element $e_1+ie_2$ having $(\mathbf{Q},\mathbf{Q})=1+i^2=0$ with a non-zero vector part. The locus is not the isotropic cone of the norm, a distinction made in *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

## The Invertibility Criterion

### The Criterion

**Theorem (the criterion).** An element $\tilde Q$ of the block is invertible if and only if its generic norm is non-zero:

$$
\tilde Q\ \text{invertible of }\bullet\iff N(\tilde Q)\neq0 .
$$

*Proof.* Suppose $N(\tilde Q)\neq0$ and put $\tilde{R}=\tilde Q^{\natural}/N(\tilde Q)$. The quadratic identity, divided by $N(\tilde Q)$, is $\tilde Q^{\bullet2}/N(\tilde Q)-T(\tilde Q)\tilde Q/N(\tilde Q)+e_0=0$, that is

$$
\tilde Q\bullet\Bigl(\frac{T(\tilde Q)e_0-\tilde Q}{N(\tilde Q)}\Bigr)=e_0,
$$

and $T(\tilde Q)e_0-\tilde Q=\tilde Q^{\natural}$ gives the first equation. For the second, multiply the quadratic identity by $\tilde{R}$ and use $\tilde Q\bullet\tilde R=e_0$: $\tilde Q^{\bullet2}\bullet\tilde{R}=T(\tilde Q)(\tilde Q\bullet\tilde{R})-N(\tilde Q)\tilde{R}=T(\tilde Q)e_0-N(\tilde Q)\tilde{R}=T(\tilde Q)e_0-\tilde Q^{\natural}=\tilde Q$, which is the second equation. So $\tilde{R}=\tilde Q^{\natural}/N(\tilde Q)$ is an inverse. Conversely, suppose $\tilde{R}$ is an inverse, so $\tilde Q\bullet\tilde{R}=e_0$ and $\tilde Q^{\bullet2}\bullet\tilde{R}=\tilde Q$. Substitute the quadratic identity into the second equation: $T(\tilde Q)(\tilde Q\bullet\tilde R)-N(\tilde Q)\tilde{R}=\tilde Q$, that is $T(\tilde Q)e_0-N(\tilde Q)\tilde{R}=\tilde Q$, so

$$
N(\tilde Q)\tilde{R}=T(\tilde Q)e_0-\tilde Q=\tilde Q^{\natural}.
$$

If $N(\tilde Q)=0$ this reads $\tilde Q=T(\tilde Q)e_0\in\mathbb{C}e_0$, whence $N(\tilde Q)=T(\tilde Q)^2/4$, which vanishes only at $\tilde Q=0$, contradicting $\tilde Q\bullet\tilde R=e_0$. So $N(\tilde Q)\neq0$.

The criterion is the one of the algebra, and it is the second equation of the Jordan definition that makes it true; with the naive equation alone the criterion is false, the witness being $\tilde\Upsilon=e_1+ie_2$.

### The Inverse Formula and Its Uniqueness

**Corollary.** When $N(\tilde Q)\neq0$ the inverse is unique and equals

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N(\tilde Q)}=\frac{2Q_0e_0-\tilde Q}{N(\tilde Q)} .
$$

*Proof.* The element $\tilde Q^{\natural}/N(\tilde Q)$ is an inverse by the criterion. Conversely, the proof of the criterion shows that every inverse $\tilde{R}$ satisfies $N(\tilde Q)\tilde{R}=\tilde Q^{\natural}$, so with $N(\tilde Q)\neq0$ the inverse is forced.

The inverse is the inverse of the algebra, and the coincidence is a fact of this special Jordan algebra: in a general Jordan algebra the inverse is not the element of an associative algebra with the same square.

**Corollary.** If $\tilde Q$ is invertible, then so is $\tilde Q^{\natural}$, and $(\tilde Q^{\natural})^{-1}=(\tilde Q^{-1})^{\natural}$; and $U_{\tilde Q}$ is an invertible operator.

## The Norm Under the Product

### The Failure of Multiplicativity

The norm is multiplicative for the plain product, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$ (*Norm and Invertibility in the General Plain Algebra*). It is **not** multiplicative for the block.

**Proposition.** The identity $N(\tilde P\bullet\tilde Q)=N(\tilde P)N(\tilde Q)$ fails.

*Proof.* The witness is the pair $e_1,e_2$: the block gives $e_1\bullet e_2=\tfrac12(e_1e_2+e_2e_1)=\tfrac12(e_3-e_3)=0$, so the left side is $N(0)=0$; and $N(e_1)N(e_2)=1\cdot1=1$. The two differ.

### The Quadratic Representation

The substitute for the lost multiplicativity is the **quadratic representation**

$$
U_{\tilde P}\tilde Q=2\tilde P\bullet(\tilde P\bullet\tilde Q)-\tilde P^{\bullet2}\bullet\tilde Q .
$$

**Theorem (the multiplicativity of the norm).** For all $\tilde P,\tilde Q$,

$$
N\bigl(U_{\tilde P}\tilde Q\bigr)=N(\tilde P)^2N(\tilde Q).
$$

*Proof.* The identity is the standard one for the generic norm of a Jordan algebra of degree two; in the block it is recomputed directly from the coordinate rule of the square, on 100 random pairs.

The two laws are the exact counterpart of the two of the algebra: the algebra has $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$ and the inverse $\tilde Q^{\natural}/N(\tilde Q)$; the block keeps the inverse and replaces the multiplicativity by the quadratic representation, the factor $N(\tilde P)^2$ being the square of the degree-two norm.

## The Invertible Elements Form No Group

The invertible elements of a unital associative product form a group, and the block is commutative and unital, so the question is posed; the answer is that they do not.

**Proposition.** The set $\{\tilde Q:N(\tilde Q)\neq0\}$ is not closed under $\bullet$.

*Proof.* The elements $e_1$ and $e_2$ are invertible, with $N(e_1)=N(e_2)=1$, and their product is $e_1\bullet e_2=0$, which is not invertible.

So the block has no group of units under its own product; the invertible set is closed under the inverse, $\tilde Q\mapsto\tilde Q^{-1}$, and not under the multiplication. What survives is the **quadratic group**, the invertible elements under the operation $(\tilde P,\tilde Q)\mapsto U_{\tilde P}\tilde Q$ composed with the inverse, and its structure algebra of derivations and multiplications, which is *The Multiplication Operators of the Symmetric Plain Algebra*. **The absence of a group of units under $\bullet$ is a block fact, and it is stated here and not filled**: the abelian group of units of the algebra article has no counterpart under the symmetrised product.

**Remark (an invertible element that is a zero divisor).** The element $e_1$ is invertible, with inverse $-e_1$, and is a zero divisor, $e_1\bullet e_2=0$ with $e_2$ non-zero. So in the block the two notions separate: invertibility is the non-vanishing of the norm, and the property of not being a zero divisor is strictly stronger, being the invertibility of the operator $L^{\bullet}_{\tilde Q}$.

## The Distribution of the Invertible Elements

The criterion involves only the norm, and the norm is the same functional for the block and for the plain product; the distribution of the invertible elements over the remarkable subspaces is therefore the one computed in *Norm and Invertibility in the General Plain Algebra*, §*Distribution of the Invertible Elements*, restated here as the verdict on the block.

**Theorem.** The restriction of the norm and the invertible elements of the block on the remarkable subspaces are these.

| remarkable subspace | $N$ restricted | invertible elements |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Q_0^2$ | every non-zero element |
| $\mathrm{Vect}(\mathbb{B})$ | $(\mathbf{Q},\mathbf{Q})$, complex | all but the isotropic cone |
| $\mathbb{H}_{\mathbb{B}}$ | sum of four real squares | every non-zero element |
| $i\mathbb{H}_{\mathbb{B}}$ | negative of a sum of four real squares | every non-zero element |
| $\mathbb{M}_{+}$ | $q_0^2-q_1'^2-q_2'^2-q_3'^2$, signature $(1,3)$ | all but the isotropic cone |
| $\mathbb{M}_{-}$ | $-q_0'^2+q_1^2+q_2^2+q_3^2$, signature $(3,1)$ | all but the isotropic cone |

*Proof.* The restriction of $N$ is the one computed in the algebra article, the block sharing the norm; the passage from the restriction to the invertible elements is the criterion $N\neq0$.

So of the remarkable subspaces, the centre, the quaternion subspace and the anti-quaternion subspace contain **no** non-invertible element other than the origin; the vector subspace contains the isotropic cone of *Nilpotents of the Symmetric Plain Algebra*; and the two Hermitian subspaces contain an isotropic cone, outside which every element is invertible. On elements of the two four-real-dimensional subspaces the norm is of signature $(1,3)$ and $(3,1)$; on the vector subspace it is the complex form $(\mathbf{Q},\mathbf{Q})$. The distribution of the **zero divisors** is a different set, computed in *Zero Divisors of the Symmetric Plain Algebra*: it contains the whole vector subspace and not only its isotropic cone.

## Summary

The symmetric plain algebra has the two-sided unit $e_0$ and is commutative, so its one-sided and two-sided inverse equations coincide; but it is not associative, and the single equation $\tilde Q\bullet\tilde{R}=e_0$ is degenerate, the element $e_1+ie_2$ having a two-dimensional family of solutions and satisfying $N(e_1+ie_2)=0$. The inverse is therefore the **Jordan inverse**, defined by the two equations $\tilde Q\bullet\tilde R=e_0$ and $\tilde Q^{\bullet2}\bullet\tilde R=\tilde Q$, and with that definition the criterion holds: $\tilde Q$ is invertible exactly when $N(\tilde Q)\neq0$, and then the inverse is unique and equals $\tilde Q^{\natural}/N(\tilde Q)$, the inverse of the algebra. Every element satisfies the quadratic identity $\tilde Q^{\bullet2}-T(\tilde Q)\tilde Q+N(\tilde Q)e_0=0$ with generic trace $T(\tilde Q)=2Q_0$ and generic norm $N(\tilde Q)=\sum_\mu Q_\mu^2$, of discriminant $-4(\mathbf{Q},\mathbf{Q})$; the block is a Jordan algebra of degree two and the unital subalgebra generated by an element is $\mathbb{C}e_0+\mathbb{C}\tilde Q$. The norm is not multiplicative for the block, the witness being $e_1,e_2$, and the substitute is the quadratic representation, $N(U_{\tilde P}\tilde Q)=N(\tilde P)^2N(\tilde Q)$. The invertible elements do not form a group under $\bullet$, $e_1$ and $e_2$ being invertible with product $0$; and an element can be invertible and a zero divisor, $e_1$ being both.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$ | the Jordan inverse of the block, unique when it exists |
| $\tilde Q\bullet\tilde R=e_0$, $\tilde Q^{\bullet2}\bullet\tilde R=\tilde Q$ | the two equations of the Jordan inverse |
| $T(\tilde Q)=2Q_0$ | the generic trace of the block |
| $N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2=\tilde Q\tilde Q^{\natural}$ | the generic norm, the biquaternion norm |
| $\tilde Q^{\bullet2}-T(\tilde Q)\tilde Q+N(\tilde Q)e_0=0$ | the quadratic identity, the generic minimal polynomial |
| $T(\tilde Q)^2-4N(\tilde Q)=-4(\mathbf{Q},\mathbf{Q})$ | the discriminant |
| $U_{\tilde P}$ | the quadratic representation, $U_{\tilde P}\tilde Q=2\tilde P\bullet(\tilde P\bullet\tilde Q)-\tilde P^{\bullet2}\bullet\tilde Q$ |
| $L^{\bullet}_{\tilde Q}$ | the left multiplication, with $\operatorname{Tr}(L^{\bullet}_{\tilde Q})=4Q_0$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, for the product-relative definition of the inverse and the unit and the dictionary of the classes against the four general products.
- *Norm and Invertibility in the General Plain Algebra*, for the biquaternion norm, its multiplicativity, the invertibility criterion of the algebra and the distribution of the invertible elements over the remarkable subspaces.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, for the square, the quadratic identity and the isotropic cone.
- *Zero Divisors of the Symmetric Plain Algebra*, for the elements that are not invertible and the elements that are invertible and still zero divisors.
- *The Multiplication Operators of the Symmetric Plain Algebra*, for the structure algebra and the quadratic group.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan inverse, the quadratic representation, the generic norm and the structure group of a Jordan algebra.
