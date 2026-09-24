
# __Octonion Representations__

## Introduction

This article is the representations slot of the octonion system. Its subject is what can replace the representation theory of an algebra when the algebra is not associative. The article shows that the ordinary notion of a module fails completely for $\mathbb{O}$ — every unital bimodule over the octonions is zero — and that the representations which do exist are of two kinds: the multiplication operators, which are linear and injective but not multiplicative, and the ordinary representations of the structure objects $\operatorname{Der}(\mathbb{O}) = \mathfrak{g}_2$ and $\operatorname{Aut}(\mathbb{O}) = G_2$ together with their relative $\operatorname{Spin}(7)$ and $\operatorname{Spin}(8)$.

The article takes the multiplication and the identities of *Octonion Algebra*, the norm and the invertibility theory of *Octonion Norm and Invertibility*, and the model of the quaternion case from *Quaternion Representations*. The general theory of modules over an associative algebra, of algebras of endomorphisms and of the enveloping algebra of a Lie algebra is that of the Part I companions *Modules*, *Algebras: A General Introduction* and *Universal Enveloping Algebras*; the Clifford algebras and their classification are the subject of *Clifford Algebras in Finite Dimensions* and *Spin Representations and Clifford Modules*, and the identification of the number systems with Clifford algebras is the subject of *The Number Systems as Clifford Algebras*. The finite-dimensional representation theory of $G_2$ and its role in the exceptional groups is taken up aga; the present article states the representations and does not derive the classification of the exceptional groups.

**Conventions.** The octonion algebra has basis $e_0,\dots,e_7$ with the Fano multiplication of *Octonion Algebra*, inner product $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$ and norm $\lvert x\rvert^2 = \langle x,x\rangle$. For $x\in\mathbb{O}$ the operators $L_x,R_x\in\operatorname{End}_{\mathbb{R}}(\mathbb{O})$ are left and right multiplication, $L_x(y) = xy$, $R_y(x) = xy$. The associator is $[x,y,z] = (xy)z - x(yz)$.

## The Failure of an Associative Module Theory

### Bimodules over a Non-Associative Algebra

**Definition.** Let $A$ be a non-associative algebra with identity over $\mathbb{R}$. A **bimodule** over $A$ is a real vector space $M$ with bilinear maps $A\times M\to M$, $(a,m)\mapsto am$, and $M\times A\to M$, $(m,a)\mapsto ma$, satisfying

$$
a(bm) = (ab)m, \qquad (ma)b = m(ab), \qquad a(mb) = (am)b
$$

for all $a,b\in A$ and $m\in M$. The bimodule is **unital** if $e_0m = me_0 = m$ for all $m$.

For an associative algebra these are the usual three axioms of a bimodule; for a non-associative algebra they are the strongest reasonable demand, since they require the two-sided action to be compatible with the product of $A$ in every order of association. The first axiom says that the left action is an algebra homomorphism $A\to\operatorname{End}(M)$; the second says the same for the right action, with reversed order; the third says the two actions commute in the appropriate sense.

**Theorem.** Let $M$ be a unital bimodule over the octonion algebra $\mathbb{O}$. Then $M = 0$.

*Proof.* By the first axiom the map $a\mapsto L^M_a$, where $L^M_a(m) = am$, is a homomorphism of $\mathbb{O}$ into the associative algebra $\operatorname{End}(M)$: $L^M_{ab} = L^M_aL^M_b$. In an associative algebra the associator of three elements vanishes, so

$$
L^M_{[x,y,z]} = L^M_{(xy)z} - L^M_{x(yz)} = L^M_{xy}L^M_z - L^M_xL^M_{yz} = L^M_xL^M_yL^M_z - L^M_xL^M_yL^M_z = 0 .
$$

Hence every associator of $\mathbb{O}$ acts as the zero operator on $M$. Now the associators span the imaginary subspace $\operatorname{Im}\mathbb{O}$, a seven-dimensional space, and the two-sided ideal that they generate is all of $\mathbb{O}$: it contains $e_1e_1 = -e_0$, hence $e_0\mathbb{O} = \mathbb{O}$. Since $L^M$ is a homomorphism, the left action of every element of the generated ideal is zero, so $L^M_a = 0$ for every $a\in\mathbb{O}$. Applying this to $a = e_0$ and using unitality gives $m = e_0m = 0$ for every $m\in M$, so $M = 0$. $\square$

