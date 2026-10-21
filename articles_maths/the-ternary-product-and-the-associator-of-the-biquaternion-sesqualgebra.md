
# __The Ternary Product and the Associator of the Biquaternion Sesqualgebra__

## Introduction

The multiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ of *Introduction to the General Plain Sesqualgebra* is neither associative nor commutative, and the object that measures the failure of associativity is the **associator**

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_4]=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4-\tilde Q_1\star(\tilde Q_2\star\tilde Q_4) .
$$

On $\mathbb{B}$ it reads

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_4]=\tilde Q_1\bigl(\tilde Q_2^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q_2^{*}\bigr) ,
$$

a difference of two groupings of the associative product, and it is nonzero as soon as the involution is nontrivial. The operation that carries a structure in place of the associator is the **ternary product**

$$
\{\tilde Q_1,\tilde Q_2,\tilde Q_4\}=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4^{*}=\tilde Q_1\tilde Q_2^{*}\tilde Q_4 ,
$$

and it satisfies the Jordan triple identity; equivalently, $\mathbb{B}$ with this ternary product is an **algebraic $J^{*}$-algebra**. The binary product is the shadow of the ternary one: inserting the unit in the third slot recovers the multiplication, and inserting it in the first and third slots recovers the involution.

The article is the fourth of the structural batch, and it is the biquaternion reading of the general pair *The Sesquilinear Associator and the Ternary Product* and *Algebraic J\*-Algebras*, whose parity theorems, vanishing criteria and Jordan triple identity are quoted. The operator forms of the ternary product are *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product*, and the sibling reading whose ternary product fails the identity is *Introduction to the General Quaternionic Sesqualgebra*.

The setting is that of *Introduction to the General Plain Sesqualgebra*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the unit, ${}^{*}$ the conjugate-linear involution, and the multiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$. The scalar and vector parts are written $\tilde Q=Q_te_t+\vec Q$ with $(\vec Q_1,\vec Q_2)=\sum_kQ_{1,k}Q_{2,k}$ and the cross product $\vec Q_1\times\vec Q_2$, and the two halves of the involution are the subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Hermitian and Skew-Hermitian Elements*.

## The Associator

### The Definition and the Parity

**Definition.** The **associator** of $\tilde Q_1,\tilde Q_2,\tilde Q_4$ is

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_4]=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4-\tilde Q_1\star(\tilde Q_2\star\tilde Q_4) .
$$

**Proposition (the parity).** The associator is additive in each variable, $\mathbb{C}$-linear in the first variable, and conjugate-linear in the second, and it vanishes identically if and only if the product is associative.

**Proof.** This is the proposition of *The Sesquilinear Associator and the Ternary Product*, §*Definition and Parity*, read on $\mathbb{B}$: both groupings are additive in each variable, the first slot is linear in both, and the second slot is conjugate-linear in both, so the difference is; the product is associative exactly when the two groupings agree, which is the vanishing of the difference.

**Remark.** The third slot is where the associator is not homogeneous, and the general theorem of *The Sesquilinear Associator and the Ternary Product*, §*The Twist in the Third Slot*, makes this precise: the grouping $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4$ is conjugate-linear in $\tilde Q_4$, the grouping $\tilde Q_1\star(\tilde Q_2\star\tilde Q_4)$ is linear in $\tilde Q_4$, and the associator is the difference of the two, so it is neither linear nor conjugate-linear in that slot unless it vanishes. The associator therefore lives on a difference of two modules in its third variable and on a single module in its first two.

### The Associator of the Biquaternion Multiplication

**Theorem.** For the multiplication of $\mathbb{B}$,

$$
[\tilde Q_1,\tilde Q_2,\tilde Q_4]=\tilde Q_1\bigl(\tilde Q_2^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q_2^{*}\bigr)=\tilde Q_1\bigl((\tilde Q_4\tilde Q_2)^{*}-\tilde Q_4\tilde Q_2^{*}\bigr) .
$$

In particular the associator is the product of $\tilde Q_1$ with the defect $\tilde Q_2^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q_2^{*}$ of the multiplication in the second and third slots.

