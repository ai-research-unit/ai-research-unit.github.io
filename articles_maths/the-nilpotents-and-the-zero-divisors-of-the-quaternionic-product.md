
# __The Nilpotents and the Zero Divisors of the Quaternionic Product__

## Introduction

The product of this group is the **complex quaternionic bilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q , \qquad \tilde P^{\natural} = P_0 - \mathbf P ,
$$

the second of the four products of the biquaternion algebra $\mathbb{B}$ (*The Four Biquaternion Complex Products* §*The Complex Quaternionic Bilinear Product*), whose algebra and whose left unit are *Biquaternions as a Quaternionic Algebra over $\mathbb{C}$*. Its square is central,

$$
\tilde Q\star\tilde Q = N(\tilde Q)\,e_0 , \qquad N(\tilde Q) = Q_0^2+Q_1^2+Q_2^2+Q_3^2 ,
$$

and the previous article (*Idempotents of the Quaternionic Product*) read that equation when the square is required to return the element. This article reads the other value, the square equal to $0$.

The equation $N(\tilde Q) = 0$ is the vanishing of the complex quadratic form that the algebra carries, and its nonzero solutions are the **zero divisors** of $\mathbb{B}$; this is why the answer here is so different from the answer for the associative multiplication, whose square-zero elements are the pure isotropic vectors alone. The article establishes four things. First, the equivalence

$$
\tilde Q\star\tilde Q = 0 \iff N(\tilde Q) = 0 \iff \tilde Q = 0 \ \text{or} \ \tilde Q \ \text{is a zero divisor of } \mathbb{B} ,
$$

so the square-zero elements of $\star$ are exactly the elements of norm zero. Second, that set is a real cone of dimension six and not a subspace. Third, the left and the right annihilator of an element with respect to $\star$ each have complex dimension two when the element is a zero divisor and dimension zero when it is a unit. Fourth, and least expected, the two annihilators **coincide for every element**, unit or zero divisor alike, because the natural conjugation is an involutive anti-automorphism and exchanges them.

## The Square-Zero Equation

**Theorem (square-zero).** For $\tilde Q \in \mathbb{B}$,

$$
\tilde Q\star\tilde Q = 0 \iff N(\tilde Q) = 0 .
$$

**Proof.** By the square lemma of *Idempotents of the Quaternionic Product*, $\tilde Q\star\tilde Q = N(\tilde Q)e_0$, and $e_0 \neq 0$, so the left side vanishes exactly when the coefficient $N(\tilde Q)$ does. $\square$

The criterion for a zero divisor of the algebra is the companion statement.

**Theorem (unit criterion).** An element $\tilde Q$ of $\mathbb{B}$ is a unit if and only if $N(\tilde Q) \neq 0$, and if $N(\tilde Q) = 0$ with $\tilde Q \neq 0$ then $\tilde Q$ is a zero divisor of the algebra; the inverse is $\tilde Q^{-1} = \tilde Q^{\natural}/N(\tilde Q)$ when it exists.

**Proof.** The natural conjugation satisfies $\tilde Q\tilde Q^{\natural} = \tilde Q^{\natural}\tilde Q = N(\tilde Q)e_0$ and is an anti-automorphism, so if $N(\tilde Q)\neq0$ the displayed element is a two-sided inverse. If $N(\tilde Q)=0$ and $\tilde Q\neq0$, then $\tilde Q^{\natural}\neq0$ and $\tilde Q^{\natural}\tilde Q = 0$ exhibits a nonzero product equal to zero. The detail is *Biquaternion Norm and Invertibility* and *Biquaternion Zero Divisors*. $\square$

Combining the two theorems gives the equivalence that names the article.

**Theorem (square-zero elements are the zero divisors).** For a nonzero $\tilde Q \in \mathbb{B}$,

$$
\tilde Q\star\tilde Q = 0 \iff \tilde Q \ \text{is a zero divisor of } \mathbb{B} .
$$

The square-zero elements of $\star$ are therefore $0$ together with the whole zero-divisor set of the algebra.

**Proof.** By the square-zero theorem $\tilde Q\star\tilde Q = 0$ is $N(\tilde Q) = 0$, and by the unit criterion $N(\tilde Q) = 0$ is exactly the zero-divisor condition for $\tilde Q \neq 0$. $\square$