**Corollary.** There is no non-zero left $\mathbb{O}$-module in the unital sense, and no non-zero right $\mathbb{O}$-module, and the same argument applies to any unital bimodule over an algebra whose associators span a subspace generating the algebra as a two-sided ideal.

The obstruction is therefore not a technicality but a vanishing theorem, and it is the exact sense in which the octonions have no associative representation theory. The natural candidate $M = \mathbb{O}$ with $am = L_am$ and $ma = R_am$ is not a bimodule, because the third axiom would require $a(mb) = (am)b$, that is $L_aR_b = R_bL_a$, which fails for the same reason that the associator is non-zero.

### The Category of Representations

The vanishing theorem forces the following reading of the phrase "the representations of the octonions".

1. The multiplication operators $L_x$ and $R_x$ are linear endomorphisms of $\mathbb{O}$; they define an injective linear map $\mathbb{O}\to\operatorname{End}(\mathbb{O})$ that is **not** an algebra homomorphism, and the defect is exactly the associator.
2. The derivations and automorphisms of $\mathbb{O}$ are the structure-preserving linear maps; they form the Lie algebra $\mathfrak{g}_2$ and the group $G_2$, both of which are linear in the ordinary sense, so their representation theory is the usual one.
3. The unit sphere $S^7$ acts on $\mathbb{O}$ by multiplication and embeds in the orthogonal group; it is a Moufang loop of isometries, and its image generates the relative groups $\operatorname{Spin}(7)$ and $\operatorname{SO}(8)$.

Each of the three is taken up in turn. Nothing else survives: there are no modules, so there are no "irreducible octonion modules" of the usual kind, and the two sides of the theory must be built from operators and from the structure group.

## The Regular Representations

### Left and Right Multiplication

**Definition.** The **left regular representation** of $\mathbb{O}$ is the map

$$
\lambda : \mathbb{O}\longrightarrow\operatorname{End}_{\mathbb{R}}(\mathbb{O}), \qquad \lambda(x) = L_x, \quad L_x(y) = xy ,
$$

and the **right regular representation** is $\rho(x) = R_x$, $R_x(y) = yx$.

**Proposition.** The maps $\lambda$ and $\rho$ are injective and $\mathbb{R}$-linear, and $\lambda(e_0) = \rho(e_0) = \mathrm{id}$. Neither is an algebra homomorphism: for all $x,y$

$$
\lambda(x)\lambda(y) - \lambda(xy) : z\longmapsto -[x,y,z], \qquad
\rho(y)\rho(x) - \rho(xy) : z\longmapsto [x,y,z] ,
$$

that is, the defect of multiplicativity of the regular representation is the associator operator. Consequently $\lambda$ is multiplicative precisely on the set of pairs $(x,y)$ for which $[x,y,\cdot]$ vanishes identically, and in particular on every pair lying in a common associative subalgebra, by Artin's theorem.

*Proof.* Injectivity: $L_xe_0 = x$, so $L_x = 0$ only for $x = 0$; linearity is the bilinearity of the product; $\lambda(e_0) = \mathrm{id}$ is the identity axiom. For the defect, $(\lambda(x)\lambda(y))(z) - \lambda(xy)(z) = x(yz) - (xy)z = -[x,y,z]$. The analogue on the right is the same computation with the reversed product. The last statement is Artin's theorem. $\square$

The defect is thus an operator-valued trilinear form, and it is not something that can be removed by a change of basis: it vanishes on a pair $(x,y)$ only for those pairs whose generated subalgebra is associative, and by the previous section it cannot vanish identically on any non-zero module.

**Proposition.** For imaginary $x,y$ the operators satisfy the **Clifford relations**

$$
L_xL_y + L_yL_x = -2\langle x,y\rangle\,\mathrm{id}, \qquad
R_xR_y + R_yR_x = -2\langle x,y\rangle\,\mathrm{id} .
$$

Hence the assignment $e_k\mapsto L_{e_k}$ for $k = 1,\dots,7$ extends to a representation of the Clifford algebra $\mathrm{Cl}_{0,7}$ on the vector space $\mathbb{O}$, and $\mathbb{O}$ is a Clifford module of dimension eight over $\mathrm{Cl}_{0,7}$.

