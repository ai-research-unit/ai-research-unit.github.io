
# __Associative Algebras__

## Introduction

This article studies the first of the two axioms that the corpus adds to the broad sense of an algebra. An $R$-algebra in the sense fixed in *Algebras* is an $R$-module with a bilinear product and no further hypothesis; this article adds **associativity**, $(xy)z = x(yz)$, and states what that single axiom buys. The other axiom the corpus adds, the existence of an identity, is the subject of *Unital Algebras*, the next article of this category, and the two are independent: an associative algebra need not be unital, and a unital algebra need not be associative. The identities weaker than associativity are the rungs developed in *Non-Associative Algebras and the Property Ladder*, later in the same category.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ and $A$ is an $R$-algebra in the broad sense, unless a sentence names a stronger hypothesis. Associativity is the only hypothesis added: $A$ is not assumed commutative and not assumed unital. The article is algebraic throughout and uses no distance, no norm and no limit.

The constructions that other articles own are cited and not repeated. The tensor algebra $T(M)$ and its universal property belong to *Tensor Powers and the Free Algebra*; the formalism of ideals and quotients to *Ideals and Quotients of Algebras*; the linearisation of the identities below associativity to *Non-Associative Algebras and the Property Ladder*; the unit group and the regular module to *Centre, Units, Zero Divisors and Division Algebras*; the matrix algebra to *Matrix Algebras*; the Lie algebra to *Lie Algebras*; and the enveloping algebra, its filtration and the Poincaré–Birkhoff–Witt theorem to *Universal Enveloping Algebras*. The relevant module theory is that of *Modules*.

## Associativity and the Associator

**Definition.** Let $A$ be an $R$-algebra. The product is **associative** if

$$
(xy)z = x(yz)
$$

for all $x, y, z \in A$, and $A$ is then an **associative algebra**. Associativity is a **polynomial identity**: it is the assertion that the polynomial $(xy)z - x(yz)$, with coefficients in $R$ and with the non-commuting indeterminates $x, y, z$, vanishes for every substitution of elements of $A$.

**Definition.** The **associator** of $x, y, z \in A$ is

$$
[x,y,z] = (xy)z - x(yz).
$$

The associator is the trilinear map that measures the failure of associativity, and it is the object in which the identities below associativity are written in *Non-Associative Algebras and the Property Ladder*; with it, associativity is the statement that the associator vanishes identically.

**Proposition.** The associator is an $R$-trilinear map $A \times A \times A \to A$.

*Proof.* The product is bilinear, so adding in one argument distributes:

$$
[x + x', y, z] = ((x+x')y)z - (x+x')(yz) = [x,y,z] + [x',y,z],
$$

and the same computation applies in the second and third arguments. For $r \in R$,

$$
[rx, y, z] = ((rx)y)z - (rx)(yz) = r\bigl((xy)z - x(yz)\bigr) = r\,[x,y,z],
$$

by the scalar compatibility of the product, and again in the other two arguments. $\square$

**Theorem.** An $R$-algebra $A$ is associative if and only if $[x,y,z] = 0$ for all $x, y, z \in A$.

*Proof.* The identity $(xy)z = x(yz)$ is equivalent to $(xy)z - x(yz) = 0$, which is $[x,y,z] = 0$, for every triple. $\square$

**Corollary (associativity is a linear condition).** The algebra $A$ is associative if and only if the associator vanishes on every triple drawn from a spanning set of the $R$-module $A$. In particular, if $A$ is a free $R$-module with basis $(e_i)_{i \in I}$, it is enough to check $[e_i, e_j, e_k] = 0$ for all $i, j, k \in I$.

*Proof.* Writing $x = \sum_i r_i e_i$ and similarly for $y$ and $z$, with finite sums, trilinearity gives

$$
[x,y,z] = \sum_{i,j,k} r_i s_j t_k\, [e_i, e_j, e_k],
$$

so the associator vanishes on all triples as soon as it vanishes on the spanning triples. $\square$

Associativity is therefore not a condition of a different kind from bilinearity: it is one more multilinear identity, and it is verified on a spanning set. This is the reason the corpus can prescribe an algebra by a multiplication table.

**Proposition (inheritance).** Associativity is inherited by subalgebras, by quotient algebras and by homomorphic images, and is preserved by direct sums and by tensor products of algebras.

