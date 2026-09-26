
# __List of Geometric Forms__

## Introduction

This article lists the forms of the corpus — the bilinear, quadratic, sesquilinear, Hermitian, alternating and symplectic forms — each with the space it is defined on, the invariants that classify it and the article that introduces it. A form is a scalar-valued rule on two vectors, or on one vector, that is linear or conjugate-linear in its arguments; the structure it defines on the space is what the geometric groups of the following catalogues are required to preserve. The list records the invariants — the rank, the radical, the discriminant, the signature, the Witt index — and the classification each classical field affords.

Every entry points to the article that introduces the form or the invariant. The article introduces nothing and proves nothing: it records the classifying data the introducing article establishes, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the forms that the classification separates it lists the cases in which the classification collapses or the correspondence fails: the quadratic forms and the symmetric bilinear forms, which are in bijection only when $2$ is invertible in the base ring; the alternating forms, which are not the skew-symmetric forms in characteristic $2$; the split octonions, whose norm form is isotropic although the octonion norm of the division algebra is not; and the forms over $\mathbb{Q}$ and over a number field, whose classification needs the local invariants and is not read from the signature alone, each with the failure named and the article that records it.

## The Bilinear and Sesquilinear Forms

The bilinear form is the basic datum: a rule linear in each argument, represented by a Gram matrix once a basis is chosen, with the radical measuring its degeneracy. The sesquilinear and Hermitian forms are the case of a non-commutative ring with an involution.

| Form or invariant | Its classifying data | Introduced in |
|---|---|---|
| a bilinear form $B : M \times M \to R$ | bilinearity; the Gram matrix $G_{ij} = B(e_i,e_j)$ in a basis, with $G \mapsto P^TGP$ under a change of basis | *Bilinear Forms* |
| the radical $\operatorname{rad}(B)$ | $\{u : B(u,v) = 0 \ \forall v\}$; the form is non-degenerate when the radical is zero | *Bilinear Forms* |
| the rank $\operatorname{rank}(B)$ | the rank of the Gram matrix; the discriminant $\Delta(B) = \det G \in F^\times/(F^\times)^2$ | *Bilinear Forms* |
| the orthogonal direct sum $B_1 \perp B_2$ | the form on $M_1 \oplus M_2$ with $B(M_1,M_2) = 0$; the operation of the classification | *Bilinear Forms* |
| the isometry group $\operatorname{Isom}(M,B)$ | the linear maps preserving $B$; $\operatorname{O}(M,B)$ in the symmetric case, $\operatorname{Sp}(M,B)$ in the alternating case | *Bilinear Forms*; *List of Classical Geometric Groups* |
| a $\sigma$-sesquilinear form | linear in one argument and $\sigma$-linear in the other for an involution $\sigma$ of the ring | *Hermitian Forms and Involutions* |
| a Hermitian form $s(x,y)$ | $s(x,y) = \sigma(s(y,x))$; the diagonal $q(x) = s(x,x)$ is a quadratic form over the fixed ring | *Hermitian Forms and Involutions* |
| the Hermitian Gram matrix $H$ | $H^\dagger = \sigma(H)^T = H$; the unitary group is its isometry group | *Hermitian Forms and Involutions*; *The Unitary and Symplectic Groups* |
| the trace form $T(x,y) = \operatorname{Tr}(m_{xy})$ | the regular trace of a finite-dimensional algebra; the reduced trace form in the central simple case | *Hermitian Forms and Involutions* |
| the reduced norm form $\operatorname{Nrd}$ | the norm of a central simple algebra of degree $d$; a form of dimension $d^2$ | *Hermitian Forms and Involutions* |

## The Quadratic Forms

A quadratic form is homogeneous of degree two, and it is recovered from its polar form when $2$ is invertible; its classification over the classical fields is the content of Sylvester's law and of the rank.

