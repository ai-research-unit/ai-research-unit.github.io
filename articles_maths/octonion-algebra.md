
# __Octonion Algebra__

## Introduction

This article is the algebra slot of the octonion system. It constructs the octonion algebra $\mathbb{O}$, fixes its multiplication table and its standard conventions, develops the identities that survive the loss of associativity, and states the place the octonions occupy among the finite-dimensional real division algebras. The article is the octonion entry of the ladder that Part V traverses one number system at a time, and it is the first of the ten octonion articles of this Part; the norm form and the invertibility it governs are the subject, and the present article introduces only what the multiplication itself requires.

The article assumes the construction of the real division algebras from the general theory of *Division Algebras*, and the quaternion algebra $\mathbb{H}$ with its basis $e_0 = 1, e_1, e_2, e_3$, its multiplication and its conjugation, from *Quaternion Algebra*; the octonions are the Cayley–Dickson double of $\mathbb{H}$ in the same sense in which $\mathbb{H}$ is the double of $\mathbb{C}$. The basic facts about non-associative algebras — that the associator measures the failure of associativity, that a subalgebra is a subspace closed under multiplication, and that a unit is a two-sided identity — are used in their standard sense; the corpus's general theory of algebras is the Part I companion *Algebras: A General Introduction*. The composition algebras over a field and their norm forms are the subject of *Quadratic Forms over Algebras and Norm Forms*. No structure from the other articles of this category is used.

**Conventions.** The base field is $\mathbb{R}$ throughout; the octonions are a real algebra of dimension eight. The basis is $e_0, e_1, \dots, e_7$, with $e_0 = 1$ the identity and

$$
e_k^2 = -e_0 \quad (1\leq k\leq 7).
$$

Conjugation is the linear map $\bar{\cdot}$ with $\bar{e_0} = e_0$ and $\bar{e_k} = -e_k$. The product of two distinct imaginary basis elements is $\pm e_l$ according to the orientation rule of the next section. All products are written without brackets only where associativity is known; the convention is that $xyz$ abbreviates $(xy)z$, and that a bracket is dropped only inside an associative subalgebra.

## The Cayley–Dickson Construction

### The Doubling

**Definition.** Let $A$ be an algebra over $\mathbb{R}$ with an involution $a\mapsto\bar a$ and with $a + \bar a\in\mathbb{R}1$ and $a\bar a\in\mathbb{R}1$ for all $a\in A$. The **Cayley–Dickson double** $\mathrm{CD}(A)$ is the vector space $A\oplus A$ with the product

$$
(a,b)(c,d) = \left(ac - \bar d b,\ da + b\bar c\right), \qquad a,b,c,d\in A .
$$

**Proposition.** If $A$ is a composition algebra with $N(a) = a\bar a$, then $\mathrm{CD}(A)$ is a composition algebra with $N((a,b)) = N(a) + N(b)$, the conjugation $(\overline{a,b}) = (\bar a,-b)$, and the identity $(1,0)$.

*Proof.* An expansion using the composition law in $A$ shows $N(xy) = N(x)N(y)$ for $x,y\in \mathrm{CD}(A)$ and $x\bar x = N(x)(1,0)$; the statements about the identity and the conjugation are immediate from the definition. $\square$

The construction is the same one that produces $\mathbb{C}$ from $\mathbb{R}$ and $\mathbb{H}$ from $\mathbb{C}$. It produces $\mathbb{O}$ from $\mathbb{H}$:

$$
\mathbb{O} = \mathrm{CD}(\mathbb{H}) = \mathbb{H}\oplus\mathbb{H}.
$$

Writing an octonion as a pair $(a,b)$ of quaternions, the product is

$$
(a,b)(c,d) = (ac - \bar d b,\ da + b\bar c).
$$

