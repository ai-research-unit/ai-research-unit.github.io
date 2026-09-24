
# __Exterior Powers__

## Introduction

The tensor powers $M^{\otimes n}$ introduced in *Modules* are the universal recipients of $n$-multilinear maps. Every $n$-multilinear map on a module $M$ factors uniquely through $M^{\otimes n}$, and the tensor algebra $T(M) = \bigoplus_{n \geq 0} M^{\otimes n}$ records all of them at once. **Alternating** maps are the special multilinear maps that change sign when two arguments are exchanged, and they have their own universal recipient, the **exterior power** $\Lambda^n M$. Passing from $M^{\otimes n}$ to $\Lambda^n M$ is the operation of imposing the relation $x \otimes x = 0$; the graded pieces obtained this way are the subject of this article, and the graded algebra they assemble into is treated .

The exterior powers are the antisymmetric counterpart of the symmetric powers, and the exterior algebra is the antisymmetric counterpart of the symmetric algebra: the symmetric theory belongs to the category on symmetric algebras, the tensor algebra itself to the category on algebras, and only the alternating case is treated here. The three companion articlesandcontinue the thread, beginning with the wedge product on the pieces constructed below.

Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$ and $M$, $N$ are $R$-modules; over a commutative ring left and right modules coincide, so no side is specified. The field is written $K$, and $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ when only those two are meant. The corpus default base is the commutative ring, so the construction is carried out over $R$, and every point where a field, a characteristic assumption, or the invertibility of $2$ is required is flagged. No physics is invoked: an alternating form here is a function of module elements, never of a physical field.

## Alternating Multilinear Maps

### Multilinear Maps

**Definition.** Let $n \geq 1$. A map $f : M^n \to N$ is **$n$-multilinear** if it is $R$-linear in each argument separately, that is, for every $i$ and all $x, y \in M$ and $r \in R$,

$$
f(\ldots, x + y, \ldots) = f(\ldots, x, \ldots) + f(\ldots, y, \ldots), \qquad f(\ldots, r x, \ldots) = r\, f(\ldots, x, \ldots),
$$

with the remaining arguments held fixed. A $1$-multilinear map is an $R$-linear map and a $2$-multilinear map is the bilinear map of *Modules*. The set of $n$-multilinear maps $M^n \to N$ is an $R$-module under pointwise operations, written $\operatorname{Mult}_n(M; N)$.

The tensor power represents this functor: the canonical map

$$
\otimes : M^n \to M^{\otimes n}, \qquad (x_1, \ldots, x_n) \mapsto x_1 \otimes \cdots \otimes x_n
$$

is $n$-multilinear, and every $n$-multilinear $f$ factors uniquely as $f = \bar{f} \circ \otimes$ with $\bar{f} : M^{\otimes n} \to N$ linear. Equivalently,

$$
\operatorname{Mult}_n(M; N) \cong \operatorname{Hom}_R(M^{\otimes n}, N).
$$

### Alternating Maps

**Definition.** An $n$-multilinear map $f : M^n \to N$ is **alternating** if

$$
f(x_1, \ldots, x_n) = 0
$$

whenever $x_i = x_j$ for some pair of distinct indices $i \neq j$.

Because $f$ is multilinear, it is enough to test adjacent pairs: if $f$ vanishes whenever two adjacent arguments are equal, then it vanishes whenever any two are equal. Indeed, by the computation below, adjacent vanishing forces $f$ to change sign under an adjacent transposition; a sequence of adjacent transpositions brings any equal pair into adjacent positions, and each transposition at worst changes the sign of a value already known to be zero.

**Proposition (sign lemma).** Let $f$ be alternating and let $\sigma$ be a permutation of $\{1, \ldots, n\}$ with sign $\operatorname{sgn}(\sigma) \in \{\pm 1\}$. Then

$$
f(x_{\sigma(1)}, \ldots, x_{\sigma(n)}) = \operatorname{sgn}(\sigma)\, f(x_1, \ldots, x_n).
$$

**Proof.** It suffices to prove the claim for an adjacent transposition $\tau$ exchanging $i$ and $i+1$, since every permutation is a product of these and $\operatorname{sgn}$ is multiplicative. For fixed arguments other than the $i$-th and $(i+1)$-st, put $g(u, v) = f(\ldots, u, v, \ldots)$. Then $g$ is bilinear and $g(w, w) = 0$ for all $w$, so

