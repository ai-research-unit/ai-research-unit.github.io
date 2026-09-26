
# __Octonions and the Exceptional Lie Groups__

## Introduction

This article is the second half of the representations slot of the octonion system. It describes how the exceptional Lie groups are built out of the octonion algebra: the derivation algebra and the automorphism group $G_2$ directly, the group $F_4$ as the automorphism group of the exceptional Jordan algebra of Hermitian $3\times3$ matrices over $\mathbb{O}$, the groups $E_6$, $E_7$ and $E_8$ from the Freudenthal triple systems and from the magic square, and the associated geometries. The article is a construction of these objects from the octonions, not a classification of them: the classification of the simple Lie algebras and of the simple Lie groups is that of the Part I companions *Root Systems and Classification* and *Finite Simple Groups of Lie Type*, and it is cited and not re-derived here.

The article takes the multiplication, the Fano rule and the associator from *Octonion Algebra*, the norm and the inner product from *Octonion Norm and Invertibility*, and the representations of $\mathfrak{g}_2$ and the triality of $\operatorname{Spin}(8)$ from *Octonion Representations*. The exceptional Jordan algebra and the magic square are standard constructions; their sources are listed in the Further Reading. The geometry built on the exceptional groups, and the holonomy groups $G_2$ and $\operatorname{Spin}(7)$ of Part II, are not covered here.

**Conventions.** As in *Octonion Algebra*, the basis is $e_0,\dots,e_7$ with $e_k^2 = -e_0$ for $k\geq1$, the Fano lines oriented as in that article, the conjugation $\bar x$, the imaginary space $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$, the inner product $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$ and the cross product $u\times v = \operatorname{Vect}(uv)$ on the imaginary space. The operators $L_x,R_x$ are left and right multiplication; the commutator of endomorphisms is written $[A,B] = AB - BA$, so that the associator and the commutator are distinct notations and must not be confused.

## The Automorphism Group and the Derivation Algebra

### The Derivations

**Definition.** A **derivation** of $\mathbb{O}$ is a linear map $d : \mathbb{O}\to\mathbb{O}$ with

$$
d(xy) = (dx)y + x(dy) \qquad \text{for all }x,y\in\mathbb{O},
$$

and $\operatorname{Der}(\mathbb{O})$ is the space of all derivations, a Lie subalgebra of $\operatorname{End}(\mathbb{O})$ under the commutator.

**Theorem.** For imaginary $x,y\in\mathbb{O}$ the endomorphism

$$
D_{x,y} = [L_x,L_y] + [L_x,R_y] + [R_x,R_y]
$$

is a derivation of $\mathbb{O}$, and the derivations $D_{e_i,e_j}$ for $1\leq i,j\leq 7$ span a real vector space of dimension fourteen. Hence

$$
\operatorname{Der}(\mathbb{O}) = \operatorname{span}\{D_{e_i,e_j} : 1\leq i,j\leq 7\}
$$

is the exceptional simple Lie algebra $\mathfrak{g}_2$, and it is contained in $\mathfrak{so}(7)$, acting trivially on $e_0$ and irreducibly on $\operatorname{Im}\mathbb{O}$.

*Proof.* The verification that each $D_{x,y}$ satisfies the Leibniz rule is finite and is carried out on the basis with the Fano rule; the spanning statement is a linear computation on the $49$ operators $D_{e_i,e_j}$, whose rational rank is fourteen. That the resulting algebra is the exceptional algebra $\mathfrak{g}_2$ of rank two is the standard identification, with the standard sources cited; the vanishing on $e_0$ is $D_{x,y}e_0 = x y + xy - yx - xy - xy + yx$ expanded from the definition, which is zero, and skew-adjointness follows from the derivation of the identity $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$. $\square$

### The Group $G_2$

**Theorem.** The automorphism group $\operatorname{Aut}(\mathbb{O})$ is a compact, connected, simply connected simple Lie group $G_2$ of dimension fourteen, with Lie algebra $\mathfrak{g}_2 = \operatorname{Der}(\mathbb{O})$, and it acts transitively on the unit sphere of the imaginary space with isotropy a copy of $SU(3)$:

$$
S^6 = G_2/SU(3), \qquad \dim G_2 = 14,\ \dim S^6 = 6,\ \dim SU(3) = 8 .
$$

Every automorphism preserves the norm form, hence $G_2\subset SO(7)$ for the action on $\operatorname{Im}\mathbb{O}$, and it is exactly the stabiliser of the **associative three-form**

