# __Involutions of a Sesquilinear Tensor Product__

## Introduction

The tensor product of two sesquialgebras over a common datum is again a sesquialgebra over that datum, its product is built slotwise from the two products, and its **tensor involution** is

$$
\natural(x\otimes y) = x^{*}\otimes y^{*} ,
$$

as in *Tensor Products of Sesquialgebras*. That article reads the product and the transposition $\natural(x\star y) = y\star x$; this one reads the involution itself, and the involutions it generates where the predecessor leaves off. When the two factors are the same object there is a second map beside $\natural$, the **flip** $\tau(x\otimes y) = y\otimes x$, which is an automorphism; the twist and the flip together generate the involutions of the tensor square, and the two anti-involutions among them, $\natural$ and $\natural\tau$, are the subject of the middle of the article.

The model is bilinear and is *Involutions of the Tensor Algebra*. There the tensor algebra of a space with an involution carries a **reversal**, which twists every letter and reads the word backwards, and a **grade involution**, which is an automorphism and needs a degree; the reversal of a word of length $n$ is the $n$-fold tensor power of the involution composed with the reversal of the order of the factors, and the two involutions commute. The sesquilinear case keeps the reversal and the twist and loses the sign: the twist is $\varsigma$-semilinear while the flip is linear, so the two carry opposite parities, and a sign involution needs a grading, which is *The Graded Sesquilinear Action*. The single new datum with respect to the bilinear case is $\varsigma$ itself.

The article recalls the tensor involution and its two scalar rules, develops the flip, the two involutions of the tensor square and the group they generate, extends both to the higher tensor powers, compares the whole with the tensor algebra, and works the cases $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$. Throughout, $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, $A$ and $B$ are sesquialgebras over $(R,\varsigma)$ whose datum involutions are written ${}^{*}$, and $\natural$ is the tensor involution. The tensor product and its universal property are *Tensor Products of Sesquialgebras*; the involutions of a sesquialgebra and the set they form are *The Involutions of a Sesquialgebra*; the two parities of the semilinear maps are *The Sesquilinear Product*; the bilinear model is *Involutions of the Tensor Algebra*; and the graded case is *The Graded Sesquilinear Action*. The article stays inside the algebra: no distance and no continuity occurs.

## The Tensor Involution Recalled

### The Two Scalar Rules

**Definition.** The **tensor involution** of $A\otimes_RB$ is the additive map

$$
\natural : A\otimes_RB \longrightarrow A\otimes_RB , \qquad \natural(x\otimes y) = x^{*}\otimes y^{*} .
$$

**Theorem.** The tensor involution is additive, bijective and of order two; it is $\varsigma$-**semilinear**,

$$
\natural(\lambda\, X) = \varsigma(\lambda)\,\natural(X) , \qquad \lambda\in R , \quad X\in A\otimes_RB ;
$$

and when the two factor involutions are anti-automorphisms of their products, it is an anti-automorphism of the envelope,

$$
\natural(XY) = \natural(Y)\,\natural(X) .
$$

*Proof.* On elementary tensors $\natural^2(x\otimes y) = x^{**}\otimes y^{**} = x\otimes y$, and additivity extends it, so $\natural$ is its own inverse. For the scalars, $\natural(\lambda(x\otimes y)) = \natural((\lambda x)\otimes y) = \varsigma(\lambda)x^{*}\otimes y^{*} = \varsigma(\lambda)\natural(x\otimes y)$, the scalar acting on the first component, and additivity gives the general case. For the envelope, $\natural((x\otimes y)(u\otimes v)) = \natural(xu\otimes yv) = (xu)^{*}\otimes(yv)^{*} = u^{*}x^{*}\otimes v^{*}y^{*} = \natural(u\otimes v)\natural(x\otimes y)$, since each factor involution reverses products, and additivity extends it. $\square$

**Remark (the parity is the only new datum).** Over the trivial involution of the base the tensor involution is $R$-linear, because $\varsigma(\lambda) = \lambda$, and the whole construction is the bilinear one. It is $\varsigma$-semilinear and not $R$-linear exactly as soon as $\varsigma \neq \mathrm{id}$ and the tensor product is nonzero, that is, as soon as the twist is visible at all. The distinction between $\varsigma = \mathrm{id}$ and $\varsigma \neq \mathrm{id}$ is therefore the only thing that separates this article from *Involutions of the Tensor Algebra*.