$$
0 = g(u + v, u + v) = g(u, u) + g(u, v) + g(v, u) + g(v, v) = g(u, v) + g(v, u),
$$

giving $g(u, v) = -g(v, u)$. Hence $f$ changes sign when two adjacent arguments are exchanged, and the general statement follows. $\square$

**Corollary.** An alternating map satisfies $f(x_1, \ldots, x_n) = 0$ whenever two of the arguments are equal.

**Remark (the sign convention).** The sign of a permutation is the unique homomorphism $\operatorname{sgn} : S_n \to \{\pm 1\}$ sending each transposition to $-1$. It can be computed as $\operatorname{sgn}(\sigma) = (-1)^{N(\sigma)}$, where $N(\sigma)$ is the number of inversions, the number of pairs $i < j$ with $\sigma(i) > \sigma(j)$.

### Alternating and Skew-Symmetric Maps

There is a second, formally weaker, symmetry condition on a multilinear map.

**Definition.** An $n$-multilinear map $f : M^n \to N$ is **skew-symmetric** if exchanging any two arguments changes the sign:

$$
f(\ldots, x_i, \ldots, x_j, \ldots) = -f(\ldots, x_j, \ldots, x_i, \ldots).
$$

The two notions are not the same over an arbitrary commutative ring.

**Proposition.** Every alternating map is skew-symmetric. Conversely, every skew-symmetric map is alternating when $2$ is not a zero divisor in $R$.

**Proof.** The first claim is the sign lemma applied to a transposition. For the second, take a skew-symmetric $f$ and set two arguments equal, say $x_i = x_j$; the skew-symmetry gives $f = -f$, that is $2 f = 0$. If $2$ is not a zero divisor, then $f = 0$, so $f$ is alternating. $\square$

**Example.** Over $R = \mathbb{F}_2$ the element $-1$ equals $1$, so the skew-symmetry condition is $f = f$ and is satisfied automatically by every multilinear map, while the alternating condition $f(x, x) = 0$ is a genuine restriction. For instance the bilinear form $f(x, y) = x_1 y_1$ on $\mathbb{F}_2^2$ is skew-symmetric but not alternating, since $f(e_1, e_1) = 1 \neq 0$. This is why the exterior power is built from alternation, not from skew-symmetry: alternation is the condition available over every commutative ring, and it specialises to skew-symmetry once $2$ is invertible.

## The Exterior Power

### Construction as a Quotient

**Definition.** Let $n \geq 1$ and let $D_n \subseteq M^{\otimes n}$ be the submodule generated by all elementary tensors $x_1 \otimes \cdots \otimes x_n$ in which two adjacent entries are equal, that is,

$$
D_n = \operatorname{span}_R\{ x_1 \otimes \cdots \otimes x_n : x_i = x_{i+1} \ \text{for some } i \}.
$$

The **$n$-th exterior power** of $M$ is the quotient

$$
\Lambda^n M = M^{\otimes n} / D_n.
$$

The class of $x_1 \otimes \cdots \otimes x_n$ is written $x_1 \wedge \cdots \wedge x_n$, and an element of this form is called an **elementary wedge** or a **decomposable $n$-vector**. For $n = 0$ one sets $\Lambda^0 M = R$.

The canonical map

$$
\wedge : M^n \to \Lambda^n M, \qquad (x_1, \ldots, x_n) \mapsto x_1 \wedge \cdots \wedge x_n
$$

is $n$-multilinear, because $\otimes$ is and the quotient map is linear, and it is alternating, because each generator of $D_n$ is killed. The construction is the alternating analogue of the definition of the tensor power as a quotient of the free module on $M^n$: here one starts from $M^{\otimes n}$ and imposes the relations that force alternation.

### The Universal Property

**Theorem (universal property of the exterior power).** For every $R$-module $N$ and every alternating $n$-multilinear map $f : M^n \to N$, there is a unique $R$-linear map $\bar{f} : \Lambda^n M \to N$ with

$$
f(x_1, \ldots, x_n) = \bar{f}(x_1 \wedge \cdots \wedge x_n)
$$