**Proof.** The derived-operation formula of *Sesqualgebras*, §*The Associator of the Derived Product*, transported to $\mathbb{B}$: $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4=\tilde Q_1\tilde Q_2^{*}\tilde Q_4^{*}$ and $\tilde Q_1\star(\tilde Q_2\star\tilde Q_4)=\tilde Q_1\tilde Q_4\tilde Q_2^{*}$, whose difference is $\tilde Q_1(\tilde Q_2^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q_2^{*})$. The second form uses $\tilde Q_2^{*}\tilde Q_4^{*}=(\tilde Q_4\tilde Q_2)^{*}$, which is the anti-multiplicativity of the involution.

**Corollary (the criterion).** The multiplication of $\mathbb{B}$ is associative if and only if $\tilde Q^{*}\tilde Q_4^{*}=\tilde Q_4\tilde Q^{*}$ for all $\tilde Q,\tilde Q_4$, and neither holds: with a nontrivial involution on a unital algebra the derived operation is never associative, by the collapse theorem of *Sesqualgebras*.

**Proof.** The associator vanishes identically exactly when the defect vanishes for all $\tilde Q_1,\tilde Q_2,\tilde Q_4$; taking $\tilde Q_1=e_t$ removes the factor and gives the condition. The impossibility is the collapse at the identity: associativity of the derived operation forces the involution to be trivial on the scalars, and here the involution is conjugating.

**Example (the witness).** At $(\tilde Q_1,\tilde Q_2,\tilde Q_4)=(e_t,\vec e_x,\vec e_x)$ the two groupings are

$$
(e_t\star \vec e_x)\star \vec e_x=(-\vec e_x)\star \vec e_x=\vec e_x^{2}=-e_t , \qquad e_t\star(\vec e_x\star \vec e_x)=e_t\star e_t=e_t ,
$$

so the associator is $-2e_t$, and the defect $\tilde Q^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q^{*}=\vec e_x^{*}\vec e_x^{*}-\vec e_x\vec e_x^{*}=\vec e_x^{2}-e_t$ evaluates to $-e_t-e_t=-2e_t$ as well, in agreement with the theorem.

**Proof.** The two groupings are computed from the multiplication table of *Introduction to the General Plain Sesqualgebra*: $e_t\star \vec e_x=-\vec e_x$, $\vec e_x\star \vec e_x=e_t$, hence $(-\vec e_x)\star \vec e_x=\vec e_x^{2}=-e_t$ and $e_t\star e_t=e_t$; the defect is $\vec e_x^{*}=-\vec e_x$, so $\vec e_x^{*}\vec e_x^{*}=\vec e_x^{2}=-e_t$ and $\vec e_x\vec e_x^{*}=-\vec e_x^{2}=e_t$.

**Remark.** The witness is the one the group article records for the failure of associativity, and the value $-2e_t$ is the associator there; the criterion of the corollary is the same failure read in the second and third slots alone. The associator is a central multiple of the unit at this triple because the first factor is the unit, which is the simplest case of the formula.

### Non-Commutativity and Flexibility

**Proposition.** The multiplication is not commutative, not flexible and not power-associative: at $(\vec e_x,\vec e_y)$ one has $\vec e_x\star \vec e_y=-\vec e_z$ and $\vec e_y\star \vec e_x=\vec e_z$, so commutativity fails; at $(\tilde Q_1,\tilde Q_2)=(ie_t,e_t)$ the flexible law $(\tilde Q_1\star\tilde Q_2)\star\tilde Q_1=\tilde Q_1\star(\tilde Q_2\star\tilde Q_1)$ fails with the two sides $e_t$ and $-e_t$; and at $\tilde Q_1=ie_t$ the degree-three identity $\tilde Q_1\star(\tilde Q_1\star\tilde Q_1)=(\tilde Q_1\star\tilde Q_1)\star\tilde Q_1$ fails with the two sides $ie_t$ and $-ie_t$.

**Proof.** The witnesses are those of *Introduction to the General Plain Sesqualgebra*, §*Neither Associative Nor Commutative*, read through the multiplication table; each is a direct computation from the rule $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$.

**Remark.** The associator measures associativity, and the flexible and power identities are weaker forms of it that the multiplication also fails; the corpus keeps the three apart because for a sesqualgebra the first is the one that the ternary product repairs, while the second and the third fail before the ternary product is reached. Associativity is the strongest of the three, and the collapse theorem already excludes it.

## The Ternary Product

### The Definition and the Parity

**Definition.** The **ternary product** attached to the multiplication is

$$
\{\tilde Q_1,\tilde Q_2,\tilde Q_4\}=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4^{*}=\tilde Q_1\tilde Q_2^{*}\tilde Q_4 .
$$

