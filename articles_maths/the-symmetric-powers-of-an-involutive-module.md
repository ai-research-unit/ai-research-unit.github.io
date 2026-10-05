# __The Symmetric Powers of an Involutive Module__

## Introduction

The symmetric algebra of a module $M$ is graded, $\operatorname{Sym}(M) = \bigoplus_{k\ge0}\operatorname{Sym}^k(M)$, and an involution $\sigma_M$ of $M$ induces an involution $\sigma$ of the whole algebra; the degree is preserved, so the induced involution restricts to an involution $\sigma_k$ of each **symmetric power** $\operatorname{Sym}^k(M)$. The eigenvalues of $\sigma_k$ are $\pm1$, because $\sigma_k$ is an involution, and the two eigenspaces are the **symmetric part** $\operatorname{Sym}^k(M)^+$ and the **skew part** $\operatorname{Sym}^k(M)^-$ of the power; the decomposition $\operatorname{Sym}^k(M) = \operatorname{Sym}^k(M)^+\oplus\operatorname{Sym}^k(M)^-$ is the degree-$k$ part of the decomposition of the symmetric algebra, and the sum of the symmetric parts over all $k$ is the fixed subalgebra computed in *The Symmetric Algebra of a Module with an Involution*. The purpose of this article is to compute the eigenvalues explicitly and to describe the two eigenspaces.

The article restricts the induced involution to each homogeneous piece and shows that the eigenvalue of a monomial is $(-1)^{j}$, where $j$ is the number of its factors drawn from the anti-fixed part $M^-$ of the module; in a basis of eigenvectors of $\sigma_M$ with $p$ fixed and $q$ anti-fixed vectors, the generating function of the eigenvalues is $1/((1-t)^p(1+t)^q)$, and the symmetric and the skew parts of the power have the generating functions $\tfrac12\bigl(1/((1-t)^{p+q}) \pm 1/((1-t)^p(1+t)^q)\bigr)$. The two parts are then combined over all degrees, and the fixed subalgebra of the symmetric algebra is recognised as the sum of the symmetric parts; the worked cases are the two-dimensional module with the swapped basis and the one-dimensional module with $\sigma_M = -1$, where the involution of $\operatorname{Sym}^k$ is the parity $(-1)^k$.

The article assumes *The Symmetric Algebra of a Module with an Involution* for the induced involution and its fixed subalgebra, *The Symmetric and Exterior Powers* for $\operatorname{Sym}^k(M)$, *Involutive Linear Spaces* for the involution of a module, *The Symmetric Algebra of a Module* for the universal property, and *Linear Algebra* for the bases of eigenvectors. The involution-invariant ideals of the symmetric algebra are *Involution-Invariant Ideals of the Symmetric Algebra*, later in this group. Throughout, $R$ is a commutative ring with identity, $M$ is an $R$-module with an $R$-linear involution $\sigma_M$, $M^+$ and $M^-$ are the fixed and anti-fixed parts, $\sigma_k$ is the induced involution of $\operatorname{Sym}^k(M)$, and no form, norm or distance occurs.

## The Induced Involution on the Symmetric Powers

### Restriction to a Homogeneous Piece

**Definition.** The **$k$-th symmetric power** $\operatorname{Sym}^k(M)$ is the $R$-span of the products $v_1\cdots v_k$ of $k$ elements of $M$; the symmetric algebra is the direct sum of the $\operatorname{Sym}^k(M)$. The **induced involution of the power** is

$$
\sigma_k = \sigma|_{\operatorname{Sym}^k(M)} : \operatorname{Sym}^k(M)\to\operatorname{Sym}^k(M), \qquad \sigma_k(v_1\cdots v_k) = \sigma_M(v_1)\cdots\sigma_M(v_k).
$$

**Theorem.** $\sigma_k$ is well defined, $R$-linear, and an involution of the power: $\sigma_k^2 = \mathrm{id}$. The map $\sigma_k$ is the $k$-th symmetric power of the map $\sigma_M$, and the induced involution $\sigma$ of the symmetric algebra is the direct sum of the $\sigma_k$.

*Proof.* The products of $k$ elements span the power and the relations are preserved by the multiplicativity of the induced involution, so $\sigma$ restricts as displayed; $\sigma_k^2 = \mathrm{id}$ is the restriction of $\sigma^2 = \mathrm{id}$; the direct-sum statement is the degree preservation. $\square$

**Corollary.** The involution $\sigma_k$ is a linear map of the power of order two, so the power splits as the direct sum of its eigenvalue-one and eigenvalue-minus-one parts when $2$ is invertible:

$$
\operatorname{Sym}^k(M) = \operatorname{Sym}^k(M)^+ \oplus \operatorname{Sym}^k(M)^- .
$$