for all $x_1, \ldots, x_n \in M$. Consequently the assignment $\bar{f} \mapsto \bar{f} \circ \wedge$ is an isomorphism

$$
\operatorname{Hom}_R(\Lambda^n M, N) \cong \operatorname{Alt}_n(M; N),
$$

where $\operatorname{Alt}_n(M; N)$ denotes the submodule of $\operatorname{Mult}_n(M; N)$ consisting of the alternating maps. The pair $(\Lambda^n M, \wedge)$ is determined up to unique isomorphism by this property.

**Proof.** Since $f$ is $n$-multilinear, it factors uniquely through the tensor power as $f = g \circ \otimes$ with $g : M^{\otimes n} \to N$ linear. Because $f$ is alternating, $g$ kills every elementary tensor with two adjacent entries equal, hence kills the submodule $D_n$ they generate. Therefore $g$ descends to a unique linear map $\bar{f}$ on the quotient $\Lambda^n M$, and $f = \bar{f} \circ \wedge$ by construction. Uniqueness is immediate on the elementary wedges, which generate $\Lambda^n M$. $\square$

**Remark.** The theorem is the exact sense in which $\Lambda^n M$ is the universal module through which alternating maps factor. Setting $N = \Lambda^n M$ recovers the identity of $\Lambda^n M$ from the alternating map $\wedge$, and setting $N = R$ identifies the alternating forms of degree $n$ on $M$ with the linear functionals on $\Lambda^n M$; this is taken up in the final section.

### Elementary Properties

**Proposition.** Let $M$ be an $R$-module and let $n \geq 1$. 

**(a)** $\Lambda^0 M = R$ and $\Lambda^1 M = M$.

**(b)** For all $x \in M$ one has $x \wedge x = 0$ in $\Lambda^2 M$; more generally, any elementary wedge with two equal entries is zero.

**(c)** $y \wedge x = -x \wedge y$ in $\Lambda^2 M$ for all $x, y \in M$.

**(d)** $\Lambda^n M$ is generated as an $R$-module by the elementary wedges.

**(e)** If $M$ is generated by $m$ elements, then $\Lambda^n M = 0$ for $n > m$.

**Proof.** (a) is the definition for $n = 0$; for $n = 1$ the submodule $D_1$ is generated by tensors with two adjacent entries equal, and there is no such pair, so $D_1 = 0$ and $\Lambda^1 M = M^{\otimes 1} = M$.

(b) The element $x \wedge x$ is the image of $x \otimes x \in D_2$, hence is zero; the general statement follows by bringing the equal entries into adjacent positions, using the sign relation of (c).

(c) The tensor $(x + y) \otimes (x + y)$ lies in $D_2$, so its image in $\Lambda^2 M$ is zero. Expanding, $x \wedge x + x \wedge y + y \wedge x + y \wedge y = 0$, and the first and last terms vanish by (b), leaving $x \wedge y + y \wedge x = 0$.

(d) The tensor power $M^{\otimes n}$ is generated by elementary tensors, and $\Lambda^n M$ is their image under the quotient map.

(e) If $M$ is generated by $x_1, \ldots, x_m$, then every elementary wedge $y_1 \wedge \cdots \wedge y_n$ with $n > m$ involves $n$ elements of a generating set of size $m$, so by multilinearity it is a sum of wedges in which some generator is repeated; such a wedge is zero by (b). $\square$

## Basis, Rank and Functoriality

### Free Modules and the Binomial Basis

The exterior powers of a free module are again free, with an explicit basis indexed by subsets.

**Theorem.** Let $M$ be a free $R$-module with basis $(e_i)_{i \in I}$, and suppose the index set is finite of cardinality $m$. Then $\Lambda^n M$ is free with basis

$$
\{ e_{i_1} \wedge e_{i_2} \wedge \cdots \wedge e_{i_n} : i_1 < i_2 < \cdots < i_n \},
$$

so its rank is the binomial coefficient $\binom{m}{n}$. In particular $\Lambda^n M = 0$ for $n > m$, and $\Lambda^m M$ is free of rank $1$.