**Proposition (the parity).** The ternary product is additive in each variable, $\mathbb{C}$-linear in the first and the third variables and conjugate-linear in the middle variable; it satisfies the Hermitian symmetry

$$
\{\tilde Q_1,\tilde Q_2,\tilde Q_4\}^{*}=\{\tilde Q_4^{*},\tilde Q_2^{*},\tilde Q_1^{*}\} ,
$$

and the plain symmetry $\{\tilde Q_1,\tilde Q_2,\tilde Q_4\}=\{\tilde Q_4,\tilde Q_2,\tilde Q_1\}$ fails as soon as the algebra is noncommutative.

**Proof.** This is the proposition of *The Sesquilinear Associator and the Ternary Product*, §*Definition and Parity*: the parity is read from $\tilde Q_1\tilde Q_2^{*}\tilde Q_4$, where a scalar in the outer slots is a scalar of the algebra product and a scalar in the middle slot meets the involution; the Hermitian symmetry is $(\tilde Q_1\tilde Q_2^{*}\tilde Q_4)^{*}=\tilde Q_4^{*}\tilde Q_2\tilde Q_1^{*}=\{\tilde Q_4^{*},\tilde Q_2^{*},\tilde Q_1^{*}\}$, because the involution reverses the order and is of order two. On $\mathbb{B}$ the plain symmetry fails at $(\vec e_x,\vec e_y,e_t)$, where the two sides are $-\vec e_z$ and $\vec e_z$.

**Remark.** The correction is the one the general article names: the ternary product's middle slot is conjugate-linear, and the symmetry it satisfies is the Hermitian one, which carries the conjugates. The ternary product is not a symmetric operation but a Hermitian-symmetric one, and this is the parity of the middle slot of the binary product promoted to the triple.

### The Passage from the Binary to the Ternary Product

**Theorem.** For $\mathbb{B}$, which is unital with unit $e_t$,

$$
\{\tilde Q_1,\tilde Q_2,e_t\}=\tilde Q_1\star\tilde Q_2 , \qquad \{e_t,\tilde Q,e_t\}=\tilde Q^{*} ,
$$

so the ternary product determines the multiplication and the involution, and it determines the algebra together with its involution.

**Proof.** This is the theorem of *The Sesquilinear Associator and the Ternary Product*, §*The Passage from the Binary to the Ternary Product*: $\{\tilde Q_1,\tilde Q_2,e_t\}=(\tilde Q_1\star\tilde Q_2)\star e_t^{*}=(\tilde Q_1\star\tilde Q_2)\star e_t=\tilde Q_1\tilde Q_2^{*}=\tilde Q_1\star\tilde Q_2$, using $e_t^{*}=e_t$ and the right unit; and $\{e_t,\tilde Q_2,e_t\}=(e_t\star\tilde Q_2)\star e_t=e_t\star\tilde Q_2=\tilde Q_2^{*}$.

**Remark.** The insertion of the unit is what makes the binary product the **shadow** of the ternary one, in the terminology of *Algebraic J\*-Algebras*, §*The Binary Product as a Shadow*. On $\mathbb{B}$ the two displayed identities read the multiplication and the involution out of the ternary product, and there is no datum left over: the triple determines the pair.

### Worked Values

**Example.** On the basis the ternary product is read from the multiplication table. A few values are

$$
\{e_t,e_t,e_t\}=e_t , \qquad \{\vec e_x,\vec e_x,e_t\}=e_t , \qquad \{\vec e_x,\vec e_y,e_t\}=-\vec e_z ,
$$

and the third is the plain-symmetry failure: $\{\vec e_y,\vec e_x,e_t\}=\vec e_z$. The first variable enters as the ordinary product on the left, the middle as the conjugate, and the third as the ordinary product on the right, so raising the outer variables and the middle variable by the basis reproduces the four general products of the corpus read with their three slot conventions.

**Proof.** Each is $\tilde Q_1\tilde Q_2^{*}\tilde Q_4$ evaluated with the basis, using $\vec e_k^{*}=-\vec e_k$ and the products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_x=-\vec e_z$.

**Remark.** The ternary product on the basis is not a new table: it is the binary table with three slots, and the values above are there to fix the convention. The three slots are the two outer slots, which are the plain product, and the middle slot, which is the product with the conjugate, and the reading of the ternary product as a sequence of two binary multiplications is the one the operator theory of *The Ternary Product as an Operator* develops.

## The Jordan Triple Identity