This is the sharpest contrast of the group with the associative multiplication. There the square is $\tilde Q\tilde Q = Q_0^2e_0 + 2Q_0\mathbf Q + \mathbf Q^2$, and its vanishing forces $Q_0 = 0$ and $(\mathbf Q,\mathbf Q) = 0$: the square-zero elements of the plain product are the **pure** isotropic vectors, a real cone of dimension four, and they are a proper subset of the zero divisors (*Comparison Between the Four Biquaternion Products* §*The Squares, the Idempotents and the Roots*). Reading the first slot through ${}^{\natural}$ removes the scalar term from the square — the two copies of $Q_0\mathbf Q$ cancel and the scalar part becomes the signless sum — and the square-zero set expands to the whole zero-divisor cone.

**Example.** The Hermitian projector $\tilde\Pi_+(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ over a real unit vector $\hat\mu$ has norm
$$
N(\tilde\Pi_+) = \tfrac14\bigl(1+(i\hat\mu,i\hat\mu)\bigr) = \tfrac14\bigl(1-(\hat\mu,\hat\mu)\bigr) = 0 ,
$$
in agreement with the square $\tilde\Pi_+\star\tilde\Pi_+ = 0$ of the previous article. It is a zero divisor of the algebra, and its plain square is the projector itself; the two products see the same element as a projector and as a nilpotent.

## The Cone of Norm Zero

**Definition.** The **nilpotent cone** of the quaternionic product is the vanishing set of the norm,

$$
C = \{\tilde Q \in \mathbb{B} : N(\tilde Q) = 0\} = \{\tilde Q : \tilde Q\star\tilde Q = 0\} .
$$

**Proposition (shape).** The cone $C$ is a real algebraic cone of real dimension $6$ in the real eight-dimensional space $\mathbb{B}$, and it is not a real subspace.

**Proof.** With $Q_\mu = q_\mu + iq'_\mu$ the real and imaginary parts, $N = \sum_\mu Q_\mu^2 = \sum_\mu (q_\mu^2 - q'_\mu{}^2) + 2i\sum_\mu q_\mu q'_\mu$ is one complex equation, that is two real equations, and the set is a cone because $N$ is homogeneous of degree two; the two equations are independent off $0$, so the real dimension is $8-2 = 6$. For the failure of linearity, the elements $e_1+ie_2$ and $e_1-ie_2$ both have norm $1-1 = 0$, while their sum $2e_1$ has norm $4$. $\square$

**Corollary.** The cone is closed under multiplication by the product and under multiplication by complex scalars: for any $\tilde P$ and any $\tilde Q$ with $N(\tilde Q) = 0$,

$$
N(\tilde P\star\tilde Q) = N(\tilde P)N(\tilde Q) = 0 ,
$$

so the cone together with $0$ is a multiplicative set, and it is closed under multiplication by every element on either side.

**Proof.** The biquaternion norm is multiplicative for the plain product and invariant under ${}^{\natural}$, so $N(\tilde P^{\natural}\tilde Q) = N(\tilde P^{\natural})N(\tilde Q) = N(\tilde P)N(\tilde Q)$ (*Biquaternion Norm and Invertibility* §*Multiplicativity*); the statement follows on evaluating at $N(\tilde Q) = 0$. $\square$

**The two families of zero divisors.** The cone was described in the algebra by *Biquaternion Zero Divisors* as the union of two families: the **pure** zero divisors, the vectors $\mathbf P \neq 0$ with $(\mathbf P,\mathbf P)=0$, and the **non-pure** ones, the complex multiples of the Hermitian projectors. In the quaternionic product the distinction is invisible at the level of the square — every element of the cone has square zero, pure or not — but it is visible at the level of the plain square: a pure zero divisor has $\mathbf P^2 = -(\mathbf P,\mathbf P)e_0 = 0$, while a non-pure one, being a multiple of a projector, has a nonzero plain square. The displacement of the previous article is this sentence read in reverse: the nontrivial idempotents of the algebra, which are the non-pure zero divisors, are exactly the Hermitian projectors that the quaternionic square sends to $0$.

## The Annihilators

**Definition.** For $\tilde Q \in \mathbb{B}$ the **left annihilator** and the **right annihilator** with respect to $\star$ are

$$
\mathrm{Ann}_\ell(\tilde Q) = \{\tilde X \in \mathbb{B} : \tilde X\star\tilde Q = 0\} = \{\tilde X : \tilde X^{\natural}\tilde Q = 0\} ,
$$

$$
\mathrm{Ann}_r(\tilde Q) = \{\tilde X \in \mathbb{B} : \tilde Q\star\tilde X = 0\} = \{\tilde X : \tilde Q^{\natural}\tilde X = 0\} .
$$

