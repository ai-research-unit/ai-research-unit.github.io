# __Involutive Graded Algebras__

## Introduction

A graded algebra carries two independent structures: the grading, which splits it into homogeneous pieces, and an involution, which reverses products. When the two are present at once they interact, and the interaction produces a sign. An involution that preserves the homogeneous pieces is a **graded involution**; an involution that satisfies the Koszul sign rule, reversing the product and multiplying by the parity of the two arguments, is a **superinvolution**; and the two are different data, not two names for one object. The grade involution of the grading — the automorphism that is $+1$ on the even part and $-1$ on the odd one — is a third order-two map, an automorphism rather than an anti-automorphism, and it is the map that makes the sign of the Koszul rule visible.

This article develops the graded algebras, the graded involutions and the superviolutions, the parity signs relating them, the graded commutator and the compatibility of the involution with it, and the examples of the matrix superalgebra, the exterior algebra and the Clifford algebra. The grading and the graded modules belong to *Superalgebras and Graded Structures*, the general theory of an involution on the elements is *Involutive Linear Algebras*, the tensor algebra and its coloured quotients are *Involutions of the Tensor Algebra*, and the graded action of an algebra on a module is *The Graded Action on a Module over an Algebra*, in the group `- Operator Theory` of this category.

Throughout, $k$ is a field of characteristic not two, $G$ is an abelian group written additively, and $A = \bigoplus_{g \in G} A_g$ is a $G$-graded associative $k$-algebra with $A_gA_h \subseteq A_{g+h}$ and $1 \in A_0$. The case that matters most is $G = \mathbb{Z}/2$, where the parts are written $A_0$ and $A_1$ and are called the **even** and the **odd** parts; the degree of a homogeneous element $x$ is written $|x|$, and it lies in $\mathbb{Z}/2$. The grading and its modules are those of *Superalgebras and Graded Structures*, and the involution is that of *Involutive Linear Algebras*.

## Graded Algebras and Order-Two Maps

### The Structure

**Definition.** A **graded involution** of $A$ is a $k$-linear map $\sigma : A \to A$ with

$$
\sigma^2 = \mathrm{id}, \qquad \sigma(A_g) \subseteq A_g, \qquad \sigma(xy) = \sigma(y)\sigma(x),
$$

and a **superinvolution** is a $k$-linear map with $\sigma^2 = \mathrm{id}$, $\sigma(A_g)\subseteq A_g$ and

$$
\sigma(xy) = (-1)^{|x||y|}\,\sigma(y)\sigma(x)
$$

for homogeneous $x$ and $y$. The **grade involution** of the grading is the linear map $\alpha$ with $\alpha(x) = (-1)^{|x|}x$ on homogeneous elements; it is also written $\alpha = (-1)^{|\cdot|}$.

Both $\sigma$ and the sign $(-1)^{|x||y|}$ are linear in the product, and the Koszul sign is symmetric in the two arguments, so the second definition is consistent with $\sigma^2 = \mathrm{id}$; without the symmetry the order-two condition would force the sign to vanish.

### Elementary Properties

**Proposition.** Let $A$ be $G$-graded.

**(a)** The grade involution $\alpha$ is an algebra automorphism of $A$ with $\alpha^2 = \mathrm{id}$; its fixed algebra is the even part $A_0$ and its negated part is the odd part.

**(b)** A graded involution and a superinvolution both preserve every homogeneous piece, and their restrictions to the even part $A_0$ agree as anti-automorphisms of $A_0$; on the odd part the superinvolution satisfies $\sigma(xy) = -\sigma(y)\sigma(x)$ for odd $x, y$, whereas the graded involution satisfies $\sigma(xy) = \sigma(y)\sigma(x)$.

**(c)** The grade involution $\alpha$ commutes with every graded involution and with every superinvolution, and both $\alpha\sigma$ and $\sigma\alpha$ are again of the same kind as $\sigma$.

