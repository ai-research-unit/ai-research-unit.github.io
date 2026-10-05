# __Involutions of a Tensor Power__

## Introduction

An involution of a linear space acts on every tensor power, on every symmetric power and on every exterior power, and the three families behave differently: the tensor and exterior powers carry induced involutions with closed formulas for the type, while the symmetric powers do not. This article develops the tensor power, the flip and the two powers it cuts out, the induced involutions and their types, and the reason the symmetric case is exceptional. It is the tensor-level companion of *Involutions of the Dual Space* and *Involutions of a Graded Linear Space* inside the `*`-theory group.

*Involutive Linear Spaces* states, among the induced involutions, the type of $T^{\otimes k}$ and of the operator induced on $\Lambda^{k}V$, and warns that the symmetric powers have no such formula; this article is the detailed owner of those statements, adding the flip, the decomposition of the tensor square into its symmetric and alternating parts, and the action of the involution on each. The multilinear spaces, the tensor product and the universal property are *Multilinear Spaces* and *The Balanced Product*; the symmetric and exterior algebras and the sign rule are the symmetric-bilinear-algebra and the graded categories and are named only as the owners of what is not used here. The forms are Part II.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, $T$ is a linear involution of $V$ of type $(p,q)$, and $V^{\otimes k}$, $S^{k}V$ and $\Lambda^{k}V$ are the $k$-fold tensor, symmetric and exterior powers of $V$. The flip is $\tau : V\otimes V \to V\otimes V$, $\tau(x\otimes y) = y\otimes x$. No form and no topology is used.

## The Tensor Power

**Definition.** The **induced involution** on $V^{\otimes k}$ is $T^{\otimes k} = T\otimes\cdots\otimes T$, defined on elementary tensors by $T^{\otimes k}(x_1\otimes\cdots\otimes x_k) = Tx_1\otimes\cdots\otimes Tx_k$ and extended linearly.

**Proposition.** $T^{\otimes k}$ is a linear involution of $V^{\otimes k}$, and its type is

$$
\Bigl( \sum_{j\ \mathrm{even}} \binom{k}{j} p^{\,k-j}q^{\,j},\ \sum_{j\ \mathrm{odd}} \binom{k}{j} p^{\,k-j}q^{\,j} \Bigr), \qquad \operatorname{tr}\bigl(T^{\otimes k}\bigr) = (p-q)^{k} .
$$

**Proof.** $(T^{\otimes k})^2 = (T^2)^{\otimes k} = \mathrm{id}$. A basis vector of $V^{\otimes k}$ is a word in $k$ basis vectors of $V$; its eigenvalue under $T^{\otimes k}$ is the product of the eigenvalues of the letters, hence $+1$ if the number $j$ of negated letters is even and $-1$ if it is odd, and the number of words with a prescribed $j$ is $\binom{k}{j}p^{k-j}q^{j}$. The trace is the difference of the two parts of the type, which is $(p-q)^k$.

**Corollary (the tensor algebra).** The maps $T^{\otimes k}$ assemble to an algebra automorphism of the tensor algebra $T(V)$ of order two, fixing the unit; it preserves the grading by the number of factors and acts on the degree-$k$ part as $T^{\otimes k}$. The tensor algebra and its automorphisms belong to the symmetric-bilinear-algebra category of this Part, later in it, and the statement is recorded here only to place the graded pieces.

**Proof.** On the concatenation product of two tensors the definition gives
$T^{\otimes(k+\ell)}(x\otimes y) = T^{\otimes k}(x)\otimes T^{\otimes\ell}(y)$; the maps therefore preserve the product, and the unit is fixed.

## The Flip and the Two Powers

**Proposition (the flip and its eigenspaces).** The flip $\tau$ is a linear involution of $V\otimes V$, and since $2 \neq 0$ the space $V\otimes V$ is the direct sum of the **symmetric square** and the **alternating square**,

$$
V\otimes V = S^{2}V \oplus \Lambda^{2}V, \qquad
S^{2}V = \ker(\tau-\mathrm{id}), \qquad \Lambda^{2}V = \ker(\tau+\mathrm{id}) ,
$$

of dimensions $n(n+1)/2$ and $n(n-1)/2$.

**Proof.** $\tau^2 = \mathrm{id}$ because $\tau(x\otimes y) = y\otimes x$ and applying it twice returns $x\otimes y$; the projectors $\tfrac12(\mathrm{id}\pm\tau)$ exhibit the direct sum, and the dimensions are the standard counts for a symmetric and an alternating form on $n$ letters.

**Proposition (the induced involution preserves the two parts).** $T\otimes T$ commutes with the flip, $(T\otimes T)\tau = \tau(T\otimes T)$, so it preserves $S^{2}V$ and $\Lambda^{2}V$; the induced involutions are the ones denoted $S^{2}T$ and $\Lambda^{2}T$, and the type of $T\otimes T$ is the sum of their types.

**Proof.** For an elementary tensor, $(T\otimes T)\tau(x\otimes y) = Tx\otimes Ty = \tau(Ty\otimes Tx)$ after the flip, so $(T\otimes T)\tau = \tau(T\otimes T)$; an operator commuting with an involution preserves its eigenspaces, and the type of $T\otimes T$ is the sum of the types of the restrictions.

### The Exterior Power

**Proposition (the induced involution on $\Lambda^{k}V$).** On the $k$-th exterior power the induced involution $\Lambda^{k}T$ is a linear involution of type

