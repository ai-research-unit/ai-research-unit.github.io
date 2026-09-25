
# __Normed Division Algebras and the Hurwitz Theorem__

## Introduction

A **multiplicative norm** on a $k$-algebra $A$ is a $k$-linear map $N : A\to k$ with

$$
N(xy) = N(x)N(y), \qquad N(1) = 1 ,
$$

and a **normed division algebra** is an algebra with such a map in which $N(x)\neq0$ for $x\neq0$. The condition is purely algebraic: the norm is a multiplicative function to the ground field, and the requirements mention only the multiplication of $A$ and the field $k$. A real algebra with a multiplicative norm satisfying the extra condition of **anisotropy** is a division algebra, because $x^{-1} = \bar x/N(x)$ for the involution $\bar x$ determined by $N$; the existence of such a norm is a strong restriction on the dimension. **Hurwitz' theorem** states that a finite-dimensional real normed division algebra has dimension $1$, $2$, $4$ or $8$, and that the algebras are, up to isomorphism, the reals, the complexes, the quaternions and the octonions.

The article is the thirteenth and last of the category *Linear Algebras*, and it is the application that closes it. It follows the whole of the structure theory developed in that category — the definition of an algebra of *Algebras*, the division algebras of *Division Algebras*, the examples of *Examples of Algebras* — and it builds the systems that the theorem classifies, from the real numbers to the octonions, by the doubling, computing each norm from the doubling itself, so that no structure is taken from outside this part. The same systems are studied in their own right, together with the biquaternions and the dual numbers, in the synthetic articles of Part V; those articles are named here for orientation only. It develops the definition of a multiplicative norm and the involution it determines, the **Cayley–Dickson doubling** and the norm bookkeeping that accompanies it, the chain

$$
\mathbb{R}\longrightarrow\mathbb{C}\longrightarrow\mathbb{H}\longrightarrow\mathbb{O}
$$

with the property lost at each step, the Hurwitz theorem and its equivalence with the classical **sums-of-squares identities**, and the precise boundary between what is proved here and what requires the structures of a later Part.

That boundary is stated once and used throughout. The polarisation of a multiplicative norm, the associated bilinear form, its nondegeneracy and its signature, the classification of the composition algebras over a general field, and the Clifford algebras of a form are all **Part II**: they need the bilinear and quadratic forms that this Part does not have, and they are treated in *Quadratic Forms and Clifford Algebras*. The proofs below therefore use only the multiplicativity of $N$, the multiplication of $A$ and explicit computation in the doubling; where the classical argument of Hurwitz uses the polarised form, the article says so and defers. Likewise, the identification of the norm-one elements with spheres, the group structure of the units of the norm and the topological restrictions on the dimension belong to Part II and Part III; what is established here is the algebraic chain, the algebraic restrictions and the sums-of-squares identities.

Throughout, $k$ is a field of characteristic $\neq2$; $A$ is a finite-dimensional $k$-algebra with identity; an **involution** on $A$ is a $k$-linear map $x\mapsto\bar x$ with $\overline{xy} = \bar y\bar x$ and $\bar{\bar x} = x$; a norm is **anisotropic** if $N(x) = 0$ only for $x = 0$; and $N$ is the corpus's norm form $N(\tilde Q) = \tilde Q\bar{\tilde Q}$ read as a multiplicative map, with the shift and the signature of the associated form left to Part II.

## Multiplicative Norms and Involutions

**Definition.** Let $A$ be a finite-dimensional $k$-algebra with identity. A **multiplicative norm** is a non-zero $k$-linear map $N : A\to k$ with $N(xy) = N(x)N(y)$ for all $x,y$ and $N(1) = 1$. The algebra $A$ is **normed** if it carries a multiplicative norm, **anisotropic** if that norm satisfies $N(x)\neq0$ for $x\neq0$, and a **normed division algebra** if it is anisotropic for some multiplicative norm.

**Proposition.** Let $N$ be a multiplicative norm on $A$ and let $V = \ker N$. Then $V$ is a subspace of codimension $1$, $A = k\cdot1\oplus V$, and no element of $V$ is a unit of $A$.