*Proof.* The identity is the linearisation of $L_xL_x = L_{x^2}$ for imaginary $x$: since $x^2 = -\lvert x\rvert^2e_0$, one has $L_x^2 = -\lvert x\rvert^2\mathrm{id}$, and polarising in $x$ gives the displayed relation. Equivalently, the relation is a finite computation on the basis using the Fano rule. The universality of $\mathrm{Cl}_{0,7}$ then gives the representation. $\square$

**Theorem.** The algebra generated inside $\operatorname{End}_{\mathbb{R}}(\mathbb{O})\cong M_8(\mathbb{R})$ by the seven operators $L_{e_1},\dots,L_{e_7}$ is the full matrix algebra $M_8(\mathbb{R})$, of dimension sixty-four.

*Proof.* The verification is finite: spanning the products of the seven generators up to length four by Gaussian elimination gives rank sixty-four, equal to the dimension of $M_8(\mathbb{R})$; since the generated algebra is a subalgebra of $M_8(\mathbb{R})$, it is all of it. $\square$

The theorem is the precise statement of the "enveloping" of the octonions in an associative algebra: although $\mathbb{O}$ has no modules, the operators it spans generate the whole matrix algebra $M_8(\mathbb{R})$, and every associative representation-theoretic statement about the octonions is a statement about this generated algebra and its subgroups.

### The Unit Sphere as a Loop of Operators

**Proposition.** For every unit octonion $u$ the operators $L_u$ and $R_u$ are orthogonal and have determinant one, so that

$$
L : S^7\longrightarrow SO(8), \qquad u\longmapsto L_u ,
$$

is an injective map of the unit sphere onto a seven-dimensional submanifold of $SO(8)$, with $L_ue_0 = u$; the image is **not** a subgroup, since $L_uL_v\neq L_{uv}$ in general, the defect being the operator of the previous proposition. The products of an even number of left multiplications by unit imaginary octonions generate the group $\operatorname{Spin}(7)$, which acts transitively on $S^7$ with isotropy a copy of $G_2$, so that

$$
S^7 = \operatorname{Spin}(7)/G_2 .
$$

*Proof.* Orthogonality is the invariance of the inner product, $\langle uy,uz\rangle = \lvert u\rvert^2\langle y,z\rangle$, at $\lvert u\rvert = 1$; the determinant is one because $u\mapsto L_u$ is continuous with $L_{e_0} = \mathrm{id}$ and $S^7$ is connected. Injectivity is $L_ue_0 = u$; the failure of multiplicativity is the defect $\lambda(u)\lambda(v) - \lambda(uv) = -[u,v,\cdot]$, which is non-zero for suitable $u,v$, for instance $u = e_1$, $v = e_4$, where the operator applied to $e_2$ gives $\pm2e_7$. The generation of $\operatorname{Spin}(7)$ by the even Clifford products, the transitivity of its action on $S^7$ and the identification of the isotropy with $G_2$ are standard, with the standard sources cited. $\square$

The proposition is the octonion replacement for the embedding of the quaternion unit sphere in $SO(4)$: the sphere acts on the algebra by isometries, and the failure of associativity appears as the difference between the loop $S^7$ and the group generated by its left translations.

## Representations of the Structure Objects

### The Derivation Algebra and Its Representations

**Definition.** A **derivation** of $\mathbb{O}$ is a linear map $d : \mathbb{O}\to\mathbb{O}$ satisfying the Leibniz rule $d(xy) = (dx)y + x(dy)$ for all $x,y$; the space of derivations is written $\operatorname{Der}(\mathbb{O}) = \mathfrak{g}_2$.

**Theorem.** $\operatorname{Der}(\mathbb{O})$ is a Lie subalgebra of $\mathfrak{so}(8)$ of dimension fourteen, acting trivially on $e_0$ and irreducibly on $\operatorname{Im}\mathbb{O}\cong\mathbb{R}^7$, and it is the exceptional simple Lie algebra $\mathfrak{g}_2$. The group $\operatorname{Aut}(\mathbb{O})$ is the compact simply connected simple Lie group $G_2$ of dimension fourteen; it acts transitively on the unit sphere $S^6\subset\operatorname{Im}\mathbb{O}$ with isotropy $SU(3)$, so that

$$
S^6 = G_2/SU(3) .
$$