**Proof.** Every elementary wedge is a linear combination of the displayed ones by multilinearity and the sign relation, and the displayed wedges generate. To see that they are independent, fix an increasing $n$-tuple $J = (j_1 < \cdots < j_n)$ and define an alternating $n$-multilinear map $f_J : M^n \to R$ by

$$
f_J(x_1, \ldots, x_n) = \det\bigl(e^{j_p}(x_q)\bigr)_{p,q=1}^{n},
$$

where $(e^i)$ is the dual basis of $M^*$ and the determinant is the Leibniz expansion

$$
\det(a_{pq}) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{p=1}^{n} a_{p,\sigma(p)}.
$$

This is a polynomial in the coefficients, hence defined over any commutative ring, and it is alternating because the determinant changes sign under a column exchange and vanishes when two columns agree. By the universal property it gives a linear functional $\bar{f}_J$ on $\Lambda^n M$ with $\bar{f}_J(e_{i_1} \wedge \cdots \wedge e_{i_n}) = 1$ when $(i_1, \ldots, i_n) = J$ and $= 0$ when the tuple is increasing and different from $J$. A linear relation $\sum_J c_J e_J = 0$ among the basis candidates therefore gives $c_J = \bar{f}_J(\sum_J c_J e_J) = 0$ for every $J$. Hence the displayed wedges are independent. $\square$

The determinant used in the proof is developed for its own sake ; here it is only the explicit alternating form that separates the basis elements.

**Corollary.** Let $V$ be a vector space over a field of dimension $m$. Then $\dim \Lambda^n V = \binom{m}{n}$ for $0 \leq n \leq m$, and $\Lambda^n V = 0$ for $n > m$. In particular $\dim \Lambda^n V = \dim \Lambda^{m-n} V$.

**Example.** For $M = R^3$ with basis $e_1, e_2, e_3$, the exterior powers are

$$
\Lambda^0 M = R, \quad \Lambda^1 M = \langle e_1, e_2, e_3 \rangle, \quad \Lambda^2 M = \langle e_1 \wedge e_2, e_1 \wedge e_3, e_2 \wedge e_3 \rangle, \quad \Lambda^3 M = \langle e_1 \wedge e_2 \wedge e_3 \rangle,
$$

of ranks $1, 3, 3, 1$. The symmetry of the ranks is the numerical shadow of the pairing $\Lambda^n V \times \Lambda^{m-n} V \to \Lambda^m V$ discussed below.

### Induced Maps

**Definition.** Let $f : M \to N$ be an $R$-linear map. For each $n \geq 0$ the **$n$-th exterior power of $f$** is the linear map

$$
\Lambda^n f : \Lambda^n M \to \Lambda^n N, \qquad x_1 \wedge \cdots \wedge x_n \mapsto f(x_1) \wedge \cdots \wedge f(x_n),
$$

which exists by the universal property applied to the alternating map $(x_1, \ldots, x_n) \mapsto f(x_1) \wedge \cdots \wedge f(x_n)$.

**Proposition.** The exterior powers are functorial: $\Lambda^n(\mathrm{id}_M) = \mathrm{id}_{\Lambda^n M}$ and

$$
\Lambda^n(g \circ f) = \Lambda^n g \circ \Lambda^n f
$$

for composable linear maps $f : M \to N$ and $g : N \to P$. Hence $M \mapsto \Lambda^n M$, $f \mapsto \Lambda^n f$ is a functor from $R$-modules to $R$-modules. On the top power of a free module of rank $n$, the map $\Lambda^n f$ is multiplication by the determinant of $f$.

**Proof.** Both statements are checked on elementary wedges, which generate; associativity of composition of maps then gives the second. The assertion about the top power is the definition of the determinant given in the companion article. $\square$

### Direct Sums and Base Change

**Theorem.** For all $R$-modules $M, N$ and all $n \geq 0$ there is a natural isomorphism

$$
\Lambda^n(M \oplus N) \cong \bigoplus_{p + q = n} \Lambda^p M \otimes_R \Lambda^q N,
$$

the map from the right to the left being $(u, v) \mapsto u \wedge v$ on each summand.