| Form or invariant | Its classifying data | Introduced in |
|---|---|---|
| a quadratic form $q : M \to R$ | $q(av) = a^2q(v)$ and the polar identity; the polar form $B$ with $q(v) = B(v,v)$ | *Quadratic Forms and Polarisation* |
| the passage to the polar form | a bijection between quadratic and symmetric bilinear forms when $2$ is invertible; a genuine obstruction otherwise | *Quadratic Forms and Polarisation* |
| the diagonal form $\langle a_1,\ldots,a_n\rangle$ | $\sum_i a_ix_i^2$; the diagonalisation of a form over a field of characteristic not $2$ | *Quadratic Forms and Polarisation* |
| Sylvester's law of inertia | over $\mathbb{R}$ a form is classified by its signature $(p,r)$; the indices are invariant | *Quadratic Forms and Polarisation* |
| the signature $\sigma(q) = p - r$ and the rank $p + r$ | the real classification; the complex classification is the rank alone | *Quadratic Forms and Polarisation*; *Pseudo-Riemannian and Lorentzian Geometry* |
| the discriminant $\Delta(q)$ | $a_1\cdots a_n \in F^\times/(F^\times)^2$; an invariant of the isometry class | *Quadratic Forms and Polarisation*; *Bilinear Forms* |
| the hyperbolicity and the isotropic vectors | a form is isotropic when $q(v) = 0$ for some $v \neq 0$; the hyperbolic plane is the model | *Witt's Theorems* |
| the norm forms of the algebras | $N(x) = x\bar x$ on $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B}$ and $\mathbb{O}$; a composition law $N(xy) = N(x)N(y)$ only in dimensions $1$, $2$, $4$, $8$ | *Quadratic Forms over Algebras and Norm Forms* |
| a Pfister form $\langle\!\langle a_1,\ldots,a_n\rangle\!\rangle$ | the norm form of a composition algebra of dimension $2^n$; the tensor product $\bigotimes_i\langle 1,-a_i\rangle$ | *Quadratic Forms over Algebras and Norm Forms*; *The Witt Group and the Grothendieck–Witt Ring* |

## The Alternating and Symplectic Forms

An alternating form satisfies $\omega(u,u) = 0$, which over a field of characteristic not $2$ is the skew-symmetry of its matrix; the non-degenerate alternating forms are the symplectic forms, and their normal form is the linear Darboux theorem.

| Form or invariant | Its classifying data | Introduced in |
|---|---|---|
| an alternating form $\omega$ | $\omega(u,u) = 0$ for all $u$; equivalently $\omega(u,v) = -\omega(v,u)$ when $2$ is invertible | *Symplectic Forms and Poisson Brackets*; *Bilinear Forms* |
| an alternating $2$-form as a wedge | an element of $\Lambda^2(V^*)$; the algebra of alternating forms is $\Lambda(V^*)$ | *The Determinant and Alternating Forms* |
| the Pfaffian | $\operatorname{Pf}(\Omega)$ for an alternating matrix of even size; $\det\Omega = \operatorname{Pf}(\Omega)^2$, so a symplectic map has determinant $1$ | *The Determinant and Alternating Forms*; *Symplectic Forms and Poisson Brackets* |
| a symplectic form | a non-degenerate alternating form on a finite-dimensional space; the dimension is even | *Symplectic Forms and Poisson Brackets* |
| the linear Darboux normal form | the symplectic basis $e_1,\ldots,e_n,f_1,\ldots,f_n$ with $\omega(e_i,f_j) = \delta_{ij}$; $\omega_0$ has matrix $J$ | *Symplectic Forms and Poisson Brackets* |
| the symplectic group $Sp(V,\omega)$ | the isometries of $\omega$; $A^TJA = J$; contained in $SL(V)$ by the Pfaffian | *Symplectic Forms and Poisson Brackets*; *The Unitary and Symplectic Groups* |
| the Lagrangians | the maximal totally isotropic subspaces; the Lagrangian Grassmannian | *Symplectic Forms and Poisson Brackets*; *Symplectic Geometry* |

## The Classification Theorems and Their Invariants

The classification of quadratic forms over a field is governed by Witt's theorems; over $\mathbb{R}$, $\mathbb{C}$, $\mathbb{F}_q$ and $\mathbb{Q}$ it takes the forms recorded below, and the Witt ring is the algebraic home of the invariants.

