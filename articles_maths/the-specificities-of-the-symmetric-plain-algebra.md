# __The Specificities of the Symmetric Plain Algebra__

## Introduction

The symmetric plain product is the commutative half of the plain product of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$,

$$
\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P),
$$

the multiplication of *Introduction to the Symmetric Plain Algebra*. It makes the complex space a commutative unital Jordan algebra, and of the twelve structures of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* it is the only one that is a Jordan product. What is specific to the block is the structure a Jordan product carries and an arbitrary commutative product does not: a square that is the plain square, a multiplication operator that is the symmetric half of the two plain multiplications, a quadratic identity of degree two with a generic trace, a generic norm and an inverse, a quadratic representation, and a Peirce theory at the idempotents. Each is an explicit computation on the four coordinates, and each is developed below in the block's own terms.

The block is exact in the opposite sense as well. The Jordan law is weaker than associativity, so the block does not inherit the parent's operator calculus: no non-trivial idempotent gives a projector, a square-zero element gives an operator of index three rather than a square-zero operator, the Peirce decomposition is cubic rather than quadratic, and the invertible elements form no group. Those absences are stated with the theorems they accompany, and §*The Isolation among the Twelve* names the one law from which the theorems and the absences both follow.

**Placement.** The article closes the *Specific Theory* section of the block, after *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, whose element theory it reads as a consequence of the law, and after the Common Theory articles *Norm and Invertibility in the Symmetric Plain Algebra*, *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* and *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*. The trace form of the block is *The Trace Form and the Invariance of the Symmetric Plain Algebra*, its operators are *The Multiplication Operators of the Symmetric Plain Algebra*, and the plain product it symmetrises is *Introduction to the Biquaternion Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$ and central scalar imaginary $i$. An element is $\tilde Q=Q_0e_0+\vec Q$ with $\vec Q=\sum_{k=1}^{3}Q_ke_k$ and $Q_\mu\in\mathbb{C}$, and $(\vec Q,\vec Q)=\sum_kQ_k^2$. The plain product is juxtaposition $\tilde P\tilde Q$; the product of the block is $\bullet$, the symmetrisation above, and $\tilde X^{\bullet2}=\tilde X\bullet\tilde X$. The natural conjugation is $\tilde Q^{\natural}=Q_0e_0-\vec Q$, and the biquaternion norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$. The **left multiplication** of the block is $L^{\bullet}_{\tilde X}:\tilde Y\mapsto\tilde X\bullet\tilde Y$, and $L_{\tilde X},R_{\tilde X}$ without a mark are the plain left and right multiplications. An **idempotent** is an element equal to its square, a **projector** an idempotent operator.

## The Product and Its Square

**Proposition (the shape of the product).** For $\tilde P=P_0e_0+\vec P$ and $\tilde Q=Q_0e_0+\vec Q$,

$$
\tilde P\bullet\tilde Q=\bigl[P_0Q_0-(\vec P,\vec Q)\bigr]e_0+P_0\vec Q+Q_0\vec P.
$$

*Proof.* The plain product is $\tilde P\tilde Q=[P_0Q_0-(\vec P,\vec Q)]e_0+P_0\vec Q+Q_0\vec P+\vec P\times\vec Q$, with $\vec P\times\vec Q$ the cross product of the vector parts; the reverse product carries $-\vec P\times\vec Q$ in its place, and the half-sum is the display.

The block is therefore **the plain product with the cross term dropped**, and the cross term is exactly the antisymmetric part of the plain product.

**Proposition (square, commutativity, unit).** The block is commutative, unital with unit $e_0$, and

$$
\tilde Q\bullet\tilde Q=\tilde Q^2=\bigl[Q_0^2-(\vec Q,\vec Q)\bigr]e_0+2Q_0\vec Q.
$$

*Proof.* Commutativity is read on the shape of the product, and $e_0\bullet\tilde Q=\tfrac12(e_0\tilde Q+\tilde Qe_0)=\tilde Q$. The cross product cancels on the diagonal, $\vec Q\times\vec Q=0$, so $\tilde Q\bullet\tilde Q=\tilde Q\tilde Q$, and the displayed form is the plain square.

