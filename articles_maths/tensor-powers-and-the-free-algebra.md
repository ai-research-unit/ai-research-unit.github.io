
# __Tensor Powers and the Free Algebra__

## Introduction

Every construction of a graded algebra from a module begins with the tensor powers of that module. This article builds the tensor powers $V^{\otimes n}$, assembles them into the tensor algebra $T(V) = \bigoplus_{n \geq 0} V^{\otimes n}$ with concatenation as product, and identifies $T(V)$ as the free associative algebra on $V$ by its universal property. The free algebra $R\langle X\rangle$ on a set $X$ is the tensor algebra of the free module on $X$, so it is a special case, and the two are treated together.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ and $V$ is an $R$-module. The tensor product of modules and its universal property are assumed from *Modules*, §13; the construction here is the iterated use of that product. The tensor product of two *algebras*, with its own product formula, is a different construction and is not covered here; this article uses only the tensor product of modules.

The tensor algebra is the source of the quotient presentations of the number systems and of the symmetric, exterior and Clifford algebras: all of these are quotients of $T(V)$ by ideals generated in low degree, and that construction is not covered here. What is fixed here is the free object, before any relation is imposed.

## Tensor Powers

**Definition.** Let $V$ be an $R$-module. The **tensor powers** of $V$ are the modules

$$
V^{\otimes 0} = R, \qquad V^{\otimes 1} = V, \qquad V^{\otimes n} = \underbrace{V \otimes_R \cdots \otimes_R V}_{n \text{ factors}}, \quad n \geq 2.
$$

The elements of $V^{\otimes n}$ are finite sums of **elementary tensors** $v_1 \otimes \cdots \otimes v_n$, and the product $\otimes$ is $R$-multilinear in the $n$ arguments.

**Universal property.** For every $R$-module $W$, the $R$-linear maps $V^{\otimes n} \to W$ correspond bijectively to the $R$-**multilinear** maps $V^n \to W$, the correspondence being $\tilde{f} \leftrightarrow f$ with

$$
f(v_1, \dots, v_n) = \tilde{f}(v_1 \otimes \cdots \otimes v_n).
$$

This is the universal property of the tensor product of two modules applied $n-1$ times, and it is the form in which $V^{\otimes n}$ is used.

**Associativity and commutativity of the tensor powers.** There are canonical isomorphisms

$$
V^{\otimes m} \otimes_R V^{\otimes n} \;\cong\; V^{\otimes (m+n)}, \qquad
V^{\otimes m} \otimes_R V^{\otimes n} \;\cong\; V^{\otimes n} \otimes_R V^{\otimes m},
$$

the first given by concatenation, $(v_1 \otimes \cdots \otimes v_m) \otimes (w_1 \otimes \cdots \otimes w_n) \mapsto v_1 \otimes \cdots \otimes v_m \otimes w_1 \otimes \cdots \otimes w_n$, extended $R$-linearly, and the second by the symmetry of the tensor product (*Modules*, §13). The first isomorphism is the reason the tensor algebra below is associative.

**Basis and dimension.** If $V$ is free with basis $\{e_i\}_{i \in I}$, then $V^{\otimes n}$ is free with basis the tensors

$$
e_{i_1} \otimes e_{i_2} \otimes \cdots \otimes e_{i_n}, \qquad i_1, \dots, i_n \in I,
$$

indexed by the functions $\{1,\dots,n\} \to I$. Hence, when $I$ is finite of cardinality $d$,

$$
\dim_R V^{\otimes n} = d^{\,n}.
$$

In particular, for a two-dimensional free module the tensor power has dimension $2^n$. Over a general commutative ring the rank is well defined by the invariant basis number property (*Modules*, §10), so this dimension is unambiguous.

**Functoriality.** An $R$-linear map $f : V \to W$ induces $f^{\otimes n} : V^{\otimes n} \to W^{\otimes n}$ by

$$
f^{\otimes n}(v_1 \otimes \cdots \otimes v_n) = f(v_1) \otimes \cdots \otimes f(v_n),
$$

well defined by the universal property. One has $(\mathrm{id}_V)^{\otimes n} = \mathrm{id}$ and $(g \circ f)^{\otimes n} = g^{\otimes n} \circ f^{\otimes n}$, so $V \mapsto V^{\otimes n}$ is a functor on $R$-modules.

