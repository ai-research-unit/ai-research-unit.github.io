# __Norm and Invertibility in the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra of Quaternions*, and a degree-two Jordan algebra carries a norm with it. This article reads the **norm** of the block,

$$
N(\tilde q)=\tilde q\,\tilde q^{\natural}=q_0^2+|\vec q|^2,
$$

its polarisation, the quadratic identity that links it to the trace, the **Jordan inverse** and the criterion for the invertibility of an element, the failure of the invertible elements to form a group, the three-way classification of the elements, and the comparison with the plain algebra of the same space.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication from the plain product $\tilde p\tilde q$ and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

The norm and the criterion for the invertibility of the block are the same objects as those of the plain algebra, because the norm is read off the plain product and the unit; they are *Norm and Invertibility in the General Plain Algebra* for the plain product, and what this article adds is the reading of them on the Jordan product, where the inverse is the Jordan inverse and where the invertible elements do **not** form a group. The trace form, the other form of the block, is *The Trace Form and the Invariance of the Symmetric Plain Algebra*; the square and the quadratic representation are *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, so that $e_1^2=e_2^2=e_3^2=-e_0$. A generic element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $\vec p\cdot\vec q=\sum_kp_kq_k$ and $|\vec q|^2=\vec q\cdot\vec q$. The plain product, the quaternion norm, the unit group and the division property are those of *Introduction to the General Plain Algebra of Quaternions* and *Norm and Invertibility in the General Plain Algebra*.

## The Norm of the Block

### The Definition

**Definition.** The **norm** of the block is the quadratic map

$$
N(\tilde q)=\tilde q\,\tilde q^{\natural}=\tilde q^{\natural}\tilde q=q_0^2+|\vec q|^2 .
$$

It is the **algebraic norm** of the ambient algebra, read as the norm of the Jordan algebra. It agrees with the square of the Euclidean modulus, $N(\tilde q)=|\tilde q|^2$, and it is the generic norm of the degree-two Jordan algebra $\mathbb{H}^{\bullet}$.

**Proposition.** The norm is **positive definite** and **multiplicative** for the plain product:

$$
N(\tilde q)\geq 0,\qquad N(\tilde q)=0\iff\tilde q=0,\qquad N(\tilde p\tilde q)=N(\tilde p)N(\tilde q).
$$

*Proof.* $N(\tilde q)=q_0^2+|\vec q|^2$ is a sum of squares of real numbers, so it is non-negative and vanishes only when all the coordinates vanish; multiplicativity is the identity $(\tilde p\tilde q)(\tilde p\tilde q)^{\natural}=\tilde p\tilde q\tilde q^{\natural}\tilde p^{\natural}=\tilde p N(\tilde q)\tilde p^{\natural}=N(\tilde p)N(\tilde q)$ of the plain algebra, quoted from *Norm and Invertibility in the General Plain Algebra*.

The norm is **positive definite where the trace form is indefinite**. The trace form $\tau(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\bullet\tilde q)=p_0q_0-\vec p\cdot\vec q$ has signature $(1,3)$ and an isotropic cone; the norm has signature $(4,0)$ and no isotropic element but the origin. The two are different forms of the block, and the definiteness of the norm is the definite property of the block, whose underlying product is not formally real, as *The Specificities of the Symmetric Plain Algebra*, below this article in this category states and reconciles.

### The Polarisation

**Definition.** The **polarisation** of the norm is the symmetric bilinear form

$$
N(\tilde p,\tilde q)=\tfrac12\bigl(N(\tilde p+\tilde q)-N(\tilde p)-N(\tilde q)\bigr)=p_0q_0+\vec p\cdot\vec q .
$$

It is the **quaternion form** $\mathrm{Sc}(\tilde p^{\natural}\tilde q)$ of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, of Gram matrix $\mathrm{I}_4$ and signature $(4,0)$, positive definite.

