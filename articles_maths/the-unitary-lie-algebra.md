# __The Unitary Lie Algebra__

## Introduction

An involution of a sesqualgebra selects the elements it reverses, and those elements are closed under the commutator. The **unitary Lie algebra** of $A$ is the skew-Hermitian part

$$
\mathfrak{u}(A) = \bigl(S(A), [\ ,\ ]\bigr), \qquad S(A) = \{x \in A : x^{*} = -x\} ,
$$

the set $S(A)$ with the bracket $[x,y] = xy - yx$. It is the Lie companion of *The Hermitian Jordan Algebra*: the same involution cuts the same algebra into two halves, the Hermitian half carries the symmetrised product and a Jordan algebra, and the skew-Hermitian half carries the commutator and a Lie algebra. This article reads the Lie algebra that arises there, its scalars, the behaviour of the product of two skew-Hermitian elements, the action of the unitary group, and its standard cases.

The article turns on one difference from its Jordan twin and on one parallel. The difference is the hypothesis: the Jordan structure needs $2$ invertible in $R$, and the Lie structure needs nothing on $2$ at all, because the commutator is alternating and the closure computation uses only that the involution is an anti-automorphism of order two. The parallel is the scalars: as for the Hermitian half, the skew-Hermitian half is a module over the **fixed ring** $R^{\varsigma}$ and not over $R$, and the Lie algebra is an algebra over $R^{\varsigma}$. The bilinear theory of the skew part is *The Self-Adjoint Part of an Algebra*, §*The Skew Part as a Lie Algebra*, and the present article is its sesquilinear counterpart, obtained by cutting the scalars down to the fixed ring. That article writes $K(A)$ for the skew part; here the sesquilinear notation $S(A)$ is kept throughout.

The setting is that of *Sesqualgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and $A$ is an associative $R$-algebra with a $\varsigma$-semilinear involution $*$. The two halves and the closure of $S(A)$ under the commutator are *Hermitian and Skew-Hermitian Elements*, §*The Skew-Hermitian Part is a Lie Algebra*; the skew-Hermitian elements under the symmetrised product are the Jordan twin, *The Hermitian Jordan Algebra*; the unitary elements, the group $U(A)$ and the inner $*$-automorphisms $x \mapsto uxu^{*}$ are *Units and the Unitary Elements*; the derivations and the inner derivations $D_{a}(x) = ax - xa$ are *Derivations of a Sesqualgebra*; the general theory and the structure theory are *Lie Algebras* and *Structure of Lie Algebras*; and the Lie structures a sesqualgebra carries as a whole are *Lie Algebras of Sesqualgebras*.

---

## The Skew-Hermitian Part as a Lie Algebra

### The Closure

**Theorem.** $S(A)$ is closed under the commutator $[x,y] = xy - yx$, and with this bracket it is a Lie algebra over the fixed ring $R^{\varsigma}$. No hypothesis on $2$ is needed.

**Proof.** For $x, y \in S(A)$ one has $x^{*} = -x$ and $y^{*} = -y$, so

$$
[x,y]^{*} = (xy - yx)^{*} = y^{*}x^{*} - x^{*}y^{*} = (-y)(-x) - (-x)(-y) = yx - xy = -[x,y] ,
$$

using the anti-multiplicativity of $*$ and $*^{2} = \mathrm{id}$; hence $[x,y] \in S(A)$. The bracket is alternating because $[x,x] = x^{2} - x^{2} = 0$, it is additive in each variable, and the Jacobi identity is the expansion of the associativity of the product of $A$. For the scalars, let $\lambda \in R^{\varsigma}$ and $x, y \in S(A)$; then $(\lambda x)^{*} = \varsigma(\lambda)x^{*} = -\lambda x$, so $\lambda x \in S(A)$, and $[\lambda x, y] = \lambda(xy - yx) = \lambda[x,y]$, the scalar passing through both products by the first scalar rule of *Sesqualgebras*. $\square$