**Example.** For $V = R$, every tensor power is $R$ itself, because $R \otimes_R R \cong R$; for $V = 0$ every positive tensor power is $0$, and $V^{\otimes 0} = R$ by convention. The convention $V^{\otimes 0} = R$ is what supplies the unit of the tensor algebra.

## The Tensor Algebra

**Definition.** The **tensor algebra** of the $R$-module $V$ is the direct sum of all its tensor powers,

$$
T(V) = \bigoplus_{n \geq 0} V^{\otimes n} = R \oplus V \oplus V^{\otimes 2} \oplus V^{\otimes 3} \oplus \cdots,
$$

equipped with the product defined on elementary tensors by concatenation,

$$
(v_1 \otimes \cdots \otimes v_m)\,(w_1 \otimes \cdots \otimes w_n) = v_1 \otimes \cdots \otimes v_m \otimes w_1 \otimes \cdots \otimes w_n,
$$

and extended to all of $T(V)$ by bilinearity.

The concatenation $\otimes$ of two elementary tensors is the image of their product under the canonical isomorphism $V^{\otimes m} \otimes_R V^{\otimes n} \cong V^{\otimes(m+n)}$; because that isomorphism is associative in the evident sense, the product is associative.

**Proposition.** $T(V)$ is an associative, unital $R$-algebra. Its unit is the element $1 \in V^{\otimes 0} = R$. Its elements are the finite sums $\sum_n t_n$ with $t_n \in V^{\otimes n}$, the **homogeneous components**, and they are unique.

*Proof.* Associativity follows from the associativity of concatenation of finite strings, unitality from $R \otimes_R V^{\otimes n} \cong V^{\otimes n} \cong V^{\otimes n} \otimes_R R$ with $1 \in R$ acting as the empty word, and bilinearity from the bilinearity of $\otimes$ together with the direct-sum decomposition. Uniqueness of homogeneous components is the definition of the direct sum. $\square$

The natural inclusion of the degree-one part is an injective $R$-linear map

$$
\iota: V \hookrightarrow T(V), \qquad \iota(v) = v \in V^{\otimes 1},
$$

and $T(V)$ is generated as an $R$-algebra by the image of $\iota$: every elementary tensor is a product $v_1 \cdots v_n$ of degree-one elements.

**Proposition (grading).** $T(V)$ is an $\mathbb{N}$-graded algebra:

$$
T(V) = \bigoplus_{n \geq 0} T^n(V), \qquad T^n(V) = V^{\otimes n}, \qquad T^m(V) \cdot T^n(V) \subseteq T^{m+n}(V).
$$

The grading is the decomposition into homogeneous components, and the $n$-th graded piece $T^n(V)$ is $V^{\otimes n}$.

*Proof.* The product of an elementary tensor of length $m$ and one of length $n$ is a tensor of length $m+n$, and both sides extend by bilinearity. $\square$

**Remark (commutativity).** If $V = Rv$ is generated by a single element, then $T(V)$ is commutative, because $V^{\otimes n}$ is spanned by $v^{\otimes n}$ and $v^m v^n = v^{m+n} = v^n v^m$. If instead $V$ contains two $R$-linearly independent elements $u$ and $v$, then $uv = u \otimes v$ and $vu = v \otimes u$ are distinct elements of $V^{\otimes 2}$, so $T(V)$ is not commutative; in particular $T(V)$ is non-commutative whenever $V$ is free of rank at least two. This is the algebraic expression of the fact that concatenation of words does not commute.

**Example (one generator).** For $V = R$ free of rank one on $x$, the $n$-th tensor power is free on $x^n$ and the product is $x^m \cdot x^n = x^{m+n}$; hence

$$
T(R) \cong R[x],
$$

the polynomial algebra in one variable. The variable $x$ is the image of the generator of $V$ under $\iota$. Since one variable generates a commutative algebra, this is the unique case in which the tensor algebra of a free module of positive rank is commutative.

**Example (several generators).** For a free module $V = R^n$ with basis $x_1, \dots, x_n$, the tensor algebra has basis the **words**

$$
x_{i_1} x_{i_2} \cdots x_{i_k}, \qquad k \geq 0, \quad i_j \in \{1,\dots,n\},
$$