*Pro.* The derivations of a composition algebra form the Lie algebra of its automorphism group, and for the octonions this algebra is the exceptional simple Lie algebra of type $G_2$, of dimension fourteen; the statements about $e_0$ and the irreducibility of the action on $\operatorname{Im}\mathbb{O}$ follow because a derivation annihilates the identity and preserves the imaginary subspace, which is irreducible under the automorphism group. The orbit statement is the standard transitivity of $G_2$ on the imaginary units with isotropy $SU(3)$. These are the standard facts, listed with their sources in the Further Reading; the construction of $\mathfrak{g}_2$ from the octonions and its place among the exceptional Lie algebras is not covered here. $\square$

**Theorem (the low-dimensional representations).** As a $\mathfrak{g}_2$-module, $\mathfrak{so}(7)$ decomposes as

$$
\mathfrak{so}(7) = \mathfrak{g}_2\oplus\mathbb{R}^7 , \qquad 21 = 14 + 7 ,
$$

and the tensor square of the seven-dimensional representation decomposes as

$$
\mathbb{R}^7\otimes\mathbb{R}^7 = \mathbb{R}\oplus\mathbb{R}^7\oplus\mathfrak{g}_2\oplus V_{27},
$$

that is $49 = 1 + 7 + 14 + 27$, with $\operatorname{Sym}^2\mathbb{R}^7 = \mathbb{R}\oplus V_{27}$ and $\Lambda^2\mathbb{R}^7 = \mathbb{R}^7\oplus\mathfrak{g}_2$, where $V_{27}$ is a simple module of dimension twenty-seven. The representations $\mathbb{R}$, $V_7$, $\mathfrak{g}_2$ and $V_{27}$ are the four nontrivial irreducible representations of $\mathfrak{g}_2$ of smallest dimension.

*Proof.* The decompositions are the standard branching rules for the exceptional algebra; the dimensions are those of the displayed modules, and the identities $21 = 14+7$, $49 = 1+7+14+27$, $28 = 1+27$ and $21 = 7+14$ are arithmetic. The interpretation of $\Lambda^2\mathbb{R}^7 = \mathbb{R}^7\oplus\mathfrak{g}_2$ is that the cross product and the derivation action together exhaust the alternating square; this is the octonion statement that the multiplication is determined by the derivation algebra up to the vector multiplication itself. $\square$

The module $V_{27}$ is the one that reappears as the traceless part of the exceptional Jordan algebra $\mathfrak{h}_3(\mathbb{O})$, whose automorphism group is $F_4$; the passage from the representations of $\mathfrak{g}_2$ to the exceptional groups is taken up.

### Triality

**Theorem (triality).** The group $\operatorname{Spin}(8)$ has three inequivalent irreducible real representations of dimension eight, the vector representation and the two half-spin representations, and it has an outer automorphism of order three that permutes them cyclically; the group of outer automorphisms of $\operatorname{Spin}(8)$ is the symmetric group $S_3$, corresponding to the symmetry of the Dynkin diagram of type $D_4$. The fixed subgroup of the order-three automorphism is a copy of $G_2$, and the octonion multiplication

$$
m : \mathbb{O}\times\mathbb{O}\longrightarrow\mathbb{O}
$$

is equivariant for the identification of the three eight-dimensional representations with $\mathbb{O}$ under the three projections of triality.

*Proof.* The three eight-dimensional representations of $\operatorname{Spin}(8)$ and the diagram symmetry are standard, as is the identification of the fixed points of the triality automorphism with $G_2$. The equivariance of the multiplication is the standard statement that the octonion product is the triality-invariant tensor of type $(1,1,1)$; the multiplication table exhibits the tensor explicitly, and the identity is verified by the Fano rule. $\square$

Triality is the reason why the octonions, alone among the number systems, are tied to a group whose representation theory is symmetric: the product $\mathbb{O}\times\mathbb{O}\to\mathbb{O}$ is a tensor with one leg in each of the three eight-dimensional representations, and the group $G_2$ is exactly the symmetry that preserves this tensor. The statement belongs to the same circle of ideas as the existence of the vector cross product on $\mathbb{R}^7$ and of the exceptional isomorphisms of the low-dimensional Dynkin diagrams, treated in *Root Systems and Classification*.

## Summary

