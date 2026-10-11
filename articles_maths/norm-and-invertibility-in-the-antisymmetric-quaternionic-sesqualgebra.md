# __Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

A unit of a product is an element that leaves every element fixed, an inverse is defined by an equation with the unit on the right side, and the group of units is the set of the invertible elements of a unital product; the algebraic norm is the quadratic form whose value at an element is the central value of its square. For the conjugate cross product

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}}
$$

of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* the three notions fail together, and they fail for one reason: **the unit of the parent algebra is a square-zero element of the block.** The block has no unit on either side, so no element is invertible and the group of units is empty; the block has no algebraic norm, so the criterion of invertibility by the non-vanishing of a norm is unavailable; and the notion of a regular element, which the corpus defines only in a unital product, has no referent.

An absence article of the corpus is written with the substitutes it hands over in place of the absent objects, and the substitutes here are three and they are computed. The **annihilators** of an element form a complex plane, so the left multiplication by a non-central element has a nontrivial kernel and a nontrivial image; the equation $\tilde A\diamond\tilde R=\tilde W$ is solvable exactly on the complex plane of the values orthogonal to the vector part of $\tilde A$ in the complex bilinear dot, and the solutions form a coset of the annihilator, so that the block has a **relative inverse** of complex dimension two on each of its elements; and the form-theoretic reading of a value is the **pairing** with the Krein form, $K(\tilde X\diamond\tilde Y,\tilde X\diamond\tilde Y)=-\lvert\tilde X\diamond\tilde Y\rvert^{2}$, which is the substitute for the norm of the value and is developed in *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*.

The definitions are *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*, with the unit table of the four general products, and the element theory that uses the substitutes is *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*; the invertibility criterion of the model block, where the norm exists, is *Norm and Invertibility in the General Plain Algebra*; the forms of the algebra are *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*, and the parent products are *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* and its symmetric companion.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$ and $e_k^2=-e_0$, a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_kQ_ke_k$, and the product $\diamond$ for the block. The left multiplication by $\tilde A$ is written $L_{\tilde A}$; the complex bilinear dot product of two vector parts is $(\mathbf{A},\mathbf{B})=\sum_kA_kB_k$; the algebraic norm of the biquaternion algebra is

$$
N(\tilde Q)=\sum_\mu Q_\mu^{2}=c(\tilde Q),
$$

the multiplicative form of the plain product, so that $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$ and $\tilde Q$ is invertible in the plain product exactly when $N(\tilde Q)\neq0$; the Krein form of the row is $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$.

## The Definitions, Relative to a Product

**Definition (unit).** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$; a **right unit** when $x\star e=x$ for every $x$; and a **two-sided unit**, or **identity**, when it is both. A product with a two-sided unit is **unital**, and the two-sided unit, when it exists, is unique.

**Definition (inverse and group of units).** Let $\star$ be a unital product with identity $e$. An element $x$ is **left-invertible of $\star$** when there is $y$ with $y\star x=e$; **right-invertible** when there is $y$ with $x\star y=e$; and **invertible** when there is $y$ with $x\star y=y\star x=e$. In an associative unital product the invertible elements form the **group of units**, and an element that is neither a left nor a right zero divisor is **regular**.

**Definition (algebraic norm).** A **norm** of a product $\star$ is a quadratic form $N_\star$ whose value at an element is the central value of its square, $\tilde X\star\tilde X=N_\star(\tilde X)e_0$, and which is multiplicative, $N_\star(x\star y)=N_\star(x)N_\star(y)$. For the plain product the norm exists and is the form $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ up to the sign, and it furnishes the invertibility criterion; the structure of the four norms of the algebra is *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*.

Throughout this article the product is the block $\diamond$, so that, unqualified, a unit, an inverse and a norm are read in the block, and the unit of the parent products is written $e_0$ as an element of the same space.

## The Unit