**Remark.** The computation is the one of *Hermitian and Skew-Hermitian Elements*, §*The Skew-Hermitian Part is a Lie Algebra*, and the two steps are the only two used: the involution reverses the order of a product, and the two minus signs of the skew condition cancel in pairs. Neither the symmetrisation nor the invertibility of $2$ appears, and this is the structural reason the Lie case is the cheaper of the two.

**Remark (the closure is a property of the skew half alone).** The Hermitian part does not have it: for $h_1, h_2 \in H(A)$ the bracket is $[h_1,h_2] = h_1h_2 - h_2h_1$, whose conjugate is $h_2h_1 - h_1h_2 = -[h_1,h_2]$, so $[H,H] \subseteq S(A)$ and the Hermitian elements are not closed under the bracket unless every such bracket vanishes. The two halves are therefore not interchangeable under the commutator: the skew half is a Lie subalgebra and the Hermitian half is not, although both are stable under the commutator with the opposite half, $[S,H] \subseteq H$, which is the $\mathbb{Z}/2$-grading of *Lie Algebras of Sesqualgebras*.

### The Scalars

**Proposition.** $S(A)$ is a module over $R^{\varsigma}$ and not over $R$ in general, and $\mathfrak{u}(A)$ is a Lie algebra over $R^{\varsigma}$ and not over $R$. A scalar $\lambda$ with $\varsigma(\lambda) = -\lambda$ carries $S(A)$ into $H(A)$, so it is not a scalar of the Lie algebra.

**Proof.** For $\lambda \in R^{\varsigma}$ and $s \in S(A)$, $(\lambda s)^{*} = \varsigma(\lambda)s^{*} = \lambda(-s) = -\lambda s$, so $\lambda s \in S(A)$. For $\varsigma(\lambda) = -\lambda$ the same computation gives $(\lambda s)^{*} = \varsigma(\lambda)s^{*} = (-\lambda)(-s) = \lambda s$, so $\lambda s \in H(A)$ and the scalar with $\varsigma(\lambda) = -\lambda$ carries the skew-Hermitian part to the Hermitian one. The scalars that preserve $S(A)$ are the $\lambda$ with $(\varsigma(\lambda) - \lambda)S(A) = 0$, a subring that contains $R^{\varsigma}$ and equals it when $S(A)$ has zero annihilator in $R$, over an integral domain for instance. This is *Hermitian and Skew-Hermitian Elements*, §*The Scalar Action*. $\square$

**Remark (the fixed ring is not literally the whole answer).** Over a ring with zero divisors the preserved scalars can be strictly larger than $R^{\varsigma}$. Let $R = k[x]/(x^{3})$, so that the nonzero element $x$ satisfies $x^{3} = 0$, and let $\varsigma$ be the substitution $\varsigma(x) = -x$; let $A = R$ with the involution $* = \varsigma$, and put $\lambda = 1 + x$ and $h = x^{2}$. Then $\varsigma(\lambda) = 1 - x \neq \lambda$ and $h$ is Hermitian, while $\lambda h = x^{2} + x^{3} = x^{2}$ is Hermitian, nonzero, and $\varsigma(\lambda) - \lambda = -2x$ annihilates $h$ because $x^{3} = 0$. So $\lambda$ preserves $H(A)$ without being fixed by $\varsigma$, and the annihilator condition above is not redundant. Over an integral domain the factor $(\varsigma(\lambda) - \lambda)$ cannot annihilate a nonzero element, and the two statements agree.

**Remark.** In the model $M_n(\mathbb{C})$ with the conjugate transpose the fixed ring is $\mathbb{R}$, and the multiplication by $i$ is the scalar that exchanges the two halves, carrying the skew-Hermitian matrices to the Hermitian ones: the two halves are two real forms of the ambient complex algebra and not two complex subspaces of it. The Lie algebra $\mathfrak{u}(A)$ is therefore a real Lie algebra while $A$ is a complex algebra, and the fixed ring is the whole of the difference from the bilinear theory, exactly as in the Jordan twin.

