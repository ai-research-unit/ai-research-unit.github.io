
# __Involutions of the Exterior Algebra__

## Introduction

The exterior algebra $\Lambda^\bullet V$ of a finite-dimensional vector space carries three canonical order-two maps that need no extra structure: the **grade involution** $\alpha$, an algebra automorphism acting by $(-1)^k$ on $\Lambda^kV$; the **reversion** $r$, an algebra anti-automorphism reversing the order of the factors; and their composite $\alpha r=\alpha\circ r$, the **reversal**, again an anti-automorphism. A fourth order-two map, the **Hodge star**, needs a symmetric bilinear form and an orientation and reverses the degree; it is named here and its theory is *The Hodge Star and the Real Structure of the Exterior Algebra*. This article, the fourth of the `- * Theory` group, defines the involutions and anti-involutions of the exterior algebra, classifies the degree-preserving ones that act by a scalar on each homogeneous component, identifies them as the grade involution, the reversion and the reversal, and exhibits their action on the wedge product and on the basis. The exterior algebra and the wedge product are *The Exterior Algebra*; the graded sign rule is *Superalgebras and Graded Structures*.

The base is a field $K$ of characteristic not two and $V$ has dimension $m$; the algebra is $A=\Lambda^\bullet V$ with homogeneous parts $A^k=\Lambda^kV$, the order-two maps are written $\alpha,r,\alpha r$, and the Hodge star is written $\star$. The article reasons with the grading and the product only.

## Involutions and Anti-Involutions

**Definition.** An **involution** of $A$ is a $K$-linear map $\varphi$ with $\varphi^2=\mathrm{id}$ and $\varphi(xy)=\varphi(x)\varphi(y)$; an **anti-involution** is a linear map $\varphi$ with $\varphi^2=\mathrm{id}$ and $\varphi(xy)=\varphi(y)\varphi(x)$. An involution or anti-involution is **graded** when it preserves the homogeneous degree and **reversing** when it sends $A^k$ to $A^{m-k}$.

**Definition.** A linear map $\varphi$ is a **signed identity** when it acts on each homogeneous component by a scalar, $\varphi(x)=\epsilon_kx$ for $x\in A^k$.

**Proposition.** A signed identity is an involution exactly when every $\epsilon_k=\pm1$; it is an algebra automorphism exactly when $\epsilon_k=\epsilon_1^{k}$ for all $k$, and then it is the identity if $\epsilon_1=1$ and the grade involution if $\epsilon_1=-1$.

**Proof.** An involution requires $\epsilon_k^2=1$; multiplicativity requires $\epsilon_{j+k}=\epsilon_j\epsilon_k$, which for a multiplicative family forces $\epsilon_k=\epsilon_1^k$; and then $\epsilon_1^2=1$ gives $\epsilon_1=\pm1$. $\square$

**Corollary.** The only degree-preserving algebra involutions of the exterior algebra that act by a scalar on each component are the identity and the grade involution; every other order-two automorphism of the exterior algebra arises from an order-two automorphism of $V$ and is not a signed identity unless it is one of these two.

## The Grade Involution

**Definition.** The **grade involution** is

$$
\alpha(x)=(-1)^k x\qquad (x\in A^k).
$$

**Proposition.** $\alpha$ is an algebra automorphism, $\alpha^2=\mathrm{id}$, and it is the unique automorphism of $A$ that extends the map $v\mapsto-v$ on $V$.

**Proof.** Multiplicativity is $\alpha(xy)=(-1)^{|x|+|y|}xy=\alpha(x)\alpha(y)$; the extension statement follows because $V=A^1$ determines the signs $\epsilon_k=(-1)^k$ and hence $\alpha$. $\square$

**Corollary.** The fixed algebra of $\alpha$ is the even part $A^{\mathrm{even}}$ and its anti-fixed part is the odd part $A^{\mathrm{odd}}$; $\alpha$ is the grade involution of the $\mathbb{Z}/2$-grading of $A$, in the sense of *Superalgebras and Graded Structures*.

## Reversion and the Reversal

**Definition.** The **reversion** $r$ is the linear map determined on products by

$$
r(v_1\wedge\cdots\wedge v_k)=v_k\wedge\cdots\wedge v_1,
$$

and the **reversal** is the composite $\alpha r$. On a homogeneous element of degree $k$,

$$
r(x)=(-1)^{k(k-1)/2}x,\qquad \alpha r(x)=(-1)^{k(k+1)/2}x .
$$

**Proof.** Reversing the order of $k$ factors takes $k(k-1)/2$ transpositions of neighbours, each contributing $-1$ by the graded commutativity of the wedge product; composing with $\alpha$ adds the sign $(-1)^k$, and $k(k-1)/2+k=k(k+1)/2$. $\square$