### The Two Readings

**Definition.** The **envelope** of the tensor product is the associative product

$$
(x\otimes y)(u\otimes v) = xu\otimes yv ,
$$

and the **sesquilinear product** is the product of the sesquialgebras,

$$
(x\otimes y)\star(u\otimes v) = (x\star u)\otimes(y\star v) ,
$$

both extended additively. In the derived case $x\star u = xu^{*}$ the second is the first with $\natural$ inserted in the second slot, by the predecessor.

**Theorem (the involution transposes the sesquilinear product).** Suppose the two factor involutions are anti-automorphisms of their products. Then

$$
\natural(X\star Y) = Y\star X \qquad \text{for all } X, Y\in A\otimes_RB .
$$

*Proof.* On elementary tensors, $\natural((x\otimes y)\star(u\otimes v)) = \natural(x\star u\otimes y\star v) = (x\star u)^{*}\otimes(y\star v)^{*}$; the factor identity $(x\star u)^{*} = u\star x$ holds in the derived case, $(xu^{*})^{*} = ux^{*} = u\star x$, and it is exactly the hypothesis that each factor involution is an anti-automorphism of its product. So the value is $(u\star x)\otimes(v\star y) = (u\otimes v)\star(x\otimes y)$, and additivity extends it. $\square$

**Remark.** The two theorems above are the whole content of the involution at the level of the product: it reverses the envelope and it transposes the sesquilinear product. They are not in conflict, because the sesquilinear product is the envelope with $\natural$ inserted in the second slot and not the envelope itself. The distinction is the one of *Tensor Products of Sesquialgebras*, §*The Two Products of the Tensor Product*, and it is the reason the transposition clause needs its hypothesis on the factors and the anti-multiplicativity clause does not.

## The Flip and the Tensor Square

### The Flip

Let the two factors be one object: the **tensor square** is $A\otimes_RA$, with the same product and the same tensor involution $\natural$ obtained by taking $B = A$.

**Definition.** The **flip** of the tensor square is

$$
\tau : A\otimes_RA \longrightarrow A\otimes_RA , \qquad \tau(x\otimes y) = y\otimes x ,
$$

extended additively.

**Theorem.** The flip is an $R$-linear algebra automorphism of order two,

$$
\tau(XY) = \tau(X)\tau(Y) , \qquad \tau^2 = \mathrm{id} , \qquad \tau(\lambda X) = \lambda\,\tau(X) ,
$$

and it commutes with the tensor involution, $\natural\tau = \tau\natural$.

*Proof.* On elementary tensors $\tau((x\otimes y)(u\otimes v)) = \tau(xu\otimes yv) = yv\otimes xu = (y\otimes x)(v\otimes u) = \tau(x\otimes y)\tau(u\otimes v)$, and additivity extends it; $\tau^2 = \mathrm{id}$ and $R$-linearity are immediate on elementary tensors. For the commutation, $\natural\tau(x\otimes y) = \natural(y\otimes x) = y^{*}\otimes x^{*} = \tau(x^{*}\otimes y^{*}) = \tau\natural(x\otimes y)$. $\square$

**Remark.** The flip exists only when the two factors are the same object; for $A\otimes_RB$ with $A\neq B$ there is no map $x\otimes y\mapsto y\otimes x$ into $A\otimes_RB$. This is why the two involutions of the next section belong to the tensor square and not to the general tensor product.

### The Two Involutions of the Tensor Square

**Definition.** The **twisted tensor involution** is the composite $\natural\tau = \tau\natural$, that is

$$
\natural\tau(x\otimes y) = y^{*}\otimes x^{*} .
$$

**Theorem.** The tensor square $A\otimes_RA$ carries the two anti-involutions $\natural$ and $\natural\tau$, of order two and $\varsigma$-semilinear, and the four maps

$$
\mathrm{id}, \quad \natural, \quad \natural\tau, \quad \tau
$$

form a commutative group of exponent two: $\natural\,\natural\tau = \tau$, $\tau\,\natural = \natural\tau$ and $\tau\,\natural\tau = \natural$. The tensor involution $\natural$ is the identity exactly when the factor involution is trivial, and the two anti-involutions agree exactly when the flip is the identity.

