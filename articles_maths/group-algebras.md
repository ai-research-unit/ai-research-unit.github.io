
# __Group Algebras__

## Introduction

The group algebra $k[G]$ linearises a group: it is the $k$-algebra with $k$-basis the elements of $G$ and with multiplication the bilinear extension of the group law. It carries the group inside its unit group, it gives every representation of $G$ the structure of a module, and for a finite group over a field whose characteristic does not divide the order it decomposes into matrix algebras. This article develops the definition and the elementary structure, the regular representation, the augmentation ideal, the unit and zero-divisor theory, and the decomposition theory of finite groups, with the divisibility of the characteristic marking the boundary between the semisimple and the non-semisimple cases.

The ground ring is a field $k$ and the group $G$ is written multiplicatively with identity $1_G$; the finite case is the main one, and the infinite case is mentioned only where it differs.

## Definition and Basic Properties

**Definition.** The **group algebra** $k[G]$ is the set of formal finite sums

$$
\sum_{g \in G} a_g\, g, \qquad a_g \in k,
$$

with addition defined coefficientwise and multiplication defined by

$$
\Bigl(\sum_{g} a_g g\Bigr)\Bigl(\sum_{h} b_h h\Bigr) = \sum_{g,h} a_gb_h\, (gh).
$$

The elements of $G$ form a $k$-basis, so $\dim_k k[G] = |G|$ when $G$ is finite, and $k[G]$ is commutative if and only if $G$ is abelian.

**Proposition (elementary structure).** $k[G]$ is an associative $k$-algebra with unit $1_G$; the map $g \mapsto g$ embeds $G$ as a subgroup of the unit group $k[G]^\times$; and $k^\times \subseteq k[G]^\times$ sits in the centre as the scalar multiples of $1_G$.

*Proof.* Associativity of the product follows from associativity in $G$ and bilinearity, and the identity element is $1_G$ since $1_Gg = g1_G = g$. Each $g$ has inverse $g^{-1}$, so $G$ lies in the unit group, and the scalars $\lambda 1_G$ commute with every basis element and are invertible when $\lambda \neq 0$. $\square$

**Remark (the identification with convolution).** Writing an element as a function $a : G \to k$ of finite support, the product becomes the **convolution**

$$
(ab)(g) = \sum_{h \in G} a(h)\, b(h^{-1}g),
$$

and for finite $G$ the group algebra is the algebra of $k$-valued functions on $G$ with this product.

## The Regular Representation

**Definition.** The **left regular representation** is the action of $G$ on $k[G]$ by left multiplication, extended to an algebra map

$$
\lambda : k[G] \longrightarrow \operatorname{End}_k(k[G]), \qquad \lambda(x)(y) = xy .
$$

**Proposition.** $\lambda$ is an injective algebra homomorphism, so $k[G]$ is isomorphic to the subalgebra $\lambda(k[G])$ of $\operatorname{End}_k(k[G])$; for finite $G$ it is an isomorphism onto the algebra of all $k$-linear endomorphisms that commute with right multiplication by every element of $G$.

*Proof.* Injectivity: $k[G]$ is a free module with basis the group elements, and $\lambda(x) = 0$ implies $xg = 0$ for all $g$, hence $x = 0$. The commutant statement is standard: an endomorphism commuting with all right multiplications is determined by the image of $1_G$, which can be any element. $\square$

Every $k[G]$-module is thus a representation of $G$ by $k$-linear maps, and conversely; the group algebra is precisely the algebra whose module category is the representation category of $G$. This is the sense in which $k[G]$ linearises the group, and it is the reason the structure theory of representations is the structure theory of modules over $k[G]$.

**Theorem (the regular module).** For finite $G$ and $k = \mathbb{C}$, the left regular module $k[G]$ decomposes as

$$
\mathbb{C}[G] \cong \bigoplus_{\rho} V_\rho^{\oplus n_\rho},
$$