**Proposition.** The norm is recovered from its polarisation, $N(\tilde q)=N(\tilde q,\tilde q)$, and the polarisation is non-degenerate.

*Proof.* Setting $\tilde p=\tilde q$ in the polarisation gives $N(\tilde q,\tilde q)=\tfrac12(4N(\tilde q)-2N(\tilde q))=N(\tilde q)$; the Gram matrix $\mathrm{I}_4$ is invertible.

**Remark (the norm is not the quadratic trace of the block).** The quadratic trace of the block is $\mathrm{Sc}(\tilde q\bullet\tilde q)=\mathrm{Sc}(\tilde q^2)=q_0^2-|\vec q|^2$, an indefinite quadratic form, whose polarisation is the trace form $\tau$. The norm $N$ and the quadratic trace differ in the sign of the vector part, and their polarisations are the two forms of the block: **the norm polarises to the quaternion form and the quadratic trace polarises to the trace form**.

### The Quadratic Identity

**Definition.** The **generic trace** of the block is the linear form

$$
T(\tilde q)=2\,\mathrm{Sc}(\tilde q)=2q_0,\qquad T(e_0)=2 .
$$

**Theorem (quadratic identity).** Every element of the block satisfies

$$
\tilde q^{\bullet2}-T(\tilde q)\tilde q+N(\tilde q)e_0=0,
\qquad\text{that is}\qquad
\tilde q^2-2q_0\tilde q+N(\tilde q)e_0=0 .
$$

*Proof.* With $\tilde q^{\bullet2}=\tilde q^2=(q_0^2-|\vec q|^2)e_0+2q_0\vec q$, the left-hand side is $\bigl[(q_0^2-|\vec q|^2)-2q_0^2+(q_0^2+|\vec q|^2)\bigr]e_0+(2q_0\vec q-2q_0\vec q)=0$.

The two coefficients $T$ and $N$ are the only degree-one and degree-two symmetric functions of the element that the block distinguishes, and the identity is the characteristic identity of the ambient degree-two algebra read on the Jordan product. It is the engine of the Jordan inverse below.

## The Jordan Inverse

### The Definition and the Criterion

**Definition.** An element $\tilde q$ is **invertible** when there is an element $\tilde q^{-1}$ with

$$
\tilde q\bullet\tilde q^{-1}=e_0
\qquad\text{and}\qquad
\tilde q^{\bullet2}\bullet\tilde q^{-1}=\tilde q .
$$

The element $\tilde q^{-1}$ is the **Jordan inverse** of $\tilde q$.

**Theorem (the inverse).** An element is invertible if and only if $N(\tilde q)\neq 0$, in which case its inverse is

$$
\tilde q^{-1}=\frac{T(\tilde q)e_0-\tilde q}{N(\tilde q)}=\frac{2q_0e_0-\tilde q}{N(\tilde q)}=\frac{\tilde q^{\natural}}{N(\tilde q)} .
$$

*Proof.* If $N(\tilde q)\neq0$ set $\tilde q^{-1}=(2q_0e_0-\tilde q)/N(\tilde q)$. Then $\tilde q\bullet\tilde q^{-1}=\bigl(2q_0\tilde q-\tilde q^{\bullet2}\bigr)/N(\tilde q)=N(\tilde q)e_0/N(\tilde q)=e_0$ by the quadratic identity, and $\tilde q^{\bullet2}\bullet\tilde q^{-1}=\bigl(2q_0\tilde q^{\bullet2}-\tilde q^{\bullet3}\bigr)/N(\tilde q)=\tilde q$, because $\tilde q^{\bullet3}=2q_0\tilde q^{\bullet2}-N(\tilde q)\tilde q$ from the identity multiplied by $\tilde q$. Conversely if $N(\tilde q)=0$ and $\tilde q\neq0$, then $\tilde q$ is a zero divisor by *Zero Divisors of the Symmetric Plain Algebra*, below this article in this category, so no inverse exists; and $N(0)=0$ with the two equations failing at the origin.