$$
\varphi(u,v,w) = \langle u\times v, w\rangle, \qquad u,v,w\in\operatorname{Im}\mathbb{O},
$$

so that $G_2 = \{\,g\in SO(7) : g^*\varphi = \varphi\,\}$.

*Proof.* Automorphisms of a composition algebra preserve the norm form, so $G_2\subset O(8)$; they fix $e_0$, hence preserve $\operatorname{Im}\mathbb{O}$ and the orientation, so $G_2\subset SO(7)$. The stabiliser of the three-form inside $SO(7)$ contains $G_2$ by invariance of the cross product, and the reverse inclusion is the standard theorem that the three-form determines the multiplication; the dimension count $21 - 14 = 7$ shows that the stabiliser has dimension at most twenty-one and that the orbit of the three-form has dimension at least zero; the sharp statements are standard, with the sources cited. The transitivity on $S^6$ with isotropy $SU(3)$ is the standard orbit decomposition of the imaginary units. $\square$

**Proposition.** The action of $G_2$ on $\operatorname{Im}\mathbb{O}$ is irreducible, and the stabiliser of an imaginary unit $u$ is $SU(3)$ acting on the orthogonal complement of $u$ as the standard six-dimensional real representation of $SU(3)$; the stabiliser of an oriented two-plane is the subgroup $SU(2)\times SU(2)$ preserving the quaternion subalgebra generated by the plane.

*Proof.* The isotropy statements are those of the homogeneous space $G_2/SU(3) = S^6$; the stabiliser of a quaternion subalgebra is the automorphism group of $\mathbb{H}$ inside $G_2$, namely $SO(3)\times SO(3)\cong SU(2)\times SU(2)$ up to the central quotient, acting on the two three-dimensional subspaces of the subalgebra. $\square$

The three-form $\varphi$ is the octonionic **associative calibration**: a three-dimensional subspace of $\operatorname{Im}\mathbb{O}$ on which the restriction of $\varphi$ attains the value one is exactly an oriented quaternion subalgebra, that is, one of the Fano lines, and this is the beginning of the geometry of exceptional holonomy treated.

## The Exceptional Jordan Algebra

### Hermitian Matrices over the Octonions

**Definition.** The **exceptional Jordan algebra** is the real vector space

$$
\mathfrak{h}_3(\mathbb{O}) = \left\{A\in M_3(\mathbb{O}) : A^* = A\right\}, \qquad A = \begin{pmatrix}\alpha & x & y\\ \bar x & \beta & z\\ \bar y & \bar z & \gamma\end{pmatrix}, \quad \alpha,\beta,\gamma\in\mathbb{R},\ x,y,z\in\mathbb{O},
$$

with the symmetrised product $A\circ B = \tfrac{1}{2}(AB + BA)$.

**Proposition.** $\mathfrak{h}_3(\mathbb{O})$ is a real vector space of dimension $3 + 3\cdot 8 = 27$; the product $\circ$ is commutative and satisfies the Jordan identity $(A\circ B)\circ(A\circ A) = A\circ(B\circ(A\circ A))$, and the algebra is **exceptional**, that is, it is not isomorphic to a subalgebra of an associative algebra with the symmetrised product.

*Proof.* The dimension count is immediate: three real diagonal entries and three octonion off-diagonal entries, the conjugate entries determined. The Jordan identity is the standard theorem on Hermitian matrices over a composition algebra, verified by a finite expansion using the alternating property of the associator; exceptionality is the theorem of Albert, quoted as standard. $\square$

The product $\circ$ requires the two octonion products $xy$ and $yx$ and is well defined although the individual products $AB$ and $BA$ of the matrices depend on the bracketing: the symmetrisation and the Hermitian symmetry together kill the associator terms.

**Definition.** The **determinant** of $A\in\mathfrak{h}_3(\mathbb{O})$ is the real cubic form

$$
\det A = \alpha\beta\gamma + 2\operatorname{Sc}(xyz) - \alpha\lvert z\rvert^2 - \beta\lvert y\rvert^2 - \gamma\lvert x\rvert^2 ,
$$

and the **trace** is $\operatorname{tr}A = \alpha + \beta + \gamma$.

**Theorem.** The determinant is invariant under the product in the sense of the identities of a Jordan algebra of degree three, and its polarisation defines a non-degenerate symmetric trilinear form on $\mathfrak{h}_3(\mathbb{O})$; the group of linear transformations preserving the determinant is