**Definition.** The **symmetric part** of the power is $\operatorname{Sym}^k(M)^+ = \{u : \sigma_k(u) = u\}$ and the **skew part** is $\operatorname{Sym}^k(M)^- = \{u : \sigma_k(u) = -u\}$; a monomial is **symmetric** when it is fixed and **skew** when it is negated.

## Eigenvalues and the Sign

### The Eigenvalue of a Monomial

**Theorem.** Suppose that $M$ decomposes as $M = M^+\oplus M^-$ — which holds when $2$ is invertible or when the involution is split — and let $m = v_1\cdots v_k$ be a monomial with each factor homogeneous with respect to the eigenspace decomposition. Then

$$
\sigma_k(m) = (-1)^{j}m, \qquad j = \#\{i : v_i \in M^-\},
$$

the number of the factors drawn from the anti-fixed part. Hence a monomial is symmetric exactly when it has an even number of anti-fixed factors, and skew exactly when the number is odd.

*Proof.* $\sigma_M(v_i) = v_i$ for a factor in $M^+$ and $\sigma_M(v_i) = -v_i$ for a factor in $M^-$, so $\sigma_M(v_1)\cdots\sigma_M(v_k) = (-1)^j v_1\cdots v_k$. $\square$

**Corollary (dimension count).** Let $M$ be free with $p$ fixed and $q$ anti-fixed basis elements, so $M = M^+\oplus M^-$ with $\dim M^+ = p$, $\dim M^- = q$. The **character** of $\sigma_k$ and the two generating functions are

$$
\sum_{k\ge0}\operatorname{tr}(\sigma_k)\,t^k = \frac{1}{(1-t)^p(1+t)^q}, \qquad
\sum_{k\ge0}\dim\operatorname{Sym}^k(M)^\pm\,t^k = \frac12\left(\frac{1}{(1-t)^{p+q}} \pm \frac{1}{(1-t)^p(1+t)^q}\right).
$$

*Proof.* A monomial $u^a v^b$ with $u$ in the fixed basis (degree $a$) and $v$ in the anti-fixed basis (degree $b$) has eigenvalue $(-1)^b$, so the trace generating function sums $(-1)^b t^{a+b}$ over the monomials, which is $\bigl(\sum_a t^a\bigr)^p\bigl(\sum_b(-t)^b\bigr)^q = 1/((1-t)^p(1+t)^q)$. The fixed and the skew parts are the $\pm1$-eigenspaces, with the projectors $\tfrac12(\mathrm{id}\pm\sigma)$, giving the second formula from the first and the total generating function $1/(1-t)^{p+q}$. $\square$

## The Decomposition

### The Two Eigenspaces

**Theorem.** With $M = M^+\oplus M^-$ and $2$ invertible, the symmetric and the skew parts of the power are

