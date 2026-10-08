# __Hermitian and Skew-Hermitian Elements__

## Introduction

An involution is an operation of order two, and an operation of order two singles out the part of its domain it fixes and the part it negates. Applied to the $\varsigma$-semilinear involution of a sesqualgebra, this gives the two sets studied here, the **Hermitian elements** and the **skew-Hermitian elements**, and they are the two halves of the algebra; the two coincide in characteristic two, as the failure theorem below shows.

The setting and the notation are those of *Sesqualgebras*: $A$ is an $R$-algebra with a product additive in each variable, $R$-linear in the first variable and $\varsigma$-semilinear in the second, and $*$ is the $\varsigma$-semilinear involution of $A$. The feature that distinguishes this layer from the bilinear one appears at once: the base involution $\varsigma$ need not be the identity, and the two halves of $A$ are then not $R$-submodules but only modules over the fixed ring $R^{\varsigma}$.

What is added here: the definition of the two sets and their closure properties, the decomposition of the algebra into the two halves and its failure when $2$ is not invertible, the symmetrised product on the Hermitian part and the commutator on the skew-Hermitian part, and the splitting of the sesquilinear product over the two halves. The Lie algebra carried by the skew-Hermitian part is developed in *The Unitary Lie Algebra*, and the elements of the form $x^{*}x$ are the subject of *Hermitian Squares and the Algebraic Positive Cone*.

## The Fixed and Anti-Fixed Sets

### Definition

**Definition.** Let $A$ be a sesqualgebra with involution $*$. The **Hermitian elements** and the **skew-Hermitian elements** of $A$ are the sets

$$
H(A) = \{x \in A : x^{*} = x\}, \qquad S(A) = \{x \in A : x^{*} = -x\} .
$$

**Remark.** The two sets are the fixed set and the anti-fixed set of the involution. Both contain $0$, and both are closed under addition; when the halving of an element is available their sum is the whole algebra, as the decomposition theorem below shows. An element of $H(A)$ is called **Hermitian**, or **self-adjoint** with respect to $*$; an element of $S(A)$ is called **skew-Hermitian**, or **anti-self-adjoint**.

### The Scalar Action

**Proposition.** $H(A)$ and $S(A)$ are closed under addition, and they are closed under the scalars of the fixed ring $R^{\varsigma} = \{\lambda \in R : \varsigma(\lambda) = \lambda\}$, so that both are $R^{\varsigma}$-submodules of $A$. A scalar $\lambda$ with $\varsigma(\lambda) = -\lambda$ sends $H(A)$ into $S(A)$ and $S(A)$ into $H(A)$.

**Proof.** For $h, h' \in H(A)$, $(h + h')^{*} = h^{*} + h'^{*} = h + h'$, and for $s, s' \in S(A)$, $(s + s')^{*} = -s - s'$. For $\lambda \in R^{\varsigma}$ and $h \in H(A)$, $(\lambda h)^{*} = \varsigma(\lambda) h^{*} = \lambda h$, so $\lambda h \in H(A)$; the calculation for $S(A)$ is the same with $\varsigma(\lambda) = \lambda$ and a sign. For $\lambda$ with $\varsigma(\lambda) = -\lambda$, $(\lambda h)^{*} = \varsigma(\lambda) h^{*} = -\lambda h$, so $\lambda h \in S(A)$, and $(\lambda s)^{*} = \varsigma(\lambda) s^{*} = (-\lambda)(-s) = \lambda s$, so $\lambda s \in H(A)$. $\square$

**Remark.** The closure under addition needs nothing of the scalars, but the closure under scalars is governed by an annihilator: the $\lambda$ with $\lambda H(A) \subseteq H(A)$ are exactly those with $(\varsigma(\lambda) - \lambda)H(A) = 0$. That set always contains the fixed ring $R^{\varsigma}$, and it equals it when $H(A)$ has zero annihilator in $R$, over an integral domain for instance; over a ring with zero divisors it can be strictly larger, and the counterexample is in *The Unitary Lie Algebra*, §*The Scalars*. In the model $A = M_n(\mathbb{C})$ with $\varsigma(z) = \bar z$ and the conjugate transpose, $H(A)$ is the space of the Hermitian matrices, which is a real vector space and not a complex one, and multiplication by $i$ is the scalar with $\varsigma(\lambda) = -\lambda$ that carries it to the skew-Hermitian matrices.

