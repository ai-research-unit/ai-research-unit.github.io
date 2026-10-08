# __The Topological Witt Group and the Brauer–Wall Group__

## Introduction

The isometry classes of non-degenerate quadratic forms form a ring under the orthogonal sum and the tensor product, the Witt ring, and the classes of Clifford algebras form an eightfold periodic group, the Brauer–Wall group. Both constructions are algebraic, and both acquire a topology when the forms and the algebras are read over a topological field: the space of forms is a topological space on which the general linear group acts, the invariants of the classification are **locally constant** functions on it, and the periodicity of the classification is the periodicity of a topological invariant of a group. This article is the topological reading of that classification.

The first content is the topology of the space of forms. The non-degenerate forms of a fixed dimension form an open subset of the space of all symmetric forms, the general linear group acts on it, and the orbits are the signature classes; the signature is a continuous map into a discrete set, so it is locally constant and each orbit is open and closed. The space is therefore the disjoint union of finitely many connected pieces, one per signature, and each piece is a homogeneous space of the general linear group. Every invariant of the Witt classification — the dimension, the discriminant, the signature — is either a continuous homomorphism into a discrete group or a locally constant function on the pieces, and that is the sense in which the topological Witt group is the group of locally constant invariants of the space of forms.

The second content is the periodicity. The Brauer–Wall group of the real numbers is the cyclic group of order eight, and the eight classes of real Clifford algebras are represented by the algebras $\mathrm{Cl}_{p,q}$ with $p-q$ read modulo eight; the periodicity of the classification is the periodicity of the homotopy groups of the orthogonal group, $\pi_{n}(\mathrm{O})=\pi_{n+8}(\mathrm{O})$, which is **Bott periodicity** and belongs to Algebraic Topology and to *Topological K-Theory*. This article records the topological reading, states the table, and defers the proofs; it does not reprove the classification of *The Brauer–Wall Group and the Eightfold Way* nor the periodicity of *Bott Periodicity and the Classification*.

The article treats the space of forms and the orbit decomposition, the locally constant invariants and the two rings, the Brauer–Wall group and the periodicity, the relation to topological K-theory, and the examples of the real forms. The algebraic theory of the Witt and Grothendieck–Witt rings is *The Witt Group and the Grothendieck–Witt Ring*, the Clifford classification is *The Brauer–Wall Group and the Eightfold Way* and *Bott Periodicity and the Classification*, the signature is *Quadratic Forms over Algebras and Norms* and *Witt's Theorems*, and the K-theory is *Topological K-Theory*. Throughout, $F$ is a topological field of characteristic not $2$ or $0$ as the antisymmetrisation requires, and the space of forms is that of *The Continuous Quadratic Form and the Polar Form*.

## The Space of Forms and its Orbits

**Definition.** Let $\Omega_{n}$ be the set of non-degenerate symmetric bilinear forms on $F^{n}$, a subset of the space $\operatorname{Sym}_{n}$ of all symmetric forms, and let $GL_{n}(F)$ act by $B\mapsto B\circ(T\times T)$.

**Proposition (the space of forms is open and the action is continuous).** The set $\Omega_{n}$ is open in $\operatorname{Sym}_{n}$, the action of $GL_{n}(F)$ on $\Omega_{n}$ is continuous, and the orbit of a form is its isometry class.

*Proof.* A symmetric form is non-degenerate exactly when the determinant of its matrix is nonzero, and the determinant is a continuous function of the coefficients; hence $\Omega_{n}$ is the complement of a closed set. The action is a polynomial map in the entries of $T$ and of the matrix of $B$, hence continuous, and two forms lie in the same orbit exactly when one is carried to the other by a change of basis, which is an isometry. $\square$

**Theorem (the orbits are the signatures and each is connected).** Let $F=\mathbb{R}$. Then the orbits of $GL_{n}(\mathbb{R})$ on $\Omega_{n}$ are the classes of a fixed signature $(p,q)$ with $p+q=n$, there are $n+1$ of them, each orbit is **open and closed** in $\Omega_{n}$, each is **connected**, and each is homeomorphic to the homogeneous space $GL_{n}(\mathbb{R})/\mathrm{O}(p,q)$ of *The Topological Orthogonal Group and the Spin Group*.