including the empty word $1$, with the product given by juxtaposition. This is the algebra of **non-commutative polynomials** in $x_1, \dots, x_n$, written $R\langle x_1, \dots, x_n\rangle$ and treated in the next section. Its degree-$k$ part has rank $n^k$.

## The Universal Property

The tensor algebra is characterised, up to a unique isomorphism, by the following property.

**Theorem (universal property of $T(V)$).** Let $A$ be an associative unital $R$-algebra and let $\varphi : V \to A$ be an $R$-linear map. Then there is a unique unital $R$-algebra homomorphism $\tilde{\varphi} : T(V) \to A$ such that $\tilde{\varphi} \circ \iota = \varphi$, namely

$$
\tilde{\varphi}(v_1 \otimes \cdots \otimes v_n) = \varphi(v_1)\varphi(v_2)\cdots\varphi(v_n), \qquad \tilde{\varphi}(1) = 1_A.
$$

Equivalently, there is a natural bijection

$$
\operatorname{Hom}_{R\text{-alg}}(T(V), A) \;\cong\; \operatorname{Hom}_R(V, A), \qquad \tilde{\varphi} \longmapsto \tilde{\varphi} \circ \iota.
$$

*Proof.* The map $V^n \to A$, $(v_1, \dots, v_n) \mapsto \varphi(v_1)\cdots\varphi(v_n)$, is $R$-multilinear, since $\varphi$ is linear and the product of $A$ is bilinear. By the universal property of $V^{\otimes n}$ it induces a unique $R$-linear map $T^n(V) \to A$ with the stated values on elementary tensors. Taking the direct sum over $n$ and sending $1 \in V^{\otimes 0}$ to $1_A$ gives an $R$-linear map $\tilde{\varphi} : T(V) \to A$. It is multiplicative on elementary tensors, since concatenation on the left corresponds to product in $A$ on the right; both sides extend by bilinearity, so $\tilde{\varphi}$ is a unital algebra homomorphism. If $\psi$ is another such homomorphism, then $\psi$ and $\tilde{\varphi}$ agree on $V = T^1(V)$ and on $1$, hence on all products of these, hence on all of $T(V)$ by generation; so $\psi = \tilde{\varphi}$. $\square$

**Corollary (the free-forgetful adjunction).** Write $U$ for the forgetful functor from unital associative $R$-algebras to $R$-modules, sending an algebra to its underlying module. Then the tensor algebra functor $T$ is left adjoint to $U$:

$$
\operatorname{Hom}_{R\text{-alg}}(T(V), A) \;\cong\; \operatorname{Hom}_R(V, U(A))
$$

naturally in the $R$-module $V$ and the algebra $A$. In the notation of adjoint functors, $T \dashv U$.

*Proof.* The displayed bijection is the theorem, with $U(A) = A$ as a module; naturality is immediate from the definitions of the maps induced by a linear map $V \to V'$ and an algebra homomorphism $A \to A'$. $\square$

The adjunction says exactly that $T(V)$ is the **free algebra** on the module $V$: a linear map out of $V$ into any algebra extends uniquely to an algebra homomorphism out of $T(V)$. The universal property also identifies $T$ as a functor: a linear map $f : V \to W$ gives the algebra homomorphism $T(f) : T(V) \to T(W)$ extending $\iota_W \circ f$, and $T$ preserves composition and identities.

**Corollary (every algebra is a quotient of a tensor algebra).** Let $A$ be a unital associative $R$-algebra. Choose an $R$-module $V$ and a surjection $\varphi : V \to A$; for instance, take $V$ free on a generating set of $A$ with $\varphi$ sending each generator to the corresponding element. Then $\tilde{\varphi} : T(V) \to A$ is a surjective algebra homomorphism, so

$$
A \;\cong\; T(V)/\ker\tilde{\varphi}.
$$

This is the general form of a presentation of an algebra by generators and relations. Taking $V$ free on the generators produces the presentation $A \cong R\langle X\rangle/I$ used for $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{H}$ in *Ideals and Quotients of Algebras*, and the ideal $I$ is generated by the relations.