## The Decomposition

### The Two Halves

**Theorem (the decomposition into the two halves).** Suppose $2$ is invertible in $R$. Then $H(A) \cap S(A) = 0$, and every $x \in A$ has the unique decomposition

$$
x = \frac{x + x^{*}}{2} + \frac{x - x^{*}}{2}, \qquad \frac{x + x^{*}}{2} \in H(A), \qquad \frac{x - x^{*}}{2} \in S(A) ,
$$

so that $A = H(A) \oplus S(A)$ as $R^{\varsigma}$-modules.

**Proof.** Put $h = (x + x^{*})/2$ and $s = (x - x^{*})/2$. The involution is additive and $*^{2} = \mathrm{id}$, so

$$
h^{*} = \frac{x^{*} + x}{2} = h, \qquad s^{*} = \frac{x^{*} - x}{2} = -s ,
$$

hence $h \in H(A)$ and $s \in S(A)$, and $h + s = x$ by inspection. For the intersection, if $x \in H(A) \cap S(A)$ then $x = x^{*} = -x$, so $2x = 0$ and $x = 0$ because $2$ is invertible. For the uniqueness, if $h + s = h' + s'$ with $h, h' \in H(A)$ and $s, s' \in S(A)$, then $h - h' = s' - s \in H(A) \cap S(A) = 0$. The scalar $\tfrac12$ lies in $R^{\varsigma}$ because $\varsigma(2^{-1}) = \varsigma(2)^{-1} = 2^{-1}$, so each projection is $R^{\varsigma}$-linear and the decomposition is one of $R^{\varsigma}$-modules. $\square$

**Remark.** The theorem is the statement that the halving $x \mapsto x/2$ is available. It is a decomposition of $R^{\varsigma}$-modules and not, in general, of $R$-modules: the projection $x \mapsto (x + x^{*})/2$ sends $\lambda x$ to $(\lambda x + \varsigma(\lambda) x^{*})/2$, which is $\lambda (x + x^{*})/2$ only for $\lambda \in R^{\varsigma}$. For $R = \mathbb{C}$, $\varsigma(z) = \bar z$ and $A = M_n(\mathbb{C})$ the decomposition is the usual one into a Hermitian and a skew-Hermitian part, and it is a decomposition of real vector spaces and not of complex ones.

### The Failure in Characteristic Two

**Proposition.** If $2 = 0$ in $R$ then $S(A) = H(A)$, so the sum $H(A) + S(A)$ is $H(A)$ and the decomposition $A = H(A) \oplus S(A)$ holds only for $A = 0$. In general $H(A) \cap S(A) = \{x \in H(A) : 2x = 0\}$ is the $2$-torsion subgroup of $H(A)$.

**Proof.** If $2 = 0$ then $-x = x$ for every $x$, so the equations $x^{*} = -x$ and $x^{*} = x$ coincide and $S(A) = H(A)$. In general, $x \in H(A) \cap S(A)$ means $x^{*} = x$ and $x^{*} = -x$, hence $2x = 0$; conversely an $x \in H(A)$ with $2x = 0$ satisfies $x = -x$, so $x^{*} = x = -x$ and $x \in S(A)$. $\square$

**Remark.** The failure is not a defect of the involution but of the halving, and in characteristic two it is total: there the involution has one fixed set and not two, and the two halves of the algebra collapse into one. Over a ring in which $2$ is a zero divisor but not zero, the intersection is the $2$-torsion, which measures the failure of uniqueness, while the existence of a decomposition can survive: over $\mathbb{Z}/4$ with the trivial involution one has $H(A) = A$, so every element is already Hermitian and no halving is needed. What the division by $2$ manufactures is the two projections, so the projections are available when $2$ is invertible and not otherwise.

## The Two Halves as Algebras

### The Hermitian Part is a Jordan Algebra

**Theorem.** Suppose $2$ is invertible in $R$ and put $x \circ y = (xy + yx)/2$. Then $H(A)$ is closed under $\circ$, and with this product it is a Jordan algebra over $R^{\varsigma}$: the product is commutative and $R^{\varsigma}$-bilinear, and it satisfies the Jordan identity $(x \circ y) \circ (x \circ x) = x \circ (y \circ (x \circ x))$.