**Theorem (the block has no unit on either side).** The block has no left unit, no right unit and no two-sided unit.

*Proof.* A left unit $e$ must satisfy $e\diamond e_0=e_0$; but $e\diamond e_0=\mathbf{e}\times\overline{\mathbf{0}}=0$, since the vector part of $e_0$ is zero, so the equation reads $0=e_0$ and is false. A right unit $e$ must satisfy $e_0\diamond e=e$; but $e_0\diamond e=\mathbf{0}\times\overline{\mathbf{e}}=0$, so the equation reads $0=e$ and is false for a nonzero $e$, while the origin satisfies it only at the element zero.

**Remark (the absence is inherited from the row).** The four general products have the unit table of *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*: the plain product has the two-sided unit $e_0$, the natural product has the left unit $e_0$ alone, the plain sesquilinear product has the right unit $e_0$ alone, and the quaternionic sesquilinear product has none on either side. The row of the block is the last one, so the block inherits the absence of the unit from its parent product, and the antisymmetrisation cannot create one: an antisymmetric product of two central elements is zero, while a unit would have to reproduce the central elements. Of the twelve, only the plain product and its symmetric half are unital, and the block is not among them.

**Remark (the unit is a square-zero element).** The failure of the identity equations is not a subtle one: the unit of the parent algebra satisfies $e_0\diamond e_0=0$ in the block, so it is not merely a non-unit, it is a nilpotent of index two. The whole scalar line shares the reading, $\lambda e_0\diamond\lambda e_0=0$, and the centre is annihilated by the block in both slots, so that the central line, which is the line of the units of the algebras and of the largest annihilator of the general products, is the line of the square-zero elements of the block. The reading is the element-theoretic form of the split, and it is recorded in *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*.

## The Absence of the Inverse and of the Regular Element

**Corollary (no element is invertible).** No element of the block is left-invertible, right-invertible or invertible, and the group of units of the block is empty.

*Proof.* The three definitions of the inverse are equations with the unit of the product on the right side, and the block has no unit on either side by the theorem above, so the equations cannot be written down. The statement is not vacuous and it is not a statement about the elements: it is the statement that the class of the invertible elements of the block is empty, and that the group of units, the object through which the algebra of the model block is read, has no referent for the block.

**Corollary (no element is regular).** The notion of a regular element is defined for a unital product alone, so the block has no regular and no non-regular element; the dichotomy of the element theory of the corpus is not available to it, and the only reading is the pair of annihilators and the relative inverse below.

**Remark (the zero divisors are everything).** The reader of the absence is the size of the zero-divisor set: in the model block the zero divisors are the elements of vanishing norm and the generic element is invertible, while in the block every nonzero element is a two-sided zero divisor, as *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra* proves. The two statements are the same statement read twice: the block has no unit and therefore no inverse, and every multiplication by a fixed nonzero element has a nonzero kernel, so the information of the factor is lost at every step. The quantification of the loss is the dimension of the annihilator, which is the next section.

## The Substitutes

**The annihilators.** For a non-central element $\tilde A$ the two annihilators coincide in the complex plane

$$
A_\diamond(\tilde A)=B_\diamond(\tilde A)=\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf{A}},
$$

of complex dimension two and real dimension four; for a central element they are the whole space. They are the kernels of the two one-sided multiplications, they replace the group of units as the incoming data of the element theory, and their computation is *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*.

**The relative inverse.** The left multiplication by a non-central element,

$$
L_{\tilde A}\tilde R=\mathbf{A}\times\overline{\mathbf{R}},
$$

has the annihilator $A_\diamond(\tilde A)$ as its kernel and the complex plane of the values orthogonal to the vector part of $\tilde A$ in the complex bilinear dot as its image,

$$
\mathrm{im}\,L_{\tilde A}=\{\tilde W:\mathbf{W}\in\mathrm{Vect}(\mathbb{B}),\ (\mathbf{W},\mathbf{A})=0\},
$$