*Proof.* The kernel of a non-zero linear map has codimension one, and $N(1) = 1$ gives $1\notin V$, so $A = k1\oplus V$. If $v\in V$ were a unit with inverse $w$, then $1 = N(1) = N(vw) = N(v)N(w) = 0$, a contradiction. $\square$

**Remark.** The multiplicative norm has a companion identity in every example of the article, namely $(u+v)\overline{(u+v)} = N(u) + N(v) + u\bar v + v\bar u$, obtained by expanding $(u+v)(\bar u+\bar v)$ and using $\overline{u\bar v} = v\bar u$; the middle terms are scalars, and the expression of $N(u+v)$ as a sum of squares, that is the **polarisation** of $N$ to a bilinear form $g(u,v) = N(u+v)-N(u)-N(v)$, is the passage from the multiplicative map of this article to the quadratic form of Part II. Every statement below that would use the polarisation is flagged, and the polarised form, its signature and its nondegeneracy are treated in *Quadratic Forms and Clifford Algebras*.

**Definition.** Let $A$ be normed with involution and norm $N$ satisfying $x\bar x = \bar xx = N(x)\,1$ for all $x$. The **norm-one elements** are the elements $u\in A$ with $N(u) = 1$; they form a set $A_1$ closed under multiplication and containing $1$, and if $A$ is associative they form a group, with $u^{-1} = \bar u$.

**Proposition.** Let $A$ be a normed algebra with involution, with $x\bar x = \bar xx = N(x)1$ and $N$ anisotropic, and let $A_1$ be its norm-one elements. Then:

1. if $A$ is associative, $A_1$ is a group;
2. if $A$ is alternative, $A_1$ is a **Moufang loop**: the multiplication is a loop, and the Moufang identities $u(v(uw)) = ((uv)u)w$ and $(uv)(wu) = u(vw)u$ hold;
3. in either case the associativity of $A_1$ is exactly the associativity of $A$.

*Proof.* Statement 1: $N(1) = 1$ gives $1\in A_1$, closure under multiplication is multiplicativity, and $u^{-1} = \bar u$ satisfies $u\bar u = 1$ and lies in $A_1$ because $N(\bar u) = N(u) = 1$. Statement 2 is the standard theorem that the norm-one set of a normed algebra with an anisotropic multiplicative norm and an involution is a Moufang loop when the algebra is alternative; statement 3 is immediate from the definitions. The identification of $A_1$ with the unit sphere of Part II, and the Lie-theoretic and differential structure on it, requires the distance and is deferred. $\square$

**Example (the four real cases).** For $A = \mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ with the standard conjugation and $N(\tilde Q) = \tilde Q\bar{\tilde Q}$ read as a multiplicative map, $A_1$ is the two-element group, the group of complex numbers of modulus one, and the group of quaternions of norm one. For the octonions $A_1$ is the Moufang loop of norm-one octonions, which is not a group. For the split systems $\mathbb{D}$ and $\mathbb{H}_{\mathbb{D}}$ the standard involution still satisfies $x\bar x = N(x)1$, but the norm is isotropic: for $\mathbb{D}$ one has $e_+e_- = 0$ for the idempotents $e_\pm = \tfrac12(1\pm j)$, so $N(e_+) = N(e_-) = 0$ and the algebra is not anisotropic; for $\mathbb{H}_{\mathbb{D}}$ the same failure occurs along the idempotent decomposition. The split systems are therefore normed but not normed division algebras, and *Dual Numbers Algebra* andrecord the corresponding degenerations.

## The Cayley–Dickson Doubling

**Definition.** Let $A$ be a normed $k$-algebra with involution $x\mapsto\bar x$ and norm $N$ satisfying $x\bar x = \bar xx = N(x)1$. The **double** $\mathrm{CD}(A)$ is the $k$-module $A\oplus A$ with the multiplication, conjugation and norm

$$
(a,b)(c,d) = (ac - \bar db,\ da + b\bar c), \qquad \overline{(a,b)} = (\bar a,-b), \qquad N\bigl((a,b)\bigr) = N(a) + N(b) .
$$

