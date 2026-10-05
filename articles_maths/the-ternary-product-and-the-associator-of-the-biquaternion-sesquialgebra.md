
# __The Ternary Product and the Associator of the Biquaternion Sesquialgebra__

## Introduction

The multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of *Biquaternions as a Sesquialgebra over $\mathbb{C}$* is neither associative nor commutative, and the object that measures the failure of associativity is the **associator**

$$
[\tilde P,\tilde Q,\tilde R]=(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R) .
$$

On $\mathbb{B}$ it reads

$$
[\tilde P,\tilde Q,\tilde R]=\tilde P\bigl(\tilde Q^{*}\tilde R^{*}-\tilde R\tilde Q^{*}\bigr) ,
$$

a difference of two groupings of the associative product, and it is nonzero as soon as the involution is nontrivial. The operation that carries a structure in place of the associator is the **ternary product**

$$
\{\tilde P,\tilde Q,\tilde R\}=(\tilde P\star\tilde Q)\star\tilde R^{*}=\tilde P\tilde Q^{*}\tilde R ,
$$

and it satisfies the Jordan triple identity; equivalently, $\mathbb{B}$ with this ternary product is an **algebraic $J^{*}$-algebra**. The binary product is the shadow of the ternary one: inserting the unit in the third slot recovers the multiplication, and inserting it in the first and third slots recovers the involution.

The article is the fourth of the structural batch, and it is the biquaternion reading of the general pair *The Sesquilinear Associator and the Ternary Product* and *Algebraic J\*-Algebras*, whose parity theorems, vanishing criteria and Jordan triple identity are quoted. The operator forms of the ternary product are *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product*, and the sibling reading whose ternary product fails the identity is *Biquaternions as a Quaternionic Sesquialgebra over $\mathbb{C}$*.

The setting is that of *Biquaternions as a Sesquialgebra over $\mathbb{C}$*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, ${}^{*}$ the conjugate-linear involution, and the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The scalar and vector parts are written $\tilde Q=Q_0e_0+\mathbf Q$ with $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ and the cross product $\mathbf P\times\mathbf Q$, and the two halves of the involution are the subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Hermitian and Skew-Hermitian Elements*.

## The Associator

### The Definition and the Parity

**Definition.** The **associator** of $\tilde P,\tilde Q,\tilde R$ is

$$
[\tilde P,\tilde Q,\tilde R]=(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R) .
$$

**Proposition (the parity).** The associator is additive in each variable, $\mathbb{C}$-linear in the first variable, and conjugate-linear in the second, and it vanishes identically if and only if the product is associative.

**Proof.** This is the proposition of *The Sesquilinear Associator and the Ternary Product*, §*Definition and Parity*, read on $\mathbb{B}$: both groupings are additive in each variable, the first slot is linear in both, and the second slot is conjugate-linear in both, so the difference is; the product is associative exactly when the two groupings agree, which is the vanishing of the difference. $\square$

**Remark.** The third slot is where the associator is not homogeneous, and the general theorem of *The Sesquilinear Associator and the Ternary Product*, §*The Twist in the Third Slot*, makes this precise: the grouping $(\tilde P\star\tilde Q)\star\tilde R$ is conjugate-linear in $\tilde R$, the grouping $\tilde P\star(\tilde Q\star\tilde R)$ is linear in $\tilde R$, and the associator is the difference of the two, so it is neither linear nor conjugate-linear in that slot unless it vanishes. The associator therefore lives on a difference of two modules in its third variable and on a single module in its first two.

### The Associator of the Biquaternion Multiplication

**Theorem.** For the multiplication of $\mathbb{B}$,

$$
[\tilde P,\tilde Q,\tilde R]=\tilde P\bigl(\tilde Q^{*}\tilde R^{*}-\tilde R\tilde Q^{*}\bigr)=\tilde P\bigl((\tilde R\tilde Q)^{*}-\tilde R\tilde Q^{*}\bigr) .
$$

In particular the associator is the product of $\tilde P$ with the defect $\tilde Q^{*}\tilde R^{*}-\tilde R\tilde Q^{*}$ of the multiplication in the second and third slots.