**Corollary (the criterion).** Since the norm is positive definite, the invertibility criterion is

$$
\tilde q\ \text{invertible}\iff \tilde q\neq 0 .
$$

**Every nonzero element of the block has a Jordan inverse.** The block is therefore a Jordan algebra of degree two in which the invertible set is as large as it can be.

### The Two-Sidedness of the Inverse

**Proposition.** The inverse is two-sided and involutive: $\tilde q\bullet\tilde q^{-1}=\tilde q^{-1}\bullet\tilde q=e_0$ and $(\tilde q^{-1})^{-1}=\tilde q$ for every nonzero $\tilde q$; the inverse is unique; and for a scalar multiple, $(a\tilde q)^{-1}=a^{-1}\tilde q^{-1}$ for $a\in\mathbb{R}^{\times}$.

*Proof.* The product is commutative, so the one equation gives the other. The second defining equation and the first characterise $\tilde q^{-1}$ uniquely once $N(\tilde q)\neq0$, by the first equation read with the norm. The scalar rule follows from $N(a\tilde q)=a^2N(\tilde q)$ and $T(a\tilde q)=aT(\tilde q)$.

**Remark (the inverse is not multiplicative).** The map $\tilde q\mapsto\tilde q^{-1}$ is not a homomorphism of the block: from $\tilde q\bullet\tilde q^{-1}=e_0$ and the failure of associativity it does not follow that $(p\bullet q)^{-1}=p^{-1}\bullet q^{-1}$, and the witness is the pair $p=e_1$, $q=e_2$, for which $p\bullet q=0$ has no inverse while $p^{-1}\bullet q^{-1}=(-e_1)\bullet(-e_2)=e_1\bullet e_2=0$. The failure is the group failure of the next section read on the inverse.

## The Invertible Elements

### The Failure of the Group of Units

The invertible elements of the block are all the nonzero elements. In the plain algebra they form the group $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$. In the block they do not.

**Proposition.** The set of invertible elements of the block is not closed under the product, and it is not a group:

$$
e_1\ \text{and}\ e_2\ \text{are invertible},\qquad e_1\bullet e_2=0\ \text{is not}.
$$

*Proof.* $N(e_1)=N(e_2)=1$, so both are invertible, with $e_1^{-1}=-e_1$ and $e_2^{-1}=-e_2$; and $e_1\bullet e_2=0$, whose norm is zero, so the product is not invertible. The product of two invertible elements has left the invertible set, so the set is not a semigroup, let alone a group.

**Remark (the contrast with the plain algebra).** In the plain algebra the invertible set is the group $\mathbb{H}^{\times}$, it is closed, and it carries the division property; in the block the two invertible elements $e_1$ and $e_2$ multiply to the non-invertible element $0$. **The division property of the ambient algebra does not pass to the Jordan product**, because the Jordan product of two units can fail to be a unit; the failure is exactly the presence of zero divisors, and it is why the block has a rich zero-divisor theory where the plain algebra has none.

### The Three-Way Classification

The norm and the invertibility split the nonzero elements into two kinds, and with the origin this is the three-way classification.

**Theorem.** Every element of the block falls into exactly one of three classes:

| class | representative | $N$ | $\tilde q^{-1}$ | zero divisor? |
|---|---|---|---|---|
| the origin | $0$ | $0$ | none | no |
| a nonzero pure element | $e_1$ | $>0$ | $-e_1$ | yes |
| a non-pure element | $e_0$ | $>0$ | $e_0$ | no |

*Proof.* The norm is positive definite, so the origin is the only element of norm zero, and it is the only non-invertible element. A nonzero element $\tilde q=q_0e_0+\vec q$ is a **zero divisor** exactly when $q_0=0$, that is, exactly when it is pure, by *Zero Divisors of the Symmetric Plain Algebra*; a nonzero pure element is therefore invertible **and** a zero divisor, while a non-pure element is invertible and not a zero divisor.