Both are $\mathbb{C}$-subspaces, because the product is $\mathbb{C}$-linear in each slot and the conjugation ${}^{\natural}$ is $\mathbb{C}$-linear.

The two sets are the kernels of the two one-sided multiplication maps, read through the conjugation. Since $X\mapsto X^{\natural}$ is a bijection of $\mathbb{B}$, the left annihilator is the image under ${}^{\natural}$ of the set $\{\tilde Y : \tilde Y\tilde Q = 0\}$, the kernel of right multiplication by $\tilde Q$ in the ordinary product, and its dimension is therefore governed by the rank of that multiplication in the algebra.

**Theorem (dimension of the annihilators).** Let $\tilde Q \in \mathbb{B}$.

- If $\tilde Q$ is a unit, $N(\tilde Q) \neq 0$, then $\mathrm{Ann}_\ell(\tilde Q) = \mathrm{Ann}_r(\tilde Q) = 0$.
- If $\tilde Q \neq 0$ is a zero divisor, $N(\tilde Q) = 0$, then $\mathrm{Ann}_\ell(\tilde Q)$ and $\mathrm{Ann}_r(\tilde Q)$ are each of complex dimension two, and each contains $\tilde Q$.

**Proof.** The left annihilator is $\{\tilde X : \tilde X^{\natural}\tilde Q = 0\} = \{ \tilde Y^{\natural} : \tilde Y\tilde Q = 0\}$; the substitution $\tilde Y = \tilde X^{\natural}$ is a bijection, so its dimension is the dimension of the kernel of right multiplication by $\tilde Q$ in the associative algebra, which is $4-\operatorname{rank}(R_{\tilde Q})$. The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, so $\operatorname{rank}(R_{\tilde Q})$ is $4$ for a unit and $2$ for a nonzero zero divisor; hence the dimensions $0$ and $2$. For the right annihilator the same argument with left multiplication, whose rank is the same. Finally, if $N(\tilde Q) = 0$ then $\tilde Q^{\natural}\tilde Q = 0$, so $\tilde Q \in \mathrm{Ann}_\ell(\tilde Q)$, and $\tilde Q\tilde Q^{\natural} = 0$, so $\tilde Q \in \mathrm{Ann}_r(\tilde Q)$. $\square$

The fact that a zero divisor annihilates itself on both sides is the statement that the two maps $\tilde X \mapsto \tilde X\star\tilde Q$ and $\tilde X \mapsto \tilde Q\star\tilde X$ both have $\tilde Q$ in their kernel; it is the reason the annihilators are the natural two-dimensional objects attached to a cone point, and it is what makes the next theorem possible.

## The Two Annihilators Coincide

For an arbitrary non-associative product the two annihilators of an element have no reason to be equal. Here they always are.

**Theorem (coincidence).** For **every** $\tilde Q \in \mathbb{B}$, unit or zero divisor alike,

$$
\mathrm{Ann}_\ell(\tilde Q) = \mathrm{Ann}_r(\tilde Q) .
$$

**Proof.** Let $\tilde X \in \mathbb{B}$. Applying the involution ${}^{\natural}$ to the equation $\tilde X^{\natural}\tilde Q = 0$ gives $(\tilde X^{\natural}\tilde Q)^{\natural} = 0$, and since ${}^{\natural}$ is an anti-automorphism of order two this is $\tilde Q^{\natural}\tilde X = 0$; the argument reverses because ${}^{\natural}$ is a bijection. Hence

$$
\tilde X\star\tilde Q = 0 \iff \tilde X^{\natural}\tilde Q = 0 \iff \tilde Q^{\natural}\tilde X = 0 \iff \tilde Q\star\tilde X = 0 ,
$$

so the two annihilators contain exactly the same elements. $\square$

**Corollary.** The two-sided annihilator of a zero divisor, $\mathrm{Ann}(\tilde Q) = \mathrm{Ann}_\ell(\tilde Q) = \mathrm{Ann}_r(\tilde Q)$, is the set of elements $\tilde X$ that annihilate $\tilde Q$ on both sides, and it is a two-dimensional $\mathbb{C}$-subspace. An element is a unit exactly when its two-sided annihilator is $0$.

The coincidence is a property of the specific product: it holds because ${}^{\natural}$ is a **$\mathbb{C}$-linear** anti-automorphism of order two, so that the first factor can be conjugated away without changing the annihilation. The two sesquilinear products of the chapter carry the conjugate-linear Hermitian conjugation in their slot instead, and the corresponding statement there is theirs to make; it is not a general property of an algebra with an involution.