*Proof.* The composite of two anti-automorphisms is an automorphism, so $\natural\tau$ and $\tau\natural$ are anti-automorphisms, and they are equal by the commutation of the flip and the twist; $(\natural\tau)^2 = \natural\tau\natural\tau = \natural\natural\tau\tau = \mathrm{id}$. For the products of the group, $\natural(\natural\tau) = \natural\natural\tau = \tau$ because $\natural^2 = \mathrm{id}$, and $\tau(\natural\tau) = \natural\tau\tau = \natural$; the group is commutative because $\natural$ and $\tau$ commute. If $\natural = \mathrm{id}$ then $x^{*}\otimes y^{*} = x\otimes y$ for all $x, y$, hence ${}^{*} = \mathrm{id}$ when the tensor square is nonzero; conversely ${}^{*} = \mathrm{id}$ gives $\natural = \mathrm{id}$. Finally $\natural\tau = \natural$ if and only if $\tau = \natural\,\natural\tau = \mathrm{id}$, and conversely. $\square$

**Proposition (when the flip is the identity).** The flip is the identity on $A\otimes_RA$ exactly when $x\otimes y = y\otimes x$ for all $x, y\in A$. This holds when $A$ is the base ring itself and fails as soon as $A$ contains two $R$-independent elements.

*Proof.* The first statement is the definition read on elementary tensors. For $A$ of rank one over $R$ the tensor square is $R\otimes_RR\cong R$ and the two sides agree; for two independent elements $e_1, e_2$ the tensors $e_1\otimes e_2$ and $e_2\otimes e_1$ are two different elements of a basis of the tensor square, so they differ. $\square$

**Corollary (the two involutions are genuinely two).** For any object of rank at least two the two anti-involutions $\natural$ and $\natural\tau$ of the tensor square are distinct, and they differ on the same element on which the flip differs from the identity.

*Proof.* Immediate from the proposition and the criterion of the theorem: $\natural$ and $\natural\tau$ agree if and only if $\tau = \mathrm{id}$. $\square$

**Example (a fixed element outside the Hermitian tensors).** Let $A = M_2(\mathbb{C})$ with the conjugate transpose and let $E_{ij}$ be the matrix units. The element

$$
X = E_{12}\otimes E_{21} + E_{21}\otimes E_{12}
$$

is fixed by $\natural$, since $\natural$ exchanges the two summands, and it is not a sum of tensors $h\otimes h'$ of Hermitian elements: with $H_1 = \tfrac12(E_{12}+E_{21})$ Hermitian and $K_1 = \tfrac12(E_{12}-E_{21})$ skew-Hermitian one has $2H_1\otimes H_1 - 2K_1\otimes K_1 = X$, and the decomposition $M_2(\mathbb{C}) = H\oplus S$ into Hermitian and skew-Hermitian parts is direct, so the second summand is not removable. So the fixed set of $\natural$ contains $H(A)\otimes H(A)$ and is strictly larger than it.

*Proof.* The computation $2H_1\otimes H_1 - 2K_1\otimes K_1 = \tfrac12(E_{12}+E_{21})\otimes(E_{12}+E_{21}) - \tfrac12(E_{12}-E_{21})\otimes(E_{12}-E_{21}) = E_{12}\otimes E_{21} + E_{21}\otimes E_{12}$ is the expansion of the two squares; and $K_1\otimes K_1\neq0$ lies in the summand $S\otimes S$ of the direct decomposition $M_2\otimes M_2 = (H\oplus S)\otimes(H\oplus S)$. $\square$

## The Reversal of the Tensor Powers

### The Two Maps on $A^{\otimes n}$

**Definition.** For $n\geq1$ the **$n$-fold tensor power** $A^{\otimes n} = A\otimes_R\cdots\otimes_RA$ carries the two additive maps

$$
\natural_n(a_1\otimes\cdots\otimes a_n) = a_1^{*}\otimes\cdots\otimes a_n^{*} , \qquad
\rho_n(a_1\otimes\cdots\otimes a_n) = a_n^{*}\otimes\cdots\otimes a_1^{*} ,
$$

the second called the **reversal** of the tensor power.

**Theorem.** Both maps are $\varsigma$-semilinear anti-automorphisms of $A^{\otimes n}$ of order two; the reversal is the twist composed with the order-reversing permutation,