$$
\operatorname{Sym}^k(M)^+ = \operatorname{span}_R\{v_1\cdots v_k : \#\{i : v_i\in M^-\} \ \text{even}\}, \qquad
\operatorname{Sym}^k(M)^- = \operatorname{span}_R\{v_1\cdots v_k : \#\{i : v_i\in M^-\} \ \text{odd}\},
$$

and the projections onto the two summands are $\tfrac12(\mathrm{id}\pm\sigma_k)$. The symmetric part is spanned by the products of the fixed elements together with the products with pairs of anti-fixed elements, and the skew part is spanned by the products with an odd number of anti-fixed factors.

*Proof.* The eigenvalue formula gives the spanning sets, and the projectors split the identity by $\sigma_k^2 = \mathrm{id}$. $\square$

### The Sum Over the Degrees

**Theorem.** The fixed subalgebra of the symmetric algebra is the direct sum of the symmetric parts of the powers,

$$
\operatorname{Sym}(M)^\sigma = \bigoplus_{k\ge0}\operatorname{Sym}^k(M)^+ ,
$$

and it is a graded subalgebra of $\operatorname{Sym}(M)$; the skew elements form the complementary graded submodule $\bigoplus_k\operatorname{Sym}^k(M)^-$, which is not a subalgebra but satisfies $\operatorname{Sym}(M)^-\cdot\operatorname{Sym}(M)^-\subseteq\operatorname{Sym}(M)^+$.

*Proof.* The induced involution preserves the degree, so the fixed set is the sum of the fixed sets of the pieces; the fixed set of an algebra automorphism is a subalgebra; the products of two skew monomials have an even number of anti-fixed factors, hence are fixed. $\square$

**Corollary.** The fixed subalgebra is the commutant of the involution inside the symmetric algebra: $\operatorname{Sym}(M)^\sigma$ is generated by $M^+$ and by the products of pairs of elements of $M^-$, matching the description of *The Symmetric Algebra of a Module with an Involution*.

## Examples

**Example (the swapped basis).** Let $M = R^2$ with basis $e_1, e_2$ and $\sigma_M$ exchanging them, and let $2$ be invertible. Then $M^+ = R(e_1+e_2)$ and $M^- = R(e_1-e_2)$, so $p = q = 1$. The character is $1/((1-t)(1+t)) = 1/(1-t^2)$, giving $\operatorname{tr}(\sigma_k) = 1$ for even $k$ and $0$ for odd $k$; the generating functions are $\tfrac12\bigl(1/(1-t)^2 \pm 1/(1-t^2)\bigr)$. In degree two, $\operatorname{Sym}^2(M)$ has basis $e_1^2, e_1e_2, e_2^2$, the symmetric part is spanned by $e_1e_2$ and $e_1^2+e_2^2$, and the skew part by $e_1^2-e_2^2$; the dimensions $2$ and $1$ agree with the generating function, whose $t^2$-coefficient is $\tfrac12(3\pm1)$.

**Example (the single anti-fixed generator).** Let $M = R$ with $\sigma_M = -1$, so $p = 0$, $q = 1$ and $\operatorname{Sym}^k(M)\cong R$ with $\sigma_k = (-1)^k$. The symmetric part is $R$ in even degrees and $0$ in odd degrees, the skew part is complementary, and the generating function $\tfrac12\bigl(1/(1-t)\pm1/(1+t)\bigr)$ gives $1/(1-t^2)$ for the symmetric part and $t/(1-t^2)$ for the skew part. The fixed subalgebra is the even polynomial ring $R[x^2]$ of *Commutative Algebras with an Involution*.

**Example (the trivial involution).** If $\sigma_M = \mathrm{id}$ then $M = M^+$, $q = 0$, the induced involution of every power is the identity, and $\operatorname{Sym}^k(M)^+ = \operatorname{Sym}^k(M)$, $\operatorname{Sym}^k(M)^- = 0$; the fixed subalgebra is the whole symmetric algebra.

## Summary

An $R$-linear involution $\sigma_M$ of a module $M$ restricts to an involution $\sigma_k$ of each **symmetric power** $\operatorname{Sym}^k(M)$, which therefore splits as the direct sum of its **symmetric part** $\operatorname{Sym}^k(M)^+$ and its **skew part** $\operatorname{Sym}^k(M)^-$ when $2$ is invertible. A monomial has eigenvalue $(-1)^j$, where $j$ is the number of its factors from the anti-fixed part $M^-$; in a basis with $p$ fixed and $q$ anti-fixed vectors the character of $\sigma_k$ has generating function $1/((1-t)^p(1+t)^q)$ and the two eigenspaces have the generating functions $\tfrac12(1/(1-t)^{p+q}\pm1/((1-t)^p(1+t)^q))$. The sum of the symmetric parts is the fixed subalgebra of the symmetric algebra, a graded subalgebra generated by $M^+$ and the products of pairs of elements of $M^-$; the skew parts form a graded submodule whose products land in the fixed subalgebra. The swapped and the negated bases are the worked examples. No form, norm or distance occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $\sigma_M$ | Module with an $R$-linear involution |
| $M^+, M^-$ | Fixed and anti-fixed parts |
| $\operatorname{Sym}^k(M)$ | $k$-th symmetric power |
| $\sigma_k$ | Induced involution of the power |
| $\operatorname{Sym}^k(M)^\pm$ | Symmetric and skew parts |
| $\sigma_k(m) = (-1)^j m$ | Eigenvalue $j$ anti-fixed factors |
| $\sum\operatorname{tr}(\sigma_k)t^k = 1/((1-t)^p(1+t)^q)$ | Character generating function |
| $\tfrac12(1/(1-t)^{p+q}\pm1/((1-t)^p(1+t)^q))$ | Dimensions of the two eigenspaces |
| $\operatorname{Sym}(M)^\sigma = \bigoplus_k\operatorname{Sym}^k(M)^+$ | Fixed subalgebra |

## Further Reading

- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for the symmetric powers, the symmetric algebra and their functoriality.
- Werner Greub, *Multilinear Algebra* (Springer, second edition, 1978), for the symmetric powers of a module and the decompositions.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of a module and their induced maps on the tensor constructions.
- Igor Shafarevich and Alexander Kostrikin, *Linear Algebra and Geometry* (Gordon and Breach, 1989), for the symmetric powers over a field and the eigenspace decompositions.
- Serge Lang, *Algebra* (Springer, revised third edition, 2002), for the symmetric and the tensor algebras and the functorial properties.