**Corollary (the square of the block is the square of the algebra).** Because the antisymmetric part of the plain product is alternating, it vanishes on the diagonal and carries none of the square. **The square of the block and the square of the algebra are the same map**, so the idempotents, the nilpotents, the square roots and the spectrum of the block are those of the algebra, and the generic norm of §*The Degree-Two Structure* is the algebraic norm. The block and the algebra part company at the product and not at the square.

**Proposition (the block is not associative).**

$$
e_1\bullet(e_1\bullet e_2)=0,\qquad (e_1\bullet e_1)\bullet e_2=-e_2 .
$$

*Proof.* $e_1\bullet e_1=e_1^2=-e_0$ and $e_1\bullet e_2=\tfrac12(e_1e_2+e_2e_1)=\tfrac12(e_3-e_3)=0$. The left side is then $e_1\bullet0=0$ and the right side is $(-e_0)\bullet e_2=-e_2$.

**Proposition (polarisation).**

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl((\tilde P+\tilde Q)^{\bullet2}-\tilde P^{\bullet2}-\tilde Q^{\bullet2}\bigr).
$$

*Proof.* The product is $\mathbb{C}$-bilinear and commutative, so the square of a sum expands as the sum of the two squares and twice the product.

So the quadratic map $\tilde Q\mapsto\tilde Q^{\bullet2}$, together with the linear structure, determines the product; the square is the primitive object and the product is its polarisation.

## The Multiplication Operator

**Proposition (the operator is the symmetric half).** For every $\tilde A$,

$$
L^{\bullet}_{\tilde A}=\tfrac12\bigl(L_{\tilde A}+R_{\tilde A}\bigr).
$$

*Proof.* $L^{\bullet}_{\tilde A}\tilde Y=\tilde A\bullet\tilde Y=\tfrac12(\tilde A\tilde Y+\tilde Y\tilde A)=\tfrac12(L_{\tilde A}+R_{\tilde A})\tilde Y$, and the identity of maps follows.

The operator of the block is thus the mean of a plain left and a plain right multiplication, and the two compose with cross terms; this is the exact sense in which the block is a symmetrisation of the parent's operator theory and not a restriction of it.

**Theorem (the operator identity of the block).** The block satisfies

$$
L^{\bullet}_{\tilde X}L^{\bullet}_{\tilde X^{\bullet2}}=L^{\bullet}_{\tilde X^{\bullet2}}L^{\bullet}_{\tilde X}\qquad\text{for every }\tilde X,
$$

equivalently the Jordan identity $(\tilde X^{\bullet2}\bullet\tilde Y)\bullet\tilde X=\tilde X^{\bullet2}\bullet(\tilde Y\bullet\tilde X)$.

*Proof.* The block is the symmetrisation of the associative plain product, so it is Jordan-admissible by *The Symmetric and Antisymmetric Parts of an Algebra Product*; the Jordan identity is that admissibility, and for a commutative product it is equivalent to the operator identity, the two sides being $L^{\bullet}_{\tilde X}L^{\bullet}_{\tilde X^{\bullet2}}\tilde Y$ and $L^{\bullet}_{\tilde X^{\bullet2}}L^{\bullet}_{\tilde X}\tilde Y$ after commutativity is used twice.

**Proposition (the block fails left alternativity).**

$$
e_1\bullet(e_1\bullet e_2)=0\neq-e_2=(e_1\bullet e_1)\bullet e_2 .
$$

*Proof.* From the non-associativity display above. Left alternativity is the demand $L^{\bullet}_{\tilde X}{}^{2}=L^{\bullet}_{\tilde X^{\bullet2}}$ at every element, and this is its failure.

**Corollary (no projector from a non-trivial idempotent).** A non-trivial idempotent $\tilde\Pi$ satisfies $L^{\bullet}_{\tilde\Pi}{}^{2}\neq L^{\bullet}_{\tilde\Pi}$. The unit alone gives a projector, $L^{\bullet}_{e_0}=\mathrm{id}$, and the origin gives the zero operator.