**Corollary.** In the block, invertibility and non-division are different properties: **every nonzero element is invertible, and yet the nonzero pure elements are zero divisors.** The two properties separate the nonzero elements into the two kinds of the table.

## The Comparison with the Plain Algebra

The two algebras of the same space are read side by side.

| | the plain algebra $\mathrm{GPA}$ | the symmetric plain algebra $\mathrm{SPA}$ |
|---|---|---|
| inverse | the two-sided algebra inverse $\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$ | the Jordan inverse $(2q_0e_0-\tilde q)/N(\tilde q)$ |
| criterion | $\tilde q\neq0$ | $\tilde q\neq0$ |
| invertible set | the group $\mathbb{H}^{\times}$ | the nonzero elements, not a group |
| zero divisors | none | the nonzero pure elements |
| nilpotents | none | none |
| norm | $N(\tilde q)=q_0^2+\lvert\vec q\rvert^2$, multiplicative | the same, and the generic norm of the block |

**Remark (what the change of product changes).** The norm, the inverse and the criterion are shared, because they are read off the plain product and the unit; what the Jordan product changes is the **closure** of the invertible set, hence the existence of zero divisors. The plain algebra is a division algebra and has no zero divisor; the block is a degree-two Jordan algebra with the same invertible elements and a family of zero divisors, because a product in it can pair an element with its conjugate direction and collapse.

## Summary

The norm of the block is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+|\vec q|^2$, positive definite and multiplicative for the plain product, polarising to the quaternion form $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$ of signature $(4,0)$; its companion is the trace form $p_0q_0-\vec p\cdot\vec q$ of signature $(1,3)$, the polarisation of the quadratic trace. The generic trace is $T(\tilde q)=2q_0$, the quadratic identity is $\tilde q^2-T(\tilde q)\tilde q+N(\tilde q)e_0=0$, and an element is invertible if and only if $N(\tilde q)\neq0$, that is, if and only if $\tilde q\neq0$, with Jordan inverse $\tilde q^{-1}=(T(\tilde q)e_0-\tilde q)/N(\tilde q)=\tilde q^{\natural}/N(\tilde q)$. The invertible elements are therefore all the nonzero elements, but they do not form a group: $e_1,e_2$ are invertible and $e_1\bullet e_2=0$ is not. The three classes are the origin, the nonzero pure elements, which are invertible and are the zero divisors, and the non-pure elements, which are invertible and are not; invertibility and division are different properties in the block, where in the plain algebra they coincide.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+\lvert\vec q\rvert^2$ | the norm of the block, the quaternion norm |
| $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$ | the polarisation of the norm, the quaternion form |
| $T(\tilde q)=2q_0$ | the generic trace |
| $\tilde q^2-T(\tilde q)\tilde q+N(\tilde q)e_0=0$ | the quadratic identity |
| $\tilde q^{-1}=(T(\tilde q)e_0-\tilde q)/N(\tilde q)=\tilde q^{\natural}/N(\tilde q)$ | the Jordan inverse |
| $\tilde q$ invertible $\iff N(\tilde q)\neq0\iff\tilde q\neq0$ | the invertibility criterion |
| the three classes | the origin, the nonzero pure elements, the non-pure elements |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product, its laws and its square.
- *Zero Divisors of the Symmetric Plain Algebra*, below this article in this category, for the criterion $q_0=0$ and the family of zero divisors.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category, for the quadratic representation, the idempotents and the fuller inverse theory.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra*, below this article in this category, for the other form of the block.
- *Norm and Invertibility in the General Plain Algebra*, for the same norm and criterion read on the plain product.
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, for the two forms and their signatures.
- *The Specificities of the Symmetric Plain Algebra*, below this article in this category, for the formal reality of $\mathbb{H}$ as a Jordan algebra.