**Proof.** The derived-operation formula of *Sesquialgebras*, §*The Associator of the Derived Product*, transported to $\mathbb{B}$: $(\tilde P\star\tilde Q)\star\tilde R=\tilde P\tilde Q^{*}\tilde R^{*}$ and $\tilde P\star(\tilde Q\star\tilde R)=\tilde P\tilde R\tilde Q^{*}$, whose difference is $\tilde P(\tilde Q^{*}\tilde R^{*}-\tilde R\tilde Q^{*})$. The second form uses $\tilde Q^{*}\tilde R^{*}=(\tilde R\tilde Q)^{*}$, which is the anti-multiplicativity of the involution. $\square$

**Corollary (the criterion).** The multiplication of $\mathbb{B}$ is associative if and only if $\tilde Q^{*}\tilde R^{*}=\tilde R\tilde Q^{*}$ for all $\tilde Q,\tilde R$, and neither holds: with a nontrivial involution on a unital algebra the derived operation is never associative, by the collapse theorem of *Sesquialgebras*.

**Proof.** The associator vanishes identically exactly when the defect vanishes for all $\tilde P,\tilde Q,\tilde R$; taking $\tilde P=e_0$ removes the factor and gives the condition. The impossibility is the collapse at the identity: associativity of the derived operation forces the involution to be trivial on the scalars, and here the involution is conjugating. $\square$

**Example (the witness).** At $(\tilde P,\tilde Q,\tilde R)=(e_0,e_1,e_1)$ the two groupings are

$$
(e_0\star e_1)\star e_1=(-e_1)\star e_1=e_1^{2}=-e_0 , \qquad e_0\star(e_1\star e_1)=e_0\star e_0=e_0 ,
$$

so the associator is $-2e_0$, and the defect $\tilde Q^{*}\tilde R^{*}-\tilde R\tilde Q^{*}=e_1^{*}e_1^{*}-e_1e_1^{*}=e_1^{2}-e_0$ evaluates to $-e_0-e_0=-2e_0$ as well, in agreement with the theorem.

**Proof.** The two groupings are computed from the multiplication table of *Biquaternions as a Sesquialgebra over $\mathbb{C}$*: $e_0\star e_1=-e_1$, $e_1\star e_1=e_0$, hence $(-e_1)\star e_1=e_1^{2}=-e_0$ and $e_0\star e_0=e_0$; the defect is $e_1^{*}=-e_1$, so $e_1^{*}e_1^{*}=e_1^{2}=-e_0$ and $e_1e_1^{*}=-e_1^{2}=e_0$. $\square$

**Remark.** The witness is the one the group article records for the failure of associativity, and the value $-2e_0$ is the associator there; the criterion of the corollary is the same failure read in the second and third slots alone. The associator is a central multiple of the unit at this triple because the first factor is the unit, which is the simplest case of the formula.

### Non-Commutativity and Flexibility

**Proposition.** The multiplication is not commutative, not flexible and not power-associative: at $(e_1,e_2)$ one has $e_1\star e_2=-e_3$ and $e_2\star e_1=e_3$, so commutativity fails; at $(\tilde P,\tilde Q)=(ie_0,e_0)$ the flexible law $(\tilde P\star\tilde Q)\star\tilde P=\tilde P\star(\tilde Q\star\tilde P)$ fails with the two sides $e_0$ and $-e_0$; and at $\tilde P=ie_0$ the degree-three identity $\tilde P\star(\tilde P\star\tilde P)=(\tilde P\star\tilde P)\star\tilde P$ fails with the two sides $ie_0$ and $-ie_0$.

**Proof.** The witnesses are those of *Biquaternions as a Sesquialgebra over $\mathbb{C}$*, §*Neither Associative Nor Commutative*, read through the multiplication table; each is a direct computation from the rule $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. $\square$

**Remark.** The associator measures associativity, and the flexible and power identities are weaker forms of it that the multiplication also fails; the corpus keeps the three apart because for a sesquialgebra the first is the one that the ternary product repairs, while the second and the third fail before the ternary product is reached. Associativity is the strongest of the three, and the collapse theorem already excludes it.

## The Ternary Product

### The Definition and the Parity

**Definition.** The **ternary product** attached to the multiplication is

