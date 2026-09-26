
# __Ideals and Quotients of Algebras__

## Introduction

An algebra over a commutative ring $R$ is an $R$-module equipped with a bilinear product. That is the broad sense fixed in *Algebras: A General Introduction*: an algebra need not be associative, need not be commutative, and need not have a unit. This article develops the part of the structure theory on which every later construction rests — subalgebras, the three kinds of ideal, quotient algebras, algebra homomorphisms, and the isomorphism theorems.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, and $A$ is an algebra over $R$ in the broad sense, unless a sentence names a stronger hypothesis. Associativity is flagged at each point where it is used. The module-theoretic facts we invoke — submodules, quotient modules, kernels, images, and the correspondence between the submodules of a quotient and the submodules above the kernel — are those of *Modules*, §4–§7, and the ring-theoretic analogues are those of *Rings*, §6.

The guiding observation is that the formalism of ideals and quotients depends very little on associativity. The definitions, the quotient construction, and the isomorphism theorems need only bilinearity. Associativity enters when one wants to multiply ideals, to describe a generated ideal by expressions $asb$, or to speak of powers of an ideal. The final sections collect the ideals of the small algebras and the quotient presentations that produce the number systems.

## Subalgebras

**Definition.** Let $A$ be an $R$-algebra. A submodule $B \subseteq A$ is a **subalgebra** of $A$ if it is closed under the product, that is, $xy \in B$ for all $x, y \in B$. With the restricted product, $B$ is an $R$-algebra in its own right.

A subalgebra of an associative algebra is associative, and a subalgebra of a commutative algebra is commutative; these properties are inherited because they are identities between products. The unit does not automatically lie in a subalgebra: $\{0\}$ is a subalgebra of every algebra, unital or not. A **unital subalgebra** of a unital algebra $A$ is one containing $1_A$; then it has its own unit, necessarily $1_A$.

**Proposition.** The intersection $\bigcap_i B_i$ of any family of subalgebras of $A$ is a subalgebra.

*Proof.* The intersection is a submodule by *Modules*, §4, and if $x, y$ lie in every $B_i$ then $xy$ lies in every $B_i$ by closure. $\square$

The **subalgebra generated** by a subset $S \subseteq A$ is the intersection of all subalgebras containing $S$; it is the smallest subalgebra containing $S$. Its elements are the $R$-linear combinations of products of elements of $S$. For a general algebra the products are read as iterated products with a fixed bracketing, since no associativity is available to reassociate them.

**Example.** The subspaces of a matrix algebra and of a tensor algebra discussed in *Algebras: A General Introduction* are subalgebras: the diagonal matrices in $M_n(k)$ form a commutative subalgebra isomorphic to $k^n$; the upper triangular matrices form a subalgebra; the purely off-diagonal matrices do not, since the square of an off-diagonal matrix can be diagonal.

## Ideals

There are three notions, distinguished by the side on which the algebra acts.

**Definition.** Let $A$ be an $R$-algebra. A submodule $I \subseteq A$ is a

- **left ideal** if $ax \in I$ for all $a \in A$ and $x \in I$;
- **right ideal** if $xa \in I$ for all $a \in A$ and $x \in I$;
- **two-sided ideal** (or simply **ideal**) if it is both a left and a right ideal.

Every two-sided ideal is a submodule and, since $xx' \in I$ for $x, x' \in I$, also a subalgebra. Left ideals and right ideals need not be subalgebras. If $A$ is commutative the three notions coincide, and we speak of **ideals** without qualification.

The trivial ideals are $\{0\}$ and $A$; an ideal is **proper** if it is neither. In a unital algebra $A$ a proper ideal $I$ contains no unit, because $u \in I$ together with $u u^{-1} = 1$ would give $1 \in I$ and then $I = A$; consequently $A$ is a division algebra precisely when it is unital and its only left ideals are $0$ and $A$, a point developed.

**Proposition (kernels and images).** Let $\varphi : A \to B$ be an algebra homomorphism. Then $\ker \varphi$ is a two-sided ideal of $A$ and $\operatorname{im} \varphi$ is a subalgebra of $B$.