**Theorem.** The reversion is an anti-involution, $r(xy)=r(y)r(x)$ and $r^2=\mathrm{id}$; so is the reversal; and $\alpha$ commutes with $r$. The three maps $\mathrm{id},\alpha,r,\alpha r$ form a group isomorphic to $(\mathbb{Z}/2)^2$ under composition.

**Proof.** Reversion reverses the order of each wedge of factors, so it converts a product into the product in the reverse order; applying it twice restores the order; the reversal is the composite of two commuting order-two maps; the group table is immediate. $\square$

**Corollary.** The signs $(-1)^k$, $(-1)^{k(k-1)/2}$ and $(-1)^{k(k+1)/2}$ distinguish the three non-identity members on the homogeneous components, and they agree on the even part; on the odd part the grade involution is $-1$, while reversion is $-1$ for $k\equiv2,3\pmod 4$.

## The Hodge Star, Named

**Remark (forward reference).** When $V$ carries a nondegenerate symmetric bilinear form and an orientation, the Hodge star $\star$ is a linear map reversing the degree, $\star:A^k\to A^{m-k}$, determined by $\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\theta$ for the volume element $\theta$; it is an involution up to the sign $(-1)^{k(m-k)}$ and it is not an algebra homomorphism or anti-homomorphism. Its theory, its square, the real and the complex structures it defines on the exterior algebra and the relative positions of $\star$ with $\alpha,r,\alpha r$ are the subject of *The Hodge Star and the Real Structure of the Exterior Algebra*; the form and the orientation are not used here.

## Worked Case: The Exterior Algebra of a Two-Dimensional Space

Let $V$ have basis $e_1,e_2$, so $A$ has basis $1,e_1,e_2,e_1e_2$. The three involutions act as

| | $1$ | $e_1$ | $e_2$ | $e_1e_2$ |
|---|---|---|---|---|
| $\alpha$ | $1$ | $-e_1$ | $-e_2$ | $e_1e_2$ |
| $r$ | $1$ | $e_1$ | $e_2$ | $-e_1e_2$ |
| $\alpha r$ | $1$ | $-e_1$ | $-e_2$ | $-e_1e_2$ |

so $\alpha$ negates the vectors and fixes the top element, $r$ fixes the vectors and negates the top element, and $\alpha r$ negates both. The anti-involution property of $r$ is visible on $e_1e_2$: $r(e_1e_2)=e_2\wedge e_1=-e_1e_2=r(e_2)r(e_1)$.

**Verified.** The table was recomputed from the signs $(-1)^k$, $(-1)^{k(k-1)/2}$, $(-1)^{k(k+1)/2}$ and checked against the products of the basis elements; the anti-involution property was checked on all products of basis elements.

## Summary

The exterior algebra $A=\Lambda^\bullet V$ carries the order-two maps $\alpha,r,\alpha r$: the **grade involution** $\alpha$, the unique algebra automorphism extending $v\mapsto-v$, acting by $(-1)^k$ on $A^k$; the **reversion** $r$, the anti-automorphism reversing the order of the factors, acting by $(-1)^{k(k-1)/2}$; and the **reversal** $\alpha r$, acting by $(-1)^{k(k+1)/2}$. They form a group $(\mathbb{Z}/2)^2$ and agree on the even part. Among the degree-preserving algebra involutions acting by a scalar on each component, only the identity and $\alpha$ occur; the reversion and the reversal are anti-involutions. The **Hodge star** is the degree-reversing order-two-up-to-sign map that needs a symmetric bilinear form and an orientation, and it is named here and treated in *The Hodge Star and the Real Structure of the Exterior Algebra*. For the exterior algebra of a two-dimensional space the three maps are displayed by their action on the basis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $V$ | a finite-dimensional $K$-vector space of dimension $m$ |
| $A=\Lambda^\bullet V$ | the exterior algebra, with parts $A^k=\Lambda^kV$ |
| $\alpha$ | the grade involution, $(-1)^k$ on $A^k$ |
| $r$ | the reversion, $(-1)^{k(k-1)/2}$ on $A^k$ |
| $\alpha r$ | the reversal, $(-1)^{k(k+1)/2}$ on $A^k$ |
| $\star$ | the Hodge star, named, deferred |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for the exterior algebra, its grading and its anti-automorphisms.
- Werner Greub, *Multilinear Algebra*, Universitext (Springer, 2nd ed. 1978), for the involutions of the exterior and Clifford algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reversion, the grade involution and the Hodge star.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works, Volume 2 (Springer, 1997), for the order-two maps of the exterior algebra.