## The Product of Two Skew-Hermitian Elements

### The Reversal of the Product

**Theorem.** Let $x, y \in S(A)$. Then $(xy)^{*} = yx$, and

$$
xy \in S(A) \iff xy = -yx, \qquad xy \in H(A) \iff xy = yx .
$$

In particular the skew-Hermitian part is closed under the product exactly when any two of its elements anticommute, and it is carried into the Hermitian part exactly when they commute.

**Proof.** $(xy)^{*} = y^{*}x^{*} = (-y)(-x) = yx$. Hence $xy$ is skew-Hermitian, that is $(xy)^{*} = -xy$, exactly when $yx = -xy$; and it is Hermitian, that is $(xy)^{*} = xy$, exactly when $yx = xy$. $\square$

**Remark.** The product of two skew-Hermitian elements is therefore skew-Hermitian only in the anticommuting case and Hermitian only in the commuting case, and in general it is neither. Both cases occur: in $M_2(\mathbb{C})$ the skew-Hermitian matrices $x = E_{12} - E_{21}$ and $y = i(E_{11} - E_{22})$ anticommute, and $xy = -iE_{12} - iE_{21}$ is skew-Hermitian, while $x$ and the central $z = i(E_{11} + E_{22})$ commute and $xz = iE_{12} - iE_{21}$ is Hermitian. The rule is the reason the bracket is taken rather than the product: the commutator of two skew-Hermitian elements is always skew-Hermitian, whereas the product is not, and $\mathfrak{u}(A)$ is a Lie algebra and not an algebra.

### The Hermitian Correction

**Proposition.** Let $x, y \in S(A)$. Then $xy + yx$ is Hermitian, and

$$
[x,y] = xy - yx \in S(A), \qquad xy + yx \in H(A) .
$$

**Proof.** $(xy + yx)^{*} = y^{*}x^{*} + x^{*}y^{*} = (-y)(-x) + (-x)(-y) = yx + xy$, so the sum is Hermitian; the difference is skew-Hermitian by the closure theorem above. $\square$

**Remark.** The two combinations are exactly the symmetrisation and the antisymmetrisation of the two products $xy$ and $yx$, and the pair $(xy + yx, xy - yx)$ separates the Hermitian and the skew-Hermitian parts of the sesquilinear product of two skew-Hermitian elements. This is the same splitting that *The Sesquilinear Commutator* and *The Sesquilinear Symmetrised Product* perform on the product of two general elements, read on the skew-Hermitian half, and it is the reason the Hermitian and the skew-Hermitian elements are the natural arguments of the two halves of the theory.

## The Adjoint Action

### The Inner Derivations

**Theorem.** For $s \in S(A)$ define $\mathrm{ad}_{s}(x) = [s,x] = sx - xs$. Then $\mathrm{ad}_{s}$ is a $*$-derivation of $A$ that preserves $H(A)$ and $S(A)$, the map $s \mapsto \mathrm{ad}_{s}$ is a homomorphism of Lie algebras

$$
[\mathrm{ad}_{s}, \mathrm{ad}_{t}] = \mathrm{ad}_{[s,t]} ,
$$

and its kernel is the set of the central skew-Hermitian elements, that is $S(A) \cap Z(A)$.

**Proof.** The Leibniz rule for $\mathrm{ad}_{s}$ is the associativity of $A$:

$$
\mathrm{ad}_{s}(xy) = sxy - xys = (sx - xs)y + x(sy - ys) = \mathrm{ad}_{s}(x)\,y + x\,\mathrm{ad}_{s}(y) ,
$$

and $\mathrm{ad}_{s}(x)^{*} = (sx - xs)^{*} = x^{*}s^{*} - s^{*}x^{*} = s\,x^{*} - x^{*}s = \mathrm{ad}_{s}(x^{*})$, so $\mathrm{ad}_{s}$ commutes with the involution and is a $*$-derivation; it preserves each half because it commutes with $*$. The identity $[\mathrm{ad}_{s},\mathrm{ad}_{t}] = \mathrm{ad}_{[s,t]}$ is the Jacobi identity of the commutator, and it is a direct expansion:

$$
[\mathrm{ad}_{s},\mathrm{ad}_{t}](x) = \mathrm{ad}_{s}\bigl(\mathrm{ad}_{t}(x)\bigr) - \mathrm{ad}_{t}\bigl(\mathrm{ad}_{s}(x)\bigr) = [s,[t,x]] - [t,[s,x]] = [[s,t],x] = \mathrm{ad}_{[s,t]}(x) .
$$

Finally $\mathrm{ad}_{s} = 0$ if and only if $sx = xs$ for every $x$, that is if and only if $s$ is central. $\square$

**Remark.** The inner derivations of $\mathfrak{u}(A)$ are therefore the inner $*$-derivations of $A$ generated by the skew-Hermitian elements, and the central skew-Hermitian elements have the same standing in $\mathfrak{u}(A)$ as the centre has in $A$: they are the derivations that vanish. The general theory of the derivations, their module structure and the twisted derivation that the derived operation $x \star y = xy^{*}$ forces are *Derivations of a Sesqualgebra*; the Lie algebra generated by the $\mathrm{ad}_{s}$ is the inner part of $\operatorname{Der}(A)$ and is the subject of *Derivations of a Sesqualgebra*, §*The Inner Derivations*.

### The Unitary Group

**Theorem.** Let $u \in U(A)$ be unitary and let $\alpha_{u}(x) = uxu^{*}$. Then $\alpha_{u}$ preserves $S(A)$, and it is an automorphism of the Lie algebra $\mathfrak{u}(A)$:

$$
\alpha_{u}\bigl([x,y]\bigr) = \bigl[\alpha_{u}(x), \alpha_{u}(y)\bigr] \quad \text{for all } x, y \in S(A) .
$$

The assignment $u \mapsto \alpha_{u}$ is a homomorphism of the group $U(A)$ into the automorphism group of $\mathfrak{u}(A)$, and its kernel is the group of the central unitary elements.

**Proof.** For $s \in S(A)$, $\alpha_{u}(s)^{*} = (usu^{*})^{*} = u s^{*} u^{*} = -usu^{*}$, so $\alpha_{u}(s) \in S(A)$. For the bracket, $\alpha_{u}(xy - yx) = uxyu^{*} - uyxu^{*} = (uxu^{*})(uyu^{*}) - (uyu^{*})(uxu^{*}) = [\alpha_{u}(x), \alpha_{u}(y)]$, using the multiplicativity of the conjugation by $u$. The map is multiplicative in $u$, since $\alpha_{u}\alpha_{v} = \alpha_{uv}$, and it fixes $x$ for all $x$ exactly when $ux = xu$ for all $x$, that is when $u$ is central; this is the computation of *Units and the Unitary Elements*, §*Inner $*$-Automorphisms*, read on the skew-Hermitian half. $\square$

**Remark.** The unitary group therefore acts on its own Lie algebra by the adjoint action, the elements of the kernel being the central unitary elements; for $A = M_n(\mathbb{C})$ that kernel is the circle of the scalar unitary matrices. The same inner $*$-automorphisms act on the Hermitian Jordan algebra of *The Hermitian Jordan Algebra* by $x \mapsto uxu^{*}$, so that the two halves of the algebra carry the action of the same group, one as a Lie algebra and one as a Jordan algebra. The relation of the group to its Lie algebra through the exponential map belongs to Part II of the series and is *The Exponential Map on a Banach Sesqualgebra*.

## The Degeneration to the Bilinear Case

**Theorem.** Put $\varsigma = \mathrm{id}$. Then the fixed ring is all of $R$, the skew-Hermitian part is an $R$-submodule of $A$, and $\mathfrak{u}(A)$ is a Lie algebra over $R$, the skew part of *The Self-Adjoint Part of an Algebra*, §*The Skew Part as a Lie Algebra*.