so that the equation $\tilde A\diamond\tilde R=\tilde W$ has a solution exactly when $\tilde W$ lies on that plane, and the set of its solutions is then a coset of the kernel. The two spaces have complex dimension two, and the left multiplication induces a conjugate-linear bijection of the quotient of the space by the kernel onto the image: the block has no inverse, and it has a relative inverse in which each non-central element acts invertibly between two spaces of dimension two, the loss and the gain being accounted by the kernel and the image.

**The pairing of the values.** The substitute for the norm of an element is the reading of the value through the form of the row: for the Krein form,

$$
K(\tilde X\diamond\tilde Y,\tilde X\diamond\tilde Y)=-\lvert\tilde X\diamond\tilde Y\rvert^{2}\leq0 ,
$$

with equality exactly on the values of the cone of the diagonal. The self-pairing of a value is therefore the negative of a non-negative real number, and the pairing is the only quadratic reading the block carries: it is defined on the values and not on the elements, and it is developed, with the Gram matrix of the values and the invariant forms, in *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*.

**Remark (the operators and their adjoints).** The left multiplication has a second reading, in which the absence of the inverse is the presence of the adjoint: for the Krein form the adjoint of the left multiplication is its negative, so that the operator is skew with respect to the form of the row, and the pairing of an element and its conjugate is conserved. The operator theory of the block is *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, and it is the operator form of the annihilation pair $(\tilde A,\overline{\tilde A})$ of the element theory.

## The Absence of the Norm

**Theorem (the block has no algebraic norm).** There is no quadratic form $N_\diamond$ on $\mathbb{B}$ with $\tilde X\diamond\tilde X=N_\diamond(\tilde X)e_0$ for every $\tilde X$, and there is no multiplicative form on $\mathbb{B}$ extending the norm of the algebra to the block: the square of an element is never a nonzero central value, and the norm of the algebra fails the multiplicativity at the block.

*Proof.* The square of an element is the conjugate cross product $\mathbf{X}\times\overline{\mathbf{X}}$, a pure vector for every $\tilde X$, so that the equation $\tilde X\diamond\tilde X=N_\diamond(\tilde X)e_0$ holds only where the square vanishes, that is on the cone of the diagonal, and the form would be forced to vanish there and to be undefined outside: no quadratic form meets the equation. For the second statement it is enough to read one pair, $\tilde X=\tilde Y=e_1$: the square is $e_1\diamond e_1=0$, so $N(e_1\diamond e_1)=N(0)=0$, while $N(e_1)N(e_1)=1$, and the multiplicativity fails.

**Remark (the square has no polarisation).** The absence of the norm is the absence of the polarisation of the square. For a product in which the square is the restriction of a quadratic form, the symmetrisation $\tilde X\star\tilde Y+\tilde Y\star\tilde X$ is the polarisation and is a symmetric bilinear form; for the block the symmetrisation is the sesquilinear expression $\mathbf{X}\times\overline{\mathbf{Y}}+\mathbf{Y}\times\overline{\mathbf{X}}$, which is conjugate-linear in the second slot and therefore not the polarisation of a quadratic form. The block carries a sesquilinear product and no quadratic form, and the only quadratic object of the block is the pairing of its values through the form of the row.

**Remark (what the model block uses the norm for).** In the plain product the norm is used three times: it defines the scalar coordinate of the product, it gives the invertibility criterion $N(\tilde Q)\neq0$, and it defines the norm of an element as the value of the form at the element, $N(\tilde Q)=(\tilde Q,\tilde Q)$ in the bilinear reading. The block replaces the three uses by three readings: the scalar coordinate of the product is identically zero, the invertibility criterion is replaced by the relative inverse on the plane of the values, and the norm of an element is replaced by the self-pairing of the value, which is the negative of a non-negative real number and is read on the values alone. The comparison of the three replacements with the criterion of the parent products is *Comparison Between the Four General Products*, and the criterion of the model block is *Norm and Invertibility in the General Plain Algebra*.