*Proof.* Write the idempotent as $\tilde\Pi=\tfrac12(e_0+\vec q)$ with $\vec q$ a pure root of $+1$, so $\vec q^2=e_0$ and the scalar coordinate of $\vec q$ vanishes; then $L^{\bullet}_{\tilde\Pi}=\tfrac12(\mathrm{id}+L^{\bullet}_{\vec q})$. If $L^{\bullet}_{\tilde\Pi}$ were a projector, squaring and comparing would give $(L^{\bullet}_{\vec q})^{2}=\mathrm{id}$. But for a pure $\vec q$ the square of its operator is $L^{\bullet}_{\vec q}{}^{2}\tilde Y=Y_0-(\vec q,\vec W)\vec q$, which vanishes at every vector $\vec W$ of the two-dimensional complex subspace orthogonal to $\vec q$; such a $\vec W$ is nonzero, so $(L^{\bullet}_{\vec q})^{2}\neq\mathrm{id}$ and $L^{\bullet}_{\tilde\Pi}$ is not a projector.

**Proposition (a square-zero element gives an operator of index three).** For a pure isotropic $\tilde\Upsilon$, that is $Q_0=0$ and $(\vec Q,\vec Q)=0$, the operator $L^{\bullet}_{\tilde\Upsilon}$ satisfies $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$ and $L^{\bullet}_{\tilde\Upsilon}{}^{3}=0$, with image not contained in the kernel; the witness is $\tilde\Upsilon=e_1+ie_2$.

*Proof.* *Square Roots of Zero and the Nilpotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*: the elements of square zero are exactly the pure isotropic vectors, and their left multiplication has the stated index, the image $\mathrm{span}\{e_0,\tilde\Upsilon\}$ not lying in the kernel.

So the block has neither of the two operator constructions of the parent: an idempotent produces no projector and a square-zero element produces no flag. Both failures are the failure of left alternativity, and neither is repaired by any choice of element.

## The Idempotents and the Cubic Peirce Theory

**Proposition (the idempotents of the block).** The idempotents $\tilde\Pi\bullet\tilde\Pi=\tilde\Pi$ are the idempotents of the plain product: the origin, the unit $e_0$, and the elements

$$
\tilde\Pi=\tfrac12(e_0+\vec q),\qquad \vec q\ \text{pure},\ \vec q^2=e_0,
$$

They are read off the quadratic identity at integral trace, $(T,N)=(0,0)$, $(2,1)$ and $(1,0)$, so that the non-trivial idempotents are exactly the isotropic ones.

*Proof.* The square of the block is the plain square, so the equation is $\tilde\Pi^2=\tilde\Pi$, classified in *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*; the quadratic identity of §*The Degree-Two Structure* is then evaluated at the three traces.

**Corollary (the cubic Peirce identity).** For every idempotent $\tilde\Pi$,

$$
L^{\bullet}_{\tilde\Pi}\bigl(2L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)\bigl(L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)=0,
$$

equivalently $2L^{\bullet}_{\tilde\Pi}{}^{3}-3L^{\bullet}_{\tilde\Pi}{}^{2}+L^{\bullet}_{\tilde\Pi}=0$; the eigenvalues of $L^{\bullet}_{\tilde\Pi}$ lie in $\{0,\tfrac12,1\}$.

*Proof.* *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, verified at the witness $\tilde\Pi=\tfrac12(e_0+ie_1)$, whose operator has the eigenvalues $0$, $\tfrac12$ and $1$.

**Corollary (the Jordan Peirce decomposition).** For a non-trivial idempotent,

$$
\mathbb{B}=\mathbb{B}_{1}\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_{0},\qquad
\mathbb{B}_{\lambda}=\{\tilde Y:\tilde\Pi\bullet\tilde Y=\lambda\tilde Y\},
$$

with $\mathbb{B}_1=\mathbb{C}\tilde\Pi$ of dimension one, $\mathbb{B}_0=\mathbb{C}(e_0-\tilde\Pi)$ of dimension one and $\dim\mathbb{B}_{1/2}=2$. At $\tilde\Pi=\tfrac12(e_0+ie_1)$ the three dimensions are $1,2,1$.

*Proof.* *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*; the dimensions are the multiplicities computed there.