where $\rho$ runs over the irreducible complex representations, $V_\rho$ has dimension $n_\rho$, and each occurs with multiplicity equal to its dimension; comparing dimensions gives $\sum_\rho n_\rho^2 = |G|$.

*Proof.* This is the decomposition of the regular representation of a finite group; the multiplicity of an irreducible representation in the regular representation equals its dimension by the orthogonality relations. $\square$

## The Augmentation Ideal

**Definition.** The **augmentation map** is the algebra homomorphism

$$
\pi : k[G] \longrightarrow k, \qquad \pi\Bigl(\sum_g a_g g\Bigr) = \sum_g a_g ,
$$

and its kernel is the **augmentation ideal** $I(G) = \ker\pi$.

**Proposition.** $I(G)$ is a two-sided ideal of codimension $1$, generated as a left ideal — equivalently as a two-sided ideal — by the elements $g - 1_G$, $g \in G$. Moreover

$$
\frac{k[G]}{I(G)} \cong k, \qquad \frac{I(G)}{I(G)^2} \cong G^{\mathrm{ab}}\otimes_{\mathbb{Z}} k
$$

for finite $G$, where $G^{\mathrm{ab}} = G/[G,G]$ is the abelianisation.

*Proof.* That $\pi$ is an algebra homomorphism follows from $\pi(gh) = 1 = \pi(g)\pi(h)$. Every element of $I(G)$ is a combination $\sum_g a_g g$ with $\sum_g a_g = 0$, and

$$
\sum_g a_g g = \sum_g a_g (g - 1_G) + \Bigl(\sum_g a_g\Bigr)1_G = \sum_g a_g(g-1_G),
$$

so the $g - 1_G$ generate $I(G)$; the quotient statement is the first isomorphism theorem. The second identification is the standard computation of $I/I^2$ in terms of the abelianisation. $\square$

**Corollary.** If $G$ is a nontrivial finite group and $k$ has characteristic zero, then $I(G) \neq 0$ is a nontrivial ideal, so $k[G]$ is not simple; if in addition the characteristic does not divide $|G|$, then $k[G]$ is semisimple and $I(G)$ is a direct sum of matrix algebras.

## Units and Zero Divisors

**Proposition (units).** For any group $G$, the group $G$ and the scalars $k^\times$ lie in $k[G]^\times$, so $k^\times G \subseteq k[G]^\times$. The inclusion can be strict: for $k = \mathbb{R}$ and $G = \mathbb{Z}/2$ one has $\mathbb{R}[\mathbb{Z}/2] \cong \mathbb{R}\times\mathbb{R}$, whose units are the pairs with both entries nonzero, and $(1,2)$ is a unit of $\mathbb{R}\times\mathbb{R}$ lying outside $\mathbb{R}^\times G$, which consists of the pairs $(\lambda,\lambda)$ and $(\lambda,-\lambda)$.

*Proof.* The first statement is the proposition on elementary structure. For the second, the isomorphism $\mathbb{R}[\mathbb{Z}/2] \cong \mathbb{R}\times\mathbb{R}$ sends $1_G$ to $(1,1)$ and $g$ to $(1,-1)$, so the units are the pairs $(\lambda,\mu)$ with $\lambda\mu \neq 0$, while $\mathbb{R}^\times G$ consists of $\lambda(1,1)$ and $\lambda(1,-1)$; the pair $(1,2)$ is a unit outside that set. $\square$

**Proposition (zero divisors).** Let $g \in G$ have finite order $m \geq 2$. Then

$$
(1_G - g)\bigl(1_G + g + g^2 + \dots + g^{m-1}\bigr) = 1_G - g^m = 0,
$$

with both factors nonzero, so $1_G - g$ is a zero divisor and $k[G]$ is not a domain.

*Proof.* The product telescopes, and $g^m = e$; both factors are nonzero because $g \neq e$ and the group elements are linearly independent. $\square$

Thus the group algebra of a nontrivial finite group always has zero divisors, and it is a division algebra only in the trivial case $G = \{e\}$, where $k[G] \cong k$. This is the first place where the torsion of the group is visible in the algebra.