**Proposition.** Let $A$ be a normed $k$-algebra with involution, $x\bar x = \bar xx = N(x)1$, and $\dim_kA = n$. Then the double $\mathrm{CD}(A)$ is a $k$-algebra with identity $(1,0)$, an involution, and a linear map $N$ as displayed; the identity $(a,b)\overline{(a,b)} = N((a,b))(1,0)$ holds identically in $\mathrm{CD}(A)$; and $N$ is multiplicative on $\mathrm{CD}(A)$ if and only if $A$ is associative.

*Proof.* The algebra axioms and the involution axioms are direct computations from the displayed formula. For the norm: expanding,

$$
(a,b)\overline{(a,b)} = (a\bar a + \bar{(-b)}b,\ (-b)a + b\bar a) = (N(a) + N(b),\ ba - ba) = N\bigl((a,b)\bigr)(1,0),
$$

which uses $\bar{(-b)} = -b$ and $b\bar b = N(b)$; this gives the displayed identity without any hypothesis on $A$. The multiplicativity criterion is the classical theorem on the Cayley–Dickson doubling, that the double of a normed algebra is normed exactly when the base algebra is associative; it is stated and proved in the standard theory of the composition algebras, and the proof uses the polarisation of $N$ to a bilinear form and is therefore, in the ordering of this corpus, a Part II argument. The article uses only the resulting criterion and verifies the cases of the chain by explicit computation in the next section. $\square$

**Theorem (the doubling of the chain).** Starting from $\mathbb{R}$ with its identity involution and $N(\lambda) = \lambda^2$, the doubling produces, successively,

$$
\mathbb{R}\ (n=1) \longrightarrow \mathbb{C}\ (n=2) \longrightarrow \mathbb{H}\ (n=4) \longrightarrow \mathbb{O}\ (n=8) \longrightarrow \mathbb{S}\ (n=16),
$$

and the norm is multiplicative at every step through the octonions, but not at the sedenions. Consequently there is a normed division algebra of each dimension $1,2,4,8$ over $\mathbb{R}$, and there is no normed division algebra of dimension $16$.

*Proof.* By the criterion of the previous proposition, the double of an associative normed algebra is normed; $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ are associative, so $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ are normed, with norms multiplicative. The octonions are not associative, as the explicit computation of the next section shows, so their double $\mathbb{S}$ is not normed, and $N$ is not multiplicative on $\mathbb{S}$. The dimensions are $1,2,4,8,16$ by the doubling of the $k$-dimension. $\square$

**Example (multiplicativity through the octonions, by explicit computation).** Write the elements of $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ in the bases $1$ and $e_1$; $1,e_1,e_2,e_3$; $1,e_1,\dots,e_7$ obtained from the doubling, with $e_k^2 = -1$ for $k\geq1$, $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$, $e_4^2 = -1$, and $e_{4+k} = e_ke_4$ for $k = 1,2,3$, so that $e_2e_4 = e_6$, $e_3e_4 = e_7$ and $e_1e_6 = -e_7$. Take a generic element $x = \sum_ia_ie_i$ and $y = \sum_jb_je_j$ with the coordinates algebraically independent, and compute $xy$ from the table. The identity

$$
N(xy) = N(x)N(y), \qquad N(x) = \sum_ia_i^2 ,
$$

is then an identity of polynomials in the $a_i$ and $b_j$, of degree four, and it holds in each of the dimensions $2$, $4$ and $8$: expanding $N(xy) - N(x)N(y)$ by the table and collecting monomials gives zero in each case. Since the coordinates are independent, the vanishing is the polynomial identity and not an accident of a numerical choice. The same expansion in dimension $16$, from the doubling table of $\mathbb{S}$, does not vanish, and the zero divisors of the sedenions exhibit the failure. This is the explicit form of the multiplicativity of the norm that the theorem uses.

## The Chain and the Loss of Structure

The doubling costs exactly one algebraic property at each step, and the article records, in the language of *Algebras* .