$$
F_4 = \operatorname{Aut}(\mathfrak{h}_3(\mathbb{O})) = \left\{g\in GL_{27}(\mathbb{R}) : \det(gA) = \det A\right\},
$$

a compact, connected, simply connected simple Lie group of dimension $52$ and rank four.

*Proof.* The determinants of the three principal $2\times2$ minors together with $\det$ give the structure of a cubic Jordan algebra; closedness under the inverse and the identities are the standard ones of a Jordan algebra of degree three, verified by expansion. The identification of the automorphism group with the compact $F_4$ and the dimension count $\dim F_4 = 52$ are the standard theorem of Chevalley and Schafer, quoted with the sources cited. $\square$

The appearance of the associative triple $\operatorname{Sc}(xyz)$ in the determinant is the way in which the octonion multiplication enters: the triple product is alternating in $x,y,z$, so the three bracketings agree on its real part, and the non-associativity of $\mathbb{O}$ does not reach the determinant.

### The Freudenthal Triple System and the Groups $E_6$, $E_7$

**Definition.** The **Freudenthal triple system** associated with $\mathfrak{h}_3(\mathbb{O})$ is the pair $(\mathbb{R}\oplus\mathbb{R}\oplus\mathfrak{h}_3(\mathbb{O})\oplus\mathfrak{h}_3(\mathbb{O}), [\cdot,\cdot,\cdot])$ with the triple product built from the determinant, the adjoint (the quadratic map $A\mapsto A^\# = A\circ A - \operatorname{tr}(A)A + \cdots$) and the trace pairing.

**Theorem.** The groups associated with the exceptional Jordan algebra are the following.

1. The reduced structure group of the cubic form, that is the group of linear maps preserving the determinant up to a scalar, is the group $E_6$; in its simply connected form it is a compact simple Lie group of dimension $78$ and rank six, and the automorphism group $F_4$ sits inside it as the subgroup fixing the trilinear form, giving the chain
$$
F_4\subset E_6, \qquad 52 < 78 .
$$
2. The automorphism group of the Freudenthal triple system is the group $E_7$, of dimension $133$ and rank seven, acting on a fifty-six-dimensional space; the associated geometry has the Freudenthal triple system as its model space.
3. The group constructed from the pair $(\mathbb{O},\mathbb{O})$ in the magic square is $E_8$, of dimension $248$ and rank eight.

*Proof.* These are the standard identifications of the exceptional groups with the structure groups of the exceptional Jordan algebra and its Freudenthal triple system; the dimensions $52$, $78$, $133$, $248$ and the ranks $4$, $6$, $7$, $8$ are those of the simple Lie algebras $\mathfrak{f}_4$, $\mathfrak{e}_6$, $\mathfrak{e}_7$, $\mathfrak{e}_8$ classified in *Root Systems and Classification*, and the simply connected compact groups realising them are those of *Finite Simple Groups of Lie Type*. The present article constructs the algebras from $\mathbb{O}$ and cites the classification rather than repeating it. $\square$

**Remark.** The dimension count is a check on the chain: $\dim F_4 = 52 = 26 + 26$ decomposes as twice the traceless part of $\mathfrak{h}_3(\mathbb{O})$, of dimension $27 - 1 = 26$, and $\dim E_6 = 78 = 52 + 26$ adds the traceless part once more; the two $26$-dimensional pieces and the $F_4$ are respectively the isotropy, the translations and the structure group, as in the realisation of $E_6$ on the $27$-dimensional space $\mathfrak{h}_3(\mathbb{O})$.

## The Magic Square

### The Freudenthal–Tits Construction

**Theorem (Freudenthal–Tits).** There is a construction that assigns to every pair $A,B$ of real composition algebras of dimensions $1,2,4,8$ a real Lie algebra $\mathfrak{L}(A,B)$, natural in the pair and symmetric in $A$ and $B$, built from the derivations of $A$ and $B$, the traceless parts of $A$ and $B$ with respect to their norm forms, and the tensor products of these pieces. The resulting algebras are those of the following table; the entry in row $A$ and column $B$ is the simple Lie algebra obtained.

| $\mathfrak{L}(A,B)$ | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{H}$ | $\mathbb{O}$ |
|---|---|---|---|---|
| $\mathbb{R}$ | $\mathfrak{su}(2)$ | $\mathfrak{su}(3)$ | $\mathfrak{sp}(3)$ | $\mathfrak{f}_4$ |
| $\mathbb{C}$ | $\mathfrak{su}(3)$ | $\mathfrak{su}(3)\oplus\mathfrak{su}(3)$ | $\mathfrak{su}(6)$ | $\mathfrak{e}_6$ |
| $\mathbb{H}$ | $\mathfrak{sp}(3)$ | $\mathfrak{su}(6)$ | $\mathfrak{so}(12)$ | $\mathfrak{e}_7$ |
| $\mathbb{O}$ | $\mathfrak{f}_4$ | $\mathfrak{e}_6$ | $\mathfrak{e}_7$ | $\mathfrak{e}_8$ |

The table is symmetric, and the exceptional algebras $\mathfrak{f}_4,\mathfrak{e}_6,\mathfrak{e}_7,\mathfrak{e}_8$ occur exactly in the positions in which at least one of $A$ and $B$ is the octonion algebra: the construction applied to the three classical composition algebras alone returns only the classical algebras of the first three rows and columns.

*Proof.* The construction and the identification of the entries are the standard Freudenthal–Tits magic square; the dimensions of the entries are those of the simple Lie algebras listed in *Root Systems and Classification*, namely $3$, $8$, $21$, $52$, $16$, $35$, $78$, $66$, $133$ and $248$, and the symmetry is the symmetry of the construction. $\square$

The magic square produces the four exceptional algebras $\mathfrak{f}_4,\mathfrak{e}_6,\mathfrak{e}_7,\mathfrak{e}_8$ exactly at the positions in which an octonion factor is available, over and above the exceptional algebra $\mathfrak{g}_2$, which is the derivation algebra of $\mathbb{O}$ itself; the construction applied to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ alone returns the classical algebras of the first three rows and columns. The classification of the simple Lie algebras as $\mathfrak{a}_n$, $\mathfrak{b}_n$, $\mathfrak{c}_n$, $\mathfrak{d}_n$ and the five exceptionals $\mathfrak{g}_2,\mathfrak{f}_4,\mathfrak{e}_6,\mathfrak{e}_7,\mathfrak{e}_8$ is that of *Root Systems and Classification*, and the present article's contribution is the construction of the exceptional entries from the octonion algebra.

### The Cayley Plane and the Rosenfeld Planes

**Definition.** The **Cayley plane** is the homogeneous space

$$
\mathbb{OP}^2 = F_4/\operatorname{Spin}(9),
$$

of real dimension $16$, the space of idempotents of trace one in $\mathfrak{h}_3(\mathbb{O})$ that are of rank one, that is, the set of projections onto lines of the exceptional Jordan algebra.

**Theorem.** The Cayley plane is a compact symmetric space of rank one with the following properties: it is simply connected, it has a transitive group $F_4$ with isotropy $\operatorname{Spin}(9)$ acting on the tangent space by its sixteen-dimensional spin representation, it is a projective plane in the sense of the incidence axioms of a Moufang plane, and it admits a cell decomposition with cells of dimensions $0$, $8$ and $16$, so that its rational cohomology is that of a projective plane with the degrees $1$, $8$ and $16$.

*Proof.* The homogeneous description is the orbit decomposition of $F_4$ on the rank-one idempotents of $\mathfrak{h}_3(\mathbb{O})$; the compactness and connectedness are those of the groups, the simplicity and rank one follow from the transitivity and the irreducible isotropy representation; the incidence structure is the Moufang plane over $\mathbb{O}$ constructed from the rank-one and rank-two idempotents, where the octonion multiplication is used only through the determinant; the cell decomposition and the cohomology are the standard description of the Cayley plane. The sources are cited in the Further Reading. $\square$

The Cayley plane cannot be coordinatised by a field, and its lines meet in a single point rather than forming a projective geometry in the sense of the associative cases; the obstruction is the non-associativity of $\mathbb{O}$, and the plane is the exact geometric object that survives. The higher exceptional analogues are the **Rosenfeld planes**, the projective planes over $\mathbb{C}\otimes\mathbb{O}$, $\mathbb{H}\otimes\mathbb{O}$ and $\mathbb{O}\otimes\mathbb{O}$, whose automorphism groups are $E_6$, $E_7$ and $E_8$; they are taken up with the exceptional geometry.

## Summary

The exceptional Lie groups are constructed from the octonion algebra as follows. The derivation algebra $\operatorname{Der}(\mathbb{O})$ is spanned by the operators $D_{x,y} = [L_x,L_y] + [L_x,R_y] + [R_x,R_y]$ with $x,y$ imaginary, it has dimension fourteen, and it is the exceptional simple Lie algebra $\mathfrak{g}_2$; its group is $G_2 = \operatorname{Aut}(\mathbb{O})$, compact connected simply connected of dimension fourteen, acting on $\operatorname{Im}\mathbb{O}$ with $S^6 = G_2/SU(3)$ and characterised as the stabiliser in $SO(7)$ of the associative three-form $\varphi(u,v,w) = \langle u\times v,w\rangle$.

The exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$ of Hermitian $3\times3$ matrices over $\mathbb{O}$, of dimension $27$, with the symmetrised product and the cubic determinant, is exceptional (not special); its automorphism group is $F_4$, of dimension $52$ and rank four, and the group preserving the determinant up to scale is $E_6$, of dimension $78$; the automorphism group of the associated Freudenthal triple system is $E_7$, of dimension $133$, and the Freudenthal–Tits magic square, whose rows and columns are the composition algebras, produces $E_8$, of dimension $248$, from the pair $(\mathbb{O},\mathbb{O})$. The exceptional algebras occur in the last row and column of the square, which is the precise sense in which the octonions are responsible for them.

Geometrically, the octonions produce the Cayley plane $\mathbb{OP}^2 = F_4/\operatorname{Spin}(9)$, of dimension sixteen, a Moufang plane with cells in dimensions $0$, $8$ and $16$, together with the Rosenfeld planes of $E_6$, $E_7$ and $E_8$. The classification of the simple Lie algebras and groups is presupposed, in *Root Systems and Classification* and *Finite Simple Groups of Lie Type*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$, $e_0,\dots,e_7$ | Octonion algebra and its basis, $e_k^2 = -e_0$ |
| $L_x$, $R_x$ | Left and right multiplication; $[A,B] = AB - BA$ |
| $D_{x,y} = [L_x,L_y] + [L_x,R_y] + [R_x,R_y]$ | Derivation of $\mathbb{O}$ for imaginary $x,y$ |
| $\mathfrak{g}_2 = \operatorname{Der}(\mathbb{O})$, $G_2 = \operatorname{Aut}(\mathbb{O})$ | Exceptional Lie algebra and group, $14$-dimensional |
| $S^6 = G_2/SU(3)$ | Imaginary unit sphere; isotropy $SU(3)$ |
| $\varphi(u,v,w) = \langle u\times v,w\rangle$ | Associative three-form, $G_2 = \operatorname{Stab}_{SO(7)}\varphi$ |
| $\mathfrak{h}_3(\mathbb{O})$ | Exceptional Jordan algebra, Hermitian $3\times3$ matrices, $\dim 27$ |
| $A\circ B = \tfrac12(AB+BA)$, $\operatorname{tr}$, $\det$ | Jordan product, trace, cubic determinant |
| $F_4 = \operatorname{Aut}(\mathfrak{h}_3(\mathbb{O}))$ | Compact simple group, $\dim 52$, rank $4$ |
| $E_6$, $E_7$, $E_8$ | Structure group of the determinant ($78$), Freudenthal triple system ($133$), magic square ($248$) |
| $\mathbb{OP}^2 = F_4/\operatorname{Spin}(9)$ | Cayley plane, $\dim 16$, Moufang plane |
| $\mathfrak{L}(A,B)$ | Freudenthal–Tits algebra of a pair of composition algebras |





## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for $\mathfrak{h}_3(\mathbb{O})$, its determinant and the groups $F_4$ and $E_6$.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the derivations $D_{x,y}$, the automorphism group and the exceptional Jordan algebra.
- Hans Freudenthal, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 1968), for the triple systems and the construction of $E_7$ and $E_8$.
- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* **39** (2002), 145–205, for the magic square, the Cayley plane and the survey of the constructions.
- Ichiro Yokota, *Exceptional Lie Groups* (Springer, 2009), for the explicit realisations of $G_2$, $F_4$, $E_6$, $E_7$ and $E_8$ from the octonions.
- Jacques Tits, "Algèbres alternatives, algèbres de Jordan et algèbres de Lie exceptionnelles", *Indagationes Mathematicae* **28** (1966), 223–237, for the original construction of the magic square.