**Proof.** With $\varsigma = \mathrm{id}$ the scalar rule of the two halves loses its twist, so $S(A)$ is stable under every scalar of $R$; the bracket is $R$-bilinear because the products are, and the closure and the Jacobi identity are the theorem above. $\square$

**Remark.** The comparison is the one of the two twins, and of the rows below only the first changes: the bilinear case is the sesquilinear one with the twist forgotten.

| | sesquilinear | bilinear ($\varsigma = \mathrm{id}$) |
|---|---|---|
| ring of scalars of the half | $R^{\varsigma}$ | $R$ |
| hypothesis on $2$ | none | none |
| the two halves | $H(A)$, $S(A)$, two $R^{\varsigma}$-modules | $H(A)$, $S(A)$, two $R$-submodules |
| the bracket on $S(A)$ | $xy - yx$ | $xy - yx$ |
| the structure on $H(A)$ | the Jordan algebra, needs $2$ invertible | the Jordan algebra, needs $2$ invertible |

The Lie rows of the table have the same entries in the two columns, and only the ring of scalars changes; the asymmetry between the two halves, that the Jordan half needs $2$ invertible and the Lie half does not, is present already in the bilinear theory and is not an effect of the twist.

## Worked Cases

### The Complex Matrices

For $A = M_n(\mathbb{C})$ with the conjugate transpose the skew-Hermitian matrices are the matrices $x$ with $x^{*} = -x$, that is $x = i\,h$ with $h$ Hermitian; they are the real span of the $n$ matrices $iE_{ii}$, the $n(n-1)/2$ matrices $E_{ij} - E_{ji}$ and the $n(n-1)/2$ matrices $i(E_{ij} + E_{ji})$ with $i < j$. The bracket is the commutator, and $\mathfrak{u}(A)$ is the Lie algebra $\mathfrak{u}(n)$ of the unitary group over $\mathbb{R}$, the skew-Hermitian matrices with the commutator. The Hermitian half is $\mathfrak{u}(n)$ multiplied by $i$, it is the Jordan algebra of *The Hermitian Jordan Algebra*, and the product of two of its elements is Hermitian exactly when they commute, which is the statement that the Hermitian matrices do not form an algebra under the product.

### The Field

For $A = \mathbb{C}$ over the datum $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation and the derived product $x \star y = x\bar y$, the involution is the conjugation, the Hermitian elements are the real numbers and the skew-Hermitian elements are the purely imaginary numbers, $S(A) = i\mathbb{R}$. The product of $\mathbb{C}$ is commutative, so the bracket vanishes identically and $\mathfrak{u}(A)$ is the abelian Lie algebra $i\mathbb{R}$ over $\mathbb{R}$. It is the smallest case in which the fixed ring is a proper subring of $R$ and the half a proper real form of the algebra, and it is the case in which the Lie algebra is as small as it can be.

### The Quaternions

For $A = \mathbb{H}$ with the quaternion conjugation over the datum $(\mathbb{R},\mathrm{id})$ the twist is invisible and the product is bilinear, so the case belongs to *The Self-Adjoint Part of an Algebra*. The skew-Hermitian quaternions are the purely imaginary ones, the span of $i$, $j$ and $k$, and the commutator of two of them is twice their cross product:

$$
[p,q] = pq - qp = 2\,(p \times q) \qquad (p, q \in \mathbb{H},\ p^{*} = -p,\ q^{*} = -q) .
$$

Hence $\mathfrak{u}(\mathbb{H})$ is the space of the purely imaginary quaternions with the bracket $2\,(\cdot \times \cdot)$, that is the cross product in disguise, and it is the compact Lie algebra of the unit quaternions. It is the case in which the sesquilinear layer and the bilinear one coincide, the fixed ring being the whole of $R$, and it is recorded to mark the boundary.

### The Biquaternion Algebra

For $A = \mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the star-involution the skew-Hermitian subspace is the purely imaginary part of the biquaternions, a real Lie algebra under the commutator, and its structure, its relation to the two copies of the complex numbers and its comparison with the other antisymmetrisations of the biquaternion products are *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. That article is the worked case in which the closure, the bracket and the inner derivations of this article are computed on a basis of eight elements, and it is the case that pairs the biquaternion half of the corpus with the general theory above.

