# __Introduction to the Symmetric Quaternionic Algebra of Quaternions__

## Introduction

The quaternion space carries six bilinear products (*The 6 Products of the Quaternion Real Space*), and one of them is the **general quaternionic product** $\tilde p^{\natural}\tilde q$, the plain product with the quaternion conjugation read on the first factor. Every bilinear product splits into a symmetric part and an antisymmetric part, and this article introduces the block that reads the symmetric part of $\tilde p^{\natural}\tilde q$ as a multiplication:

$$
\tilde p\star\tilde q = \tfrac12\bigl(\tilde p^{\natural}\tilde q + \tilde q^{\natural}\tilde p\bigr).
$$

The general construction of the splitting, and the general definitions of the unit, the inverse, the zero divisor, the idempotent, the nilpotent and the root, are *Definitions for the Study of the 6 Algebraic Structures*; here they are cited and not restated. The article establishes the elementary theory of the operation: its rule, its coefficient, the sixteen products of the basis, its laws, its image, the absence of a unit, and the placement of the structure $\mathrm{SQA}$ among the six. The name $\mathrm{SQA}$ and the verb *collapse* are the two threads: the operation collapses the whole space onto its scalar line, and every later article of the block is a reading of the single formula $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$.

**Boundaries.** The six products and the six structures are *The 6 Products of the Quaternion Real Space* and *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the two general products are *The Two General Products of the Quaternion $\mathbb{R}$ Space*; the antisymmetric quaternionic companion of this block is *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, below this article in this category; the parallel of this block among the plain products is *Introduction to the Symmetric Plain Algebra of Quaternions*, above this article in this category. The companion articles of the block read the same operation through its zero divisors, its roots of a central value, its specificities, its radical and isotropy, its form, its multiplication operators and its two matrix models. The quaternion norm and the invertibility criterion are *Norm and Invertibility in the General Plain Algebra*.

**Conventions.** Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$, with basis $e_0=1,e_1,e_2,e_3$, the products $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and $e_k^{2}=-e_0$. A quaternion is $\tilde q=q_0e_0+q_1e_1+q_2e_2+q_3e_3$, its **scalar part** is $\mathrm{Sc}\,\tilde q=q_0$ and its **vector part** is $\mathrm{Vect}\,\tilde q=\mathbf q=q_1e_1+q_2e_2+q_3e_3$. The **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\mathbf q$. On $\mathbb{R}$ the corpus convention reads: the **bar** is the identity, $\mathbb{R}$ having no nontrivial involution; the **natural sign** is ${}^{\natural}$; and the **star** coincides with the natural sign and adds nothing. The **quaternion form** is

$$
N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q=\mathrm{Sc}\bigl(\tilde p^{\natural}\tilde q\bigr),\qquad \mathbf p\cdot\mathbf q=\sum_{k=1}^{3}p_kq_k,
$$

and the **plain form** is $B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q$. The two forms are the subject of *The 2 Forms over the Quaternion $\mathbb{R}$ Space* and are cited here.

## The Operation

**Definition.** The **symmetric quaternionic multiplication** of $\mathbb{H}$ is the operation

$$
\tilde p\star\tilde q = \tfrac12\bigl(\tilde p^{\natural}\tilde q + \tilde q^{\natural}\tilde p\bigr).
$$

It is the symmetric part of the general quaternionic product $\tilde p^{\natural}\tilde q$ for the exchange of the two arguments, and its antisymmetric half is the quaternionic bracket $[\tilde p,\tilde q]_{\natural}=\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p$ of *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, below this article in this category. The two halves reconstruct the parent product,

$$
\tilde p^{\natural}\tilde q = \tilde p\star\tilde q + \tfrac12\,[\tilde p,\tilde q]_{\natural},
$$

and the operation is the multiplication of the structure denoted $\mathrm{SQA}$ in *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. Both slots are read linearly: the operation is $\mathbb{R}$-bilinear, the class of the parent product, and no conjugation is inserted in either slot of $\star$.

**Theorem (the value is scalar and the coefficient is the quaternion form).** For all $\tilde p,\tilde q\in\mathbb{H}$,

$$
\tilde p\star\tilde q = N(\tilde p,\tilde q)\,e_0 .
$$

*Proof.* Write the parent product in scalar and vector parts. Since $\tilde p^{\natural}\tilde q=(p_0e_0-\mathbf p)(q_0e_0+\mathbf q)$, its scalar part is $p_0q_0+\mathbf p\cdot\mathbf q$ and its vector part is $p_0\mathbf q-q_0\mathbf p-\mathbf p\times\mathbf q$, as in *Introduction to the General Quaternionic Algebra of Quaternions*. The exchange $\tilde q^{\natural}\tilde p$ has the same scalar part and the vector part $q_0\mathbf p-p_0\mathbf q-\mathbf q\times\mathbf p$. In the half-sum the two mixed terms cancel and the two vector products cancel by $\mathbf p\times\mathbf q=-\mathbf q\times\mathbf p$.