$$
\rho_n = \pi_n\,\natural_n , \qquad \pi_n(a_1\otimes\cdots\otimes a_n) = a_n\otimes\cdots\otimes a_1 ,
$$

where $\pi_n$ is an $R$-linear automorphism of order two; and for $n = 2$ these are the two involutions of the tensor square, $\natural_2 = \natural$ and $\rho_2 = \natural\tau$.

*Proof.* The two maps are the $n$-fold tensor products of ${}^{*}$ and of the order-reversing permutation on the indices, and both are additive and invertible on the basis of decomposable tensors; $\natural_n^2 = \mathrm{id}$ and $\pi_n^2 = \mathrm{id}$ give $\rho_n^2 = \pi_n\natural_n\pi_n\natural_n = \pi_n^2\natural_n^2 = \mathrm{id}$, since a permutation of the factors commutes with the slotwise twist. Semilinearity is the scalar rule on the first factor; anti-multiplicativity is the reversal of the $n$ factors. For $n = 2$ the permutation $\pi_2$ is the flip and the reversal is $\natural\tau$. $\square$

### The Sign That Is Absent

**Remark (the missing grade involution).** The tensor algebra carries a second involution beside the reversal, the grade involution, which is an automorphism and acts by a sign on the words of a fixed length. There is no such map here: the sign needs a degree, a sesquialgebra has no degree unless it is graded, and in the graded case the sign is a Koszul sign belonging to the graded twist of *The Graded Sesquilinear Action*. What the tensor square offers in its place is the flip $\tau$, which is an automorphism of order two and plays the role of the order-reversing permutation of the tensor algebra; it is not a sign on the homogeneous parts, and it is $R$-linear while the twist beside it is $\varsigma$-semilinear.

**Corollary (the two involutions of the tensor algebra, read here).** In the tensor algebra $T(V)$ the reversal of a word of length $n$ is the map $\rho_n$ above with $A = T(V)$, the involution of the space being the restriction of ${}^{*}$ to $V$; the grade involution has no counterpart in a sesquialgebra without a grading, and the pair $(\natural, \tau)$ of the tensor square is the sesquilinear shadow of the reversal and of the grade involution of the tensor algebra.

## The Examples

### The Case $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$

Let $A = \mathbb{C}$ over $(\mathbb{R},\mathrm{id})$ with the conjugation and $B = \mathbb{H}$ over $(\mathbb{R},\mathrm{id})$ with the quaternion conjugation ${}^{\natural}$. Both are sesquialgebras over the trivial datum, so both derived operations are bilinear, and the tensor product is the biquaternion algebra

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} = \mathbb{B}
$$

with the tensor involution $\natural(z\otimes q) = \bar z\otimes{}^{\natural}q$. That involution is the **Hermitian conjugation** ${}^{*}$ of $\mathbb{B}$, the conjugate-linear map that conjugates the coefficients and negates the quaternion units; it is the datum involution of $\mathbb{B}$ read over $(\mathbb{C},\varsigma)$, and it is $R$-linear here because the base involution is trivial. The flip is not defined, the two factors being different objects. This case exhibits the tensor involution as a familiar map on a corpus algebra, and it is the degenerate one: the tensor product is taken over $(\mathbb{R},\mathrm{id})$, so its sesquilinear structure collapses, and the twist appears only when $\mathbb{B}$ is read over $(\mathbb{C},\varsigma)$, which is the next case.

### The Case $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$

Let $B = \mathbb{B}$ over $(\mathbb{C},\varsigma)$ with the star ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ of *Biquaternions as a Sesquialgebra over $\mathbb{C}$*, and let $A = B$, so that the tensor product is the tensor square $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$. Its product is the sesquilinear product

$$
(P\otimes Q)\star(R\otimes S) = (P\star R)\otimes(Q\star S) = PR^{*}\otimes QS^{*} ,
$$

which is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, and its tensor involution is $\natural = {}^{*}\otimes{}^{*}$, which is conjugate-linear, of order two, and an anti-automorphism of the envelope. The flip $\tau$ and the two anti-involutions $\natural$ and $\natural\tau$ are those of the section above, and the tensor square is a matrix algebra:

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B} \cong M_2(\mathbb{C})\otimes_{\mathbb{C}}M_2(\mathbb{C}) \cong M_4(\mathbb{C})
$$