## The Comparison with the Other Products

| product | unit | invertibility criterion | the norm |
|---|---|---|---|
| $\tilde P\tilde Q$ | $e_0$, two-sided | $c(\tilde P)\neq0$ | $B$ |
| $\tilde P^{\natural}\tilde Q$ | $e_0$, left only | one-sided only | $N=c$ |
| $\tilde P\tilde Q^{*}$ | $e_0$, right only | one-sided only | $H$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | none on either side | none | $K$ |
| the block $\mathbf{P}\times\overline{\mathbf{Q}}$ | none on either side | none; the relative inverse instead | none; the pairing of the values instead |

The table is read with the unit table of the four general products of the definitions of the corpus, with the criterion $c(\tilde P)=\sum_\mu P_\mu^{2}$ of *Norm and Invertibility in the General Plain Algebra*, and with the four algebraic norms $B$, $N$, $H$, $K$ of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*, each the diagonal of the form of its product; only $N$ is multiplicative, and the block, whose product has no scalar part, carries no algebraic norm at all. The block is the only row in which all three entries fail, and its zero-divisor set is the whole punctured space, as large as a zero-divisor set can be, against the cone of the four general products, so that the table is the form-theoretic form of the extremity of the block: the antisymmetric part of the sesquilinear product has neither unit nor inverse nor norm, and it has the annihilators, the relative inverse and the pairing in their place.

## Summary

The block has no unit on either side, so no element of it is invertible and the group of units is empty; the notion of a regular element is unavailable, since it is defined only in a unital product; and the block has no algebraic norm, since the square of an element is never a nonzero central value and the norm of the algebra fails the multiplicativity at the block, the pair of the element $e_1$ with itself being the witness. The unit of the parent algebra is a square-zero element of the block, and the whole central line is annihilated by the block in both slots. The substitutes are three: the annihilators, which are complex planes of real dimension four for every non-central element and the whole space for the central ones; the relative inverse, in which the left multiplication by a non-central element is a conjugate-linear bijection of a quotient of the space onto the plane of the values orthogonal to its vector part, so that the equation $\tilde A\diamond\tilde R=\tilde W$ is solvable exactly on that plane and the solutions form a coset of the annihilator; and the pairing of the values with the Krein form, whose self-pairing is the negative of a non-negative real number. The comparison with the four general products is the table in which the block is the only row with no unit, no invertibility criterion and no norm.

## Summary of Notation

| symbol | meaning |
|---|---|
| $e\star x=x$, $x\star e=x$ | the two identity equations of the unit |
| $e_0$ | the unit of the plain product, a square-zero element of the block |
| $A_\diamond(\tilde A)=B_\diamond(\tilde A)=\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf{A}}$ | the common annihilator, of complex dimension two |
| $L_{\tilde A}\tilde R=\mathbf{A}\times\overline{\mathbf{R}}$ | the left multiplication by $\tilde A$ |
| $(\mathbf{W},\mathbf{A})=0$ | the image of $L_{\tilde A}$, the plane of the solvable values |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the norm of the algebra, not a norm of the block |
| $K(\tilde X\diamond\tilde Y,\tilde X\diamond\tilde Y)=-\lvert\tilde X\diamond\tilde Y\rvert^{2}$ | the self-pairing of a value |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*, for the unit, the one-sided inverse, the group of units and the unit table of the four general products.
- *Norm and Invertibility in the General Plain Algebra*, for the model block, where the norm exists and the invertibility criterion is the non-vanishing of the central square.
- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*, for the norms of the four general products.
- *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*, for the annihilators, the relative inverse and the zero-divisor set of the block.
- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, for the pairing of the values, which replaces the norm.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, for the left multiplications and their adjoints.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, for the row whose antisymmetric part the block is, and the absence of the unit it inherits.
