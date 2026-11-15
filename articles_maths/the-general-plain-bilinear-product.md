# __The General Plain Bilinear Product__

## Introduction

The underlying complex vector space of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, obtained by reading each slot of a pair as it stands or through a conjugation. This article reads the first of them alone: the **general plain bilinear product** $\tilde Q_1\tilde Q_2$, in which neither slot is conjugated. The rule is the multiplication of the algebra and nothing else, and it is the one product of the four that makes $\mathbb{B}$ an associative algebra with unit over $\mathbb{C}$.

The article is organised along the product and not along the family: the coordinate rule and the scalar–vector form, the laws it keeps and the one it loses, the units, the image and the diagonal, the two halves and the four composites they generate, the trace form read against the halves, and the row of the product in the comparison of the four.

The coordinate basis is $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $e_t$ the identity, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclically, so that $\vec e_y\vec e_x=-\vec e_z$. An element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, the scalar part is $\langle\tilde Q\rangle_{*}=Q_t$, and $\mathrm{Sc}$ and $\mathrm{Vec}$ are the two projections. The three conjugations are the coefficientwise $\overline{\tilde Q}$, the quaternion involution ${}^{\natural}$ fixing $e_t$ and negating the $\vec e_k$, and the Hermitian ${}^{*}={}^{\natural}\circ\overline{\phantom{x}}$. The pairings are the complex bilinear dot product $(\vec Q_1,\vec Q_2)=\sum_k Q_{1k}Q_{2k}$ and the complex bilinear cross product $\vec Q_1\times\vec Q_2$.

The comparison of the four is [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html); the twelve operations are [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html); the vector halves are [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html); the forms are [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html). The algebra, the element and the four conjugations are [The Biquaternion Algebra](the-biquaternion-algebra.html).

## The Split of a Space and the Split of a Product

Two splits are used throughout the twelve articles, and they are different in kind. The first is a split of the **space** by an involution; the second is a split of a **product** by the exchange of its arguments. They give the counts $2$ and $12$, and confusing them is the one error the notation invites.

**The split of the space.** The quaternion involution ${}^{\natural}$ is $\mathbb{C}$-linear, of order two, and an anti-automorphism. Its eigenspaces are the centre $\mathbb{B}_{C}=\mathbb{C}e_t$, of complex dimension $1$, and the vector subspace $\mathbb{B}_{V}=\mathbb{C}\vec e_x\oplus\mathbb{C}\vec e_y\oplus\mathbb{C}\vec e_z$, of complex dimension $3$,
$$
\mathbb{B}=\mathbb{B}_{C}\oplus\mathbb{B}_{V},\qquad
\tilde Q=\tfrac12(\tilde Q+\tilde Q^{\natural})+\tfrac12(\tilde Q-\tilde Q^{\natural})=Q_te_t+\vec Q .
$$
The Hermitian involution ${}^{*}$ is conjugate-linear instead, and its fixed sets $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are real subspaces of real dimension $4$, not complex ones. A conjugate-linear involution does not split a complex space into complex lines, and the two cases are not parallel.

**The split of the product.** The exchange of a product is a second involution, acting on the space of binary operations and not on $\mathbb{B}$. For the two $\mathbb{C}$-bilinear products it is the interchange of the arguments, and for the two sesquilinear products it is the interchange followed by the coefficientwise conjugation of the value. Applied to a product $f$ it returns the symmetric part $f^{\mathrm{s}}$ and the antisymmetric part $f^{\mathrm{a}}$, and the reconstruction $f=f^{\mathrm{s}}+f^{\mathrm{a}}$ is the only relation needed.

**Proposition (the two counts).** The involution ${}^{\natural}$ produces two summands. Each of the four general products produces two halves, and each half is again a product of the class of its parent, so the space carries $4\cdot 3=12$ products: the four general products and their eight halves.