The octonions have no associative module theory: a unital bimodule over $\mathbb{O}$ is necessarily zero, because the left action of a bimodule is an algebra homomorphism into an associative algebra, in which all associators vanish, while the associators of $\mathbb{O}$ span $\operatorname{Im}\mathbb{O}$ and generate $\mathbb{O}$ as a two-sided ideal.

What replaces modules are the multiplication operators and the representations of the structure objects. The left and right regular representations $x\mapsto L_x$, $x\mapsto R_x$ are injective linear maps, and their defect of multiplicativity is exactly the associator operator: $\lambda(x)\lambda(y) - \lambda(xy) = -[x,y,\cdot]$. For imaginary elements the operators satisfy the Clifford relations $L_xL_y + L_yL_x = -2\langle x,y\rangle\mathrm{id}$, so that $\mathbb{O}$ is a Clifford module over $\mathrm{Cl}_{0,7}$; the seven operators $L_{e_k}$ generate the full matrix algebra $M_8(\mathbb{R})$, and the unit sphere acts by orthogonal maps, $S^7\to SO(8)$, as a Moufang loop; the even products generate $\operatorname{Spin}(7)$ and $S^7 = \operatorname{Spin}(7)/G_2$.

The structure objects have ordinary representation theory. The derivation algebra $\mathfrak{g}_2 = \operatorname{Der}(\mathbb{O})$ has dimension fourteen and acts irreducibly on $\operatorname{Im}\mathbb{O}$; $\mathfrak{so}(7) = \mathfrak{g}_2\oplus\mathbb{R}^7$ and $\mathbb{R}^7\otimes\mathbb{R}^7 = \mathbb{R}\oplus\mathbb{R}^7\oplus\mathfrak{g}_2\oplus V_{27}$. The automorphism group $G_2$ acts transitively on the imaginary units with isotropy $SU(3)$, so $S^6 = G_2/SU(3)$. Finally, $\operatorname{Spin}(8)$ has three eight-dimensional representations permuted by an outer automorphism of order three whose fixed subgroup is $G_2$, and the octonion multiplication is the triality-equivariant tensor coupling the three.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$ | The octonion algebra, $\dim_{\mathbb{R}} = 8$ |
| $L_x$, $R_x$ | Left and right multiplication by $x$ |
| $\lambda$, $\rho$ | Left and right regular representations, $x\mapsto L_x$, $x\mapsto R_x$ |
| $[x,y,z] = (xy)z - x(yz)$ | Associator; $\lambda(x)\lambda(y) - \lambda(xy) = -[x,y,\cdot]$ |
| $\langle x,y\rangle = \operatorname{Sc}(x\bar y)$ | Inner product, $L_xL_y + L_yL_x = -2\langle x,y\rangle\mathrm{id}$ for imaginary $x,y$ |
| $\mathrm{Cl}_{0,7}$ | Clifford algebra acting on $\mathbb{O}$ through the $L_{e_k}$ |
| $M_8(\mathbb{R})$ | Generated by $L_{e_1},\dots,L_{e_7}$ |
| $S^7 = \operatorname{Spin}(7)/G_2$ | Unit sphere as a homogeneous space |
| $S^6 = G_2/SU(3)$ | Imaginary unit sphere |
| $\mathfrak{g}_2 = \operatorname{Der}(\mathbb{O})$, $G_2 = \operatorname{Aut}(\mathbb{O})$ | Exceptional Lie algebra and group, dimension $14$ |
| $V_7$, $V_{14} = \mathfrak{g}_2$, $V_{27}$ | Irreducible $\mathfrak{g}_2$-modules; $49 = 1+7+14+27$, $21 = 14+7$ |
| $\operatorname{Spin}(8)$, $8_v$, $8_s$, $8_c$ | Vector and half-spin representations, permuted by triality |





## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for bimodules over non-associative algebras and the obstruction to the associative theory.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the derivation algebra, $G_2$ and the low-dimensional modules.
- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* **39** (2002), 145–205, for triality, the Clifford action on $\mathbb{O}$ and the classification of the octonion representations.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the embeddings $S^7\subset SO(8)$, $\operatorname{Spin}(7)$ and the cross product.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the branching rules of $\mathfrak{g}_2$ and the dimensions of the small modules.
- H. S. M. Coxeter, "Integral Cayley numbers", *Duke Mathematical Journal* **13** (1946), 561–578, for the arithmetic of the multiplication operators and the integral structure.