### The Identity

**Definition.** The ternary product satisfies the **Jordan triple identity** when

$$
\{x,y,\{u,v,w\}\}=\{\{x,y,u\},v,w\}-\{u,\{y,x,v\},w\}+\{u,v,\{x,y,w\}\}
$$

for all $x,y,u,v,w$, the identity being the defining axiom of an algebraic $J^{*}$-algebra in *Algebraic J\*-Algebras*.

### The Biquaternions Are an Algebraic J*-Algebra

**Theorem.** With the ternary product $\{\tilde Q_1,\tilde Q_2,\tilde Q_3\}=\tilde Q_1\tilde Q_2^{*}\tilde Q_3$, the biquaternion algebra $\mathbb{B}$ is an algebraic $J^{*}$-algebra: the ternary product has the parity of §*The Ternary Product*, and it satisfies the Jordan triple identity.

**Proof.** The model theorem of *Algebraic J\*-Algebras*, §*The Derived Model*: for an associative $\mathbb{C}$-algebra with a conjugate-linear involution the formula $xyz\mapsto xy^{*}z$ is the **middle model**, and the middle model satisfies the Jordan triple identity, the proof being a finite expansion in the associativity of the algebra and the anti-multiplicativity of the involution. The biquaternion ternary product is the middle model read on $\mathbb{B}$ with the involution ${}^{*}$, so the identity holds and the parity was checked in §*The Ternary Product*. The abstract axioms of an algebraic $J^{*}$-algebra are those of *Algebraic J\*-Algebras*, §*The Axioms*.

**Remark.** The theorem is the positive statement of the batch: the multiplication is not associative and carries no associativity identity, and the ternary product carries the Jordan triple identity in its place. The identity is the exact replacement, and it is why the ternary product rather than the binary one is the natural structure of the sesquilinear reading.

### The Operator Interpretation

**Remark.** The ternary product has two operator readings that the corpus develops separately. Fixing the two outer variables gives the linear operators $\tilde Q_3\mapsto\{\tilde Q_1,\tilde Q_2,\tilde Q_3\}=\tilde Q_1\tilde Q_2^{*}\tilde Q_3$ and $\tilde Q_1\mapsto\{\tilde Q_1,\tilde Q_2,\tilde Q_3\}=\tilde Q_1\tilde Q_2^{*}\tilde Q_3$, the ordinary left and right multiplications by $\tilde Q_1\tilde Q_2^{*}$ and by $\tilde Q_2^{*}\tilde Q_3$; fixing the middle variable gives the conjugate-linear operator $\tilde Q_2\mapsto\{\tilde Q_1,\tilde Q_2,\tilde Q_3\}$, which is the sandwich $S_{\tilde Q_1,\tilde Q_3^{*}}$ of *The Sesquilinear Sandwich on the Biquaternion*. The **quadratic representation** is the case $\tilde Q_1=\tilde Q_3$ of *The Ternary Product as an Operator*, and the conjugation of the middle variable is the adjoint of the ternary product of *The Adjoint of the Ternary Product*. On $\mathbb{B}$ the quadratic representation is $\tilde Q_3\mapsto\tilde Q_3\tilde Q_2^{*}\tilde Q_3=\tilde Q_3\star\tilde Q_2\star\tilde Q_3^{*}$, the sandwich of *The Sesquilinear Sandwich on the Biquaternion* with the two parameters tied to one element.

## The Contrast with the Quaternionic Sibling

### The Middle Model and the Left Model

The general theory of *Algebraic J\*-Algebras* attaches the Jordan triple identity to the **middle model** $xyz\mapsto xy^{*}z$, in which the involution sits in the middle slot. The three other placements of the involution are the **left model** $x^{*}yz$, the **right model** $xy z^{*}$ and the model with no involution; the middle model satisfies the identity and the others need not. The general plain sesquilinear product of the present article is the derived operation, and its ternary product is the middle model, which is why it is an algebraic $J^{*}$-algebra.

### The Failure for the Fourth Product

**Theorem (the sibling).** For the general quaternionic sesquilinear product $\tilde Q_1^{\natural}\tilde Q_2^{*}$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, whose ternary product is the left model, the Jordan triple identity fails: at $(\tilde Q_1,\tilde Q_2,\tilde Q_5,\tilde S,\tilde W)=(e_t,\vec e_x,e_t,\vec e_y,e_t)$ the left-hand side is $\vec e_z$ and the right-hand side is $-3\vec e_z$.