*Proof.* The first count is the dimension count of the eigenspaces above, $1+3=4$. The second is the closure of the class under the exchange, proved in [The Symmetric and Antisymmetric Parts of an Algebra Product](the-symmetric-and-antisymmetric-parts-of-an-algebra-product.html) for the bilinear case and in [The Symmetric and Antisymmetric Parts of a Sesqualgebra Product](the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.html) for the sesquilinear one; it is verified on the twelve coordinate rules of the decomposition article.

**Remark (why the two must not be confused).** The split of the space is one involution acting on one space, and its count is fixed at two. The split of the product runs over four products and is governed by the class of each, and its count is twelve. A subspace of $\mathbb{B}$ is an eigenspace of ${}^{\natural}$ or of ${}^{*}$; a half of a product is an operation on $\mathbb{B}$, not a subspace of it.

## The Product and Its Coordinate Rule

**Definition.** The **general plain bilinear product** multiplies the coordinates on the basis,
$$
\tilde Q_1\tilde Q_2=\sum_{\mu}\sum_{\nu}Q_{1\mu}Q_{2\nu}\,e_\mu e_\nu ,
$$
the indices running over $\{t,x,y,z\}$.

**Proposition (the coordinate rule).** For all $\tilde Q_1,\tilde Q_2$,
$$
\tilde Q_1\tilde Q_2=\bigl(Q_{1t}Q_{2t}-Q_{1x}Q_{2x}-Q_{1y}Q_{2y}-Q_{1z}Q_{2z}\bigr)
+\bigl(Q_{1t}Q_{2x}+Q_{1x}Q_{2t}+Q_{1y}Q_{2z}-Q_{1z}Q_{2y}\bigr)\vec e_x
+\bigl(Q_{1t}Q_{2y}-Q_{1x}Q_{2z}+Q_{1y}Q_{2t}+Q_{1z}Q_{2x}\bigr)\vec e_y
+\bigl(Q_{1t}Q_{2z}+Q_{1x}Q_{2y}-Q_{1y}Q_{2x}+Q_{1z}Q_{2t}\bigr)\vec e_z .
$$

*Proof.* The four products of units are $e_te_\mu=e_\mu e_t=e_\mu$, $\vec e_x\vec e_x=\vec e_y\vec e_y=\vec e_z\vec e_z=-e_t$, and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ with the reversed products negated. Collecting the coefficients of each unit gives the display. Verified exactly on the sixteen pairs of the basis and on general elements with coefficients in $\mathbb{Q}(i)$.

The rule is linear in the four coordinates of $\tilde Q_1$ and linear in the four coordinates of $\tilde Q_2$. The sixteen structure constants $c_{\mu\nu}{}^{\lambda}$, defined by $e_\mu e_\nu=\sum_\lambda c_{\mu\nu}{}^{\lambda}e_\lambda$, are integers, and they are the structure constants of the real quaternion algebra read on the complexification.

## The Scalar–Vector Form

Adding and subtracting the ranks of the two factors gives the compact form.

**Theorem (the scalar–vector form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\tilde Q_2=\bigl(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr)+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2\;}
$$

*Proof.* In the coordinate rule, the coefficient of $e_t$ is the sum of the four products with the three vector signs negative, that is $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$. The coefficient of $\vec e_x$ has the two diagonal terms $Q_{1t}Q_{2x}+Q_{1x}Q_{2t}$ plus $Q_{1y}Q_{2z}-Q_{1z}Q_{2y}$, which is the $\vec e_x$-coordinate of $\vec Q_1\times\vec Q_2$; the other two coordinates are the same computation. Computed exactly on general elements.

The scalar part is $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\sum_{\mu}\varepsilon_\mu Q_{1\mu}Q_{2\mu}$ with $\varepsilon=(1,-1,-1,-1)$, and the vector part is the two mixed terms and the cross term. Three readings follow at once.

**Remark (the three pieces).** The scalar part is the **plain form** $P(\tilde Q_1,\tilde Q_2)$, a symmetric $\mathbb{C}$-bilinear form of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and rank $4$, read with its hyperbolic basis and its index in [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html). The mixed part $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ is symmetric in the two factors. The cross term $\vec Q_1\times\vec Q_2$ is the only piece that changes sign under the interchange, and it is the whole of the antisymmetric part.