**Theorem (Maschke, standard).** If $G$ is finite and $\operatorname{char} k$ does not divide $|G|$, then $k[G]$ is semisimple. If $\operatorname{char} k$ divides $|G|$, then $k[G]$ is not semisimple and its radical contains the element $\sum_{g\in G} g$, which satisfies $g\bigl(\sum_h h\bigr) = \sum_h h$ for all $g$ and squares to $|G|\sum_h h = 0$.

*Proof (first part, standard).* Given a submodule $W \subseteq V$ of a $k[G]$-module, choose any $k$-linear projection $p : V \to W$ and average it over $G$:

$$
\tilde p(v) = \frac{1}{|G|}\sum_{g\in G} g\,p(g^{-1}v),
$$

which is $k[G]$-linear because the averaging is invariant under $G$, and which is still a projection onto $W$; hence every submodule is a direct summand. $\square$

**Example (characteristic two).** Let $k = \mathbb{F}_2$ and $G = \mathbb{Z}/2 = \{1_G, g\}$. Then $\operatorname{char} k = 2$ divides $|G| = 2$, and

$$
k[G] \cong \frac{\mathbb{F}_2[x]}{(x^2-1)} = \frac{\mathbb{F}_2[x]}{(x-1)^2} \cong \frac{\mathbb{F}_2[\varepsilon]}{(\varepsilon^2)},
$$

the algebra of dual numbers over $\mathbb{F}_2$, with $\varepsilon = x - 1$. It is local with nilpotent maximal ideal $(\varepsilon)$ and is not semisimple, in agreement with the failure of Maschke. In characteristic not $2$ the same group gives

$$
k[\mathbb{Z}/2] \cong \frac{k[x]}{(x^2-1)} \cong \frac{k[x]}{(x-1)}\times\frac{k[x]}{(x+1)} \cong k\times k,
$$

which over $k = \mathbb{R}$ is the split complex algebra $\mathbb{D}$.

## Finite Groups and the Decomposition

**Theorem (structure of a finite group algebra, standard).** Let $\operatorname{char} k$ not divide $|G|$. Then

$$
k[G] \cong \prod_{\rho} M_{n_\rho}(D_\rho),
$$

the product running over the irreducible representations of $G$ over $k$ and $D_\rho$ being the division algebra of endomorphisms of the corresponding simple module. Over an algebraically closed field, $D_\rho = k$ and

$$
k[G] \cong \prod_{\rho} M_{n_\rho}(k), \qquad |G| = \sum_\rho n_\rho^2 .
$$

*Proof.* By Maschke the algebra is semisimple, so the Wedderburn–Artin theorem applies and gives the product of matrix algebras over division algebras; over an algebraically closed field every finite-dimensional division algebra over $k$ is $k$, and the number of factors and their sizes come from the decomposition of the regular module. $\square$

**Corollary (the centre).** $\dim_k Z(k[G])$ equals the number of conjugacy classes of $G$; over an algebraically closed field, $\dim_k Z(k[G])$ equals the number of irreducible representations, and a basis is given by the **class sums**

$$
C_\chi = \sum_{g \in \chi} g,
$$

one for each conjugacy class $\chi$.

*Proof.* An element $\sum a_g g$ is central exactly when its coefficients are constant on conjugacy classes, as in *Centre, Units, Zero Divisors and Division Algebras*. $\square$

**Example (cyclic groups).** For $G = \mathbb{Z}/n$ generated by $g$, the group algebra is

$$
k[\mathbb{Z}/n] \cong \frac{k[x]}{(x^n-1)},
$$

and when $k$ contains a primitive $n$-th root of unity $\zeta$ and $\operatorname{char} k \nmid n$,

$$
k[\mathbb{Z}/n] \cong \prod_{j=0}^{n-1} \frac{k[x]}{(x - \zeta^j)} \cong k^n,
$$