$$
\{\tilde P,\tilde Q,\tilde R\}=(\tilde P\star\tilde Q)\star\tilde R^{*}=\tilde P\tilde Q^{*}\tilde R .
$$

**Proposition (the parity).** The ternary product is additive in each variable, $\mathbb{C}$-linear in the first and the third variables and conjugate-linear in the middle variable; it satisfies the Hermitian symmetry

$$
\{\tilde P,\tilde Q,\tilde R\}^{*}=\{\tilde R^{*},\tilde Q^{*},\tilde P^{*}\} ,
$$

and the plain symmetry $\{\tilde P,\tilde Q,\tilde R\}=\{\tilde R,\tilde Q,\tilde P\}$ fails as soon as the algebra is noncommutative.

**Proof.** This is the proposition of *The Sesquilinear Associator and the Ternary Product*, §*Definition and Parity*: the parity is read from $\tilde P\tilde Q^{*}\tilde R$, where a scalar in the outer slots is a scalar of the algebra product and a scalar in the middle slot meets the involution; the Hermitian symmetry is $(\tilde P\tilde Q^{*}\tilde R)^{*}=\tilde R^{*}\tilde Q\tilde P^{*}=\{\tilde R^{*},\tilde Q^{*},\tilde P^{*}\}$, because the involution reverses the order and is of order two. On $\mathbb{B}$ the plain symmetry fails at $(e_1,e_2,e_0)$, where the two sides are $-e_3$ and $e_3$. $\square$

**Remark.** The correction is the one the general article names: the ternary product's middle slot is conjugate-linear, and the symmetry it satisfies is the Hermitian one, which carries the conjugates. The ternary product is not a symmetric operation but a Hermitian-symmetric one, and this is the parity of the middle slot of the binary product promoted to the triple.

### The Passage from the Binary to the Ternary Product

**Theorem.** For $\mathbb{B}$, which is unital with unit $e_0$,

$$
\{\tilde P,\tilde Q,e_0\}=\tilde P\star\tilde Q , \qquad \{e_0,\tilde Q,e_0\}=\tilde Q^{*} ,
$$

so the ternary product determines the multiplication and the involution, and it determines the algebra together with its involution.

**Proof.** This is the theorem of *The Sesquilinear Associator and the Ternary Product*, §*The Passage from the Binary to the Ternary Product*: $\{\tilde P,\tilde Q,e_0\}=(\tilde P\star\tilde Q)\star e_0^{*}=(\tilde P\star\tilde Q)\star e_0=\tilde P\tilde Q^{*}=\tilde P\star\tilde Q$, using $e_0^{*}=e_0$ and the right unit; and $\{e_0,\tilde Q,e_0\}=(e_0\star\tilde Q)\star e_0=e_0\star\tilde Q=\tilde Q^{*}$. $\square$

**Remark.** The insertion of the unit is what makes the binary product the **shadow** of the ternary one, in the terminology of *Algebraic J\*-Algebras*, §*The Binary Product as a Shadow*. On $\mathbb{B}$ the two displayed identities read the multiplication and the involution out of the ternary product, and there is no datum left over: the triple determines the pair.

### Worked Values

**Example.** On the basis the ternary product is read from the multiplication table. A few values are

$$
\{e_0,e_0,e_0\}=e_0 , \qquad \{e_1,e_1,e_0\}=e_0 , \qquad \{e_1,e_2,e_0\}=-e_3 ,
$$

and the third is the plain-symmetry failure: $\{e_2,e_1,e_0\}=e_3$. The first variable enters as the ordinary product on the left, the middle as the conjugate, and the third as the ordinary product on the right, so raising the outer variables and the middle variable by the basis reproduces the four products of the corpus read with their three slot conventions.

**Proof.** Each is $\tilde P\tilde Q^{*}\tilde R$ evaluated with the basis, using $e_k^{*}=-e_k$ and the products $e_1e_2=e_3$, $e_2e_1=-e_3$. $\square$

**Remark.** The ternary product on the basis is not a new table: it is the binary table with three slots, and the values above are there to fix the convention. The three slots are the two outer slots, which are the plain product, and the middle slot, which is the product with the conjugate, and the reading of the ternary product as a sequence of two binary multiplications is the one the operator theory of *The Ternary Product as an Operator* develops.

## The Jordan Triple Identity