This is the Peirce theory of the block, and it is **cubic**: the decomposition is into one middle space, not into a pair of off-diagonal corners. There are no corner subalgebras, the complementary idempotent $e_0-\tilde\Pi$ contributes the line $\mathbb{B}_0$ and not a second central piece, and the middle space is a single two-dimensional space carrying no product of its own. The quadratic Peirce calculus is the parent's, and it is not available here.

## The Degree-Two Structure

**Theorem (the quadratic identity).** Every element satisfies

$$
\tilde Q^{\bullet2}-T(\tilde Q)\tilde Q+\langle\tilde Q\rangle_{\natural}e_0=0,\qquad
T(\tilde Q)=2Q_0,\qquad \langle\tilde Q\rangle_{\natural}=\sum_{\mu=0}^{3}Q_\mu^2 .
$$

*Proof.* On the square of §*The Product and Its Square* and $T(\tilde Q)\tilde Q=2Q_0^2e_0+2Q_0\vec Q$, the difference is $\bigl(Q_0^2-(\vec Q,\vec Q)-2Q_0^2+\langle\tilde Q\rangle_{\natural}\bigr)e_0$, and the coefficient vanishes because $\langle\tilde Q\rangle_{\natural}=Q_0^2+(\vec Q,\vec Q)$.

The functional $T$ is the **generic trace** of the block and $\langle\cdot\rangle_{\natural}$ its **generic norm**; the identity is the generic minimal polynomial, **of degree two**, so the block is a Jordan algebra of degree two. The discriminant is

$$
T(\tilde Q)^2-4\langle\tilde Q\rangle_{\natural}=-4(\vec Q,\vec Q),
$$

which vanishes exactly on the isotropic cone of the vector part; there the two generic roots coincide, and the element $e_1+ie_2$ is the witness with a nonzero vector part.

**Theorem (the inverse).** An element with $\langle\tilde Q\rangle_{\natural}\neq0$ is invertible in the Jordan sense, with

$$
\tilde Q^{-1}=\frac{2Q_0e_0-\tilde Q}{\langle\tilde Q\rangle_{\natural}}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}},
$$

which is the inverse of the algebra; the invertibility criterion is $\langle\tilde Q\rangle_{\natural}\neq0$.

*Proof.* Dividing the quadratic identity by $\langle\tilde Q\rangle_{\natural}$ exhibits $(T(\tilde Q)e_0-\tilde Q)/\langle\tilde Q\rangle_{\natural}$ as a Jordan inverse, and $T(\tilde Q)e_0-\tilde Q=2Q_0e_0-\tilde Q=\tilde Q^{\natural}$; the formula of the associative inverse is *Norm and Invertibility in the General Quaternionic Algebra*.

**Theorem (the quadratic representation).** For $U_{\tilde P}\tilde Q=2(\tilde P\bullet\tilde Q)\bullet\tilde P-\tilde P^{\bullet2}\bullet\tilde Q$,

$$
N\bigl(U_{\tilde P}\tilde Q\bigr)=\langle\tilde P\rangle_{\natural}^2\langle\tilde Q\rangle_{\natural},
$$

while $\langle\cdot\rangle_{\natural}$ itself is not multiplicative, $\langle\tilde P\bullet\tilde Q\rangle_{\natural}\neq \langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$ in general.

*Proof.* *Norm and Invertibility in the Symmetric Plain Algebra*, where the failure of multiplicativity and its replacement by the quadratic representation are proved on the coordinates.

**Corollary (the block is not a division Jordan algebra).** The isotropic cone $\{\langle\tilde Q\rangle_{\natural}=0\}$ is the union of the origin and the zero-divisor cone of the algebra, so the norm form is **non-degenerate but isotropic**, of realified signature $(4,4)$; it is the Hermitian form, and not the norm form, that is definite. The elements of square zero are the **pure** isotropic vectors, a proper subset of the cone, and $e_0+ie_1$ separates the two notions: $\langle e_0+ie_1\rangle_{\natural}=0$ while $(e_0+ie_1)^{\bullet2}=2e_0+2ie_1\neq0$.

*Proof.* *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, where the cone, the signature and the separation are computed.

## What the Block Does Not Inherit

Three things the parent product has are absent, and the absences belong to the block's description as much as its theorems.