*Proof.* (a) On homogeneous elements, $\alpha(xy) = (-1)^{|x|+|y|}xy = (-1)^{|x|}x\,(-1)^{|y|}y = \alpha(x)\alpha(y)$, and $\alpha^2 = \mathrm{id}$. (b) Parity preservation is the definition; since $|x||y|$ is odd only when both are odd, the sign is $1$ on the even part and can be $-1$ only on two odd factors. (c) The grade involution is scalar on each graded piece, so it commutes with every parity-preserving map; the composite of two parity-preserving maps is parity-preserving, and an automorphism composed with an anti-automorphism of either kind is of the same kind, because the Koszul sign is unchanged by the parity.

**Corollary.** For a superalgebra the two classes of order-two anti-maps are genuinely distinct: the transpose of a matrix algebra is a graded involution and the supertranspose is a superinvolution, and on two odd elements they differ by the sign $-1$. Composing with the grade involution does not pass from one class to the other.

## The Sign of the Koszul Rule

### Superinvolutions and the Graded Commutator

**Definition.** The **graded commutator** of two homogeneous elements of a superalgebra is

$$
[x, y] = xy - (-1)^{|x||y|}\,yx,
$$

and the **graded centre** of $A$ is the set of the elements $z$ with $[z, x] = 0$ for every homogeneous $x$.

**Theorem.** Let $\sigma$ be a superinvolution of the superalgebra $A$. Then $\sigma$ carries the graded commutator to the graded commutator with the arguments exchanged and the sign reversed,

$$
\sigma([x,y]) = -[\sigma(x), \sigma(y)] ,
$$

and it preserves the graded centre; restricted to the even part, where the graded commutator is the ordinary commutator, it is an anti-automorphism of the Lie algebra $A_0$.

*Proof.* Apply $\sigma$ to $xy - (-1)^{|x||y|}yx$: the first term is $(-1)^{|x||y|}\sigma(y)\sigma(x)$ and the second is $-(-1)^{|x||y|}\cdot(-1)^{|x||y|}\sigma(x)\sigma(y) = -\sigma(x)\sigma(y)$; so the image is $(-1)^{|x||y|}\sigma(y)\sigma(x) - \sigma(x)\sigma(y) = -[\sigma(x),\sigma(y)]$. The graded centre is preserved because the condition $[z,x]=0$ is carried to $-[\sigma(z),\sigma(x)] = 0$. On the even part the sign is $1$ and the graded commutator is the commutator, so $\sigma$ reverses the bracket.

**Corollary.** A graded involution satisfies the companion identity

$$
\sigma([x,y]) = -(-1)^{|x||y|}\,[\sigma(x),\sigma(y)]
$$

for the same graded commutator; on the even part, and on any pair with one even factor, where the Koszul sign is $1$, this is $\sigma([x,y]) = -[\sigma(x),\sigma(y)]$, the Lie anti-automorphism of $A_0$, while on two odd elements it reads $\sigma([x,y]) = +[\sigma(x),\sigma(y)]$. The two classes therefore differ by the Koszul sign of the two arguments: the superinvolution carries no sign of its own, the graded involution carries the sign in front of the bracket.

*Proof.* The computation of the theorem with the Koszul sign omitted from the defining rule of $\sigma$: the image of $xy - (-1)^{|x||y|}yx$ is $\sigma(y)\sigma(x) - (-1)^{|x||y|}\sigma(x)\sigma(y)$, and this equals $-(-1)^{|x||y|}\bigl(\sigma(x)\sigma(y) - (-1)^{|x||y|}\sigma(y)\sigma(x)\bigr)$ because the square of the Koszul sign is $1$; the two parity cases are then read off the front sign.

### The Three Order-Two Maps

**Proposition.** Let $A$ be a superalgebra. The graded involutions and the superviolutions of $A$ are exactly the maps $\sigma$ with $\sigma^2 = \mathrm{id}$ and $\sigma(A_0) \subseteq A_0$, $\sigma(A_1)\subseteq A_1$ whose restriction to $A_0$ is an anti-automorphism of $A_0$ and whose value on a product of two odd elements is $\pm$ the reversed product. The grade involution $\alpha$ is an automorphism, and the three maps $\sigma$, $\alpha$, $\alpha\sigma$ satisfy the multiplication table of the group $(\mathbb{Z}/2)^2$: any two commute and the product of the two non-identity ones is the third.

