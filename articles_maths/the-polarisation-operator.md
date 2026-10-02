# __The Polarisation Operator__

## Introduction

A symmetric multilinear map and a homogeneous polynomial map are two views of one object: from the multilinear map one takes its diagonal, and from the polynomial map one recovers the multilinear map by **polarisation**. For the Jordan product this is the familiar identity

$$
x \circ y = \tfrac12\bigl((x+y)^2 - x^2 - y^2\bigr),
$$

in which the bilinear product is rebuilt from the square of a single element; a Jordan algebra is what remains when the associative law is dropped from this reconstruction. The passage in the opposite direction, from a homogeneous map of degree $n$ to its polarising $n$-linear map, is carried by a single operator on the module of maps, the **polarisation operator**

$$
(\Pi f)(x_1, \dots, x_n) = \frac{1}{n!}\sum_{S \subseteq \{1,\dots,n\}}(-1)^{n-|S|}\, f\Bigl(\sum_{i \in S} x_i\Bigr),
$$

which is the $n$-fold difference at the origin, normalised. The article defines this operator, shows that it is the inverse of the diagonal map on symmetric multilinear maps, and identifies the operators it produces when applied to the square of a Jordan algebra: the Jordan product itself in degree two, the Jordan triple product in degree three, and the quadratic representation $U_{a,b}$ when the quadratic map polarised is $a\mapsto U_a$.

The article assumes *Jordan Algebras* for the product and the quadratic representation, *The Jordan Multiplication Operators* for the operator reading of the Jordan identity by polarisation, and *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System* for the ternary product. The polarisation of a **quadratic form**, where the map polarised is $x\mapsto q(x)$ and the result is the polar form, is settled in *Quadratic Forms and Polarisation* and is not restated here; the present article treats the polarisation of a general symmetric multilinear map and of a general homogeneous map, together with the operator that effects it. No form, no norm and no distance is used; the only hypothesis is that $n!$ be invertible, which is a statement about the ground ring. Throughout, $R$ is a commutative ring with identity $1 \neq 0$, $V$ and $W$ are $R$-modules, and the integer $n$ is fixed.

## The Polarisation of the Jordan Product

### The Square and the Product

Let $J$ be a Jordan $R$-algebra and let $f(x) = x^2 = x \circ x$ be its square. The square is a homogeneous map of degree two, and the identity

$$
(x+y)^2 = x^2 + 2\,x\circ y + y^2
$$

expands it; solving for the middle term gives the **polarisation identity**

$$
x \circ y = \tfrac12\bigl((x+y)^2 - x^2 - y^2\bigr).
$$

Thus the product is recovered from the square, and this is why the axioms of a Jordan algebra are stated as identities in the square alone: power associativity, flexibility (which is the commutativity of the product) and the Jordan identity all involve only the powers of an element and of sums of two elements. Polarising the Jordan identity in its operator form $[L_a, L_{a^2}] = 0$ gives the linearised and the cyclic forms recorded in *The Jordan Multiplication Operators*, and every such linearisation is an instance of the operator defined below.

### The Polarisation of the Cube

Polarising the cube $g(x) = x^3 = x\circ(x\circ x)$ in the two extra variables $y$ and $z$ gives the **Jordan triple product**

$$
\{x, y, z\} = (x\circ y)\circ z + (z\circ y)\circ x - (x\circ z)\circ y ,
$$

symmetric in its outer two variables, which is the ternary product of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*. In a special Jordan algebra $J = A^+$ with the halved product it is $\{x,y,z\} = \tfrac12(xyz + zyx)$, the symmetrisation of the associative triple product, and the identity of the two expressions is the computation of the quadratic representation below.

## The Polarisation Operator

### Definition

Let $f : V \to W$ be any map for which the expression makes sense, that is, any map to which addition and the scalar $1/n!$ apply; the polarised map

$$
\Pi f : V^n \longrightarrow W, \qquad
(\Pi f)(x_1,\dots,x_n) = \frac{1}{n!}\sum_{S \subseteq \{1,\dots,n\}}(-1)^{n-|S|}\,f\Bigl(\sum_{i\in S}x_i\Bigr)
$$

is defined whenever $n!$ is invertible in $R$. Its symmetry is immediate: the right-hand side is a sum over subsets $S$, and the permutation of the variables $x_i$ permutes the subsets and their complements' cardinalities, so $(\Pi f)(x_{\sigma(1)},\dots,x_{\sigma(n)}) = (\Pi f)(x_1,\dots,x_n)$ for every $\sigma \in S_n$. It is $R$-linear in $f$, and it is natural: for an $R$-linear map $u : W \to W'$ one has $\Pi(uf) = u(\Pi f)$.

**Proposition (the difference reading).** Let $\nabla_h f(x) = f(x+h) - f(x)$ be the difference operator in the direction $h$. Then

$$
(\Pi f)(x_1,\dots,x_n) = \frac1{n!}\,\bigl(\nabla_{x_1}\cdots\nabla_{x_n} f\bigr)(0) .
$$