- **No projector calculus.** A non-trivial idempotent does not give a projector (§*The Multiplication Operator*), so there is no image–kernel splitting of the type $\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B}$ and no ideal generated by an idempotent. The unit gives the identity operator and the origin the zero operator, and those are the only projectors produced by idempotents.
- **No associative Peirce calculus.** The Peirce theory is the cubic one of §*The Idempotents and the Cubic Peirce Theory*: one middle space, no corners, no matrix units, and no module theory over the algebra. The element theory of the block — the generic trace and norm, the inverse, the quadratic representation — is the substitute, and it is a different subject.
- **No group of units.** The invertible elements are not closed under $\bullet$: the pair $e_1,e_2$ is invertible, $\langle e_1\rangle_{\natural}=\langle e_2\rangle_{\natural}=1$, with product $e_1\bullet e_2=0$. The block also has its own zero-divisor set, strictly larger than the algebra's isotropic cone, and it is **not** the complement of the invertible elements: $e_1$ is a zero divisor, $e_1\bullet e_2=0$, and yet is invertible. The criterion $\det L^{\bullet}_{\tilde Q}=Q_0^2\langle\tilde Q\rangle_{\natural}=0$ is *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, and it separates the two notions.

## The Isolation among the Twelve

One law separates the block from the other eleven structures, and it is stated here to close the article, not to enumerate them. The block is **commutative** and satisfies the **Jordan identity**, equivalently the operator identity of §*The Multiplication Operator*; a commutative product with the Jordan identity is a **Jordan product**, and the block is the only Jordan product of the twelve.

**Theorem.** Of the twelve structures of *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, the symmetric plain product is the only one that is commutative and satisfies the Jordan identity.

*Proof.* The twelve are generated from the plain product by twisting a slot with a conjugation or by (anti)symmetrising, and each of the three operations destroys at least one clause of the criterion. The four general products are non-commutative, the four antisymmetric parts are non-commutative, the symmetric quaternionic product is commutative but fails the identity, and the two symmetric sesquilinear products are only conjugate-commutative and fail the identity. The block is commutative by construction and satisfies the identity by Jordan-admissibility, so it alone meets both clauses.

| structure | commutative | Jordan identity | witness of the failure |
|---|---|---|---|
| GPA | no | yes (associative) | $e_1e_2=e_3$ against $e_2e_1=-e_3$ |
| SPA | **yes** | **yes** | — (the criterion) |
| APA | no | yes (vacuous) | $e_1\wedge e_2=e_3$ against $e_2\wedge e_1=-e_3$ |
| GQA | no | yes | $e_0\circ e_1=e_1$ against $e_1\circ e_0=-e_1$ |
| SQA | yes | no | $(x^{\circ2}\circ x)\circ x=0$ against $x^{\circ2}\circ(x\circ x)=e_0$ |
| AQA | no | yes (vacuous) | $e_0\circ e_1=e_1$ against $e_1\circ e_0=-e_1$ |
| GPS | no | no | $e_0\circ e_1=-e_1$ against $e_1\circ e_0=e_1$ |
| SPS | conjugate | no | $(x^{\circ2}\circ x)\circ x=0$ against $x^{\circ2}\circ(x\circ x)=e_0$ |
| APS | no | no | $e_0\circ e_1=-e_1$ against $e_1\circ e_0=e_1$ |
| GQS | no | no | $e_0\circ ie_1=ie_1$ against $ie_1\circ e_0=-ie_1$ |
| SQS | conjugate | no | $(x^{\circ2}\circ x)\circ x=-e_0$ against $x^{\circ2}\circ(x\circ x)=e_0$ |
| AQS | no | no | $e_1\circ e_2=e_3$ against $e_2\circ e_1=-e_3$ |

Two fine points, kept because they are about the law and not about the list. The Jordan identity **alone** does not isolate the block: it holds at every element of the associative general plain product, at every element of the general quaternionic product, whose square is central, and vacuously at every element of the two alternating antisymmetrisations. What excludes those four is the **commutativity** clause, and it is the conjunction that the definition names. So the correct exclusive statement is that no other structure is a Jordan product, and not that no other structure satisfies the identity.

## Summary