Iterating further produces the sedenions $\mathbb{S} = \mathrm{CD}(\mathbb{O})$, of dimension sixteen, in which $N$ is no longer multiplicative and which contain zero divisors; the octonions are the last normed division algebra, a fact stated precisely in the last section of this article (Hurwitz's theorem).

### The Fano Plane and the Multiplication Table

**Definition.** The **Fano plane** $\mathbb{F}$ has seven points $1,2,\dots,7$ and seven lines

$$
(1,2,3),\quad (1,4,5),\quad (1,7,6),\quad (2,4,6),\quad (2,5,7),\quad (3,4,7),\quad (3,6,5),
$$

each line a **cyclically ordered** triple $(a,b,c)$. Every point lies on exactly three lines, every pair of points lies on exactly one line, and the numbering is chosen so that the ordering is cyclic, that is, the triples $(a,b,c)$, $(b,c,a)$, $(c,a,b)$ all present the same line and the reversed triples present the opposite orientation.

**Definition.** The **multiplication** on the basis is defined by the two rules

$$
e_0e_j = e_je_0 = e_j, \qquad e_k^2 = -e_0 \quad (1\leq k\leq 7),
$$

and, for every cyclically ordered line $(a,b,c)$ of the Fano plane, by

$$
e_ae_b = e_c, \qquad e_be_c = e_a, \qquad e_ce_a = e_b, \qquad e_be_a = e_ce_b = e_ae_c = -e_c, -e_a, -e_b ,
$$

with the products extended bilinearly.

The multiplication is thus completely determined by the two rules and the Fano plane; the last display is the statement that reversing the order of a pair on a line negates the product. The rule is consistent because every unordered pair of distinct imaginary basis elements lies on exactly one line, so that each product of two distinct imaginary units is fixed once and only once.

**Example.** On the line $(1,2,3)$ one has $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$, and $e_2e_1 = -e_3$, $e_3e_2 = -e_1$, $e_1e_3 = -e_2$. On the line $(1,7,6)$ one has $e_1e_7 = e_6$ and $e_7e_1 = -e_6$; the same pair $1,7$ occurs on no other line, so there is no inconsistency.

**Proposition.** The multiplication is well defined and makes $\mathbb{O}$ a real algebra of dimension eight with identity $e_0$. It agrees with the Cayley–Dickson product obtained from $\mathbb{H}$ under the identification $e_0 = (1,0)$, $e_1 = (i,0)$, $e_2 = (j,0)$, $e_3 = (k,0)$, $e_4 = (0,1)$, $e_5 = (0,i)$, $e_6 = (0,j)$, $e_7 = (0,k)$, where $i,j,k$ is the quaternion basis.

*Proof.* Each product of basis elements is assigned once, and bilinear extension is unambiguous; the identification with the Cayley–Dickson product is a finite check, carried out in the table below. $\square$

The identification of the display fixes the indexing used throughout this Part: the octonion units are indexed so that the four-space spanned by $e_0,e_1,e_2,e_3$ is the quaternion subalgebra $\mathbb{H}$, the four-space spanned by $e_4,e_5,e_6,e_7$ is the subspace $\mathbb{H}e_4$, and $e_4$ is the vector $(0,1)$ of the doubling.

**Table (multiplication of the imaginary basis).** Rows are left factors, columns right factors; the entry is the coefficient $s$ in $e_re_c = s\,e_k$, written $e_k$ with the sign omitted when positive.

| $e_r\backslash e_c$ | $e_1$ | $e_2$ | $e_3$ | $e_4$ | $e_5$ | $e_6$ | $e_7$ |
|---|---|---|---|---|---|---|---|
| $e_1$ | $-e_0$ | $e_3$ | $-e_2$ | $e_5$ | $-e_4$ | $-e_7$ | $e_6$ |
| $e_2$ | $-e_3$ | $-e_0$ | $e_1$ | $e_6$ | $e_7$ | $-e_4$ | $-e_5$ |
| $e_3$ | $e_2$ | $-e_1$ | $-e_0$ | $e_7$ | $-e_6$ | $e_5$ | $-e_4$ |
| $e_4$ | $-e_5$ | $-e_6$ | $-e_7$ | $-e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_5$ | $e_4$ | $-e_7$ | $e_6$ | $-e_1$ | $-e_0$ | $-e_3$ | $e_2$ |
| $e_6$ | $e_7$ | $e_4$ | $-e_5$ | $-e_2$ | $e_3$ | $-e_0$ | $-e_1$ |
| $e_7$ | $-e_6$ | $e_5$ | $e_4$ | $-e_3$ | $-e_2$ | $e_1$ | $-e_0$ |

**Definition.** The **vector part** and **scalar part** of an octonion $x = \sum_{k=0}^{7}x_ke_k$ are

$$
\operatorname{Sc}(x) = x_0, \qquad \operatorname{Vect}(x) = \sum_{k=1}^{7}x_ke_k,
$$

and the **conjugate** is $\bar x = \operatorname{Sc}(x) - \operatorname{Vect}(x)$; the octonion is **imaginary** or **pure** if $\operatorname{Sc}(x) = 0$, and the imaginary subspace is written $\operatorname{Im}\mathbb{O}$, a real seven-space.

## Identities

### Conjugation and the Scalar Part

**Proposition.** The following hold for all $x,y\in\mathbb{O}$ and $\lambda\in\mathbb{R}$:

1. $\overline{\bar x} = x$, $\overline{x + y} = \bar x + \bar y$, $\overline{\lambda x} = \lambda\bar x$;
2. $x + \bar x = 2\operatorname{Sc}(x)e_0$, so that $x + \bar x\in\mathbb{R}e_0$;
3. $x\bar x = \bar xx\in\mathbb{R}e_0$, and the scalar $\lvert x\rvert^2 = x\bar x$ is the sum of the squares of the coefficients, $\lvert x\rvert^2 = \sum_{k=0}^{7}x_k^2$;
4. $\overline{xy} = \bar y\,\bar x$;
5. $x\bar x = 0$ implies $x = 0$.

*Proof.* Statements 1 and 2 are immediate from the definitions. For 3, multiplicativity of the norm form in the Cayley–Dickson doubling together with $N(e_0) = 1$ gives $x\bar x = N(x)e_0$, and the displayed coordinate expression follows by expansion; the equality $\bar xx = x\bar x$ follows from $\overline{x\bar x} = x\bar x$ and statement 4. For 4, both sides are bilinear, and the identity is checked on basis elements from the table: for an oriented line $(a,b,c)$ one has $\overline{e_ae_b} = \bar e_c = -e_c$ and $\bar e_b\bar e_a = (-e_b)(-e_a) = e_be_a = -e_c$, and the remaining cases are similar. For 5, use statement 3. $\square$

The scalar $\lvert x\rvert^2$ is the **quadratic norm** of $x$; its systematic treatment, the invariance of the associated bilinear form under multiplication, and the invertibility theory, are the subject and are used here only where the multiplication forces them.

### The Associator

**Definition.** The **associator** of $x,y,z\in\mathbb{O}$ is

$$
[x,y,z] = (xy)z - x(yz).
$$

**Theorem.** The associator is trilinear over $\mathbb{R}$ and **alternating**: it changes sign under the interchange of any two arguments, and vanishes whenever two arguments are equal. Consequently

$$
[x,y,z] = [y,z,x] = [z,x,y] = -[y,x,z] = -[x,z,y] = -[z,y,x] ,
$$

and the associator vanishes identically on any two-dimensional subspace, that is, the subalgebra generated by any two octonions is associative.

*Proof.* Trilinearity is clear. The alternating property is checked on the basis: if two of $x,y,z$ are equal the associator vanishes by the multiplication table, and the sign change under transposition is a finite check on the $7^3 = 343$ triples of imaginary basis elements, all of which are covered by the seven-line rule. Vanishing on a two-dimensional subspace then follows because the associator of three elements of $\operatorname{span}(x,y)$ expands into associators with a repeated argument. $\square$

The last statement is **Artin's theorem**, in the form in which it is used throughout the theory: *every subalgebra generated by two elements of $\mathbb{O}$ is associative*. Its consequence is that the octonions retain an associative "slice" through every point, and this is the reason why ordinary calculations with two octonions never require care with brackets. The first genuine failure of associativity requires three independent directions:

**Example.** $[e_1,e_2,e_4] = (e_1e_2)e_4 - e_1(e_2e_4) = e_3e_4 - e_1e_6 = e_7 - (-e_7) = 2e_7$, so the associator is non-zero and is a pure imaginary octonion orthogonal to each of $e_1,e_2,e_4$; reversing two arguments changes its sign, $[e_1,e_4,e_2] = -2e_7$.

**Proposition.** Let $x,y,z$ be imaginary octonions, pairwise orthogonal and of norm one. Then the associator $[x,y,z]$ is imaginary and is orthogonal to each of $x,y,z$; it vanishes exactly when $z$ lies in the quaternion subalgebra $\operatorname{span}(e_0,x,y,xy)$ generated by $x$ and $y$. In particular $[e_1,e_2,e_4] = 2e_7\neq0$, while $[e_1,e_2,e_3] = 0$ because $e_1,e_2,e_3$ span a quaternion subalgebra with $e_0$.

*Proof.* The orthogonality is verified by expanding in an orthonormal basis adapted to the triple and using the multiplication table; the vanishing criterion is the observation that the associator is determined by the Fano incidence, so that it vanishes precisely when the three units together with the identity close under multiplication. $\square$

### Alternativity and the Moufang Identities

The weakening of associativity that the octonions satisfy is alternativity and the Moufang laws.

**Theorem (Artin).** The octonions are **alternative**: for all $x,y\in\mathbb{O}$,

$$
(xx)y = x(xy), \qquad (xy)x = x(yx), \qquad (yx)x = y(xx) \quad\text{and}\quad (xy)y = x(yy),
$$

equivalently the associator changes sign when any two arguments are interchanged and vanishes when two are equal.

**Theorem (Moufang).** For all $x,y,z\in\mathbb{O}$,

$$
(xyx)z = x(y(xz)), \qquad z(xyx) = ((zx)y)x, \qquad (xy)(zx) = x(yz)x ,
$$

where $xyx$ means $(xy)x$.

*Proof.* Each identity is trilinear, so it suffices to check it on basis elements, which is finite and is done from the table; alternatively each is a consequence of the corresponding identity in the Cayley–Dickson double, where it follows from the associativity of the quaternion factor. $\square$

**Proposition.** The following further identities hold for all $x,y\in\mathbb{O}$, and are the form in which invertibility is normally used:

$$
x(\bar xy) = \lvert x\rvert^2 y, \qquad (x\bar y)y = \lvert y\rvert^2 x, \qquad (\bar xy)\bar x = \lvert x\rvert^2 y, \qquad \bar x(xy) = \lvert x\rvert^2 y .
$$

*Proof.* Expand in coordinates and use the table; the identities express the two-sidedness of the Cayley–Dickson conjugation in the algebra and are the exact substitutes for associativity in the cancellation arguments. $\square$

## Subalgebras and the Fano Plane

### Two-Dimensional and Four-Dimensional Subalgebras

**Proposition.** Every one-dimensional subalgebra is $\mathbb{R}e_0$, and the subalgebras generated by two elements are the copies of $\mathbb{C}$ and of $\mathbb{H}$:

- the subalgebra generated by $e_0$ and one imaginary unit $u$ is $\operatorname{span}(e_0,u)\cong\mathbb{C}$;
- the subalgebra generated by two imaginary units $u,v$ that are orthogonal is $\operatorname{span}(e_0,u,v,uv)\cong\mathbb{H}$.

*Proof.* By Artin's theorem the generated subalgebra is associative; the two-dimensional space $\operatorname{span}(e_0,u)$ with $u$ an imaginary unit is closed under multiplication and is $\mathbb{R}[u]/(u^2+1)\cong\mathbb{C}$, and the four-dimensional space $\operatorname{span}(e_0,u,v,uv)$ with $u,v$ orthogonal imaginary units is closed under multiplication and, by the multiplication table, has the same products as the quaternion basis $e_0,e_1,e_2,e_3$. $\square$

The quaternion subalgebras of $\mathbb{O}$ are parametrised by the oriented two-planes in the imaginary space; each is obtained by choosing an orthonormal pair of imaginary units and adjoining their product. There are, up to the action of the automorphism group $G_2 = \operatorname{Aut}(\mathbb{O})$, exactly two classes of such subalgebras, the class of $\mathbb{C}$ and the class of $\mathbb{H}$, and the automorphism group acts transitively on the imaginary units.

### The Seven Lines and the Fano Structure

**Proposition.** The set of imaginary units $\{e_1,\dots,e_7\}$ with the product $\pm$ constitutes a **Moufang loop** under the loop product obtained by projecting to units, and the Fano plane records its multiplication: each line $(a,b,c)$ presents the quaternion subalgebra $\operatorname{span}(e_0,e_a,e_b,e_c)\cong\mathbb{H}$ with $e_ae_b = e_c$.

*Proof.* The loop axioms are checked from the table; the identification of the lines with quaternion subalgebras is the previous proposition, and the Fano incidence properties are verified directly from the list of lines. $\square$

**Example.** The line $(1,2,3)$ gives the quaternion subalgebra $\operatorname{span}(e_0,e_1,e_2,e_3)$, which under the identification of the Cayley–Dickson construction is the initial copy of $\mathbb{H}$. The line $(1,4,5)$ gives $\operatorname{span}(e_0,e_1,e_4,e_5)$, the subalgebra generated by $e_1$ and $e_4$, whose product $e_1e_4 = e_5$ is read from the table.

## The Structure of the Algebra

### The Place of the Octonions

**Theorem (Frobenius, Hurwitz).** Every finite-dimensional real associative division algebra is isomorphic to $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$; every finite-dimensional real normed division algebra — that is, every real algebra with a positive definite quadratic form satisfying $\lvert xy\rvert = \lvert x\rvert\lvert y\rvert$ and with no zero divisors — is isomorphic to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ or $\mathbb{O}$. The octonions are therefore the largest normed division algebra, and the largest division algebra obtainable from the Cayley–Dickson construction.

*Proof.* The associative statement is Frobenius's theorem; the general statement is Hurwitz's theorem on composition algebras, of which the octonion case is the last step. Both are quoted as standard, with the standard sources listed in the Further Reading; the corpus states the composition algebras of a general field in *Quadratic Forms over Algebras and Norm Forms*. $\square$

**Proposition.** The octonion algebra is **not** associative and is **not** commutative; it is **flexible**,

$$
x(yx) = (xy)x \quad\text{for all }x,y\in\mathbb{O},
$$

and it is a **division algebra**: the only octonion $x$ with $xy = 0$ or $yx = 0$ for some $y\neq0$ is $x = 0$.

*Proof.* Non-associativity and non-commutativity are the example and the skew-symmetric entries of the table. Flexibility is the specialisation $x = z$ of the alternating property of the associator. For the division statement, if $xy = 0$ with $y\neq0$ then $x = \lvert y\rvert^{-2}(xy)\bar y = 0$ using the identities of the previous section. $\square$

The **centre** of $\mathbb{O}$ is $\mathbb{R}e_0$: an element commuting and associating with every element is a real scalar. The derivation algebra $\operatorname{Der}(\mathbb{O})$ is the exceptional Lie algebra $\mathfrak{g}_2$, of dimension fourteen, and the automorphism group is the exceptional Lie group $G_2$; both are treated.

### Vector Matrices

The octonions admit a presentation by $2\times2$ matrices of scalars and septuples, in which the non-associativity of $\mathbb{O}$ is replaced by an explicit product rule and the mysterious part of the multiplication is carried by the cross product of $\mathbb{R}^7$.

**Definition.** A **Zorn vector matrix** is an array

$$
\begin{pmatrix} \alpha & u\\ v & \beta\end{pmatrix}, \qquad \alpha,\beta\in\mathbb{R},\ u,v\in\mathbb{R}^7,
$$

with the product

$$
\begin{pmatrix} \alpha & u\\ v & \beta\end{pmatrix}
\begin{pmatrix} \alpha' & u'\\ v' & \beta'\end{pmatrix}
=
\begin{pmatrix}
\alpha\alpha' + u\cdot v' & \alpha u' + \beta' u - v\times v'\\
\alpha'v + \beta v' + u\times u' & \beta\beta' + v\cdot u'
\end{pmatrix},
$$

where the dot and cross products on $\mathbb{R}^7$ are those induced by the octonion product on the imaginary space,

$$
u\cdot v = \operatorname{Sc}(u\bar v), \qquad u\times v = \operatorname{Vect}(uv), \qquad u,v\in\operatorname{Im}\mathbb{O} .
$$

**Proposition.** The dot product is a positive definite symmetric bilinear form on $\mathbb{R}^7$ with $u\cdot u = \lvert u\rvert^2$, the cross product is bilinear and alternating, and the two satisfy, for all $u,v,w\in\mathbb{R}^7$,

$$
u\times v = -v\times u, \qquad u\cdot(v\times w) = (u\times v)\cdot w, \qquad
u\times(u\times v) = (u\cdot v)u - (u\cdot u)v ,
$$

the last being the seven-dimensional form of the triple product identity. The Zorn vector matrices form a non-associative real algebra of dimension sixteen with identity the matrix with $\alpha = \beta = 1$ and $u = v = 0$, and the map

$$
(\alpha,u,v,\beta)\longmapsto \alpha E_{00} + \beta E_{11} + \sum_{k=1}^{7}u_kE_{01}e_k + \sum_{k=1}^{7}v_kE_{10}e_k
$$

embeds it as a subalgebra of the algebra of $2\times2$ matrices over $\mathbb{O}$ taken with the left-associated product, that is, the product of two such matrices is computed with the brackets fixed on the left.

*Proof.* The properties of the dot and cross products are the standard identities of the seven-dimensional vector product, which follow from the Fano rule; the alternation of the cross product is the skew symmetry of the multiplication table, the scalar triple product identity is the associativity of the scalar part $\operatorname{Sc}((uv)w)$, which holds because the scalar part of a product of three imaginary units is given by the alternating three-form of the orientation, and the triple product identity is its contraction. The dimension and the identity are immediate. The embedding is the identification of the array with the matrix whose entries are the corresponding octonions; the product rule is then obtained by computing the four entries of the product with all brackets on the left and using the identities $u\bar u' = u\cdot u' + u\times u'$ and the like. $\square$

**Proposition.** The **determinant**

$$
\det\begin{pmatrix} \alpha & u\\ v & \beta\end{pmatrix} = \alpha\beta - u\cdot v
$$

is a quadratic form on the sixteen-dimensional Zorn algebra of signature $(8,8)$; its restriction to the **Hermitian** elements, those with $v = -u$, is a quadratic form of signature $(1,9)$ on a ten-dimensional space, and on the three-dimensional Hermitian matrices over $\mathbb{O}$ the corresponding cubic form defines the exceptional Jordan algebra, treated.

*Proof.* The form $\alpha\beta - u\cdot v$ is the sum of the hyperbolic form $\alpha\beta$ on the two scalar coordinates, of signature $(1,1)$, and of the form $-u\cdot v$ on $\mathbb{R}^{14}$, which pairs the two copies of $\mathbb{R}^7$; the latter has signature $(7,7)$, since it is the standard split form of a real vector space paired with its dual. Hence the total signature is $(8,8)$. On the Hermitian subspace one has $u\cdot v = -u\cdot u = -\lvert u\rvert^2$, so the form is $\alpha\beta - \lvert u\rvert^2$, whose signature is $(1,9)$ because $\alpha\beta$ has signature $(1,1)$ on two variables and the remaining eight variables contribute eight negative directions. $\square$

The $2\times2$ Hermitian matrices form a Jordan algebra under the symmetrised product $\tfrac12(MN + NM)$, of degree two over $\mathbb{R}$; the degree-three analog, the exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$, is the object through which the exceptional groups $F_4$, $E_6$, $E_7$ and $E_8$ are constructed, and its treatment belongs.

## Summary

The octonion algebra $\mathbb{O}$ is the real vector space of dimension eight with basis $e_0 = 1, e_1,\dots,e_7$, with $e_k^2 = -e_0$ and with the products of distinct imaginary units determined by the orientation of the seven lines of the Fano plane: on a cyclically ordered line $(a,b,c)$ one has $e_ae_b = e_c$, $e_be_c = e_a$, $e_ce_a = e_b$, and reversing any factor negates the product. Equivalently, $\mathbb{O} = \mathbb{H}\oplus\mathbb{H}$ is the Cayley–Dickson double of the quaternions, with product $(a,b)(c,d) = (ac - \bar db, da + b\bar c)$.

The algebra has identity $e_0$ and is neither commutative nor associative. Its associator $[x,y,z] = (xy)z - x(yz)$ is alternating, so the algebra is alternative and flexible and every subalgebra generated by two elements is associative; it satisfies the Moufang identities $(xyx)z = x(y(xz))$, $z(xyx) = ((zx)y)x$ and $(xy)(zx) = x(yz)x$. Conjugation is an anti-automorphism, $\overline{xy} = \bar y\bar x$, and $x + \bar x$ and $x\bar x$ are real; the scalar $\lvert x\rvert^2 = x\bar x$ is the sum of the squares of the coefficients. The identities $x(\bar xy) = \lvert x\rvert^2y$ and $(x\bar y)y = \lvert y\rvert^2x$ replace associativity in cancellation. The algebra is a division algebra, and by Hurwitz's theorem it is the largest normed division algebra over $\mathbb{R}$. Its subalgebras generated by one and two elements are the copies of $\mathbb{C}$ and $\mathbb{H}$; its Fano lines record the quaternion subalgebras; its centre is $\mathbb{R}e_0$; and it may be presented by Zorn vector matrices, in which the product is expressed by the dot and cross products on $\mathbb{R}^7$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$ | The octonion algebra, $\dim_{\mathbb{R}} = 8$ |
| $e_0 = 1, e_1,\dots,e_7$ | Basis, $e_k^2 = -e_0$ for $k\geq1$ |
| $\mathbb{F}$, $(a,b,c)$ | Fano plane and its cyclically ordered lines |
| $\bar{x}$ | Conjugation, $\bar e_0 = e_0$, $\bar e_k = -e_k$, $\overline{xy} = \bar y\bar x$ |
| $\operatorname{Sc}(x)$, $\operatorname{Vect}(x)$ | Scalar and vector parts, $\operatorname{Im}\mathbb{O} = \operatorname{Vect}(\mathbb{O})$ |
| $\lvert x\rvert^2 = x\bar x = \bar xx = \sum_kx_k^2$ | Quadratic norm (developed) |
| $[x,y,z] = (xy)z - x(yz)$ | Associator, alternating |
| $xyx = (xy)x$ | Abbreviation in the Moufang identities |
| $\mathrm{CD}(A)$ | Cayley–Dickson double of $A$ |
| $\mathbb{O} = \mathrm{CD}(\mathbb{H}) = \mathbb{H}\oplus\mathbb{H}$ | The doubling construction |
| $\operatorname{Der}(\mathbb{O}) = \mathfrak{g}_2$, $\operatorname{Aut}(\mathbb{O}) = G_2$ | Derivation algebra and automorphism group |
| $u\cdot v = \operatorname{Sc}(u\bar v)$, $u\times v = \operatorname{Vect}(uv)$ | Dot and cross products on $\mathbb{R}^7$ |
| $\det\begin{pmatrix}\alpha & u\\ v & \beta\end{pmatrix} = \alpha\beta - u\cdot v$ | Determinant of a Zorn vector matrix |





## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the Cayley–Dickson construction, the Moufang identities and the structure theory of non-associative algebras.
- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* **39** (2002), 145–205, for the standard modern survey of the algebra and its applications.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the identity theory and the vector-matrix presentation.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Zorn matrices and the exceptional Jordan algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the cross product on $\mathbb{R}^7$, the vector matrices and the Fano plane.
- Max Zorn, "Theorie der alternativen Ringe", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **8** (1931), 123–147, for the original treatment of alternative rings.