## The Laws It Keeps and the Laws It Loses

**Theorem (associativity).** The product is associative,
$$
(\tilde Q_1\tilde Q_2)\tilde Q_3=\tilde Q_1(\tilde Q_2\tilde Q_3)
$$
for all $\tilde Q_1,\tilde Q_2,\tilde Q_3\in\mathbb{B}$.

*Proof.* On the basis the product is the quaternion product, which is associative, and the complex bilinear extension of an associative product is associative. The identity was also verified on all sixty-four triples of the basis and on general elements of $\mathbb{Q}(i)$; the maximal deviation is zero.

**Corollary (flexibility, alternation, degree three).** The product is flexible, $\tilde Q_1(\tilde Q_2\tilde Q_1)=(\tilde Q_1\tilde Q_2)\tilde Q_1$; it is left and right alternative, $\tilde Q_1(\tilde Q_1\tilde Q_2)=(\tilde Q_1\tilde Q_1)\tilde Q_2$ and $(\tilde Q_1\tilde Q_2)\tilde Q_2=\tilde Q_1(\tilde Q_2\tilde Q_2)$; it satisfies the degree-three identity $\tilde Q_1(\tilde Q_1\tilde Q_1)=(\tilde Q_1\tilde Q_1)\tilde Q_1$; and it is power associative.

*Proof.* Each identity is a rearrangement of a product of three or four factors in an associative algebra, and each is obtained from associativity by inserting brackets. The ladder of implications is [Non-Associative Algebras and the Property Ladder](non-associative-algebras-and-the-property-ladder.html); the verification here is on the sixty-four and the two hundred fifty-six basis instances, all exact.

**Proposition (the law that fails).** The product is not commutative.

*Proof.* $\vec e_x\vec e_y=\vec e_z$ while $\vec e_y\vec e_x=-\vec e_z$, and the two values differ. The defect of commutativity is the cross term, and it is measured by $\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1=2\,\vec Q_1\times\vec Q_2$, which is the antisymmetrisation of the next sections.

**Remark (the shape of the four laws).** Associativity, flexibility, alternation and the degree-three identity hold together, and commutativity fails alone. This is the pattern of a unital associative algebra that is not commutative, and it is why the element theory, the idempotents, the nilpotents and the zero divisors, is read on this product and not on its halves. Of the four general products it is the only one for which the whole ladder holds.

## The One-Sided Units

**Proposition (the two-sided unit).** The element $e_t$ is a two-sided identity, $e_t\tilde Q=\tilde Qe_t=\tilde Q$ for every $\tilde Q$.

*Proof.* $e_t$ is the identity of the quaternion product and the complex bilinear extension keeps it.

**Theorem (uniqueness).** The identity is unique: if $\tilde U\tilde Q=\tilde Q$ for all $\tilde Q$ then $\tilde U=e_t$, and the same holds on the right.

*Proof.* Put $\tilde Q=e_t$: a left unit satisfies $\tilde Ue_t=e_t$, and $\tilde Ue_t=\tilde U$, so $\tilde U=e_t$. The right side is the same computation. The linear system for a left unit, sixteen equations in four unknowns, has the unique solution $(1,0,0,0)$ and no residual.

**Remark (the pattern, and the check behind it).** The three other products have $e_t$ on the left alone, on the right alone, and on neither side. Each of the eight linear systems, two sides to a product, was solved here and has the residual zero exactly where the pattern says; the solution is unique wherever it exists.

## The Image, the Diagonal and the Scalar Part

**Proposition (the image is the whole space).** The image of the product is $\mathbb{B}$, of complex dimension $4$.

*Proof.* $e_te_t=e_t$, $e_t\vec e_x=\vec e_x$, $e_t\vec e_y=\vec e_y$ and $e_t\vec e_z=\vec e_z$ are four values that span the space. The span of the sixteen products of basis elements has dimension $4$, computed exactly.

