
# __The Volume Element, Duality and the Hodge Star__

## Introduction

The top grade of the Clifford algebra of an $n$-dimensional quadratic space is one-dimensional, spanned by the product of the elements of an orthogonal basis, and multiplication by that element is a bijection from each grade to the complementary grade. This article develops that operation. The element itself is the volume element; the map it induces is the **complement map**, a linear isomorphism $\mathrm{Cl}_k(V,q)\to\mathrm{Cl}_{n-k}(V,q)$ that carries a simple $k$-vector on a subspace to a simple $(n-k)$-vector on the orthogonal complement when the subspace is non-degenerate; normalised by the inverse of the volume element it is the **Hodge star**, whose square is a scalar determined by the metric. The star gives the cross product of three-dimensional space as the complement of a bivector, and in the biquaternion algebra it is the duality of the pseudoscalar that the physics articles write with the factor $-i$.

The volume element, its square and its centrality are from *Clifford Algebras in Finite Dimensions*; the grade subspaces, the grade projection and the grade theorem are from *The Geometric Product and the Grade Decomposition*; the biquaternion algebra and its identification with $\mathrm{Cl}_{3,0}$, with the pseudoscalar acting as the central unit $i$, are from *The Biquaternion Algebra as a Clifford Algebra*. Nothing owned by those entries is re-derived. The base is a field $F$ of characteristic not $2$, with $q$ non-degenerate on the finite-dimensional space $V$ of dimension $n$ and $B$ its polar form; the convention is $v^2=q(v)\cdot1$.

## The Complement Map

### Multiplication by the Volume Element

Let $e_1,\ldots,e_n$ be an orthogonal basis and let

$$
\omega=e_1e_2\cdots e_n
$$

be the **volume element**, also called the pseudoscalar. Its square is the scalar

$$
\omega^2=(-1)^{n(n-1)/2}\,q(e_1)q(e_2)\cdots q(e_n),
$$

and $\omega\neq0$ because $q$ is non-degenerate and the basis is orthogonal; hence $\omega$ is invertible, with $\omega^{-1}=\omega/\omega^2$. The volume element is central when $n$ is odd and is central up to sign when $n$ is even, commuting with the even part and anticommuting with the odd part; those facts are from *Clifford Algebras in Finite Dimensions*.

**Definition.** For $A\in\mathrm{Cl}(V,q)$ the **right complement** is $A\omega$ and the **left complement** is $\omega A$.

**Theorem.** For $A\in\mathrm{Cl}_k(V,q)$ both complements lie in the complementary grade:

$$
A\omega\in\mathrm{Cl}_{n-k}(V,q), \qquad \omega A\in\mathrm{Cl}_{n-k}(V,q).
$$

**Proof.** By bilinearity it suffices to take a monomial $A=e_{i_1}\cdots e_{i_k}$ with increasing indices. The index set of $A$ is contained in the index set of $\omega$, so in the product $A\omega$ every index of $A$ occurs twice and every other index once. Moving the factors so that the repeated indices become adjacent and replacing each $e^2$ by the scalar $q(e)$ leaves a scalar multiple of the product of the $n-k$ distinct indices outside $A$; that product is an element of $\mathrm{Cl}_{n-k}(V,q)$. The same computation applies to $\omega A$, the repeated indices being the same. $\square$

The proof is the mechanism of the grade theorem of *The Geometric Product and the Grade Decomposition* in the case in which one factor is of top grade: of the grades $n-k,n-k+2,\ldots,n+k$ that the theorem permits, only the first occurs, because the second factor already contains every index.

**Corollary.** Right multiplication by $\omega$ is a bijection $\mathrm{Cl}_k(V,q)\to\mathrm{Cl}_{n-k}(V,q)$, of inverse $A\mapsto A\omega^{-1}$; and left multiplication by $\omega$ is a bijection with the same target and the same inverse.

**Proof.** Both maps are linear and their images lie in the stated grade. The map $A\mapsto A\omega$ is injective because $\omega$ is invertible in $\mathrm{Cl}(V,q)$, and both spaces have dimension $\binom{n}{k}=\binom{n}{n-k}$, so injectivity gives bijectivity. The inverse is right multiplication by $\omega^{-1}$, and the case of left multiplication is the same. $\square$