**Example (the augmentation).** For $V$ free of finite rank $d$ over a field, the composite $T(V) \to T^0(V) = R$ killing every positive-degree component is the **augmentation**, a unital algebra homomorphism; its kernel $T^+(V) = \bigoplus_{n \geq 1} V^{\otimes n}$ is the **augmentation ideal**, the two-sided ideal generated by $V$. Its square is $\bigoplus_{n \geq 2} V^{\otimes n}$.

## The Free Algebra

**Definition.** Let $X$ be a set and let $R^{(X)} = \bigoplus_{x \in X} R x$ be the free $R$-module on $X$. The **free algebra** on $X$ over $R$ is the tensor algebra

$$
R\langle X \rangle = T\bigl(R^{(X)}\bigr),
$$

with the elements of $X$ identified with their images in $T^1$. When $X = \{x_1, \dots, x_n\}$ is finite we write $R\langle x_1, \dots, x_n\rangle$.

An element of $R\langle X\rangle$ is a finite $R$-linear combination of **words** $x_{i_1} x_{i_2} \cdots x_{i_k}$ in the letters $X$, including the empty word $1$; the product is juxtaposition. It is a **non-commutative polynomial** in the letters.

**Theorem (universal property of the free algebra).** Let $A$ be an associative unital $R$-algebra and let $f : X \to A$ be any map. Then there is a unique unital $R$-algebra homomorphism $F : R\langle X\rangle \to A$ with $F(x) = f(x)$ for all $x \in X$.

*Proof.* The map $f$ extends uniquely to an $R$-linear map $R^{(X)} \to A$, since $X$ is a basis of $R^{(X)}$, and the universal property of $T$ extends that linear map to $R\langle X\rangle \to A$. $\square$

**Corollary.** The monomials $x_{i_1}\cdots x_{i_k}$, $k \geq 0$, form an $R$-basis of $R\langle X\rangle$, and the degree-$k$ part is free on the $|X|^k$ words of length $k$. Hence $R\langle X\rangle$ is a graded algebra with Hilbert series

$$
\sum_{k \geq 0} \dim_R R\langle X\rangle_k\, t^k = \sum_{k \geq 0} |X|^k t^k = \frac{1}{1 - |X|\,t}
$$

for finite $X$.

**Corollary.** $R\langle X\rangle$ is commutative if and only if $|X| \leq 1$. For $X = \{x\}$ it is $R[x]$.

**Example.** The quaternion algebra has the presentation

$$
\mathbb{H} = \mathbb{R}\langle x, y\rangle/(x^2+1,\; y^2+1,\; xy+yx),
$$

where the relations are those making $x$ and $y$ anticommute and square to $-1$; the images of $x, y$ correspond to $e_1, e_2$, and $xy$ to $e_3$. This is the quotient construction applied to the free algebra on two generators.

**Relation to the polynomial algebra.** The commutative polynomial algebra $R[x_1, \dots, x_n]$ is *not* the free algebra on $n$ letters; it is the free *commutative* algebra, and it is the quotient of $R\langle x_1,\dots,x_n\rangle$ by the two-sided ideal generated by the commutators $x_i x_j - x_j x_i$. Equivalently it is the symmetric algebra of $R^n$, a quotient of the tensor algebra treated in category 06 (symmetric algebras). The distinction between the free algebra and the free commutative algebra is exactly the distinction between imposing no relations and imposing commutativity.

## Grading, Functoriality and Change of Rings

**Graded ideals.** An ideal $I \subseteq T(V)$ is **homogeneous** (or **graded**) if it is the direct sum of its intersections $I \cap T^n(V)$. The quotient $T(V)/I$ by a homogeneous ideal inherits the grading, because the product of homogeneous classes is homogeneous. This is the mechanism by which the symmetric, exterior and Clifford algebras acquire their gradings, and it is developed.

**Functoriality.** The assignment $V \mapsto T(V)$ is a functor; more is true. For a direct sum,

$$
T(V \oplus W) \;\cong\; T(V) \sqcup T(W),
$$

where $\sqcup$ is the **free product** of algebras, the coproduct in the category of unital associative algebras. This is the algebra-level complement of the tensor product of algebras, which is the coproduct in the commutative case; both are treated. The identification follows from the universal property, since linear maps $V \oplus W \to A$ correspond to pairs of linear maps $V \to A$ and $W \to A$.

