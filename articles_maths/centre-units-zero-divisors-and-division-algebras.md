
# __Centre, Units, Zero Divisors and Division Algebras__

## Introduction

The ideal theory of *Ideals and Quotients of Algebras* divides an algebra by its two-sided ideals. This article studies the elements of an algebra rather than its ideals: which elements commute with everything, which are invertible, which annihilate something nonzero, and when the three notions combine to make the algebra a division algebra.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, and $A$ is an $R$-algebra. The centre, the group of units and the notion of a zero divisor are meaningful for a general algebra, but the theory is at its sharpest for a **unital associative** algebra, and most statements below assume unitality and associativity and say so. The base ring stays a commutative ring except where the classical theorems require a field; those places are flagged.

The article closes with the **regular module** $A_A$: the algebra acting on itself by right multiplication. Its submodules are the right ideals, and the simplicity of $A_A$ is exactly the division-algebra condition. This is the bridge from elements to modules, and it prepares the module theory of category 08.

## The Centre

**Definition.** Let $A$ be an $R$-algebra. The **centre** of $A$ is the set

$$
Z(A) = \{z \in A : za = az \text{ for all } a \in A\}.
$$

Equivalently, $Z(A)$ is the centralizer of $A$ in itself: $Z(A) = C_A(A)$ where the **centralizer** of a subset $S \subseteq A$ is

$$
C_A(S) = \{a \in A : as = sa \text{ for all } s \in S\}.
$$

The centre is the set of elements whose left and right multiplications coincide.

**Proposition.** Let $A$ be associative. Then $Z(A)$ is a commutative subalgebra of $A$, and if $A$ is unital then $1_A \in Z(A)$.

*Proof.* If $z, w \in Z(A)$ and $a \in A$, then

$$
(z + w)a = za + wa = az + aw = a(z + w), \qquad (zw)a = z(wa) = z(aw) = (za)w = (az)w = a(zw),
$$

using associativity in the second chain; so $Z(A)$ is closed under addition and multiplication and is a subalgebra. For $z, w \in Z(A)$,

$$
zw = wz,
$$

because $z$ is central; so $Z(A)$ is commutative. Finally $1_A a = a = a 1_A$ for all $a$. $\square$

Associativity is essential in the displayed chain $(zw)a = z(wa)$. Without it the centre of a non-associative algebra need not be closed under multiplication, and one accordingly defines the centre of a non-associative algebra as the set of elements satisfying the *three* centrality conditions $za = az$, $z(ab) = (za)b$, and $(ab)z = a(bz)$ for all $a,b$; for an associative algebra the last two are automatic. This article uses the associative convention.

**Proposition.** An algebra automorphism $\sigma \in \operatorname{Aut}_R(A)$ maps $Z(A)$ onto itself.

*Proof.* If $z$ is central then for every $x$,

$$
\sigma(z)x = \sigma(z)\sigma(\sigma^{-1}(x)) = \sigma(z\sigma^{-1}(x)) = \sigma(\sigma^{-1}(x)z) = \sigma(\sigma^{-1}(x))\sigma(z) = x\sigma(z),
$$

so $\sigma(z)$ is central; applying the same to $\sigma^{-1}$ gives equality of sets. $\square$

This is why restriction to the centre governs the automorphism group; it is used.

**Definition.** An algebra $A$ over a commutative ring $R$ is **central** if $Z(A) = R \cdot 1_A$, that is, if the only central elements are the scalars; it is **central simple** if in addition it is simple.

**Example (the small algebras).** The centres of the standard examples are immediate from the multiplication:

| Algebra $A$ | $Z(A)$ | Comment |
|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | a field, central over itself |
| $\mathbb{C}$ | $\mathbb{C}$ | commutative, so $Z(\mathbb{C}) = \mathbb{C}$ |
| $\mathbb{D}$ | $\mathbb{D}$ | commutative |
| $\mathbb{D}'$ | $\mathbb{D}'$ | commutative |
| $\mathbb{H}$ | $\mathbb{R}\cdot 1$ | central over $\mathbb{R}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\mathbb{D}\cdot 1$ | the split complex scalars |
| $\mathbb{B}$ | $\mathbb{C}\cdot 1$ | the central scalar imaginary $i$ commutes with everything |
| $M_n(k)$ | $k \cdot I_n$ | the scalar matrices |

The entries for $\mathbb{H}$, $\mathbb{H}_{\mathbb{D}}$ and $\mathbb{B}$ follow from the scalar-vector multiplication formula: an element commutes with every pure vector precisely when its vector part is zero, and the scalars that commute with the quaternion units are exactly the coefficients in the ground ring. In $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the centre is the copy of $\mathbb{C}$ spanned by $e_0$, of real dimension $2$; in the eight-dimensional real view this is the subspace $\mathbb{C}_{\mathbb{B}}$.

**Example (matrix and endomorphism algebras).** For a commutative ring $R$ and $n \geq 1$, the centre of $M_n(R)$ is the set of scalar matrices $\{r I_n : r \in R\}$, isomorphic to $R$. Indeed a matrix commuting with every matrix unit $E_{ij}$ is scalar. More generally, for a faithful module $M$ over a ring $A$, the centre of $\operatorname{End}_A(M)$ need not be the scalars; for $A$ central simple and $M$ the regular module it is.

**Proposition (centre of a tensor product).** Let $A$ and $B$ be unital associative $R$-algebras. Then

$$
Z(A) \otimes_R Z(B) \;\subseteq\; Z(A \otimes_R B),
$$

with the inclusion realised by $z \otimes w \mapsto z \otimes w$. If $A$ and $B$ are central simple algebras over a field $F$, then $A \otimes_F B$ is central simple and $Z(A \otimes_F B) = F = Z(A) \otimes_F Z(B)$.

*Proof.* If $z \in Z(A)$ and $w \in Z(B)$ then for all $a \in A$, $b \in B$,

$$
(z \otimes w)(a \otimes b) = za \otimes wb = az \otimes bw = (a \otimes b)(z \otimes w),
$$

and both sides extend bilinearly, so $z \otimes w$ is central. The second statement is the standard theorem that the tensor product of central simple algebras is central simple, proved over an algebraically closed field by the identification with matrix algebras and in general by Galois descent. $\square$

## Units

**Definition.** Let $A$ be a unital associative $R$-algebra. An element $u \in A$ is a **unit** if there exists $v \in A$ with

$$
uv = vu = 1_A.
$$

The element $v$ is unique when it exists and is written $u^{-1}$; the units form a group $A^\times$ under multiplication, the **group of units** of $A$.

**Proposition.** The group of units is closed under multiplication and inversion, contains $1_A$, and every unit is neither a zero divisor nor a member of any proper two-sided ideal.

*Proof.* If $u,v$ are units then $(uv)(v^{-1}u^{-1}) = 1$ and $(v^{-1}u^{-1})(uv) = 1$, so $uv$ is a unit; $u^{-1}$ is a unit; $1_A$ is a unit. If $ux = 0$ then $x = u^{-1}ux = 0$, so a unit is not a zero divisor, and if $u$ lies in a two-sided ideal $I$ then $1 = u^{-1}u \in I$, whence $I = A$. $\square$

**Proposition (uniqueness of the inverse and cancellation).** In a unital associative algebra, if $uv = 1_A$ and $wu = 1_A$, then $v = w$; in particular, if $u$ has both a left inverse and a right inverse the two coincide and $u$ is a unit, and units cancel in products.

*Proof.* From $uv = 1$ and $wu = 1$, $w = w1 = w(uv) = (wu)v = 1v = v$. $\square$