*Proof.* The kernel is a submodule by module theory, and for $x \in \ker\varphi$ and $a \in A$ one has $\varphi(ax) = \varphi(a)\varphi(x) = 0$ and $\varphi(xa) = \varphi(x)\varphi(a) = 0$, so $\ker\varphi$ is two-sided. The image is a submodule closed under products, since $\varphi(x)\varphi(y) = \varphi(xy)$ is again in the image. $\square$

**Proposition (preimages and images of ideals).** Let $\varphi : A \to B$ be an algebra homomorphism. If $J \subseteq B$ is a (left, right, two-sided) ideal, then $\varphi^{-1}(J)$ is an ideal of $A$ of the same kind. If $I \subseteq A$ is a two-sided ideal with $\ker \varphi \subseteq I$, then $\varphi(I)$ is a two-sided ideal of $\operatorname{im}\varphi$.

*Proof.* For the preimage, if $\varphi(x) \in J$ then $\varphi(ax) = \varphi(a)\varphi(x) \in J$, and dually on the right. For the image, if $y = \varphi(x)$ with $x \in I$ and $b = \varphi(a)$, then $by = \varphi(ax)$ with $ax \in I$, and dually. $\square$

The hypothesis $\ker\varphi \subseteq I$ is exactly what makes $I$ the preimage of $\varphi(I)$: an element $x \in A$ with $\varphi(x) \in \varphi(I)$ differs from an element of $I$ by an element of $\ker\varphi$, hence lies in $I$.

### Generated Ideals

**Definition.** For a subset $S \subseteq A$, the **two-sided ideal generated by $S$**, written $(S)$ or $\langle S \rangle$, is the intersection of all two-sided ideals containing $S$.

**Proposition.** The ideal generated by $S$ consists of the finite $R$-linear combinations of elements obtained from elements of $S$ by repeatedly multiplying on the left or on the right by elements of $A$.

*Proof.* The set described is a submodule containing $S$, and it is closed under left and right multiplication by $A$ because adjoining one more factor preserves the description. It is therefore a two-sided ideal containing $S$, and it is contained in every such ideal by induction on the number of factors. $\square$

When $A$ is associative the description simplifies: the two-sided ideal generated by $S$ is the set of finite sums

$$
\sum_i a_i s_i b_i, \qquad a_i, b_i \in A, \ s_i \in S,
$$

with the $R$-linear combinations absorbed into the coefficients. In the commutative associative case this collapses further to $\sum_i a_i s_i$, the familiar ideal generated by a set in a ring.

**Example.** In the polynomial algebra $k[x]$, the ideal generated by $f$ is $(f) = \{fg: g \in k[x]\}$, and $k[x]/(f)$ is the quotient algebra; for $f$ irreducible this quotient is a field, and for $f = (x-a)^2$ it is the algebra of dual numbers over $k$.

### Products and Sums of Ideals

**Proposition.** Let $I$ and $J$ be two-sided ideals of $A$. Then $I \cap J$ and $I + J$ are two-sided ideals. If $A$ is associative, the submodule $IJ$ spanned by the products $xy$ with $x \in I$, $y \in J$ is a two-sided ideal, and $IJ \subseteq I \cap J$.

*Proof.* Intersections and sums of submodules are submodules (*Modules*, §4), and both are stable under multiplication by $A$ because each summand is. For $IJ$, associativity gives $a(xy) = (ax)y \in IJ$ and $(xy)a = x(ya) \in IJ$; the inclusion $IJ \subseteq I \cap J$ holds because $xy \in I$ and $xy \in J$ for $x \in I$, $y \in J$. $\square$

Associativity is genuinely needed for $IJ$ to be an ideal. In a non-associative algebra the span of the products need not be closed under multiplication by $A$, and one must work instead with the ideal generated by the products.

**Example (square-zero ideals).** An ideal $I$ with $I^2 = 0$ is called **square-zero**. The dual numbers $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ have the maximal ideal $(\varepsilon)$, which is square-zero. A square-zero ideal is the algebraic expression of an infinitesimal thickening, and it is the local model for a deformation.

## Quotient Algebras

The purpose of an ideal is to be divided out.

**Theorem.** Let $I$ be a two-sided ideal of the $R$-algebra $A$. On the quotient module $A/I$ define a product by