*Proof.* Sylvester's law of inertia says that a real form is determined up to isometry by the numbers $p$ and $q$ of positive and negative squares in a diagonal form, so the orbits are exactly the signature classes and there are $n+1$. The signature is a function into the finite set $\{0,\dots,n\}$, and the ordered eigenvalues of a symmetric matrix are continuous functions of its entries, by the max–min characterisation $\lambda_{k}(G)=\max_{\dim S=k}\min_{0\neq v\in S}q_{G}(v)/\lVert v\rVert^{2}$; on the open set where the determinant does not vanish the count of positive eigenvalues is therefore locally constant, being the largest $k$ with $\lambda_{k}>0$. A locally constant map into a discrete set makes each of its level sets open, and the level sets are the orbits; they are closed as well, the complement being the union of the other level sets. Connectedness is the connectedness of $GL_{n}(\mathbb{R})$ and the continuity of the orbit map from the connected group; Connectedness is the connectedness of $GL_{n}(\mathbb{R})$ and the continuity of the orbit map from the connected group; the stabiliser of a form of signature $(p,q)$ is the orthogonal group $\mathrm{O}(p,q)$, and the orbit is thus the quotient, with the quotient topology. $\square$

**Remark (what the topology of the space of forms says).** The theorem says that the moduli of real forms of dimension $n$ is a finite discrete set with no topology beyond the point count, each point being a connected homogeneous space. The invariants of the classification are therefore exactly the locally constant functions on $\Omega_{n}$, and this is the sense in which the topological layer adds nothing to the classification over the real numbers and everything to its interpretation: it identifies the invariants with the locally constant functions, and it identifies the path components of the space of forms with the signatures.

## The Locally Constant Invariants and the Two Rings

**Definition.** The **dimension**, the **discriminant** and the **signature** are

$$
\dim(B)=n,\qquad \Delta(B)=\det G_{B}\in F^{\times}/(F^{\times})^{2},\qquad \operatorname{sign}(B)=p-q ,
$$

as in *The Witt Group and the Grothendieck–Witt Ring*, §§*The Grothendieck–Witt Ring* and *Orderings and the Signature*.

**Proposition (each invariant is locally constant or a discrete homomorphism).** The dimension is a continuous homomorphism $\Omega_{n}\to\mathbb{Z}$; the discriminant is a continuous map $\Omega_{n}\to F^{\times}/(F^{\times})^{2}$ into the square-class group, which over $\mathbb{R}$ is the two-element discrete group $\{\pm1\}$ and over $\mathbb{C}$ is trivial; the signature is locally constant. Consequently each invariant is constant on the connected components of $\Omega_{n}$.

*Proof.* The dimension is constant on $\Omega_{n}$ by definition. The determinant of the matrix of a form is continuous, and the quotient map to the square classes is continuous for the quotient topology, which over $\mathbb{R}$ and over $\mathbb{C}$ is discrete on the image, so the discriminant is locally constant. The signature is a function of the orbit, which is locally constant by the theorem above. $\square$

**Theorem (the Witt and Grothendieck–Witt groups).** The Grothendieck group of the monoid of isometry classes of non-degenerate forms under orthogonal sum is the **Grothendieck–Witt group** $GW(F)$; the subgroup generated by the class $[H]$ of the hyperbolic plane is an ideal, and the quotient $W(F)=GW(F)/\mathbb{Z}[H]$ is the **Witt ring**. Over the real numbers

$$
GW(\mathbb{R})\;\cong\;\mathbb{Z}\langle 1\rangle\oplus\mathbb{Z}\langle-1\rangle\;\cong\;\mathbb{Z}^{2}, \qquad W(\mathbb{R})\;\cong\;\mathbb{Z},
$$

the dimension and the signature being the two coordinates of $GW(\mathbb{R})$, and the signature being the isomorphism $W(\mathbb{R})\to\mathbb{Z}$.