**Proof.** For $x, y \in H(A)$, $(x \circ y)^{*} = (y^{*}x^{*} + x^{*}y^{*})/2 = (yx + xy)/2 = x \circ y$, so $x \circ y \in H(A)$. The product is commutative by construction; for a scalar $\lambda \in R^{\varsigma}$ one has $\varsigma(\lambda) = \lambda$, so the sesquilinear product is linear in each slot over $R^{\varsigma}$, and the symmetrised product is $R^{\varsigma}$-bilinear. The Jordan identity holds for the symmetrisation of any associative product, both sides expanding to the same sum of the words of length four. $\square$

**Remark.** The ordinary product of two Hermitian elements is Hermitian exactly when they commute, since $(xy)^{*} = y^{*}x^{*} = yx$; the symmetrisation is the correction, and it is the reason the Hermitian part is a Jordan algebra and not an algebra. For two skew-Hermitian elements likewise, $(st)^{*} = t^{*}s^{*} = (-t)(-s) = ts$, so $st$ is Hermitian exactly when $s$ and $t$ commute, and in general the product of two elements of the same parity is neither Hermitian nor skew-Hermitian. For a Hermitian $h$ and a skew-Hermitian $s$ the mixed products satisfy $(hs)^{*} = -sh$ and $(sh)^{*} = -hs$, so $hs + sh \in S(A)$ and $hs - sh \in H(A)$, while $hs$ alone lies in $S(A)$ exactly when $h$ and $s$ commute. When $A$ is commutative the product does respect the two halves, since then $(xy)^{*} = yx = xy$, $(st)^{*} = ts = st$ and $(hs)^{*} = -sh = -hs$ for $h \in H(A)$ and $s \in S(A)$, so a commutative sesqualgebra with an involution is a $\mathbb{Z}/2$-graded algebra with even part $H(A)$ and odd part $S(A)$; the graded example is a polynomial algebra with the involution $x \mapsto -x$, whose even and odd parts are the even and the odd polynomials.

### The Skew-Hermitian Part is a Lie Algebra

**Theorem.** $S(A)$ is closed under the commutator $[x,y] = xy - yx$, and with $[\cdot,\cdot]$ it is a Lie algebra over $R^{\varsigma}$. No hypothesis on $2$ is needed.

**Proof.** For $x, y \in S(A)$, $[x,y]^{*} = y^{*}x^{*} - x^{*}y^{*} = (-y)(-x) - (-x)(-y) = yx - xy = -[x,y]$, so $[x,y] \in S(A)$. The bracket is alternating because $[x,x] = 0$, and it is $R^{\varsigma}$-bilinear: for $\lambda \in R^{\varsigma}$, $[x, \lambda y] = x(\lambda y) - (\lambda y)x = \varsigma(\lambda)xy - \lambda yx = \lambda(xy - yx) = \lambda[x,y]$, the sesquilinearity collapsing to linearity on the fixed ring. The Jacobi identity holds for the commutator of an associative product, the three double brackets expanding into the words of length three, which cancel in opposite pairs. $\square$

**Remark.** The two halves carry two different structures, and the asymmetry is the theme of the pair of articles: the Hermitian part carries the symmetrised product and the Jordan algebra, the skew-Hermitian part carries the commutator and the Lie algebra. The commutator needs no halving, so the Lie structure on $S(A)$ needs no hypothesis on $2$, while the symmetrised product and the Jordan structure on $H(A)$ require $2$ to be invertible, and the Lie algebra they form, the unitary Lie algebra, is developed in *The Unitary Lie Algebra*.

## The Sesquilinear Product on the Two Halves

### The Splitting

**Theorem (the sesquilinear product splits over the halves).** Let $2$ be invertible in $R$ and let $y = h + s$ be the decomposition of $y$ into its Hermitian and skew-Hermitian parts. Then for every $x \in A$,

$$
x \star y = xy^{*} = xh - xs .
$$

**Proof.** $y^{*} = h^{*} + s^{*} = h - s$, so $xy^{*} = x(h - s) = xh - xs$. $\square$

**Remark.** The derived operation of *The Sesquilinear Product* acts as the ordinary product on the Hermitian half and as minus the ordinary product on the skew-Hermitian half, and the sign is the only difference between the two halves: for a Hermitian $y$ the sesquilinear product is the ordinary product, $x \star y = xy$, and for a skew-Hermitian $y$ it is its negative, $x \star y = -xy$. In the model with the conjugate transpose the sesquilinear product with a skew-Hermitian element is minus the ordinary product, so the derived operation and the algebra product agree on the Hermitian half and differ by that sign on the skew-Hermitian half.