The coefficient $N$ is the **quaternion form**, the one of the two forms of the space that *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* attaches to $\mathrm{SQA}$.

**Corollary (the class and the commutativity).** The operation is $\mathbb{R}$-bilinear and commutative, its value is always scalar, and its commutator vanishes identically,

$$
\tilde p\star\tilde q=\tilde q\star\tilde p,\qquad \tilde p\star\tilde q-\tilde q\star\tilde p=0 .
$$

*Proof.* Bilinearity is read on the definition, both slots being linear; commutativity is read on the defining half-sum; the value is scalar by the theorem; and the commutator vanishes because the product is commutative.

**Remark (the value is scalar although neither summand is).** The two summands $\tilde p^{\natural}\tilde q$ and $\tilde q^{\natural}\tilde p$ are exchanged by the quaternion conjugation, $(\tilde p^{\natural}\tilde q)^{\natural}=\tilde q^{\natural}\tilde p$, and the average of two elements exchanged by an involution is fixed by it; the elements fixed by ${}^{\natural}$ are the scalar ones. This is the reason for the centrality, and the reason $\mathrm{SQA}$ behaves unlike the symmetric part of the plain product, which keeps a vector part. The operation is the pairing $N$ placed on the scalar line.

**Remark (the definite character).** The form $N$ is positive definite: $N(\tilde q,\tilde q)=q_0^{2}+q_1^{2}+q_2^{2}+q_3^{2}\geq0$, with equality only at $\tilde q=0$. Every value of the operation is therefore a real multiple of $e_0$, and every square $\tilde q\star\tilde q=N(\tilde q,\tilde q)e_0$ is a nonnegative multiple of $e_0$.

## The Multiplication Table

**Proposition (the basis table).** For $\mu,\nu\in\{0,1,2,3\}$,

$$
e_\mu\star e_\nu = \delta_{\mu\nu}\,e_0 .
$$

*Proof.* For $\mu=\nu=0$: $e_0\star e_0=e_0$ and $N(e_0,e_0)=1$. For $\mu=\nu=k\ne0$: $e_k\star e_k=e_k^{\natural}e_k=(-e_k)e_k=-e_k^{2}=e_0$, and $N(e_k,e_k)=1$. For $\mu\ne\nu$: if both indices are nonzero then $e_\mu^{\natural}e_\nu=-e_\mu e_\nu$ and $e_\nu^{\natural}e_\mu=-e_\nu e_\mu$, and $e_\mu e_\nu=-e_\nu e_\mu$ for the basis, so the summands cancel; if one index is $0$ and the other is $k\ne0$ then $e_0^{\natural}e_k=e_k$ and $e_k^{\natural}e_0=-e_k$, which cancel. So the value is $0=\delta_{\mu\nu}e_0$.

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $0$ | $0$ | $0$ |
| $e_1$ | $0$ | $e_0$ | $0$ | $0$ |
| $e_2$ | $0$ | $0$ | $e_0$ | $0$ |
| $e_3$ | $0$ | $0$ | $0$ | $e_0$ |

**Corollary (bilinearity and the determination by the table).** The sixteen products are exactly the sixteen entries of the identity matrix read on the scalar line: the coefficient $N$ is the standard symmetric bilinear form of $\mathbb{R}^4$, with Gram matrix the identity in the basis, and the operation is determined by its table,

$$
\Bigl(\sum_\mu p_\mu e_\mu\Bigr)\star\Bigl(\sum_\nu q_\nu e_\nu\Bigr)=\Bigl(\sum_\mu p_\mu q_\mu\Bigr)e_0 .
$$

*Proof.* The table gives $e_\mu\star e_\nu=\delta_{\mu\nu}e_0$, and $\mathbb{R}$-bilinearity extends the display to the general pair; conversely the display evaluates the definition of $N$.

**Remark (the table is not the one of the plain product).** The plain product gives a fixed-point-free permutation table with signs (*Introduction to the General Plain Algebra of Quaternions*), and the general quaternionic product one with the first column negated. The entry $e_\mu\star e_\nu$ is the symmetrisation of the second, and it is diagonal because the antisymmetric part is what carries the off-diagonal signs: the symmetric half keeps only the diagonal of the quaternionic table. The table is the smallest possible for a nonzero operation.

## The Laws of the Operation

The reference for the laws of a product is *Definitions for the Study of the 6 Algebraic Structures*; the reading of the six one by one is *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

### Commutativity, and the Collapse of the Derived Operation