**Proposition (the diagonal is the square).** The diagonal map $\tilde Q\mapsto\tilde Q\tilde Q=\tilde Q^2$ has image $\mathbb{B}$, and it is homogeneous of degree two,
$$
\tilde Q^2=\bigl(Q_t^2-(\vec Q,\vec Q)\bigr)+2Q_t\vec Q .
$$

*Proof.* The scalar–vector form at the two equal arguments, with $\vec Q\times\vec Q=0$. The image is four-dimensional: the squares $\vec e_x^2=-e_t$, $(\vec e_x+\vec e_y)^2=-2e_t+2\vec e_z$, $(\vec e_x+i\vec e_y)^2=-2e_t+2i\vec e_z$ and $(\tilde Q)^2$ for a general element span $\mathbb{B}$, computed exactly.

**Remark (what the diagonal sees).** The square sees the symmetric half alone,
$$
(\tilde Q_1+\tilde Q_2)^2-\tilde Q_1^2-\tilde Q_2^2=2\,\tilde Q_1\bullet\tilde Q_2,
$$
because the antisymmetric half is alternating and cancels on the diagonal. The antisymmetric half is therefore invisible to every power map and is recovered from the product only through the commutator. The consequence for the block is The Specificities of the Symmetric Plain Algebra of the Biquaternions, where the identity of the two squares is the first of the specificities.

**The scalar part.** The scalar part of the product is the form $P$, with Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and rank $4$. It is symmetric and nondegenerate, its radical is zero, and its isotropic cone is $\langle\tilde Q\rangle_{P}=Q_t^2-Q_x^2-Q_y^2-Q_z^2=0$.

## The Two Halves of This Product

**Definition.** The **symmetric plain product** and the **antisymmetric plain product** are the two halves of the product under the interchange of the arguments,
$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr),\qquad
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr).
$$

**Theorem (the reconstruction and the two forms).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\tilde Q_2=\tilde Q_1\bullet\tilde Q_2+\tilde Q_1\wedge\tilde Q_2\;},
$$
$$
\tilde Q_1\bullet\tilde Q_2=\bigl(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr)+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1,\qquad
\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2 .
$$

*Proof.* Adding and subtracting the two orders of the product, whose scalar parts and mixed terms agree and whose cross terms are opposite. The reconstruction is the sum of the two displays. Verified on general elements.

**Remark (the two halves are of different kinds).** The symmetrisation is commutative and unital, with $e_t$ on both sides, and satisfies the Jordan identity; it is the only one of the four symmetrisations that does. The antisymmetrisation is alternating, has zero diagonal, has no unit, and satisfies the Jacobi identity; it is the only one of the four antisymmetrisations that does. The two are read in [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html) and [The Lie Structure of the Antisymmetric Plain Product](the-lie-structure-of-the-antisymmetric-plain-product.html).

**Corollary (the alternation of the second half).** $\tilde Q\wedge\tilde Q=0$ and $\tilde Q_1\wedge\tilde Q_2=-\tilde Q_2\wedge\tilde Q_1$. The second half is therefore not a product with a diagonal: every square in it vanishes, and it carries no idempotent, no norm and no inverse.

## The Four Composites

The two halves can be composed with one another, and the four composites carry a table that is the same in shape for the four families.

**Definition.** The four **composites** of the family are the operations
$$
ss(x,y,z)=s\bigl(s(x,y),z\bigr),\quad sa(x,y,z)=s\bigl(a(x,y),z\bigr),\quad as(x,y,z)=a\bigl(s(x,y),z\bigr),\quad aa(x,y,z)=a\bigl(a(x,y),z\bigr),
$$
with $s$ and $a$ the two halves.

**Theorem (the table of the composites).** For the plain family the images and the scalar parts are

| composite | image, complex dimension | scalar part |
|---|---|---|
| $ss$ | $4$ | present |
| $sa$ | $4$ | present |
| $as$ | $3$ | zero |
| $aa$ | $3$ | zero |