**Remark (one-sided inverses).** The hypothesis that an inverse exists on both sides is not redundant. In the algebra $\operatorname{End}_F(V)$ of linear endomorphisms of a vector space with basis $e_0, e_1, e_2, \dots$, the shift $R(e_i) = e_{i+1}$ has the left inverse $L$ defined by $L(e_0) = 0$ and $L(e_{i+1}) = e_i$, so $LR = \mathrm{id}$, while $RL(e_0) = 0$ and $RL \neq \mathrm{id}$; thus $R$ has a one-sided inverse and is not a unit. Finite dimension removes the possibility, and it is precisely this that the division-algebra criterion below uses.

**Example (matrix units).** For a field $k$, $M_n(k)^\times = GL_n(k)$, the invertible matrices; an element of $M_n(k)$ is a unit if and only if its determinant is a unit of $k$, which over a field means nonzero. Over a general commutative ring $R$, an element of $M_n(R)$ is a unit if and only if its determinant is a unit of $R$, a strictly stronger condition than $\det \neq 0$.

**Example (the number systems).** The group of units of the small algebras is tabulated below, with the norm form that detects invertibility.

| Algebra | Unit criterion | Group of units |
|---|---|---|
| $\mathbb{R}$ | $a \neq 0$ | $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$ |
| $\mathbb{C}$ | $N(z) = a^2+b^2 \neq 0$ | $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ |
| $\mathbb{D}$ | $N(z) = a^2-b^2 \neq 0$ | four components, $\cong \mathbb{R}^\times \times \mathbb{R}^\times$ |
| $\mathbb{D}'$ | $a \neq 0$ | $\{a + b\varepsilon : a \neq 0\}$, an abelian group |
| $\mathbb{H}$ | $N(q) = q_0^2+q_1^2+q_2^2+q_3^2 \neq 0$ | $\mathbb{H}\setminus\{0\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $N(u)$ a unit of $\mathbb{D}$ | $\{u : N(u) \in \mathbb{D}^\times\}$ |
| $\mathbb{B}$ | $N(\tilde{Q}) = \sum_\mu Q_\mu^2 \neq 0$ | $\mathbb{B}^\times = \{\tilde{Q} : N(\tilde{Q}) \neq 0\}$ |

The criterion for the quaternionic cases is the standard one: in a quaternion algebra over a commutative ring $R$, an element $u$ is a unit if and only if its norm $N(u)$ is a unit of $R$, and then $u^{-1} = \bar{u}\,N(u)^{-1}$. The identity is verified directly:

$$
u \cdot \bar{u}\,N(u)^{-1} = N(u)\,N(u)^{-1} = 1, \qquad \bar{u}\,N(u)^{-1}\cdot u = N(u)^{-1}\,\bar{u}u = 1,
$$

using $u\bar{u} = \bar{u}u = N(u)$ and the centrality of $N(u) \in R$. For $\mathbb{D}'$ the norm form is $N(a + b\varepsilon) = a^2$, which is a unit of $\mathbb{R}$ exactly when $a \neq 0$; the inverse is $a^{-1} - b a^{-2}\varepsilon$.

## Zero Divisors

**Definition.** Let $A$ be an $R$-algebra. A nonzero element $z \in A$ is a **left zero divisor** if there exists $0 \neq w \in A$ with $zw = 0$, and a **right zero divisor** if there exists $0 \neq w$ with $wz = 0$. It is a **zero divisor** if it is a left or a right zero divisor. An algebra with no zero divisors is a **domain**, and a commutative unital associative algebra with no zero divisors is an **integral domain**.

In a commutative algebra the two notions coincide. A left zero divisor cannot be a unit, and by the proposition above a unit cannot be a zero divisor; the two classes are disjoint. They need not exhaust the algebra: in $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ the elements are $0$, the units $a + b\varepsilon$ with $a \neq 0$, and the zero divisors $b\varepsilon$ with $b \neq 0$, but in general there are elements that are neither — in $\mathbb{Z}$, the element $2$ is neither a unit nor a zero divisor.

**Proposition.** Let $A$ be a unital associative algebra and $z \in A$. The left annihilator

$$
\operatorname{Ann}_\ell(z) = \{w \in A : zw = 0\}
$$

is a right ideal, and it is nonzero if and only if $z$ is a left zero divisor. Dually, the right annihilator

$$
\operatorname{Ann}_r(z) = \{w \in A : wz = 0\}
$$

is a left ideal, and it is nonzero if and only if $z$ is a right zero divisor.

*Proof.* Both sets are submodules. If $w \in \operatorname{Ann}_\ell(z)$ and $a \in A$, then $z(wa) = (zw)a = 0$, so $wa \in \operatorname{Ann}_\ell(z)$: the left annihilator is closed under right multiplication, hence a right ideal. Dually, if $w \in \operatorname{Ann}_r(z)$ then $(aw)z = a(wz) = 0$, so the right annihilator is a left ideal. The nonvanishing statements restate the definitions. Note the sides are opposite: multiplication by $a$ must be applied on the side away from $z$. $\square$

Consequently $A/\operatorname{Ann}_r(z) \cong Az$ as left $A$-modules, by $a + \operatorname{Ann}_r(z) \mapsto az$; well-definedness is the statement that $a' - a \in \operatorname{Ann}_r(z)$ gives $(a'-a)z = 0$, and $A$-linearity is $(ba)z = b(az)$.