| Theorem or invariant | Its statement or classifying data | Introduced in |
|---|---|---|
| the Witt extension theorem | every isometry between subspaces of a non-degenerate quadratic space extends to the whole space; complements exist | *Witt's Theorems* |
| the Witt index $m$ | the common dimension of the maximal totally isotropic subspaces; $V \cong V_0 \perp mH$ with $V_0$ anisotropic | *Witt's Theorems* |
| the Witt cancellation theorem | $q \perp q_1 \cong q \perp q_2 \Rightarrow q_1 \cong q_2$ for non-degenerate forms; the basis of the Witt ring | *Witt's Theorems* |
| the classification over $\mathbb{R}$ | the signature $(p,r)$ by Sylvester's law; rank and signature | *Quadratic Forms and Polarisation* |
| the classification over $\mathbb{C}$ | the rank alone; every non-degenerate complex form is $\langle 1,\ldots,1\rangle$ | *Quadratic Forms and Polarisation*; *Witt's Theorems* |
| the classification over $\mathbb{F}_q$, $q$ odd | the dimension and the discriminant; the number of maximal totally isotropic subspaces of $mH$ is $\prod_{i=0}^{m-1}(q^i+1)$ | *Witt's Theorems* |
| the Hasse–Minkowski principle | the classification over a number field by the completions; the local invariants determine the global form | *Witt's Theorems* |
| the Witt ring $W(F)$ | the isometry classes modulo the hyperbolic forms, under $\perp$ and $\otimes$; the Grothendieck–Witt ring $GW(F)$ above it | *The Witt Group and the Grothendieck–Witt Ring* |
| the invariants $\dim$, $\Delta$, $\operatorname{sign}$ | the dimension, the discriminant and the total signature $W(F) \to \prod_P\mathbb{Z}$ | *The Witt Group and the Grothendieck–Witt Ring* |
| the Hasse invariant $e_2$ | the invariant $I^2/I^3 \hookrightarrow \operatorname{Br}_2(F)$; the Milnor K-theory quotients $I^n/I^{n+1}$ | *The Witt Group and the Grothendieck–Witt Ring* |

## The Forms on the Number Systems

The norm forms of the number systems are the examples through which the general theory is read, and the Cayley–Dickson doubling produces them in dimensions one, two, four and eight.

| Space and form | The form and its properties | Introduced in |
|---|---|---|
| $\mathbb{C}$ with $N(z) = z\bar z$ | the positive definite norm form of dimension $2$; a composition law | *Quadratic Forms over Algebras and Norm Forms*; *The Complex Numbers* |
| $\mathbb{H}$ with $N(q) = q\bar q$ | the positive definite quaternion norm of dimension $4$; a composition law; anisotropic | *Quadratic Forms over Algebras and Norm Forms*; *Quaternion Algebra* |
| $\mathbb{B}$ with $N(q) = q\bar q$ | the complex-valued biquaternion norm; the real part and imaginary part are forms of signature $(4,4)$ | *Quadratic Forms over Algebras and Norm Forms*; *The Biquaternion Algebra as a Clifford Algebra* |
| the split biquaternions $\mathbb{H}_{\mathbb{D}}$ | a norm form that is isotropic; the split form of the quaternion norm | *Quadratic Forms over Algebras and Norm Forms*; *Split-Biquaternions and Hyperbolic Geometry* |
| $\mathbb{O}$ with $N(x) = x\bar x$ | the octonion norm of dimension $8$; a composition law; anisotropic | *Quadratic Forms over Algebras and Norm Forms*; *Octonion Algebra* |
| the split octonions | the isotropic norm form of dimension $8$; the $\mu = +1$ double of $\mathbb{H}_{\mathbb{D}}$ | *Quadratic Forms over Algebras and Norm Forms* |
| the quadric $\mathcal{Q}(Q)$ | the projective quadric $\{[x] : Q(x) = 0\}$ of an $A$-valued form | *Quadratic Forms over Algebras and Norm Forms*; *Projective Geometry* |

## Non-examples and Warnings

| Object | Why the expected statement fails | Introduced in |
|---|---|---|
| a quadratic form over $\mathbb{F}_2$ | the polar form does not determine the quadratic form when $2$ is not invertible; the correspondence is an obstruction, not a bijection | *Quadratic Forms and Polarisation* |
| an alternating form in characteristic $2$ | it is not the same as a skew-symmetric form; skew-symmetry with $\omega(u,u) = 0$ is the condition available over every ring | *The Determinant and Alternating Forms*; *Symplectic Forms and Poisson Brackets* |
| the split octonions | their norm form is isotropic, unlike the norm of the division algebra $\mathbb{O}$; the two are different forms of the same dimension | *Quadratic Forms over Algebras and Norm Forms* |
| the classification over $\mathbb{Q}$ | it is not read from the signature alone; the Hasse–Minkowski principle needs the local invariants at the completions | *Witt's Theorems* |
| the Hermitian form over a non-commutative ring | the diagonal $q(x) = s(x,x)$ is a quadratic form over the fixed ring and not over the base; the transfer is part of the theory | *Hermitian Forms and Involutions* |
| a degenerate form, $\langle 0\rangle$ | its matrix is not invertible and there is no discriminant in $F^\times/(F^\times)^2$; the radical is the whole space | *Bilinear Forms* |
| a form of odd dimension over a finite field | the discriminant alone does not classify it in characteristic $2$; the classification stated above needs $q$ odd | *Witt's Theorems* |