$$
(a + I)(b + I) = ab + I.
$$

This is well defined, and it makes $A/I$ an $R$-algebra. The natural projection $\pi : A \to A/I$, $\pi(a) = a + I$, is a surjective algebra homomorphism with kernel $I$.

*Proof.* Suppose $a' = a + x$ and $b' = b + y$ with $x, y \in I$. Bilinearity gives

$$
a'b' = (a + x)(b + y) = ab + ay + xb + xy.
$$

Now $ay \in I$ and $xb \in I$ because $I$ is a right ideal and a left ideal respectively, and $xy \in I$ because $I$ is closed under products. Hence $a'b' - ab \in I$, and $a'b' + I = ab + I$: the product is well defined. The algebra axioms transfer from $A$ because addition, scalar multiplication and the product are computed from representatives, and bilinearity of the product on $A$ gives bilinearity on $A/I$. The projection is $R$-linear, surjective, multiplicative, and has kernel $I$. $\square$

Notice that the proof uses only that $I$ is closed under products and under multiplication by $A$; associativity of $A$ is never invoked. The quotient of a non-associative algebra by a two-sided ideal is therefore again an algebra of the same kind, and the quotient of an associative algebra is associative.

**Definition.** $A/I$ is the **quotient algebra** of $A$ by $I$, and $\pi$ is the **quotient map**.

**Example.** Every quotient of $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ is read off from the idempotents $e_\pm = \tfrac{1}{2}(1 \pm j)$. The ideals $\mathbb{D}e_+$ and $\mathbb{D}e_-$ are two-sided, $\mathbb{D}/\mathbb{D}e_- \cong \mathbb{R}$, and since $e_+ e_- = 0$ one has $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$ as an algebra, so $\mathbb{D}$ is the direct sum of the two quotients.

**Example.** $\mathbb{H}$ has no proper nonzero two-sided ideal, so the only quotients of $\mathbb{H}$ are $0$ and $\mathbb{H}$ itself. This is the content of $\mathbb{H}$ being a division algebra, and it is proved in *Quaternion Algebra ($\mathbb{H}$)*.

## Algebra Homomorphisms

**Definition.** Let $A$ and $B$ be $R$-algebras. A map $\varphi : A \to B$ is an **algebra homomorphism** if it is $R$-linear and multiplicative:

$$
\varphi(x + y) = \varphi(x) + \varphi(y), \quad \varphi(rx) = r\varphi(x), \quad \varphi(xy) = \varphi(x)\varphi(y)
$$

for all $x, y \in A$ and $r \in R$. It is a **monomorphism** if injective, an **epimorphism** if surjective, an **isomorphism** if bijective, an **endomorphism** if $A = B$, and an **automorphism** if it is a bijective endomorphism. A homomorphism of unital algebras is **unital** if $\varphi(1_A) = 1_B$.

The composite of two homomorphisms is a homomorphism, and the identity is a homomorphism; consequently the $R$-algebra automorphisms of $A$ form a group under composition, written $\operatorname{Aut}_R(A)$ and studied.

**Proposition.** A homomorphism $\varphi$ is injective if and only if $\ker\varphi = 0$. A bijective homomorphism has a two-sided inverse, which is again a homomorphism.

*Proof.* The first statement is the module-theoretic criterion. For the second, if $\varphi$ is bijective and $u, v \in B$, write $u = \varphi(x)$, $v = \varphi(y)$; then $\varphi^{-1}(uv) = \varphi^{-1}(\varphi(xy)) = xy = \varphi^{-1}(u)\varphi^{-1}(v)$, and $R$-linearity of $\varphi^{-1}$ follows from that of $\varphi$. $\square$

**Example (the universal property of a quotient).** Let $I$ be a two-sided ideal of $A$. For every algebra $B$, precomposition with the quotient map is a bijection

$$
\{\text{algebra homomorphisms } A/I \to B\} \;\longrightarrow\; \{\text{algebra homomorphisms } \varphi : A \to B \text{ with } I \subseteq \ker\varphi\}.
$$

This is the defining universal property of the quotient, and it is the form in which quotients are used to present algebras by generators and relations.