The operation is commutative, so its **commutator** vanishes identically and the derived operation is the zero operation. The derived algebra is therefore the scalar line $\mathbb{R}e_0$ alone, on which the operation is the multiplication of $\mathbb{R}$: for real $a,b$,

$$
(ae_0)\star(be_0)=ab\,e_0 .
$$

The operation carries no Lie structure; the antisymmetric half of the parent carries it instead, and that half is the block $\mathrm{AQA}$.

### Associativity

**Proposition (the operation is not associative).** At $\tilde p=\tilde q=e_1$ and $\tilde r=e_0$ the two bracketings differ,

$$
(e_1\star e_1)\star e_0=e_0\neq0=e_1\star(e_1\star e_0),
$$

and the general associator is

$$
(\tilde p\star\tilde q)\star\tilde r-\tilde p\star(\tilde q\star\tilde r)
=\bigl(N(\tilde p,\tilde q)r_0-p_0N(\tilde q,\tilde r)\bigr)e_0 .
$$

*Proof.* $(\tilde p\star\tilde q)\star\tilde r=N(\tilde p,\tilde q)e_0\star\tilde r=N(\tilde p,\tilde q)r_0e_0$, and $\tilde p\star(\tilde q\star\tilde r)=N(\tilde q,\tilde r)p_0e_0$. At the witness the first is $N(e_1,e_1)e_0=e_0$ and the second is $N(e_1,e_0)e_0=0$.

### Power-Associativity

**Proposition (the operation is not power-associative).** At $\tilde x=e_0+e_1$, whose square is $\tilde x\star\tilde x=2e_0$, the two bracketings of the fourth power differ,

$$
(\tilde x\star\tilde x)\star(\tilde x\star\tilde x)=4e_0\neq2e_0=\bigl((\tilde x\star\tilde x)\star\tilde x\bigr)\star\tilde x .
$$

*Proof.* $\tilde x\star\tilde x=N(\tilde x,\tilde x)e_0=2e_0$. On the left the product is $2e_0\star2e_0=4e_0$. On the right, $(\tilde x\star\tilde x)\star\tilde x=2e_0\star\tilde x=2x_0e_0=2e_0$, and $2e_0\star\tilde x=2e_0$ again; so the right side is $2e_0$. The three-element powers agree, by commutativity, and the failure appears at the fourth power.

### The Two Classical Identities

**Proposition (the Jordan identity fails).** With the parenthesisation of *Definitions for the Study of the 6 Algebraic Structures*, the identity

$$
\tilde x\star\bigl(\tilde y\star(\tilde x\star\tilde x)\bigr)=\bigl(\tilde x\star\tilde y\bigr)\star\bigl(\tilde x\star\tilde x\bigr)
$$

fails, and at $\tilde x=\tilde y=e_1$ the two sides are $0$ and $e_0$.

*Proof.* At $\tilde x=e_1$ the square is $\tilde x\star\tilde x=e_0$. The left side is $\tilde x\star(\tilde x\star e_0)=\tilde x\star N(\tilde x,e_0)e_0=\tilde x\star0=0$; the right side is $(\tilde x\star\tilde x)\star(\tilde x\star\tilde x)=e_0\star e_0=N(e_0,e_0)e_0=e_0$.

**Proposition (the Jacobi identity fails).** The identity

$$
\tilde x\star(\tilde y\star\tilde z)+\tilde y\star(\tilde z\star\tilde x)+\tilde z\star(\tilde x\star\tilde y)=0
$$

fails, and at $\tilde x=\tilde y=\tilde z=e_0$ its left side is $3e_0$.

*Proof.* $\tilde y\star\tilde z=N(\tilde y,\tilde z)e_0$, so the first term is $x_0N(\tilde y,\tilde z)e_0$ and the sum is $\bigl(x_0N(\tilde y,\tilde z)+y_0N(\tilde z,\tilde x)+z_0N(\tilde x,\tilde y)\bigr)e_0$, which at the three units is $3e_0$.

**Proposition (the alternating law fails).** The operation is not alternating: $e_0\star e_0=e_0\neq0$, so there is an element whose square does not vanish.

The operation is therefore neither associative, nor power-associative, nor a Jordan product, nor a Lie bracket. It is the only operation of the six whose values lie in the scalar line, and the collapse of the commutator does not imply the collapse of the associator.

## The Image and the Unit

**Proposition (the image is the scalar line).** The image of $\star$ is the scalar line $\mathbb{R}e_0$, and the map is onto it; on that line the operation is the multiplication of $\mathbb{R}$.

*Proof.* Every value is scalar by the theorem of §*The Operation*, so the image is contained in $\mathbb{R}e_0$; conversely $N(\tilde q,t\tilde q)=t\,N(\tilde q,\tilde q)$ is an arbitrary real multiple of $N(\tilde q,\tilde q)$ as $t$ ranges over $\mathbb{R}$, and $N(e_0,e_0)=1$ gives the whole line.