*Proof.* The algebraic construction of the two groups as the Grothendieck group of the monoid of isometry classes and its quotient by the hyperbolic ideal is that of *The Witt Group and the Grothendieck–Witt Ring*, §§*The Grothendieck–Witt Ring* and *The Witt Ring*. Over $\mathbb{R}$ the monoid of isometry classes is the set of pairs $(a,b)$ of multiplicities of the positive and the negative squares with $a,b\ge0$, isomorphic to $\mathbb{N}^{2}$ under addition, because Sylvester's law says that no two distinct pairs are isometric; the Grothendieck group of $\mathbb{N}^{2}$ is $\mathbb{Z}^{2}$, generated by $\langle1\rangle$ and $\langle-1\rangle$. The hyperbolic plane is $\langle1,-1\rangle$, of class $\langle1\rangle+\langle-1\rangle$, and quotienting by that class identifies the two generators up to sign, leaving $\mathbb{Z}$ generated by the class of $\langle1\rangle$, which is the signature by its value on the generators. $\square$

**Remark (the topological reading).** The two groups are discrete, and their elements are the locally constant invariants of the space of forms assembled into a group: this is why no topology is lost by passing to them. The topological content of the classification over a general topological field is the statement that each of the maps above is continuous for the discrete topologies on the targets, and therefore that the classification is rigid — no form can cross a signature class along a continuous path.

## The Brauer–Wall Group and the Periodicity

**Definition.** The **Brauer–Wall group** $\mathrm{BW}(F)$ is the group of classes of finite-dimensional $\mathbb{Z}/2$-graded central simple algebras over $F$ under the graded tensor product, modulo the graded matrix algebras, as in *The Brauer–Wall Group and the Eightfold Way*; the Clifford algebra $\mathrm{Cl}(V,q)$ of a non-degenerate form represents an element of it.

**Theorem (the eightfold periodicity).** Over the real numbers the Brauer–Wall group is cyclic of order eight,

$$
\mathrm{BW}(\mathbb{R})\cong\mathbb{Z}/8 ,
$$

and the class of $\mathrm{Cl}_{p,q}$ depends only on $p-q$ modulo eight. The periodicity is the periodicity of the classification of the real Clifford algebras of *Bott Periodicity and the Classification*.

*Proof.* The algebraic classification, that the graded central simple real algebras are classified by an element of $\mathbb{Z}/8$ read off from the pair $(p,q)$ modulo eight, is that of *The Brauer–Wall Group and the Eightfold Way*; the statement is quoted, and its proof by the graded tensor product and the periodicity of the eight classes is not reproduced here. $\square$

**Theorem (the periodicity is topological).** The eightfold periodicity of the real Clifford algebras is the periodicity of the homotopy groups of the orthogonal group,

$$
\pi_{n}(\mathrm{O}) = \pi_{n+8}(\mathrm{O}) \qquad\text{with}\qquad (\pi_{0},\dots,\pi_{7}) = (\mathbb{Z}/2,\ \mathbb{Z}/2,\ 0,\ \mathbb{Z},\ 0,\ 0,\ 0,\ \mathbb{Z}),
$$

and the identification of the two statements is **Bott periodicity**, a theorem of Algebraic Topology. Consequently the eight classes of the Brauer–Wall group are in bijection with the eight values of the homotopy of the orthogonal group, and the "eightfold way" of the algebra is the periodicity of the homotopy invariant.

*Proof.* The statement of Bott periodicity, that the homotopy groups of the stable orthogonal group are periodic of period eight with the table displayed, is the theorem of *Bott Periodicity and the Classification*, where the table is derived and the classification of the real Clifford algebras is read from it; the present article records the identification and does not reprove it. The bijection of the eight classes with the eight values is the standard correspondence between the graded central simple algebras and the elements of the coefficient group of the corresponding K-theory, which is developed in *Topological K-Theory*. $\square$

**Remark (what is proved here and what is quoted).** This article proves the topology of the space of forms, the local constancy of the invariants, the orbit decomposition and the computation of the two groups over $\mathbb{R}$, all of which are elementary and belong to the layer. It quotes the periodicity, the eightfold classification and the identification with the homotopy groups, which belong to Algebraic Topology, and it points to the articles that prove them. The boundary is therefore between the locally constant invariants of a space of forms, which is the content of this category, and the homotopy of a classifying space, which is not.