**Example (evaluation).** For a commutative ring $k$ and a point $a \in k$, the evaluation map $k[x] \to k$, $f \mapsto f(a)$, is a unital homomorphism of $k$-algebras with kernel the ideal $(x - a)$. The map $k[x] \to \operatorname{Fun}(k,k)$ recording all evaluations is not injective in general: over $k = \mathbb{Z}/4\mathbb{Z}$ the polynomial $2x^2 + 2x$ is nonzero and vanishes at all four points $0, 1, 2, 3$, and over the field $\mathbb{F}_2$ the polynomial $x^2 - x$ is nonzero and vanishes at both points. Over an infinite integral domain the map *is* injective, since a nonzero polynomial has only finitely many roots there.

**Remark (no algebra structure on $\operatorname{Hom}$).** The set $\operatorname{Hom}_R(A,B)$ of algebra homomorphisms is not an $R$-algebra under pointwise operations: the pointwise product of two multiplicative maps need not be multiplicative. It is a set, and when $A = B$ it is a monoid under composition. The pointwise operations do make the *linear* maps $\operatorname{Hom}_R(A,B)$ into an $R$-module, and into an $R$-algebra when $B$ is commutative.

## The Isomorphism Theorems

The three isomorphism theorems and the correspondence theorem carry over from modules without change, with "submodule" replaced by "subalgebra" or "ideal" as appropriate.

**Theorem (first isomorphism theorem).** Let $\varphi : A \to B$ be an algebra homomorphism. Then $\varphi$ induces an isomorphism

$$
A/\ker\varphi \;\cong\; \operatorname{im}\varphi,
$$

given by $a + \ker\varphi \mapsto \varphi(a)$.

*Proof.* The map is well defined and $R$-linear by the module theorem; it is multiplicative because $\varphi$ is, and it is bijective onto the image by construction. $\square$

**Theorem (second isomorphism theorem).** Let $B$ be a subalgebra and $I$ a two-sided ideal of $A$. Then $B + I$ is a subalgebra of $A$, $B \cap I$ is a two-sided ideal of $B$, and

$$
(B + I)/I \;\cong\; B/(B \cap I).
$$

*Proof.* For $b, b' \in B$ and $x, x' \in I$,

$$
(b + x)(b' + x') = bb' + bx' + xb' + xx' \in B + I,
$$

since $bb' \in B$ and the remaining three terms lie in $I$; this also shows that $I$ is an ideal of $B + I$. The intersection $B \cap I$ is a submodule of $B$ closed under multiplication by $B$, hence an ideal of $B$, and the map $b + (B\cap I) \mapsto b + I$ is the required isomorphism. $\square$

**Theorem (third isomorphism theorem).** Let $I \subseteq J$ be two-sided ideals of $A$. Then $J/I$ is a two-sided ideal of $A/I$, and

$$
(A/I)/(J/I) \;\cong\; A/J.
$$

*Proof.* The set $J/I$ is the image of $J$ under the quotient map, so it is an ideal by the proposition on images of ideals. The composite $A \to A/I \to (A/I)/(J/I)$ has kernel $J$, so the first isomorphism theorem applies. $\square$

**Theorem (correspondence theorem).** Let $I$ be a two-sided ideal of $A$ and $\pi : A \to A/I$ the quotient map. The map $J \mapsto \pi^{-1}(J)$ is a bijection from the set of two-sided ideals of $A/I$ onto the set of two-sided ideals of $A$ containing $I$, with inverse $J \mapsto J/I$. The bijection preserves inclusion, and it restricts to a bijection between the maximal ideals on the two sides.

*Proof.* Combine the module correspondence theorem with the proposition on preimages and images; the preimage of an ideal of $A/I$ is an ideal of $A$ containing $I = \ker\pi$, and the two constructions are mutually inverse. The statement about maximal ideals is immediate from the preservation of inclusion. $\square$

## Simplicity, Maximality and the Radical

**Definition.** A nonzero algebra $A$ is **simple** if its only two-sided ideals are $0$ and $A$. In the non-unital case one adds the requirement $A^2 \neq 0$, so that an algebra with $A^2 = 0$ is not counted as simple.