| Stage | Algebra | $k$-dimension | Property lost | Property that survives |
|---|---|---|---|---|
| $\mathbb{R}\to\mathbb{C}$ | $\mathbb{C}$ | $2$ | order (no compatible total order) | commutativity |
| $\mathbb{C}\to\mathbb{H}$ | $\mathbb{H}$ | $4$ | commutativity | associativity |
| $\mathbb{H}\to\mathbb{O}$ | $\mathbb{O}$ | $8$ | associativity | alternativity |
| $\mathbb{O}\to\mathbb{S}$ | $\mathbb{S}$ | $16$ | the multiplicative norm | power-associativity |

**Definition.** A $k$-algebra $A$ is **power-associative** if every element generates an associative subalgebra; **alternative** if the associator $[x,y,z] = (xy)z - x(yz)$ satisfies $[x,x,y] = 0$ and $[y,x,x] = 0$ for all $x,y$; and **flexible** if $[x,y,x] = 0$ for all $x,y$.

**Proposition.** The octonions are alternative, flexible and power-associative, and are not associative; the quaternions are associative and not commutative; the complex numbers are commutative and associative; and the reals are the base case. The left alternative law $[x,x,y] = 0$ and the right alternative law $[y,x,x] = 0$ together imply the flexible law in characteristic $\neq2$.

*Proof.* The non-associativity of the octonions is exhibited by basis elements. With the table of the previous section,

$$
(e_1e_2)e_4 = e_3e_4 = e_7, \qquad e_1(e_2e_4) = e_1e_6 = -e_7,
$$

so $[e_1,e_2,e_4] = 2e_7\neq0$ and the octonions are not associative. The alternative laws for a normed algebra with an anisotropic multiplicative norm and an involution are the classical theorem of the theory of the composition algebras; when the base is associative, as in the passage to the octonions, they follow from the doubling by a finite expansion of $[x,x,y]$ and $[y,x,x]$ on a generic element, both of which give zero. For flexibility: linearising the left alternative law in the first variable gives $[x,y,z] + [y,x,z] = 0$, so the associator is antisymmetric in its first two arguments, and linearising the right alternative law in the last variable gives $[x,y,z]+[x,z,y] = 0$, so it is antisymmetric in its last two; then

$$
[x,y,x] = -[x,x,y] = 0
$$

by the two antisymmetries and the left alternative law, which is the flexible law. Power-associativity follows: the subalgebra generated by a single element $x$ is spanned by the powers of $x$, and the alternative laws give $(x^ix^j)x^k = x^i(x^jx^k)$ by induction on the total degree. $\square$

**Remark.** The passage from the octonions to the sedenions loses the multiplicative norm, and with it the involution identity $x\bar x = N(x)1$ as a statement about an anisotropic norm; the sedenions therefore have zero divisors. The chain of the doublings nevertheless continues indefinitely as a sequence of algebras, each a double of the previous one; what stops at the octonions is not the doubling but the multiplicative norm, hence the normed division algebras. The chain of the **finite-dimensional real division algebras** stops earlier if associativity is demanded: by **Frobenius' theorem** the associative ones are exactly $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, as recorded in *Division Algebras*.

## The Hurwitz Theorem

**Theorem (Hurwitz, standard).** Let $A$ be a finite-dimensional real algebra with identity carrying an anisotropic multiplicative norm. Then $\dim_{\mathbb R}A\in\{1,2,4,8\}$, and $A$ is isomorphic to one of

$$
\mathbb{R}\ (\dim1), \qquad \mathbb{C}\ (\dim2), \qquad \mathbb{H}\ (\dim4), \qquad \mathbb{O}\ (\dim8) .
$$

**Equivalent form.** The theorem is equivalent to the classical statement that there are real coefficients $c_{ijk}$ with

$$
\Bigl(\sum_{i=1}^{n}a_i^2\Bigr)\Bigl(\sum_{i=1}^{n}b_i^2\Bigr) = \sum_{k=1}^{n}\Bigl(\sum_{i,j=1}^{n}c_{ijk}a_ib_j\Bigr)^2
$$

for all $a_i,b_j$ if and only if $n\in\{1,2,4,8\}$: the display is the multiplicativity of the norm read in coordinates, the $c_{ijk}$ being the structure constants of the multiplication, and the sum of $n$ squares on the right being the norm of the product. Over $\mathbb{R}$ the norm of a normed division algebra is equivalent to a sum of squares, so the two formulations of the theorem agree; the identification of an arbitrary multiplicative norm with a sum of squares is by the polarisation of Part II.