**Corollary.** For $\omega$ central, that is for $n$ odd, the two complements coincide, $A\omega=\omega A$. For $n$ even they agree up to the sign of the grade, $\omega A=(-1)^kA\omega$ for $A\in\mathrm{Cl}_k(V,q)$.

**Proof.** The volume element commutes with even elements and anticommutes with odd ones, so for $A$ homogeneous of grade $k$ the two products differ by $(-1)^k$. $\square$

### The Geometric Reading

**Proposition.** Let $e_I=e_{i_1}\cdots e_{i_k}$ be a basis blade of an orthogonal basis, with index set $I$. Then $e_I\omega$ is, up to sign, the basis blade of the complementary index set,

$$
e_I\omega=\pm\,e_{I^{c}}, \qquad I^{c}=\{1,\ldots,n\}\setminus I,
$$

so that the complement map carries the subspace spanned by the index set $I$ to its orthogonal complement in $V$.

**Proof.** The computation of the theorem exhibits $e_I\omega$ as a scalar multiple of the product of the generators with indices outside $I$, and that scalar is a product of squares $q(e_i)$ and of signs. The indices outside $I$ index a basis of the orthogonal complement of the span of $e_I$. For an orthonormal basis, $q(e_i)=\pm1$, and the scalar is $\pm1$. $\square$

**Example.** In $\mathrm{Cl}_{3,0}$ with $\omega=e_1e_2e_3$ one has $e_1\omega=e_2e_3$, $e_2\omega=e_3e_1$, $e_3\omega=e_1e_2$, and $e_1e_2\omega=-e_3$, $e_2e_3\omega=-e_1$, $e_3e_1\omega=-e_2$. So the complement of a vector is a bivector on the perpendicular plane and the complement of a bivector is a vector, the two being related by the volume element and the sign.

**Remark.** The map depends on the choice of orthogonal basis through the orientation only. Replacing one basis element $e_i$ by $-e_i$ changes $\omega$ to $-\omega$ and therefore changes both complements by a sign, while leaving the metric and the grades intact. The complement map is thus an operation of an oriented quadratic space, and the reversal of the orientation reverses it.

## The Hodge Star

### Definition and Square

The complement map acquires a canonical normalisation from the inverse of the volume element.

**Definition.** The **Hodge star** is the linear map

$$
\star A=A\omega^{-1}, \qquad A\in\mathrm{Cl}(V,q).
$$

By the corollary above, $\star$ carries $\mathrm{Cl}_k(V,q)$ isomorphically onto $\mathrm{Cl}_{n-k}(V,q)$. For $n$ odd it coincides with left multiplication by $\omega^{-1}$, and for $n$ even it satisfies $\omega A=(-1)^k A\omega$ for $A$ of grade $k$.

**Theorem.** The square of the star is the scalar inverse of the square of the volume element:

$$
\star\star A=A\omega^{-2}=(\omega^2)^{-1}A,
$$

so that $\star^2=(\omega^2)^{-1}\operatorname{id}$, and when $\omega^2=\pm1$ the star is an involution or a complex structure accordingly, $\star^2=\omega^2\operatorname{id}$.

**Proof.** $\star\star A=(A\omega^{-1})\omega^{-1}=A\omega^{-2}$, and $\omega^{-2}=(\omega^2)^{-1}$ is a scalar because $\omega^2$ is a scalar, so the scalar commutes with $A$. If $\omega^2=\pm1$ then $(\omega^2)^{-1}=\omega^2$. $\square$

**Corollary (parity of the star).** If $n$ is even the star preserves the parity grading, because $k$ and $n-k$ have the same parity; if $n$ is odd it exchanges the two parity parts.

**Proof.** The star maps $\mathrm{Cl}_k$ to $\mathrm{Cl}_{n-k}$, and $k$ and $n-k$ differ by $n$. If $n$ is even they have the same parity and the image of an even element is even; if $n$ is odd they have opposite parity. $\square$

### The Low-Dimensional Cases

The square of the star is read off from the square of the volume element, and the metric enters through the product of the squares of the basis generators.