**Definition.** A proper two-sided ideal $I \subsetneq A$ is **maximal** if there is no two-sided ideal strictly between $I$ and $A$. Over a unital algebra, Zorn's lemma applied to the proper ideals containing a given proper ideal produces a maximal ideal above it, exactly as for rings (*Rings*, §6).

**Proposition.** Let $I$ be a proper two-sided ideal of a unital algebra $A$. Then $I$ is maximal if and only if $A/I$ is simple.

*Proof.* By the correspondence theorem, the ideals of $A/I$ correspond to the ideals of $A$ containing $I$. The quotient $A/I$ has only the two trivial ideals exactly when there is no proper ideal strictly between $I$ and $A$. The condition $A^2 \nsubseteq I$ holds for a maximal ideal of a unital algebra because otherwise $A^2 \subseteq I$ and, since $A^2 = A$ for unital $A$, $I = A$. $\square$

**Corollary.** Let $k$ be a field and $A$ a commutative unital $k$-algebra. A two-sided ideal $I \subsetneq A$ is maximal if and only if $A/I$ is a field.

*Proof.* A commutative unital algebra is simple exactly when it is a field: if $A/I$ is simple and $a + I \neq 0$, the ideal generated by $a + I$ is nonzero, hence all of $A/I$, so $a + I$ is a unit; conversely a field has no proper nonzero ideals. $\square$

The **Jacobson radical** $J(A)$ of a unital associative algebra is the intersection of its maximal left ideals; it is a two-sided ideal, and $x \in J(A)$ if and only if $1 - ax$ is a unit for every $a \in A$. The radical is the natural home of the algebra analogue of Nakayama's lemma (*Modules*, §11), and it measures the failure of the regular module to be semisimple. The structure theory of modules over an algebra belongs to category 08 and is not developed here.

## Ideals and Quotients in the Small Algebras

The ideals of the standard examples are collected in the following table, with the quotient that each produces. The entries are verified in the companion articles named in the right-hand column; the table is a guide to those computations, not a substitute for them.

| Algebra | Two-sided ideals | Quotient | Reference |
|---|---|---|---|
| $\mathbb{R}$ | $0$, $\mathbb{R}$ | field, no proper quotient ||
| $\mathbb{C}$ | $0$, $\mathbb{C}$ | field ||
| $\mathbb{D}$ | $0$, $\mathbb{D}e_+$, $\mathbb{D}e_-$, $\mathbb{D}$ | $\mathbb{D}/\mathbb{D}e_\pm \cong \mathbb{R}$ | *Split Complex Algebra* |
| $\mathbb{D}'$ | $0$, $(\varepsilon)$, $\mathbb{D}'$ | $\mathbb{D}'/(\varepsilon)\cong\mathbb{R}$ | *Dual Numbers Algebra* |
| $\mathbb{H}$ | $0$, $\mathbb{H}$ | $\mathbb{H}$ is a division algebra | *Quaternion Algebra ($\mathbb{H}$)* |
| $\mathbb{H}_{\mathbb{D}}$ | $0$, $\mathbb{H}_{\mathbb{D}}e_+$, $\mathbb{H}_{\mathbb{D}}e_-$, $\mathbb{H}_{\mathbb{D}}$ | $\mathbb{H}_{\mathbb{D}}/\mathbb{H}_{\mathbb{D}}e_\pm \cong \mathbb{H}$ ||
| $\mathbb{B}$ | $0$, $\mathbb{B}$ | $M_2(\mathbb{C})$ is simple | *Biquaternion Algebra ($\mathbb{B}$)* |
| $M_n(k)$ | $0$, $M_n(k)$ | $M_n(k)$ is simple ||
| $k[x]$, $k$ a field | $(f)$, $f \in k[x]$ | $k[x]/(f)$ ||
| $k[G]$ | augmentation ideal and its sub-ideals | $k[G]/I(G) \cong k$ ||

The pattern is that the ideals of a division algebra are trivial, that a simple algebra which is not a division algebra — $M_n(k)$, $\mathbb{B}$ — also has trivial two-sided ideals, and that zero divisors bring nontrivial ideals with them. The precise relation between zero divisors, units and division algebras is not covered here.