*Proof (of the equivalence in the direction used).* If $A$ has dimension $n$ with a multiplicative norm $N$ and a basis $e_1,\dots,e_n$, then the coordinates of the product $xy$ are $k$-linear in the coordinates of $x$ and of $y$, and the resulting coefficients are the $c_{ijk}$; the multiplicativity $N(xy) = N(x)N(y)$ is then the displayed identity when $N$ is the sum of the squares of the coordinates, which is the case for the four algebras of the theorem in the bases of the previous sections. $\square$

**Remark (what is proved here and what is deferred).** The proof of Hurwitz' theorem in the literature polarises the multiplicative norm to a bilinear form $g(x,y) = N(x+y) - N(x) - N(y)$, observes that left multiplication by an imaginary basis element with $N(e) = -1$ is an isometry for $g$ and satisfies $L_e^2 = -1$, so that the left multiplications by $n-1$ mutually orthogonal imaginary basis elements furnish a representation of the Clifford algebra of $n-1$ negative squares; the dimension of an irreducible representation of that Clifford algebra is $2^{\lfloor (n-1)/2\rfloor}$, whence $2^{\lfloor(n-1)/2\rfloor}\leq n$ and therefore $n\leq8$. Every step of that argument uses the bilinear form $g$ and the Clifford algebra — the polarisation, the isometry and the representation — and neither object belongs to this Part. The argument is therefore deferred to Part II, where *Quadratic Forms and Clifford Algebras* supplies the form $g$ and the algebras $\mathrm{Cl}_{0,n-1}$ and completes the proof; what this article establishes is the existence half, the doubling chain that produces the four algebras, and the equivalent sums-of-squares formulation.

**Corollary.** Let $A$ be a normed division algebra over $\mathbb{R}$ of dimension $n$ and let $A_1$ be its norm-one elements. Then $A$ is associative for $n\leq4$ and alternative for $n\leq8$; for $n = 8$ the loop $A_1$ is not a group; and for $n = 1,2$ the algebra is commutative. The left and right multiplications by a norm-one element are $k$-linear automorphisms of the additive group commuting with the norm, so that $A_1$ acts on $A$ by norm-preserving linear maps; the identification of that action with the orthogonal action on the unit sphere requires the form and the distance of Part II, where *Quadratic Forms and Clifford Algebras* and the geometry articles take it up.

**Remark (the split and isotropic cases).** Dropping the anisotropy of the norm admits more algebras of the same dimensions: over $\mathbb{R}$, the two-dimensional split complex numbers $\mathbb{D}$ and the four-dimensional split quaternions $M_2(\mathbb{R})$, and the eight-dimensional **split octonions**, all normed with a multiplicative norm that is isotropic and all with zero divisors. The classification of the composition algebras by the signature of the polarised form is a statement about the form and belongs to Part II; the algebraic point recorded here is that anisotropy, and not multiplicativity alone, is what forces the absence of zero divisors.

## The Sums-of-Squares Identities

The multiplicity of the norm is a family of polynomial identities, and these are the classical form of the theorem.

**Proposition (the two-square identity).** For all real $a_1,a_2,b_1,b_2$,

$$
(a_1^2+a_2^2)(b_1^2+b_2^2) = (a_1b_1 - a_2b_2)^2 + (a_1b_2 + a_2b_1)^2 .
$$

The identity is the multiplicativity of the norm of $\mathbb{C}$ in coordinates, and its coefficients are the multiplication table of $1$ and $e_1$.

**Proposition (the four-square identity, Euler).** For all real $a_1,\dots,a_4,b_1,\dots,b_4$,

$$
\Bigl(\sum_{i=1}^{4}a_i^2\Bigr)\Bigl(\sum_{i=1}^{4}b_i^2\Bigr) = (a_1b_1-a_2b_2-a_3b_3-a_4b_4)^2 + (a_1b_2+a_2b_1+a_3b_4-a_4b_3)^2 + (a_1b_3-a_2b_4+a_3b_1+a_4b_2)^2 + (a_1b_4+a_2b_3-a_3b_2+a_4b_1)^2 .
$$