**Proof.** The statement and its proof are the theorem and the corollary of *Introduction to the General Quaternionic Sesqualgebra*, §*The Ternary Product*, where the two sides are computed and the failure is read as the transposition of the two models by the insertion of the $\mathbb{C}$-linear ${}^{\natural}$ in the first slot.

**Remark.** The comparison is sharp: the same construction applied to the two sesquilinear products of the corpus gives the middle model for the derived operation and the left model for the $\natural$-isotope, and only the first is in the class. The two products are related by the insertion of a $\mathbb{C}$-linear map in the first slot, by *Comparison Between the Four General Products*, and it is that insertion, and not the sesquilinearity, that moves the involution out of the middle slot and destroys the identity.

| ternary product | model | Jordan triple identity |
|---|---|---|
| $\tilde Q_1\tilde Q_2^{*}\tilde Q_4$ (middle, this article) | $xy^{*}z$ | holds; $\mathbb{B}$ is an algebraic $J^{*}$-algebra |
| $\overline{\tilde Q_2}\tilde Q_1\tilde Q_4$ (left, sibling) | $x^{*}yz$ | fails at $(e_t,\vec e_x,e_t,\vec e_y,e_t)$, $\vec e_z$ against $-3\vec e_z$ |

**Remark.** The table is the biquaternion form of the general dichotomy: the middle model is the model of the theory and the other placements leave it. The two sesquilinear products of the corpus are therefore separated not by their binary parity, which is the same, but by the position of the involution in their ternary readings, which is what the Jordan triple identity detects.

## Summary

The multiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ has the associator $[\tilde Q_1,\tilde Q_2,\tilde Q_4]=\tilde Q_1(\tilde Q_2^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q_2^{*})$, a difference of the two groupings of the associative product, conjugate-linear in the middle slot and of mixed parity in the third; it is not identically zero, and the multiplication is neither associative nor commutative. The ternary product $\{\tilde Q_1,\tilde Q_2,\tilde Q_4\}=\tilde Q_1\tilde Q_2^{*}\tilde Q_4$ has the parity of the middle model of *Algebraic J\*-Algebras*, it satisfies the Hermitian symmetry and recovers the multiplication and the involution by inserting the unit, and it satisfies the Jordan triple identity, so $\mathbb{B}$ with this ternary product is an algebraic $J^{*}$-algebra. The identity is the replacement of the associativity that the collapse theorem forbids, and the sibling general quaternionic sesquilinear product, whose ternary product is the left model, fails it; the two products are separated by the position of the involution in the ternary reading.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the sesquilinear multiplication |
| $[\tilde Q_1,\tilde Q_2,\tilde Q_4]=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4-\tilde Q_1\star(\tilde Q_2\star\tilde Q_4)$ | the associator |
| $\tilde Q_1(\tilde Q_2^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q_2^{*})$ | the associator on the biquaternions |
| $\{\tilde Q_1,\tilde Q_2,\tilde Q_4\}=(\tilde Q_1\star\tilde Q_2)\star\tilde Q_4^{*}=\tilde Q_1\tilde Q_2^{*}\tilde Q_4$ | the ternary product |
| $\{x,y,z\}^{*}=\{z^{*},y^{*},x^{*}\}$ | the Hermitian symmetry of the ternary product |
| $\{\tilde Q_1,\tilde Q_2,e_t\}=\tilde Q_1\star\tilde Q_2$, $\{e_t,\tilde Q,e_t\}=\tilde Q^{*}$ | the recovery of the binary product and the involution |
| Jordan triple identity | the defining axiom of an algebraic $J^{*}$-algebra |
| middle model $xy^{*}z$, left model $x^{*}yz$ | the two placements of the involution in the ternary product |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan triple identity and the triple systems that carry it.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and Their Applications* (Springer Lecture Notes in Mathematics 1710, 1999), for the quadratic representation of a Jordan structure and the identity it satisfies.
- Ottmar Loos, *Jordan Pairs* (Springer Lecture Notes in Mathematics 460, 1975), for the triple product $xy^{*}z$, the Jordan triple systems and the operator forms of the triple product.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan triple identity, the quadratic representation and the relation between the binary and the ternary operations.
- Erhard Neher, *Jordan Triple Systems by the Grid Approach* (Springer Lecture Notes in Mathematics 1280, 1987), for the algebraic $J^{*}$-triples and the middle and left models of the involution.