*Proof.* Each is an identity between products, and an identity is preserved by passage to a submodule closed under the product, by passage to a quotient, and by the componentwise or tensor product formulas of *Algebras*; the tensor product of algebras is treated in *Tensor Products of Algebras*. $\square$

## Linearisation and Power-Associativity

Associativity is the strongest identity of the ladder, and every weaker identity on it is a consequence of associativity. This section records the consequence that outlives associativity in the study of the corpus's non-associative objects, and shows that it does not characterise associativity.

**Definition.** For $x \in A$ the **powers** of $x$ are $x^1 = x$ and $x^{n+1} = x^n x$ for $n \geq 1$. The algebra $A$ is **power-associative** if the subalgebra generated by any single element is associative, equivalently if $x^p x^q = x^{p+q}$ for all $p, q \geq 1$ and all $x$.

The definition is that of *Non-Associative Algebras and the Property Ladder*, where it is listed after flexibility and before the Moufang identities, and where flexibility and power-associativity are recorded as not comparable with one another: an alternative algebra is power-associative, and an algebra that is flexible alone need not be.

**Theorem.** Every associative algebra is power-associative.

*Proof.* Let $x \in A$. The subalgebra generated by $x$ is the image of the polynomial algebra $R[t]$ under the $R$-algebra homomorphism $t \mapsto x$, since every element of that subalgebra is an $R$-linear combination of products of copies of $x$, that is, a polynomial in $x$. A homomorphic image of an associative algebra is associative, and $R[t]$ is associative and commutative; hence the subalgebra generated by $x$ is associative, and $A$ is power-associative. Alternatively, for an associative $A$ the identity $x^mx^n = x^{m+n}$ follows by induction on $n$, so the two bracketings of any power agree. $\square$

**Corollary.** An associative algebra satisfies every identity of the ladder of *Non-Associative Algebras and the Property Ladder*: it is alternative, flexible, power-associative and satisfies the Moufang identities, each by a direct substitution, over any commutative ring and without the characteristic restrictions that the ladder article imposes on its implications. The ladder is a chain of implications and not a chain of equivalences, and associativity is its top rung.

**Theorem (the converse fails).** There are power-associative algebras that are not associative.

*Proof.* Let $k$ be a field of characteristic not $2$ and let $B = M_2(k)$ carry the **symmetrised product**

$$
x \circ y = \tfrac{1}{2}(xy + yx),
$$

the algebra $B$ of *Non-Associative Algebras and the Property Ladder*, §*What the Ladder Does Not Decide*, where it is proved power-associative by the computation $z^{\circ n} = z^n$ of the powers of a single matrix. That verification is not repeated; what is needed here is that $B$ fails associativity, which is a failure on a different triple. With $x = E_{11}$, $y = E_{12}$ and $z = E_{21}$,

$$
(x \circ y) \circ z = \tfrac12 E_{12} \circ E_{21} = \tfrac14(E_{12}E_{21} + E_{21}E_{12}) = \tfrac14 I,
$$

while

$$
x \circ (y \circ z) = E_{11} \circ \tfrac12 I = \tfrac12\bigl(E_{11}\tfrac12 I + \tfrac12 I E_{11}\bigr) = \tfrac12 E_{11},
$$

and $\tfrac14 I \neq \tfrac12 E_{11}$, since the characteristic is not $2$. Hence $B$ is power-associative and not associative. $\square$

**Remark.** The example $B$ is the algebra used in *Non-Associative Algebras and the Property Ladder* to separate power-associativity from alternativity. Since an associative algebra is alternative, the failure of alternativity recorded there is already a failure of associativity, and the same algebra witnesses the strictness of the implication of §*Linearisation and Power-Associativity*.

**Remark (third-power associativity).** The weakest of the identities of the ladder, the single identity $x^2 x = x x^2$, is a consequence of associativity: it is flexibility with $y = x$, and every associative algebra is flexible. It is strictly weaker than power-associativity. The commutative algebra $A$ of *Non-Associative Algebras and the Property Ladder*, §*What the Ladder Does Not Decide*, is flexible, so by commutativity it satisfies $x^2 x = x x^2$, and it is not power-associative; hence third-power associativity does not imply power-associativity, and the implication is strict, the converse direction being immediate from $x^2x = x x^2 = x^3$.

## The Free Associative Algebra and the Tensor Algebra

The free algebra is the object that shows the identity of associativity is realised in the most general way: it satisfies it and imposes nothing else.