| Space | $n$ | $\omega^2$ | $\star^2$ | Behaviour of $\star$ |
|---|---|---|---|---|
| $\mathrm{Cl}_{1,0}$ | $1$ | $1$ | $+1$ | scalars against vectors |
| $\mathrm{Cl}_{2,0}$ | $2$ | $-1$ | $-1$ | a quarter turn on the vectors |
| $\mathrm{Cl}_{1,1}$ | $2$ | $+1$ | $+1$ | an involution on the vectors that negates the form |
| $\mathrm{Cl}_{3,0}$ | $3$ | $-1$ | $-1$ | vectors against bivectors |
| $\mathrm{Cl}_{4,0}$ | $4$ | $+1$ | $+1$ | self-dual and anti-self-dual bivectors |
| $\mathrm{Cl}_{1,3}$ | $4$ | $-1$ | $-1$ | a complex structure on the bivectors |

**Verification of the table.** In $\mathrm{Cl}_{1,0}$ with $q(e_1)=1$ one has $\omega=e_1$ and $\omega^2=1$. In $\mathrm{Cl}_{2,0}$ with $q(e_1)=q(e_2)=1$ one has $\omega=e_1e_2$ and $\omega^2=-e_1^2e_2^2=-1$, while in $\mathrm{Cl}_{1,1}$ with $q(e_1)=1$, $q(e_2)=-1$ the same computation gives $\omega^2=-q(e_1)q(e_2)=+1$. In $\mathrm{Cl}_{3,0}$ the factor $(-1)^{3\cdot2/2}=(-1)^3=-1$ and the product of the three squares is $1$, so $\omega^2=-1$. In $\mathrm{Cl}_{4,0}$ the factor is $(-1)^{4\cdot3/2}=+1$ and the product of the four squares is $1$, so $\omega^2=+1$. In $\mathrm{Cl}_{1,3}$ the same factor $+1$ multiplies the product $1\cdot(-1)\cdot(-1)\cdot(-1)=-1$, so $\omega^2=-1$. The star is then $(\omega^2)^{-1}=\omega^2$ on each element in the cases $\omega^2=\pm1$.

**The star in the plane and in three dimensions.** In $\mathrm{Cl}_{2,0}$ the star sends $1$ to $-e_1e_2$, $e_1$ to $-e_2$, $e_2$ to $e_1$ and $e_1e_2$ to $1$, so that on the vectors it is the quarter turn of the plane and its square is $-1$. In $\mathrm{Cl}_{1,1}$ the same table of signs is read with $\omega^2=+1$ and $\omega^{-1}=\omega$: the star sends $e_1$ to $e_2$ and $e_2$ to $e_1$, so on the plane it is an involution exchanging the two coordinate directions, and it is an anti-isometry rather than an isometry, since $q(\star v)=\varepsilon\,q(v)=-q(v)$ for $\varepsilon=q(e_2)=-1$. The definite and the indefinite planes are thus distinguished by the sign of $\omega^2$, and with it by whether the star preserves or negates the form. In $\mathrm{Cl}_{3,0}$ the star sends $1$ to $-\omega$, $e_1$ to $-e_2e_3$, $e_1e_2$ to $e_3$ and $\omega$ to $1$; on the space of bivectors, of dimension three, it carries a bivector to its dual vector, and on that space its square is $-1$, since $\star^2=(\omega^2)^{-1}=-1$.

**The star in four dimensions.** In $\mathrm{Cl}_{4,0}$ the star preserves the six-dimensional space $\mathrm{Cl}_2$ of bivectors and satisfies $\star^2=+1$ there, so that the bivectors split into the eigenspaces of $\star$ for the eigenvalues $+1$ and $-1$, of dimension three each: the self-dual and the anti-self-dual bivectors. In $\mathrm{Cl}_{1,3}$ the same space carries $\star^2=-1$, so that $\star$ is a complex structure on it, with no real eigenspace and with the two complex eigenspaces corresponding to the two chiral halves of the Lorentz group. The change from $+1$ to $-1$ is the change of the sign of $\omega^2$ between the two signatures.

## The Cross Product in Three Dimensions

The complement map supplies the cross product of a three-dimensional space with a definite form.

**Theorem.** Let $V$ be three-dimensional with a definite form, $\omega$ the volume element of an orthonormal basis, and $a,b\in V$. Then