**Example.** For the pure zero divisor $\tilde Q = e_1+ie_2$, whose vector part is $\mathbf Q = e_1+ie_2$ with $(\mathbf Q,\mathbf Q) = 1-1 = 0$, the common annihilator is

$$
\mathrm{Ann}(e_1+ie_2) = \mathbb{C}\{e_1+ie_2,\ e_3-ie_0\} ,
$$

and for the non-pure zero divisor $\tilde Q = e_0+ie_1$, of norm $1-1 = 0$,

$$
\mathrm{Ann}(e_0+ie_1) = \mathbb{C}\{e_0+ie_1,\ e_2+ie_3\} .
$$

In both cases the element $\tilde Q$ lies in its own annihilator, and the annihilator is a two-dimensional $\mathbb{C}$-subspace; the two bases are read off the multiplication table and verified by multiplication.

## The Square-Zero Elements of the Four Products

The square of an element, and hence its square-zero set, separates the four products of the chapter (*Comparison Between the Four Biquaternion Products* §*The Squares, the Idempotents and the Roots*):

| product | square-zero elements |
|---|---|
| $\tilde P\tilde Q$ | the pure isotropic cone $\{P_0 = 0,\ (\mathbf P,\mathbf P) = 0\}$ |
| $\tilde P^{\natural}\tilde Q$ | the whole nilpotent cone $\{N(\tilde P) = 0\}$ |
| $\tilde P\tilde Q^{*}$ | only $0$ |
| $\tilde P^{\natural}\tilde Q^{*}$ | a proper subset of $\{N(\tilde P) = 0\}$ |

The quaternionic column is this article, and it is the largest of the four: it contains both the pure isotropic cone of the first column and the displaced Hermitian projectors, and it is the whole zero-divisor set of the algebra. The comparison article owns the table; the present article owns the equivalence of its second column with the zero divisors, the cone and the annihilators.

## Summary

In the complex quaternionic bilinear product the square of an element is the central element $N(\tilde Q)e_0$, so the square-zero elements are exactly the elements of norm zero. These are $0$ together with the zero divisors of the algebra, and the unit criterion converts the square equation into the divisibility condition; the set is a real cone of dimension six, the light cone of the complex quadratic form $\sum_\mu Q_\mu^2$, and it is closed under multiplication by the product and by scalars. For a zero divisor the left and the right annihilator are each a complex plane containing the element; for a unit both are $0$. The two annihilators coincide for every element, a consequence of the natural conjugation being a $\mathbb{C}$-linear anti-automorphism of order two; this is peculiar to the $\natural$-product and fails for the two sesquilinear products, whose annihilators are exchanged by the conjugation instead. The whole cone is the square-zero set of the product, which is the sharpest contrast of this group with the associative multiplication, whose square-zero elements are the pure isotropic vectors alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2 = -e_0$ |
| $\tilde Q = \sum_\mu Q_\mu e_\mu$ | an element and its four complex coordinates |
| $\mathbf Q = \sum_{k=1}^{3}Q_ke_k$ | the vector part |
| $(\mathbf Q,\mathbf Q)$ | the complex bilinear dot product $\sum_k Q_k^2$ |
| ${}^{\natural}$ | the natural conjugation $\tilde Q^{\natural} = Q_0 - \mathbf Q$ |
| $N(\tilde Q) = \tilde Q^{\natural}\tilde Q = \sum_\mu Q_\mu^2$ | the norm of the algebra |
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q$ | the complex quaternionic bilinear product, the multiplication of this group |
| $C = \{\tilde Q : N(\tilde Q) = 0\}$ | the nilpotent cone, the square-zero set |
| $\tilde\Pi_+(\hat\mu) = \tfrac12(e_0+i\hat\mu)$ | the Hermitian projector over a real unit vector $\hat\mu$ |
| $\mathrm{Ann}_\ell(\tilde Q)$, $\mathrm{Ann}_r(\tilde Q)$ | the left and the right annihilator of $\tilde Q$ for the product $\star$ |
| $\mathrm{Ann}(\tilde Q)$ | their common value, the two-sided annihilator |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for nilpotent elements and zero divisors in a non-associative algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for isotopes and homotopes and the way a change of product moves the zero divisors.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the anti-automorphism of an algebra and the conjugation of a product.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for annihilators in a ring with an involution and the symmetry that an anti-automorphism imposes on them.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the isotropic vectors of the complex quaternion algebra and the quadratic form $\sum_\mu Q_\mu^2$.