**Example (the quotient presentations of the number systems).** The complex, split complex and dual numbers are the quotients of a polynomial algebra by the principal ideals generated by $x^2 + 1$, $x^2 - 1$ and $x^2$ respectively:

$$
\mathbb{C} = \mathbb{R}[x]/(x^2+1), \qquad \mathbb{D} = \mathbb{R}[x]/(x^2-1), \qquad \mathbb{D}' = \mathbb{R}[x]/(x^2).
$$

In each case the quotient is generated as an $\mathbb{R}$-algebra by the image of $x$, whose square is $-1$, $+1$ and $0$ respectively. The quaternion algebra admits the analogous presentation by two generators and three relations,

$$
\mathbb{H} = \mathbb{R}\langle x, y \rangle / (x^2 + 1, y^2 + 1, xy + yx),
$$

where $\mathbb{R}\langle x, y \rangle$ is the free algebra on two generators, constructed. These presentations are the simplest instances of the general quotient construction, and they are worked out.

## Summary

A **subalgebra** is a submodule closed under the product; a **left**, **right** or **two-sided ideal** is a submodule closed under multiplication by the algebra on the left, on the right, or on both sides. Kernels of algebra homomorphisms are two-sided ideals and images are subalgebras; preimages of ideals are ideals. A two-sided ideal $I$ is exactly what is needed to form the quotient algebra $A/I$, whose product $(a+I)(b+I) = ab + I$ is well defined by bilinearity and by the closure of $I$.

The first isomorphism theorem gives $A/\ker\varphi \cong \operatorname{im}\varphi$, the second gives $(B+I)/I \cong B/(B\cap I)$ for a subalgebra $B$ and an ideal $I$, the third gives $(A/I)/(J/I) \cong A/J$ for ideals $I \subseteq J$, and the correspondence theorem identifies the ideals of $A/I$ with the ideals of $A$ containing $I$. A nonzero algebra is **simple** when it has no proper nonzero two-sided ideal, a proper ideal is **maximal** when nothing lies strictly between it and the algebra, and maximality is equivalent to simplicity of the quotient.

Associativity is not needed for any of this. It is needed only to multiply ideals — to make the span of the products $xy$, $x \in I$, $y \in J$ an ideal — and to describe a generated ideal by expressions $asb$. The quotient presentations $\mathbb{C} = \mathbb{R}[x]/(x^2+1)$, $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, $\mathbb{D}' = \mathbb{R}[x]/(x^2)$ and $\mathbb{H} = \mathbb{R}\langle x,y\rangle/(x^2+1, y^2+1, xy+yx)$ are the concrete output of the construction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $A$, $B$ | $R$-algebras |
| $I$, $J$ | Ideals (two-sided unless qualified) |
| $ax$, $xa$ | Left and right multiplication by $a$ |
| $(S)$, $\langle S \rangle$ | Two-sided ideal generated by $S$ |
| $I + J$, $I \cap J$, $IJ$ | Sum, intersection, product of ideals |
| $A/I$ | Quotient algebra by a two-sided ideal $I$ |
| $\pi : A \to A/I$ | Quotient map, $\ker\pi = I$ |
| $\varphi : A \to B$ | Algebra homomorphism |
| $\ker\varphi$, $\operatorname{im}\varphi$ | Kernel (an ideal) and image (a subalgebra) |
| $\operatorname{Aut}_R(A)$ | Group of $R$-algebra automorphisms of $A$ |
| $J(A)$ | Jacobson radical |
| $\mathbb{R}\langle x, y\rangle$ | Free algebra on two generators |
| $\mathbb{C} = \mathbb{R}[x]/(x^2+1)$ | Complex numbers as a quotient |
| $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$ | Split complex numbers as a quotient |
| $\mathbb{D}' = \mathbb{R}[x]/(x^2)$ | Dual numbers as a quotient |
| $\mathbb{H}$ | Quaternions as a quotient of the free algebra |





## Further Reading

- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for ideals, quotients and the isomorphism theorems in the general algebra setting.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the structure theory of algebras and their ideals.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the Jacobson radical and simplicity.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the full structure theory of associative algebras.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the ring-theoretic analogue of the isomorphism theorems.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for algebras over commutative rings and their quotients.