## Summary

The skew-Hermitian elements of a sesqualgebra with a $\varsigma$-semilinear involution form, under the commutator $[x,y] = xy - yx$, a Lie algebra over the fixed ring $R^{\varsigma}$, with no hypothesis on $2$. The product of two skew-Hermitian elements is skew-Hermitian exactly when the two anticommute and Hermitian exactly when they commute, and the sum $xy + yx$ is always Hermitian; this is the reason the bracket is taken and not the product. The inner derivations $\mathrm{ad}_{s}$ for $s$ skew-Hermitian are the $*$-derivations of $A$ generated by that half, they satisfy $[\mathrm{ad}_{s},\mathrm{ad}_{t}] = \mathrm{ad}_{[s,t]}$, and their kernel is the centre intersected with the half. The unitary group acts on $\mathfrak{u}(A)$ by the inner $*$-automorphisms $x \mapsto uxu^{*}$, the kernel of the action being the central unitary elements.

The one structural difference from the bilinear theory of the skew part of *The Self-Adjoint Part of an Algebra* is the scalars: the base involution is not the identity, the two halves are modules over the fixed ring and not over $R$, and the Lie algebra is an algebra over $R^{\varsigma}$. Everything else is the closure computation of *Hermitian and Skew-Hermitian Elements* and the associativity of $A$, and the sharpest contrast with the Jordan twin of *The Hermitian Jordan Algebra* is the hypothesis: the Jordan identity is inherited from the associativity through a symmetrisation and needs $2$ invertible, whereas the Jacobi identity is inherited from the associativity through a rearrangement of the products and needs nothing.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathfrak{u}(A) = (S(A), [\ ,\ ])$ | the unitary Lie algebra |
| $S(A) = \{x : x^{*} = -x\}$ | the skew-Hermitian elements, the underlying set of $\mathfrak{u}(A)$ |
| $[x,y] = xy - yx$ | the commutator, the bracket of $\mathfrak{u}(A)$ |
| $R^{\varsigma}$ | the fixed ring, the scalars of $\mathfrak{u}(A)$ |
| $(xy)^{*} = yx$ | the reversal of the product of two skew-Hermitian elements |
| $xy = -yx$ | the anticommutation that keeps the product skew-Hermitian |
| $xy + yx \in H(A)$ | the Hermitian correction, the symmetrisation of the two products |
| $\mathrm{ad}_{s}(x) = [s,x]$ | the inner $*$-derivation attached to $s \in S(A)$ |
| $[\mathrm{ad}_{s},\mathrm{ad}_{t}] = \mathrm{ad}_{[s,t]}$ | the homomorphism of the half into $\operatorname{Der}(A)$ |
| $S(A) \cap Z(A)$ | the kernel of $s \mapsto \mathrm{ad}_{s}$ |
| $\alpha_{u}(x) = uxu^{*}$ | the adjoint action of $u \in U(A)$ on $\mathfrak{u}(A)$ |
| $[p,q] = 2\,(p \times q)$ | the quaternion case, the cross product up to the factor $2$ |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Lie axioms, the Jacobi identity, the inner derivations and the derivations as a Lie algebra.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the general theory, the classical algebras and the relation to the Lie algebra of a matrix group.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 1–3* (Springer, 1989), for the Lie algebra of a matrix group, the adjoint action and the exponential map.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the skew elements of a ring with involution and the commutator they carry.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of an algebra and the two halves they cut.
- The companion articles of this series: *Sesqualgebras*, *Hermitian and Skew-Hermitian Elements*, *Lie Algebras of Sesqualgebras*, *Derivations of a Sesqualgebra*, *Units and the Unitary Elements*, *The Hermitian Jordan Algebra*, *The Sesquilinear Commutator*, and *The Self-Adjoint Part of an Algebra*.