**Proof.** The map sending $(m, n) \in M \oplus N$ to $m \otimes 1 + 1 \otimes n$ in the graded tensor product $\Lambda(M) \hat{\otimes} \Lambda(N)$ is a linear map out of $M \oplus N$ whose image anticommutes, so it extends to a homomorphism of graded algebras $\Lambda(M \oplus N) \to \Lambda(M) \hat{\otimes} \Lambda(N)$. In degree $n$ this is the displayed map. Both sides are generated in each degree by elementary terms, and the relation $(m_1 + n_1) \wedge \cdots (m_n + n_n)$, expanded by multilinearity, expresses every wedge in $M \oplus N$ through wedges in $M$ and $N$; counting ranks over a free module, where both sides are free of rank $\binom{m + r}{n} = \sum_{p+q=n} \binom{m}{p}\binom{r}{q}$ by Vandermonde's identity, shows that the map is an isomorphism there. For general modules the natural transformation obtained is an isomorphism because both sides are right exact functors of $M$ and of $N$ — the power $\Lambda^n$ by the right-exactness proposition above, and the sum of tensor products because tensor product and direct sum are right exact — and a natural transformation between right exact functors that is an isomorphism on free modules is an isomorphism. $\square$

**Proposition (base change).** Let $R \to S$ be a ring homomorphism and let $M$ be an $R$-module. Then there is a natural isomorphism of $S$-modules

$$
\Lambda^n(M \otimes_R S) \cong \Lambda^n M \otimes_R S.
$$

**Proof.** Both sides represent the same functor: an $S$-linear map $\Lambda^n M \otimes_R S \to P$ corresponds, by the tensor–hom adjunction, to an $R$-linear map $\Lambda^n M \to P$, equivalently to an alternating $R$-multilinear map $M^n \to P$, equivalently to an alternating $S$-multilinear map $(M \otimes_R S)^n \to P$. $\square$

### Right Exactness

**Proposition.** The functor $\Lambda^n$ preserves surjections: if $f : M \to N$ is surjective, so is $\Lambda^n f$. More generally $\Lambda^n$ is right exact.

**Proof.** Write $\Lambda^n M$ as the quotient of $M^{\otimes n}$ by $D_n$ and observe that the tensor power functor is right exact. A surjection $f$ induces a surjection $M^{\otimes n} \to N^{\otimes n}$, and the image of $D_n(M)$ under $f^{\otimes n}$ lies in $D_n(N)$; hence the induced map of quotients $\Lambda^n M \to \Lambda^n N$ is surjective. The stronger statement that $\Lambda^n$ preserves arbitrary cokernels is the standard right exactness of exterior powers, proved by the same reduction to the tensor power together with the identification of $D_n(N)$ with the image of $D_n(M)$. $\square$

## The Top Power and Alternating Forms

**Definition.** An **alternating form of degree $n$** on $M$ with values in $R$ is an element of

$$
\operatorname{Alt}^n(M; R) = \operatorname{Alt}_n(M; R),
$$

the module of alternating $n$-multilinear maps $M^n \to R$. By the universal property,

$$
\operatorname{Alt}^n(M; R) \cong \operatorname{Hom}_R(\Lambda^n M, R) = (\Lambda^n M)^*.
$$

Thus the alternating forms of degree $n$ are exactly the linear functionals on the $n$-th exterior power, and the pairings between forms of complementary degrees are the linear functionals on the exterior powers.

**Proposition.** Let $M$ be free of finite rank $m$. Then for each $n$ there is a natural isomorphism $\Lambda^n(M^*) \cong (\Lambda^n M)^*$, so an alternating form of degree $n$ may be regarded as an element of $\Lambda^n(M^*)$.

This identification is the point of departure for the calculus of differential forms: at a point of a smooth manifold the cotangent space plays the role of $M^*$, and a differential $k$-form is a smoothly varying element of $\Lambda^k$ of it. That is the subject of with this one.

**Definition.** Let $M$ be free of rank $m$. The **top exterior power** is $\Lambda^m M$, a free module of rank $1$, called the **determinant line** of $M$. For an endomorphism $f$ of $M$ the scalar by which $\Lambda^m f$ acts on $\Lambda^m M$ is the **determinant** $\det f$; for a basis $(e_1, \ldots, e_m)$ one has

$$
\Lambda^m f(e_1 \wedge \cdots \wedge e_m) = \det(f)\, e_1 \wedge \cdots \wedge e_m.
$$