## The Relation to Topological K-Theory

**Remark (the three groups).** The Witt group, the Grothendieck–Witt group and the Brauer–Wall group are the degree-zero parts of three cohomology theories of the point in the real case: the Witt group corresponds to the group $KO_{0}$ of the real K-theory of a point, the Brauer–Wall group to the class in $KO^{-1}$ or to the group of the invertible elements of the Clifford algebra, and the eightfold periodic table of the Clifford algebras to the eight homotopy groups $\pi_{n}(\mathrm{O})$. The identifications are the content of *Topological K-Theory* and of *Bott Periodicity and the Classification*; the present article states the correspondence and does not use it beyond the table of the homotopy groups, and the reader who needs the K-theoretic machinery is referred there.

**Remark (the general topological field).** Over a general topological field the three objects are still defined, and the topological content is only the continuity of the invariants; the computation of the groups requires more than the topology and belongs to the algebra, to *The Witt Group and the Grothendieck–Witt Ring* and to *The Brauer–Wall Group and the Eightfold Way*. This article therefore takes the topological field to be $\mathbb{R}$ or $\mathbb{C}$ in every computation and treats the general case only through the continuity of the maps.

## Examples

### The Real Forms of Low Dimension

**Example ($\mathbb{R}^{1}$ and $\mathbb{R}^{2}$).** For $n=1$ the space $\Omega_{1}$ is the two-component set of the forms $x^{2}$ and $-x^{2}$, the orbit decomposition has two pieces, and the Witt group of the line is generated by the class of $\langle1\rangle$ with the relation $\langle1\rangle+\langle-1\rangle=0$; the Grothendieck–Witt group keeps the two classes apart. For $n=2$ the space $\Omega_{2}$ has three components, of signatures $(2,0)$, $(1,1)$ and $(0,2)$, and the middle one is the class of the hyperbolic plane, which vanishes in the Witt group and not in the Grothendieck–Witt group. The examples exhibit in the smallest dimension the difference between the two groups and the meaning of the locally constant signature.

**Example ($\mathbb{C}$).** Over the complex numbers every non-degenerate form is isometric to the standard one, so $\Omega_{n}$ is a single orbit, the discriminant is trivial, the signature is not defined and $W(\mathbb{C})\cong\mathbb{Z}/2$, $GW(\mathbb{C})\cong\mathbb{Z}$, as in *The Witt Group and the Grothendieck–Witt Ring*, §*Examples*. The example is the extreme case of the orbit decomposition, with a single connected piece and no locally constant invariant beyond the dimension.

### The Brauer–Wall Class of the Lorentzian Form

**Example (signature $(1,3)$).** The Lorentzian form on $\mathbb{R}^{4}$ and its Clifford algebra $\mathrm{Cl}_{1,3}$ represent an element of $\mathrm{BW}(\mathbb{R})\cong\mathbb{Z}/8$. The algebra is $\mathrm{Cl}_{4,0}$ by the identity $\mathrm{Cl}_{p+1,q}\cong\mathrm{Cl}_{q+1,p}$ of *The Low-Dimensional Classification*, hence $M_{2}(\mathbb{H})$, the algebra listed at $\mathrm{Cl}_{0,4}$ in the table of *The Brauer–Wall Group and the Eightfold Way*; the difference $p-q=-2$ is congruent to $6$ modulo eight, so the class is the sixth position of the eightfold table. The example shows that the invariant is the difference $p-q$ modulo eight and not the dimension, and it connects the table of the layer to the real division algebras.

**Example (the split and the definite cases).** The definite form of dimension $n$ has $p-q=n$, and the periodicity matches the periodicity of the Clifford algebra of the Euclidean space, whose class in $\mathrm{BW}(\mathbb{R})$ runs through all eight values as $n$ increases; the split form of dimension $2m$ has $p-q=0$ and the hyperbolic class, the neutral element. The two families are the extremes of the table, and they show that the periodicity is driven by the signature difference and not by the dimension.