The symmetric plain product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ is the plain product with the cross term dropped, $\tilde P\bullet\tilde Q=[P_0Q_0-(\vec P,\vec Q)]e_0+P_0\vec Q+Q_0\vec P$, commutative and unital, with the plain square, $\tilde Q^{\bullet2}=[Q_0^2-(\vec Q,\vec Q)]e_0+2Q_0\vec Q$. Its multiplication operator is the symmetric half $L^{\bullet}_{\tilde A}=\tfrac12(L_{\tilde A}+R_{\tilde A})$ of the two plain multiplications, and it satisfies the operator identity $L^{\bullet}_{\tilde X}L^{\bullet}_{\tilde X^{\bullet2}}=L^{\bullet}_{\tilde X^{\bullet2}}L^{\bullet}_{\tilde X}$, equivalent to the Jordan identity. The block fails left alternativity at $e_1,e_2$, and therefore yields no projector from a non-trivial idempotent and no flag from a square-zero element, whose operator has index three instead. Its idempotents are $0$, $e_0$ and the isotropic $\tfrac12(e_0+\vec q)$ with $\vec q$ a pure root of $+1$; at a non-trivial idempotent the operator obeys the cubic Peirce identity with eigenvalues $0,\tfrac12,1$ and the space splits as $\mathbb{C}\tilde\Pi\oplus\mathbb{B}_{1/2}\oplus\mathbb{C}(e_0-\tilde\Pi)$ with dimensions $1,2,1$. The block is of degree two: every element satisfies $\tilde Q^{\bullet2}-T(\tilde Q)\tilde Q+\langle\tilde Q\rangle_{\natural}e_0=0$ with $T=2Q_0$ and $\langle\cdot\rangle_{\natural}=\sum_\mu Q_\mu^2$, its inverse is $\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$, its norm obeys $\langle U_{\tilde P}\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}^2\langle\tilde Q\rangle_{\natural}$ though it is not multiplicative, and the isotropic cone makes it a non-division Jordan algebra with pure isotropic elements of square zero proper inside the cone. The block inherits none of the parent's projector calculus, associative Peirce calculus or group of units, and its zero-divisor set is larger than the non-invertible elements. Of the twelve structures it is the only Jordan product, the four general and four antisymmetric products failing by non-commutativity, the symmetric quaternionic product by the identity, and the two symmetric sesquilinear products by both clauses read in the conjugate sense.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\bullet$ | the symmetric plain product, the block's multiplication |
| $\tilde P\bullet\tilde Q=[P_0Q_0-(\vec P,\vec Q)]e_0+P_0\vec Q+Q_0\vec P$ | the shape of the product |
| $\tilde Q^{\bullet2}=\tilde Q^2$ | the square, the plain square |
| $L^{\bullet}_{\tilde A}=\tfrac12(L_{\tilde A}+R_{\tilde A})$ | the multiplication operator of the block |
| $L^{\bullet}_{\tilde X}L^{\bullet}_{\tilde X^{\bullet2}}=L^{\bullet}_{\tilde X^{\bullet2}}L^{\bullet}_{\tilde X}$ | the operator identity, equivalent to the Jordan identity |
| $\tfrac12(e_0+\vec q)$, $\vec q^2=e_0$ pure | the non-trivial idempotents |
| $L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$ | the cubic Peirce identity, eigenvalues $0,\tfrac12,1$ |
| $\mathbb{B}_1\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_0$ | the Jordan Peirce decomposition, dimensions $1,2,1$ |
| $T(\tilde Q)=2Q_0$, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the generic trace and the generic norm |
| $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$ | the Jordan inverse, the algebra inverse |
| $\{\langle\tilde Q\rangle_{\natural}=0\}$ | the isotropic cone, the origin and the zero-divisor cone |
| $\mathrm{GPA}\dots\mathrm{AQS}$ | the twelve structures, coded as in *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan identity, the operator identity, the cubic Peirce identity and the degree-two theory.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the left and the right multiplications and the alternative laws.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.md`), for the element theory the law delivers.
- *The Multiplication Operators of the Symmetric Plain Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-algebra.md`), for the operators, the derivations and the structure algebra.
- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the Jordan-admissibility of an associative algebra.
- *The Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the twelve operations and the isolation table.