### The Hermitian Squares

**Proposition.** For every $x \in A$ the elements $xx^{*}$ and $x^{*}x$ are Hermitian, and $xx^{*} = x \star x$ is the square of $x$ in the sesquilinear product.

**Proof.** Using the anti-multiplicativity of $*$ and $*^{2} = \mathrm{id}$, $(xx^{*})^{*} = (x^{*})^{*}x^{*} = xx^{*}$ and $(x^{*}x)^{*} = x^{*}(x^{*})^{*} = x^{*}x$. The identification $x \star x = xx^{*}$ is the derived product with the two arguments equal. $\square$

**Remark.** The elements of the form $x^{*}x$ are the Hermitian squares, and they are the ones that generate the algebraic positive cone of the category; the cone and its properties are *Hermitian Squares and the Algebraic Positive Cone*. The two squares coincide when $A$ is commutative and differ in general by the element $xx^{*} - x^{*}x$, which is itself Hermitian, being the difference of two Hermitian elements; its vanishing is the statement that $x$ commutes with $x^{*}$.

## Summary

An involution of order two cuts a sesqualgebra into the Hermitian elements $H(A) = \{x : x^{*} = x\}$ and the skew-Hermitian elements $S(A) = \{x : x^{*} = -x\}$, the fixed set and the anti-fixed set of the involution. Both are closed under addition and under the scalars of the fixed ring $R^{\varsigma}$, and a scalar with $\varsigma(\lambda) = -\lambda$ exchanges them; this is the first place where the sesquilinear layer differs from the bilinear one, since for $\varsigma = \mathrm{id}$ the fixed ring is all of $R$ and the two sets are $R$-submodules. When $2$ is invertible, $H(A) \cap S(A) = 0$ and every $x$ decomposes as $x = (x + x^{*})/2 + (x - x^{*})/2$, so that $A = H(A) \oplus S(A)$ as $R^{\varsigma}$-modules; when $2 = 0$ the two halves coincide, and in general the intersection is the $2$-torsion. The Hermitian part is closed under the symmetrised product $x \circ y = (xy + yx)/2$ and is a Jordan algebra over $R^{\varsigma}$, while the skew-Hermitian part is closed under the commutator $[x,y] = xy - yx$ and is a Lie algebra over $R^{\varsigma}$ with no hypothesis on $2$; the ordinary product of two elements of the same parity is Hermitian exactly when they commute, and for $h \in H(A)$ and $s \in S(A)$ one has $hs + sh \in S(A)$ and $hs - sh \in H(A)$. Finally the sesquilinear product splits over the decomposition, $x \star y = xh - xs$ for $y = h + s$, acting as the ordinary product on the Hermitian half and as its negative on the skew-Hermitian half, and the squares $xx^{*}$ and $x^{*}x$ are Hermitian.

## Summary of Notation

| symbol | meaning |
|---|---|
| $H(A)$ | the Hermitian elements, the fixed set $\{x : x^{*} = x\}$ of the involution |
| $S(A)$ | the skew-Hermitian elements, the anti-fixed set $\{x : x^{*} = -x\}$ |
| $R^{\varsigma}$ | the fixed ring of the base involution, the scalars that preserve the two halves |
| $x = \frac{x+x^{*}}{2} + \frac{x-x^{*}}{2}$ | the decomposition into the two halves, when $2$ is invertible |
| $x \circ y = \frac{xy+yx}{2}$ | the symmetrised product, under which $H(A)$ is a Jordan algebra |
| $[x,y] = xy - yx$ | the commutator, under which $S(A)$ is a Lie algebra |
| $x \star y = xy^{*} = xh - xs$ | the sesquilinear product split over $y = h + s$ |
| $xx^{*} = x \star x$ | the Hermitian square of $x$ |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the fixed and anti-fixed sets of an involution over a general ring, the Hermitian and skew-Hermitian elements, and the Jordan and Lie structures they carry.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of an algebra and the two halves they cut.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the symmetrised product, the Jordan identity and the Jordan algebras that the Hermitian part gives.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the commutator Lie algebra and the classical Lie algebras attached to the skew-Hermitian elements.