$$
a\times b:=\star(a\wedge b)=(a\wedge b)\omega^{-1}
$$

is a vector, bilinear and alternating in $a$ and $b$, orthogonal to both, of squared length $q(a)q(b)-B(a,b)^2$, and it satisfies $a\times b=0$ exactly when $a$ and $b$ are linearly dependent.

**Proof.** The product $a\wedge b$ is a bivector and the star carries it to $\mathrm{Cl}_1$, so the result is a vector; bilinearity and alternation are those of the outer product, and antisymmetry is the graded-commutativity $b\wedge a=-a\wedge b$. For the remaining properties take an orthonormal basis $e_1,e_2,e_3$ with $\omega=e_1e_2e_3$, so that $\omega^{-1}=-\omega$ and the computation of the example below gives $e_i\times e_j=e_k$ for $(i,j,k)$ a cyclic permutation of $(1,2,3)$ and $e_i\times e_i=0$. Writing $a=\sum a_ie_i$ and $b=\sum b_ie_i$, bilinearity gives

$$
a\times b=(a_2b_3-a_3b_2)e_1+(a_3b_1-a_1b_3)e_2+(a_1b_2-a_2b_1)e_3,
$$

which is orthogonal to $a$ and to $b$ and vanishes exactly when the three $2\times2$ minors vanish, that is when $a$ and $b$ are linearly dependent. Its squared length, computed from the three coordinates, is the Lagrange identity $q(a)q(b)-B(a,b)^2$. $\square$

**Example.** In $\mathrm{Cl}_{3,0}$ one has $\omega^2=-1$, hence $\omega^{-1}=-\omega=-e_1e_2e_3$, and

$$
(e_2e_3)\omega^{-1}=e_1, \qquad (e_3e_1)\omega^{-1}=e_2, \qquad (e_1e_2)\omega^{-1}=e_3,
$$

so that $\star(e_ie_j)=e_k$ on the cyclic pairs and $e_1\times e_2=e_3$, $e_2\times e_3=e_1$, $e_3\times e_1=e_2$.

**Corollary (scalar triple product).** For $a,b,c\in V$ three-dimensional and definite,

$$
a\cdot(b\times c)=(a\wedge b\wedge c)\omega^{-1},
$$

the right-hand side being a scalar because $a\wedge b\wedge c$ is of top grade.

**Proof.** Substituting $b\times c=(b\wedge c)\omega^{-1}$ and using the centrality of $\omega^{-1}$ in three dimensions, $a(b\times c)=a(b\wedge c)\omega^{-1}=(a(b\wedge c))\omega^{-1}$. The product $a(b\wedge c)$ has the grades $1$ and $3$; the grade-three part is $a\wedge b\wedge c$, of top grade, and its product with $\omega^{-1}$ is therefore a scalar, while the grade-one part multiplied by $\omega^{-1}$ lies in grade $3-1=2$. Taking the scalar part of $a(b\times c)$ selects the grade-three term, so

$$
a\cdot(b\times c)=\langle a(b\wedge c)\rangle_3\,\omega^{-1}=(a\wedge b\wedge c)\omega^{-1}.
$$

$\square$

## The Biquaternion Case

The star is the operation that the applications of the category call the dual, and in the biquaternion algebra it has a one-line form.

**Proposition.** Let $\mathbb{B}\cong\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$ with the volume element $\omega=e_1e_2e_3$, a central element of square $-1$ that the algebra identifies with the imaginary unit $i$. Then $\omega^{-1}=-i$, so that

$$
\star A=-iA \qquad (A\in\mathbb{B}),
$$

and the star exchanges the vectors with the bivectors and the scalars with the pseudoscalar multiples of the identity.

**Proof.** $\omega^2=-1$ gives $\omega^{-1}=\omega/\omega^2=-\omega=-i$, and the star is right multiplication by $\omega^{-1}$, which here equals left multiplication because $\omega$ is central. The grade exchange is the corollary on the parity of the star in the case $n=3$, and the two grades are those named. $\square$

This is the sign convention of the physics articles, where the dual of a bivector $F$ is written $\tilde F_\star=-i\tilde F$; the identification of $\mathbb{B}$ with $\mathrm{Cl}_{3,0}$ and of the pseudoscalar with $i$ is from *The Biquaternion Algebra as a Clifford Algebra*, and the same operation appears there as the duality that maps a bivector to a vector and a scalar to a pseudoscalar.