**Proposition (there is no unit).** The operation has no unit, and no one-sided unit either. For every element $\tilde a$,

$$
\tilde a\star e_0=e_0\star\tilde a=a_0\,e_0 ,
$$

so $e_0$ is a unit for the scalar line alone. An element $\tilde u$ with $\tilde u\star\tilde q=\tilde q$ for every $\tilde q$ would give $\tilde u\star e_0=u_0e_0=e_0$, hence $u_0=1$, and then $\tilde u\star e_1=u_1e_0=e_1$, which is impossible because $u_1e_0$ is scalar and $e_1$ is not.

*Proof.* The display is the theorem read at $\tilde q=e_0$; the unit argument is the one displayed. The same computation with the roles exchanged excludes a right unit, and an element invertible from both sides would be a unit.

**Corollary (no inverse).** No nonzero element of the block has an inverse: an inverse would be a unit of the multiplication, and the multiplication has none.

## The Block among the Six

The six products of *The 6 Products of the Quaternion Real Space* are generated from the two general products by symmetrisation and antisymmetrisation, and the block is one row of the catalogue *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

| code | product | $\tilde p\circ\tilde q$ | character |
|---|---|---|---|
| $\mathrm{GPA}$ | general plain | $\tilde p\tilde q$ | associative, unit $e_0$, division |
| $\mathrm{SPA}$ | symmetric plain | $\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ | commutative, Jordan, unit $e_0$ |
| $\mathrm{APA}$ | antisymmetric plain | $\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$ | alternating, no unit |
| $\mathrm{GQA}$ | general quaternionic | $\tilde p^{\natural}\tilde q$ | non-associative, left unit only |
| $\mathrm{SQA}$ | symmetric quaternionic | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | commutative, scalar valued, no unit |
| $\mathrm{AQA}$ | antisymmetric quaternionic | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | alternating, no unit |

**Remark (the position of the block).** The block is the symmetric part of the general quaternionic product, and its antisymmetric companion is $\mathrm{AQA}$; the two reconstruct $\mathrm{GQA}$ by the formula of §*The Operation*. It is one of the two commutative structures, the other being $\mathrm{SPA}$, and it is the only one whose values are scalar; the isolation is stated and proved in *The Specificities of the Symmetric Quaternionic Algebra*.

Over $\mathbb{R}$ the coefficient is definite, the block is $\mathbb{R}$-bilinear, and the reading of its zero divisors is the opposite extreme; the comparison is carried by the companion articles and not restated here.

## Summary

The symmetric quaternionic product is the operation $\tilde p\star\tilde q=\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)=N(\tilde p,\tilde q)e_0$, the pairing of the quaternion form placed on the scalar line. It is $\mathbb{R}$-bilinear, commutative and scalar valued, its table is the identity table $e_\mu\star e_\nu=\delta_{\mu\nu}e_0$, and its image is the whole scalar line $\mathbb{R}e_0$. It is not associative, not power-associative, not a Jordan product, not a Lie bracket and not alternating: the witnesses are $(e_1,e_1,e_0)$, the element $e_0+e_1$, the pair $(e_1,e_1)$ and the triple $(e_0,e_0,e_0)$. It has no unit, no one-sided unit and no inverse, and the element $e_0$ is a unit for the scalar line alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde q=q_0e_0+\mathbf q$ | a quaternion, with scalar part $q_0$ and vector part $\mathbf q$ |
| ${}^{\natural}$ | the quaternion conjugation $\tilde q^{\natural}=q_0e_0-\mathbf q$; the bar is the identity, the star coincides with ${}^{\natural}$ |
| $N(\tilde p,\tilde q)$ | the quaternion form $p_0q_0+\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$ |
| $B(\tilde p,\tilde q)$ | the plain form $p_0q_0-\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p\tilde q)$ |
| $\star$ | the symmetric quaternionic product $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)=N(\tilde p,\tilde q)e_0$ |
| $[\tilde p,\tilde q]_{\natural}$ | the quaternionic bracket $\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p$, the companion block $\mathrm{AQA}$ |
| $\circ$ | the generic product of another structure of the catalogue |

## Further Reading

- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six products and their owners
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the catalogue of the six structures and the $\mathrm{SQA}$ row
- *Introduction to the General Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternions.md`), for the parent product $\tilde p^{\natural}\tilde q$ and its left multiplications
- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for the antisymmetric companion and the reconstruction of the parent
- *Introduction to the Symmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternions.md`), for the other commutative structure, whose values are not scalar
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-quaternions.md`), for the invertibility criterion and the inverse formula