**Extension of scalars.** Let $R \to S$ be a homomorphism of commutative rings and let $V_S = V \otimes_R S$ be the base change of $V$ (*Modules*, §13). Then

$$
T(V_S) \;\cong\; T(V) \otimes_R S
$$

as $S$-algebras, because the tensor product commutes with direct sums and with itself over $R$: $(V^{\otimes n}) \otimes_R S \cong (V \otimes_R S)^{\otimes n}$ over $S$. In particular, complexifying the real free algebra on $n$ generators gives the complex free algebra on $n$ generators.

**Growth.** For $V$ free of rank $d \geq 1$, the degree-$n$ part of $T(V)$ has rank $d^n$; the total rank of $T(V)$ is infinite, and the rank grows exponentially in the degree when $d \geq 2$. This exponential growth is what makes the tensor algebra large enough to admit the many quotients.

## Summary

The **tensor powers** $V^{\otimes n}$ are the iterated tensor products of an $R$-module with itself, with $V^{\otimes 0} = R$; they are characterised by the universal property that linear maps out of $V^{\otimes n}$ are multilinear maps on $V^n$, and for a free module of rank $d$ the rank of $V^{\otimes n}$ is $d^n$. The **tensor algebra**

$$
T(V) = \bigoplus_{n \geq 0} V^{\otimes n}
$$

is the associative unital $R$-algebra with product given by concatenation of tensors and unit $1 \in V^{\otimes 0}$; it is $\mathbb{N}$-graded, generated by its degree-one part $V$, and non-commutative as soon as $V$ contains two independent elements. Its universal property is that every $R$-linear map $V \to A$ into a unital associative algebra extends uniquely to a unital algebra homomorphism $T(V) \to A$, which is the statement of the adjunction $T \dashv U$; consequently every such algebra is a quotient of a tensor algebra.

The **free algebra** $R\langle X\rangle$ is the tensor algebra of the free module on $X$; its elements are non-commutative polynomials, its degree-$k$ part is free on the $|X|^k$ words of length $k$, and it is commutative only when $|X| \leq 1$, the case $R\langle x\rangle = R[x]$. The tensor algebra of $R^n$ is the free algebra $R\langle x_1,\dots,x_n\rangle$, and the polynomial algebra is its commutative quotient. Homogeneous ideals give graded quotients, and extension of scalars commutes with $T$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $V$, $W$ | $R$-modules |
| $V^{\otimes n}$ | $n$-fold tensor power, $V^{\otimes 0} = R$, $V^{\otimes 1} = V$ |
| $v_1 \otimes \cdots \otimes v_n$ | Elementary tensor |
| $T(V) = \bigoplus_{n \geq 0} V^{\otimes n}$ | Tensor algebra of $V$ |
| $T^n(V) = V^{\otimes n}$ | $n$-th graded piece |
| $T^+(V) = \bigoplus_{n \geq 1} V^{\otimes n}$ | Augmentation ideal |
| $\iota : V \hookrightarrow T(V)$ | Inclusion of the degree-one part |
| $\tilde{\varphi} : T(V) \to A$ | Algebra homomorphism extending $\varphi : V \to A$ |
| $T \dashv U$ | Tensor algebra left adjoint to the forgetful functor |
| $R\langle X\rangle$ | Free algebra on the set $X$ |
| $R\langle x_1,\dots,x_n\rangle$ | Free algebra on $n$ generators |
| $\sqcup$ | Free product of algebras |
| $d = \dim_R V$ | Rank of a free module; $\dim_R V^{\otimes n} = d^n$ |
| $\mathbb{H} = \mathbb{R}\langle x,y\rangle/(x^2+1, y^2+1, xy+yx)$ | Quaternion algebra as a quotient |







## Further Reading

- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for tensor powers, the tensor algebra and the free algebra.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009), for the universal property and the free associative algebra.
- Paul M. Cohn, *Free Rings and Their Relations* (Academic Press, 2nd ed. 1985), for the free algebra and its structure.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for free algebras and their quotients.
- Saunders Mac Lane, *Categories for the Working Mathematician* (Springer, 2nd ed. 1998), for the free-forgetful adjunction.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the multilinear and tensor constructions in full generality.