**Example (zero divisors in $\mathbb{D}$).** For $z = a + bj$ one has $N(z) = a^2 - b^2$, and

$$
(a + bj)(a - bj) = a^2 - b^2 = N(z).
$$

If $a = \pm b$ and $z \neq 0$ then $N(z) = 0$ and $z$ is a zero divisor. The two generators of the null cone are the idempotent-related elements $1 \pm j$:

$$
(1 + j)(1 - j) = 1 - j^2 = 0.
$$

Since every zero divisor of $\mathbb{D}$ has $a^2 = b^2$, the zero divisors of $\mathbb{D}$ are exactly the nonzero multiples of $1 + j$ and of $1 - j$, that is, the two lines $\mathbb{R}(1+j)$ and $\mathbb{R}(1-j)$. In the idempotent basis $e_\pm = \tfrac{1}{2}(1 \pm j)$ these are the ideals $\mathbb{D}e_\pm$.

**Example (zero divisors in $\mathbb{D}'$).** For $z = a + b\varepsilon$ one has $z \cdot b\varepsilon = ab\varepsilon$, so if $a \neq 0$ then $z$ is a unit, and if $a = 0$ and $b \neq 0$ then $z^2 = 0$ and $z$ is a zero divisor. The zero divisors of $\mathbb{D}'$ are exactly the nonzero elements of the maximal ideal $(\varepsilon) = \mathbb{R}\varepsilon$, which is a square-zero ideal.

**Example (zero divisors in $\mathbb{B}$).** For a biquaternion $\tilde{Q}$ the norm form $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ is multiplicative, and

$$
\tilde{Q}\bar{\tilde{Q}} = N(\tilde{Q}).
$$

Hence if $N(\tilde{Q}) = 0$ and $\tilde{Q} \neq 0$, then $\bar{\tilde{Q}} \neq 0$ and $\tilde{Q}$ is a zero divisor; and conversely, since $N(\tilde{Q}) \neq 0$ makes $\tilde{Q}$ a unit, every nonzero $\tilde{Q}$ with $N(\tilde{Q}) = 0$ is a zero divisor. The algebra $\mathbb{B}$ is thus partitioned into $\{0\}$, the units $N \neq 0$, and the zero divisors $N = 0$. The explicit pairs are exhibited .

**Example (zero divisors in $\mathbb{H}_{\mathbb{D}}$).** The split biquaternions contain the central split complex scalars, and the zero divisors of $\mathbb{D}$ are inherited: with $j$ central and $j^2 = +1$,

$$
(1 + j)(1 - j) = 0.
$$

Thus $\mathbb{H}_{\mathbb{D}}$ has zero divisors and is not a division algebra, even though its quaternion part $\mathbb{H}$ is one. The unit criterion $N(u) \in \mathbb{D}^\times$ shows again that the central element $u = 1+j$ fails to be a unit: its norm is $N(1+j) = (1+j)^2 = 2+2j$, and $N(2+2j) = 4-4 = 0$, so $2+2j$ is a zero divisor of $\mathbb{D}$ rather than a unit.

**Proposition (zero divisors and finite dimension).** Let $A$ be a finite-dimensional unital associative algebra over a field $F$. Then $A$ is a division algebra if and only if $A$ has no zero divisors.

*Proof.* A division algebra has no zero divisors by the proposition on units. Conversely, suppose $A$ has no zero divisors and let $0 \neq a \in A$. The left multiplication $\lambda_a : x \mapsto ax$ is $F$-linear and injective, since $ax = 0$ forces $x = 0$. As $A$ is finite-dimensional, $\lambda_a$ is surjective, so $ab = 1$ for some $b$; by uniqueness of inverses $a$ is a unit. Hence every nonzero element is a unit. $\square$

Finite dimension is used at the step where injectivity of $\lambda_a$ is converted into surjectivity, and it is finite dimension over a field that makes that step available. Over a general commutative ring the equivalence fails: the ring $\mathbb{Z}$, regarded as a $\mathbb{Z}$-algebra, has no zero divisors yet is not a division algebra, because $2$ has no inverse; the argument above would have to produce $b$ with $2b = 1$, which does not exist.

## The Regular Module and Division Algebras

**Definition.** Let $A$ be a unital associative $R$-algebra. The **regular left module** ${}_A A$ is the set $A$ with the left action $a \cdot x = ax$, and the **regular right module** $A_A$ is the set $A$ with the right action $x \cdot a = xa$. The submodules of ${}_A A$ are the left ideals of $A$, and the submodules of $A_A$ are the right ideals.

The algebra acts on itself, and this action is faithful: $a \cdot x = 0$ for all $x$ forces $a = a\,1 = 0$. The regular module is the simplest module over $A$, and every module is a quotient of a direct sum of copies of it.

**Theorem.** Let $A$ be a unital associative $R$-algebra. The following are equivalent:

1. $A$ is a division algebra, that is, every nonzero element of $A$ is a unit;
2. $A_A$ is a simple right $A$-module;
3. ${}_A A$ is a simple left $A$-module.

*Proof.* $(1) \Rightarrow (2)$: if $A$ is a division algebra and $M \subseteq A_A$ is a nonzero submodule, take $0 \neq m \in M$; then $m$ is a unit, so $A = mA \subseteq M$, whence $M = A$. $(2) \Rightarrow (1)$: if $A_A$ is simple and $0 \neq a \in A$, then $aA$ is a nonzero submodule, hence $aA = A$, so $ab = 1$ for some $b$; a ring in which every nonzero element has a right inverse is a division ring, as shown next. The equivalence with $(3)$ is symmetric. $\square$

For completeness, the standard argument alluded to: if every nonzero $a$ has a right inverse, choose $b$ with $ab = 1$; the element $b$ is nonzero and has a right inverse $c$ with $bc = 1$; then

$$
a = a\cdot 1 = a(bc) = (ab)c = 1\cdot c = c,
$$

so $ba = bc = 1$ and $b$ is a two-sided inverse of $a$.

**Corollary.** Let $A$ be a finite-dimensional unital associative algebra over a field $F$. Then $A$ is a division algebra if and only if $A_A$ is simple if and only if $A$ has no zero divisors.

Because $A_A$ is simple for a division algebra, a division algebra has no nonzero proper right ideal, and by the same argument no nonzero proper two-sided ideal: every division algebra is **simple**. The converse fails. The matrix algebra $M_n(k)$ over a field $k$ is simple, asshows, but $A_A$ is not simple as a module — its nonzero proper right ideals are the column-type subspaces — and $M_n(k)$ has zero divisors. Simplicity of the algebra and simplicity of the regular module are therefore genuinely different conditions; the second is the division condition.

**Example.** The division algebras among the standard examples are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ over their own ground fields, and their finite-dimensional extensions are not covered here. The algebras $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$, $M_n(k)$ for $n \geq 2$, $k[x]$ and $k[G]$ for $|G| \geq 2$ all have zero divisors or non-units and are not division algebras. Over $\mathbb{R}$ the finite-dimensional associative division algebras are exactly $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ (Frobenius), so no example beyond these three exists; over $\mathbb{C}$ the only one is $\mathbb{C}$ itself (Wedderburn). The proofs are given.

## Summary

The **centre** $Z(A) = C_A(A)$ is the set of elements commuting with everything; for an associative algebra it is a commutative subalgebra containing the unit, and it is preserved by every algebra automorphism. An algebra is **central** when $Z(A) = R\cdot 1$. The standard centres are $\mathbb{R}$ for $\mathbb{H}$, $\mathbb{D}$ for $\mathbb{H}_{\mathbb{D}}$, $\mathbb{C}$ for $\mathbb{B}$, and $k I_n$ for $M_n(k)$.

A **unit** is an element with a two-sided inverse, and the units form the group $A^\times$; a unit is neither a zero divisor nor a member of a proper ideal. A **zero divisor** is a nonzero element annihilating a nonzero element on one side, and the annihilator of an element is a one-sided ideal. In $\mathbb{D}$ the zero divisors are the nonzero multiples of $1 \pm j$; in $\mathbb{D}'$ they are the nonzero elements of the square-zero maximal ideal $(\varepsilon)$; in $\mathbb{B}$ they are exactly the nonzero elements with $N(\tilde{Q}) = 0$; in $\mathbb{H}_{\mathbb{D}}$ they include the inherited split complex ones, beginning with $1 \pm j$.

A unital associative algebra $A$ is a **division algebra** exactly when every nonzero element is a unit and exactly when the regular module $A_A$ is simple; over a field, a finite-dimensional such algebra is a division algebra exactly when it has no zero divisors. The division algebras among the standard examples are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$; the simple algebras $M_n(k)$ and $\mathbb{B}$ fail to be division algebras because the regular module is not simple and zero divisors exist.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $A$ | $R$-algebra, unital and associative where stated |
| $Z(A)$ | Centre of $A$ |
| $C_A(S)$ | Centralizer of $S$ in $A$ |
| $A^\times$ | Group of units of $A$ |
| $u^{-1}$ | Inverse of a unit $u$ |
| $\operatorname{Ann}_\ell(z)$, $\operatorname{Ann}_r(z)$ | Left and right annihilator of $z$ |
| $N$ | Norm form detecting units: $N(u) = u\bar u$ |
| $A_A$, ${}_A A$ | Regular right and left module |
| $\mathbb{R}, \mathbb{C}, \mathbb{H}$ | The finite-dimensional division algebras over $\mathbb{R}$ |
| $\mathbb{D}$ | Split complex numbers, zero divisors $\mathbb{R}(1\pm j)$ |
| $\mathbb{D}'$ | Dual numbers, zero divisors the maximal ideal $(\varepsilon)$ |
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternions, zero divisors inherited from $\mathbb{D}$ |
| $\mathbb{B}$ | Biquaternions, $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ |
| $M_n(k)$ | Matrix algebra, centre $k I_n$ |





## Further Reading

- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the centre, units and zero divisors in associative algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for annihilators, the regular module and division rings.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory and the division-algebra condition.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, MAA, 1968), for zero divisors and the regular representation.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the norm criterion for invertibility in quaternion algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for invertibility over a commutative coefficient ring.