*Proof.* Expanding the product of differences at $0$ gives $\sum_{S}(-1)^{n-|S|}f(\sum_{i\in S}x_i)$, with $S$ the set of the $x_i$'s that have been added, since each factor $\nabla_{x_i}$ either adds $x_i$ or does not, with the sign $+$ for not adding and $-$ after; the number of factors not added is $n-|S|$. Division by $n!$ gives the statement. $\square$

The proposition is the reason the polarisation operator is a **finite-difference operator**: it is the normalised top difference, and it measures the failure of $f$ to be of lower degree. In particular $\Pi f = 0$ for $f$ of degree $<n$ in the polynomial sense, and for $f$ of degree $n$ it returns the leading multilinear form.

### The Diagonal and the Inverse

Define the **diagonal** of a symmetric $n$-linear map $F : V^n \to W$ to be the homogeneous map of degree $n$

$$
\Delta F : V \longrightarrow W, \qquad \Delta F(x) = F(x, x, \dots, x),
$$

so that $\Delta(x\circ -)^{\ }$ is the square in degree two. The diagonal is $R$-linear in $F$ and injective, by the standard argument of *Quadratic Forms and Polarisation* for the case $n = 2$.

**Theorem.** For every symmetric $n$-linear $F$,

$$
\Pi \Delta F = F ,
$$

and for every homogeneous map $f$ of degree $n$ one has $\Delta\Pi f = f$ when $n!$ is invertible in $R$. Hence, in that case, $\Delta$ and $\Pi$ are mutually inverse isomorphisms

$$
\operatorname{Mult}^n(V; W) \ \underset{\Pi}{\overset{\Delta}{\rightleftarrows}}\ \operatorname{Pol}^n(V; W),
$$

between the symmetric $n$-linear maps and the homogeneous maps of degree $n$.

*Proof.* Let $F$ be symmetric $n$-linear. Substituting into the definition and expanding $F$ multilinearly gives, for a subset $S$, $F(\sum_{i\in S}x_i) = \sum_{j_1,\dots,j_n\in S}F(x_{j_1},\dots,x_{j_n})$. The coefficient of $F(x_{j_1},\dots,x_{j_n})$ with the $j$'s a permutation of $1,\dots,n$ is $\sum_{S \supseteq \{1,\dots,n\}}(-1)^{n-|S|} = 1$, taken over the one subset $S = \{1,\dots,n\}$, so the whole sum is $n!\,F(x_1,\dots,x_n)$ after using the symmetry of $F$ to collect the $n!$ orderings; hence $\Pi\Delta F = \tfrac1{n!}n!F = F$. For the second statement, if $f = \Delta F$ is homogeneous of degree $n$ then $\Pi f = \Pi\Delta F = F$ and $\Delta\Pi f = \Delta F = f$; a general homogeneous map of degree $n$ is of this form by definition. $\square$

**Corollary.** The polarisation operator is the inverse of the diagonal: on a homogeneous map of degree $n$ it produces the unique symmetric $n$-linear map whose diagonal is the map. In particular the passage is canonical, and the module of homogeneous maps of degree $n$ is isomorphic to the module of symmetric $n$-linear maps.

## The Operators Defined by Polarisation

### The Product and the Triple Product

For $n = 2$ the operator is $(\Pi f)(x,y) = \tfrac12(f(x+y) - f(x) - f(y))$. Applied to the square $f(x) = x^2$ of a Jordan algebra it returns the Jordan product,

$$
\Pi(x\mapsto x^2)(x,y) = \tfrac12\bigl((x+y)^2 - x^2 - y^2\bigr) = x \circ y ,
$$

which is the polarisation identity of the first section read as an operator statement.

For $n = 3$ the operator is

$$
(\Pi f)(x,y,z) = \tfrac16\bigl(f(x+y+z) - f(x+y) - f(x+z) - f(y+z) + f(x) + f(y) + f(z)\bigr),
$$

and applied to the cube $f(x) = x^3$ of a Jordan algebra it returns the Jordan triple product,

$$
\Pi(x\mapsto x^3)(x,y,z) = \{x,y,z\} ,
$$

the ternary product of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*. The verification is the expansion of $(x+y+z)^3$ in the special Jordan algebra generated by $x, y, z$, where $x\circ y = \tfrac12(xy+yx)$.

### The Quadratic Representation

The quadratic representation is the map $a \mapsto U_a$, quadratic on $J$ with values in the operators; its polarisation is

$$
\Pi(a \mapsto U_a)(a,b) = \tfrac12\bigl(U_{a+b} - U_a - U_b\bigr) = U_{a,b} ,
$$

which is the polarisation formula of *The Left and Right Multiplication Operators on a Jordan Algebra* and the source of the bilinear operator $U_{a,b}$. The same computation in the special case gives $U_{a,b}(x) = \tfrac12(axb + bxa)$ and, at $b = a$, $U_a(x) = axa$, so that the diagonal of the bilinear operator $U_{\cdot,\cdot}$ is the quadratic representation $U_a$ and the polarisation recovers the two-sided product from it. The triple product admits the same reading: the polarisation of the map $x\mapsto x^3$ can be written $\{x,y,z\} = U_{x,z}(y)$ when the product is special, which is the classical expression of the Jordan triple product through the quadratic representation.