**Definition.** Let $X$ be a set and let $X^*$ be the **free monoid** on $X$, the set of words $x_{i_1} \cdots x_{i_k}$ in the letters $X$, including the empty word, with the concatenation of words as its product. The **monoid algebra** $R[X^*]$ is the free $R$-module on $X^*$ with the product extended from concatenation by bilinearity; its elements are the finite $R$-linear combinations of words. The **free associative algebra** on $X$ is this monoid algebra, written

$$
R\langle X \rangle = R[X^*],
$$

and $R\langle x_1, \dots, x_n \rangle$ when $X = \{x_1, \dots, x_n\}$ is finite. The monoid algebra $k[M]$ of a monoid $M$ is defined in *Non-Commutative Domains*, §*The Free Algebra*, and the construction there is the one used here.

**Theorem (universal property of the free algebra).** Let $A$ be an associative unital $R$-algebra and let $f : X \to A$ be any map. Then there is a unique unital $R$-algebra homomorphism $\bar f : R\langle X \rangle \to A$ with $\bar f(x) = f(x)$ for all $x \in X$.

*Proof.* The monoid algebra is generated by the images of the letters; the empty word is the identity. A homomorphism on $R\langle X\rangle$ is determined by its values on the letters, and prescribing $\bar f(x) = f(x)$ extends to words by multiplicativity, $\bar f(x_{i_1}\cdots x_{i_k}) = f(x_{i_1})\cdots f(x_{i_k})$, and to finite linear combinations by $R$-linearity. The result is well defined because a word has a unique expression in the basis of words, and it is multiplicative and unital by construction; uniqueness is clear since the letters generate $R\langle X\rangle$. $\square$

**Corollary.** The words in $X$, including the empty word, form an $R$-basis of $R\langle X\rangle$, and the degree-$k$ part of $R\langle X\rangle$ is free on the words of length $k$. In particular, over a field and for $X$ finite of cardinality $n$, the degree-$k$ part has dimension $n^k$; the algebra is commutative if and only if $n \leq 1$, and for $n = 1$ it is the polynomial algebra, $R\langle x\rangle = R[x]$.

The free algebra on a set is the special case of the free algebra on a module, and the general object is the tensor algebra.

**Theorem (the tensor algebra is the free associative algebra).** Let $M$ be an $R$-module and let $T(M) = \bigoplus_{n \geq 0} M^{\otimes n}$ be its tensor algebra, with $T^0(M) = R$ and with the product by concatenation of tensors. Then $T(M)$ is an associative unital $R$-algebra, and for every associative unital $R$-algebra $A$ the $R$-linear maps $M \to A$ correspond bijectively to the unital $R$-algebra homomorphisms $T(M) \to A$. Equivalently, in the notation of adjoint functors, the tensor algebra functor is left adjoint to the forgetful functor $U$ from unital associative $R$-algebras to $R$-modules,

$$
T \dashv U .
$$

The construction, the grading and the proof are those of *Tensor Powers and the Free Algebra*, §*The Universal Property*; they are quoted here and not repeated.

The theorem is the precise sense in which $T(M)$ is *the* free associative algebra on the module $M$: any linear map out of $M$ into an associative algebra extends to a homomorphism out of $T(M)$, uniquely, and this property determines $T(M)$ up to a unique isomorphism of algebras.

**Corollary.** For the free module $R^{(X)}$ on a set $X$ the tensor algebra is the free algebra, $R\langle X\rangle \cong T\bigl(R^{(X)}\bigr)$; and a choice of generators of $A$ and the induced surjection $R\langle X\rangle \to A$ present it as a quotient of a free one, $A \cong R\langle X\rangle/I$, the general form of a presentation by generators and relations (*Tensor Powers and the Free Algebra*, §*The Universal Property*).

## The Universal Enveloping Algebra

Associativity is not the only structure that a bilinear product may carry: the anti-symmetric product of a Lie algebra, defined and studied in *Lie Algebras*, satisfies the Jacobi identity in place of associativity. The two are related in both directions. In one direction every associative algebra carries a Lie algebra structure; in the other every Lie algebra carries a universal associative algebra.

**Definition.** Let $A$ be an associative $R$-algebra. The **commutator algebra** $A^-$ is the $R$-module $A$ with the product

$$
[x,y] = xy - yx .
$$

**Theorem.** For an associative algebra $A$, the commutator product is bilinear and anti-symmetric and satisfies the Jacobi identity