**Remark (comparison with the star of the exterior algebra).** The Hodge star of the differential forms of the geometric layer performs the same exchange of a $k$-form with an $(n-k)$-form, and it is the present operation read through the symbol isomorphism $\sigma$ of *The Geometric Product and the Grade Decomposition*. The two differ by a sign on each grade, the sign depending on the grade and on the ordering convention chosen for the complementary basis; the signs displayed in this article are those of the Clifford normalisation, in which $\star\star A=(\omega^2)^{-1}A$ exactly and the cross product takes the form $(a\wedge b)\omega^{-1}$.

## Summary

The volume element $\omega=e_1e_2\cdots e_n$ of an orthogonal basis has square $\omega^2=(-1)^{n(n-1)/2}\prod_iq(e_i)$, is invertible for a non-degenerate form, and is central for odd $n$ and central up to sign for even $n$. Multiplication by $\omega$ raises or lowers the grade to its complement: for $A$ of grade $k$ both $A\omega$ and $\omega A$ lie in grade $n-k$, so that right and left multiplication by $\omega$ are bijections $\mathrm{Cl}_k\to\mathrm{Cl}_{n-k}$; on a basis blade the operation returns the basis blade of the complementary index set, up to sign, and so carries a subspace to its orthogonal complement. The map depends on the orientation, changing sign when the orientation of the basis is reversed.

Normalised by the inverse volume element, the operation is the Hodge star $\star A=A\omega^{-1}$, of square $\star^2=(\omega^2)^{-1}\operatorname{id}$, which preserves the parity grading for even $n$ and exchanges the two parity parts for odd $n$. The square of the star is $+1$ on the four-dimensional Euclidean space, where the six-dimensional space of bivectors splits into self-dual and anti-self-dual halves of dimension three, and $-1$ on the four-dimensional space of signature $(1,3)$, where it is a complex structure on the same space. In three definite dimensions the star of an outer product of two vectors is their cross product, $a\times b=\star(a\wedge b)$, of squared length $q(a)q(b)-B(a,b)^2$, and the scalar triple product is $a\cdot(b\times c)=(a\wedge b\wedge c)\omega^{-1}$. In the biquaternion algebra the star is multiplication by $-i$, the convention of the dual of the physics articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\omega=e_1e_2\cdots e_n$ | Volume element, the pseudoscalar |
| $\omega^2=(-1)^{n(n-1)/2}\prod_iq(e_i)$ | Square of the volume element, a scalar |
| $\omega^{-1}=\omega/\omega^2$ | Inverse of the volume element |
| $A\omega$, $\omega A$ | Right and left complement of $A$ |
| $\mathrm{Cl}_k\to\mathrm{Cl}_{n-k}$ | The grade exchange performed by the complement |
| $\star A=A\omega^{-1}$ | Hodge star |
| $\star^2=(\omega^2)^{-1}\operatorname{id}$ | Square of the star |
| $e_I\omega=\pm e_{I^{c}}$ | Complement of a basis blade |
| $a\times b=\star(a\wedge b)$ | Cross product in three definite dimensions |
| $a\cdot(b\times c)=(a\wedge b\wedge c)\omega^{-1}$ | Scalar triple product |
| $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, $\omega=i$ | Biquaternion case, $\star A=-iA$ |
| $\sigma$ | Symbol isomorphism $\Lambda(V)\to\mathrm{Cl}(V,q)$ |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the volume element, the duality of the grades and the cross product.
- David Hestenes and Garret Sobczyk, *Clifford Algebra to Geometric Calculus* (Reidel, 1984), for the Hodge star $\star A=A\omega^{-1}$ and the duality between the outer and the contracted products.
- Leo Dorst, Daniel Fontijne and Stephen Mann, *Geometric Algebra for Computer Science* (Morgan Kaufmann, 2007), for the complement maps as pairs of dualities on the grades.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the pseudoscalar and its role in the classification of the Clifford algebras.
- Marcel Riesz, *Clifford Numbers and Spinors* (Kluwer, 1993), for the volume element and the duality of the degrees.