$$
\Bigl( \sum_{j\ \mathrm{even}} \binom{p}{k-j}\binom{q}{j},\ \sum_{j\ \mathrm{odd}} \binom{p}{k-j}\binom{q}{j} \Bigr),
\qquad \operatorname{tr}\bigl(\Lambda^{k}T\bigr) = \sum_{j} (-1)^{j}\binom{p}{k-j}\binom{q}{j} ,
$$

with $0 \le k-j \le p$ and $0 \le j \le q$; for $k = n$ the operator is multiplication by $\det T = (-1)^{q}$.

**Proof.** A basis of $\Lambda^{k}V$ is given by the wedges $e_{i_1}\wedge\cdots\wedge e_{i_k}$ with $i_1<\cdots<i_k$; the induced operator multiplies a wedge by the product of the eigenvalues of its factors, which is $+1$ if the number $j$ of factors drawn from $V_-$ is even and $-1$ if it is odd, and the count of such wedges is $\binom{p}{k-j}\binom{q}{j}$; the trace is the difference of the two parts, and the top exterior power is one-dimensional, spanned by the wedge of a basis of $V$, on which the operator acts by the product of the eigenvalues, that is $\det T = (-1)^q$.

### The Symmetric Power

**Remark (the symmetric powers have no closed type formula).** On $S^{k}V$ the induced involution multiplies a monomial $x_1\cdots x_k$ by the product of the eigenvalues, which is $\pm1$ according to the parity of the number of factors drawn from $V_-$ **counted with multiplicity**; the type is therefore the multiset count, not a single binomial sum, and it depends on the parities of the multiplicities. The smallest display is $S^{1}V = V$ with the involution $T$ of type $(p,q)$; in particular no statement of the form "the symmetric power is fixed" can hold. The exterior powers are the well-behaved family.

**Proof.** The monomials in a basis of eigenvectors with repetition of total degree $k$ form a basis of $S^{k}V$, and the eigenvalue on a monomial is computed as for the tensor power; the count is the number of multisets of size $k$ drawn from the multiset of eigenvalues, which is not a product of binomial coefficients. The case $k=1$ gives back the space $V$ and the operator $T$.

## The Flip and the Deferred Sign

**Remark (the sign rule).** On the tensor square the flip satisfies $\tau^2 = \mathrm{id}$, and its two eigenspaces are the symmetric and the alternating squares; the assignment $\tau = -\mathrm{id}$ on the odd-odd part of a graded tensor square, which makes the flip an odd map and the tensor product of graded algebras a graded algebra, is the **sign rule** and belongs to *Superalgebras and Graded Structures*. It is named here because the involution on a graded tensor power is stated with it there and without it here.

## Summary

A linear involution $T$ of type $(p,q)$ induces on the $k$-fold tensor power the involution $T^{\otimes k}$, of type $(\sum_{j\ \mathrm{even}}\binom{k}{j}p^{k-j}q^{j}, \sum_{j\ \mathrm{odd}}\binom{k}{j}p^{k-j}q^{j})$ and trace $(p-q)^{k}$; on the $k$-th exterior power $\Lambda^{k}T$, of the analogous type with the binomials $\binom{p}{k-j}\binom{q}{j}$ and trace $\sum_j(-1)^j\binom{p}{k-j}\binom{q}{j}$, the top exterior power acting by $\det T = (-1)^{q}$; and on the symmetric power $S^{k}V$ it has no closed type formula, because the count is a multiset count, the case $S^{1}V = V$ displaying the failure. The maps $T^{\otimes k}$ assemble into an algebra automorphism of the tensor algebra of order two. The flip $\tau$ of the tensor square is an involution whose fixed and negated parts are the symmetric and the alternating squares, and $T\otimes T$ commutes with it, so it preserves both parts; the two involutions $S^{2}T$ and $\Lambda^{2}T$ are the restrictions. The sign rule on the flip is *Superalgebras and Graded Structures*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the field of scalars, of characteristic not two |
| $V$, $n$ | the space and its dimension |
| $T$ | a linear involution of type $(p,q)$ |
| $V^{\otimes k}$, $S^{k}V$, $\Lambda^{k}V$ | tensor, symmetric and exterior powers |
| $T^{\otimes k}$ | the induced involution on $V^{\otimes k}$ |
| $\Lambda^{k}T$, $S^{k}T$ | the induced involutions on $\Lambda^{k}V$, $S^{k}V$ |
| $\tau(x\otimes y) = y\otimes x$ | the flip of the tensor square |
| $S^{2}V = \ker(\tau-\mathrm{id})$, $\Lambda^{2}V = \ker(\tau+\mathrm{id})$ | symmetric and alternating squares |
| $(T^{\otimes k})^{2}=\mathrm{id}$, $\operatorname{tr}T^{\otimes k}=(p-q)^{k}$ | the tensor laws |
| $\det T = (-1)^{q}$ | the action on the top exterior power |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for tensor, symmetric and exterior powers and the actions of an operator on them.
- Werner Greub, *Multilinear Algebra* (Springer, 2nd ed. 1978), for the tensor algebra and the symmetric and exterior algebras.
- Nathan Jacobson, *Lectures in Abstract Algebra*, volume II: *Linear Algebra* (Van Nostrand, 1953), for the induced maps on the tensor and exterior powers.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the multilinear constructions and the flip.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the sign rule and the graded tensor product.