## Summary

The set $\Omega_{n}$ of non-degenerate symmetric forms on $F^{n}$ is an **open** subset of the space of symmetric forms, the general linear group acts on it continuously, and over $\mathbb{R}$ the orbits are the **signatures**: there are $n+1$ of them, each **open and closed** and each **connected**, homeomorphic to the homogeneous space $GL_{n}(\mathbb{R})/\mathrm{O}(p,q)$. The classification invariants — **dimension**, **discriminant**, **signature** — are continuous homomorphisms into discrete groups or locally constant functions, hence constant on the components; this is the sense in which the topological layer adds nothing to the real classification but identifies the invariants with the locally constant functions.

The **Grothendieck–Witt group** is the Grothendieck group of the monoid of isometry classes under orthogonal sum, the **Witt ring** is its quotient by the hyperbolic ideal, and over $\mathbb{R}$ one has $GW(\mathbb{R})\cong\mathbb{Z}\langle1\rangle\oplus\mathbb{Z}\langle-1\rangle\cong\mathbb{Z}^{2}$ and $W(\mathbb{R})\cong\mathbb{Z}$, the dimension and the signature being the coordinates. The **Brauer–Wall group** of $\mathbb{R}$ is cyclic of order eight, the class of $\mathrm{Cl}_{p,q}$ depending only on $p-q$ modulo eight, and its periodicity is the **Bott periodicity** of the homotopy groups of the orthogonal group, $\pi_{n}(\mathrm{O})=\pi_{n+8}(\mathrm{O})$ with the table $(\mathbb{Z}/2,\mathbb{Z}/2,0,\mathbb{Z},0,0,0,\mathbb{Z})$ — a theorem of Algebraic Topology, quoted here and proved in *Bott Periodicity and the Classification*.

What the article owns is the topology of the space of forms and the local constancy of the invariants; what it quotes is the classification, the periodicity and the K-theoretic identification, which belong to *The Witt Group and the Grothendieck–Witt Ring*, *The Brauer–Wall Group and the Eightfold Way*, *Bott Periodicity and the Classification* and *Topological K-Theory*. The examples exhibit the orbit decomposition over $\mathbb{R}$ and over $\mathbb{C}$, the hyperbolic class vanishing in the Witt group and not in the Grothendieck–Witt group, and the Brauer–Wall class of the Lorentzian form as the sixth position of the table.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Omega_{n}\subseteq\operatorname{Sym}_{n}$ | the open set of non-degenerate forms on $F^{n}$ |
| $(p,q)$, $\operatorname{sign}=p-q$ | the signature, the orbit label, locally constant |
| $\Delta$, $\dim$ | the discriminant and the dimension, discrete homomorphisms |
| $GL_{n}(\mathbb{R})/\mathrm{O}(p,q)$ | the homogeneous space of one signature class |
| $GW(F)$, $W(F)=GW/\mathbb{Z}[H]$ | the Grothendieck–Witt group and the Witt ring |
| $GW(\mathbb{R})\cong\mathbb{Z}^{2}$, $W(\mathbb{R})\cong\mathbb{Z}$ | the real computation |
| $\mathrm{BW}(\mathbb{R})\cong\mathbb{Z}/8$ | the Brauer–Wall group, the eightfold way |
| $\pi_{n}(\mathrm{O})=\pi_{n+8}(\mathrm{O})$ | Bott periodicity, the topological form of the periodicity |

## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the Witt and Grothendieck–Witt groups and the signature.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the orthogonal group, the space of forms and the orbit decomposition.
- Max Karoubi, *K-Theory: An Introduction* (Springer, 1978), for the Brauer–Wall group, the Clifford algebras and the relation to topological K-theory.
- Dale Husemoller, *Fibre Bundles*, 3rd edition (Springer, 1994), for Bott periodicity and the homotopy groups of the orthogonal group.
- Raoul Bott, *Lectures on K(X)* (W. A. Benjamin, 1969), for the periodicity theorem in its original form.
- Nicolas Bourbaki, *Topological Groups* (Springer, 1998), for the orbit map of a continuous action and the quotient topology of a homogeneous space.