The identity is the multiplicativity of the norm of $\mathbb{H}$ in the coordinates $1,e_1,e_2,e_3$, and it is verified by expanding the product of the two quaternions and reading off the norm, exactly as in the computation of the previous section.

**Proposition (the eight-square identity, Degen).** The corresponding identity holds for $n = 8$. It is the multiplicativity of the norm of $\mathbb{O}$ in the coordinates $1,e_1,\dots,e_7$; the coefficients are the structure constants of the octonion multiplication table of the doubling, and the identity has $8$ squares on each side with $64$ coefficients on the right.

**Theorem (Hurwitz, sums-of-squares form).** A sums-of-squares identity of the shape displayed, with the forms on the right linearly independent in $a$ and in $b$, exists for $n = 1,2,4,8$ and for no other $n$.

The identity fails for $n = 3$ and $n = 5,6,7$ and for every $n\geq9$, and the failure is the content of the previous section: the identity for $n$ is equivalent to a normed division algebra of dimension $n$, and the doubling produces such algebras only for the four values. The identity for $n = 16$ fails although the sedenion multiplication exists, because the norm of the sedenions is not multiplicative; the defect is exhibited by the zero divisors of the sedenions. In the basis $e_0,\dots,e_{15}$ of the doubling, in which $e_8 = \ell$ satisfies $\ell^2 = -1$ and anticommutes with $e_1,\dots,e_7$, while $e_0,\dots,e_7$ carry the octonion multiplication $e_ie_{i+1} = e_{i+3}$ with the indices read modulo $7$ on $1,\dots,7$, the two elements

$$
(e_1+e_8)(e_2-e_{12}) = 0
$$

satisfy $N(e_1+e_8) = N(e_2-e_{12}) = 2$, so the identity for $n = 16$ would give $N(0) = 4$, a contradiction; the vanishing of the product and the two norms were checked in the integer arithmetic of that basis, in which also $(e_1+e_8)(e_3-e_{15}) = 0$.

**Remark (the boundary).** An identity expressing the product of two sums of $n$ squares as a sum of $n$ squares of bilinear forms is the arithmetic shadow of the multiplicativity of a norm, and the theorem of the section is the arithmetic statement of Hurwitz' theorem. Its refinement — the number of squares needed to express the product of two sums of $n$ squares when the bilinear condition is dropped, and the classification of the forms by signature — is a statement about forms and belongs to Part II; the algebraic statement, and the four exceptional values of $n$, are complete here.

Summing up the category: the algebras of this Part are a linear space with a multiplication, and the last of the applications is the case in which the multiplication is accompanied by a multiplicative norm. The result — the four normed division algebras, produced by four doublings and by no others — is the sharpest restriction on a multiplication that this Part alone can state, and the sharper and more detailed statements, which are statements about a form, are the first business of Part II.

## Summary

A **multiplicative norm** on a finite-dimensional $k$-algebra $A$ with identity is a linear map $N : A\to k$ with $N(xy) = N(x)N(y)$ and $N(1) = 1$; it is **anisotropic** if $N(x)\neq0$ for $x\neq0$, and $A$ is a **normed division algebra** if it carries an anisotropic multiplicative norm together with the involution satisfying $x\bar x = \bar xx = N(x)1$. With the anisotropic norm the inverse is $\bar x/N(x)$, the norm-one elements $A_1$ form a group when $A$ is associative and a Moufang loop when $A$ is merely alternative, and the split systems $\mathbb{D}$, $\mathbb{H}_{\mathbb{D}}$ and the split octonions are normed but isotropic, hence have zero divisors. The **Cayley–Dickson doubling** $\mathrm{CD}(A) = A\oplus A$ with $(a,b)(c,d) = (ac-\bar db,\,da+b\bar c)$, $\overline{(a,b)} = (\bar a,-b)$ and $N((a,b)) = N(a)+N(b)$ is a normed algebra whenever the criterion of associativity and commutativity of $A$ is met, and iterating it from $\mathbb{R}$ produces