and the two composites whose outer operation is the antisymmetrisation have image $\mathbb{B}_{V}$.

*Proof.* $s(\tilde Q_1,\tilde Q_2)$ has the scalar part $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ and the vector part $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$; multiplying it by $\tilde Q_3$ by $s$ or by $a$ keeps the scalar part in the first case and kills it in the second, since $a$ is alternating. The dimension count is the span of the values over all triples of the complex basis $\{e_\mu,ie_\mu\}$, computed exactly: $4,4,3,3$.

**Remark (the discriminator).** The scalar part separates the two rows: an outer symmetrisation keeps a scalar part, an outer antisymmetrisation has none. The inner operation separates the entries of a row: a family with a central symmetric part carries a one-dimensional image into the composite, and the dimension falls from $4$ to $1$. The twelve-row table is [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

**Corollary (the composites never leave the vector subspace).** The two antisymmetrised composites $as$ and $aa$ take their values in $\mathbb{B}_{V}$: applied twice in the antisymmetric slot, the operation cannot produce a scalar part.

## The Trace Form and the Halves

**Definition.** The **trace form** of a family is the scalar part of its product read as a form, $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2\bigr)$. For the plain family it is the form $P$.

**Proposition (the cross term survives here).** There are $\tilde Q_1,\tilde Q_2,\tilde Q_3,\tilde Q_4$ with
$$
\mathrm{Sc}\bigl(\tilde Q_1\bullet\tilde Q_2\;\cdot\;\tilde Q_3\wedge\tilde Q_4\bigr)\neq0 .
$$

*Proof.* Take $\tilde Q_1=e_t$, $\tilde Q_2=\vec e_x$, $\tilde Q_3=\vec e_y$, $\tilde Q_4=\vec e_z$. Then $\tilde Q_1\bullet\tilde Q_2=\vec e_x$ and $\tilde Q_3\wedge\tilde Q_4=\vec e_x$, so the product is $\vec e_x^2=-e_t$ and the scalar part is $-1$. Verified exactly.

**Theorem (the failure of the split of the form).** Since the cross term survives, the form does not split over the halves:
$$
\tau(\tilde Q_1,\tilde Q_2)=\tau\bigl(s(\tilde Q_1,\tilde Q_2),s(\tilde Q_1,\tilde Q_2)\bigr)+2\,\tau\bigl(s(\tilde Q_1,\tilde Q_2),a(\tilde Q_1,\tilde Q_2)\bigr)+\tau\bigl(a(\tilde Q_1,\tilde Q_2),a(\tilde Q_1,\tilde Q_2)\bigr),
$$
and the middle term is not zero in general. On a **single pair** the middle term does vanish, $\mathrm{Sc}\bigl(s(x,y)\,a(x,y)\bigr)=0$ for all $x,y$, and the split holds there; the failure appears only when the two halves are evaluated on different pairs.

*Proof.* The expansion of $\tau$ on the decomposition $f=s+a$ is the bilinearity of $\tau$ and of the product. The single-pair vanishing was verified on the basis and on random pairs, the four-argument value on the witness above.

**Remark (which families are orthogonal).** The four-argument vanishing of $\tau(s,a)$ holds for the general quaternionic bilinear product and for the general plain sesquilinear product, and for those two the split of the form is exact. It fails for the plain product and for the general quaternionic sesquilinear product. The reason is the same in both cases: the vanishing needs one of the two halves to be central, which happens only for the two central symmetrisations.

## The Place among the Four

| | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
|---|---|---|---|---|
| class | $\mathbb{C}$-bilinear | $\mathbb{C}$-bilinear | sesquilinear | sesquilinear |
| associative | yes | no | no | no |
| unit | $e_t$, both sides | $e_t$, left | $e_t$, right | none |
| image | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ | $\mathbb{B}$ |
| diagonal image | $\mathbb{B}$ | $\mathbb{B}_{C}$ | $\mathbb{B}_{\Psi}$ | $\mathbb{B}$ |
| trace form | $P$, rank $4$ | $N$, rank $4$ | $H$, rank $4$ | $K$, rank $4$ |
| $\tau(s,a)=0$ for all arguments | no | yes | yes | no |
| Jacobi defect of the bracket | $0$ | $3$ | $3$ | $3$ |
| Jordan defect of the symmetrisation | $0$ | $1$ | $1$ | $4$ |