### The Identity

**Definition.** The ternary product satisfies the **Jordan triple identity** when

$$
\{x,y,\{u,v,w\}\}=\{\{x,y,u\},v,w\}-\{u,\{y,x,v\},w\}+\{u,v,\{x,y,w\}\}
$$

for all $x,y,u,v,w$, the identity being the defining axiom of an algebraic $J^{*}$-algebra in *Algebraic J\*-Algebras*.

### The Biquaternions Are an Algebraic J*-Algebra

**Theorem.** With the ternary product $\{\tilde X,\tilde Y,\tilde Z\}=\tilde X\tilde Y^{*}\tilde Z$, the biquaternion algebra $\mathbb{B}$ is an algebraic $J^{*}$-algebra: the ternary product has the parity of §*The Ternary Product*, and it satisfies the Jordan triple identity.

**Proof.** The model theorem of *Algebraic J\*-Algebras*, §*The Derived Model*: for an associative $\mathbb{C}$-algebra with a conjugate-linear involution the formula $xyz\mapsto xy^{*}z$ is the **middle model**, and the middle model satisfies the Jordan triple identity, the proof being a finite expansion in the associativity of the algebra and the anti-multiplicativity of the involution. The biquaternion ternary product is the middle model read on $\mathbb{B}$ with the involution ${}^{*}$, so the identity holds and the parity was checked in §*The Ternary Product*. The abstract axioms of an algebraic $J^{*}$-algebra are those of *Algebraic J\*-Algebras*, §*The Axioms*. $\square$

**Remark.** The theorem is the positive statement of the batch: the multiplication is not associative and carries no associativity identity, and the ternary product carries the Jordan triple identity in its place. The identity is the exact replacement, and it is why the ternary product rather than the binary one is the natural structure of the sesquilinear reading.

### The Operator Reading

**Remark.** The ternary product has two operator readings that the corpus develops separately. Fixing the two outer variables gives the linear operators $\tilde Z\mapsto\{\tilde X,\tilde Y,\tilde Z\}=\tilde X\tilde Y^{*}\tilde Z$ and $\tilde X\mapsto\{\tilde X,\tilde Y,\tilde Z\}=\tilde X\tilde Y^{*}\tilde Z$, the ordinary left and right multiplications by $\tilde X\tilde Y^{*}$ and by $\tilde Y^{*}\tilde Z$; fixing the middle variable gives the conjugate-linear operator $\tilde Y\mapsto\{\tilde X,\tilde Y,\tilde Z\}$, which is the sandwich $S_{\tilde X,\tilde Z^{*}}$ of *The Sesquilinear Sandwich on the Biquaternions*. The **quadratic representation** is the case $\tilde X=\tilde Z$ of *The Ternary Product as an Operator*, and the conjugation of the middle variable is the adjoint of the ternary product of *The Adjoint of the Ternary Product*. On $\mathbb{B}$ the quadratic representation is $\tilde Z\mapsto\tilde Z\tilde Y^{*}\tilde Z=\tilde Z\star\tilde Y\star\tilde Z^{*}$, the sandwich of *The Sesquilinear Sandwich on the Biquaternions* with the two parameters tied to one element.

## The Contrast with the Quaternionic Sibling

### The Middle Model and the Left Model

The general theory of *Algebraic J\*-Algebras* attaches the Jordan triple identity to the **middle model** $xyz\mapsto xy^{*}z$, in which the involution sits in the middle slot. The three other placements of the involution are the **left model** $x^{*}yz$, the **right model** $xy z^{*}$ and the model with no involution; the middle model satisfies the identity and the others need not. The complex sesquilinear product of the present article is the derived operation, and its ternary product is the middle model, which is why it is an algebraic $J^{*}$-algebra.

### The Failure for the Fourth Product

**Theorem (the sibling).** For the complex quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ of *The Four Biquaternion Complex Products*, whose ternary product is the left model, the Jordan triple identity fails: at $(\tilde X,\tilde Y,\tilde U,\tilde V,\tilde W)=(e_0,e_1,e_0,e_2,e_0)$ the left-hand side is $e_3$ and the right-hand side is $-3e_3$.