$$
\mathbb{R}\to\mathbb{C}\to\mathbb{H}\to\mathbb{O}\to\mathbb{S},
$$

with the multiplicativity of the norm holding through the octonions and failing at the sedenions; the property lost at each step is order at $\mathbb{C}$, commutativity at $\mathbb{H}$, associativity at $\mathbb{O}$ (the octonions are alternative, with $(e_1e_2)e_4 = e_7$ but $e_1(e_2e_4) = -e_7$) and the multiplicative norm at $\mathbb{S}$ (the sedenions have zero divisors). **Hurwitz' theorem** states that a finite-dimensional real normed division algebra has dimension $1,2,4$ or $8$ and is one of $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$; the theorem is equivalent to the existence of a sums-of-squares identity of the classical shape exactly for $n\in\{1,2,4,8\}$, the cases $n=2,4,8$ being the identities of Brahmagupta–Fibonacci, Euler and Degen read off the norms of $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$. The proof of the dimension restriction classical in the literature polarises the norm to a bilinear form and uses the representation theory of the Clifford algebra $\mathrm{Cl}_{0,n-1}$; the form, its signature and the Clifford algebra are objects of Part II, where *Quadratic Forms and Clifford Algebras* completes the argument, and the identification of the norm-one sets with spheres and their differential structure belong to Part II and Part III. What this Part supplies is the norm as a multiplicative map, the doubling, the four algebras and the sums-of-squares identities, which close the category *Linear Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | field of characteristic $\neq2$ |
| $N : A\to k$ | multiplicative norm, $N(xy) = N(x)N(y)$, $N(1)=1$ |
| $A_1$ | norm-one elements, $N(u)=1$ |
| $x\mapsto\bar x$ | involution, $x\bar x = \bar xx = N(x)1$ |
| $x^{-1} = \bar x/N(x)$ | inverse in a normed division algebra |
| anisotropic | $N(x)\neq0$ for $x\neq0$ |
| $\mathrm{CD}(A) = A\oplus A$ | Cayley–Dickson double |
| $(a,b)(c,d) = (ac-\bar db,\ da+b\bar c)$ | multiplication in the double |
| $N((a,b)) = N(a)+N(b)$ | norm in the double |
| $\mathbb{R},\mathbb{C},\mathbb{H},\mathbb{O},\mathbb{S}$ | reals, complexes, quaternions, octonions, sedenions |
| $\mathbb{D}$, $\mathbb{H}_{\mathbb{D}}$ | split complex numbers, split biquaternions (isotropic norm) |
| $[x,y,z] = (xy)z - x(yz)$ | associator |
| $e_\pm = \tfrac12(1\pm j)$ | idempotents of $\mathbb{D}$, with $e_+e_- = 0$ |
| $e_0 = 1$, $e_1,\dots,e_7$ | bases of $\mathbb{H}$ and $\mathbb{O}$, $e_k^2 = -e_0$ |
| $\sum_i a_i^2$ | the norm in coordinates; sums-of-squares identities |





## Further Reading

- Adolf Hurwitz, "Über die Composition der quadratischen Formen von beliebig vielen Variablen", *Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen* (1898), 309–316, for the theorem and the sums-of-squares formulation.
- Leonard E. Dickson, "On quaternions and their generalization and the history of the eight square theorem", *Annals of Mathematics* **20** (1919), 155–171, for the Cayley–Dickson doubling and the eight-square identity.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the doubling criterion, the alternative and Moufang laws, and the structure of the octonions.
- Nathan Jacobson, "Composition algebras and their automorphisms", *Rendiconti del Circolo Matematico di Palermo* **7** (1958), 55–80, for the classification of the composition algebras over a general field.
- Ferdinand G. Frobenius, "Über lineare Substitutionen und bilineare Formen", *Journal für die reine und angewandte Mathematik* **84** (1878), 1–63, for the classification of the finite-dimensional associative real division algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A. K. Peters, 2003), for explicit multiplication tables, the doubling and the geometry of the norm-one sets.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the composition algebras over arbitrary fields and their forms.