**Remark (the two rows that are this product's own).** The plain product is the only column with yes in the associativity row, the only column with a two-sided unit, and the only column whose two defects vanish. These three facts are one: associativity. The three other columns read the same multiplication through a conjugation in one or both slots; each insertion destroys associativity, restricts or removes the unit, and leaves a defect in one of the two identities of the halves.

The product is read as a multiplication in its own right in [The Biquaternion Algebra](the-biquaternion-algebra.html), and its element theory, the idempotents, the nilpotents and the zero divisors, is the element theory of the algebra. Its two halves are the subjects of the two companion articles of this block.

## Summary

The general plain bilinear product of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the multiplication of the algebra, $\tilde Q_1\tilde Q_2=[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$, with structure constants the structure constants of the quaternion algebra read on the complexification. It is $\mathbb{C}$-bilinear, associative, flexible, alternative, power associative and of degree three, and it is not commutative; its failure of commutativity is exactly the cross term. The unit $e_t$ is two-sided and unique.

The image of the product is the whole space, the image of the diagonal is the whole space, and the diagonal is the square, $\tilde Q^2=(Q_t^2-(\vec Q,\vec Q))+2Q_t\vec Q$. The scalar part is the form $P$ of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ and rank $4$.

The product splits into the symmetrisation $\tilde Q_1\bullet\tilde Q_2$, the plain product with the cross term dropped, and the antisymmetrisation $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$, and the two halves are a Jordan product and a Lie bracket respectively, the only ones of their kinds in the batch. The four composites have images of dimensions $4,4,3,3$, the two antisymmetrised ones landing in the vector subspace, and the scalar part is the discriminator between the rows.

The trace form $P$ does not split over the halves: the cross term $\mathrm{Sc}(s\,a)$ survives, with the witness $x=e_t$, $y=\vec e_x$, $u=\vec e_y$, $v=\vec e_z$ giving $-1$. On a single pair it vanishes, so the failure is a failure of the four-argument orthogonality and not of the split at the equal pairs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the coefficient basis, $e_t$ the identity, $\vec e_k^{2}=-e_t$ |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\tilde Q_2$ | the general plain bilinear product |
| $\mathrm{Sc}$, $\mathrm{Vec}$ | the scalar part and the vector part of an element |
| $(\vec Q_1,\vec Q_2)$, $\vec Q_1\times\vec Q_2$ | the complex bilinear dot product and cross product |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the plain product |
| $\tilde Q_1\bullet\tilde Q_2$ | the symmetric plain product, the symmetrisation |
| $\tilde Q_1\wedge\tilde Q_2$ | the antisymmetric plain product, the antisymmetrisation |
| $s$, $a$ | the two halves of a product |
| $ss,sa,as,aa$ | the four composites of a family |
| $P(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | the plain form, the scalar part of the product |
| $\mathbb{B}_{C}$, $\mathbb{B}_{V}$ | the centre and the vector subspace |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | the Hermitian and anti-Hermitian subspaces |

## Further Reading

- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products, the identities that link them and the comparison.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve products of the space and the table of the halves.
- [The Vector Parts of the Products over the Biquaternion Algebra](the-vector-parts-of-the-products-over-the-biquaternion-algebra.html), for the vector halves and the two-bit rule.
- [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html) and [The Lie Structure of the Antisymmetric Plain Product](the-lie-structure-of-the-antisymmetric-plain-product.html), for the two halves of this product read as algebras.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, the basis and the four conjugations.
- [Non-Associative Algebras and the Property Ladder](non-associative-algebras-and-the-property-ladder.html), for the laws tested above and their implications.