through the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ of *Matrix Sesquialgebras*, under which the star is the conjugate transpose and the tensor involution is the **conjugate transpose of $M_4(\mathbb{C})$**, because the conjugate transpose of a Kronecker product is the Kronecker product of the conjugate transposes. The two anti-involutions are distinct: on the matrix units, with $X = E_{12}\otimes E_{21}$,

$$
\natural(X) = E_{21}\otimes E_{12} , \qquad \natural\tau(X) = E_{12}\otimes E_{21} ,
$$

and these are the two different matrix units $E_{3,2}$ and $E_{2,3}$ of $M_4(\mathbb{C})$ under the Kronecker identification. This is the corollary of the section above read on the corpus's own algebra, and it is the case in which the second involution is visible as a map of the tensor square and not only as the transposition of *Tensor Products of Sesquialgebras*.

## Summary

The tensor product $A\otimes_RB$ of two sesquialgebras over a common datum carries the **tensor involution** $\natural(x\otimes y) = x^{*}\otimes y^{*}$, which is additive, bijective, of order two, **$\varsigma$-semilinear** — $\natural(\lambda X) = \varsigma(\lambda)\natural(X)$ — an anti-automorphism of the envelope when the factor involutions are, and the map that transposes the sesquilinear product, $\natural(X\star Y) = Y\star X$. The parity is the single new datum with respect to the bilinear model *Involutions of the Tensor Algebra*: over the trivial involution of the base the map is linear and the picture is the bilinear one.

On the **tensor square** $A\otimes_RA$ there is beside the twist the **flip** $\tau(x\otimes y) = y\otimes x$, an $R$-linear algebra automorphism of order two commuting with $\natural$. The two **anti-involutions of the tensor square** are $\natural$ and the twisted $\natural\tau(x\otimes y) = y^{*}\otimes x^{*}$, they are $\varsigma$-semilinear of order two, they differ exactly when the flip is the identity — that is, exactly for the base itself and no other object — and with the flip they form the commutative group $\{\mathrm{id}, \natural, \natural\tau, \tau\}$ of exponent two. On the **$n$-fold tensor power** the twist $\natural_n$ and the reversal $\rho_n(a_1\otimes\cdots\otimes a_n) = a_n^{*}\otimes\cdots\otimes a_1^{*}$ are the two $\varsigma$-semilinear anti-involutions, and $\rho_n = \pi_n\natural_n$ is the twist composed with the order-reversing permutation, which is the sesquilinear form of the reversal of *Involutions of the Tensor Algebra*; the grade involution of that article has no counterpart without a grading, and the graded sign is *The Graded Sesquilinear Action*.

The worked cases are $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} = \mathbb{B}$, where the tensor involution is the Hermitian conjugation and the datum is trivial, and $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$, where the tensor involution is the conjugate transpose of $M_4(\mathbb{C})$ under $\mathbb{B}\cong M_2(\mathbb{C})$ and the second anti-involution is visible on the matrix units. The tensor involution, its universal property and the transposition are *Tensor Products of Sesquialgebras*; the involutions of a single sesquialgebra are *The Involutions of a Sesquialgebra*; and the bilinear model is *Involutions of the Tensor Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $\varsigma$ | the base ring and its involution |
| $A$, $B$ | sesquialgebras over $(R,\varsigma)$ |
| ${}^{*}$ | the datum involution of a factor |
| $A\otimes_RB$ | the sesquilinear tensor product |
| $(x\otimes y)(u\otimes v) = xu\otimes yv$ | the envelope |
| $(x\otimes y)\star(u\otimes v) = (x\star u)\otimes(y\star v)$ | the sesquilinear product |
| $\natural(x\otimes y) = x^{*}\otimes y^{*}$ | the tensor involution |
| $\tau(x\otimes y) = y\otimes x$ | the flip of the tensor square |
| $\natural\tau(x\otimes y) = y^{*}\otimes x^{*}$ | the twisted tensor involution |
| $\natural_n$, $\rho_n$, $\pi_n$ | the twist, the reversal and the order-reversing permutation on $A^{\otimes n}$ |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the tensor product of algebras, its universal property and the tensor powers.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the tensor constructions on algebras with an involution and the reversal of words.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions of the tensor constructions and the behaviour of the twist under them.