$$
[x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0 ,
$$

so that $A^-$ is a Lie algebra. Equivalently, every associative algebra is a Lie algebra under the commutator. The theorem is proved in *Lie Algebras*, §*The Relationship with Associative Algebras*, and it is the reason that the Lie algebras of Part I are not foreign objects: they are the anti-symmetric shadows of associative ones.

**Definition.** Let $\mathfrak{g}$ be a Lie algebra over $R$ with bracket $[\cdot,\cdot]$, as introduced in *Lie Algebras*. The **universal enveloping algebra** $U(\mathfrak{g})$ is the associative $R$-algebra, with identity, characterised by the following universal property: for every associative unital $R$-algebra $A$ and every $R$-linear map $\varphi : \mathfrak{g} \to A$ satisfying

$$
\varphi([x,y]) = \varphi(x)\varphi(y) - \varphi(y)\varphi(x),
$$

there is a unique unital $R$-algebra homomorphism $\Phi : U(\mathfrak{g}) \to A$ with $\Phi \circ \iota = \varphi$, where $\iota : \mathfrak{g} \to U(\mathfrak{g})$ is the canonical $R$-linear map. Equivalently, $\iota$ is a Lie algebra homomorphism $\mathfrak{g} \to U(\mathfrak{g})^-$, and there is a natural bijection

$$
\operatorname{Hom}_{\mathsf{Lie}_R}\bigl(\mathfrak{g}, A^-\bigr) \;\cong\; \operatorname{Hom}_{\mathsf{Alg}_R}\bigl(U(\mathfrak{g}), A\bigr).
$$

In the language of adjoint functors, the enveloping algebra functor $U$ is left adjoint to the commutator functor $A \mapsto A^-$. The construction of $U(\mathfrak{g})$ as the quotient $T(\mathfrak{g})/\langle x \otimes y - y \otimes x - [x,y]\rangle$ of the tensor algebra by the two-sided ideal generated by the displayed relations, and the proof of the universal property, belong to *Universal Enveloping Algebras*; only the statement is used here.

**Theorem (Poincaré–Birkhoff–Witt).** Let $k$ be a field, let $\mathfrak{g}$ be a Lie algebra over $k$ and let $(x_i)_{i \in I}$ be a basis of $\mathfrak{g}$, totally ordered. Then the ordered monomials

$$
x_{i_1}^{a_1} x_{i_2}^{a_2} \cdots x_{i_r}^{a_r}, \qquad i_1 < i_2 < \cdots < i_r, \quad a_j \geq 1,
$$

together with the identity, form a $k$-basis of $U(\mathfrak{g})$. Consequently the canonical map $\iota : \mathfrak{g} \to U(\mathfrak{g})$ is injective, and the associated graded of the degree filtration is the symmetric algebra, $\operatorname{gr} U(\mathfrak{g}) \cong \operatorname{Sym}(\mathfrak{g})$.

The theorem and its proof are those of *Universal Enveloping Algebras*, §*The Filtration and the Poincaré–Birkhoff–Witt Theorem*, where the filtration, the diamond lemma argument and the Poincaré series are given; they are quoted here.

**Remark.** The pair of constructions shows the exact relation between associativity and its failure. The functor $A \mapsto A^-$ forgets associativity and keeps the commutator; the functor $U$ restores an associative product in the most economical way, and the adjunction says that the two are inverse in the only sense available: an algebra homomorphism $U(\mathfrak{g}) \to A$ is the same thing as a linear map $\mathfrak{g} \to A$ that respects the bracket. When $\mathfrak{g}$ is abelian the bracket vanishes and $U(\mathfrak{g}) = \operatorname{Sym}(\mathfrak{g})$, the symmetric algebra; when $\mathfrak{g}$ is the Lie algebra of a Lie group, $U(\mathfrak{g})$ is the algebra whose modules are the representations of the group, a statement of Parts II and III. The enveloping algebra is the one construction of this article that is genuinely new, and it is the reason an associative algebra is attached in a canonical way to every non-associative one.

## The Model: Matrix and Endomorphism Algebras

The model associative algebra is the endomorphism algebra of a module, and every associative algebra embeds in one.

**Theorem.** Let $M$ be an $R$-module. Then $\operatorname{End}_R(M)$, with addition and composition of maps, is an associative $R$-algebra with identity $\mathrm{id}_M$. For $M = R^n$ the choices of a basis give an isomorphism

$$
M_n(R) \cong \operatorname{End}_R(R^n)
$$

of $R$-algebras, and the matrix units $E_{ij}$ form a basis of $M_n(R)$ with $E_{ij}E_{kl} = \delta_{jk}E_{il}$. The matrix algebra, its units and its ideals are the subject of *Matrix Algebras*, where these statements are proved.

**Proposition (the regular representation).** Let $A$ be an $R$-algebra and let $L : A \to \operatorname{End}_R(A)$ be given by $L(a)(x) = ax$. Then $L$ is $R$-linear, and

$$
L(ab) = L(a) \circ L(b) \quad \text{for all } a, b \in A
$$

if and only if $A$ is associative. If $A$ is associative and unital then $L$ is injective, so $A$ embeds in $\operatorname{End}_R(A)$.

*Proof.* The map $L$ is $R$-linear because the product is. For $a, b, x \in A$, $L(a)L(b)(x) = a(bx)$ while $L(ab)(x) = (ab)x$; the two are equal for every $x$ exactly when $a(bx) = (ab)x$ for all $a, b, x$, that is, when $A$ is associative. If $A$ is unital and $L(a) = 0$ then $a = a\,1 = L(a)(1) = 0$. $\square$

The proposition locates associativity precisely: it is the condition that the left multiplications compose, $L_a L_b = L_{ab}$. Without it there is no homomorphism $A \to \operatorname{End}_R(A)$, and the regular module $A_A$ of *Centre, Units, Zero Divisors and Division Algebras* has no algebra of operators to come from.

**Theorem (modules are homomorphisms).** Let $A$ be an associative unital $R$-algebra and $M$ an $R$-module. A unital $A$-module structure on $M$ is the same thing as a unital $R$-algebra homomorphism $\rho : A \to \operatorname{End}_R(M)$; the correspondence is $\rho(a)(m) = a \cdot m$.

*Proof.* If $M$ is an $A$-module then $\rho(a)$ is $R$-linear, $\rho$ is $R$-linear and $\rho(ab) = \rho(a)\rho(b)$, $\rho(1_A) = \mathrm{id}_M$. Conversely a unital algebra homomorphism $\rho$ defines an action by $a \cdot m = \rho(a)(m)$, whose module axioms are the assertions that $\rho$ is linear, multiplicative and unital. $\square$

The theorem is the reason the representation theory of the corpus is written as the module theory of an associative algebra: a representation and a homomorphism into an endomorphism algebra are the same object.

## Algebras That Fail Associativity

Each of the following is a named object of the corpus for which associativity fails, with the article that records it.

- **The commutator algebra $A^-$.** For an associative $A$ that is not commutative, the anti-symmetric product $[x,y] = xy - yx$ is not associative. In $A = M_2(k)$,

$$
[[E_{11}, E_{12}], E_{21}] = [E_{12}, E_{21}] = E_{11} - E_{22}, \qquad [E_{11}, [E_{12}, E_{21}]] = [E_{11}, E_{11} - E_{22}] = 0,
$$

so the two bracketings differ. The construction and its properties are in *Lie Algebras*, §*The Relationship with Associative Algebras*.

- **A Lie algebra under its bracket.** The definition of *Lie Algebras* imposes anti-symmetry and the Jacobi identity rather than associativity, and the cross product algebra on $\mathbb{R}^3$ is the simplest example. Associativity fails at once: $(e_1 \times e_2) \times e_2 = e_3 \times e_2 = -e_1$, while $e_1 \times (e_2 \times e_2) = 0$. The cross product is named as a non-example in *Algebras*.

- **The octonions $\mathbb{O}$.** The octonion algebra is alternative, flexible, power-associative and satisfies the Moufang identities, and it is not associative: over a field of characteristic not $2$ its associator is nonzero, with $[e_1, e_2, e_4] = 2e_7$ on the basis of *Non-Associative Algebras and the Property Ladder*. It is the extreme rung of the doubling ladder $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ at which associativity is lost while power-associativity survives.

- **The sixteen-dimensional Cayley–Dickson algebra.** One further doubling past the octonions produces an algebra that is not even alternative and has zero divisors, recorded as such in *Non-Associative Algebras and the Property Ladder*.

- **The Jordan algebras.** A commutative algebra satisfying the Jordan identity $x^2(yx) = (x^2y)x$ is not associative in general: the symmetrised product $x \circ y = \tfrac12(xy + yx)$ of an associative algebra is a Jordan algebra (*Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*), and for $M_2(k)$ over a field of characteristic not $2$ the result is the commutative unital algebra $B$ of §*Linearisation and Power-Associativity*, which is not associative.

- **The strictness witnesses of the ladder.** The algebra $A$ with basis $u, v$ and products $u^2 = v$, $uv = vu = v$, $v^2 = 0$ is flexible and not power-associative, and so not associative; the symmetrised matrix algebra $B$ of §*Linearisation and Power-Associativity* is power-associative and not associative. Both are in *Non-Associative Algebras and the Property Ladder*, §*What the Ladder Does Not Decide*.

Associativity is thus an axiom that the corpus's non-associative objects visibly fail, and the ladder measures where each of them stands.

## Where the Corpus Uses Associativity

Associativity is assumed in most of the corpus, and it is used at specific points, each with an article that records the use.

- **Products of ideals.** For two-sided ideals $I$ and $J$ of an algebra $A$, the intersection $I \cap J$ and the sum $I + J$ are two-sided ideals, and the span $IJ$ of the products $xy$ with $x \in I$, $y \in J$ satisfies $IJ \subseteq I \cap J$; that $IJ$ is itself a two-sided ideal needs associativity, because the proof moves a factor through the bracket, $a(xy) = (ax)y$ and $(xy)a = x(ya)$. The statements are *Ideals and Quotients of Algebras*, §*Products and Sums of Ideals*, where the same distinction is drawn, and its §*Quotient Algebras* notes that the quotient construction itself needs no associativity.

- **Powers of an ideal.** The sequence $I \supseteq I^2 \supseteq I^3 \supseteq \cdots$ exists only when the products are associative, and it is what makes sense of a nilpotent ideal, of a square-zero ideal such as $(\varepsilon) \subset \mathbb{D}'$, and of the nilradical of *Reduced Rings and the Nilradical*.

- **Modules and representations.** The identification of a representation with a homomorphism $A \to \operatorname{End}_R(M)$ of §*The Model: Matrix and Endomorphism Algebras* is a statement about associative algebras, and it is the form in which the module theory of *Modules* and the representation theory of *Group Algebras* are written.

- **The bar resolution and Hochschild homology.** The Hochschild complex of an algebra is a complex, its differential satisfying $b^2 = 0$, because the multiplication is associative; the bar resolution and its homology and cohomology are built on that identity in *Hochschild Homology*, whose standing hypothesis is an associative algebra with unit.

- **Presentations by generators and relations.** The quotient presentations $\mathbb{C} = \mathbb{R}\langle x\rangle/(x^2+1)$, $\mathbb{D} = \mathbb{R}\langle x\rangle/(x^2-1)$, $\mathbb{D}' = \mathbb{R}\langle x\rangle/(x^2)$ and $\mathbb{H} = \mathbb{R}\langle x,y\rangle/(x^2+1, y^2+1, xy+yx)$ are presentations of associative algebras, in the form and the notation of *Quotients of the Tensor Algebra*, and the free algebra on which the last of them is built is the free associative algebra of this article.

Associativity is therefore not an incidental hypothesis. It is what makes the product of an algebra act on its ideals, on its modules and on its homology; it holds for the matrix algebras, the endomorphism algebras, the polynomial algebras, the group algebras, the tensor algebra, the algebras of *The Symmetric Algebra*, *The Exterior Algebra* and *Clifford Algebras in Finite Dimensions*, the enveloping algebras and the algebras of the number systems, with the octonions and the algebras of the ladder the named exceptions.

## Summary

An $R$-algebra is **associative** when $(xy)z = x(yz)$ for all $x, y, z$. The identity is a **polynomial identity**, and it is expressed by the **associator** $[x,y,z] = (xy)z - x(yz)$, which is $R$-trilinear; the algebra is associative exactly when the associator vanishes identically, and because the associator is trilinear it is enough to check the identity on a spanning set, or on a basis when $A$ is free. Associativity is inherited by subalgebras, quotients and homomorphic images and preserved by direct sums and tensor products.

Associativity implies **power-associativity**, the associativity of the subalgebra generated by any one element, and hence every identity of the ladder of *Non-Associative Algebras and the Property Ladder*; the converse fails, the symmetrised matrix algebra $M_2(k)$ with $x \circ y = \tfrac12(xy + yx)$ being power-associative and not associative. The **free associative algebra** $R\langle X\rangle$ is the monoid algebra of the free monoid on $X$, with basis the words and the universal property that every map $X \to A$ into an associative unital algebra extends uniquely; the **tensor algebra** $T(M) = \bigoplus_{n \geq 0} M^{\otimes n}$ is the free associative algebra on a module, with the adjunction $T \dashv U$ of *Tensor Powers and the Free Algebra*. The **universal enveloping algebra** $U(\mathfrak{g})$ is the associative algebra attached to a Lie algebra by the adjunction $U \dashv (-)^-$ with the commutator functor, and by the **Poincaré–Birkhoff–Witt theorem** the Lie algebra sits inside it with associated graded the symmetric algebra; both statements are quoted from *Universal Enveloping Algebras*.

The model associative algebra is $\operatorname{End}_R(M)$, with $M_n(R) \cong \operatorname{End}_R(R^n)$ as its matrix case, and a unital $A$-module is the same thing as a homomorphism $A \to \operatorname{End}_R(M)$. The algebras of the corpus that fail associativity are the commutator algebras $A^-$, the Lie algebras and the cross product on $\mathbb{R}^3$, the octonions, the sixteen-dimensional Cayley–Dickson algebra, the Jordan algebras that are not associative and the strictness witnesses of the ladder. Associativity is assumed in the corpus where it is needed: for the product of ideals and powers of an ideal, for modules and representations, for the bar resolution of Hochschild homology, and for the presentations of the number systems by generators and relations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $A$ | An $R$-algebra in the broad sense of *Algebras*, associative where stated |
| $[x,y,z] = (xy)z - x(yz)$ | The associator, an $R$-trilinear map, as in *Non-Associative Algebras and the Property Ladder* |
| $x^n$ | The $n$-th power, $x^{n+1} = x^n x$ |
| $X^*$, $R\langle X\rangle$ | The free monoid on $X$ and its monoid algebra, the free associative algebra |
| $R\langle x_1,\dots,x_n\rangle$ | The free associative algebra on $n$ generators |
| $T(M) = \bigoplus_{n \geq 0} M^{\otimes n}$ | The tensor algebra, the free associative algebra on $M$; $T(R^{(X)}) \cong R\langle X\rangle$ |
| $T \dashv U$ | Tensor algebra left adjoint to the forgetful functor to $R$-modules |
| $A^-$ | The commutator algebra of an associative algebra, $[x,y] = xy - yx$ |
| $[x,y] = xy - yx$ | The commutator bracket of $A^-$, of arity two, distinct from the ternary associator $[x,y,z]$ |
| $\mathfrak{g}$, $U(\mathfrak{g})$ | A Lie algebra and its universal enveloping algebra |
| $U \dashv (-)^-$ | Enveloping algebra left adjoint to the commutator functor |
| $\iota : \mathfrak{g} \to U(\mathfrak{g})$ | The canonical map, injective by Poincaré–Birkhoff–Witt |
| $\operatorname{Sym}(\mathfrak{g})$ | The symmetric algebra, $\cong \operatorname{gr} U(\mathfrak{g})$ |
| $M_n(R)$, $E_{ij}$ | The matrix algebra and its matrix units, $E_{ij}E_{kl} = \delta_{jk}E_{il}$ |
| $\operatorname{Hom}_{\mathsf{Lie}_R}$, $\operatorname{Hom}_{\mathsf{Alg}_R}$ | Homomorphisms of Lie algebras, and of unital associative $R$-algebras |
| $\operatorname{End}_R(M)$, $L_a$ | The endomorphism algebra and the left multiplication $L_a(x) = ax$ |
| $x \circ y = \tfrac12(xy + yx)$ | The symmetrised product, commutative and generally non-associative; *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*, writes the same symmetrisation as $xy + yx$, the two differing by the unit $2$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory of associative algebras, the free algebra and the enveloping algebra.
- Paul M. Cohn, *Free Rings and Their Relations* (Academic Press, 2nd ed. 1985), for the free associative algebra and its quotients.
- Jacques Dixmier, *Enveloping Algebras* (North-Holland, 1977), for the universal enveloping algebra and the Poincaré–Birkhoff–Witt theorem in full.
- A. A. Albert, *Power-associative rings* (Transactions of the American Mathematical Society, 1948), for power-associativity and the identities that generate it.