*Proof.* The restriction to the even part is an anti-automorphism in either case; on the odd part, the sign in the Koszul rule is the only freedom, and it is the sign distinguishing the two classes. The commutation of $\alpha$ with $\sigma$ and the order of the three maps give the table.

**Remark.** The two classes can be read through the grade involution: an invertible element $u$ of the even part defines an inner automorphism $\iota_u$ commuting with $\alpha$, and the conjugate $\iota_u\sigma\iota_u^{-1}$ is of the same kind as $\sigma$. The classification of the superviolutions up to conjugacy, and the correspondence with the symmetric and the alternating forms of the even part, belong to *Hilbert Algebras* and to Part II.

## The Examples

### The Matrix Superalgebra

Let $A = M_{p|q}(k)$ be the matrix superalgebra with the even part $M_p \oplus M_q$ and the odd part the off-diagonal block, written in blocks as $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$. The **supertranspose** is

$$
\begin{pmatrix} A & B \\ C & D \end{pmatrix}^{\mathrm{st}} = \begin{pmatrix} D^{\mathsf{T}} & -B^{\mathsf{T}} \\ C^{\mathsf{T}} & A^{\mathsf{T}} \end{pmatrix},
$$

the two diagonal blocks exchanged and the upper odd block negated; the construction needs $p = q$, since the two diagonal blocks must be interchangeable, and it is the balanced case that is treated here. Its square is the identity, because applying it twice transposes each block twice and the two minus signs cancel; it preserves the even and the odd parts; and for homogeneous $P$ and $Q$ it satisfies $(PQ)^{\mathrm{st}} = (-1)^{|P||Q|}Q^{\mathrm{st}}P^{\mathrm{st}}$, which is checked on the blocks: the two products $\sigma(PQ)$ and $\sigma(Q)\sigma(P)$ differ in the even blocks by the terms $F^{\mathsf{T}}C^{\mathsf{T}}$ and $G^{\mathsf{T}}B^{\mathsf{T}}$, and these terms involve one odd block of $P$ and one of $Q$, so they are absent unless both factors are odd — exactly where the Koszul sign is $-1$. Hence the supertranspose is a superinvolution, while the ordinary transpose is a graded involution, because it has no sign, and the two differ exactly on the products of two odd matrices. The grade involution is conjugation by the diagonal matrix with entries $+1$ on the first block and $-1$ on the second; other sign conventions for the supertranspose appear in the literature.

### The Exterior Algebra

Let $A = \Lambda(V)$ with its $\mathbb{Z}/2$-grading by the degree, and let $\sigma$ be a linear involution of $V$. The reversal $\theta_\sigma$ of *Involutions of the Tensor Algebra* preserves the degree, so it is a parity-preserving anti-automorphism, and it is a graded involution of $\Lambda(V)$. It is **not** a superinvolution: on two odd elements $v$ and $w$ the superinvolution condition reads $\theta_\sigma(vw) = -\theta_\sigma(w)\theta_\sigma(v)$, which is $\theta_\sigma(vw)+\theta_\sigma(w)\theta_\sigma(v) = 0$, and computing with $vw = -wv$ this would force $2\,vw = 0$, false for a free pair. The grade involution $\alpha$ is the automorphism that is $-1$ on the odd part; it commutes with $\theta_\sigma$, and $\alpha\theta_\sigma$ is again a graded involution. Whether $\Lambda(V)$ carries a superinvolution at all is a different question, whose answer depends on the space and whose classification belongs to Part II.

### The Clifford Algebra