a product of $n$ copies of $k$, corresponding to the $n$ one-dimensional representations. This is the polynomial-algebra description of the group algebra and specialises to the case $n = 2$ above.

**Example (the symmetric group $S_3$).** The complex group algebra has three irreducible representations, of dimensions $1, 1, 2$, so

$$
\mathbb{C}[S_3] \cong \mathbb{C}\times\mathbb{C}\times M_2(\mathbb{C}),
$$

of dimension $1+1+4 = 6 = |S_3|$; the centre is three-dimensional, matching the three conjugacy classes. The two-dimensional factor is the standard representation, and the two one-dimensional factors are the trivial representation and the sign representation.

**Remark (infinite groups).** For infinite $G$ the algebra $k[G]$ consists of finite sums and is generally non-Noetherian and not semisimple in the Artinian sense. For $G = \mathbb{Z}$ generated by $g$, $k[\mathbb{Z}] \cong k[x, x^{-1}]$, the Laurent polynomial algebra, which is a principal ideal domain and a doma, so an infinite torsion-free group can give a group algebra without zero divisors. The operator-algebraic completions of $k[G]$ for infinite $G$ are treated.

## Summary

The group algebra $k[G]$ has $k$-basis $G$, multiplication extending the group law, dimension $|G|$ for finite $G$, unit $1_G$, and unit group containing $G$ and $k^\times$; it is commutative exactly when $G$ is abelian, and its product is convolution of finitely supported functions. The **left regular representation** identifies $k[G]$ with an algebra of endomorphisms and makes $k[G]$-modules the same thing as representations of $G$. The **augmentation map** $\pi\bigl(\sum a_g g\bigr) = \sum a_g$ has kernel the **augmentation ideal** $I(G)$, generated by the elements $g - 1_G$, with $k[G]/I(G) \cong k$ and $I/I^2 \cong G^{\mathrm{ab}}\otimes_\mathbb{Z} k$. A group element of finite order $m \geq 2$ gives the zero-divisor pair $(1_G-g)(1_G+g+\dots+g^{m-1}) = 0$, so the group algebra of a nontrivial finite group is never a domain. If $\operatorname{char} k \nmid |G|$, **Maschke's theorem** makes $k[G]$ semisimple and $k[G] \cong \prod_\rho M_{n_\rho}(D_\rho)$, over an algebraically closed field $k[G]\cong\prod_\rho M_{n_\rho}(k)$ with $\sum_\rho n_\rho^2 = |G|$; if the characteristic divides $|G|$ the algebra is not semisimple, as $\mathbb{F}_2[\mathbb{Z}/2] \cong \mathbb{F}_2[\varepsilon]/(\varepsilon^2)$ shows. The centre is spanned by the class sums and has dimension the number of conjugacy classes, and $k[\mathbb{Z}/n] \cong k[x]/(x^n-1)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k[G]$ | Group algebra of $G$ over $k$ |
| $1_G$ | Identity of $G$ and of $k[G]$ |
| $\dim_k k[G] = \lvert G\rvert$ | Dimension for finite $G$ |
| $\lambda$ | Left regular representation |
| $\pi$ | Augmentation map, $\pi(g) = 1$ |
| $I(G) = \ker\pi$ | Augmentation ideal |
| $G^{\mathrm{ab}} = G/[G,G]$ | Abelianisation |
| $M_{n_\rho}(D_\rho)$ | Wedderburn factors, $n_\rho$ the representation degrees |
| $C_\chi$ | Class sum over the conjugacy class $\chi$ |
| $\operatorname{char} k$ | Characteristic of $k$ |
| $k[x,x^{-1}]$ | Laurent polynomial algebra $\cong k[\mathbb{Z}]$ |



## Further Reading

- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the group algebra and its decomposition.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the regular representation, the orthogonality relations and $\sum n_\rho^2 = |G|$.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Dover, 1994), for the class sums, the centre and the number of irreducible representations.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Wedderburn–Artin decomposition of a semisimple algebra.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the augmentation ideal, the units and the infinite-group case.