**Proof.** The statement and its proof are the theorem and the corollary of *Biquaternions as a Quaternionic Sesquialgebra over $\mathbb{C}$*, §*The Ternary Product*, where the two sides are computed and the failure is read as the transposition of the two models by the insertion of the $\mathbb{C}$-linear ${}^{\natural}$ in the first slot. $\square$

**Remark.** The comparison is sharp: the same construction applied to the two sesquilinear products of the corpus gives the middle model for the derived operation and the left model for the $\natural$-isotope, and only the first is in the class. The two products are related by the insertion of a $\mathbb{C}$-linear map in the first slot, by *Comparison Between the Four Biquaternion Products*, and it is that insertion, and not the sesquilinearity, that moves the involution out of the middle slot and destroys the identity.

| ternary product | model | Jordan triple identity |
|---|---|---|
| $\tilde P\tilde Q^{*}\tilde R$ (middle, this article) | $xy^{*}z$ | holds; $\mathbb{B}$ is an algebraic $J^{*}$-algebra |
| $\overline{\tilde Q}\tilde P\tilde R$ (left, sibling) | $x^{*}yz$ | fails at $(e_0,e_1,e_0,e_2,e_0)$, $e_3$ against $-3e_3$ |

**Remark.** The table is the biquaternion form of the general dichotomy: the middle model is the model of the theory and the other placements leave it. The two sesquilinear products of the corpus are therefore separated not by their binary parity, which is the same, but by the position of the involution in their ternary readings, which is what the Jordan triple identity detects.

## Summary

The multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ has the associator $[\tilde P,\tilde Q,\tilde R]=\tilde P(\tilde Q^{*}\tilde R^{*}-\tilde R\tilde Q^{*})$, a difference of the two groupings of the associative product, conjugate-linear in the middle slot and of mixed parity in the third; it is not identically zero, and the multiplication is neither associative nor commutative. The ternary product $\{\tilde P,\tilde Q,\tilde R\}=\tilde P\tilde Q^{*}\tilde R$ has the parity of the middle model of *Algebraic J\*-Algebras*, it satisfies the Hermitian symmetry and recovers the multiplication and the involution by inserting the unit, and it satisfies the Jordan triple identity, so $\mathbb{B}$ with this ternary product is an algebraic $J^{*}$-algebra. The identity is the replacement of the associativity that the collapse theorem forbids, and the sibling quaternionic sesquilinear product, whose ternary product is the left model, fails it; the two products are separated by the position of the involution in the ternary reading.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the sesquilinear multiplication |
| $[\tilde P,\tilde Q,\tilde R]=(\tilde P\star\tilde Q)\star\tilde R-\tilde P\star(\tilde Q\star\tilde R)$ | the associator |
| $\tilde P(\tilde Q^{*}\tilde R^{*}-\tilde R\tilde Q^{*})$ | the associator on the biquaternions |
| $\{\tilde P,\tilde Q,\tilde R\}=(\tilde P\star\tilde Q)\star\tilde R^{*}=\tilde P\tilde Q^{*}\tilde R$ | the ternary product |
| $\{x,y,z\}^{*}=\{z^{*},y^{*},x^{*}\}$ | the Hermitian symmetry of the ternary product |
| $\{\tilde P,\tilde Q,e_0\}=\tilde P\star\tilde Q$, $\{e_0,\tilde Q,e_0\}=\tilde Q^{*}$ | the recovery of the binary product and the involution |
| Jordan triple identity | the defining axiom of an algebraic $J^{*}$-algebra |
| middle model $xy^{*}z$, left model $x^{*}yz$ | the two placements of the involution in the ternary product |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan triple identity and the triple systems that carry it.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and Their Applications* (Springer Lecture Notes in Mathematics 1710, 1999), for the quadratic representation of a Jordan structure and the identity it satisfies.
- Ottmar Loos, *Jordan Pairs* (Springer Lecture Notes in Mathematics 460, 1975), for the triple product $xy^{*}z$, the Jordan triple systems and the operator forms of the triple product.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan triple identity, the quadratic representation and the relation between the binary and the ternary operations.
- Erhard Neher, *Jordan Triple Systems by the Grid Approach* (Springer Lecture Notes in Mathematics 1280, 1987), for the algebraic $J^{*}$-triples and the middle and left models of the involution.