Objects that a reader may expect in a list of geometric forms, and does not find here.

| Object | Why it is not listed | Introduced in |
|---|---|---|
| differential forms | they are forms on the tangent bundle of a manifold, a Part III construction, and are catalogued with the manifolds | *Differential Forms and Stokes' Theorem* |
| the integral forms of a lattice | they are recorded with the geometric lattices and the integral quadratic forms | *List of Geometric Lattices and Integral Forms* |
| the symplectic form of a symplectic manifold | it is a closed non-degenerate $2$-form on a manifold; the algebraic form is listed here and the manifold there | *Symplectic Geometry*; *Symplectic and Contact Topology* |
| the Killing form of a Lie algebra | an invariant symmetric bilinear form on a Lie algebra, recorded with the structure theory | *Structure of Lie Algebras* |
| the Petersson inner product and the automorphic forms | the Hermitian forms of the analytic theory belong to a different catalogue | *Automorphic Forms* |

## Summary

This article has listed the forms of the corpus: the bilinear forms with their Gram matrices, radicals and discriminants; the sesquilinear and Hermitian forms with an involution, their trace forms and reduced norms; the quadratic forms with their polar forms, diagonalisations, signatures and discriminants, and the norm forms of $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B}$, the split biquaternions and $\mathbb{O}$; the alternating and symplectic forms with the Pfaffian, the Darboux normal form and the Lagrangians; and the classification theorems — Witt's extension, index and cancellation, Sylvester's law, the classifications over $\mathbb{C}$ and $\mathbb{F}_q$, the Hasse–Minkowski principle, and the Witt and Grothendieck–Witt rings with their invariants. Beside the examples stand the non-examples: the characteristic-$2$ failures of the polar correspondence and of alternation, the isotropic split octonion norm, the forms over $\mathbb{Q}$ that need their local invariants, and the degenerate forms without a discriminant. The list introduces and proves nothing; it is the index of the forms of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following, and they are the symbols of the articles that introduce them.

| Symbol | Meaning |
|---|---|
| $B$ | a bilinear form, symmetric unless stated |
| $G = (G_{ij})$ | the Gram matrix of a bilinear form in a basis |
| $\operatorname{rad}(B)$, $\operatorname{rank}(B)$ | the radical and the rank of a form |
| $\Delta$ | the discriminant, in $F^\times/(F^\times)^2$ |
| $\perp$ | the orthogonal direct sum |
| $q$ | a quadratic form; $B$ its polar form, $q(v) = B(v,v)$ |
| $\langle a_1,\ldots,a_n\rangle$ | the diagonal form $\sum_i a_ix_i^2$ |
| $\sigma(q) = p - r$ | the signature of a real quadratic form, of positive index $p$ and negative index $r$ |
| $H$ | the hyperbolic plane |
| $m$ | the Witt index |
| $\omega$, $\omega_0$, $J$ | an alternating $2$-form, the standard symplectic form, its matrix |
| $\operatorname{Pf}$ | the Pfaffian |
| $Sp(V,\omega)$ | the symplectic group |
| $W(F)$, $GW(F)$, $I$ | the Witt ring, the Grothendieck–Witt ring, the fundamental ideal |
| $\langle\!\langle a_1,\ldots,a_n\rangle\!\rangle$ | a Pfister form |
| $N$, $\operatorname{Nrd}$, $\operatorname{Tr}$, $\operatorname{Trd}$ | a norm form, the reduced norm, the trace and reduced trace |
| $s(x,y)$, $\sigma$, $A^\sigma$ | a sesquilinear form, an involution, its fixed ring |

## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the classification of quadratic forms, Witt's theorems, the Witt ring and the Hasse–Minkowski principle.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for bilinear, quadratic, Hermitian and alternating forms in one account.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions, Hermitian forms and the reduced norm of a central simple algebra.
- Michael Artin, *Geometric Algebra* (Interscience, 1957), for the classical treatment of the forms and of the orthogonal and symplectic groups they define.