Let $A = \mathrm{Cl}(V,q)$ with the $\mathbb{Z}/2$-grading by the parity of the degree. The main involution is the grade involution $\alpha$; the transpose $\theta$ is the reversal, a graded involution; and the conjugation $\alpha\theta$ is their composite, again a graded involution, because the composite of an automorphism with an anti-automorphism is an anti-automorphism. The three are the standard order-two maps of the Clifford algebra, and the identification of the superinvolutions of a Clifford algebra with the maps induced by the isometries of the form belongs to *Quadratic Forms and Clifford Algebras* of Part II, where the form is owned.

### A Group Algebra

Let $G$ be a group with a homomorphism $G \to \mathbb{Z}/2$, and let $A = k[G]$ be graded by the image. The inversion $g \mapsto g^{-1}$ is a parity-preserving anti-automorphism, because the homomorphism is constant on the inverse; it is a graded involution. It is a superinvolution only if the Koszul sign is trivial on the products of two odd elements, which fails unless the odd part is empty or the characteristic is two, so the example is one in which the grading exists and the two classes of order-two anti-maps are strictly different. When the homomorphism is trivial the grading is concentrated in degree zero, the Koszul sign is $1$, and the two notions collapse.

## Summary

A $G$-graded algebra $A = \bigoplus_g A_g$ carries the **grade involution** $\alpha(x) = (-1)^{|x|}x$, an automorphism of order two whose fixed algebra is the even part, and it may carry a **graded involution** $\sigma(xy) = \sigma(y)\sigma(x)$ or a **superinvolution** $\sigma(xy) = (-1)^{|x||y|}\sigma(y)\sigma(x)$, both parity-preserving and both of order two. The Koszul sign $(-1)^{|x||y|}$ is the whole difference between them: it is $1$ unless both arguments are odd, and on the even part the two restrictions agree. The grade involution commutes with either and composing with it does not change the class.

A superinvolution satisfies $\sigma([x,y]) = -[\sigma(x),\sigma(y)]$ for the graded commutator $[x,y] = xy - (-1)^{|x||y|}yx$ and preserves the graded centre; a graded involution satisfies $\sigma([x,y]) = -(-1)^{|x||y|}[\sigma(x),\sigma(y)]$, which is $-[\sigma(x),\sigma(y)]$ unless both arguments are odd and $+[\sigma(x),\sigma(y)]$ there. The three maps $\sigma$, $\alpha$, $\alpha\sigma$ form a group of order dividing four. The examples are the supertranspose as a superinvolution and the transpose as a graded involution of the matrix superalgebra; the reversal of the exterior algebra and of the Clifford algebra, with the main involution and the conjugation; and the inversion of a graded group algebra. The grading and the graded modules belong to *Superalgebras and Graded Structures*; the involutions of the tensor algebra and its quotients are *Involutions of the Tensor Algebra*; the graded action of an algebra on a module is *The Graded Action on a Module over an Algebra*; and the general theory of the involution on the elements is *Involutive Linear Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$ | the abelian grading group, written additively |
| $A = \bigoplus_g A_g$ | the graded algebra |
| $A_0, A_1$ | the even and the odd parts when $G = \mathbb{Z}/2$ |
| $|x|$ | the parity of a homogeneous element |
| $\alpha(x) = (-1)^{|x|}x$ | the grade involution |
| $\sigma(xy) = \sigma(y)\sigma(x)$ | a graded involution |
| $\sigma(xy) = (-1)^{|x||y|}\sigma(y)\sigma(x)$ | a superinvolution |
| $[x,y] = xy - (-1)^{|x||y|}yx$ | the graded commutator |
| $X^{\mathrm{st}} = \begin{pmatrix} D^{\mathsf{T}} & -B^{\mathsf{T}} \\ C^{\mathsf{T}} & A^{\mathsf{T}}\end{pmatrix}$ | the supertranspose of a matrix |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for graded algebras and the grade involution.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for graded algebras and the Koszul sign rule.
- Christian Kassel, *Quantum Groups* (Springer, 1995), for superalgebras, superinvolutions and the graded commutator.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the graded involutions and their classification.