The determinant, its multiplicativity, and the minors of $\Lambda^n f$ are the content .

## Summary

An $n$-multilinear map $f : M^n \to N$ is alternating if it vanishes whenever two arguments are equal. Alternation implies skew-symmetry over any commutative ring, and the converse holds exactly when $2$ is not a zero divisor; the exterior power is built from alternation so that the construction is available over every $R$. The $n$-th exterior power is the quotient $\Lambda^n M = M^{\otimes n}/D_n$, where $D_n$ is generated by elementary tensors with two adjacent equal entries, and its universal property is

$$
\operatorname{Hom}_R(\Lambda^n M, N) \cong \operatorname{Alt}_n(M; N).
$$

The elementary wedges generate $\Lambda^n M$; the relations $x \wedge x = 0$ and $y \wedge x = -x \wedge y$ hold; and if $M$ is generated by $m$ elements then $\Lambda^n M = 0$ for $n > m$. When $M$ is free of rank $m$, the exterior power is free with basis the increasing wedges $e_{i_1} \wedge \cdots \wedge e_{i_n}$, of rank $\binom{m}{n}$.

Exterior powers are functorial, so each linear $f$ induces $\Lambda^n f$; they carry direct sums to sums of tensor products, $\Lambda^n(M \oplus N) \cong \bigoplus_{p+q=n} \Lambda^p M \otimes \Lambda^q N$; they commute with base change; and they are right exact. The alternating forms of degree $n$ are the linear functionals on $\Lambda^n M$, and the top power $\Lambda^m M$ of a free module of rank $m$, the determinant line, carries the determinant of an endomorphism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$; the default base |
| $K$ | Field |
| $M$, $N$ | $R$-modules (left, over a commutative ring) |
| $M^{\otimes n}$ | $n$-th tensor power of $M$ |
| $T(M) = \bigoplus_{n \geq 0} M^{\otimes n}$ | Tensor algebra of $M$ |
| $\operatorname{Mult}_n(M; N)$ | $R$-module of $n$-multilinear maps $M^n \to N$ |
| $\operatorname{Alt}_n(M; N)$ | Submodule of alternating $n$-multilinear maps |
| $\operatorname{sgn}(\sigma)$ | Sign of a permutation, $(-1)^{N(\sigma)}$ with $N(\sigma)$ the inversion number |
| $D_n$ | Submodule of $M^{\otimes n}$ generated by elementary tensors with two adjacent equal entries |
| $\Lambda^n M = M^{\otimes n}/D_n$ | $n$-th exterior power of $M$ |
| $x_1 \wedge \cdots \wedge x_n$ | Class of $x_1 \otimes \cdots \otimes x_n$; elementary wedge |
| $\wedge : M^n \to \Lambda^n M$ | Canonical alternating $n$-multilinear map |
| $\Lambda^0 M = R$, $\Lambda^1 M = M$ | Exterior powers in degrees $0$ and $1$ |
| $\Lambda^n f$ | Induced map, $x_1 \wedge \cdots \wedge x_n \mapsto f(x_1) \wedge \cdots \wedge f(x_n)$ |
| $\operatorname{Alt}^n(M; R) \cong (\Lambda^n M)^*$ | Alternating forms of degree $n$ |
| $\Lambda^m M$ | Top exterior power, the determinant line, when $M$ is free of rank $m$ |
| $\det f$ | Scalar by which $\Lambda^m f$ acts on the determinant line |
| $\binom{m}{n}$ | Rank of $\Lambda^n M$ for $M$ free of rank $m$ |



## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the exterior powers over a commutative ring and their universal property.
- Werner Greub, *Multilinear Algebra* (Springer, 2nd ed. 1978), for alternating multilinear maps and the construction of the exterior product.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the exterior algebra and its functorial properties.
- D. G. Northcott, *Multilinear Algebra* (Cambridge University Press, 1984), for the exterior powers over general rings and the binomial basis.
- Saunders Mac Lane and Garrett Birkhoff, *Algebra* (AMS Chelsea, 3rd ed. 1999), for the quotient construction and the relation to tensor powers.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for exterior powers of representations and the top power.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the exactness properties of the exterior power functors.