### The Multiplication Operators from the Square

Each element $a$ of a Jordan algebra defines the multiplication operator $L_a(x) = a \circ x$, which is linear in the parameter $a$; polarising a linear map in degree two gives nothing, since $(\Pi g)(a,b) = \tfrac12(g(a+b)-g(a)-g(b))$ vanishes for an additive $g$. The one-sided multiplication operators are therefore not a polarised family, and the polarisation of the algebra produces instead the **product map**: the square $s(a) = a^2$ is the defining quadratic map, its polarisation is the bilinear product

$$
\Pi s(a,b) = a \circ b ,
$$

and the multiplication operator $L_a$ is that bilinear map with its first argument fixed, $L_a(b) = \Pi s(a,b)$. In the same way the quadratic representation $U_{a,b}$ is the polarisation of the quadratic family $a\mapsto U_a$, and the triple product is the polarisation of the cube. The rule is that polarisation applies to the **defining map** of the structure, which for a Jordan algebra is the square; the operators linear in a parameter carry no polarisation of their own.

## The Failure in Characteristic Two

**Remark.** The polarisation operator involves the scalar $1/n!$, and when $n!$ is not invertible in $R$ there is no such operator. The failure is not a matter of a missing inverse formula: symmetry fails to imply multilinearity in characteristic two, and the diagonal map $\Delta$ need not be injective. The standard example is the quadratic form $q(x) = \sum_i x_i^2$ over a field of characteristic two, whose polar form $\Pi q$ is zero although $q$ is not; the general failure of polarisation in characteristic two is the subject of *Quadratic Forms and Polarisation*, where the kernel of the polar map and the classification in characteristic two are given. For a Jordan algebra the same caveat applies to every polarisation: over a ring in which $2$ is not invertible, the identity $x\circ y = \tfrac12((x+y)^2 - x^2 - y^2)$ does not recover the product, and the theory must be stated in the square alone.

## Summary

The **polarisation operator** is

$$
(\Pi f)(x_1,\dots,x_n) = \frac1{n!}\sum_{S \subseteq \{1,\dots,n\}}(-1)^{n-|S|}f\Bigl(\sum_{i\in S}x_i\Bigr) = \frac1{n!}\,\nabla_{x_1}\cdots\nabla_{x_n}f(0) ,
$$

the normalised $n$-fold difference at the origin. It is symmetric, $R$-linear in $f$ and natural; it satisfies $\Pi\Delta F = F$ for every symmetric $n$-linear map $F$, and it inverts the diagonal $\Delta F(x) = F(x,\dots,x)$ on the homogeneous maps of degree $n$ whenever $n!$ is invertible in $R$. For a Jordan algebra it produces the product from the square, $\Pi(x\mapsto x^2)(x,y) = x\circ y$, the Jordan triple product from the cube, $\Pi(x\mapsto x^3) = \{x,y,z\}$, and the quadratic representation $U_{a,b}$ from the quadratic family $a\mapsto U_a$. Over a ring in which $2$ is not invertible the operator does not exist and polarisation fails, as in the characteristic-two theory of quadratic forms of *Quadratic Forms and Polarisation*. No form, norm or distance is involved; the operator is a purely algebraic finite difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $V, W$ | $R$-modules |
| $n$ | Fixed positive integer, the degree |
| $f$ | A map $V \to W$ to be polarised |
| $\Pi f$ | Polarisation of $f$, a symmetric $n$-linear map $V^n \to W$ |
| $\Delta F$ | Diagonal of a symmetric $n$-linear map, $\Delta F(x) = F(x,\dots,x)$ |
| $\nabla_h$ | Difference operator, $\nabla_hf(x) = f(x+h)-f(x)$ |
| $\operatorname{Mult}^n(V;W)$ | Symmetric $n$-linear maps $V^n \to W$ |
| $\operatorname{Pol}^n(V;W)$ | Homogeneous maps $V \to W$ of degree $n$ |
| $x\circ y = \tfrac12((x+y)^2 - x^2 - y^2)$ | Polarisation identity of the Jordan product |
| $\{x,y,z\}$ | Jordan triple product, polarisation of the cube |
| $U_{a,b} = \tfrac12(U_{a+b} - U_a - U_b)$ | Polarisation of the quadratic representation |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the polarisation of the Jordan product and of the quadratic representation.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan triple product and the quadratic representation.
- Nathan Jacobson, *Lectures in Abstract Algebra*, Vol. II: *Linear Algebra* (Van Nostrand, 1953), for the polarisation of a multilinear map from its diagonal over a ring of coefficients containing $1/n!$.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for symmetric multilinear maps, the diagonal and the finite-difference form of polarisation.
- Charles Jordan, *Calculus of Finite Differences*, 3rd ed. (Chelsea, 1965), for the difference operator $\nabla_h$ and the higher-difference formula.
